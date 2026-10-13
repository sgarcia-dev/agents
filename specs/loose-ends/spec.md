---
created_at: 2026-08-08
model: gpt-5.6-sol
doc_type: spec
purpose: Define durable behavior for tracking and resuming global loose ends.
related:
  - path: ./STATE.md
    why: Authoritative active loose-ends list.
  - path: ../../conventions/artifact-authoring.md
    why: Location, naming, and frontmatter rules for compact handoffs.
  - path: ../../conventions/memory-files.md
    why: Authority, state, and durable-memory update rules.
---

# Global Loose Ends Spec

The global loose-ends system preserves actionable work across session and machine
restarts without making agents reconstruct the largest findings and decisions.

## Start Here

- Status: `./STATE.md` owns the active loose-ends list.
- Operate: the `Lifecycle`, `Operation Contract`, and `Verification` sections
  below define add, update, remove, complete, and resume behavior. There is no
  separate skill; an agent asked to operate the list follows this spec directly.
- Artifacts: `../../conventions/artifact-authoring.md` governs compact handoffs.

## Scope

- Track global, cross-project, and project-referencing loose ends in one active
  index.
- Link to project-owned truth instead of copying project behavior or decisions.
- Keep secrets, credentials, raw transcripts, and unnecessary sensitive payloads
  out of entries and handoffs.
- Treat artifacts as supporting restart context, never authoritative current truth.

## Entry Contract

Each active entry must contain:

- stable `LE-YYYYMMDD-NN` ID and concise title
- scope and status (`open` or `blocked`)
- objective and why it matters
- current findings and decisions needed to resume
- exact next action, blockers, and completion/removal condition
- authoritative source pointers
- created and updated dates
- one compact handoff artifact link

The active entry should be detailed enough to choose the next action without
opening the handoff. The handoff owns compact session context that would make the
active ledger noisy, including investigation history and rejected alternatives.

## Lifecycle

- Add by allocating the next unused daily `LE-YYYYMMDD-NN` ID and writing the
  state entry and handoff together.
- Update by exact ID and refresh both surfaces when restart context materially
  changes.
- Remove by exact ID, delete the active entry, and mark its handoff completed with
  the removal reason and date. Git preserves list history.
- After removal, the handoff keeps its scoped-state link as a former-owner
  pointer; reciprocal entry-to-handoff linkage is required only while active.
- Never use fuzzy title matching for update or removal.
- Do not report success unless both current state and artifact linkage verify.
- Ask for material missing context instead of inventing objectives, findings,
  decisions, blockers, or completion conditions.

## Handoff Contract

Use one root `artifacts/handoffs/` document per loose end, named and authored by
`conventions/artifact-authoring.md`. It must contain:

- status, as-of date, and last-verified date
- loose-end ID, objective, importance, and link to the active entry
- resume-first next action and stopping condition
- compact findings and important negative findings
- decisions, constraints, and rejected alternatives
- open questions, blockers, and unblock conditions
- authoritative source pointers
- staleness, uncertainty, and privacy notes
- an explicit statement that the scoped loose-ends `STATE.md` is current truth

Update the same handoff in place while its item is active. After removal, retain
it as historical context, mark it completed, and state the removal reason and date.

## Operation Contract

An agent operating this list must recognize natural-language requests to add,
update, remove, complete, or resume an item in the “global todo” or “loose ends”
list, and carry them out by following this spec directly.

- Add captures current-session context, asks for missing material information,
  allocates the ID, writes the handoff and active entry, verifies both, and commits.
- Update requires an exact ID, updates the active entry and existing handoff in
  place, verifies both, and commits.
- Remove requires an exact ID, completes the handoff, removes the active entry,
  verifies both states, and commits.
- Resume requires an exact ID, reads the active entry and handoff, checks source
  freshness where material, and reports the next action and unresolved blockers.

## Verification

For every mutation:

- validate required entry and handoff fields
- resolve reciprocal links while active or the former-owner state link after removal
- confirm state and handoff agree on ID, status, scope, and next action while active
- confirm completed handoffs record the removed ID, reason, and date
- confirm secrets, credentials, raw transcripts, and unnecessary sensitive
  payloads were excluded
- run `git diff --check` and inspect the complete task diff
- stage and commit only the loose-end mutation and its directly required memory
  updates

Initialization is valid only when the active state says `None` and no fabricated
handoff artifact was created.
