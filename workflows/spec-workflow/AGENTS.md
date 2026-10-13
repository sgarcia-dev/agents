# Spec Workflow

OpenSpec-inspired durable workflow for serious agent-assisted work. Use this
workflow when the task needs restartable planning, scoped changes, delegated
workers, explicit verification, or durable memory reconciliation.

Do not use this workflow for simple edits, obvious one-file fixes, typos, or
small formatting changes unless the user asks for durable planning.

## Read Order

- `../../skills/plan-create/SKILL.md` for creating a reviewed plan before
  execution.
- `../../skills/plan-execute/SKILL.md` for executing an approved plan.
- `../../skills/plan-reconcile/SKILL.md` for updating durable memory after
  execution.
- `references/change-folder-contract.md` when creating or consuming change
  folders.
- `references/discovery-cadence.md` when planning discovery for a change
  (plan-create).
- `references/task-folder-contract.md` only when consuming legacy task folders.
- `../../roles/task-worker-tiers.md` before any delegation. It is the sole
  authority for enabled roles, packet size, and worker-count limits.
- Load the corresponding base role and high overlay only after the tier guidance
  authorizes the selected wrapper.
- `templates/` for copyable file skeletons.

## Core Model

Serious work runs as fresh top-level phases connected by durable files:

```text
plan-create -> plan-execute -> plan-reconcile
```

No phase may rely on prior chat context for correctness. Each phase starts from
declared input files and writes durable outputs for the next phase. New serious
work uses one `changes/<YYMMDD_HHMM__semantic-slug>/` folder as the reviewable
execution packet.

## Scope Selection

Create specs and change folders only in allowed root or repository-project
scopes.

- Root `specs/` and `changes/` are for global Agents workspace behavior,
  conventions, or cross-project changes.
- Project-specific work uses `projects/<project>/specs/` and
  `projects/<project>/changes/`.
- New serious work uses `changes/<YYMMDD_HHMM__semantic-slug>/` or
  `projects/<project>/changes/<YYMMDD_HHMM__semantic-slug>/` as the execution
  packet.
- Nested initiative, epic, pillar, spec, and artifact folders may have legacy
  links, but they are not valid destinations for new change folders.

When scope is unclear, stop and record the ambiguity in `PLAN.md` instead of
inferring a nested change or artifact destination.

## Phase And Worker Boundary

Assume top-level phase agents use stronger reasoning models. Micro workers handle
only tiny packets; high workers handle bounded moderately complex tasks. Their
reports and diffs can contain mistakes, misses, hallucinations, or overlooked coupling.

- Phase agents reason, decide, integrate, verify, and accept or reject work.
- Workers execute bounded packets with minimal judgment.
- Worker packets declare `worker_model_tier: default | high | phase_owned` and a
  judgment boundary before dispatch. Fast variants remain disabled; a normal
  orchestrator needs a verified active-tool mapping.
- `phase_owned` packets are not delegated; the top-level phase agent owns that
  reasoning and integration work.
- Workers must not spawn, call, or coordinate other workers.
- Workers must not decide durable truth.
- A `task-explore` worker may create new Markdown reports in one exclusive
  packet-assigned output directory. It remains forbidden from changing existing
  files, source, product state, plans, specs, or durable memory.
- If a worker needs broad reasoning, hidden chat context, or another worker, the
  packet is wrong and must be split, handled in the phase agent, or blocked.
- Critical content authorship stays phase-owned. When the exact wording is the
  deliverable (a new spec, a spec delta, durable memory, guidance, or another
  critical or irreversible artifact), the phase agent writes the final text
  itself and persists it verbatim in the change folder. Workers may mechanically
  apply already-authored text but must never originate or paraphrase it. See
  `../../skills/plan-create/SKILL.md` "Critical Content Is Phase-Owned And
  Written Verbatim".

## Worker Model Tiers

Follow `../../roles/task-worker-tiers.md` without exception. Prefer the cheap default
micro roles for truly tiny independent packets; use high roles for real bounded
delegated tasks with several steps or coupled reasoning. Never spawn
a native/generic subagent or a worker that inherits the phase agent's model.
Strictly inspect worker reports, relevant diffs, and verification evidence before
accepting output. If confidence is unclear or the work does not fit either bounded
tier, split independent work, handle it in the phase agent, or stop blocked.

## Worker Connector Availability

When the root/phase session makes an approved knowledge integration available at
tool, session, or project scope, a `task-explore` worker may use it for its
assigned bounded question. This does not create a role-specific grant or adapter
customization. If an integration is unavailable, workers should continue with the
remaining sources and report the missing surface rather than failing the packet.
Internal-search answers remain hints until verified against authoritative docs,
source code, or user-provided context.

## Attempt Budget

Workers get at most three serious attempts on a packet unless the phase agent or
user sets a stricter limit. After repeated failure, unclear verification,
missing context, or scope conflict, the worker stops and reports blocked.

Interactive phase agents must stop for user input when repeated worker failure,
conflicting sources, unclear product behavior, forbidden edit scope, or
inconclusive verification prevents confident progress. An explicitly autonomous
orchestrator instead chooses a safe in-scope fallback or records the item blocked
or deferred; it does not invent authority or ask a question.

## Privacy Boundary

Private Agents workspace paths, change folder names, subtask IDs, worker IDs, agent
plans, tool names, and internal workflow mechanics must not appear in commits,
PRs, Jira tickets, Slack messages, review replies, code comments, or other
reviewer-facing output.

## Legacy Compatibility

Existing `artifacts/tasks/` and lightweight handoff artifacts remain valid as
legacy compatibility inputs. The old `task-folder-workflow`,
`sharded-agent-handoffs`, workflow-local `skills/`, and workflow-local
`subagents/` trees are retired; do not recreate them. Use root `skills/` and
`roles/` plus this `spec-workflow` package and its change-folder contract for all
new serious durable work. Migrate deprecated project-root task packets to
timestamped `changes/` folders when practical; do not migrate nested historical
artifacts only for naming consistency.
