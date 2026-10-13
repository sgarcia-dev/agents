---
name: task-hermes
description: Use when delegating a bounded task to Hermes Agent.
created_at: 2026-09-29
updated_at: 2026-10-07
model: openai-codex/gpt-6.1-sol
doc_type: skill
purpose: Dispatch and verify a scoped Hermes task from another agent harness.
metadata:
  opencode/autoinvoke: false
related:
  - path: ~/agents/capabilities/hermes.md
    why: Route choice, models, capability menu and access limits.
  - path: ~/agents/capabilities/hermes/STATE.md
    why: Dated verification and known failures.
---

# Task Hermes

## When to Use

Use from Claude Code, Codex, OpenCode or another caller when the user requests
Hermes, or has explicitly authorized a workflow that delegates to it. Good
reasons include Hermes's browser routes, Mac tools, persistent context, research,
artifact creation, messaging or scheduled work. Do not silently delegate routine
work. Inside Hermes prefer native tools/subagents; do not launch Hermes calling
Hermes in a loop. A separate profile/process requires a scoped reason.

Read [the capability](../../capabilities/hermes.md) and
[its status](../../capabilities/hermes/STATE.md), then only the
chosen route guide. Do not treat this skill as enabling anything in a caller.

## Procedure

1. **Pick the job, not just the model.** Check the
   [delegation menu](../../capabilities/hermes/delegation-menu.md).
   Prefer the caller's native tool for simple work it can already do. Hermes is
   an independent agent with its own permissions and credentials, not a sandboxed
   copy of the parent or automatically this Discord conversation.
2. **Choose a route.** Default to local CLI for a bounded task. Use the existing
   authenticated HTTP API for a running service, long-task events, or conversation
   chaining. Native MCP is a messaging/history/approval bridge, not a general
   task runner. A2A is optional and must be enabled/tested first.
   Do not assume one-shot CLI execution provides parent/child overlap. For
   persistent monitoring, consult the runs API guide and its verification limits.
3. **Pin the runtime per task.** Take the model, provider and effort from the
   Hermes rows (sections 3 and 4) of
   [`delegation-briefing.md`](../../ai-models/delegation-briefing.md)
   and read that model's card. Do not choose from memory. Do not
   confuse `openai-codex` with the billed OpenAI API provider `openai`. Do not
   change global defaults. For another model, use an authenticated exact pair;
   refuse unavailable pairs instead of silently substituting. Inspect fallback
   telemetry when available and reject an unapproved model change.
4. **Write a task packet.** Include goal, source context, working directory,
   profile, allowed/excluded paths, allowed sites/accounts/actions, read-only vs
   editing scope, output destination/format, acceptance checks, time/iteration
   budget, and stop/ask conditions. Ask the child to print `PROGRESS n/total` (for example `PROGRESS 2/5`) as it finishes each step; the agent-watch Claude Code mod reads it to show progress and time left. No secrets. Say: no delegation, cross-harness
   calls, memory/skill edits, scheduling or message sends unless those specific
   actions are authorized. An allowed browser action must identify its profile.
5. **Preflight the selected route and task tools.** CLI: executable/help, current
   repo/branch/diff and relevant toolsets. API: authenticated capabilities and
   toolsets, plus the task's actual backend. A published tool list is not proof
   of account login or OS consent. Load shared workspace/site skills explicitly
   when needed; caller skills are not inherited.
6. **Launch and supervise.** Follow the
   [CLI guide](../../capabilities/hermes/cli.md) or
   [API guide](../../capabilities/hermes/api.md). Capture IDs,
   events, stderr and final response in an appropriately private location. Bound
   wall-clock time and iterations. No automatic approval bypass. A headless
   question is a blocker to relay, not permission to invent the answer.
   For monitoring or benchmarks, follow the CLI guide's
   [child and accounting notes](../../capabilities/hermes/cli.md#child-monitoring-and-benchmarks).
   Inspect authorized children's receipts and linked sessions, parse machine
   events from both captured channels, and measure wall time independently.
7. **Verify, then report.** Inspect actual successful tool events and all errors;
   read back the exact external write; inspect changed paths/diff and run checks.
   Do not trust exit code or the child's self-report alone. Report requested and
   observed model/effort/provider, route/profile/session, permissions, outputs,
   checks and blockers. Label unavailable telemetry. Retain the exact session or
   response ID for follow-ups; never resume another user's or active chat by guess.

## Improvement Boundary

Improve this shared skill and capability only for lessons that help all callers.
Keep caller-specific MCP config, command discovery and approval mechanics in that
caller's adapter. Keep Hermes's global defaults, secrets, native tool definitions
and local wrapper skills outside the shared workspace. `/sync-tool-adapter`
onboards one caller in its own session; do not edit several harnesses here.
