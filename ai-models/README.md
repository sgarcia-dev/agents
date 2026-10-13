---
created_at: 2026-09-30
updated_at: 2026-10-13
doc_type: index
purpose: Human and agent entrypoint for model comparisons and their collection process.
related:
  - path: ./STATE.md
    why: Current coverage, gaps and next action after compaction.
  - path: ./data/2026-09-30/TABLE.md
    why: Human-readable master comparison generated from the data. (raw data not published)
  - path: ./collection/README.md
    why: Efficient retrieval and maintenance, separate from reading the numbers.
---

# AI models

This is the permanent home for the owner's model data, selection preferences,
collection tools, lessons and supporting evidence. The owner explicitly chose
this top-level root. Research reports and Downloads are no longer working inputs.

## Two entry points

| I want to… | Start here |
|---|---|
| Compare models | `data/2026-09-30/TABLE.md` (raw data not published) |
| Read exact machine-readable numbers | `data/2026-09-30/favorites.snapshot.json` (raw data not published) |
| Query one favorite | Run the command below |
| Add a model or reasoning level | [Collection guide](collection/README.md) |
| Improve collection speed or reliability | [Lessons and shortcuts](collection/LEARNINGS.md) |
| Compare local document-tailoring quality, cost and time | Two-role pilot (report private, not published), Claude comparison (report private, not published) |
| Choose another benchmark | [Benchmark follow-ups](collection/benchmark-backlog.md) |
| Resume after compaction | [Current state](STATE.md) |
| Check evidence and trust limits | [Sources](SOURCES.md) |

```bash
python3 ~/agents/ai-models/scripts/query_snapshot.py --model sol
python3 ~/agents/ai-models/scripts/query_snapshot.py --model luna --effort xhigh
```

Default effort is **medium**, explicitly configured in `favorites.json`
(Haiku 5.5 defaults to high). Other aliases are `opus`, `sonnet`, `haiku` and `luna`. Unsupported configurations fail;
there is no silent max, high, provider or model substitution.

## Where each model comes from

Know this before picking a model. It decides which harness to call it from.

| Models | Paid through | Best harness | Also works in |
|---|---|---|---|
| GPT-class (Sol, Luna) | OpenAI subscription, $100 tier | Codex | OpenCode, Hermes Agent |
| Claude (Opus, Sonnet, Haiku) | Anthropic Claude Max, $100 tier | Claude Code | OpenCode, but only temporarily; call it from Claude Code |
| OpenCode Go models (MiMo, DeepSeek, GLM, Qwen, Kimi, Muse Spark) | OpenCode subscription, $10 a month | OpenCode | Hermes Agent |
| Gemini 3.8 Flash | Google AI subscription | Gemini (`agy`) | |
| Any of the non-GPT, non-Claude models | OpenRouter, billed per API token | OpenCode | |

- The $10 OpenCode subscription covers all the non-GPT, non-Claude models, but
  because it is only $10 it is best spent on the cheaper ones.
- OpenRouter is pay per token, so heavy use of an expensive model there costs
  real money. Prefer the flat-fee plans first.
- Gemini runs through the owner's Google AI subscription in Gemini (Antigravity CLI / `agy`). Gemini 3.8 Flash is its only usable model. All other models accessible in Gemini are abysmally bad: the Gemini Pro series defaults to 3.1, which is ancient, and older Flash versions like 3.7 are obsolete. Gemini 4 will require separate benchmark tests and workspace indexing when released.
- OpenCode Go is best used through OpenCode, which acts as its adapter.
- Hermes Agent, another harness, supports the GPT models and the OpenCode Go
  models.

Which model every worker, orchestrator and bridge uses, with each model's trade-offs (read before delegating): [delegation-briefing.md](delegation-briefing.md).
OpenCode Go plan limits: [opencode-go-limits.md](opencode-go-limits.md).
Which model for which job (value, reliability, sensitive work): [SELECTION.md](SELECTION.md).
Where each model's reasoning-effort sweet spot is (Haiku, Sonnet, Opus 5.5, GPT-6.1 Sol): [EFFORTS.md](EFFORTS.md).

## Current coverage

Snapshot date: **September 30, 2026**, not a live feed. On October 7 the
website (not the API) added Claude Haiku 5.5, refreshed every Sonnet 5.5 effort,
and added Opus 5.5 high/xhigh/max, GPT-6.1 Sol xhigh/max and both GPT Luna
families at every effort including max (marked `*`).

| Favorite | Default | Also selected | Important gap |
|---|---|---|---|
| GPT-6.1 Sol | medium | low, high, xhigh*, max* | Actual wall-clock task time unknown |
| GPT-6 Luna | medium | low, high, xhigh, max (all Oct 7*) | Re-scored up 0.4 to 0.8 on Oct 7; recall falls past about 128K tokens |
| Claude Opus 5.5 | medium | low, high*, xhigh*, max* | Adaptive reasoning with default fallback |
| Claude Sonnet 5.5 | medium | low, high, xhigh, max (all Oct 7*) | Refreshed Oct 7: low now scored, new $0.10 cache price |
| Claude Haiku 5.5 | high | low, medium, xhigh, max | Website-only; AA costs ignore the 5x price above 100K-token prompts |
| GPT-6 Sol | (none set) | low, medium | Separate from GPT-6.1 Sol |
| GPT-5.6 Luna | high | low, medium, xhigh, max (all Oct 7*) | Separate from GPT-6 Luna |
| MiMo V2.6 Flash, DeepSeek V4.1 Flash, GLM 5.3 Flash, Qwen 3.8 Flash (`qwen3-8-flash-next`) | provider default | none | OpenCode Go set; defaults, not chosen levels |
| Muse Spark 1.3 | xhigh | none | |
| GLM 5.3, Qwen 3.8 Max, MiMo V2.6 Pro, Kimi K3 | provider default | none | Single default entries |

Captured: Intelligence Index; AutomationBench-AA; Terminal-Bench 4.0;
AA-Omniscience and accuracy/hallucination subfields; GDP.pdf; AA-LCR; AA-Briefcase; token prices;
index costs; total and per-task output tokens; speed; decode-time estimates.
Full original model objects retain extra fields and evaluation breakdowns.

**Do not confuse these numbers:** task time is estimated decode time, not elapsed
agent task completion. Hallucination rate is conditional on non-correct responses,
not the percentage of all questions answered incorrectly. Cost/task is an index
benchmark average, not a promised budget for the owner's tasks.

## Layout

- `favorites.json`: model aliases, exact configuration UUIDs/slugs and defaults.
- `benchmarks.json`: metric definitions, units, source keys and extension slots.
- `data/<date>/`: curated JSON, generated master table and validation results (raw data not published).
- `sources/<date>/`: complete reusable source payloads, including all 686 API rows (raw data not published).
- `collection/`: retrieval procedure, API setup and practical lessons.
- `scripts/`: standard-library tools; no service or database dependency.
- `evidence/<date>/`: archived original experiments and reader evidence (raw data not published).
- `cache/`: ignored staging/cache for future refreshes, never the API key.

Querying or rebuilding the current snapshot is offline. No scheduler or website
refresh bot is installed. Original Downloads and research artifacts remain as
historical copies, but this folder contains everything needed for normal use.
