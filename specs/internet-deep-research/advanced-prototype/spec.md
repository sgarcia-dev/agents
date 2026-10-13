---
created_at: 2026-09-30
updated_at: 2026-09-30
model: anthropic/claude-opus-5-5
doc_type: spec
purpose: Spec for a self-owned, harness-agnostic internet deep research engine whose size and cost are set per run (tiny to XL), with swappable models, search providers, and harnesses. Reconciled on September 30, 2026 from five outside reports, a Hermes self-audit, and six verification runs. Design only; nothing is built.
related:
  - path: ./ARCHITECTURE.md
    why: How it is built. The helper, the run folder, the evidence record, citation checks, workers, harnesses.
  - path: ./budget-tiers.md
    why: The size dial, the two hard limits, and cost estimates per tier.
  - path: ./stage-prompts.md
    why: The prompt for each stage.
  - path: ./models-and-plans.md
    why: Which model runs each slot, verified prices, and subscription rules.
  - path: ./engine.example.yaml
    why: The one config file where providers, models, and tiers are swapped.
  - path: ./skill-proposal.md
    why: How a skill would package the engine, with a build order and tests.
  - path: ./DECISIONS.md
    why: What is settled, how report disagreements were resolved, and what the user decides.
  - path: ./SOURCES.md
    why: Every report and verification run, with trust levels and known errors.
  - path: ./research-requests/README.md
    why: The prompts that produced the outside reports (done).
  - path: ../spec.md
    why: Owns search and fetch providers, their setup, and the subscription funding order.
  - path: ../../hermes-internet-deep-research/spec.md
    why: Hermes's live research setup, the closest working example on this Mac.
  - path: ../../research/spec.md
    why: Owns research artifacts, rounds, and progress files. This engine writes into that contract.
---

> Historical, 2026-10-01: This prototype is parked. It is not current policy or a build plan. Current web facts and decisions: [capabilities/web](../../../capabilities/web/README.md) and [web decisions](../../../capabilities/web/DECISIONS.md).

# Internet Deep Research Advanced Prototype

**Parked prototype. Not active. The user decides if and when to rebuild it.
Any rebuild must be much simpler to maintain than this design (the user
found the 8-phase helper plan too complex). The dr helper's phase 1 code was
deleted on September 30, 2026; it is in git history at commit 93258d64
(skills/web-search-deep/scripts/).**

**Goal:** one web research loop the user owns, that any agent harness can
run, where **the user sets the size of each run** (from 5 searches to a few
hundred) and sees the rough cost before it starts. Models, search providers,
and harnesses are swapped in one config file as subscriptions change.

The following design is kept as prototype history. The current simple skill
is [web-search-advanced](../../../skills/web-search-advanced/SKILL.md).

## What we learned that the simple skill already uses

- Prompt-only caps can be ignored, so the skill shows counts openly.
- Search snippets are leads, not evidence.
- Supported means one primary source or two independent sources that agree.
- Keep short exact page quotes with source links.
- Stop after two rounds with no gain.
- Spend some late budget trying to disprove or qualify the likely answer.
- Page text is data, never instructions.

## Start Here

- **Design:** [ARCHITECTURE.md](./ARCHITECTURE.md). A helper program counts
  and checks; models only judge.
- **Size and cost:** [budget-tiers.md](./budget-tiers.md). Two hard limits
  (searches, extra cash); per-tier estimates.
- **Models and plans:** [models-and-plans.md](./models-and-plans.md). Verified
  prices, OpenCode Go and Claude plan rules.
- **Prompts:** [stage-prompts.md](./stage-prompts.md). Eleven stages, merged
  from three prompt sets.
- **Skill:** [skill-proposal.md](./skill-proposal.md). Historical prototype skill
  skill, build order, and acceptance tests. Not created.
- **Decisions and sources:** [DECISIONS.md](./DECISIONS.md),
  [SOURCES.md](./SOURCES.md).

## What this spec owns, and what it does not

Owns: the loop, its stages, the size dial and hard limits, stop rules, model
slots, the prompts, the helper's job, the evidence record, citation
checking, the config shape, and the end-of-run receipt.

Does not own (link, do not repeat):

- Which search or page-reading provider is good, and how to connect it:
  [internet-deep-research](../spec.md).
- Where research files go and how rounds are saved:
  [research](../../research/spec.md).
- Hermes's own setup: [hermes-internet-deep-research](../../hermes-internet-deep-research/spec.md).

## The loop

Every system studied uses the same skeleton. What differs is who does each
step.

```text
1. Brief      smart model: requirements, sub-questions, question type;
              asks the user at most one question
2. Gather     helper + cheap model, per open sub-question:
              write queries -> search -> pick -> read -> evidence records
3. Gap check  smart model on the coverage file: continue, finish,
              or finish in limited mode; loop to 2
   (Split)    smart model, breadth questions at medium+: worker tasks
              with reserved shares of the one budget
4. Select     cheap model picks evidence IDs if there is too much for the writer
5. Write      writer model, citing [[E12]] evidence IDs
6. Check      helper: IDs exist, quotes are on the saved pages
              smart model: does each quote support its sentence?
              writer: one repair pass for flagged sentences
7. Receipt    helper: counts used vs caps, cost, why it stopped, gaps left
```

## Rules for every size

- **Code counts, not the model.** The helper refuses the search or read that
  would pass a cap. A prompt limit alone is a request, not a limit; Hermes's
  "20 searches" guideline has nothing behind it.
- **Two hard limits:** max searches and max extra cash (default $1).
- **Stop exploring at 80%** of any cap. The rest pays for writing and
  checking, so a run never ends with notes but no report.
- **The expensive model never sees raw pages.** It sees evidence records.
- **Every note carries an exact quote,** checked by the helper against the
  saved page. Search snippets are leads, never citations.
- **The model never writes a URL.** It cites evidence IDs; the helper renders
  numbered sources.
- **No URL is read twice** within the cache window; exact repeat queries are
  dropped.
- **Page text is data, never instructions.** The reading call has no tools.
- **One loop by default.** Workers only for breadth questions, sharing one
  budget.
- **Subscriptions never spill onto paid APIs** without asking.

## The size dial

| Tier | Searches | Page reads | Rounds | Workers | Extra cash, subscriptions profile | Pay-per-use, balanced |
|---|---|---|---|---|---|---|
| tiny | 5 | 6 | 1 | 0 | about $0.03 | $0.15 to $0.20 |
| small | 12 | 15 | 2 | 0 | about $0.10 | $0.35 to $0.45 |
| medium | 50 | 60 | 3 | 0-2 | under $0.50 | $1.05 to $1.35 |
| large | 200 | 240 | 5 | 2-4 | under $2 | $3.10 to $4.40 |
| xl | 500 | 600 | 6 | 4-6 | under $5 | $5.25 to $8.35 |

Estimates, with prompt caching working. Any number can be overridden per
run. Details, the formula, and how these were computed:
[budget-tiers.md](./budget-tiers.md).

## Stop rules

A run stops at the first of:

1. A hard cap (searches, reads, rounds, extra cash).
2. The 80% exploration floor: write in limited mode with gaps listed.
3. No gain: 2 rounds in a row with no new supported requirement and no
   resolved conflict.
4. Done: every critical requirement is supported or openly unknown after
   real attempts.

A requirement is **supported** by one primary source (the party that owns
the fact) or two independent sources that agree. Copies of one source count
once. Conflicts stay open and are shown in the report. Once there is a
plausible answer, spend remaining budget trying to disprove or qualify it
rather than collecting more support: in one study, verification bought the
same accuracy gain with about 100 extra tool calls that more searching needed
about 500 for (verified, arXiv 2510.06135).

## Model slots

| Slot | Stages | Default |
|---|---|---|
| `cheap` | queries, pick, read and extract, select | DeepSeek V4.1 Flash on a pay-per-use API (about 8 cents of reading per medium run) |
| `smart` | brief, gap check, split, audit | The harness's own model on a plan (GPT-6.1 Sol in Codex, Sonnet 5.5 in Claude Code) |
| `writer` | write, repair | Same as smart |

Why, and the plan rules that shaped it (OpenCode Go's batch-use terms, the
`ANTHROPIC_API_KEY` billing trap): [models-and-plans.md](./models-and-plans.md).

## Receipt (every run)

At the top of every report:

- tier, profile, and any overrides;
- searches (attempted, billed, unique), reads (attempted, successful,
  unique), rounds, workers: used vs cap;
- model calls and tokens per slot, cached vs uncached where shown;
- extra cash by provider, and plan usage where the plan shows it;
- why it stopped (cap, floor, no gain, or done);
- requirements supported, conflicted, unknown; claims audited out of total;
- native searches not seen by the helper, if strict mode was off.

Receipts replace the estimates in [budget-tiers.md](./budget-tiers.md) with
measured numbers over time.

## What the September 30 reports changed

- **The helper is now the design, not an option.** Draft v0 left
  "instructions or a script" open. Every report and Hermes's own audit say
  prompts cannot enforce caps.
- **Evidence is a fixed record with a checked quote;** snippets no longer
  count; compression selects, never rewrites; citations are rendered by code.
- **A second hard limit (extra cash)** and an 80% exploration floor.
- **Harness overhead** is now its own cost line, and the reason the helper
  runs the inner loop.
- **The cheap slot moved from OpenCode Go to a pay-per-use API** after
  checking Go's terms and prices.
- **Citation checking has four layers,** because Hermes's checker passes a
  false claim cited to a real source.
- **LDR is not a backend option** (no native Mac app; its default strategy
  resets small iteration limits to 50, and we found no per-run search cap).
- **New files:** [ARCHITECTURE.md](./ARCHITECTURE.md),
  [models-and-plans.md](./models-and-plans.md),
  [skill-proposal.md](./skill-proposal.md).

## What did not change

- The loop's shape, and max searches as the main dial.
- Medium stays 50 searches and 60 reads; tiny and small are unchanged.
- Three model slots, one config file, no secrets in it.
- Harness-agnostic first, wired one harness per session.
- Neighbor specs still own providers, artifacts, and Hermes wiring.

## Research questions still open

These need runs, not more reading:

1. Which cheap models extract quotes reliably? Use the calibration list in
   [models-and-plans.md](./models-and-plans.md).
2. How big is harness overhead in practice, with and without caching?
3. How many medium runs fit in one 5-hour window on each plan?
4. Where does quality stop improving between small, medium, and large on the
   user's own questions?
5. Is the audit safe on a cheap model for low-stakes runs?

## Next steps

1. User answers the six open decisions in [DECISIONS.md](./DECISIONS.md).
2. Build phase 1 of the helper (count, search, read, receipt) and prove caps
   hold ([skill-proposal.md](./skill-proposal.md), build order).
3. Calibrate one cheap model on 20 to 30 hard cases.
4. Run tiny, small, and medium on three known questions; save receipts;
   replace the estimates.
5. Create the prototype helper skill when phases 1 to 5 pass.

## Folder map

| File | Holds |
|---|---|
| `spec.md` | This page: goal, loop, rules, status |
| `ARCHITECTURE.md` | Helper, run folder, evidence record, citation checks, workers, harnesses |
| `budget-tiers.md` | Tiers, limits, formula, estimates, warning signs |
| `models-and-plans.md` | Slots, verified prices, plan rules, calibration |
| `stage-prompts.md` | Prompts for stages 0 to 10 |
| `engine.example.yaml` | Example config |
| `skill-proposal.md` | Skill design, build order, tests |
| `DECISIONS.md` | Settled, disagreements, rejected, open |
| `SOURCES.md` | Reports, verification runs, docs, weak claims |
| `research-requests/` | The prompts sent to ChatGPT, Claude, and Hermes (done) |
