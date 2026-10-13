---
created_at: 2026-07-09
updated_at: 2026-09-15
model: gpt-5.6-sol
doc_type: capability
purpose: Portable runbook for repository collaboration through a GitHub MCP connector.
related:
  - path: ../connectors.md
    why: Connector inventory and default posture.
  - path: ../AGENTS.md
    why: Capability-folder rules and write boundaries.
---

# GitHub MCP

## Overview

GitHub MCP provides hosted repository context such as repositories, files, pull
requests, issues, discussions, and CI status. The exact server URL, available
tools, and write permissions depend on the host and GitHub deployment.

Use the GitHub CLI when a mutation is not clearly exposed and verified through
the connector.

## When To Use

- Read repository files and metadata.
- Inspect pull requests, issues, reviews, branches, and workflow status.
- Summarize repository-scoped discussion without switching to a browser.
- Use Git MCP for a local checkout and GitHub MCP for hosted objects.

## Install / Configure

Configure the GitHub MCP server through the host's native MCP settings. Use the
endpoint supplied by the host or GitHub administrator rather than copying an
endpoint from another deployment. Keep the server name stable after setup.

Do not store tokens, client secrets, private headers, or credentials in this
guide. Use the host's OAuth flow or credential manager.

## Authentication And Safety

- Complete authentication separately in each host that uses the connector.
- Review requested repository and organization scopes before approval.
- Treat write-capable tools as explicit actions requiring confirmation.
- Prefer `gh` for bulk, scripted, or write-heavy operations.

## Verification

1. Confirm the server appears connected in the host.
2. Read a repository or file the user can already access.
3. Inspect a pull request or issue and verify its title and status.
4. Confirm returned data matches the selected repository and account.

## Troubleshooting

- Server missing: check the resolved host configuration and restart the session.
- OAuth loop: reconnect and verify the server name and callback settings.
- Empty results: confirm repository permissions and the exact owner/name.
- Write failure: check scopes, then use `gh` if the action is supported there.
- Stale data: refresh the host session and verify the object directly on GitHub.

## Known Limitations

- Tool coverage and permissions vary by deployment.
- Hosted data can lag the current repository state.
- Broad code search may require a dedicated code-search tool or local checkout.
- The connector is not a substitute for reviewing the actual diff before a merge.

## Evidence Sources

- https://github.com/github/github-mcp-server
- https://cli.github.com/manual/

## Maintenance Notes

- Keep deployment-specific URLs and auth details in native host configuration.
- Update the registry when the connector's tools or default posture changes.
- Keep write guidance conservative until the exposed tools are verified.
