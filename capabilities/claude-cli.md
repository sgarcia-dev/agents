---
created_at: 2026-09-28
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: capability
purpose: Full reference for Claude Code as a headless CLI bridge other AI harnesses can call; what it can do, how to run it, what it costs, and what was verified.
related:
  - path: ~/agents/capabilities/connectors.md
    why: Portable awareness inventory of external bridges.
  - path: ~/agents/capabilities/opencode-cli.md
    why: The mirror bridge in the other direction.
  - path: ~/agents/capabilities/codex-cli.md
    why: The Codex bridge, for comparison.
  - path: ~/agents/skills/task-claude/SKILL.md
    why: Step-by-step procedure for non-Claude callers. This file holds the facts.
  - path: ~/agents/capabilities/web/README.md
    why: How the child picks web tools once it is running.
---

# Claude Code CLI bridge

Another harness (OpenCode, Codex, Hermes, ...) can hand Claude Code one bounded
task with `claude -p`. The caller owns scope, approval, monitoring, and review.
Claude Code owns the session, model, skills, subagents, and tools in the folder
it runs in. It is a local CLI bridge, not an MCP connector or a native
subagent. The child does not see the caller's conversation, tools, or
permissions.

Inside Claude Code, use native subagents instead of calling yourself.

The procedure lives in [`task-claude`](../skills/task-claude/SKILL.md). This
file holds the facts: what the child can do, flags, costs, and test results.

## At a glance

| | |
|---|---|
| **Best for** | Hard reasoning, careful review, web research, and the user's Gmail, Drive, and Calendar |
| **Not for** | Cheap bulk work. Send that to OpenCode's cheaper models |
| **Default model** | Set in [delegation-briefing](../ai-models/delegation-briefing.md) |
| **Cost** | Historical reported examples: $0.12 trivial run, $0.17 small web search, $0.27 for 3 Google reads; reported model-price cost is not an actual bill |
| **Parallel runs** | Claude is premium in the [delegation briefing](../ai-models/delegation-briefing.md): usually 1 to 3; more only when the user asks |
| **Needs** | The `claude` executable and a logged-in account. Checked on 2.1.283 (Sept 28) and 2.1.284 (Sept 29) |
| **Risk** | Write-capable with the host user's authority. Not a sandbox |

## What the child can do

- **Web search and page reads.** See [Web research](#web-research) below.
  - Parallel and Firecrawl (search and page read) run with no flag.
  - Claude Code's own WebSearch and WebFetch are prompt-free under this machine's
    owner-approved bypass default; restrictive sessions need explicit allows.
- **Google account.** Gmail, Google Drive, and Google Calendar, through the
  connectors on the user's claude.ai account. The current bypass default preapproves
  read tools; exact ask rules gate account mutations. See [Google access](#google-access).
- **Workspace skills and instructions.** The child loads
  `~/.claude/CLAUDE.md` (the Agents workspace `AGENTS.md`), the folder's
  project instructions, and every skill Claude Code maps. Ask for a skill by
  name: "use the research skill".
- **Subagents.** `task-explore`, `task-execute`, their `-high` versions, and
  `task-orchestrator` work inside the child. Blocked by default; see
  [Subagents](#subagents).
- **Files and shell.** The current user default permits routine reads, edits and shell commands
  without a permission flag (see [Permissions](#permissions)).
- **Structured output.** `--json-schema '<schema>'` returns output that
  matches a schema.

## Quick start

Run from the folder the task is about. The child reads that folder's settings
and instructions.

```sh
claude -p 'Your bounded task, what to return, and when to stop.' \
  --agent "$AGENT" --model "$MODEL" --effort "$EFFORT" --output-format json \
  --disallowedTools Agent --max-budget-usd 1 \
  < /dev/null > "$RUN_LOG" 2> "$RUN_ERR"

jq -r '.result' "$RUN_LOG"          # final answer
jq -r '.session_id' "$RUN_LOG"      # keep it to resume or answer questions
jq '.total_cost_usd, .modelUsage, .permission_denials' "$RUN_LOG"
```

- `-p` (`--print`) runs one task and exits.
- `< /dev/null` stops a 3-second wait for piped input.
- `--output-format json` returns one object with `result`, `session_id`,
  `total_cost_usd`, `num_turns`, `modelUsage`, and `permission_denials`. Use
  `stream-json` to watch progress live.
- **Put the prompt right after `-p`.** `--allowedTools` and
  `--disallowedTools` take a list and swallow a prompt that follows them. The
  run then fails with "Input must be provided".
- macOS has no `timeout` command. To stop a run after 10 minutes:
  `perl -e 'alarm shift; exec @ARGV' 600 claude -p ...`

## Live monitoring and accounting

Use final JSON for a short result; opt into streaming when live inspection or a
benchmark needs it. Add these flags to the authorized launch, retaining its
model, effort, permissions, budget, timeout and separate stderr capture:

```text
--output-format stream-json --verbose --include-partial-messages
--forward-subagent-text --include-hook-events
```

Keep `--disallowedTools Agent` unless child execution is authorized. Forwarding
flags do not grant that authorization. Preserve the session ID, native child/task
IDs and parent tool-use IDs. The October 5 test exposed child launch, progress,
completion, tool inputs/results and text linked to the parent call. Use those
links to locate the exact saved parent/child transcripts, not the latest session.
Retain transcript pointers privately; completed transcript messages expose the
message IDs and usage needed for final child accounting.

- Count unique tool-use IDs separately for parent and children; partial and
  completed events can describe the same call. Inspect results and errors too.
- Completed content-block events can still contain provisional output usage.
  Reconcile against completed transcript messages, deduplicated by message ID,
  or final cumulative `modelUsage`. Keep root and child attribution separate.
- Multiple result envelopes repeated the same cumulative `total_cost_usd` in
  the test. Use one final cumulative total; do not sum envelopes or add child
  charges again when the chosen total already includes them. On continuation,
  a task-only cost needs a recorded starting total as well as the ending total.
- Cost was labeled `costBasis: list`: model-price accounting, not proof of an
  incremental subscription charge. Record actual billed amount as unknown
  unless independently available.
- Forwarded completed child content is live visibility, not proof of
  token-by-token child generation. Request timing via OpenTelemetry is
  documented but no collector was exercised in this test.

For a benchmark, record installed version, requested/observed model and effort,
parent/child IDs, caller-measured monotonic launch-to-exit seconds, first visible
content latency, reconciled input/cache/output categories, cost basis and
acceptance result. Effective task output tokens/s is deduplicated root plus child
output divided by whole-task seconds, not generation speed. Record last-request
input and model capacity separately for a context-occupancy proxy; cumulative
input across requests is not context occupancy. Missing measurements are unknown,
not zero. Process completion and completed children still require the promised
outputs, sources or tests to pass before the task is accepted.

Verified on Claude Code 2.1.289, 2026-10-05: see the
experiment and measurement limits (private, not published).
This adds a capture/readback recipe, not an automatic benchmark runner or monitor.
Use equivalent packets and runtime settings for comparisons; prefer fresh sessions.
If resuming, record usage baselines and per-turn versus cumulative semantics first.

## Models and effort

Which model and effort to use (default, step up, web search) comes only from
the Claude Code rows of the [delegation briefing](../ai-models/delegation-briefing.md).
In the examples here, set `AGENT`, `MODEL` and `EFFORT` from that row. Full IDs:

| Model | ID | Note |
|---|---|---|
| Opus 5.5 | `claude-opus-5-5` | |
| Sonnet 5.5 | `claude-sonnet-5-5` | A trivial run cost $0.07 (Sept 29, 2026) |
| Fable 5.1 | `claude-fable-5-1` | Not in the briefing; only when the user asks |
| Haiku 5.5 | `claude-haiku-5-5` | Added 2026-10-07 |
| Haiku 4.5 | `claude-haiku-4-5-20251001` | Old; rejected by the user for worker tasks |

- Effort levels: `low`, `medium`, `high`, `xhigh`, `max`. Which level each
  agent and job uses comes from the briefing, not from this file.
- `--agent <name>` runs the child as a maintained Claude Code worker
  (`task-explore`, `task-execute` and their `-high` versions, defined in
  `~/.claude/agents/`). It loads the worker role rules and the agent's own
  tool limits. Still pass `--model` and `--effort` from the briefing's row for
  that agent. Live-checked 2026-10-08: `--agent task-explore --model
  claude-haiku-5-5 --effort high` ran and reported `claude-haiku-5-5`.
- **Login.** Headless runs sign in with the `CLAUDE_CODE_OAUTH_TOKEN`
  environment variable, which this machine sets in the user's shell profile
  (the browser login expires too often). A launch from another tool's shell
  picks it up. Claude Code's own shell tool does not pass it through, so a
  `claude -p` started from inside Claude Code fails with "OAuth session
  expired" unless the variable is supplied to that one command. Never print
  or copy the token.
- Always pass `--model` and `--effort`, including on resume. Otherwise the run
  uses this machine's saved default, which changes with normal use.
- Use full IDs, never aliases like `opus`. Never pass `--fallback-model`; it
  swaps models silently.
- There is no `claude models` command.
- Claude Code may also use Haiku in the background to process search
  results. That is normal, not a model swap.

## Web research

Two sets of web tools are available to the child:

| Tools | Headless, no flag | Notes |
|---|---|---|
| Parallel `web_search`, `web_fetch` | **Runs** | Allowed in the user's Claude Code settings |
| Firecrawl `firecrawl_search`, `firecrawl_scrape`, `map`, `parse` | **Runs** | Same. Crawl, agent, interact, and monitor tools are hidden |
| Exa `web_search_exa`, `web_fetch_exa` | Runs | Used only when the user asks for Exa |
| Claude Code `WebSearch`, `WebFetch` | Prompt-free under current bypass default | Restrictive modes may need `--allowedTools WebSearch WebFetch` |

The first three rows were verified on Sept 29, 2026 with and without
`--dangerously-skip-permissions`: no denials, and the hidden Firecrawl tools
did not appear. They come from `~/.claude/settings.json`, so a run launched
with `--strict-mcp-config` or `--settings` that drops them loses them.

The child uses native search and fetch by default. Tool facts, allowed escalation and acceptance checks live in [the web reference](web/README.md). Load web-search only when explicitly requested or named in the packet. Authorized terminal search runs use the task skill's full-permission launch and capture flags. Pass the allowed tools and budget. Do not use the older native-plus-Parallel prompt as a default.

Keep it cheap:

- Ask for quick browsing with a search cap and an answer length, not "deep
  research".
- Ask for source URLs and dates. In one test the child noticed its only result
  was months old and said so.
- WebSearch refuses reddit.com and WebFetch returns a summary, not the page.
  Parallel covers both gaps. For Reddit replies, Codex is the only tool that
  worked (see [`codex-cli.md`](codex-cli.md)).

## Google access

The Gmail, Google Drive, and Google Calendar connectors on the user's claude.ai
account load in every headless run on this machine. Setup lives on the
account, not in a config file. Verified Sept 28: 50 tools loaded; one read
from each worked (3 calls, 5 turns, $0.27, 13 seconds).

```sh
claude -p 'Find the email from X about Y in the last 30 days. Summarize it in 3 bullets. Quote nothing else.' \
  --model "$MODEL" --effort "$EFFORT" --output-format json \
  --allowedTools mcp__claude_ai_Gmail__search_threads mcp__claude_ai_Gmail__get_thread \
  --disallowedTools Agent --max-budget-usd 1 < /dev/null
```

- **Current default:** read tools have no ask rule and are permitted under bypass.
  Account mutations have exact ask rules. These current Google rules are
  documentation-supported but not live-tested locally. The earlier denied-read
  result predates the September 30 permission migration.
- **Known read tools.** In restrictive modes allow them by exact name. Prefixes: `mcp__claude_ai_Gmail__`,
  `mcp__claude_ai_Google_Drive__`, `mcp__claude_ai_Google_Calendar__`.
  - Gmail: `search_threads`, `get_thread`, `get_message`, `list_labels`,
    `list_drafts`, `get_draft`
  - Drive: `search_files`, `list_recent_files`, `get_file_metadata`,
    `read_file_content`, `download_file_content`, `get_file_permissions`
  - Calendar: `list_calendars`, `list_events`, `search_events`, `get_event`,
    `suggest_time`
- **Every other tool acts as the user**: send, reply, trash, relabel, share,
  create, delete, respond. Since 2026-09-30 these 33 tools have exact-name
  `ask` rules in user settings. `ask` beats allow rules and is not
  auto-approved even under bypass (official permission-modes docs), so
  `--allowedTools` cannot unlock them. In `-p` they are refused; they need an
  interactive session where the user says yes. Not live-tested locally.
- **Privacy.** What the child reads lands in its answer and logs. Ask only
  for what is needed and say what not to print.
- **Can be slow to load.** `claude mcp list` shows them as `claude.ai Gmail`,
  and so on. In one test a run hung until its 4-minute timeout while these were
  timing out; the next run was fine. Always use a timeout.
  `--strict-mcp-config` turns them off.
- The child may first call `ToolSearch` to load the tool definitions. That
  reads no Google data.

## Permissions

Since 2026-09-30 the user settings set `defaultMode: bypassPermissions`, so a
plain `claude -p` already runs with full access and needs no bypass flag. Google
read tools run freely; the 33 write/send/share/delete tools have exact-name
`ask` rules, which are always refused in `-p` (an `--allowedTools` allow
cannot override `ask`). Project settings or a `--permission-mode` flag
can still override the default. Worker subagents inherit enabled root MCP tools
(no limiting `tools` list in their wrappers); one default explore worker
successfully called Parallel. The other wrappers use the same inherited setup.
The table below still applies when a caller
wants less than full access.

In `-p` mode nobody can click "allow". Anything that needs approval is denied,
the run keeps going, and the denial shows in `permission_denials`.

| Goal | Flag |
|---|---|
| Read-only work, Parallel, Firecrawl | No flag |
| Allow specific tools | `--allowedTools WebSearch WebFetch "Bash(git *)" Edit` |
| Block specific tools | `--disallowedTools Edit Write` |
| Allow file edits only | `--permission-mode acceptEdits` |
| Allow everything | `--dangerously-skip-permissions` (same as `--permission-mode bypassPermissions`) |

- Full bypass gives the child the user's whole shell and file access. Use it
  only when the user authorized it for a clearly scoped task. Prefer a separate
  checkout or `--worktree` for edits, and check the diff after.
- `--yolo` and `--allow-all-permissions` do not exist.
  `--allow-dangerously-skip-permissions` only makes bypass available; it does
  not turn it on.
- Deny rules in settings still apply under bypass. "Ask" rules turn into
  refusals in headless runs, even under bypass. That is why the web search
  servers use allow and deny rules only (see
  [`mcp-setup.md`](web/tools/parallel.md)).

## Subagents

A child can start its own subagents, and they add to the cost. Follow the CLI
child rule in [`task-worker-tiers.md`](../roles/task-worker-tiers.md).

- **Block by default** with `--disallowedTools Agent`. Verified: asked to
  start one, the child said it had no such tool.
- **Allow** only when the user approved it or the task uses a skill that needs
  delegation (`research`, `plan-execute`). Leave the flag off and state the
  limit in the prompt: "You may use up to 3 subagents."
- Say it in the prompt either way: "You are one worker. Do not start subagents
  or call other AI CLIs."
- `--agent <name>` makes a maintained subagent the main agent for the run.

## Questions and resuming

A headless child cannot pop up a question. It ends its turn with the question
in `result`. Answer in the same session, from the same folder (sessions are
stored per folder):

```sh
claude -p 'Your answer to its question.' --resume "$SESSION_ID" \
  --model "$MODEL" --effort "$EFFORT" --output-format json < /dev/null
```

- Answer only what the caller truly knows. Send judgment calls to the user.
  Never invent an answer.
- `total_cost_usd` on a resumed run is the running total for the session.
- `--fork-session` with `--resume` branches a copy.
- Prefer `--resume <id>` over `-c` (`--continue`), which picks the latest
  session and is ambiguous with parallel runs.

## Parallel and background runs

```sh
for i in 1 2 3; do
  claude -p "Task $i ..." --model "$MODEL" --effort "$EFFORT" \
    --output-format json --disallowedTools Agent --max-budget-usd 1 \
    < /dev/null > "run-$i.json" 2> "run-$i.err" &
done
wait
```

- Five parallel runs worked in one test. Counts follow the briefing (Claude is premium: usually 1 to 3).
- Never run two editing tasks in the same checkout.
- `claude --bg ...` starts a background session. `claude agents --json`
  lists them, `claude logs <id>` shows output, `claude stop <id>` stops one,
  `claude attach <id>` opens it.
- A quiet log does not mean a run finished. Keep the PID and `wait`.
- `--no-session-persistence` skips saving the session. Only use it when you
  will never resume.

## Other useful flags

- `--add-dir <path>`: give the child access to another folder.
- `--append-system-prompt '<text>'`: add rules without replacing the defaults.
- `--bare`: skips instructions and hooks, but needs `ANTHROPIC_API_KEY`. It
  does not work with this machine's subscription login.

## Checking the result

A run is done only when all of these hold:

- Exit code 0. **Not enough alone:** a run full of denials still exits 0.
- `result` answers the task and is not a question.
- `permission_denials` has nothing unexpected.
- The files and tests the task promised exist and pass.
- The cost is in line with the task.

## Verified results

Sept 28, 2026, Claude Code 2.1.283, scratch folder:

- Basic run: `PONG`, 1 turn, $0.12.
- Question, then resume in the same session: worked.
- WebSearch with `--allowedTools WebSearch`: 3 turns, $0.17.
- Bypass: shell write worked. Same prompt without the flag: denied, exit 0.
- `--disallowedTools Agent`: no subagent possible.
- Google: 50 tools visible; one read each from Gmail, Drive, Calendar worked
  ($0.27). Without an allow flag the Calendar call was denied.

Sept 29, 2026, Claude Code 2.1.284:

- Parallel search, Firecrawl search, and Firecrawl scrape ran with no flag,
  with and without bypass. No denials. Firecrawl crawl, agent, interact, and
  monitor tools were absent.

## Setup

Nothing to install for callers beyond the `claude` executable and login. Each
caller exposes [`task-claude`](../skills/task-claude/SKILL.md) in its own
adapter sync. The web search servers' Claude Code settings are in
[`mcp-setup.md`](web/tools/parallel.md).
