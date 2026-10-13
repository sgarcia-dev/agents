---
created_at: 2026-07-09
updated_at: 2026-09-15
model: gpt-5.6-sol
doc_type: capability
purpose: Portable runbook for design inspection through the Figma MCP connector.
related:
  - path: ../connectors.md
    why: Connector inventory and default posture.
  - path: ../AGENTS.md
    why: Capability-folder rules and portable-layer boundaries.
---

# Figma MCP

## Overview

Figma MCP provides structured access to design files, frames, components, and
design tokens. Treat it as a read-first design-data connector.

## When To Use

- Inspect components, variants, tokens, and layout details before implementation.
- Read a node-specific URL for precise design context.
- Compare a visual result with the source design.
- Use the desktop bridge when the target file is already open locally.

Prefer a direct Figma link or screenshot when the request is primarily visual or
does not identify a specific file or node.

## Install / Configure

The hosted connector endpoint is:

```text
https://mcp.figma.com/mcp
```

Figma Desktop may also expose a local connector while Dev Mode MCP is enabled:

```text
http://127.0.0.1:3845/mcp
```

Use the host's native MCP configuration and keep aliases consistent with that
configuration. Do not store credentials in this guide.

## Authentication

- Use the sign-in or OAuth flow provided by the host.
- Re-authenticate when the connector reports an expired or invalid session.
- File access follows the user's Figma permissions.

## Verification

1. Connect to a file the user can already open.
2. Query a node-specific URL.
3. Confirm the returned frame, component, or token values match the design.
4. For the desktop bridge, confirm the file is open in Figma Desktop.

## Troubleshooting

- Connection refused: start Figma Desktop and enable Dev Mode MCP when using the
  local bridge.
- Empty data: verify the file is open locally or that the remote account has
  access.
- Access denied: request permission to the target file.
- Vague results: use a node-specific URL instead of a file-only URL.
- Rate limiting: reduce repeated calls and query one focused node at a time.

## Known Limitations

- File access is permission-gated.
- The local bridge only works while Figma Desktop is running.
- File-level URLs without a node ID may not provide enough structured context.
- This guide does not define write behavior for design files.

## Evidence Sources

- https://www.figma.com/developers/api
- https://github.com/GLips/Figma-Context-MCP

## Maintenance Notes

- Keep endpoint and alias examples aligned with the connector registry.
- Recheck the hosted and desktop endpoints when Figma changes its MCP offering.
- Keep design-system-specific procedures in the owning project or skill.
