---
created_at: 2026-09-26
updated_at: 2026-09-29
model: anthropic/claude-opus-5-5
doc_type: sources
purpose: Evidence ledger for the internet deep research spec, mapping the 13 September 26 research artifact files and the September 29 search and fetch bundle, with status, summary, and when to read each.
related:
  - path: ./spec.md
    why: Current contract and entrypoint that this evidence supports.
  - path: ../research/spec.md
    why: Generic research workflow that produced these bundles.
---

> Historical decisions and evidence. For current generic web facts, use ~/agents/capabilities/web/README.md.

# Internet Deep Research Sources

## Source Hierarchy

1. **Current contract:** [spec.md](./spec.md) owns the accepted guidance. It
   wins over any single artifact.
2. **Newest bundle wins on conflicts:** the subscription compatibility bundle
   (23:15) and its root corrections supersede the two earlier bundles on
   funding routes, OpenCode v2 web search, and GPT Researcher Codex-auth status.
3. **Official docs and source code** cited inside the artifacts rank above
   forum reports, which rank above third-party reviews and search snippets.
4. **Search and fetch layers:** the four guides in this folder own the
   checked summary of the September 29 bundle. Where a guide and a bundle file
   disagree, the guide wins; it records what was checked against official docs.
5. **MCP setup (second Sept 29 pass):** [mcp-setup.md](./mcp-setup.md),
   [provider-usage.md](./provider-usage.md), and the `capabilities/mcp/`
   runbooks own the checked facts for Parallel, Exa, and Firecrawl. They win
   over the four guides and over Bundle 4 on those providers' prices, tools,
   and defaults, because they were checked against docs, source code, and
   live tool lists.
6. **All artifacts are generated evidence** from September 26 and 29, 2026, not
   verified current truth. Nothing in them was installed or run as a quality
   test. Citations and user opinions inside them carry their own dates and
   limits.

Status labels used below:

- **Current:** still the best evidence for its topic.
- **Corrected:** contains a claim later corrected; read with the noted fix.
- **Historical:** superseded recommendation or framing; keep for context and
  raw evidence only.

## Bundles

- Bundle 1: Internet deep research options (21:57) (private, not published):
  first landscape survey and trial order. **Historical.** 6 files.
- Bundle 2: Community deep research (22:49) (private, not published):
  Reddit and forum evidence plus the OpenCode v1/v2 search split.
  **Corrected** in part. 3 files.
- Bundle 3: Subscription compatibility (23:15) (private, not published):
  subscription-first compatibility verdicts with root corrections.
  **Current.** 4 files.
- Bundle 4: Web search and fetch tools (Sept 29, ChatGPT) (private, not published):
  one ChatGPT conversation (primer, four Deep Research reports, MCP answer)
  plus a hosted-provider landscape handoff with prices and a ~$15/month plan.
  **Current, mixed trust.** 8 files. Its RESEARCH.md has a per-file trust
  table and known errors. Summarized and checked in
  [search-in-harnesses.md](./search-in-harnesses.md),
  [search-services.md](./search-services.md),
  [fetch-in-harnesses.md](./fetch-in-harnesses.md),
  [fetch-services.md](./fetch-services.md), and
  [connecting-and-routing.md](./connecting-and-routing.md).
- Bundle 5: Search and fetch MCP setup (Sept 29, second pass) (private, not published):
  multi-round research on connecting Parallel, Exa, and Firecrawl as hosted
  MCP servers in Claude Code, Codex, and OpenCode v2: billing, cheapest
  settings, approval gates, OpenCode v2 config shape, a Codex adversarial
  review, and per-harness native routes including Hermes. **Current.**
  Distilled into [mcp-setup.md](./mcp-setup.md),
  [provider-usage.md](./provider-usage.md), and the runbooks.

## Generated Reference: Full File Map (13 files)

### Bundle 1: Internet deep research options (6 files)

Folder: `artifacts/investigations/26-09-26_21-57__research__internet_deep_research_options_gpt-6-sol/`

1. RESEARCH.md (private, not published)
   **Historical.** Root synthesis. Finds no community consensus and proposes
   Codex CLI first, OpenCode second, GPT Researcher third, LDR as alternate.
   Its OpenCode "native search without an API key" claim and its Codex-first
   order are superseded. Notes OpenRouter was not in the local OpenCode auth
   list. **Read when:** you need the original framing, the first cost split, or
   why DeerFlow, Open Deep Research, and Vane were set aside.
2. R01 W01 standalone landscape (private, not published)
   **Historical.** Survey of LDR, GPT Researcher, DeerFlow, Open Deep Research,
   STORM, Vane, Onyx, and long-tail tools: activity, model support, search
   cost, setup, and a comparison table. Reddit was blocked; star counts are
   approximate. **Read when:** you need per-project background or the other
   candidates' details.
3. R01 W02 agent CLIs (private, not published)
   **Corrected.** Introduces the model vs search tool vs search bill split.
   Covers Codex, OpenCode, Claude Code, OpenRouter, MCP bridges, and failure
   modes. Its "OpenCode search off by default" and "Go includes no search"
   lines are version-dependent and not current for v2. **Read when:** you need
   the three-layer cost model, third-party harness policy history, or reported
   CLI research failure modes.
4. R02 W01 community validation (private, not published)
   **Historical.** HN and GitHub issue evidence only (no Reddit). Confirms the
   Open Deep Research archive and lists GPT Researcher 2026 issues and early LDR
   complaints. **Read when:** you need dated HN or issue evidence, or the 2025
   "open clones lag the trained model" opinion.
5. R02 W02 integrations and cost (private, not published)
   **Corrected.** Official-doc check of Codex plan coverage, OpenAI terms,
   OpenCode Go terms and endpoints, OpenRouter search prices, and a tool vs
   route table. Its OpenCode no-key search claim came from v1 docs and is
   corrected by bundles 2 and 3. Budget figures are assumptions. **Read when:**
   you need OpenRouter search prices, Go terms detail, or the route-risk ranking.
6. R02 W03 Mac setup (private, not published)
   **Historical.** Mac constraints (no Docker), a four-tool comparison table,
   operational gotchas, and a staged smoke plan. Its Codex-first order, "Go has
   no search" line, and Python observation are superseded by later checks.
   **Read when:** you are designing the hands-on comparison or need setup
   gotchas such as server binding and embeddings.

### Bundle 2: Community deep research (3 files)

Folder: `artifacts/investigations/26-09-26_22-49__research__community_deep_research_gpt-6-luna/`

7. RESEARCH.md (private, not published)
   **Corrected.** Keeps "no consensus", moves LDR ahead of GPT Researcher for a
   dedicated-tool trial on community signal, and first flags that OpenCode v2
   search is separately configured and billed. Its trial order predates the
   subscription findings; its Codex-baseline advice is superseded. **Read
   when:** you need the summary of the community sample or the first v2 search
   correction.
8. R01 W01 user opinion (private, not published)
   **Current** (as community evidence). Table of 27 firsthand reports from 27
   accounts (20 Reddit, 4 HN, 3 GitHub) with dates, plus an access ledger. A
   convenience sample, not a poll. **Read when:** you need who said what about
   LDR, GPT Researcher, Codex, OpenCode, or DeerFlow.
9. R01 W02 practical compatibility (private, not published)
   **Corrected.** Resolves the OpenCode v1 vs v2 search conflict, narrows Go to
   coding-agent use, and reviews Open WebUI, Khoj, Onyx, and Vane. Its
   "start with Codex" decision card is superseded. **Read when:** you need the
   v1/v2 search explanation, Go usage-boundary wording, or snippet-vs-page
   evidence (GPT Researcher issue 1846).

### Bundle 3: Subscription compatibility (4 files)

Folder: `artifacts/investigations/26-09-26_23-15__research__subscription_compatibility_setup_claude-opus-5-5/`

10. RESEARCH.md (private, not published)
    **Current.** Root verdict: LDR and GPT Researcher do not natively use Go or
    ChatGPT/Codex logins; OpenRouter is native; OpenCode v2 with Go is the
    documented subscription route; v2 web search is separate and billed.
    Contains the root corrections. Its install commands are an untested
    adaptation, not a recipe this spec adopts. Frontmatter records the root
    model as `openai/gpt-6-sol` although the folder slug names Claude Opus 5.5.
    **Read when:** you need the authoritative compatibility verdict or the
    corrections.
11. R01 W01 LDR (private, not published)
    **Current.** LDR backend verdict table, search sources, OpenRouter setup
    routes, why its generic endpoint cannot meet Go's client guidance, and
    smoke checks. **Read when:** you need LDR provider or search details.
12. R01 W02 GPT Researcher and OpenCode (private, not published)
    **Corrected.** GPT Researcher install, OpenRouter settings, retrievers,
    CLI export; OpenCode provider login paths and headless commands. An
    in-file root correction withdraws its no-key Go web search claim, but its
    bottom line and comparison table still show the old claim. **Read when:**
    you need GPT Researcher config names or OpenCode headless commands; ignore
    its search rows.
13. R01 W03 adversarial (private, not published)
    **Current** (with its in-file correction). Route matrix for Go, Codex OAuth
    proxies, OpenAI API key, and OpenRouter; terms evidence; community proxy
    projects; written-policy and smoke-test gates. Root correction: GPT
    Researcher Codex-auth issue 1710 is closed not planned, not open. **Read
    when:** you need the policy and permission reasoning or test gates.

## External / Canonical Docs

Checked directly on September 29, 2026 for the search and fetch guides:

- Claude Code WebSearch and WebFetch behavior: https://code.claude.com/docs/en/tools-reference
- Codex `web_search` modes: https://learn.chatgpt.com/docs/config-file/config-reference
- OpenCode v2 web search providers: https://opencode.ai/v2/docs/websearch (v1 tools page https://opencode.ai/docs/tools/ still shows the old keyless env vars)
- Exa MCP and pricing: https://exa.ai/docs/reference/exa-mcp and https://exa.ai/pricing
- Parallel Search MCP and pricing: https://docs.parallel.ai/integrations/mcp/search-mcp and https://parallel.ai/pricing
- Firecrawl MCP and pricing: https://docs.firecrawl.dev/mcp-server and https://www.firecrawl.dev/pricing
- LDR MCP client removal: https://github.com/LearningCircuit/local-deep-research/pull/4567 and issue https://github.com/LearningCircuit/local-deep-research/issues/4566

Checked on September 29 (second pass) for the MCP setup, by workers using
`curl`, public GitHub source, and keyless `tools/list` calls:

- Harness MCP docs: https://code.claude.com/docs/en/mcp , https://code.claude.com/docs/en/permissions , https://developers.openai.com/codex/mcp , https://developers.openai.com/codex/config-reference , https://opencode.ai/v2/docs/mcp-servers/ , https://opencode.ai/v2/docs/permissions/
- Harness source for approval behavior: https://github.com/openai/codex (`codex-rs/core/src/mcp_tool_call.rs`, `codex-rs/codex-mcp/src/mcp/mod.rs`) and https://github.com/sst/opencode (`packages/opencode/src/cli/cmd/run.ts`)
- Provider docs: https://docs.parallel.ai/integrations/mcp/search-mcp , https://exa.ai/docs/get-started/exa-mcp , https://docs.firecrawl.dev/mcp-server/tools , and each provider's billing page
- Provider MCP source: https://github.com/exa-labs/exa-mcp-server (`api/mcp.ts`), https://github.com/firecrawl/firecrawl-mcp-server (`src/index.ts`)

Read on September 26 by workers:

Primary pages cited by the artifacts, for rechecks. Each was read on
September 26, 2026 through a worker, often via a summarizing fetcher.

- OpenCode v2 web search: https://opencode.ai/v2/docs/websearch
- OpenCode v2 Console search ($0.01 per successful search): https://opencode.ai/v2/docs/console/websearch
- OpenCode Go (v2 Console and detailed guide): https://opencode.ai/v2/docs/console/go and https://opencode.ai/docs/go
- OpenCode providers: https://opencode.ai/v2/docs/providers
- OpenCode terms: https://opencode.ai/legal/terms-of-service
- Codex web search and plan use: https://developers.openai.com/codex/web-search and https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan
- OpenAI terms: https://openai.com/policies/terms-of-use/
- OpenRouter search tool pricing: https://openrouter.ai/docs/guides/features/server-tools/web-search
- LDR providers and search engines: https://github.com/LearningCircuit/local-deep-research (see `docs/search-engines.md` and `src/local_deep_research/llm/providers/implementations/`)
- GPT Researcher LLM docs: https://docs.gptr.dev/docs/gpt-researcher/llms
- GPT Researcher Codex-auth request: https://github.com/assafelovic/gpt-researcher/issues/1710

## Related Specs

- [Generic research spec](../research/spec.md): owns how research runs are
  performed and saved. Neighbor, not a competitor.
- [Browser use spec](../browser-use/spec.md): owns signed-in browser routes,
  which may help read sites that block plain fetchers.

## Weak Claims To Avoid

From the September 29 bundle:

- "Codex has no search tool and uses ChatGPT browsing through Bing" or "Codex
  search is DuckDuckGo" (Codex has `web_search`, default `cached`).
- "Claude Code search is Bing" or "a curated index" (not published).
- "Claude Code WebFetch returns the raw page" (it returns a small model's
  answer unless you fetch another way).
- "OpenCode websearch is keyless with `OPENCODE_ENABLE_EXA=1`" (v1 only; v2
  needs a key per provider).
- "Hermes search defaults to Perplexity" (only with a Nous subscription).
- "LDR can use Exa or Parallel MCP servers" (removed June 2026).
- "Exa search costs $7 per 1,000" as the floor (Instant is $4).
- The handoff's popularity and "power" scores as measurements (made up to show
  tradeoffs; no quality test exists).

From the second September 29 pass:

- OpenCode MCP config as `"mcp": {"exa": ...}` or `"permission": {...}` (v1
  shape; the installed v2 uses `mcp.servers` and a `permissions` array).
- "Exa's MCP lets you pick the cheap search tier per call" (the default tool
  has no type knob; only the hosted `defaultSearchType` URL setting does).
- "Parallel's spend limit caps your bill" (it only emails you).
- "A keyed Parallel MCP runs `fast` by default" (undocumented; pin it).
- "Parallel's OpenCode plugin is the cheap route" (it hardcodes `advanced`, $5
  per 1,000).

From the September 26 bundles:

- "OpenCode Go includes free, no-key web search" (true only for older v1 docs;
  not established for v2).
- "Go never includes search" (also too broad; depends on version and route).
- "The GPT Researcher Codex-auth request is open" (closed not planned,
  September 26, 2026).
- "LDR or GPT Researcher can spend a Go or ChatGPT subscription" (no native
  route; only untested endpoints or unofficial proxies).
- "Codex CLI should be tried first" (superseded by the user's funding order;
  Codex is a comparison baseline).
- "OpenRouter is connected in OpenCode on this Mac" (not in the local auth list
  when checked).
- "Tool X is the best open deep research tool" (no hands-on comparison exists).
- Star counts, source counts, or vendor benchmarks as proof of report quality.
- Worker per-report cost estimates as measured costs.

## Historical / Stale Conflicts

- OpenRouter Exa search price: a May 2026 blog said $0.005 per request; the docs
  page read September 26 said $0.007. Trust the live docs.
- GPT Researcher minimum Python: one worker read "3.11 or later" in the README;
  others reported 3.12+ and CI dropping 3.11. Recheck before any install.
- OpenCode search: v1 docs describe keyless Exa or Parallel via environment
  variables; v2 docs require a key per provider. Trust v2 for the installed
  version.
- Exa search price: the September 29 handoff says $7 per 1,000; the pricing
  page read the same day also lists a $4 Instant tier.
- Codex plan coverage: an early worker could not read OpenAI's help page; a
  later bundle read it and found Codex included across plans with variable
  limits. Web search coverage per plan tier is still not fully confirmed.

## 2026-10-01: Web reference moved

Generic search and fetch facts, tool quality, ladders and current routing decisions now live in [capabilities/web](../../capabilities/web/README.md) and [its decisions](../../capabilities/web/DECISIONS.md). This file retains dated history. Earlier provider defaults and budgets are not current policy. Hermes setup and research workflow retain their own spec.
