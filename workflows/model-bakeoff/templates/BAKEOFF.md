---
created_at: <YYYY-MM-DDTHH:MM:SSZ>
model: <orchestrator-model>
artifact_category: <audits-or-changes>
doc_type: audit
purpose: Define one model bake-off benchmark run.
related: []
---

# Model Bakeoff: <Title>

## Status

Prepared | Configured | Executing | Evaluating | Cleanup Pending | Complete | Blocked

## Scope

- Task type: research | coding | review | mixed
- Scope: global | project | repository | cross-repo
- Repository path, if applicable:
- Base branch, if applicable:
- Base commit, if applicable:

## Benchmark Task

```text
<Exact prompt given to every contestant>
```

## Competitors

| Label | Requested model | Adapter status | Resolved native model | Native wrapper | Notes |
|---|---|---|---|---|---|
| <label> | <requested> | pending |  |  |  |

## Isolation

- Mode: reports | git_worktrees | other
- Contestant output root:
- Worktree root, if applicable:
- Peer-output access forbidden: yes

## Verification

- Required commands or checks:
- Optional commands or checks:
- Uniformity notes:

## Timing Method

- Orchestrator records wall-clock start/end: yes
- Timeout policy:
- Self-reported contestant timing accepted only as fallback: yes

## Rubric

- Rubric type: default | custom
- Weights, if non-equal:
- Additional criteria:

## Cleanup Policy

- Cleanup: auto | ask | keep_finalist | keep_all
- Native config cleanup required:
- Worktree cleanup required:
- Restart or new session required after cleanup:

## Stop Conditions

- Unresolved competitors:
- Missing authorization:
- Isolation risk:
- Verification mismatch:
- Cleanup risk:
