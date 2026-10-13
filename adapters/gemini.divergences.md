---
created_at: 2026-09-30
updated_at: 2026-10-07
model: gemini-3.8-flash
doc_type: adapter
purpose: Record Gemini-specific choices, approved divergences, and standing preferences to revisit during each reconciliation.
related:
  - path: ./gemini.md
    why: Defines the current Gemini adapter mapping.
  - path: ../capabilities/connectors.md
    why: Defines the portable MCP connector registry.
---

# Gemini Approved Divergences and Standing Decisions

## Decisions Confirmed 2026-10-07

- **Worker description alignment:** Updated `task-explore` and `task-execute` descriptions to reference the Gemini part of section 3 of `~/agents/ai-models/delegation-briefing.md` for capability limits and keep one short model line (`Gemini 3.8 Flash, effort medium (mid cost, medium guessing)`). Removed former packet size text.
- **Persistent agent definition path:** Moved custom agent definitions from ephemeral conversation session brain storage to the global configuration directory scanned during startup discovery: `~/.gemini/config/agents/task-explore/agent.md` and `~/.gemini/config/agents/task-execute/agent.md`. This fixed the October 5 test (fresh-session launch passed 2026-10-08; whether the worker's own model pin applies, rather than the parent's, is not yet shown) where a fresh session failed to find `task-explore`. Verified with `agy agent`.
- **Standing exclusions retained:** High workers (`task-explore-high`, `task-execute-high`) and orchestrators (`task-orchestrator`, `task-orchestrator-fast`) remain unsupported and disabled per user directive.

## Decisions Confirmed 2026-09-30

- **Global Gemini onboarding:** Onboarded Gemini / Antigravity CLI (`agy`) as an active adapter in the Agents workspace.
- **Persistent routine permissions:** Configured `~/.gemini/antigravity-cli/settings.json` with pre-approved permissions (`permissions.allow: ["*"]`, `permission_mode: proceed-in-sandbox`, `skip_permission_checks: true`) and trusted workspace paths per `autonomous-task-permissions.md`. Headless runs use `--dangerously-skip-permissions`.
- **Worker subagents initialization:** Initialized `task-explore` (read-only) and `task-execute` (bounded mutation) subagents using `Gemini 3.8 Flash` on medium reasoning (`gemini-3.8-flash-medium`).
- **High worker tiers deleted:** `task-explore-high` and `task-execute-high` are marked unsupported and deleted from native configuration per user directive. Gemini Pro models are rejected because the latest is 3.1, which is ancient and abysmally bad. Gemini 3.8 Flash is the only usable model; older Flash versions like 3.7 are obsolete. Gemini 4 will require fresh testing and indexing upon release.
- **Frontier orchestrator disabled:** `task-orchestrator` and `task-orchestrator-fast` are marked unsupported and disabled per user directive.
- **Web search and fetch MCP connectors:** Configured `parallel`, `exa`, and `firecrawl` hosted endpoints in `~/.gemini/config/mcp_config.json` via `agy mcp add`. These servers operate as default-on without interactive prompts.
- **Other registry MCP connectors:** `playwright`, `chrome-devtools`, `jev-browser`, `figma`, `git`, and `github` are not configured in global Gemini. Native shell and built-in capabilities handle local operations. These remain declined for now.
- **Antigravity built-in skills:** Built-in skills under `~/.gemini/antigravity-cli/builtin/skills/` stay local to the Antigravity runtime and are not promoted to the workspace.
- **Root model preference:** `gemini-3.8-flash-high` with reasoning effort `high` is the preferred default root session configuration.
