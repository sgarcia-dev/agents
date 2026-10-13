# Orchestrator Packet: <Phase Or Bounded Queue>

> **PAUSED TEMPLATE: DO NOT CREATE OR USE THIS PACKET.** `task-orchestrator` is
> disabled by `../../../roles/task-worker-tiers.md`. Retain this template only for
> a future explicit user re-enable.

## Identity And Depth

- Orchestration run ID:
- Parent task or queue ID:
- Mode: ad hoc queue | research | research-deep | plan-create | plan-execute | plan-reconcile
- Native wrapper or one-run profile:
- Profile lifetime: permanent wrapper | this process only
- Requested model, reasoning, and service class, or adapter default:
- Verified runtime profile and evidence:
- Exact user instruction authorizing each fast selection, or `n/a`:
- Current delegation depth: 1
- Maximum delegation depth: 2
- Child remaining delegation depth: 0

## Objective And Completion Boundary

## Interaction Mode

- `interactive` | `autonomous`
- Explicit autonomous instruction, if any:

## Authority Boundary

- In-scope decisions delegated:
- Root-owned decisions:
- User-authority decisions:
- Granted permissions:
- Forbidden actions:

## Canonical Inputs And Outputs

- Authoritative input paths:
- Durable outputs:
- Parent handoff path:
- Existing handoff/checkpoint to resume, or `none`:
- Native continuation/session ID when supported, or `none`:

## Source And Runtime Identity

- Source checkout selector:
- Resolved working directory:
- Expected repository identity:
- Runtime target, or `n/a`:

## Delegation Plan

- Allowed children: determine only after a future explicit re-enable from
  `../../../roles/task-worker-tiers.md`.
- Leaf packets, dependencies, and sequencing:
- No orchestrator, generic-agent, peer-orchestrator, or deeper delegation:

## Budget And Scheduling

- Maximum leaf packets:
- Maximum rounds:
- Maximum serious attempts per leaf:
- Concurrency limit:
- Default scheduling: sequential
- Explicitly independent parallel groups:

## Known Facts And Assumptions

## Verification

## Attempt Limit And Stop Conditions

## Parent Return

Return only status, the canonical handoff path, and one next root action.
