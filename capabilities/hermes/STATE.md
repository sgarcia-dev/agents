---
created_at: 2026-09-29
updated_at: 2026-10-05
model: openai-codex/gpt-6.1-sol
doc_type: state
status: CLI task and synchronous child verified; stream-channel defect observed; HTTP response and MCP discovery verified; API controls untested
scope: Hermes cross-harness capability on the owner's Mac
related:
  - path: ~/agents/capabilities/hermes.md
    why: Portable capability entrypoint.
  - path: ~/agents/skills/task-hermes/SKILL.md
    why: Caller procedure and model preference.
---

# Hermes capability status

## Verified 2026-09-29

- Installed help/version: `Hermes Agent v0.21.5+4681.g7968c72 (2026.9.24)`,
  upstream `7968c72a`. Actual CLI path:
  `~/.hermes/hermes-agent/.hermes/bin/hermes`.
- Local CLI handoff with explicit `openai-codex`, `gpt-6.1-sol`, `low`, terminal
  toolset, four-iteration cap and 100-second agent budget completed in 11.2 s.
  Structured init named `gpt-6.1-sol`; a real `pwd` tool_result had exit 0 and
  `is_error:false`; final result had exit 0 and `HERMES_TASK_SMOKE_OK`.
  Exact session: `20260929_224055_57ac56`. Read-only exact-session metadata
  independently recorded model `gpt-6.1-sol` and reasoning effort `low`.
  Provider was explicitly requested; CLI events did not expose served-provider
  or fallback telemetry. This proves a bounded local task, not all integrations.
- Fresh medium-effort CLI smoke completed with `HERMES_MEDIUM_SMOKE_OK`.
  Exact session `20260929_225325_2ba6f8` recorded `gpt-6.1-sol` and medium
  effort in independently read session metadata. No tools were requested there.
- Exact-session CLI continuation retained the earlier successful working-directory
  result and returned `HERMES_CLI_CHAIN_OK`. Medium was requested for that turn;
  stored session metadata still reflected its original low-effort launch. Do not
  treat an existing session's launch metadata as per-turn effort telemetry.
- API at `http://127.0.0.1:8642/v1`: health HTTP 200; authenticated capabilities,
  models and toolsets succeeded; auth advertises required bearer token.
- `POST /v1/responses` with `gpt-6.1-sol`, `openai-codex`, low effort returned
  `status:completed` and `HERMES_API_SMOKE_OK`. Exact stored response was read
  back successfully: `resp_24d9182857164e969b984b7944d7`. No task tools were
  requested in this HTTP smoke. No `runtime` field was returned: effective
  provider/model/effort cannot be independently asserted from its model echo.
- HTTP follow-up with `previous_response_id` recalled the preceding marker and
  returned `HERMES_API_CHAIN_OK`. Exact follow-up response readback succeeded:
  `resp_4e8c70cfb46242b9b12689f9a4cc`. No task tools were requested.
- Native `hermes mcp serve`: real stdio initialize and tools/list succeeded.
  Server name `hermes`, protocol `2025-11-25`; ten discovered tools documented
  in the MCP guide. No conversation content read, message sent or approval
  granted. The initial probe's client serialization failed because MCP SDK 2
  uses `server_info`, not `serverInfo`; alias-aware model_dump fixed the probe.
  That was a probe bug, not a Hermes server failure.

## Current Monitoring Verification

The 2026-10-05 test on Hermes 0.21.5+7324.g33c9b1d completed one native child
with a model/usage/duration/tool-trace receipt and parent-linked session records.
The one-shot route joined synchronously, so parent/child overlap was not verified.
Later structured events reached stderr, including the final result: stdout-only
capture is insufficient on that tested route. Cause unknown; no runtime fix applied.
Input/cache conventions differed between receipt and database; a numeric zero
child cost accompanied by unknown billing status must not be reported as free.

Use the [CLI monitoring/accounting instructions](cli.md#child-monitoring-and-benchmarks)
for future measurements and the
dated investigation (private, not published)
for evidence. API stop/steer, crash recovery and live child-log polling remain
untested here. Documentation now covers benchmark measurements; no benchmark
runner, collector, new service or native settings change was introduced.

## Inventory, not task proof

Live API enabled toolsets: `web`, `browser`, `terminal`, `file`,
`code_execution`, `vision`, `image_gen`, `skills`, `todo`, `memory`,
`session_search`, `connections`, `delegation`, `cronjob`.

Live API disabled toolsets: `video`, `video_gen`, `x_search`, `tts`, `stt`,
`kanban`, `context_engine`, `clarify`, `homeassistant`, `spotify`, `discord`,
`discord_admin`, `yuanbao`, `computer_use`, `a2a`. `homeassistant` also reported
unconfigured. The API reported browser-extension control disabled. These flags
are not proof that enabled browser/account/media backends can execute; CLI and
Discord toolsets can differ. Never copy this dated list into caller tool schemas.

API advertises runs/status/events/stop/steer/approvals/session control and model
options; these controls were not exercised. Jobs-admin, config-write and direct
memory-write API feature flags were false. Tool-enabled cron is a separate
surface, not proof jobs CRUD is ready.

## Known gaps and next verification

- Authenticated `/v1/skills` returned HTTP 500 despite advertising skills API.
  Use the fallback in the API guide. No gateway fix/restart attempted.
- No listener answered on A2A's default loopback port 9900. A2A enablement on a
  nondefault route was not audited; do not claim A2A ready or globally absent.
- Run cancellation/approval, named-conversation routing, MCP sends/history reads
  and account-only browser/API work were not task-tested
  in this pass. ACP/TUI/library routes remain documentation-level only.
- No caller-native config was edited; no Claude Code/Codex/OpenCode adapter sync
  was run. No new profile/server, API credential, permission, global model default
  or persistent scheduled job was created.
- Re-probe in the target caller/session before relying on a route. Account access,
  OS consent, awake host and the selected profile/controller are separate gates.

Raw harmless smoke events and discovery responses remain in local scratch under
`~/.hermes/cache/scratch/task-hermes-verification/`; scratch is
prunable, not a durable source dependency. This file retains the substantive
verification results without credentials, private transcripts or account data.
