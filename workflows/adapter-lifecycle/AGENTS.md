# Adapter Lifecycle

Use this workflow package for platform-agnostic adapter initialization and drift
alignment. It tells an agent how to connect an AI runtime to the Agents
workspace without making that runtime's native config canonical.

## Workflows

- `sync-tool.md`: onboard or reconcile a tool adapter against Agents workspace
  source-of-truth roots via one exhaustive, bidirectional, ledgered comparison.
  Onboarding is reconciliation from an empty adapter (onboard vs reconcile mode);
  it replaces the retired separate `init-tool.md` and `align-drift.md`.

## Rules

- Keep the Agents workspace tool-agnostic.
- Every run starts with a read-only audit. A clear current-message instruction to
  apply the changes now authorizes the run to continue from that audit into edits
  without asking again. Without that instruction, report the exact apply set and
  wait; explicit audit-only requests report and stop without an apply question.
- Prefer adapter docs and thin wrappers over copied source-of-truth text.
- Use `../../adapters/adapter-contract.md` as the baseline.
- Keep `../../adapters/INDEX.md` current when an adapter is onboarded,
  materially repaired, or retired. Do not create full manifests unless the user
  explicitly asks for machine-readable adapter inventory.
