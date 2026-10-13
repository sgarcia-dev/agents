---
created_at: 2026-09-15
updated_at: 2026-10-07
model: gpt-6.1-sol
doc_type: adapter
purpose: Map the canonical Agents workspace to the current Codex harness after the post-employment cleanup.
related:
  - path: ~/agents/adapters/adapter-contract.md
    why: Owns the portable reconciliation rules.
  - path: ~/agents/adapters/codex.divergences.md
    why: Records Codex-only choices and limits to recheck.
  - path: ~/agents/roles/task-worker-tiers.md
    why: Owns worker availability and boundaries.
  - path: ~/agents/capabilities/connectors.md
    why: Lists the portable MCP connectors considered for Codex.
---

# Codex Adapter

The global agents workspace at `~/agents` is canonical. Global Codex
uses it through thin instruction and skill loaders. Codex-native settings and
runtime services remain replaceable implementation details.

## Native Surfaces

- **Global agents workspace instructions:** `~/.agents/AGENTS.md`
  symlinks to `~/agents/AGENTS.md`.
- **Global agents workspace skill loaders:** `~/.agents/skills/`
  contains nineteen thin canonical loaders, including `web-search-advanced`,
  `task-hermes`, and `artificial-analysis-model-data`.
  `task-codex` is discoverable here but is a procedure for non-Codex callers;
  a Codex session uses native tools instead of invoking itself through the CLI.
- **Global Codex configuration:** `~/.codex/config.toml` currently
  saves `gpt-6.1-sol`, `medium` reasoning, and `default` service, read October 7.
  This differs from the historical September 30 low default. This bounded run
  preserved the saved settings; existing sessions may keep their loaded profile.
- **Global Codex role dispatch:** five named custom agents under
  `~/.codex/agents/` pin their model and effort and load canonical
  role files. Native child model and effort telemetry is unavailable.
- **Global Codex runtime inventory:** `codex mcp list` and `codex plugin list`.
- **Codex current project (`~`):** no separate project `.codex/`
  configuration or project `AGENTS.md` is present. The `.codex/` directory is
  the user-level Codex home described above.

## Source Mapping

| Global agents workspace concept | Global Codex implementation |
|---|---|
| Instructions | The `.agents/AGENTS.md` symlink loads canonical root instructions. |
| Skills | Thin files in `.agents/skills/` load every canonical skill applicable inside Codex; `task-codex` is for other harnesses. |
| Worker roles | Named custom agents load the canonical base role, high overlay where applicable, and `task-worker-tiers.md`. |
| Worker model choice | Set by the [delegation briefing](../ai-models/delegation-briefing.md) (Codex section). Agent files pin `gpt-6-luna`/`xhigh` (explore), `gpt-6.1-sol`/`low` (execute) and `gpt-6.1-sol`/`medium` (both high workers), synced and smoke-tested 2026-10-01. |
| Frontier orchestrator | Named `task-orchestrator` agent pins `gpt-6.1-sol`/`high` (2026-10-01, from the briefing) and loads the canonical orchestrator role. One nested `task-explore` dispatch completed September 29; effective child profile and a native child allowlist remain unverified. |
| Commands | `$skill-name` discovery; no separate custom command registry. |
| MCP connectors | Parallel, Exa, and Firecrawl are configured and enabled in global Codex with environment-sourced keys; six declined connectors remain absent. |

## Skills

Global Codex exposes these current global agents workspace skills through thin
loaders: `browser-use`, `chatgpt-browser`, `claude-browser`,
`memory-reconcile`, `model-bakeoff`, `plan-create`, `plan-execute`,
`plan-reconcile`, `research`, `research-deep`, `role-dispatch`,
`sync-tool-adapter`, `task-claude`, `task-codex`, `task-opencode`, and
`web-search`, `web-search-advanced`, `task-hermes`, and
`artificial-analysis-model-data`. The `task-codex` loader is shared cross-tool
discovery; the
canonical skill restricts it to non-Codex callers.
In a new read-only CLI session on September 28, Codex reported both
`task-claude` and `task-opencode` as discoverable by name. The smoke did not
invoke either skill.

On September 30 a fresh read-only Codex CLI session discovered
`web-search-advanced` and `task-hermes` and quoted the advanced skill's explicit
invocation restriction. Its loader retains `disable-model-invocation: true`.
Advanced search uses Codex native search and page open by default; named
providers and helpers are opt-in. Parallel, Exa and Firecrawl are available
when named. A full-budget experimental `codex` Luna/xhigh search helper is not
mapped: the fixed Luna micro role permits only tiny packets, while maintained
high roles fix Sol/low and cannot accept a Luna override. Do not stretch the micro
role or substitute a generic agent. Supporting that experiment needs an explicit
maintained-role variant and verification. Sonnet and Go extras route through their
canonical task skills only when named; neither was executed in this sync.
The shared `web-search` loader's discovery
text now reflects the native-only quick-lookup default. `task-hermes` discovery
neither enables Hermes nor starts a service or sends messages.

No deprecated user-managed skill loader remains in global Codex. Codex system and
plugin-provided skills are runtime-owned and stay local by the September 15
decision; they are not copies of global agents workspace procedures. Current
system skill names are `imagegen`, `openai-docs`, `skill-creator`, and
`skill-installer`. Current plugin skill groups are Documents, Google Drive
(Docs, Drive, comments, Sheets, Slides), PDF, Plugin Management,
Presentations, Spreadsheets (including Excel live control), Template Creator,
Visualize, Pages (write, maintain, organize, schedules), and Work Pets
(create, inspect, update). These names are present in
this session's skill catalog; the next sync must re-inventory them.

## Roles and Worker Tiers

The global agents workspace enables four terminal roles. Global Codex now has a
named custom agent for each, with a pinned model and effort and a thin canonical
loader. Model choices come from the Codex rows in
`~/agents/ai-models/delegation-briefing.md`. The table below records
the native wiring checked October 1, not a separate model policy. If the exact
model or effort is unavailable, refuse launch.
Before dispatch, read the Codex part of section 3 of the delegation briefing.
That block owns capability, packet sizing, escalation and suggested counts;
the tier names alone do not determine them.

| Role | Model and effort | Availability | Native file |
|---|---|---|---|
| `task-explore` | `gpt-6-luna` / `xhigh` | Configured | `~/.codex/agents/task-explore.toml` |
| `task-execute` | `gpt-6.1-sol` / `low` | Live read checked October 1 | `~/.codex/agents/task-execute.toml` |
| `task-explore-fast` | none | Disabled | Refuse launch. |
| `task-explore-high` | `gpt-6.1-sol` / `medium` | Live read checked October 1 | `~/.codex/agents/task-explore-high.toml` |
| `task-execute-fast` | none | Disabled | Refuse launch. |
| `task-execute-high` | `gpt-6.1-sol` / `medium` | Live read checked October 1 | `~/.codex/agents/task-execute-high.toml` |

Every enabled child remains terminal and may not delegate. `task-explore` and
`task-explore-high` retain the source-read-only boundary, with the canonical
exclusive new-Markdown-report exception. `task-execute` and `task-execute-high`
write only within their assigned packet scope. Codex cannot enforce the explore
create-only report boundary at the runtime permission layer; the root assigns an
exclusive output directory and verifies changes.
All four worker files set `approval_policy = "never"` as their no-prompt default.
Codex can reapply a parent turn's live permission override when spawning a child.
All four files now explicitly set `sandbox_mode = "danger-full-access"`. Explore
source reads and new reports, execute packet scope, and terminal non-recursion
remain prompt-enforced through unchanged canonical loaders and root verification.
This is full technical access, not filesystem confinement.

## Permissions and unattended execution

Policy: `~/agents/conventions/autonomous-task-permissions.md`.
Saved root/maintained-role controls use `approval_policy = "never"` and
`sandbox_mode = "danger-full-access"`; start a new session for saved changes.
Explicit all-access example: `codex exec --yolo -C <task-checkout> '<task>'`.
`--yolo` aliases `--dangerously-bypass-approvals-and-sandbox`; this is not task
or account authority. Keep the packet's named-worker/depth rules: numeric depth
is supported, exact child names remain behavioral. Permission-only updates do
not authorize model/connector changes or repeat live tests. See existing role
sections for per-role saved settings and actual verification limits.

## Frontier Orchestrator

**Access follow-up 2026-09-30: configured, static-only, not runtime-tested.**
The normal role explicitly saves `approval_policy = "never"` and
`sandbox_mode = "danger-full-access"`; root `[agents].max_depth = 2` permits
root -> orchestrator -> one terminal-leaf layer. Broad shell access covers
Node.js (`node`), installed interpreters/runners, scripts and absolute paths;
existing enabled MCP settings are preserved. Numeric depth is a native ceiling,
not a child-name allowlist. Exact four-leaf routing and terminal behavior remain
canonical-instruction-enforced, not technically guaranteed by Codex. Models and
other settings were retained in that September 30 permission pass. Two short
supervisors timed out, but the final saved-key readback and receipt confirm the edits; no clean final CLI exit or
live orchestrator test is claimed for that permission pass.

Global Codex now has a named `task-orchestrator` custom agent at
`~/.codex/agents/task-orchestrator.toml`, wired to the briefing's
Codex orchestrator choice, checked October 1 as `gpt-6.1-sol` / `high`.
Its October 1 read-only smoke passed, with model and effort visible in the
child session records. It launched no leaves in that smoke.
`task-orchestrator-fast` remains disabled. Codex has no native child-role allowlist, so the canonical orchestrator contract restricts routing to the four
enabled named default/high leaves; disabled fast roles remain unavailable.
A September 29 native smoke launched this named orchestrator, which launched
exactly one named `task-explore` child. The child completed a read-only heading
probe and returned `# Task Worker Tiers`; the task path and one-layer depth were
observable. Actual child role, model, effort, and service were not independently
observable. The native launcher still has no child-role allowlist, so the
canonical role contract supplies that restriction without native enforcement.

## One-Run Role Profiles

- **Global Codex selectable maintained roles:** `task-explore`, `task-execute`,
  `task-explore-high`, `task-execute-high`, and `task-orchestrator`. Fast roles
  remain disabled. In this September 30 native tool schema, each maintained
  role fixes model and reasoning; the schema explicitly says those settings
  cannot be changed. Generic roles accept partial-fork overrides but are not
  substitutes for maintained roles. Earlier claims of maintained-role overrides
  are superseded by this observed interface.
- **Global Codex model choices:** use the Codex rows and model cards in
  `~/agents/ai-models/delegation-briefing.md`. The October 1 worker
  and orchestrator decisions are applied to their native files. Each description
  now carries the model's cost, trust and speed note. Root model, effort and
  service settings were not changed in this pass. Fast roles remain disabled.
- **Global Codex model discovery:** `codex debug models` refreshes and prints
  the CLI catalog. CLI 0.159.0 accepted this read-only discovery on October 1.
  It lists `gpt-6.1-sol` with `low`, `medium` and `high`, and `gpt-6-luna` with
  `xhigh`. All requested pairs are supported; no substitution was needed.
- **Global Codex maintained-role launch:**
  `spawn_agent({agent_type: "task-explore", fork_turns: "none",
  message: "<bounded packet>"})` selects its fixed profile. `interrupt_agent`
  cancels; `list_agents` and the handoff identify completion. Four active agents,
  including root, is the tighter runtime limit. Preserve the selected wrapper,
  permissions and terminal-worker boundary. The dispatcher has no service field.
  Child model and effort can be checked in the local session records; the
  dispatcher itself does not expose them or effective service telemetry.
- **Global Codex explicit CLI root controls:**
  `codex --ask-for-approval never exec --strict-config --ephemeral --disable
  multi_agent --model <id> -c model_reasoning_effort=<level> -c
  service_tier=default -s read-only -C <dir> --json --output-last-message <path>
  <prompt>`. `service_tier=fast` requests priority on supported models; it is
  not automatically selected. `codex exec resume <id>` continues a session.
  Process interruption cancels; capture JSONL and stderr and check tool events
  and final output. CLI 0.159.0 help confirms model, profile, sandbox, directory,
  structured-output and capture flags. A CLI root is not a maintained child role.
- **Global Codex full one-run role triple:** unsupported. Fixed maintained-role
  models/efforts and absent child service control prevent the requested
  model/reasoning/service triple. Temporary
  native role variants would need a separate design and user decision; none was
  created. Never fall back to a generic or inherited-profile child or widen its
  permissions.
- **Global Codex October 1 role smoke:** a fresh CLI supervisor
  `01a0f74a-0947-7881-aefa-bae032baa704` launched the four changed roles
  sequentially. Each returned `# Agents Workspace` from a read-only packet.
  The orchestrator read directly and launched no leaves. Child session IDs:
  `task-execute`: `01a0f74a-642f-7842-9578-9a83e02211ad`;
  `task-explore-high`: `01a0f74a-a9d8-7373-b754-b4601676217f`;
  `task-execute-high`: `01a0f74a-e6a4-7a52-a686-eaf757807e04`;
  `task-orchestrator`: `01a0f74b-1d5c-75c3-a6ee-21d5d92b48b7`.
  Read-only queries of `~/.codex/state_5.sqlite` confirmed each
  child role, parent, model and effort. Each child's session JSONL
  `turn_context` independently recorded the requested model and effort.
  These are runtime session records, not provider-side execution receipts.
  Effective service and nested delegation were not tested. All five TOML files
  parsed; keys outside description, model and effort were unchanged.
- **Global Codex verification:** September 30 strict-config, ephemeral,
  read-only root requested `gpt-6.1-sol`/`low` and confirmed both new skills.
  JSON events establish completion, not the effective runtime profile. Saved
  worker and orchestrator TOML pairs are checked separately. The September 29
  normal-orchestrator smoke completed one nested named explore read; it predates
  the September 30 orchestrator model update. The user authorized a September 30
  fresh CLI nested diagnostic. It returned
  accepted `task-orchestrator` and `task-explore`, completion, and the expected
  heading. JSONL exposed empty receiver lists in wait events and no identifiable
  child-launch records. Nested execution is self-reported, not independently
  verified from that capture. No child account inheritance claim is made.
- **Global Codex cross-harness CLI bridge:** `task-codex` is for other harnesses
  and starts a root process. The caller must follow its capture, tool and
  authorization rules; Codex does not self-dispatch through this bridge.

## MCP Connectors and Plugins

The global agents workspace registry has nine curated MCP connectors. Their
global Codex posture was rechecked on September 30:

| Registry connector | Global Codex posture and auth |
|---|---|
| `parallel` | Enabled, keyed through `PARALLEL_API_KEY`; bearer header, `?mode=fast`, 120-second timeout, no approval prompt. Fresh full-access CLI search and fetch succeeded September 29. |
| `exa` | Enabled, keyed through `EXA_API_KEY` in `x-api-key`; instant URL limits tools to search and fetch, 120-second timeout, no approval prompt. Fresh full-access CLI search and fetch succeeded September 29. |
| `firecrawl` | Enabled, keyed through `FIRECRAWL_API_KEY`; only search, scrape, map, and parse exposed, 120-second timeout, no approval prompt. Fresh full-access CLI calls to all four tools succeeded September 29, using only public or synthetic data. |
| `playwright` | Absent by user decline dated September 15; signed-in attachment would need a selected profile and auth. |
| `chrome-devtools` | Absent by user decline dated September 15; CDP attachment would need an explicit browser identity. |
| `jev-browser` | Absent by user decline dated September 29. Its runbook would require a pinned vetted package, private nested-model credential, and step budget if revisited. |
| `figma` | Absent by user decline dated September 15; account authorization required if added. |
| `git` | Absent by user decline dated September 15; no connector auth. |
| `github` | Absent by user decline dated September 15; hosted account authorization required if added. |

The three web servers are configured in `~/.codex/config.toml`
with environment variable names only. Fresh full-access CLI 0.159.0 sessions
completed Parallel and Exa search/fetch plus Firecrawl search/scrape/map/parse
without prompts. Codex native web search/open also passed. Firecrawl parse used
a deleted synthetic temporary file; no user data was uploaded. `codex mcp list`
alone establishes enabled config, not live connection. September 30 direct calls
in the current desktop session passed Parallel search,
Exa search, and Firecrawl scrape without prompts. This establishes current tool
availability, not a fresh test of every fetch/map/parse operation. No Codex current
project connector config exists. Detailed proof is in the
September 29 smoke audit (private, not published).

Browser and desktop awareness routes are distinct from this curated MCP list.
Their current Codex inventory is:

| Route | Identity, permission, and verification |
|---|---|
| Native web search and page open | Public search and page open passed September 29. No account identity or browser login is implied. |
| Bundled `cua_repl` in-app browser | Config lists `iab`, but live `createBrowserTab` returned `Browser is not available: iab`; no task tab was created. |
| Bundled `cua_repl` Chrome extension | One controller exposed a personal profile name with pre-existing private tabs. It was not used or equated with the dedicated CDP identity. |
| Desktop/accessibility driver | Neutral Calculator discovery worked, but a click was blocked by unfinished Computer Use onboarding in cmux. Calculator was closed; action control is unverified. |
| Standalone `agent-browser` CLI | Version 0.38.1 passed two concurrent isolated public sessions with storage separation and zero remaining sessions. Its `--cdp 9222 --pin-tab` mode attached to the previously selected dedicated Chrome and passed a signed-in Google account-only check. The exact task tab and controller session closed; Chrome stayed running on loopback. |
| Hosted browser API or service | Awareness only; no configured Codex provider, selected profile, or live proof. No hosted session was created. |

The shared route selector is `~/agents/skills/browser-use/SKILL.md`
and its `references/onboarding.md` defines the proof tier. For Codex's verified
CLI fallback, use a unique `agent-browser --namespace <job> --session <worker>`
on every call; for the dedicated signed-in identity, add `--cdp 9222 --pin-tab`,
check account-only state, and close the exact owned tab plus named controller
session. Do not attach Codex's extension controller to an unselected profile.
No optional browser MCP or hosted service was enabled. Native IAB and desktop
action need their own runtime/onboarding gates resolved before a fresh smoke.

Global Codex root also has ChatGPT-account-linked Gmail and Google Drive
application connectors. They are available to the root even though `codex mcp
list` does not show them as configured MCP servers. On September 22, root
authorization health checks succeeded with Gmail `list_labels` filtered to
`INBOX` and Google Drive `get_profile`; no email or file content was read. These
connectors were not callable in either the native child or the task-explore-style
child. Google research that needs those connectors therefore cannot be delegated
to those tested native children. On September 28, a separate read-only `codex
exec` CLI root smoke successfully called the same limited Gmail and Drive tools.
It also ran live web search and returned Reddit results. The CLI smoke did not
verify a scraping advantage or connector inheritance by subagents.
In the September 30 root session, Gmail `list_labels` filtered to `INBOX` and
Google Drive `get_profile` both succeeded again. No message or file content was
read, and child access was not retested.

Global Codex also has internal runtime MCP services: `node_repl` and `cua_repl`
are enabled, while `codex_app`, `computer-use`, and the new `code-review` MCP are
disabled. They support the
Codex product itself, are not entries from the global agents workspace registry,
and remain local.

Global Codex plugins remain local under the September 15 decision. On September
30 the CLI confirmed installed/enabled `browser`, `chrome`, `codex-app-tools`,
`computer-use`, `code-review`, `documents`, `pdf`, `spreadsheets`, `presentations`,
`template-creator`, `unified-computer-use`, `visualize`, `google-calendar`, and
`slack`. Remote marketplace inventory failed both sandboxed and approved retries;
that is an inventory gap, not evidence that remote plugins were removed. Current
session tools additionally expose Gmail, Google Drive, Contacts, Pages, Plugin
Management, Work Pets, and Skyscanner. Runtime system/plugin skills remain local;
no upstream promotion or new connector enablement occurred.

Global Codex awareness routes retain September 29 evidence only: IAB unavailable,
Chrome extension identity unselected, desktop action blocked by onboarding,
standalone isolated/CDP browser tested, and hosted browser unconfigured. No browser
was attached or account browser operated during the September 30 sync. Artificial
Analysis has a shared skill loader; its API was not called. Hermes has a shared
skill loader only; no Hermes CLI/API/MCP/A2A route was launched or configured.

## Commands and Permissions

Codex has no custom command wrappers. The global agents workspace skill loaders
are the supported entrypoints. `task-codex` is discoverable through the shared
loader directory but applies only to non-Codex callers.

Global Codex marks `~` as trusted. The owner-authorized September 30
permission migration sets persistent `approval_policy = "never"` and
`sandbox_mode = "danger-full-access"` in `~/.codex/config.toml`
and all four enabled worker files. The policy is
`~/agents/conventions/autonomous-task-permissions.md`. Root model,
effort, service, enabled connectors and intentional tool exclusions are preserved.
Full shell access includes task-selected paths and public HTTP; it does not
authorize cross-provider delegation or account side effects. There are no
role-specific MCP grants or former-company knowledge-broker entries.
The user-level rule file contains prior explicit allowances, with no routine ask
or deny rule found; it remains unchanged. No hook was added or trust bypassed. The browser sub-config's existing no-ask modes and CDP permission are
local Codex settings. They were inventoried, not changed or treated as proof of
an authenticated browser identity.

Because the root Gmail and Google Drive connectors include mutation tools, any
root connector research must use a read-only allowlist and the narrowest
authorized call. It cannot be moved to a child under the tested runtime.

## Recheck Points

- Global Codex worker and orchestrator choices come from the delegation briefing.
  Native files were synced October 1; root settings were unchanged.
- Global Codex has nineteen thin canonical skill loaders. Recheck explicit-only
  advanced-search discovery in fresh sessions, and retain task-codex's non-Codex
  boundary and task-hermes's explicit delegation boundary.
- Global Codex child model and effort were observable in October 1 session
  records. Effective service and provider-side execution remain unverified.
- Global Codex arbitrary maintained-role model/effort overrides and child service
  selection are unsupported in the current interface. Decide whether temporary
  maintained role variants are worth supporting; do not claim generic agents suffice.
- Global Codex native orchestrator lacks a child-name allowlist. Canonical prompt
  restrictions do not constitute native enforcement.
- Global Codex web MCPs passed direct calls September 30. Re-surface September 15
  connector declines and September 29 Jev decline as dated reminders.
- Global Codex root Gmail and Drive health passed September 30. Recheck child
  access before any account-backed delegation; no content was accessed in this sync.
- Global Codex remote marketplace refresh failed; installed plugin accounting may
  be incomplete. Browser IAB and desktop onboarding still need fresh route tests
  after their underlying gates are resolved.
- Global Codex's older `artifacts/usage-guide/codex.md` has outdated lifecycle and
  role names. Treat it as historical until a dedicated refresh replaces its claims;
  the current adapter mapping and canonical skills remain the authority.

## Web reference, 2026-10-01

By default use this harness's built-in search and fetch. [Capabilities/web](../capabilities/web/README.md) owns tool strengths, both ladders, costs and compatibility. Use web-search only on explicit user request or when a task packet names it. web-search-advanced requires an explicit user request by name. Both canonical skills set disable-model-invocation: true and metadata.opencode/autoinvoke: false. Native discovery metadata must be aligned in this tool's own session. This shared-doc change did not inspect, edit or verify native loaders. Keep the native wiring and approved fallbacks documented above.

## Worker and orchestrator check, 2026-10-07

Global Codex: this apply-now run covered only workflow steps 5 and 6. All five
native model/effort pairs match the Codex briefing table. All five role bodies
still load their canonical role files and `task-worker-tiers.md`. Their old
descriptions lacked the explicit Codex section 3 pointer; each now carries that
pointer and one short model, effort, cost and guessing line, preceded by the
original role sentence. No other native
keys changed. Both fast worker cells and the fast orchestrator remain disabled,
with no native files. The normal orchestrator remains present; no new nesting
verification was performed.

Global Codex: root config lines 3 and 4 save GPT-6.1 Sol medium, the exact high
worker pair, so the briefing's near-root comparison holds but understates parity.
The current native dispatcher permits four active agents including root, leaving
at most three direct workers, or two leaves while root and orchestrator are both
active. This limits the briefing's suggested pool counts; it is not a new saved
cap. Root config line 9 still sets maximum depth two. Quota, subscription cost,
throughput and comparative speed were not measured.

Global Codex: all five files parsed with Python `tomllib`; parsed comparisons
confirmed only descriptions changed. `codex doctor --json` reported
`config.load: ok`, summary `config loaded`. `codex debug prompt-input` exited
successfully with JSON but omitted dispatch descriptions; `--strict-config`
is unsupported for that debug command. Edited dispatch descriptions, effective
child profiles and nesting were not live-tested. No git or delegation was run.

Global agents workspace: the Sol medium and Sol high section 5 cards lack
"Tell the worker" lines. The briefing and roles were left untouched.
