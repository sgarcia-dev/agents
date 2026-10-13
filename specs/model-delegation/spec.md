---
created_at: 2026-10-01
model: claude-opus-5-5
doc_type: spec
purpose: Define who owns model choices for every kind of delegation, how agents must use them, and how changes reach each tool without drift.
related:
  - path: ../../ai-models/delegation-briefing.md
    why: The single source of model choices, labels, cards and field notes.
  - path: ../../roles/task-worker-tiers.md
    why: Worker roles, packet rules and the count rules that read the briefing's labels.
  - path: ../../workflows/adapter-lifecycle/sync-tool.md
    why: How one tool applies the briefing to its native files.
  - path: ../../adapters/adapter-contract.md
    why: Single-tool boundary and adapter duties.
---

# Model Delegation Spec

Agents delegate work to other models all the time: native workers, orchestrators,
CLI bridges to other tools, Hermes subagents, web-search helpers. Before
2026-10-01 each tool, skill and memory kept its own idea of which model to use
and how many workers to run. Those copies drifted, and agents launched workers
knowing only a model name, not what that model is bad at.

This spec makes one file the source of model choices and requires every
delegating agent to read it.

## Start Here

- Choices and trade-offs: `ai-models/delegation-briefing.md`.
- Worker roles, packet size, count rules: `roles/task-worker-tiers.md`.
- Applying a change to a tool: `skills/sync-tool-adapter`, one tool per session.

## Scope

Every route by which an agent hands work to a model other than itself:

- native workers (`task-explore`, `task-execute`, their high versions);
- `task-orchestrator`;
- CLI bridges: `task-codex`, `task-claude`, `task-opencode`, `task-gemini`,
  `task-hermes`;
- Hermes `delegate_task` subagents and any other tool-native subagent;
- web-search helpers and hand-offs;
- any future route (mixture-of-agents, cron agents, background agents).

Out of scope: how to collect benchmark data (`ai-models/collection/`), and which
model a human chooses for their own interactive session.

## Ownership

| What | Owner | Others may |
|---|---|---|
| Which model and effort each role or route uses | `ai-models/delegation-briefing.md` | point to it |
| What each model is good and bad at, its labels | the briefing's model cards | point to it |
| Real-world model failures | the briefing's field notes | point to it |
| Roles, packet size, count rules (model-blind) | `roles/task-worker-tiers.md` | point to it |
| How a tool wires a model (file paths, flags, live-check evidence) | that tool's adapter in `adapters/` | |
| Launch procedure and flag syntax | each `task-*` skill | |
| The live setting | each tool's native files | must match the briefing |

## Requirements

**R1. One source.** Only the briefing chooses or recommends a model or effort
for delegation. Benchmark numbers come from `ai-models/data/<date>/`.

**R2. No copies.** Skills, capabilities, adapters, roles, prompts, tool memories,
tool-local skills and personas must not restate a model choice as current
guidance. They may show flag syntax with values marked as coming from the
briefing, keep dated history, or record live-check evidence. A tool-local file
whose only job was model advice becomes a one-line pointer or is deleted.

**R3. Informed dispatch.** Before any delegation, the dispatching agent reads its
harness's section and the chosen model's card, and decides packet size, worker
count, how hard to check results, and whether to tell the user a different route
is better. Launching from a model name alone is a failure.

**R4. Counts follow the model.** Worker counts come from the briefing's labels:
cost sets how many, guessing sets which packets are allowed, speed sets
deadlines, quota caps override. An explicit user count still wins.

**R5. Orchestrator step.** An orchestrator runs one step above its harness's
high workers, never on the most expensive setting.

**R6. Visible status.** Each briefing row shows whether the tool's native files
match ("live", with how it was checked) or not yet ("pending sync").

**R7. Change path.** To change a model: edit the briefing row and card first,
mark it pending sync, then run `sync-tool-adapter` in each affected tool's own
session. That run treats any native setting that differs from the briefing as
drift, applies the row, live-checks it and marks it live.

**R8. Dispatch-time note.** Where a tool shows worker descriptions to the root at
dispatch, each description carries a one-line model, cost and trust note kept in
step with the briefing on every sync.

**R9. The user's experience counts.** When the owner reports a model letting them
down, record it as a dated field note even if benchmarks disagree.

**R10. Privacy.** A model whose data is used for training (Muse Spark
Contributor) never sees private files and is never a tool's global subagent model.

**R11. No silent fallback.** An unavailable model is reported. Fallback is only
within the same row of the briefing's fallback table, once, and announced.

**R12. Single-tool boundary.** No session edits more than one tool's native
configuration. Aligning N tools is N sessions.

## Verification

Run these from `~/agents`. Each should return only history,
evidence, flag syntax marked as from the briefing, or the briefing itself.

```sh
grep -rn -i -E "luna|gpt-6|sonnet|opus|glm|mimo|muse|deepseek|qwen|kimi|gemini-3" \
  skills capabilities roles workflows conventions prompts adapters AGENTS.md \
  | grep -v -E "^[^:]+:[0-9]+:model:"
grep -rn "delegation-defaults" --exclude-dir=artifacts --exclude-dir=changes --exclude-dir=.git .
grep -n "pending sync (live" ai-models/delegation-briefing.md
```

Each tool's own sync run also compares its native files against the briefing.

## History

- 2026-10-01: created. `delegation-defaults.md` became `delegation-briefing.md`;
  Claude Code, Codex, OpenCode and Hermes synced in their own sessions. Hermes
  local skills were left for a Hermes-run cleanup.
