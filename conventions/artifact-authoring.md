---
created_at: 2026-07-07
updated_at: 2026-09-30
model: claude-opus-4.8
doc_type: convention
purpose: >-
  Self-contained write-time contract for generated markdown artifacts: allowed
  write locations, artifact categories, file naming, and frontmatter. Read this
  before writing ANY generated markdown/report/plan/audit/readout/summary/doc.
related:
  - path: ../AGENTS.md
    why: Kernel routing table gates all artifact writes to this file.
  - path: ./memory-files.md
    why: Durable-memory file rules (STATE.md/curated structure) live there.
  - path: ./legacy-compat.md
    why: Retired-workflow and legacy artifact-folder history.
---

# Artifact Authoring Convention

Read this before creating any generated markdown artifact (report, plan, audit,
review, readout, investigation, summary, handoff, doc, or similar). It is
self-sufficient: you do not need another file to write an artifact correctly.

## Where Artifacts May Be Written

- AI-generated Markdown documents (reports, plans, audits, readouts, summaries,
  drafts, proposals, and similar) must be written under an allowed artifact root
  by default: root `artifacts/` for global or cross-project work, or
  `projects/<repo>/artifacts/` for repo-specific work.
- Serious `plan-create` / `plan-execute` workflow packages are NOT artifact
  writes. They must be created under `changes/<YYMMDD_HHMM__semantic-slug>/` for
  global or cross-project work, or
  `projects/<repo>/changes/<YYMMDD_HHMM__semantic-slug>/` for repo-specific work.
- If the user asks for a generated document without naming a destination, choose
  one of the two allowed artifact roots. Do not write into arbitrary source-repo
  folders or nested Agents workspace artifact folders.
- Always write through the workspace-relative path (`agents/…`, i.e. the repo-local
  `agents/` symlink, or a `projects/<repo>/…` path); NEVER hardcode a resolved
  absolute path like `/Users/<user>/agents/…`. The `agents/` symlink usually points
  at the repo's project scope (`.../agents/projects/<repo>`), not the global
  workspace root, so a hardcoded global path silently misplaces repo-specific work
  into the global root with no error. To inspect the symlink's target use `readlink`
  / `ls -l` on it — never `git rev-parse --show-toplevel`, which returns the shared
  repository root and does not reveal where the symlink points.
- In a user-facing final response, always show an artifact's absolute filesystem
  path so the user can open it. This does not change the relative-path rule for
  links inside generated Markdown artifacts or the reviewer-facing privacy rule.
- Do not choose a destination by looking for the nearest `artifacts/` folder.
  Nested artifact roots are legacy read targets only, not write targets.
- Edit or create Markdown inside a source repo only when the user explicitly asks
  for product/source documentation there, or when modifying an existing codebase
  file in place as part of implementation work.
- Create new `artifacts/` folders only at allowed artifact roots (root
  `artifacts/` and `projects/<repo>/artifacts/`). Do not create new artifact
  folders under specs, nested projects, epics, initiatives, pillars, or other
  curated subfolders. Existing nested artifact folders may remain for historical
  links and legacy readers; do not add new generated artifacts to them.

## Artifact Categories

Standard artifact categories are fixed folder names:

- `investigations/`: research, deep system analysis, feasibility analysis,
  diagnosis, and exploratory analysis of how something works or why something
  happens. This is the default home for research that is not a polished document
  meant for presentation.
- `audits/`: audits, meta-audits, and systematic checks against criteria.
- `web-searches/`: reports from the `web-search-advanced` skill.
- `readouts/`: experiment readouts and direct experiment-analysis
  artifacts only.
- `reviews/`: PR reviews, review-comment triage, reviewer-response prep, and
  review-cycle artifacts.
- `browser-runbooks/`: living, runtime-verified browser verification/playtest
  harnesses — step-by-step "how to drive the browser to prove this feature
  works" guides (concrete selectors, testids, probe/action scripts, expected
  assertions) meant to be re-run as smoke or regression checks and to grow over
  time. These are executable verification memory, not presentation material: keep
  them out of `docs/`, and keep ordinary ops/incident procedures out of here.
  Typically `doc_type: runbook`. Prefer this over `docs/` whenever the artifact's
  primary value is demonstrating and asserting real feature behavior.
- `handoffs/`: lightweight context-transfer artifacts that let a future human or
  agent resume work without reconstructing state. Do not use handoffs as
  execution workspaces; serious execution packets belong in `changes/`.
- `summaries/`: condensed context summaries that are not task handoffs.
- `docs/`: product- or engineering-facing **presentation** material — briefs,
  proposals, explainers, roadmaps, and team-facing documents meant to be read by
  people. This is not a catch-all: system research/analysis belongs in
  `investigations/`, audits in `audits/`, PR/peer reviews in `reviews/`, and
  browser verification/playtest harnesses in `browser-runbooks/`.
- `system/`: curated Agents workspace system references, conceptual contracts,
  primers, design rationale, evolution proposals, and teaching material. These
  explain the system but do not override current specs, routing, or live memory.
- `changelog/`: frozen changelog archives and overflow "intent" records for ad hoc
  work whose intent did not fit a commit message (see `memory-files.md`). Linked
  from the relevant commit via an `Intent:`/`Change:` trailer, not a `CHANGELOG.md`.
- `misc/`: exception bucket for useful artifacts that do not fit a stronger
  standard category.
- `tasks/`: deprecated legacy task folders and historical task-oriented notes.
  Do not create new `artifacts/tasks/` content.

When initializing a new allowed `artifacts/` root, create every standard category
directory and preserve empty directories with `.gitkeep`. For existing roots, add
missing standard categories only when actively initializing or normalizing that
root; do not migrate historical files only for taxonomy cleanup. Do not invent new
artifact category folders unless the user explicitly requests them; use `misc/`
when no standard category fits.

## Bundle Index Artifacts

When one unit of work produces several tightly-coupled artifacts (for example a
diagnosis, its solution space, and its verification harness), bind them with a
single index artifact instead of leaving readers to reassemble the unit from
scattered links. An index artifact:

- uses `doc_type: index` (its filename `__index__` token), and lives in the
  category that best fits the unit (often `investigations/`);
- lists the member artifacts in its `related:` block in canonical read order,
  each with a one-line "why" and status;
- states the unit's current status (for example hypothesis-stage vs proven) so a
  fresh agent inherits the framing without re-reading every member.

Durable memory then references the ONE index rather than enumerating members:
a spec's `SOURCES.md` cites the index under its `Bundles` subsection as a single
entry (see `memory-files.md` "Spec Folder Organization"). This keeps a large
cohesive unit discoverable as one thing without bloating the linking file.

## Research Artifacts And Progress Bundles

Every `research` and `research-deep` run must finish with one disk-backed artifact
under the applicable allowed artifact root. A chat answer is never the sole
deliverable. The default final artifact is one timestamped Markdown file under
`artifacts/investigations/`, or `artifacts/summaries/` when the result is a
condensed briefing.

When the user requests a multi-file final result or progress files, represent the
whole run as one directory under the applicable `artifacts/investigations/` root,
not as scattered files or a new artifact category. Name new bundles:

```text
[yy]-[mm]-[dd]_[HH]-[MM]__research__[snake_case_title]_[model]/
```

Use a filesystem-safe model slug in the directory name: lowercase the model's
short display name and replace separators or punctuation with hyphens. Preserve
the exact provider/model identifier in frontmatter. If the directory already
exists, append `_02`, `_03`, and so on; never reuse or overwrite a prior run.
Existing `__deep_research__` bundles and `bundle_type: deep_research` metadata
remain valid historical artifacts and do not need migration.

Use only the parts of this layout the selected progress and final-output shape
need:

```text
<research-bundle>/
  RESEARCH.md
  sections/
    <optional_final_section>.md
  rounds/
    R01_<purpose>/
      workers/
        W01_<slice>/
          REPORT.md
          <optional_supporting_topic>.md
        W02_<slice>/
          REPORT.md
```

`RESEARCH.md` is always the root-owned final synthesis and canonical bundle
entrypoint. In recoverable progress mode it is also the checkpoint, round ledger,
and resume entrypoint. In worker-reports mode workers may populate their assigned
directories while the root waits until completion to create `RESEARCH.md`. A
transient run creates no progress files; when its final result needs several
files, the root creates the complete bundle only at the end. `sections/` is only
for a user-requested multi-file final result, and every member must be linked from
`RESEARCH.md` in canonical read order.

Each reporting worker owns one exclusive directory and must create `REPORT.md`.
Supporting Markdown is optional and only for materially distinct evidence. This
nesting keeps one run as one artifact even when it has many final sections,
rounds, or workers.

Every Markdown file in the bundle uses the generated-artifact frontmatter below
with `artifact_category: investigations`. New `RESEARCH.md` files add
`bundle_type: research`, `research_depth: standard | deep`, and
`progress_mode: transient | worker_reports | recoverable`; worker files add
`round` and `worker_id`. Bundle files may use stable operational names because
their timestamp, type, title, and model are carried by the containing directory.

Research artifacts are generated evidence, not canonical product truth. Commit
the final artifact once when the run completes or ends blocked. Progress files
may stay uncommitted during the run; do not create a commit after every round.

## File Naming Convention

Use this filename convention for generated markdown reports, plans, audits,
handoffs, or other AI artifacts in `~/agents`:

```text
[yy]-[mm]-[dd]_[HH]-[MM]__[doc_type]__[snake_case_title]_[model].md
```

Use a concrete `doc_type` such as: `investigation`, `feasibility`, `audit`,
`meta_audit`, `review`, `task`, `task_note`, `handoff`, `summary`, `doc`,
`readout`, `runbook`, `index`, etc.

Do not use vague or overloaded labels when a more specific doc type exists. Use
`readout` only for experiment readouts or direct experiment-analysis
artifacts; use `investigation`, `summary`, `doc`, or `task_note` for
non-experiment briefings.

## File Frontmatter Convention

Every new generated markdown artifact or change-folder file should start with
concise YAML frontmatter. Legacy artifacts may be brought into compliance
opportunistically when actively edited or promoted.

Minimum fields for generated artifacts and change-folder files:

- `created_at`
- `model`
- `artifact_category`
- `doc_type`
- `purpose`
- `related`

For files under `artifacts/`, `artifact_category` must match the containing
standard artifact category (`investigations`, `audits`, `readouts`, `reviews`,
`browser-runbooks`, `handoffs`, `summaries`, `web-searches`, `docs`, `system`, `changelog`, or
`misc`). Deprecated
legacy task records may keep `artifact_category: tasks` until migrated. For files
under `changes/`, use `artifact_category: changes`. `doc_type` should match the
filename `__doc_type__` token and may be more specific than the folder category.

Each `related` item must include:

- `path`
- `why`

Use relative paths for Agents workspace-internal links whenever practical. Use
repo-root paths only for source files outside the Agents workspace.
