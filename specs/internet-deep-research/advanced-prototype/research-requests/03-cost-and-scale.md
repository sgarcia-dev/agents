---
created_at: 2026-09-30
updated_at: 2026-09-30
model: anthropic/claude-opus-5-5
artifact_category: specs
doc_type: prompt
purpose: Copy-paste deep research request 3 of 3. How to make deep research cheap, how cost grows with size, and how to design small, medium, and large budget tiers.
related:
  - path: ../spec.md
    why: The engine this research feeds.
  - path: ../budget-tiers.md
    why: Our draft tier table, which this research should check and correct.
  - path: ./README.md
    why: Which prompt to send to which tool, and where to save the result.
---

> Historical, 2026-10-01: This prototype is parked. It is not current policy or a build plan. Current web facts and decisions: [capabilities/web](../../../../capabilities/web/README.md) and [web decisions](../../../../capabilities/web/DECISIONS.md).

# Request 3: Cost, efficiency, and budget tiers

Send to: **ChatGPT Deep Research**. Optional for Claude Research.
Save the result as described in [README.md](./README.md).

Copy everything below the line.

---

I am building my own deep research system (plan, search, read, check gaps,
search again, write a cited report). Budget is my biggest worry. I want to
**set the size of every run myself**: sometimes under 5 searches, sometimes
10, sometimes 50, sometimes a few hundred. I want to know in advance roughly
what each size will cost and how good it will be. Please research this
thoroughly and write a detailed report.

## My situation

- **Models I can use**: cheap open models through an OpenCode Go subscription
  (flat monthly fee with usage caps), OpenAI models through a ChatGPT plan
  (flat fee with usage limits), Claude models through a Claude plan, and
  OpenRouter (pay per token). I may cancel or add plans later, so the design
  must let me swap providers easily.
- **Search and reading**: self-hosted SearXNG (free, but upstream engines
  rate-limit), Parallel, Exa, Firecrawl, Brave, Tavily, and built-in search
  in coding agents.
- **Harnesses**: Claude Code, Codex CLI, OpenCode, Hermes Agent. Not decided
  which will run this.

## Questions

### A. Where does the money go?

- In a typical deep research run, what share of cost is search calls, page
  reading, model input tokens, and model output tokens? Find real
  measurements, not guesses. Anthropic has said multi-agent research uses
  many times more tokens than chat. Find that number and any others like it.
- Which step burns the most tokens? (My guess is reading full pages. Is that
  right?)

### B. What makes it efficient?

Find evidence for and against each of these, and add ones I missed:

- Cheap model for reading and note taking, strong model for planning and
  writing.
- Compressing notes before the writer sees them.
- Reading only the relevant part of a page instead of the whole thing.
- Skipping repeat URLs and near-duplicate queries.
- Prompt caching (reusing the same prompt start across calls).
- Stopping early when new searches keep returning the same facts.
- One agent looping versus several sub-agents in parallel: cost versus
  quality.
- Using search snippets only for easy facts and full reads only for key
  claims.
- Asking the user one clarifying question up front to avoid wasted rounds.

### C. How does quality grow with size?

- Is there evidence of diminishing returns, for example a point where more
  searches stop improving the report? Look at benchmarks (BrowseComp,
  DeepResearch Bench, and newer 2026 ones) and papers on test-time scaling
  for search agents.
- What is the smallest run that still produces a useful cited answer?

### D. Current prices (with dates)

- Search APIs: price per 1,000 searches for Brave, Tavily, Exa, Parallel,
  Firecrawl, SerpAPI, and others you find. Note free tiers.
- Page reading / extraction APIs: price per 1,000 pages.
- Model prices per million input and output tokens for a few cheap open
  models (for example Qwen, GLM, DeepSeek, Kimi, MiniMax families) and a few
  frontier models.
- What flat-fee subscriptions (OpenCode Go, ChatGPT plans, Claude plans)
  allow for automated or agent use, and their usage caps. Note terms of
  service limits.

## What I want at the end

1. A **cost model**: a simple formula I can fill in, like
   `cost = searches x price + pages x tokens_per_page x price + ...`, with
   realistic default numbers and sources.
2. A **tier table** for Tiny, Small, Medium, Large, and XL runs. For each:
   searches, page reads, rounds, sub-questions, sub-agents, model calls,
   rough tokens, and cost range with (a) cheap open models and (b) frontier
   models. Mark which numbers come from sources and which you estimated.
3. **The 5 most important levers** for keeping cost down without hurting
   quality, ranked, with evidence.
4. **Which settings a user should be able to control**, and sensible defaults
   for each. Keep the list short. I want it simple to use.
5. **Warning signs** that a run is wasting money (for example the same query
   repeated, pages that return nothing, loops with no new facts).

## Rules for sources

- Real measurements beat estimates. Label every estimate as an estimate.
- Give dates for all prices. Link the pricing page.
- Prefer primary sources: docs, pricing pages, papers, engineering posts,
  GitHub. Community reports are fine when labeled as opinion.
- Write in plain, simple English.
