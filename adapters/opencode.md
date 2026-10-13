---
created_at: 2026-09-15
updated_at: 2026-10-07
model: gpt-6.1-sol
doc_type: adapter
purpose: Map global OpenCode V2 to the canonical Agents workspace.
related:
  - path: ~/agents/adapters/INDEX.md
    why: Registry status and next action.
  - path: ~/agents/adapters/adapter-contract.md
    why: Portable reconciliation requirements.
  - path: ~/agents/adapters/opencode.divergences.md
    why: Dated user choices and unresolved differences.
  - path: ~/agents/roles/task-worker-tiers.md
    why: Worker availability and concurrency authority.
---

# OpenCode Adapter Mapping

Reconciled in OpenCode v2.0.19 on 2026-09-29. This is an implementation map,
not a source of role or skill behavior. The global agents workspace owns that
behavior. This run was started in `~`, which has no OpenCode
current-project configuration; the direct and `.opencode/` project config paths
were checked. Restart an existing client if it retains an old resolved agent.

## Native Surfaces

- Global OpenCode config: `~/.config/opencode/opencode.jsonc`.
  No `cli.json`, global agent-file directory, or configured plugin was found.
- Global OpenCode commands: `~/.config/opencode/commands/*.md`.
- Shared discovery: `~/.agents/AGENTS.md` symlinks to
  `~/agents/AGENTS.md`; thin skill loaders live in
  `~/.agents/skills/`. The OpenCode-specific `web-search` loader
  lives at `~/.config/opencode/skills/web-search/SKILL.md`.
- Live registry checks: `opencode debug config`, `opencode debug agents`,
  `opencode api get /api/skill`, `opencode api get /api/command`, and
  `opencode mcp list`. No OpenCode current project (`~`) config.

## Source Mapping

- Global OpenCode advanced-search support checked 2026-09-30: the thin loader
  at `~/.config/opencode/skills/web-search-advanced/SKILL.md`
  uses `metadata.opencode/autoinvoke: false`, retaining explicit loading without
  automatic model advertisement. The new command at
  `~/.config/opencode/commands/web-search-advanced.md` passes
  `$ARGUMENTS` unchanged. This adds a thirteenth procedure command.
- Global OpenCode supports native `websearch` and `webfetch`, but native search
  is disabled by the current `websearch: false` setting. Native fetching was
  live-verified against the official V2 tools documentation on 2026-09-30.
  User-approved 2026-09-30: for `web-search-advanced`, use Parallel search when
  native search is unavailable, and Parallel fetch when native fetching is
  unavailable. Announce the fallback and retain native fetching when it works;
  use the canonical skill's per-provider limits and receipt. This decision
  neither enables native search nor opts into other providers or helpers.
  Live `/api/skill` readback confirms the OpenCode-owned path and
  `autoinvoke: false`; `/api/command` confirms the new command is registered.
  The canonical loader body and unchanged argument placeholder were checked.
  No advanced research run or preference-dependent child smoke was performed.
- Global OpenCode's four worker mappings were synced on 2026-10-01 and passed
  sequential read-only smokes. Model choices now come from
  `~/agents/ai-models/delegation-briefing.md`, section 3, OpenCode.
  The IDs below record the native wiring and verification, not separate choices.
  Permissions did not change. Orchestrator nesting, one-run overrides and
  priority posture remain unverified.

- Global agents workspace instructions load through the shared `AGENTS.md`
  symlink. There is no duplicate OpenCode instruction body.
- Global agents workspace skills `memory-reconcile`, `model-bakeoff`,
  `plan-create`, `plan-execute`, `plan-reconcile`, `research`, `research-deep`,
  `role-dispatch`, `sync-tool-adapter`, `task-claude`, `task-codex`,
  `task-opencode`, `browser-use`, `chatgpt-browser`, and `claude-browser`
  have shared loader files. `web-search` has an OpenCode loader. OpenCode
  discovers the loaders through `/api/skill`; `task-opencode` is for other
  callers, not a self-delegating command. Built-in and externally synced
  skills are listed separately in the divergence record, not promoted.
- Twelve global OpenCode slash commands expose the applicable procedures:
  `memory-reconcile`, `model-bakeoff`, `plan-create`, `plan-execute`,
  `plan-reconcile`, `research`, `research-deep`, `role-dispatch`,
  `sync-tool-adapter`, `task-claude`, `task-codex`, `web-search`.
  They load canonical skills and pass `$ARGUMENTS` without reinterpretation.
  Browser skills are discovered as skills, not given new slash commands.
- Global agents workspace role files load through native agent `system`
  pointers. The normal orchestrator and both default/high explore and execute
  tiers resolve as subagents. Fast tiers must not launch.
  The `model-bakeoff-contestant` contract is loaded by its skill when needed,
  not mapped to a standing agent.
- Global agents workspace workflows load on demand through the relevant skill;
  no copied workflow bodies live in native commands or agents.

## Worker Tier Mapping

### Root model preference

User-confirmed 2026-09-29: global OpenCode's usual root baseline may be
`openai/gpt-6.1-sol#low`. Scale reasoning to `#medium` or `#high` for difficult
tasks. This is a changeable preference, not a required model: the user may switch
models or reasoning for a session. This request documents the preference without
pinning a global root model or resetting an existing session's selection.
GPT 6 Sol is deprecated for this user's OpenCode mappings because it is slow;
use GPT 6.1 Sol instead. This is a user preference, not a provider retirement claim.

Global OpenCode V2's top-level `model` does not retain a reasoning variant; do
not represent `model: provider/model#low` there as an enforced Low default.
Use the session model/reasoning selection or an explicit CLI `--model` for a
chosen primary run. Low, Medium, and High are roster-verified on GPT 6.1 Sol.

| Global agents workspace cell | Global OpenCode status on 2026-10-01 |
|---|---|
| `task-explore` default | Present: `opencode-go/glm-5.3-flash`; default variant; read-only smoke passed; child dispatch denied. |
| `task-explore` fast | Disabled by `../roles/task-worker-tiers.md`; no wrapper, refuse launch. |
| `task-explore` high | Present: `opencode-go/mimo-v2.6-pro`; default variant; read-only smoke passed; child dispatch denied. |
| `task-execute` default | Present: `opencode-go/glm-5.3-flash`; default variant; read-only smoke passed; edit/shell permissions unchanged; child dispatch denied. |
| `task-execute` fast | Disabled by `../roles/task-worker-tiers.md`; no wrapper, refuse launch. |
| `task-execute` high | Present: `opencode-go/glm-5.3`; default variant; read-only smoke passed; edit/shell permissions unchanged; child dispatch denied. |

The four 2026-10-01 smokes returned `# Agents Workspace`, the first line of
`~/agents/AGENTS.md`. Session and message readback confirmed each
role, the model above, `variant: default`, successful completion, reads only,
and no changed files:

- `task-explore`: `ses_f08b5b0cdffeWoqFzKA1UMKRgn`.
- `task-execute`: `ses_f08b59135ffeOnR2AWsyO5hpLv`.
- `task-explore-high`: `ses_f08b56c8fffelLgiTN4VBbNSu1`.
- `task-execute-high`: `ses_f08b531a6ffeZ0GqjvmXUeVxUp`.

These checks do not verify writes, shell execution, one-run overrides or nesting.
The caller marked the briefing's OpenCode rows live after reviewing this sync.

Global OpenCode's owner-authorized permission migration on 2026-09-30 adds
`external_directory:* -> allow` and removes the two execute wrappers' edit/shell
ask rules. Root and all four workers run routine tools with host access, not a
sandbox. Explore's source-read-only/create-only-report scope and execute's path
scope remain prompt-enforced and root-checked. All four deny `subagent:*`.
Environment-file read safeguards remain asks; Firecrawl costly-tool exclusions
remain. The orchestrator shell deny was removed in the static-only follow-up below. No model, connector, login or budget
changed. The high-worker sessions used Low reasoning and default service.
The original implementation exceeded its supervisor deadline and was resumed
only to preserve evidence and finish documentation, not to repeat tests.
Evidence and rollback details:
`changes/260930_1900__autonomous-task-permissions/results/opencode/REPORT.md` (private, not published).
Default/high pool guidance is canonical; there is no native cap.

### Sync 2026-10-07: worker and orchestrator descriptions

Worker-tier and orchestrator pass only; nothing else was inspected or changed.
The five agent descriptions in
`~/.config/opencode/opencode.jsonc` were rewritten: each keeps a
role summary, one short model line (model, effort, cost and trust labels), and
ends by pointing the root to the OpenCode part of section 3 of
`~/agents/ai-models/delegation-briefing.md`. The old "Tiny narrow"
and "Tiny bounded" capability wording, the inline counts and the quota numbers
came out; the briefing block owns them now. No model or effort changed.

- What already passed the audit: live models still `opencode-go/glm-5.3-flash`
  (task-explore, task-execute), `opencode-go/mimo-v2.6-pro`
  (task-explore-high), `opencode-go/glm-5.3` (task-execute-high) and
  `openai/gpt-6.1-sol#medium` (task-orchestrator), matching briefing section 3;
  all five still load their role files plus `roles/task-worker-tiers.md`.
- Validation: a fresh-process `opencode debug agents` parsed the edited config
  and resolved the new descriptions, and live `opencode api get /api/agent`
  showed them; the running server picked the change up without a restart.
- Block check against native state: quotas and counts in the briefing's
  OpenCode block match `ai-models/opencode-go-limits.md` (GLM 5.3: 220 requests
  per 5 hours; GLM 5.3 Flash: 6,320; MiMo V2.6 Pro: 3,250) and briefing section
  2's cheap and premium count rows. The native config adds no count caps, which
  is correct. Speed labels (Flash and MiMo slow at 45 and 42 tokens per second,
  GLM 5.3 normal) come from the September 30 cards and were not re-measured.
- Root model: global OpenCode config pins no root model (the primary agents
  carry no model in the live readback), the documented preference stays
  `openai/gpt-6.1-sol#low` with medium or high for hard tasks (user-confirmed
  2026-09-29, above), and the session that ran this sync itself ran
  `opencode-go/glm-5.3-flash`. So the briefing block's line that the Go workers
  are "weaker than a Sol or Opus root" does not hold for the real root. The
  exact replacement text is in the 2026-10-07 entry of
  `opencode.divergences.md`; the briefing itself was not edited in this run.

## Permissions and unattended execution

Policy: `~/agents/conventions/autonomous-task-permissions.md`.
Persistent V2 permission rules apply at their configured global/project/agent
scope. Explicit unattended example:
`opencode run --standalone --auto --model '<configured-provider/model#variant>' '<task>'`.
`--auto` preapproves asks, not explicit denies. `--standalone` gives CLI-scoped
configuration overrides their own server; existing shared services may need
reload/new session for persistent changes. Preserve named-leaf allow/deny rules,
terminal-leaf dispatch denies and existing deliberate exclusions. No live tests
were added by this documentation update; saved-patch/readback limits remain in
the current orchestrator section. Do not treat this flag as a universal sandbox
or managed-policy bypass.

## Frontier Orchestrator

- Normal `task-orchestrator`: present as `openai/gpt-6.1-sol#medium` with a
  native child allowlist for the four configured worker wrappers; all other
   child IDs are denied. Model choices come from the delegation briefing.
   Native config and `opencode debug agents` confirmed the unchanged model,
   Medium variant, child allowlist and `shell:*` allow on 2026-10-01.
   V2 base permissions plus the global external-directory grant provide routine
   file/network/enabled-MCP access; environment-file asks and deliberate MCP
   exclusions remain. No fast or
  generic-agent fallback is permitted. The root must provide a leaf budget.
  An older configuration passed one nested read-only dispatch on 2026-09-25,
  but current nested execution and actual child reasoning are not verified.
  The 2026-09-29 model replacement preserves Medium reasoning and permissions;
  its roster and resolved-agent preflight passed, not a new-model live smoke;
  do not treat the current mapping as launch-ready until a fresh smoke.
- `task-orchestrator-fast`: disabled by `../roles/task-worker-tiers.md`, no
  wrapper, refuse launch. Native allowlist limits child names, but a fresh
  nested delegation check is still needed.

## One-Run Role Profiles

- Selectable maintained roles for standing dispatch: `task-explore`,
  `task-explore-high`, `task-execute`, `task-execute-high`, and
  `task-orchestrator` (normal mapping still needs a current nested smoke).
  All three fast names are disabled. No generic substitute.
- Discover exact IDs with `opencode models`; the 2026-10-01 worker shortlist is
  `opencode-go/glm-5.3-flash`, `opencode-go/mimo-v2.6-pro` and
  `opencode-go/glm-5.3`. The native model catalog lists GLM variants `low`,
  `high`, `max`, and no named MiMo Pro variants. The worker config uses no suffix,
  leaving the provider default; all four smokes recorded `variant: default`.
  The orchestrator remains `openai/gpt-6.1-sol#medium`.
  `opencode models` takes no provider
  positional argument in V2. Roster presence alone is not verification of a
  model/variant or its cost. Older `opencode models openai --verbose` and
  `opencode debug agent` commands are V1 history, not V2 instructions.
- V2 headless primary syntax: from the intended working directory, run
  `opencode run --agent <primary> --model provider/model#variant --format json
  --title <run-id> '<message>'`. There is no `--dir` or `--variant` flag.
  Standard service uses the exact non-`-fast` model ID; a separately listed
  `-fast` ID selects provider priority service when available, not an
  invented `--priority` flag. The worker reasoning levels are confirmed;
  root baseline is documented above, but fast/priority posture is not confirmed.
  `openai/gpt-6.1-sol-fast#low` is roster-listed with priority service, not a
  user-selected or live-verified profile. `--continue` or
  `--session <id>` resumes; terminate and reap the owning process to cancel.
  Capture JSON events/stderr separately, verify identity with
  `opencode api get /api/session/<session-id>` and use
  `opencode api get /api/session/<session-id>/message` for tool events;
  `opencode export` is not a V2 CLI command. Inspect checkout state. The OpenCode
  server can own concurrent sessions; independent read-only outputs must be
  unique and mutating runs require separate checkouts and process ownership.
- A direct `opencode run --agent task-explore` previously fell back to a
  primary agent because `task-explore` was `mode: subagent`. The supported
  standing path is the root's `subagent` tool with the maintained wrapper and
   its configured model. The current native `subagent` tool schema exposes a
   per-call `model` string accepting `provider/model#variant`; reasoning uses
   that suffix and priority uses an exact `-fast` model ID. Preservation of the
   maintained role and permissions under this override has not been live-tested.
   A temporary native profile with `mode: all` or direct primary
  mode has not been tested for permission and role preservation. Therefore
   **one-run explicit subagent profiles remain unverified and not launch-ready**, not silently
  implemented by CLI root flags, inherited models, or `--auto`.
- Worker subset **confirmed 2026-10-01**: use the delegation briefing's OpenCode
  rows. The exact native IDs and default variants above passed roster, resolved
  agent and read-only session checks. The root preference remains unchanged.
  The orchestrator model was statically confirmed, not run-tested in this pass.
  Priority-service posture and one-run overrides remain unverified. No inherited
  model or unverified role substitution is allowed.

## Connectors / MCP Inventory

- Global OpenCode has `parallel` (keyed bearer header, fast URL), `exa`
  (keyed `x-api-key`, only search/fetch), and `firecrawl` (keyed bearer,
  search/scrape allowed, costly tools denied). All three are **on**,
  `oauth: false`, with env substitutions and 120-second execution timeouts.
  `opencode mcp list` reported connected 2026-09-29; prior live search/fetch
  and headless scrape passed. Vendor dashboard charges remain unverified.
  This matches the global agents workspace registry's dated default-on choice.
  Native `websearch` stays off to avoid unpinned provider costs; `webfetch`
  stays available. No per-role MCP configuration is maintained.
- Global agents workspace connectors `playwright`, `chrome-devtools`, and
  `jev-browser` are not configured in global OpenCode; expected posture if
  added is configured **default-off** via `disabled: true`, not deleted.
  Previously deferred; each needs a tested version/mode before configuration.
  Playwright has managed/CDP/extension identities; Chrome DevTools has
  managed/CDP modes; Jev stock MCP uses an isolated, signed-out browser and
  another model. None inherits an existing login. No current enablement or
  signed-in smoke is authorized.
- Global agents workspace connectors `figma`, `git`, and `github` are likewise
  absent in global OpenCode and previously deferred. Figma's hosted endpoint
  needs per-OpenCode browser OAuth before a private-file test; Git's local
  connector needs no auth; GitHub's deployment endpoint and host-managed OAuth
  or token need user selection and per-OpenCode authorization. Native Git and
  `gh` CLI are available separately, not proof of these MCP servers.
- Global agents workspace browser/desktop awareness: OpenCode's `browser`
  tool is visible through Code Mode, but `browser.tabs.list()` returned
  `browser.disconnected` on 2026-09-29. No native-browser page, login identity,
  or account-only read was proved. Its tab IDs are explicit and task-owned tabs
  must be closed. OpenCode's shell can launch `agent-browser` 0.38.1 in a fresh,
  named, isolated, signed-out CLI session. This is a separate controller and
  identity, not a repair for or silent substitution of the native browser.
  Standalone scripts, hosted APIs, and desktop OS control were not configured
  as native OpenCode routes here. No plugin was configured.
  Read `~/agents/skills/browser-use/SKILL.md` and
  `~/agents/skills/browser-use/references/onboarding.md` before
  selecting a route. Awareness is not enablement.
- After the user requested child smokes, global OpenCode loaded the thin
  `browser-use`, `chatgpt-browser`, `claude-browser`, and `task-codex` skills
  successfully inside four default-explore children. Another default-explore
  child loaded `web-search` and called Parallel search on a public query.
  A later high-explore child checked the four resolved worker models/variants,
  permissions, and five skill loader pointers. These checks prove discovery,
  not website workflow completion.
- On 2026-09-29, a task-owned `agent-browser` CLI session opened the public
  OpenCode V2 docs, used the site's **Search documentation** control to find
  `Skills`, selected the result, and read back `/v2/docs/skills/`. Generic
  search was not reliable in that isolated browser: DuckDuckGo returned 418,
  Brave and Google presented bot checks, and Bing returned unrelated results.
  OpenCode's Parallel `web_search` then found the relevant V2 documentation,
  verifying the authorized public-search fallback. An earlier default-explore
  child also completed a Parallel search. The isolated browser reached
  Cloudflare human-verification challenges on `chatgpt.com` and `claude.ai`;
  neither was bypassed. No signed-in project, conversation, or export workflow
  passed. The named CLI browser session was closed and `session list` showed
  no active sessions. No Chrome profile, saved login, or browser MCP was used.
- A `task-execute-high` child loaded `task-codex` and launched one bounded
  Codex CLI 0.159.0 public search from OpenCode with read-only sandbox,
  subagents and browser/computer-use routes disabled. JSONL recorded a
  successful `web_search` and final V2 skills URL, exit 0, with no repository
  edit. The child requested `gpt-5.6-luna`/`xhigh` and default service, but
  Codex JSONL did **not** independently confirm the effective model, reasoning,
  or service tier; a transient routing error recovered. This tests the
  OpenCode-to-Codex bridge, not Codex's native adapter or account connectors.

## Drift Checks

- Compare global agents workspace `skills/`, `roles/`, `workflows/`, and
  `capabilities/connectors.md` against global OpenCode's config and live skill,
  command, agent, and MCP registries. Re-list dated decisions and tool-only
  extras from `opencode.divergences.md`. Do not inspect another tool's config.
- Check shared symlink inode, thin wrappers, command `$ARGUMENTS` passthrough,
  every enabled role's explicit model, disabled fast names, leaf denial, and
   orchestrator `shell:*` allow using `opencode debug agents`. Resolve agent
  permissions rather than assuming comments enforce them.
- Check `/api/command` has the twelve named commands and `/api/skill` resolves
  each to the canonical loader, including the browser skills. Verify the
  `sync-tool-adapter` command is registered; a client autocomplete smoke is
  separate. `opencode mcp list` verifies connection only; run a bounded tool
  invocation when connection behavior must be established again.
- Recheck current orchestrator nesting, mutating execute permission behavior,
  remaining preference questions and one-run override path before claiming
  full role support. Reconnect the desktop browser for a native page smoke;
  select an authorized signed-in identity before testing the two website
  procedures. Browser tool discovery or a public CLI page never proves a
  signed-in account. Treat generic browser search challenges as a reason to
  use the verified public-search connector, not to bypass a challenge.

## Web reference, 2026-10-01

By default use this harness's built-in search and fetch. [Capabilities/web](../capabilities/web/README.md) owns tool strengths, both ladders, costs and compatibility. Use web-search only on explicit user request or when a task packet names it. web-search-advanced requires an explicit user request by name. Both canonical skills set disable-model-invocation: true and metadata.opencode/autoinvoke: false. Native discovery metadata must be aligned in this tool's own session. This shared-doc change did not inspect, edit or verify native loaders. Keep the native wiring and approved fallbacks documented above.
