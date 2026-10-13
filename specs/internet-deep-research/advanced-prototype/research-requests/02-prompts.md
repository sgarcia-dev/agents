---
created_at: 2026-09-30
updated_at: 2026-09-30
model: anthropic/claude-opus-5-5
artifact_category: specs
doc_type: prompt
purpose: Copy-paste deep research request 2 of 3. The actual prompt text deep research systems use for each stage, and what makes those prompts work.
related:
  - path: ../spec.md
    why: The engine this research feeds.
  - path: ../stage-prompts.md
    why: Our draft stage prompts, which this research should improve.
  - path: ./README.md
    why: Which prompt to send to which tool, and where to save the result.
---

> Historical, 2026-10-01: This prototype is parked. It is not current policy or a build plan. Current web facts and decisions: [capabilities/web](../../../../capabilities/web/README.md) and [web decisions](../../../../capabilities/web/DECISIONS.md).

# Request 2: The prompts deep research systems use

Send to: **ChatGPT Deep Research** (first choice). Good second pick for
Claude Research, since it is the prompt most likely to change what we build.
Save the result as described in [README.md](./README.md).

Copy everything below the line.

---

I am building my own deep research system: a loop that plans, searches the
web, reads pages, checks for gaps, searches again, and writes a cited report.
I already understand the general idea and I already have search, page
reading, and many models. **What I am missing is the actual prompt text** for
each step. I want to learn from the prompts that real systems use, so please
find them, quote them, and explain what makes them work.

## My situation

- Search and reading tools are ready (SearXNG, Parallel, Exa, Firecrawl, and
  built-in agent search). Models range from very cheap open models (through
  an OpenCode Go subscription) to frontier models (OpenAI, Anthropic).
- I want to use **cheap models for high-volume steps** (reading pages,
  pulling notes) and **strong models only where it matters** (planning,
  judging gaps, writing). So I need prompts a cheap model can follow reliably.
- The system must run inside different agent tools (Claude Code, Codex,
  OpenCode, Hermes Agent), so prompts should be plain text, not tied to one
  framework.

## Find the real prompts for each step

For each step below, find the prompts that open-source systems actually use.
Quote the important parts (short excerpts are fine) and link the exact source
file.

1. **Clarify**: asking the user follow-up questions, or deciding not to.
2. **Research brief / plan**: turning a request into sub-questions.
3. **Query writing**: turning a sub-question into search queries.
4. **Result picking**: deciding which search results are worth opening.
5. **Page reading / note taking**: pulling useful facts and quotes from one
   page, with the source URL kept.
6. **Compressing**: shrinking many notes before they reach the writer.
7. **Gap check / reflection**: deciding what is still missing and whether to
   do another round. How do prompts avoid endless looping?
8. **Supervisor / delegation**: how a lead agent splits work between
   sub-agents and tells them how much effort to spend.
9. **Writing the report**: structure, citation format, handling conflicts.
10. **Checking citations**: making sure each claim is backed by its source.

Places to look (not a complete list): LangChain open_deep_research
(`prompts.py`), GPT Researcher (`prompts.py`), dzhng/deep-research, Jina
node-DeepResearch, Stanford STORM, LearningCircuit Local Deep Research,
Hugging Face open_deep_research, Anthropic's engineering post on their
multi-agent research system and its open-sourced prompts in their cookbook,
OpenAI's deep research API guide and cookbook, and any 2026 projects that
score well on public deep research benchmarks.

## Then explain the patterns

- What instructions show up again and again across systems? (For example
  "scale effort to the question", "stop when new searches return the same
  facts", "always keep the URL next to the fact".)
- How do prompts tell the model **how much effort to spend**? Anthropic's post
  describes putting effort rules in the prompt. Find the actual wording and
  any others like it.
- How do prompts keep a cheap model from making things up while reading?
- What output formats do stages use to hand work to each other (JSON, bullet
  lists, markdown)? Which are easiest for cheap models?
- Which prompt mistakes are known to cause bad results (from issues, blog
  posts, or benchmarks)?

## What I want at the end

1. For each of the 10 steps: the best 1 or 2 real prompt examples (quoted,
   linked), and one short "what makes this work" note.
2. A list of the prompt patterns that matter most, ranked.
3. **A draft prompt of your own for each step**, written to be model-agnostic
   and budget-aware. Each prompt should take its budget as an input (for
   example "you may run at most {max_queries} searches") so the same prompt
   works for a tiny run and a huge run.
4. Which steps are safe to give to a cheap model and which are not, with
   evidence.

## Rules for sources

- Quote and link real prompt files. Do not invent a prompt and call it
  someone else's.
- Give dates and version or commit when possible. Prompts change often.
- Mark what a source says versus what you infer.
- Write in plain, simple English.
