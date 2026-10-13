---
created_at: 2026-10-06
updated_at: 2026-10-06
model: claude-opus-5-5
doc_type: spec
status: researched
scope: MCP servers for web scraping site access (Apify, ReefAPI, Bright Data, SerpApi, X official data MCP, Bluesky, Mastodon and Threads MCPs)
purpose: Which MCP servers could give agents platform data, what they cost, the security rules they must meet, and which ones duplicate tools we already have.
related:
  - path: ../spec.md
    why: Owning spec and the provider table.
  - path: ../shared/rules.md
    why: Rules a provider must pass, including home-IP and no-login rules.
  - path: ../sites/x.md
    why: X official data MCP.
  - path: ../sites/reddit.md
    why: Reddit wrappers cannot bypass Reddit's approval rule.
  - path: ../sites/threads.md
    why: Threads MCPs and their publishing tools.
  - path: ../sites/stepstone-ireland.md
    why: Apify actors for Jobs.ie and IrishJobs.ie.
---

# MCP servers for web scraping site access

MCP servers let an agent call a data provider as a tool. This file lists
the ones that matter for reading platforms and the security rules they
must meet. An MCP server adds tools; it does not change anyone's right to
the data.

**Enabling any MCP server is a per-tool user decision.** It is recorded
in `~/agents/capabilities/connectors.md` and in that tool's
adapter, not here. This file only says which servers are worth asking
about.

Sources: deep research round 1 (5 October 2026; private, not published), report G9, plus the 6 October corroboration. Lines marked
"not rechecked" come only from G9.

## Status

- **Worth asking about, in order:** Apify MCP with an actor allowlist;
  ReefAPI hosted MCP for a free-credit test only; SerpApi MCP only if
  Google Jobs matters (it does not cover Ireland). Not Bright Data MCP
  first, because Bright Data does not approve personal projects.
- **Allowed today:** no MCP enablement, no account, no purchase, no pilot.
- **Last checked:** 6 October 2026 for Apify, ReefAPI, Bright Data and
  SerpApi pages. Others from G9 only.

## Servers

### Apify MCP

- **Covers:** the Apify actor store through `search-actors`,
  `call-actor` and dataset tools (https://github.com/apify/actors-mcp-server,
  v0.17.2, 5 Oct 2026, G9).
- **Price:** free plan $5 a month usage; Starter $19 ($17 yearly). Actors
  bill per result on top. Confirmed 6 Oct 2026 at https://apify.com/pricing.
- **Individual eligibility:** terms (effective 9 July 2026) say "The
  Services are intended for business use only and are not designed,
  marketed, or suitable for consumers"
  (https://docs.apify.com/legal/general-terms-and-conditions, read 6 Oct).
- **Rule if enabled:** an explicit actor allowlist. Turn off open actor
  search and execution. Reject any actor that asks for cookies, `li_at`,
  a session token or a browser profile.
- **Label:** Official doc (confirmed).

### ReefAPI hosted MCP

- **Covers:** five generic tools (`search_engines`, `get_catalog`,
  `get_engine_schema`, `get_action_schema`, `call_engine`); discovery tools
  need no key. Catalogue claims Reddit, Bluesky, HN, Indeed, more (Vendor
  claim). X, Threads and LinkedIn-post coverage is disputed.
- **Price:** 1,000 free credits; Pro $15 a month for 10,000, never expire;
  top-ups $1.72 per 1,000. Its homepage says card or crypto; its pricing
  page says crypto only for now. Read 6 Oct 2026 at
  https://reefapi.com/pricing (Vendor claim). See
  [reefapi.md](reefapi.md).
- **Individual eligibility:** no business-only clause, but its terms
  (updated 16 Sep 2026) name no company or country.
- **Reliability:** joined Apify June 2026; MCP repo created 23 Jun 2026,
  1 star. VerifyMCP trust score 80/100 (scan 20 Sep 2026); no tool
  declares a destructive hint.
- **Role:** free-credit test only.

### Bright Data MCP

- **Covers:** X, Reddit and LinkedIn known-URL readers, search and
  scrape-as-markdown (https://github.com/brightdata/brightdata-mcp, v2.11.3,
  17 Sep 2026, G9).
- **Price:** 5,000 free credits a month, shared with other Bright Data
  use; then $1.50 per 1,000 records. Free accounts stop when credits run
  out. Confirmed 6 Oct 2026.
- **Individual eligibility:** docs say "Personal projects... are not
  approved" (https://docs.brightdata.com/proxy-networks/residential/network-access,
  read 6 Oct). Blocks it unless there is a real business use.
- **Note:** LinkedIn tools must stay disabled under our rules.

### SerpApi MCP

- **Covers:** search, including Google Jobs
  (https://github.com/serpapi/serpapi-mcp, v2.0.0, 22 Sep 2026).
- **Price:** free 250 searches a month; Starter $25 for 1,000; only
  successful searches billed. Confirmed 6 Oct 2026 at
  https://serpapi.com/pricing.
- **Caveat:** Google Jobs does not cover Ireland (6 Oct check). SerpApi's
  status page reported low Google Jobs success rates.

### X official data MCP

- **Covers:** X API reads such as post search and timelines, at
  `api.x.com/mcp`; `docs.x.com/mcp` is docs only (https://docs.x.com/tools/mcp,
  G9, not rechecked).
- **Price:** X pay-per-use, prepaid; search unit price not found outside
  the console.
- **Rule:** requests still reach X from where the server runs. Run it on
  a hosted worker.

### Platform MCPs for Bluesky, Mastodon and Threads (G9, not rechecked)

- **Bluesky** (`bsky-mcp-server`): needs a handle and app password. Not
  needed; Bluesky's public API is anonymous. Prefer a small own reader.
- **Mastodon** (`mcp-server-mastodon`, v1.0.5, 11 Sep 2026): needs an
  instance token. Keep `READ_ONLY=true`.
- **Threads** (`threads-mcp`): needs Meta OAuth and has publishing tools.
  Remove them. `threads-lyr` scrapes anonymously from wherever it runs.
- **Reject outright:** LinkedIn MCPs that drive a logged-in browser
  (`linkedin-mcp-server`, SuperMCP).

## Security rules

Any server above must meet these before a user is asked to enable it.

1. **Prompt injection and tool poisoning.** Posts, job adverts and even
   tool descriptions can carry hidden instructions. A 23 March 2026 study
   showed attacks through tool metadata across seven clients
   (https://arxiv.org/abs/2603.22489, Independent report). Treat all
   fetched text as data.
2. **Read-only modes.** Use them where offered (Mastodon `READ_ONLY=true`).
   A read-only hint is a label, not a lock; enforce it in config.
3. **Remove publishing tools.** Strip post, reply and account tools from
   Threads, Mastodon, Reddit and X servers.
4. **Keep keys out of coding agents.** Research tools run in a worker with
   no shell, no repository and no secrets. GitGuardian reports 24,008
   secrets found in MCP config files (Vendor claim,
   https://www.gitguardian.com/state-of-secrets-sprawl-report-2026).
   Scrapfly warns against exposing a key-bearing server without per-caller
   auth.
5. **Hosted workers only.** A local MCP that calls an official API still
   sends requests from the home IP. Run platform servers on a hosted
   worker.
6. **Spend caps.** Per-task limits on requests and money; stop on repeated
   errors. A refused request never falls back to a personal login.

## Which ones duplicate what we have

Parallel, Exa and Firecrawl already cover search and page reading. See
`~/agents/capabilities/web/tools/parallel.md`,
`~/agents/capabilities/web/tools/exa.md` and
`~/agents/capabilities/web/tools/firecrawl.md`.

- **Duplicates, do not add without a measured gap:** Tavily, Brave,
  Perplexity, Oxylabs and Scrapfly MCPs, and the general scrape tools
  inside Bright Data and Decodo.
- **Not duplicates:** Apify actors (site-specific readers), ReefAPI and
  Bright Data structured readers, SerpApi Google Jobs, X data MCP, and
  xAI Grok X Search (a model tool, priced in
  `~/agents/specs/web-scraping-site-access/providers/social-apis.md`).

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | G9: add Bright Data MCP first. | Bright Data does not approve personal projects; not first. | docs.brightdata.com, read 6 Oct |
| 2026-10-06 | ReefAPI MCP repo has 4 stars; card payment accepted. | 1 star; crypto only today. | github.com/reefapi/reefapi-mcp and reefapi.com/pricing, read 6 Oct |

## Open questions

1. Does Apify's "business use only" clause void a free account for an
   Irish consumer? It decides whether Apify MCP is usable at all.
2. Who operates ReefAPI, and where? Needed before sending it queries.
3. Which ReefAPI engines really cover X, Threads and LinkedIn posts, and
   at what credit cost? Answer: its `/apis` pages, then an Observed test.

## Sources

- https://apify.com/pricing, https://docs.apify.com/legal/general-terms-and-conditions (read 6 Oct 2026)
- https://reefapi.com/pricing, https://reefapi.com/terms, https://reefapi.com/mcp (read 6 Oct 2026)
- https://docs.brightdata.com/proxy-networks/residential/network-access, https://brightdata.com/pricing/mcp-server (6 Oct 2026)
- https://serpapi.com/pricing (read 6 Oct 2026)
- https://docs.x.com/tools/mcp (5 Oct 2026, via G9)
- https://arxiv.org/abs/2603.22489; https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- Deep research round 1 (5 October 2026; private, not published), report G9; 6 October corroboration.
