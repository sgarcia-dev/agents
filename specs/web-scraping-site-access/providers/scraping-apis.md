---
created_at: 2026-10-06
updated_at: 2026-10-06
model: claude-opus-5-5
doc_type: spec
status: researched
scope: General scraping APIs (Oxylabs, Decodo, Zyte, ScraperAPI, ScrapingBee, ScrapingDog, ScrapFly) and hosted browsers seen in round 3
purpose: What each general hosted scraping API covers, what it costs, whether an individual can use it, and why the default role is skip.
related:
  - path: ../spec.md
    why: Owning spec and the provider table.
  - path: ../shared/rules.md
    why: Rules a provider must pass, including terms and data protection.
  - path: ../sites/reddit.md
    why: Decodo sells Reddit tools; Oxylabs is a Reddit defendant.
  - path: ../sites/stepstone-ireland.md
    why: A hosted URL fetcher is one possible Irish-board fallback.
  - path: ../sites/indeed.md
    why: Several of these advertise Indeed as a target.
---

# General scraping APIs

Hosted services that fetch a URL for us through their own proxies and
browsers, and sometimes parse it. They are not social data APIs: none
gives clean keyword search and full reply trees across our platforms. We
already have page readers (Parallel, Firecrawl, Exa), so these add little.

**Default role for the whole group: skip unless a measured gap appears.**
A measured gap means a dated Observed test where our current readers fail
on a page we need and one of these succeeds.

Sources: deep research round 1 (5 October 2026; private, not published), report G2 sections 3.3 to 3.8 and its cost table, report G9,
plus the 6 October corroboration. Every line here is from a report and
not rechecked unless it says so.

Our existing page readers, owned elsewhere:
`~/agents/capabilities/web/tools/parallel.md`,
`~/agents/capabilities/web/tools/firecrawl.md`,
`~/agents/capabilities/web/tools/exa.md`.

## Status

- **Role:** skip unless a measured gap appears (all seven). ScrapFly,
  added in round 3, is the one with real user support and is first in
  line if a gap appears.
- **Allowed today:** no account, no trial, no purchase, no pilot.
- **Last checked:** 5 October 2026 by report G2. The 6 October
  corroboration rated the group "skip" and confirmed the ScraperAPI
  LinkedIn credit cost. Round 2 (6 October) checked the eligibility
  wording of Oxylabs, ScraperAPI and ScrapingBee. Who accepts an
  individual, across all providers, is summarised in
  [shared/eligibility.md](../shared/eligibility.md).

## Providers

### Oxylabs

- **Covers:** hosted fetch and parse; Indeed and Google Jobs advertised.
  No social search or full comment trees found. Official MCP exists.
- **Price:** entry $49 a month; "other" targets $1.15 per 1,000 (Micro),
  $1.10 (Starter); JavaScript costs more. 2,000-result no-card trial
  (https://oxylabs.io/products/scraper-api/web, 5 Oct 2026).
- **Individual eligibility:** effectively business only. "Every customer
  has to answer a KYC questionnaire to get access to our solutions";
  "Only 75% of customers are approved"; the questionnaire asks for a
  "Registered company name" and "Date of incorporation"
  (https://oxylabs.io/kyc-and-safety, checked 6 Oct 2026, round 2). Its AI
  Studio terms do let an individual contract, but KYC still applies.
- **Legal:** a defendant in Reddit v SerpApi. On 1 October 2026 the judge
  said he is unlikely to grant its motion to dismiss (see
  [sites/reddit.md](../sites/reddit.md));
  (https://www.businessinsider.com/reddit-lawsuit-perplexity-ai-firms-data-scrapers-scraping-google-2025-10,
  Independent report). Another reason to keep it away from Reddit work.
- **Reliability:** September 2026 Trustpilot reviews mixed, mostly about
  proxies.
- **Label:** Official doc and Independent report.

### Decodo (formerly Smartproxy)

- **Covers:** hosted scraping API; MCP with `reddit_post`,
  `reddit_subreddit` and `reddit_user` tools (G9). Indeed advertised.
- **Price:** free plan 2,000 standard requests or about 667 premium plus
  JavaScript; paid from $19 a month for 38,000 standard or about 12,000
  premium requests; also $49 and $99 (https://decodo.com/scraping/web/pricing,
  5 Oct 2026).
- **Individual eligibility:** licence names research, personal and
  commercial use (https://decodo.com/legal/license-agreement, report G2,
  not rechecked in round 2). The only one in this group that clearly
  allows personal use.
- **Reliability:** Trustpilot reviews from September 2026, mixed.
- **Label:** Official doc.

### Zyte

- **Covers:** hosted fetch and extraction, including job postings.
- **Hard limit:** its acceptable-use policy bans LinkedIn scraping
  (https://www.zyte.com/terms-policies/acceptable-use-policy/, Official
  doc). Fine for us, since agents do not read LinkedIn anyway.
- **Price:** pay as you go, HTTP $0.13 to $1.27 per 1,000; browser $1.01 to
  $16.08 per 1,000; $5 trial credit (https://www.zyte.com/pricing/, 5 Oct
  2026). Some browser features need business verification.
- **Label:** Official doc.

### ScraperAPI

- **Covers:** hosted URL fetch and some structured APIs.
- **Price:** $49 a month for 100,000 credits; 7-day 5,000-credit no-card
  trial. LinkedIn requests cost 30 credits (https://www.scraperapi.com/pricing/,
  5 Oct 2026; LinkedIn cost confirmed by the 6 October corroboration).
- **Individual eligibility: two terms pages conflict.** scraperapi.com
  says "1.4 – This Platform is for use by businesses and not consumers"
  (page dated 10 Nov 2025). A Traject Data copy (dated 18 Nov 2025)
  covers "individuals who purchase a Subscription" for "personal use".
  Neither says which wins. Treat it as business only until clarified.
  Official doc, checked 6 Oct 2026 (round 2),
  https://www.scraperapi.com/terms/,
  https://trajectdata.com/traject-data-terms-of-service/.
- **Reliability:** no recent independent report found.
- **Label:** Official doc.

### ScrapingBee

- **Covers:** hosted HTML and browser fetch; a Google Jobs scraper (not
  useful for Ireland; see
  `~/agents/specs/web-scraping-site-access/providers/job-data-apis.md`).
- **Price:** $49 a month for 250,000 credits; JavaScript requests 5
  credits, stealth up to 75; 1,000 free credits, no card
  (https://www.scrapingbee.com/pricing/, 5 Oct 2026).
- **Individual eligibility: no.** "Use of the API or the Services for
  personal purposes is strictly forbidden." The terms (last updated 15
  July 2024) say consumer law is not meant to apply. Operator: VostokInc,
  Paris. It offers a DPA and acts as processor. Official doc, checked 6
  Oct 2026 (round 2), https://www.scrapingbee.com/terms-and-conditions/.
- **Label:** Official doc.

### ScrapingDog

- **Covers:** dedicated APIs for LinkedIn, Indeed, Google Jobs, X
  profiles and posts, YouTube comments. No X keyword search or full reply
  trees found. LinkedIn endpoints are out of bounds for us.
- **Price:** $40 a month for 200,000 credits, then $90 for 1 million;
  structured calls 5 credits; 100 free credits
  (https://www.scrapingdog.com/pricing/, 5 Oct 2026).
- **Reliability:** May 2026 Trustpilot reviews, mixed.
- **Label:** Official doc.

### ScrapFly (added round 3, 6 October 2026)

- **Status:** first candidate if a measured gap appears. Report G19
  calls it "the strongest new paid service I found".
- **Covers:** URL fetch with JavaScript rendering, anti-bot unblocking and
  residential proxies. A fetch layer, not a social data API.
- **Price:** Discovery $30 a month for 200,000 credits; "1,000 free
  credits, no credit card"; a plain request costs the base credit,
  "+ JS rendering or Unblocker" 5 credits, "+ residential proxies" 25
  credits (https://scrapfly.io/pricing, checked 6 Oct 2026). On protected
  sites the real cost per page is 5 to 30 times the base.
- **What users say:** four independent opinions (two organic G2 reviews,
  two Reddit comments, one saying "way less maintenance"). Several come
  from one Reddit thread, so they are less independent than they look
  (G19, not rechecked).
- **Individual eligibility:** not checked.
- **Label:** Official doc (price), Independent report (opinions).

### Hosted browsers and open-source tools (round 3, for reference)

Browser automation itself is owned by
[specs/browser-use](../../browser-use/spec.md).
These came up in G19 as scraping building blocks; none is a social data
source.

- **Browserbase:** Developer plan $20 a month, 100 browser hours, then
  $0.12 an hour, "with a one-minute and one-MB minimum per session"
  (https://www.browserbase.com/pricing,
  https://docs.browserbase.com/account/billing/plans, checked 6 Oct
  2026). Two user opinions. Short sessions cost a full minute each.
- **Browserless:** "Free $0/month - 1k units/month", a unit being up to
  30 seconds of browser time; paid from $25 a month
  (https://www.browserless.io/pricing, checked 6 Oct 2026). Mixed user
  opinions (sessions that "silently die").
- **Playwright** (plus its MCP and CLI), **Camoufox** (anti-detect
  Firefox, "under development"), **Crawl4AI** (LLM-oriented crawler):
  free, with 3 to 5 favourable user opinions each (G19, not rechecked).
  Camoufox is an anti-detect tool; for our own requests it falls under
  rule 12 in shared/rules.md (no anti-detect tools for our own
  requests; P2).

## Rough cost (G2 cost table, Inference)

At 2,000 / 20,000 / 200,000 ordinary requests a month, 5 Oct 2026 prices:
Oxylabs $49 / $49 / about $220; Decodo $0 / $19 / $99; Zyte $0.26-2.54 /
$2.60-25.40 / $26-254; ScraperAPI $49 / $49 / $149; ScrapingBee $49 / $49
/ $99; ScrapingDog $40 / $40 / $90. Hard sites cost far more: ScraperAPI
at the LinkedIn rate becomes $49 / $149 / $975.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | ScrapingBee eligibility "unclear for us" (our file). | Its terms forbid personal use outright. | ScrapingBee terms, round 2 corroboration W03 |
| 2026-10-06 | Oxylabs KYC rules "not found" (our file). | Every customer goes through KYC; 75 percent approved; company details asked. | Oxylabs KYC page, round 2 |

## Open questions

1. Is there any page our current readers fail on that one of these
   fetches? Without that measured gap, nothing here is worth an account.
   Answer: an Observed test recorded per
   `~/agents/specs/web-scraping-site-access/shared/evaluation.md`.
2. Would Decodo's hosted fetch read Jobs.ie, which blocks plain HTTP?
   Answer: a free-trial Observed test, only after a user decision.

## Sources

- https://oxylabs.io/products/scraper-api/web (5 Oct 2026)
- https://decodo.com/scraping/web/pricing, https://decodo.com/legal/license-agreement (5 Oct 2026)
- https://www.zyte.com/pricing/, https://www.zyte.com/terms-policies/acceptable-use-policy/ (5 Oct 2026)
- https://www.scraperapi.com/pricing/ (5 Oct 2026; checked 6 Oct)
- https://www.scrapingbee.com/pricing/, https://www.scrapingbee.com/terms-and-conditions/ (5 Oct 2026)
- https://www.scrapingdog.com/pricing/ (5 Oct 2026)
- https://www.businessinsider.com/reddit-lawsuit-perplexity-ai-firms-data-scrapers-scraping-google-2025-10
- https://oxylabs.io/kyc-and-safety, https://www.scraperapi.com/terms/, https://trajectdata.com/traject-data-terms-of-service/ (6 Oct 2026, round 2)
- https://scrapfly.io/pricing, https://www.browserbase.com/pricing, https://docs.browserbase.com/account/billing/plans, https://www.browserless.io/pricing (6 Oct 2026, round 3 check V6)
- Deep research rounds 1 to 3 (5 and 6 October 2026; private, not published), reports G2, G9, C5 and G19; all corroboration rounds.
