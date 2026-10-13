---
created_at: 2026-07-09
updated_at: 2026-09-15
model: gpt-5.6-sol
doc_type: capability
purpose: Portable runbook for local repository operations through the Git MCP connector.
related:
  - path: ../connectors.md
    why: Connector inventory and default posture.
  - path: ../AGENTS.md
    why: Capability-folder rules and write boundaries.
---

# Git MCP

## Overview

Git MCP provides repository-scoped status, history, diff, branch, and limited
file-state operations against a local checkout. It is local and requires no
connector authentication.

Use native Git when the command is clearer, when staging is required, or for
history surgery and other operations outside the connector's allowlist.

## When To Use

- Inspect status, branches, commits, and diffs from an agent session.
- Review local repository state before a change.
- Create or switch branches in a controlled checkout.

## Safety

- Confirm the active repository and working tree before write operations.
- Never assume the connector is operating on the repository in the terminal.
- Keep credentials and remote tokens in the host's Git credential manager.
- Use native Git for precise staging, reset, restore, rebase, cherry-pick, stash,
  bisect, and submodule operations.

## Verification

1. Ask for repository status.
2. Confirm the current branch.
3. Compare the latest commit with native `git log -1 --oneline`.
4. Inspect the working-tree diff before any write.

## Troubleshooting

- Wrong repository: open the intended checkout and repeat the status check.
- Missing write action: use native Git for the unsupported operation.
- Unexpected branch or diff: stop and resolve repository identity before editing.
- Authentication failure: use the host's normal Git credential or SSH setup.

## Known Limitations

- The connector is narrower than the Git CLI.
- It does not replace GitHub or other hosted repository connectors.
- Connector availability is bounded by host filesystem permissions.

## Maintenance Notes

- Keep the documented operation scope aligned with the connector registry.
- Do not add credentials, tokens, or host-specific secrets to this guide.
