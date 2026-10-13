---
created_at: 2026-09-25
model: openai/gpt-6-sol
artifact_category: investigations
doc_type: index
purpose: Index six preserved Claude research reports and their provenance, link status and evidence limits.
related:
  - path: ./sources/hermes-cloud.md  # private, not published
    why: Research-only Hermes cloud backend and named-session comparison; not live-tested.
  - path: ./sources/agent-browser.md  # private, not published
    why: Research-only standalone agent-browser session, profile and state-copy comparison; not installed.
  - path: ./sources/cloud-mcp.md  # private, not published
    why: Research-only hosted MCP provider comparison, with vendor and code-reading claims.
  - path: ./sources/local-alternatives.md  # private, not published
    why: Research-only local Playwright, DevTools, Camofox and stealth-route comparison.
  - path: ./sources/camofox-deep-dive.md  # private, not published
    why: Research-only Camofox identity, persistence and process-risk investigation.
  - path: ./sources/authenticated-parallel-validation.md  # private, not published
    why: Research-only adversarial comparison of one-login parallel designs and unresolved contradictions.
---

# Parallel browser options: six-source research index

**Status:** Comparative research dated September 25, 2026. None of these six reports installed a service or ran an authenticated multi-agent browser test. Their recommendations disagree and are not policy. The accepted behavior is in [spec.md](../../../spec.md), current local observations in [STATE.md](../../../STATE.md), and choices in [DECISIONS.md](../../../DECISIONS.md). The earlier three-worker read-only browser test was a separate September 24 observation, not a ten-agent test of any route below.

## Provenance and integrity

These six Markdown files were copied without edits from `~/browser-research-2026-09-25/` into `sources/`. The original external files were left in place rather than deleted. The index and owning memory are new OpenCode writing, **not** original Claude report text. Original reports have mixed headers and no standard Agents artifact frontmatter; preserving their bytes takes precedence over retrofitting metadata. SHA-256 below covers each whole file, including its original header and line endings. Read in the order in `related:` above.

| Original filename, now under `sources/` | Bytes | SHA-256 |
|---|---:|---|
| `hermes-cloud.md` | 16,195 | `648489995b6e752eeaf61912e5d1acdf824295f9a27e03ef5e052ec78a214ec6` |
| `agent-browser.md` | 33,187 | `d14d1b8aa849bbddd4c4d94859e28b427391c360b4b70d1558baf7a3f7d20f22` |
| `cloud-mcp.md` | 26,722 | `c3004c1af6ef88f536bc0bd9b074c678ee57089103f7d5415455e54485337612` |
| `local-alternatives.md` | 31,538 | `bb9a2442bb7a5f924f94c45228420adfcc4d05dbc7e5ce7230b04cdd0c30fdcb` |
| `camofox-deep-dive.md` | 18,030 | `6c78bd983cc3cb906d9f4146b67a3bf8644e682fd9759a70a36e78275eac508e` |
| `authenticated-parallel-validation.md` | 15,821 | `bbd1873259a7d3b8385c04274b17710e603f4d15ab7816c82acca71a4b31df8e` |

The original Downloads report, separately authored `README.md`, logs, session JSON and other neighboring files are **not** members. The retained reports mention that README and Downloads input in prose, including local paths; those references are source provenance, not links to bundled members or endorsement of their claims. No relative Markdown hyperlinks inside the six reports need rewriting; their Markdown hyperlinks point to external HTTP(S) resources and must be checked afresh before reliance. The new index's relative links to owning memory and all six members must resolve. The September 24 Jev bundle is a separate earlier exception and was not modified.

**Link check on September 25:** A Markdown hyperlink scan of these six sources, this index and the five owning files (`AGENTS.md`, `spec.md`, `STATE.md`, `DECISIONS.md`, `SOURCES.md`) found **55 local path links, 55 existing targets, 0 missing targets** and 145 external HTTP(S) links. This checks local target files only, not fragment anchors or the external URLs. None of the six copied sources contains a relative Markdown hyperlink. Prose citations to absent documents are flagged above rather than silently redirected. The Jev bundle's tracked files were unchanged; its research entrypoint retained SHA-256 `bcdac2942d21183a01a275027500a365ebf0eac1e25caf8a48977e25f4cb8908`.

## Reading boundary and contradictions

- **Local observation versus cloud possibility:** The reports describe September 25 read-only source/config checks of an installed Hermes version and public documentation. This index did not re-open native configuration or run browser services. A `cdp_url` override shadowing a Hermes-native cloud/Camofox choice, and a CLI auto-start attaching to a listening debug port, are setup risks to check in the exact future runtime. The reports give inconsistent precedence wording; the effective route needs a runtime check before any migration.
- **Control is not identity:** A Hermes named session or pinned CDP tab can still use the same signed-in Chrome. A shared MCP transport can have hidden active-session/page state. Kernel's explicit IDs and read-only profile snapshots are vendor-documented, not a measured Hermes integration. Browserbase hosted MCP's active-session fallback and lack of hosted Context startup in the reported interface need exact version checks. Browser Use Cloud's claimed concurrency is not proof that Hermes auto-start binds an authenticated profile; the suggested explicit profile start is not tested.
- **One login and many workers:** Copying a local login state is not an independent account, and ten simultaneous site sessions may trigger logout or MFA. Playwright MCP profile-per-agent proposals require separate exclusive directories and manual sign-ins; Camofox `userId` scope and shared Firefox process limit isolation. Kernel profile writes reportedly replace whole snapshots. Browser Use Cloud profile concurrency/save timing remains unresolved. No candidate passed an authenticated 10- or 20-agent run on this Mac.
- **Limits and safety:** The cited Browser Use pricing and concurrency pages disagree about the threshold for 50 browsers; prices and provider quotas are dated vendor claims. RAM estimates, stealth/bot-success claims, page focus behavior, persistence and site tolerance are not local benchmarks. CAPTCHA solving defaults in some providers conflict with the current human-handoff contract; never infer permission to solve a challenge. A live-view URL and exported state are sensitive access, not harmless observation.

The next decision, if requested, is a **single** owner-authorized, tool-owned pilot with a low-stakes account: verify routing, explicit browser/tab ownership, manual login and restart, two or three read-only workers, independent account/URL checks and cleanup, then check site-side effects and billing before scaling. Do not run the setup snippets in these reports as instructions from this index.
