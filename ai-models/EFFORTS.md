---
doc_type: guide
updated_at: 2026-10-07
purpose: Where the reasoning-effort sweet spot sits for Claude Haiku, Sonnet and Opus 5.5, GPT-6.1 Sol and the two GPT Lunas, what each effort is for, and how the models line up against each other.
related:
  - path: ./data/2026-09-30/EFFORTS.md
    why: Generated Artificial Analysis curves (every number in the AA lines below). (raw data not published)
  - path: ./delegation-briefing.md
    why: The only place that picks a model and effort for a role or job. This file is the evidence behind it.
  - path: ./SELECTION.md
    why: Value, reliability and per-model gotchas.
  - path: ./evidence/2026-10-07/
    why: Ten Codex research reports with links, dates and effort labels for every outside number here. (raw data not published)
---

# Effort sweet spots

Effort is how long a model thinks before and between actions. Higher effort
means more tokens, more money and a longer wait before the first visible text.
The sweet spot is the last effort before an extra point of quality gets several
times more expensive.

Data as of October 7, 2026. Artificial Analysis (AA) curves are generated in
`data/2026-09-30/EFFORTS.md` (raw data not published).
Outside numbers come from the reports in `evidence/2026-10-07/`; each one there
has its link, date and effort.

## One-screen answer

| Model | Sweet spot | Step down | Step up | Avoid |
|---|---|---|---|---|
| Claude Haiku 5.5 | **high** | medium for narrow lookups; low only for routing | xhigh for short-context coding and agent tasks | max; long agent runs over 100K tokens (Sonnet is cheaper there) |
| Claude Sonnet 5.5 | **high** | medium for small, well-specified edits | xhigh for hard coding, only after a failure | max (one coding test got worse, cost triples) |
| Claude Opus 5.5 | **medium** | low for short, bounded reads | high for ambiguous repo work | xhigh and max (flat on two independent tests, 2 to 5 times the cost) |
| GPT-6.1 Sol | **medium** | low for simple reads | high (cheap; hit the full pass rate in one test) | max |
| GPT-6 Luna | **xhigh** | high for simple extraction | max only for one short, hard question | low and medium for anything but routing; max on long agent runs; any packet past about 128K tokens |
| GPT-5.6 Luna | **xhigh**, coding only | | max for hard code rebuilds (19/23 vs 12/23) | everything that is not coding: Luna 6 is cheaper and guesses less |

Confidence is moderate for all of them. Nobody has run these exact efforts on
worker packets like ours. A small trial on real packets would settle it.

## Claude Haiku 5.5

**Sweet spot: high.** It is the lowest effort that clears three bars at once:

- **It beats Sonnet medium on coding at under half the cost.** CursorBench
  (Cursor's independent multi-file coding test): Haiku high 42.3% at $0.32
  per task, Sonnet medium 39.2% at $0.52.
- **Broad research collapses below it.** WANDR (gathering many facts across the
  web): 3.5% at low, 12.9% at medium, 37.3% at high, 45.9% at xhigh.
- **Anthropic recommends it for strict instruction following.** Below it, low
  and medium can skip checks and claim work is done.

| Test | low | medium | high | xhigh | max |
|---|---:|---:|---:|---:|---:|
| AA Intelligence | 29.4 | 34.5 | 37.8 | 41.2 | 43.4 |
| CursorBench, $/task | 30.9%, 0.08 | 36.9%, 0.17 | 42.3%, 0.32 | 44.3%, 0.56 | 48.4%, 1.12 |
| FrontierCode Main (Claude Code), $/task | 34.8%, 0.06 | 41.6%, 0.13 | 41.9%, 0.26 | 45.8%, 0.63 | 46.4%, 1.33 |
| FrontierCode minutes per task | 6.7 | 8.7 | 11.1 | 16.0 | 23.6 |
| Terminal-Bench (Anthropic), $/attempt | 12.7%, 0.42 | 20.3%, 0.68 | 24.8%, 1.04 | 31.5%, 1.75 | 39.2%, 2.64 |
| DRACO deep research | 64.3% | 72.4% | 77.8% | 80.5% | 81.5% |
| WANDR wide research | 3.5% | 12.9% | 37.3% | 45.9% | 49.9% |
| HLE with tools | 38.6% | 45.0% | 50.1% | 54.8% | 57.4% |
| AA wait before first visible text | 6 s | 13 s | 26 s | 87 s | 415 s |

What each effort is for:

- **low:** routing, classification, one named-file lookup the caller checks.
  Skips searches and stops early on long prompts.
- **medium:** the API and Claude Code default. Narrow lookups and extraction.
  FrontierCode shows medium about equal to high on bounded coding, but medium
  can claim untested work is done.
- **high:** the default for discovery, review questions and research.
- **xhigh:** hard coding or agent tasks that stay under 100K tokens. Can end a
  multi-turn reply with the answer stuck in hidden thinking.
- **max:** not worth it. Seven-minute wait, flat agent scores, small gains.

Limits that effort does not fix:

- **Over 100K tokens of prompt, every token costs 5 times more.** On Anthropic's
  Terminal-Bench chart, Sonnet medium (28.8%, $0.68) beats Haiku xhigh (31.5%,
  $1.75) on value because those runs are long. Haiku is cheap only for short
  context.
- **Sonnet reads more faithfully.** Anthropic's system card says Sonnet 5.5 is
  strictly better than Haiku 5.5 at not misreading file and tool contents, not
  leaving out important things, and not claiming false completion.
- **Weak at multi-step tool workflows.** AA AutomationBench tops out at 36%
  (xhigh), below Sonnet low (49%).
- Claude Code cannot turn Haiku's thinking off; `effort` in an agent file works.

## Claude Sonnet 5.5

**Sweet spot: high.** Every test shows its biggest jump from medium to high,
and the next step costs about three times more per point.

| Test | low | medium | high | xhigh | max |
|---|---:|---:|---:|---:|---:|
| AA Intelligence | 35.9 | 40.8 | 46.8 | 51.9 | 56.0 |
| AA USD/task | 0.35 | 0.48 | 0.88 | 2.01 | 5.46 |
| AA hallucination | 50% | 51% | **65%** | 63% | 47% |
| CursorBench, $/task (Oct 7 prices) | 35.8%, 0.37 | 39.2%, 0.52 | 47.8%, 1.20 | 53.1%, 2.81 | 55.5%, 7.05 |
| FrontierCode Main | 29.3% | 36.5% | 49.4% | 52.1% | **46.2%** |
| Terminal-Bench (Anthropic), $/attempt | 20.0%, 0.62 | 28.8%, 0.68 | 43.0%, 1.46 | 61.5%, 4.34 | 70.6%, 10.44 |
| OSWorld offline | 57.9% | 66.0% | 73.2% | 81.1% | 83.9% |
| Read-only bug hunt (6 planted bugs, 2 runs) | 5, 5 | 5, 5 | 6, 6 | | |
| AA wait before first visible text | 1.1 s | 4.5 s | 12.3 s | 35 s | 457 s |

What each effort is for:

- **low:** quick lookups with a clear answer check. Low now has an AA score
  (35.9), but Haiku high scores higher for far less.
- **medium:** small, well-specified edits with a real test. Fast to start.
- **high:** investigation, review, bug hunting, multi-file changes, longer
  agent tasks. Only high found the subtle sixth bug in the read-only sweep.
- **xhigh:** hard coding after a high attempt failed. Same score and about the
  same cost as Opus medium on CursorBench since the October 7 cache cut.
- **max:** worse on FrontierCode (52.1% to 46.2%) because extra review
  subagents caused timeouts and out-of-scope edits. Terminal work still improves.

Gotchas:

- **High guesses more when wrong** (AA hallucination 51% at medium, 65% at high).
  Ask high workers for file and line evidence and check decisive claims.
- Effort names were recalibrated from Sonnet 5; old habits do not carry over.
  Claude Code defaults Sonnet to medium; the API defaults to high.
- Cache reads dropped to $0.10 per million on October 7, about 20% cheaper on
  most agent work.
- Higher effort adds unrequested tests and files. Give explicit scope rules.

## Claude Opus 5.5

**Sweet spot: medium.** Low to medium is the biggest jump of any family
(AA 42.3 to 51.2, Terminal-Bench 31% to 52%). After medium, gains are small.

| Test | low | medium | high | xhigh | max |
|---|---:|---:|---:|---:|---:|
| AA Intelligence | 42.3 | 51.2 | 53.6 | 56.0 | 57.6 |
| AA USD/task | 0.55 | 1.34 | 1.82 | 3.46 | 5.98 |
| CursorBench, $/task | 43.7%, 1.17 | 52.5%, 2.91 | 56.0%, 3.97 | 56.0%, 6.98 | 57.8%, 13.43 |
| Legacy rewrite (VulcanBench, Claude Code), tasks passed | 17/23 | **23/23** | 22/23 | 22/23 | 21/23 |
| Legacy rewrite minutes per task | 13.7 | 18.6 | 21.4 | 20.7 | 37.5 |
| AA wait before first visible text | 13 s | 23 s | 33 s | 136 s | 723 s |

- **low:** short, bounded reads. Weak for a strong model: Sonnet high beats it
  on every test at about the same CursorBench cost.
- **medium:** orchestration, hard reasoning, review, architecture.
- **high:** ambiguous repository work when medium missed something.
- **xhigh, max:** CursorBench ties high at xhigh; the rewrite test passes fewer
  tasks at max. Higher efforts also triggered more fallback to Opus 4.8.
- Guesses most of all (AA hallucination 66% to 68% up to xhigh). Check facts.

## GPT-6.1 Sol

**Sweet spot: medium.** Cheapest per point of the strong models.

| Test | low | medium | high | xhigh | max |
|---|---:|---:|---:|---:|---:|
| AA Intelligence | 42.1 | 47.8 | 50.2 | 51.0 | 51.8 |
| AA USD/task | 0.13 | 0.21 | 0.32 | 0.39 | 0.72 |
| Legacy rewrite (VulcanBench, Codex), tasks passed, $/task | 20/23, 0.31 | 22/23, 0.40 | **23/23, 0.33** | 23/23, 0.43 | 23/23, 0.46 |
| Legacy rewrite minutes per task | 6.9 | 10.6 | 10.2 | 15.4 | 14.5 |
| AA wait before first visible text | 2.4 s | 5.5 s | 58 s | 134 s | 327 s |

- **low:** simple reads and extraction.
- **medium:** OpenAI's documented default; real coding and reasoning.
- **high:** correctness-focused coding. In the rewrite test it cost no more
  than medium and passed every task.
- **xhigh, max:** under one point each on AA.
- On the Codex subscription Sol runs about a third of API speed
  (`subscription-speed.md`). Not on CursorBench yet.

## GPT-6 Luna and GPT-5.6 Luna

**Sweet spot: GPT-6 Luna xhigh.** It is the first effort where coding works at
all, and max adds little on real agent runs. AA added max for both Lunas on
October 7 and re-scored GPT-6 Luna up by 0.4 to 0.8 points at every effort.

| Test (Luna 6 / Luna 5.6) | low | medium | high | xhigh | max |
|---|---:|---:|---:|---:|---:|
| AA Intelligence | 21.5 / 21.0 | 29.9 / 25.0 | 32.9 / 32.1 | 34.6 / 34.6 | 38.1 / 37.3 |
| AA USD/task | 0.005 / 0.010 | 0.017 / 0.016 | 0.029 / 0.044 | 0.042 / 0.085 | 0.068 / 0.178 |
| AA Terminal-Bench | 0% / 0% | 3% / 1% | 5% / 3% | 8% / 4% | 13% / 12% |
| AA AutomationBench | 12% / 12% | 40% / 23% | 48% / 36% | 48% / 43% | 53% / 50% |
| AA hallucination | 84% / 90% | 85% / 91% | 84% / 92% | 82% / 92% | 77% / 93% |
| Code rebuild (VulcanBench, 23 tasks), passed | 0 / 0 | 0 / 1 | 2 / 9 | 11 / 13 | 12 / 19 |
| Code rebuild $/task | 0.03 / 0.02 | 0.01 / 0.07 | 0.05 / 0.22 | 0.16 / 0.28 | 0.10 / 0.45 |
| Godot game score, 3 runs (out of 100) | 90.5 / 78.8 | 86.3 / 83.9 | 89.5 / 99.6 | 95.1 / 96.2 | 94.2 / 98.4 |
| AA wait before first visible text | 2.7 s / 1.5 s | n/a / 2.1 s | 14 s / 7 s | 27 s / 62 s | 109 s / 137 s |

What each GPT-6 Luna effort is for:

- **low:** routing and classification only. Zero on every coding test.
- **medium:** one-line lookups. Biggest AA jump, but 0 of 23 code rebuilds.
- **high:** extraction and summaries you will check. Coding still fails (2/23).
- **xhigh:** the default. Coding starts to work (11/23). Keep the packet small.
- **max:** one short, hard question. On AA it is cheap (+3.5 points for
  $0.03 more) and guesses a bit less (77%). On long agent runs it is no better
  than xhigh: 12/23 against 11/23, with four timeouts against two. In Codex,
  max runs have looped on context compaction for hours (openai/codex #41318).

Luna 5.6 against Luna 6 (the owner's "5.6 is better but costs more"):

- **True for coding agents.** Code rebuilds 9 vs 2 at high and 19 vs 12 at
  max. One user's Terminal-Bench rerun: 93 vs 40 of 100 at xhigh (Luna 6
  wrongly treated a writable container as read-only). A 10-task A/B judged
  Luna 5.6's final code better 6 to 4. Vals: 5.6 ahead on finance (+5) and
  legal research (+6).
- **It costs 2 to 4.6 times more per task** (price is $0.20/$1.20 vs
  $0.10/$0.50 per million).
- **Not true for anything else.** Same AA score at xhigh, same Vals index at
  max (51.7 vs 51.2). Luna 6 guesses less (77% to 85% vs 90% to 93%), does
  multi-step tool workflows better (AutomationBench) and won a Godot test at
  low and medium.
- **Better option for coding: GPT-6.1 Sol low** (AA 42.1, Terminal-Bench 31%,
  hallucination 52%, $0.13) costs less than Luna 5.6 max ($0.18) and beats it
  on every AA measure.

Long context (the owner's "Luna tanks past 100K"): partly true. In a planted
fact recall test (Dmitriev, Sept 27) GPT-6 Luna at high held 90% at 64K and
82% at 128K, then fell to 76% at 192K, 63% at 224K and 26% at 512K. With
reasoning off it was already at 67% by 128K. It mostly missed facts rather
than inventing them, but when it does not know, it guesses (AA 77% to 85%).
Details and the Haiku comparison are in
[`SELECTION.md`](SELECTION.md).

## Cross-model ladder

Models at about the same quality, cheapest first. AA index and Terminal-Bench,
plus CursorBench where measured. Wait is AA time to first visible text.

| Quality tier | Options |
|---|---|
| **About 34 to 38** | Luna 6 xhigh (34.6, TB 8%, $0.04, 27 s) · Haiku high (37.8, TB 22%, $0.08, 26 s; Cursor 42.3%) · Luna 6 max (38.1, TB 13%, $0.07, 109 s) · Luna 5.6 max (37.3, TB 12%, $0.18) |
| **About 41 to 44** | Sol low (42.1, TB 31%, $0.13, 2 s) · Haiku xhigh (41.2, TB 29%, $0.12, 87 s; Cursor 44.3%) · Sonnet medium (40.8, TB 30%, $0.48, 4.5 s; Cursor 39.2%) · Opus low (42.3, TB 31%, $0.55, 13 s; Cursor 43.7%) |
| **About 47 to 48** | Sol medium (47.8, TB 48%, $0.21) · Sonnet high (46.8, TB 44%, $0.88; Cursor 47.8%) · Haiku max (43.4; Cursor 48.4%, but 7-minute wait) |
| **About 51 to 53** | Sol high (50.2, TB 52%, $0.32) · Opus medium (51.2, TB 53%, $1.34; Cursor 52.5%) · Sonnet xhigh (51.9, TB 57%, $2.01; Cursor 53.1%) |
| **About 56** | Opus xhigh (56.0, TB 60%, $3.46) · Sonnet max (56.0, TB 64%, $5.46) |

Reading the ladder:

- Effort names do not line up across families. Sonnet high is about Sol
  medium; Opus medium is about Sonnet xhigh and Sol high.
- In Claude Code, **Sonnet high beats Opus low on every measure** at about the
  same CursorBench cost, and Haiku high beats Sonnet medium on coding for less.
- Sol is cheapest at every tier but slow on the Codex subscription.
- Haiku's cost edge holds only below 100K tokens of context.
- At the same AA score, Haiku high does about twice the terminal work of Luna 6
  max (22% vs 13%) and guesses far less (45% vs 77%).

## What would settle the open questions

Run the same 10 to 20 real packets with known answers through Haiku medium,
Haiku high and Sonnet medium (explore), and Sonnet medium vs high (execute).
Record model, effort, wall time, tokens, cited-path accuracy, missed findings,
scope violations and how often the root had to re-check. Still unknown: Max
plan quota weight of Haiku vs Sonnet, and whether Claude Code's subscription
accounting applies Haiku's over-100K price.
