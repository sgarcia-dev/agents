---
created_at: 2026-06-29
model: gpt-5.5
doc_type: spec
purpose: Define current Agents workspace project-memory behavior.
related:
  - path: ../spec-workflow/spec.md
    why: Defines the workflow that maintains project memory during reconciliation.
  - path: ../../AGENTS.md
    why: Root Agents workspace routing and taxonomy rules.
---

# Project Memory Spec

Agents workspace projects are scoped durable memory roots for real work areas. For
artifact placement, a project means a code-repository project root such as
`projects/my-web-app` (private, not published), not a nested initiative or pillar folder.

## Growth Model

Projects should start small and grow only when useful:

```text
STATE.md
-> DECISIONS.md / SOURCES.md / CODEMAP.md
-> specs/<domain>/spec.md
-> changes/<YYMMDD_HHMM__semantic-slug>/
-> artifacts/<category>/
```

## Live Memory Docs

Use these files as current-truth docs, not execution logs:

- `STATE.md`: current router, status, active truth, blockers, and next steps.
- `DECISIONS.md`: durable choices, rejected alternatives, tradeoffs, and
  consequences.
- `SOURCES.md`: trusted evidence, stale or weak evidence, and freshness notes.
- `CODEMAP.md`: code landmarks, ownership boundaries, and navigation notes for
  future agents.

After successful serious work, `plan-reconcile` should create or update these
files in the declared owning project scope unless it can clearly justify that the
change altered no durable project truth.

Plan-reconcile triages each candidate update with one action:

- `NO-OP`: durable truth did not change, or skipping the update will not harm
  future agents.
- `PATCH`: a small live-memory update is needed.
- `PROMOTE`: artifact insight is accepted as durable truth and should be copied
  into live memory or a current spec.
- `MARK`: an artifact should be marked stale or superseded because it may
  mislead.
- `FOLLOWUP`: the issue is real but should not block reconciliation.

Default to `NO-OP` unless future agents would be harmed by missing or stale
memory. Plan-reconcile should touch at most three live-memory files unless a current
spec changed or broader memory repair is explicitly justified.

## Project Specs

Create `projects/<project>/specs/<domain>/spec.md` when a repository project has
stable behavior, requirements, contracts, or protocols that future agents should
treat as current truth.

Do not create project specs for one-off notes, transient execution details, or
historical outputs. Put those in artifacts.

For how a spec folder surfaces its links and what is authoritative in which file
(the `spec.md` "Start Here" router, `SOURCES.md` subsection labels, the
`related:`-is-adjacency rule, and the bundle-index pattern), see
`../../conventions/memory-files.md` "Spec Folder Organization".

## Project Changes

Create `projects/<project>/changes/<YYMMDD_HHMM__semantic-slug>/` for
repo-specific serious work that needs reviewable intent, restartable execution,
worker packets, verification, memory reconciliation, or updates to one or more
project specs.

Changes that span multiple projects may live at root
`changes/<YYMMDD_HHMM__semantic-slug>/` and reference affected project scopes.

Do not create changes under nested projects, epics, initiatives, pillars, specs,
or artifacts. A change may touch multiple specs or legacy memory areas, so the
change folder belongs at the root or repository-project level.

## Artifacts

Generated or historical outputs must go under root `artifacts/<category>/` for
global or cross-project work, or `projects/<repo>/artifacts/<category>/` for
repo-specific work. Do not infer artifact placement from the folder being read,
and do not write new artifacts to nested project, epic, initiative, pillar, or
spec-local artifact roots. Artifacts explain how work happened; live memory docs
explain what future agents should believe now.

## Skip Rule

If a successful serious task does not update `DECISIONS.md`, `SOURCES.md`, or
`CODEMAP.md`, record a concise skip reason in `RESULT.md`, the reconcile packet,
or memory delta.
