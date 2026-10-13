---
doc_type: guide
updated_at: 2026-10-07
purpose: Which model to use for which job, by value and by reliability.
related:
  - path: ./README.md
    why: Where each model comes from and which harness to call it from.
  - path: ./data/2026-09-30/VALUE.md
    why: Generated value table (points per dollar). Numbers come from there. (raw data not published)
  - path: ./data/2026-09-30/TABLE.md
    why: Source numbers for hallucination, Omniscience and speed. (raw data not published)
  - path: ./evidence/2026-10-07/codex-effort-levels.md
    why: Non-AA effort evidence for Claude Haiku 5.5 (Anthropic, CursorBench, system card). (raw data not published)
  - path: ./evidence/2026-10-07/codex-vs-sonnet-luna.md
    why: Launch-day Haiku 5.5 vs Sonnet 5.5 vs GPT-6 Luna comparison and anecdotes. (raw data not published)
  - path: ./evidence/2026-10-07/codex-luna-long-context.md
    why: Long-context and long-run audit of both Lunas and Haiku 5.5. (raw data not published)
  - path: ./evidence/2026-10-07/codex-luna-vs-haiku-efforts.md
    why: Haiku 5.5 vs GPT-6 Luna vs GPT-5.6 Luna, effort by effort and at matched spend. (raw data not published)
  - path: ./evidence/2026-10-07/codex-cheap-to-big-jump.md
    why: What moving from Haiku or Luna up to Sonnet 5.5 or GPT-6.1 Sol buys. (raw data not published)
---

# Choosing a model

Numbers are from the September 30, 2026 snapshot. Check `README.md` first for
which subscription and harness each model needs.

## Value: intelligence per dollar

Artificial Analysis does not publish one "intelligence per dollar" number. It
publishes charts of Intelligence Index against cost per task and cost to run the
index. We already have both inputs, so we divide them ourselves with no new
calls. `scripts/value_ratings.py` writes `data/2026-09-30/VALUE.md`.

- Cheapest per intelligence point: the Luna models (GPT-6 Luna low is far ahead),
  then MiMo V2.6 Flash and MiMo V2.6 Pro.
- Expensive for what they score: Qwen 3.8 Max, Kimi K3, GLM 5.3, Muse Spark.
- Sonnet 5.5 rows were refreshed on October 7 (new cache price; low now has a score).
- This is a value guide, not a quality ranking. A cheap model that is wrong
  often is not good value for careful work. Token-heavy models cost more per task
  than their price per million tokens suggests.

## Reliability for careful work

Hallucination rate here is the share of non-correct answers that were guesses
instead of "I don't know". Lower is safer. Omniscience above zero means more
right than wrong. The table has no test of spec reading or reconciliation, so
treat this as a proxy.

**Safe for delicate work (artifacts, reconciliation, reading specs)**

- GLM 5.3 Flash: hallucination 27.6%, Omniscience +7.5. Very slow but careful.
- GLM 5.3: 29.6%, +14.3.
- Qwen 3.8 Max: 28.8%, +12.0. Honest but slow and expensive.
- Muse Spark 1.3 (xhigh): 31.5%, +23.1, fast. Better than "in between": it has the
  best mix of accuracy, honesty and speed among the OpenCode set.
- MiMo V2.6 Pro: 40.6%, +8.4, strong long-document score.

**Usable, but check the output**

- Claude Haiku 5.5: 44% at every effort except max (40%), Omniscience +3 to +11.
  Guesses less than Sonnet, Opus, Sol and Gemini, but knows less.
- GPT-6 Sol and GPT-6.1 Sol, Kimi K3, Claude Sonnet 5.5: hallucination above 50%
  but positive Omniscience, so they know a lot and still guess when wrong.
- Qwen 3.8 Flash: 45.3%, Omniscience negative.
- MiMo V2.6 Flash: 54.4%, Omniscience negative, very slow.

**Avoid for delicate work**

- DeepSeek V4.1 Flash: hallucination 96.5%. Fast and reckless. Fine for quick
  throwaway work, never for artifacts or reconciliation.
- GPT-6 Luna and GPT-5.6 Luna: hallucination 77% to 93%, Omniscience about zero or
  negative.
  Great value for simple bulk tasks, not for anything that must be right.

## Best for long, delicate work

Ranked by hallucination rate (lower is better), with knowledge (Omniscience) and
long-document score (AA-LCR) beside it. Hallucination is the share of wrong
answers that were guesses. The Claude, GPT and Gemini models are not low on it:
they know a lot but guess about half the time, so their output needs checking.

| Model | Hallucination | Omniscience | AA-LCR | Note |
|---|---:|---:|---:|---|
| GLM 5.3 Flash | 27.6% | +7.5 | 80.0% | Lowest guessing, slow, cheap |
| Qwen 3.8 Max | 28.8% | +12.0 | 80.3% | Honest, slow, expensive |
| GLM 5.3 | 29.6% | +14.3 | 79.7% | Best honest model with more knowledge |
| Muse Spark 1.3 | 31.5% | +23.1 | 83.0% | Fast. Public material only |
| MiMo V2.6 Pro | 40.6% | +8.4 | 86.3% | Cheap, strong long reading |
| Claude Haiku 5.5 xhigh | 44.4% | +6.1 | 78.3% | Cheapest Claude; October 7 website data |
| Claude Sonnet 5.5 medium | 51.2% | +20.1 | 76.3% | High guesses more: 64.6% |
| Gemini 3.8 Flash medium | 51.9% | +28.6 | 84.0% | Fast, decent knowledge |
| GPT-6.1 Sol medium | 51.6% | +40.0 | 83.3% | Most knowledge, sluggish in practice |
| Claude Opus 5.5 medium | 68.4% | +40.3 | 84.3% | Knows most, guesses most of the big models |

Suggested pick: GLM 5.3 (or GLM 5.3 Flash to save money) when it must not make
things up. GPT-6.1 Sol medium when depth matters and you will verify. Opus and
Sonnet do not stand out on this measure. The earlier guess that Claude and Sol
hallucinate very little is not supported by these numbers.

Speed caveat: Artificial Analysis speeds are API speeds. On a Codex subscription the Sol
models run about 3 to 4 times slower. See
[subscription-speed.md](subscription-speed.md).

## Claude Haiku 5.5 (added October 7, 2026)

Released October 7. The cheapest Claude by far: $0.10 in and $0.50 out per
million tokens, a tenth of Haiku 4.5 and a twentieth of Sonnet 5.5. Runs in
Claude Code on the Max plan (`/model claude-haiku-5-5`). 1M context, 128K
output, efforts low to max, **API and Claude Code default is medium**.

All five efforts are in the data as website-only rows (`*` in the tables),
captured October 7 without an API refresh. Raw evidence from Anthropic, Cursor
and early users is in `evidence/2026-10-07/`.

### Effort: high is the sweet spot

Full curves and evidence are in
[`EFFORTS.md`](EFFORTS.md). Summary:

- **Default high.** It beats Sonnet 5.5 medium on CursorBench (42.3% vs 39.2%)
  for under half the cost, is where broad research stops collapsing (WANDR
  12.9% at medium, 37.3% at high), and is Anthropic's pick for strict
  instruction following.
- **medium** for narrow lookups and extraction. **low** only for routing.
- **xhigh** for hard coding or agent tasks with short context. It is the AA
  value knee (41.2, matching Sonnet medium), but it waits about 87 s before
  visible text and can end a reply inside hidden thinking.
- **Never max.** Seven-minute wait, flat agent scores.
- Revised the same day: the first pass picked xhigh from the AA curve alone.
  Cognition's FrontierCode, Cursor, the system card's research curves and the
  latency cost moved it to high.

### Against the models we already use

| | Haiku 5.5 high | Haiku 5.5 xhigh | Sonnet 5.5 medium | Sonnet 5.5 high | Opus 5.5 low | GPT-6 Luna xhigh | GPT-6.1 Sol low | GLM 5.3 Flash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Intelligence | 37.8 | 41.2 | 40.8 | 46.8 | 42.3 | 34.6 | 42.1 | 41.8 |
| USD per task | 0.08 | 0.12 | 0.48 | 0.88 | 0.55 | 0.04 | 0.13 | 0.25 |
| CursorBench | 42.3% | 44.3% | 39.2% | 47.8% | 43.7% | | | |
| Terminal-Bench | 21.7% | 29.3% | 29.8% | 43.9% | 31.3% | 8.1% | 30.8% | 32.8% |
| Hallucination | 45% | 44% | 51% | 65% | 68% | 82% | 52% | 28% |
| Wait before first text | 26 s | 87 s | 4.5 s | 12 s | 13 s | 27 s | 2.4 s | 3.3 s |

AA numbers, Sonnet refreshed October 7. CursorBench is Cursor's independent
coding test at October 7 prices.

- **vs Sonnet 5.5 medium:** Haiku high codes better on CursorBench and guesses
  less, for about a sixth of the AA price on short tasks. Sonnet starts faster,
  reads files more faithfully (system card), handles multi-step tool workflows
  far better (AutomationBench 55% vs 34%), and is cheaper on long agent runs.
- **vs GPT-6 Luna:** same token prices below 100K. Haiku is far stronger on
  terminal and computer-use work and guesses much less. Luna knows more facts
  and is better at multi-step tool workflows. Full audit in the next section.
- **vs GLM 5.3 Flash:** about the same intelligence at xhigh. GLM guesses less
  (28%); Haiku is four times faster per token and on a different budget.

### Gotchas

- **Prompts over 100K tokens cost 5 times more**: $0.50 in, $2.50 out, $0.05
  cache reads. AA priced every Haiku token at the short rate, so its costs are
  too low for long agent runs. Anthropic's own Terminal-Bench chart, with the
  real rates, puts Haiku xhigh at $1.75 per attempt against Sonnet medium at
  $0.68. Long Claude Code sessions cross 100K easily. Treat Haiku as cheap only
  for short-context work.
- **Sonnet 5.5 cache reads dropped to $0.10 on October 7** (from $0.20). The
  Sonnet rows were refreshed the same day, so the tables include it.
- On the Claude Max plan, how much quota Haiku uses relative to Sonnet is not
  published. Anthropic only says it uses less. Do not assume 20 times less.
- The same text counts as about 30% more tokens than on Haiku 4.5.
- Thinking is on by default and counts toward `max_tokens`. A small cap can
  end the reply with no visible text.
- At xhigh, multi-turn chats can end with the answer stuck inside thinking and
  no visible text. Check for empty replies.
- Low can stop early or skip searches and checks. Low and medium can say a code
  change is done without running it.
- Turning thinking off is a 400 error at xhigh and max. Temperature, top_p,
  top_k and assistant prefill are rejected.
- Safety classifiers can refuse, and Haiku has no server-side fallback. About
  1.8% of Terminal-Bench trials stopped on a refusal.
- Early users (Hacker News, Reddit, launch day) report skipped instructions,
  prompt leaks and weak complex UI work. Effort unknown; anecdotes only.

### Use it for

| Job | Effort |
|---|---|
| Classification, routing, extraction | low or medium |
| One named-file or symbol lookup the caller will check | medium |
| Codebase discovery, review questions, research | high |
| Hard coding or agent tasks with short context | xhigh |
| Code edits | Sonnet medium or high, not Haiku (reads files less faithfully) |
| Wide fact gathering (many sources) | high at least; WANDR collapses below it |
| Long autonomous coding, hard debugging, architecture | not Haiku: Sonnet or Opus |
| Anything that must not invent facts | not Haiku alone: GLM 5.3 Flash, or check it |

Open questions: Max-plan quota weight versus Sonnet; a matched effort trial on
our own worker packets (success, retries, tokens, wall time); whether Claude
Code's subscription accounting applies the over-100K price.

## Cheap tier audit: Haiku 5.5, GPT-6 Luna, GPT-5.6 Luna (October 7, 2026)

Three Codex reports and one Gemini run, plus AA's new max rows for both Lunas.
Evidence is in `evidence/2026-10-07/codex-luna-*.md` and
`codex-cheap-to-big-jump.md`. Effort tables are in
[`EFFORTS.md`](EFFORTS.md).

### Verdict

- **Haiku is the cheap doer; Luna is the cheap knower that guesses.** Haiku
  wins terminal, coding and computer-use work and guesses about half as often.
  Luna knows more facts, follows multi-step tool workflows better, and stays
  cheap past 100K tokens. When it does not know, it guesses three times in four.
- **For anything you will build on, pick Haiku.** For bulk lookups you will
  check anyway, Luna 6 xhigh is fine and a little cheaper.
- **Neither should run long.** Haiku costs 5 times more past 100K tokens. Luna's
  recall drops after about 128K. Split the work or step up.

### Side by side at the same spend

| | Haiku high | Luna 6 max | Haiku xhigh | Luna 5.6 max | Sol 6.1 low |
|---|---:|---:|---:|---:|---:|
| AA Intelligence | 37.8 | 38.1 | 41.2 | 37.3 | 42.1 |
| AA USD per task | 0.079 | 0.068 | 0.124 | 0.178 | 0.131 |
| Terminal-Bench (AA) | 22% | 13% | 29% | 12% | 31% |
| AutomationBench (multi-step tool workflows) | 34% | 53% | 36% | 50% | 53% |
| Hallucination (guesses when wrong) | 45% | 77% | 44% | 93% | 52% |
| Knowledge accuracy (Omniscience) | 35% | 44% | 35% | 43% | 59% |
| Long documents (AA-LCR) | 77% | 83% | 78% | 84% | 84% |
| Wait before first visible text | 26 s | 109 s | 87 s | 137 s | 2.4 s |
| Price past 100K prompt tokens | 5x | 1x until 272K, then 2x in, 1.5x out | 5x | 1x until 272K | 1x until 272K |

Anthropic's own charts, run with real per-token prices:

- **Computer use (OSWorld 2.1), same spend:** Haiku medium 53.3% vs Luna 6
  medium 37.5%, both about $0.13 per task. Haiku high 61.3% ($0.18) vs Luna 6
  max 48.9% ($0.21).
- **Terminal-Bench 4.0 at max:** Haiku 39.2%, Luna 6 16.4%.
- **FrontierCode (scoped coding) at max:** Haiku 46.4%, Luna 6 42.4%.

### The owner's three claims

| Claim | Verdict |
|---|---|
| Luna 6 is cheap enough to run at xhigh or max | **True.** Max is $0.07 per AA task, cheaper than Haiku high. But max is not more reliable on long agent runs: 12/23 code rebuilds vs 11/23 at xhigh, with twice the timeouts, and Codex compaction loops at max. |
| Luna 5.6 beats Luna 6, at higher cost | **True for coding agents, false elsewhere.** Code rebuilds 19 vs 12 at max, 9 vs 2 at high, for 2 to 4.6 times the cost. Equal on AA and Vals overall; Luna 6 guesses less. Sol low beats both for coding at about Luna 5.6 max's price. |
| Luna tanks once a task passes about 100K tokens | **Partly true.** At high effort, recall holds to 128K (82%) and then falls: 76% at 192K, 63% at 224K, 26% at 512K. With reasoning off it falls earlier (67% at 128K). The measured failure is missing facts. More guessing is plausible given its 77% to 85% guess rate, but no test proves it. No test splits coding quality by context length. |

### Long context, both models

| | GPT-6 Luna | Claude Haiku 5.5 |
|---|---|---|
| Measured recall by length | Holds to 128K at high, falls after (above) | No length curve published |
| Long-run coding evidence | ProgramBench whole-task pass 1.0% at max (Sol 6.3%) | ProgramBench hidden-test pass 82.0% with runs up to 1M, ahead of Sonnet's 79.7% (Anthropic, different scoring from Mercor's) |
| Harness window | Codex default window 272K for both Lunas; compaction reported near 200K to 258K | 1M in Claude Code |
| Known harness failure | Codex compaction loop at xhigh and max on long runs (#41318, Aug 28; Luna max comment Sept 1) | None found yet |
| Price past 100K | Unchanged until 272K | 5 times higher ($0.50 / $2.50) |

The 100K line is Haiku's price line, not a measured quality line. For Luna
it is close to the measured recall line. So both models want packets under
about 100K, for different reasons.

### The jump to Sonnet 5.5 and GPT-6.1 Sol

| | Haiku to Sonnet | Luna 6 to Sol 6.1 |
|---|---|---|
| Price per token | 20 times (4 times past 100K) | 20 times |
| Price per AA task, sweet spot to sweet spot | Haiku high $0.08 to Sonnet high $0.88: 11 times | Luna xhigh $0.04 to Sol low $0.13: 3 times; Sol medium $0.21: 5 times |
| Scoped coding | Small gap: FrontierCode 46.4 vs 46.2 at max; Haiku high beats Sonnet medium on CursorBench | Small on easy tasks (38/38 both); large with dense constraints (14/20 vs 20/20) |
| Terminal work at max | 39.2% to 70.6% | 16.4% to 58.2% |
| Long software builds | Haiku slightly ahead (ProgramBench 82.0 vs 79.7) | 1.0% to 6.3% |
| Honesty | Sonnet reads files more faithfully, but guesses more when wrong (51% to 65% vs 44%) | Luna hid a broken search tool 28.7% of the time, Sol 2.1%; guessing 82% to 52% |
| Web research | Gap of about 7 points (HLE with tools) | 61.9 to 70.4 on Parallel's search test, at 3.9 times the cost per attempt |

What this means:

- **On Codex, step up early.** Sol low costs only about 3 times Luna xhigh per
  task and fixes Luna's weak spots: terminal work 8% to 31%, guessing 82% to
  52%. Keep Luna for lookups and summaries that someone checks.
- **On Claude Code, Haiku can carry more.** It is close to Sonnet on scoped
  coding and reading. Step up to Sonnet for terminal work, visual or UI
  changes, runs past 100K tokens, and findings nobody will re-check.
- **Past 100K tokens, Sonnet is the cheap Claude.** It only costs 4 times
  Haiku there, and it scores far higher on long terminal runs.

### Gotchas

- Effort names do not line up. Luna 6 max scores about the same as Haiku high
  on AA and waits four times longer.
- AA prices both models at their short-prompt rate. Real long runs cost Haiku
  up to 5 times more and Luna up to 2 times more.
- Luna 5.6 on Codex shares the 272K default window and the same compaction loop.
- First-hand reports are few and small (10 to 100 tasks). Treat the Luna 5.6
  coding lead as likely, not settled.
- Rejected: Gemini's "GPT-6 Luna MRCR 41.3%" (that is Luna 5.6's vendor number),
  and any figure from haiku55.com or askai.free.

Open questions: a fixed coding task run at context sizes below and above 100K
on all three models; Luna 6 xhigh vs max with explicit "the container is
writable" instructions; Max-plan quota weight of Haiku.

## Gemini 3.8 Flash (only usable Gemini model)

Added at medium and high from the saved catalogue. Medium is the worker default, and high is the root default. Runs through the owner's Google AI subscription using the Gemini harness (`agy`).

**Filtering rule:** Gemini 3.8 Flash is the only usable model in the Gemini family.
The runtime gives access to other models, but they are abysmally bad. The Gemini Pro series defaults to 3.1, which is ancient by modern standards. Older Flash versions like 3.7 are obsolete. Never select Gemini Pro or older Flash versions.

Gemini 3.8 Flash remains the only useful Gemini model until Gemini 4 releases. When Gemini 4 launches, it will require separate benchmark testing, evaluation, and indexing into this folder before any use.

| | Medium | High |
|---|---:|---:|
| Intelligence | 39.8 | 40.9 |
| Index USD per task | 0.93 | 1.24 |
| Tokens per second | N/A | 242 |
| Hallucination | 51.9% | 55.2% |
| Omniscience | +28.6 | +29.6 |

Price is $0.75 in and $3.75 out per million tokens. High scores about one point
higher for about a third more cost, and hallucinates slightly more, so medium is
the better value for workers. High has the speed data, medium does not. Its speed
(242 tokens per second) is the fastest we track.

## Muse Spark has two prices

Muse Spark 1.3 comes in a default version and a Contributor version. The
Contributor version is the one the owner can use. It is priced far lower
because the owner accepts that Meta uses the data for training. The Artificial
Analysis price ($1.25 in, $4.25 out per million tokens) is for the default
version, so it overstates what the owner pays and understates its value here.

On the Go plan, Contributor gets the most requests of any model (45,300 per 5
hours, $60 monthly cap), ahead of MiMo V2.6 Flash and DeepSeek V4.1 Flash. See
[opencode-go-limits.md](opencode-go-limits.md).
We cannot turn that into an exact dollar price, so the value table ranks Muse
Spark low only because of the default price. In practice it is among the cheapest,
and with a 31.5% hallucination rate it is also one of the more reliable.

Because Contributor data is used for training, use it only for internet research
and work outside the private workspace. Never give it a private spec or other
private material. If a task needs a private spec, question whether it should be
done at all, then use a model from a plan you trust.

## Claude Sonnet 5.5 low (now measured)

The September 30 estimate (index near 34, about $0.24 per task) is replaced by
the October 7 AA measurement: index 35.9 at $0.35 per task, Terminal-Bench
20.7%. Haiku 5.5 high scores higher (37.8) for about a quarter of the price,
so Sonnet low has no clear job. Sonnet effort guidance is in
[`EFFORTS.md`](EFFORTS.md).
