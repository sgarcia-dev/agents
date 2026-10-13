"""Deterministic API-client tests; no live key or network."""
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from datetime import datetime, timezone

spec = importlib.util.spec_from_file_location('model_data', Path(__file__).with_name('model_data.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def row(id='one', slug='first', name='First'):
    return {'id': id, 'slug': slug, 'name': name, 'evaluations': {
        'artificial_analysis_intelligence_index': None},
        'artificial_analysis_intelligence_index_cost': {'total_cost': 8, 'cost_per_task': {'total_cost': .5}}}


def page(n, total=2, records=None, version=4.3):
    return {'tier': 'free', 'intelligence_index_version': version,
            'pagination': {'page': n, 'page_size': 200, 'total_pages': total, 'has_more': n < total},
            'data': records if records is not None else [row(str(n), 'model-'+str(n))]}


class Response(io.BytesIO):
    status = 200
    headers = {'X-AA-Tier': 'free', 'X-RateLimit-Remaining': '99'}


class Opener:
    def __init__(self, objects):
        self.objects = iter(objects)
        self.requests = []

    def open(self, request, timeout):
        self.requests.append(request)
        value = next(self.objects)
        if isinstance(value, Exception):
            raise value
        return Response(json.dumps(value).encode())


class Tests(unittest.TestCase):
    def test_registry_default_efforts_and_distinct_families(self):
        root = Path(__file__).resolve().parents[1]
        registry = json.loads((root/'favorites.json').read_text())
        models = registry['models']
        configurations = [c for model in models.values() for c in model['configurations']]
        self.assertEqual(len(configurations), 43)
        self.assertEqual(len({c['id'] for c in configurations}), 43)
        self.assertEqual(len({c['slug'] for c in configurations}), 43)
        self.assertNotEqual(models['sol']['family_slug'], models['sol-6']['family_slug'])
        self.assertNotEqual(models['luna']['family_slug'], models['luna-5-6']['family_slug'])
        defaults = [model for model in models.values() if model.get('effort_policy') == 'default']
        self.assertEqual(len(defaults), 9)
        for model in defaults:
            self.assertEqual(len(model['configurations']), 1)
            self.assertEqual(model['default_effort'], model['configurations'][0]['effort'])
        self.assertIsNone(models['mimo-flash']['default_effort'])
        self.assertEqual(models['kimi']['default_effort'], 'max')

    def test_accepted_benchmark_units_and_sources(self):
        root = Path(__file__).resolve().parents[1]
        metrics = {item['slug']: item for item in json.loads((root/'benchmarks.json').read_text())['metrics']}
        self.assertEqual(metrics['aa-lcr-v1-1']['website_key'], 'lcr')
        self.assertEqual(metrics['aa-lcr-v1-1']['unit'], 'fraction')
        self.assertEqual(metrics['aa-briefcase']['evaluation_slug'], 'aa-briefcase')
        self.assertEqual(metrics['aa-briefcase']['unit'], 'Elo')
        for key in ['aa-lcr-v1-1', 'aa-briefcase']:
            self.assertEqual(metrics[key]['status'], 'accepted')
            self.assertTrue(metrics[key]['higher_is_better'])
        self.assertNotIn('ifbench', metrics)

    def test_complete_pagination(self):
        log = []
        result = m.fetch_catalog('SECRET_FOR_TEST', 10, log, Opener([page(1), page(2)]))
        self.assertTrue(result['complete'])
        self.assertEqual(len(result['data']), 2)
        self.assertEqual(len(log), 2)
        self.assertNotIn('SECRET_FOR_TEST', json.dumps(result)+json.dumps(log))

    def test_missing_has_more_rejected(self):
        p = page(1)
        del p['pagination']['has_more']
        with self.assertRaises(m.DataError):
            m.fetch_catalog('SECRET_FOR_TEST', 10, [], Opener([p]))

    def test_duplicate_id_rejected(self):
        with self.assertRaises(m.DataError):
            m.fetch_catalog('SECRET_FOR_TEST', 10, [], Opener([page(1, records=[row()]), page(2, records=[row()])]))

    def test_page_cap(self):
        log = []
        with self.assertRaises(m.DataError):
            m.fetch_catalog('SECRET_FOR_TEST', 1, log, Opener([page(1)]))
        self.assertEqual(len(log), 1)

    def test_version_change_rejected(self):
        with self.assertRaises(m.DataError):
            m.fetch_catalog('SECRET_FOR_TEST', 10, [], Opener([page(1), page(2, version=5)]))

    def test_null_and_per_task_cost(self):
        r = m.compact(row(), {'fetched_at': 'test', 'intelligence_index_version': 4.3})
        self.assertIsNone(r['scores']['intelligence'])
        self.assertIsNone(r['pricing_usd_per_1m_tokens']['input'])
        self.assertEqual(r['aa_intelligence_eval_cost_usd'], 8)
        self.assertEqual(r['aa_intelligence_cost_per_task_usd'], .5)

    def test_exact_matches_and_ambiguity(self):
        self.assertEqual(m.resolve([row()], 'one')['matched_by'], 'id')
        self.assertEqual(m.resolve([row()], 'FIRST')['matched_by'], 'name')
        self.assertEqual(m.resolve([row()], 'firs')['status'], 'missing')
        self.assertEqual(m.resolve([row(), row('two')], 'first')['status'], 'ambiguous')

    def test_http_error_no_retry(self):
        opener = Opener([HTTPError(m.ENDPOINT, 429, 'quota', {'Retry-After': '100'}, io.BytesIO(b'error'))])
        log = []
        with self.assertRaisesRegex(m.DataError, '429'):
            m.fetch_catalog('SECRET_FOR_TEST', 10, log, opener)
        self.assertEqual(len(opener.requests), 1)
        self.assertEqual(log[0]['headers']['Retry-After'], '100')

    def test_redirect_not_followed(self):
        self.assertIsNone(m.NoRedirect().redirect_request(None, None, 302, '', {}, 'https://example.com'))

    def test_atomic_write_secret_guard(self):
        with tempfile.TemporaryDirectory() as d:
            target = Path(d)/'cache.json'
            m.atomic_json(target, {'old': True})
            with self.assertRaises(m.DataError):
                m.atomic_json(target, {'bad': 'SECRET_FOR_TEST'}, 'SECRET_FOR_TEST')
            self.assertEqual(json.loads(target.read_text()), {'old': True})

    def test_cache_validity(self):
        catalog = {'complete': True, 'fetched_at': datetime.now(timezone.utc).isoformat(),
                   'intelligence_index_version': 4.3, 'data': [row()]}
        self.assertTrue(m.cache_valid(catalog, 6))
        catalog['complete'] = False
        self.assertFalse(m.cache_valid(catalog, 6))

    def test_cached_lookup_needs_no_key_or_network(self):
        with tempfile.TemporaryDirectory() as d:
            cache = Path(d)/'cache.json'
            catalog = {'complete': True, 'fetched_at': datetime.now(timezone.utc).isoformat(),
                       'intelligence_index_version': 4.3, 'tier': 'free', 'data': [row()]}
            m.atomic_json(cache, catalog)
            with patch.dict(m.os.environ, {}, clear=True), patch.object(m, 'fetch_catalog') as fetch:
                code = m.main(['--cache', str(cache), '--output', str(Path(d)/'out'), '--model', 'first'])
                fetch.assert_not_called()
            self.assertEqual(code, 0)
            run = json.loads((Path(d)/'out/run.json').read_text())
            self.assertTrue(run['cache_used'])
            self.assertEqual(run['request_count'], 0)

    def test_failed_refresh_preserves_old_cache(self):
        with tempfile.TemporaryDirectory() as d:
            cache = Path(d)/'cache.json'
            original = {'old': 'keep'}
            m.atomic_json(cache, original)
            with patch.dict(m.os.environ, {'ARTIFICIAL_ANALYSIS_API_KEY': 'SECRET_FOR_TEST'}), \
                    patch.object(m, 'fetch_catalog', side_effect=m.DataError('Incomplete pagination')):
                code = m.main(['--cache', str(cache), '--output', str(Path(d)/'out'), '--refresh'])
            self.assertEqual(code, 1)
            self.assertEqual(json.loads(cache.read_text()), original)

    def test_missing_model_refreshes_once(self):
        with tempfile.TemporaryDirectory() as d:
            cache = Path(d)/'cache.json'
            catalog = {'complete': True, 'fetched_at': datetime.now(timezone.utc).isoformat(),
                       'intelligence_index_version': 4.3, 'tier': 'free', 'data': [row()]}
            m.atomic_json(cache, catalog)
            with patch.dict(m.os.environ, {'ARTIFICIAL_ANALYSIS_API_KEY': 'SECRET_FOR_TEST'}), \
                    patch.object(m, 'fetch_catalog', return_value=catalog) as fetch:
                code = m.main(['--cache', str(cache), '--output', str(Path(d)/'out'), '--model', 'missing'])
                fetch.assert_called_once()
            self.assertEqual(code, 2)


if __name__ == '__main__':
    unittest.main()
