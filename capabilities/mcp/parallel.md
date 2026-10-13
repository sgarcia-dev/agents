---
created_at: 2026-09-29
updated_at: 2026-10-01
model: anthropic/claude-opus-5-5
doc_type: capability
purpose: Connection and setup reference for Parallel MCP; web tool facts live in capabilities/web.
related:
  - path: ~/agents/capabilities/connectors.md
    why: Connector inventory and default posture.
  - path: ~/agents/capabilities/mcp/exa.md
    why: Escalation connector for meaning-based search.
  - path: ~/agents/capabilities/mcp/firecrawl.md
    why: Escalation connector for hard pages and whole sites.
  - path: ~/agents/capabilities/web/tools/parallel.md
    why: Shared setup pattern, permissions, and install order for all three harnesses.
  - path: ~/agents/capabilities/web/README.md
    why: When agents should use Parallel, and when to escalate.
---

# Parallel MCP connection

2026-10-01: This file keeps connection and setup facts. Search and fetch quality, prices, limits and routing moved to [parallel](../web/tools/parallel.md). Current ladders and compatibility: [web reference](../web/README.md).

Keyed Codex calls passed the September 29 CLI tests and September 30 adapter checks. Older pending status is superseded. Configure only the current harness in its own authorized session. No native configuration was changed by this consolidation.

## Endpoints and auth

| URL | Auth | Use |
|---|---|---|
| `https://search.parallel.ai/mcp` | None, or `Authorization: Bearer <key>` | **Default.** Keyless is free with lower limits. A key raises limits and unlocks setting overrides. |
| `https://search.parallel.ai/mcp-oauth` | OAuth sign-in or key. Anonymous gets 401 | Only if you prefer OAuth. |
| `https://task-mcp.parallel.ai/mcp` | Key or OAuth; never anonymous | Deep research tasks. **Not part of this setup.** |

- Transport: streamable HTTP. Live server said "Parallel Web Search MCP
  Server" v1.27.0 on Sept 29.
- The old address `https://search-mcp.parallel.ai/mcp` is retired. Replace it
  in any old config.
- Key goes in the `Authorization: Bearer` header. No key-in-URL form exists.
  Never put a key in a URL.
- Keyless limits are not published. The tools ask the model for a
  `session_id`, which Parallel uses to rate-limit the free tier. Reusing one
  per conversation is fine.


## Connect (server name `parallel`)

Use the name `parallel` everywhere so permission rules match:
`mcp__parallel__*` in Claude Code, `mcp__parallel__*` in Codex, and
`parallel_*` in OpenCode.

**Claude Code**

```sh
# Keyless
claude mcp add --transport http --scope user parallel https://search.parallel.ai/mcp

# Keyed (single quotes keep ${PARALLEL_API_KEY} out of the shell)
claude mcp add-json --scope user parallel '{"type":"http","url":"https://search.parallel.ai/mcp?mode=fast","headersHelper":"~/agents/capabilities/mcp/search-key-header.sh parallel"}'
```

Parallel's docs say to log in through `/mcp` after adding. That step is not
needed for the keyless URL.

**Codex**

```sh
# Keyless
codex mcp add parallel --url https://search.parallel.ai/mcp

# Keyed
codex mcp add parallel --url 'https://search.parallel.ai/mcp?mode=fast' --bearer-token-env-var PARALLEL_API_KEY
```

Then add `default_tools_approval_mode = "approve"` under
`[mcp_servers.parallel]` in `~/.codex/config.toml`.

**OpenCode v2**

Edit `~/.config/opencode/opencode.jsonc` by hand. `opencode mcp add
--header` may store the key as plain text.

```jsonc
"mcp": { "servers": {
  // Keyless
  "parallel": {
    "type": "remote",
    "url": "https://search.parallel.ai/mcp",
    "oauth": false
  }
  // Keyed: use this instead
  // "parallel": {
  //   "type": "remote",
  //   "url": "https://search.parallel.ai/mcp?mode=fast",
  //   "oauth": false,
  //   "headers": { "Authorization": "Bearer {env:PARALLEL_API_KEY}" }
  // }
} }
```

Allow it in the `permissions` array:
`{ "action": "parallel_*", "resource": "*", "effect": "allow" }`.

## Approval posture

The configured MCP calls are prompt-free. Usage authority and spending rules live in [the web reference](../web/README.md).

## Troubleshooting

- **HTTP 400 on connect:** a bad override in the URL. Check spelling.
- **401:** the key env var is empty in the shell that started the harness.
- **429 keyless:** free-tier limit. Wait, or add a key.
- **Claude Code shows the literal text `${PARALLEL_API_KEY}`:** header
  expansion did not happen for that scope. See
  [mcp-setup.md](../web/tools/parallel.md).
