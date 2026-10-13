---
created_at: 2026-09-30
updated_at: 2026-09-30
model: anthropic/claude-opus-5-5
artifact_category: specs
doc_type: prompt
purpose: Copy-paste single Claude Research request that merges the three topics, for when only one expensive Claude run is affordable. Asks Claude to go deepest on prompts and budget design.
related:
  - path: ../spec.md
    why: The engine this research feeds.
  - path: ./README.md
    why: Which prompt to send to which tool, and where to save the result.
---

> Historical, 2026-10-01: This prototype is parked. It is not current policy or a build plan. Current web facts and decisions: [capabilities/web](../../../../capabilities/web/README.md) and [web decisions](../../../../capabilities/web/DECISIONS.md).

# Request 4: One combined request for Claude Research

Send to: **Claude Research**, when you only want to pay for one Claude run. If
you can afford a second Claude run, send [02-prompts.md](./02-prompts.md) as
the second one instead of repeating this.

Why a separate prompt: ChatGPT gets three focused requests. Claude gets one
that asks for the design answer directly, so its report can be compared
against ChatGPT's three and checked for disagreements.

Copy everything below the line.

---

I am building my own deep research system and I want your best research-backed
design for it. It loops: plan, search the web, read pages, check for gaps,
search again, then write a cited report. Please research how the best
existing systems do this and write a detailed report that ends in a concrete
design I can build.

## My situation

- **Already have**: web search (self-hosted SearXNG, Parallel, Exa, Firecrawl,
  Brave, and the built-in search in Claude Code, Codex CLI, and OpenCode),
  page reading (Parallel, Firecrawl, built-in fetch), and models (cheap open
  models through an OpenCode Go subscription, OpenAI through a ChatGPT plan,
  Claude through a Claude plan, OpenRouter pay-per-token).
- **Missing**: the loop design, the prompt text for each step, and a way to
  set the size of each run.
- **Must**: run in any agent tool (Claude Code, Codex, OpenCode, Hermes
  Agent); let me swap models, search providers, and tools as my
  subscriptions change; stay simple, with little to maintain.
- **Budget is the top concern.** I want to pick a size per run: tiny (under
  5 searches), small (about 10), medium (about 50), large (a few hundred), and
  know roughly what each costs and what quality to expect.

## Research these, in order of importance

1. **The prompts.** Find the real prompt text that open-source systems use for
   each step (plan, write queries, pick results, read and take notes, compress,
   check gaps and decide to stop, delegate to sub-agents, write, check
   citations). Good places: LangChain open_deep_research, GPT Researcher,
   dzhng/deep-research, Jina node-DeepResearch, STORM, LearningCircuit Local
   Deep Research, Hugging Face open_deep_research, and your own company's
   engineering post and cookbook prompts for the multi-agent research system.
   Quote the key parts and link the files. Explain which patterns matter most,
   especially how prompts tell a model how much effort to spend.
2. **Budget and cost.** Where does the money go (search, reading, input
   tokens, output tokens)? Which efficiency tricks have real evidence (cheap
   model for reading, compressing notes, dedupe, caching, early stopping,
   single loop versus parallel sub-agents)? Is there a point where more
   searches stop helping? Give current prices with dates.
3. **How the systems are built.** The stages each system uses, the size knobs
   and their defaults, stopping rules, and typical run sizes. Keep this part
   shorter than the first two.

## What I want at the end

1. A ranked list of the prompt patterns that matter most, with real quoted
   examples.
2. **Your draft prompt for each step**, model-agnostic, taking its budget as an
   input (for example `{max_queries}`, `{max_pages}`, `{rounds_left}`), so the
   same prompt works for tiny and huge runs. Say which steps a cheap model can
   handle safely.
3. A **tier table** (Tiny, Small, Medium, Large, XL): searches, page reads,
   rounds, sub-questions, sub-agents, model calls, rough tokens, and cost with
   cheap open models versus frontier models. Label estimates.
4. A simple **cost formula** I can fill in.
5. The **shortest list of settings** a user should control, with defaults.
6. **Where you disagree with common practice**, and why.

## Rules for sources

- Prefer primary sources: repos and exact source files, official docs,
  pricing pages, papers, engineering posts. Label community posts as opinion.
- Give dates for prices and prompts; both change often.
- Mark what a source says versus what you infer. Say unknown instead of
  guessing.
- Write in plain, simple English.
