---
created_at: 2026-07-06
model: gpt-5.5
doc_type: workflow
purpose: Define the portable model bake-off workflow for cross-tool model benchmarking.
related:
  - path: ../../skills/model-bakeoff/SKILL.md
    why: User-facing skill entrypoint for this workflow.
  - path: ../../roles/model-bakeoff-contestant.md
    why: Isolated contestant role used by adapter-specific worker wrappers.
  - path: ../../adapters/adapter-contract.md
    why: Keeps native model config and model availability in tool adapters.
  - path: ../spec-workflow/AGENTS.md
    why: Serious coding benchmark setup may compose with change folders and bounded workers.
---

# Model Bakeoff Workflow

Run evidence-backed comparisons between requested model contestants on the same
task. The workflow is portable; native model selection, temporary subagent files,
permissions, and restart requirements belong to the active tool adapter.

## Core Rule

The Agents workspace owns the benchmark contract and report formats. Tool
adapters own model resolution and native runtime wiring. Never make a global
canonical list of model names or availability.

## Stages

1. Prepare the benchmark packet.
2. Resolve contestants through the current tool adapter.
3. Configure temporary native contestants only when the adapter supports it and
   the user approved that scope.
4. Execute isolated contestants in parallel when safe.
5. Evaluate results with evidence and rubric scores.
6. Clean up temporary native config and workspaces according to the cleanup
   preference.

## Required Inputs

- `task_type`: `research`, `coding`, `review`, or `mixed`.
- `task`: the exact benchmark prompt to give every contestant.
- `requested_competitors`: requested model names, model aliases, or labels.
- `isolation`: `reports`, `git_worktrees`, or an adapter-supported equivalent.
- `rubric`: `default` or explicit criteria.
- `cleanup`: `auto`, `ask`, `keep_finalist`, or `keep_all`.
- `scope`: global, project, repository, or cross-repo benchmark context.
- `verification`: commands or manual checks that should be applied uniformly.

If any required input is missing, ask one concise clarification before preparing
native config. For low-risk research bake-offs, reasonable defaults are allowed
when the user clearly wants the workflow to proceed.

## Output Location

Write benchmark run artifacts under an allowed Agents workspace artifact root:

```text
artifacts/audits/<yy>-<mm>-<dd>_<HH>-<MM>__audit__model_bakeoff_<slug>_<model-or-root>.md
```

For serious coding bake-offs that need restartable execution or durable planning,
compose with `../spec-workflow/` and create a normal change folder. The bake-off
packet can live in that change folder's `results/` area when the plan explicitly
says so. Files under a change folder use `artifact_category: changes`.

## Benchmark Packet

Use `templates/BAKEOFF.md` for the run contract. It must capture:

- exact benchmark prompt
- requested and resolved competitors
- adapter limitations
- isolation mode
- worktree or report paths
- rubric and scoring weights
- timing method
- verification requirements
- cleanup policy

## Contestant Isolation

Every contestant receives the same task prompt, constraints, allowed tools,
allowed paths, verification expectations, and output schema.

Contestants must not read peer outputs, worktrees, result files, evaluation
notes, or private orchestrator notes. The orchestrator may read every result only
after contestant execution ends or is declared blocked.

Research, review, and source-inspection tasks normally use `reports` isolation.
Coding or mutation tasks should use `git_worktrees` unless the user explicitly
chooses another safe isolation mode.

## Coding Worktrees

For coding bake-offs, the orchestrator owns worktree creation and cleanup.
Contestant workers must not create branches, create worktrees, commit, push, or
open PRs.

Use one worktree per resolved contestant from the same base commit. Record:

- source repository
- base branch and base commit
- worktree path
- contestant branch name, if created
- changed files
- verification commands and results
- final diff summary

## Timing

The orchestrator records wall-clock start and end timestamps for each contestant.
Contestants may also report their own start and end times, but self-reported time
is fallback evidence only.

Record timeout, blocked, and user-interrupted states explicitly. Do not score a
missing duration as zero seconds.

## Evaluation

Use `templates/EVALUATION.md`. Score each category from 0 to 100 with short
evidence. Default categories:

- correctness
- completeness
- instruction following
- speed
- tool-use efficiency
- verification quality
- reasoning quality
- risk handling
- final usability

For coding tasks, also score:

- code quality
- test quality
- diff minimality
- maintainability
- integration risk

For research tasks, also score:

- source quality
- citation quality
- synthesis quality
- uncertainty handling

Report winners by category and by practical use case. Avoid declaring one
universal winner when the evidence supports task-specific tradeoffs.

## Cleanup

Use `templates/CLEANUP.md`.

- `auto`: remove temporary native contestant config and temporary worktrees after
  preserving the final evaluation artifact.
- `ask`: stop before deleting temporary config, branches, or worktrees.
- `keep_finalist`: keep the winning coding worktree or report set and remove the
  rest after confirmation when deletion is destructive.
- `keep_all`: preserve all temporary outputs and report their paths.

Native adapter config cleanup must follow the active adapter mapping. If the
adapter requires a restart or new session for cleanup to take effect, say so.

## Stop Conditions

Stop and ask the user when:

- requested models cannot be resolved and no fallback policy was provided
- native config edits are required but not authorized
- a coding benchmark would modify the current checkout without worktree isolation
- contestants cannot be isolated from peer outputs
- verification would be materially different across contestants
- cleanup would delete user-created or unrelated files

## Related Templates

- `templates/BAKEOFF.md`: benchmark contract.
- `templates/CONTESTANT_PACKET.md`: exact contestant prompt and result schema.
- `templates/CONTESTANT_RESULT.md`: per-contestant output.
- `templates/EVALUATION.md`: final comparison report.
- `templates/CLEANUP.md`: cleanup checklist.
