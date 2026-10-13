---
name: browser-use
description: Use for public, signed-in, hosted, or desktop browser tasks.
created_at: 2026-09-29
updated_at: 2026-09-29
model: openai-codex/gpt-6-sol
doc_type: skill
purpose: Provide a portable browser route selector with on-demand operating references.
related:
  - path: ../../capabilities/connectors.md
    why: Browser bridge inventory and onboarding guides.
---
# Browser Use

## When to Use

Load when a task requires browser route selection, account access, concurrent
browsers, desktop fallback, or onboarding a browser bridge. For a site-specific
task, also load that site's skill.

Start here for a browser task. This skill describes **what to do and how to prove it**, not any harness's tool syntax or live configuration. Read the browser-use spec for authorization, identity, privacy, tab ownership, concurrency, and verification. Check its state file (also private) before treating a dated test as current. Use the active harness's own adapter for native calls. A shared guide does not grant a login or turn on a connector.

## Pick a route

1. **Public page, no account needed:** Read `~/agents/skills/browser-use/references/public.md`. Prefer a clean isolated browser or supported API. Do not spend a signed-in profile on an anonymous read.
2. **Account or an existing session needed:** Read `~/agents/skills/browser-use/references/signed-in.md`. Name the *browser identity* that owns the login, the process location, and the controller separately. Stop for human login, MFA, CAPTCHA, or a new permission boundary. Do not assume an isolated browser inherits Chrome sessions.
3. **Mac unavailable or multiple remote browsers needed:** Read `~/agents/skills/browser-use/references/hosted.md`. Hosting moves account state and may incur costs; a named session is not a saved login.
4. **Two or more agents:** Also read `~/agents/skills/browser-use/references/parallel.md`. Separate job, controller session, tab, and profile ownership; serialize same-account changes and global clipboard/download/dialog use.
5. **Native picker, desktop app, or browser chrome:** Read `~/agents/skills/browser-use/references/desktop.md`. Browser DOM access is not desktop control.
6. **Export, upload, or a state-changing action:** Also read `~/agents/skills/browser-use/references/verification.md` for result and cleanup checks. Load the site's own shared skill if one exists, such as `~/agents/skills/chatgpt-browser/SKILL.md` or `~/agents/skills/claude-browser/SKILL.md`.

## Find and onboard a controller

`~/agents/capabilities/connectors.md` lists MCP, native, CLI, API, extension, and desktop routes. Its linked guides explain connection modes, prerequisites, authorization, known failures, and a real smoke test. The browser identity is not the controller: several controllers may attach to the *same* Chrome profile and share its account state. Pick the least privileged route with the required capabilities, then use the active harness's own `/sync-tool-adapter` session to audit and configure **that harness only**. See `~/agents/skills/browser-use/references/onboarding.md`.

Never equate documented, configured, connected, public-page verified, signed-in verified, and unattended-ready. Report the highest tier actually proven, plus any unresolved login, restart, or cleanup check. Browser use is still bounded by the user's request and the target site's rules; a tool connection is not authorization for a job.
