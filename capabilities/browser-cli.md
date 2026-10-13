---
created_at: 2026-09-29
updated_at: 2026-09-29
model: openai-codex/gpt-6-sol
doc_type: capability
purpose: Describe standalone browser CLIs and deterministic scripts as portable bridge candidates.
related:
  - path: ./connectors.md
    why: Bridge registry and posture.
  - path: ../skills/browser-use/references/parallel.md
    why: Session, profile, and cleanup contract.
---
# Browser CLI and script bridges

A standalone browser CLI (such as `agent-browser`) can start isolated sessions without an MCP server. A small Playwright script can instead attach over CDP to an existing signed-in Chrome or launch a separate persistent profile. Those are different identities even if both are driven from a shell. CLI/scripting access is a tool permission decision, not a fallback that bypasses the browser job's scope.

**Onboard one harness:** Discover the installed executable/version and documented flags in that harness; do not assume a Hermes-bundled binary matches a separately installed one. For parallel `agent-browser`, assign one stable, unique `--session` on **every** call, never attach all workers to a shared CDP port, and verify each session's own URL plus cookie separation. A persistent `--profile` directory must have exactly one running owner and human login; a saved `--state` is credential-bearing cookies/local storage, not equivalent to a complete login profile. Keep profile and state files outside Git with private permissions. Close every owned session and confirm none remain.

For deterministic Playwright/CDP recovery, use the library's documented `connectOverCDP` on a loopback endpoint, open a new task page, check an account-only element if needed, close that page in `finally`, and disconnect without calling `browser.close()` on the shared Chrome. A bounded script can solve a specific upload, frame, or download problem, but it is not automatically the agent's standard connector. Read `~/agents/capabilities/mcp/playwright.md` for the reusable MCP alternative.

**Evidence:** Five standalone named sessions passed a public-page isolation and zero-remainder pilot; authenticated per-agent reuse and site-side same-account concurrency were not proved. Inspect current versions and run the active harness's own harmless smoke before adoption.
