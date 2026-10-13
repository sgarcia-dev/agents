---
created_at: 2026-09-29
updated_at: 2026-10-05
model: openai-codex/gpt-6.1-sol
doc_type: capability-reference
purpose: Launch, supervise and resume a bounded local Hermes CLI task.
related:
  - path: ~/agents/capabilities/hermes.md
    why: Capability and model policy.
  - path: ~/agents/capabilities/hermes/STATE.md
    why: Dated smoke results.
---

# Hermes CLI handoff

## Preflight

Run `command -v hermes`, `hermes --version`, `hermes chat --help` in the caller's
actual environment. On the tested Mac the executable resolves to
`~/.hermes/hermes-agent/.hermes/bin/hermes`. A caller with a filtered
PATH may need that verified absolute executable. Do not assume another host has
it. Use a trusted executable, correct profile and provider login; never ask for
provider credentials in task text. CLI does not require the gateway to be running.

Use `hermes -p <profile> chat ...` only for an explicitly selected existing
profile. The default profile is the current tested route. Another profile has
its own config, skills, memory, sessions and credentials.

## One bounded task

The caller creates a UTF-8 packet file first and supplies the four absolute paths
below. Use a scratch directory for read-only probes or an approved repo/worktree
for editing. Capture logs privately, not automatically in the shared workspace.

Model values below are from the briefing's Hermes row in
`~/agents/ai-models/delegation-briefing.md`. Read that row before
launching; examples show flag syntax, not a separate model choice.

```bash
hermes chat \
  --query-file "$PACKET" \
  --oneshot --format stream-json \
  --provider openai-codex --model gpt-6-sol --reasoning medium \
  --in "$WORKDIR" \
  --toolsets terminal,file \
  --max-turns 20 --run-budget 180 \
  --source tool \
  > "$EVENTS" 2> "$ERRORS"
```

- `PACKET`: caller-authored task instructions, context and authorized scope.
- `WORKDIR`: exact execution directory; inspect branch/diff before repo edits.
- `EVENTS`: output JSONL path; `ERRORS`: stderr path. Avoid reusing another job's
  files. Supervise this process with an outer deadline too.
- Take model and effort from the briefing's Hermes row. Do not change global config.
- Toolsets are task-dependent: `terminal,file` for local coding/data tasks;
  `web` for public retrieval; `browser` for explicitly scoped browser work;
  `skills` when loading a Hermes skill is necessary. Verify installed names and
  actual tools. `--skills <name>` preloads a Hermes-discoverable skill, not an
  arbitrary skill from the caller's registry. Include workspace skill paths in
  the packet when explicit reads are needed.
- `--max-turns` caps tool-calling iterations, not conversation count or spending.
  `--run-budget` is the agent's wall-clock budget, not a hard kill boundary.
  Cancel and account for outstanding tools/child processes on an outer timeout.
- `--source tool` tags the integration session; it is not a privacy or permission
  boundary.

For short text output use `--oneshot -Q -q "bounded task"` instead. For arbitrary
text use `--query-file` or `--query-file -` with stdin: do not interpolate raw
user content into a shell command.

**Do not use top-level `hermes -z` as the safe handoff shortcut.** The installed
help says that mode automatically bypasses approvals. `hermes chat --oneshot`
is different. Do not add `--yolo` or `--accept-hooks` by default. Existing host
approval policies still matter, and non-TTY prompts can block a job.

## Supervision and Acceptance

JSONL from the tested route contains `system`/`init` with `model` and `session_id`,
`tool_use`, `tool_result` with `is_error`, streamed `text`, and a final `result`
with `exit_code`, final `text`, usage and duration. Parse lines, do not mistake a
text delta or commentary for the terminal result. Inspect nested tool results
for nonzero exits/errors and compare the final output against acceptance checks.
For a tool-dependent task require actual successful tool events.

Initialization reports the selected model; it does not expose all final provider
or fallback telemetry. Use available run/session metadata, logs and caller-side
launch records; mark missing fields, never accept the model's self-identification
as proof. The dated smoke also read the exact session's model/effort metadata.

Stored session metadata can describe the original launch, not the latest
resumed turn. The tested low-to-medium follow-up still stored the initial low
metadata; do not use it to attest a resumed turn's effort. A fresh medium session
independently recorded medium. Distinguish requested settings from observed
per-turn runtime when telemetry is absent.

Prompts are not a sandbox. `--in`, `--worktree` and `--toolsets` do not provide
OS containment; MCP/plugin tools and host integrations may have separate
availability. Narrow enabled tools where supported, prohibit further delegation
unless specifically authorized in the packet, and use an externally isolated
runner/profile for a genuinely untrusted job. A different profile does not
isolate host filesystem permissions.

## Child Monitoring and Benchmarks

The October 5 finite one-shot route joined its native child synchronously: the
parent investigated afterward, not concurrently. A multi-child batch can still
run children in parallel, but this is not parent/child overlap. Interactive
completion-consumer sessions have a different lifecycle. For persistent external
monitoring, consult the existing
[runs API guide](api.md#long-tasks-approvals-and-cancellation)
and its untested-control limits; do not promise automatic crash recovery.

- Enable the `delegation` toolset only when native children are authorized.
  Preserve parent/child IDs from dispatch and verify their linkage in exact
  session records. A child receipt exposed model, API-call count, token usage,
  duration, tool trace, cost status and a live-transcript path. Use that exact
  private path for child content rather than scanning unrelated sessions.
- Later machine events, including the terminal result, appeared on stderr in
  this test. Capture both stdout and stderr and attempt JSON parsing of each
  line; retain non-JSON stderr separately as diagnostics. Deduplicate event/tool
  IDs when present and mark coverage uncertain if identifiers are missing.
  Do not assume every stderr line is JSON or that stdout alone contains usage.
- Reconcile receipt and session-store counters before summing. The tested child
  receipt's input included cache-read tokens, while the database stored input
  and cache-read separately. Do not add cached input twice. Keep root and child
  accounting separate and do not treat a repeated summary as new usage.
- Preserve billing status with numeric cost: zero plus `cost_status: unknown`
  is unknown, not free. The root's subscription-included status does not establish
  the child's charge. Full per-response timing and effective context capacity
  were not verified; tool/child durations are not whole-task duration.
- Durable completion delivery is not durable child execution. Loss of the
  owner process does not automatically resume an executing child; this run did
  not test API stop, crash recovery or live child-log polling.

For a benchmark, record installed version, requested/observed runtime, route,
profile, parent/child IDs, caller-measured monotonic launch-to-exit seconds, first
visible content latency, reconciled token categories, separate billing statuses
and acceptance result. Effective task output tokens/s is deduplicated root plus
child output divided by whole-task seconds, not generation speed. Record missing
capacity or response timing as unknown, not inferred from cumulative usage.
Verify required child completion and promised outputs/checks independently of the
CLI's terminal result. Keep transcript pointers/content private and task-scoped.

Verified on Hermes 0.21.5+7324.g33c9b1d, 2026-10-05: see the
experiment and stream/accounting limits (private, not published).
The channel defect's cause remains unknown; this documentation does not repair
the runtime or install a collector/automatic benchmark runner.
Use equivalent packets and runtime settings for comparisons; prefer fresh sessions.
If resuming, record usage baselines and per-turn versus cumulative semantics first.

## Follow-ups

Save the exact `session_id`, then submit a new packet with the same explicit
model/provider/effort and limits:

```bash
hermes chat --resume "$SESSION_ID" --query-file "$FOLLOWUP" \
  --oneshot --format stream-json \
  --provider openai-codex --model gpt-6-sol --reasoning medium \
  --in "$WORKDIR" --max-turns 20 --run-budget 180 --source tool
```

Alternatively `--continue "unique-job-name" --create-if-missing` uses a named
conversation. Never use bare `latest` for an integration: it may select another
job. Do not resume an active Discord/Telegram/UI session from a second process.
Fresh sessions need explicit context; saved history can contain sensitive data.
Parallel repo edits need separate worktrees/owned paths and exact session IDs.
Browser account writes remain serialized under the shared browser-use spec.

The CLI supports an input image via `--image /absolute/image-path`. Document
creation and other file tasks should identify host-readable input/output paths;
remote callers cannot assume their files exist on the Hermes machine.
