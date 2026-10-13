---
created_at: 2026-09-30
updated_at: 2026-10-05
model: gemini-3.8-flash
doc_type: capability
purpose: Full reference for Antigravity CLI (agy / Gemini) as a headless CLI bridge other AI harnesses can call.
related:
  - path: ~/agents/capabilities/connectors.md
    why: Portable awareness inventory of external bridges.
  - path: ~/agents/capabilities/claude-cli.md
    why: The Claude Code CLI bridge for comparison.
  - path: ~/agents/capabilities/codex-cli.md
    why: The Codex CLI bridge for comparison.
  - path: ~/agents/capabilities/opencode-cli.md
    why: The OpenCode CLI bridge for comparison.
  - path: ~/agents/skills/task-gemini/SKILL.md
    why: Procedure for non-Gemini callers. This file holds the facts.
---

# Gemini CLI Bridge (Antigravity CLI / agy)

Another harness (Claude Code, Codex, OpenCode, Hermes) can hand Gemini a bounded task using the `agy` CLI in print mode (`agy -p`). The caller owns authorization, packet scope, monitoring, and final review. Gemini owns its runtime session, model, built-in tools, workspace skills, and MCP connectors.

This is a local CLI bridge, not an MCP connector or a native subagent. Caller permissions and conversation context do not carry over to the child process.

Inside Gemini, use native tools and subagents instead of calling the CLI.

The step-by-step caller procedure lives in [`task-gemini`](../skills/task-gemini/SKILL.md). This file holds the technical facts: executable paths, flags, supported models, output schemas, and verified test results.

## At a Glance

| Property | Value |
|---|---|
| **Binary path** | `~/.local/bin/agy` |
| **App data directory** | `~/.gemini/antigravity-cli` |
| **Global config directory** | `~/.gemini/config` |
| **Best for** | Fast Google model reasoning, high token throughput, multimodal understanding, structured JSON schema outputs |
| **Which model** | From the Gemini rows of the [delegation briefing](../ai-models/delegation-briefing.md) |
| **Usable models** | Gemini 3.8 Flash only (`high`, `medium`, `low`). All other models are abysmally bad. |
| **High / Pro tier** | Disabled / unsupported. Gemini Pro defaults to 3.1, which is ancient and rejected. |
| **Headless flag** | `-p` or `--print` (runs one task and exits) |
| **Permission flag** | `--dangerously-skip-permissions` (required for unattended headless runs) |
| **Output formats** | `text`, `json`, `stream-json` |
| **Cost** | Task dollar cost was not exposed in the October 5 subscription test; do not infer a zero bill from missing cost telemetry |
| **Parallel runs** | Per the briefing's count rules (Gemini 3.8 Flash is mid cost: usually 2 to 4); no high workers |

## What the Child Can Do

- **Public web search and URL reading:** Native `search_web` and `read_url_content` tools run without extra external setup. `search_web` returns a written summary with sources, not a result list; `read_url_content` saves the page to a file to read in a second call. Tested behavior, limits, and what works per site: `~/agents/capabilities/web/tools/gemini.md`. Give web tasks 8 to 10 calls.
- **Configured MCP connectors:** Hosted HTTP servers configured in `~/.gemini/config/mcp_config.json` (`parallel`, `exa`, `firecrawl`) run automatically.
- **Agents workspace instructions and skills:** `agy` traverses parent directories to discover `.agents/`. It automatically reads `~/.agents/AGENTS.md` and discovers thin skill loaders in `~/.agents/skills/`.
- **Filesystem and shell:** Native tools allow viewing files, writing files, replacing text blocks, and running shell commands in the target workspace.
- **Subagents:** September 30 recorded definition/registration of `task-explore` and `task-execute`, but the October 5 test failed to invoke `task-explore` as not found or not allowed. That local mapping needs a Gemini-owned retest before reliance; child monitoring was not demonstrated. Keep subagents off by default and follow the current worker tiers/active adapter for permitted roles. Registration alone is not execution proof.
- **Structured JSON output:** With `--output-format json`, `agy` returns a single JSON object containing `conversation_id`, `status`, `response`, `duration_seconds`, `num_turns`, and `usage`.
- **Session continuation:** Retains conversation state. A caller can resume a previous session using `--conversation <conversation_id>`.

## Quick Start

Run from the folder relevant to the task:

```sh
agy -p 'Your bounded task description here.' \
  --model gemini-3.8-flash-medium \
  --effort medium \
  --dangerously-skip-permissions \
  --output-format json \
  < /dev/null > "$RUN_LOG" 2> "$RUN_ERR"

# Extract fields from the JSON result:
jq -r '.response' "$RUN_LOG"         # Final model answer
jq -r '.conversation_id' "$RUN_LOG"  # ID to resume or inspect
jq -r '.status' "$RUN_LOG"           # SUCCESS or ERROR
jq '.usage' "$RUN_LOG"               # Token counts and cache metrics
```

Key execution notes:
- Use `< /dev/null` to avoid waiting on interactive terminal input.
- Always include `--dangerously-skip-permissions` in non-interactive print mode. Without this flag, tool permission requests are denied automatically because there is no interactive prompt.
- For streaming updates, pass `--output-format stream-json`.

## Telemetry and Task Acceptance

Use final JSON for a simple result. For live model-step/tool inspection, change
the authorized invocation to `--output-format stream-json`, preserving its pinned
model/effort, permission scope, timeout, stdin handling and separate stderr log.
Retain `conversation_id` and correlate repeated state updates by native step
index before counting tools or model responses.

- The October 5 stream exposed model-step duration and usage plus tool states.
  Inspect transitions through `ACTIVE`, completion and `ERROR`, not just final
  prose. Keep input, output, thinking and cache-read categories as emitted;
  their relationships need provider verification before cross-tool summation.
- `invoke_subagent` entered `ERROR`: `task-explore` was not found or not allowed.
  The CLI nevertheless exited zero and returned `SUCCESS`. A required child
  must have a verified identity and completion; top-level success did not meet
  that task's acceptance criteria. Do not retry by silently creating a role,
  substituting another worker or changing another harness's configuration.
- Parent-only tools and summaries remained usable, but no child content,
  child token accounting or parent/child overlap was demonstrated. This is a
  dated local mapping failure, not proof Antigravity cannot delegate.
- Task dollar cost and effective context capacity were unavailable. Record
  them as unknown with a reason; token counts are not a cost or context meter.

For a benchmark, record installed version, requested/observed model and effort,
conversation ID, caller-measured monotonic launch-to-exit seconds, first visible
content latency, native model-step durations/usage and unique tool steps/errors.
Effective task output tokens/s is reconciled reported output divided by whole-task
seconds, not generation speed. Label the scope parent-only when no child ran;
do not rank it as an equivalent successful parent/child workload. Thinking and
cache categories must stay separately labeled until their semantics are verified.

Accept only when the final result meets the requested outputs/checks and all
required tools/children succeeded. A failure of required delegation makes the
whole requested task incomplete even if the parent returns a useful answer.
Record unavailable measurements explicitly; do not invent child IDs or zero costs.

Verified on Antigravity `agy` 1.2.17, 2026-10-05: see the
experiment and failed child launch (private, not published).
No runtime repair, child retest, cancellation test or automatic benchmark runner
was performed by this documentation update.
Use equivalent packets and runtime settings for comparisons; prefer fresh conversations.
If resuming, record usage baselines and per-turn versus cumulative semantics first.

## Supported Models

**Gemini 3.8 Flash is the only usable model family in Gemini.**

The runtime CLI has access to other models, but they are abysmally bad. The Gemini Pro series defaults to 3.1, which is ancient by modern standards. Older Flash models like 3.7 and 3.6 are obsolete and unusable.

Gemini 3.8 Flash remains the only useful model until Gemini 4 releases. When Gemini 4 launches, it will require separate benchmark testing, evaluation, and indexing into `ai-models/` before adoption.

| Model ID | Human-Readable Name | Status / Role |
|---|---|---|
| `gemini-3.8-flash-high` | Gemini 3.8 Flash (High) | Usable. Role set by the briefing |
| `gemini-3.8-flash-medium` | Gemini 3.8 Flash (Medium) | Usable. Role set by the briefing |
| `gemini-3.8-flash-low` | Gemini 3.8 Flash (Low) | Usable. Role set by the briefing |
| `gemini-3.7-flash-high` | Gemini 3.7 Flash (High) | Unusable (obsolete and abysmally bad, do not use) |
| `gemini-3.7-flash-medium` | Gemini 3.7 Flash (Medium) | Unusable (obsolete and abysmally bad, do not use) |
| `gemini-3.7-flash-low` | Gemini 3.7 Flash (Low) | Unusable (obsolete and abysmally bad, do not use) |
| `gemini-3.6-flash-high` | Gemini 3.6 Flash (High) | Unusable (obsolete and abysmally bad, do not use) |
| `gemini-3.6-flash-medium` | Gemini 3.6 Flash (Medium) | Unusable (obsolete and abysmally bad, do not use) |
| `gemini-3.6-flash-low` | Gemini 3.6 Flash (Low) | Unusable (obsolete and abysmally bad, do not use) |
| `gemini-3.1-pro-high` | Gemini 3.1 Pro (High) | Unusable (ancient 3.1 base model, abysmally bad, rejected) |
| `gemini-3.1-pro-low` | Gemini 3.1 Pro (Low) | Unusable (ancient 3.1 base model, abysmally bad, rejected) |
| `claude-sonnet-4-6` | Claude Sonnet 4.6 (Thinking) | External model (delegate to Claude Code instead) |
| `claude-opus-4-6-thinking` | Claude Opus 4.6 (Thinking) | External model (delegate to Claude Code instead) |
| `gpt-oss-120b-medium` | GPT-OSS 120B (Medium) | External open-weights model |

## Command-Line Flags

```text
Usage of agy:
  -p, --print                    Run a single prompt non-interactively and print the response
  --model <model>                Model for the current CLI session
  --effort <low|medium|high|max> Reasoning effort level
  --dangerously-skip-permissions Auto-approve all tool permission requests without prompting
  --output-format <format>       Output format for print mode (text, json, stream-json)
  --input-format <format>        Input format for print mode (text, stream-json)
  --json-schema <schema>         Optional JSON schema string or path to enforce structured output
  --print-timeout <duration>     Time limit for print mode (e.g. 300s; 0 waits until done)
  --conversation <id>            Resume a previous conversation by ID
  -c, --continue                 Continue the most recent conversation
  --add-dir <dir>                Add a directory to the workspace (repeatable)
  --mode <mode>                  Execution mode (accept-edits, plan)
  --sandbox                      Run in a sandbox with terminal restrictions enabled
  --disable-slash-commands       Disable slash command and skill expansion in print mode
```

Subcommands:
- `agy models`: List available models.
- `agy mcp`: Manage MCP servers (`add`, `remove`, `list`, `enable`, `disable`).
- `agy agent` / `agy agents`: List available agents.
- `agy plugin` / `agy plugins`: Manage plugins (`install`, `uninstall`, `list`, `enable`, `disable`).
- `agy changelog`: View release notes and updates.

## Permissions and Autonomous Execution

Under `~/agents/conventions/autonomous-task-permissions.md`:
- Routine permissions are configured in `~/.gemini/antigravity-cli/settings.json` with pre-approved allow rules and trusted workspaces.
- Headless runs via `agy -p` require `--dangerously-skip-permissions` to auto-approve tool calls without prompt friction.
- When sandboxing is required for concrete high-risk tasks, add `--sandbox`. For ordinary tasks, scope is enforced by the prompt and packet boundaries.

## Verified Live Checks (September 30, 2026)

1. **Binary check:** Verified `~/.local/bin/agy` is present and functional.
2. **Model roster:** `agy models` successfully retrieved active model candidates including `gemini-3.8-flash-high` and `gemini-3.8-flash-medium`.
3. **Headless text print test:** `agy -p 'echo hello' --dangerously-skip-permissions --output-format text` exited 0 with clean output `hello`.
4. **Headless JSON print test:** `agy -p 'echo "json test"' --dangerously-skip-permissions --output-format json` returned structured JSON with conversation ID, token usage, duration, and status `SUCCESS`.
5. **Instruction discovery:** Verified the headless child automatically discovered `.agents/` and read `~/.agents/AGENTS.md`.
6. **MCP connectivity:** Configured `parallel`, `exa`, and `firecrawl` hosted endpoints via `agy mcp add`. Verified with `agy mcp list`.
7. **Web benchmark (Sept 30, night):** 6 test sessions and 2 interviews, all run on `gemini-3.8-flash-high` (the default is now medium; the results were not re-run on medium); `--output-format stream-json` showed every tool call, and its `init` event lists the tool roster (58 tools, including browser tools). Firecrawl search failed keyless inside Gemini. Detail in the linked spec.
8. **Worker subagents (historical registration, not current execution proof):** Defined and registered `task-explore` and `task-execute` on `gemini-3.8-flash-medium`. The later October 5 invocation failed; see Telemetry and Task Acceptance before relying on that mapping.
