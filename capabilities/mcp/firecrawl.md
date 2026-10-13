---
created_at: 2026-09-29
updated_at: 2026-10-01
model: anthropic/claude-opus-5-5
doc_type: capability
purpose: Connection and setup reference for Firecrawl MCP; web tool facts live in capabilities/web.
related:
  - path: ~/agents/capabilities/connectors.md
    why: Connector inventory and default posture.
  - path: ~/agents/capabilities/mcp/parallel.md
    why: Parallel connection and setup reference.
  - path: ~/agents/capabilities/mcp/exa.md
    why: The other escalation connector.
  - path: ~/agents/capabilities/web/tools/parallel.md
    why: Shared setup pattern, permissions, and install order for all three harnesses.
  - path: ~/agents/capabilities/web/README.md
    why: When agents should escalate to Firecrawl.
---

# Firecrawl MCP connection

2026-10-01: This file keeps connection and setup facts. Search and fetch quality, prices, limits and routing moved to [firecrawl](../web/tools/firecrawl.md). Current ladders and compatibility: [web reference](../web/README.md).

Keyed Codex calls passed the September 29 CLI tests and September 30 adapter checks. Older pending status is superseded. Configure only the current harness in its own authorized session. No native configuration was changed by this consolidation.

## Endpoints and auth

| URL | Auth | Tools |
|---|---|---|
| `https://mcp.firecrawl.dev/v2/mcp` | None (keyless), or `Authorization: Bearer <key>` | Keyless: 3 tools. Keyed: about 26. |
| `https://mcp.firecrawl.dev/v2/mcp-oauth` | Browser sign-in | Same as keyed |
| `https://mcp.firecrawl.dev/v2/mcp-search` | Key or OAuth, no keyless | A fixed 8-tool search-first profile: search (no `scrapeOptions`), developer search, research tools, and scrape for one supplied URL. Smaller, but not needed here. |

- Transport: streamable HTTP. The live server reported `firecrawl-fastmcp`
  3.26.0 on Sept 29.
- The key goes in the bearer header. The server also accepts `x-api-key` and
  `x-firecrawl-api-key`. No key-in-URL form is documented.
- **Keyless limits:** a per-IP daily cap on requests and on credits. The
  numbers are not published. Everyone behind the same public IP (office,
  VPN) shares it. Over the cap: HTTP 429.
- **Keyless did not work in practice (Sept 29, 2026 live test).** Without a
  key the server connects and lists its 3 tools, but every call (search and
  scrape) returned `KEYLESS_ACCESS_NOT_AVAILABLE`, asking for a key. Plan on
  a free key (1,000 credits a month, no card) to actually use Firecrawl.
- **There is no URL setting to hide tools.** Use the harness's tool filters
  instead (see Connect).


## Connect (server name `firecrawl`)

Keys come from the `FIRECRAWL_API_KEY` env var. Tool names repeat the
prefix, for example `mcp__firecrawl__firecrawl_crawl` in Claude Code and
`firecrawl_firecrawl_crawl` in OpenCode.

**Claude Code**

```sh
# Keyless
claude mcp add --transport http --scope user firecrawl https://mcp.firecrawl.dev/v2/mcp

# Keyed
claude mcp add-json --scope user firecrawl '{"type":"http","url":"https://mcp.firecrawl.dev/v2/mcp","headersHelper":"~/agents/capabilities/mcp/search-key-header.sh firecrawl"}'
```

Allow it and hide the expensive tools in settings (no `ask` rule; it would
stall headless runs):

```json
"allow": ["mcp__firecrawl__*"],
"deny": ["mcp__firecrawl__firecrawl_crawl", "mcp__firecrawl__firecrawl_agent",
         "mcp__firecrawl__firecrawl_interact",
         "mcp__firecrawl__firecrawl_monitor_check", "mcp__firecrawl__firecrawl_monitor_checks",
         "mcp__firecrawl__firecrawl_monitor_create", "mcp__firecrawl__firecrawl_monitor_delete",
         "mcp__firecrawl__firecrawl_monitor_get", "mcp__firecrawl__firecrawl_monitor_list",
         "mcp__firecrawl__firecrawl_monitor_run", "mcp__firecrawl__firecrawl_monitor_update"]
```

**Codex**

```sh
# Keyless
codex mcp add firecrawl --url https://mcp.firecrawl.dev/v2/mcp

# Keyed
codex mcp add firecrawl --url https://mcp.firecrawl.dev/v2/mcp --bearer-token-env-var FIRECRAWL_API_KEY
```

Then in `~/.codex/config.toml`:

```toml
[mcp_servers.firecrawl]
default_tools_approval_mode = "approve"
enabled_tools = ["firecrawl_search", "firecrawl_scrape", "firecrawl_map", "firecrawl_parse"]
```

**OpenCode v2**

Edit `~/.config/opencode/opencode.jsonc` by hand, under `"mcp": { "servers": { ... } }`:

```jsonc
"firecrawl": {
  "type": "remote",
  "url": "https://mcp.firecrawl.dev/v2/mcp",
  "oauth": false
  // Keyed: add
  // "headers": { "Authorization": "Bearer {env:FIRECRAWL_API_KEY}" }
}
```

In OpenCode, deny all Firecrawl tools first, then allow search and scrape
without prompts as directed on 2026-09-29 (the last matching rule wins):

```jsonc
{ "action": "firecrawl_*", "resource": "*", "effect": "deny" },
{ "action": "firecrawl_firecrawl_search", "resource": "*", "effect": "allow" },
{ "action": "firecrawl_firecrawl_scrape", "resource": "*", "effect": "allow" },
```

OpenCode v2 has no per-server tool filter, and a deny rule hides a tool
from the model without stopping it from being listed. Do not deny with
`firecrawl_*crawl*`: because the tool name repeats `firecrawl`, that pattern
matches every Firecrawl tool, including `firecrawl_firecrawl_scrape`.

## Local stdio alternative

`firecrawl-mcp@3.26.0` on npm (Node 22 or newer), with env
`FIRECRAWL_API_KEY`. It needs a key and spends the same cloud credits. Use it
only if a harness cannot do remote MCP. Pin the version.


## Troubleshooting

- **429 keyless:** daily per-IP cap (shared with your whole network). Add a
  free key.
- **402:** out of credits, or a spend limit was reached.
- **401 on `/v2/mcp`:** bad key. On `/v2/mcp-oauth`: sign in again.
- **Tools missing after adding:** restart the harness session.
