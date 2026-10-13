---
created_at: 2026-09-30
updated_at: 2026-09-30
model: anthropic/claude-opus-5-5
artifact_category: specs
doc_type: prompt
purpose: Copy-paste deep research request 1 of 3. How open-source and local deep research systems actually work, stage by stage, and which knobs control their size.
related:
  - path: ../spec.md
    why: The engine this research feeds.
  - path: ./README.md
    why: Which prompt to send to which tool, and where to save the result.
---

> Historical, 2026-10-01: This prototype is parked. It is not current policy or a build plan. Current web facts and decisions: [capabilities/web](../../../../capabilities/web/README.md) and [web decisions](../../../../capabilities/web/DECISIONS.md).

# Request 1: How deep research works under the hood

Send to: **ChatGPT Deep Research** (first choice). Optional for Claude Research.
Save the result as described in [README.md](./README.md).

Copy everything below the line.

---

I am building my own deep research system. I want to understand how existing
deep research systems work inside, stage by stage, so I can copy what works
and skip what does not. Please research this thoroughly and write a detailed
report.

## My situation

- I already have the building blocks: web search (self-hosted SearXNG, plus
  Parallel, Exa, Firecrawl, and the built-in search in coding agents like
  Claude Code, Codex CLI, and OpenCode), page reading (Parallel, Firecrawl,
  built-in fetch), and many models (cheap open models through an OpenCode Go
  subscription, OpenAI models through a ChatGPT plan, Claude models,
  OpenRouter pay-per-token).
- What I do not have is the research loop itself: the stages, the order, what
  each stage passes to the next, and the rules for when to stop.
- The system must work in any agent harness (Claude Code, Codex, OpenCode,
  Hermes Agent), so I care about the design, not one framework's code.

## Systems to cover

Cover as many as you can, in roughly this priority order. Skip any you cannot
find real evidence for, and tell me you skipped it.

1. LearningCircuit **Local Deep Research** (LDR), including its strategies
   (for example "focused iteration" and others) and its Mac app if any.
2. **GPT Researcher** (assafelovic), including its "deep research" mode.
3. **LangChain open_deep_research** (supervisor plus researcher sub-agents).
4. **Stanford STORM / Co-STORM**.
5. **dzhng/deep-research** (the breadth and depth recursive design).
6. **Jina node-DeepResearch** (the search, read, reason loop with a token
   budget).
7. **Hugging Face smolagents open_deep_research**.
8. Newer 2026 open-source projects that have real adoption (for example
   anything that tops a public deep research benchmark). Name them and say
   why they matter.
9. What is publicly known about how **OpenAI Deep Research**, **Anthropic's
   Research feature** (their engineering post on the multi-agent research
   system), **Google Gemini Deep Research**, and **Perplexity** work inside.

## For each system, tell me

- **The stages**, in order: clarify the question, plan, write search queries,
  search, pick which results to open, read and extract notes, compress notes,
  check for gaps, decide whether to keep going, write, cite, verify. Which
  ones does it have, which ones does it skip?
- **What moves between stages**: full pages, extracted notes, summaries,
  citation lists? How big?
- **Size knobs**: breadth, depth, iterations, max results per query, max
  pages, token budgets, concurrency, number of sub-agents. Give the real
  config names and defaults when you can find them.
- **Stopping rules**: fixed rounds, a token budget, "no new information", a
  model's judgment, or something else?
- **Model use**: which stages use a cheap model and which use a strong one?
- **Typical run size**: how many searches, page reads, and model calls a
  normal run makes, and measured cost if anyone published it.
- **Known weaknesses**: from issues, benchmarks, and user reports.

## What I want at the end

1. A comparison table of all systems across the points above.
2. **The common skeleton**: the smallest loop that almost all of them share.
3. **The knobs that matter most** for scaling one design from a tiny run (under
   5 searches) to a huge one (200+ searches), and what breaks first as you
   scale up.
4. **Design choices that clearly differ** between systems (for example one
   loop versus many parallel sub-agents, recursive versus flat, reading full
   pages versus snippets), with evidence on which works better and when.
5. A short list of the 3 to 5 designs you would study first if you were
   building this, and why.

## Rules for sources

- Prefer primary sources: GitHub repositories and their actual source and
  config files, official docs, papers, engineering blog posts. Link the exact
  file when you cite code.
- Community posts (Reddit, Hacker News, forums) are welcome as experience
  reports, but label them as opinion.
- Give dates. This field changes monthly, so say how recent each fact is.
- Mark clearly what a source says versus what you infer. If a number is
  unknown, say unknown. Do not estimate silently.
- Write in plain, simple English. Explain any technical term the first time
  you use it.
