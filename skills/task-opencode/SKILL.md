---
name: task-opencode
description: Use from a harness other than OpenCode when the user wants to send a bounded task to OpenCode CLI, use its models or skills, monitor a headless run, or resume an OpenCode session. Do not use from inside OpenCode itself; use native tools/subagents there. Do not silently turn a request for normal local work into an OpenCode delegation.
created_at: 2026-09-28
updated_at: 2026-10-07
model: openai/gpt-6-sol
doc_type: skill
purpose: Safely dispatch and supervise a bounded OpenCode V2 CLI task from another harness.
metadata:
  opencode/autoinvoke: false
related:
  - path: ../../capabilities/opencode/cli.md
    why: Maintained V2 command, model, cost, permission and verification reference.
  - path: ../../capabilities/opencode/sessions.md
    why: Monitoring, questions, cancellation and resuming a child.
---

# Task OpenCode

**Explicit user request only.** Loading this skill never authorizes a handoff.
Read `~/agents/conventions/autonomous-task-permissions.md` for the
owner-approved non-interactive defaults, routine roots, enabled MCP preapproval,
and high-risk exceptions. Preserve the bounded packet and child-depth limits.

Use only when running in a harness other than OpenCode. If running inside
OpenCode, stop and use native tools or supported native subagents instead. This
skill is a procedure, not permission to install a wrapper in every harness.

Read `~/agents/capabilities/opencode/cli.md` and its session guide
before invoking CLI commands. Preflight `opencode --version` and
`opencode run --help` because the V2 command surface can change. Work in the
intended checkout. For a task bound to a repository, confirm its identity, branch,
and initial status. Give OpenCode one bounded packet: goal, allowed edits, excluded
paths, output, tests, decision points, and stop condition. Ask the child to print `PROGRESS n/total` (for example `PROGRESS 2/5`) as it finishes each step; the agent-watch Claude Code mod reads it to show progress and time left. Pass only necessary
context; CLI sessions do not inherit the parent conversation.

Read [`delegation-briefing.md`](../../ai-models/delegation-briefing.md)
first: section 4 for the OpenCode default and step-ups, section 5 for the model's
card (Go request limits cap how many to run; Muse Spark never gets private
files). Do not choose from memory. Choose an exact available `provider/model#variant` from the current
location's catalog. Favor a current user preference when appropriate. If a model
is unavailable or rate limited, fall back only within the same row of the briefing's fallback table
and report the switch; do not substitute silently. Use `--agent` only
for a verified primary agent; a subagent name may fall back to the default. Use
the guide's JSON capture recipe for unattended or auditable runs.

**Claude models.** OpenCode also exposes Claude through the `claude-code`
provider, as `claude-code/<model>#<effort>` (a 1M-context Opus ID has
brackets, so quote it). Reasoning levels are
`low`, `medium`, `high`, `xhigh`, `max`. Claude spends the scarce Claude quota:
pick the model and effort from the briefing's Claude Code bridge row, and use
anything above that row's default only when the user explicitly approves it.
On a `provider.quota` error, stop and report. Details:
`~/agents/capabilities/opencode/cli.md`.

**Subagents are off by default.** Follow the CLI child rule in
`~/agents/roles/task-worker-tiers.md`. Block them technically with
`OPENCODE_CONFIG_CONTENT='{"permissions":[{"action":"subagent","resource":"*","effect":"deny"}]}'` plus
`opencode run --standalone` (the override is ignored by the shared service
without `--standalone`). This V2 shape was checked by loading the private
server's config; a live subagent-denial run with the corrected syntax is still
unverified. Verify it before large fan-out. Say in the packet that the run is
one worker that must not delegate. Allow subagents only when the user approved
it or the packet asks for a skill that
needs them, and then state the maximum count. Never use `task-claude` or
`task-codex` from the child unless the user asked for that chain.

For many small read-only checks, follow the capability's parallel guidance:
one short packet per run, separate logs, and the caller merges and checks the
answers.

Default to full permissions with `--auto`, so a headless run never stops
for approval (user decision, 2026-09-30); it cannot bypass explicit denials.
Use ordinary permissions only when the user asks or the permission convention
identifies concrete high-risk work. Do not use it to emulate a RoleDispatch role profile, alter
another tool's native config, or enlarge the user's task scope. Set a timeout,
retain the process handle, and keep stdout and stderr separate. Monitor events,
session status, pending forms and permissions. Route clarifying questions back to
the human or calling root; do not invent answers. If interactive reply is not
safe, stop and resume the same session later rather than restarting blindly.
For parent/child monitoring or benchmarks, follow the session guide's
[accounting recipe](../../capabilities/opencode/sessions.md#parentchild-metrics-and-benchmarks).
Use completed session counters for each session, not sums of possibly incomplete
CLI step events; measure whole-task wall time independently.

On completion or interruption, inspect the session result, output files, and
repository diff. Report the selected model/variant, agent, session ID, completion
status, edits/tests, open questions and next action. A child run is not accepted
just because its CLI process exited successfully.
