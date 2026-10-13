---
name: task-claude
description: Use from a harness other than Claude Code when the user wants to send a bounded task to Claude Code's headless CLI, for example hard reasoning, careful review, web research, or reading the user's Gmail, Google Drive, or Google Calendar. Do not use from inside Claude Code; use native subagents there. Do not silently turn ordinary local work into a Claude delegation.
created_at: 2026-09-28
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: skill
purpose: Safely dispatch and supervise a bounded Claude Code CLI task from another harness.
metadata:
  opencode/autoinvoke: false
related:
  - path: ~/agents/capabilities/claude-cli.md
    why: Full reference. What the child can do, flags, models, costs, Google tool names, and test results.
---

# Task Claude

**Explicit user request only.** Loading this skill never authorizes a handoff.
Read `~/agents/conventions/autonomous-task-permissions.md` for the
owner-approved non-interactive defaults, routine roots, enabled MCP preapproval,
and high-risk exceptions. Preserve the bounded packet and child-depth limits.

Use only from a harness other than Claude Code. Inside Claude Code, use native
subagents instead.

This is the procedure. The facts (exact flags, tool names, costs, what was
verified) live in [`capabilities/claude-cli.md`](../../capabilities/claude-cli.md).
Read it before the first run, and check `claude --version` and `claude --help`,
because flags change between releases.

1. **Decide Claude is worth it.** Runs consume quota and can expose model-price
   accounting rather than an actual bill. Use Claude for hard reasoning, careful
   review, web research, or the user's Gmail, Google Drive, and Google Calendar. Send cheap
   bulk work to cheaper models instead.
2. **Pick the folder.** Run from the checkout the task is about. For editing
   tasks, confirm the repository, branch, and `git status --short` first.
3. **Write one bounded prompt.** Include the goal, allowed edits, excluded
   paths, expected output, tests, a search or length cap, and when to stop and
   ask. The child does not see the caller's conversation.
4. **Pick the agent, then pin model and effort every time.** Run the child as
   one of Claude Code's maintained workers with `--agent <name>`. The agent
   loads the worker role rules and blocks subagents; the model and effort for
   each agent come from
   [`delegation-briefing.md`](../../ai-models/delegation-briefing.md)
   (section 3, Claude Code rows; section 4 for when to step up or down).
   - **Regular handoff: `task-explore-high`** for review, reasoning and
     research, or **`task-execute-high`** when the child edits. Claude is
     worth its quota for careful work, and these are its best value there.
   - **Cheaper: `task-explore` or `task-execute`** for a short job you will
     check: a Gmail, Drive or Calendar lookup, a small web search with quoted
     links, one small edit with a real test. Never past about 100K tokens of
     context.
   - **More expensive: no agent**, for architecture, ambiguous root-cause work,
     or a packet the regular handoff already got wrong. Pass the briefing's
     hard-task model and effort and `--disallowedTools Agent` yourself.
   - **Web search**: the briefing's "Claude for web search" table picks the
     agent by search size.
   Also pass the agent's `--model <full-id> --effort <level>` from the
   briefing, so a stale native agent file cannot change the run. Full model IDs
   only, never `--fallback-model`. Do not choose from memory. On a rate limit,
   fall back only within the same row of the briefing's fallback table, and
   report the switch.
5. **Pick permissions.** See the capability's Permissions section.
   - Read-only work: full access too; in `-p` mode a refused tool fails silently.
   - Web search: always full permissions, plus a line naming which search
     tools to use and a no-hand-off line. Read [the web reference](../../capabilities/web/README.md). Native tools are the default; load web-search only if explicitly requested or named in the packet.
   - Google: allow only the read tools the task needs, by exact name. Allow a
     send, share, or delete tool only for an action the user asked for.
     Never use full bypass with Google work.
   - Everything else: **full access by default** with
     `--dangerously-skip-permissions` (user decision, 2026-09-30). Scope comes
     from the prompt and `--disallowedTools`, not from permission prompts.
     Restrict permissions only when the user asks or the permission convention
     identifies concrete high-risk work.
   - Put the prompt right after `-p`; the tool-list flags swallow a prompt
     that follows them.
6. **Block subagents by default.** Pass `--disallowedTools Agent` and say in
   the prompt that the run is one worker that must not delegate. Allow
   subagents only when the user approved it or the task uses a skill that
   needs them, and then state the maximum count. Follow the CLI child rule in
   [`task-worker-tiers.md`](../../roles/task-worker-tiers.md). Never chain to
   `task-opencode` or `task-codex` unless the user asked.
7. **Run and capture.** Use `-p --output-format json`, separate stdout and
   stderr logs per run, `--max-budget-usd` as a cost cap, a timeout, and
   `< /dev/null`. Keep the `session_id`. Default to 1 to 3 parallel runs.
   Never run two editing tasks in the same checkout.
   When live monitoring is requested, use the capability guide's
   [streaming and accounting recipe](../../capabilities/claude-cli.md#live-monitoring-and-accounting).
   Forward child content only when subagents are authorized; retain parent/child
   identifiers. For benchmarks, measure wall time independently and reconcile
   usage before reporting cost or effective task output tokens per second.
8. **Handle questions.** If `result` is a question, send it to the user or
   calling root. Never invent an answer. Reply with
   `claude -p '<answer>' --resume <session_id>` from the same folder, with
   model and effort again.
9. **Accept only verified work.** Check `result`, `permission_denials`, cost,
   changed files, and tests. A zero exit code alone proves nothing.

Report the agent, model, effort, permission mode, subagent setting, session ID, cost,
outcome, open questions, and next step.
