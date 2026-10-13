---
doc_type: sources
updated_at: 2026-10-07
purpose: Source trust and self-contained provenance for model data.
related:
  - path: ./sources/2026-09-30/manifest.json
    why: Original byte hashes and canonical source paths. (raw data not published)
  - path: ./data/2026-09-30/raw-selected.json
    why: Exact UUIDs and JSON pointers for each published configuration. (raw data not published)
---

# Sources and trust

## Current numeric evidence

- `sources/2026-09-30/api/catalog.json`: complete Free API response assembled from
  four successful pages; all 686 rows retained. `api/run.json` keeps original
  request statuses, quota headers and timestamp. It contains no authentication key.
- `sources/2026-09-30/browser/claude-opus-5-5.embedded.json`: saved public page
  application payload with the detailed model list. Exact UUID+slug+effort checks
  precede numeric acceptance. Browser capture date is known; exact timestamp is
  not in the supplied metadata. Do not invent one from file mtime.
- `data/2026-09-30/raw-selected.json`: selected original objects and folder-relative
  source pointers/hashes. API and site values remain separate.
- `data/2026-09-30/validation.json`: deterministic numeric/identity checks.
- `sources/2026-09-30/browser/structured-results.json`: captured rendered table
  values used to corroborate raw seconds versus chart minutes.

## October 7 website supplement (Claude Haiku 5.5)

- `sources/2026-10-07/browser/`: five public model page payloads (Haiku low,
  Sonnet low, medium, high, GPT-5.6 Luna) holding every October 7
  configuration: all Haiku 5.5 and Sonnet 5.5 efforts, Opus 5.5 high/xhigh/max,
  GPT-6.1 Sol xhigh/max, all GPT-6 Luna and GPT-5.6 Luna efforts. Plain HTTPS
  GET, no login, no key. `fetch.json` lists all 27 fetched URLs with
  page hashes, each kept payload's Flight pointer, and the drift found against
  September 30. `manifest.json` has file hashes.
- No API refresh: the API key was not available, so these rows have no API
  cross-check. Opus low/medium and Sol low/medium/high keep their September 30
  API-checked rows (only speed medians had moved).
- AA priced Haiku at the short-prompt rate throughout (implied $0.50 per million
  output tokens). Anthropic charges 5 times that above 100K-token prompts.
- `evidence/2026-10-07/`: ten Codex research reports with prompts (Haiku
  efforts, system card, Claude Code use; Sonnet efforts; Opus and Sol efforts;
  job strengths; Haiku vs Sonnet vs Luna; Luna long context; Luna vs Haiku by
  effort; the jump to Sonnet and Sol), two Gemini notes with the root's
  verdicts, and `runs.json` telemetry. Vendor numbers there are Anthropic's or
  OpenAI's, not reproduced; CursorBench, FrontierCode (Cognition) and
  VulcanBench are independent.

## Definitions

Original `claude-opus-5-5.txt` documents weighted task cost/tokens and task decode
time (lines 326–368, 421–422). `evaluations.txt` describes the benchmark purposes.
The direct [AA-Omniscience evaluation](https://artificialanalysis.ai/evaluations/omniscience)
defines hallucination as `incorrect / (incorrect + partial + not attempted)`.
Reader/source-note receipts are in `evidence/2026-09-30/native/`.

[Current V2 API docs](https://artificialanalysis.ai/data-api/docs) own current
endpoints/tier/quota guidance. The [legacy reference](https://artificialanalysis.ai/api-reference/)
recommends caching, but its old 1,000/day quota is not current. Internal cache use
does not prove export or redistribution rights.

## Historical evidence

`evidence/2026-09-30/` retains the original research bundle, native logs and full
API/favorites/five-page fetch-test archives. Paths in archived reports/logs reflect
where files existed at capture time; they are history, not live dependencies.
Archives may contain old network scripts: do not execute them as part of reading
this dataset. The original research/Downloads copies were left intact, not deleted.

## Weak claims to avoid

No inspected source proves actual elapsed task completion, zero hallucinations,
identical results in the owner's harness, complete API access to website fields,
future site-parser stability, successful Pro export, unrestricted redistribution
or exact per-stage wall-clock/currency cost for the original investigation.
