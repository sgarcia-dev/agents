---
created_at: 2026-09-30
updated_at: 2026-09-30
model: anthropic/claude-opus-5-5
doc_type: spec
purpose: The size dial for the engine. Tier presets, the two hard limits (searches and extra cash), how numbers are derived, a fill-in cost formula, and per-tier cost estimates recomputed from prices verified on September 30, 2026. All costs are estimates until real run receipts exist.
related:
  - path: ./spec.md
    why: The engine these tiers size.
  - path: ./engine.example.yaml
    why: Where tier numbers and prices live as config.
  - path: ./models-and-plans.md
    why: Model prices and subscription limits used below.
  - path: ./ARCHITECTURE.md
    why: What the helper counts and enforces.
  - path: ../search-services.md
    why: Search provider guide.
  - path: ../fetch-services.md
    why: Page-reading provider guide.
---

> Historical, 2026-10-01: This prototype is parked. It is not current policy or a build plan. Current web facts and decisions: [capabilities/web](../../../capabilities/web/README.md) and [web decisions](../../../capabilities/web/DECISIONS.md).

# Budget tiers

**Everything priced here is an estimate.** Prices were checked on vendor
pages on September 30, 2026
(V01 (private, not published),
V02 (private, not published)).
Token counts are our assumptions, not measurements. Replace them with run
receipts as soon as runs exist.

## Two hard limits on every run

1. **Max searches.** The main dial. It sets how much the run explores.
2. **Max extra cash** (`max_usd`). Money spent beyond flat-fee plans: paid
   search, paid page reading, and pay-per-use model calls. Default **$1**.
   A subscription never spills over into paid API use without asking.

Both limits are enforced by the helper, not by a prompt. The ChatGPT cost
report makes the case for two separate limits: searches bound exploration,
cash bounds everything else (retries, long reasoning, repeated context).

Everything else (reads, rounds, workers) follows from the tier unless you
override it. Any number is accepted: "medium, but 30 searches" or "17
searches" both work. Tiers are presets, not a menu.

## The five tiers

| Tier | Searches | Page reads | Rounds | Sub-questions | Workers | Good for |
|---|---|---|---|---|---|---|
| tiny | 5 | 6 | 1 | 1 | 0 | One fact, a quick check |
| small | 12 | 15 | 2 | 2-3 | 0 | A short cited answer |
| medium | 50 | 60 | 3 | 4-6 | 0-2 | A real report on one topic |
| large | 200 | 240 | 5 | 10-15 | 2-4 | A broad comparison or market scan |
| xl | 500 | 600 | 6 | 20-30 | 4-6 | Rare, high-value questions only |

All caps are ceilings. A large run should still stop after 40 searches if
the question is answered.

**Key research rule.** For research that matters, do not starve it: about 15
searches and 20 to 30 page reads is the floor (user preference, September
30). That is "small, with searches raised to 15 and reads to 25", or a
small medium.

How these compare with the outside proposals (all were estimates too):

| Tier | Draft v0 | ChatGPT cost report | Claude report | This version |
|---|---|---|---|---|
| tiny | 5 / 5 | 3 / 4 | 3-5 / 3-5 | 5 / 6 |
| small | 12 / 15 | 10 / 12 | ~10 / 10-15 | 12 / 15 |
| medium | 50 / 60 | 50 / 60 | ~50 / ~60 | 50 / 60 |
| large | 200 / 200 | 150 / 180 | ~300 / ~300 | 200 / 240 |
| xl | 500 / 500 | 300 / 400 | ~1,000 / ~1,000 | 500 / 600 |

(searches / reads). Kept close to the user's original ask: tiny under 5,
small about 10, medium about 50, large 200 and up. Workers dropped from 3-5
at large to 2-4, because every source says to bias toward one loop and the
Claude report's own advice caps sub-agents at 5.

## How the numbers relate

- **Reads = about 1.2 x searches.** The best measured ratio we have is
  FS-Researcher's: 28.6 searches to 32.4 page reads at 3 rounds, 66 to 58 at
  10 rounds (verified (private, not published)).
  Read attempts count, including failures: Firecrawl bills a returned 403 or
  404 page (verified).
- **Stop exploring at 80% of any cap.** The last 20% goes to select, write,
  audit, and repair, so a run never ends with notes but no report. Jina uses
  85% ("regularBudget = tokenBudget * 0.85", verified in code); both ChatGPT
  reports suggest reserving about 20%. Draft v0 said 15%.
- **Straightforward questions** (one fact) use at most the tiny budget even
  inside a bigger tier (Claude report, P1).
- **Workers share one budget.** The helper reserves each worker's share up
  front and releases what it does not use.

## Where the money goes

Three buckets, and the third one surprised us:

1. **Tools:** searches and page reads. Cheap. $0 with SearXNG and our own
   fetch; $1 per 1,000 for Parallel Fast search or Parallel Extract; $5 per
   1,000 for Brave or Parallel Basic.
2. **Work tokens:** the stage calls themselves (reading pages, planning,
   writing, auditing). The cheap reading slot is most of the volume.
3. **Harness overhead:** when the smart model runs as an agent inside Claude
   Code, Codex, OpenCode, or Hermes, every turn resends the whole
   conversation. A medium run is about 26 agent turns with 20k to 60k of
   context each, about 1.5M input tokens. On a pay-per-use API this is the
   biggest line unless prompt caching works. Cache reads cost 10% of input
   on Anthropic (Sonnet 5.5: $0.20 vs $2 per million) and 5% on OpenAI
   (GPT-6.1 Sol: $0.10 vs $2), both verified. The estimates below assume 90%
   of harness input is a cache hit at 10%, so harness input costs about 19%
   of the full price. Cache writes are ignored.

What this means for design:

- **The cheap reading slot is nearly free on a pay-per-use API.** DeepSeek
  V4.1 Flash direct is $0.15 in and $0.60 out per million (off-peak). A
  medium run's 370k reading tokens cost about 8 cents. There is little reason
  to push this volume through a subscription.
- **The smart slot is where a subscription pays off,** because that is where
  harness overhead lands. On ChatGPT, Codex, or Claude plans it costs plan
  usage, not dollars.

## Cost estimates per run

Pay-per-use prices, one run, including tools at $0 to $5 per 1,000 searches
and $0 to $1 per 1,000 reads, and harness overhead **with prompt caching
working**. Without caching, add about 4x the "harness" part (see the note
below the table).

| Tier | All cheap (DeepSeek V4.1 Flash everywhere) | Balanced (cheap reader, Sonnet 5.5 or GPT-6.1 Sol for smart and writer) | Frontier (Sonnet 5.5 everywhere) |
|---|---|---|---|
| tiny | $0.02 to $0.05 | $0.15 to $0.20 | $0.25 to $0.30 |
| small | $0.04 to $0.10 | $0.35 to $0.45 | $0.65 to $0.70 |
| medium | $0.15 to $0.45 | $1.05 to $1.35 | $2.00 to $2.30 |
| large | $0.50 to $1.75 | $3.10 to $4.40 | $7.00 to $8.25 |
| xl | $1.05 to $4.15 | $5.25 to $8.35 | $15 to $18 |

Without caching, the balanced medium run is about $3.50 to $3.80; the balanced
large run about $11 to $12. Opus 5.5 ($4 / $20) for smart and writer costs
about the same as Sonnet in every slot at medium, and about double balanced.

**On subscriptions** ("subscriptions" profile: cheap slot on a pay-per-use
API, smart and writer on a ChatGPT or Claude plan): extra cash is only tools
plus cheap reading, so under **$0.50 for medium** and under $2 for large. The
real cost is plan usage, about 26 agent turns for medium and 50 for large.
How many runs fit in one 5-hour window is unknown until measured.

Sanity checks against measured runs (not our design, different models):

- LangChain open_deep_research, 100-task benchmark: $45.98 and 58M tokens
  total at default settings, about $0.46 and 580k tokens per task (verified,
  README table). Its submission config: $87.83, about $0.88 per task.
- Google Gemini Deep Research standard: about 80 queries, 250k input and 60k
  output tokens, "$1-3" per task; Max: up to about 160 queries, $3 to $7
  (Google's own preview estimates, verified).
- FS-Researcher with GPT-5: $6.10 model cost per question at 3 rounds, $12.54
  at 10 rounds (verified).

Our balanced medium ($1.05 to $1.35) sits between LangChain's default and
Gemini's standard run, which is where we would expect it.

## Cost formula

For one run:

```text
cost =  searches x search_price
      + read_attempts x read_price
      + sum over slots (cheap, smart, writer):
          (uncached_in x in_price + cache_read x cache_price
           + cache_write x write_price + out x out_price) / 1,000,000
      + platform fees (OpenRouter: 5.5% on credit purchases, verified)
```

Token assumptions per call (estimates; replace with receipts):

| Call | Slot | Input | Output | Count per run |
|---|---|---|---|---|
| Read one page chunk | cheap | 4,000 | 400 | page reads |
| Write queries | cheap | 2,000 | 200 | sub-questions x rounds |
| Pick results | cheap | 1,500 | 50 | searches |
| Select evidence | cheap | 300 per page read + 1,000 | 300 | 1 |
| Brief and plan | smart | 3,000 | 1,500 | 1 |
| Gap check | smart | 3,000 + evidence so far | 1,000 | rounds |
| Audit | smart | report + 500 per checked claim | 80 per claim | 1 |
| Write | writer | 3,000 + evidence (capped at 60k) | 1.4 x words | 1 |
| Harness turns | smart | 20k base + 1.5k per turn | small | about 1 + rounds x (open sub-questions + 1) + 4 |

Two reasons real runs may cost more than this table: reasoning tokens (one
documented run had 89% of its output as hidden reasoning, per the ChatGPT
cost report), and long pages if the helper does not trim them.

The script behind these numbers is simple arithmetic; any agent can redo it
from this table.

## Plans and caps that change the math

Short version here; details and sources in
[models-and-plans.md](./models-and-plans.md).

- **OpenCode Go** ($10 a month; Go Plus $40): limits are per model, not one
  dollar pool. Each model has a monthly allowance (for example $60 for
  DeepSeek V4.1 Flash, $15 for Kimi K3 and GPT-5.6 Luna), with at most 20% of
  it in any 5 hours and 50% in any week (verified on opencode.ai/docs/go,
  updated September 29, 2026). The Claude report's "$12 per 5 hours, $30 per
  week, $60 per month" is just the numbers for a $60 model.
- **ChatGPT Plus** ($20): Codex allows about 15 to 160 local messages per 5
  hours on GPT-6.1 Sol (verified). A message is not a research run.
- **Claude Pro and Max:** rolling 5-hour and weekly limits, no public
  conversion to runs. An `ANTHROPIC_API_KEY` in the environment makes Claude
  Code bill the API instead of the plan; in `claude -p` it always does
  (verified). The helper must refuse to start a "subscriptions" run when that
  key is set.

## Warning signs during a run

Suggested alarms, not proven thresholds (ChatGPT cost report, section 11).
The helper can compute all of them from its own counters.

| Sign | Alarm | Response |
|---|---|---|
| Repeat searches or reads | Over 30% of recent attempts | Check dedupe and worker scopes |
| Blocked, empty, or off-topic pages | Over 20% of recent reads | Change provider or route |
| No new supported item | 2 rounds in a row | Stop, or switch to checking key claims |
| Input tokens rise, evidence does not | Rising tokens per call | Prune context |
| 80% of a cap spent, no outline | At the 80% floor | Write in limited mode |

## What to measure first

1. Real tokens per page read and per harness turn on tiny and small runs.
2. Harness overhead with and without prompt caching, same small run.
3. How many medium runs fit in one 5-hour window on each subscription.
4. Where quality stops improving: 10 real questions at small and medium,
   judged without knowing the budget (ChatGPT cost report, section 3). Promote
   only the questions that improve to large.

## What the September 30 reports changed here

- Added the second hard limit (extra cash) and the 80% exploration floor.
- Added harness overhead as its own cost bucket. Draft v0 only warned about it.
- Replaced secondary-source prices with vendor-page prices. DeepSeek V4.1
  Flash is $0.0198 / $0.396 on OpenRouter's main listing and $0.15 / $0.60 from
  DeepSeek directly; draft v0 used $0.14 / $0.28 from a secondary page.
- Large and xl reads raised to 1.2x searches; worker counts lowered.

What did not change: the main dial is still max searches, the medium tier is
still 50 searches and 60 reads, and the balanced medium estimate moved only
from "$0.35 to $0.60 before overhead" to "$1.05 to $1.35 with overhead".
