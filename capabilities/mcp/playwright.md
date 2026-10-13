---
created_at: 2026-07-09
updated_at: 2026-09-29
model: openai-codex/gpt-6-sol
doc_type: capability
purpose: Explain Playwright MCP's isolated, CDP, and Chrome-extension connection modes.
related:
  - path: ../connectors.md
    why: Registry and default-off posture.
  - path: ../../skills/browser-use/SKILL.md
    why: Portable browser route selection.
---
# Playwright MCP

Playwright MCP exposes browser navigation, snapshots, clicks, typing and other actions to an MCP client. **It does not identify a login store on its own.** Three modes matter:

- **Managed/isolated context:** Start a browser under the server. Normally signed out; use for public tasks or a separately approved persistent profile. One server's implicit active page is not safe for arbitrary concurrent workers.
- **Attach to existing Chrome through CDP:** Launch a separately owned Chrome with a non-default persistent user-data directory and loopback-only CDP listener; start the server with `--cdp-endpoint http://127.0.0.1:<port>`. It reaches that browser's existing site sessions while the process runs. No Playwright extension or extension token is involved. Raw CDP is broad, unauthenticated locally and must not be exposed remotely. The pinned `@playwright/mcp@0.0.82` direct-client pilot passed a signed-in project snapshot on the local dedicated Chrome; that does **not** establish every harness's gateway integration.
- **Attach through Microsoft's Chrome extension:** Install the extension inside the *exact* UI-created Chrome profile; use `--extension --profile-dir-name '<internal profile directory>'`. The profile display name is not necessarily that internal directory. The extension may show a browser-local Allow screen; a profile-specific `PLAYWRIGHT_MCP_EXTENSION_TOKEN` can be passed privately to the server to avoid repeated connection prompts. That token grants broad profile access and must not appear in Git, chat, a raw connection URL in logs, or shared MCP config. The harness's own MCP approval/trust is a **different** gate. Extension-connected clients can have separate tab groups, so an existing tab is not automatically in another client's group. The local `sergei-automation` (`Profile 1`) pilot passed post-restart signed-in navigation with a private token; it is not the owner's everyday/default Chrome.

## Onboard one harness

1. Audit its effective MCP schema, permission controls, exposed tool list, and installed server version. Pin a version tested by that harness rather than copying `@latest` blindly. The registry's default-off posture means configured-off when supported, not automatic signed-in access. Do not edit another harness's config.
2. Select **one mode and one exact browser identity**. Use a managed context for the first public smoke. For CDP, verify the Chrome process/profile and loopback listener first; do not start another process on that directory. For extension, let the owner install/approve in the intended profile and store the token through that harness's private credential mechanism. Do not assume it inherits Hermes's environment or token.
3. Expose only needed actions. Reload the MCP child after changing its environment. Run a fresh `browser_navigate` and `browser_snapshot` through the **active harness**, first on a harmless public page. For signed-in use, verify an account-only control after hydration, not merely a URL or absence of a login prompt. Keep a failed extension approval probe short and inspect the owner-visible screen rather than waiting for a long timeout.
4. Record exact task-owned tab/page ID, close it on all exits and verify disappearance. Disconnect clients; never call `browser.close()` on shared CDP Chrome. For multiple agents, use separate servers/profiles or proved explicit page ownership; tab groups, named sessions and shared cookies solve different problems.

**Known limits:** CDP does not start a down Chrome; extension token rotation needs a new MCP subprocess; a shared server may keep hidden active-page state; browser-native file upload or download controls may not be exposed by the harness's tool allowlist. A tool-discovery success or a saved MCP entry is not a completed browser task. Inspect the active tool list before promising a method.

Upstream: https://github.com/microsoft/playwright-mcp
