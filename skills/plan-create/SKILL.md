---
name: plan-create
description: Create a standalone Agents workspace spec-workflow change folder for serious durable work after interactive review or explicit autonomous delegated approval.
created_at: 2026-06-29
updated_at: 2026-09-25
model: gpt-5.6-sol
doc_type: skill
purpose: Define the plan-create phase for the Agents workspace spec workflow.
related:
  - path: ../../workflows/spec-workflow/AGENTS.md
    why: Workflow invariants and composition rules for the spec workflow.
  - path: ../../workflows/spec-workflow/references/change-folder-contract.md
    why: Defines change-folder structure and file roles.
  - path: ../../workflows/spec-workflow/references/discovery-cadence.md
    why: Delegation-first discovery cadence this phase must follow before deciding scope.
  - path: ../../roles/task-explore.md
    why: Read-only micro worker role available for bounded planning discovery.
  - path: ../../roles/task-worker-tiers.md
    why: Portable worker model-tier semantics for planning delegation.
  - path: ../../conventions/artifact-authoring.md
    why: Write-time contract for change-folder and artifact locations, naming, and frontmatter.
  - path: ./references/human-review-proposal.md
    why: Mandatory late-loaded template and quality contract for interactive or autonomous implementation review.
---

# Plan Create

You are the high-reasoning root planner. Fully investigate the work, agree the
direction with the human, then write a standalone, reviewable change folder. Do
not implement product/source changes in this phase.

Three responsibilities define this phase:

- **Own discovery to closure.** Resolve the unknowns now, using delegated
  sub-agents, so the plan is set in stone before it is written. Do not defer
  resolvable discovery or validation to `plan-execute`.
- **Author critical content verbatim.** When the exact wording is the deliverable
  (a new spec, a spec delta, durable memory, guidance, or another critical or
  irreversible artifact), write the final text yourself and persist it in the
  change folder. Do not hint at it and do not delegate its authoring to a
  subagent. See "Critical Content Is Phase-Owned And Written Verbatim" below.
- **Resolve the approval gate before writing an executable plan.** Interactive
  runs present a readable proposal and get explicit sign-off. An explicitly
  autonomous orchestrated run may use the user's up-front delegated approval,
  subject to the narrower authority rules below.

## Phase Order

Run these in order. No executable change folder is written or committed before
interactive approval or valid autonomous delegated approval. An interactive
orchestrated run may write only the non-executable recovery handoff described
below.

1. Inputs - load routing and memory anchors.
2. Source Checkout Resolution - resolve and validate the effective checkout
   before any code/source discovery.
3. Discovery Cadence - delegate discovery to closure while protecting root
   context.
4. Required Decisions - synthesize the proposed direction.
5. Approval Gate - present the implementation review snapshot, then either obtain
   interactive approval or apply explicit autonomous delegated approval.
6. Change Folder - write the change folder and artifacts, only after approval.
7. Commit Gate - commit the plan-create output.
8. Final Output - report what was written and the approved decisions.

## Delegation Availability

The root owns this phase unless it explicitly assigns it to a verified
`task-orchestrator`.
Before dispatching any worker, read `../../roles/task-worker-tiers.md`; it permits
enabled micro and high wrappers and defines the packet and concurrency limits.

## Inputs

- user request
- nearest applicable `AGENTS.md`
- nearest applicable `STATE.md` when it exists
- `../../conventions/artifact-authoring.md` before creating the change folder or
  any generated file (write locations, naming, frontmatter)
- relevant live specs, project memory, source files, docs, and artifacts only as
  needed

## Source Checkout Resolution

Before code/source discovery, inspect the applicable project guidance for named
source-checkout selectors, its default, and any managed-session opt-in. Capture
the initial session workspace once before tools change directories. Resolve an
explicit invocation selector first. Otherwise, for an opted-in project, resolve
the captured path only when it is at or below exactly one managed checkout root
whose path, Git top level, and repository identity validate. A later `cd` never
reselects the checkout, and an unrecognized initial workspace falls back to the
project default rather than selecting arbitrary source. When no managed-session
contract exists, preserve the project's current default behavior. If the chosen
selector fails validation, stop before discovery rather than guessing.

Disclose the effective selector, selection origin, whether it is the default, and
the resolved absolute working directory in the human review proposal. Persist
`source_checkout` in a new `PLAN.md` whenever the effective selector is
non-default, including when the validated initial session workspace selected it;
leave it absent for the default. Pass the effective selector, resolved absolute
working directory, and expected repository identity to every source, test, Git,
or checkout-bound runtime/browser worker packet.

When project guidance defines a lane claim ledger for its managed non-default
checkouts, do not resolve to a lane whose ledger row is already owned by another
active session; stop and ask rather than double-booking it. Disclose the intended
lane and its current claim in the review snapshot. After approval, mark the
claimed lane `BUSY` with its branch and this change folder in the same commit
that writes the change folder, editing only that lane's row in place per the
ledger's rules.

## Parallel Checkout And Runtime Planning

Keep ordinary plans single-checkout and omit a checkout allocation table. A user
request may motivate a parallel proposal, but allocate additional managed
checkouts only after the human-approved execution strategy explicitly selects
parallel or multithreaded work. The root phase records the packet owner,
selector, resolved path, repository identity, and lifecycle for each allocation;
workers never choose or coordinate checkouts.

Allocate a runtime only when execution or browser verification needs one. An
ordinary plan may own at most one active runtime. Multiple simultaneous runtimes
require the same approved parallel strategy as multiple checkouts. Record the
checkout, resolved working directory, instance or identifier, exact URL, process
owner, reuse permission, and stop or handoff responsibility. Mark packets that do
not need a runtime with `Runtime Target: n/a`; selection alone never starts a
process.

Browser checks use a bounded `task-execute` worker on an affordable tier, and the
phase agent never calls browser tools directly.

## Discovery Cadence

Research this task by following
`../../workflows/spec-workflow/references/discovery-cadence.md`. The short form:
orient cheaply, delegate a round of disjoint `task-explore` workers, idle until
the whole round returns, integrate and optionally read a few decision-critical
files, refine with more rounds only if needed, and stop as soon as you can
confidently fill the `PLAN.md` contract. Protect root context: do not read
broadly yourself or analyze partial results mid-round. The `## Required
Decisions` below are the output of this cadence.

Own discovery to closure. The reason this phase leans so heavily on sub-agents
is to resolve the unknowns during planning without exhausting root context, so
the plan is set in stone before the review gate. Run as many readiness-gated
parallel `task-explore` rounds as needed - including sharper follow-up rounds
whose only purpose is to verify or validate a hypothesis - not a single fixed
round. The stop-early gate (you can confidently fill the `PLAN.md` contract) is
the only stop condition; the "about 3 rounds" figure in the cadence is a soft
default, not a cap. Do NOT defer resolvable discovery, validation, or a
"figure this out later" to `plan-execute`; that defeats the purpose of planning.
A genuinely execution-time-only unknown may be deferred only as an explicit,
bounded, declared `plan-execute` investigation subtask with a stated reason,
never as accidental punting.

## Required Decisions

- Owning scope: root or repository project.
- Change folder path and concise kebab-case change slug.
- Structured `PLAN.md` execution contract fields, including allowed paths,
  forbidden paths, required reads, verification, worker strategy, permission
  profile, and plan-reconcile expectations.
- Planning tier: inline answer for trivial work, minimal change folder, or
  multi-subtask change folder.
- Whether `MEMORY_DELTA.md` is needed.
- Whether worker subtasks are needed.
- Parallel-safe work, sequential dependencies, critical path, and stop
  conditions.
- Whether approved parallel checkout allocations or runtime targets are needed,
  who owns them, and their lifecycle boundaries.
- Verification strategy and completion criteria.
- Concrete implementation review inputs: current-to-target design, responsibility
  boundaries, important proposed names, expected edit surfaces, and material
  alternatives or assumptions.

## Approval Gate

Before writing or committing an executable change folder, resolve the approval
mode. Interactive runs put the human in the loop and block for explicit approval.
An interactive orchestrated run may first write one non-executable recovery
handoff under an allowed `artifacts/handoffs/` root. Autonomous orchestrated runs
may proceed from explicit up-front delegated approval when they remain inside the
stated scope and permissions. The review must not depend on reading the eventual
agent-optimized `PLAN.md`.

After discovery reaches closure and before asking any clarifying question, read
`./references/human-review-proposal.md` and present its **Implementation Review
Snapshot**. Follow that reference's required headings, concrete-content rules,
tier scaling, question integration, and approval semantics. This late read keeps
the detailed template out of discovery context while making it mandatory at the
review gate.

The snapshot is the primary design review, not a progress summary. It must let a
human engineer review the intended current-to-target design, responsibility
boundaries, important names, concrete edit surfaces, execution shape,
alternatives, risks, and behavioral verification without opening the eventual
agent-optimized `PLAN.md`. Questions refine this disclosed proposal; they do not
replace it.

The snapshot must disclose the checkout selection origin and any proposed
parallel checkout or runtime allocations. Additional checkouts or multiple
simultaneous runtimes are not authorized until the human approves that execution
shape.

In interactive mode, after the snapshot ask **clarifying questions** using the runtime's structured
multiple-choice question mechanism when available, otherwise clearly labeled
options in the reply. Ask only about material decisions that discovery cannot
resolve, and tie every question to the affected snapshot section and practical
impact.

In interactive mode, always ask a **final gate question**, even when no clarifications are needed:
does the human approve the current snapshot - proceed, change direction, or "I
have questions to clarify first". Approval covers its outcome, boundaries,
design, ownership, important names, edit surfaces, execution shape, and
verification bar. An acknowledgement or answer to a clarification is not
approval. Honor the loop: answer the engineer's own questions before proceeding,
and re-present the complete current snapshot when a material decision changes.
Uncertainty or a hunch is a valid reason to keep clarifying.

In autonomous orchestrated mode, do not ask those questions. Resolve each
in-scope decision using the strongest available evidence and record the selected
option, alternatives, rationale, confidence, and consequence. The user's explicit
autonomous instruction is the approval evidence. It does not authorize scope
expansion, missing permissions, destructive or external actions, credentials, or
safety/privacy exceptions; defer or block those items instead.

If answering feedback needs more investigation, dispatch another parallel
`task-explore` round rather than reading broadly on the root, then re-present.

Do not create the change folder or commit until the current snapshot has either
interactive human approval or valid autonomous delegated approval. Before
writing, compare the intended `PLAN.md` scope,
design, edit map, execution graph, and verification strategy with that snapshot.
Any material delta defined by the reference returns to the review gate. Once
approved, capture the direction, answered clarifications, and any reapproval
evidence durably in `PLAN.md`; `plan-execute` must not need chat context.

## Change Folder

Create a `changes/<YYMMDD_HHMM__semantic-slug>/` folder for all serious durable
work that needs restartable planning, execution, verification, or memory
reconciliation.

Use only these roots:

```text
changes/<YYMMDD_HHMM__semantic-slug>/
projects/<project>/changes/<YYMMDD_HHMM__semantic-slug>/
```

Do not create change folders under nested projects, epics, initiatives, pillars,
specs, or artifacts. When working through a repo-local `agents/` symlink,
repo-specific work may use `agents/changes/<YYMMDD_HHMM__semantic-slug>/`,
which resolves to the project Agents workspace change root.

Within a change folder, mirror affected specs under `specs/<domain>/spec.md` only
when the change proposes a durable spec delta. The mirrored spec path must make
the merge target obvious.

## Change Folder Outputs

For serious changes, create uppercase canonical files in the change folder:

```text
AGENTS.md
PLAN.md
EXECUTION_LOG.md
RESULT.md
```

Create only when useful:

```text
MEMORY_DELTA.md
RECONCILE_PACKET.md
subtasks/
followups/
results/
specs/
```

## Critical Content Is Phase-Owned And Written Verbatim

For some work the exact wording is the deliverable. Treat as critical content:

- a new spec or a spec delta,
- durable memory (`STATE.md`, `DECISIONS.md`, `SOURCES.md`, `CODEMAP.md`, and the
  like),
- a convention, skill, role, workflow, or `AGENTS.md` guidance file,
- a migration, schema, or config whose text must be exact,
- anything the user flags as critical, delicate, or irreversible.

For critical content the phase agent writes the exact final text itself and
persists it verbatim in the change folder before execution:

- Author the real content, not a hint, an outline, or a "write a spec about X"
  note. A new spec's `specs/<domain>/spec.md` delta in the change folder holds
  the final spec text. For a critical edit to an existing file, capture the exact
  diff (current lines plus exact proposed lines) in `PLAN.md` or a dedicated
  proposed-changes file so nothing is left to compose later.
- Do not delegate authoring critical content to a subagent. Workers are prone to
  mistakes and hallucination, and this is content where a single wrong word
  matters. A worker may only mechanically apply text you already wrote word for
  word; it must never originate, draft, or paraphrase it.
- Make `plan-execute` a copy-paste job. A fresh execution session may start with
  compacted or wiped memory, so the durable change folder must already contain
  everything needed to apply the change with zero invention. If a memory-wiped
  executor could not reproduce the change from the change folder alone, the plan
  is not finished.

This is the standing expectation for `plan-create`, not an extra the user must
request each time. When unsure whether content is critical, treat it as
critical.

## Worker Packet Strategy

Prefer bounded workers when they reduce root context load. Do not create
subtasks when one standalone plan is simpler and safe.

After the direction is approved, protect root context while writing. When the
plan is large, you may delegate purely mechanical drafting to `task-execute`
workers with explicit paths and acceptance criteria: subtask packet scaffolding,
frontmatter, status fields, and applying content you already authored verbatim.
Never delegate authoring critical content itself (see "Critical Content Is
Phase-Owned And Written Verbatim"): the phase agent writes specs, spec deltas,
durable memory, and other critical text word for word. Keep `PLAN.md` and the
human review proposal phase-owned. This keeps the root from exhausting context
and triggering compaction mid-write.

Right-size every worker packet before dispatch. A packet must be small enough for
the worker to finish well under its context limit; split a large surface into
several disjoint parallel packets rather than overloading one worker past its
compaction cliff, and do not fragment work into trivially tiny packets either.
See the sizing rule in `../../roles/task-worker-tiers.md`.

Always dispatch through the non-frontier `task-explore` / `task-execute` wrapper
family; never spawn a native/generic subagent or any worker that inherits this
phase's frontier model. See the hard rule and delegation economics in
`../../roles/task-worker-tiers.md`.

Set the `PLAN.md` `worker_strategy` fields before creating subtasks. Prefer
enabled default `task-explore` or `task-execute` for tiny, disjoint packets;
use enabled high counterparts for any real bounded delegated task with several
steps or coupled reasoning. Fast wrappers remain disabled; normal orchestration
requires a verified active-tool mapping.
See `../../roles/task-worker-tiers.md`.

Each worker packet must include:

- one objective
- required read set
- allowed edits
- forbidden edits
- known facts and assumptions
- dependencies and parallel-safety
- acceptance criteria
- verification expectations
- worker model tier, judgment boundary, max files to read, attempt budget, and
  stop conditions; high packets also state why micro decomposition is unsafe,
  their estimated working-material budget, finite deadline, and rich handoff path
- exact report path and report shape; browser verification packets must report
  pass/fail, observed differences, driver and tool status, session isolation, and
  page cleanup

Use `worker_model_tier: default` for small micro packets. Use
`worker_model_tier: fast` only for explicit user-requested hurry mode. Use
`worker_model_tier: high` for bounded, irreducibly coupled, context-heavy, or
consequential packets that satisfy the high-tier handoff contract. Use
`worker_model_tier: phase_owned` for work that must stay with the top-level
phase agent and should not be dispatched. Workers should not need hidden chat
context or broad source archaeology.

## Memory Delta

Create `MEMORY_DELTA.md` when the change may affect durable memory, including
`STATE.md`, `DECISIONS.md`, `SOURCES.md`, `CODEMAP.md`, current specs,
change-local spec deltas, or artifact staleness.

If no memory delta is needed, record why in `PLAN.md`.

## Commit Gate

Plan-create writes durable Agents workspace markdown that must be tracked. After writing
the change folder and any required scoped `STATE.md` updates,
the phase must create a semantic Agents workspace git commit for its own output when the
changes are safely separable.

This workflow instruction is explicit authorization to commit the plan-create
Agents workspace output. Do not treat generic "commit only when explicitly requested"
guidance as a reason to leave plan-create artifacts uncommitted.

Before committing:

- Run `git -C ~/agents status --short`.
- Inspect the Agents workspace diff and include only current-task files.
- Do not stage or commit unrelated pre-existing dirty files.

If a commit cannot be created because the worktree contains inseparable unrelated
changes, state that exact reason in the final response. Otherwise the final
response must include `Agents commit: <hash>`.

## Final Output

The human already reviewed and approved the direction at the review gate, so
this is a post-write report, not the place to raise first-time questions. After
writing the change folder, respond with:

- change folder path
- selected scope and tier
- whether subtasks were created
- execution graph
- verification strategy
- plan-reconcile expectations
- a short record of the approved direction and any resolved clarifications
- `Agents commit: <hash>` or the exact reason no commit was created
