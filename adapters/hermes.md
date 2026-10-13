---
created_at: 2026-09-17
updated_at: 2026-10-01
model: deepseek-v4.1-flash
doc_type: adapter
purpose: Map the canonical Agents workspace to the Hermes harness, which is a personal agent rather than a coding harness.
related:
  - path: ~/agents/adapters/adapter-contract.md
    why: Owns the portable reconciliation rules.
  - path: ~/agents/adapters/hermes.divergences.md
    why: Records Hermes-only choices and limits to recheck.
  - path: ~/agents/roles/task-worker-tiers.md
    why: Owns worker availability and boundaries.
  - path: ~/agents/capabilities/connectors.md
    why: Lists the portable MCP connectors considered for Hermes.
  - path: ~/agents/conventions/artifact-authoring.md
    why: Write-time contract for generated artifacts Hermes may produce in the workspace.
  - path: ~/agents/conventions/memory-files.md
    why: Write-time contract for durable-memory updates Hermes may make.
---

# Hermes Adapter

## Model source

Model choices and trade-offs come only from
`~/agents/ai-models/delegation-briefing.md`, especially the Hermes
rows in sections 3 and 4. Read it before picking or delegating. This adapter
records native wiring and verification, not a separate model policy.

Applied on 2026-10-01: the main default is `openai-codex/gpt-6-sol`, reasoning
`medium`. Native `delegate_task` children are pinned to
`opencode-go/glm-5.3-flash`. These values implement the briefing's Hermes rows.
The one-shot CLI session `20261001_130537_93f21d` read the kernel and returned
its first line. Usage recorded `gpt-6-sol`, `openai-codex`, and
`subscription_included`; session metadata recorded medium effort.
Native child `20261001_130522_d5a0eb` did the same. Usage recorded
`glm-5.3-flash`, `opencode-go`, and the Go endpoint. Neither smoke substituted
a model. Existing sessions keep their own pins; no gateway restart was performed.

On 2026-10-01, the Hermes-local delegation skills were reconciled. Old CLI
recipes now load the global agents workspace `task-*` skills. Local model advice
was replaced with a pointer to the briefing. No other harness configuration was
inspected or changed.

The global agents workspace at `~/agents` is canonical. Global Hermes
is a personal agent, it runs a terminal, a browser, scheduled jobs, a messaging
gateway, and durable cross-session memory, not a coding harness. It therefore
connects to this workspace at the routing and durable-memory layer, and explicitly
does not mirror coding-harness roles or connectors. Its named task bridges are
loaders for explicit cross-tool requests.

## Native Surfaces

- **Global Hermes home:** `~/.hermes`.
- **Global Hermes identity:** `~/.hermes/SOUL.md` is always loaded and
  carries agent identity and reply style only. It is not a second copy of the
  canonical kernel.
- **Global Hermes settings:** `~/.hermes/config.yaml`. Relevant keys
  are `skills.external_dirs`, `skills.auto_load`, `skills.create_dir`,
  `skills.trusted_project_dirs`, `mcp_servers`, and `delegation`.
- **Global Hermes skills:** `~/.hermes/skills/<category>/<name>/SKILL.md`.
- **Global Hermes runtime inventory:** `hermes skills list`, `hermes tools`,
  `hermes cron list`, `hermes plugins`.
- **Global Hermes configuration discovery:** `AGENTS.md` and `CLAUDE.md` load from
  the working directory only; `.hermes.md` walks parents up to the git root. The
  default working directory is `~`, which holds none of them.
- **Harness binaries Global Hermes may call:** `~/.local/bin/claude`
  (Claude Code 2.1.274), `/opt/homebrew/bin/codex` (Codex 0.154.0), and
  `~/.nvm/versions/node/v25.8.0/bin/opencode` (OpenCode 1.18.31).
  `/opt/homebrew/bin/cmux`, a terminal workspace manager for agent sessions, is
  also installed and running. Versions were read on 2026-09-17.
- **How global agents workspace instructions reach global Hermes:**
  `~/.claude/CLAUDE.md` is a symlink to
  `~/agents/AGENTS.md`. The canonical kernel therefore loads when
  Hermes works with its working directory set inside `~/agents`, and
  Hermes also surfaces the nearest `AGENTS.md` for any directory a tool call
  touches, including the private repo's root guidance. From the home
  directory, no canonical file loads on its own.
- **Hermes current project (`~`):** no `.hermes.md`, no `AGENTS.md`,
  and no `.cursorrules`. There is no folder-scoped Hermes configuration.

## Source Mapping (September 17 baseline; browser and MCP rows superseded below)

| Global agents workspace concept | Global Hermes implementation |
|---|---|
| Instructions | `SOUL.md` for identity. The canonical `AGENTS.md` loads only when the working directory or a touched file sits under `~/agents` or the private repo. |
| Skills | `agents-workspace`, `browser-use`, six task/search loaders and the three bundled CLI-name overrides point to canonical sources. Other workspace skills are not mirrored wholesale. |
| Workspace routing | One local Hermes skill, `agents-workspace`, routes workspace work to the canonical files and read gates. It is a loader and carries no workspace procedure text. |
| `task-explore` and `task-execute` | Not launchable as maintained roles. Hermes has one delegation primitive, `delegate_task`, with a global child pin but no maintained per-role wrapper. See "Harness Launch" below for the separate CLI caller path. |
| Worker model wiring | `delegation.provider: opencode-go` and `delegation.model: glm-5.3-flash` implement the briefing's Hermes child row. This is one global native-child pin, not a per-tier mapping. Applied and smoke-tested on 2026-10-01. |
| Commands | Workspace skills are not exposed as Hermes slash commands, cron jobs, or native tools. |
| Durable work (specs, changes, artifacts, memory) | Reached with ordinary file tools against `~/agents`, under the workspace's own conventions and read gates. |
| Private repo | Reachable by file tools, governed by that repository's own root guidance, which wins on privacy and Git rules. |
| MCP connectors | Browser routes plus `parallel`, `exa`, and `firecrawl` are configured in global Hermes. Search MCP calls passed in fresh CLI sessions; the running Discord gateway still needs reload. Other curated connectors follow prior decisions. |

The API-server model-route map now also lists `gpt-6.1-sol`; its older `gpt-6-sol` route remains for explicit callers. Existing session pins and the in-memory API/gateway server still require their own session selection or reload before reflecting config changes.

## Skills

On 2026-10-01, six global Hermes loaders point to the global agents workspace
`task-codex`, `task-claude`, `task-opencode`, `task-gemini`, `web-search`, and
`web-search-advanced` skills. They carry no launch procedure or model choice.
The old global Hermes `codex`, `claude-code`, and `opencode` bundled skills
were replaced by same-name local wrappers pointing to the matching `task-*`
skill and briefing. Hermes seeds bundled skills into the local directory;
deleting only the local copy would let a future sync restore the old recipe.
`hermes skills list-modified` records these wrappers as user-modified so
updates keep them. No bundled skill was disabled globally. The global Hermes
`hermes-agent` and `computer-use` skills remain available. Discovery does not
authorize a CLI handoff or prove a live child run.

The existing Hermes-local `browser-use` loader is also discovered. It points to the portable browser route selector and is not proof that each browser identity or controller is signed in and usable. The native browser MCP entries and signed-in verification limits remain governed by the browser-use state and the per-route live checks.

On 2026-09-30, global Hermes added the default-on `parallel`, `exa`, and `firecrawl` hosted MCP servers with environment-placeholder headers, full trust (no per-call approval), 120-second tool timeout, disabled sampling and a narrow tool allowlist. Parallel pins `mode=fast`; Exa exposes only search/fetch with `defaultSearchType=instant`; Firecrawl selects search, scrape, map and parse, excluding crawl, agent, interact and monitors. `hermes mcp test` connected to each; fresh CLI one-shot sessions called each server's search tool and returned the official Python homepage, with tool names independently read from the session store. This establishes fresh-CLI readiness, not yet a gateway reload in this running Discord session. Exa's key is installed in Hermes's private `.env`; no key values belong in this mapping. Built-in web tools and existing browser connectors were not changed. `web.keyless_fallback` and `web.keyless_rescue` remain off.

The September 17 baseline exposed no canonical workspace skill. Browser-use was added later and the three original task bridge loaders were added on September 30. The browser loader's discovery does not prove a browser task or another harness's skill auto-discovery.
Audit any further native skill settings in a Hermes-owned `/sync-tool-adapter`
run. Do not alter another harness configuration here.

The global Hermes `agents-workspace` loader continues to point at the
canonical kernel and read gates. The old `delegation-routing` recipe is now
a thin pointer to the briefing, worker tiers, and named workspace task skills.
Global Hermes `hermes-model-config` and `hermes-model-catalog-maintenance`
remain technical Hermes procedures, not model-selection policy. GUI, browser,
cron, computer-use, and desktop skills remain, with outdated model-selection
and CLI launch instructions stripped. The unverified batch-size explanation
was removed from the `delegate_task` diagnostic reference; it now requires
submitted-call and log evidence before attributing a cap. No skill was deleted.
The backup of edited global Hermes files is at
`~/.hermes/backups/delegation-guidance-cleanup-2026-10-01/`.

## Roles and Worker Tiers

| Role | Model and reasoning | Availability | Native launch form |
|---|---|---|---|
| `task-explore` | none | Unsupported, because `delegate_task` has a global child pin but no maintained role wrapper or per-launch role/model selection. | Not available. Do not substitute a generic subagent. |
| `task-explore-fast` | none | Disabled by `roles/task-worker-tiers.md` | Refuse launch. |
| `task-explore-high` | none | Enabled by current tier policy but unsupported in Hermes without a verified explicit-model maintained role wrapper. | Not available. |
| `task-execute` | none | Unsupported, for the same maintained-role reason as `task-explore`. | Not available. Do not substitute a generic subagent. |
| `task-execute-fast` | none | Disabled by `roles/task-worker-tiers.md` | Refuse launch. |
| `task-execute-high` | none | Enabled by current tier policy but unsupported in Hermes without a verified explicit-model maintained role wrapper. | Not available. |

The current tier policy enables default and high explore/execute wrappers, but Hermes has not mapped them to verified maintained role wrappers. Both fast wrappers remain disabled. Do not substitute a generic subagent or inherit the root model.

Two limits are recorded rather than papered over. First, the global child pin
does not provide a maintained role wrapper or per-role selection. Second,
Hermes cannot enforce `task-explore`'s create-only output
directory at the tool layer; if a Hermes path ever runs that role, the root must
assign an exclusive output directory and verify the result.

Hermes does own a separate native capability: `delegate_task` children run in
isolated contexts with a concurrency ceiling (`delegation.max_concurrent_children`).
Their explicit provider/model pin follows the briefing's Hermes row. It is not
a mapping of `task-explore` or `task-execute`.

## Frontier Orchestrator

`task-orchestrator` is enabled by tier policy only where explicitly mapped and verified; Hermes has no such maintained wrapper, so it is unsupported here. `task-orchestrator-fast` remains disabled.

## One-Run Role Profiles

- **Selectable maintained roles:** none from global Hermes. No maintained-role
  wrapper exists here, so there is nothing for a one-run profile to select.
- **What Hermes does have:** a per-session model choice for itself, and the ability
  to launch a different harness once with an explicit model. The second path
  belongs to that harness's adapter, not to this one. Hermes is the caller, not the
  runtime. The reviewed call forms for it are recorded in "Harness Launch (Hermes
  as Caller)" below.
- **Model discovery:** `opencode models` lists the OpenCode provider and model
  identifiers, and 420 were available on 2026-09-17. Hermes's own list comes from
  `hermes models` or the in-session model picker. Claude Code and Codex expose no
  model-list command; each takes an explicit identifier or falls back to its own
  configured default.
- **Model choices and effort:** read the briefing's Hermes rows. Native settings
  are implementation details, not another source of model advice.
- **Native children:** one explicit global provider/model pin, applied on
  2026-10-01. Per-call model selection remains unsupported.
- **Verification status:** the worker-tier and role cells remain roster-only, and
  they stay disabled or unsupported. The model identifiers come from
  `opencode models` and Hermes's own model list. Dated 2026-09-17 harness
  call smokes are historical only; current forms live in the task skills.
- **Concurrency:** the global agents workspace budget in
  `roles/task-worker-tiers.md` applies, and a lower Hermes or provider limit wins.
- **Cancellation and capture:** Hermes subagent control for its own delegation, and
  process control for a launched harness.
- **Unsupported cases:** native maintained-role launch, per-call model selection
  for subagents, and any fast or priority service control for a maintained role.

## Harness Launch (Hermes as Caller)

For a user-authorized bounded CLI handoff, global Hermes loads the matching
global agents workspace skill under `~/agents/skills/task-*/SKILL.md`
and its linked capability guide. Read
`~/agents/ai-models/delegation-briefing.md` for the chosen
model, limits, and trust checks. The task skill owns packet, flags, permission,
capture, and supervision. This adapter does not copy those instructions or the
old September 17 launch forms, which included obsolete CLI syntax. The
Hermes process remains responsible for independent verification of the result.
A CLI child is not a maintained Hermes worker-tier role.

## Connectors and MCP (historical snapshot plus new browser guidance)

The no-MCP inventory in this file's September 17 baseline is historical, not
current readiness. Later browser-use tests in
`specs/browser-use/STATE.md` describe Hermes Jev and
Playwright MCP entries, a native CDP route, and separate login identities. The
shared registry now describes native browser tools, MCP, CLI/library, hosted/API,
and desktop bridges. Listing Hermes's browser and computer-use tools there is a
portable **capability description**, not native configuration or automatic
permission for another harness. Current effective entries and enablement must be
audited inside Hermes before a fresh readiness claim. Signed-in routes require
their own dated enablement decision and account-only smoke; a registered or
configured tool alone does not transfer a login.

## Permissions and unattended execution

Permission bootstrap applied in Hermes on 2026-10-01, following
`~/agents/conventions/autonomous-task-permissions.md`.
The persistent default-profile settings in `~/.hermes/config.yaml`
are `approvals.mode: off`, `approvals.cron_mode: approve`,
`approvals.single_query_mode: approve`, and `approvals.unattended_mode: approve`.
`terminal.backend` remains `local`: shell execution is not container-sandboxed.
This covers shell/interpreter/task-script commands and authorized CLI launches,
including absolute executable paths, without a command-by-command allowlist.
It does not configure permissions inside another harness.

Copyable one-shot launch: `hermes chat -q '<authorized task>'`.
The saved defaults need no extra bypass flag. For an explicitly authorized
per-invocation bypass, Hermes supports `hermes chat --yolo -q '<authorized task>'`;
this skips command approval checks, not hardline blocks or OS protections.
The approval reader loads the live file-signature-cached config before checks,
so these approval keys do not require a gateway restart. Hosted-room policies
can override profile settings; foreign CLI sessions retain their own controls.

Root sessions and native Hermes children use this shared approval configuration;
no maintained workspace orchestrator or explore/execute wrapper was enabled or
added. Their existing unsupported/disabled status and child limits are unchanged.
Packet scope under full shell access is instruction-enforced, not a filesystem
sandbox. Existing MCP enablement, tool allowlists and trust settings are unchanged;
`approvals.mode` is a shell-command setting, not blanket MCP consent.

Secret redaction, vault-mediated entry, hardline command blocks, supervised-gateway
lifecycle guards, platform privacy controls and task/account authority remain.
This supported mode bypasses shell approval checks broadly, not only routine
arguments, so scope must still be enforced by the agent. No connector installation,
provider handoff, model change or unrelated destructive action is authorized.
A private configuration backup was retained under Hermes's own backups directory.

Status: configuration saved and read back; the installed runtime resolver returned
`off / approve / approve / approve`. No agent/worker smoke campaign was run for
this permission-only update. This is static/runtime-loader verification, not proof
that every future scheduled task or foreign CLI can never encounter a blocker.
This section supersedes earlier approval-preservation and September 17 caller
restriction descriptions where they conflict with the canonical permission policy.

## Commands and Permissions

Global Hermes exposes no command wrapper for `sync-tool-adapter`. Its available
entrypoints are skills, the `hermes` command line, and scheduled jobs. The local
`agents-workspace` skill is the supported way for Hermes to reach this workspace's
procedures.

Hermes keeps its own approval model: a security scan and allowlist for terminal
commands, approval scopes for desktop control, and vault-mediated credential entry.
It does not use a file-based permission mode. Role profiles, if ever added, must
preserve that model and must not broaden permissions. The permission posture Hermes
applies when it calls a foreign harness is a separate matter and is recorded under
"Harness Launch (Hermes as Caller)".

## Recheck Points

- Reconcile the actual `mcp_servers` entries against the current registry; the
  September 17 no-MCP baseline was superseded by later browser pilots.
- Audit `skills.external_dirs`, `skills.auto_load`, `skills.create_dir`, and
  `skills.trusted_project_dirs` in a Hermes-owned sync before asserting shared
  skill discoverability; the older empty-list expectation predates `/browser-use`.
- Confirm the `agents-workspace` skill still contains routing and canonical paths
  only, with no copied workspace procedure text.
- Confirm `~/.claude/CLAUDE.md` still symlinks to
  `~/agents/AGENTS.md`, and that `~/.agents/AGENTS.md` still symlinks to
  the same canonical file.
- Confirm maintained worker roles remain unsupported unless explicit role wrappers
  are added and verified. The native-child pin does not enable those roles.
- Recheck native model settings against the briefing when its Hermes rows change.
- Re-read the matching workspace `task-*` skill and capability guide before a CLI
  launch. Verify its current flags and permissions rather than relying on old
  September 17 launch forms.
- Confirm no cmux hooks have been installed for Hermes and `cmux.json` is unedited,
  unless the user asks for that integration.

## Web reference, 2026-10-01

By default use this harness's built-in search and fetch. [Capabilities/web](../capabilities/web/README.md) owns tool strengths, both ladders, costs and compatibility. Use web-search only on explicit user request or when a task packet names it. web-search-advanced requires an explicit user request by name. Both canonical skills set disable-model-invocation: true and metadata.opencode/autoinvoke: false. Native discovery metadata must be aligned in this tool's own session. This shared-doc change did not inspect, edit or verify native loaders. Keep the native wiring and approved fallbacks documented above.
