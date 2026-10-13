---
created_at: 2026-09-29
updated_at: 2026-09-29
model: openai-codex/gpt-6-sol
doc_type: capability
purpose: Distinguish Jev's public MCP from its injected-page library route.
related:
  - path: ../connectors.md
    why: Bridge registry and posture.
  - path: ../../skills/browser-use/references/signed-in.md
    why: Authentication boundary and supervision.
---
# Jev Browser MCP and library

The tested community `@jkudish/jev-browser` package exposes a `jev_navigate` MCP action and a CLI. Its stock server starts a separate, usually headless Playwright Chromium context, **signed out** of local Chrome accounts. It calls an additional model for decisions; page content goes to that provider, and host plus nested usage/cost must both be counted. Pin a vetted version; the historical 0.5.0 install had seven transitive runtime advisories, including one high.

**Stock MCP onboarding:** In the active harness, choose a private provider credential/launcher, pin and inspect the package and its actual tool schema, set a short step/time budget, and restrict first use to a public read. Discover `jev_navigate`, then invoke it through the actual harness on a harmless page. Independently check final URL/content and its trace; `done` alone is not proof. The Hermes/OpenCode pilots proved bounded public navigation, not authentication or general reliability. A connector's trust setting and the browser job's authorization are separate.

**Signed-in library route:** `navigate({page})` can receive a caller-owned Playwright page attached to an owner-signed-in browser. That is a custom wrapper, **not** a feature of the stock MCP; it shares the injected page's login and tab. A supervised ChatGPT project navigation passed on the dedicated CDP identity, but autonomous nested scrolling failed an independent pane-offset check. Build and verify a separate adapter in a single harness before claiming private access, bound all actions, and independently measure progress. Do not export cookies to make the stock MCP appear signed in. Private page exposure to the nested model needs its own owner decision. Close the exact injected page and disconnect without killing shared Chrome.
