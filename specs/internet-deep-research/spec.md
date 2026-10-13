---
created_at: 2026-09-26
updated_at: 2026-10-01
model: anthropic/claude-opus-5-5
doc_type: spec
purpose: One public-internet research spec for search and fetch tools and providers, the simple explicit-only web-search-advanced skill design, and the parked Internet Deep Research Advanced Prototype. Keeps provider setup, funding, and source-quality reference.
related:
  - path: ~/agents/capabilities/web/DECISIONS.md
    why: Simple explicit-only skill design.
  - path: ~/agents/specs/internet-deep-research/advanced-prototype/spec.md
    why: Parked bigger design and retained research.
  - path: ~/agents/specs/internet-deep-research/DECISIONS.md
    why: User choices and reasons for simplifying.
  - path: ~/agents/specs/internet-deep-research/SOURCES.md
    why: Evidence ledger for the September 26 bundles and the September 29 search and fetch bundle.
  - path: ~/agents/capabilities/web/README.md
    why: Built-in web search in Claude Code, Codex, OpenCode, Hermes, and LDR.
  - path: ~/agents/capabilities/web/README.md
    why: Outside search services (Parallel, Exa, Brave, Tavily, SearXNG, others) with prices.
  - path: ~/agents/capabilities/web/README.md
    why: Built-in page reading in the same five harnesses.
  - path: ~/agents/capabilities/web/README.md
    why: Outside page readers, crawlers, and browsers with prices.
  - path: ~/agents/capabilities/web/README.md
    why: MCP portability, turning built-ins off, routing, the ~$15/month plan, and the bakeoff.
  - path: ~/agents/capabilities/web/tools/parallel.md
    why: Install-ready MCP config for Parallel, Exa, and Firecrawl in Claude Code, Codex, and OpenCode v2.
  - path: ~/agents/capabilities/web/README.md
    why: Which provider agents use, escalation, costs, and wrong-tool signs.
  - path: ~/agents/capabilities/web/README.md
    why: Finding and reading Reddit, X, and Bluesky posts and replies, tested across harnesses.
  - path: ~/agents/specs/hermes-internet-deep-research/spec.md
    why: Hermes-specific search and reader setup that is live on this Mac.
  - path: ~/agents/specs/research/spec.md
    why: Neighbor spec for the generic research workflow (artifacts, rounds, progress modes); not replaced by this spec.
---

# Internet Deep Research Spec

This spec retains standalone public-web research apps, funding choices and historical evidence. Generic search and fetch facts now have one home: [capabilities/web](../../capabilities/web/README.md). The larger prototype is parked, not an active build plan. Rebuild only on user request.

## Start Here

- Current web facts, ladders and compatibility: [web reference](../../capabilities/web/README.md).
- Current web decisions: [web decisions](../../capabilities/web/DECISIONS.md).
- Advanced procedure: [request-only skill](../../skills/web-search-advanced/SKILL.md).
- App funding: [three separate bills](#three-separate-bills-model-search-and-report-workflow) below.
- History: [decisions](DECISIONS.md), [sources](SOURCES.md) and [parked prototype](advanced-prototype/spec.md).
- Hermes setup and workflow: [Hermes spec](../hermes-internet-deep-research/spec.md).

## Scope

In scope:

- The explicit-only `web-search-advanced` skill design and retained advanced
  prototype. The skill's procedure is separate from the generic research workflow.
- The two building blocks under any web research: **search** (find pages) and
  **fetch** (read a known page), whether built into a harness or bought as a
  hosted or self-hosted service.
- Tools that search the public web, read pages, and write a cited report or
  answer: standalone report apps, agent CLIs used for research, and nearby
  self-hosted search products.
- How each tool can be paid for, with the user's subscription priorities.
- Rules for judging sources and verifying a finished report.
- What is still unknown and when this spec must be rechecked.

Non-goals:

- The generic research workflow (rounds, workers, artifacts, progress modes).
  That lives in [../research/spec.md](../research/spec.md).
- Research over private company data or internal documents as the main job.
- Branded hosted products (ChatGPT Deep Research, Claude Research) except as the
  quality bar other tools are compared against.
- Installation steps, tool-native config, or credential handling. Any install
  is a separate, explicitly authorized task.
- Browser automation. Signed-in browser routes are owned by
  [../browser-use/spec.md](../browser-use/spec.md).

## Folder map

The old search, fetch, provider, setup and social guide paths are dated compatibility pointers. Use [capabilities/web](../../capabilities/web/README.md) for facts. DECISIONS.md and SOURCES.md retain history. advanced-prototype is historical.

## Search and fetch: the two building blocks

Moved to [the web reference](../../capabilities/web/README.md). It owns native defaults, the two ladders, tool costs and acceptance checks. Older native-plus-Parallel defaults, automatic skill loading and keyless Firecrawl availability claims are superseded.

## Funding priorities

The user wants to reuse subscriptions they already pay for, and dislikes vendor
lock-in. The order is:

1. **OpenCode Go** ($10/month subscription for open models).
2. **ChatGPT / Codex** subscription.
3. **OpenRouter** (pay per token), only when the first two cannot do the job.

A route that meets these priorities only through an unofficial bridge does not
count as meeting them.

## Three separate bills: model, search, and report workflow

Most confusion comes from mixing these up. A login for one does **not** give
you the others.

| Layer | Question it answers | Examples |
|---|---|---|
| Model access | Who pays for the model's tokens? | OpenCode Go, ChatGPT plan, OpenAI API key, OpenRouter credits, a local model |
| Search and fetch tool | Can the model search the web and read pages in this tool? | Codex `web_search`, OpenCode `websearch`/`webfetch`, a retriever setting in LDR or GPT Researcher |
| Search provider bill | Who pays for the search backend? | Included in a plan, Exa/Parallel/Tavily/Firecrawl/Brave per request, OpenRouter search per request, self-hosted SearXNG, DuckDuckGo |
| Report workflow | Who plans sub-questions, gathers sources, and writes the report? | A dedicated app (LDR, GPT Researcher) or a prompt you write for an agent CLI |

Rules that follow:

- **A ChatGPT sign-in is not an OpenAI API key.** Subscription use and API
  platform billing are separate. An API key is billed per use and does not draw
  on the ChatGPT plan.
- **An OpenRouter model does not switch on OpenRouter's search tool** inside
  another app. OpenRouter search is a separate, per-request priced server tool.
- **Standalone report apps may also need an embedding model**, which can be a
  third provider and a third key. Test it separately.
- **Cost per report is unmeasured.** Worker estimates (a few cents to a few
  dollars per report on OpenRouter) are assumptions, not measurements. Vendor
  example costs do not predict your prompts.

## Choosing a tool by funding route and desired experience

"Documented native" means the tool's own docs or code support it. "Plausible,
untested" means a generic OpenAI-compatible endpoint might technically work but
nobody has shown it working and the provider may not allow it. "Unofficial"
means a community proxy or token bridge.

| Funding route | OpenCode v2 | LDR | GPT Researcher | Codex CLI |
|---|---|---|---|---|
| OpenCode Go | **Documented native** model provider | Plausible, untested, policy-sensitive | Plausible, untested, policy-sensitive | Not applicable |
| ChatGPT / Codex plan | Offered by OpenCode docs; not retested on the installed v2 | **Not supported**; only unofficial proxies | **Not supported**; feature request closed not planned | **Documented native** |
| OpenRouter | Documented (API key) | **Documented native** provider | **Documented native** configuration | Not a primary route |
| OpenAI API key (not the plan) | Documented | Documented native | Documented native | Documented (usage billing) |

Pick by the experience you want:

- **You want to stay on subscriptions (Go first):** use **OpenCode v2 with Go**
  and build a cited-research prompt around it. This is the only documented way
  to spend Go on research without a bridge. The cost is that OpenCode is a
  coding agent, not a report app: you supply the research brief, the source
  checks, and the output file. Web search must be set up and paid for
  separately (see below).
- **You want a finished-report app with a web UI:** LDR or GPT Researcher, paid
  through **OpenRouter** (or a local model). This accepts the third funding
  priority. Neither app naturally uses Go or a ChatGPT login.
- **You want local or private runs, or academic sources:** LDR has the widest
  documented model list (including local models) and built-in academic sources.
  Local models on this class of Mac are the privacy option, not the quality
  option.
- **You want a baseline to compare against:** Codex CLI on the ChatGPT plan has
  model and web search inside one plan. Use it as the **comparison control** in
  a hands-on test, not as the default recommendation. It ties research to one
  vendor, and users report mixed depth.
- **You mainly want quick cited answers, not long reports:** a search-and-answer
  product (Vane, Open WebUI agentic search) fits better. Do not judge one kind of
  tool by the other kind's job.

Lock-in note: OpenCode, LDR, and GPT Researcher can each switch model providers.
Codex CLI and the Codex-backed DeerFlow route depend on OpenAI's plan and terms.

## Providers and products

### OpenCode v2 (priority route for Go)

For native web tools read [OpenCode web capability](../../capabilities/web/tools/opencode.md). For Go funding and current model choices read [ai-models](../../ai-models/README.md) and [delegation briefing](../../ai-models/delegation-briefing.md). Standalone app compatibility remains in the funding sections above.

### Local Deep Research (LDR)

- Dedicated report app with a browser UI (default port 5000), REST API, and MCP
  server. Per-user encrypted databases.
- Documented native: OpenRouter provider, OpenAI API key, local models (Ollama
  and similar), and a generic OpenAI-compatible endpoint.
- **No native Go connector and no ChatGPT/Codex login.** Its generic endpoint
  exposes only URL, key, and streaming usage. It cannot send the header and user
  agent Go asks for. Some Go models use the Responses protocol rather than Chat
  Completions, and another project's attempt to use Go as a drop-in endpoint hit
  tool-schema errors.
- Search options include DuckDuckGo (no key, strict rate limits), SearXNG
  (needs a running instance; public instances get banned), Wikipedia, arXiv,
  PubMed, Semantic Scholar, GitHub, Wayback Machine, local documents, and paid
  Tavily, Brave, and Google routes.
- It can serve other agents as an MCP server, but since June 2026 it can no
  longer **use** outside MCP servers such as Exa or Parallel (PR #4567; issue
  #4566 to restore it is open, checked September 29).
- Community signal (small convenience sample): the most repeat-use reports of
  any dedicated tool, described as good after tuning, with shallow defaults,
  memory problems, rate limits, instability, and no resume after a failed call.
  Very frequent releases. Benchmark numbers are project claims.
- **Checked September 30, 2026** (V03 (private, not published)):
  no official native macOS app; install is pip or Docker, with the web UI on
  port 5000. Latest release 1.10.7 (August 28, 2026). The default strategy is
  now `langgraph-agent`, and that strategy resets any iteration limit below 10
  to 50, so a small "3 iterations" setting does not make a small run.
  `search.snippets_only` still defaults to true; the ChatGPT internals report
  says it is documented differently for pipeline strategies and agents (not
  re-verified).

### GPT Researcher

- Dedicated report app with planner, executor, and writer steps; web UI and a
  CLI that writes Markdown, PDF, and DOCX reports.
- Documented native: API-key routes including OpenRouter (`OPENROUTER_API_KEY`,
  `OPENAI_BASE_URL`, model settings). Example model IDs in its docs are old.
  The embedding model is a separate setting and may need another provider.
- **No subscription login.** A Codex-auth feature request was **closed as not
  planned on September 26, 2026**. The maintainer said the project uses provider
  API keys and does not want to build on a consumer CLI login.
- Default search is Tavily (key needed). DuckDuckGo, arXiv, and SearXNG are
  no-key options.
- Community signal: praised as solid and easy by some users; 2026 issues report
  hangs with no logs, an empty deep-mode writing context, a broken release, and a
  bug where search snippets were counted as fetched sources.

### Codex CLI (comparison baseline only)

For web tools read [Codex web capability](../../capabilities/web/tools/codex.md). Subscription funding remains in [ai-models](../../ai-models/README.md). Current model and effort choices stay in the delegation briefing.

### Other researched candidates

- **DeerFlow 2.x:** now a general agent platform, not a focused researcher;
  heavy setup; can drift into writing code. Its Codex CLI provider reads Codex
  auth material. That is a vendor claim and a terms gray area.
- **LangChain Open Deep Research:** archived by its owner on August 21, 2026.
  Reference design only.
- **STORM:** quiet since early 2025. Sources disagree on whether it writes full
  reports or outlines.
- **Vane (formerly Perplexica):** self-hosted cited answers, not long reports.
- **Onyx, Khoj:** centered on workplace data or personal notes plus web search.
- **Open WebUI agentic search:** a local-model chat UI that can fetch full pages;
  not shown to be a better report writer.
- **DIY SearXNG plus page fetcher:** common among local users; more assembly,
  less install surface.
- **Claude Code:** Claude subscriptions may not be used in outside tools, and
  Claude is not in the user's funding order.
- **Deep-research MCP bridges and community skills:** API-billed or single
  anecdotes; not evaluated.

### Unofficial bridges (not a funding route)

Community proxies that turn a Codex/ChatGPT OAuth login into an OpenAI-style
API exist and may work. They are unsupported by OpenAI, can break on token or
backend changes, and sit against terms that forbid programmatic extraction,
bypassing limits, and credential sharing. A Go proxy that adds the requested
headers would be custom work with the same policy question. Never share, pool,
or paste subscription tokens into another app. If Go is ever used from a
standalone app, get a written answer from OpenCode first.

## Data-source types

See [the web compatibility list](../../capabilities/web/compatibility.md) for separate search and fetch categories. Local files and private account connectors are outside the public-web catalogue.

## Source quality and verification rules

Use [the web acceptance and evidence rules](../../capabilities/web/README.md). Standalone reports must still be checked against source pages. Fluent report text is not proof of support.

## Tradeoffs

- **Subscription reuse vs report polish:** Go and ChatGPT funding work in agent
  CLIs, not in the dedicated report apps. A polished report app means paying
  per token.
- **Flexibility vs lock-in:** OpenCode and the open report apps switch
  providers; Codex is simplest but ties research to one vendor.
- **Free search vs reliability:** DuckDuckGo and public SearXNG cost nothing but
  rate-limit or get banned; paid search adds a bill.
- **Local privacy vs quality:** local models keep data home but are slower and
  weaker at citation discipline.
- **Fast-moving projects vs stability:** LDR and DeerFlow ship often; pin
  versions for any trial.

## Current state

2026-10-01: No standalone report app installation is established by the supplied evidence. September app comparisons remain proposals. October search and fetch tests now exist in [the web reference](../../capabilities/web/README.md); the old no-bakeoff claim is superseded. Dated keyed MCP tests completed for Claude Code, OpenCode and Codex. Current connection state belongs to each adapter. Hermes setup and workflow stay in its own spec. This consolidation changed shared documentation only.

## Unresolved tests

Standalone app comparisons, subscription consumption during long reports, and Go policy for external clients remain unverified. The October tests compare discovery and page reading, not complete standalone report workflows. Provider quality, freshness and pricing checks now belong to [capabilities/web](../../capabilities/web/README.md). Each adapter owns its own native verification.

## Freshness and recheck triggers

Recheck the affected section, and add a new dated artifact, when any of these
happen:

- OpenCode ships a new major version, or changes its web search, provider, or
  Go docs or terms.
- OpenAI changes Codex pricing, plan coverage, web search, or terms on
  third-party harnesses.
- GPT Researcher or LDR adds a subscription login or a Go connector, or the
  GPT Researcher Codex-auth request is reopened.
- OpenRouter changes model or search pricing.
- Parallel, Exa, Firecrawl, Brave, or Tavily change prices, free credits, or
  their MCP servers; or Claude Code, Codex, or OpenCode change their built-in
  search or fetch tools.
- LDR restores outside MCP support (issue #4566).
- A listed project is archived, revived, or renamed.
- A hands-on test in this spec completes.
- Before any install or budget decision if this spec's evidence is more than
  about 30 days old.

## Retained standalone-app web details, 2026-09-29

Local Deep Research uses its own configured search-engine list and feeds an internal report pipeline. It is not a callable search or fetch tool. Outside MCP support was removed in June 2026. Its internal reader was reported to run locally without JavaScript; that claim was unverified. These app-specific facts stay here. Generic web quality, prices and routing belong to [capabilities/web](../../capabilities/web/README.md).
