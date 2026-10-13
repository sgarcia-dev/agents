---
created_at: 2026-09-29
updated_at: 2026-09-29
model: openai-codex/gpt-6.1-sol
doc_type: capability
purpose: Describe Hermes Agent as an optional cross-harness task and conversation bridge.
related:
  - path: ~/agents/skills/task-hermes/SKILL.md
    why: Bounded delegation procedure.
  - path: ~/agents/capabilities/hermes/STATE.md
    why: Current verified routes, failures and limits.
  - path: ~/agents/capabilities/connectors.md
    why: Cross-harness bridge awareness registry.
---

# Hermes Agent capability

Hermes is a callable agent with tools, skills and persistent context. Another
harness can hand it a task without adopting Hermes as its own model provider.
Its shell, browsers and integrations execute on the Hermes host, not the caller's
sandbox. Permission to call it is not permission to use every account or tool.

## Start Here

- [Task procedure](../skills/task-hermes/SKILL.md).
- [Status and verified limits](hermes/STATE.md).
- [Delegation menu](hermes/delegation-menu.md):
  all task families, prerequisites, and when not to delegate.
- [CLI](hermes/cli.md): simplest local task route.
- [HTTP API](hermes/api.md): running service,
  model overrides, continuation, progress and cancellation.
- [MCP, A2A and other protocols](hermes/mcp-a2a.md):
  different surfaces, not interchangeable task runners.

## Choose Whether to Use It

Use Hermes when it contributes a verified capability the caller lacks: the
selected Mac browser identity or desktop controller, an installed workflow,
ongoing Hermes context, account integration, messaging delivery, or durable
scheduled execution. It can also perform research, coding, review, data processing
and document creation. It is not inherently better at those tasks than the same
model in the caller. Another agent loop adds cost, latency and a review burden.

Prefer native caller tools for small local tasks, work already scoped to its
sandbox, or jobs requiring a connector only that caller has. Use shared browser
and web-search procedures directly when no Hermes-specific access is needed.
Do not use Hermes to bypass the caller's permissions, gain unapproved account
access, or hide tool failures. Keep private content out of this public
repository and out of public channels.

## Models and Reasoning

**Which model to use:** the Hermes rows in
`~/agents/ai-models/delegation-briefing.md` (main model, step up,
`delegate_task` subagents, search). This file only covers how to pin it.

CLI pins `--model`, `--provider`, `--reasoning`. HTTP pins `model`, `provider`,
`model_options.reasoning_effort`. Send all three, including on follow-ups. Use
`openai-codex` for OpenAI ChatGPT/Codex subscription auth here; `openai` means
the separate OpenAI API provider and needs its own credentials/billing. Do not
silently substitute one for the other. Use default service tier unless selected
otherwise. A model alias from `/v1/models` is not the underlying model catalog.

Other configured Hermes providers/models may be chosen for an explicit task.
Check availability in Hermes, not the caller's catalog. Request low-cost effort
first, do not assume the same reasoning levels exist on every model, and record
fallbacks. Nothing in this guide changes provider login or global defaults.

## Route and Identity Boundaries

- **CLI:** fresh Hermes process/session by default. Runs without the messaging
  gateway. Can resume an exact authorized session. Uses the selected profile,
  host config, CWD rules and toolsets, not the parent's conversation or sandbox.
- **HTTP API:** gateway-backed independent conversation by default. Local base
  URL currently `http://127.0.0.1:8642/v1`; bearer auth required. On a different
  machine, localhost means that different machine. Remote reachability requires
  a separately authorized secure tunnel/service, not an exposed port.
- **Native MCP:** stdio `hermes mcp serve`; conversation history, event polling,
  message delivery and approval tools. No general `ask_hermes` tool or per-call
  model/provider/effort fields in the tested schemas. Message send is not proof
  of an agent reply or an agent-task handoff.
- **A2A:** purpose-built inbound/outbound agent tasks, context IDs, discovery,
  streaming and cancellation. Optional, not verified as enabled here.
- **ACP / TUI gateway / Python library:** richer integration surfaces for IDEs,
  custom hosts or embedded applications; not automatically consumed by other
  coding CLIs.

The raw subscription `hermes proxy` is **not** Hermes delegation: it forwards
model inference, without Hermes's tool loop, skills and memory.

## Onboarding Through `/sync-tool-adapter`

This is an **awareness-only, opt-in** capability. Sync inventories the caller's
selected CLI/API/MCP/A2A route, profile, model policy, secret source and proof
status. Documentation does not install a connector, distribute the API key,
start an A2A server or authorize broad MCP transcript access. Run sync in exactly
one caller harness per run, with its native configuration owned there.

For CLI, prove command execution and a harmless task tool. For API, authenticate,
check capabilities and prove a bounded task. For MCP, enumerate tool schemas
before requesting owner-approved content; disable sending and approval tools in
the caller unless needed. For signed-in work separately verify the selected
account through the actual route. Configured, discovered, task-verified and
signed-in verified are separate claims.

## Sources

- [Official programmatic integration](https://hermes-agent.nousresearch.com/docs/developer-guide/programmatic-integration).
- [API server](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server).
- [A2A](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a).
- [Tools](https://hermes-agent.nousresearch.com/docs/reference/tools-reference)
  and [documentation index](https://hermes-agent.nousresearch.com/docs/llms.txt).
- Installed `hermes --help`, `hermes chat --help`, `hermes mcp serve --help`,
  live API capability/toolset responses and MCP discovery. Exact dated evidence
  and gaps live in the status file; documentation may outpace the running gateway.
