---
name: memory-reconcile
description: Reconcile durable Agents workspace memory after ad hoc work, commit/diff review, suspected drift, or user-described stale memory outside the formal plan-create -> plan-execute -> plan-reconcile workflow.
created_at: 2026-07-02
updated_at: 2026-09-05
model: gpt-5.6-sol
doc_type: skill
purpose: Define lightweight durable-memory reconciliation for work that did not start as a spec-workflow change folder.
related:
  - path: ../../AGENTS.md
    why: Root workspace routing, memory update rules, and git completion gate.
  - path: ../../workflows/spec-workflow/AGENTS.md
    why: Formal workflow to use when reconciliation needs restartable or delegated execution.
  - path: ../plan-reconcile/SKILL.md
    why: Formal third phase for spec-workflow change folders.
  - path: ../../roles/task-explore.md
    why: Read-only worker role available for bounded memory, source, code, review, or verify questions.
  - path: ../../roles/task-execute.md
    why: Bounded mutation worker role available for exact authorized memory patches.
  - path: ../../conventions/memory-files.md
    why: Write-time contract for durable-memory files (STATE/DECISIONS/SOURCES/CODEMAP) and update triggers.
---

# Memory Reconcile

You are the lightweight memory reconcile agent. Decide whether ad hoc work,
commit history, a diff, or suspected drift changed durable Agents workspace truth,
then apply clear authorized updates directly or use a reviewed reconciliation
change only when the work actually needs one.

Use this skill outside the formal spec-workflow phase sequence. For completed or
blocked spec-workflow change folders with `RECONCILE_PACKET.md`, use
`plan-reconcile` instead; it also accepts legacy `CLOSEOUT_PACKET.md` folders.

## Input Modes

Identify the mode before reading broadly:

- `same-session`: use the current chat context plus git diff/status and touched
  files.
- `post-hoc`: use a user-provided commit, commit range, diff, branch, or summary.
- `drift`: use the user's suspected stale area, current memory, and narrow source
  checks.
- `summary-only`: use the user's description and ask when evidence is
  insufficient.

## Authorization

Resolve write authorization separately from the reconciliation classification:

- `apply-now`: the current user message clearly tells you to update, fix, apply,
  or reconcile durable memory now. Complete the read-only inspection first, then
  write in the same invocation. Do not ask for the same approval again.
- `review-first`: the user asks to inspect, check, assess, or reconcile without a
  clear request to write now. Stay read-only, present a compact file-level apply
  set, ask one confirmation question, and stop.
- `audit-only`: the user explicitly asks for no changes. Report findings and stop
  without asking to apply them.

Explicit authorization is semantic, not a magic phrase. Clear instructions such
as "make these changes now", "update the memory", "apply the reconciliation", or
"do not stop for approval" count in the current message. A bare skill invocation,
silence, a request to check what changed, or standing permission from an earlier
unrelated task does not count.

`apply-now` authorizes only edits within the clearly requested scope. It does not
resolve contradictory evidence, choose between materially different truths, or
expand into unrelated memory. Ask only for a decision that is genuinely missing,
not for approval the user already gave.

## Minimal Reads

Read the smallest set that can answer whether durable memory changed:

- nearest applicable `AGENTS.md`
- nearest applicable `STATE.md` when it exists
- `../../conventions/memory-files.md` before writing any durable-memory update
- git status, diff, commit, or commit range when available
- touched source or memory files only as needed
- `DECISIONS.md`, `SOURCES.md`, `CODEMAP.md`, current specs, or old artifacts
  only when the change or suspected drift points to them

If a recent spec-workflow change folder exists and provenance is the suspected
drift, prefer that folder's `RESULT.md` `## Git Provenance` before doing extra
git archaeology. Only use broader history checks when the section is missing,
stale, or the user explicitly asks for post-hoc provenance repair.

Do not browse historical artifacts or all project memory by default.

## Classification

Classify the reconcile outcome as exactly one of:

- `NO-OP`: no future agent would be harmed by skipping a memory update.
- `APPLY-DIRECT`: the durable update is clear enough to apply without a formal
  reconciliation change folder.
- `CREATE-RECONCILIATION-CHANGE`: the issue is real and needs restartable,
  delegated, or otherwise structured execution.
- `BLOCKED`: required evidence, ownership, source truth, or user intent is
  unclear.

Classification does not grant write permission. In `review-first` mode,
`APPLY-DIRECT` is a proposal until the user confirms it.

## Direct Reconciliation Default

Use `APPLY-DIRECT` when all are true:

- owning scope is clear
- sources do not conflict
- the intended current truth is clear from context, source evidence, or an
  explicit user decision
- the edits can be completed and verified safely in the current invocation

Direct reconciliation may update more than three files, current specs, or more
than one memory scope. File count, hunk count, spec involvement, or cross-scope
policy involvement are risk signals to inspect, not automatic reasons to create a
change folder. Prefer direct reconciliation for clear same-session and post-hoc
work when the user has authorized `apply-now`.

When applying, prefer the nearest scoped `STATE.md`,
`DECISIONS.md`, `SOURCES.md`, or `CODEMAP.md` that owns the changed truth. Do not
create optional memory files as ceremony.

Direct reconciliation may backfill a missing `RESULT.md` `## Git Provenance`
section for a recent change folder when the correct branch/commit/PR state is
obvious from current evidence. If that would require broad history
reconstruction, escalate instead.

## Lane Release

When project guidance defines a lane claim ledger and the ad hoc work being
reconciled ran on a managed non-default lane, release it: set that lane's ledger
row `FREE` when the work is durably captured (branch pushed, or captured in this
workspace) and the checkout is reusable, or leave it `HELD` with the reason when a
reuse-blocking condition remains (unpushed work, an owned runtime still running,
interrupted rebase/merge/stash or overlay recovery). Edit only that lane's row in
place. The ledger is operational coordination state, not durable product memory,
so this release is outside the `NO-OP`/`APPLY-DIRECT` memory classification above.

## Optional Escalation

Use `CREATE-RECONCILIATION-CHANGE` only when at least one is true:

- the user explicitly asks for a reviewable or restartable change packet
- execution needs independently sequenced or delegated units
- the work cannot be completed and verified safely in the current invocation
- broad investigation must resolve source ownership or competing truths before
  edits can be specified
- the result needs the formal `plan-execute` to `plan-reconcile` handoff because
  it is part of a serious existing workstream

Do not create a reconciliation change solely because a numeric threshold was
crossed, a current spec must change, or several scopes are involved. A change
folder is an execution aid, not an approval gate.

When escalating, create or recommend a normal `changes/<YYMMDD_HHMM__semantic-slug>/`
or `projects/<repo>/changes/<YYMMDD_HHMM__semantic-slug>/` reconciliation change
folder. The purpose should be honest: reconcile durable memory after ad hoc work
or detected drift. Do not pretend the change folder planned the original ad hoc
implementation.

In `apply-now` mode, if a change folder is genuinely needed and the user asked to
complete the changes now, treat that instruction as up-front delegated approval
for the in-scope plan and continue through execution when feasible. Do not stop
only to ask the user to approve the same work again. In `review-first` mode,
recommend the folder and wait.

## Worker Use

Use workers only for bounded help:

- `task-explore mode=memory` for current/stale memory inspection
- `task-explore mode=sources` for evidence checks
- `task-explore mode=code` for code landmark confirmation
- `task-explore mode=review` or `mode=verify` for reconcile review
- `task-execute packet_type=memory-patch` only for exact authorized patches
- `task-execute packet_type=mechanical-doc-update` only for low-judgment edits

Workers do not decide current durable truth.

## Final Output

Finish with:

- reconcile result: `NO-OP`, `APPLY-DIRECT`, `CREATE-RECONCILIATION-CHANGE`, or
  `BLOCKED`
- authorization mode: `apply-now`, `review-first`, or `audit-only`
- scope inspected
- evidence used
- durable files changed, if any
- files intentionally skipped and why
- escalation or followups, if any
- lane released to `FREE` or left `HELD` with reason, when a lane claim ledger
  applies
- `Agents commit: <hash>` or the exact reason no Agents commit was created when
  Agents workspace files changed
