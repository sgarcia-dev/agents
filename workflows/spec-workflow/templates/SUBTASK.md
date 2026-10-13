# TNN: <Verb Object>

## Objective

## Why This Exists

## Required Read Set

## Do Not Read By Default

## Allowed Edits

## Forbidden Edits

## Known Facts And Assumptions

## Source Checkout (source, test, Git, or checkout-bound runtime/browser packets)

- Effective selector:
- Resolved absolute working directory:
- Expected repository identity:
- For unrelated packets: not applicable.

## Runtime Target (runtime/browser packets only)

- Required: yes/no
- Instance or identifier:
- Exact URL:
- Process owner:
- Reuse permission:
- Stop or handoff responsibility:
- For packets without runtime needs: `Runtime Target: n/a`.

## Dependencies

- Depends on:
- Blocks:
- Parallel-safe with:

## Worker Model Tier And Judgment

- Worker model tier: default | fast | high | phase_owned
- Judgment allowed: false | bounded | phase-owned-only
- Estimated working material: <characters across packet, reads, and output>
- Expected runtime and cancellation threshold:
- Max files to read:
- Max serious attempts: 3
- Escalate if:

Use `default` for small micro packets. Use `fast` only when the user explicitly
requests hurry-mode micro delegation. Use `high` for a bounded packet that cannot
be split safely and needs stronger reasoning, more integrated context, or a richer
handoff. Use `phase_owned` when the work
requires top-level integration, product judgment, durable-memory judgment,
security sensitivity, or final acceptance; do not dispatch those packets to
workers.

## Implementation Steps

## Acceptance Criteria

## Verification

## Stop Conditions

Stop if:
- packet contradicts source truth
- required context is missing
- edit requires forbidden scope
- verification fails repeatedly
- broader design judgment appears

## Report Shape

Write `../results/TNN.result.md` using `WORKER_RESULT.md`.
