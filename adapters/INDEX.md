---
created_at: 2026-07-01
updated_at: 2026-09-30
model: claude-sonnet-5
doc_type: index
purpose: Provide a lightweight registry of AI runtime adapters maintained against the Agents workspace.
related:
  - path: ./adapter-contract.md
    why: Platform-neutral adapter rules and reconciliation requirements.
  - path: ./hermes.md
    why: Current Hermes adapter mapping and open decisions.
  - path: ./opencode.md
    why: Current OpenCode adapter mapping and migration status.
  - path: ./codex.md
    why: Current Codex adapter mapping and migration status.
  - path: ./cursor.md
    why: Current Cursor adapter mapping and migration status.
  - path: ./claude-code.md
    why: Current Claude Code adapter mapping and migration status.
  - path: ../workflows/adapter-lifecycle/AGENTS.md
    why: Workflow package for onboarding and reconciling adapters.
  - path: ../capabilities/connectors.md
    why: Portable connector registry adapters reconcile native configuration against.
---

# Adapter Registry

This registry is a routing table, not a native configuration inventory. Native
runtime state is verified only in that runtime's own `sync-tool-adapter` session.

| Tool | Status | Mapping | Next action |
|---|---|---|---|
| OpenCode | active, routine permissions migrated | `opencode.md` + `opencode.divergences.md` | 2026-09-30: persistent routine root/default-high access repaired; root and both high workers live-tested. Default Luna mappings static-only pending version confirmation. Disabled connectors, secret-file asks and costly-tool denies retained. See the permission migration result for supervisor/transport failures and remaining browser/orchestrator checks. Orchestrator shell now allows routine scripts; four-name child deny/allow rules retained. Follow-up static-only. |
| Codex | active, routine permissions migrated | `codex.md` + `codex.divergences.md` | 2026-09-30: root and four enabled workers save never/full-access defaults. Fresh root and both high workers live-tested; high execute needed one replacement after timeout. Default Luna mappings static-only pending version confirmation. Existing connectors and model mappings preserved; one-run profile and browser limits remain in the owning mapping. Orchestrator never/full access and root depth two saved; named-child limits remain behavioral. Follow-up static-only. |
| Cursor | active, provisional | `cursor.md` + `cursor.divergences.md` | Run a Cursor-owned migration audit before relying on legacy native state. |
| Claude Code | active, routine permissions migrated | `claude-code.md` + `claude-code.divergences.md` | 2026-10-07: workers moved to Haiku 5.5 high (regular) and Sonnet 5.5 high (high), orchestrator stays Opus 5.5 medium; static change, live-checked 2026-10-08 (each worker reported its model; both execute workers wrote a test file). Root default found at Opus high, left for the user to decide. 2026-09-30: root bypass default and four enabled workers verified; workers inherit enabled MCP tools with terminal leaves preserved. Exact Google mutation ask rules retained; account actions not live-tested. Reopen existing sessions to load changes. Orchestrator now inherits shell/MCP/file tools with bypass; four-leaf hook and terminal leaf Agent exclusions retained. Follow-up static-only. |
| Hermes | active, gateway reload pending | `hermes.md` + `hermes.divergences.md` | 2026-09-30: three named task skill loaders and browser-use discovered; Parallel, Exa and Firecrawl MCP search calls passed in fresh Hermes CLI sessions. Reload the live Discord gateway's MCP registry, then confirm its direct tool calls. Maintained worker roles and non-frontier delegation still need separate decisions. |
| Gemini | active, routine permissions migrated | `gemini.md` + `gemini.divergences.md` | 2026-09-30: routine permissions applied in settings.json; task-explore and task-execute initialized as subagents on Gemini 3.8 Flash (Medium); high worker tiers and orchestrator deleted per user directive. Search MCP servers (Parallel, Exa, Firecrawl) verified. |
| GitHub Copilot | not onboarded | none | Run `sync-tool-adapter` in onboarding mode if needed. |

## Registry Rules

- Add a row only when the tool is intentionally onboarded or explicitly marked as
  not onboarded.
- Add or update a tool-specific mapping and divergence ledger before marking a tool
  active.
- Keep rows short. Tool-specific docs own runtime details and verification state.
- Model choices are not adapter content: they live in
  `~/agents/ai-models/delegation-briefing.md`. Adapters record how
  each choice is wired and checked.
- Remove a row only when the adapter is intentionally retired and no current native
  configuration depends on it.
