# Capabilities

Use this folder for portable descriptions of external bridges agents may use.
A capability describes what an agent can reach outside the context window; a
skill or role describes how to use it.

## Belongs Here

- MCP or connector capabilities.
- Non-MCP tool bridges such as plugins and extensions (for example, Codex plugins).
- CLI capabilities.
- Script capabilities.
- API or SDK capabilities.
- Retrieval, search, browser, local runtime, or IDE capabilities.
- Capability risks, permissions, approval expectations, and verification notes.

## Does Not Belong Here

- Tool-specific runtime config, credentials, or secrets.
- Full vendor manuals or exhaustive API docs.
- Workflow instructions that belong in `../skills/` or `../workflows/`.

## Portable Layer vs Tool Layer

Capabilities are the **portable layer**: what an external bridge is, what it is
for, its approval posture, and how to verify results, independent of any tool.
The **tool layer** (each `adapters/<tool>.md` connectors/MCP inventory) records
which native servers a specific tool wires and maps them back to this portable
layer. Keep them separate: a connector's identity and risk live here; a tool's
wiring of it lives in that tool's adapter doc.

## Connectors & Plugins Registry

`connectors.md` is the portable awareness inventory of retained MCP servers and
non-MCP bridges (plugins/extensions). During `sync-tool-adapter`, each tool's
native connector/plugin config is reconciled against it. Listing is not
endorsement: promotion upstream and enabling a connector for a tool are explicit
per-item user decisions, never automatic. A tool-exposed bridge with no registry
coverage is surfaced as `missing-in-workspace` for a user decision. Never store
credentials or secrets in the registry.

## Current Guidance

A capability doc is the full working reference for its bridge: what it can
do, exact commands and flags, costs, approvals, known failures, and dated test
results. Skills stay short and hold the procedure; they link here for facts.
Dated guides (kept in a private folder, not published) are the evidence trail, not the place to look
first. Keep vendor manuals out; record only what agents here need. Do not expose dangerous write-capable actions as normal defaults.

The browser section in `connectors.md` intentionally includes native browser
tools, CLI/library calls, hosted APIs/services, and desktop drivers as
**awareness-only** bridges. Their inclusion does not require installation,
configuration, or enablement during sync. The curated Playwright, DevTools and
Jev MCP entries follow the registry's default-off connector rule. The portable
`../skills/browser-use/SKILL.md` selects the route; each bridge guide owns its
connection modes, onboarding prerequisites, known failures, and proof check.

Adapters retain exact native identifiers and launch mechanics, but must not copy
live vendor catalogs into multiple durable files.

## Web reference

`web/` is the single home for search and fetch tool facts, separate escalation ladders, compatibility and generic observations. Read [the web reference](web/README.md). Native search and fetch are the ordinary default. Both web-search skills are request-only.

## Web scraping site access

Per-platform access routes (social networks, forums, job boards, employer job feeds) and third-party data providers (Apify, ReefAPI, Bright Data, SerpApi and similar) live in the web-scraping-site-access spec, one file per site and per provider, so this folder does not grow a file per platform. When a provider is wired into a tool as a live bridge, record the wiring in `connectors.md` and the tool adapter; its facts stay in the spec.
