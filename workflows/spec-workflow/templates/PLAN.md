---
plan_version: 1
# Optional; persist any effective non-default named selector.
# source_checkout: <selector>
scope: project # global | project | cross-repo
project: <project-or-null>
repos:
  - <repo-or-null>
allowed_paths:
  - <path>/**
forbidden_paths:
  - <path>/**
required_reads:
  - AGENTS.md
  - PLAN.md
optional_reads: []
verification:
  required:
    - <command-or-manual-check>
  optional: []
worker_strategy:
  workers_allowed: true
  default_worker_model_tier: default
  allowed_worker_model_tiers:
    - default
  max_worker_packets: 3
permission_profile: workspace-edit-with-tests
plan_reconcile:
  required: true
  expected_files: []
---

# PLAN

## Status
Planned | Approved | Executing | Blocked | Superseded

If the structured frontmatter conflicts with the prose plan, stop and ask for
clarification or update `PLAN.md` before execution. The frontmatter is the
compact execution contract; the body explains rationale and details.

## Scope

- Owning scope:
- Source repo / project:
- Change folder:
- Current spec targets:
- Change-local spec deltas:

## Source Checkout

- `source_checkout`: omit for the owning project's default/current existing
  behavior; set for any effective non-default named selector, including one
  selected from an opted-in managed initial session workspace.
- Plan-create must disclose the effective selector during human review and
  validate its checkout before source discovery. Capture the initial workspace
  once; later CWD changes never reselect it.
- Plan-execute resolves the selector before source work and propagates the
  resolved absolute working directory and repository identity to source, test,
  Git, and checkout-bound runtime/browser worker packets. Once this plan exists,
  its selector or intentional omission governs.

## Parallel Checkout Allocations (optional)

Omit for ordinary single-checkout work. Add only when the human-approved
execution strategy explicitly authorizes parallel or multithreaded work.

| Packet / owner | Selector | Absolute working directory | Repository identity | Lifecycle |
|---|---|---|---|---|
| `<packet>` | `<selector>` | `<path>` | `<identity>` | `<start/stop/handoff>` |

## Runtime Target (optional)

Omit when no runtime is needed. An ordinary plan may own at most one active
runtime; multiple simultaneous runtimes require the approved parallel strategy.

| Packet / owner | Selector | Absolute working directory | Instance / identifier | Exact URL | Reuse | Stop / handoff |
|---|---|---|---|---|---|---|
| `<packet>` | `<selector>` | `<path>` | `<instance>` | `<URL>` | `<allowed?>` | `<responsibility>` |

## Goal

## Non-Goals

## Selected Tier

- Tier:
- Reason:
- Rejected lighter/heavier tiers:

## Execution Strategy

- Execution mode: single-agent | orchestrated-subtasks
- Subtask ordering: none | sequential | parallel | mixed
- Top-level responsibilities:
- Worker responsibilities:
- Reasoning budget:

## Execution Graph

- Parallel-safe:
- Sequential dependencies:
- Critical path:

## Worker Packet Strategy

- Single-worker plan only: yes/no
- Subtasks required: yes/no
- Worker model tiers allowed: default | fast | high | phase_owned
- Fast tier explicitly requested by user: yes/no
- High tier justification and bounded context estimate, or `n/a`:
- Why:

## Verification Strategy

- Commands:
- Review/verify workers:
- Manual checks:
- Skip reasons:

## Durable Memory Impact

- `MEMORY_DELTA.md` required: yes/no
- Expected impacted files:
- Change-local spec deltas required: yes/no

## Plan Reconcile Requirements

- Plan-reconcile required: yes/no
- Expected reconcile inputs:

## Stop Conditions

## Approved Direction & Review Fidelity

- Human sign-off (who / when):
- Approved outcome and boundaries:
- Approved design, ownership, and important names:
- Approved edit surfaces:
- Approved verification bar:
- Resolved clarifications (question -> answer):
- Material differences from the presented proposal: none | <difference>
- Reapproval evidence for material differences:
- Residual or deferred questions:
