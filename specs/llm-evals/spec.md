---
created_at: 2026-10-13
updated_at: 2026-10-13
model: claude-sonnet-5-5
doc_type: spec
purpose: Router for the LLM evals spec: how to learn evals from the captured sources and how to build a small worker-evals loop for this workspace.
related:
  - path: ./COMPENDIUM.md
    why: Superdoc 1. Teaches evals from every captured source.
  - path: ./IMPLEMENTATION-GUIDE.md
    why: Superdoc 2. Steps to build the worker evals loop, by time budget.
  - path: ./STATE.md
    why: What exists, what is missing, decisions still open.
  - path: ./SOURCES.md
    why: Evidence ledger for every capture and digest.
  - path: ./DECISIONS.md
    why: Choices the user made when starting this spec.
  - path: ./AGENTS.md
    why: How to add a source or edit here.
  - path: ../youtube-extraction/spec.md
    why: Sibling spec for pulling YouTube transcripts, used for the videos here.
  - path: ../../skills/model-bakeoff/SKILL.md
    why: Existing model comparison skill the guide proposes to extend.
  - path: ../../skills/spec-from-research/SKILL.md
    why: Reusable procedure that encodes how this spec was built.
---

# LLM evals

This spec holds what we learned about evaluating LLM apps and agents, so the Agents workspace can later check its own workers: did the worker do the job, stay in scope, and was it worth the cost. It started from one ChatGPT deep research report on 13 October 2026. Every link in that report was captured word for word, each source was summarised, and the summaries were merged into a learning document and a build guide. Nothing has been built yet. The guide is a proposal.

## Start Here

- **Learn:** [COMPENDIUM.md](COMPENDIUM.md), about 60 to 75 minutes. Part 2 is a one-page overview and part 10 is a learning path.
- **Build:** [IMPLEMENTATION-GUIDE.md](IMPLEMENTATION-GUIDE.md). Section 1 has the recommendation. Section 2 gives plans for 2 hours, 1 day, 1 week and ongoing.
- **Status:** [STATE.md](STATE.md), including capture gaps and open decisions.
- **Decisions:** [DECISIONS.md](DECISIONS.md), what the user chose and why.
- **Sources:** [SOURCES.md](SOURCES.md), the ledger, links not captured and claims to avoid.
- **Working here:** [AGENTS.md](AGENTS.md), layout and how to add a source.

## What this spec covers

- How to find and name failures in LLM runs, check them with code, and add a judge only when code cannot decide.
- Agent-specific checks: result and path, repeated runs, reset and isolation, routing and effort.
- Tools compared: promptfoo, Inspect AI, AgentEvals, the evals-skills repo, Recipe Chatbot exercises.
- A proposed `worker-evals` skill for this workspace, built around the existing model-bakeoff workflow.

It does not cover YouTube extraction (see [../youtube-extraction/spec.md](../youtube-extraction/spec.md)) or model choices (see [../../ai-models/delegation-briefing.md](../../ai-models/delegation-briefing.md)).

## Current answer

From [IMPLEMENTATION-GUIDE.md section 1](IMPLEMENTATION-GUIDE.md#1-recommendation-first). All of this is inference, not a tested result.

- Build one portable `worker-evals` skill around [model-bakeoff](../../skills/model-bakeoff/SKILL.md).
- Start with one role (`task-execute`), in Codex, on small TypeScript edits.
- Review saved runs first, then turn observed failures into five to ten reusable cases checked by code.
- Add a local promptfoo suite when replaying cases by hand gets tedious. Add one human-validated judge only for a failure code cannot decide. Keep Inspect AI for later.
- Today's first step: review five recent `task-execute` runs and write one failure note per flawed run.

## How this spec was built

[../../skills/spec-from-research/SKILL.md](../../skills/spec-from-research/SKILL.md) now encodes the procedure used here (capture, digest, compendium, guide, spec files, review). Reuse it for the next research report.
