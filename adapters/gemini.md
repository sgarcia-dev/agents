---
created_at: 2026-09-30
updated_at: 2026-10-07
model: gemini-3.8-flash
doc_type: adapter
purpose: Map the canonical Agents workspace to the Gemini / Antigravity harness.
related:
  - path: ~/agents/adapters/adapter-contract.md
    why: Defines the platform-neutral reconciliation contract and report requirements.
  - path: ~/agents/adapters/gemini.divergences.md
    why: Records Gemini-specific choices and divergence items to recheck.
  - path: ~/agents/roles/task-worker-tiers.md
    why: Defines worker availability and delegation boundaries.
  - path: ~/agents/capabilities/connectors.md
    why: Defines portable MCP connector registry.
  - path: ~/agents/capabilities/gemini-cli.md
    why: Full capability reference for agy CLI.
---

# Gemini Adapter (Antigravity CLI / agy)

The global agents workspace at `~/agents` is the canonical source of truth. Global Gemini (Antigravity) connects to it via thin instruction and skill loaders. Gemini-native configuration, binary subcommands, and runtime services are replaceable implementation details.

## Native Surfaces

- **Global agents workspace instructions:** `~/.agents/AGENTS.md` symlinks to canonical `~/agents/AGENTS.md`. Antigravity discovers this directory automatically by hierarchical parent walk.
- **Global agents workspace skill loaders:** `~/.agents/skills/` contains thin loader wrappers that load canonical procedures from `~/agents/skills/`.
- **Global Gemini configuration:**
  - MCP configuration lives at `~/.gemini/config/mcp_config.json`.
  - User settings and routine permissions live at `~/.gemini/antigravity-cli/settings.json`.
  - Global custom agent definitions live at `~/.gemini/config/agents/<agent_name>/agent.md`.
- **Global Gemini binary:** `~/.local/bin/agy` manages sessions, models, plugins, and MCP servers.
- **Global Gemini built-in skills:** `~/.gemini/antigravity-cli/builtin/skills/` holds application-specific skills (`agy-customizations`, `antigravity_guide`, `automation`, `generative_ui`, `migrate-workflows`, `permissioned-github`, `plugin`, `ui-extension`, `ui-plugin-navigation`). These stay local to Antigravity.
- **Gemini current project (`~`):** No separate project-specific Gemini configuration is present. The user-level configuration applies across the workspace.

## Source Mapping

| Global Agents Workspace Concept | Global Gemini Implementation |
|---|---|
| Instructions | The `.agents/AGENTS.md` symlink loads canonical root instructions. |
| Skills | Thin files in `.agents/skills/` load canonical procedures. Built-in skills remain local. |
| Worker roles | Global custom agents (`task-explore`, `task-execute`) in `~/.gemini/config/agents/` initialized with Gemini 3.8 Flash on medium reasoning (`gemini-3.8-flash-medium`), or headless print execution (`agy -p`). High workers deleted. |
| Worker model choice | Set by the [delegation briefing](../ai-models/delegation-briefing.md) (Gemini section and card). Native mapping today: `gemini-3.8-flash-medium` for default workers. High and fast tiers disabled. |
| Frontier orchestrator | Not mapped / unsupported. User directive explicitly removed `task-orchestrator` and `task-orchestrator-fast`. |
| Commands | Native slash commands and `agy` subcommands (`models`, `mcp`, `agent`, `plugin`). |
| MCP connectors | Configured via `agy mcp add` in `~/.gemini/config/mcp_config.json`. Default-on search connectors (`parallel`, `exa`, `firecrawl`) are enabled. |

## Skills

Global Gemini discovers workspace skills through `.agents/skills/`. Each entry is a thin loader directing the model to read the canonical procedure under `~/agents/skills/`:

- Core workflows: `plan-create`, `plan-execute`, `plan-reconcile`, `memory-reconcile`, `model-bakeoff`.
- Research: `research`, `research-deep`, `browser-use`, `chatgpt-browser`, `claude-browser`.
- Delegation and adapters: `role-dispatch`, `sync-tool-adapter`, `task-claude`, `task-codex`, `task-opencode`, `task-hermes`, `task-gemini`.
- Search: `web-search`, `web-search-advanced`, `artificial-analysis-model-data`.

Built-in Antigravity skills remain local to the runtime and are not promoted to the global agents workspace.

## Worker Tier Matrix

The global agents workspace defines six worker tier cells. Global Gemini resolves them as follows:

| Role | Model and Effort | Status | Native Mechanism |
|---|---|---|---|
| `task-explore` | `gemini-3.8-flash-medium` | Configured | Global custom agent in `~/.gemini/config/agents/task-explore/agent.md`, read-only tools (`enable_write_tools=false`), description points to delegation briefing section 3 |
| `task-execute` | `gemini-3.8-flash-medium` | Configured | Global custom agent in `~/.gemini/config/agents/task-execute/agent.md`, mutation tools enabled within assigned packet, description points to delegation briefing section 3 |
| `task-explore-fast` | none | Disabled | Refuse launch per canonical guidance |
| `task-execute-fast` | none | Disabled | Refuse launch per canonical guidance |
| `task-explore-high` | none | Unsupported-with-reason | Deleted per user directive: Gemini Pro rejected (latest is 3.1, ancient and abysmally bad) |
| `task-execute-high` | none | Unsupported-with-reason | Deleted per user directive: Gemini Pro rejected (latest is 3.1, ancient and abysmally bad) |

Enabled micro workers are terminal and must not launch child agents.

## Frontier Orchestrator Mappings

| Orchestrator Role | Model and Settings | Status | Native Mechanism |
|---|---|---|---|
| `task-orchestrator` | none | Unsupported-with-reason | Disabled per user directive; no frontier orchestrator mapped for Gemini |
| `task-orchestrator-fast` | none | Disabled | Refuse launch per canonical guidance |

## One-Run Role Profiles

Global Gemini supports one-run role execution through two native surfaces:

1. **Interactive subagent dispatch:** The root session invokes `invoke_subagent` using global custom agents `task-explore` and `task-execute`.
2. **Headless CLI execution:** External or peer callers launch `agy -p '<prompt>'` with explicit flags:
   - Model selection: `--model <model_id>` (e.g. `gemini-3.8-flash-medium`)
   - Reasoning effort: `--effort <low|medium|high|max>`
   - Permissions: `--dangerously-skip-permissions` (required for unattended runs)
   - Structured capture: `--output-format json`

Model choices (root, workers, which Gemini models are banned) live in the
[delegation briefing](../ai-models/delegation-briefing.md). Native settings today, confirmed by the user on
September 30, 2026: root `gemini-3.8-flash-high` with `--effort high`; micro
workers `gemini-3.8-flash-medium` with `--effort medium`; no high workers.

Concurrency: the briefing's count rules apply (Gemini 3.8 Flash is mid cost:
usually 2 to 4 default workers, ceiling 5). No high workers.

### October 5 subagent launch failure: fixed (2026-10-07, launch-tested 2026-10-08)

An October 5 test showed `invoke_subagent` failed to launch `task-explore` in a fresh headless CLI session. Audit showed that the September 30 initialization used the interactive `define_subagent` tool, which only saved definitions into that specific conversation's brain directory. Global startup discovery in `agy` scans `~/.gemini/config/agents/<name>/agent.md`. Placing persistent agent definitions in `~/.gemini/config/agents/` should let both interactive and headless sessions find the workers. Launch smoke passed 2026-10-08: a fresh headless `agy -p` session launched `task-explore`, which read a role file and answered correctly. The child said it inherited the parent's model; the parent was also Gemini 3.8 Flash medium, so whether the worker file's own pin applies is not yet shown.

## Connectors and MCP Inventory

Reconciled against [`capabilities/connectors.md`](../capabilities/connectors.md):

| Connector | Type | Posture in Global Gemini | Runbook / Endpoint |
|---|---|---|---|
| `parallel` | Hosted HTTP | Configured and enabled | `https://search.parallel.ai/mcp` |
| `exa` | Hosted HTTP | Configured and enabled | `https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa&defaultSearchType=instant` |
| `firecrawl` | Hosted HTTP | Configured and enabled | `https://mcp.firecrawl.dev/v2/mcp` |
| `playwright` | Local stdio | Not configured (declined) | Native browser / CLI preferred |
| `chrome-devtools`| Local stdio | Not configured (declined) | Native tools preferred |
| `jev-browser` | Local stdio | Not configured (declined) | Dedicated browser bridge preferred |
| `figma` | Remote/local | Not configured (declined) | Add when needed |
| `git` | Local stdio | Not configured (declined) | Native shell git preferred |
| `github` | Hosted | Not configured (declined) | Local git and web fetch preferred |

## Permissions and Autonomous Execution

Under [`autonomous-task-permissions.md`](../conventions/autonomous-task-permissions.md):
- `~/.gemini/antigravity-cli/settings.json` is configured with `permissions.allow` for routine command and file actions, `permission_mode: proceed-in-sandbox`, and `skip_permission_checks: true`.
- Trusted workspaces include `~`, `~/agents`, `~/agents-workspace`, and `~/Downloads`.
- Headless runs use `--dangerously-skip-permissions` by default.

## Drift Checks

During every reconciliation run, verify:
1. `~/.agents/AGENTS.md` is a valid symlink to `~/agents/AGENTS.md`.
2. Workspace skill loaders in `~/.agents/skills/` are thin and point to canonical paths.
3. Built-in Antigravity skills remain local and are not copied into the workspace.
4. `task-explore` and `task-execute` map to Gemini 3.8 Flash (Medium) in `~/.gemini/config/agents/` with descriptions pointing to section 3 of the delegation briefing.
5. High worker tiers and orchestrators remain disabled/unsupported.
6. MCP configuration in `~/.gemini/config/mcp_config.json` retains default-on search connectors.

## Web reference, 2026-10-01

By default use this harness's built-in search and fetch. [Capabilities/web](../capabilities/web/README.md) owns tool strengths, both ladders, costs and compatibility. Use web-search only on explicit user request or when a task packet names it. web-search-advanced requires an explicit user request by name. Both canonical skills set disable-model-invocation: true and metadata.opencode/autoinvoke: false. Native discovery metadata must be aligned in this tool's own session. This shared-doc change did not inspect, edit or verify native loaders. Keep the native wiring and approved fallbacks documented above.
