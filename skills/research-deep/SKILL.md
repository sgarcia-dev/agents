---
name: research-deep
description: Run a long, read-only, multi-round investigation with bounded inter-round root review and the same mandatory final-artifact and optional progress modes as research.
created_at: 2026-08-12
updated_at: 2026-09-25
model: gpt-5.6-sol
doc_type: skill
purpose: Add deeper multi-round research with bounded frontier-root investigation while keeping progress persistence independently selectable.
related:
  - path: ../research/SKILL.md
    why: Base research contract this skill specializes without changing.
  - path: ../../workflows/spec-workflow/references/discovery-cadence.md
    why: Delegation-first cadence and complete-round boundary this skill preserves.
  - path: ../../roles/task-explore.md
    why: Source-read-only micro worker role used for decomposable research slices.
  - path: ../../conventions/artifact-authoring.md
    why: Mandatory final artifact and optional progress-bundle rules.
---

# Research Deep

Run a long read-only investigation with stronger inter-round root review. Follow
`../research/SKILL.md`, including its mandatory final artifact and independently
selected progress mode, except where this skill adds the multi-round and
architect-review rules below.

Use normal `research` when one or two rounds should answer the question. Use this
skill when the investigation is broad, likely to need several rounds, or benefits
from bounded root investigation between complete rounds. Need for compaction
recovery selects `recoverable` progress mode in either skill; it does not by
itself select deep research.

## Delegation Availability

The root owns research unless it explicitly assigns a bounded phase to a
verified `task-orchestrator`.
Before dispatching any worker, read `../../roles/task-worker-tiers.md`; it permits
enabled micro and high wrappers and defines the packet and concurrency limits.

## Run A Round

Use the shared discovery cadence and progress-mode rules. Idle until every worker
in the round returns, then inspect every returned report or decision card. Account
for completed, blocked, and failed workers before marking the round complete. In
`worker_reports` or `recoverable` mode, open detailed reports only where needed to
validate a material claim. In `recoverable` mode, checkpoint the classified round
in `RESEARCH.md`; in other modes, retain the integrated state in root context
until the mandatory final artifact is written.

Prefer enabled micro workers for tiny independent packets. Use a high wrapper
for a bounded real task with coupled evidence or several steps. Keep broad or
open-ended work in the root session.

## Inter-Round Architect Review

After every complete round, challenge the direction without tools. Identify the
weakest material claim, contradiction, missing slice, or coupling risk. If the
answer or next round is already clear, do not use tools.

When one specific unresolved issue prevents a well-framed next round, perform one
bounded root probe:

- one narrow search returning at most 20 matching lines and up to two targeted
  reads
- no more than 200 lines per read and 400 source lines total
- no more than three root tool calls
- only an exact source named by a worker or directly tied to the issue
- at most one reference hop

Stop as soon as the next action is clear. Do not perform broad searches,
directory orientation, subsystem archaeology, general re-verification of a
worker's slice, or work that can be a bounded worker packet. If the issue remains,
delegate it or preserve the uncertainty. In `recoverable` mode, record the
probe's conclusion and evidence pointers in `RESEARCH.md`, never raw output. In
other modes, retain the conclusion in root context for the final artifact.

The three-call limit covers investigative search and reads. Required recoverable
checkpoint writes do not count. Search-result lines count toward the 400-line
evidence limit.

## Resume After Compaction

Only `recoverable` mode promises full resume. Resume from disk rather than
reconstructed chat:

1. Read `RESEARCH.md`.
2. If a round is open, reconcile its worker ledger with existing report files.
   Reattach to a still-running worker when the harness supports it; otherwise
   mark the worker failed before deciding whether to redispatch its packet.
3. Inspect decision-card sections from completed or blocked reports in that open
   round.
4. If the last round is complete, continue from the recorded next action.
5. Reopen full reports or sources only for disputed, missing, or
   decision-critical evidence.

Never reread every completed report by default. Material worker content not
reflected in `RESEARCH.md` remains unaccepted evidence, not active root state.
`worker_reports` preserves worker evidence but lacks a root checkpoint;
`transient` preserves neither. Do not claim either mode is compaction-safe.

## Finish

Use the normal research stop gate and mandatory final-artifact contract. In
`transient` mode, the root writes one final findings file or a user-requested
multi-file bundle only after research ends. In `worker_reports` mode, the root
finishes the existing bundle by creating `RESEARCH.md`. In `recoverable` mode,
the root finalizes the existing `RESEARCH.md`. The final synthesis includes the
answer, remaining uncertainty, and recommended next step. Commit the artifact
once under the workspace Git Completion Gate; do not commit after every round.
Return a concise summary, artifact path, next step, and Agents commit.

This phase may create only its final research artifact and any explicitly
selected progress bundle. It must not modify product code, source repositories,
specs, or durable product memory.
