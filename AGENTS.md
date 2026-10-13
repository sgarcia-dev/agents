# Agents Workspace

Canonical instruction file for the durable, coworker-visible Agents workspace at
`~/agents`. Sensitive material belongs in a separate private repo, never in this
repository. This file
is a lean always-on kernel: it must be self-sufficient for a quick task and
route you to on-demand detail for everything else.

You may be reading this as `~/agents/AGENTS.md` or through the `~/.agents/AGENTS.md`
adapter symlink (same inode). If you are reading it, canonical guidance is loaded;
symlink/adapter maintenance rules live in `adapters/AGENTS.md`.

## Purpose

Programming is theory building, not text production (1985): the real system
is a *theory*, the map between intent and code, the rationale, the paths not
taken, that lives in a mind and dies when that mind leaves. Every AI agent
session arrives as a newcomer with zero theory, and the repository text alone
under-determines it. Meanwhile the tools hosting those sessions churn faster than
the work itself.

This workspace exists to defeat both losses at once, as one thesis. It is the
durable, plain-text, human-owned source of truth for shared work:

1. **The theory of the work**, decisions, rationale, state, and the intent↔code
   map, so it outlives every session boundary and long tasks resume instead of
   being rebuilt from scratch.
2. **The tool-agnostic operating contract**, instructions, skills, roles,
   capabilities, procedures, so accumulated knowledge is never hostage to a
   single vendor's lifecycle.

Governing corollary: **tools converge to this system; the system never bends to a
tool.** Each runtime is a thin, replaceable adapter over this source of truth, and
every divergence between a tool and this workspace is surfaced and reconciled ,
never silently absorbed. Full grounding: `specs/agents-workspace/mission.md`.

A separate private repo uses the same operating model for sensitive and
credential-bearing memory. This repository must not depend on its internal paths
or content.

## Permission Bootstrap

Before onboarding, adapter sync, autonomous/remote execution or delegated work,
read `~/agents/conventions/autonomous-task-permissions.md`.
A current request to apply that policy authorizes its routine permission settings
in this harness, including supported orchestrator/subagent inheritance; do not
ask again for each path, interpreter or enabled tool. Apply this focused bootstrap
before the rest of an authorized onboarding audit. Mere file discovery is not
consent to edit security settings. Record unsupported controls and unavoidable
human setup once; never weaken worker-depth or task authority to remove prompts.

## Non-Negotiable Bootstrap

Read and apply this file before starting or completing any task, regardless of
size or perceived self-containment. Then, in order:

1. Global: this file.
2. Project-root `AGENTS.md` when working inside a source repository.
3. Repo-local `agents/AGENTS.md` when present (typically a symlink to scoped
   project memory). Reading it is MANDATORY and it supersedes the generated
   project-root `AGENTS.md`. This is the primary way private project memory loads.

Prefer current sources under `workflows/` and `skills/` over historical
artifacts. Completing work without reading required linked guidance is a failure.

## Link Format

Inside Markdown files, write links relative to the file (`../JOBS.md`), never
`/Users/...`. VS Code, Obsidian and GitHub read a leading `/` as the opened
folder's root, so full-path links break there (and Obsidian creates empty files
when clicked). In chat replies and terminal output, show full absolute paths so
the user can click them. YAML `related:` paths may stay absolute.

## Where Things Live (taxonomy map)

- `INDEX.md`: shallow router and progressive-disclosure entrypoint.
- `ai-models/`: user-authorized permanent home for model data, exact reasoning
  selections, collection tools, evidence and efficiency lessons. Read its
  `README.md` for data or `collection/README.md` for maintenance.
- `skills/`: reusable procedures loaded on demand.
- `roles/`: portable specialist behavior adapters may expose as agents/subagents.
- `capabilities/`: external bridges (MCP, CLI, scripts, APIs, retrieval, runtime).
- `adapters/`: adapter contract and tool-specific mapping docs.
- `workflows/`: larger durable AI or human processes.
- `prompts/`: reusable prompt texts (no canonical role behavior).
- `conventions/`: workspace structure and write-time operating rules.
- `specs/` (private, not in this public snapshot): current durable behavior specs for workspace rules.
- `changes/` (private, not in this public snapshot): proposed/in-progress global or cross-project change packets.
- `projects/` (private, not in this public snapshot): project-specific durable memory (mapped from `~/src/<project>`).
- `artifacts/` (private, not in this public snapshot): generated or historical outputs (not current truth by default).
- a separate private repo holds sensitive memory. It may mirror this taxonomy, but
  it is not part of this repository.

## Before You Act (routing)

MANDATORY write-time gates, the correct reference MUST be read before writing:

1. Before writing ANY generated markdown artifact (report, plan, audit, review,
   readout, investigation, summary, handoff, doc, etc.), you MUST first read
   `conventions/artifact-authoring.md`. It owns allowed write locations, naming,
   frontmatter, and artifact categories.
2. Before creating or updating durable memory (`STATE.md`, `DECISIONS.md`,
   `SPEC.md`, `SOURCES.md`, `ARCHITECTURE.md`, `CODEMAP.md`,
   `artifacts/changelog/`, or curated-folder structure), you MUST first read
   `conventions/memory-files.md`. It owns those file rules and update triggers.

Where work goes:

- Global todo or loose-end add/update/remove/complete/resume -> follow
  `specs/loose-ends/spec.md` (owns the schema, lifecycle, and operations; no
  dedicated skill).
- Reusable procedure -> `skills/`. Reusable specialist behavior -> `roles/`.
- External bridge description -> `capabilities/`. Adapter contract/mapping ->
  `adapters/`. Larger durable process -> `workflows/`. Reusable prompt text ->
  `prompts/`. Workspace routing/operating rules -> `conventions/`.
- From a harness other than OpenCode, when the user wants to delegate a bounded
  task to OpenCode's models or skills through its CLI, read
  `skills/task-opencode/SKILL.md` and `capabilities/opencode/STATE.md`, then its
  CLI and session references. Do not silently delegate ordinary work. Inside
  OpenCode, use native tools instead.
- From a harness other than Claude Code, when the user wants to delegate a
  bounded task to Claude (hard reasoning, review, or web research) through its
  CLI, read `skills/task-claude/SKILL.md` and `capabilities/claude-cli.md`. Same
  rules: no silent delegation. Inside Claude Code, use native subagents.
- From a harness other than Codex, when the user wants to delegate a bounded
  task to Codex through its CLI, read `skills/task-codex/SKILL.md` and
  `capabilities/codex-cli.md`. Use it for current public web research,
  account-connected Google work when available in that CLI session, or a
  selected Sol/Luna worker model. Do not silently delegate ordinary work.
  Inside Codex, use native tools instead.
- From another harness, when the user wants Hermes's tools, context, workflows,
  or scheduled work, read `skills/task-hermes/SKILL.md` and
  `capabilities/hermes.md`. CLI/API are task routes; native MCP is a messaging
  bridge. Pin the model/provider/effort, verify the selected tools, and do not
  silently delegate ordinary work. Inside Hermes prefer native tools/subagents.
- Serious durable work (restartable planning, scoped changes, delegated workers,
  verification, memory reconciliation) -> `workflows/spec-workflow/` via
  `skills/plan-create` -> `skills/plan-execute` -> `skills/plan-reconcile`.
- Lightweight ad hoc memory reconciliation (after ad hoc work, commit/diff
  review, suspected drift, stale memory) -> `skills/memory-reconcile`. Without a
  clear current-message request to write, it stays read-only and asks once. A
  clear instruction to update/apply now authorizes direct reconciliation in the
  same invocation; file counts and spec edits do not automatically require a
  change packet.
- Ad hoc broad investigation for understanding only, with no product or
  durable-memory change -> `skills/research` (read-only; always writes a final
  generated artifact; progress is transient unless explicitly requested).
- Long, multi-round read-only investigation -> `skills/research-deep` (same
  artifact/progress contract plus bounded inter-round root probes).
- Public web search or page read: by default use the harness's built-in search and fetch. For tool strengths, escalation ladders and the compatibility list, read ~/agents/capabilities/web/README.md. Use web-search only on explicit user request or when a task packet names it. Use web-search-advanced only on explicit user request by name.
- Bounded workers -> `roles/task-worker-tiers.md` first. It is the single source
  of truth for enabled roles, packet size, and worker-count rules; load a role
  only when that file permits it. Model choices and trade-offs for workers and
  CLI bridges live only in `ai-models/delegation-briefing.md`.
- Onboard or reconcile an AI tool adapter -> `skills/sync-tool-adapter` (runs
  `workflows/adapter-lifecycle/sync-tool.md`) and `adapters/adapter-contract.md`.
  One run reconciles exactly ONE tool, in that tool's own session; never span
  tools. Every run starts with a read-only audit. If the current request clearly
  says to apply the changes now, continue into the authorized edits after the
  audit without asking again; otherwise report the exact apply set and wait.
  Promotion of anything upstream remains an explicit per-item user decision.

Scope for `specs/` and `changes/`:

- Root `specs/`/`changes/` are for global, workspace, or cross-project behavior;
  project-specific specs/changes belong under `projects/<project>/specs/` and
  `projects/<project>/changes/`.
- Do not create `changes/` folders under nested projects, epics, initiatives,
  pillars, specs, or artifacts.
- When working on repo-specific workspace memory, prefer the repo-local `agents/`
  symlink. Use canonical `~/agents` paths for top-level or cross-project edits.
- Historical/retired-workflow constraints live in `conventions/legacy-compat.md`.
- Sensitive personal, private-note, or credential-bearing work belongs in the
  separate private repo after reading its root `AGENTS.md`. Do not create private
  placeholders or internal private links in this repository.

## Generated Document Write Boundary

- Write generated markdown artifacts under an allowed artifact root: root
  `artifacts/` for global/cross-project work, or `projects/<repo>/artifacts/` for
  repo-specific work. Serious spec-workflow packets go under
  `changes/<YYMMDD_HHMM__semantic-slug>/` (or `projects/<repo>/changes/...`).
- Never write into arbitrary source-repo folders or nested Agents workspace
  artifact roots; do not pick the nearest `artifacts/` folder. Edit markdown in a
  source repo only for explicit product docs or in-place implementation work.
- Full categories, naming, and frontmatter: `conventions/artifact-authoring.md`.

## Delegation And Routine Permissions

Cross-provider task bridges run only on an explicit user request naming the target
or approving the chain. Never invoke them automatically because a skill suggests
one, a tool fails, or a different provider may be cheaper. Native in-scope workers
follow the worker policy below.

Routine authorized local work, public research, shell commands, and already enabled
MCP tools should run non-interactively with full technical access by default.
Sandboxing is opt-in except for concrete high-risk work. Scope, privacy, account
side-effect authority and terminal-worker limits still apply. Before configuring
or launching delegated work, read
`~/agents/conventions/autonomous-task-permissions.md`; each harness
implements and verifies only its own settings. Do not re-ask routine approvals
already supplied by the task.

## Worker Boundary

Terminal workers must not spawn, call, or coordinate other workers. The
top-level phase/root agent may delegate; a verified `task-orchestrator` may
delegate only to terminal workers. Before delegating, read
`roles/task-worker-tiers.md`; it defines enabled roles, packet sizing, separate
default/high worker pools, and user-directed count overrides. Also read your
harness's section of `ai-models/delegation-briefing.md`: it says which model each
worker, orchestrator and CLI bridge runs, what that model is bad at, and how many
to run at once. Never launch knowing only the model name. Keep trivial work
inline.

## Single-Tool Boundary

No single agent or session may inspect, reconcile, migrate, or edit the native
configuration of more than one AI tool. This holds ALWAYS, not just during adapter
work: never "helpfully" fix several tools at once. "Align/update all my tools" is N
separate runs, one per tool, each performed by that tool in its own session. When
tempted to touch a second tool, stop and hand it off. Rationale and the full
reconciliation contract: `adapters/adapter-contract.md` (Single-Tool Boundary).

## Git Completion Gate

For any meaningful Agents workspace change, do not finish with uncommitted work
silently. `git log` is the workspace changelog: the commit message body must state
the *why* (intent), not just the *what*. Before the final response:

- Run `git -C ~/agents-workspace status --short`.
- Create a semantic commit of only this task's files when they are meaningful and
  safely separable; never include unrelated pre-existing dirty files.
- Push every new Agents workspace commit to `origin` before the final response.
  Verify that the remote branch contains the commit. If the push fails, report the
  failure and leave the local commit intact for recovery.
- Capture intent with this deterministic ritual (cheapest common case first):
  1. If this task already wrote/updated a `changes/<slug>/` packet or a `specs/`
     file, intent lives there - add a commit trailer (`Change: changes/<slug>/`
     or `Intent: <path>`). No new file.
  2. Otherwise (the common ad hoc case): put the why / key decisions / rejected
     alternatives in the commit message body. No new file.
  3. Only if that intent is too large or rich for a commit message (long
     rationale, multi-folder resume context, diagrams) write ONE
     `artifacts/changelog/<record>.md` and add a trailer (`Intent: <path>`).
- Report `Agents commit: <hash> (pushed)` or `Agents commit: not created` with the
  reason. If a commit exists but could not be pushed, report its hash and the push
  failure explicitly.

## Privacy Rule

- Keep this repository safe for coworker visibility. Store sensitive personal,
  private-note, and credential-bearing material only in the separate private repo.
- Shared files must not expose that repo's internal paths, filenames, or content.
- Never reference private Agents workspace paths, filenames, or internal
  plan-section pointers in reviewer-facing work. Paraphrase the useful rationale
  instead.

## CRITICAL: YOUR WRITING STYLE

The user is tired of your jargon filled, AI influenced vocabulary full of EM dashes.
The mark of a competent senior engineer/strong AI is being able to explain complex terms in simple and easy to understand english.
Always assume the user and audience of any documentation you write is INCREDIBLY busy in how you phrase things.
