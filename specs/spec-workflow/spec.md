---
created_at: 2026-06-29
updated_at: 2026-09-06
model: gpt-5.6-sol
doc_type: spec
purpose: Define the current Agents workspace spec-workflow behavior.
related:
  - path: ../../workflows/spec-workflow/AGENTS.md
    why: Executable workflow package that implements this spec.
  - path: ../../skills/plan-create/SKILL.md
    why: Canonical planning phase procedure for this workflow.
  - path: ../../skills/plan-execute/SKILL.md
    why: Canonical execution phase procedure for this workflow.
  - path: ../../skills/plan-reconcile/SKILL.md
    why: Canonical durable-memory reconcile procedure for this workflow.
  - path: ../../roles/task-explore.md
    why: Canonical source-read-only worker role for bounded investigation and review.
  - path: ../../roles/task-explore-high.md
    why: High-capability source-read-only overlay for larger bounded packets.
  - path: ../../roles/task-execute.md
    why: Canonical bounded mutation worker role for explicit packets.
  - path: ../../roles/task-execute-high.md
    why: High-capability mutation overlay for larger bounded coupled packets.
  - path: ../../roles/task-worker-tiers.md
    why: Portable worker model-tier semantics for spec-workflow delegation.
  - path: ../../roles/task-orchestrator.md
    why: Canonical frontier role for one-layer coordination of terminal workers.
  - path: ../project-memory/spec.md
    why: Defines durable project memory maintained by plan-reconcile.
---

# Spec Workflow Spec

The Agents workspace spec workflow is the canonical OpenSpec-inspired workflow for
serious durable agent work. It exists to keep agent performance high even when
worker models are cheaper, weaker, or context-limited.

## Requirements

### Fresh Phase Execution

Serious work must be split into fresh top-level phases when the change needs
restartability, delegation, scoped changes, verification, or durable memory
reconciliation.

The standard phases are:

```text
plan-create -> plan-execute -> plan-reconcile
```

No phase may rely on prior chat context for correctness.

The canonical phase procedures live under root `skills/`:

```text
skills/plan-create/SKILL.md
skills/plan-execute/SKILL.md
skills/plan-reconcile/SKILL.md
```

The `workflows/spec-workflow/` package composes those skills with templates and
references. It must not recreate workflow-local `skills/` or `subagents/`
directories.

### Model-Tier Boundary

Top-level phase agents own reasoning, judgment, integration, verification, and
acceptance. Worker agents execute bounded packets with explicit context and low
need for independent reasoning.

Canonical worker role contracts live under root `roles/`:

```text
roles/task-explore.md
roles/task-explore-high.md
roles/task-execute.md
roles/task-execute-high.md
```

Workers must not spawn, call, or coordinate other workers. Workers must not
decide durable truth.

`task-explore` is source-read-only, not report-output-disabled. When a packet
assigns one exclusive output directory, it may create new Markdown research or
review files there while remaining forbidden from modifying existing files,
source, product state, plans, specs, or durable memory.

Tool-specific adapters may expose default, `fast`, and `high` wrappers around the
canonical worker roles. Concrete provider, model, service-tier, reasoning, and
fallback choices belong in tool-specific adapter docs or native config. Every
delegated worker must resolve to an explicit non-frontier model rather than
inheriting the phase model.

The default worker tier is a cheap micro worker for small bounded delegation. The
`fast` tier has equivalent micro scope and may be used only when the user
explicitly requests hurry mode. The `high` tier is a stronger non-frontier worker
for bounded work that is irreducibly coupled, context-heavy, difficult, or
consequential. It requires a richer handoff and remains below the phase agent.
Worker output must be validated before it affects planning, acceptance,
verification, or durable truth, with stricter corroboration for micro output.

Worker packets must be right-sized to the worker's practical context budget. A worker's
quality collapses once its context is compacted, and it will still return a
confident but degraded and partly invented result, so the phase agent sizes each
packet to finish well under that limit, splits a surface that is too large into
several disjoint parallel packets rather than overloading one worker, and avoids
fragmenting work into trivially tiny packets. Because the root cannot read a
worker's live context, sizing uses observable proxies such as reading breadth and
approximate input characters, tool-call volume, and runtime. Prefer broad
parallelism through disjoint micro packets, and escalate only an irreducible
bounded slice to high. The portable sizing and trust rules live in
`../../roles/task-worker-tiers.md`.

### Frontier Orchestration

A root frontier session may delegate one workflow phase or bounded ad hoc queue
to a frontier `task-orchestrator`. It is a distinct role, not a worker tier. The
only permitted delegation graph is:

```text
root frontier session
  -> task-orchestrator
       -> task-explore | task-explore-fast | task-explore-high
       -> task-execute | task-execute-fast | task-execute-high
```

The root may launch orchestrators sequentially, or in parallel only after it
determines their work is independent. An orchestrator may not launch another
orchestrator or a generic native agent. Leaves remain non-recursive and terminal.
Direct root-to-leaf delegation remains valid when no orchestrator owns that
bounded unit.

Every orchestrator packet selects `interactive` or `autonomous`; interactive is
the default. Interactive material questions and approval gates return to the
user-facing root through a durable handoff. Autonomous operation requires an
explicit user instruction, may resolve in-scope decisions and treat that
instruction as delegated plan approval, and records the selected option,
alternatives, rationale, confidence, and consequence. It never expands scope,
grants permissions, authorizes destructive or external actions, invents
credentials, or bypasses safety and privacy limits. An authority gap is blocked
or deferred.

Existing phase artifacts remain canonical and serious workflows use fresh
orchestrators for `plan-create`, `plan-execute`, and `plan-reconcile`. An
interactive delegated plan creation may write one non-executable pre-approval
handoff, but must not create an executable change folder or claim approval.
Every handoff records status, canonical paths, completed and remaining work,
decisions and alternatives, approval and authority state, verification evidence
and gaps, risks, blockers, and one next root action. Parent returns contain only
the status, handoff path, and that action.

### Discovery Cadence

`plan-create` must research via a delegation-first, idle-per-round,
coarse-to-fine loop. The root planner orients cheaply, delegates breadth to
bounded `task-explore` workers, and does not read broadly or analyze partial
results while a round is running, so its context stays lean. Discovery refines
across rounds and stops as soon as the `PLAN.md` execution contract is
confidently fillable; round and file counts are guardrails, not quotas. The
detailed procedure lives in
`workflows/spec-workflow/references/discovery-cadence.md`. This requirement
currently applies to `plan-create`.

### Approval Gate

After discovery and before approval or executable change-folder creation,
`plan-create` must produce a concrete, human-readable implementation proposal.
The proposal must expose enough of the selected design, responsibility
boundaries, important names, intended edit surfaces, execution shape, and
verification bar for a human engineer to identify overengineering, duplication,
misplaced ownership, confusing naming, and missing regression coverage.

Questions must refine disclosed decisions rather than substitute for an
undisclosed plan. Interactive runs require explicit human approval; answering a
clarification or acknowledging the proposal does not by itself constitute
approval. An interactive orchestrated run may write one non-executable recovery
handoff before approval, but no executable change folder.

An autonomous orchestrated run requires explicit up-front user instruction. That
instruction delegates approval for decisions inside the stated scope and
permissions. The orchestrator records each material choice, alternatives,
rationale, confidence, and consequence. Delegated approval cannot expand scope,
grant missing permissions, authorize destructive or external actions, invent
credentials, or bypass safety and privacy limits; those items are deferred or
blocked.

Material changes to scope, architecture, responsibility ownership, important
names or edit surfaces, dependency shape, or verification expectations require a
revised proposal and renewed interactive approval or a fresh check against the
autonomous authority boundary. The approved direction and resolved decisions
must be preserved in `PLAN.md` so later phases do not depend on chat context.

### Verbatim Critical Content

When the exact wording of an artifact is the deliverable, `plan-create` must
author the final text itself and persist it verbatim in the change folder before
execution. Critical content includes a new spec, a spec delta, durable memory, a
convention, skill, role, workflow, or `AGENTS.md` guidance file, an exact
migration or config, and anything the user flags as critical, delicate, or
irreversible.

The phase agent must not hint at critical content, leave it for `plan-execute` to
compose, or delegate its authoring to a worker. A worker may only mechanically
apply text the phase agent already wrote word for word; it must never originate,
draft, or paraphrase critical content. A new spec's change-folder
`specs/<domain>/spec.md` delta holds the final spec text, and a critical edit to
an existing file is captured as an exact diff in `PLAN.md` or a dedicated
proposed-changes file.

A change folder is complete for critical content only when a fresh,
memory-wiped `plan-execute` session could apply the change from the change folder
alone without inventing wording. This is the standing expectation for
`plan-create`, not an option the user must request per run.

### Scoped Changes

Reviewable durable changes should use
`changes/<YYMMDD_HHMM__semantic-slug>/` in the root scope for global or
cross-project work, or
`projects/<repo>/changes/<YYMMDD_HHMM__semantic-slug>/` for repo-specific work.
The change folder is the execution packet for `plan-create`, `plan-execute`, and
`plan-reconcile`.

A change may mirror affected current specs under
`changes/<YYMMDD_HHMM__semantic-slug>/specs/<domain>/spec.md` so the proposed
delta has an obvious merge target.

Root `changes/` is only for global Agents workspace behavior, conventions, or
cross-project changes. Project-specific changes belong under
`projects/<project>/changes/`. Do not create change folders under nested
projects, epics, initiatives, pillars, specs, or artifacts.

### Current Specs

Durable behavior, contracts, protocols, and requirements that future agents
should treat as current truth should live in `specs/<domain>/spec.md` in the
declared owning scope.

Not every change is a spec change. Use specs when behavior needs durable source
of truth beyond a result file.

### Change Folders

Serious execution work should use change folders with uppercase canonical files
such as `PLAN.md`, `EXECUTION_LOG.md`, and `RESULT.md`. Use `subtasks/`,
`followups/`, and `results/` inside the change folder for worker packets and
worker reports when decomposition is useful.

`PLAN.md` includes a compact structured execution contract in frontmatter. The
contract declares scope, affected projects/repos, allowed and forbidden paths,
required and optional reads, verification requirements, worker strategy,
permission posture, and plan-reconcile expectations. The plan body explains the
rationale and details. If the structured contract conflicts with the prose plan,
the executing phase agent must stop for clarification or update the plan before
continuing.

`RESULT.md` includes a compact `Context Used` receipt for material reads,
intentionally skipped context categories, stale or confusing context, and
prune/update candidates. It is not a transcript and must not require browsing
unused docs.

`RESULT.md` is also the canonical per-change git/PR provenance record. It
should capture only the final known lightweight facts future agents need to
trace execution back to source-control review state, such as source repo,
branch, compare base, head commit, and PR URL/status. The workflow must not
require broad git-history scans just to populate this section. If a later
commit/push/PR step runs while the same change folder is still active, that step
should update `RESULT.md` rather than inventing another provenance record.

Worker packets declare worker model-tier suitability and judgment boundaries.
Use `default` for small micro packets and `fast` only for explicit user-requested
hurry mode. Use `high` for bounded packets whose coupling, context, difficulty, or
importance exceeds the micro envelope. Use `phase_owned` as a non-dispatch ownership marker
when the top-level phase agent must own the judgment; it is not a model tier or
native worker wrapper.

Existing `artifacts/tasks/` folders remain valid legacy records, but new serious
spec-workflow work must not create task-folder-style execution packets there.

### Source Checkout Selection

Project guidance may define named source-checkout selectors and a project
default. `source_checkout` is optional in `PLAN.md`; when absent, the owning
project default or current existing behavior applies, so existing plans without
the field remain valid. A project whose existing behavior uses its primary
checkout therefore continues to use primary when the field is omitted. Only an
explicit non-default selection is persisted.

`plan-create` resolves and validates the effective selector before code/source
discovery, discloses the selector and resolved absolute working directory in the
human review proposal, and persists an explicit non-default selector. Validation
checks the path, Git top-level, and repository identity. `plan-execute` resolves
the plan selector or project default, may add an explicit invocation selector
before source work, and stops for confirmation when it conflicts with an
existing selector. The process CWD never silently overrides a project default or
approved selector.

Every source, test, or Git worker packet receives the effective selector,
resolved absolute working directory, and expected repository identity. Workers
must use that directory rather than infer one from their CWD. `plan-reconcile`
follows the selector recorded in `PLAN.md`/`RESULT.md` for source confirmation.
The stable selector catalog belongs in project guidance; selected-lane and
resolved-path provenance must not leak into product/spec memory.

### Lane Claim Ledger

A project with a managed multi-checkout catalog may define a lane claim ledger:
a single operational file, one row per managed non-default checkout, recording
whether each is `FREE`, `BUSY`, or `HELD` and by what work. It exists so a human
or agent can ask for a free checkout instead of tracking ownership by memory.

The ledger is operational coordination state, not durable product/spec memory:
`plan-reconcile` and `memory-reconcile` do not subject it to memory update
triage, and it stays out of the checkout-neutral product/spec memory above.

Its cost stays near zero. A session edits only its own checkout's row, in place,
never reordering the file, so concurrent sessions in the shared workspace do not
clobber claims; the edit rides in the commit the phase already makes. `plan-create`
(or ad hoc source work) claims a `FREE` row `BUSY` and never resolves to a row
another active session owns. `plan-execute` keeps the row current and downgrades
to `HELD` with a reason on a blocked finish or a reuse-blocking condition.
`plan-reconcile` and `memory-reconcile` release the row to `FREE` once the work is
durably captured and the checkout is reusable. The project owns the concrete
status vocabulary, release criteria, blocking reasons, and any stale-reclaim rule.

### Verification Gate

`plan-execute` must not mark serious work complete until required subtasks and
followups are complete or explicitly deferred, worker outputs are inspected,
verification is run or skipped with reason, nontrivial output receives
review/verify coverage or an explicit skip reason, and reconcile inputs are
prepared.

### Attempt Budget

Worker packets should set an attempt budget. The default maximum is three
serious attempts. Repeated failure, ambiguous behavior, forbidden scope, missing
context, or unclear verification must stop the worker and escalate to the phase
agent.

### Non-Engineering Work

The workflow may be used for non-engineering tasks when durable planning,
evidence gathering, synthesis, review, or memory reconciliation is useful. In those
cases, workers still operate from bounded packets and current truth still
reconciles into durable memory.

## Non-Goals

- Do not force the spec workflow onto trivial chat sessions or small edits.
- Do not import the full OpenSpec toolchain or folder structure.
- Do not make worker agents recursive coordinators.
- Do not migrate legacy task folders or handoffs only for consistency.
- Do not use `artifacts/tasks/` for new serious spec-workflow execution packets.
