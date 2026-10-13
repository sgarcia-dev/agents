---
created_at: 2026-09-29
updated_at: 2026-09-29
model: openai-codex/gpt-6-sol
doc_type: capability
purpose: Describe desktop-control fallback for browser-adjacent native UI.
related:
  - path: ./connectors.md
    why: Bridge registry and posture.
  - path: ../skills/browser-use/references/desktop.md
    why: Selection and verification procedure.
---
# Desktop control for browser-adjacent UI

A desktop/accessibility controller operates windows, browser chrome, file pickers, app dialogs and other native controls. It is not a DOM browser connector and does not inherit a browser tool's page targeting, login store or safety gates. Hermes `computer_use` is one implementation; another harness may have different OS permissions or none. A screenshot of an account page does not prove that a CDP/MCP controller can attach to its browser identity.

**Onboard one harness:** Audit its effective desktop tool, OS grants, target-window scoping, screenshot/accessibility output and approval policy. Do not grant permissions silently or translate a browser MCP's broad trust into desktop approval. Verify the selected window/profile with a harmless read and one low-stakes control. For native file selection, verify the exact file reached the site after reload rather than stopping when a picker opens. Stop for owner-only OS permission, password, MFA, CAPTCHA, or payment gates. Use a fresh observation for each coordinate; prefer accessibility labels.

**Fallback boundary:** Change approach after a bounded headless/login or connector failure instead of repeatedly retrying a disconnected browser. Desktop clicks can mutate account state; scope them to the user's task and read back the exact server-side result. Restore clipboard or global settings and close only task-owned tabs, never an owner window by guesswork. A desktop route is awareness-only until the active harness verifies its own integration.
