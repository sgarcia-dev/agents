---
name: task-codex
description: Use from a harness other than Codex when the user wants to delegate a bounded task to the Codex CLI for public web research, account-connected Google work when available, or a selected low-cost worker model. Do not use inside Codex or silently delegate ordinary work.
created_at: 2026-09-28
updated_at: 2026-10-07
model: gpt-6-sol
doc_type: skill
purpose: Safely dispatch and supervise one bounded Codex CLI task from another harness.
metadata:
  opencode/autoinvoke: false
related:
  - path: ~/agents/capabilities/codex-cli.md
    why: Portable bridge capability and verified limits.
---

# Task Codex

**Explicit user request only.** Loading this skill never authorizes a handoff.
Read `~/agents/conventions/autonomous-task-permissions.md` for the
owner-approved non-interactive defaults, routine roots, enabled MCP preapproval,
and high-risk exceptions. Preserve the bounded packet and child-depth limits.

Use this only from a harness other than Codex. Read `../../capabilities/codex-cli.md` before
launching. Check `codex --version`, `codex --help`, `codex exec --help`, login
status, and the intended folder. The CLI child receives a new session, not the
caller's conversation, permissions, tools, or account connections.

1. Choose a bounded task that benefits from Codex: current public web research,
   a user-authorized Google account task when the CLI connection is verified, or
   a cheap focused worker. Do not claim a special Reddit scraper or guaranteed
   Gmail/Drive availability. For research, request source links, dates, and a
   distinction between first-hand comments and inference.
2. Check the repository, branch, and starting diff before an editing run. Give
   Codex the goal, allowed paths, excluded paths, output shape, checks, tool and
   search limits, decision points, and a stop condition. Ask the child to print `PROGRESS n/total` (for example `PROGRESS 2/5`) as it finishes each step; the agent-watch Claude Code mod reads it to show progress and time left. For research or
   output-only packets, add "Do not run git; I commit." Children load the
   workspace git rule and otherwise commit and push their own output (8 of
   14 did on 6 October 2026).
3. Read [`delegation-briefing.md`](../../ai-models/delegation-briefing.md) first: section 4 for the Codex default, step-up and search
   models, and section 5 for that model's card (what it fails at, how many to
   run, how hard to check it). Do not choose a model from memory. Pin the exact
   model with `-m <model>` and `-c model_reasoning_effort=<effort>`. Keep
   service at `default` unless the briefing allows fast. If an exact pair is
   unavailable or rate limited, fall back only within the same row of the
   briefing's fallback table, and report the switch.
4. Block subagents by default with invocation-scoped `--disable multi_agent`
   and say the child must not delegate. Follow
   `../../roles/task-worker-tiers.md` if the user requests subagents or a
   delegation-dependent skill requires them. Give any allowed run a maximum
   child count. Do not let the CLI child call another harness CLI without an
   explicit request for that chain.
5. For research and review packets, also block the bundled browser and
   computer-use routes, which the sandbox does not cover: `--disable plugins --disable apps --disable computer_use --disable browser_use --disable browser_use_external --disable in_app_browser -c 'mcp_servers.node_repl.enabled=false' -c 'mcp_servers.computer-use.enabled=false'`. Never add
   `--disable code_mode_host`; it breaks every tool in CLI 0.158.0. Reject a
   report whose events show no successful tool calls.
6. Use `codex --search` for live public web research. For a search run,
   always use `--yolo`. Read [the web reference](../../capabilities/web/README.md). Name allowed tools and forbid further hand-offs in the packet. Use native tools by default; load web-search only if explicitly requested or named in the packet. Check Gmail and Google
   Drive tools in the CLI session before relying on them. Scope account calls to
   the user's task. In particular, public web search is independent of access
   to the user's account connectors.
7. **Full access, no sandbox by default** (user decision, 2026-09-30): run
   every packet with `--yolo` (short for
   `--dangerously-bypass-approvals-and-sandbox`). Sandboxes and approval
   prompts make headless runs fail silently. Scope comes from the packet
   (allowed paths, no subagents, no hand-offs), not from the sandbox. Use a
   sandbox only when the user asks or the permission convention identifies
   concrete high-risk work: then `--sandbox
   read-only`, or `--sandbox workspace-write -C <folder>` (add `-c
   sandbox_workspace_write.network_access=true` if it needs the network; in
   `exec`, set `-c approval_policy=never`, since `--ask-for-approval` is not
   an `exec` flag on CLI 0.159.0). Launch with `codex` as the first word of
   the command (no `cd ...;` or `sh -c` wrapper) so the caller's
   `Bash(codex:*)` allow rule matches.
8. Capture `--json` events and `--output-last-message`, preserve the thread ID,
   set a deadline, and inspect the final event, tool errors, edits, and checks.
   CLI JSON can omit native child activity and usage. When child inspection or
   benchmarking is requested, use the capability's
   [parent/child readback](../../capabilities/codex-cli.md#parentchild-inspection-and-benchmarks),
   not the parent's summary, to reconcile sessions, usage and independently
   measured wall time. Record unavailable cost or timing fields as unknown.
   If Codex asks a question, relay it to the user or calling root and resume
   that same session with `codex exec resume <id>` after the answer arrives.

Report the exact model, effort, service tier when observable, permission mode,
subagent setting, session ID, result, changed paths and checks, and any open
question. A zero process exit code alone is not acceptance.
