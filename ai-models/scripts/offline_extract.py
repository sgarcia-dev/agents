#!/usr/bin/env python3
"""Offline, standard-library exact-identity extraction. Re-run to verify sources."""
import hashlib
import json
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = json.loads((ROOT/'favorites.json').read_text())
DATE = REGISTRY['snapshot_date']
OUT = ROOT/'data'/DATE
API = ROOT/'sources'/DATE/'api'
SITE = ROOT/'sources'/DATE/'browser'
SELECT = [(c['slug'], c['id'], c['effort'], c.get('website_source', model.get('website_source')))
          for model in REGISTRY['models'].values() for c in model['configurations']]
# Website-only supplements: newer model pages captured without an API refresh.
# A configuration's own website_source overrides its model's. Each dated folder's
# fetch.json names the kept payloads and each one's explicit Flight pointer.
SUPPLEMENTS = sorted({x[3] for x in SELECT if x[3]})
POINTER = '/3/children/0/3/children/3/children/1/3/children/1/3/children/0/3/models'

def load(p):
    return json.loads(p.read_text())

def source(p):
    return {'path':p.relative_to(ROOT).as_posix(), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}

def field(obj, path, unit=None):
    value=obj
    for key in path.split('.'):
        if value is None:
            return {'source_key':path,'status':'unavailable','reason':'null_parent','unit':unit}
        if not isinstance(value,dict) or key not in value:
            return {'source_key':path,'status':'missing','unit':unit}
        value=value[key]
    return {'source_key':path,'status':'null' if value is None else 'present','raw':value,'unit':unit}

def inventory(obj, path=''):
    result={}
    if isinstance(obj,dict):
        for k,v in obj.items():
            p=path+'/'+k.replace('~','~0').replace('/','~1')
            result[p]='null' if v is None else type(v).__name__
            result.update(inventory(v,p))
    elif isinstance(obj,list):
        for i,v in enumerate(obj): result.update(inventory(v,path+'/'+str(i)))
    return result

def flight_records(embedded):
    text=''.join(chunk[1] for chunk in embedded['next_flight_chunks'] if len(chunk)>1 and isinstance(chunk[1],str))
    records={}
    for line in text.splitlines():
        rid,sep,payload=line.partition(':')
        if sep:
            try: records[rid]=json.loads(payload)
            except json.JSONDecodeError: pass
    return records

def supplement(date):
    base=ROOT/'sources'/date
    fetch=load(base/'fetch.json')
    payloads=[]
    for kept in fetch['kept_payloads']:
        path=base/kept['path']
        models=flight_records(load(path))[kept['record']]
        for key in kept['json_pointer'].strip('/').split('/'):
            models=models[int(key)] if isinstance(models,list) else models[key]
        payloads.append({'models':models,'source':source(path),'pointer':{'record':kept['record'],'json_pointer':kept['json_pointer']}})
    return {'payloads':payloads,'fetch':{k:v for k,v in fetch.items() if k!='pages'}}

def main():
    catalogue=load(API/'catalog.json'); run=load(API/'run.json')
    supplements={d:supplement(d) for d in SUPPLEMENTS}
    embedded=load(SITE/'claude-opus-5-5.embedded.json')
    records={}; failures=[]; tests=[]
    def check(name, ok, detail=None):
        tests.append({'test':name,'passed':bool(ok),'detail':detail})
        if not ok: failures.append(name)
    text=''.join(chunk[1] for chunk in embedded['next_flight_chunks'] if len(chunk)>1 and isinstance(chunk[1],str))
    for line in text.splitlines():
        rid,sep,payload=line.partition(':')
        if sep:
            try: records[rid]=json.loads(payload)
            except json.JSONDecodeError: pass
    models=records['e']
    for key in POINTER.strip('/').split('/'):
        models=models[int(key)] if isinstance(models,list) else models[key]
    metadata={
      'sources':{n:source(p) for n,p in [('catalog',API/'catalog.json'),('api_run',API/'run.json'),('website',SITE/'claude-opus-5-5.embedded.json'),('browser_results',SITE/'results.json'),('browser_structured_results',SITE/'structured-results.json')]},
      'api_catalog_metadata':{k:v for k,v in catalogue.items() if k!='data'},
      'api_run':run,
      'browser_capture_metadata':[{k:v for k,v in row.items() if k not in ('controls','responses')} for row in load(SITE/'results.json') if row.get('id')=='claude-opus-5-5'],
      'website_supplements':{d:{'payloads':[{'source':p['source'],'flight_pointer':p['pointer']} for p in x['payloads']],'fetch':x['fetch']} for d,x in supplements.items()},
      'collection_time_note':'No precise browser capture timestamp in supplied metadata; date encoded in source directory is 2026-09-30. File mtime is not treated as collection time.',
      'website_dataset_metadata':[{'pointer':'/json_ld/'+str(i),'name':x.get('name'),'description':x.get('description')} for i,x in enumerate(embedded['json_ld']) if isinstance(x,dict) and x.get('@type')=='Dataset'],
      'unit_notes':{'cost':'USD, confirmed by JSON-LD descriptions','price':'USD per million tokens, confirmed by Pricing JSON-LD','task_time':'Source-reported weighted decode estimate excluding TTFT/overhead, NOT wall-clock. Numeric Flight values are seconds (corroborated by supplied structured comparison rows); JSON-LD chart description says minutes, so retain that chart-vs-raw distinction.','omniscience':'Index in [-100,100], not percent. Accuracy and hallucination fields are fractions checked within [0,1].','performance':'API generic performance and site first-party performance may differ; not required to match.'}}
    raw=[]; favorites=[]; comparisons=[]
    check('unique_requested_ids_and_slugs',bool(SELECT) and len(SELECT)==len({x[1] for x in SELECT})==len({x[0] for x in SELECT}))
    for slug,uid,effort,website_date in SELECT:
        if website_date:
            sup=supplements[website_date]
            # Website-only: absent from the saved API catalogue by design, so only the site must match.
            # (A refreshed row may still exist in the saved API catalogue; it is deliberately not used.)
            hits=[(p,i,x) for p in sup['payloads'] for i,x in enumerate(p['models']) if isinstance(x,dict) and x.get('id')==uid and x.get('slug')==slug]
            check(slug+':site_only_found_once_per_payload',bool(hits) and len({id(p) for p,_,_ in hits})==len(hits))
            check(slug+':site_only_identical_across_payloads',len({json.dumps(x,sort_keys=True) for _,_,x in hits})==1)
            if not hits: continue
            pay,wi,w=hits[0]; a=None
            check(slug+':effort_agreement',(w.get('effort') or {}).get('slug')==effort)
            provenance={'api':None,'website':dict(pay['source'],flight_record=pay['pointer']['record'],json_pointer=pay['pointer']['json_pointer']+'/'+str(wi),captured=website_date)}
        else:
            am=[(i,x) for i,x in enumerate(catalogue['data']) if x['id']==uid and x['slug']==slug]
            wm=[(i,x) for i,x in enumerate(models) if isinstance(x,dict) and x.get('id')==uid and x.get('slug')==slug]
            check(slug+':exact_unique_API_and_site',len(am)==len(wm)==1)
            if len(am)!=1 or len(wm)!=1: continue
            ai,a=am[0]; wi,w=wm[0]
            check(slug+':effort_agreement',(w.get('effort') or {}).get('slug')==effort)
            provenance={'api':dict(metadata['sources']['catalog'],json_pointer='/data/'+str(ai)), 'website':dict(metadata['sources']['website'],flight_record='e',json_pointer=POINTER+'/'+str(wi))}
        raw.append({'id':uid,'slug':slug,'provenance':provenance,'api':a,'website':w})
        api=None if a is None else {k:field(a,k,u) for k,u in [('evaluations','index points'),('artificial_analysis_intelligence_index_cost','USD'),('pricing','USD per million tokens'),('performance','actual key defines seconds or tokens/second')]}
        web={k:field(w,k,u) for k,u in [('intelligenceIndex','index points'),('intelligenceIndexCost','USD'),('canonicalIntelligenceIndexTokenCount','tokens, whole suite'),('intelligenceIndexOutputTokensPerTask','tokens per task, weighted'),('intelligenceIndexCostPerTask','USD per task, weighted'),('intelligenceIndexTimePerTask','seconds, source estimate'),('intelligenceIndexEvaluations','per-evaluation raw units'),('timescaleData','source key defines unit'),('performanceByPromptType','prompt length, NOT reasoning effort'),('endToEndResponseTime','seconds'),('timeToFirstAnswerToken','seconds'),('performanceDataSource',None)]}
        web['prices']={k:field(w,k,'USD per million tokens') for k in ['price1mInputTokens','price1mOutputTokens','cacheHitPrice','cacheWritePrice']}
        web['benchmarks']={}
        for k in ['automationBenchPartialScore','terminalBench40','gdpPdfAllPass','omniscience','omniscienceAccuracy','omniscienceHallucinationRate','lcr']:
            f=field(w,k,'index points' if k=='omniscience' else 'fraction')
            if f['status']=='present' and k!='omniscience':
                check(slug+':fraction:'+k,isinstance(f['raw'],(int,float)) and 0<=f['raw']<=1)
                f['pct_display']=f['raw']*100
            web['benchmarks'][k]=f
        for ev in web['intelligenceIndexEvaluations'].get('raw',[]):
            ev=dict(ev)
            ev['time_availability']=field(ev,'timePerTask','seconds, source estimate')
            ev['output_tokens_availability']=field(ev,'outputTokensPerTask','tokens per evaluation task')
            ev['reasoning_tokens_availability']=field(ev,'reasoningTokensPerTask','tokens per evaluation task')
            ev['answer_tokens_availability']=field(ev,'answerTokensPerTask','tokens per evaluation task')
            ev['cost_availability']=field(ev,'costPerTask','USD per evaluation task, unweighted')
            if ev['slug'] in ('automationbench-aa','terminalbench-4-0','gdp-pdf'):
                ev['score_pct_display']=ev['score']*100
            web.setdefault('per_evaluation',[]).append(ev)
        if a is None:
            favorites.append({'id':uid,'slug':slug,'name':w['name'],'short_name':w['shortName'],'effort':w.get('effort'),'provenance':provenance,'api':None,'website':web})
            continue
        maps=[('evaluations.artificial_analysis_intelligence_index','intelligenceIndex',1),('artificial_analysis_intelligence_index_cost.total_cost','intelligenceIndexCost.total',2),('artificial_analysis_intelligence_index_cost.cost_per_task.total_cost','intelligenceIndexCostPerTask.cost.total',4)]
        maps += [('pricing.'+ak,wk,2) for ak,wk in [('price_1m_input_tokens','price1mInputTokens'),('price_1m_output_tokens','price1mOutputTokens'),('price_1m_cache_hit_tokens','cacheHitPrice'),('price_1m_cache_write_tokens','cacheWritePrice')]]
        for ak,wk,digits in maps:
            af=field(a,ak);wf=field(w,wk);av=af.get('raw');wv=wf.get('raw')
            if av is not None and wv is not None:
                rounded=float(Decimal(str(wv)).quantize(Decimal(1).scaleb(-digits),rounding=ROUND_HALF_UP)) if digits is not None else wv
                ok=isinstance(av,(int,float)) and isinstance(wv,(int,float)) and av==rounded
                if not ok and digits is not None and isinstance(av,(int,float)) and isinstance(wv,(int,float)):
                    # The API rounds exact ties down while the site rounds them up; accept either only on an exact tie.
                    scaled=Decimal(str(wv)).scaleb(digits)
                    if scaled%1==Decimal('0.5'):
                        ok=av==float(scaled.quantize(Decimal(1),rounding=ROUND_HALF_DOWN).scaleb(-digits))
            else: ok=av is None and wv is None and af['status']!='missing'
            check(slug+':rounded_match:'+ak,ok)
            comparisons.append({'slug':slug,'api':af,'website':wf,'round_site_digits':digits,'rounding_mode':'decimal half up','matched':ok,'availability_difference':af['status']!=wf['status']})
        favorites.append({'id':uid,'slug':slug,'name':w['name'],'short_name':w['shortName'],'effort':w.get('effort'),'provenance':provenance,'api':api,'website':web})
    by={x['slug']:x for x in raw}
    if DATE == '2026-09-30' and 'claude-sonnet-5-5-low' in by and by['claude-sonnet-5-5-low']['api'] is not None:
        sn=by['claude-sonnet-5-5-low']
        check('Sonnet_low_null_aggregate',sn['api']['evaluations']['artificial_analysis_intelligence_index'] is None and sn['api']['artificial_analysis_intelligence_index_cost'] is None and sn['website']['intelligenceIndex'] is None and sn['website'].get('intelligenceIndexCost') is None and sn['website']['intelligenceIndexEvaluations']==[])
    if DATE == '2026-09-30' and 'gpt-6-luna-medium' in by and by['gpt-6-luna-medium']['api'] is not None:
        lm=by['gpt-6-luna-medium']
        check('Luna_medium_unavailable_performance_and_time',all(v is None for v in lm['api']['performance'].values()) and lm['website']['timescaleData']=={} and lm['website'].get('intelligenceIndexTimePerTask') is None and all('timePerTask' not in e for e in lm['website']['intelligenceIndexEvaluations']))
    check('all_requested_records_output',len(favorites)==len(SELECT))
    check('missing_vs_null_distinct',field({},'x')['status']=='missing' and field({'x':None},'x')['status']=='null' and field({'x':None},'x.y')['reason']=='null_parent')
    for x in raw:
        w=x['website']
        for key in ['intelligenceIndexCost','intelligenceIndexOutputTokensPerTask','canonicalIntelligenceIndexTokenCount']:
            if key in w:
                check(x['slug']+':numeric:'+key,all(isinstance(v,(int,float)) and not isinstance(v,bool) and v>=0 for v in w[key].values()))
        if 'intelligenceIndexCost' in w:
            cost=w['intelligenceIndexCost'];tokens=w['intelligenceIndexOutputTokensPerTask']
            check(x['slug']+':cost_and_token_parts',abs(cost['total']-cost['input']-cost['output'])<1e-8 and abs(tokens['output']-tokens['reasoning']-tokens['answer'])<1e-8)
    # Unit check against displayed max comparison, only metadata, not another page payload.
    comparison=next(x for x in load(SITE/'structured-results.json') if x.get('id')=='comparisons')
    displayed=next(row for table in comparison['tables'] for row in table['rows'] if row[0]=='Time per Task')
    def walk(value):
        if isinstance(value,dict):
            yield value
            for child in value.values(): yield from walk(child)
        elif isinstance(value,list):
            for child in value: yield from walk(child)
    max_opus=next(x for x in walk(records['e']) if x.get('slug')=='claude-opus-5-5' and 'intelligenceIndexTimePerTask' in x)
    check('raw_task_time_seconds_corroborated',round(max_opus['intelligenceIndexTimePerTask'],2)==float(displayed[1].removesuffix('s')), {'raw_seconds':max_opus['intelligenceIndexTimePerTask'],'display':displayed[1],'warning':'JSON-LD describes chart minutes, not these raw values'})
    validation={'passed':not failures,'test_count':len(tests),'failures':failures,'tests':tests,'api_vs_website_comparisons':comparisons,'field_inventory':{x['slug']:{'api':None if x['api'] is None else inventory(x['api']),'website':inventory(x['website'])} for x in raw},'source_metadata':metadata}
    if failures:
        OUT.mkdir(parents=True,exist_ok=True)
        (OUT/'validation.failed.json').write_text(json.dumps(validation,indent=2,allow_nan=False)+'\n')
        print(json.dumps({'passed':False,'failures':failures,'outputs_unchanged':True}))
        raise SystemExit(1)
    OUT.mkdir(parents=True,exist_ok=True)
    for name,obj in [('favorites.json',{'metadata':metadata,'favorites':favorites}),('raw-selected.json',{'metadata':metadata,'selected':raw}),('validation.json',validation)]:
        (OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
    print(json.dumps({'passed':not failures,'tests':len(tests),'failures':failures,'outputs':[str(OUT/n) for n in ['favorites.json','raw-selected.json','validation.json']]}))
    if failures: raise SystemExit(1)

if __name__=='__main__': main()
