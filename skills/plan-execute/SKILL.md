---
name: plan-execute
description: Execute an approved Agents workspace spec-workflow PLAN.md to completion or a clear blocked result while preserving root-agent ownership of orchestration and durable truth.
created_at: 2026-06-29
updated_at: 2026-09-25
model: gpt-5.6-sol
doc_type: skill
purpose: Define the plan-execute phase for the Agents workspace spec workflow.
related:
  - path: ../../workflows/spec-workflow/AGENTS.md
    why: Workflow invariants and composition rules for the spec workflow.
  - path: ../../workflows/spec-workflow/references/change-folder-contract.md
    why: Defines change-folder structure and execution files.
  - path: ../../roles/task-explore.md
    why: Read-only worker role for bounded investigation, review, and verification.
  - path: ../../roles/task-execute.md
    why: Bounded mutation worker role for explicit execution packets.
  - path: ../../roles/task-worker-tiers.md
    why: Portable worker model-tier semantics for dispatch and validation.
---

# Plan Execute

You are the high-reasoning root executor. Execute an approved change folder's
`PLAN.md` to completion or a clear blocked result. Own orchestration, judgment,
verification, followups, and final acceptance.

## Required First Reads

Read only the execution contract first. Start with the structured `PLAN.md`
frontmatter, then read the supporting plan body and status files:

- change `AGENTS.md` if present
- `PLAN.md`
- `EXECUTION_LOG.md`
- `RESULT.md`
- `MEMORY_DELTA.md` if present

Then read subtasks, followups, worker results, source files, tests, docs, and
change-local spec deltas only as needed.

## Delegation Availability

The root owns this phase unless it explicitly assigns it to a verified
`task-orchestrator`.
Before dispatching any worker, read `../../roles/task-worker-tiers.md`; it permits
micro and high wrappers and defines the packet and concurrency limits.

## Execution Rules

- Do not replan from scratch unless the plan is invalid or obsolete.
- Before source operations, resolve `source_checkout` from `PLAN.md` when it is
  present; otherwise use the owning project's default or current existing
  compatibility behavior. Once a plan exists, its selector or intentional
  omission governs; the execution session's launch workspace does not reselect
  it. An explicit invocation selector may be persisted in `PLAN.md` as a
  non-default selector before source work begins. If it conflicts with an
  existing plan selector or intentional omission, stop for confirmation rather
  than silently changing the approved checkout.
- Validate the resolved checkout path, Git top-level, and repository identity
  before any source operation. The process CWD never silently overrides the
  project default or an approved selector.
- Propagate the effective selector, resolved absolute working directory, and
  expected repository identity to every source, test, Git, or checkout-bound
  runtime/browser worker packet.
- Ordinary plans use one effective checkout. Validate every additional packet
  allocation independently and dispatch it only when the human-approved
  execution strategy explicitly authorizes parallel or multithreaded work.
  Simultaneous mutating packets must use different checkouts; workers never
  choose, reserve, or coordinate allocations.
- Allocate a runtime only when a packet needs execution or browser verification.
  An ordinary plan may own at most one active runtime; multiple simultaneous
  runtimes require the same approved parallel strategy as multiple checkouts.
  Propagate the runtime's checkout, resolved working directory, instance or
  identifier, exact URL, process owner, reuse permission, and stop or handoff
  responsibility. Packets without runtime needs receive `Runtime Target: n/a`.
  Never start a process merely because a checkout was selected.
- Browser checks: delegate probes to a bounded `task-execute` worker on an
  affordable tier; the phase agent must never call browser tools directly.
- Resolve checkout, branch, worktree, commit, push, and PR permissions before
  taking those actions.
- Do not create or update a PR unless the user requested PR work or the approved
  plan contains an explicit PR creation/update step.
- When PR work is requested after a delegated plan execution, prefer a bounded
  `task-execute` PR-publication packet for diff/body preparation and PR mechanics
  if that keeps the phase thread from absorbing large PR-writing context. For
  tiny one-worker changes, the phase agent may do the PR work directly.
- Always dispatch through the non-frontier `task-explore` / `task-execute`
  wrapper family; never spawn a native/generic subagent or any worker that
  inherits this phase's frontier model. See the hard rule and delegation
  economics in `../../roles/task-worker-tiers.md`.
- Dispatch `task-execute` workers for bounded code, test, verification-command,
  memory-patch, or mechanical-doc packets when useful.
- Dispatch `task-explore` workers for bounded investigation, code/test discovery,
  review, or verification checks; for interactive browser checks, use a
  delegated `task-execute` worker and never browse from the phase agent.
- Prefer parallel default micro workers for truly tiny, independent packets and
  high workers for real bounded tasks with multiple steps or coupled work. Validate
  their reports, relevant diffs, and verification evidence strictly before
  accepting output. A micro run beyond the three-to-four-minute quality threshold
  is suspect unless its packet names a known external wait.
- Do not use fast wrappers. A normal orchestrator requires a verified mapping
  and an explicit bounded phase assignment. Use high workers for bounded
  coupled tasks, split truly independent micro packets, or keep unbounded work
  in the root.
- Before dispatching a worker, validate the packet against the `PLAN.md`
  structured contract: allowed paths, forbidden paths, required reads,
  `worker_strategy`, and the packet's worker model tier and judgment boundary.
- Do not dispatch packets marked `worker_model_tier: phase_owned`; the phase
  agent owns that judgment and integration work.
- Give each worker exactly one packet plus explicitly listed context.
- Workers write result files under the change folder's `results/` when a result
  path is provided.
- Inspect worker reports and relevant diffs before accepting work.
- Use review or verify workers for nontrivial outputs unless skipped with a
  recorded reason.
- Create narrow followups when worker output is incomplete, wrong, or reveals new
  bounded work.
- Update `PLAN.md` only when scope, dependency graph, stop conditions, or
  execution strategy changes, or when recording an explicit non-default
  invocation selector before source work after the conflict check above.
- Record meaningful events in `EXECUTION_LOG.md`; do not write a transcript.
- Keep `RESULT.md` `## Git Provenance` current when execution creates or changes
  branch, commit, push, or PR state, using only cheap facts already available
  during the work.
- Keep the `Source checkout` provenance line in `RESULT.md` current with the
  effective selector and resolved absolute working directory used for source
  confirmation.
- Keep any checkout/runtime allocation summary in `RESULT.md` compact and current
  when execution used additional checkouts or owned runtimes.
- When project guidance defines a lane claim ledger and this plan works a managed
  non-default checkout, keep that lane's ledger row current: refresh its branch,
  change/task, and timestamp as execution proceeds, editing only that row in
  place. On a blocked finish, or when you leave an owned runtime running or any
  other reuse-blocking condition, set the row `HELD` with the reason rather than
  leaving it silently `BUSY`. Releasing to `FREE` is `plan-reconcile`'s job.

## Verification Gate

Before marking work complete:

- required subtasks and followups are completed or explicitly deferred
- accepted worker outputs match their packets
- relevant verification ran or was skipped with reason
- nontrivial work received review or verify coverage, or the skip reason is
  recorded
- known gaps have followups or explicit deferrals
- unrelated scope creep is absent
- private workflow details are not leaked to reviewer-facing output
- `RECONCILE_PACKET.md` is prepared in the change folder for serious changes

## Stop Conditions

Stop and write a blocked `RESULT.md` when any are true:

- the plan is wrong, obsolete, or underspecified
- required edits exceed allowed scope
- a packet fails after three serious attempts
- the same verification failure repeats without new information
- more than three followups are required unless the user configured otherwise
- unrelated dirty files block safe execution
- requested git or PR behavior is not authorized
- product behavior, durable truth, or verification remains unclear

## Reconcile Inputs

For serious changes, write or update:

- `RESULT.md`
- `EXECUTION_LOG.md`
- `RECONCILE_PACKET.md`
- `MEMORY_DELTA.md` when durable memory may change

Fill `RESULT.md` `## Context Used` with only materially relevant reads, skipped
context categories, stale/confusing context, and prune/update candidates. Do not
turn it into a transcript or browse unused docs just to populate it.

Fill `RESULT.md` `## Git Provenance` with the final known lightweight repo,
branch, compare-base, head-commit, and PR state for the change folder. Do not
run broad git-history scans just to populate it. If a later commit/push/PR step
continues the same change folder, update that same section instead of creating a
separate provenance record.

Do not perform broad durable-memory repair in this phase. Prepare the reconcile
packet so `plan-reconcile` can run from fresh context.

## Final Output

Finish with:

- final status
- change folder path
- changed files summary
- verification summary
- followups created or remaining
- plan-reconcile readiness
- whether commit, push, or PR work was done or intentionally skipped
- the lane's ledger status left on finish (`BUSY`, or `HELD` with reason), when a
  lane claim ledger applies
