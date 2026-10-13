---
created_at: 2026-06-29
updated_at: 2026-08-25
model: gpt-5.5
doc_type: workflow
purpose: Define the change-folder contract for new Agents workspace spec-workflow execution packets.
related:
  - path: ../AGENTS.md
    why: Entry point and invariants for the spec workflow.
  - path: ../../../skills/plan-create/SKILL.md
    why: Creates change folders from this contract.
  - path: ../../../skills/plan-execute/SKILL.md
    why: Executes change folders from this contract.
---

# Change Folder Contract

A change folder is the canonical restartable execution packet for new serious
Agents workspace spec-workflow work. It should contain enough intent, plan, worker
packets, execution state, verification, and reconciliation context for fresh phase
agents to continue without relying on chat history.

## Allowed Locations

Use only these roots:

```text
changes/<YYMMDD_HHMM__semantic-slug>/
projects/<repo>/changes/<YYMMDD_HHMM__semantic-slug>/
```

Do not create change folders under nested projects, epics, initiatives, pillars,
specs, or artifacts.

Use `changes/<YYMMDD_HHMM__semantic-slug>/` for global, cross-project, or
workspace behavior changes. Use
`projects/<repo>/changes/<YYMMDD_HHMM__semantic-slug>/` for repo-specific work.
When working through a repo-local `agents/` symlink, the same repo-specific path
is visible as `agents/changes/<YYMMDD_HHMM__semantic-slug>/`.

## Standard Layout

```text
changes/<YYMMDD_HHMM__semantic-slug>/
  AGENTS.md
  PLAN.md
  EXECUTION_LOG.md
  RESULT.md
  MEMORY_DELTA.md
  RECONCILE_PACKET.md
  specs/
    <domain>/
      spec.md
  subtasks/
    T01_<verb>_<object>.md
  followups/
    F01_<reason>_<object>.md
  results/
    T01.result.md
    F01.result.md
```

Required for serious change folders:

- `AGENTS.md`
- `PLAN.md`
- `EXECUTION_LOG.md`
- `RESULT.md`

Optional unless needed:

- `MEMORY_DELTA.md`
- `RECONCILE_PACKET.md`
- `specs/`
- `subtasks/`
- `followups/`
- `results/`

## File Roles

- `AGENTS.md`: local operating rules for this change folder.
- `PLAN.md`: approved execution contract, including structured frontmatter for
  scope, path boundaries, required reads, verification, worker strategy,
  permission posture, plan-reconcile expectations, plus prose rationale, graph,
  and details.
- `EXECUTION_LOG.md`: root-owned meaningful decisions, failures, followups,
  verification outcomes, and plan changes. Not a transcript.
- `RESULT.md`: final or current outcome summary. This is the canonical per-change
  record for lightweight git/PR provenance such as source repo, branch, compare
  base, head commit, and PR URL/status, plus a compact context receipt for
  material reads, stale/confusing context, and prune/update candidates.
- `MEMORY_DELTA.md`: proposed and applied durable-memory impacts across state,
  specs, decisions, sources, codemaps, and artifact staleness.
- `RECONCILE_PACKET.md`: execution-to-reconcile handoff. Legacy
  `CLOSEOUT_PACKET.md` remains readable for older change folders. It may
  summarize or point to `RESULT.md` provenance, but `RESULT.md` is the
  authoritative per-change provenance record.
- `specs/`: OpenSpec-style proposed spec deltas that mirror the owning current
  `specs/` tree.
- `subtasks/`: initial worker packets.
- `followups/`: root-created worker packets discovered during execution.
- `results/`: worker reports.

## Source Checkout Contract

Project guidance may define named source-checkout selectors and one project
default. It may also opt into managed-session selection for new plans and ad hoc
work. A selector resolves to a checkout path and the repository identity that the
path is expected to contain.

Capture the initial session workspace once before tools change directories. For
an opted-in project, that path selects a checkout only when it is at or below
exactly one managed checkout root and the resolved root validates as the expected
Git top level and repository identity. Later process CWD changes never reselect a
checkout. Selection precedence before a plan exists is an explicit invocation
selector, then a validated managed-session selector, then the project default.

`source_checkout` is optional in `PLAN.md`. Persist any effective non-default
selector used to create a plan, including a managed-session-derived selector.
Omission means the owning project's default or existing compatibility behavior,
so existing plans without the field remain valid. Once a plan exists, its
selector or intentional omission governs later phases. A conflicting invocation
selector requires confirmation before the approved plan changes.

Before any source operation, the phase agent must resolve and validate the
effective selector, including that the path exists, its Git top level is the
intended checkout, and its repository identity matches the project guidance or
plan. Every source, test, Git, or checkout-bound runtime/browser worker packet
receives the effective selector, resolved absolute working directory, and
expected repository identity; workers must use that directory rather than infer
one from their CWD.

Ordinary plans use one effective checkout and omit multi-checkout allocation
ceremony. Additional checkout allocations are allowed only when the plan's
human-approved execution strategy explicitly selects parallel or multithreaded
work. The root phase records and validates each packet allocation; workers never
choose, reserve, or coordinate lanes. Simultaneous mutating workstreams must use
different checkouts.

Allocate a runtime only when execution or browser verification needs one. An
ordinary single-checkout plan may own at most one active runtime. Multiple
simultaneous runtimes require the same approved parallel strategy as multiple
checkout allocations. A runtime target records its checkout, resolved working
directory, instance or identifier, exact URL, process owner, reuse permission,
and stop or handoff responsibility. Packets without runtime needs mark `Runtime
Target: n/a`; selecting a checkout never starts a process.

## Browser Verification Packets

Follow `browser-verification`. Phase agents delegate probes to bounded
`task-execute` workers on an affordable tier and never call browser MCP tools
directly. Browser worker reports must include: pass/fail, probe diffs,
`driver_status`, `tool_capability_level` (A-E), `session_isolation`
(fresh | shared | unknown), `pages_closed`, and `pages_remaining`.

`plan-reconcile` uses the selector recorded by `PLAN.md` and `RESULT.md` for
source confirmation and never uses its launch CWD as a selector. Product/spec
memory remains checkout-neutral: the stable selector catalog and opt-in policy
belong in project guidance, while selected paths, packet allocations, and runtime
ownership stay in the change packet/provenance.

## Spec Deltas

Use `changes/<YYMMDD_HHMM__semantic-slug>/specs/<domain>/spec.md` only when the
change proposes to add, modify, or remove durable behavior, requirements,
contracts, or protocols. This file is a proposed delta, not current truth.

A spec delta is critical content: the phase agent writes its exact final text
during `plan-create` and does not delegate that authoring to a worker or leave it
as a stub, outline, or "fill in later" note. `plan-reconcile` should be able to
apply the delta to the owning current spec as a near-mechanical copy, so the
delta file must already contain the wording the spec will end up with.

Accepted deltas are applied during `plan-reconcile` to the owning current spec:

```text
specs/<domain>/spec.md
projects/<repo>/specs/<domain>/spec.md
```

Do not create delta specs for one-off notes, transient execution details, or
historical outputs.

## Minimal Change Mode

Minimal change mode may omit `specs/`, `subtasks/`, `followups/`, and `results/`.
The phase agent still writes `PLAN.md`, `EXECUTION_LOG.md`, and `RESULT.md`, and
may use one bounded worker if useful.

## Naming

Use a timestamp-prefixed semantic change slug:

```text
260629_1314__en-immersive
260629_1404__q3-mt-performance
260629_1546__spec-first-taxonomy-q3-mt-migration
```

The timestamp is local creation time in `YYMMDD_HHMM` format. The semantic slug
describes the product or workspace change, not the workflow artifact. Do not
include document-type labels such as `task`, `plan`, `handoff`, `spec`, or
`investigation`, and do not include model names.

Use stable worker IDs and concise names:

```text
T01_investigate_current_behavior.md
T02_update_server_logic.md
T03_add_unit_tests.md
F01_fix_t02_type_error.md
```

Do not encode parallelism in filenames. Put dependency and parallel-safety rules
in `PLAN.md` and packet files.

## Legacy Compatibility

Older execution packets under `artifacts/tasks/` remain valid legacy records.
Treat nested historical legacy records as read targets only. New serious
spec-workflow work must use a change folder, and project-root task packets should
be migrated to timestamped change folders when practical.
