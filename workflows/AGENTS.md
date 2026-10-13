# Workflows

Use this folder for portable process documents that can be reused across tools
and repositories.

## Belongs Here

- Review-diff checklists.
- Bug localization methods.
- Safe refactor checklists.
- `spec-workflow/`: canonical OpenSpec-inspired durable workflow for new
  serious agent-assisted work.
- `adapter-lifecycle/`: platform-agnostic workflow for onboarding and reconciling
  tool adapters against Agents workspace source-of-truth roots (`sync-tool.md`).
- `model-bakeoff/`: portable model comparison workflow for benchmarking
  adapter-resolved contestants on the same task.

## Does Not Belong Here

- Tool-specific slash commands.
- Agent runtime config.
- Canonical reusable skills or roles. Use `../skills/` and `../roles/`.
- Repo-specific implementation plans.

## Current Guidance

Use `spec-workflow/` for new serious work that needs restartable planning,
scoped changes, delegated workers, verification, or memory reconciliation. Its phase
procedures live in `../skills/`, and its worker role contracts live in
`../roles/`.

Use `adapter-lifecycle/` when a tool needs to onboard itself against the Agents
workspace or reconcile differences in skills, roles, capabilities, connectors,
worker tiers, workflow entrypoints, stale paths, or native wrappers. Onboarding
and drift alignment are one workflow (`sync-tool.md`): onboarding is
reconciliation from an empty adapter. The older task-folder and sharded-handoff
workflow trees were retired; only historical records should still mention them.

Use `model-bakeoff/` when comparing models across tools or IDEs. The workflow
defines the benchmark contract, isolation, timing, scoring, and cleanup, while
tool adapters resolve native model names and temporary runtime config.
