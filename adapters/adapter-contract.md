---
created_at: 2026-07-01
updated_at: 2026-09-30
model: gpt-5.6-sol
doc_type: contract
purpose: Define the platform-neutral adapter contract for connecting AI tools to the Agents workspace via exhaustive, bidirectional, ledgered reconciliation.
related:
  - path: ../INDEX.md
    why: Shallow router for Agents workspace source-of-truth roots.
  - path: ../skills/AGENTS.md
    why: Defines reusable procedure ownership.
  - path: ../roles/AGENTS.md
    why: Defines reusable specialist behavior ownership.
  - path: ../roles/task-worker-tiers.md
    why: Defines portable worker model-tier semantics that adapters resolve.
  - path: ../roles/task-orchestrator.md
    why: Defines the portable frontier orchestration boundary that adapters preserve.
  - path: ../capabilities/AGENTS.md
    why: Defines external bridge ownership.
  - path: ../capabilities/connectors.md
    why: Portable connector/MCP registry that adapters reconcile native MCP config against.
  - path: ./INDEX.md
    why: Lightweight registry of intentionally maintained tool adapters.
  - path: ../workflows/adapter-lifecycle/sync-tool.md
    why: The onboard/reconcile workflow that applies this contract.
---

# Adapter Contract

Adapters connect a specific AI runtime to the Agents workspace. The Agents
workspace remains the source of truth; native tool files are implementation
details.

## Single-Tool Boundary (Commandment)

One `sync-tool-adapter` run reconciles exactly ONE tool, and that run should be
performed by that tool, in its own session. No single AI agent or session may
inspect, reconcile, migrate, or edit the native configuration of more than one
tool. "Align all my tools" is never one session's job; it is N separate runs, one
per tool, each in that tool's own runtime.

Why this is a hard rule, not a preference:

- **Faithful introspection.** Only a tool running inside its own runtime can
  actually see its live native config, available MCP/plugins, subagents, and
  permissions. Any agent reconciling a *different* tool is working blind from
  files and guesses.
- **Verification.** Only the tool itself can apply a native change and confirm it
  took effect (reload/restart, tier resolves, MCP connects). A foreign agent
  cannot verify another tool's runtime.
- **Blast radius.** A mistake stays scoped to one tool instead of corrupting
  several at once.
- **Context.** Reconciling N tools in one session bloats context and degrades
  every tool's result.
- **The thesis itself.** The workspace is the hub; each tool converges to it
  independently. One agent editing many tools recreates the coupling this system
  exists to eliminate.

Adapter docs seeded by a central workspace change (rather than by a tool's own
run) are **provisional**: each tool must confirm its own mapping, tier matrix,
connectors, and divergences in its own `sync-tool-adapter` session.

## Permission Bootstrap And Required Mapping

Load `~/agents/conventions/autonomous-task-permissions.md` before
onboarding, sync or unattended execution. An explicit current permission-policy
apply request authorizes its focused own-harness inspection/apply step before
an exhaustive sync audit. The remainder stays subject to the normal audit/apply
gate; merely reading this contract does not authorize security changes.

Every maintained adapter must document **Permissions and unattended execution**:
persistent rule locations/scope; exact supported all-access/approval/sandbox flags
and a copyable headless launch; root/orchestrator/leaf tool inheritance; native
child-name/depth enforcement versus behavioral limits; retained exceptions;
reload/new-session needs; human-only or unsupported controls; and configured,
static-checked versus live-tested status. State whether a flag bypasses asks,
sandboxing or explicit denies. Never invent a YOLO flag or claim the policy can
remove OS/managed/provider limits. Refer to the canonical policy rather than
copying its whitelist. Permission-only changes use its bounded check procedure,
not the full reconciliation or an automatic live smoke campaign.

## Portable Concepts

```text
instructions = standing context and routing rules
skills = reusable procedures
roles = reusable specialist behaviors
capabilities = external bridges agents may use
workflows = durable multi-phase processes
policies = permission and enforcement expectations
changes = restartable execution packets
adapters = runtime-specific mappings
model bake-offs = portable benchmark contracts whose requested competitors are
  resolved by the active runtime adapter
worker model tiers = portable default-micro/fast-micro/high semantics for task worker
  wrappers, resolved by the active runtime adapter
one-run role profiles = explicit per-launch model, reasoning, and service
  settings applied to an adapter-maintained role without changing its behavior
skill capability hints = portable skill dependency declarations that adapters
  reconcile against tool/session/project connector availability
operator entrypoints = human-invoked native shortcuts for adapter lifecycle
  skills when the target runtime supports them
native config = generated, copied, linked, or manual implementation detail
```

## Source-Of-Truth Roots

- `../AGENTS.md`: canonical workspace instructions.
- `../INDEX.md`: shallow router and progressive-disclosure entrypoint.
- `../skills/`: canonical reusable procedures.
- `../roles/`: canonical reusable specialist behaviors.
- `../capabilities/`: canonical capability descriptions.
- `../workflows/`: durable process composition.
- `specs/`, `changes/`, `projects/`, and `artifacts/` (private, not published):
  durable work, current behavior, scoped memory, and historical output roots.

## Adapter Rules

- Do not make native tool config the source of truth.
- Do not duplicate skill or role behavior into an adapter doc. If the runtime
  cannot point to or load the source file, record that limitation instead.
- Prefer thin wrappers that name the native concept and point back to the Agents
  workspace.
- **Shared and native skill wrappers are loaders, not procedure definitions.** A
  wrapper may carry only runtime discovery metadata and the instruction needed to
  load the canonical skill. It must not copy authorization rules,
  classifications, workflow steps, stop conditions, report shapes, privacy rules,
  or other canonical skill content. Copied behavior prevents workspace changes
  from propagating and is `duplicated` drift.
- **Operator command wrappers pass through the current request.** A native command
  may identify its target tool, load the canonical skill, and pass the user's raw
  arguments as the current request. It must not reinterpret those arguments,
  declare that they cannot authorize edits, or copy procedure and stop rules.
- **Native role wrappers are loaders, not role definitions.** A wrapper may carry
  only the runtime-native identity/description, model or tier resolution,
  sandbox/permission settings, and the instruction needed to load the canonical
  role and tier files. It must not copy packet types, behavior rules, stop
  conditions, report shapes, connector policy, or other canonical role content.
  Any such copied content is `duplicated` drift and must be replaced with a thin
  loader during that tool's next own-run sync.
- Preserve permission and role boundaries when translating to native config.
- Preserve `task-explore` create-only reporting: workers may create new Markdown
  files inside a packet-assigned exclusive output directory but may not modify
  existing files or any inspected source. Use compatible native path and tool controls without
  blocking authorized reports or routine work under
  `~/agents/conventions/autonomous-task-permissions.md`. If full access
  cannot technically express this boundary, preserve it in the canonical role and
  packet, verify it at the root, and record prompt-enforced scope explicitly.
  Blocking required reports or claiming technical confinement without it is drift.
- Resolve model bake-off competitors in the active runtime adapter. Do not add a
  global canonical model list or silently substitute unavailable requested models.
- Model choices for worker tiers, orchestrators and CLI bridges come from
  `~/agents/ai-models/delegation-briefing.md` (since 2026-10-01). The adapter records how each
  choice is wired and whether it was live-checked; any native setting that
  differs from the briefing is drift. Do not silently substitute unavailable
  tier models or treat a missing tier as supported without user confirmation.
- Resolve one-run role profiles in the active runtime adapter. A temporary profile
  may change only model, reasoning, service, and the minimum native launch mode
  required to select the maintained role. It must preserve the role's canonical
  prompt source, permissions, sandbox, authority, delegation boundary, and stop
  conditions. Do not broaden task authority as a profile field. Routine technical permissions
  follow `~/agents/conventions/autonomous-task-permissions.md`, including
  its owner-approved non-interactive default; model selection is not a new grant.
- An explicit user-invoked RoleDispatch run may select any exact, verified harness
  model for any maintained role, including a frontier model for `task-explore` or
  `task-execute`. It must preserve the maintained wrapper and must not inherit or
  silently substitute a model. This one-run freedom does not change the adapter's
  standing default, fast, or high worker mappings.
- Keep exact model identifiers, supported reasoning values and service controls
  in the tool-specific mapping. Which model to use, and why, stays in the
  delegation briefing only. Do not duplicate choices into portable roles,
  procedures or tool memory.
- When a tool cannot safely select a maintained role with a one-run profile,
  record `unsupported-with-reason`. Inheriting the parent model, silently
  substituting another model, or falling back to a generic agent is not support.
- Expose adapter lifecycle operator entrypoints only where supported by the
  runtime; do not imply every reusable skill needs a native command.
- Report unsupported concepts explicitly.
- **Every sync is audit-first; explicit apply-now authorization is reusable.**
  Phase 1 is read-only across native config, shared wrappers, adapter docs, the
  registry, and canonical sources. A clear current-message instruction to apply,
  fix, update, repair, or complete the adapter changes now authorizes Phase 2 in
  the same invocation after the audit. Without that instruction, Phase 1 reports
  the exact proposed apply set, asks for confirmation, and stops. An explicit
  audit-only request reports and stops without an apply question. Authorization is
  semantic, not tied to a magic phrase or a mandatory second reply.
- **Apply-now does not fill in missing decisions.** It authorizes deterministic
  in-scope alignment and per-item choices the user actually supplied. It does not
  imply model preferences, connector enablement, promotion, permission broadening,
  or unrelated scope. Apply resolved items and leave true choices untouched.
- **Report connectors with unambiguous scope labels.** Every connector line MUST
  name its location: "Agents workspace registry" (tool-agnostic curated set) vs
  "`<Tool>` global" (this tool's user config) vs "`<Tool>` project (`<repo>`)"
  (this tool's repo-scoped config). Never write a bare "globally" — it hides
  whether something lives in the workspace or the tool.
- **`default-off` never means delete.** A connector the user wants kept default-off
  MUST stay present in native config and merely be toggled off. Removing it from
  native config is drift. (Recording a wanted connector as "off / not configured"
  and dropping it from `mcp.json` is the failure this rule prevents.)
- **Awareness-only bridges are not default-off MCP connectors.** Browser-native,
  CLI/library, hosted API, and desktop entries in the registry's browser/desktop
  awareness section are audited and mapped as capabilities. Listing them does not
  require installation, native config, credentials, or an enabled signed-in route.
  If the user selects one, follow its guide and verify it in this tool's own
  session. Keep each route's browser identity and proof tier explicit.
- **Registry default-on connectors.** A connector the registry marks default-on
  with a dated user decision is expected configured and on in every tool. The
  tool's own sync adds it by following the registry's linked setup guide,
  including its approval gates, and asks instead when the tool cannot meet
  them.
- **Retired interfaces are removal-required.** When canonical capability policy
  retires a native interface, that interface is not a curated connector to keep
  default-off and not a tool-side extra to promote or keep local. Its tool's own
  own-tool Phase 1 reports the required removal and replacement. Phase 2 removes
  it, reloads the runtime, verifies its tools are absent, installs or aligns the
  named replacement routing when supported, verifies the replacement, and records
  the superseding decision during an authorized apply phase. Apply-now
  authorization may carry from the initial request after the audit; review-first
  mode waits for post-report confirmation. Audit-only runs report it as pending.
  Central sessions may record migration as pending but must not inspect or edit
  another tool's native state.
- **Decisions are reminders, not repeated action items.** Once a connector/tier/
  capability disposition is decided, later runs re-list it from the divergence
  ledger as a dated reminder in the "previously-decided" bucket and MUST NOT re-ask
  it as an action item unless the user reopens it or state changed.
- **Record auth expectation.** Note which connectors use interactive browser OAuth
  (each tool holds its own token store and may need a per-tool login/`mcp auth`
  step) vs static token/credential vs no-auth.
- **Retire legacy role-MCP records instead of preserving them.** Existing tool docs,
  ledgers, or native wrappers that describe per-role/subagent MCP customization are
  stale canonical drift and should be removed during that tool's next own-run sync,
  without generating replacement per-role records.
- Keep secrets and local credentials out of the Agents workspace.
- Keep the lightweight `INDEX.md` registry current when a tool adapter is
  onboarded, materially repaired, or retired.

## Reconciliation Is Exhaustive, Bidirectional, and Never Silenced

Onboarding and drift alignment are one operation: reconciliation. Onboarding is
just reconciliation from an empty adapter. Every reconciliation MUST:

- **Enumerate every difference in both directions and drop nothing.** Compare
  workspace -> tool (what the workspace defines that the tool lacks) AND
  tool -> workspace (what the tool supports that the workspace lacks). An empty
  diff is an explicit positive claim ("N differences found, all classified"), not
  a section skipped.
- **Surface every tool-side extra for a user decision — never auto-promote.**
  Anything a tool supports that the workspace does not — a skill, role, worker
  tier, MCP/connector, plugin, permission posture, or behavior — MUST be surfaced
  individually and its disposition decided by the user. Promotion into the
  workspace is ALWAYS an explicit, per-item user decision; a reconciliation run
  must never assume something belongs upstream, and must never merge or enable
  anything on its own. The **default disposition is to leave it tool-local** and
  record the decision; promotion is the exception the user opts into.
- **Record every decision so it re-surfaces as a reminder.** Approved divergences,
  declined promotions, and "keep tool-local" choices are all written to the tool's
  divergence ledger and listed again on the next run, annotated
  `user-decided <date>` (e.g. `approved`, `declined`, `keep-local`). Decisions are
  reminders, not silencers: the run re-lists them so the user stays aware and can
  change their mind. There is no silent "noticed and moved on" state.

This operationalizes the mission corollary: tools converge to the system; the
system never bends to a tool.

## Drift Categories (internal diff aid, not report headings)

These labels are an internal aid for the person or agent running the sync, so the
diff cannot hide gaps on either side. They are NOT the words the user-facing report
uses: the report says things in plain English per Report Shape ("aligned",
"missing", "out of date", "extra in the harness", "kept on purpose"). Categories
are directional:

- `missing-in-tool`: an Agents workspace skill, role, worker tier, capability,
  connector, or workflow has no corresponding native entry where one is expected.
- `missing-in-workspace`: the tool supports a skill, role, tier, connector,
  permission posture, or behavior that the workspace has not decided on. Must be
  promoted or recorded as an approved divergence (supersedes the old passive
  `tool-local` bucket, which allowed silent tolerance).
- `stale`: a native entry points to moved, deleted, or superseded Agents workspace
  paths.
- `duplicated`: native config copies source text that should be a thin wrapper.
- `intentionally-divergent`: native behavior differs for a documented tool
  limitation or explicit user choice. Recorded in the tool divergence ledger and
  re-surfaced every run; never a reason to skip reporting.
- `missing-in-tool` (global bootstrap): `~/.agents/AGENTS.md` is a regular file or
  thin redirect instead of a symlink (or documented equivalent) to canonical
  `~/agents/AGENTS.md`.

When a runtime supports human-invoked commands, a missing native entrypoint for
`sync-tool-adapter` is `missing-in-tool` drift unless the tool-specific adapter
documents an intentional limitation.

## Scope Labels (always spell these out)

Every line in a report or mapping doc names exactly which of three places it means.
Never write a bare "workspace", "the tool", or "globally"; those hide which place
you mean. Always write the harness's real name, because a run may happen in any
harness. Repeat the full label as often as needed; repetition is better than
ambiguity.

- **global agents workspace**: the agent-agnostic source of truth at `~/agents`. It
  belongs to no tool. Skills, roles, worker tiers, capabilities, the connector
  registry, and workflows live here. Always write all three words.
- **global `<harness>`**: the harness's own user-level config that applies in every
  folder. For Cursor that is the user rules, `~/.cursor/` skills and subagents, and
  the global `~/.cursor/mcp.json`. Write it with the real name, e.g. "global Cursor"
  or "global Codex".
- **`<harness>` current project (`<repo>`)**: the harness's config scoped to the
  folder this run is inside, but only when that folder has its own config. For
  Cursor that is `<repo>/.cursor/`. Include this place only when the current folder
  actually carries harness project config; otherwise say so once and move on.

A run may sit inside a folder that carries its own harness config, so one thing can
be defined in the global agents workspace, present or absent in global `<harness>`,
and separately present or absent in `<harness>` current project. Report all three
where they apply.

## Report Shape

A report is plain English and easy to scan. No status codes, no abbreviations, no
tables of coded verdicts, and none of the words "matrix", "ledger", or "drift" in
the user-facing text. It has, in order:

1. **Current state summary** — one short paragraph: which harness, onboard or
   reconcile, when it was last synced, and the headline of what is aligned and what
   is not.

2. **One section per area**, each with its own heading, in this order: Instructions,
   Skills, Roles and subagents, Worker tiers and models, Frontier orchestrator,
   One-run role profiles, MCP connectors, Commands and entrypoints, Permissions and
   policies. Inside each section use up to three separate bullet lists so the reader
   always knows whose point of view a line takes:

   - **From the global agents workspace** — one top-level bullet for every item the
     global agents workspace defines in this area. Under each item, one nested
     bullet per place it should appear:
     - **global `<harness>`**: one or two sentences. Is it present, does it match,
       and if it is aligned, since when. If not, say plainly what is missing or
       wrong.
     - **`<harness>` current project (`<repo>`)**: the same, and only when the
       current folder has its own config for this area.
   - **Only in global `<harness>`** — one bullet for each harness-global item the
     global agents workspace does not define, with a short note on what it is and
     the standing choice (kept in the harness on purpose, promoted, or waiting on a
     decision).
   - **Only in `<harness>` current project (`<repo>`)** — the same, when applicable.

   If any of these lists is empty, write "none" so the reader knows it was checked.
   Never omit a list silently.

3. **Summary of changes and recommendations** — grouped under the same section
   names. For every recommended change, state four things in plain words: what the
   change is, the current state, the recommendation, and whether it "needs your
   decision" or is "safe to apply". This is the single place that gathers action
   items, so the reader can act without re-reading the whole report.

Hard rules for the report:

- Never drop an item. An empty list is written as "none", not omitted.
- Say it in words: "aligned", "missing", "out of date", "extra in the harness", or
  "kept on purpose", plus the date when known. Do not use coded verdicts.
- Anything a harness has that the global agents workspace does not define goes in
  the matching "Only in ..." list and gets a recommendation: promote it into the
  global agents workspace, or keep it in the harness. Promotion is always the user's
  explicit choice; the default is to keep it in the harness and say so. Nothing is
  silently accepted.
- Prior decisions are repeated every run as short dated reminders under the place
  they apply, so the user stays aware without being re-asked.
- In review-first mode, finish with the exact proposed apply set and one
  confirmation question, then stop. In apply-now mode, state a concise apply set
  after the audit, proceed without another approval turn, and finish with the exact
  applied and skipped sets. In audit-only mode, do not ask to apply changes.

## Per-Tool Mapping Doc Skeleton

Each intentionally maintained tool has one mapping doc (`adapters/<tool>.md`) with
these mandatory sections, plus a separate divergence ledger
(`adapters/<tool>.divergences.md`):

- **Native surfaces**: where the tool's instructions, skills, agents, commands,
  MCP, permissions, and hooks live.
- **Source mapping**: each workspace concept -> its native concept.
- **Worker tier matrix**: all six cells of
  `{task-explore, task-execute} x {default, fast, high}`, each present with
  its model/settings or explicitly marked unsupported-with-reason.
- **Frontier orchestrator mappings**: normal and fast mappings of the canonical
  role, each present with model/settings or explicitly unsupported-with-reason.
- **One-run role profiles**: native per-dispatch support, headless/inline or
  temporary-profile support, exact tool-local controls, preferred profiles,
  capture/verification, concurrency, and limitations.
- **Connectors / MCP inventory**: native MCP/connectors mapped to
  `capabilities/connectors.md` entries.
- **Drift checks**: the tool-specific invariants a reconciliation run verifies.

## Worker Model Tiers

Adapters may retain `task-explore`, `task-explore-fast`, `task-explore-high`,
`task-execute`, `task-execute-fast`, and `task-execute-high` as runtime-native
wrappers around the portable role contracts. Availability and tier semantics are
defined in `../roles/task-worker-tiers.md`.

- `default`: the cheaper worker model in each tool. How capable it is varies a
  lot by tool; each tool's part of section 3 of
  `../ai-models/delegation-briefing.md` says what it may take.
- `high`: enabled for bounded moderately complex work. Each tool must verify an
  explicit model and effort or report unsupported-with-reason.
- `fast`: disabled by canonical tier guidance and must refuse launch.

Every intentionally maintained tool doc MUST resolve all six tier cells as present,
disabled, or unsupported-with-reason. A disabled cell must identify the canonical
tier guidance as its authority and must not be available to one-run dispatch. A
cell with no recorded decision is `missing-in-tool` drift. Reconciliation verifies
the recorded matrix against current native config each run. Native config remains
the implementation detail.

No enabled `task-explore` or `task-execute` tier cell may resolve to "inherit the
parent / phase model." Every enabled cell must resolve to an explicit model or
be marked unsupported-with-reason. Delegated discovery and execution must never
silently run on the root's model, so an inherit-parent resolution is a
contract violation; reconciliation flags it as `missing-in-tool` drift (the
required non-inheriting decision is absent).

An explicit user-controlled RoleDispatch run may select another verified model only
for a role currently enabled by `task-worker-tiers.md`. A one-run selection cannot
override a disabled role.

## Frontier Orchestrator Mapping

`task-orchestrator` is a distinct portable frontier role, not a worker tier and
not an extra generic-agent fallback. When a runtime supports it, its native
wrapper remains thin and loads the canonical role contract.

Each intentionally maintained adapter must resolve both `task-orchestrator` and
`task-orchestrator-fast` as present, disabled, or unsupported-with-reason. Normal
orchestration is enabled only when that tool verifies its mapping; fast remains
disabled by `task-worker-tiers.md`. The fast name is an adapter-level mapping of
the same role, not another portable role or worker-tier cell.

This requirement rolls out one tool at a time. A central policy change may mark
other maintained adapters pending, but it must not inspect or edit their native
configuration or claim support. Each tool fills and verifies its own mappings in
its next own-runtime `sync-tool-adapter` run.

The native mapping must preserve this exact depth: a root may launch an
orchestrator; an orchestrator may launch only `task-explore`,
`task-explore-fast`, `task-explore-high`, `task-execute`, `task-execute-fast`, and
`task-execute-high`; those leaves may not delegate. Do not map an orchestrator to another orchestrator, a generic
native agent, inherited worker dispatch, or a deeper delegation path. If native
permissions can restrict child dispatch, allow only the six named wrappers. If
they cannot, record the limitation explicitly rather than claiming enforcement.

Native interaction controls must preserve the canonical authority boundary:
interactive questions and approvals return through a durable handoff to the
user-facing root, while autonomous operation requires explicit user instruction
and never extends scope or permissions. Native wrappers must not copy the
canonical packet, handoff, or authority rules.

## One-Run Role Profiles

Every intentionally maintained tool mapping must document whether an
adapter-maintained role can be launched once with an explicit runtime profile.
The goal is user-controlled freedom to run any maintained role on any exact,
verified model the harness supports without creating permanent wrappers for every
model. This is an execution path, not a permanent role or global model registry.

Existing mappings may remain explicitly pending until that tool's next own-run
sync. Pending is not support and must not trigger inherited-model or generic-agent
fallback.

The mapping must record:

- supported dispatch paths: native per-call override, headless or inline process,
  temporary native profile, manual-only, or unsupported;
- the maintained roles that path can select and any mode bridge required to make
  them directly launchable;
- the exact model-discovery command and a compact user-selected favorite subset,
  with the date the user confirmed it; do not copy the harness's full catalog;
- exact commands or native controls for model discovery, model selection,
  reasoning, service class, working directory, structured output, continuation,
  and cancellation;
- the tool-local model identifiers and supported reasoning/service combinations
  the user wants preserved as preferred profiles;
- exact standard/default and fast/priority syntax and whether fast/priority is
  opt-in, unavailable, or provider-defined;
- how the launch preserves the role prompt, permissions, sandbox, task allowlist,
  and non-recursion rules;
- how the root verifies actual role, model, reasoning, service when exposed,
  session identity, completion, output path, and mutation state;
- concurrency limits, process ownership, timeout and cleanup behavior, and the
  isolation required for parallel read-only or mutating runs;
- unsupported cases and explicit failure behavior, with no inherited-model or
  generic-agent fallback.

Onboarding always asks the user for favorite models, default reasoning,
fast/priority posture, and which small read-only profiles to verify. Reconciliation
re-lists current favorites and asks again only when the record is missing, stale,
unverified, or affected by a changed model roster or CLI. A mapping missing any of
the required role, model, command, reasoning, service, preference-date, or
verification fields is not aligned.

One-run overrides are process- or invocation-scoped and must not mutate permanent
native config unless the user separately requests a persistent profile. Temporary
mode changes grant no new permissions or authority. Selected read-only smokes run
only in an authorized Phase 2. A mutating smoke is not required.

## Adapter Output Expectations

When onboarding or reconciling an adapter, produce a report in the Report Shape
above, using the Scope Labels above. Across the per-area sections and the closing
changes list, the report must cover:

- which harness this is, onboard or reconcile, and which native concepts it supports
- which global agents workspace roots and which native files or settings were read
- how each global agents workspace concept maps to a native concept
- all six worker tier cells with their current model and settings, or an explicit
  "not supported, because ..." for any cell
- the normal and fast frontier orchestrator mappings, each with its model and
  settings or an explicit "not supported, because ..."
- one-run role-profile support: the exact native way to launch it, the preferred
  models and settings, how permissions and identity are preserved and checked,
  concurrency limits, favorite-model confirmation date, exact reasoning and
  fast/priority syntax, per-profile verification status, and any unsupported cases
- the MCP connector picture reconciled against `../capabilities/connectors.md`, laid
  out by place (global agents workspace registry, global `<harness>`, and
  `<harness>` current project), naming each connector's auth expectation
- prior decisions repeated as short dated reminders under the place they apply
- unsupported or manual setup items
- the closing changes list, each item marked "needs your decision" or "safe to
  apply", plus, when edits were authorized, what changed and how it was checked
- any registry, mapping-doc, or reminder-ledger updates made this run
- in review-first mode, the exact proposed apply set and an explicit confirmation
  question before stopping; in apply-now mode, the concise pre-apply set and exact
  final applied/skipped set; in audit-only mode, no apply question
