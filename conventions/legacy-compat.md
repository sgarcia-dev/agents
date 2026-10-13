---
created_at: 2026-07-07
model: claude-opus-4.8
doc_type: convention
purpose: >-
  Historical/legacy compatibility narrative for the Agents workspace: retired
  workflows and folders that must stay readable but must not be recreated.
  Reference only; not a write-time gate.
related:
  - path: ../AGENTS.md
    why: Kernel routes historical/retired-workflow constraints here.
  - path: ./artifact-authoring.md
    why: Current artifact write locations, categories, and naming.
  - path: ./memory-files.md
    why: Current durable-memory file rules.
---

# Legacy Compatibility

The Agents workspace consolidated new serious durable work onto root `skills/`,
root `roles/`, and `workflows/spec-workflow/`. This file preserves the historical
narrative so old links keep working; it does not override current write rules in
`artifact-authoring.md` and `memory-files.md`.

## Retired Trees (do not recreate)

The legacy `task-folder-workflow`, `sharded-agent-handoffs`, workflow-local
`workflows/spec-workflow/skills/`, and workflow-local
`workflows/spec-workflow/subagents/` trees were retired and removed. Keep only
historical links and artifacts readable for callers that still need old records.

- Use `changes/<YYMMDD_HHMM__semantic-slug>/` or
  `projects/<repo>/changes/<YYMMDD_HHMM__semantic-slug>/` for new spec-workflow
  execution packets. Existing `artifacts/tasks/` folders are deprecated readable
  legacy records only.
- Existing task-folder-workflow artifacts remain valid legacy compatibility
  inputs. Do not create new legacy lowercase task-folder workflow artifacts.
- Use `artifacts/handoffs/` (under an allowed artifact root) only for lightweight
  context-transfer artifacts that let a future human or agent resume work without
  reconstructing state. Do not use handoffs as execution workspaces; use
  `changes/` for serious execution packets.
- Do not recreate `sharded-agent-handoffs` for new implementation work. Do not
  migrate old handoff folders just for naming consistency.

## Nested Containers And Epics

- Keep existing nested project, initiative, and `epics/` folders readable for
  history and routing. Do not create new nested initiative containers by default;
  prefer project-level `specs/` or `changes/` for durable truth and reviewed
  change work.
- Keep `epics/` valid where it already exists. Do not rename active epics just for
  taxonomy cleanup.
- If a nested sub-area needs long-lived state and history, prefer promoting it to a
  clearer root or project-level `specs/`, `changes/`, or dedicated domain scope instead of
  adding recursive `STATE.md` or `artifacts/` layers.

## Nested Artifact Folders

- Create new `artifacts/` folders only at allowed artifact roots: root `artifacts/`
  and `projects/<repo>/artifacts/`. Do not create new artifact folders under specs,
  nested projects, epics, initiatives, pillars, or other curated subfolders.
- Existing nested artifact folders may remain for historical links and legacy
  readers. Do not add new generated artifacts to them.
- Existing nonstandard artifact folders may remain for compatibility. Do not invent
  new artifact category folders unless the user explicitly requests them; use
  `misc/` when no standard category fits.
