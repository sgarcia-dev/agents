#!/usr/bin/env python3
"""Build a compact, source-separated snapshot from verified offline records."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = json.loads((ROOT/'favorites.json').read_text())
DATE = REGISTRY['snapshot_date']
HERE = ROOT/'data'/DATE
BENCHMARKS = {m['slug']: m for m in
              json.loads((ROOT/'benchmarks.json').read_text())['metrics']
              if m.get('status') == 'accepted' and m.get('view') == 'benchmark'}


def headline(a, w):
    """Display values: API when present, else the website's own fields, labelled."""
    if a is not None:
        costs = a.get('artificial_analysis_intelligence_index_cost') or {}
        return {'source': 'api', 'intelligence_index': a['evaluations']['artificial_analysis_intelligence_index'],
                'price_usd_per_million_tokens': a['pricing'],
                'intelligence_index_total_cost_usd': costs.get('total_cost'),
                'intelligence_index_cost_per_task_usd': (costs.get('cost_per_task') or {}).get('total_cost'),
                'median_output_tokens_per_second': a['performance']['median_output_tokens_per_second'],
                'median_time_to_first_token_seconds': a['performance']['median_time_to_first_token_seconds']}
    speed = w.get('timescaleData') or {}
    return {'source': 'website', 'intelligence_index': w.get('intelligenceIndex'),
            'price_usd_per_million_tokens': {'price_1m_input_tokens': w.get('price1mInputTokens'),
                'price_1m_output_tokens': w.get('price1mOutputTokens'),
                'price_1m_cache_hit_tokens': w.get('cacheHitPrice'),
                'price_1m_cache_write_tokens': w.get('cacheWritePrice')},
            'intelligence_index_total_cost_usd': (w.get('intelligenceIndexCost') or {}).get('total'),
            'intelligence_index_cost_per_task_usd': ((w.get('intelligenceIndexCostPerTask') or {}).get('cost') or {}).get('total'),
            'median_output_tokens_per_second': speed.get('medianOutputSpeed'),
            'median_time_to_first_token_seconds': speed.get('medianTimeToFirstChunk')}


def main():
    raw = json.loads((HERE / 'raw-selected.json').read_text())
    checked = json.loads((HERE / 'validation.json').read_text())
    assert checked['passed'] and not checked['failures']
    models = []
    for r in raw['selected']:
        a, w = r['api'], r['website']
        assert w['id'] == r['id'] and w['slug'] == r['slug']
        assert a is None or (a['id'] == r['id'] and a['slug'] == r['slug'])
        effort = (w.get('effort') or {}).get('slug')
        configuration = next(c for model in REGISTRY['models'].values()
                             for c in model['configurations'] if c['id'] == r['id'])
        assert configuration['slug'] == r['slug'] and configuration['effort'] == effort
        costs = (a or {}).get('artificial_analysis_intelligence_index_cost') or {}
        models.append({
            'id': r['id'], 'slug': r['slug'], 'name': w['name'], 'effort': effort,
            'headline': headline(a, w),
            'api': None if a is None else {
                'intelligence_index': a['evaluations']['artificial_analysis_intelligence_index'],
                'index_version': raw['metadata']['api_catalog_metadata']['intelligence_index_version'],
                'price_usd_per_million_tokens': a['pricing'],
                'intelligence_index_total_cost_usd': costs.get('total_cost'),
                'intelligence_index_cost_per_task_usd': (costs.get('cost_per_task') or {}).get('total_cost'),
                'performance': a['performance'],
            },
            'website': {
                'intelligence_index_unrounded': w.get('intelligenceIndex'),
                'benchmark_scores': {name: {'raw': w.get(metric['website_key']),
                    'unit': metric['unit'],
                    'percent': w.get(metric['website_key']) * 100 if metric['unit'] == 'fraction' and w.get(metric['website_key']) is not None else None,
                    'source_key': metric['website_key']} for name, metric in BENCHMARKS.items() if 'website_key' in metric} | {
                    name: {'raw': next((e['score'] for e in w.get('intelligenceIndexEvaluations', []) if e['slug'] == metric['evaluation_slug']), None),
                           'unit': metric['unit'], 'percent': None, 'source_key': 'intelligenceIndexEvaluations.' + metric['evaluation_slug'] + '.score'}
                    for name, metric in BENCHMARKS.items() if 'website_key' not in metric},
                'omniscience_accuracy_fraction': w.get('omniscienceAccuracy'),
                'omniscience_hallucination_fraction_of_noncorrect_responses': w.get('omniscienceHallucinationRate'),
                'intelligence_index_total_tokens': w.get('canonicalIntelligenceIndexTokenCount'),
                'intelligence_index_total_cost_usd': w.get('intelligenceIndexCost'),
                'intelligence_index_output_tokens_per_task': w.get('intelligenceIndexOutputTokensPerTask'),
                'intelligence_index_cost_per_task': w.get('intelligenceIndexCostPerTask'),
                'intelligence_index_decode_time_per_task_seconds': w.get('intelligenceIndexTimePerTask'),
                'headline_performance': w.get('timescaleData'),
                'performance_source': w.get('performanceDataSource'),
                'performance_by_prompt_length': w.get('performanceByPromptType'),
                'per_evaluation': w.get('intelligenceIndexEvaluations'),
            },
            'provenance': r['provenance'],
        })
    expected = sum(len(m['configurations']) for m in REGISTRY['models'].values())
    assert len(models) == len({m['id'] for m in models}) == expected
    snapshot = {
        'source': 'Artificial Analysis', 'snapshot_date': DATE,
        'api_fetched_at': raw['metadata']['api_catalog_metadata']['fetched_at'],
        'website_supplements': raw['metadata'].get('website_supplements', {}),
        'website_capture_time': 'Date established from original capture; exact timestamp unavailable',
        'notes': [
            'Offline feasibility snapshot, not a live or scheduled service.',
            'Time per task is weighted decode time, not wall-clock completion; excludes TTFT and overhead.',
            'Omniscience hallucination denominator is incorrect + partial + not attempted, not all questions.',
            'Costs are benchmark-suite costs, not a guarantee for your workload.',
            'Claude configurations include adaptive reasoning and default fallback.',
            'Missing compact values are null; favorites.json retains missing versus explicit-null source states.',
            'Generic API performance and website first-party performance are separate measurements.',
            'Rows with api null are website-only supplements (see provenance.website.captured). Their headline values come from the website and are marked with * in TABLE.md.',
        ],
        'models': models,
    }
    def fmt(value, digits=2):
        return 'N/A' if value is None else f'{value:,.{digits}f}'
    table = [f'---\ndoc_type: reference\nupdated_at: {DATE}\npurpose: Generated human-readable view of the configuration-specific snapshot.\nrelated:\n  - path: ./favorites.snapshot.json\n    why: Machine-readable source of this table.\n---\n',
             '# Model comparison',
             f'Snapshot: {DATE}. Source: Artificial Analysis. Generated by `scripts/build_snapshot.py`; do not edit numbers here.',
             'Time is estimated decode time, NOT wall-clock task completion. Hallucination rate uses non-correct responses as its denominator. N/A is not zero.',
             '| Configuration | Intelligence | Input/output USD per million | Index USD/task | Estimated decode s/task | API output tokens/s |',
             '|---|---:|---:|---:|---:|---:|']
    for m in models:
        h,w=m['headline'],m['website'];p=h['price_usd_per_million_tokens']
        star='' if h['source']=='api' else '*'
        table.append(f"| {m['slug']}{star} | {fmt(h['intelligence_index'],1)} | {fmt(p['price_1m_input_tokens'])} / {fmt(p['price_1m_output_tokens'])} | {fmt(h['intelligence_index_cost_per_task_usd'],4)} | {fmt(w['intelligence_index_decode_time_per_task_seconds'])} | {fmt(h['median_output_tokens_per_second'])} |")
    table.append('')
    table.append('\\* Website-only row captured later (see `sources/<date>/fetch.json`); no API cross-check. Speed is the website first-party median.')
    table += ['', '## Benchmark scores',
              '| Configuration | AutomationBench-AA | Terminal-Bench 4.0 | AA-Omniscience index | GDP.pdf all-pass | Hallucination rate | AA-LCR pass-rate | AA-Briefcase Elo |',
              '|---|---:|---:|---:|---:|---:|---:|---:|']
    for m in models:
        w=m['website'];b=w['benchmark_scores']
        values=[fmt(b[key]['percent'])+'%' if b[key]['percent'] is not None else 'N/A'
                for key in ['automationbench-aa','terminalbench-4-0']]
        hallucination=w['omniscience_hallucination_fraction_of_noncorrect_responses']
        values += [fmt(b['aa-omniscience']['raw']),fmt(b['gdp-pdf']['percent'])+'%' if b['gdp-pdf']['percent'] is not None else 'N/A',fmt(hallucination*100)+'%' if hallucination is not None else 'N/A']
        values += [fmt(b['aa-lcr-v1-1']['percent'])+'%' if b['aa-lcr-v1-1']['percent'] is not None else 'N/A', fmt(b['aa-briefcase']['raw'])]
        table.append('| '+m['slug']+' | '+' | '.join(values)+' |')
    table += ['', '## Index token use and total cost',
              'Per-task output tokens are weighted averages, including reasoning and answer tokens. Whole-suite totals are original counts, not extrapolated task averages.',
              '| Configuration | Output tokens/task | Whole-index output tokens | Whole-index USD |',
              '|---|---:|---:|---:|']
    for m in models:
        h,w=m['headline'],m['website']
        task=w['intelligence_index_output_tokens_per_task'] or {}
        total=w['intelligence_index_total_tokens'] or {}
        table.append(f"| {m['slug']} | {fmt(task.get('output'),0)} | {fmt(total.get('output'),0)} | {fmt(h['intelligence_index_total_cost_usd'])} |")
    encoded=json.dumps(snapshot,indent=2,ensure_ascii=False,allow_nan=False)+'\n'
    (HERE/'favorites.snapshot.json').write_text(encoded)
    (HERE/'TABLE.md').write_text('\n\n'.join(table[:4])+'\n\n'+'\n'.join(table[4:])+'\n')
    print(json.dumps({'status': 'ok', 'models': len(models), 'network_calls': 0}))


if __name__ == '__main__':
    main()
