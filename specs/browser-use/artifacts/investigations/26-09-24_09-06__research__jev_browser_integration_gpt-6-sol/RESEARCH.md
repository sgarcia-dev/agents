---
created_at: 2026-09-24
model: openai-codex/gpt-6-sol
artifact_category: investigations
doc_type: research
purpose: Preserve the Jev browser integration decision, source reports, exact local setup, test evidence, limits, and a separate proposal for desktop computer use.
bundle_type: research
research_depth: standard
progress_mode: transient
related:
  - path: ./sources/jevreport1.md  # private, not published
    why: First user-supplied research report, preserved byte for byte as received.
  - path: ./sources/jevreport2.md  # private, not published
    why: Second user-supplied research report, preserved byte for byte as received.
---

# Jev browser integration: investigation and operating record

**Status: Completed for the investigation and initial browser setup. Native desktop computer use is not implemented.**

**Checked:** September 24, 2026. **Scope:** Hermes Agent and OpenCode on this Mac. Codex and Claude were not changed.

## Start here

- **Question:** Does this do computer use? **It drives web pages in a separate headless Chromium browser. It does not control macOS windows, menus, Finder, the user's current Chrome tabs, or Hermes's `computer_use` tool.**
- **What works:** A pinned Jev Browser package, a shared credential-safe launcher, a Hermes MCP connection, and an OpenCode MCP connection. OpenCode made an end-to-end agent-to-tool call. A direct CLI run clicked a real Wikipedia link. The current Hermes session lists the tool schema, but a live Hermes call has not been made because the server is marked untrusted and calls may require user approval.
- **What is pending:** A user-approved, public-page Hermes tool call, followed by independent inspection of its result. No macOS Settings grant was needed for the headless browser tests. Native desktop control would be a separate project.
- **Raw inputs:** First user report (private, not published) and second user report (private, not published). They are background research, not proof that every cited claim remains current. Their `turn...` citation markers came from another research session and do not resolve inside this bundle.

## The two reports and the decision

The reports agree on the key distinction: TypeSafe's Jev returns bounded decisions, not prose, code, or a complete browser agent. TypeSafe documents Choice, Score, and Noul answers over text or structured textual state; it does not take screenshots or operate the computer by itself.[3]

They differ in what to install first. The first report favors `@jkudish/jev-browser` as a ready-made browser MCP server, plus a separate generic Jev judgment MCP. The second favors `itsmostafa/typesafe-mcp` for generic judgments and treats Browser Use's Jev Ultrafast as a separate experimental browser runner. Those are not interchangeable: a generic `evaluate` tool judges a supplied state, while a browser runner owns page observation and execution. The user asked first for browser automation, so only the browser component was installed. No general-purpose Jev judgment MCP was added.

The chosen package, `@jkudish/jev-browser` version **0.5.0**, exposes a single MCP tool named `jev_navigate`, plus a CLI and JavaScript library. It owns a Playwright browser, presents observed page controls as bounded choices to Jev, and returns a trace, final page, usage estimate, and optional screenshot. Its own README calls it early software. The upstream Browser Use `jev-ultrafast` project uses Browser Harness to connect to Chrome and documents a Python library/CLI and local inspector, but not the generic browser MCP interface needed for this initial Hermes/OpenCode deployment.[1][2]

**Why not Ultrafast now:** It requires a separate Browser Harness/Chrome connection and a TypeSafe key plus a text-model key for its documented setup. On this Mac its offline tests passed, but `browser-harness --doctor` reported the daemon and active browser connections absent. No live Ultrafast navigation was performed. Its published September 20, 2026 Google Flights example is already dated before this investigation, so it is not a valid current smoke task. An upstream issue independently calls out that expired demo date.[2][6]

## Architecture and current local implementation

```text
Hermes (MCP) ──────┐
                   ├── ~/.local/bin/jev-browser-launch
OpenCode (MCP) ────┘        │
                            ├── pinned @jkudish/jev-browser 0.5.0
                            ├── Playwright's separate headless Chromium
                            ├── Jev judgments through OpenRouter
                            └── optional typing via Gemini 2.5 Flash Lite through OpenRouter
```

- **Package:** `~/.local/share/jev-browser/node_modules/@jkudish/jev-browser/`. Installed at exact package version 0.5.0. The browser binary is in Playwright's cache under the user's Library, not in this workspace.
- **Launcher:** `~/.local/bin/jev-browser-launch`, executable only by the user. It reads `OPENROUTER_API_KEY` from the default Hermes `.env` at runtime. It does not print or copy the key into either MCP config. It removes inherited TypeSafe and OpenAI keys, forces `JEV_PROVIDER=openrouter`, forces `JEV_BROWSER_TYPE_PROVIDER=openrouter`, and selects `google/gemini-2.5-flash-lite` for generated field text. This also avoids the package's OpenAI auto-detection default, which names a deprecated GPT-5.6 model. The launcher uses the configured Hermes Python environment for `python-dotenv` and the pinned local Node runtime.
- **Hermes:** `mcp_servers.jev_browser` points at the launcher, selects only `jev_navigate`, disables MCP resources/prompts and server-initiated sampling, and sets `trust: untrusted`. `hermes mcp test jev_browser` connected and discovered one tool. The tool schema `mcp__jev_browser__jev_navigate` was visible in this Discord session when checked on September 24. A visible schema is not a successful browser call. Hermes's MCP documentation says `/reload-mcp` refreshes changed server config; there is no need to bypass approvals to test a call.[4]
- **OpenCode:** The global `~/.config/opencode/opencode.jsonc` has an enabled local MCP entry named `jev-browser` that launches the same wrapper, with a 180,000 ms connection timeout. OpenCode exposes `jev-browser_jev_navigate`. Its `mcp list` showed `connected`, and a Plan-agent run invoked the tool successfully. OpenCode documents this `mcp` configuration shape and its ability to disable a server without removing it.[5]
- **Credentials and cost:** No new TypeSafe key was obtained. The existing OpenRouter credential is used for Jev and, when text is needed, the configured typing model. This is paid usage under the existing OpenRouter account, not free inference. The package's `est_cost_usd` is an estimate from reported tokens, not a verified invoice.[1]

This setup intentionally does **not** share the user's logged-in Chrome profile. Password and cookie handoff features described by the package are not configured. Do not assume an authenticated browser session exists merely because Chrome is open elsewhere.[1]

## Verification record

These are actual observations from September 24, 2026, not intended future tests:

1. `uv sync --frozen`, `ruff check`, `pytest -q`, and `uv build` in a temporary clone of Browser Use Ultrafast: **31 tests passed**, lint passed, wheel and source archive built. Commit inspected: `1231850a0bf1a0c0341fe408ef1668dbbfdfac46`. `browser-harness --doctor` saw Chrome running but no harness daemon and zero active browser connections. This proves package health in a local test environment, not live Ultrafast browser operation.
2. `npm ci` and `npm run build` in a temporary Jev Browser clone succeeded. Commit inspected: `269cd1076faf370402a7db337531bee5b6c55978`. After installing Playwright Chromium and setting the task's scratch `TMPDIR`, **72 of 72 offline tests passed**. The initial test run had two failures because macOS's inherited temporary directory did not meet a test's strict 0700 handoff-directory check. A second run without any provider key had three failures in tests that start Chromium and resolve a transport even with a zero-second budget. Supplying a dummy key *for those offline tests only* made them pass; those tests performed no paid provider call. Neither initial failure should be recorded as a production navigation failure.
3. Direct CLI smoke: opened `https://example.com` in headless Chromium with typing and screenshots disabled. Returned `status=done`, title `Example Domain`, and provider `openrouter`. It made one Jev call, with an estimated cost of `$0.000027636`.
4. Direct CLI navigation: started at Wikipedia's Coffee article, asked Jev to click through to Espresso, and independently checked the resulting `final_url=https://en.wikipedia.org/wiki/Espresso`. Trace: `click_e28` on the Espresso link, then `done`. Two Jev calls, about 3.1 seconds, estimated `$0.001597176`, `degraded=false`. The observed final URL, rather than Jev's `done` label alone, supports the success claim.
5. OpenCode Plan-agent smoke: explicitly invoked `jev-browser_jev_navigate` on `https://example.com` with no typing or screenshot. It returned `done`, final URL `https://example.com/`, provider `openrouter`, and an ARIA level-one heading `Example Domain`. This is the end-to-end OpenCode integration check.
6. Hermes connection: `hermes mcp test jev_browser` connected and discovered `jev_navigate`; the running session's tool catalog now exposes the schema. **No Hermes agent-to-navigation execution has been claimed.** Its untrusted-server approval is left in place.

The cloned source trees used for tests live under `~/.hermes/cache/scratch/jev-eval-20260924/` and may be pruned. The installed package, launcher, this evidence record, and the original reports are the durable parts. To reproduce upstream tests later, reclone the exact commits above rather than relying on scratch.

## Browser versus computer use

| Requested action | This Jev installation | Correct route today |
|---|---|---|
| Click links and read text on a public website | Yes, in its own headless Chromium | Jev Browser MCP or its CLI |
| Fill an ordinary web field | Supported, with a separate text-generation call | Jev Browser after a scoped, low-risk task; inspect `degraded` and `warnings` |
| Use an existing logged-in Chrome tab or session | Not by default | A real-session browser or desktop route, with the user's consent and its own security controls |
| Click Finder, system dialogs, native apps, menus, or another desktop window | **No** | Hermes `computer_use` / cua-driver, subject to its own macOS permissions and approval boundaries |
| Understand a desktop screenshot directly | **No** | A vision-capable agent interprets the screenshot; Jev currently consumes text/structured text only[3] |

A possible future adapter, **not implemented**, would capture a desktop accessibility snapshot with Hermes `computer_use`, turn its currently actionable elements into a short Choice question for Jev, validate that the selected handle came from that exact snapshot, execute one approved `computer_use` action, recapture, and check the outcome independently. A text-generating model would still be needed for new strings; a vision model would still be needed for visual controls not represented in accessibility text. The deterministic executor, not Jev, would enforce app allowlists, action types, stale-handle checks, approval gates, and stop budgets. This would be a separate engineering project, not a flag on Jev Browser. No desktop permission should be requested until there is a concrete native-app task and an implementation to test.

## Security, reliability, and operating limits

- `npm audit --omit=dev` on the installed package reported **7 advisories: 2 low, 4 moderate, 1 high**. The high-severity item was in `undici`; `npm audit fix --dry-run` did not offer a complete remedy. The package remains experimental. Reassess before exposing it to sensitive sites, unattended high-impact automation, or a broadly trusted agent.
- The MCP tool can click web forms and may submit them. `trust: untrusted` on Hermes was intentional; do not replace it with blanket approval to save a prompt. OpenCode's successful Plan test was limited to an anonymous, read-only page. For payments, account changes, deletes, access-control changes, or credentials, require a fresh scoped decision and an execution gate outside Jev's judgment.
- Site text is untrusted. Neither Jev's confidence nor a successful `done` status is a security guarantee or a final-state proof. Inspect the trace and check the resulting page or application state independently.[1][3]
- Current upstream Jev Browser limits include very dense pages (240 extracted elements per step), shadow DOM, iframes, file inputs, hover-only menus, and arbitrary keyboard widgets. Its own README says bot protection may end a run as `blocked`. Use a different browser route when those are essential.[1]
- Each run can spend model calls. Set a small `max_steps` and `max_seconds` for a first test, and use `allow_typing=false` when no text is needed. No screenshot is required for plain text extraction.
- This separate Chromium did not require macOS Accessibility or Screen Recording grants in the live tests. Hermes native `computer_use` is a different driver with its own permissions, so success here says nothing about that driver's grants.

## Troubleshooting and handoff

1. **Does the server connect?** Run `hermes mcp test jev_browser` for Hermes, or `opencode mcp list` in an OpenCode session. If the config changed while Hermes was running, `/reload-mcp` is the documented in-session refresh path. Do not force a gateway restart from an agent running inside that gateway; the runtime blocks it because the command would kill itself.[4][5]
2. **Does the browser work without an agent?** Run:
   ```bash
   ~/.local/bin/jev-browser-launch run \
     'Open the example page and stop once Example Domain is visible' \
     https://example.com --no-typing --no-screenshot --max-steps 3 --max-seconds 30
   ```
   Check `status`, `final_url`, `jev_provider`, `degraded`, `warnings`, and `steps`. Never print the underlying key for diagnosis.
3. **Missing credential?** The launcher expects `OPENROUTER_API_KEY` in the default Hermes `.env`. Check presence and shape without exposing its value. OpenCode's model login is not proof that the MCP subprocess received a key; the shared launcher deliberately supplies one.
4. **Missing browser executable?** Check Playwright's Chromium installation for this package. The initial install used `playwright install chromium` from the test clone; a package update can change the required browser revision. Use the installed package's Playwright CLI and re-test rather than copying a binary by hand.
5. **Typed text missing or degraded?** Inspect `typing_provider`, `typing_model`, `degraded`, and `warnings`; distinguish a Jev judgment failure from a typing-model failure. This setup forces OpenRouter for both. Never permit the package to fall back to its deprecated GPT-5.6 default.
6. **Unexpected page, bot challenge, or `done` too early?** Read each trace step, console/network events, and final URL/content. An agent's completion score is advisory. Stop rather than retrying an action that may have submitted a form.
7. **Before upgrades:** compare the pinned package release and dependency audit, run its offline tests and an anonymous live smoke, then confirm both MCP hosts still discover the tool. Preserve the prior version for rollback. No automatic latest-version `npx` resolution was left in the agent configs.
8. **Rollback/disable:** Hermes can set `mcp_servers.jev_browser.enabled` to `false` with its config CLI and reload MCP. OpenCode can change this entry's `enabled` flag to `false` in its global config. Disable both consumers before removing the shared package or launcher. Do not delete or rotate the existing OpenRouter key just to disable Jev.

## Open decisions

- Whether a native desktop Jev decision adapter is worth building. First choose a concrete app and bounded task; determine whether existing `computer_use` already handles it better.
- Whether to keep this community package enabled for general use while its runtime dependency audit includes a high advisory. The current Hermes approval gate reduces action risk, but it does not remove dependency risk.
- Whether generic Jev judgments (`evaluate`, reranking, classification) should be a separate future MCP project. The two attached reports discuss this, but it was outside the browser-first implementation.
- Codex and Claude integration remains a later, separate per-tool decision. Neither was configured or tested in this work.
- The existing Hermes adapter mapping in this workspace predates this experiment and says no MCP servers were configured at its earlier check. This record supersedes that historical **observation** for Jev Browser only; a proper one-tool adapter reconciliation should update the mapping without silently promoting this community connector to portable workspace policy.

## Provenance and sources

**User-supplied originals:**

- `sources/jevreport1.md`, 33,221 bytes, SHA-256 `fb7c3eddc664adbf325d4471cb8ebff86e13d3c3db72a341b6597682dd710443`.
- `sources/jevreport2.md`, 38,959 bytes, SHA-256 `2e0ae3f42dd401259a510e080f61c716a3cffed33e47c1553612365d61a871a2`.

These are preserved byte-for-byte from the two documents the user supplied. Their recommendations and unresolved citation markers are retained as evidence of the input, not silently adopted as fact. The local observations above are labeled separately. The upstream repository commits inspected were Jev Browser `269cd1076faf370402a7db337531bee5b6c55978` and Browser Use Ultrafast `1231850a0bf1a0c0341fe408ef1668dbbfdfac46`. Repository documentation and provider behavior can change after this check.

## Sources

[1] https://github.com/jkudish/jev-browser
[2] https://github.com/browser-use/jev-ultrafast
[3] https://docs.typesafe.ai/introduction
[4] https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
[5] https://opencode.ai/docs/mcp-servers
[6] https://github.com/browser-use/jev-ultrafast/issues/93
