---
doc_type: state
updated_at: 2026-10-05
status: active
scope: OpenCode V2 as a CLI bridge for other AI harnesses
related:
  - path: ./cli.md
    why: Start here for commands, model selection, costs, permissions, and verified behavior.
  - path: ./sessions.md
    why: Read when monitoring, resuming, answering a question, or cancelling a child run.
  - path: ../../skills/task-opencode/SKILL.md
    why: Procedure for an authorized bounded delegation from a non-OpenCode harness.
---

# OpenCode CLI bridge

OpenCode V2 can run bounded tasks from another harness with `opencode run`.
Use [cli.md](cli.md) for the working reference and [sessions.md](sessions.md)
for supervision. The caller retains responsibility for scope, cost, approvals,
and checking the result. This is not an MCP connector or a sandbox.

The commands below were checked against local `opencode v2.0.19` on
2026-09-29. Model availability, prices, tool permissions, and server API
responses depend on the location and can change. The skill is already mapped
in Claude Code and Codex; it is not a self-delegation shortcut inside OpenCode.
No other harness configuration is changed by these docs.

On 2026-10-05, OpenCode 2.0.22 completed overlapping parent/native-child work.
Exact-session readback exposed parent linkage, runtime, token/cost counters and
message/tool timestamps. CLI step events undercounted final root cost; use the
[session accounting recipe](sessions.md#parentchild-metrics-and-benchmarks).
The dated experiment (private, not published)
verified stored child readback, not live child subscriptions, cancellation or
crash recovery. No collector or automatic benchmark runner was installed.
