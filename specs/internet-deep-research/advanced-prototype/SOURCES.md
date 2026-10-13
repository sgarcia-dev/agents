---
created_at: 2026-09-30
updated_at: 2026-09-30
model: anthropic/claude-opus-5-5
doc_type: sources
purpose: Evidence ledger for the internet deep research engine spec. Every outside report with a summary, trust level, and known errors; the verification runs; canonical docs checked; and claims to avoid.
related:
  - path: ./spec.md
    why: The spec this evidence supports.
  - path: ./DECISIONS.md
    why: Choices made from this evidence.
---

> Historical, 2026-10-01: This prototype is parked. It is not current policy or a build plan. Current web facts and decisions: [capabilities/web](../../../capabilities/web/README.md) and [web decisions](../../../capabilities/web/DECISIONS.md).

# Sources

All paths below are in the research bundle
`artifacts/investigations/26-09-30_13-24__research__deep_research_engine_scan_claude-opus-5-5/`
(the folder kept its original name when the spec was renamed).

## Bundles

- Engine research bundle (private, not published):
  one index for everything below. Three rounds: R01 small first scans (four
  workers, built-in search only), R02 structured extractions of the outside
  reports, R03 web verification of the claims that drive decisions.

## Outside reports (filed verbatim in `external/`)

Each report body is unedited; frontmatter was added. Their known errors are
listed here, not in the files.

| Report | Answers | Best for | Trust | Known errors and gaps |
|---|---|---|---|---|
| ChatGPT 1: under the hood (private, not published) | Request 1 | Exact defaults for LDR, GPT Researcher, LangChain, STORM, dzhng, Jina, smolagents, NVIDIA AI-Q, Perplexity, Gemini; the four stores; counters; failure modes at 200+ searches | High on code facts (spot-checked, all confirmed) | All 75 citation markers are broken ChatGPT export placeholders, so claims carry no URLs; its size profiles skip medium and set reads at 2x searches |
| ChatGPT 2: prompts (private, not published) | Request 2 | Real prompt excerpts per stage, effort-scaling rules, failure patterns, cheap-model routing table | Medium: quotes checked where we could; routing is its own opinion | 37 broken citation markers; its prompt-pack ZIP links point to a sandbox that cannot be opened (the Markdown pack was saved separately) |
| ChatGPT 2: prompt pack (private, not published) | Request 2 | Ten stage prompts, shared contract, controller duties, data contract, calibration list | Design proposal, untested | Long for per-page cheap calls; does not say which model runs the audit |
| ChatGPT 3: cost and scale (private, not published) | Request 3 | Two-limit budget, cost formula with per-call overhead, vendor price tables, subscription rules, warning signs, receipt fields | High on prices (vendor pages, re-verified); arithmetic rechecked and correct | 44 broken citation markers; Willison's "60% output / 89% reasoning" run was not re-verified |
| Claude 4: combined (private, not published) | Request 4 | Anthropic and LangChain prompt quotes, P1-P11 prompts, `drtool` helper idea, verification-over-search evidence, where it disagrees with common practice | High on quotes (21 of 22 confirmed); low on model prices (third-party trackers) | OpenCode Go "$12/$30/$60" is one model's limits, not the plan's; Jina effort budgets wrong (actual 100K/500K/1M); "better model beats double budget" is only shown for Sonnet 4 vs Sonnet 3.7; sub-agent counts disagree internally (10-30 in the table, cap 5 in the advice) |
| Hermes 5: self-report (private, not published) | Request 5 | What Hermes enforces in code versus only instructs; the citation checker's real limits (with a test); reusable pieces; a four-operation interface | High: read from its own files at commit `7968c72a`; five named paths confirmed to exist | Did not name the model that wrote it; it is a self-audit, not an outside check |

## Worker extractions (R02, read-only, no web)

One per report, comparing it line by line with draft v0:
W01 (private, not published),
W02 (private, not published),
W03 prompt merge (private, not published),
W04 (private, not published),
W05 (private, not published),
W06 Hermes drift (private, not published).
The root read all six outside reports itself as well; worker claims were
checked against them.

## Verification runs (R03, built-in web search only)

Codex runs had Parallel, Exa, and Firecrawl switched off for the run; Claude
runs were told to use only WebSearch and WebFetch. Event logs were checked.

| Run | Checked | Result |
|---|---|---|
| V01 Codex (private, not published) | OpenAI, Anthropic, OpenRouter, DeepSeek prices; OpenCode Go limits and terms | All prices confirmed on vendor pages; Go limits are per model; OpenCode terms of service restrict programmatic extraction |
| V02 Codex (private, not published) | Brave, Exa, Parallel, Tavily, Firecrawl, Serper, SerpAPI, Jina, built-in search tools | Confirmed; Firecrawl stealth no longer costs extra; Parallel does offer $5 a month free; Jina's dollar rate only on third-party pages |
| V03 Codex (private, not published) | LDR, NVIDIA AI-Q, LangChain, Jina, Perplexity, Gemini facts | Confirmed; no native LDR Mac app; Jina effort budgets corrected |
| V04 Sonnet (private, not published) | OpenCode Go, ChatGPT, Claude plan limits and terms | Confirmed; second opinion on Go terms ("should", no explicit ban) |
| V05 Sonnet (private, not published) | Anthropic post and cookbook prompts, LangChain prompts, context editing | 21 of 22 confirmed; one scope correction |
| V06 Sonnet (private, not published) | FS-Researcher, Asymmetric Verification, BrowseComp-Plus, W&D, DeepResearch Bench II, smolagents | Confirmed, with two wording corrections |

## Related Specs

- [internet-deep-research](../spec.md): providers,
  prices, funding order, source quality rules. Trusted current; its OpenCode
  Go and Parallel notes were updated from this work.
- [hermes-internet-deep-research](../../hermes-internet-deep-research/spec.md):
  Hermes's live research setup. Partly stale: the September 30 self-audit
  found about a dozen drifts, recorded in that spec's dated note.
- [research](../../research/spec.md): artifact and round rules.

## External / Canonical Docs (checked September 30, 2026)

- Anthropic, "How we built our multi-agent research system", published June
  13, 2025: 4x and 15x token use, 90.2% gain, 80% and 95% of BrowseComp
  variance, "start with short, broad queries", "about 20 queries".
- Anthropic cookbook prompts `research_lead_agent.md`, `research_subagent.md`,
  `citations_agent.md` (github.com/anthropics/claude-cookbooks,
  `patterns/agents/prompts/`).
- Anthropic context management post, September 29, 2025: 84% token cut in a
  100-turn web search evaluation.
- LangChain open_deep_research: `prompts.py`, `configuration.py`, README
  benchmark table; repository archived August 21, 2026.
- Jina node-DeepResearch: `src/agent.ts` (1M default, 85% regular budget),
  `src/app.ts` (effort mapping).
- LDR `docs/CONFIGURATION.md` and `langgraph_agent_strategy.py`; release
  1.10.7, August 28, 2026.
- NVIDIA AI-Q `resource_limits.py` on the `develop` branch.
- Google Gemini Deep Research API docs, updated September 23, 2026.
- Perplexity Agent API presets; Sonar retirement announcement (September 27,
  2026).
- Papers: FS-Researcher (arXiv 2602.01566, ACL 2026); Asymmetric
  Verification (arXiv 2510.06135, ICLR 2026); BrowseComp-Plus (arXiv
  2508.06600); W&D (arXiv 2602.07359); Agentic Search in the Wild (arXiv
  2601.17617, SIGIR 2026).
- Vendor price and plan pages: developers.openai.com pricing, claude.com
  pricing, openrouter.ai model pages, api-docs.deepseek.com pricing,
  opencode.ai/docs/go (updated September 29, 2026), opencode.ai terms
  (effective August 15, 2026), learn.chatgpt.com pricing,
  code.claude.com authentication and legal pages, and each search vendor's
  pricing page.

## Weak Claims To Avoid

- **Every per-tier token count and cost is an estimate.** Nothing here was
  measured on our runs.
- **"Better model beats doubling the budget"** is only shown for Sonnet 4
  versus Sonnet 3.7 (Anthropic post). Do not state it as a general rule.
- **Asymmetric Verification:** keep "about 370 extra calls versus about 77"
  for Kimi K2 but not the "about 18%" endpoint (not found). For Qwen3-2507,
  it is tool use that barely grows from a 15 to 50 quota, and accuracy can
  drop; not "marginal gains".
- **The W&D paper's Salesforce affiliation** was not on its arXiv page.
- **DeepResearch Bench II ranks** (AI-Q 54.50 and Hermes Agent 51.88, two of
  only three open entries) come from one leaderboard page with no date. Do not confuse closed "Hermes Ultra" (55.64) with open "Hermes Agent".
- **ChatGPT Pro $200 grandfathering until October 29, 2026** rests on a news
  article and search snippets, not an official page.
- **Jina Reader's dollar rate** (about $0.05 per million tokens) is from
  third-party pages only.
- **OpenCode Go's terms for batch use** are read differently by the two
  verifiers. Treat heavy batch use as a risk, not as allowed or banned.
- **Willison's run (60% output cost, 89% reasoning tokens)** came from the
  ChatGPT cost report and was not re-checked.
- **Codex workers self-report their model as "gpt-5"** even when pinned;
  trust the launch flags, not the self-report.

## Historical / Stale

- Draft v0 of this spec (spec, tiers, prompts, config, decisions) is in git
  history at commit `4252131a` under the old folder name
  `specs/deep-research-engine/`.
- The R01 scans' secondary-source prices (Brave, Tavily, Serper, DeepSeek) are
  superseded by the R03 vendor-page checks.
