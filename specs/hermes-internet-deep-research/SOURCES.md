---
created_at: 2026-09-26
updated_at: 2026-09-28
model: anthropic/claude-opus-5-5
doc_type: sources
purpose: Evidence ledger for the Hermes internet deep research spec. Traces all 30 files from the September 26, 2026 Hermes research run with status, provenance audit, dedupe notes, and reading guidance.
related:
  - path: ./spec.md
    why: Current contract this evidence supports.
  - path: ./DECISIONS.md
    why: Choices and open decisions drawn from this evidence.
  - path: ../internet-deep-research/SOURCES.md
    why: Neighbor evidence ledger for standalone research apps and funding; separate source set.
---

> Historical decisions and evidence. For current generic web facts, use ~/agents/capabilities/web/README.md.

# Hermes Internet Deep Research Sources

## Verification / Runbooks

- September 28 five-question research suite (private, not published)
  is the current bounded end-to-end functional receipt: 20 searches, 22
  distinct public-page reads, a single combined report with a durable
  citation ledger (private, not published),
  a clean citation check and 5/5 independent source-support judgments. This
  does not verify paid-account balances, T4/T5 baseline superiority or
  sustained upstream-engine reliability.
- September 28 SearXNG engine recovery (private, not published)
  supersedes the smoke test's live blocked-search status: default upstream
  engines were rate-limited or challenged; Google/Yahoo/Yandex were enabled
  and verified through both direct SearXNG and fresh Hermes searches. Old
  identical queries remained temporarily cached as empty in Hermes.
- September 28 bounded research smoke test (private, not published)
  documents the earlier partial result: keyed page reading and citation
  verification worked, while the then-enabled SearXNG engines were blocked.
  Do not present this as a successful five-question deep-research evaluation.
- Installed Hermes deep-research procedure
  is a Hermes-profile **runtime skill**, not a standalone source bundle or a
  Claude Code workflow. Created and loaded through Hermes on September 28;
  describes three effort lanes, public-URL boundaries, source verification and
  call budgets. The owning [spec](./spec.md#current-research-procedure) is the
  durable behavioral contract; a complete research-quality suite is untested.
- September 28 keyed Parallel and Firecrawl gateway test (private, not published)
  is the current installation state: keys tested and privately installed,
  provider SDKs loaded after an external gateway restart, both readers tested
  through live gateway calls, keyed Parallel selected, and billing limits still
  unverified. Supersedes the prior receipt's anonymous-reader status.
- September 27 live SearXNG and reader installation receipt (private, not published)
  records the actual Mac, gateway and CLI tests, selected settings, measured
  short-run resource use, a public-URL cross-vendor retry found during testing,
  its routing guard, and the still-open reliability/account decisions. It
  supersedes the research bundles **as installation evidence**, not as the
  explanation of vendor capabilities.

## Bundles

- September 30 Hermes self-audit (private, not published)
  (current, highest-trust description of what the installed research code
  enforces, at commit `7968c72a`). Written by Hermes from its own files, no
  web; includes an in-memory test showing `verify` passes a false claim.
  Filed in the internet deep research engine bundle; drift against this spec
  is in W06, section 7 (private, not published).
  Self-audit: the model that wrote it is not named, and only file existence
  was independently confirmed.
- September 27 native deep-research installation index (private, not published)
  (current research guide, **not** a verified install). Two new reports actually
  used Claude Code's bundled `/deep-research` Workflow: Hermes integration and
  OpenCode/Codex/Claude Code integration. Read the index's audit notes and the
  reports' separately attributed editorial gap checks; two attempted follow-up
  Workflow calls hit a Claude session limit and did not complete.
- September 27 search and reader research index (private, not published)
  (current as a research handoff, not installation proof). Five Claude Code
  Opus 5.5/low reports: SearXNG, Parallel, Firecrawl, combined integration,
  and troubleshooting. The index lists them in reading order, explains
  corrections made during audit, and records unmeasured Mac and price questions.
  Read it before deciding on a live install or reusing the reports' proposed
  commands. This bundle is additional to, not part of, the 30-file September 26
  inventory below.

## September 26 source ledger

All source files live **outside this repository**, in one local folder that is
read-only for this spec:
~/.hermes/research/internet-deep-research-2026-09-26/.
These local files are not published.

## Source Hierarchy

When sources conflict, trust in this order:

1. **This spec** ([spec.md](./spec.md)) owns accepted guidance.
2. **Measured local facts:** the baseline failure and the commit check. Dated;
   recheck before use.
3. **Installed Hermes code and local docs,** as read by Claude 03 and 04 at
   commit `ffa40b07f0`. Read, not executed.
4. **Vendor docs** read September 26 (prices, limits, API shape). Current for
   that date only; not quality evidence.
5. **First-person community reports** from the three Codex reports and Claude
   02. Convenience samples. Codex reports beat the root synthesis on community
   coverage because they are later and reached Reddit.
6. **Weak:** vendor articles, star counts, search snippets, self-promotion,
   model memory.

Status labels:

- **Current:** best available evidence for its topic.
- **Superseded:** a later file replaces part of it; the note says which part.
- **Disputed:** contains a claim this audit found wrong or unsupported.

A file can be current overall and still carry a disputed detail.

## Run Timeline (local time, September 26, 2026)

| Time | Event |
|---|---|
| 21:54 | Local audit written (`00-hermes-baseline.md`) |
| 21:54 to 22:10 | Five Claude Code runs, one after another, each reading the earlier reports. Three earlier parallel starts of 03 to 05 were stopped and not kept |
| 22:11 to 22:13 | Root synthesis `RESEARCH.md` and citation `ledger.json` written |
| 22:39 to 22:40 | Three Codex prompts written; three Codex runs start at the same time |
| 23:16 to 23:28 | Codex reports finish (03, then 02, then 01) |

**The root synthesis predates all three Codex reports.** Its statement that
Reddit was blocked describes the Claude pass only.

## Inventory (30 files)

Counted programmatically on September 26: 30 files, about 1.89 MB, of which
the three Codex event traces are about 1.63 MB. No files were missing, and no
new files appeared during this reconciliation.

| # | File | Kind | Status | Read when |
|---|---|---|---|---|
| 1 | 00-hermes-baseline.md | Local audit | Current (dated) | You need the measured failure |
| 2 | 01-landscape.md | Claude report | Superseded in part | Provider matrix and prices |
| 3 | 01-landscape-prompt.md | Prompt | Current | Checking what was asked |
| 4 | 01-landscape-result.json | Receipt | Current | Checking cost, turns, denied commands |
| 5 | 02-community.md | Claude report | Superseded in part | HN evidence and vendor-voice checks |
| 6 | 02-community-prompt.md | Prompt | Current | Checking what was asked |
| 7 | 02-community-result.json | Receipt | Current | Checking provenance |
| 8 | 03-providers.md | Claude report | Current, one disputed detail | Code paths, prices, first fix |
| 9 | 03-providers-prompt.md | Prompt | Current | Checking what was asked |
| 10 | 03-providers-result.json | Receipt | Current | Checking provenance |
| 11 | 04-workflow.md | Claude report | Current, one superseded line | Workflow, security, test suite |
| 12 | 04-workflow-prompt.md | Prompt | Current | Checking what was asked |
| 13 | 04-workflow-result.json | Receipt | Current | Checking provenance |
| 14 | 05-turnkey.md | Claude report | Current | Turnkey APIs and benchmarks |
| 15 | 05-turnkey-prompt.md | Prompt | Current | Checking what was asked |
| 16 | 05-turnkey-result.json | Receipt | Current | Checking provenance |
| 17 | RESEARCH.md | Root synthesis | Superseded in part | The original proposal and phases |
| 18 | ledger.json | Citation ledger | Current | Root synthesis source list |
| 19 | codex-community/01-hermes-reddit/REPORT.md | Codex report | Current | What Hermes users run |
| 20 | codex-community/01-hermes-reddit/PROMPT.md | Prompt | Current | Seed thread IDs and counting rules |
| 21 | codex-community/01-hermes-reddit/LAST_MESSAGE.txt | Final message | Current | Quick completion check |
| 22 | codex-community/01-hermes-reddit/events.jsonl | Event trace (381 KB) | Current | Auditing edits and retrieval |
| 23 | codex-community/02-agent-forums/REPORT.md | Codex report | Current, two disputed details | What general agent builders report |
| 24 | codex-community/02-agent-forums/PROMPT.md | Prompt | Current | Checking what was asked |
| 25 | codex-community/02-agent-forums/LAST_MESSAGE.txt | Final message | Current | Quick completion check |
| 26 | codex-community/02-agent-forums/events.jsonl | Event trace (305 KB) | Current | Auditing edits and retrieval |
| 27 | codex-community/03-forum-crosscheck/REPORT.md | Codex report | Disputed counts; rest current | Bounded Hermes sample and maintainer activity |
| 28 | codex-community/03-forum-crosscheck/PROMPT.md | Prompt | Current | Checking what was asked |
| 29 | codex-community/03-forum-crosscheck/LAST_MESSAGE.txt | Final message | Current | Quick completion check |
| 30 | codex-community/03-forum-crosscheck/events.jsonl | Event trace (947 KB) | Current | Auditing edits and retrieval |

## Generated Reference: Report Summaries

Every substantive report was read in full for this spec. The Claude runs were
Claude Code on Opus 5.5 at low effort. The Codex runs were Codex on GPT-6 Luna
at extra-high effort. All were read-only apart from writing their own report.

### Baseline: 00-hermes-baseline.md

Local file, not published.
**Current (dated September 26).** The only measured evidence. Hermes has
separate `web_search` and `web_extract` tools with separate backends. The
effective probe returned `openai-native` for both. `web_extract` on the Hermes
`llms.txt` failed with the search-only error. No provider credential was
present (names checked, values not read). Lists the existing browser tools and
research skills. Says restore extraction first and not to infer that anything
was installed.

### Claude 01: 01-landscape.md

Local file, not published.
**Superseded in part.** Fast landscape pass. Opened the Hermes web search docs
and vendor pricing pages for Firecrawl, Tavily, Exa, Parallel, and Brave, plus
one semi-independent benchmark (AIMultiple) that found Brave, Firecrawl, Exa,
and Parallel search quality statistically tied, with a disclosed SerpAPI
conflict. Lists which Hermes backends can extract. First flags Firecrawl issues
#99533 and #106904. Recommends Firecrawl or Parallel for extract.

- Superseded: the Firecrawl-first option (by Claude 03's code reading).
- Provenance: its receipt shows the batch `gh api` command for star counts was
  denied, yet the report says star counts came from `gh api`. Treat its star
  counts as unverified (GPT Researcher's count was later confirmed by Claude 05
  through the GitHub API). Opened no Reddit or HN thread.
- **Read when:** you need the backend capability list, the price matrix, or the
  benchmark caveat.

### Claude 02: 02-community.md

Local file, not published.
**Superseded in part** by the Codex reports on community coverage. Reddit was
unreachable with Claude's tools. Opened 9 HN threads (its opening caveat says 8;
the table and receipt show 9) and saw about 16 GitHub issue titles only. Finds
no vendor consensus; a repeated "cheap search, separate extract, browser
fallback" pattern; pain from blocking, rate limits, per-page cost, billing
surprises, and vendor terms on query data. Flags vendor voices (Parallel
founder, Context.dev, Draco author, a promotional Crawl4AI post). One HN thread
(48557609) had three Hermes users: self-hosted SearXNG, a SearXNG plus Exa plus
Tavily fusion, and one who recommends paying for Brave.

- Still useful: the vendor-voice checks and the query-data terms lead
  (unverified at source).
- **Read when:** you need HN evidence or the astroturf checks.

### Claude 03: 03-providers.md

Local file, not published.
**Current, one disputed detail.** The most important technical report. Read the
installed Hermes code at `ffa40b07f0`. Findings (Code-read): empty web config
lets autodetect pick the search-only plugin; explicit `web.extract_backend`
wins; adding a keyed provider also moves search. Issue #27580 is fixed in code;
#99533 (Firecrawl empty success, which also blocks rescue) and #106904 (no lazy
wait) look unfixed. Rescue fires only on exception, timeout, or when every URL
in a batch fails. Cache is 20 minutes and stores only non-empty successes.
Perplexity "extract" returns snippets. Firecrawl free tier is 1,000 per month
on the vendor page (local Hermes docs say 500, stale). Worked example: 100
searches plus 300 extracts cost about $0.40 to $1.60 at list price. Recommends
Parallel keyed primary, Exa backup, Tavily alternative, Firecrawl demoted.

- Disputed detail: the rollback uses `hermes config unset`, but only `config
  set --help` and `config --help` output is cited. Confirm `unset` exists (T0).
- Provenance: git commands were denied, so the commit was confirmed by a ref
  grep. This reconciliation confirmed it with `git log`: `ffa40b07f0`, dated
  September 25. Vendor pages went through a summarizing fetcher.
- **Read when:** you need code paths, the precedence rule, or the first-fix
  commands.

### Claude 04: 04-workflow.md

Local file, not published.
**Current, one superseded line.** Designs the Hermes-native workflow. Read the
installed skills and parts of Hermes docs and code; fetched no web pages
(receipt shows no fetch model use, which matches). Maps existing skills and
their gaps, an 11-stage workflow, three architectures (config plus thin skill,
MCP tool, delegated heavy mode), deployment steps, gateway and prompt-cache
effects, cost caps, prompt-injection rules, a failure table, and the 5-query
acceptance suite with pass thresholds it labels as its own proposal.

- Superseded: its turnkey cost line ("$5 to $2,400 per 1,000 runs") is replaced
  by Claude 05's per-run tiers.
- Inferred, not tested: config is read per call so no restart is needed.
- **Read when:** you are writing the thin skill or the acceptance suite.

### Claude 05: 05-turnkey.md

Local file, not published.
**Current.** Compares Parallel Task, Tavily Research, Exa Agent, Perplexity
Sonar Deep Research, OpenAI and Gemini deep research APIs, GPT Researcher, and
LangChain `open_deep_research` (archived August 21, 2026). No independent
benchmark compares these APIs. FutureSearch's 2025 result (plain o3 beat OpenAI
Deep Research) is the strongest counterexample. Corrects Claude 04: cost is not
the objection; unverified quality, vendor-side evidence, latency, upkeep, and
cache churn are. Proposes an opt-in Parallel Task MCP trial only if the suite
fails on coverage.

- Vendor claims kept as vendor claims: Parallel DeepSearchQA figures (snippet
  only), latency numbers.
- **Read when:** anyone proposes a turnkey research API.

### Root synthesis: RESEARCH.md and ledger.json

RESEARCH.md,
ledger.json.
**Superseded in part.** Reconciles the baseline and Claude 01 to 05. Adds that
the `web` config keys were empty. Proposes four phases: restore extraction with
a keyless Parallel smoke, measured tests, one thin skill, optional turnkey.
Says credentials must come through a masked local handoff, not Discord. The
ledger lists its 10 cited URLs, all accessed September 26, with empty titles.

- Superseded: "Reddit was blocked" and "no broad community consensus was
  established" as a coverage statement. The later Codex reports reached Reddit.
  The no-consensus conclusion itself still holds.
- **Read when:** you want the original proposal or the phase framing.

### Codex 01: codex-community/01-hermes-reddit/REPORT.md

Local file, not published.
**Current.** What Hermes users say they run. 11 independent Reddit threads
(mostly r/hermesagent, plus one each from r/LocalLLM and r/LocalLLaMA) with
direct comment links; **27 unique non-promotional commenters**. Counting unit
is one account times one tool times one job, deduplicated.

- Search: SearXNG 14 current users (plus 1 attempt), DDG 2, Tavily 2, Brave 1,
  Exa 1, Kagi 1, a Gemini script 1.
- Extraction: Firecrawl 6 current (plus 3 earlier, costly, or failed), Scrapling
  2, Crawl4AI 1, Tavily 1, Trafilatura 1.
- Browser: Camofox 3, and one each for Camoufox, Browserbase, BrowserOS,
  Chrome remote debugging, Playwright.
- 51 provider-job pairs: 36 positive, 12 neutral, 3 complaints. This
  reconciliation re-added them: 44 current plus 7 trial or attempt pairs, so
  the sentiment totals mix current and past use.
- Promotion kept apart: Hound, Forage, and a paid research-profile seller.
- Four GitHub issues outside the count: #78984 (cron report broke on Tavily
  quota then Firecrawl rate limits), #29617 (key set but backends unset gave a
  no-op), #32698 (confusion when search-only SearXNG was asked to extract),
  #21003 (a feature request).
- One custom director-and-investigator research skill (no provider named). No
  independent turnkey research product use.
- Provenance: 8 of 9 seed threads matched; `1tws7pv` unresolved; `1ub4cmp` read
  but excluded because comment links did not resolve. Reddit `.json` failed;
  pages were opened through Codex's built-in web tool (the trace shows page-open
  actions and a single Computer Use state check, not local browser navigation).
  The count rose from 26 to 27 in late edits that spelled out the account list;
  the final JSON is internally consistent (checked here).
- **Read when:** you need what Hermes users actually deploy, or the frequency
  and failure anecdotes.

### Codex 02: codex-community/02-agent-forums/REPORT.md

Local file, not published.
**Current, two disputed details.** General agent builders, Hermes threads
excluded. 19 fully read source units: 12 Reddit threads, 3 HN threads, 4 GitHub
issues. Unique accounts that used or tested each tool: SearXNG 12, Tavily 9,
Firecrawl 9, browser automation 8, Exa 7, Brave 6, Crawl4AI 3, Jina API 3,
Jina Reader 1, Parallel 1, Perplexity Sonar Deep Research 1. Firsthand
recommendations: Brave 2, Jina API 2, SearXNG 1, Parallel 1, browser 1.

- Main findings: a separable pipeline and fallback between layers recur;
  anti-bot handling is incomplete (Cloudflare challenges, datacenter-IP 403s,
  one same-host case where Browserless worked and Firecrawl's Playwright did
  not); cost evidence is anecdotal; **no source evaluates claim-level citation
  accuracy.**
- Disputed: one sentence credits the Exa surprise-bill anecdote to R4; the
  table puts it in H1. Two accounts in the tally JSON (the likely R2 and R4
  thread authors) are never named in the evidence table, so they cannot be
  audited from the prose.
- Coding note: its strict recommendation rule gives Firecrawl zero
  recommendations even though one operator (R9) said Firecrawl improved their
  pipeline.
- Provenance: late edits removed an advice-only account from the Tavily counts
  (10 to 9), a valid fix. Reddit `.json` returned 403; pages came through
  Codex's web tool; HN checked through the public Firebase API.
- **Read when:** you need non-Hermes builder experience with the same vendors.

### Codex 03: codex-community/03-forum-crosscheck/REPORT.md

Local file, not published.
**Disputed counts; rest current.** Asks whether any defensible popularity
signal exists. A reproducible bounded search (4 exact queries, January 1 to
September 26, 2026) gave 12 URLs; 6 overlapped Codex 01; 5 of the 6 new ones
opened. Reports 20 Reddit handles plus 4 GitHub issue authors (24, or 23
without the Crawl4AI plugin's author). Reddit `.json` failed 3 of 3; GitHub
Discussions are disabled (HTTP 410). Separates maintainer activity (web-tool
commits September 10 to 24; Linkup, Ollama, SearXNG pacing pull requests) from
adoption. Concludes with high confidence that no winner exists and with medium
confidence that a layered stack recurs.

- Disputed dedupe: it counts `BrillianTico`, who is already in Codex 01's list,
  and it drops `dellis87` as a Codex 01 duplicate, but that handle appears
  nowhere in Codex 01's report or trace. Issue #78984 is in both reports.
  Corrected: about 19 Reddit handles new to Codex 01, 22 accounts with the 3 new
  GitHub authors, 21 without the plugin author, plus one if `dellis87` is not a
  duplicate.
- Gap: no per-provider tally, so its accounts cannot be merged into Codex 01's
  provider counts.
- Provenance: the report was written twice by shell and not edited afterward;
  its size matches the last write. Page text is not stored in the trace, so
  "fully read" claims cannot be re-verified from it. One cited commit
  (September 10) has no link.
- **Read when:** you need the bounded sample method, the selection-bias audit,
  or the maintainer-activity signal.

## Receipts, Prompts, and Traces

What each supporting file proves. None of these were copied into the spec.

| Run | Prompt asked for | Receipt or trace shows |
|---|---|---|
| Claude 01 | Landscape of search, extract, turnkey, workflows | 18 turns, $0.55 list; Haiku used for fetch summaries; 1 denied command (the `gh api` star-count batch) |
| Claude 02 | Independent community consensus; Reddit and HN | 25 turns, $0.65; 2 denied listing commands; 9 HN pages in the final summary |
| Claude 03 | Provider docs, installed code, Firecrawl 500 vs 1,000, first fix | 38 turns, $1.19; 5 denied commands (locating Hermes, `git log`) |
| Claude 04 | Hermes-native workflow, acceptance suite | 19 turns, $0.87; no fetch model use (no web pages, as stated); 1 denied command |
| Claude 05 | Turnkey APIs versus a Hermes loop; challenge 04 | 33 turns, $1.03; 1 denied command |
| Codex 01 | Hermes user reports; 9 seed thread IDs; dedupe rules | 126 events; 40 web-tool actions; 12 shell commands; 5 late edits (26 to 27); 7.9M input and 130K output tokens |
| Codex 02 | Non-Hermes builder reports across forums | 122 events; 38 web-tool actions; Reddit `.json` 403; HN API calls; 2 late edits (Tavily 10 to 9); 4.5M input and 129K output tokens |
| Codex 03 | Bounded popularity check; bias audit | 99 events; 15 web-tool actions; 30 shell commands (public GitHub, HN, and Algolia APIs); no edits after the final write; 3.3M input and 68K output tokens |

- Claude runs total about $4.29 at list price. These are model costs, not bills,
  and they are not Hermes retrieval costs.
- Claude runs have no event traces, only result receipts. Their "opened" pages
  went through a summarizing fetcher, so quotes are close to verbatim, not exact.
- The Codex 01 process output included one `apply_patch verification failed`
  message when an expected line no longer matched. The event traces themselves
  did not contain that diagnostic; the final on-disk report was audited after
  the run. Other failed commands concerned a wrong relative path, `git status`
  outside a repo, a missing skill file, and a Discussions API parse error.
- Codex 02 also read Agents workspace research guidance while starting; it
  wrote nothing outside its report.

## Community Evidence: Overlap and Dedupe

Do not add these samples together without removing overlaps.

| Overlap | Where | Handling |
|---|---|---|
| HN thread 48557609 (Brave key for Hermes) | Claude 02 and Codex 03 (reply 48557710) | Count once; mostly recommendations |
| HN thread 48779454 (SearXNG) | Claude 02 row 4 and Codex 02 H1 | Count once |
| GitHub #78984 (cron quota failure) | Codex 01 and Codex 03 | One author |
| One Reddit account (name omitted) | Codex 01 and Codex 03 | One account |
| r/LocalLLaMA 1ua2w5t | Counted by Codex 01, excluded by Codex 02 as Hermes-centered | Correct split |

Rough combined Hermes-specific picture: about 46 Reddit handles (27 from Codex
01 plus about 19 new from Codex 03) and 7 distinct GitHub issues. Only Codex 01
has per-provider counts. This is a size check, not a denominator for any share.

How each provider's evidence breaks down across all samples:

| Provider | Firsthand use | Endorsement | Troubleshooting | Vendor or self-promotion |
|---|---|---|---|---|
| SearXNG | Most repeated among Hermes and general builders | A few explicit | CAPTCHAs, upstream rate limits, one quit | Builder posts (Forage, Hound) use it |
| Firecrawl | Most repeated Hermes extractor | One pair recommendation | Credits, cost, failed setup, empty responses, rate limits | Firecrawl staff replies (excluded); vendor blogs |
| Parallel | None among Hermes users; 1 general builder | 1 | Launch free-credit complaint | Founder replies; vendor benchmark |
| Tavily | A few | None explicit | Config no-op, plugin failure, quota | None noted |
| Exa | A few | 1 Hermes user | Surprise bills, freshness wrapper confound | Exa staff reply (excluded) |
| Brave | A few, search only | 2 general, 1 HN | Query length cap, quota | Vendor "best API" articles |
| Crawl4AI | A few, via plugin or skill | 1 | Version bugs, later partly fixed | Plugin author's own post; a promotional docs post |
| Browsers | Several products, fallback use | 1 | Datacenter IPs, strong bot defenses | TinyFish staff promotion (excluded) |
| Turnkey APIs | None independent among Hermes users | None | 1 general builder left Sonar Deep Research | That post promotes a competitor |

## External / Canonical Docs

Primary pages cited by the reports, all read September 26, 2026 by a worker.

- Hermes web search docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/web-search
- Hermes issues: https://github.com/NousResearch/hermes-agent/issues/99533 (opened), https://github.com/NousResearch/hermes-agent/issues/106904 (snippet only), https://github.com/NousResearch/hermes-agent/issues/27580 (snippet only)
- Firecrawl pricing: https://www.firecrawl.dev/pricing and rate limits: https://docs.firecrawl.dev/rate-limits
- Parallel pricing: https://docs.parallel.ai/getting-started/pricing and Task MCP: https://docs.parallel.ai/integrations/mcp/task-mcp
- Tavily credits: https://docs.tavily.com/documentation/api-credits
- Exa pricing: https://exa.ai/pricing
- Perplexity pricing: https://docs.perplexity.ai/getting-started/pricing
- FutureSearch benchmark: https://futuresearch.ai/deep-research-bench
- LangChain Open Deep Research (archived): https://github.com/langchain-ai/open_deep_research

## Related Specs

- [Internet deep research spec](../internet-deep-research/spec.md): standalone
  research apps, funding order, and general source-quality rules. Its evidence
  is a different set of 13 artifacts inside this workspace.
- [Research spec](../research/spec.md): how research runs are performed and
  saved.
- [Browser use spec](../browser-use/spec.md): browser identities and signed-in
  safety for the fallback step.

## Not Re-verified or Excluded

- **Hermes code line numbers and skill contents** come from Claude 03 and 04.
  This session could not read the Hermes checkout or skills, so no CODEMAP was
  written. Only the commit was rechecked.
- **Effective backends and the profile environment** were not rechecked, by the
  Single-Tool Boundary. See spec step T0.
- **Event traces** were inspected for event types, edits, failures, retrieval
  actions, and the disputed dedupe claims. Their long outputs were not copied.
- **Page text inside Codex traces** is not stored, so full-read claims rest on
  each report's own statement.

## Weak Claims To Avoid

- "Parallel is the most reliable extractor." Price and code path only; zero
  Hermes user reports.
- "Firecrawl is broken in Hermes." A code-level empty-page risk, not reproduced.
- "Firecrawl is the best because most Hermes users run it." Popularity in a
  convenience sample, likely shaped by it being the default.
- "SearXNG fixes Hermes web research." It is search-only.
- "52% of Hermes users run SearXNG." 14 of 27 is a hand-coded sample.
- "Reddit could not be reached." True only for the Claude pass.
- "Turnkey research is too expensive." Pro tiers list at about $0.10 per run.
- "Turnkey citations are verified." They are vendor excerpts.
- "Config changes apply without a restart." Inferred, not tested.
- "Keyless rescue is harmless." It sends URLs to up to four vendors.
- Firecrawl star counts from Claude 01. The command was denied.
- The Hermes local docs' 500-credit Firecrawl free tier. The vendor page said
  1,000 on September 26.
- A report of 20 to 30 fetches using most of a Firecrawl free tier. It does not
  fit list prices and is unexplained.

## 2026-10-01: Web reference moved

Generic search and fetch facts, tool quality, ladders and current routing decisions now live in [capabilities/web](../../capabilities/web/README.md) and [its decisions](../../capabilities/web/DECISIONS.md). This file retains dated history. Earlier provider defaults and budgets are not current policy. Hermes setup and research workflow retain their own spec.
