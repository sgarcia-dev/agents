---
created_at: 2026-07-06
updated_at: 2026-09-15
model: gpt-5.6-terra
doc_type: adapter
purpose: Document the current Cursor mapping from Agents workspace source-of-truth roots to native Cursor surfaces.
related:
  - path: ./adapter-contract.md
    why: Platform-neutral adapter rules and reconciliation requirements.
  - path: ./cursor.divergences.md
    why: Current intentional Cursor differences and pending verification.
  - path: ../capabilities/connectors.md
    why: Portable connector registry that Cursor reconciles against.
---

# Cursor Adapter

The Agents workspace remains canonical. Cursor rules, skills, subagents, MCP
servers, permissions, and editor state are native implementation details.

## Temporary Post-Employment Migration Notice

**Remove this section during Cursor's next `sync-tool-adapter` run, after its
audit and required native changes are complete.** The user is no longer affiliated
with the former organization. Do not restore entries removed from the canonical
workspace based on older adapter records. The next Cursor run must audit live
configuration and remove or disable remaining legacy organization-specific entries.

`../roles/task-worker-tiers.md` is the availability authority. Its currently
disabled fast, high, and orchestration wrappers must remain unavailable when the
next Cursor-owned sync audits native configuration.

## Native Surfaces

- Global configuration: `~/.cursor`.
- Shared instructions: `~/.agents/AGENTS.md`, a symlink to `~/agents/AGENTS.md`.
- Shared skills: `~/.agents/skills/` thin loaders.
- Native rules, agents, MCP servers, permissions, and editor state: Cursor-owned
  configuration. Inspect them only in a Cursor-owned sync.

## Source Mapping

| Agents workspace concept | Cursor surface | Required posture |
|---|---|---|
| Instructions | User rules | Thin pointer to the canonical workspace file. |
| Skills | `~/.agents/skills/` | Load canonical skill files; never copy procedure text. |
| Roles | Global or project agents | Thin loaders of canonical role files. |
| Commands | Native command surface | Pass the raw user request to the matching canonical skill. |
| Connectors | Cursor MCP configuration | Reconcile only against `../capabilities/connectors.md`. |

## Worker And Orchestrator Status

The next own-runtime sync must verify native model, reasoning, permission, and
availability settings. Until then, do not infer support from older records.

| Mapping | Temporary status |
|---|---|
| `task-explore` | Requires own-runtime verification before use. |
| `task-execute` | Requires own-runtime verification before use. |
| `task-explore-fast` | Disabled pending a user decision. |
| `task-explore-high` | Disabled pending a user decision. |
| `task-execute-fast` | Disabled pending a user decision. |
| `task-execute-high` | Disabled pending a user decision. |
| `task-orchestrator` | Disabled pending a user decision. |
| `task-orchestrator-fast` | Disabled pending a user decision. |

## Connectors And Browser Tools

Only the portable connector registry defines maintained connector intent. The next
Cursor sync must identify native extras, remove retired organization-specific
entries, and record deliberate local exceptions in the divergence ledger. Keep the
real-browser connector disabled unless the current conversation explicitly asks to
inspect the user's running browser session.

## Drift Checks

- The shared instruction path is a symlink to `~/agents/AGENTS.md`.
- Shared skills and role wrappers remain thin loaders.
- Native connector and browser-tool state is checked only by Cursor in its own
  session.
- The temporary disabled mappings remain unavailable until the user changes that
  decision.
- The next successful own-runtime sync replaces this provisional mapping and its
  ledger with verified native state.
