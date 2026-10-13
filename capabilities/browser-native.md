---
created_at: 2026-09-29
updated_at: 2026-09-29
model: openai-codex/gpt-6-sol
doc_type: capability
purpose: Inventory harness-native browser controllers and their onboarding checks.
related:
  - path: ./connectors.md
    why: Bridge registry and posture.
  - path: ../skills/browser-use/SKILL.md
    why: Portable route-selection procedure.
---
# Harness-native browser tools

A built-in browser tool is a **controller**, not a browser identity or an interchangeable cross-harness API. Its backend may start an isolated browser, attach to CDP, use a real-profile copy, or create a cloud browser. Resolve the *effective* backend, profile, process and permissions from the active harness at run time. A native tool may not need an MCP installation at all.

**Hermes example (tool-specific detail, not a portable command):** `browser_exec` can navigate/inspect pages with browser helpers and, in the locally configured CDP route, attach to a dedicated visible Chrome. Hermes's MCP `browser_*` actions are a different controller and may reach another profile. Neither `local=True`, a named session, nor a successful tool call alone proves the user's login. Other harnesses must map their own browser tool names and backend precedence in their adapters; do not copy Hermes configuration into them.

**Onboard in the active harness:** Inventory the browser tool and its available backends without editing another harness. Pick public isolated mode by default. For an explicitly approved signed-in mode, establish a separately owned profile, confirm loopback-only CDP or the documented profile attachment, and check account-only state through the actual tool. Confirm tab ownership and exact-target close; repeat after browser restart if persistence matters. A listener/health response, model `done`, or package version does not prove page control. Stop if the profile is locked, the browser is offline, or the tool selects the wrong identity; do not copy the ordinary Chrome profile.

**Known hazards:** Backend precedence may shadow cloud selection; real-profile snapshots can stall on Chrome's locked databases; a shared current-tab pointer can cause concurrent workers to navigate each other's pages; a named session need not bind a saved cloud profile. Recheck those behaviors in the active version and require explicit page/session IDs for concurrency. Keep raw CDP on loopback and out of shared traces. The harness's adapter owns tool calls, vault-mediated login mechanics, effective settings and current health.
