# Roles

Use this folder for portable reusable specialist behavior. A role defines who
should perform or review part of a workflow. A tool may implement a role as a
native subagent, custom agent, prompt wrapper, command, or instruction bundle.

## Belongs Here

- Cross-tool specialist behavior such as read-only exploration, bounded
  execution, model bake-off contestants, CI diagnosis, review, security review,
  testing, or documentation writing.
- Role boundaries, allowed actions, authority limits, forbidden actions, stop
  conditions, and output shapes.
- Worker behavior that can be reused by multiple workflows.

## Does Not Belong Here

- Step-by-step reusable procedures. Use `../skills/`.
- Tool-native subagent, custom-agent, or permission config. Use `../adapters/` to
  describe how a tool maps this role into its native format.
- One-off delegated work packets. Use a change folder's `subtasks/` and
  `results/` directories.

## Current Guidance

The canonical spec-workflow worker roles are listed in
`task-worker-tiers.md`, which is the sole authority for their availability,
selection, packet size, and concurrency. Do not infer that a retained role file is
enabled.

Current retained role contracts are:

- `task-explore.md`: source-read-only bounded discovery, review, and verification;
  it may create new Markdown reports in one packet-assigned output directory.
- `task-explore-high.md`: enabled bounded moderately complex exploration overlay.
- `task-execute.md`: bounded mutation for exactly one explicit packet.
- `task-execute-high.md`: enabled bounded moderately complex execution overlay.
- `task-worker-tiers.md`: availability, small-packet limits, concurrency budget,
  and portable wrapper semantics.
- `task-orchestrator.md`: bounded orchestration contract. Dispatch only through
  an explicitly mapped and verified adapter, subject to tier guidance.

The canonical model bake-off contestant role is:

- `model-bakeoff-contestant.md`: isolated benchmark contestant behavior for
  adapter-resolved model comparison runs.

These roles are portable source-of-truth contracts. Tool-native subagent files
must be treated as adapters around these roles, not independent definitions.

## MCP Neutrality

Roles are portable behavior contracts, not per-role connector/MCP permission
surfaces. Do NOT declare individual connector grants, per-role MCP settings, or
native scoping requirements in role frontmatter or body text.

Rules:

- External connector inventory and default posture live in
  `../capabilities/connectors.md`.
- Tool adapters reconcile connector wiring only at tool/session/project scope, not
  per role or subagent.
- Generic safety boundaries still belong here (for example read-only vs mutation,
  sandbox limits, forbidden actions, or escalation conditions).
