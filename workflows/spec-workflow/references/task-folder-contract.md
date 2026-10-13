---
created_at: 2026-06-29
model: gpt-5.5
doc_type: workflow
purpose: Define the legacy task-folder contract retained for old spec-workflow records.
related:
  - path: ../AGENTS.md
    why: Entry point and invariants for the spec workflow.
  - path: change-folder-contract.md
    why: Current contract for new serious spec-workflow work.
---

# Legacy Task Folder Contract

Task folders under `artifacts/tasks/` are deprecated legacy restartable
execution packets. They remain valid read targets for old work, but new serious
spec-workflow work must use `changes/<YYMMDD_HHMM__semantic-slug>/` or
`projects/<repo>/changes/<YYMMDD_HHMM__semantic-slug>/` instead. See
`change-folder-contract.md` for the current contract.

## Standard Layout

```text
artifacts/tasks/<task-folder>/
  AGENTS.md
  PLAN.md
  EXECUTION_LOG.md
  RESULT.md
  MEMORY_DELTA.md
  RECONCILE_PACKET.md or legacy CLOSEOUT_PACKET.md
  subtasks/
    T01_<verb>_<object>.md
  followups/
    F01_<reason>_<verb>_<object>.md
  results/
    T01.result.md
    F01.result.md
```

Required in legacy serious spec-workflow task folders:

- `AGENTS.md`
- `PLAN.md`
- `EXECUTION_LOG.md`
- `RESULT.md`

Optional unless needed:

- `MEMORY_DELTA.md`
- `RECONCILE_PACKET.md` or legacy `CLOSEOUT_PACKET.md`
- `subtasks/`
- `followups/`
- `results/`

## File Roles

- `PLAN.md`: approved execution contract, scope, graph, verification, and
  plan-reconcile expectations.
- `EXECUTION_LOG.md`: root-owned meaningful decisions, failures, followups,
  verification outcomes, and plan changes. Not a transcript.
- `RESULT.md`: final or current outcome summary.
- `MEMORY_DELTA.md`: proposed and applied durable-memory impacts.
- `RECONCILE_PACKET.md`: execution-to-reconcile handoff. Legacy task folders may
  still use `CLOSEOUT_PACKET.md`.
- `subtasks/`: initial worker packets.
- `followups/`: root-created worker packets discovered during execution.
- `results/`: worker reports.

## Minimal Task Mode

Minimal task mode may omit `subtasks/`, `followups/`, and `results/`. The phase
agent still writes `PLAN.md`, `EXECUTION_LOG.md`, and `RESULT.md`, and may use one
bounded worker if useful.

## Naming

Use stable IDs and concise names:

```text
T01_investigate_current_behavior.md
T02_update_server_logic.md
T03_add_unit_tests.md
F01_fix_t02_type_error.md
```

Do not encode parallelism in filenames. Put dependency and parallel-safety rules
in `PLAN.md` and packet files.

## Legacy Compatibility

Older task folders may use lowercase files such as `plan.md`, `events.md`, and
`result.md`. Treat them as valid legacy contracts. Do not create new task
folders for serious spec-workflow work; create a timestamped change folder
instead. Migrate project-root task folders to `changes/` when practical, but do
not move nested historical task folders only for naming consistency.
