---
doc_type: guide
updated_at: 2026-10-07
purpose: Fast, configuration-safe model collection and maintenance.
related:
  - path: ../favorites.json
    why: Selected configurations and explicit defaults.
  - path: ./LEARNINGS.md
    why: Shortcuts, failures and inefficiencies from the initial work.
  - path: ./API.md
    why: Authentication, quota and field coverage.
---

# Collect and maintain model data

## Fast path: existing source data

**Do not start with search, subagents, native readers or a browser.** The retained
Free catalogue and public website payload cover hundreds of models.

1. Find candidates locally, then choose an exact configuration:

   ```bash
   python3 ~/agents/ai-models/scripts/list_configurations.py --search 'gpt-6-luna'
   ```

   Search is discovery only, not fuzzy matching for publication. Check full
   model/configuration name, UUID, slug and fallback settings.
2. Add confirmed entries to `favorites.json`. Use a stable alias and explicit
   `default_effort`; each configuration stores `id`, `slug`, `effort`. Existing
   medium defaults are intentional. An absent effort must not fall back to max.
3. Rebuild once for the whole batch:

   ```bash
   python3 ~/agents/ai-models/scripts/offline_extract.py
   python3 ~/agents/ai-models/scripts/build_snapshot.py
   python3 ~/agents/ai-models/scripts/value_ratings.py
   python3 ~/agents/ai-models/scripts/cheat_scores.py
   python3 ~/agents/ai-models/scripts/effort_curves.py
   ```

4. Check `data/<date>/validation.json`, then query or read `TABLE.md`. Keep
   missing values; do not chase a confirmed N/A with extra providers.
5. Update scoped `STATE.md` and commit only the intended selection/data changes.

`offline_extract.py` uses the saved Flight record `e` and an explicit JSON
pointer. This deliberately fails visibly if a future payload changes structure.
It validates all selected identities and preserves API/site precision separately.
Do not present it as a general live scraper. Cross-source disagreements need
inspection; they are not permission to overwrite one source with another.

## If freshness or a genuinely absent model requires a refresh

- API first: one complete paginated batch for all models, using
  `scripts/model_data.py`. September 30's batch was four requests, not one per
  model. Stage output in ignored `cache/`; review before publishing a dated source.
- Supply the key through environment or the human-run hidden-input launcher in
  [key setup](api-key-setup.md).
  Nothing automatically opens Terminal or persists a key.
- Preserve the previous published snapshot. API-only refresh does not update
  website-only benchmark/token/time fields. Keep source timestamps separate.
- For website gaps, first check whether one public page payload contains the
  whole relevant model list. Parse it once; avoid one fetch per chart or effort.
  A fresh raw-HTTP route has not been implemented or verified here.
- Use a native reader only for a specific unresolved label/definition. Require
  source evidence before accepting numbers. For full numeric ingestion, prefer
  captured structured payload over a model-generated summary.
- If a needed public payload is still inaccessible, follow the owner's current
  authorized provider order/budget. No automatic paid fallback. Headless is not
  immune to throttling. Visible browser requires permission; stop on challenges,
  403/429, Pro gates or login requirements rather than bypassing them.

## Add a new model from the website only (verified October 7)

Used for Claude Haiku 5.5 when the model was missing and no API key was set.

1. `curl` the public page `https://artificialanalysis.ai/models/<slug>` with a
   desktop User-Agent. It returned HTTP 200 with no login. Save each page in a
   fresh scratch folder.
2. Parse the `self.__next_f.push` chunks into the same `next_flight_chunks`
   JSON the old capture used. Find the list holding full model objects (on
   October 7: record `33`, `/3/children/3/children/3/initialModels`, about 26
   models). Pick the one page that lists every configuration you need (the
   variant selector shows the slugs; the lowest-effort page held all five).
3. Keep that payload under `sources/<date>/browser/`, write `fetch.json` (URLs,
   status, page hashes, the pointer) and `manifest.json` (file hashes).
4. Add the model to `favorites.json` with `"website_source": "<date>"`, or put
   it on single configurations to supplement a model whose other rows stay
   API-checked. List every kept payload in `fetch.json` `kept_payloads` with its
   own record id (it differs page to page: 33, 36, 38 on October 7). The
   extractor requires each configuration to be identical in every payload that
   holds it, skips the API cross-check, and tables mark it with `*`.
5. Regenerate `data/<date>/EFFORTS.md` with `scripts/effort_curves.py` after
   `cheat_scores.py`.
6. Rebuild as above and update the configuration count in
   `scripts/test_model_data.py`.

## Add fields without tangling data and collection

`benchmarks.json` owns field meanings and source-key mappings. Full raw selected
records and the full payload retain additional fields. Promote a new metric only
after checking its version, unit, direction, task population, reasoning settings
and applicability. Change `build_snapshot.py` to expose it in the compact view;
regenerate the table rather than maintaining another hand-edited metric table.

Keep new providers in separate namespaces. Do not change the meaning of an
existing field just because a different source uses a similar label.
