---
created_at: 2026-07-07
updated_at: 2026-09-25
model: gpt-5.6-sol
doc_type: workflow
purpose: Define the phase-neutral delegation-first discovery cadence reused by plan-create and research.
related:
  - path: ../AGENTS.md
    why: Spec workflow invariants and worker boundary this cadence operates under.
  - path: ../../../skills/plan-create/SKILL.md
    why: Planning phase that must follow this cadence.
  - path: ../../../skills/research/SKILL.md
    why: Read-only investigation phase that reuses this cadence.
  - path: ../../../roles/task-explore.md
    why: Read-only worker role dispatched each discovery round.
  - path: ../../../roles/task-worker-tiers.md
    why: Delegation economics, tier semantics, and the hard non-inheritance rule.
---

# Discovery Cadence

The discovery cadence is how a high-reasoning root/phase agent researches a task
while protecting its own context. The frontier root is the scarce, expensive
resource: its context is the budget to protect. This cadence keeps the root
context-lean by delegating breadth to bounded workers, idling while they run,
and refining coarse-to-fine until the phase can produce its output. Why this
matters - delegation economics and the hard rule that delegated work never runs
on the root's frontier model - lives in `../../../roles/task-worker-tiers.md`.

This cadence is phase-neutral. Its consumers supply their own stop gate and
output:

- `plan-create` researches until it can author a change folder / `PLAN.md`.
- `research` researches until it can write the mandatory final findings artifact
  without hand-waving.

## When It Applies

- Follow this cadence in `plan-create` whenever the task warrants the spec
  workflow.
- Follow it in `research` for any non-trivial broad investigation.
- Skip it for trivial one-file edits, typos, small changes that do not use the
  spec workflow, or questions answerable from a file or two.

The simple-question bypass applies only before a `research` skill or command is
invoked. An explicit research invocation always follows its mandatory final
artifact contract even if the answer becomes simple.

## The Real Control: Stop-Early Gate

Round counts and file counts below are guardrails, not quotas. The actual stop
condition is a readiness test: stop discovery as soon as you can confidently
satisfy your phase's output contract. Do not pad discovery to hit a round count,
and do not under-research a task whose output is still fuzzy.

Concrete gates per consumer:

- `plan-create`: stop when you can confidently fill the `PLAN.md` execution
  contract fields - `allowed_paths`, `forbidden_paths`, `required_reads`,
  `verification`, `worker_strategy`.
- `research`: stop when the question is confidently answerable, or the findings
  artifact's sections can be filled without hand-waving.

If one round already satisfies the gate with confidence, stop. If it is still
uncertain, run another round.

## Phases

### Phase 0 - Cheap orientation (root)

Read only routing and memory anchors: the nearest `AGENTS.md`, `STATE.md`, and
`INDEX.md`, plus any files the user explicitly referenced. Do not do broad
source archaeology on the root. This phase exists to decide where to point the
first round, not to understand the whole system.

### Phase 1 - Round 1 (broad delegate, then idle)

Dispatch one parallel batch of enabled default `task-explore` micro packets only
when the harness and question support it. `task-worker-tiers.md` gives separate
default and high worker guidance, subject to the user's explicit count. Use fewer
when that covers the useful independent slices. Each packet:

- owns a distinct slice (subsystem, hypothesis, or bounded question),
- is seeded with distilled context, not raw dumps,
- is right-sized so the worker finishes well under the micro context and runtime
  envelope. If one slice is too big, split it into smaller disjoint packets or
  keep it in the root session. See `../../../roles/task-worker-tiers.md`.

Then idle. Until every worker in the round returns, do not read source, do not
analyze partial results, and do not dispatch a new round. The failure mode this
prevents is the root interleaving large reads or analysis mid-round and bloating
its own context.

### Phase 2 - Integrate + optional pinpoint reads

Synthesize the returned reports. Optionally read up to about 3-8
decision-critical files that only a direct root read can resolve well (for
example, the exact file to be modified, or a tricky type or contract). Prefer
worker summaries over direct reads whenever a worker can answer as well.

### Phase 3 - Round 2 (targeted, optional, then idle)

If the stop-early gate is not yet satisfied, dispatch a sharper round. By now the
root understands where to look, so these packets are more targeted. Seed them
with Round 1 findings plus each report's `Recommended Next Context` and
`Risks / Ambiguities`. Continue using small, enabled default micro packets where
possible. Give bounded coupled or multi-step work to an enabled high wrapper;
keep broad or open-ended issues in the root. Idle again under the Phase 1 rule.

### Phase 4 - Final reads + produce output

Read any last critical files, then produce your phase output: for `plan-create`
produce the human review proposal and, only after approval, write the change
folder and `PLAN.md` (its `## Required Decisions` are the output of this
  cadence); for `research` write the mandatory final findings artifact, then
  follow the skill's final receipt contract for status, summary, next step,
  artifact path, and commit status.

## Complexity Guidance (soft)

Rough defaults, subordinate to the stop-early gate:

- Small task: about 1 round. May instead read a slightly larger direct set
  (about 10-15 files) if that is genuinely cheaper than a round.
- Moderate task: about 2 rounds. This is the common sweet spot.
- Complex task: up to about 3 rounds.

These numbers are soft defaults, not a cap. Run additional rounds - including
rounds whose only purpose is to verify or validate a hypothesis - whenever the
stop-early gate is not yet met. Under-researching and deferring the remainder is
a failure, not a shortcut.

## Cross-Cutting Rules

- Disjoint packets per round: no two workers in the same round should read the
  same slice. Real breadth requires non-overlapping questions.
- Distill context in, harvest context out: give workers the current findings,
  hypotheses, bounded question, and known landmarks, not replicated raw file
  dumps. Feed the next round from the prior round's `Recommended Next Context`
  and `Risks / Ambiguities`.
- Tier mapping: prefer enabled default micro workers for tiny independent packets;
  use enabled high workers for bounded real tasks within their separate suggested
  pool. Fast wrappers remain disabled. The normal orchestrator requires a verified
  mapping in the active tool.
- Runtime and trust: investigate or cancel a micro worker after roughly three
  minutes and treat an unexplained four-minute-plus result as suspect. Strictly
  corroborate micro claims before integration.
- Never inherit the frontier model: every round is dispatched through the
  non-frontier `task-explore` family, never a native/generic subagent that
  inherits the root's model. See the hard rule in `task-worker-tiers.md`.
- Dispatch boundary: terminal workers never spawn, call, or coordinate other
  workers. The root fans out rounds directly, or a verified orchestrator fans
  out its assigned leaf round; neither interleaves large reads mid-round.
- When a bounded external-source lookup has a tool-specific concurrency limit, the
  root must enforce that limit and avoid automatic retries or fallback recovery.
  Record the unavailable source if the lookup cannot run.
