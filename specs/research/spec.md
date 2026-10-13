---
created_at: 2026-08-12
updated_at: 2026-08-17
model: gpt-5.6-sol
doc_type: spec
purpose: Define portable normal and deep research behavior, mandatory final artifacts, optional progress reporting, and compaction recovery.
related:
  - path: ../../skills/research/SKILL.md
    why: Lean default research procedure.
  - path: ../../skills/research-deep/SKILL.md
    why: Multi-round research procedure with bounded inter-round root review.
  - path: ../../roles/task-explore.md
    why: Source-read-only worker role with create-only report output.
  - path: ../../conventions/artifact-authoring.md
    why: Final research artifact and optional progress-bundle rules.
---

# Research Spec

Research builds evidence and understanding without changing product or durable
product truth. Every run persists its final findings as one disk-backed artifact.
Normal research optimizes for root context efficiency. Deep research adds a small
frontier-root review between complete delegated rounds. Progress persistence is
selected independently from depth.

## Requirements

### Two Explicit Procedures

`research` is the lean default for broad read-only investigation.

`research-deep` is an explicit opt-in for investigations likely to need several
rounds or benefit from bounded root investigation between rounds. It specializes
normal research; it does not replace it or change the shared discovery cadence
used by `plan-create`.

### Mandatory Final Artifact

Every invoked `research` or `research-deep` run, whether completed or blocked,
must write one final root-owned artifact under an allowed artifact root. The
chat response is a concise receipt and summary, never the sole research output.
There is no inline-only completion path inside either skill.

The root artifact and final receipt declare `Status: Completed | Blocked`. A
blocked artifact identifies each blocker, its impact, and the smallest action
that could unblock the investigation. It must not look like a completed finding.

The default artifact is one findings file. When the user requests a multi-file
result, or progress files already created a bundle, the directory is the one
artifact and root-owned `RESEARCH.md` is its canonical entrypoint. It links every
final member in read order. Generated research remains evidence rather than
canonical product truth.

### Progress Modes

Depth and progress storage are independent. Resolve one mode before the first
delegated round:

- `transient` is the default. Workers return reports through the internal worker
  channel, the root keeps synthesis in context, and no progress files are
  written. The root writes the mandatory final artifact only at completion or
  blockage.
- `worker_reports` is selected when the user asks workers or subagents to write
  findings to disk. Workers write in exclusive directories while the root keeps
  synthesis in context. The root creates the bundle's `RESEARCH.md` only at
  completion or blockage.
- `recoverable` is selected by an explicit request for small-context,
  compaction-safe, memory-wipe-safe, resumable, or checkpointed research. Workers
  write reports and the root maintains `RESEARCH.md` throughout the run.

Using `research-deep` does not by itself authorize progress writes. Plain-language
requests select a mode; users do not need to know its formal name. Only
`recoverable` promises full root recovery after context loss. `worker_reports`
preserves evidence but not accepted root state or the next action. `transient`
provides no progress recovery guarantee.

### Orchestrated Research

When `task-orchestrator` owns one bounded research run, `recoverable` is
mandatory before its first delegated round. `transient` and `worker_reports` are
not valid orchestrated modes. `RESEARCH.md` is the recovery checkpoint and the
durable parent handoff.

It also carries or links every field required by the orchestrator handoff:
orchestration identity, interaction and authority state, complete child ledger,
completed and remaining work, accepted evidence and negative findings, material
decisions, verification gaps, changed artifact paths, scope deviations, blockers,
and one next root action. There is no second competing restart entrypoint.

Interactive is the default. A material question, scope change, permission
request, or approval gate is recorded in that handoff and returned to the
user-facing root; the orchestrator does not wait in a hidden session.

Autonomous operation requires an explicit user instruction. It may resolve only
in-scope questions and must record each material decision, alternatives,
rationale, confidence, and consequence in `RESEARCH.md`. It does not expand
scope, permissions, or research's read-only boundary, and cannot authorize
destructive or external work, credentials, or safety/privacy exceptions. An
unavoidable authority gap is blocked or deferred.

### Research Bundle

Any run that writes progress or has a multi-file final result creates one nested
bundle under the applicable existing `artifacts/investigations/` root. It must not
scatter worker or final-section files directly into `investigations/`.

In `recoverable` mode, `RESEARCH.md` is the sole restart entrypoint. The root
checkpoints it before dispatching a round, after the whole round is classified,
after any bounded root probe, and at completion or blockage. It records accepted
findings, evidence pointers, uncertainty, the stop-gate decision, and the exact
next action without copying raw reports. Its round ledger uses stable worker IDs
and records packet, report path, and `planned`, `running`, `completed`, `blocked`,
or `failed` status.

### Source-Read-Only Report Creation

`task-explore` remains non-mutating with respect to inspected systems. It may
create new Markdown research or review files only when a packet assigns one
exclusive output directory. It must not alter existing files or write outside
that directory. Packets writing into the Agents workspace must supply the owning
scope, artifact category, frontmatter values, and artifact-authoring convention.

In `worker_reports` and `recoverable` modes, the required worker entrypoint is
`REPORT.md`. A worker may add supporting Markdown only for materially distinct
evidence and must link it from the report. Each report contains required artifact
frontmatter first, then a compact decision card, then the complete evidence
required by the worker role. The worker returns only the card and paths through
the internal worker channel so detailed evidence does not bloat root context. In
`transient` mode, no output directory is assigned and the complete worker report
returns internally to the root.

### Complete-Round Boundary

The root does not analyze partial worker results, read source, or start another
round while a round is running. Before marking a round complete, it accounts for
every expected worker, including blocked or failed workers. It updates
`RESEARCH.md` immediately only in `recoverable` mode.

### Bounded Architect Probe

In `research-deep`, after every complete round the root challenges the current
direction without tools. It uses tools only when one specific contradiction,
missing dependency, or framing problem prevents a good next round.

One probe permits one narrow search returning at most 20 matching lines, two
targeted reads, 200 lines per read, 400 evidence lines total, three investigative
root tool calls total, and one reference hop. Search-result lines count toward the
evidence limit; required recoverable checkpoints do not count as investigative
calls. Reaching any limit ends the probe. Broad orientation, subsystem
archaeology, general worker re-verification, and discovery that can be delegated
remain forbidden.

### Compaction Recovery

In `recoverable` mode, a resumed root reads `RESEARCH.md` first and reconciles an
open round's worker ledger with its report files. It reattaches to a live worker
where supported; otherwise it marks that worker failed before deciding whether to
redispatch. It reads decision cards as needed, then opens full reports or source
only for disputed or decision-critical evidence. It must not reload every
completed report by default. Unindexed worker material is unaccepted evidence,
not active root state.

### Completion

Both procedures use the shared readiness gate and may end complete or blocked.
The final artifact contains the question, inspected sources, answer, material
evidence, residual uncertainty, and recommended next step. A bundle's final
`RESEARCH.md` contains that synthesis and links every final member. The artifact
is committed once at the end, not after every round. The final chat response must
include status, a concise summary, recommended next step, artifact path, and
commit status.
