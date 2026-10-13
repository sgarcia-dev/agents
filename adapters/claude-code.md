---
created_at: 2026-09-15
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: adapter
purpose: Document the current Claude Code mapping from Agents workspace source-of-truth roots to native Claude Code surfaces.
related:
  - path: ~/agents/adapters/adapter-contract.md
    why: Platform-neutral adapter rules and reconciliation requirements.
  - path: ~/agents/adapters/claude-code.divergences.md
    why: Current intentional Claude Code differences and pending decisions.
  - path: ~/agents/capabilities/connectors.md
    why: Portable connector registry that Claude Code reconciles against.
  - path: ~/agents/roles/task-worker-tiers.md
    why: Portable worker-tier semantics this mapping resolves.
---

# Claude Code Adapter

The Agents workspace remains canonical. Native Claude Code configuration, skills,
subagents, commands, MCP servers, plugins, permissions, and hooks are
implementation details. Onboarded 2026-09-15, in this Claude Code's own session.

## Native Surfaces

- Global instructions: `~/.claude/CLAUDE.md`, a symlink to
  `~/agents/AGENTS.md` (same inode as the shared `~/.agents/AGENTS.md`
  discovery-layer symlink).
- Global skills: `~/.claude/skills/<name>/SKILL.md`.
- Global subagents: `~/.claude/agents/<name>.md`.
- Global commands: `~/.claude/commands/<name>.md`.
- Global settings: `~/.claude/settings.json` (model, effort, notification, and
  permission defaults) and `~/.claude/settings.local.json` (this machine's
  permission allow/deny/ask lists).
- Native MCP servers: `~/.claude.json` (`mcpServers`: `parallel`, `exa`,
  `firecrawl`, added 2026-09-29) plus the
  four claude.ai-managed connectors (Claude Docs, Google Calendar, Google Drive,
  Gmail), visible via `claude mcp list`.
- Native plugins/marketplaces: `~/.claude/plugins/`. Marketplaces
  `claude-plugins-official` and `openai-codex` are registered. One plugin is
  installed: `codex@openai-codex` (added by the user 2026-10-02, see "Codex
  plugin" below).
- Host-synced skills: `~/.claude/skills/synced/` holds nine skills pushed from the
  claude.ai account (`docs`, `docx`, `pptx`, `xlsx`, `pdf`, `skill-creator`,
  `import-memory`, `morning`, plus staging). Host-managed and re-synced
  automatically; not hand-edited and not promoted to the global agents workspace.
  `~/.claude/skills/.trash/` is harness housekeeping.
- Shared discovery layer: `~/.agents/AGENTS.md` and
  `~/.agents/skills/` are also present (used by OpenCode) but Claude
  Code does not read `~/.agents/`; its own `~/.claude/CLAUDE.md` and
  `~/.claude/skills/` are the surfaces that matter for this tool.

## Source Mapping

| Agents workspace concept | Claude Code surface | Required posture |
|---|---|---|
| Instructions | `~/.claude/CLAUDE.md` | Symlink (same inode) to `~/agents/AGENTS.md`. Not a copy or thin redirect file. |
| Skills | `~/.claude/skills/<name>/SKILL.md` | Thin loader: frontmatter `name`/`description` plus one line loading the canonical `agents/skills/<name>/SKILL.md` file by absolute path. Never copy procedure text. |
| Roles (`task-explore-high`, `task-execute-high`, `task-orchestrator`) | `~/.claude/agents/<name>.md` | Thin loader: native `name`/`description`/`model`/`effort`/`tools`/`disallowedTools` plus a short body loading the canonical role and tier files. Never copy packet types, behavior, stop conditions, or report shape. |
| Commands | `~/.claude/commands/<name>.md` | Thin pass-through: `description` plus one line invoking the matching skill with `$ARGUMENTS` verbatim. Never reinterpret arguments or copy skill procedure/stop rules. |
| Connectors | `~/.claude.json` `mcpServers` plus claude.ai-managed connectors | Reconcile only against `../capabilities/connectors.md`. |

## Skills Mapped (15 of 21)

Fifteen canonical skills are mapped: `research`, `research-deep`, `plan-create`,
`plan-execute`, `plan-reconcile`, `memory-reconcile`, `sync-tool-adapter`,
`task-opencode` (added 2026-09-28), `task-codex` (added 2026-09-28), and
`web-search` (added 2026-09-29), plus `browser-deep-research-prompts`
(added 2026-10-05), `web-search-advanced` (loader only, no command), and the
three browser skills `browser-use`, `chatgpt-browser` and `claude-browser`
(added 2026-10-05). Each has a `~/.claude/skills/<name>/SKILL.md` loader and,
except `web-search-advanced`, a matching `~/.claude/commands/<name>.md`
pass-through command.

The three browser skills were canonical since 2026-09-29 and loaded in Codex,
OpenCode, Gemini and Hermes, but were never mapped here, so Claude Code could
not use them. Fixed 2026-10-05 after a browser run could not reach them. The
loaders appeared in the live session's skill list right after being written.

### Browser route

Claude Code's browser route is the Claude in Chrome extension. `~/.claude.json`
shows it installed, onboarded and on by default. On 2026-10-05 its tools were not
exposed to the CLI session doing this fix, and no browser task has been run from
Claude Code, so the route is **not verified** here. The recorded passing browser
runs are Hermes and Codex on the dedicated signed-in Chrome (see
`specs/browser-use/STATE.md`). Until a Claude Code smoke passes, hand signed-in
browser jobs to those harnesses. Claude in Chrome running in claude.ai or as the
extension reads only claude.ai account skills, never this machine's files, so the
loaders above do not reach it.

Not yet mapped and not yet decided: `artificial-analysis-model-data`,
`task-gemini` and `task-hermes`.

`task-opencode` lets Claude Code hand work to OpenCode's cheap models through
the OpenCode CLI, including many small read-only checks in parallel. User
decision 2026-09-28: Claude Code models are too costly for mass fan-out, so this
is the approved way to do it. Verified the same day from this Claude Code: 10
parallel `opencode run` tasks (DeepSeek V4.1 Flash and Muse Spark 1.3, `#low`)
all finished in 7s, both on the shared service and with `--standalone` plus
the subagent block. Children start with subagents blocked by default (CLI
child rule in `../roles/task-worker-tiers.md`). Default parallel count is the caller's call per task; the
user suggested around 10 for cheap read-only checks.

`task-codex` lets Claude Code hand a bounded task to the Codex CLI, only when the
user asks. User decision 2026-09-28: the main reason is research Claude cannot
do, such as social media and Reddit posts. Children block subagents by default
(`--disable multi_agent`).

### Codex plugin (extra option, not a worker route)

User decision 2026-10-02: the OpenAI `codex` plugin is an extra option the root
Claude session may use. It is not the standard worker route, and the native
`task-*` agents stay on Claude models. It still sends work to OpenAI, so the
explicit-request rule for cross-provider bridges applies: suggest it, or use it
when the user asks. Do not wrap it in Claude subagents; the root calls it
directly. Models come from `../ai-models/delegation-briefing.md` (Codex rows).

- Call: `node ~/.claude/plugins/cache/openai-codex/codex/<version>/scripts/codex-companion.mjs task --background --write --model <model> --effort <effort> "<packet>"`,
  then `status --all` and `result <job-id>`. Several background jobs run in
  parallel from one root (tested 2026-10-02: 3 at once, about 11 s each on
  GPT-6.1 Sol low, each its own Codex session).
- Permissions: the plugin is read-only unless `--write` is passed. Always pass
  `--write` to match `../conventions/autonomous-task-permissions.md`; leave it
  off only for clearly high-risk work such as operating system changes.
  Explore-style packets stay read-only by packet scope, not by sandbox.
- Pick the plugin for quick local reading or coding jobs in parallel. Pick
  `task-codex` (`codex exec`) for web research (`--search`), when browser,
  computer use, apps or subagents must be switched off (the plugin has no
  flags for these), or when the JSONL event log is needed to audit tool calls.

Three canonical skills are intentionally not mapped (see the divergence ledger):

- `task-claude`, added 2026-09-28 for other harnesses to call Claude Code.
  Claude Code calling itself through the CLI is pointless; it uses native
  subagents instead.

- `model-bakeoff`, user-approved skip 2026-09-15.
- `role-dispatch`, unmapped 2026-09-22. The skill exists for harnesses that
  expose many models per role. Claude Code has a small roster and its native
  subagent interface already covers the useful cases, so the skill earns nothing
  here. Removed from `~/.claude/skills/` and `~/.claude/commands/`. The canonical
  skill remains in the global agents workspace for other tools.

## Worker Tier Matrix (user decision 2026-10-07)

| Tier cell | Current Claude Code mapping |
|---|---|
| `task-explore` default | `~/.claude/agents/task-explore.md`, `model: claude-haiku-5-5`, `effort: high` (user decision 2026-10-07; was Sonnet 5.5 medium). Static change, live-checked 2026-10-08 (each worker reported its model; both execute workers wrote a test file). Denies `Edit, Write, NotebookEdit, Agent`. |
| `task-explore` fast | Disabled by `../roles/task-worker-tiers.md`. Not mapped. |
| `task-explore` high | `~/.claude/agents/task-explore-high.md`, `model: claude-sonnet-5-5`, `effort: high` (user decision 2026-10-07; was Opus 5.5 low). Static change, live-checked 2026-10-08 (each worker reported its model; both execute workers wrote a test file). |
| `task-execute` default | `~/.claude/agents/task-execute.md`, `model: claude-haiku-5-5`, `effort: high` (user decision 2026-10-07; was Sonnet 5.5 medium). Static change, live-checked 2026-10-08 (each worker reported its model; both execute workers wrote a test file). Denies `Agent`. |
| `task-execute` fast | Disabled by canonical tier guidance. Not mapped. |
| `task-execute` high | `~/.claude/agents/task-execute-high.md`, `model: claude-sonnet-5-5`, `effort: high` (user decision 2026-10-07; was Opus 5.5 low). Static change, live-checked 2026-10-08 (each worker reported its model; both execute workers wrote a test file). |

**Parked default wrappers (both re-enabled 2026-09-28; the parked copies remain as history).** The old `task-explore.md` and `task-execute.md`
(Sonnet 5, medium via `modelSettings`) moved on 2026-09-23 to
`~/.claude/rollback-20260923-adapter-sync/agents/`, next to a copy of the prior
`settings.json`. To roll back, move them back into `~/.claude/agents/` and
restore that `settings.json`. While parked, Claude Code cannot select them, so no
task can quietly fall back to them.

All four worker wrappers pin the full model ID, not an alias, and pin their own
effort. None inherits the root model or root effort. Since 2026-09-30 the four explore/execute
wrappers (default and high) have no `tools` list, so they inherit every tool
the root has, including enabled MCP tools (official subagent docs: omitting
`tools` inherits all). Explore denies `Edit, Write, NotebookEdit, Agent`;
execute denies `Agent`. All are terminal: no nested dispatch. They can now see
the claude.ai connector tools too: reads run freely, and the 33 Google
mutation tools keep the root's exact-name `ask` gates. Tool access is not task
authority; the packet still sets scope. Live check: a `task-explore` child
(`claude-sonnet-5-5`) made one successful `mcp__parallel__web_search` call,
session `9c719204-668b-4e53-8e54-ee5544242e06`, zero denials.

### How Effort Resolves (corrected 2026-09-23)

The 2026-09-22 claim that subagent frontmatter has no effort field was wrong for
Claude Code 2.1.280. Agent definitions accept `effort`
(`low|medium|high|xhigh|max`). Resolution order for a child, read from the CLI
source and then observed live:

1. the agent file's `effort` field, if set;
2. otherwise `modelSettings["<model-id>"].effortLevel`;
3. otherwise the global `effortLevel`.

**Live check, 2026-09-23.** A headless root launched with `--effort medium`
dispatched `task-explore-high` with a `PreToolUse` hook logging each tool call's
reported effort. The root's calls reported `medium`. The child's `Read` reported
`low`, with `agent_type: task-explore-high`. Model usage showed only
`claude-opus-5-5` (the child's line was labeled `claude-opus-5-5[1m]`, the
1M-context form of the same model). So a medium root does **not** push medium onto
the child, and per-child low is pinned. That hook value is Claude Code's own
per-turn effort record. It is the best telemetry available here, not an API-side
receipt.

A second headless run with no flags reported the root at `low` on
`claude-opus-5-5`, confirming the saved default.

A separate low-root native dispatch to `task-execute-high` created and read back
an exact one-line scratch file; Hermes read it back independently and removed it.
The run reported `claude-opus-5-5` in model usage. Unlike the explore check above,
this execute run had no effort hook, so its low effort is confirmed by agent
frontmatter and the matching resolution rule, not direct child telemetry.

### Native Child Model Selection (verified 2026-09-22, still current)

Built-in agents such as `general-purpose` inherit the parent model unless the
root sets a per-call `model` override. Maintained wrappers avoid this by pinning
a model ID. Built-in agents are not maintained workers and must not be used as
substitutes.

### Root Default (user decision 2026-09-23)

New root sessions: `claude-opus-5-5` at **low**. `~/.claude/settings.json` sets
`model: claude-opus-5-5` and `modelSettings["claude-opus-5-5"].effortLevel: low`.
For unusually hard root work, raise one session with `claude --effort medium` at
launch. That flag is session-only and, per the live check, does not change the
high workers' pinned low. Avoid in-session `/effort` for one-offs: it may save a
new default.

Older `modelSettings` entries for `claude-opus-5` and `claude-sonnet-5` (both
medium) and the global `effortLevel: xhigh` are left as-is. They reach no model
the user runs by default and keep rollback simple.

These settings are local to this machine's Claude Code CLI. They are not shared
with the Claude desktop app or claude.ai (declined to standardize 2026-09-22).

## Permissions and unattended execution

Policy: `~/agents/conventions/autonomous-task-permissions.md`.
Saved root `permissions.defaultMode` is `bypassPermissions`; supported role
`permissionMode` settings and tool inheritance are described below. New sessions
load saved changes. Explicit unattended example:
`claude -p '<task>' --dangerously-skip-permissions --model claude-opus-5-5 --effort low`.
This flag does not automatically approve retained exact ask rules. Orchestrator
MCP inheritance must preserve its child-allowlist hook and terminal leaf Agent
exclusions. Task/account authority, models and connector choices are unchanged.
Current orchestrator follow-up is static-only, not a fresh live orchestration test.

## Frontier Orchestrator

**`task-orchestrator`: enabled (user decision and live check 2026-09-25).**

**Access follow-up 2026-09-30 (configured, static-only, NOT runtime-tested).**
The old Bash deny and `NotebookEdit` deny are gone. The wrapper has no `tools`
list, so it inherits every enabled root tool: files, Bash (any command, including
node, npm/npx, python, shells, bun, deno, uv, ruby, perl, absolute paths), web,
and enabled MCP. It runs with `permissionMode: bypassPermissions`. Child names
are enforced by the PreToolUse hook `~/.claude/hooks/orchestrator-child-allowlist.sh`
(the `Agent(...)` syntax is not enforced in subagents). The hook allows only
`task-explore`, `task-execute`, `task-explore-high` and `task-execute-high`.
Leaves still deny `Agent`. Account-mutation ask gates are unchanged.

- **Child allowlist is enforced by a hook, not by `tools`.** Claude Code 2.1.282
  ignores the `Agent(a, b)` limit inside a subagent: a live test on 2026-09-25
  let the orchestrator start `general-purpose`. The wrapper's frontmatter
  `hooks.PreToolUse` (matcher `Agent`) runs
  `~/.claude/hooks/orchestrator-child-allowlist.sh`, which blocks any
  `subagent_type` other than the four enabled default/high explore/execute leaves. The hook
  only runs inside the orchestrator, so it does not affect the root.
- **Depth.** Verified live 2026-09-25 through `claude -p`: root -> orchestrator
  -> `task-explore-high` returned the exact probe file contents. The hook refused
  `general-purpose` and a nested `task-orchestrator`. Leaves deny `Agent`, so the
  graph stops one layer below the orchestrator.
- **Leaves available.** The four enabled default/high explore/execute wrappers;
  all remain terminal. Fast workers and peer/nested orchestrators are excluded.
- **Historical headless failure.** Before the current bypass defaults, the
  orchestrator could not read its role in `claude -p` because a prompt had nowhere
  to go. Current root/role bypass defaults address routine permission gates; this
  follow-up was not live-tested.

`task-orchestrator-fast` stays disabled by `../roles/task-worker-tiers.md` and is
not mapped.

## One-Run Role Profiles

**Standing decision, 2026-09-22: native subagent dispatch is the preferred path.**
Claude Code's `Agent` tool gives context compaction, session management,
background tracking, and result capture. Do not shell out to terminal `claude`
instances for normal delegation. This rule is about Claude calling Claude. Using
the OpenCode CLI through `task-opencode` for cheap models is allowed (2026-09-28).

### Preferred path: native `Agent` dispatch

- **Selectable roles**: `task-explore`, `task-execute`, `task-explore-high`,
  `task-execute-high`, `task-orchestrator`. Fast workers and the fast orchestrator
  remain unselectable.
- **Model**: the wrapper's `model:` field. The `Agent` tool also has a per-call
  `model` override (`sonnet`, `opus`, `haiku`, `fable` aliases) for explicit
  user-invoked one-run exceptions.
- **Reasoning**: the wrapper's `effort:` field. The `Agent` tool has no per-call
  effort parameter, so a one-run effort change is unsupported natively; record it,
  do not work around it.
- **Service class (fast/priority)**: not available per dispatch.
- **Concurrency**: the canonical guidance in `../roles/task-worker-tiers.md`
  applies, with counts from the model labels in the delegation briefing. Every
  Claude Code worker is premium (Claude quota), so the usual count is 1 to 3 per
  pool. Claude Code now maps both default and high workers; the earlier high-only
  mapping and its 1-3-total description predate the September 28 re-enablement.
  Use the canonical separate-pool guidance per root or orchestrator. An explicit user request for more is
  honored. No native per-session or global cap is configured, on purpose
  (user decision 2026-09-25), so exceptions stay possible.
- **Capture and verification**: results return to the root, which checks them.

### Available but not preferred: headless CLI

Present in Claude Code 2.1.283 (`claude --help`, rechecked 2026-09-28). Used here
only as a verification harness, never for Claude-to-Claude delegation. Other
harnesses use the same CLI through `task-claude`; the full, live-checked reference
is `../capabilities/claude-cli.md`.

- `--agent <name>`, `--model <alias|full-id>`, `--effort <level>` (session only).
- `-p`, `--output-format json|stream-json`, `--settings <file>` (used to inject
  the temporary logging hook), `--permission-mode`.
- `--bg` plus `claude agents --json`, `claude logs <id>`, `claude stop <id>`.
- `--fallback-model` must stay unused: silent model substitution is forbidden.

**Model discovery**: there is no `claude models` command. Roster from harness
documentation: `claude-opus-5-5`, `claude-sonnet-5-5`, `claude-haiku-5-5`
(added 2026-10-07), `claude-fable-5-1`, and older `claude-opus-5`,
`claude-sonnet-5`, `claude-haiku-4-5-20251001`. `claude-opus-5-5` is proven
runnable by the 2026-09-23 live checks.

### Favorite models (user-confirmed 2026-09-23)

Model choices now live only in
`~/agents/ai-models/delegation-briefing.md` (section 3, Claude
Code). The table below records what the native files pin and when they were
checked; if it disagrees with the briefing, the briefing wins and this tool
needs a sync. Since 2026-10-01 each wrapper's `description` also carries a short
model and cost note, because Claude Code shows descriptions to the root at
dispatch time. Keep those notes in step with the briefing on every sync.
Since 2026-10-07 every worker and orchestrator description ends with "Before
dispatch, read the Claude Code part of section 3 of the delegation briefing."
That part's six-line block (how the tiers compare, what each takes, how much to
delegate) replaced the fixed count the descriptions used to carry. Static
change: agent files load at session start, so a fresh session shows it.

| Use | Model | Effort |
|---|---|---|
| New root sessions (default) | `claude-opus-5-5` | low |
| Root, unusually hard one-off | `claude-opus-5-5` | medium, via `claude --effort medium` at launch |
| `task-explore-high` | `claude-sonnet-5-5` | high (pinned in agent file, 2026-10-07) |
| `task-execute-high` | `claude-sonnet-5-5` | high (pinned in agent file, 2026-10-07) |
| `task-explore` default | `claude-haiku-5-5` | high (pinned in agent file, 2026-10-07) |
| `task-execute` default | `claude-haiku-5-5` | high (pinned in agent file, 2026-10-07) |
| `task-orchestrator` | `claude-opus-5-5` | medium (pinned in agent file, 2026-10-01; static change, not run-tested) |

Because `role-dispatch` is unmapped in Claude Code (see Skills Mapped), this
section documents the adapter's capability, not an exposed skill.



## Connectors / MCP Inventory

- **Global agents workspace registry** (`../capabilities/connectors.md`):
  `playwright`, `chrome-devtools`, `figma`, `git`, `github`. None of the five are
  configured in global Claude Code.
  **User decision 2026-09-22: add none, mirroring OpenCode**, which also has no
  MCP server configured and its connector onboarding deferred. Revisit when the
  user wires connectors in either harness.
- **Registry default-on web connectors, configured and on in global Claude
  Code (2026-09-29, keyed):** `parallel`, `exa`, `firecrawl`, user scope in
  `~/.claude.json`, set up per
  `~/agents/capabilities/web/tools/parallel.md`. Permissions in
  `~/.claude/settings.json`: allow `mcp__parallel__*`, `mcp__firecrawl__*`,
  and `mcp__exa__*` with no `ask` rules (user decision 2026-09-29: no
  prompts; usage follows capabilities/web/README.md. Verified headless with and
  without `--dangerously-skip-permissions`: Parallel search, Firecrawl
  search, and scrape all ran, no denials); deny Firecrawl `crawl`, `agent`,
  `interact`, and the eight `monitor_*` tools (absent from the tool list in
  both runs); plus `env.MCP_TOOL_TIMEOUT = 120000`. Keys come
  from `PARALLEL_API_KEY`, `EXA_API_KEY`, `FIRECRAWL_API_KEY` through the
  `headersHelper` running `capabilities/mcp/search-key-header.sh`, which
  reads the env var or else the Keychain (no key in config; Parallel URL
  pinned to `?mode=fast`). Replaced `${VAR}` headers on 2026-09-29 after a
  Claude Code restarted in an old terminal tab sent them as literal text. Smoke passed keyless and keyed; see
  the dated MCP test evidence in capabilities/web. Built-in `WebSearch` and
  `WebFetch` stay on. The October 1 default uses native tools without a skill;
  provider escalation follows capabilities/web/README.md.
- **Only in global Claude Code**: four claude.ai-managed connectors, all
  browser-OAuth and host-managed, all verified Connected via `claude mcp list`
  on 2026-09-22, `claude.ai Claude Docs` (new since the last sync),
  `claude.ai Google Calendar`, `claude.ai Google Drive`, `claude.ai Gmail`.
  **User decision 2026-09-22: keep all four Claude-only.** Not promoted to the
  global agents workspace registry; they are account-level Anthropic connectors
  that cannot be expressed portably for other tools.
  Root-level health verified 2026-09-22: the Gmail and Google Drive connectors
  work from the root session. The check itself only confirmed connectivity
  (tool listing/auth reachability) and did not read any message or file
  content.
  A native general-purpose subagent, launched from the root the same day,
  inherited both connector tool sets and ran a minimal read-only smoke (a
  bounded Gmail and Drive read) successfully. That confirms `general-purpose`
  subagents inherit whatever MCP tools the parent session has, matching plain
  Claude Code subagent inheritance behavior; it is not a maintained
  maintained worker capability. See Worker Tier Matrix above for
  why the maintained wrappers behave differently, and Drift Checks for the
  write-capable-tool caution this implies for any future connector-research
  packet.
- **Claude Code current project**: this run started in
  `~/agents-workspace` (which `~/agents` symlinks to).
  That folder carries no `.claude/` directory, no `.mcp.json`, and no project
  `CLAUDE.md`, so there is no project place to report.
- Note for future runs: `~/.claude.json` records per-project MCP servers for
  several unrelated folders under `~/Code/`. Those are outside any run rooted in
  the Agents workspace and are not reconciled here.

## Permissions And Policies

- `~/.claude/settings.json`: `model: claude-opus-5-5` and
  `modelSettings["claude-opus-5-5"].effortLevel: low` (set 2026-09-23); older
  `claude-opus-5`/`claude-sonnet-5` medium overrides and global
  `effortLevel: xhigh` retained but unused by default;
  `alwaysThinkingEnabled: false`,
  `skipDangerousModePermissionPrompt: true`, `tui: fullscreen`.
- **Found 2026-09-28, not reverted:** `settings.json` now has `model: opus`
  (an alias) and `modelSettings["claude-opus-5-5"].effortLevel: high`. The user
  changed these with `/model` and `/effort` outside adapter work. Needs a user
  decision: keep, or restore `claude-opus-5-5` at low.
- **Prompt-free default (2026-09-30, owner decision in
  `~/agents/conventions/autonomous-task-permissions.md`):**
  `permissions.defaultMode: bypassPermissions` in `~/.claude/settings.json`.
  Every new root session, including `claude -p`, starts with full access and no
  prompts. Worker wrappers set no `permissionMode`, so they inherit it.
  Live-checked in a fresh `claude -p` with no bypass flag: root mode
  `bypassPermissions`, zero denials, all four worker cells ran shell and file
  work. Kept: the Firecrawl crawl/agent/interact/monitor deny rules (deny still
  applies under bypass). Google connectors: the 17 read tools (Gmail search/get/
  list, Drive search/read/metadata/permissions/download, Calendar list/get/
  search/suggest) are prompt-free; the 33 write/send/share/trash/label/delete/
  respond tools (exact names from the exposed tool list, 2026-09-30) have
  exact-name `ask` rules. Official docs say `ask` beats allow and is not
  auto-approved under bypass; not live-tested locally on these tools. A tool
  Google adds later is prompt-free until listed.
  Full access is not path confinement: any Bash call can touch any path the
  user can.
- `~/.claude/settings.local.json`: machine-local `permissions.allow` list
  (`Bash(sed:*)`, `Bash(mega-ls:*)`, `Bash(mega-whoami:*)`); empty `deny`/`ask`.
  Unchanged this run.
- No hooks and no status line are configured.
- Built-in Claude Code agent types (`general-purpose`, `Explore`, `Plan`,
  `claude-code-guide`, `statusline-setup`, `claude`) exist natively and are kept
  in the harness. Canonical dispatch rules in `../roles/task-worker-tiers.md`
  forbid delegating through them; their presence is not permission to use them.

## Drift Checks

- `~/.claude/CLAUDE.md` remains a symlink (same inode) to
  `~/agents/AGENTS.md`. Verified 2026-09-22: inode 44642143 on both
  sides.
- Fifteen `~/.claude/skills/*/SKILL.md` loaders exist (the canonical set minus
  `model-bakeoff`, `role-dispatch`, `task-claude`, and the three undecided
  skills listed under Skills Mapped), each containing only
  `name`/`description` frontmatter and one canonical-file loading line.
- Fourteen matching `~/.claude/commands/*.md` files (none for
  `web-search-advanced`) contain only `description`
  frontmatter and one line invoking the skill with `$ARGUMENTS` passed through
  unmodified.
- `~/.claude/skills/role-dispatch/` and `~/.claude/commands/role-dispatch.md`
  stay absent. Recreating either requires a fresh user decision.
- `~/.claude/agents/` holds exactly `task-explore.md`, `task-execute.md`,
  `task-explore-high.md`, `task-execute-high.md`, and `task-orchestrator.md`, each with only native identity/model/effort/tools
  frontmatter and a short canonical-loading body. Old parked copies remain in `~/.claude/rollback-20260923-adapter-sync/` as history.
- The regular wrappers keep `model: claude-haiku-5-5` and `effort: high`; the
  high wrappers keep `model: claude-sonnet-5-5` and `effort: high` (2026-10-07).
  Their descriptions carry the briefing's one-line cost and trust note.
- Root default found changed on 2026-10-07: `settings.json` has
  `model: opus` (alias) and `modelSettings["claude-opus-5-5"].effortLevel:
  high`, while the briefing and this doc say `claude-opus-5-5` at low. Left
  as-is: `/effort` and `/model` save new defaults through ordinary use, so a
  changed value may be the user's intent. Needs the user's decision before
  either side changes.
- **Agent files load at session start.** On 2026-10-07 the four wrappers were
  repointed mid-session; native dispatches from that same session still ran
  the old models (children reported `claude-sonnet-5-5` and `claude-opus-5-5`).
  Later in the same session, after a `/compact`, all four reported their new
  models (2026-10-08), so live-check after a compact or from a fresh session.
  Headless `claude -p` signs in with `CLAUDE_CODE_OAUTH_TOKEN` from the
  user's shell profile. Claude Code's shell tool does not pass that variable
  through, so a `claude -p` launched from inside Claude Code reports "OAuth
  session expired" unless the variable is supplied to that command. With it,
  `--agent task-explore` passed on 2026-10-08 (see `capabilities/claude-cli.md`).
- Delegation uses native `Agent` subagents. Any packet that shells out to a
  terminal `claude` instance for a maintained role is drift unless that packet
  states why the native path could not work. `opencode run` through
  `task-opencode` and `codex exec` through `task-codex` are not drift.
- Claude Code cannot natively distinguish "create a new file" from "overwrite an
  existing file" inside its `Write` tool permission model. `task-explore-high`'s
  `disallowedTools` blocks `Write` entirely by default, which is stricter than
  the canonical role (create-only reporting into one assigned directory).
  Since 2026-09-30 the canonical `task-explore` role lets both explore roles
  create their own new report in the assigned directory with Bash; the native
  wrappers only link the role and the permissions convention (behavior
  live-checked before that loader cleanup). Folder and create-only
  limits are prompt-enforced and root-reviewed, not tool-enforced. The native `Agent`
  tool does not expose a one-run `tools` override; do not claim otherwise.
- No enabled cell resolves to "inherit the parent model" or parent effort; all
  four worker wrappers pin model and effort.
- `~/.claude/agents/task-orchestrator.md` pins `claude-opus-5-5`/`medium` (raised from `low` on 2026-10-01 by the one-step-above-high-workers rule), (before 2026-09-30) denied
  `Bash`, and keeps its `PreToolUse` `Agent` hook pointing at
  `~/.claude/hooks/orchestrator-child-allowlist.sh`. Removing the hook reopens
  generic-agent dispatch. `task-orchestrator-fast` stays unmapped.
- No native agent-count limit exists in `~/.claude/settings.json`,
  `settings.local.json`, or the environment. Adding one is drift.
- No per-role or per-subagent MCP scoping is recorded anywhere in this doc.
- `~/.claude.json` `mcpServers` stays empty while the mirror-OpenCode decision
  holds.
- The claude.ai Gmail and Google Drive connector tool sets include write-capable
  operations (for example sending mail, trashing messages, or updating/sharing
  Drive files), not just reads. Since 2026-09-30 the four worker wrappers inherit
  all root tools, connectors included (see Worker Tier Matrix). Mutation tools
  stay behind exact-name `ask` rules; packets must still name what the worker
  may do.

## Web reference, 2026-10-01

By default use this harness's built-in search and fetch. [Capabilities/web](../capabilities/web/README.md) owns tool strengths, both ladders, costs and compatibility. Use web-search only on explicit user request or when a task packet names it. web-search-advanced requires an explicit user request by name. Both canonical skills set disable-model-invocation: true and metadata.opencode/autoinvoke: false. Native discovery metadata must be aligned in this tool's own session. This shared-doc change did not inspect, edit or verify native loaders. Keep the native wiring and approved fallbacks documented above.
