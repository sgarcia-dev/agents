---
name: plan-reconcile
description: Reconcile durable Agents workspace memory after a completed or blocked spec-workflow change folder from fresh context. Use after plan-execute when a RECONCILE_PACKET.md, RESULT.md, EXECUTION_LOG.md, or MEMORY_DELTA.md is ready.
created_at: 2026-07-02
updated_at: 2026-09-25
model: gpt-5.5
doc_type: skill
purpose: Define the plan-reconcile phase for the Agents workspace spec workflow.
related:
  - path: ../../workflows/spec-workflow/AGENTS.md
    why: Workflow invariants and composition rules for the spec workflow.
  - path: ../../workflows/spec-workflow/templates/RECONCILE_PACKET.md
    why: Required execution-to-reconcile handoff shape.
  - path: ../../workflows/spec-workflow/templates/MEMORY_DELTA.md
    why: Durable-memory delta shape consumed by this phase.
  - path: ../../roles/task-explore.md
    why: Read-only worker role available for bounded reconcile checks.
  - path: ../../roles/task-execute.md
    why: Bounded mutation worker role available for exact memory patches.
  - path: ../../conventions/memory-files.md
    why: Write-time contract for durable-memory files (STATE/DECISIONS/SOURCES/CODEMAP) and update triggers.
---

# Plan Reconcile

You are the high-reasoning plan reconcile agent. Reconcile durable Agents
workspace memory from fresh context after a serious spec-workflow change folder
completes or reaches a clear blocked state.

## Required First Reads

- nearest applicable `AGENTS.md`
- nearest applicable `STATE.md` when it exists
- change `AGENTS.md` if present
- `PLAN.md`
- `RESULT.md`
- `EXECUTION_LOG.md`
- `RECONCILE_PACKET.md` or legacy `CLOSEOUT_PACKET.md`
- `MEMORY_DELTA.md` if present
- `../../conventions/memory-files.md` before creating or updating any durable
  memory file (STATE/DECISIONS/SOURCES/CODEMAP and update triggers)

`RECONCILE_PACKET.md` is the canonical execution-to-reconcile handoff. Accept
legacy `CLOSEOUT_PACKET.md` for existing change folders created before the
rename.

Read change-local spec deltas, current specs, `DECISIONS.md`, `SOURCES.md`,
`CODEMAP.md`, changelogs, source files, old artifacts, or worker results only
when the reconcile packet or memory delta points to them.

Treat `RESULT.md` `## Context Used` as a hint about material context, stale or
confusing docs, and prune/update candidates. It is not a command to browse every
unused or stale-looking document.

Treat `RESULT.md` `## Git Provenance` as the authoritative per-change summary of
branch, commit, push, and PR state. Do not rediscover provenance from scratch
unless the section is missing and the reconcile decision genuinely depends on it.

## Delegation Availability

The root owns reconciliation unless it explicitly assigns a bounded phase to a
verified `task-orchestrator`.
Before dispatching any worker, read `../../roles/task-worker-tiers.md`; it permits
enabled micro and high wrappers and defines the packet and concurrency limits.

For source confirmation, follow the checkout recorded by `PLAN.md` and the
`Source checkout` line in `RESULT.md`: an explicit plan selector governs when
present; otherwise use the result's effective selector/provenance, falling back
to the owning project's default or current existing behavior only when neither
change file records one. Validate the path, Git top-level, and repository
identity before source reads. Treat recorded per-packet checkout and runtime
allocations as execution provenance; never let the reconcile launch workspace or
later process CWD choose or reassign them. Keep product/spec memory
checkout-neutral: the stable selector catalog and managed-session opt-in belong
in project guidance, while selected paths, allocations, runtime targets, and
process ownership remain execution provenance.

When reconciliation dispatches a source, test, Git, or checkout-bound
runtime/browser worker, pass the effective selector, resolved absolute working
directory, expected repository identity, and applicable recorded runtime target
in its packet. The worker must not infer them from its process CWD.

When project guidance defines a lane claim ledger and this change worked a managed
non-default lane, release it as part of reconciliation: if the work is durably
captured (branch pushed, or captured in this workspace) and the checkout is
reusable, set that lane's ledger row `FREE`, editing only that row in place. If a
reuse-blocking condition remains (unpushed work, an owned runtime still running,
interrupted rebase/merge/stash or overlay recovery), leave it `HELD` with the
reason. The ledger is operational coordination state, not durable product/spec
memory, and is not itself subject to memory update triage.

## Durable Memory Defaults

After a successful serious change, create or update these live-memory docs in the
declared owning scope unless clearly unnecessary:

- `STATE.md`: current router, status, active truth, blockers, and next steps.
- `DECISIONS.md`: accepted durable choices, rejected alternatives, tradeoffs,
  and consequences.
- `SOURCES.md`: trusted evidence, weak or stale evidence, and freshness notes.
- `CODEMAP.md`: code landmarks, ownership boundaries, and navigation notes for
  future agents.

If any of these are skipped, record a concise reason in `RESULT.md` or
`MEMORY_DELTA.md`.

## Memory Update Triage

For each possible durable-memory update, choose exactly one action:

- `NO-OP`: current durable truth did not change, or missing update would not harm
  future agents.
- `PATCH`: a small live-memory update is needed.
- `PROMOTE`: an artifact insight is accepted as durable truth and should be
  copied into live memory or a current spec.
- `MARK`: an artifact should be marked stale or superseded because it is likely
  to mislead.
- `FOLLOWUP`: the issue is real but should not block reconciliation.

Default to `NO-OP` unless future agents would be harmed by missing or stale
memory. Plan reconciliation should touch at most three live-memory files unless a
current spec changed or the reconcile packet explicitly justifies broader memory
repair. When durable truth changed but a live-memory file is skipped, record the
concise skip reason in `RESULT.md`, `MEMORY_DELTA.md`, or the final reconcile
summary.

## Specs And Changes

Apply accepted spec deltas from
`changes/<YYMMDD_HHMM__semantic-slug>/specs/<domain>/spec.md` or
`projects/<repo>/changes/<YYMMDD_HHMM__semantic-slug>/specs/<domain>/spec.md` to
the owning current `specs/<domain>/spec.md` only when the change is accepted.

Do not treat all work as a spec change. Use specs for durable behavior,
contracts, protocols, or requirements that future agents should treat as current
truth.

If the change was created in the wrong scope, nested under a forbidden folder, or
stored as a new legacy task-folder record, do not silently rewrite history or
infer ownership from locality. Record the scope mismatch and either ask the user
or create a followup to move or recreate the change under the right scope.

## Artifact Staleness

Mark old artifacts stale or superseded only when they are likely to mislead
future agents. Do not browse all historical artifacts by default.

## Worker Use

Use workers only for bounded help:

- `task-explore mode=memory` for current/stale memory inspection
- `task-explore mode=sources` for evidence checks
- `task-explore mode=code` for code landmark confirmation
- `task-explore mode=review` or `mode=verify` for reconciliation review
- `task-execute packet_type=memory-patch` only for exact approved patches
- `task-execute packet_type=mechanical-doc-update` only for low-judgment edits

Workers do not decide current durable truth.

## Stop Conditions

Stop and report blocked when:

- `RECONCILE_PACKET.md` and legacy `CLOSEOUT_PACKET.md` are both missing or
  insufficient
- the change folder is in a forbidden nested scope and ownership cannot be
  resolved from the packet
- source truth conflicts and cannot be resolved from listed inputs
- a memory update would require broad re-investigation
- an exact memory-patch packet would require judgment beyond the approved patch
- project/product behavior remains ambiguous

## Final Output

Update `RESULT.md` or `MEMORY_DELTA.md` with reconcile status, including:

- durable files changed
- durable files intentionally skipped and why
- specs updated or left pending
- stale artifacts marked
- unresolved followups
- lane released to `FREE` or left `HELD` with reason, when a lane claim ledger
  applies
