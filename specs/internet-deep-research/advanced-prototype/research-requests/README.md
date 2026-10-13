---
created_at: 2026-09-30
updated_at: 2026-09-30
model: anthropic/claude-opus-5-5
artifact_category: specs
doc_type: index
purpose: Router for the copy-paste research requests that fed the internet deep research engine spec. Says which prompt went to which tool and where each result was filed. All five were answered and reconciled on 2026-09-30.
related:
  - path: ../spec.md
    why: The engine these requests feed.
  - path: ./01-under-the-hood.md
    why: Request 1, how existing systems work inside.
  - path: ./02-prompts.md
    why: Request 2, the prompt text each stage uses.
  - path: ./03-cost-and-scale.md
    why: Request 3, cost, efficiency, and budget tiers.
  - path: ./04-claude-combined.md
    why: One merged request for a single Claude Research run.
  - path: ./05-hermes-self-report.md
    why: Ask Hermes to explain its own research loop from its files.
---

> Historical, 2026-10-01: This prototype is parked. It is not current policy or a build plan. Current web facts and decisions: [capabilities/web](../../../../capabilities/web/README.md) and [web decisions](../../../../capabilities/web/DECISIONS.md).

# Research requests

**Status: done.** All five were answered on September 30, 2026, filed
verbatim in the bundle's `external/` folder, verified, and reconciled into
this spec. See [../SOURCES.md](../SOURCES.md) for each report's summary,
trust level, and known errors. The prompts stay here so a future re-run asks
the same questions.

Five ready-to-paste prompts. Each file has a "copy everything below the line"
marker. They are self-contained: the receiving tool needs no access to this
workspace.

## What to send where

| # | Prompt | ChatGPT Deep Research | Claude Research | Hermes |
|---|---|---|---|---|
| 1 | [Under the hood](./01-under-the-hood.md) | **Send** | optional | no |
| 2 | [Prompts](./02-prompts.md) | **Send** | **2nd Claude run, if any** | no |
| 3 | [Cost and scale](./03-cost-and-scale.md) | **Send** | optional | no |
| 4 | [Claude combined](./04-claude-combined.md) | no | **Send (1st run)** | no |
| 5 | [Hermes self-report](./05-hermes-self-report.md) | no | no | **Send** |

Minimum useful set: ChatGPT 1-3, Claude 4, Hermes 5. That is five runs, only
one on Claude.

## Where to save results

Save each finished report as Markdown in the scan bundle's `external/` folder:

```text
~/agents/artifacts/investigations/26-09-30_13-24__research__deep_research_engine_scan_claude-opus-5-5/external/
  chatgpt_01_under_the_hood.md
  chatgpt_02_prompts.md
  chatgpt_02_prompt_pack.md      (the Markdown prompt pack that came with request 2)
  chatgpt_03_cost_and_scale.md
  claude_04_combined.md
  hermes_05_self_report.md
```

The `chatgpt-browser` and `claude-browser` skills can export a finished
conversation to Markdown if copying by hand is a pain. After the reports are
in, ask an agent to run `memory-reconcile` on this spec: promote what holds
up into [../spec.md](../spec.md), [../budget-tiers.md](../budget-tiers.md), and
[../stage-prompts.md](../stage-prompts.md), and record disagreements between
the reports in [../DECISIONS.md](../DECISIONS.md).
