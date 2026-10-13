---
created_at: 2026-09-29
updated_at: 2026-10-05
model: openai/gpt-6-sol
doc_type: capability
purpose: Supervise, resume, and verify an OpenCode V2 CLI child session.
related:
  - path: ./cli.md
    why: Launch settings, permissions, costs and scope.
  - path: ./STATE.md
    why: Current bridge status.
  - path: ../../skills/task-opencode/SKILL.md
    why: Caller procedure and stop conditions.
---

# Supervise an OpenCode child

`opencode run --format json` writes JSON-lines events, not a single result
object. Store stdout and stderr separately, keep the owning process handle,
and wait for its exit. A quiet log is not a completion receipt. Session and
server API data may contain private prompts or file content; keep logs private.

```sh
opencode run --title 'bounded-check' --model "$MODEL" \
  --format json 'One bounded packet and stop condition' \
  > "$RUN_LOG" 2> "$RUN_ERR"

jq -r 'select(.sessionID) | .sessionID' "$RUN_LOG" | head -1
jq -c 'select(.type == "text" or .type == "tool" or .type == "step_start")' "$RUN_LOG"
opencode session list --format json
opencode session export "$SESSION_ID" --sanitize
```

The event stream carries event-specific `part` fields. A small 2026-09-28 run
emitted `step_start` then `text`; do not rely on a fixed event sequence or a
terminal marker. Session listing is location-scoped and may omit children.
The API is experimental and responses can change; inspect their actual shape.
Use `opencode api` so local service discovery and authentication match the CLI.

```sh
opencode api get /api/session/active
opencode api get "/api/session/$SESSION_ID"
opencode api get "/api/session/$SESSION_ID/message?order=desc&limit=20"
opencode api get "/api/session/$SESSION_ID/form"
opencode api get "/api/session/$SESSION_ID/permission"
opencode api get "/api/session/$SESSION_ID/diff"
```

## Parent/child metrics and benchmarks

For authorized native children, obtain their exact session IDs from dispatch
results and verify the returned child session's `parentID` equals the root ID.
Do not assume the location-scoped session list contains every child. Apply the
existing `/api/session/$SESSION_ID` and message queries to each exact ID against
the same owning server; standalone/private servers are not the shared service.
The example message query above returns only 20 messages: paginate the full
task history before asserting complete tool or response counts.

- Session readback exposed model/provider/variant, outcome, token categories,
  cost and parent linkage. Messages and tool records exposed content and
  created/streamed/completed timestamps. Retain source fields and unique message
  and tool IDs so repeated events cannot inflate counts.
- Reconcile final usage/cost against **completed session counters**. CLI
  `step_finish` records omitted one root response in the October 5 test, so
  summing them understated cost. Parent and child accounting were separate;
  add each child once rather than assuming the root includes it.
- A completed tool state plus actual output establishes execution. A separate
  provider metadata flag such as `executed: false` did not negate successful
  tool execution in this test. Inspect tool failures and results, not one flag.
- Reported cost is model-price accounting, not proof of an actual subscription
  charge. Preserve billing basis and mark the billed amount unknown when absent.
- Message timestamps provide per-response timing proxies. A streamed block can
  arrive after generation; it is not necessarily the first generated token.
  Request input is not a context percentage without verified model capacity.

For a benchmark, record installed version, requested/observed runtime, exact
root/child IDs, caller-measured monotonic launch-to-exit seconds, first visible
content latency, per-message timings, reconciled token categories and cost basis.
The agent's prose can start its clock late: never use it for whole-task duration.
Effective task output tokens/s is deduplicated parent plus child output divided
by whole-task seconds, not generation speed. Record unavailable fields as unknown.

At acceptance, inspect root and required child outcomes, tool errors, pending
forms/permissions and promised outputs/checks. A successful session/process or a
busy stream alone does not prove the task met its criteria. Stored child readback
was verified; live child event subscription and cancellation were not tested.

Verified on OpenCode 2.0.22, 2026-10-05: see the
experiment and accounting reconciliation (private, not published).
The API remains experimental; check response shapes before a new benchmark.
These instructions do not install a collector or automatic benchmark runner.
Use equivalent packets and runtime settings for comparisons; prefer fresh sessions.
If resuming, record usage baselines and per-turn versus cumulative semantics first.

Use only the user's actual answer when a form asks for judgment. Inspect its
fields and allowed values before replying to that **same pending form**:

```sh
opencode api post "/api/session/$SESSION_ID/form/$FORM_ID/reply" \
  --data '{"answer":{"scope":"Only the parser module"}}'
```

For a pending permission request, inspect its action and resource first.
Reply `once` only when authorized for that request. `always` saves a broader
project-scoped approval; `reject` rejects pending requests in that session.
Configured denials cannot be overridden by replying or `--auto`.

```sh
opencode api post "/api/session/$SESSION_ID/permission/$REQUEST_ID/reply" \
  --data '{"decision":"once"}'
```

If the process ended and no request is pending, resume the **same** session
from the same location instead of blindly starting over:

```sh
opencode run --session "$SESSION_ID" --model "$MODEL" \
  --format json 'Here is the answer to your question; keep the original scope.'
```

`--continue` chooses the latest session in this project and is ambiguous with
parallel runs. `--fork` with `--session` branches deliberately. If a form or
permission is still pending, settle it rather than assuming a new turn will
unblock the run. If the original run used `--standalone` or a per-process
override, do not assume a new process reconnects to that private server or
inherits the override; inspect the session and effective policy first. For
long-lived two-way supervision, prefer the V2
[API](https://opencode.ai/v2/docs/api) or client over a one-shot CLI loop.

To interrupt an active session, use
`opencode api post "/api/session/$SESSION_ID/interrupt"` against the **same
server**, then terminate and reap the owning CLI process if necessary. Check
partial edits and logs before retrying; do not delete session data to cancel.

Accept only when the process finished, no question or permission is pending,
the answer actually addresses the packet, and the promised files and tests
check out. Inspect the repository diff even if the child says it made no edits.
State any incomplete or unverified step in the handoff.

## Permission migration evidence, 2026-09-30

Fresh root `ses_f0c78546affeTEpmw8MzNMMGNO` used `build` and
`openai/gpt-6.1-sol#high`, without `--auto` or permission overrides. Local
read/write, shell, public HTTP and one Parallel search passed. Native high leaves
`ses_f0c774126ffe295ecBChYDUHGu` (explore) and
`ses_f0c7615fcffeV6xdl5C8EEATSc` (execute) used their maintained wrappers and
`openai/gpt-6.1-sol#low`; their scoped checks passed sequentially. API readback
confirmed identities and empty pending permission lists. Default Luna cells were
not launched. Original implementation root `ses_f0c7cb8aeffevVNSL9j2aC4H7j`
hit the supervisor timeout and resumed only for evidence retention/documentation.
Durable private evidence is under
`~/.config/opencode/backups/permission-migration-260930/`.
