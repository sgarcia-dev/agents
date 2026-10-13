---
doc_type: guide
updated_at: 2026-10-07
purpose: Preserve the fast path and avoid repeating initial collection overhead.
related:
  - path: ./README.md
    why: Operational sequence using these lessons.
  - path: ../evidence/2026-09-30/original-research/RESEARCH.md
    why: Original evidence and exact observations, not the routine entrypoint. (raw data not published)
---

# Lessons and shortcuts

## Why the first run was slow

The owner experienced roughly 30–45 minutes across the work. Exact full wall-clock
duration and per-stage timings were not instrumented, so that range is the owner's
estimate, not a measured claim. It mixed initial access experiments, skill setup,
source inspection, reader verification, report writing and Git publication.

The avoidable overhead was **continuing to investigate collection when a complete
catalogue and detailed website payload had already been captured**. Three local
workers were used: two disjoint inspections, then an extraction worker. One native
Codex reader checked two missing configurations and API/definition pages. That
reader made two searches and five page reads, and its telemetry recorded 441,104
input tokens (373,248 cached) and 14,166 output tokens. This is substantial model
work for a narrow confirmation, even with a cheap requested model. A root page
read then confirmed the hallucination-rate denominator. Token figures are not
incremental dollar charges; subscription cost/quota impact is unknown.

The extraction worker was interrupted and resumed. Updates to the owner were too
sparse. No per-stage timing ledger was kept. More parallel workers would not fix
those problems and could multiply duplicated reads and context costs.

## What to do differently

| Situation | Fastest useful action |
|---|---|
| Read current numbers | Query local snapshot; no model/network calls |
| Add another model already in sources | Discover exact slug/UUID locally, add registry entry, rebuild once |
| Add many models | One batch selection/extraction, not one reader per model |
| Add a field already in raw objects | Verify its meaning once, then expose locally |
| Refresh Free data | One complete catalogue batch, cache, resolve all models offline |
| Fill website-only fields | Reuse a full structured page payload; do not fetch every chart |
| Source explicitly says N/A | Record unavailable and stop, not escalate across providers |
| Definition is ambiguous | One targeted source check with a small output budget |
| Source payloads disagree | Compare identity, version, timing and units before ranking sources |

Routine reading/extraction should normally take local-compute time, not another
research session. Measured replay/query timings for this promotion are in
`data/2026-09-30/promotion-verification.json`; they are not promises about fresh
network requests. Use scripts for parsing and checks, not LLMs. Use workers only
for genuinely independent unresolved questions, never to re-read the same source.

## Mistakes worth remembering

- Bare family slugs select max. Distinct `-medium`/`-low`/`-xhigh` slugs and exact
  UUIDs solve this. Do not invent URL query filters.
- Parallel and Claude returned Astra for an earlier Sol comparison URL. Correct
  URL text alone does not prove selected model identity.
- Claude WebFetch was a processed summary, not a complete page collector.
- API headline speed and website first-party speed differ. Keep both labelled.
- `performanceByPromptType.medium` is medium prompt length, not medium effort.
- AA task time excludes TTFT/overhead and is not wall-clock agent completion.
- AA-Omniscience index is not percent; hallucination rate uses non-correct
  responses as the denominator. GDP.pdf is not a direct hallucination rate.
- Sonnet low's benchmark scores exist despite missing suite aggregates. Missing
  aggregate is not missing configuration and must not become zero.
- Luna medium has hundredK-specific speed but lacks headline speed. Do not
  substitute it for a representative speed or invent task time.
- API version 4.3 lacks the website's v4.3.2 patch precision. Preserve both.
- Pro-gated exports are not required to cache a successful Free API response.
- Headless mode does not prevent rate limiting. No background recurring scraper
  or visible browser is justified by this offline workflow.

## October 7: adding Claude Haiku 5.5

- Plain `curl` of a model page works and is fast (five pages in about a
  minute). No browser, reader or search was needed for the numbers.
- The page layout changed since September 30: the full 686-model list (record
  `e`) is gone from model pages. Each page now embeds about 26 comparison models.
  The old pointer fails, so the extractor keeps it only for the saved
  September 30 payload.
- Bare slug `claude-haiku-5-5` is still max effort.
- Round 3: the record `e` list is not gone everywhere. The GPT-5.6 Luna page
  (about 4 MB) still embeds 696 models at the old pointer, which gave both Luna
  families in one fetch. Search each page for every `initialModels` and `models`
  list before fetching more pages. A `-max` slug returns 404; max is the bare
  family slug.
- AA's per-task cost uses the short-prompt price. Models with a long-prompt
  price tier (Haiku 5.5: 5 times above 100K tokens) look cheaper there than they
  are on long agent runs. Check vendor pricing tiers before ranking value.
- A Codex child could not keep a backgrounded `agy` job alive; it produced empty
  files. Launch the Gemini run from the root instead.

## Update discipline

Capture stage durations and request counts for future fresh collections. Send a
brief update on meaningful progress or a long external wait. Do not re-run the
whole access-method experiment for each new model. The initial report is now
historical evidence, not the place agents must reconstruct the workflow from.
