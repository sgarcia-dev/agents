---
created_at: 2026-07-26
updated_at: 2026-08-25
model: gpt-5.6-sol
doc_type: reference
purpose: Define the mandatory implementation review snapshot used by interactive and autonomous plan-create approval.
related:
  - path: ../SKILL.md
    why: Canonical plan-create procedure that invokes this proposal contract.
  - path: ../../../workflows/spec-workflow/templates/PLAN.md
    why: Durable plan handoff that must preserve the approved proposal.
---

# Implementation Review Proposal

Load this reference after discovery reaches closure and before resolving any
clarifying or approval decision. In interactive mode it lets a human engineer
review a mostly complete implementation direction. In autonomous orchestrated
mode it provides the same disclosed snapshot before the orchestrator applies the
user's explicit delegated approval.

The proposal is a design review, not a progress summary. It must expose enough
of the intended change for the human to catch unnecessary architecture, code
duplication, misplaced responsibilities, confusing names, hidden scope, and an
insufficient regression bar.

## Required Output Order

1. Produce the Implementation Review Snapshot.
2. In interactive mode, ask only the clarifying questions that remain.
3. In interactive mode, ask the explicit final approval question.
4. In autonomous orchestrated mode, ask no questions; record each resolved
   decision and the explicit delegated-approval instruction instead.

Questions refine a disclosed proposal. They never replace it. If user intent is
the only unresolved input, present the best credible proposal with the relevant
assumption made explicit, then ask the decision question.

## Implementation Review Snapshot

Use these headings in this order. Scale their depth to the planning tier, but do
not silently omit a heading. Write `None` with a brief reason when a section does
not apply.

````markdown
## Implementation Review Snapshot

### Outcome And Boundaries
- **Goal:** <observable user or system outcome>
- **In scope:** <behaviors and surfaces that will change>
- **Not in scope:** <material exclusions>
- **Must remain true:** <existing behavior or contract to preserve>
- **Source checkout:** <effective named selector, whether it is the project
  default or a non-default, selection origin (explicit, managed session, or
  project default), and the resolved absolute working directory; state whether
  `source_checkout` will be persisted>
- **Parallel checkout allocations:** <None for ordinary work, or each proposed
  packet owner, managed selector, resolved path, repository identity, and
  lifecycle; requires approval>
- **Runtime target:** <None when no runtime is needed, one explicit owned target
  for ordinary work, or proposed per-packet checkout, working directory,
  instance/identifier, exact URL, process owner, reuse, and stop/handoff fields
  for approved parallel work>

### Current-To-Target Design
- **Today:** <where the responsibility and flow live now>
- **After this change:** <where the responsibility and flow will live>
- **Responsibility boundaries:** <owner -> single responsibility and collaborators>
- **Contracts or state affected:** <inputs, outputs, APIs, schemas, persisted state, or None>
- **Important names:** <new or reused symbols/concepts and why the names fit local vocabulary>

### Proposed Changes

#### `<path>`: `<symbol or section>`
- **Why:** <one sentence explaining why this change is necessary>
- **Proposed change:**
```diff
<source-grounded current lines and exact proposed lines>
```
- **May vary without asking:** <demonstrably behavior-preserving mechanical
  details, or `Nothing`; this cannot waive a reviewed name, style, or behavior>

### Supporting Changes
- `<path or surface>`: <concise purpose and expected effect>

### Execution And Verification
- **Implementation order:** <only the meaningful dependency order>
- **Parallel-safe work:** <independent slices or None>
- **Critical path:** <the shortest sequence that determines completion>
- **Verification:** <behavior or regression risk -> strongest suitable proof>
- **Completion signal:** <observable condition that makes the work complete>

### Decisions, Alternatives, And Risks
- **Recommended decisions:** <material choice -> recommendation and reason>
- **Rejected alternatives:** <credible simpler/different option -> why it loses here>
- **Risks and mitigations:** <concrete failure mode -> mitigation or stop condition>
- **Assumptions:** <assumption -> supporting evidence or question below>
````

## Concrete Content Rules

- Describe the selected implementation, not topics that execution still needs to
  investigate. A resolvable unknown means discovery is not finished.
- List every expected production, configuration, workflow, schema, or durable
  documentation surface. Use an exact path when known; otherwise use the
  smallest bounded surface, mark it `candidate`, and explain what confirms it.
- Use a proposed-change block for every distinct decision-bearing non-test source
  change; behavior-bearing configuration, schema, migration, or script change;
  and documentation, workflow, spec, or template change whose content is the
  requested outcome. Reusable test harness, framework, or runtime code also
  requires a block.
- In each proposed-change block, use a concise unified diff with current lines
  grounded in inspected source and exact proposed lines. Omit unchanged context,
  not decision-bearing logic. Do not use pseudocode, placeholders, or omission
  ellipses to hide changed behavior or wording; valid source syntax remains valid.
- The phase agent authors this content itself. Do not delegate authoring critical
  proposed content to a worker. For a spec, spec delta, durable memory, guidance,
  or another critical artifact, the exact wording shown here must be the same text
  persisted verbatim into the change folder, so the durable plan matches the
  review and `plan-execute` applies it without composing anything. See
  "Critical Content Is Phase-Owned And Written Verbatim" in the plan-create skill.
- Group mechanically identical edits only when one exact hunk and an explicit
  transformation rule fully represent them. List every affected surface, and do
  not group distinct names, logic, ownership, or wording choices.
- Keep assertion-only tests, fixtures, incidental documentation in a code-led
  change, generated files, metadata, and mechanical edits under Supporting
  Changes. State their purpose and expected effect without dumping test code.
- Classify a surface by its role in this change, not its file extension. When an
  exact decision-bearing change is still unknown, discovery is not finished
  unless the human explicitly approves the bounded detail left to execution.
- Phrases such as "update relevant files," "wire it up," "refactor the logic,"
  or "handle edge cases" do not satisfy either section.
- Name important new functions, types, components, state, files, or concepts.
  Explain how each proposed name fits nearby terminology. If no important name is
  introduced, say so.
- For every new abstraction, identify its owner, one responsibility,
  collaborators, and why an existing owner cannot absorb the behavior. This is
  the primary check against unnecessary architecture and duplication.
- Explain current-to-target control flow, data flow, or state flow where it affects
  ownership or behavior. Do not provide line-by-line pseudocode unless the
  algorithm itself is the decision under review.
- Describe verification by behavior and regression risk. Name likely test
  surfaces or commands when known, but do not enumerate every unit-test case.
- Include only material alternatives, risks, and assumptions. Generic claims such
  as "cleaner," "scalable," "robust," or "maintainable" require a concrete
  constraint or failure mode.
- Do not repeat the goal in every section. Each sentence must add a mechanism,
  boundary, decision, or piece of evidence.

## Tier Scaling

### Inline Or Trivial

Keep the snapshot compact. Outcome, proposed changes, supporting changes,
verification, and the approval gate remain mandatory. Combine current-to-target
details when the change has one obvious owner; state that execution dependencies
and alternatives are `None` when that is genuinely true.

### Minimal Change Folder

Use the full template. Keep responsibility and execution detail proportional to
one cohesive implementation path. Do not invent workers, diagrams, alternatives,
or risks only to fill sections.

### Multi-Subtask Change Folder

Use the full template with explicit ownership boundaries, important proposed
names, dependency graph, parallel-safe slices, integration points, and critical
path. Prefer a small diagram when it replaces repetitive prose; do not compress
proposed changes back into a summary table.

Complexity, behavioral coupling, and architectural choices determine depth, not
raw file count. The snapshot should be scannable in one design review, while
remaining detailed enough that the human does not need to open `PLAN.md` to
understand what will be built.

## Review Length

Keep the proposal readable without weakening its change detail. Present up to
three coherent review units when one response would be overwhelming; do not ask
for separate approval of every unit. If the complete proposal would require more
than three units, ask once whether the human prefers one consolidated
human-readable review response or smaller independently planned scopes. This does
not change the existing artifact gate. After feedback, present the complete
current proposal and ask the existing single final approval question. Do not turn
each proposed-change block into another decision prompt.

## Clarifying Questions

In interactive mode, after the snapshot ask only questions whose answers materially affect user
intent, behavior, scope, ownership, an important name, an irreversible choice,
or the verification bar. Do not ask the human to resolve facts that source
discovery can answer.

For each question:

- identify the snapshot section and decision it affects,
- explain the practical impact of choosing differently,
- put the recommended concrete option first,
- provide at least one meaningful alternative,
- keep a free-form answer available.

Answering a clarification does not approve the proposal. If an answer materially
changes it, revise and re-present the snapshot before asking for approval.

In autonomous orchestrated mode, do not ask clarifying questions. Resolve only
in-scope choices, using the recommended evidence-backed option when possible, and
record the selected option, alternatives, rationale, confidence, and consequence.

## Approval And Material Changes

In interactive mode, the final gate asks whether the human approves the current snapshot's outcome,
boundaries, design, ownership, important names, edit surfaces, execution shape,
and verification bar. Offer `Proceed`, `Change direction`, and `I have
questions` (or equivalent runtime options).

Only an explicit approval of the current proposal passes the interactive gate. Silence, an
acknowledgement, an answer to one clarification, or an unrelated follow-up does
not count. In autonomous orchestrated mode, the user's explicit instruction to
ask no clarifying questions supplies delegated approval only within the stated
scope and permissions; record that instruction as the approval evidence.

A change is material when it alters any of these:

- goal, behavior, scope, or protected boundaries,
- architecture, responsibility ownership, or an important proposed name,
- expected production/configuration/schema/spec edit surfaces,
- dependency shape, integration point, migration, or critical path,
- verification expectations or completion criteria,
- a decision or assumption the human explicitly reviewed.

Mechanical packet names, formatting, or the exact location of a test that still
proves an approved verification theme are not material by themselves.

When a material change occurs, mark what changed, re-present the complete current
snapshot, and obtain renewed approval. Before writing `PLAN.md`, compare its
scope, design, edit map, execution graph, and verification strategy against the
approved snapshot. Any material delta returns to the review gate. Record the
approved direction, resolved questions, and `none` or the reapproval evidence for
material differences in `PLAN.md`.
