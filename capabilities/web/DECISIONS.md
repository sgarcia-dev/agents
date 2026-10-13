---
created_at: 2026-10-01
updated_at: 2026-10-01
model: gpt-6.1-sol
doc_type: decisions
purpose: Record the shared web knowledge home, routing and evidence loop.
related:
  - path: ~/agents/capabilities/web/README.md
    why: Current entry points, ladders and acceptance checks.
  - path: ~/agents/capabilities/web/compatibility.jsonl
    why: Separate search and fetch category verdicts.
---

# Web decisions

## 2026-10-01: One home

~/agents/capabilities/web owns generic search and fetch facts, tool docs, ladders, verdicts and observations. Skills and native tools are entry points. Existing provider guides shrink to pointers; frozen tests and prototypes remain evidence. Hermes setup and workflow stay in its spec. Model prices, plan limits and model choices stay in ai-models. This avoids competing catalogues. The shared workspace migration is complete. Legacy fact guides are dated pointers. Each tool must check and update its native skill loaders in its own session.

## 2026-10-01: Request-only skills

Ordinary questions use the current harness's built-in search and fetch without a skill. Use web-search only on explicit request or when a task packet names it, and only with permitted tools. web-search-advanced must be explicitly named for multi-round research. Retain the quick and advanced budgets. An installed tool does not grant permission to spend or call another AI CLI. Paid services need a named request or a dated harness fallback; Exa must be named. A harness without usable native search may use its approved Parallel fallback. Quick work needs approval before a sixth Firecrawl call unless a larger budget is already approved. Another AI CLI needs user approval for that tool or chain.

## 2026-10-01: Keep two ladders

Search finds sources; fetch obtains page evidence. A service can find a social URL while refusing its body. Keep separate verdicts and acceptance checks.

Search order remains current native, Codex, a few Gemini queries, Parallel Fast, Exa Auto, then Firecrawl. The search test (private, not published) gives Exa six category wins, but at seven times Parallel Fast's observed unit cost. Use Exa earlier among permitted paid tools when precise official docs, current news, contacts or board targeting are missing. Use Firecrawl earlier for community breadth. Gemini's signed-in addendum supersedes its earlier untested rows, but its final-order scores are provisional and it won no category. Skip its optional second view when you need a precise source. No global reorder is justified.

Exact fetch order remains HTTP, throwaway headless Chrome, Parallel full content, then Firecrawl markdown plus links. Native fetch remains the quick-summary default. Skip HTTP when a known shell or block already establishes the need to render. Bulk Chrome reads use the VPN. The older remote-first suggestion reduced local traffic in one sample; it did not prove a fresh remote-only route and does not replace the brief's order.

## 2026-10-01: Codex and Claude are never exact page text

Their native answers are summaries, selected extracts or refusals. In the larger fetch comparison (private, not published), Codex ordinary text was usable on two of 26 pages and presented an expired posting as active. Claude ordinary text was usable on one; its requested full-text answer sometimes changed a printed value. Exact values come only from copied HTTP, DOM, Parallel or Firecrawl evidence after comparing the source characters. Gemini and Exa remain side readers: their apparently complete output does not prove its links, IDs or wording are exact.

## 2026-10-01: Firecrawl stays the accuracy last resort

Firecrawl had 22 usable pages of 26, the strongest larger-sample completeness count. Keep markdown and links together: one team page's link-only values were wholly absent from markdown and wholly present in links. Request maxAge 0 when currentness matters, then inspect metadata and source dates. The public extension supplied no cache dates, so that request alone did not prove freshness. Firecrawl is not a universal reader: it refused Reddit, returned a Bluesky shell, and charged 30 credits for X. Ordinary pages still reported one credit. About ten requests per minute was an account observation, not a universal rate limit.

## 2026-10-01: Improve verdicts through generic observations

Keep 200 compatibility combinations, including untested cells, and 103 generic test seed observations. Each seed is one aggregated tool, operation and category result, not an independent page run. observe.mjs appends validated observations. rollup.mjs reports all-time and recent counts and flags three or more outcomes that disagree with a verdict. It also flags new evidence for untested rows. It never rewrites verdicts. A person or agent checks host mix, freshness and repeated runs, updates the JSONL deliberately, then runs render.mjs. Keep private raw evidence out of the shared repo. The pipeline export contract uses only generic fields; its connection to external exporters remains unverified in these inputs.

## 2026-10-01: Keep uncertainty and dates visible

Category wins are sample judgments, not universal guarantees. Gemini's search addendum has weaker URL provenance than the native event captures. Full-text prompts favor some fetch answers compared with ordinary pipeline text. Task completeness is separate from byte identity, pagination and freshness. Historical reach remains dated when a new thread behaves differently. Missing numeric plan allowances, missing cache metadata and unverified source claims remain unverified.

## 2026-10-01: Retire duplicate references

Both web skills are request-only. The quick description says it runs only on explicit user request or when a task packet names it, and never replaces built-in search. Both skills retain discovery keys and set disable-model-invocation: true plus metadata.opencode/autoinvoke: false. Canonical routing, adapters, CLI and research procedures point here. MCP docs retain setup; the two specs retain app funding, Hermes setup and history. Older source guides are dated pointers after their unique facts were checked or moved here. Historical prototypes remain parked.

Native files were not inspected or changed by this shared-doc migration. Each harness must apply and verify its own loader metadata. The paid-provider gates remain unchanged: this consolidation authorizes a document migration, not a new spend policy.

## 2026-10-01: Keep older proposals as history

The September proposal used Parallel Fast, then Advanced, Exa for meaning-based discovery and Brave for an independent index. It proposed Parallel Extract, Firecrawl, then specialist unblockers or browsers for reading. The current ladders replace that proposal. Its budget was $0 in fixed subscriptions, a proposed $10 to $15 Parallel spend cap above a $5 monthly grant, and Exa and Firecrawl inside their free grants. At the stated rates, $20 would buy about 20,000 Fast searches or 5,000 rounds of one search and three reads. This was arithmetic, not approved spend or measured use. A Parallel spend limit only sends email, so that proposed cap was not a hard stop.

The proposed comparison used ten to twenty questions of each kind: fresh facts, niche technical sources, meaning-based search, complete lists, articles, long pages, tables, JavaScript, PDFs and blocked pages. It called for success, accuracy, relevance, coverage, time, service cost, output size, model use, retries, browser use and honest failure reporting. The Oct 1 tests now supply search and fetch evidence, but do not measure every candidate or a complete research workflow. Popularity rankings and invented scorecards in older reports are not quality evidence.

## 2026-10-01: Preserve the simple advanced design

The September 30 decision retired an eight-phase helper program because it was too complex to maintain. Advanced search remains one instruction-only skill, without helper code, a config file or a staged build. Git history at 93258d64 retains phase 1. The parked prototype remains evidence; only the user decides whether to rebuild it, and any replacement must be simpler. Instructions do not enforce hard caps, so visible counts and one saved report remain required.

The old design allowed explicitly requested provider and model experiments, including Codex Luna, Claude Sonnet and an OpenCode Go reader using DeepSeek or Muse Spark. Those dated model examples are not current model selections. The current IDs and effort settings live in ai-models. Each requested provider gets its applicable budget, and the main agent must check helper leads against source pages. This does not change native-first defaults or the rule against silent hand-offs.
