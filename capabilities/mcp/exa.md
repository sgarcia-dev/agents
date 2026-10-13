---
created_at: 2026-09-29
updated_at: 2026-10-01
model: anthropic/claude-opus-5-5
doc_type: capability
purpose: Connection and setup reference for Exa MCP; web tool facts live in capabilities/web.
related:
  - path: ~/agents/capabilities/connectors.md
    why: Connector inventory and default posture.
  - path: ~/agents/capabilities/mcp/parallel.md
    why: Parallel connection and setup reference.
  - path: ~/agents/capabilities/mcp/firecrawl.md
    why: The other escalation connector.
  - path: ~/agents/capabilities/web/tools/parallel.md
    why: Shared setup pattern, permissions, and install order for all three harnesses.
  - path: ~/agents/capabilities/web/README.md
    why: When agents should escalate to Exa.
---

# Exa MCP connection

2026-10-01: This file keeps connection and setup facts. Search and fetch quality, prices, limits and routing moved to [exa](../web/tools/exa.md). Current ladders and compatibility: [web reference](../web/README.md).

Keyed Codex calls passed the September 29 CLI tests and September 30 adapter checks. Older pending status is superseded. Configure only the current harness in its own authorized session. No native configuration was changed by this consolidation.

## Endpoint and auth

URL: `https://mcp.exa.ai/mcp` (streamable HTTP). The live server reported
`exa-search-server` 3.2.1 on Sept 29. GitHub `main` is 3.4.1, so the live
server lags the source.

| Mode | How | Who pays |
|---|---|---|
| Keyless | Plain URL | Exa. Rate limited per IP. Source defaults are 2 calls a second and **50 calls a day**; the live values are not published. Shared office or cloud IPs get throttled sooner. |
| API key | Header `x-api-key: <key>` (documented). `Authorization: Bearer <key>` also works per the source. | Your Exa team. Free accounts: 10 calls a second, team-wide across all keys. |
| OAuth | `https://mcp.exa.ai/mcp?login` | Your Exa team |

The server also accepts `?exaApiKey=` in the URL. **Never use it.** URLs end up
in logs and config dumps.

### URL settings the hosted server reads

| Parameter | Effect |
|---|---|
| `tools=a,b,c` | Exact tool list. Replaces the defaults. Unknown names are dropped silently. |
| `defaultSearchType=instant` | Meant to make `web_search_exa` use the $4 `instant` tier. Found in the server source, not Exa's docs. **Does not lower the bill:** live keyed calls on Sept 29 still cost $0.007. Harmless, so the URLs keep it. |
| `login` | Forces the OAuth sign-in. |


## Connect (server name `exa`)

Keys come from the `EXA_API_KEY` env var and go in Exa's documented
`x-api-key` header. (A bearer header also works per the source, but use the
documented form.)

**Claude Code**

```sh
# Keyless
claude mcp add --transport http --scope user exa 'https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa&defaultSearchType=instant'

# Keyed
claude mcp add-json --scope user exa '{"type":"http","url":"https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa&defaultSearchType=instant","headersHelper":"~/agents/capabilities/mcp/search-key-header.sh exa"}'
```

Allow it: `"allow": ["mcp__exa__*"]` in settings. No `ask` rule; it would
stall headless runs.

**Codex**

```sh
# Keyless
codex mcp add exa --url 'https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa&defaultSearchType=instant'

```

Then in `~/.codex/config.toml`:

```toml
[mcp_servers.exa]
url = "https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa&defaultSearchType=instant"
default_tools_approval_mode = "approve"
tool_timeout_sec = 120
# Keyed: add
# env_http_headers = { "x-api-key" = "EXA_API_KEY" }
```

**OpenCode v2**

Edit `~/.config/opencode/opencode.jsonc` by hand, under `"mcp": { "servers": { ... } }`:

```jsonc
"exa": {
  "type": "remote",
  "url": "https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa&defaultSearchType=instant",
  "oauth": false
  // Keyed: add
  // "headers": { "x-api-key": "{env:EXA_API_KEY}" }
}
```

Allow it in the `permissions` array:
`{ "action": "exa_*", "resource": "*", "effect": "allow" }`.

## Local stdio alternative

`exa-mcp-server@3.4.1` on npm, with env `EXA_API_KEY` and
`DEFAULT_SEARCH_TYPE=instant`. It needs a key. Use it only if a harness
cannot do remote MCP. Pin the version; never run a bare `npx -y`.


## Troubleshooting

- **429 keyless:** daily per-IP limit. Add a free key.
- **402:** credits used up, or the key's budget is reached. Wait for the 1st
  or raise the key budget.
- **401 with `agent_run` in `tools=`:** that tool needs a key. Remove it.
- **Auth goes to a browser sign-in unexpectedly:** the URL contains `login`
  or a `client=` value containing "plugin".
