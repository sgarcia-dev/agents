---
name: model-bakeoff
description: Prepare, execute, evaluate, and clean up cross-tool model bake-offs for research, coding, review, or mixed benchmark tasks using adapter-resolved model contestants.
created_at: 2026-07-06
model: gpt-5.5
doc_type: skill
purpose: Provide the portable user-facing entrypoint for model comparison benchmark runs.
related:
  - path: ../../workflows/model-bakeoff/AGENTS.md
    why: Canonical workflow for preparing, running, evaluating, and cleaning up model bake-offs.
  - path: ../../roles/model-bakeoff-contestant.md
    why: Portable role contract for isolated contestant workers.
  - path: ../../adapters/adapter-contract.md
    why: Platform-neutral adapter contract that keeps model resolution native to each tool.
---

# Model Bakeoff

Use this skill to compare multiple models on the same bounded task while keeping
the benchmark portable across AI tools and IDEs.

## When To Use

- The user asks to compare, benchmark, bake off, or test-drive models.
- The user wants to evaluate model speed, quality, tool use, research quality, or
  coding output on one task.
- The user wants one tool adapter to create temporary model-specific contestants
  without making native model names canonical in the Agents workspace.

## Workflow

Follow `../../workflows/model-bakeoff/AGENTS.md`.

Default to a prepare-first workflow. Do not create temporary native model agents,
custom agents, subagents, worktrees, or branches until the benchmark inputs and
cleanup preference are explicit.

Required inputs:

- requested competitors or model labels
- benchmark task
- task type: `research`, `coding`, `review`, or `mixed`
- isolation mode: `reports`, `git_worktrees`, or adapter-supported equivalent
- rubric: `default` or explicit custom criteria
- cleanup preference: `auto`, `ask`, `keep_finalist`, or `keep_all`

## Adapter Boundary

The Agents workspace defines the benchmark contract. The current tool adapter
resolves requested competitors into native model names and temporary native
config, if supported.

Do not add a canonical global model list. Do not assume every runtime can launch
the same model names. If a requested model is unavailable, report the unresolved
competitor instead of substituting silently.

## Final Output

Return the benchmark packet path, resolved competitors, execution status,
evaluation report path, cleanup status, and any unresolved adapter limitations.
