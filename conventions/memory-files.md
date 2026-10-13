---
created_at: 2026-07-07
model: claude-opus-4.8
doc_type: convention
purpose: >-
  Self-contained write-time contract for durable Agents workspace memory: when
  and how to write STATE.md, curated-folder structure, optional canonical memory
  files, and artifacts/changelog/ records (history is the git commit log, not a
  hand-maintained changelog). Read this before creating or updating any durable
  memory.
related:
  - path: ../AGENTS.md
    why: Kernel routing table gates all durable-memory writes to this file.
  - path: ./artifact-authoring.md
    why: Generated-artifact write locations, naming, and frontmatter live there.
---

# Memory Files Convention

Read this before creating or updating durable Agents workspace memory:
`STATE.md`, `DECISIONS.md`, `SPEC.md`, `SOURCES.md`,
`ARCHITECTURE.md`, `CODEMAP.md`, `PRS.md`, spec-folder organization,
curated-folder structure, or `artifacts/changelog/` records. It is
self-sufficient.

## Update Triggers

For any work that creates, edits, moves, or deletes files under `~/agents` or a
repo-local `agents/` symlink:

- Before finishing, update the owning `STATE.md` when current truth, status,
  decisions, active work, blockers, or next steps changed.
- History is the git commit log, not a hand-maintained changelog. Capture change
  intent via the kernel `AGENTS.md` "Git Completion Gate" ritual (commit message
  by default; a `changes/`/`specs/` trailer or a rare `artifacts/changelog/`
  overflow record only when one already exists or the intent won't fit a message).
- These rules apply equally to top-level workspace files, scoped `STATE.md`,
  generated artifacts, and repo-local `agents/` symlinks.
- If the change is too small to justify updating or creating `STATE.md`, mention
  that briefly in the final response.

## Curated Folder Structure

Any curated folder in `~/agents/projects/<project_name>` or a nested non-`artifacts`
folder should use these exact filenames when it has enough durable memory to
justify them. Prefer shallow curated roots over recursive nesting:

- `AGENTS.md`: folder-specific operating guidance for agents.
- `STATE.md`: what is true now. (History is the git commit log; no per-folder
  `CHANGELOG.md`.)
- `artifacts/`: allowed only at root `artifacts/` and `projects/<repo>/artifacts/`.
  Other curated folders may link to legacy nested artifacts but must not create or
  receive new generated artifacts.

Optional canonical durable-memory files, created only when they solve a real
maintenance problem:

- `SPEC.md`: requirements, goals, non-goals, and acceptance criteria that would
  bloat `STATE.md`.
- `DECISIONS.md`: durable choices, rejected alternatives, tradeoffs, consequences.
- `SOURCES.md`: trusted evidence, weak or stale evidence, and freshness notes.
- `ARCHITECTURE.md`: reusable system or solution design explanation.
- `CODEMAP.md`: source landmarks, ownership boundaries, and code-path maps.
- `PRS.md`: detailed PR/review state when multiple PRs would clutter `STATE.md`.

Do not create these files as empty ceremony unless the user requests it. Prefer
`AGENTS.md` over `README.md` when the folder mainly exists to instruct an agent
how to work in or under it.

Operational coordination files are a distinct, non-durable category. A lane claim
ledger (e.g. `projects/<repo>/LANES.md`) records who is using which managed
checkout right now, not product or workflow truth. It is committed for visibility
but is exempt from durable-memory update triage: reconciliation does not treat it
as truth to reconcile, and it must not absorb product/spec state. The owning
project guidance defines its format and claim/release rules.

For successful serious work governed by `workflows/spec-workflow/`,
`plan-reconcile` should create or update `DECISIONS.md`, `SOURCES.md`, and
`CODEMAP.md` in the declared owning scope unless it can clearly justify that no
durable decision, source-trust, or code-landmark truth changed. See
`specs/project-memory/spec.md` for the project-memory contract.

## Spec Folder Organization

A `specs/<domain>/` folder is a durable behavior spec, not a link dump. It grows
on demand from `spec.md` alone to the `spec.md` + `SOURCES.md` + `CODEMAP.md` +
`DECISIONS.md` set (see `specs/project-memory/spec.md` "Growth Model"). This
section defines how a spec surfaces its links and what is authoritative where, so
a spec stays a reliable jumping-off point instead of improvising per author.

### Authority Model (what is truth where)

Each surface owns one job. Do not duplicate a truth across surfaces; link to the
owner instead.

- `spec.md`: authoritative for behavior/product truth AND the folder's navigation
  entrypoint. It links out to evidence; it does not inline the source ledger.
- `SOURCES.md`: authoritative evidence ledger. It owns the long tail of links -
  code sources, repo guidance, external/canonical docs, PRs, tickets, and bundle
  indexes - grouped into standard labeled subsections (below).
- `CODEMAP.md`: authoritative for code landmarks, ownership boundaries, and
  code-path maps.
- `DECISIONS.md`: authoritative for durable choices, rejected alternatives, and
  consequences.
- `related:` frontmatter: the adjacency layer only. List sibling files and the
  few directly neighboring specs, kept flat and stable so `plan-reconcile` can
  maintain it mechanically. Do NOT encode priority or grouping in `related:`;
  curation lives in the `spec.md` "Start Here" block.

PRs and tickets are evidence: record them in a `SOURCES.md` subsection, not a new
file. Reserve `PRS.md` for the rare spec where many PRs would genuinely clutter
`SOURCES.md`.

### Start Here Block

Near the top of `spec.md` (after the H1 and a one-paragraph summary), include a
short curated `## Start Here` router: roughly three to six links that a fresh
agent should open first. Omit any line that does not apply to the spec - a spec
with no runbook simply drops the Verify line. Keep it a router, not content: each
line is a pointer with a few words of "why".

Typical lines, in priority order:

- Status: one-line pointer to current truth (this spec's status section or
  `STATE.md`).
- Product brief: the product-facing brief (`artifacts/docs/...` or an external
  PRD/canonical doc).
- Engineering: `./CODEMAP.md`, plus an engineering companion doc if one exists.
- Decisions: `./DECISIONS.md` when present.
- Verify: the browser-runbook or bundle index that proves the feature works.
  OMIT when the spec has no verification harness.
- Sources: `./SOURCES.md`.

The Start Here block is authoritative as a router; its targets remain
authoritative for their content. Not every spec needs a runbook or a product
brief, so treat the block as curated-and-pruned, never as a mandatory checklist.

### SOURCES.md Subsections

`SOURCES.md` groups evidence under a small standard set of subsection labels. Use
only the ones a spec needs; do not create empty subsections:

- `Trusted Current Code`: current source files that decide behavior.
- `Repo Guidance`: in-repo docs/guidelines trusted as current.
- `Related Specs`: neighboring durable specs and their trust/caveats.
- `External / Canonical Docs`: Google Drive, Confluence, PRDs, and other external
  canonical documentation (their own group, not interleaved with code).
- `PRs & Launch State`: PRs, launch/rollout state, and tickets as evidence.
- `Verification / Runbooks`: `browser-runbooks/` harnesses and other living
  verification guides that prove the feature works.
- `Bundles`: bundle indexes (see below), one entry per unit.
- `Generated Reference / Companion Docs`: accepted generated artifacts.
- `Historical / Stale`: superseded or weak evidence kept only for context.
- `Weak Claims To Avoid`: claims the evidence does NOT support.
- Optional: `Source Hierarchy` / `Owner Map` for conflict resolution and routing.

### Bundle Index Pattern

When one unit of work produces many tightly-coupled artifacts (a diagnosis plus
its solution space plus its verification harness, say), do not enumerate every
member file in the spec. Instead bind the unit with ONE index artifact
(`doc_type: index`, see `artifact-authoring.md`) whose ordered `related:` list is
the canonical read order, and reference that single index from the `SOURCES.md`
`Bundles` subsection. The spec points at the index; the index points at the
members. This keeps a large cohesive unit discoverable as one thing without
bloating the spec's link surface.

## STATE.md

`STATE.md` should be short and current. It is the first file agents read when a
folder has active durable memory.

Root `STATE.md` should stay shallow: list active durable areas, global
constraints, stale or blocked areas, and links to scoped state files. Scoped
`STATE.md` files own current truth, decisions, active work, blockers, and next
steps for their folder. Do not repeat scoped details in root state.

Size budget: keep `STATE.md` a shallow snapshot - target under ~120 lines; if it
passes ~200, restructure (push detail into scoped `STATE.md`/`specs/`, not a longer
router). The `related:` block lists only the few top entrypoints an agent needs
next (nearest `AGENTS.md`, active scoped `STATE.md` files, the relevant `specs/`
entrypoint) - NOT an exhaustive manifest of every child. Discover completed
`changes/` folders and one-off artifacts by listing the directory or via `git log`,
never by enumerating them in `STATE.md`.

Required frontmatter fields for new or actively updated `STATE.md` files:

- `doc_type: state`
- `updated_at`
- `status`
- `scope`
- `related`

Each `related` item must include:

- `path`: a relative path from the current file
- `why`: one sentence explaining when to read it

## History and Intent (no hand-maintained CHANGELOG.md)

There is no hand-maintained `CHANGELOG.md`; it duplicated `git log` at unbounded
cost. The workspace is a git repo: `git log` is the history (what + when), and the
commit message body carries intent (why). Capture intent with the kernel
`AGENTS.md` "Git Completion Gate" ritual, ordered cheapest-first:

1. Intent already in a `changes/<slug>/` packet or a `specs/` file this task
   touched -> add a commit trailer pointing at it (`Change: changes/<slug>/`). No
   new file.
2. Otherwise (the common ad hoc case) -> state the why / key decisions / rejected
   alternatives in the commit message body. No file.
3. Only when that intent overflows a commit message (long rationale, multi-folder
   resume context, diagrams) -> write ONE overflow record under
   `artifacts/changelog/` and add a commit trailer (`Intent: <path>`).

Optimize for step 2: it creates no file. Do not create an overflow record for
routine or trivial work.

Overflow intent record (step 3 only): flat file under root `artifacts/changelog/`
(or `projects/<repo>/artifacts/changelog/` for repo-specific work), named per the
artifact naming convention with a `doc_type` such as `note`. Body stays short: what
changed, why, alternatives, links. Frontmatter uses the generated-artifact minimum
from `artifact-authoring.md` with `artifact_category: changelog`.

## artifacts/changelog/

`changelog-records/` is deprecated. The standard expanded-record location is root
`artifacts/changelog/`.

By default, use root `artifacts/changelog/` only for frozen changelog archives and
overflow intent records linked from a commit `Intent:`/`Change:` trailer (see the
"History and Intent" section above). Local recursive `artifacts/changelog/`
folders are legacy-compatible read targets only; do not create new ones or add
new generated records to them.

Create an expanded changelog record only when at least one is true:

- workflow/process/preferences changed and future agents need the reasoning
- there were mistakes and corrections that future agents should not repeat
- the resume context spans multiple folders or projects
- the detailed intent would overflow a commit message body
