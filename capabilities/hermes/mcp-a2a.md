---
created_at: 2026-09-29
updated_at: 2026-09-29
model: openai-codex/gpt-6.1-sol
doc_type: capability-reference
purpose: Distinguish Hermes messaging MCP, agent-task A2A and other integration protocols.
related:
  - path: ~/agents/capabilities/hermes.md
    why: Shared capability entrypoint.
  - path: ~/agents/capabilities/hermes/STATE.md
    why: Tested MCP discovery and unverified protocols.
---

# Hermes MCP, A2A and other protocols

## Native MCP: messaging and conversation bridge

The installed CLI ships `hermes mcp serve`. It is a stdio MCP server, not just an
MCP client. Tested discovery returned ten tools:

- `conversations_list(platform?, limit?, search?)`: active conversation metadata.
- `conversation_get(session_key)`: one selected conversation's metadata.
- `messages_read(session_key, limit?)`: recent text history.
- `attachments_fetch(session_key, message_id)`: lists attachment metadata, not a
  promise to download its bytes.
- `events_poll(after_cursor?, session_key?, limit?)`: observed events and cursor.
- `events_wait(after_cursor?, session_key?, timeout_ms?)`: bounded long-poll.
- `messages_send(target, message)`: sends to a platform target.
- `channels_list(platform?)`: available delivery targets.
- `permissions_list_open()`: live approval requests observed by this bridge.
- `permissions_respond(id, decision)`: `allow-once`, `allow-always`, or `deny`.

The tested schemas contain **no** general `ask_hermes`/task tool, no model,
provider, reasoning or CWD fields. `messages_send` invokes the delivery tool; it
is not a direct prompt submission to Hermes. Whether a posted platform message
triggers a bot depends on platform routing/allowlists and cannot be assumed.
Use CLI/API/A2A for an agent task with model selection. Do not use a `/model`
message to change a user's live chat as a workaround.

Generic stdio configuration shape (translate into the caller's actual schema):

```json
{
  "mcpServers": {
    "hermes": {
      "command": "~/.hermes/hermes-agent/.hermes/bin/hermes",
      "args": ["mcp", "serve"]
    }
  }
}
```

The path is this Mac's verified executable, not a cross-platform install rule.
An explicitly selected profile can use args `-p`, `<profile>`, `mcp`, `serve`.
A local MCP subprocess accesses that profile's state and delivery credentials.
No HTTP API key in the example is needed for stdio; local process/filesystem
access itself is powerful. Read privileges expose sensitive conversation data.
Only enable the task-needed tools in the caller, if it can enforce filtering.
Do not give approval response or send access as a routine discovery default.
Require exact approved targets, avoid all-conversation reads, and verify message
writes through the exact recipient thread. Discovery alone proves neither
message delivery nor approval execution. A successful permission-tool call is
not human authorization. MCP does not expose every internal Hermes tool directly.

`/sync-tool-adapter` may document/configure this bridge only in the caller's own
run after selection. This task did not install it in any other harness. The
server is launched per MCP connection; it is not a new always-on network service.

## A2A: structured agent-to-agent tasks

Hermes's optional A2A plugin supports inbound and outbound tasks across process,
machine and framework boundaries. This is the protocol designed for asking a
peer agent to perform work, with task/context IDs, discovery, streaming and
cancellation. The default-port probe found no listener here; do not advertise it
as ready. See the [official A2A guide](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a).

After explicit owner selection, `hermes gateway setup` can enable A2A. A
separately enabled `a2a` toolset provides `a2a_discover`, `a2a_call`, `a2a_list`,
`a2a_history`, `a2a_orchestrate` for outbound calls. Inbound discovery uses
`GET /.well-known/agent-card.json`; JSON-RPC tasks use `POST /` (v1.0
`SendMessage`, `SendStreamingMessage`, `GetTask`, `CancelTask`, etc.). Default
port is 9900. No-token deployment is loopback-only; remote exposure requires
explicit bind/auth, peer allowlisting and secure transport. Per-peer tokens,
audit logging and turn caps matter; never create an unlimited agent ping-pong.

A2A context is its own conversation, not the user's Discord thread. Do not assume
API-specific `model_options` fields are accepted in A2A messages. For exact per-
conversation model/effort selection use the tested CLI or HTTP controls, or a
separately selected Hermes profile with a verified policy. Probe interoperability
with the actual caller; an MCP-capable CLI is not automatically an A2A client.

## Other integration surfaces

- `hermes acp`: Agent Client Protocol over stdio, intended for compatible IDEs.
  Supports session/prompt/tool events and permission flow. CLI help was checked;
  no ACP client session was exercised in this pass.
- TUI gateway JSON-RPC over stdio/WebSocket: session creation, prompt submission,
  steer/interrupt, events, commands and interactive requests. A custom client
  must advertise and implement approval/clarify/vault request handling. Protocol
  is not MCP. Do not attach to someone's active session without scope.
- Python `run_agent.AIAgent`: in-process embedding for a purpose-built trusted
  application; integration must own lifecycle, auth and permissions.
- Webhook routes: event-triggered runs when configured and authenticated.
- `hermes peer`: peer gateway messaging; do not equate it with a verified generic
  task API. Bot mode and kanban can coordinate Hermes-owned jobs with explicit
  roles/limits, but are not installed cross-harness task adapters by this doc.

[Official programmatic integration](https://hermes-agent.nousresearch.com/docs/developer-guide/programmatic-integration)
explains the richer surfaces. Prefer CLI/API for ordinary other-agent callers;
do not build a new wrapper or expose a listener merely because it is possible.
