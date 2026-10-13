---
created_at: 2026-10-06
updated_at: 2026-10-06
model: claude-opus-5-5
doc_type: spec
status: researched
scope: SerpApi
purpose: What SerpApi covers, what it costs, whether an individual can use it, and its role here.
related:
  - path: ../spec.md
    why: Owning spec and the provider table.
  - path: ../shared/rules.md
    why: Rules a provider must pass, including terms and data protection.
  - path: ../providers/mcp-servers.md
    why: SerpApi MCP server and the shared MCP security rules.
  - path: ../sites/google-jobs.md
    why: Google Jobs is not a route for Ireland.
  - path: ../sites/reddit.md
    why: Reddit v SerpApi lawsuit.
---

# SerpApi

SerpApi returns search-engine results (Google and others) as structured
JSON. Here it is for discovery only: finding pages through search, not
reading platforms directly. Its Google Jobs engine does not cover
Ireland, so it is not a jobs route for us. It is a defendant in suits by
both Reddit and Google.

## Status

- **Role:** discovery only.
- **Accepts an individual customer:** yes, self-serve signup with a free
  plan (Official doc, https://serpapi.com/pricing, checked 6 October
  2026). Its terms have no business-only clause (checked 6 Oct 2026,
  round 2; see Signup).
- **Allowed today:** no account, no purchase, no pilot. No decision yet.
- **Last checked:** 6 October 2026, by reading the pricing page and the
  Google Jobs countries list (6 October corroboration).

## What it covers

| Platform | Product or endpoint | What it returns | Account or cookies needed | Label |
|---|---|---|---|---|
| Google and other engines | Search APIs | Search results pages as JSON | No | Official doc |
| Google Jobs | `engine=google_jobs` | Google's job results, 10 per page, `next_page_token` paging | No | Official doc (G9); no Ireland |
| YouTube | YouTube video API | Comments and replies with paging | No | Official doc (G2, not rechecked) |
| Reddit, LinkedIn, X, Bluesky, Threads | none native | Only search results that mention them | n/a | Official doc (G2) |

- **Google Jobs excludes Ireland.** SerpApi's supported-countries list
  (https://serpapi.com/google-jobs-countries, checked 6 October 2026) has
  gb, uk, de, fr, nl and others, but no `ie` row. Google's own JobPosting
  page (updated 8 September 2026) lists 14 European countries without
  Ireland (Official doc, 6 October corroboration).
- SerpApi's status page reported "low success rates for the Google Jobs
  API" on 6 October 2026 (Official doc).

## Pricing

- **Plans** (https://serpapi.com/pricing, checked 6 October 2026, Official
  doc): Free $0 for 250 searches a month. Starter $25 for 1,000. Developer
  $75 for 5,000. G2 also lists $150 for 15,000 and $275 for 30,000 (not
  rechecked).
- **Unit:** one search request, not one record.
- **Only successful searches count.** Refund within 7 days if no more
  than 20% was used (6 October corroboration).
- Paid searches do not roll over. Starter is capped at 200 searches an
  hour (Independent report, C2, not rechecked).
- **Worked cost** (Inference): if each search yields about 10 useful
  results, 5,000 results a month is about 500 searches, so Starter at
  $25. 50,000 results is about 5,000 searches, so $75.

## Signup, terms and data protection

- Self-serve, no KYC reported (C2). Exact card requirement for the free
  plan was not found (G2).
- Its terms keep legal and IP duties on the customer (Official doc, G2,
  not rechecked).
- **Individuals:** no business-only clause was found. The terms apply to
  all users and need only that you are "at least the age of majority";
  SerpApi may "refuse service to anyone for any reason at any time".
  Official doc, checked 6 Oct 2026 (round 2), https://serpapi.com/legal.
- **Do not use it to reach Reddit content.** SerpApi is a defendant in
  Reddit v SerpApi, which is about scraping Reddit results out of Google.
  See [sites/reddit.md](../sites/reddit.md).
- The "Legal Shield" covers the Production plan ($150) and up only (6
  October corroboration). It is US-focused; do not assume it covers an
  Irish user (G2).
- **Lawsuits** (Court record and news reports):
  - **Reddit v SerpApi** (S.D.N.Y. 1:25-cv-08736, filed October 2025;
    defendants SerpApi, Oxylabs, AWMProxy, Perplexity). On 31 July 2026
    the court largely denied the motions to dismiss from SerpApi and
    Perplexity. It held that CAPTCHA and bot-detection systems can count
    as access controls under the DMCA. Oxylabs filed its own motion on 21
    July; its reply was due 28 August 2026, so its motion was still
    pending then. The case is in discovery.
    https://www.courtlistener.com/docket/71720563/reddit-inc-v-serpapi-llc
    (6 October corroboration). Buyers of scraped data can be sued, and
    vendor customer lists can be sought in discovery (C3).
  - **Google v SerpApi** (N.D. Cal., filed December 2025). On 20 July 2026
    the court dismissed Google's two DMCA claims, with 21 days to amend
    claims about copyrighted parts. Confirmed from a news report, the
    order itself not opened:
    https://mlq.ai/news/googles-dmca-case-against-serpapi-narrows-after-court-rejects-claims-over-uncopyrighted-search-results
    (6 October corroboration). SerpApi filed a second motion to dismiss on
    25 August 2026 (C2, not rechecked).
  - Risk to us: both suits target SerpApi's collection methods, not its
    customers (Independent report, C2). An adverse ruling could cut its
    coverage (Inference).

## Reliability evidence

- Long track record. Trustpilot 104 reviews, 97% five-star; G2 29
  reviews, top complaint "High Costs" (Independent report, C2, not
  rechecked).
- A 9 February 2026 Trustpilot review described successful personal
  automation (Independent report, G2, not rechecked).

## Agent integration

- REST and official SDKs in several languages, including Node examples
  (Official doc, C2 and G2).
- SerpApi MCP (https://github.com/serpapi/serpapi-mcp): one `search` tool;
  latest release v2.0.0, 22 September 2026 (Official doc, G9). Add only
  if search discovery is a measured gap. General search is already owned
  by ~/agents/capabilities/web/README.md. See
  ~/agents/specs/web-scraping-site-access/providers/mcp-servers.md.
- Spend caps: the plan's search quota is the cap.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | Use SerpApi Starter with `gl=ie` for Irish Google Jobs (C1, C2, G9) | Google Jobs and SerpApi both exclude Ireland | https://serpapi.com/google-jobs-countries, checked 6 Oct 2026 |
| 2026-10-06 | All four defendants' motions in Reddit v SerpApi were "predominately denied" (C3) | Denied for SerpApi and Perplexity; Oxylabs's motion was still being briefed | CourtListener docket, checked 6 Oct 2026 |
| 2026-10-06 | No verified price (earlier note) | Free 250, Starter $25 for 1,000, Developer $75 for 5,000 | https://serpapi.com/pricing, checked 6 Oct 2026 |
| 2026-10-06 | No first-party MCP found (G2) | SerpApi MCP v2.0.0, 22 Sep 2026 | G9 |

## Open questions

1. What do SerpApi's terms say about customer liability in full? Round 2
   confirmed only that there is no business-only clause.
2. Answered 6 Oct 2026: on 1 October the judge said Oxylabs' motion to
   dismiss in Reddit v SerpApi is unlikely to succeed (see reddit.md).
3. Is search discovery through SerpApi better than the search tools we
   already have? Only a measured gap would justify it.

## Sources

- Deep research round 1 (5 October 2026; private, not published),
  reports C2, C3, G2 and G9, plus the 6 October corroboration.
- https://serpapi.com/pricing, accessed 6 October 2026.
- https://serpapi.com/google-jobs-countries, accessed 6 October 2026.
- https://serpapi.com/google-jobs-api, accessed 5 October 2026 (G2, G9).
- https://www.courtlistener.com/docket/71720563/reddit-inc-v-serpapi-llc,
  accessed 6 October 2026.
- https://www.lexology.com/library/detail.aspx?g=a4fa98e5-85cf-4f8a-a98d-2d9d2ccc7c53,
  accessed 6 October 2026.
- https://github.com/serpapi/serpapi-mcp, accessed 5 October 2026 (G9).
- Earlier note: ~/agents/capabilities/web/README.md, row
  "SerpAPI".
