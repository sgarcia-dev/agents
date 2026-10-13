---
created_at: 2026-09-30
updated_at: 2026-09-30
model: openai/gpt-6.1-sol
doc_type: capability
purpose: Describe Artificial Analysis model-data API access and the limits of public-page collection.
related:
  - path: ~/agents/ai-models/collection/README.md
    why: Portable retrieval procedure and bundled collector.
  - path: ~/agents/ai-models/collection/api-key-setup.md
    why: Hidden-input credential handoff and test launcher.
  - path: ~/agents/ai-models/SOURCES.md
    why: Earlier five-page browser/provider observations, including model mismatch and export gate.
---

# Artificial Analysis

This is a Python/HTTPS bridge, not an installed MCP connector. It is portable across Claude Code, Codex, OpenCode and Hermes if they can run Python and supply the environment variable. No other harness's native configuration is changed by installing it here.

## Sources and status

Promoted from the user's September 30 Downloads skill and key-setup guide. Official [API docs](https://artificialanalysis.ai/data-api/docs) were read September 30, 2026. Source-provided claims below are distinguished from live account verification.

**Status:** authenticated Free collection succeeded September 30: four HTTP 200 pages, 686 records, captured tier Free and remaining quota 96. Ten exact effort-specific favorite configurations were joined to saved website data and validated. Source responses, collector, tests and offline querying now live under `ai-models/`; no key was persisted. Quota is historical, not a current account reading.

## Endpoint and authentication

- Origin: `https://artificialanalysis.ai`.
- Base: `/api/v2`.
- Default: `GET /language/models/free?page=N`.
- Header: `x-api-key`, read from `ARTIFICIAL_ANALYSIS_API_KEY`.
- Keys belong to an organisation. Regeneration revokes the old value.
- Keep keys server-side and never log them. The helper blocks redirects, preventing an authenticated request from forwarding the key to another destination.

## Documented quota and tiers, checked September 30

| Tier | Requests per fixed 24-hour window | Language model coverage |
|---|---|---|
| Free | 100 | Paginated public subset: indices, median performance, input/output prices, evaluation total/per-task cost |
| Pro | 500 | Full model list/detail, additional benchmark data, pricing and percentiles |
| Commercial | Custom | Provider detail, time series and negotiated additions |

Quota is shared across keys in the documented user/organisation scope. It is not multiplied by making extra keys. Each catalogue page consumes a request. Page count and size are response metadata, not fixed constants.

Allowlisted response metadata: `X-AA-Tier`, `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, `Retry-After`. The helper saves only these headers, not cookies or authentication headers. On 400/401/403/429, stop; no key/tier guessing or retry loop. On transport/5xx failure, stop the bounded smoke rather than retrying automatically.

Pro list: `GET /language/models?prompt_type=long&page=N`. Pro detail: `GET /language/models/{slug}?prompt_type=medium`. These are documented, not enabled or tested by the Free collector. Provider/time-series endpoints require Commercial; the helper does not call them. Dollar subscription prices have not been verified in this promotion.

## Field mapping

| Compact field | API source |
|---|---|
| ID, slug, name, release date | `id`, `slug`, `name`, `release_date` |
| Creator | `model_creator.name` |
| Intelligence/Coding/Agentic | `evaluations.artificial_analysis_{intelligence,coding,agentic}_index` |
| Input/output $ per million tokens | `pricing.price_1m_{input,output}_tokens` |
| Cache hit/write $ per million | `pricing.price_1m_cache_{hit,write}_tokens`, if present |
| Output tokens per second | `performance.median_output_tokens_per_second` |
| First-token latency, seconds | `performance.median_time_to_first_token_seconds` |
| First-answer-token latency, seconds | `performance.median_time_to_first_answer_token_seconds` |
| End-to-end response, seconds | `performance.median_end_to_end_response_time_seconds` |
| Total evaluation cost, USD | `artificial_analysis_intelligence_index_cost.total_cost` |
| Evaluation cost per task, USD | `artificial_analysis_intelligence_index_cost.cost_per_task.total_cost` |

Missing values remain null. End-to-end timing assumes 500 answer tokens unless documented otherwise. Performance is an aggregated benchmark, not a guarantee for a chosen provider, account or workload.

The API's numeric `intelligence_index_version` carries major.minor, not patch. Official docs currently describe methodology v4.3.2. Retain the actual response version rather than hardcoding it. Compare like-for-like versions/configurations. A current response timestamp is not the date each benchmark was measured.

## Collector contract

`~/agents/ai-models/scripts/model_data.py` uses the standard library only. It caches a complete catalogue for six hours under ignored `ai-models/cache/`, follows strict pagination, checks page/version/tier consistency and duplicate IDs, and replaces caches atomically only after completion. It resolves exact IDs, slugs and names; ambiguity is an error result rather than a substituted model. A missing requested model triggers at most one refresh when using cache. Bare family slugs can still match max exactly: use effort-specific slugs from the favorites registry, never infer effort from a successful match.

Settings: `--model` (repeatable), `--cache`, `--output`, `--ttl-hours` (6), `--max-pages` (10), `--refresh`. Secrets are not settings. Output retains raw entries alongside compact favorite records and request/coverage metadata. No scheduled job or production database is installed.

## Browser and API gaps

Earlier tests found all five requested pages readable in clean Chrome and fresh Firecrawl. Parallel's comparison incorrectly showed Astra for a URL requesting Sol. Always validate model selection before accepting metrics.

Chrome can expand tables and operate observed filters, but export buttons opened a Pro gate. There is no successful authenticated Pro export. The website terms restrict automation; the user explicitly chose to continue bounded public-page tests despite that restriction. Record that distinction without treating it as API rights, permission to bypass access controls, or a claim of unrestricted redistribution.

The Free endpoint excludes detailed benchmarks, token counts, percentiles, context windows, parameters, modalities, licensing and provider detail. Engineering capability scores and coding-agent/harness results are not established by this endpoint. A model database may combine separately labelled public observations and API data; this skill does not assume fields match across those sources.

## Credential entry

Use the setup reference's launcher. It prompts invisibly in a user-owned Terminal, exports the key only for the collector child, then unsets it. It does not persist the key or modify shell profiles or harness settings. A later refresh needs a new entry or an independently configured environment. Never ask the user to paste the key into chat.

## Attribution

Credit [Artificial Analysis](https://artificialanalysis.ai) when displaying API data. Documentation describes attribution across all tiers and separate data-platform terms. No redistribution rights were verified by this task.
