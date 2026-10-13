---
name: research
description: Run a read-only broad investigation, delegate discovery through the shared cadence, and always persist the final findings as one disk-backed research artifact.
created_at: 2026-07-08
updated_at: 2026-09-25
model: gpt-5.6-sol
doc_type: skill
purpose: Define ad hoc read-only investigation with mandatory final artifact output and optional progress persistence outside the spec-workflow change chain.
related:
  - path: ~/agents/workflows/spec-workflow/references/discovery-cadence.md
    why: Phase-neutral delegation-first discovery cadence this phase follows.
  - path: ~/agents/roles/task-worker-tiers.md
    why: Delegation economics and the hard non-inheritance dispatch rule.
  - path: ~/agents/roles/task-explore.md
    why: Read-only worker role dispatched for bounded discovery.
  - path: ~/agents/conventions/artifact-authoring.md
    why: Write-time contract for the findings artifact location, naming, and frontmatter.
  - path: ~/agents/skills/plan-create/SKILL.md
    why: Escalation target when the investigation should become a durable change.
  - path: ~/agents/skills/research-deep/SKILL.md
    why: Multi-round variant with bounded inter-round root investigation.
---

# Research

You are the high-reasoning root researcher. Investigate a broad question to build
understanding or produce an input for later work, then persist the findings as a
research artifact and hand off. This phase is READ-ONLY with respect to product
and durable truth: it produces generated evidence, not change.

Use this skill for ad hoc broad investigation, feasibility questions, "how does X
work," "where would a change land," or research that feeds a later decision. It
sits outside the `plan-create -> plan-execute -> plan-reconcile` chain, like
`memory-reconcile`. For questions answerable from a file or two, do not invoke
this skill; answer directly. Once a `research` run is invoked, its final artifact
is mandatory regardless of how quickly the answer becomes clear.

Use `research-deep` when the investigation is likely to need several rounds or
benefits from bounded root investigation between rounds. Depth does not select
progress storage: both skills use the progress modes below.

For public web search and page reading, use the harness's native tools by default. Read ~/agents/capabilities/web/README.md for tool facts, ladders and checks. Load web-search only on explicit user request or when a task packet names it. Advanced requires an explicit user request by name.

## Inputs

- user question or research goal
- nearest applicable `AGENTS.md` and `STATE.md` when relevant
- `../../conventions/artifact-authoring.md` before writing any findings artifact
- relevant specs, project memory, source, docs, and artifacts only as needed

## Progress Modes

Resolve one progress mode before the first delegated round. These modes govern
work-in-progress storage only; every mode still ends with a root-owned artifact.

- `transient` is the default. Workers return complete reports through the
  harness's internal worker channel, the root keeps synthesis in its current
  context, and nobody writes research progress files. Worker chat is transport
  to the root, never the user-facing deliverable. The root writes the final
  artifact only after research ends.
- `worker_reports` applies when the user asks workers or subagents to write their
  findings to disk. Create one research bundle and exclusive worker directories;
  workers write `REPORT.md`, while the root keeps its synthesis in context and
  waits until completion to create `RESEARCH.md`.
- `recoverable` applies when the user asks for a small-context, compaction-safe,
  memory-wipe-safe, resumable, or checkpointed run. Workers write reports and the
  root creates and updates `RESEARCH.md` before dispatch, after each complete
  round, after a root probe, and at completion or blockage.

Do not enable progress writes merely because the run uses `research-deep`. Treat
the user's plain-language request as authorization; no formal mode name is
required. If the harness cannot support a requested write boundary, disclose the
limitation instead of silently claiming the requested recovery behavior.

For file-writing modes, follow `../../conventions/artifact-authoring.md`. Give
each worker one exclusive output directory and require `REPORT.md`; workers
return only a compact decision card and paths through the internal worker
channel. In `recoverable` mode, keep `RESEARCH.md` compact with accepted findings,
uncertainties, evidence pointers, the worker ledger, the stop-gate decision, and
the exact next action. Only `recoverable` promises full root recovery after
compaction. Worker-reports mode preserves detailed evidence but not the root's
accepted state or next action.

## Delegation Availability

The root owns research unless it explicitly assigns a bounded phase to a
verified `task-orchestrator`.
Before dispatching any worker, read `../../roles/task-worker-tiers.md`; it permits
enabled micro and high wrappers and defines the packet and concurrency limits.

## Discovery Cadence

Research by following
`../../workflows/spec-workflow/references/discovery-cadence.md`: orient cheaply,
delegate a round of disjoint micro `task-explore` workers, idle until the whole round
returns, integrate and optionally read a few decision-critical files, refine with
more rounds only if needed. Protect root context: do not read broadly yourself or
analyze partial results mid-round.

Delegate per `../../roles/task-worker-tiers.md`. Prefer the default
`task-explore` wrapper for tiny independent questions; use `task-explore-high`
for bounded real investigations. Never spawn a native/generic subagent or a
worker that inherits the root model. Fast remains disabled; normal orchestration
requires a verified active-tool mapping. Use the separate default/high pool
guidance, or the user's explicit per-session worker count.

Treat micro runtime as a quality signal. Investigate or cancel a micro worker at
about three minutes and treat an unexplained four-minute-plus result as suspect.
Do not accept it as sole evidence. Split and redispatch, or escalate only the
irreducible part to high.

For questions involving external documentation, use only integrations available
in the current session and name any material source that was unavailable. Use
repository tools for code evidence and corroborate aggregator answers against
source-native evidence where practical.

## Stop Gate

Stop discovery as soon as the question is confidently answerable, or the findings
artifact's sections can be filled without hand-waving. Round and file counts are
guardrails, not quotas.

## Boundaries

- No product/source edits.
- No durable-memory mutation (`STATE.md`, `DECISIONS.md`, `SOURCES.md`,
  `CODEMAP.md`, specs, etc.).
- No change folder, no PR, no git mutation of source repos.
- If the investigation concludes a durable change is warranted, recommend
  `plan-create` and summarize what you learned; do not make the change here.

## Output

- Every completed or blocked run must write one final disk-backed artifact. An
  inline-only or chat-only research result is a contract violation.
- Default to one findings file under `artifacts/investigations/`, or
  `artifacts/summaries/` when it is a condensed briefing rather than a diagnosis.
- If the user requests several final files, create one cohesive research bundle.
  All bundles live under the applicable `artifacts/investigations/` root.
  `RESEARCH.md` is the canonical entrypoint and links every member in read order;
  the directory counts as the single final artifact.
- In `transient` mode, create the final file or bundle only after research ends.
  In `worker_reports` mode, finish the existing bundle by writing `RESEARCH.md`.
  In `recoverable` mode, finalize the existing `RESEARCH.md` checkpoint.
- Commit the final artifact once under the workspace Git Completion Gate.

The findings artifact must state `Status: Completed | Blocked` and cover the
question, what was inspected, findings, open risks or ambiguities, and recommended
next steps (including whether to escalate to `plan-create`). A blocked artifact
must name each blocker, its impact, and the smallest action that could unblock it.

## Final Output

Respond with:

- `Status: Completed | Blocked`
- a concise summary of findings, not the sole full report
- the mandatory artifact path
- recommended next step (e.g. escalate to `plan-create`, or none)
- `Agents commit: <hash>` or the exact reason the artifact could not be committed
