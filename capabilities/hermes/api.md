---
created_at: 2026-09-29
updated_at: 2026-10-01
model: openai-codex/gpt-6.1-sol
doc_type: capability-reference
purpose: Call Hermes's existing authenticated HTTP agent API with explicit runtime and scope.
related:
  - path: ~/agents/capabilities/hermes.md
    why: Capability and authorization boundaries.
  - path: ~/agents/capabilities/hermes/STATE.md
    why: Running-service proof and gaps.
---

# Hermes HTTP API

## Preflight and Authentication

The tested local base is `http://127.0.0.1:8642/v1`. The gateway must be running
and the Mac awake. Another machine cannot use this loopback URL directly.
Do not expose the full agent API publicly or repurpose a frontend's port as the
agent API. Use an explicitly authorized authenticated service/tunnel for remote
callers. This guide does not enable that deployment.

Authenticate with `Authorization: Bearer <API_SERVER_KEY>`. Obtain only this
credential through the owner's secure environment/vault handoff. Do not print it,
copy the entire Hermes `.env`, write it to the shared repo, or pass it in task
content. A token authorizes access to a write-capable host agent, not task scope.

Read `GET /health` for liveness, then authenticated `GET /v1/capabilities` and
`GET /v1/toolsets`. `/health` alone proves neither provider readiness nor working
browser/account access. Inspect enabled/configured/tools per toolset; verify the
job-specific backend. Use `GET /v1/skills` only if it works; the dated local probe
returned HTTP 500. Fall back to an authorized `hermes skills list --enabled-only`
on the host or a bounded skills-list task, not a fabricated catalog.

## Explicit Model Selection

Model values below are from the briefing's Hermes row in
`~/agents/ai-models/delegation-briefing.md`. Read that row before
launching; examples show request syntax, not a separate model choice.
Send explicit fields on every request, including continuation:

```json
{
  "model": "gpt-6-sol",
  "provider": "openai-codex",
  "model_options": {"reasoning_effort": "medium"}
}
```

Take model and effort from the briefing's Hermes row. Sending only `model` can
be ignored by the OpenAI compatibility endpoints unless `direct_model_requests`
is enabled. Sending the
explicit `provider` avoids that bare-model ambiguity. An existing session model
override wins over request selection; a configured model-route alias wins next.
A conflicting provider/alias can return HTTP 400. Use a fresh conversation or an
authorized model switch rather than guessing an existing session's lock.

`GET /v1/models` lists stable agent aliases, not every available underlying model.
`GET /api/model/options` is the documented authenticated richer catalog. Check
chosen provider credentials in Hermes before choosing another exact pair.
`model_options.service_tier` exists for supported providers; do not request a
premium tier by default. Do not change global defaults for an integration.

## One Task and Multi-turn

This Python example expects a securely supplied `API_SERVER_KEY` and an existing
UTF-8 `PACKET` file, and prints a response that may contain private task data.
Keep stdout private. The caller must impose its own deadline and stop policy.

```python
import json, os, urllib.request
from pathlib import Path

base = os.environ.get("HERMES_API_BASE", "http://127.0.0.1:8642/v1").rstrip("/")
body = {
    "model": "gpt-6-sol",
    "provider": "openai-codex",
    "model_options": {"reasoning_effort": "medium"},
    "input": Path(os.environ["PACKET"]).read_text(),
    "store": True,
    "stream": False,
}
request = urllib.request.Request(
    base + "/responses", data=json.dumps(body).encode(),
    headers={"Authorization": "Bearer " + os.environ["API_SERVER_KEY"],
             "Content-Type": "application/json"}, method="POST",
)
with urllib.request.urlopen(request, timeout=180) as response:
    result = json.load(response)
print(json.dumps(result))
```

Capture `id`, status, output and usage. A stored response can be verified by
`GET /v1/responses/{id}`. For a follow-up add `previous_response_id` with that
exact ID and a new `input`, retaining the explicit model fields. Alternatively
use a unique `conversation` name for automatic latest-response chaining.
These create/continue an API conversation, not this Discord thread.

Chat Completions uses `POST /v1/chat/completions` with a `messages` array and
client-managed history instead of `input`. Responses stores tool history for
continuation. Returned Responses `function_call` items are already executed by
Hermes; never execute them again in the caller. Inline images are supported;
ordinary document uploads/file IDs are not supported on these compatibility
endpoints. Transfer files through a separately authorized route or give a
host-readable path. Do not assume advertised browser-artifact routes are enabled.

## Long Tasks, Approvals and Cancellation

Prefer `POST /v1/runs` with `input` and the explicit model fields for a task that
needs a run handle, progress, approval relay or reliable cancellation. An optional
exact `session_id` continues the selected session; do not target someone else's
active chat. For safely retryable run creation, use one unique `Idempotency-Key`
per payload when the running service advertises support.

- `GET /v1/runs/{run_id}` reads current status and result.
- `GET /v1/runs/{run_id}/events` subscribes to SSE tool/run/approval events.
- `POST /v1/runs/{run_id}/stop` requests interruption. Wait for work to settle;
  HTTP timeout or closing an SSE socket does not cancel an agent run.
- `POST /v1/runs/{run_id}/approval` relays a human decision using the running
  service's schema. Never auto-approve unrelated requests or grant always-allow
  merely because the caller is another agent.
- Session REST endpoints support metadata, history, fork and chat/stream for
  purpose-built hosts. Listing/reading unrelated sessions requires separate scope.

Check exact schemas on the running service before implementing these controls.
They were advertised but not task-tested in this documentation pass. Prompt
iteration/time limits are not a technical API sandbox. Do not invent a CLI-like
`toolsets` or `run_budget` field without confirming the endpoint accepts it.
A persistent scheduled task requires explicit schedule/permissions/delivery
scope; a synchronous API call is not durable scheduled execution.

## Verification and Known Differences

Check real terminal status and tool outcomes, not HTTP 200 alone. `completed`
with a plausible answer does not prove a tool-dependent acceptance criterion.
Modern docs describe a `runtime` field showing served provider/model and fallback
selection; if present compare it to requested values. The tested local Responses
reply omitted `runtime`, so its echoed `model` does not prove the effective
provider or reasoning level. Report that telemetry gap rather than claiming
exact runtime verification. A harmless CLI route offers independently observed
model/effort metadata on this installation.

`X-Hermes-Session-Id` is a transcript continuity header; `X-Hermes-Session-Key`
is a memory-provider scope hint, not a security boundary or arbitrary access to
another conversation. Keep default-profile memory and unrelated transcripts out
of jobs that do not need them. Use an explicitly approved separate profile for
isolation requirements; it is still not OS containment.

[Official API reference](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server)
is the feature reference. Live capabilities and successful calls govern whether
this running gateway actually exposes a feature. Never silently restart it to
make newer source behavior match documentation.
