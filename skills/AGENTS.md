# Skills

Use this folder for portable reusable procedures. A skill describes how to run a
workflow or repeatable task. It should be loadable on demand rather than included
in always-loaded instructions.

## Belongs Here

- Reusable procedures such as `plan-create`, `plan-execute`, `plan-reconcile`,
  `memory-reconcile`, and `model-bakeoff`.
- Thin entrypoints into larger workflows when the procedure is part of a durable
  process.
- Validation and final-output expectations for a procedure.

## Does Not Belong Here

- Specialist behavior without a procedure. Use `../roles/`.
- Tool-native command, slash-command, or subagent config. Use `../adapters/` to
  describe the mapping and keep native files outside the Agents workspace unless
  explicitly requested.
- One-off implementation plans. Use a change packet (kept in a private folder, not published) for serious durable work.

## Current Guidance

The canonical spec-workflow phase procedures live here:

- `plan-create/SKILL.md`
- `plan-execute/SKILL.md`
- `plan-reconcile/SKILL.md`

The lightweight ad hoc memory reconciliation procedure lives at:

- `memory-reconcile/SKILL.md`

The ad hoc read-only broad investigation procedure lives at:

- `research/SKILL.md`: delegate discovery via the phase-neutral discovery cadence
  and always write one final disk-backed findings artifact, with transient
  progress by default and explicit worker-report or recoverable modes. A sibling
  of `memory-reconcile`, outside the plan-create -> plan-execute -> plan-reconcile
  chain.
- `research-deep/SKILL.md`: multi-round variant that adds a tightly bounded root
  probe between complete rounds while reusing the same final-artifact and
  progress-mode contract.

The portable model comparison procedure lives at:

- `model-bakeoff/SKILL.md`

Additional canonical skills currently include:

- `browser-use/SKILL.md`: portable route selector for public, signed-in,
  hosted, parallel and desktop browser work; references load on demand. The
  browser-use spec owns safety and verification; capability guides own each
  connector's onboarding, and local harness wrappers own native calls.
- `chatgpt-browser/SKILL.md` and `claude-browser/SKILL.md`: portable website
  procedures, each with separate export, project, and conversation references.
  Runtime wrappers link here instead of duplicating selectors or steps.
- `browser-deep-research-prompts/SKILL.md`: writes ready-to-paste deep
  research prompt packs for ChatGPT and Claude, with start and export files
  for browser agents and one grouped `~/Downloads` folder for the reports.
- `spec-from-research/SKILL.md`: turns a deep research report into a spec folder
  with a verbatim copy of every linked source, one digest per source, a
  compendium and an implementation guide, using parallel cheap capture and digest
  workers and fast blocking workers for the superdocs; rules and packet templates
  live in its `references/`.
- `role-dispatch/SKILL.md`: one-run adapter-resolved role launch with explicit
  model, reasoning, service, monitoring, and concurrency controls.
- `sync-tool-adapter/SKILL.md`: exhaustive single-tool onboarding and drift
  reconciliation against the canonical workspace.
- `task-opencode/SKILL.md`: non-OpenCode callers dispatch and supervise a bounded
  task through the OpenCode V2 CLI; it is not used from OpenCode itself.
- `task-claude/SKILL.md`: non-Claude callers dispatch and supervise a bounded task
  through the Claude Code headless CLI; it is not used from Claude Code itself.
- `task-codex/SKILL.md`: non-Codex callers dispatch and supervise a bounded task
  through the Codex CLI; it is not used from Codex itself.
- `task-hermes/SKILL.md`: other harnesses dispatch and verify a bounded Hermes
  task via CLI/API; native MCP is a separate conversation/messaging bridge.
- `task-gemini/SKILL.md`: other harnesses dispatch and supervise a bounded Gemini
  task via the Antigravity CLI (agy); it is not used from Gemini itself.
- Public web search or page read: by default use the harness's built-in search and fetch. For tool strengths, escalation ladders and the compatibility list, read ~/agents/capabilities/web/README.md. Use web-search only on explicit user request or when a task packet names it. Use web-search-advanced only on explicit user request by name. The skill owns procedure; research and research-deep own the investigation process.
- `web-search-advanced/SKILL.md`: bigger, careful web search with per-provider
  counts, page quotes, and one saved report under `artifacts/web-searches/` (a private output folder, not published).
  Explicit invocation only; never started by an agent or by `web-search`.

Workflow packages under `../workflows/` describe how these skills compose with
roles, templates, adapter mappings, and durable output locations.

## Capability Hint

A skill may declare the connectors (see `../capabilities/connectors.md`) its
procedure depends on, as a lightweight hint in frontmatter. A skill does NOT own
connector scoping: it declares a dependency, and the root/phase plus
tool/session/project configuration own whether the connector is available.

```yaml
capabilities:
  requires: [ddg]   # procedure is blocked or materially degraded without it
  suggests: []      # nice-to-have; procedure still works without it
```

Rules:

- Declare a capability here only when the procedure genuinely leans on a
  registry connector. Skills backed by a CLI or built-in tool (e.g. `gh`) or that
  delegate discovery to a role need no `capabilities` block; most skills have none.
- `requires`/`suggests` are dependency hints, not authority. Availability and
  enablement are resolved outside the skill by the active root/phase session and
  tool configuration, never by the skill and never automatically.
