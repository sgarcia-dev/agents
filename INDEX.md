---
created_at: 2026-07-01
updated_at: 2026-09-30
model: openai-codex/gpt-6-sol-900k
doc_type: index
purpose: Provide a shallow Agents workspace router without requiring recursive inspection.
related:
  - path: ~/agents/AGENTS.md
    why: Canonical workspace operating rules and root taxonomy.
  - path: ~/agents/skills/AGENTS.md
    why: Reusable procedure ownership rules.
  - path: ~/agents/roles/AGENTS.md
    why: Portable specialist behavior ownership rules.
  - path: ~/agents/capabilities/AGENTS.md
    why: External capability bridge ownership rules.
  - path: ~/agents/adapters/AGENTS.md
    why: Tool adapter ownership and drift rules.
  - path: ~/agents/workflows/spec-workflow/AGENTS.md
    why: Durable spec-workflow process router.
  - path: ~/agents/workflows/model-bakeoff/AGENTS.md
    why: Portable model benchmark workflow for adapter-resolved model comparisons.
---

# Agents Workspace Index

Start here when orienting to the Agents workspace. Read only the sections
needed for the current task, then load the linked files on demand.

## Permission Bootstrap

For onboarding or prompt-free remote/autonomous execution, read
`~/agents/conventions/autonomous-task-permissions.md` first.
It owns routine command/path/MCP preapproval, root/orchestrator/leaf posture,
exceptions, immediate apply instructions and required per-harness bypass flags.
`ai-models/` does not own permissions.

## Core Entry Points

- `AGENTS.md`: canonical workspace rules, root taxonomy, routing, artifact
  boundaries, and completion gates.
- `skills/`: reusable procedures that an agent can load when a task calls for a
  known workflow, including artifact-producing `research` and the multi-round,
  bounded-root-review `research-deep` variant. Public web search or page read: by default use the harness's built-in search and fetch. For tool strengths, escalation ladders and the compatibility list, read ~/agents/capabilities/web/README.md. Use web-search only on explicit user request or when a task packet names it. Use web-search-advanced only on explicit user request by name. Advanced runs save a bounded research report. `role-dispatch` owns one-run
  adapter-resolved role execution with explicit runtime profiles. The
  `chatgpt-browser` and `claude-browser` skills own website procedures for
  exports, projects, and conversations, independent of the browser controller.
  `browser-use` selects the browser identity and route, with on-demand references.
  `task-hermes` dispatches a scoped job to Hermes from another harness, with
  explicit runtime selection and independent result checks.
- `roles/`: reusable specialist behaviors that adapters may expose as native
  agents, subagents, prompt bundles, or command wrappers. Default micro workers
  cover tiny parallel packets; enabled high workers cover bounded real tasks.
- `capabilities/`: descriptions of external bridges such as MCP, CLI, scripts,
  APIs, retrieval, browser-native tools and desktop control. `connectors.md`
  inventories browser bridges beyond MCP and links their setup/proof guides.
  [Hermes](capabilities/hermes.md) covers task delegation,
  its capability menu, model choice, CLI/API, messaging MCP and optional A2A.
- `adapters/`: lightweight adapter registry, platform-neutral adapter contract,
  and tool-specific mapping docs. Adapter docs must translate the Agents
  workspace contract; they must not become source of truth.
- `workflows/`: larger durable processes composed from skills, roles,
  capabilities, templates, and references.

Current high-signal workflows are `workflows/spec-workflow/`,
`workflows/adapter-lifecycle/`, and `workflows/model-bakeoff/`.

## Durable Work

- `ai-models/`: permanent model-comparison home. Read
  `~/agents/ai-models/README.md` for human/agent data access or
  `~/agents/ai-models/collection/README.md` for efficient collection,
  extension and troubleshooting. Its `STATE.md` is the compaction resume point.
  Before delegating to any model, read
  `~/agents/ai-models/delegation-briefing.md`: the only place that
  chooses models for workers, orchestrators, CLI bridges and web search.
- `specs/model-delegation/`: rules for who owns model choices and how changes
  reach each tool without drift.
- `specs/loose-ends/`: global active loose-end tracking and compact restart-context rules.
- `specs/` (only selected specs are in this public snapshot): current durable behavior specs. `specs/agents-workspace/mission.md`
  holds the founding thesis (durable theory of the work + tool-agnostic operating
  contract) and the governing "tools converge to the system" corollary.
  `specs/browser-use/spec.md` owns cross-harness browser-use safety and
  verification; `skills/browser-use` is the progressive operating entrypoint.
  [capabilities/web](capabilities/web/README.md) owns all
  search and fetch facts, ladders and compatibility.
  `specs/web-scraping-site-access` owns per-platform access routes (social,
  forums) and third-party data providers, one file per site and provider.
  `specs/internet-deep-research/spec.md` retains standalone research apps,
  funding and historical evidence.
  `specs/browser-deep-research/spec.md` owns research prompts for the
  ChatGPT and Claude websites, mode choice and the benchmark log.
  `specs/hermes-internet-deep-research/spec.md` owns restoring Hermes page
  extraction and verifying its cited research reports.
  `specs/youtube-extraction` owns getting
  faithful YouTube transcripts and visual checks for research agents, with
  tested routes and the rate-limit findings.
  `specs/llm-evals` owns learning and building LLM and
  agent evals: verbatim sources, a compendium and an implementation guide.
  `skills/spec-from-research/SKILL.md` turns a research report into a spec
  like these.
  `skills/web-search-advanced/SKILL.md` owns the explicit-only procedure.
  Current web decisions live in `capabilities/web/DECISIONS.md`. The same spec nests the parked bigger design at
  `specs/internet-deep-research/advanced-prototype/spec.md`. Its research stays
  referenceable. Only the user decides if and when to rebuild it, and any
  rebuild must be much simpler to maintain.
- `changes/` (private, not in this public snapshot): proposed or in-progress global, cross-project, or workspace change
  packets.
- `projects/` (private, not in this public snapshot): project-specific durable memory and repo-scoped specs, changes,
  and artifacts.
  `projects/agent-lab` is a research project with
  no source repo: seven specs on making cheap agents more capable and frontier
  agents cheaper (verification, context retrieval, context management,
  knowledge structure, delegation, long-running work, skills and tools). Start
  with its `ROADMAP.md`. Its specs teach and propose; accepted changes go through
  `plan-create` into the root owners.
- `artifacts/` (private, not in this public snapshot): generated or historical outputs. Do not treat artifacts as
  current truth unless current guidance points to them. Use `artifacts/system/`
  for curated Agents workspace system references and design background.

## Existing Special Roots

- `prompts/`: reusable prompt text and legacy prompt routing. Reusable specialist
  behavior belongs in `roles/`.
- `conventions/`: reserved for workspace structure and operating rules that do
  not belong in a stronger root.
- a separate private repo holds sensitive memory. Shared files do not link to its
  internal paths.

## Progressive Disclosure Rule

Do not recursively inspect the Agents workspace by default. Read `AGENTS.md`,
this index, and the nearest relevant `AGENTS.md` first. Load detailed skills,
roles, capabilities, adapter docs, specs, changes, project memory, or artifacts
only when the task requires them.
