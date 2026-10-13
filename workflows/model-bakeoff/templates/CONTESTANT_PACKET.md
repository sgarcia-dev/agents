# Contestant Packet: <Label>

## Role

You are one isolated model-bakeoff contestant. Complete the benchmark task using
only the provided context and allowed tools. Do not inspect peer contestant
outputs, worktrees, reports, evaluation notes, or orchestrator-private notes.

## Competitor

- Label:
- Requested model:
- Resolved native model:
- Native wrapper:

## Benchmark Task

```text
<Exact benchmark prompt>
```

## Constraints

- Task type: research | coding | review | mixed
- Allowed paths:
- Forbidden paths:
- Allowed tools:
- Forbidden tools:
- Mutation allowed: yes | no
- Worktree path, if applicable:

## Verification

- Required checks:
- Optional checks:
- Evidence to preserve:

## Timing

- Orchestrator start time:
- Contestant may report internal start/end times as fallback evidence.

## Stop Conditions

Stop and report blocked if:

- required context is missing
- forbidden files or peer outputs are needed
- verification cannot be run uniformly
- the task requires broad scope beyond this packet
- native tool/model configuration is wrong or unavailable

## Result Shape

Write or return a result using `CONTESTANT_RESULT.md`.
