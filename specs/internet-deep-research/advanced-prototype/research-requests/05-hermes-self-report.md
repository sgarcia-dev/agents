---
created_at: 2026-09-30
updated_at: 2026-09-30
model: anthropic/claude-opus-5-5
artifact_category: specs
doc_type: prompt
purpose: Copy-paste request asking the local Hermes Agent to explain, from its own skill files and config, exactly how its deep research works, so the engine can reuse what already runs on this Mac.
related:
  - path: ../spec.md
    why: The engine this research feeds.
  - path: ../../../hermes-internet-deep-research/spec.md
    why: What the workspace already knows about Hermes research. This request fills the gaps in how its loop and prompts work.
  - path: ./README.md
    why: Where to save the result.
---

> Historical, 2026-10-01: This prototype is parked. It is not current policy or a build plan. Current web facts and decisions: [capabilities/web](../../../../capabilities/web/README.md) and [web decisions](../../../../capabilities/web/DECISIONS.md).

# Request 5: Ask Hermes how its own research works

Send to: **Hermes Agent** (chat, CLI, or Discord). This is not web research.
Hermes should read its own skills and config and explain them. Hermes already
has a live research setup (local SearXNG search, keyed Parallel reading, a
citation ledger), so it is the one system here we can inspect directly.

Copy everything below the line.

---

I want a detailed markdown report on exactly how your deep internet research
works, so I can reuse the good parts in a research system that runs across
several agent tools. Do not search the web for this. Read your own files and
settings and explain what is really there.

## Read these first

- Your research skills under your skills folder, especially
  `research/hermes-internet-deep-research`, `research/running-research-on-request`,
  `research/grounded-citations`, `research/durable-research-bundles`, and
  anything they load (for example `blocked-page-recovery`).
- Your web settings: the search backend, the page reader, caching, fallback,
  and any limits.
- Any built-in research, delegation, or sub-agent features Hermes has that
  your skills do not use yet.

## Explain, with file paths and short quotes

1. **The loop, step by step**: what happens from the moment a research request
   arrives to the final report. For each step: which skill or tool runs, what
   goes in, what comes out, and where it is saved.
2. **The prompts**: quote the instructions that drive each step (scoping,
   search planning, picking pages, reading, note taking, checking gaps,
   deciding to stop, writing, checking citations). Point out any step that has
   no written instructions and is left to the model.
3. **Effort and budget**: your three effort lanes (focused, standard deep,
   high-stakes). How is a lane chosen? How are the search and page-read
   ceilings enforced: by code, or only by instructions? Can I set exact
   numbers per run (for example "at most 5 searches")?
4. **Counting and cost**: what you count during a run (queries, URLs read,
   repeats, cached hits), where the counts go, and whether you can report the
   cost of a run.
5. **Models**: which model does each step use today? Can different steps use
   different models (a cheap one for reading, a strong one for writing)? If
   so, how do I set that?
6. **Sub-agents**: can you split research across workers? How are they told
   their budget? How are results merged?
7. **Citations**: how the ledger works, what `verify` checks, and what it does
   not check.
8. **Reuse outside Hermes**: which parts are Hermes-only, and which parts are
   plain instructions that another agent (Claude Code, Codex, OpenCode) could
   follow as-is.
9. **Weak spots**: what breaks, what is slow, what you would change.

## Format

- Plain, simple English. Short sections. Real file paths.
- Separate "this is in a file" from "this is my understanding".
- Save the report as a markdown file and tell me its path.
- Do not change any skills, settings, or memory while doing this. Read only.
