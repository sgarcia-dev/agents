---
name: sync-tool-adapter
description: Onboard or reconcile a tool adapter against the portable Agents workspace source of truth via exhaustive, bidirectional comparison. Use when onboarding a new tool (OpenCode, Codex, Claude Code, Cursor, Copilot, ...) or checking/repairing an existing adapter for drift in either direction.
created_at: 2026-07-07
updated_at: 2026-10-07
model: gpt-5.6-sol
doc_type: skill
purpose: Provide a single reusable entrypoint for onboarding and reconciling tool adapters, replacing the separate init and align entrypoints.
related:
  - path: ../../workflows/adapter-lifecycle/sync-tool.md
    why: Full workflow procedure for onboarding and reconciling a tool adapter.
  - path: ../../adapters/adapter-contract.md
    why: Platform-neutral adapter contract, directional drift categories, and reconciliation ledger this skill follows.
---

# Sync Tool Adapter

## Permission bootstrap first

Read `~/agents/conventions/autonomous-task-permissions.md` before
onboarding or reconciliation. When the current request authorizes applying that
policy, first complete its focused, own-harness permission inspection and apply
step; do not wait for the exhaustive adapter audit or model interview. That
small bootstrap is separate from the read-only full audit below. A permission-only
request follows the bounded policy procedure and does not start an exhaustive
sync. No new consent round for already-authorized routine rules; preserve child
limits and document unsupported/human-only controls. Every maintained adapter
must record persistent defaults and exact unattended/all-access flags, including
what those flags cannot bypass. Mere skill discovery remains read-only.

Follow `../../workflows/adapter-lifecycle/sync-tool.md` to onboard or reconcile an
AI tool adapter against the Agents workspace. Onboarding is reconciliation from an
empty adapter; both modes share one exhaustive, bidirectional comparison.

Write the report in plain English using the contract's **Scope Labels** and
**Report Shape** (`../../adapters/adapter-contract.md`): a one-paragraph current
state summary, one heading per area, and inside each area up to three separate
lists (from the global agents workspace; only in global `<harness>`; only in
`<harness>` current project), then a closing changes-and-recommendations list.
Every line names exactly one place: **global agents workspace** (agent-agnostic
source of truth), **global `<harness>`** (the harness's user-level config, e.g.
global Cursor), or **`<harness>` current project (`<repo>`)** (the harness's config
for the current folder). Never write a bare "workspace" or "globally", and keep the
words "matrix", "ledger", and "drift" out of the user-facing report.

Reconcile exactly ONE tool per invocation — the tool running you. Never inspect,
migrate, or edit another tool's native config in the same session; "align all my
tools" is one run per tool, each in that tool's own runtime (see the contract's
Single-Tool Boundary).

Keep the Agents workspace (skills, roles, capabilities, connectors, workflows,
specs, changes, projects, artifacts) as the source of truth, and keep native tool
config a thin, replaceable implementation detail. Enumerate every difference in
both directions: nothing dropped. Promotion of anything upstream (an MCP, skill,
role, connector, tier, or behavior) is an explicit per-item user decision, never
automatic; the default disposition for a tool-side extra is to leave it tool-local
and record it. Surface every candidate for a user decision each run; re-surface
prior decisions (including declines) as reminders.

Every invocation is audit-first, but not every invocation requires two user turns.
Resolve authorization from the current request:

- `apply-now`: the user clearly directs you to apply, fix, update, or complete the
  adapter changes now, or explicitly says not to stop for another approval. Finish
  the read-only audit, state a concise apply set, then continue directly into the
  authorized edits and verification in the same invocation.
- `review-first`: there is no clear current-message authorization to write. Finish
  the audit, present the full report and exact proposed apply set, ask one
  confirmation question, and stop.
- `audit-only`: the user explicitly requests inspection without changes. Report
  and stop without an apply question.

Explicit authorization is semantic, not a magic phrase and not restricted to a
second reply. A bare skill invocation, "check alignment", or old standing
permission is not `apply-now`. Phase 1 itself is always read-only: do not edit
native config, shared wrappers, adapter docs, the registry, or canonical workspace
files until the audit is complete.

`apply-now` covers deterministic in-scope alignment and any per-item decisions the
user actually supplied. It does not authorize guessed model preferences,
connector enablement, promotion into the global agents workspace, permission
broadening, or unrelated scope. Apply the resolved subset and leave genuinely
undecided items untouched with concise questions. Retired-interface migrations
use the same authorization modes.

Whenever the model or effort behind `task-explore`, `task-execute`, their high
versions or `task-orchestrator` changes, the same run must also update this
tool's six-line block in section 3 of
`~/agents/ai-models/delegation-briefing.md` (how the tiers
compare, what each takes, how much to delegate). The workflow's worker-tier
step has the details. A run that changes a worker model without that block is
not done.

The workflow's frontier-orchestrator and one-run role-profile passes are
mandatory. Record normal/fast orchestrator mappings and whether the active tool
can launch maintained roles once with explicit model, reasoning, and service
settings while preserving permissions. The audit must inventory selectable roles,
the exact model-discovery and launch commands, reasoning controls, standard and
fast/priority controls, cancellation/capture/verification, and unsupported cases.
On onboarding, or when the preference record is missing or stale, ask the user for
a small favorite model subset, defaults, fast/priority posture, and selected live
smokes. Never infer them or dump the full model catalog. Exact model names,
confirmation date, and verification status remain in this tool's mapping;
unsupported paths must be stated rather than replaced by inherited or generic
agents.

For connector/MCP reconciliation, report both configuration coverage and exact
on/off posture. Curated Agents workspace connectors are expected to be configured
default-off in the target tool unless a dated per-tool enablement decision exists;
default-on without that decision is drift to surface before repair. Exception: a
connector the registry marks default-on with a dated user decision is expected
on in every tool; add it in the apply set by following its linked setup guide,
and ask instead when the tool cannot meet that guide's required gates.

The browser and desktop **awareness-only** entries in
`../../capabilities/connectors.md` are not maintained MCP install requirements:
inventory native browser/desktop/CLI/API routes and their effective login identity,
then link the shared `../browser-use/SKILL.md` and its onboarding reference in the
target adapter. Do not install optional software, inject credentials, or enable a
signed-in attachment just because it appears in the registry. For curated
default-off browser MCPs, configure the supported disabled entry in that tool
without assuming access to an existing login; activating a signed-in mode needs
a dated owner decision and a real account-only smoke in that tool's session.
Canonically retired interfaces are removal-required, but the audit must name the migration
before applying it. In `apply-now` mode, continue after the audit without a second
approval; in `review-first` mode, wait for confirmation. When the retired
interface names a replacement, align and verify that replacement in the authorized
Phase 2. Remove retired entries and verify any replacement through the active
tool's direct integration. Do not preserve or invoke retired bridges; verify
direct, non-recursive integrations where applicable.
