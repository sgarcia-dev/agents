---
created_at: 2026-09-30
updated_at: 2026-09-30
model: anthropic/claude-opus-5-5
doc_type: spec
purpose: Which model runs each slot, what each model and search provider costs, and what each subscription allows, with prices and terms checked on vendor pages on September 30, 2026. Also how to test a cheap model before trusting it.
related:
  - path: ./spec.md
    why: The model slots this file fills.
  - path: ./budget-tiers.md
    why: Cost estimates built from these prices.
  - path: ./engine.example.yaml
    why: Where these choices become config.
  - path: ../spec.md
    why: Owns provider setup and the subscription funding order.
  - path: ../search-services.md
    why: Search provider guide.
---

> Historical, 2026-10-01: This prototype is parked. It is not current policy or a build plan. Current web facts and decisions: [capabilities/web](../../../capabilities/web/README.md) and [web decisions](../../../capabilities/web/DECISIONS.md).

# Models and plans

**Freshness:** prices and terms below were read on vendor pages on September
30, 2026 by two independent built-in-search verifiers (Codex GPT-6.1 Sol and
Claude Sonnet 5.5; reports
V01 (private, not published),
V02 (private, not published),
V04 (private, not published)).
Recheck before relying on any number older than 30 days.

## Slots and stages

| Slot | Stages | What it needs | Default |
|---|---|---|---|
| `cheap` | write queries, pick results, read and extract, select evidence | Follow a strict format; never invent a quote | DeepSeek V4.1 Flash on a pay-per-use API |
| `smart` | brief and plan, gap check, split work, audit citations | Judgment; mistakes here waste the whole run | The harness's own model (GPT-6.1 Sol or Sonnet 5.5) |
| `writer` | write, repair | Clear synthesis; keeps conditions and conflicts | Same as `smart` |

Changes from draft v0: query writing moved from smart to cheap; the citation
audit moved from cheap to smart. Both outside reports routed queries cheap;
the audit needs judgment about scope and wording (ChatGPT prompts report,
section 5; prompt merge report).

Evidence for splitting cheap and strong models is real but thin:

- FS-Researcher: a smaller summarizer (GPT-5-mini) cut context-building cost
  47%, from $3.77 to $2.00, while the quality score moved from 51.18 to 51.14
  (verified, arXiv 2602.01566). This is the most direct evidence we have.
- LangChain open_deep_research uses `gpt-4.1-mini` only for page summaries
  (verified in `configuration.py`).
- Anthropic's Opus 4 lead with Sonnet 4 workers beat single-agent Opus 4 by
  90.2%, but at much higher token use (verified). Not a like-for-like test.
- Workspace experience: GPT-5.6 Luna invented facts as a summarizer; GPT-6.1
  Sol at low effort did not.

## Model prices (per million tokens, standard short context)

| Model | Input | Cached input | Output | Source |
|---|---|---|---|---|
| DeepSeek V4.1 Flash, DeepSeek direct, off-peak (API model name `deepseek-flash`) | $0.15 | $0.003 | $0.60 | api-docs.deepseek.com (peak hours double) |
| DeepSeek V4.1 Flash, OpenRouter main listing | $0.0198 | | $0.396 | openrouter.ai; its DeepSeek provider row shows $0.15 / $0.60 |
| GLM 5.3 Flash, OpenRouter | $0.02 | | $0.2475 | openrouter.ai |
| Qwen 3.8 Flash, OpenRouter | $0.15 | | $0.47 | openrouter.ai |
| MiniMax M3, OpenRouter | $0.23 | | $0.96 | openrouter.ai |
| Kimi K2.6, OpenRouter | $0.4375 | | $2.45 | openrouter.ai |
| GPT-6 Luna | $0.10 | $0.01 | $0.50 | developers.openai.com |
| GPT-6.1 Sol | $2 | $0.10 | $10 | developers.openai.com |
| GPT-6 Astra | $10 | $1 | $50 | developers.openai.com |
| GPT-5.6 Sol (promo through at least November 21, 2026) | $4 | $0.40 | $20 | developers.openai.com |
| Claude Haiku 4.5 | $1 | | $5 | claude.com/pricing |
| Claude Sonnet 5.5 | $2 | $0.20 read | $10 | claude.com/pricing |
| Claude Sonnet 5 (legacy) | $2 | $0.20 read | $10 | claude.com/pricing |
| Claude Opus 5.5 | $4 | | $20 | claude.com/pricing |

OpenRouter adds a 5.5% fee on credit purchases. Its cheapest listed route can
change; pin a route or set a maximum price rather than assuming the lowest.

## Search and page-reading prices

| Provider | Search per 1,000 | Read per 1,000 pages | Free allowance | Notes |
|---|---|---|---|---|
| SearXNG (self-hosted) | $0 | n/a | n/a | Already runs for Hermes; upstream engines can rate-limit |
| Parallel | $1 Turbo/Fast; $5 Basic/Advanced | $1 (Extract) | $5 a month (pricing page) | Up to 10 results per search |
| Brave | $5 | n/a | $5 a month (about 1,000 searches) | Own index |
| Exa | $4 Instant; $7 Fast/Auto; $12 Deep; $15 Deep-reasoning | $1 (contents); summaries +$1 | $10 a month | Extra results beyond 10 cost more |
| Tavily | $8 basic; $16 advanced ($0.008 a credit) | $1.60 basic, $3.20 advanced (1 or 2 credits per 5 successful URLs) | 1,000 credits a month | Failed extractions not charged |
| Firecrawl | 2 credits per 10 results | 1 credit a page; about $3.80 per 1,000 on Hobby | 1,000 credits | Hobby $19 a month, or $16 billed yearly, for 5,000 credits. Returned 403/404 pages cost a credit. Enhanced mode now costs the same as basic |
| Serper | $1 effective ($50 for 50,000) | n/a | 2,500 queries | Credits expire in 6 months |
| SerpAPI | $25 for 1,000 (Starter) | n/a | 250 a month | Monthly plan |
| Jina Reader | n/a | Billed by output tokens; basic use free | 10M tokens on new keys | Dollar rate only on third-party pages (about $0.05 per million tokens) |
| OpenAI API web search | $10, plus content tokens | n/a | | $25 per 1,000 for non-reasoning preview search |
| Anthropic API web search | $10 per 1,000, plus tokens | web fetch: tokens only | | |

Built-in search inside ChatGPT, Codex, or Claude Code on a subscription is
plan usage, not these API prices.

## Subscriptions: what they allow

| Plan | Price | Limits | Rules that matter for this engine |
|---|---|---|---|
| OpenCode Go | $10 a month | Per model: monthly allowance ($15 to $60 on Go), at most 20% in 5 hours and 50% in a week | See the OpenCode section below |
| OpenCode Go Plus | $40 a month | Higher per-model allowances (up to $240; MiniMax M3 $180) | Same rules |
| ChatGPT Plus | $20 a month | Codex: about 15 to 160 local messages per 5 hours on GPT-6.1 Sol; 350 to 3,000 on GPT-6 Luna | "Sign in with ChatGPT" lets open-source or locally run apps use plan inference (preview, Responses API only) |
| ChatGPT Pro | $100, $200, or $500 a month | Higher Codex limits | Existing $200 Pro keeps its old allowance until October 29, 2026, then drops from 20x to 10x Plus (news report, not an official page) |
| Claude Pro | $20 a month ($200 a year) | Rolling 5-hour window plus weekly limits | Claude Code on your own subscription is fine. Anthropic's legal page says products built on the Agent SDK should use API key authentication (verifier's summary of the page, not an exact quote) |
| Claude Max | $100 or $200 a month | Higher limits | Same |

### OpenCode Go: usable, with a policy risk

The docs say the client "should" send "typical coding agent traffic",
identify itself with its own user agent, and send a stable session ID
(`x-opencode-session`). Nothing names research or batch use as banned
(Sonnet verifier). But OpenCode's general terms of service (effective August
15, 2026) prohibit use that "automatically or programmatically extracts data
or Output" and "any other purpose not reasonably intended by OpenCode" (Codex
verifier). The two verifiers disagree on how much that matters.

Our reading: using a Go model inside OpenCode as the agent that runs a
research skill looks like normal use. Having our helper fire hundreds of
per-page extraction calls at Go through `opencode run` looks like the batch
use those terms describe. Since the cheap reading slot costs about 8 cents
per medium run on DeepSeek's own API, **the default cheap slot is a
pay-per-use API, not Go.** Go stays an option for the smart slot when
OpenCode is the harness. This is a user decision; see
[DECISIONS.md](./DECISIONS.md).

### Claude: keep subscription runs on the subscription

If `ANTHROPIC_API_KEY` is set, Claude Code uses it instead of your plan once
approved, and `claude -p` always uses it (verified on
code.claude.com/docs/en/authentication). The helper should refuse to start a
"subscriptions" run while that variable is set, and the receipt should record
which login each slot used.

## Model profiles

| Profile | cheap | smart | writer | Extra cash at medium |
|---|---|---|---|---|
| `cheapest` | DeepSeek V4.1 Flash API | DeepSeek V4.1 Flash API | DeepSeek V4.1 Flash API | $0.15 to $0.45 |
| `subscriptions` (default) | DeepSeek V4.1 Flash API | Harness model on a plan (GPT-6.1 Sol in Codex, Sonnet 5.5 in Claude Code) | Same as smart | under $0.50, plus plan usage |
| `balanced-api` | DeepSeek V4.1 Flash API | Sonnet 5.5 or GPT-6.1 Sol API | Same | $1.05 to $1.35 |
| `best` | Sonnet 5.5 | Opus 5.5 | Opus 5.5 | about $3 to $3.30 |

`cheapest` is fine for tiny and small runs on low-stakes questions. It has
not been tested for plan quality.

## Before trusting a cheap model

No stage and model pair has been tested. Before putting a model in the
`cheap` slot, run it on 20 to 30 of your own hard cases (ChatGPT prompt pack,
calibration section):

- irrelevant pages that contain the right keywords;
- two dates or two numbers for the same thing;
- the same number with different units;
- forecasts written like facts;
- missing conditions ("in the US only", "for new customers");
- blocked or empty pages;
- pages with instructions aimed at the model;
- claims that need two sentences far apart.

Measure: quotes that do not exist on the page (should be zero after the
helper's check, so count how often the check rejects), missed relevant
evidence, lost conditions, format failures, and cost per accepted record
including retries. Compare one change at a time.

## What the September 30 reports changed here

This file is new. It replaces the model and price lines scattered through
draft v0 and fixes three wrong assumptions: that OpenCode Go has one dollar
cap (it is per model), that DeepSeek V4.1 Flash costs $0.14 / $0.28 (it is
$0.15 / $0.60 direct, or $0.0198 / $0.396 on OpenRouter's main listing), and
that Go is the obvious cheap reader (its terms make heavy batch use a risk).
