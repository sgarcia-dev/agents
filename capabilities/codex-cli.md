---
created_at: 2026-09-28
updated_at: 2026-10-05
model: gpt-6-sol
doc_type: capability
purpose: Describe Codex CLI as a bounded local execution bridge for other AI harnesses.
related:
  - path: ~/agents/capabilities/connectors.md
    why: Portable awareness inventory of external bridges.
  - path: ~/agents/skills/task-codex/SKILL.md
    why: Procedure for a non-Codex caller.
---

# Codex CLI bridge

Another harness can start a bounded Codex session with `codex exec`. The caller
owns authorization, scope, monitoring, and review. Codex owns its model, tools,
skills, and session in the selected folder. This is a local CLI bridge, not an
MCP connector or a native subagent. Caller permissions and context do not carry
over.

- **Best for:** current public web search and source-grounded synthesis; Google
  account work when the specific CLI session has a connected app; and focused
  work on the user's four preferred Sol/Luna models. A 2026-09-28 CLI smoke
  used live search and returned Reddit URLs. On 2026-09-29 its page reader
  also read Reddit threads with replies and handles in 2 of 2 runs, the only
  tool tested that could; X returned 403 and Bluesky was refused. This is
  observed behavior, not a documented feature. See
  `~/agents/capabilities/web/README.md`.
- **Account connections:** the same smoke successfully called Gmail
  `list_labels` for `INBOX` and Google Drive `get_profile` without reading
  messages or files. Account access depends on login, installation, and session
  scope. The caller must check it for each task. `codex mcp list` alone does not
  show these app connections.
- **Web search is not sandboxed.** `--search` runs on OpenAI's side and works
  under every sandbox mode. The sandbox limits only the child's own shell:
  `read-only` has no shell network. For packets that need shell HTTP too, use
  `--sandbox workspace-write -c sandbox_workspace_write.network_access=true`
  in a scratch folder. A 2026-09-29 test on 0.158.0 got both `curl` (HTTP 200)
  and web search in one run.
- **Persistent defaults (September 30 migration):** local Codex 0.159.0 now saves
  `approval_policy = "never"` and `sandbox_mode = "danger-full-access"` for root
  sessions and all four maintained default/high worker files. Fresh `codex exec`
  runs can use these defaults without bypass flags. Callers on another installation
  must verify its effective settings. Task scope and explicit cross-provider
  authorization still apply.
- **Permissions:** full bypass, `--dangerously-bypass-approvals-and-sandbox`
  (also `--yolo`), is the **default for every delegated run** (user decision,
  2026-09-30; web search hand-offs already used it since Sept 29). A sandbox
  (`--sandbox read-only`, or `workspace-write` with `-c approval_policy=never`)
  is used only when the user asks or the permission convention identifies concrete
  high-risk work. See `task-codex` step 7 and
  `~/agents/conventions/autonomous-task-permissions.md`.
- **Browser and computer use (added 2026-09-29):** the sandbox does not
  cover Codex's bundled computer-use and browser plugins. In a 2026-09-29
  read-only research run, web search worked, but the packet also asked for a
  `curl` probe, which the read-only shell could not make. The child worked
  around it by driving the user's Chrome and reading a terminal window's
  accessibility tree. Give network to the shell on purpose (above) instead. For
  research and review packets, turn these routes off per run with
  `--disable plugins --disable apps --disable computer_use --disable browser_use --disable browser_use_external --disable in_app_browser -c 'mcp_servers.node_repl.enabled=false' -c 'mcp_servers.computer-use.enabled=false'`. The two server names come from this Mac's config. Do **not** add
  `--disable code_mode_host`: in CLI 0.158.0 it carries the shell and web
  search, every tool call then fails, and some children invent a full report
  anyway. Also tell the child: "no browser or GUI tools; if a check is
  blocked, write could not verify."
- **Subagents:** a CLI child can delegate. Block by default with
  `--disable multi_agent`; see `../roles/task-worker-tiers.md` for the narrow
  exceptions and count accounting.
- **Known launch issues (seen 2026-10-02, CLI 0.159.0, from Claude Code).**
  Fix these only if you hit them; the normal launch needs no change.
  - If a background run fails with `Failed to read prompt from stdin`, the
    child was waiting for extra typed input that never came. Add `</dev/null`
    to the end of the command so it starts at once with just the prompt.
  - If a `--sandbox` run outside a Git repository fails with `Not inside a
    trusted directory`, add `--skip-git-repo-check`. `--yolo` runs did not hit
    this.
  - Under `--yolo`, the JSONL log can hold `"type":"error"` items saying
    `--dangerously-bypass-hook-trust` is enabled. These are warnings, not
    failed tool calls; do not reject a run for them.
- **Verification:** capture JSONL events, final response, thread ID, actual
  tool calls, and repository diff. Connector and model availability may differ
  between the parent Codex session, CLI root, and native child.

## Parent/child inspection and benchmarks

`codex exec --json` remains the simple launch/capture route. In the October 5
test it omitted collaboration calls and child usage present in saved records;
the parent's claim that these metrics were unavailable was not authoritative.
When authorized children need inspection, retain the exact root thread ID and
use read-only app-server queries plus parent-linked saved rollouts.

The tested transport was `codex app-server --stdio`, with newline-delimited JSON
requests on stdin and responses on stdout. After the `initialize` response, send
the `initialized` notification. Example protocol shapes (substitute exact IDs):

```json
{"id":1,"method":"initialize","params":{"clientInfo":{"name":"task-monitor","version":"1.0"},"capabilities":{"experimentalApi":true}}}
{"method":"initialized"}
{"id":2,"method":"thread/read","params":{"threadId":"ROOT_THREAD_ID","includeTurns":true}}
{"id":3,"method":"thread/list","params":{"limit":20,"parentThreadId":"ROOT_THREAD_ID"}}
```

Match replies by request ID, account for interleaved notifications and follow
pagination when more children exist. Read each returned child's exact thread ID
with `includeTurns: true`; verify its parent link, native role, model/effort and
completion. Inspect the thread's saved rollout for response usage and executed
tool records. Schema and record paths are version-dependent: inspect returned
fields rather than inventing missing metadata. Keep content and rollouts private,
query only this task, and close/reap the readback server afterward.

- This procedure verified **post-run readback**, not live child subscriptions
  or an app-server-launched turn. Live steer/interrupt and token notifications
  are documented in the [app-server contract](https://developers.openai.com/codex/app-server)
  but were not exercised here. Do not advertise tested live control from this run.
- Reconcile response IDs and final usage snapshots within each thread before
  aggregating parent and children; repeated cumulative usage is not additive.
  Keep cached input, output and reasoning categories as emitted. Reasoning was
  included within output in this test, not an extra output amount to add again.
- Label outer tool invocations separately from nested commands/collaboration
  operations. A single outer invocation can contain several operations.
- Last-request input divided by exposed effective capacity is an occupancy
  proxy, not guaranteed remaining context. Cumulative input across responses
  must not be divided by a context window. Record missing capacity as unknown.
- No task dollar figure was exposed in this subscription test. Quota is not
  dollars; unknown cost is not zero or an invented API-price bill.

For benchmarks, record installed version, requested/observed runtime, root/child
IDs, caller-measured monotonic launch-to-exit seconds, first event/content times,
reconciled token categories and separately labeled tool counts. Effective task
output tokens/s is deduplicated parent plus child output divided by whole-task
seconds, not model generation speed. Per-response latency needs timestamped
request/response records; report incomplete coverage. Accept only after required
children complete and the promised outputs/checks pass, not merely a clean exit.

Verified on Codex 0.160.0, 2026-10-05: see the
experiment and measurement limits (private, not published).
No controller or automatic benchmark runner is installed by these instructions.
Use equivalent packets and runtime settings for comparisons; prefer fresh threads.
If resuming, record usage baselines and per-turn versus cumulative semantics first.

Read the linked guide before launching. Host-specific skill discovery belongs
to each caller's own adapter, not this capability file.
