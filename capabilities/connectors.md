---
created_at: 2026-07-07
updated_at: 2026-09-29
model: gpt-5.6-sol
doc_type: capability
purpose: Portable inventory of the external connectors retained in the Agents workspace.
related:
  - path: ~/agents/capabilities/AGENTS.md
    why: Capability-folder ownership and portable-layer rules.
  - path: ~/agents/adapters/adapter-contract.md
    why: Tool adapter reconciliation and connector decision rules.
---

# Connectors Registry

This is an awareness inventory, not an enablement manifest. Host configuration,
credentials, permissions, and exact launch mechanics stay in the host's native
configuration or the connector runbook.

## Default Rules

- Keep connector descriptions portable and vendor-neutral where possible.
- Never store credentials, tokens, cookies, or private headers here.
- Treat browser-driving and repository writes as explicit actions. A bridge can
  be documented without granting account access or enabling it in a harness.
- Verify the connector in the host before relying on it.
- Keep application-specific setup in the owning project.

## Retained MCP Connectors

| Connector | Purpose | Posture | Runbook |
|---|---|---|---|
| `playwright` | Managed browser, CDP attachment, or profile-specific Chrome extension | Local; configured default-off unless a dated harness decision enables it; signed-in attachment needs explicit profile selection and private token for extension | [`mcp/playwright.md`](mcp/playwright.md) |
| `chrome-devtools` | Managed Chrome inspection or explicit CDP attachment | Local; configured default-off; page routing recommended for concurrency; check telemetry before private use | [`mcp/chrome-devtools.md`](mcp/chrome-devtools.md) |
| `jev-browser` | Model-driven navigation in isolated Chromium; separately adaptable library page injection | Local MCP; configured default-off unless a dated harness decision enables it; nested model sees page state | [`mcp/jev-browser.md`](mcp/jev-browser.md) |
| `figma` | Design file, component, and token inspection | Remote or local; account permissions apply | [`mcp/figma.md`](mcp/figma.md) |
| `git` | Local repository status, history, diffs, and branches | Local; no connector auth | [`mcp/git.md`](mcp/git.md) |
| `github` | Hosted repository, pull request, issue, and CI context | Host-managed auth and permissions | [`mcp/github.md`](mcp/github.md) |

## Web Search And Fetch MCP Connectors

Added 2026-09-29 at the user's request. **Installed in Claude Code,
OpenCode, and Codex (2026-09-29, keyed, smoke-tested in fresh CLI sessions).**

**Default-on wiring (user decision, 2026-09-29).** These three servers are expected configured and allowed without harness prompts. That does not authorize automatic paid use. Native search and fetch remain the ordinary default. Tool choice, prices and permitted escalation live in [capabilities/web](web/README.md). Both web-search skills are request-only.

A sync-tool-adapter run follows the current harness's connection guide under ~/agents/capabilities/mcp/ and verifies real calls. Keep Firecrawl's costly tools hidden or denied as documented. Keys come from environment variables loaded by [the key setup script](mcp/search-keys-setup.sh). Firecrawl's tested anonymous route lists tools but refuses calls; use a free account key. Each harness configures and verifies its own native state.

| Connector | Purpose | Posture | Runbook |
|---|---|---|---|
| `parallel` | Cheap authorized web search and page reading | Hosted; keyless free tier; key in bearer header; no approval needed; no hard spend cap once keyed | [`mcp/parallel.md`](mcp/parallel.md) |
| `exa` | Meaning-based search and cheap page reads | Hosted; keyless free tier; no approval prompt; used only when the user asks for Exa; `agent_run` excluded | [`mcp/exa.md`](mcp/exa.md) |
| `firecrawl` | Hard pages, PDFs, site maps | Hosted; **needs a key to make calls** (keyless lists tools but refuses calls, tested 2026-09-29); no approval prompt; used when the default readers fail; crawl, agent, interact, and monitor tools hidden where the harness can | [`mcp/firecrawl.md`](mcp/firecrawl.md) |

## Browser and Desktop Bridges (not all MCP)

These are **awareness entries**, not blanket installation or enablement
instructions. `/sync-tool-adapter` inventories them and maps what the active
harness can actually use; optional CLI/API/desktop software is not installed
merely because it appears here. The user selects a signed-in identity and any
new secret handoff or broader permission before enablement. The shared route
selector is [`../skills/browser-use/SKILL.md`](../skills/browser-use/SKILL.md),
and its [`references/onboarding.md`](../skills/browser-use/references/onboarding.md)
defines the per-harness proof tiers.

| Bridge | Connection standard and login boundary | Guide |
|---|---|---|
| Harness-native browser | Built-in browser tool; backend may be isolated, CDP-attached, real-profile snapshot, or hosted; no automatic login inheritance | [`browser-native.md`](browser-native.md) |
| Standalone browser CLI / Playwright script | CLI/library; own session and profile, or explicit CDP attachment to an existing identity | [`browser-cli.md`](browser-cli.md) |
| Browser Use Cloud / hosted contexts / Camofox | Provider API, SDK, CDP, MCP or keyed local service; separate profile and billing/persistence semantics | [`browser-hosted.md`](browser-hosted.md) |
| Desktop/accessibility control | OS GUI driver for browser chrome and native dialogs; separate OS permissions | [`browser-desktop.md`](browser-desktop.md) |

Playwright MCP has **three distinct browser connection modes** (managed,
CDP, extension) under one connector guide; Chrome DevTools MCP can manage Chrome
or attach through CDP; Jev stock MCP does **not** inherit an injected signed-in
page. An MCP endpoint, session label, or registered tool is not an authenticated
browser. See each runbook for setup, known failures, and the live test required.

## Scope

The six MCP connectors under Retained MCP Connectors, plus the three web search
and fetch connectors above, are the maintained general-purpose MCP registry.
The optional Hermes messaging MCP is documented under agent bridges below,
not added to the default-on search set or the retained-install requirements.
The browser and desktop awareness entries also belong to the connector inventory
but are **not**
automatically installed or enabled by adapter sync. Retired or
unmaintained connectors should not be restored here without a new, explicit
decision and a current owner.

## Non-MCP CLI bridges

| Bridge | Purpose | Posture | Guide |
|---|---|---|---|
| `opencode-cli` | Let other AI harnesses run bounded tasks with OpenCode models and skills | Local CLI; write-capable; no cross-harness permission inheritance; maintained reference under `opencode/` | [OpenCode capability](opencode/STATE.md) |
| `claude-cli` | Let other AI harnesses run bounded tasks with Claude Code models, skills, subagents, web search (Parallel and Firecrawl with no flag), and the user's Gmail, Drive, and Calendar connectors | Local CLI; write-capable; about $0.12+ per run; no cross-harness permission inheritance; full reference in the guide | [`claude-cli.md`](claude-cli.md) |
| `codex-cli` | Let other AI harnesses run bounded Codex tasks with live web search and session-dependent Google account tools | Local CLI; write-capable; no cross-harness permission or connector inheritance | [`codex-cli.md`](codex-cli.md) |
| `gemini-cli` | Let other AI harnesses run bounded tasks with Gemini / Antigravity models and skills | Local CLI; write-capable; no cross-harness permission inheritance | [`gemini-cli.md`](gemini-cli.md) |

These are awareness entries, not automatic enablement in Claude Code, Codex or
any other host. Each host owns its own adapter mapping and approval decision.

## Data API Bridges (not MCP)

| Bridge | Purpose | Posture | Guide |
|---|---|---|---|
| Artificial Analysis | Cached model indices, pricing, cost per task and median performance | Read-only HTTPS; key from environment; bounded page requests; Free data is not full website coverage. No automatic MCP or cross-harness setup. | [Artificial Analysis capability](artificial-analysis.md) |

## Agent Service Bridges (CLI, API, MCP or A2A)

- **Hermes Agent:** optional task delegation via local CLI or authenticated HTTP
  API; native `hermes mcp serve` for conversation history, messaging and approvals;
  optional A2A for structured agent tasks. These surfaces are not equivalent.
  Awareness-only, opt-in, host-write-capable, with no inherited caller sandbox,
  conversation or account permissions. Do not enable broad transcript/send or
  approval access merely to run a task. Model and effort preferences are owned by
  the capability guide, not caller defaults. Read
  [the capability](hermes.md),
  [live proof and gaps](hermes/STATE.md), and
  [task-hermes](../skills/task-hermes/SKILL.md).

`/sync-tool-adapter` inventories only the active caller's selected route and
verification tier; it does not automatically add a server, start A2A, distribute
credentials, or grant permissions. Model policy and route facts are owned by the
capability; caller-native wiring stays in that caller's adapter.
