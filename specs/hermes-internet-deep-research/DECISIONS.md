---
created_at: 2026-09-26
updated_at: 2026-09-28
model: anthropic/claude-opus-5-5
doc_type: decisions
purpose: Durable choices, rejected alternatives, and open user decisions for Hermes internet search, extraction, and deep research.
related:
  - path: ./spec.md
    why: Contract these decisions shape.
  - path: ./SOURCES.md
    why: Evidence behind each choice.
---

> Historical decisions and evidence. For current generic web facts, use ~/agents/capabilities/web/README.md.

# Hermes Internet Deep Research Decisions

Early choices were planning assumptions on September 26, 2026; the installation
and September 28 skill updates below record what was actually implemented.
Unverified billing and quality remain open, not silently authorized.

## Accepted

**D1. Separate spec from the generic internet research spec.**
This spec owns Hermes's own search, extraction, and report workflow. The
[neighbor spec](../internet-deep-research/spec.md) owns standalone research
apps and the subscription funding order. Why: different questions, different
evidence, and the user asked for a separate Hermes contract. Consequence:
funding questions about the current `openai-native` search route are answered
there, not here.

**D2. Parallel is the operational primary, not a measured reliability winner.**
The first trial and post-restart keyed tests worked; keyed Firecrawl also worked
when selected. Neither long-run success rates nor real-account unit costs have
been measured. Consequence: keep the selected Parallel route without claiming
the broader comparative bakeoff is complete.

**D3. Stage search and extraction changes separately.**
Why: the September 26 search route works only in some model routes and
extraction did not work, while the user favors local SearXNG search. Changing
both at once hides which change caused what. Consequence: preserve the
before-state, test SearXNG as search, then one reader at a time; pin both
backend keys because adding a credential can move autodetection.

**D4. An empty or tiny extract is a failure for every backend.**
Why: the installed Firecrawl adapter can return an empty success, and a single
empty entry passes as success at the tool level (Code-read). Consequence: the
workflow routes empty pages to recovery and never cites them.

**D5. Turnkey research output is leads, not evidence.**
Why: vendor excerpts are not verified quotes, and no independent comparison
exists. Consequence: any turnkey trial re-fetches and quotes the cited pages.

**D6. Community counts are convenience samples.**
Why: all samples come from help and recommendation threads, with selection
bias and overlapping users. Consequence: counts inform the test plan, never a
ranking or market-share claim.

**D7. No CODEMAP for now.**
Why: code landmarks come from one report and could not be re-read in this
session. Consequence: line references stay in [SOURCES.md](./SOURCES.md) as
Code-read claims until someone re-verifies them.

**D8. Add a thin Hermes internet deep-research skill rather than another API.**
The default profile's `hermes-internet-deep-research` skill selects a focused,
standard, or high-stakes lane and orchestrates the existing research/citation
skills. It budgets calls, maps evidence gaps and requires disconfirmation. The
owning [spec](./spec.md#current-research-procedure) has the contract; the
installed native file is at
`~/.hermes/skills/research/hermes-internet-deep-research/SKILL.md`.
This is neither Claude Code's bundled `/deep-research` nor the Agents workspace
`research-deep`. A later five-question bounded run (private, not published)
demonstrated search-to-reader-to-cited-report behavior with independent
source-support review. It did not establish superior quality to the older
skill, actual billed cost, or long-term reliability. No MCP server, turnkey
research API, or automatic vendor switching was added.

## Rejected Alternatives

| Alternative | Why rejected |
|---|---|
| Pick Firecrawl because it is the Hermes default and most popular | Popularity is not reliability; code-level empty-page risk; test it instead |
| Pick Parallel outright because it is cheapest | No community footprint and no measured reliability; test it instead |
| Use a search-only backend (OpenAI Native, Brave, SearXNG, DDGS, xAI) for extract | Hermes rejects it; that is the current failure |
| Use Perplexity as the extract backend | Returns query snippets, not page text; unfit for verbatim citations |
| Assume SearXNG also reads pages | It is search-only; the user favors testing it for search alongside a separate reader |
| Build an MCP server or change Hermes core first | Config plus a thin skill covers the need with less upkeep and no cache churn |
| Adopt LangChain `open_deep_research` | Archived August 21, 2026 |
| Adopt GPT Researcher inside Hermes | Duplicates what Hermes already does; standalone apps belong to the neighbor spec |
| Reject turnkey APIs on cost | Pro tiers list at about $0.10 per run; the real objections are quality evidence and upkeep |
| Treat stars, upvotes, or vendor benchmarks as quality | They measure attention |
| Use anti-detection browsers or CAPTCHA workarounds for research | Access-control and policy risk; not needed to fix the core failure |

## Implemented September 27, 2026

The user approved a local SearXNG instance, sending **public-page URLs only**
to hosted readers for a bounded trial, and turning off automatic outside-vendor
retries. Docker Desktop was already installed. SearXNG is running on loopback;
Hermes uses it for search and explicitly selects anonymous Parallel for page
reading. The live receipt (private, not published)
records live verification, the Firecrawl 429 and the free-tier ring's unexpected
cross-vendor retry on a public 404. In that initial anonymous trial, tier pins
restricted the ring to Parallel only. These pins were **not** paid enrollments;
no account was created by that first installation.
The reliable quota, long-run behavior and alternative model routes remain open.
**September 28 update:** the user supplied two keys by masked local handoff;
both were accepted and installed. After the user's external gateway restart,
keyed Parallel and keyed Firecrawl both worked through live Hermes extraction.
Parallel remains primary, Firecrawl manually selectable only. See the
keyed receipt (private, not published).

## Remaining Open Decisions (user owns)

**O1. Research completed; first setup implemented.** Five first-pass Claude
Code Opus 5.5/low reports were written September 27 on SearXNG, Parallel,
Firecrawl, integration, and troubleshooting. Two more used Claude Code's
native `/deep-research` workflow for a Hermes install guide and a cross-harness
guide. Read the first bundle (private, not published)
and native research bundle (private, not published)
including the audit corrections and untested caveats.
The initial public-page trial is authorized and live. Key handover was later
completed; paid enrollment still needs its own decision. The tested state and next
steps are in [spec.md, Implementation handoff after compaction](./spec.md#implementation-handoff-after-compaction).

**O2. Keyless smoke tests: historical, reliability open.** Hermes's installed Parallel provider routes
no-key extraction through a separate anonymous ring, not the ordinary
Parallel API (which returned 401 without a key in a report). The ring's
practical limits and URL destinations still need longer-run observation.
The short public-page suite worked; keyed Parallel now supersedes this route.
No private URLs are authorized.

**O3. Reader selection after the trial.** Parallel's anonymous endpoint worked
for HTML, MDN and PDF; Firecrawl's anonymous cloud endpoint initially returned
text but soon throttled. Keep Parallel as the trial primary. The user
subsequently supplied keys for both hosted readers. Parallel's keyed
route is active; Firecrawl's keyed route was tested and can be selected
manually. A local reader or paid plan needs a separate decision; account
balances and any actual free quota still need checking in vendor dashboards.

**O4. Keyless rescue: off.** The user chose predictable failures over an
automatic attempt by another vendor. Both `keyless_fallback` and
`keyless_rescue` are false. In the initial anonymous trial, this build's
explicitly free provider still walked the ring on throttling, so the other
vendors were excluded by tier pins. Keyed Parallel is now the active path.
Recheck behavior after Hermes updates. A deliberate public 404 reached
Keenable before the guard was installed; see the receipt. Since September 29, keeping
both off also enforces the cross-harness rule that Exa and Firecrawl calls
need user approval ([provider-usage](../internet-deep-research/provider-usage.md)).
Upstream issue #93782 reports the switch leaking across vendors.

**O5. Search backend: SearXNG selected.** Live JSON and gateway search tests
passed. OpenAI-native remains a possible fallback but is search-only and
cannot itself restore page reading.

**O6. SearXNG runtime and upkeep.** Existing Docker Desktop runs a pinned
arm64 SearXNG container on loopback. After the bounded smoke exposed blocked
default search engines, Google, Yahoo and Yandex were enabled and selected
as the sole SearXNG engines; direct and fresh Hermes queries returned results.
This selection is a local operational fix, not proof that anonymous upstream
scraping remains reliable over time. Short-run container memory was about
155 MiB; Docker VM overhead, battery use and maintenance remain unmeasured.

**O7. Turnkey research trial.** Recommendation: only if the research suite
fails on coverage after the thin skill.

**O8. Spending controls remain unverified; handover is complete.** Keys reached
the Hermes profile by masked local handoff without chat or shared-file exposure.
The user must inspect actual vendor credit balances, billing terms, and limits
in the dashboards before sustained use or a larger bakeoff. Parallel's
documented spending limit may only notify, not block. No paid upgrade was
enrolled by this installation; successful keyed calls can still consume credits
or incur usage under account terms.

**O9. Acceptance thresholds.** The 90% useful-text rate, the 300-character
cutoff, and the 5 of 5 and 4 of 5 suite bars are proposals. Recommendation:
keep them for the first run and adjust after seeing T3 data.

## 2026-10-01: Web reference moved

Generic search and fetch facts, tool quality, ladders and current routing decisions now live in [capabilities/web](../../capabilities/web/README.md) and [its decisions](../../capabilities/web/DECISIONS.md). This file retains dated history. Earlier provider defaults and budgets are not current policy. Hermes setup and research workflow retain their own spec.
