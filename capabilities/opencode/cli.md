---
created_at: 2026-09-29
updated_at: 2026-09-30
model: openai/gpt-6-sol
doc_type: capability
purpose: Working reference for calling OpenCode V2 from another AI harness.
related:
  - path: ~/agents/capabilities/opencode/STATE.md
    why: Entry point and current status.
  - path: ~/agents/capabilities/opencode/sessions.md
    why: Session monitoring, questions, permissions, cancellation and acceptance.
  - path: ~/agents/skills/task-opencode/SKILL.md
    why: Delegation procedure; this file owns CLI facts.
  - path: ~/agents/capabilities/connectors.md
    why: Inventory and default posture of bridges.
---

# OpenCode V2 CLI bridge

`opencode run` gives another harness one OpenCode task without opening the TUI.
OpenCode uses the model, agent, skills, tools, MCP connections, and permissions
available **in the selected working directory**. It does not inherit the
caller's conversation or authority. Inside OpenCode, use native tools instead
of calling `task-opencode`.

The child can inspect and change files, call shell commands, use locally
discoverable skills and configured MCP tools, and start subagents if permitted.
None of these is guaranteed merely because the CLI exists. Check the model,
agent, skill, connector, and effective permissions in the target location.
This bridge does not grant account-connected services from the caller's
harness; any authenticated integration must be present in OpenCode itself.

## At a glance

| | |
|---|---|
| Best for | A bounded task using an explicitly selected OpenCode model, including small read-only checks that can run in parallel |
| Needs | `opencode` CLI, available provider/model in the target location, working service or `--standalone` |
| Cost | Provider-, model-, variant-, tool-, and run-dependent; no verified fixed per-run price or CLI dollar cap |
| Risk | Files, shell, network, and tools may run with the host user's authority; **not a sandbox** |
| Caller owns | Authorization, packet scope, timeouts, child budget, logs, questions, diff review, final answer |

This guide's command syntax was checked on `opencode v2.0.19` on 2026-09-29.
For current syntax check `opencode --version` and `opencode run --help`.
[V2 CLI](https://opencode.ai/v2/docs/cli),
[models](https://opencode.ai/v2/docs/models), and
[permissions](https://opencode.ai/v2/docs/permissions) are authoritative;
the 2026-09-28 field notes (private, not published)
are historical test evidence, **not** a source of current V2 config syntax.

## Before running

1. Select the repository or folder as the shell **working directory**. V2
   `opencode run` has no `--dir` flag. For writes, check `pwd`, branch, and
   `git status --short`, then isolate parallel edits in separate checkouts.
2. Check `opencode models` and `opencode api get /api/model` **from that
   location**. An ID must be enabled and its provider available. Choose an
   exact `provider/model#variant`; variants differ by model. Do not infer
   credentials from a different project or a zero price in the catalog.
3. Confirm a needed skill with `opencode api get /api/skill` and an agent with
   `opencode api get /api/agent`. Skills from the caller do not automatically
   transfer. In V2 the skill ID comes from its file path, not its display name.
4. Give the child one bounded packet: goal, allowed and excluded paths, output,
   tests, search/length limit if applicable, escalation conditions, and stop
   condition. Include only necessary context; secrets and full private logs do
   not belong in the prompt by default.

```sh
opencode run --model "$MODEL" --format json \
  'Review the named module only. Do not edit. Return findings with file locations; stop if scope is unclear.' \
  > "$RUN_LOG" 2> "$RUN_ERR"
```

`RUN_LOG` and `RUN_ERR` should name distinct, access-controlled files for this
run. Set a process timeout in the calling harness. macOS does not provide a
standard `timeout` command; when needed, wrap the command with
`perl -e 'alarm shift; exec @ARGV' 600 opencode run ...`.

| Flag | Effect |
|---|---|
| `--model provider/model#variant` | Exact model and variant for this run; no separate V2 `--variant` flag |
| `--agent <id>` | Primary agent only; do not pass a subagent without verifying its mode (it may fall back to the default) |
| `--format json` | JSON-lines events for structured capture; not one final JSON object |
| `--title <text>` | Name the session |
| `--file <path>` | Attach a file; check its sensitivity and location first |
| `--thinking` | Print thinking blocks when appropriate; logs may become sensitive |
| `--standalone` | Use a private server instead of the shared background service |
| `--auto` | Approve `ask` decisions, **not** explicit denials; only for a user-authorized scoped run |

Do not use legacy `opencode export`, `opencode models --verbose`, `--dir`,
`--variant`, or V1 permission syntax. The current export command is
`opencode session export <id> --sanitize`.

## Models and money

Select a currently available model, not a historical alias. The local
2026-09-28 favorite snapshot included `openai/gpt-6-sol`,
`openai/gpt-6-luna`, `opencode-go/qwen3.8-flash`,
`opencode-go/glm-5.3-flash`, `opencode-go/deepseek-v4.1-flash`, and
`opencode-go/muse-spark-1.3-contributor`. The temporary
`opencode-go/space-bunny-free` alias may disappear. Check each ID and its
variants with `/api/model` before relying on it. A fast/priority provider
route is not automatically equivalent to the standard route.

```sh
opencode api get /api/model | jq -r '.data[] | [.providerID + "/" + .id, ([.variants[]?.id] | join(","))] | @tsv'
```

The catalog's listed cost is not proof of the user's billing terms or a
hard spend cap. DeepSeek Flash showed a nonzero listed rate in the 2026-09-28
snapshot; do not call it free. Small live checks then took 2–4 seconds on
DeepSeek/Muse and 24 seconds on GLM, but latency and prices are not guarantees.
Set a short packet and deadline for small checks, inspect provider costs where
possible, and never assume `--auto` limits spending.

## Claude models (claude-code provider)

The `@openchamber/opencode-claude` plugin (listed in
`~/.config/opencode/opencode.jsonc`) adds a `claude-code` provider that runs
Claude through the user's Claude plan. Checked on 2026-09-30 with
`/api/model`; IDs and variants can change, so recheck before use.

| Model ID | Variants |
| --- | --- |
| `claude-code/claude-sonnet-5-5` | `low,medium,high,xhigh,max` |
| `claude-code/claude-opus-5-5[1m]` | `low,medium,high,xhigh,max` |
| `claude-code/claude-haiku-4-5-20251001` | none |

Other IDs were also listed (Fable 5.1, Sonnet 5, Opus 4.x, Sonnet 4.6). Quote IDs
that contain `[1m]` so zsh does not treat the brackets as a glob. The `[1m]`
suffix is the 1M-token context build. Sonnet 5.5 has a plain ID; Opus 5.5 is only
listed with `[1m]`.

```sh
# MODEL and EFFORT come from the briefing's Claude Code bridge row.
opencode run --standalone --model "claude-code/$MODEL#$EFFORT" --format json \
  'bounded packet here'
# Opus needs its bracketed ID, quoted: 'claude-code/claude-opus-5-5[1m]#<effort>'
```

Reasoning levels, lowest to highest effort: `low`, `medium`, `high`, `xhigh`,
`max`. Higher levels think longer and cost more. Use `#variant` after the model ID.
Haiku 4.5 has no variants.

**Cost rule (user decision, 2026-09-30).** Claude models are expensive and draw
down the user's Claude plan limits.

- Pick the Claude model and effort from the Claude Code bridge row in
  `~/agents/ai-models/delegation-briefing.md` (section 4).
- Anything above that row's default needs the user's explicit approval for that
  task.
- Never use Fable or older Opus without explicit approval. Prefer cheaper
  OpenCode Go models when the briefing says they are good enough.

Live check on 2026-09-30: the Sonnet 5.5 `low` run reached Claude but returned
`provider.quota` (HTTP 402, "out of extra usage"). The route works when the plan
has quota. On that error, stop and tell the user; do not retry in a loop or switch
to a pricier model.

## Permissions and subagents

Ordinary OpenCode permissions apply to the child. `--auto` turns `ask` into
approval; configured `deny` rules and higher-level policies still block calls.
Persistent routine permissions now follow the owner-approved
`~/agents/conventions/autonomous-task-permissions.md` (2026-09-30).
Each harness audits and repairs its own obsolete ask/deny settings within that
authorization; deliberate exclusions remain. This machine's persistent root and
default/high worker permissions were repaired on 2026-09-30. Routine work no
longer needs `--auto`; a fresh `--standalone` run without it passed local read/write,
shell, public HTTP and Parallel MCP search. Both high workers passed their scoped
checks. Default Luna workers remain static-only pending version confirmation.
`--auto` remains a supported bridge option, but must not mask persistent-default
verification. **Host access is not a sandbox or new task authority.** Environment
file safeguards still ask; excluded Firecrawl tools and leaf delegation still deny.

Default: block child subagents, especially for parallel runs. V2's action is
`subagent`, and V2 config uses the **`permissions` array**. A private server is
necessary for a per-process config override; the shared service will not read
the launching process's environment override.

```sh
OPENCODE_CONFIG_CONTENT='{"permissions":[{"action":"subagent","resource":"*","effect":"deny"}]}' \
  opencode run --standalone --model "$MODEL" --format json \
  'You are one worker. Do not start subagents or other AI CLIs. Review only the named files.' \
  > "$RUN_LOG" 2> "$RUN_ERR"
```

The 2026-09-29 local `--standalone` config inspection confirmed that this
override loads as a V2 document with the deny rule. A live subagent-denial
smoke with the **new** syntax was not performed; the earlier 2026-09-28
live check used the obsolete V1-shaped `permission` object and does not prove
the current example blocks a live child. Verify the deny in a safe smoke before
high-volume fan-out. The V2 permissions reference establishes the action and
rule semantics. The `task-opencode` skill and
[worker policy](../../roles/task-worker-tiers.md) own when delegation is
allowed. For an authorized delegation-requiring skill, omit the deny override
and state the maximum child count in the packet. Do not recursively call
another AI CLI unless the user explicitly asked for that chain.

## Parallel checks and web tools

For a batch of independent read-only checks, start one short packet per run,
with separate logs and a bounded number of concurrent processes. The caller
merges and checks the answers. A 2026-09-28 test launched ten short runs and
all returned in about seven seconds, but that is a dated performance result,
not a standing concurrency budget. Never run two mutating children in one
checkout, and always block subagents in a parallel child.

Tell a child to run long scripts in the foreground and not to end its turn
until its output is written. On 2026-10-07 a GLM 5.3 Flash child started its
script with `nohup ... &`, ended its turn, and the script died with the
session after one request; resuming with `--session` and a foreground rule
fixed it. Also say "Do not run git": children have committed on their own.

The current OpenCode adapter maps Parallel, Exa, and Firecrawl MCP servers.
Parallel search/fetch and Firecrawl search/scrape were tested on 2026-09-29;
Exa search also worked headlessly. These are host-specific connections and
may not exist on another machine or location. Use the shared
[web reference](../web/README.md) for tool choice and
[connector registry](../connectors.md) for provider posture; this bridge
does not enable connectors or authorize extra spend. OpenCode's native
`websearch` is disabled on this machine; native `webfetch` remains available.

## What to check afterward

Use [sessions.md](sessions.md) to capture session ID, inspect events and
pending requests, answer a question, resume, or cancel. A zero CLI exit code
is not proof that the child completed the requested work. Review the answer,
diff, tests, unexpected tool calls, and unresolved questions. Report exact
model/variant, primary agent, session ID, approval mode, subagent policy,
edits/tests, and any incompleteness. Host-specific skill enablement belongs
to each caller's own adapter, not this capability guide.
