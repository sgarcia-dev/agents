---
created_at: 2026-10-06
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: spec
purpose: How agents can read public platforms (social networks, developer forums, job boards, employer job feeds) and which data providers sit in front of them. One file per site and per provider, plus shared rules and a test method.
related:
  - path: ./AGENTS.md
    why: How to work in this spec, layout and growth rules.
  - path: ./STATE.md
    why: What is true now, blockers and next steps.
  - path: ./DECISIONS.md
    why: User rules and accepted choices.
  - path: ./SOURCES.md
    why: Evidence ledger and weak claims to avoid.
  - path: ./shared/rules.md
    why: Access, legal and data rules for every route.
  - path: ./shared/evaluation.md
    why: How to test a route and when to add a platform or provider.
  - path: ./shared/eligibility.md
    why: Which providers accept an individual; the options for P1.
  - path: ./shared/legal.md
    why: Irish and EU legal background, in depth.
  - path: ../internet-deep-research/spec.md
    why: Neighbouring spec for general web search and research tools.
---

# Web scraping: site access

How an agent here can read public platforms: what each one allows, which
route is best for each job, what it costs, and what is still unknown. It
covers social networks, developer forums, job boards and employer job
feeds, plus the paid providers (Apify, ReefAPI, Bright Data and others)
that read them for us. It is a general research capability; a private job
pipeline is one consumer.

The short version, as of 7 October 2026 (three research rounds, then
the first pilot): **the free routes now have Observed tests.** Hacker
News, Reddit threads through Arctic Shift, employer job feeds on six
systems, Bluesky reads and Jetstream, Mastodon hashtags, Lobsters, DEV
and X's syndication endpoint
all passed on 7 October, and 11 capped Apify runs ($0.27) returned real
data for most job boards and social sites. Free routes exist for Hacker News,
Bluesky reads, Mastodon hashtags, employer job feeds and Reddit (the
Arctic Shift archive). Bluesky and Mastodon keyword search need a
separate research account. X has a clean official API that accepts an
individual, at about $25 a month. Threads is excluded. LinkedIn stays
excluded for direct reads. The user decided on 6 October 2026 to sign up
to Apify as a business, to read the Irish boards through Apify, and to pilot Hacker News and Reddit first,
because Reddit is where genuine opinions on providers live. Round 3's
user opinions favour Apify (per-Actor testing, hard money caps) and
TwitterAPI.io, keep Bright Data as a fallback, and find no real users for
ReefAPI or SociaVault. The open choices (P10, P12, P13) now have that
evidence and wait on the user; proposals are in STATE.md.

## Start Here

- **Status:** [STATE.md](STATE.md): what is true now and the next step.
- **Rules:** [shared/rules.md](shared/rules.md): read before using or
  proposing any route. Background in [shared/legal.md](shared/legal.md).
- **Paying a provider:** [shared/eligibility.md](shared/eligibility.md): who accepts an
  individual, and the user's options.
- **Accounts:** [shared/accounts.md](shared/accounts.md): research and alert
  accounts. **Job alerts:** [shared/email-alerts.md](shared/email-alerts.md).
- **A platform:** the route table below, then its `sites/` file.
- **A provider:** the provider table below, then its `providers/` file.
- **Decisions:** [DECISIONS.md](DECISIONS.md).
- **Sources:** [SOURCES.md](SOURCES.md), including the claims we found
  to be wrong.

## Shared model

**Operations.** Keep these four apart. A provider that "supports" a
platform rarely does all four.

| Operation | Meaning |
|---|---|
| discover | Keyword or topic search across the platform. |
| retrieve | One known item by URL or ID. |
| thread | A known item with all its replies. |
| monitor | Follow accounts, tags, communities or saved searches over time. |

Job sources use **search** (find listings) and **detail** (one listing's
full text) in place of thread.

**Route types,** from lowest to highest risk. The full risk ladder and
which rungs are allowed live in [shared/rules.md](shared/rules.md).

1. Official API or open protocol, within its terms.
2. RSS feeds and public employer job feeds.
3. Email alerts delivered to an inbox the user controls.
4. Search-engine discovery (finding URLs through a search API), then a
   page reader.
5. A third-party API or actor that runs on the provider's own servers and
   IPs, with no cookies or account of ours.
6. Our own requests from the home connection (plain HTTP, then headless
   browser), only for sites that do not object.
7. Residential proxies, logged-in scraping, own cookies: not allowed.

**Evidence labels:** Official doc, Vendor claim, Independent report, Court
record, Observed test, Inference. Only an Observed test proves a route
works.

## Route table

One line per platform. Costs are rough monthly figures at about 5,000
items, from the cited file. "Gate" says what must happen before an agent
may use the route (see [DECISIONS.md](DECISIONS.md)).

| Platform | Best route today | Cost | Gate | File |
|---|---|---|---|---|
| X | Official pay-per-use API ($0.005 per post read) or TwitterAPI.io (about 30 times cheaper, unsanctioned). User opinion (round 3) favours TwitterAPI.io first, official as fallback; the choice is P12. | About $25 official; about $0.75 unofficial | P12 open; X research account approved (P6) | [x.md](sites/x.md) |
| Bluesky | Official API: anonymous reads for posts, threads and feeds; Jetstream live. Search needs an app password on a separate account (anonymous search now refused). | $0 | Anonymous reads and Jetstream piloted 7 Oct 2026 (passed); P6 for search | [bluesky.md](sites/bluesky.md) |
| Threads | Excluded by the user (P11). Official search needs Business Verification anyway. | n/a | Excluded | [threads.md](sites/threads.md) |
| Mastodon | Official per-server API: hashtag and account timelines with no account. Post search needs a user token and finds only opted-in posts. | $0 | Hashtags piloted 7 Oct 2026 (3 of 5 servers allow anonymous reads); P6 for search | [mastodon.md](sites/mastodon.md) |
| Reddit | Arctic Shift archive (free, no key) for known communities and full threads; Apify `harshmaur/reddit-scraper` as the tested paid fallback. First in line: Reddit is the main source of genuine user opinion. | $0 to about $30 | Arctic Shift piloted 7 Oct 2026 (threads passed; keyword search unreliable) | [reddit.md](sites/reddit.md) |
| Hacker News | Algolia search plus the official Firebase API. | $0 | Piloted 7 Oct 2026 (passed) | [hacker-news.md](sites/hacker-news.md) |
| Developer forums | Each forum's own API or RSS (Stack Exchange, GitHub Discussions, Lobsters, DEV, Discourse, Hugging Face). | $0 | Lobsters and DEV piloted 7 Oct 2026 (passed); others need permission | [dev-forums.md](sites/dev-forums.md) |
| LinkedIn | Excluded for direct reads. Round 3 found no vendor that users trust for LinkedIn; employer job feeds stay the jobs route. Vendor data is P10. | n/a | Direct: excluded. Vendors: P10 open | [linkedin.md](sites/linkedin.md) |
| Facebook | Deferred. No justified source set. | n/a | Deferred | [facebook.md](sites/facebook.md) |
| Indeed | Email alerts (30 jobs per email), as many narrow alerts as useful, labelled in the mailbox and parsed without opening links. No official read API. | $0 alerts | Approved (P7); the user creates the account | [indeed.md](sites/indeed.md) |
| Glassdoor | Do not read separately. It merged into Indeed on 1 July 2026; Indeed and employer feeds cover its jobs. | $0 | None needed | [glassdoor.md](sites/glassdoor.md) |
| IrishJobs.ie and Jobs.ie | Apify Black Falcon actors (tested 7 Oct 2026; parsebird dropped, 1 user) in incremental mode, plus three email alerts per account. | About $5 | Approved (P5, P7); Apify account exists | [stepstone-ireland.md](sites/stepstone-ireland.md) |
| Google Jobs | Not a route for Ireland: Google and SerpApi both leave Ireland out. | n/a | Not used for Ireland | [google-jobs.md](sites/google-jobs.md) |
| Employer job feeds (ATS) | Public no-login feeds: Greenhouse, Lever (global and EU hosts), Ashby, Workable, SmartRecruiters, Teamtailor, Personio, Recruitee, BambooHR; Workday and Eightfold through undocumented endpoints. Workday is the biggest Irish gap. | $0 | Piloted 7 Oct 2026 on six systems (passed) | [ats-feeds.md](sites/ats-feeds.md) |

## Provider table

| Provider | Role here | Accepts an individual? | Cheapest start | File |
|---|---|---|---|---|
| Apify | Long-tail actors (Irish boards, smaller sites). Best user support of any paid option (round 3); risk sits in single Actors, so cap money per run. | No on paper ("business use only"), though any adult can sign up. Options in [eligibility.md](shared/eligibility.md). | Free $5 a month | [apify.md](providers/apify.md) |
| ReefAPI | Trial candidate, free credits only: one key for many engines. Round 3 found no independent customer at all. | Yes on paper; no company named anywhere; its pages disagree on card versus crypto. | 1,000 free credits | [reefapi.md](providers/reefapi.md) |
| Bright Data | Not for this user without a real business. | No: personal projects "are not approved"; licence is for "internal business operations"; it may reuse collected data. | 5,000 free records a month | [bright-data.md](providers/bright-data.md) |
| SerpApi | Search-engine discovery only; not for Reddit content (it is a Reddit defendant). Its Google Jobs engine does not cover Ireland. | Yes: no business clause. | 250 free searches a month | [serpapi.md](providers/serpapi.md) |
| Social data APIs | Single-platform APIs: TwitterAPI.io, SocialData, RedditAPIs.com, ScrapeCreators, SociaVault, Data365, EnsembleData, FxEmbed, Grok X Search. None is sanctioned by the platform it reads. Round 3: TwitterAPI.io and ScrapeCreators have a few real users; the rest too few to judge. | Mostly unknown; see file. | Small free credits | [social-apis.md](providers/social-apis.md) |
| Job data APIs | Company discovery and aggregated listings: TheirStack, Fantastic.jobs, Techmap, Adzuna, Jooble, Coresignal. | Self-serve; see file. | TheirStack 200 free credits a month | [job-data-apis.md](providers/job-data-apis.md) |
| General scraping APIs | Oxylabs, Decodo, Zyte, ScraperAPI, ScrapingBee, ScrapingDog, ScrapFly. Skip unless a gap appears; ScrapFly first if one does. | ScrapingBee and Oxylabs no; ScraperAPI conflicting; Decodo yes. | Trials | [scraping-apis.md](providers/scraping-apis.md) |
| MCP servers | Agent wiring for the providers above, plus X's official MCP; security rules. | n/a | n/a | [mcp-servers.md](providers/mcp-servers.md) |
| Page readers | Parallel, Firecrawl, Exa: read known public pages, not search hostile platforms. Brave Search API is the cheapest general search API found ($5 per 1,000 with a $5 monthly credit). | Yes (Firecrawl's terms limit commercial use) | Already in use | [capabilities/web](../../capabilities/web/README.md) |

## What this spec does not own

- General web search and page reading tools, ladders and compatibility
  verdicts: [capabilities/web](../../capabilities/web/README.md).
- Which connectors a tool has wired: each `adapters/<tool>.md` and
  [capabilities/connectors.md](../../capabilities/connectors.md).
  When a provider is enabled as a live bridge, its wiring goes there and its
  facts stay here.
- Browser automation: [specs/browser-use](../browser-use/spec.md).
- A private job pipeline's sources and settings (separate private repo, not published).

## Proposed record format

No collector exists yet. When one is built, each stored item should keep:
platform, operation, stable ID and URL, content timestamp and retrieval
timestamp, parent and reply links, outbound links, route and provider,
evidence of pagination, omissions and deletions, and a delete-after date.
Social posts are leads, not facts or verified vacancies. Prefer short,
source-linked summaries over a permanent raw archive (see
[shared/rules.md](shared/rules.md) on retention).
