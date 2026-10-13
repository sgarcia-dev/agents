---
created_at: 2026-09-15
updated_at: 2026-10-07
model: gpt-6.1-sol
doc_type: adapter
purpose: Record Codex-specific choices and limitations that must be revisited during each Codex-owned reconciliation.
related:
  - path: ./codex.md
    why: Defines the current Codex mapping.
  - path: ../capabilities/connectors.md
    why: Defines the portable MCP registry considered here.
---

# Codex-Specific Decisions

## Decisions confirmed 2026-09-15

- **Global agents workspace registry `playwright`:** not configured in global
  Codex. The user declined to add it for now.
- **Global agents workspace registry `chrome-devtools`:** not configured in
  global Codex. The user declined to add it for now.
- **Global agents workspace registry `figma`:** not configured in global Codex.
  The user declined to add it for now.
- **Global agents workspace registry `git`:** not configured in global Codex.
  The user declined to add it for now.
- **Global agents workspace registry `github`:** not configured in global Codex.
  The user declined to add it for now.
- **Global Codex internal MCP services:** `node_repl`, `cua_repl`, `codex_app`,
  and `computer-use` stay local to Codex. They are not candidates for promotion
  into the global agents workspace.
- **Global Codex plugins:** installed plugins stay local to Codex and are not
  candidates for promotion into the global agents workspace.
- **Global Codex worker profiles:** the four maintained worker roles are
  configured as named agents. Fast names remain disabled. The multi-agent
  launcher has no service-class control, so a worker launch must not claim a
  service setting it cannot observe.
- **Global Codex role permissions:** the runtime cannot enforce the portable
  create-only output-directory boundary for `task-explore`; the root enforces it
  through packet scope and verification.
- **Legacy integration pattern:** no legacy endpoint, connector, or role-level
  MCP record is retained.

## Observed 2026-09-22

- **Global Codex root profile:** `gpt-5.6-terra` with `high` reasoning and the
  `fast` service tier. This is an observed root configuration, not a replacement
  for the dated worker-model decision above.
- **Global Codex runtime MCP services:** `node_repl` and `cua_repl` are enabled;
  `codex_app` and `computer-use` are disabled. They remain local.
- **Global Codex root Gmail and Google Drive application connectors:** both were
  available to the root through the ChatGPT account even though `codex mcp list`
  did not list them as configured MCP servers. Read-only authorization health
  checks succeeded with Gmail `list_labels` filtered to `INBOX` and Google Drive
  `get_profile`. No email or file content was accessed. Any root research using
  them must keep an explicit read-only allowlist because the connectors also
  expose mutation tools.
- **Global Codex child connector access:** a native child and a task-explore-style
  child each lacked callable Gmail and Google Drive tools.
  Connector-backed Google research cannot be delegated under the tested runtime.
- **Global Codex child form:** `task-explore` is a prompt and tool-policy role,
  not a distinct native Codex child type. The canonical maintained-worker policy
  still requires explicit, non-inheriting model and reasoning requests.
- **Global Codex model overrides:** native child-spawn requests accepted explicit
  model and reasoning parameters. The root ran as Terra/high and both tested
  child forms requested Sol/medium. The runtime does not expose actual child
  model or reasoning, so the override is accepted-but-unverified, not proven.

## Model and tier decision confirmed 2026-09-23

- **Global Codex root:** persistent `gpt-6-sol`/`low` with `default` service;
  raise to `medium` for harder work and `high` only for unusually difficult or
  high-consequence tasks. The config change may not alter ongoing sessions.
- **Global Codex micro workers:** `task-explore` and `task-execute` requested
  `gpt-6-luna`/`xhigh` on September 23, only for extremely tiny independent packets with a few
  specified files or steps and quick parallel swarms.
- **Global Codex high workers:** `task-explore-high` and `task-execute-high`
  request `gpt-6-sol`/`low` for any real bounded moderately complex or
  multi-step delegated work. High changes reasoning capacity, not permissions.
- **Global Codex exact-model policy:** roster entries and requested effort values
  were checked in the September 23 Codex cache. A default CLI smoke and an
  explicit Luna/xhigh CLI smoke both completed. Their JSON output did not
  expose actual model or effort. Refuse child launch if the exact pair is
  unavailable; never inherit or substitute. Actual child model and effort
  telemetry is unavailable, so child resolution remains unverified.

## Earlier model and role update confirmed 2026-09-25

- **Global Codex root:** persistent config already set `gpt-6-sol`/`low` with
  `default` service. New sessions should use this default unless explicitly
  overridden.
- **Global Codex micro workers:** `task-explore` and `task-execute` initially pinned
  `gpt-6-luna`/`max` in named custom-agent files.
- **Global Codex high workers:** `task-explore-high` and `task-execute-high`
  initially pinned `gpt-6-sol`/`low` in named custom-agent files.
- **Global Codex normal orchestrator:** a named custom agent pins
  `gpt-6-sol`/`low`. Codex has no native child-role allowlist; the canonical
  role contract supplies the restriction. A CLI smoke produced no reliable
  nested spawn trace, so operational delegation remains unverified.
- **Global Codex fast roles:** both fast workers and the fast orchestrator remain
  disabled by the global agents workspace policy.

## Worker profile update confirmed 2026-09-25

- **Global Codex micro workers:** `task-explore` and `task-execute` now pin exact
  `gpt-5.6-luna`/`high` in their named agent files.
- **Global Codex high workers:** `task-explore-high` and `task-execute-high` now
  pin exact `gpt-6-luna`/`max`.
- **Global Codex approval policy:** all four named worker files set
  `approval_policy = "never"` as their no-prompt default. Codex can reapply a
  parent turn's live permission override when spawning a child. Both explore
  files retain the native `read-only` sandbox; the execute files inherit the
  active sandbox. Canonical role loaders are unchanged.
- **Global Codex verification limit:** the model cache lists both exact model
  IDs and effort levels. Bounded September 25 root CLI smokes with
  `--strict-config --ephemeral` returned `OK` for both requested pairs. These
  smokes did not select a named worker, and Codex does not expose actual child
  model or effort telemetry, so a named child's effective pair remains unverified.

## Targeted default explore update confirmed 2026-09-25

- **Global Codex default `task-explore`:** now pins exact `gpt-6-luna`/`xhigh`.
  This supersedes only its pairing in the earlier worker profile update.
  Default `task-execute` remains `gpt-5.6-luna`/`high`; both high workers remain
  `gpt-6-luna`/`max`.
- **Global Codex role permissions:** default `task-explore` still sets
  `approval_policy = "never"`, `sandbox_mode = "read-only"`, and the same
  canonical role loader.
- **Global Codex verification limit:** the model cache lists the exact model and
  `xhigh` effort. A strict-config, ephemeral, read-only root CLI smoke returned
  `OK` for the pair. It did not select the named worker or expose its effective
  model and effort.

## Codex CLI bridge and profile update confirmed 2026-09-28

- **Global Codex root profile:** the user's low-to-medium Sol range retains
  the earlier confirmed `gpt-6-sol`/`low` default with `default` service. The
  native file had `high` on audit and was returned to `low`. Existing live
  sessions can retain their starting profile.
- **Global Codex high workers:** both `gpt-6-luna` high role files now request
  `xhigh`, within the user's high-to-extra-high Luna range. Native child
  telemetry is still unavailable, so these are configured, not live-proven
  effective settings.
- **Global Codex skill loaders:** `task-claude` and `task-opencode` were added as
  thin loaders. A new read-only CLI session discovered both names without
  invoking them. The new global agents workspace `task-codex` skill remains a
  non-Codex caller procedure and has no global Codex self-dispatch loader.
- **Global Codex account connections in a CLI root:** a read-only `codex exec`
  smoke successfully called Gmail `list_labels` limited to `INBOX` and Google
  Drive `get_profile`; it did not read messages or files. The same run used live
  web search and returned Reddit links. It did not test page scraping quality
  or native-child connector inheritance.
- **Global Codex external integrations:** the five curated MCP connectors remain
  absent by the September 15 decisions. Internal MCP services and installed
  Codex plugins remain local under that same decision; this run did not add or
  enable a connector.
- **Cross-harness Codex bridge:** the global agents workspace now lists
  `codex-cli` as a non-MCP CLI bridge. Another harness must map `task-codex`
  in its own runtime before claiming native skill availability. This Codex
  reconciliation did not inspect or edit another harness's native config.

## Changes observed 2026-09-29

- **Global Codex web MCPs, user decision 2026-09-29:** `parallel`, `exa`, and
  `firecrawl` are expected on in every harness without approval prompts. This
  Codex run configured them keyed through environment variable names. A fresh
  read-only CLI session called Parallel search, Exa search, Firecrawl search,
  and Firecrawl scrape without prompts. The already running desktop session
  has not reloaded the configuration. Firecrawl's allowlist hides crawl, agent,
  interact, and monitor tools. A separate full-access headless run called
  Parallel search and Firecrawl scrape without prompts.
- **Global Codex root profile:** saved `gpt-6-sol` reasoning had returned to
  `high` when audited September 29. It was restored to the user-confirmed
  September 23 and 28 `low` default with `default` service. This changes only
  new sessions.
- **Global Codex new shared skill loaders:** `browser-use`, `chatgpt-browser`,
  `claude-browser`, and `web-search` now appear alongside the prior eleven.
  `web-search` was missing and was added in this run. `task-codex` is also
  discoverable from the shared loader directory; its canonical procedure is
  for non-Codex callers, so Codex does not invoke it as self-dispatch.
- **Global Codex Jev Browser connector, user decision 2026-09-29:** declined
  for now. Its stock MCP would need a vetted pinned package, private
  nested-model credential, and step budget before a disabled entry is
  meaningful. No software or credential was installed. Re-surface this as a
  dated reminder, not a fresh action item.
- **Global Codex one-run role profile:** exact model and reasoning overrides
  can be requested with named `spawn_agent` calls, but the native launcher has
  no service-tier field and no effective child model/effort telemetry. The
  current favorite subset, default efforts, fast posture, and selected read-only
  smokes need a fresh user decision. A CLI root can set model, reasoning, and
  service, but cannot select a maintained child role. Do not treat that as a
  fully supported role-profile path.
- **Global Codex normal orchestrator:** September 29 native run selected the
  named `task-orchestrator` and completed a single nested named
  `task-explore` heading read. One-layer dispatch is observed. Codex exposes
  neither effective child profile telemetry nor a native child-role allowlist;
  the canonical role contract remains the only name restriction.
- **Global Codex local runtime extras:** the September 15 keep-local decision
  still covers internal MCP services and installed plugins. The September 29
  installed-plugin inventory adds Gmail, Google Drive, Google Contacts, Sites,
  OpenAI Templates, Plugin Management, Work Pets, and one opaque app entry;
  these remain local and are not promoted. Slack is present in config but its
  live installation was not confirmed by `codex plugin list` in this run.
- **Global Codex root account connectors:** September 29 read-only health
  checks succeeded again for Gmail `list_labels` filtered to `INBOX` and
  Google Drive `get_profile`. No message or file content was read. Child
  non-inheritance was not retested.
- **Global Codex browser-route smoke, September 29:** fresh Codex CLI sessions
  passed Parallel and Exa search/fetch and all four allowed Firecrawl tools
  without prompts. The Codex in-app browser returned unavailable despite an
  `iab` backend config value. Its only listed extension controller pointed at
  the owner's personal profile and was left untouched. A neutral desktop app could be
  discovered, but Computer Use onboarding blocked its first UI action. The
  installed `agent-browser` CLI passed isolated public sessions and a pinned
  account-only tab through the previously selected dedicated loopback CDP
  Chrome, with exact tab/session cleanup. Hosted browser remains unconfigured
  for Codex. These are route limits, not decisions to enable declined browser
  MCPs or promote a Codex plugin upstream.

## Root baseline and effort choice confirmed 2026-09-29

- **Global Codex root model:** GPT 6.1 Sol, exact native ID `gpt-6.1-sol`, is
  the user-confirmed baseline with `low` reasoning. Native config already
  records this pair with `default` service; this update changed documentation.
- **Global Codex user-selected effort:** `medium` and `high` are expected user
  choices for a task, a session, or a saved default depending on the work.
  Preserve the user's selected effort during reconciliation. Do not automatically
  restore `low`. This supersedes earlier low-restoration guidance and any
  restriction of `high` to exceptional tasks.
- **Global Codex verification:** saved model and effort were read directly.
  `gpt-6.1-sol` was absent from the inspected model cache; no new live smoke
  was requested or run. Worker and orchestrator mappings remain unchanged.

## Worker models confirmed 2026-09-29

- **Global Codex default workers:** `task-explore` and `task-execute` both pin
  `gpt-6-luna` with `xhigh` reasoning.
- **Global Codex high workers:** `task-explore-high` and `task-execute-high`
  both pin `gpt-6.1-sol` with `low` reasoning. The user explicitly confirmed
  this exact Sol model after clarification.
- **Global Codex scope and verification:** this supersedes previous worker
  model decisions for Codex only. All four native TOML files were parsed and
  checked against these pairs; canonical loaders, sandbox, and approval settings
  were preserved. No live child smoke was run. Existing sessions may retain
  their loaded profiles until a fresh session loads the saved configurations.

## Reconciliation and defaults confirmed 2026-09-30

- **Global Codex root and normal orchestrator, user decision September 30:**
  exact `gpt-6.1-sol`/`low`, with Sol medium only on demand. The saved root
  medium was changed to low following this explicit reply; the normal
  orchestrator changed from `gpt-6-sol` to `gpt-6.1-sol`. GPT 6 Sol must not
  remain a standing default. This supersedes earlier saved-medium/high default
  guidance and the September 29 orchestrator mapping. Service remains default;
  no new priority decision was supplied.
- **Global Codex workers:** both micro workers retain `gpt-6-luna`/`xhigh`;
  both high workers retain `gpt-6.1-sol`/`low`. Parsed and checked all five
  native role files and the root TOML without altering worker permissions.
- **Global Codex shared skill discovery:** nineteen canonical skills and nineteen
  thin shared loaders, no missing or extra loaders. Added `web-search-advanced`
  with `disable-model-invocation: true` and `task-hermes`; refreshed quick web
  search discovery to native tools by default. Artificial Analysis was already
  present but missing from prior adapter accounting. A fresh strict-config CLI
  root discovered both additions and quoted the explicit-only advanced rule.
  Hermes discovery does not enable its task or messaging routes.
- **Global Codex maintained-role overrides:** current native role schema fixes
  model and reasoning and explicitly disallows overriding them. Full one-run
  model/reasoning/service selection is unsupported. Generic agents are not an
  acceptable replacement. The launcher also lacks child service control and
  effective profile telemetry. Earlier maintained-role override claims are stale.
- **Global Codex model availability:** GPT 6.1 Sol remains absent from the model
  cache but is named by the runtime role schema; a fresh CLI root request for
  GPT 6.1 Sol/low completed. This is request acceptance and execution evidence,
  not independent effective-profile telemetry.
- **Global Codex search MCPs:** Parallel search, Exa search and Firecrawl scrape
  succeeded through direct current-session calls without prompts. Enablement,
  keyed environment-variable names, timeouts, approval posture and Firecrawl's
  four-tool allowlist remain aligned with the September 29 decision.
- **Global Codex account health:** Gmail list_labels filtered by INBOX and Drive
  get_profile succeeded. No email or file contents were read. Child connector
  inheritance was not tested.
- **Global Codex local extras:** code-review plugin is installed/enabled; its MCP
  is disabled. Slack is now locally confirmed installed/enabled. Remote plugin
  inventory failed both normal and approved retries; no remote removal is inferred.
  Skyscanner tools are also exposed in the current session. These remain local
  under the September 15 plugin/internal-service decision, with no promotion.
  Generic default/explorer/worker agent types remain runtime-local; they were
  inventoried but not used as maintained-worker substitutes.
- **Global Codex browser and permissions:** retained dated route evidence and
  existing settings. No browser attachment, new connector enablement, permission
  broadening, optional software, hook, or credential installation occurred.
  The shared discovery directory is not a Git repository; its loader edits are
  machine-local and cannot be committed there. Canonical adapter records carry
  the change evidence in the global agents workspace.

- **Global Codex nested role smoke, user-authorized September 30:** a fresh
  read-only CLI root requested the updated named orchestrator and one named
  explore leaf. It returned accepted roles, completion and `# Task Worker Tiers`.
  The JSONL capture had no identifiable child-launch records and wait events had
  empty receiver lists. This is a successful returned result with self-reported
  nesting, not independently observed child dispatch or effective profiles.
  No product edits or external tools were observed in the root capture.

- **Global Codex advanced-search helper support:** native-only main search and
  named providers are mapped. Full-budget Luna/xhigh helper search is not mapped:
  micro workers are too restricted for the complete search procedure, and fixed
  high workers cannot select Luna. A maintained high-capacity Luna role variant
  would need an explicit support decision and verification; do not substitute a
  generic agent or call Codex's own CLI as a research-helper workaround.

## Revisit During the Next Codex-Owned Reconciliation

- Re-list global Codex MCP services and plugins, then surface any new external
  integration individually for a promote-or-keep-local choice.
- Recheck exact model roster and whether child model and effort telemetry is
  exposed. Do not claim runtime verification from request acceptance alone.
- Recheck root Gmail and Google Drive application-connector health separately
  from `codex mcp list`, using read-only allowlisted calls only. Recheck whether
  a native child or `task-explore` policy child gains callable connector tools
  before delegating connector-backed Google research.
- Favorites and efforts were confirmed September 30. Ask only for missing
  priority posture or additional temporary-role support, not the same favorites.
- Recheck the September 30 named role smoke outcome separately from the older
  September 25 state-database diagnostic. Do not treat the old diagnostic as proof
  of a current failure or an approved database repair.

## Permission migration applied 2026-09-30

- Root config and all four enabled worker files now save `approval_policy = "never"`
  and `sandbox_mode = "danger-full-access"`. Models, efforts, canonical loaders,
  disabled fast roles and intentional connector/tool exclusions are unchanged.
- Explore reporting and execute packet scope remain prompt-enforced, with root
  verification. Full access is not filesystem confinement or authorization for
  recursive workers, other providers or account side effects.
- A fresh strict-config CLI session without permission overrides passed fixture
  read/write, shell, HTTP 200 and one enabled Parallel public fetch. Root rollout
  confirms GPT 6.1 Sol/medium and never/full access.
- High explore completed its new report. Both high child rollouts independently
  confirm named roles, GPT 6.1 Sol/low, never/full access and depth 1. High execute
  initially timed out, then a single replacement named high worker completed its
  exact fixture write; the coordinator checked output bytes and copied native
  turn context. The implementation and recovery roots reached their supervisor
  deadlines, so no clean final root exit is claimed. Default Luna workers remain
  static-only pending owner version confirmation.
- Detailed evidence and rollback:
  `changes/260930_1900__autonomous-task-permissions/results/codex/REPORT.md` (private, not published).
  Start fresh sessions to load defaults; existing live overrides can still win.

## Orchestrator access follow-up 2026-09-30

The normal role explicitly saves never approvals/full access; root native maximum
depth is two. Broad shell access includes Node.js and installed scripting tools.
Four enabled named terminal leaves are the only authorized children, but Codex
has no child-name allowlist: those restrictions are behavioral, while numeric
depth is a native ceiling. Models/efforts/connectors and leaf instructions stayed
unchanged. Configured/static-only; edited TOML parsed and exact saved keys read
back. No live tests. Both bounded CLI supervisors timed out; the second saved the
changes and receipt before termination. This supersedes any inherited-only
orchestrator permission description, not the historical runtime evidence.

## Worker and orchestrator descriptions checked 2026-10-07

- Global Codex: owner-requested apply-now run limited to workflow steps 5 and 6.
  All five model/effort pairs match the briefing and all canonical loaders remain.
  Descriptions now point explicitly to the Codex part of section 3 and retain
  the original role sentence followed by one short model/effort/cost/guessing
  line. All other native keys are unchanged.
- Global Codex: saved root is GPT-6.1 Sol medium, not the historical low default
  (`config.toml` lines 3 and 4). High workers use that same pair. The comparison
  holds; clarify exact parity. Current native dispatch permits four active agents
  including root, so pool suggestions must yield to at most three direct workers
  or two leaves with an active orchestrator. No saved count cap was added.
- Global Codex: five TOML parses passed and native `codex doctor --json` reported
  `config.load: ok`. Prompt-input rendering succeeded but omitted dispatch tools;
  its strict-config option is unsupported. No worker launch, nesting test, speed
  or quota measurement occurred. Fast workers and fast orchestrator stay disabled.
- Global agents workspace: Sol medium and Sol high cards lack "Tell the worker"
  lines. No briefing, role, skill or other shared file was changed.

Suggested comparison clarification for the global agents workspace, not applied:

> **How the tiers compare:** regular explore is GPT-6 Luna xhigh (35, guesses on
> 82% of misses), regular execute is GPT-6.1 Sol low (42), high workers are
> GPT-6.1 Sol medium (48), and the orchestrator is GPT-6.1 Sol high (50). The
> saved Codex root is GPT-6.1 Sol medium, so high workers use the same model and
> effort as the root; regular execute is one effort step below, and Luna is far weaker.

Suggested count correction for the global agents workspace, not applied:

> **How much to delegate:** a lot for lookups, less for reasoning. Cost guidance
> is 3 to 8 cheap Luna lookups and 2 to 4 Sol workers, with doubled Sol deadlines
> and fewer rounds. The current Codex dispatcher permits four active agents
> including root: at most three direct workers in total, or two leaves while an
> orchestrator is also active. These runtime limits take precedence over pool counts.
