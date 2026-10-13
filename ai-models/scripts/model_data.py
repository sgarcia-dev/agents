#!/usr/bin/env python3
"""Bounded Artificial Analysis Free catalogue client; standard library only."""
import argparse
import json
import os
from pathlib import Path
import tempfile
from datetime import datetime, timezone
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.error import HTTPError, URLError

ENDPOINT = 'https://artificialanalysis.ai/api/v2/language/models/free'
HEADERS = ['X-AA-Tier', 'X-RateLimit-Limit', 'X-RateLimit-Remaining',
           'X-RateLimit-Reset', 'Retry-After']


class DataError(Exception):
    pass


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def now():
    return datetime.now(timezone.utc).isoformat()


def atomic_json(path, data, secret=None):
    encoded = json.dumps(data, ensure_ascii=False, indent=2).encode('utf-8')
    if secret and secret.encode('utf-8') in encoded:
        raise DataError('Refused output containing the authentication secret')
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix='.' + path.name + '.', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as f:
            f.write(encoded)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def cache_valid(catalog, ttl_hours):
    try:
        stamp = datetime.fromisoformat(catalog['fetched_at'].replace('Z', '+00:00'))
        age = (datetime.now(timezone.utc) - stamp).total_seconds()
        rows = catalog['data']
        ids = [r['id'] for r in rows]
        return (catalog.get('complete') is True and 0 <= age < ttl_hours * 3600
                and isinstance(rows, list) and len(ids) == len(set(ids))
                and 'intelligence_index_version' in catalog
                and all(all(isinstance(r.get(k), str) and r[k]
                            for k in ['id', 'slug', 'name']) for r in rows))
    except (ValueError, TypeError, KeyError, AttributeError):
        return False


def resolve(rows, query):
    for field, value in [('id', query), ('slug', query), ('name', query.casefold())]:
        matches = [r for r in rows if
                   (str(r.get(field, '')).casefold() if field == 'name'
                    else r.get(field)) == value]
        if len(matches) == 1:
            return {'requested': query, 'status': 'matched', 'matched_by': field,
                    'model': matches[0]}
        if len(matches) > 1:
            return {'requested': query, 'status': 'ambiguous', 'matched_by': field,
                    'candidates': [{k: r.get(k) for k in ['id', 'slug', 'name']}
                                   for r in matches]}
    return {'requested': query, 'status': 'missing'}


def compact(row, catalog):
    evaluations = row.get('evaluations') or {}
    pricing = row.get('pricing') or {}
    performance = row.get('performance') or {}
    cost = row.get('artificial_analysis_intelligence_index_cost') or {}
    creator = row.get('model_creator') or {}
    return {
        'id': row['id'], 'name': row['name'], 'slug': row['slug'],
        'creator': creator.get('name'), 'release_date': row.get('release_date'),
        'index_version': catalog['intelligence_index_version'],
        'scores': {k: evaluations.get('artificial_analysis_' + k + '_index')
                   for k in ['intelligence', 'coding', 'agentic']},
        'pricing_usd_per_1m_tokens': {
            k: pricing.get('price_1m_' + k + '_tokens')
            for k in ['input', 'output', 'cache_hit', 'cache_write']},
        'performance': {
            k: performance.get('median_' + k) for k in [
                'output_tokens_per_second', 'time_to_first_token_seconds',
                'time_to_first_answer_token_seconds', 'end_to_end_response_time_seconds']},
        'aa_intelligence_eval_cost_usd': cost.get('total_cost'),
        'aa_intelligence_cost_per_task_usd': (cost.get('cost_per_task') or {}).get('total_cost'),
        'fetched_at': catalog['fetched_at'], 'source': 'Artificial Analysis',
        'source_url': ENDPOINT,
    }


def fetch_catalog(key, max_pages, metadata, opener=None):
    opener = opener or build_opener(NoRedirect())
    all_rows, seen, pages = [], set(), []
    version = tier = total_pages = page_size = None
    for page in range(1, max_pages + 1):
        request = Request(ENDPOINT + '?page=' + str(page),
                          headers={'x-api-key': key, 'Accept': 'application/json'})
        entry = {'page': page, 'url': request.full_url}
        metadata.append(entry)
        try:
            with opener.open(request, timeout=30) as response:
                entry['status'] = response.status
                entry['headers'] = {h: response.headers.get(h) for h in HEADERS
                                    if response.headers.get(h) is not None}
                if response.status != 200:
                    raise DataError('Unexpected API success status')
                body = response.read(20_000_001)
                if len(body) > 20_000_000:
                    raise DataError('Response exceeded the 20 MB page limit')
        except HTTPError as e:
            entry['status'] = e.code
            entry['headers'] = {h: e.headers.get(h) for h in HEADERS
                                if e.headers.get(h) is not None}
            e.close()
            raise DataError('API HTTP ' + str(e.code) + '; stopped without retry') from None
        except (URLError, TimeoutError, OSError):
            raise DataError('API transport failure; stopped without retry') from None
        if key.encode() in body:
            raise DataError('API response unexpectedly contained the authentication secret')
        try:
            obj = json.loads(body)
            pagination = obj['pagination']
            rows = obj['data']
            current_version = obj['intelligence_index_version']
            current_tier = obj['tier']
            more = pagination['has_more']
            count = pagination['total_pages']
            size = pagination['page_size']
            if (type(more) is not bool or type(count) is not int or count < 1
                    or type(size) is not int or size < 1
                    or type(pagination['page']) is not int or pagination['page'] != page
                    or not isinstance(rows, list) or len(rows) > size or page > count
                    or more != (page < count) or (more and not rows)
                    or type(current_version) not in [int, float]
                    or current_tier not in ['free', 'pro', 'commercial']):
                raise DataError('Invalid pagination, tier or version metadata')
            if page == 1:
                version, tier, total_pages, page_size = current_version, current_tier, count, size
            elif (current_version, current_tier, count, size) != (version, tier, total_pages, page_size):
                raise DataError('Catalogue changed version, tier or pagination during refresh')
            for row in rows:
                if not isinstance(row, dict) or not all(isinstance(row.get(k), str) and row[k]
                                                       for k in ['id', 'name', 'slug']):
                    raise DataError('Model record lacks a valid ID, name or slug')
                if row['id'] in seen:
                    raise DataError('Duplicate model ID across catalogue pages')
                for field in ['evaluations', 'pricing', 'performance', 'model_creator',
                              'artificial_analysis_intelligence_index_cost']:
                    if field in row and row[field] is not None and not isinstance(row[field], dict):
                        raise DataError('Invalid model field shape: ' + field)
                cost = row.get('artificial_analysis_intelligence_index_cost') or {}
                if cost.get('cost_per_task') is not None and not isinstance(cost['cost_per_task'], dict):
                    raise DataError('Invalid per-task cost shape')
                seen.add(row['id'])
            pages.append({'pagination': pagination, 'models': len(rows)})
            all_rows.extend(rows)
        except (KeyError, TypeError, ValueError, UnicodeDecodeError):
            raise DataError('API returned invalid JSON or an incomplete schema') from None
        if not more:
            return {'fetched_at': now(), 'complete': True, 'tier': tier,
                    'intelligence_index_version': version, 'source': 'Artificial Analysis',
                    'source_url': ENDPOINT, 'pages': pages, 'data': all_rows}
    raise DataError('Page-request cap reached before the catalogue was complete; cache unchanged')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', action='append', default=[])
    parser.add_argument('--cache', type=Path, default=Path(__file__).resolve().parents[1]/'cache/language-models.json')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--ttl-hours', type=float, default=6)
    parser.add_argument('--max-pages', type=int, default=10)
    parser.add_argument('--refresh', action='store_true')
    args = parser.parse_args(argv)
    if args.ttl_hours <= 0 or not 1 <= args.max_pages <= 100:
        parser.error('TTL must be positive and max-pages must be between 1 and 100')
    key = os.environ.get('ARTIFICIAL_ANALYSIS_API_KEY')
    run = {'started_at': now(), 'source': 'Artificial Analysis', 'endpoint': ENDPOINT,
           'cache_used': False, 'requests': [], 'requested_models': args.model,
           'max_page_requests': args.max_pages,
           'coverage': 'Free endpoint only; not full website or agent/harness data'}
    try:
        catalog = None
        if not args.refresh and args.cache.is_file():
            try:
                cached = json.loads(args.cache.read_text())
                if cache_valid(cached, args.ttl_hours):
                    catalog = cached
                    run['cache_used'] = True
            except (OSError, ValueError):
                pass
        if catalog is not None and any(resolve(catalog['data'], q)['status'] == 'missing' for q in args.model):
            run['refresh_reason'] = 'Requested model absent from valid cache'
            catalog = None
            run['cache_used'] = False
        if catalog is None:
            if not key or key != key.strip() or '\n' in key or '\r' in key:
                raise DataError('API key missing or malformed; use the hidden-input launcher')
            catalog = fetch_catalog(key, args.max_pages, run['requests'])
            atomic_json(args.cache, catalog, key)
        matches = [resolve(catalog['data'], q) for q in args.model]
        favorites = []
        for match in matches:
            if match['status'] == 'matched':
                model = match.pop('model')
                match['metrics'] = compact(model, catalog)
            favorites.append(match)
        atomic_json(args.output/'catalog.json', catalog, key)
        atomic_json(args.output/'favorites.json', favorites, key)
        run.update({'status': 'completed' if all(x['status'] == 'matched' for x in favorites)
                    else 'completed_with_unresolved_models', 'model_count': len(catalog['data']),
                    'catalog_fetched_at': catalog['fetched_at'], 'tier': catalog['tier'],
                    'intelligence_index_version': catalog['intelligence_index_version'],
                    'matches': [{k: x[k] for k in ['requested', 'status']} for x in favorites]})
        code = 0 if run['status'] == 'completed' else 2
    except (DataError, OSError) as e:
        # Do not echo arbitrary request/response objects or authentication details.
        run.update({'status': 'failed', 'error': str(e) if isinstance(e, DataError)
                    else 'Local file operation failed'})
        code = 1
    run['completed_at'] = now()
    run['request_count'] = len(run['requests'])
    atomic_json(args.output/'run.json', run, key)
    print(json.dumps({k: run.get(k) for k in ['status', 'model_count', 'request_count', 'cache_used', 'error']
                      if k in run}))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
