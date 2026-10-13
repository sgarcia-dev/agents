---
created_at: 2026-07-07
updated_at: 2026-09-30
model: gpt-5.6-sol
doc_type: workflow
purpose: Define one workflow to onboard or reconcile an AI tool adapter against the Agents workspace via exhaustive, bidirectional, ledgered comparison.
related:
  - path: ../../adapters/adapter-contract.md
    why: Platform-neutral adapter contract, scope labels, report shape, and directional drift categories this workflow applies.
  - path: ../../adapters/INDEX.md
    why: Registry to update when a tool adapter is onboarded, materially repaired, or retired.
  - path: ../../INDEX.md
    why: Shallow router for source-of-truth roots.
  - path: ../../capabilities/connectors.md
    why: Portable connector/MCP registry to reconcile each tool's native MCP config against.
  - path: ../../roles/task-worker-tiers.md
    why: Portable worker-tier semantics whose per-tool matrix this workflow verifies.
  - path: ../../skills/sync-tool-adapter/SKILL.md
    why: Skill entrypoint for invoking this workflow.
---

# Sync Tool Adapter

Onboard or reconcile a single AI tool adapter against the Agents workspace. This
one workflow replaces the separate init and align workflows: onboarding is just
reconciliation from an empty adapter. The Agents workspace stays canonical; native
tool config is an implementation detail.

**Single-tool commandment.** One run = exactly one tool, performed by that tool in
its own session. Never inspect, migrate, or edit more than one tool's native config
in a single session; "align all tools" is N separate runs. See the contract's
Single-Tool Boundary for the rationale. Adapter docs seeded by a central workspace
change are provisional until the tool confirms them in its own run.

## Modes

Detect the mode from current state; the comparison engine and output are identical.

- **Onboard**: no `adapters/INDEX.md` row or no tool-specific mapping doc exists
  yet (or the tool is marked `not onboarded`). Discover native surfaces, build the
  mapping, create the mapping doc + divergence ledger, and add the registry row.
- **Reconcile**: a mapping doc and registry row already exist. Run the full
  bidirectional diff against the current workspace and native config.

Do not treat a half-onboarded tool (row present, doc missing, or vice versa) as a
clean run: complete onboarding for the missing half, then reconcile.

## Permission Bootstrap Before Full Audit

Read `~/agents/conventions/autonomous-task-permissions.md` first.
A current permission-policy apply instruction authorizes a separate focused
own-harness inspection/apply step before exhaustive onboarding/reconciliation.
Use that policy's bounded procedure and minimum syntax/readback checks; do not
start a worker/MCP smoke campaign unless requested. For a permission-only task,
stop after applying/documenting that subset rather than running this full workflow.

For a full sync, finish the authorized bootstrap, record its changed settings as
the new baseline, then start the normal read-only full audit. The full audit may
not make other edits before its apply gate. Routine permission settings already
approved in the current request need no second approval round; this exception
never authorizes new connectors, model choices, cross-provider delegation or
other tool-side promotions. Audit-only/review-first discovery stays read-only.

## Audit-First Authorization Gate

Every invocation starts with a read-only audit. The audit may be followed by edits
in the same invocation when the current user message clearly authorizes applying
the in-scope changes now. Except for the separately authorized permission bootstrap above, no edits are
permitted before the full audit.

Resolve one mode semantically from the current request:

- **Apply now**: a clear imperative to apply, fix, update, repair, or complete the
  adapter changes now, including an instruction not to stop for another approval.
- **Review first**: no clear current-message authorization to write. This is the
  default for a bare skill invocation or a request to inspect/check alignment.
- **Audit only**: an explicit request to make no changes.

Do not require a magic phrase or a second reply. Old standing permission and broad
permission unrelated to this adapter run do not count.

### Phase 1: Read-Only Audit

- Inspect and compare both directions without editing native config, shared adapter
  wrappers, mapping docs, divergence records, the adapter registry, or canonical
  workspace sources.
- Discover supported models and native controls with read-only commands. Do not run
  preference-dependent RoleDispatch smokes before the user chooses the profiles.
- Complete the exhaustive audit and exact change list, including retired
  migrations and verification calls.
- In review-first mode, ask the user to approve, reject, or modify that exact list,
  then stop.
- In apply-now mode, state a concise apply set and continue directly to Phase 2.
  The full report may be delivered after verification; do not force a large
  pre-apply report or another approval turn.
- In audit-only mode, report and stop without an apply question.

### Phase 2: Authorized Apply

- Enter after either explicit apply-now authorization in the current request or a
  later user response confirming the review-first proposal.
- Apply only the authorized subset. A newly discovered deterministic edit within
  the authorized scope may be applied after it is added to the run's exact apply
  set. Scope expansion or a missing value judgment requires a user decision.
- Verify, update adapter records, commit, and report only after authorized work is
  complete.

Apply-now authorization covers deterministic alignment and any per-item decisions
the user actually supplied. It does not choose favorite models, promote a
tool-local capability, enable a connector, broaden permissions, or resolve another
material choice by implication.

## Required Reads

- `../../INDEX.md`
- `../../AGENTS.md`
- the workspace mission spec (`specs/agents-workspace/mission.md`)
- `../../adapters/AGENTS.md`
- `../../adapters/adapter-contract.md`
- `../../adapters/INDEX.md`
- `../../capabilities/AGENTS.md` and `../../capabilities/connectors.md`
- `../../conventions/autonomous-task-permissions.md` before permission bootstrap
- `../../roles/task-worker-tiers.md`
- the target tool's mapping doc and divergence ledger, when they exist
- relevant `../../skills/`, `../../roles/`, and `../../workflows/` entries as needed

## Core Principle: exhaustive, bidirectional, never silenced

Reconciliation MUST enumerate every difference between the workspace and the tool
in BOTH directions and drop nothing:

- **workspace -> tool**: workspace skills, roles, worker tiers, capabilities,
  connectors, and workflows that have no expected native entry (`missing-in-tool`).
- **tool -> workspace**: anything the tool supports that the workspace does not —
  a skill, role, tier, MCP/connector, permission posture, or behavior
  (`missing-in-workspace`).

An empty diff is a positive claim ("N differences found, all classified"), not an
omission. Every tool-side extra MUST be either **promoted** into the workspace or
**recorded as an approved divergence** in the tool's divergence ledger; there is no
silent third state. Approved divergences MUST be re-surfaced on every run,
annotated `user-approved <date>, expected` — acknowledged, never silenced. See the
mission spec corollary and the contract's Drift Categories.

## Inspection Targets

Inspect native tool files only when available and in scope:

- global or project instruction entrypoints
- skill wrappers and skill discovery paths
- role, subagent, or custom-agent wrappers
- worker model-tier wrappers and their current native model/settings choices
- frontier orchestrator default/fast mappings
- one-run role-profile launch, model/reasoning/service controls, structured
  capture, identity verification, process ownership, and concurrency limits
- command or prompt shortcuts, including adapter lifecycle operator entrypoints
- capability and MCP/connector references
- permissions, approval settings, hooks, and policy wrappers
- stale paths to moved or deleted Agents workspace files

## Procedure

1. Identify the target tool, the mode (onboard vs reconcile), and the authorization
   mode (apply now, review first, or audit only). Complete any explicitly
   authorized permission bootstrap first, then enter read-only Phase 1; no other
   edit is allowed before the full audit is complete.
2. Determine which native concepts the tool supports: instructions, skills,
   roles/subagents, commands, capabilities, MCP/connectors, permissions, hooks,
   plugins, and verification.
3. Build a small inventory of workspace source-of-truth entries relevant to the
   tool, and a matching inventory of native/adapter entries.
4. Diff both directions and classify every difference with a contract category
   (`missing-in-tool`, `missing-in-workspace`, `stale`, `duplicated`,
   `intentionally-divergent`). Do not drop anything.
5. **Worker tiers**: read `../../roles/task-worker-tiers.md` first, then compare
    native wrappers against the required six-cell matrix. Every cell MUST be
    recorded as present, disabled, or unsupported-with-reason. A disabled mapping
    must refuse launch. A cell with no decision is `missing-in-tool` drift.
    **Model choices come from `../../ai-models/delegation-briefing.md` (section 3,
    this tool's table), not from the user's last pick or the old adapter.** Any
    native model or effort that differs from the briefing is `stale` drift. A
    "pending sync" row there is an already-made user decision: apply it, check it,
    and flip that row's status to live. If a native wrapper can carry a short
    description that the root sees at dispatch, put the model's one-line cost and
    trust note there. If the user wants a different model, change the briefing
    first (its section 8), then the native files. Before applying a model the
    briefing's card says is a poor fit for that role, show the user the card.
    **Every model change behind `task-explore`, `task-execute`, their high
    versions or `task-orchestrator` also updates this tool's six-line block in
    briefing section 3** (how the tiers compare, regular takes, never give
    regular, move up to high when, give back to the root when, how much to
    delegate) and checks that each worker model's card ends with a "Tell the
    worker" line. Do this in the same run, even when the model change came from
    the briefing. Also check it on every run: a missing or stale block, or a
    block that disagrees with the native files or the live check, is `stale`
    drift. Each native worker description must point the root to this tool's
    part of briefing section 3 rather than carry its own capability rules.
6. **Frontier orchestrator mappings**: record both `task-orchestrator` and
   `task-orchestrator-fast` as present, disabled, or unsupported-with-reason.
   Normal orchestration requires a verified tool-specific mapping; fast remains
   disabled unless the user explicitly changes the canonical tier guidance.
7. **One-run role profiles and mandatory preference interview**: make RoleDispatch
   freedom concrete for this harness. Determine whether adapter-maintained roles can
   be launched once with an explicit model, reasoning level, and service class.
   Inventory native per-dispatch overrides, headless/inline launch, temporary
   profile mechanisms, role-mode constraints, exact model discovery and launch
   commands, structured capture, session/profile verification, timeout and
   cancellation, permission preservation, and independent parallel execution. The
   Phase 1 report MUST state:
   - every maintained role the path can select;
   - the exact model-discovery command and the relevant current candidates, kept to
     a useful shortlist rather than an encyclopedic roster;
   - the user's current favorite model subset, exact harness IDs, and confirmation
     date, or a clear `needs your decision` gap;
   - exact CLI/API flags or native controls for model selection, reasoning, standard
     service, fast/priority service, working directory, output, and cancellation;
   - unsupported combinations, provider-default behavior, and fail-closed rules;
   - which favorite profiles are roster-only, preflight-verified, or live-verified.
   On onboarding, or whenever any field is absent, stale, unverified, or affected by
   a changed roster/CLI, ask the user which models they favor, their default
   reasoning, whether fast/priority is opt-in, and which small read-only smokes to
   run. Never infer these preferences. Record them only in this tool's mapping
   during an authorized Phase 2. If the tool cannot preserve the selected role and
   permissions, mark the path unsupported; do not inherit, substitute, or use a
   generic agent.
8. **Connectors/MCP/plugins (exhaustive decision loop with UNAMBIGUOUS scoping).**
   Inventory the harness's native MCP servers AND non-MCP bridges
   (plugins/extensions), then reconcile the UNION of (a) every connector in the
   harness's native config and (b) every curated connector in
   `../../capabilities/connectors.md`. In EVERY line name the place precisely using
   the contract Scope Labels — never a bare "globally" that could mean the workspace
   OR the harness:
   For browser/desktop work, also inventory built-in browser tools, CLI/library
   bridges, provider APIs and desktop drivers against the registry's **awareness**
   section and `../../skills/browser-use/SKILL.md`. Record the effective browser
   identity, connection mode, login availability, permissions and verification tier
   for each route. Awareness-only entries are not missing installations and do not
   trigger automatic setup; selected routes follow the linked onboarding guide in
   this harness only. Curated browser MCPs stay configured default-off unless a
   dated decision enables a specific route. A synced skill, MCP discovery, or CDP
   listener does not prove signed-in control: use a harmless actual tool call,
   account-only readback when approved, and owned-tab cleanup before reporting it.
   - **global agents workspace registry** = the tool-agnostic curated set in
     `capabilities/connectors.md` (not the harness).
   - **global `<harness>`** = this harness's user/global native config
     (e.g. global Cursor `~/.cursor/mcp.json`).
   - **`<harness>` current project (`<repo>`)** = this harness's project/repo-scoped
     native config (e.g. `<repo>/.cursor/mcp.json`), when the current folder has it.

   Report connectors in the same three-place layout as every other area (see Report
   Shape): a "From the global agents workspace registry" list with each curated
   connector's status in global `<harness>` and, when applicable, in `<harness>`
   current project; an "Only in global `<harness>`" list; and an "Only in
   `<harness>` current project" list. The A/B/C/D grouping below is the internal
   diff aid that produces those lists; it is not the report layout.

   Before the normal four-bucket decision loop, compare native entries with
   canonical retired-interface policy. A retired entry is `stale` and
   removal-required in this tool's own authorized Phase 2; do not classify it as a
   curated default-off connector or a promotable/keep-local extra. In a normal
   sync, report its removal and named replacement as required in Phase 1. Remove,
   align, reload, and verify in Phase 2 only when apply-now authorization or later
   review-first confirmation covers that migration. In audit-only mode, report the
   migration as pending.

   The four internal buckets for non-retired entries (drop nothing; they feed the
   three-place lists above):
   - **A. In the global agents workspace registry AND configured in global
     `<harness>`** — note each connector's posture (on, or configured but
     default-off). Compare the harness's current on/off state to the registry's
     expected default posture. If the registry says configured default-off but
     global `<harness>` has it enabled, that is drift unless a dated user-approved
     enablement decision exists in the harness reminder ledger.
   - **B. In the global agents workspace registry but NOT configured in global
     `<harness>`** — surface each as add-or-decline (the run should try to wire
     curated connectors, default-off, unless a documented incompatibility blocks it).
     When the registry marks a connector **default-on** with a dated user
     decision and links a setup guide, wire it on as part of the apply set,
     following that guide's section for this harness (or its generic adoption
     checklist), including permission gates and built-in tool switches. If the
     harness cannot meet a requirement the guide marks as required, ask
     instead of adding.
   - **C. Configured in global `<harness>` or `<harness>` current project but NOT in
     the global agents workspace registry** — surface each as promote-or-keep-local.
   - **D. Previously decided** — re-list from the harness reminder ledger with the
     decision date as a **reminder only; do NOT re-ask it as an action item**.

   Decision vocabulary for A/B/C items (per-item, never auto-promote/auto-enable):
   `enable` / `keep-configured-default-off` / `disable` / `remove` /
   `decline-to-add` / `promote` / `keep-local`. **`default-off` means keep the
   connector present in native config and merely toggle it off — it MUST NOT mean
   deleting the connector from config.** Removing a connector the user wants is
   drift, not the default-off posture.

   Record auth expectation per connector (browser-OAuth connectors need a per-tool
   login/`mcp auth` step; see the registry's Authentication Expectations). Apply
   config edits ONLY during an authorized Phase 2, and record every decision in the
   tool's divergence ledger so it re-surfaces next run as a reminder.
9. **Connector availability only; no role-MCP reconciliation.** Reconcile
   connectors against tool/session/project scope and skill dependency hints, but do
   NOT inspect, generate, or preserve per-role or per-subagent MCP scoping records.
   If an existing tool doc, divergence ledger, or native wrapper still contains
   role-level MCP customization, classify it as stale and remove it during that
   tool's own sync without creating a replacement record.
10. For every tool-side extra (connector, plugin, skill, role, tier, behavior),
   surface it individually and let the user decide: promote, decline, or
   keep-local. Never assume promotion. Default to keep-local. Record every
   decision (approved / declined / keep-local) in the tool's divergence ledger with
   the decision date so it re-surfaces as a reminder next run.
11. Finish Phase 1 with the complete audit and one exact change/verification list.
    In review-first mode, include the RoleDispatch preference questions, ask for
    confirmation, and stop. In audit-only mode, report and stop. In apply-now mode,
    state a concise apply set, continue with every resolved item, and defer only
    genuinely missing choices.
12. Enter Phase 2 only with apply-now authorization or later review-first
    confirmation. Edit only
    in-scope adapter or native files. Keep native
    wrappers thin and pointed back at workspace source files. Preserve role,
    permission, and tier boundaries. Never edit another tool's native config in this
    run (Single-Tool Boundary): a limitation found here is recorded in THIS tool's
    docs only; other tools address the same workflow requirements on their own runs.
13. Update the tool mapping doc, the divergence ledger, and `../../adapters/INDEX.md`
    (status, supported surfaces, last-checked) when adapter status changes.
14. Verify stale paths are gone, wrappers remain thin, and boundaries are
    preserved. For every shared or native skill wrapper, confirm it contains only
    discovery metadata plus canonical-file loading instructions. For every native
    operator command, confirm it adds only target identity, canonical loading, and
    unmodified current-request arguments. For every native role wrapper, confirm
    it contains only native identity/model/tier/sandbox settings plus
    canonical-file loading instructions. Copied authorization, classification,
    packet, behavior, stop, report, privacy, or connector rules are `duplicated`
    drift.

## Per-Tool Mapping Doc Skeleton

Onboard mode creates, and reconcile mode maintains, a mapping doc with these
mandatory sections (see the contract for details):

- Native surfaces
- Source mapping (workspace concept -> native concept)
- Worker tier matrix (the six cells, each present or unsupported-with-reason)
- Frontier orchestrator mappings (normal and fast, each present or
  unsupported-with-reason)
- One-run role profiles (goal, selectable roles, discovery command, dated favorite
  model subset, exact reasoning/service/fast controls, launch commands,
  verification status, concurrency, and limitations)
- Connectors / MCP inventory (native servers <-> `capabilities/connectors.md`)
- Permissions and unattended execution (persistent defaults, exact bypass/sandbox
  flags, copyable remote launch, role/tool inheritance, child controls, reload
  needs, actual verification status and unsupported/human-only limits)
- Drift checks

The approved-divergence ledger lives in a separate `adapters/<tool>.divergences.md`.

## Output

Report using the **Report Shape** and **Scope Labels** from the contract. Plain
English only: no status codes, no verdict tables, and none of the words "matrix",
"ledger", or "drift" in the user-facing report. The shape is:

1. A one-paragraph **current state summary**: which harness, onboard or reconcile,
   when it was last synced, and the headline of what is and is not aligned.
2. **One heading per area**, in this order: Instructions, Skills, Roles and
   subagents, Worker tiers and models, Frontier orchestrator, One-run role profiles,
   MCP connectors, Commands and entrypoints, Permissions and policies. Inside each
   heading use up to three separate bullet lists, each stating whose point of view
   it takes:
   - **From the global agents workspace** — one bullet per source-of-truth item,
     with nested bullets for its status in **global `<harness>`** and, when the
     current folder has its own config, in **`<harness>` current project (`<repo>`)**.
     Each nested bullet is one or two plain sentences: present or not, matching or
     not, and since when if aligned.
   - **Only in global `<harness>`** — harness-global items the global agents
     workspace does not define, each with the standing choice (kept on purpose,
     promoted, or waiting on a decision).
   - **Only in `<harness>` current project (`<repo>`)** — the same, when applicable.
   - Write "none" for any empty list; never omit one silently.
3. A closing **Summary of changes and recommendations**, grouped by the same area
    names. Each item states, in plain words: what the change is, the current state,
    the recommendation, and whether it "needs your decision" or is "safe to apply".
4. In review-first mode, an exact **Proposed apply set** followed by one explicit
   confirmation question, then stop. In apply-now mode, give a concise apply set
   before editing and an exact applied/skipped set in the final report. In
   audit-only mode, report findings without an apply question.

The report must still carry every fact the contract's Adapter Output Expectations
list requires: harness and mode; global agents workspace roots and native files
read; the six worker tier cells with model/settings; the normal and fast
orchestrator mappings; one-run role-profile support with exact launch and
verification paths, preferred profiles, concurrency limits, and unsupported cases;
the RoleDispatch favorite-model confirmation date, exact selected IDs, reasoning
and fast/priority syntax, and per-profile verification status;
the full connector picture by place with per-connector auth expectations
(browser-OAuth connectors need a per-tool login step); prior decisions repeated as
dated reminders; unsupported or manual items; and what was applied or proposed and
how it was checked.
