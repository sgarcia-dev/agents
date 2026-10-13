---
created_at: 2026-07-09
updated_at: 2026-09-29
model: gpt-5.6-sol
doc_type: capability
purpose: Portable runbook for browser inspection through the Chrome DevTools MCP connector.
related:
  - path: ../connectors.md
    why: Connector inventory and default posture.
  - path: ../AGENTS.md
    why: Capability-folder rules and portable-layer boundaries.
---

# Chrome DevTools MCP

## Overview

Chrome DevTools MCP provides Chrome DevTools Protocol inspection for a managed
browser session. Use it for console logs, network requests, response bodies,
headers, DOM state, and browser interaction that needs live inspection.

Prefer Playwright for repeatable scripted automation across clean contexts.

## Install / Configure

Launch the connector with:

```text
chrome-devtools-mcp --experimentalPageIdRouting
```

Install and pin a version verified by the active harness; this is an argument
shape for an installed binary, not a universal install command. The routing
flag is recommended when multiple agents share one server. It makes page-scoped
calls target an explicit `pageId`. Do not pass `--slim`, because it
disables page routing. Add `--isolated` only when running separate server
instances.

For a separately running, explicitly selected signed-in Chrome, inspect the
installed server's `--browser-url` attachment option and connect only to a
loopback-only CDP endpoint. This attaches to that Chrome's profile; it does not
create or inherit a login by installing the MCP. Keep raw CDP off the network.
The managed browser is headed by default. Chrome or Chromium must be installed
and launchable on the host.

## Authentication And Safety

- The connector itself requires no authentication.
- Use the managed browser profile by default.
- Do not attach to a user's real browser profile unless the user explicitly asks
  for that exact inspection in the current conversation.
- Do not store tokens, cookies, private headers, or credentials in this guide.

## Concurrency And Cleanup

Warm the browser with one completed call before starting concurrent work. When
the routing flag is active, every page-scoped call must include its `pageId`.

Each agent closes pages it created and reports what remains. Never kill the
browser or shared MCP server to clean up.

## Verification

1. Open a stable local or public page.
2. Capture its `pageId`.
3. Evaluate a harmless page-context expression.
4. Confirm the title, URL, and ready state are returned.
5. If needed, verify one console entry or network response.

Example probe:

```js
() => ({
  title: document.title,
  url: location.href,
  readyState: document.readyState,
})
```

## Troubleshooting

- Browser lock during fan-out: warm the server first, then retry with bounded
  concurrency.
- Calls read the wrong page: verify `--experimentalPageIdRouting` and `pageId`.
- Connector missing: restart the host and check the resolved MCP configuration.
- No console or network detail: confirm the request uses Chrome DevTools rather
  than a browser-only connector.
- Authentication errors: the connector has no connector-level auth; inspect the
  target application's session and the active browser profile. A healthy CDP
  handshake is not an account-only page check.

## Known Limitations

- Chrome and Chromium only.
- Browser-driving actions can mutate application state.
- Page routing prevents page-selection collisions but not backend data races.
- Headless mode may behave differently on sites with bot detection.

## Evidence Sources

- https://github.com/ChromeDevTools/chrome-devtools-mcp
- https://developer.chrome.com/docs/devtools/remote-debugging

## Maintenance Notes

- Keep the launcher and routing posture aligned with the connector registry.
- Recheck command-line flags and telemetry settings when upgrading the MCP
  package. Chrome DevTools MCP documents usage statistics and optional Chrome UX
  Report lookups; decide and verify those settings before private-page work.
- Keep application-specific verification steps outside this portable guide.
