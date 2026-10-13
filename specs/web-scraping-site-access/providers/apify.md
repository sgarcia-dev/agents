---
created_at: 2026-10-06
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: spec
status: piloted
scope: Apify
purpose: What Apify covers, what it costs, whether an individual can use it, and its role here.
related:
  - path: ../spec.md
    why: Owning spec and the provider table.
  - path: ../shared/rules.md
    why: Rules a provider must pass, including terms and data protection.
  - path: ../providers/mcp-servers.md
    why: Apify MCP server and the shared MCP security rules.
  - path: ../sites/linkedin.md
    why: Dami, HarvestAPI and Bebity Actors for LinkedIn posts and jobs.
  - path: ../sites/reddit.md
    why: Reddit Actors.
  - path: ../sites/threads.md
    why: Threads Actors.
  - path: ../sites/indeed.md
    why: Indeed Actors.
  - path: ../sites/x.md
    why: API Dojo X Actors.
  - path: ../sites/stepstone-ireland.md
    why: parsebird Jobs.ie and IrishJobs.ie Actors.
  - path: ../sites/google-jobs.md
    why: Google Jobs Actors exist, but Google Jobs does not cover Ireland.
---

# Apify

Apify is a marketplace of site-specific scrapers called Actors, run on
Apify's servers and billed to one account. Here it is the long-tail
filler: LinkedIn posts, the Irish job boards and Threads, which no other
provider covers well. The headline problem is eligibility. Apify's terms
say the service is for business use only, yet any adult human can open a
free account. Two round 2 reports disagreed on whether the user can sign
up honestly (see
[shared/eligibility.md](../shared/eligibility.md)).
The user decided on 6 October 2026 (P1) to sign up as a business. Which
providers to pay long term waits on user-opinion research (P13).

## Status

- **Role:** long-tail filler and pilot candidate (P9 part 2). Eligibility settled by P1: the user signs up as a business.
- **What users say (round 3, 6 October 2026):** the best-supported paid
  option in every user-opinion report (G10, G11, G18, G19). Apify itself
  is real and support is decent. The risk lives in single Actors: they
  break when a site blocks them, some ignore item limits, and bills are
  hard to predict. Use a hard money cap on every run, keep a second Actor
  ready for each job, and do not prepay past Starter before measuring
  cost per 1,000 items. Detail under Reliability evidence.
- **Accepts an individual customer:** unclear. The General Terms (effective
  9 July 2026) say: "The Services are intended for business use only and
  are not designed, marketed, or suitable for consumers."
  https://docs.apify.com/legal/general-terms-and-conditions (Official doc,
  checked 6 October 2026). Yet a free plan exists. "Personal Account" is
  just Apify's name for any human user's login: "Personal Accounts must be
  created by humans, and you must be at least 18 years old" (s.4.1.1).
  Apify does not define "business use". Official doc, checked 6 Oct 2026
  (round 2). Report C5 reads the clause as a consumer-law shield tied to
  Czech law (s.16.9, s.16.10); report C10 reads it as a reason not to sign
  up as a private person. See [shared/eligibility.md](../shared/eligibility.md).
- **Allowed today:** the user may create the business account (P1). No purchase or pilot yet; the free-credit pilot runs in P9 part 2.
- **Last checked:** 6 October 2026, by reading the pricing page and the
  General Terms (round 1 and round 2 corroboration).

## Observed test (7 October 2026)

- **Account:** created 7 Oct 2026 on the free plan ($5 a month, hard
  cap $5, data kept 7 days). The API token lives in a keychain, never in files.
- **11 capped runs, $0.27 in total:** 9 returned real data, 1 was weak,
  1 failed. Results per platform are in each site file. A01_apify record (private, not published).
- **Choose Actors by Store data, not by research mentions.** The public
  Store API (`/v2/store?search=...&sortBy=popularity`, no token) gives
  monthly users, rating, number of ratings, 30-day run outcomes and
  pricing. `tools/store_rank.py` in the record's bundle ranks them. Most
  users is not enough: the top two X Actors are the $320 duplicate case
  and the placeholder-tweet case.
- **Caps:** pass `maxItems` and `maxTotalChargeUsd` on every run, plus
  `timeout` and `memory`. Apify's monthly usage figure lags behind runs,
  so a budget check on it reacts late; the per-run cap is the guard.
- **Billing was lower than list prices** on this run: several Actors
  billed only their start fee. Measure cost per 1,000 on a bigger run
  before trusting it.

## What it covers

Each Actor is written by a different author. Quality, limits and failure
modes vary per Actor, so Apify is a shared billing and run account, not
one reliable data service (Inference, report G1).

| Platform | Product or endpoint | What it returns | Account or cookies needed | Label |
|---|---|---|---|---|
| LinkedIn posts | Dami, HarvestAPI post search | Public posts by keyword; shallow comments | No | Vendor claim, Dami checked 6 Oct |
| LinkedIn Jobs | HarvestAPI, Bebity | Job listings with full description | No | Vendor claim, checked 6 Oct |
| Jobs.ie, IrishJobs.ie | parsebird, Black Falcon Data | Irish job listings | No | Vendor claim, parsebird checked 6 Oct |
| Reddit, X, Threads, Bluesky, Mastodon, HN, Indeed, Glassdoor, Google Jobs | Several Actors each | See the Actor table below | No, for the Actors listed | Vendor claim (G1, not rechecked) |

## Store Actors by platform

**Tested picks, 7 October 2026** (chosen by Store monthly users, rating
and 30-day success rate; see "Observed test" above). Prefer these over
the research-era rows below:

| Platform | Use first | Second | Avoid |
|---|---|---|---|
| Reddit | harshmaur/reddit-scraper (3,869 monthly users, 99% runs succeed) | trudax/reddit-scraper-lite (weak in our test) | |
| X (search) | apidojo/twitter-scraper-lite (4.76 from 101) | | apidojo/tweet-scraper ($320 duplicates), kaitoeasyapi (placeholder tweets) |
| LinkedIn jobs | curious_coder/linkedin-jobs-scraper (17,709 users) | valig/linkedin-jobs-scraper | Post and profile Actors (P10, rule 11) |
| Indeed | valig/indeed-jobs-scraper ($0.10 per 1,000) | borderline/indeed-scraper | |
| Glassdoor | valig/glassdoor-jobs-scraper | | |
| IrishJobs | blackfalcondata/irishjobs-scraper | | memo23/stepstone-group-scraper (0 results, charged), parsebird (1 user) |
| Jobs.ie | blackfalcondata/jobs-ie-scraper | | parsebird (fewer users) |

The research-era table follows.

Prices are per 1,000 results from report G1 (5 October 2026), at Starter
rate with the Free rate in brackets where it differs, unless the note says
it was checked on 6 October. Many Actors also charge a small fee per run
start. "No-login" means the author says no personal login or cookies.

| Platform | Actor | Price | No-login | Notes | Label |
|---|---|---|---|---|---|
| LinkedIn posts | dami_studio/linkedin-post-search-scraper | $0.89 ($0.90 Free), plus $0.003 per run start | Yes | About 90 posts per phrase, 1,000 per run. $5 free covers about 5,500 posts. Uses Google-indexed discovery, so it samples | Vendor claim, checked 6 Oct |
| LinkedIn posts | harvestapi/linkedin-post-search | Listing "from $1.50 / 1,000 posts" (best tier); its README still says $2 | Yes | Comments and reactions cost more. Vendor: LinkedIn gives "up to 400-500 posts per query", so split queries. Users report missing posts and a run that kept going past its $2 cap (fixed, vendor says) | Vendor claim, checked 6 Oct (round 3) |
| LinkedIn comments | harvestapi/linkedin-post-comments | $2 | Yes | Post URL in, comments out. Up to 5 replies per comment | Vendor claim (G1, W03) |
| LinkedIn Jobs | harvestapi/linkedin-job-search | $1, plus $0.001 per run | Yes | Keyword, company and location search | Vendor claim, checked 6 Oct |
| LinkedIn Jobs | curious_coder/linkedin-jobs-scraper | $1 | Yes (no cookie field in its input) | 168K total users, 18K monthly, 4.6 from 141 ratings. Store numbers only, no outside reviews | Vendor claim, checked 6 Oct (round 3) |
| LinkedIn Jobs | bebity/linkedin-jobs-scraper | Live page says "from $1.00"; G1 says $1.25 ($1.50 Free) | Yes | Rebuilt September 2026. Returns recruiter name, which is personal data | Vendor claim, checked 6 Oct |
| Jobs.ie | parsebird/jobs-ie-scraper | $0.99 on Free, $0.79 on Gold, plus a start fee | Yes | Irish residential proxy. `postedWithinDays` filter | Vendor claim, checked 6 Oct |
| Jobs.ie | blackfalcondata/jobs-ie-scraper | $1.10, plus start fee and platform usage | Yes | Takes single job URLs. 43 total users, 14 monthly. Has incremental mode but no posted-within time window | Vendor claim, checked 6 Oct (round 3) |
| IrishJobs.ie | parsebird/irishjobs-scraper | $0.99 on Free, $0.79 on Gold | Yes | README now says compute and Irish residential proxy are included in the per-job price; 1 user | Vendor claim, checked 6 Oct (round 2) |
| IrishJobs.ie | blackfalcondata/irishjobs-scraper | $1.45, plus start fee and platform usage | Yes | 155 total users, 43 monthly, against parsebird's 1. Platform usage is billed on top, so prices are not directly comparable with parsebird | Vendor claim, checked 6 Oct (round 3) |
| Reddit | harshmaur/reddit-scraper | $1.80 ($2 Free), plus $0.02 per start | Yes | Posts, comments, replies, profiles | Vendor claim (G1, not rechecked) |
| Reddit | themineworks/reddit-scraper | $1.50 ($2 Free), plus $0.005 per start | Yes | Comments bundled with posts | Vendor claim (G1, not rechecked) |
| Reddit | bovi/reddit-scraper | $1.98 ($2 Free) | Yes | Reads the Arctic Shift archive, not live | Vendor claim (G1, not rechecked) |
| X | apidojo/twitter-scraper-lite (Unlimited) | $0.016 per query, then $0.40 | Yes | One tweet by URL costs about $0.05 | Vendor claim (G1, not rechecked) |
| X | apidojo/tweet-scraper (V2) | $0.40 | Yes | Rules exclude single-tweet and reply scraping. Set `maxItems` to at least 50 or its rate limiter may block the run (vendor). One user reports six runs that cost about $320 and returned 316,871 rows with only 592 unique tweets | Vendor claim and one user report, checked 6 Oct (round 3) |
| X | kaitoeasyapi/twitter-x-data-tweet-scraper-pay-per-result-cheapest | about $0.18 | Yes | Avoid for research: it returned paid placeholder tweets when nothing matched; the developer admitted it and said it will switch to an empty result with a "no results" flag | Review and vendor reply, checked 6 Oct (round 3) |
| Threads | futurizerush/meta-threads-scraper | $2.50, plus $0.005 per start | Yes | "Replies" means the author's replies, not full threads | Vendor claim (G1, not rechecked) |
| Threads | themineworks/threads-scraper | $1.80 ($2 Free) | Yes | No full conversation traversal | Vendor claim (G1, not rechecked) |
| Bluesky | inn_corp/bluesky-post-search | "from $1.00 / 1,000" retrieved posts, plus a per-query fee | Yes | A successful search that matches nothing "still counts as a processed query"; only failed queries are free | Vendor claim, checked 6 Oct (round 3) |
| Bluesky | lexis-solutions/bluesky-posts-scraper | $0.92 ($1.10 Free), plus platform usage | Yes | | Vendor claim (G1, not rechecked) |
| Bluesky | s0rgcl/bluesky-scraper | $1, plus platform usage | Yes | | Vendor claim (G1, not rechecked) |
| Bluesky | ethanteague/bluesky-scraper | n/a | No | Needs your own app password. Unsuitable | Vendor claim (C2, not rechecked) |
| Mastodon | goat255/mastodon-scraper | $0.44 | Yes | | Vendor claim (G1, not rechecked) |
| Mastodon | dami_studio/mastodon-scraper | $1.48 ($1.50 Free) | Yes | | Vendor claim (G1, not rechecked) |
| Hacker News | fetchsmith/hacker-news-scraper | $0.17 ($0.20 Free) | Yes | HN has free official APIs anyway | Vendor claim (G1, not rechecked) |
| Indeed | borderline/indeed-scraper | $5 | Yes | Documents Ireland country code `ie` | Vendor claim (G1, not rechecked) |
| Indeed | misceres/indeed-scraper | $5 ($6 Free) | Yes | Ireland support not found | Vendor claim (G1, not rechecked) |
| Glassdoor | bebity/glassdoor-jobs-scraper | $0.35 ($0.40 Free) | Yes | | Vendor claim (G1, not rechecked) |
| Google Jobs | epctex/google-jobs-scraper | $4.50, plus platform usage | Yes | Google Jobs does not cover Ireland | Vendor claim (G1, not rechecked) |

Known breakage: comchat/reddit-api-scraper has an issue titled "AVOID!
Stopped working on 2026-05-27" (Independent report, C2, not rechecked).
In early June 2026 most LinkedIn post Actors broke for about two days at
once, and one was deleted afterwards
(https://www.reddit.com/r/apify/comments/1tvztoy/, G10, not rechecked).
HarvestAPI's profile-search Actor uses HarvestAPI's own LinkedIn
accounts, which "LinkedIn periodically blocks" (vendor reply, checked
6 Oct 2026). So "no cookies" can still mean someone's accounts.

## Pricing

- **Plans** (https://apify.com/pricing, checked 6 October 2026, Official
  doc): Free $0 with $5 of usage a month and no card. Starter $19 a month
  ($17 on annual billing) including $19 of usage. G1 also lists Scale $199
  and Business $999 (not rechecked).
- **Platform rates on Free and Starter:** residential proxy "$8 / GB",
  compute "$0.2 / CU" (Official doc, checked 6 Oct 2026, round 2). These
  matter when an Actor bills platform usage on top of its per-result fee.
- **How the bill works** (Official doc, G1): the plan fee buys the same
  amount of usage. Actor fees and platform usage draw it down. So $8 of
  usage on Starter is a $19 bill, not $27 (Inference, G1).
- **Unused usage expires.** "Prepaid usage (credits) expires at the end
  of each billing period and doesn't roll over to the next period"
  (https://help.apify.com/en/articles/13671754-navigating-apify-billing,
  updated 2 Sep 2026, checked 6 Oct 2026).
- **Rental Actors are gone.** "October 1 - Rental Actors are fully
  retired"; the rest moved to pay-per-usage
  (https://docs.apify.com/actors/running/actors-in-store, checked 6 Oct
  2026). Older reports' rental prices are void.
- **Actors are not Apify's product.** "Unless expressly stated otherwise,
  Actors are not part of the Services provided by Apify" (General Terms
  s.3.1, effective 9 July 2026, checked 6 Oct 2026). Apify can be fine
  while the Actor we pay for is broken.
- **Fees are non-refundable** (s.7.4) and VAT is added (s.7.8, Apify is a
  Czech VAT payer). Report C5; s.7.4 was not visible in the round 2
  check.
- **Failed runs are not free.** A failed run may already have paid start,
  query or result fees. No platform-wide refund rule was found (G1, not
  rechecked). Users report Actors that ignored limits, billed duplicates,
  or charged a start event twice, with "no meaningful resolution or
  refund" in one case (Reddit 9 Apr 2026, Trustpilot 29 Sep 2026, Apify
  issues; G10, G11, G18, not rechecked).
- **Worked cost** (Inference): at about 5,000 records a month on Actors
  priced near $1 per 1,000, usage is about $5 to $15, possibly inside the
  free $5 (C2). At about 50,000 records, about $50 to $150 (C2).

## Signup, terms and data protection

- **Business only:** see the quote under Status. This is the blocker.
- **KYC:** none reported for signup. No card for the free plan (Official
  doc, checked 6 October).
- **Customer carries legal risk** (General Terms, Official doc, C3): "You
  are solely responsible for the legality, accuracy, quality,
  appropriateness, and use of all Customer Data." Using Actors on
  "unauthorized sources" makes you liable for damages and third-party
  claims.
- **Data protection:** the DPA is incorporated into the General Terms.
  It says the customer is controller or processor and Apify is a
  (sub)processor. https://docs.apify.com/legal/data-processing-addendum
  (Official doc, C3 and C5).
- **Your data, its usage data.** "you retain all right, title, and
  interest in and to your Customer Data" (s.5.8). But "Usage Data",
  which includes "information derived from Actor Inputs, Actor Outputs,
  and your Customer Data", "shall belong exclusively to us" (s.1.8,
  s.5.9). "Your inputs and the resulting outputs are not used to train
  any foundation model" (s.5.10). Official doc, checked 6 Oct 2026
  (round 2).
- **Law and refusal.** Czech law and Czech courts (s.16.9 to s.16.12);
  an EU Data Act Addendum applies "if your headquarters and billing
  address are located within the European Union" (s.16.13). Apify may
  "refuse access to our Website or Services to anyone for any reason at
  any time" (s.15.1). Legal notices go to legal@apify.com (s.16.5.2).
  Official doc, checked 6 Oct 2026 (round 2).
- **No refusal reports.** No public report was found of Apify closing an
  individual's account for not being a business. Reviews show many solo
  users. Independent report, report C5; "not found" is not proof.
- **Where traffic leaves from:** Actors run on Apify's servers and proxies,
  not the home IP (Inference, C2).

## Reliability evidence

- Trustpilot 4.8 from about 765 reviews, G2 4.7 from 645 (Independent
  report, C2, not rechecked). Weigh Trustpilot low: a reviewer wrote
  "Apify invited me to review and offered a $20 reward for reviews on
  four sites and a GitHub star" (review dated 19 Sep 2026), while the page
  banner says "No recent history of asking for reviews"
  (https://www.trustpilot.com/review/apify.com, checked 6 Oct 2026).
- **What users say (round 3):** about 12 independent complaints about
  hard-to-predict bills, about 6 about Actor breakage, about 5 positive on
  support (G11, mostly G2 and Reddit). The usual failure is a target site
  blocking the Actor (Reddit from late May 2026, Apollo in 2025). Some
  users moved stable targets to their own Scrapy or Crawlee scripts. No
  firsthand report of Apify closing a buyer's account or of a platform
  suing an Apify customer was found.
- Outages: an Actor-run incident on 22 Sep 2026 on the official status
  page, and 8 incidents in 90 days by IsDown's count, some multi-hour
  proxy slowdowns (G11, not rechecked).
- Reddit Scraper Lite timed out on 6.9% of runs over 30 days, per
  use-apify.com, 9 September 2026 (Independent report, C2, not rechecked).
- No independent success rate exists for any single Actor named above.
  Displayed run success is the vendor's own number (G1).
- No lawsuit naming Apify by a platform on our list was found (G1).

## Agent integration

- REST API, official `apify-client` Node SDK, saved tasks, schedules with
  time zones, and webhooks (Official doc, G1 and C2).
- Hosted MCP server at https://mcp.apify.com. Latest release v0.17.2, 5
  October 2026 (Official doc, G9). It can expose only chosen Actors. Use
  an allowlist of checked no-cookie Actors. See
  ~/agents/specs/web-scraping-site-access/providers/mcp-servers.md.
- **Spend caps:** set the account limit in Billing, then Limits. "There
  may be a deviation of up to 10% in your actual spending." Maximum
  limits: Free $5, Starter $100, Scale $1,000, Business $5,000
  (https://help.apify.com/en/articles/11079614-reaching-platform-limits,
  checked 6 Oct 2026). The Free plan stops when the $5 runs out.
- **Per-run caps:** `maxItems` is not a money control; users report
  Actors that ran past it. Set the run's maximum total charge instead.
  For pay-per-event Actors "The limit is per run, not per user", so
  parallel runs add up; authors can force a minimum
  (`minimalMaxTotalChargeUsd`)
  (https://docs.apify.com/actors/publishing/monetize/pay-per-event,
  checked 6 Oct 2026). Rule for us: one run at a time per Actor, a
  per-run charge cap, and `maxItems` as well.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | Starter costs $29 or $39 a month (older third-party reviews) | Starter is $19 a month, $17 on annual billing | https://apify.com/pricing, checked 6 Oct 2026 |
| 2026-10-06 | Jobs.ie Actor "from $0.79" as the working price (report C1) | $0.79 is the Gold plan. Free is $0.99 plus a start fee | https://apify.com/parsebird/jobs-ie-scraper, checked 6 Oct 2026 |
| 2026-10-06 | Apify is a safe primary for an individual (reports C1, G1) | Terms say business use only. Role is pending | General Terms, effective 9 Jul 2026 |
| 2026-10-06 (round 3) | inn_corp Bluesky Actor charges for zero-result searches (G1); round 3 report said that was outdated. | Successful zero-match searches are still charged; only failed ones are free. | Actor page, round 3 check V1 |
| 2026-10-06 (round 3) | HarvestAPI LinkedIn post search costs $2 per 1,000 (G1). | Listing says from $1.50 (best tier); README still says $2. | Actor page, round 3 check V2 |
| 2026-10-06 (round 3) | HarvestAPI profile search costs $50 per 1,000 profiles (G17). | $50 per 1,000 search-page results ($0.10 a page of up to 25); scraped profiles are $4 (short) or $8 (full) per 1,000. | Actor page, round 3 check V2 |
| 2026-10-06 | Section 2.1 offers a free tier on a "Personal Account" (our round 1 note, from C5's draft) | The Personal Account rule is s.4.1.1 ("created by humans ... at least 18"); s.2.1 text was not found | General Terms, round 2 corroboration W03 |

## Open questions

1. Answered 6 Oct 2026 by the user's P1 decision: sign up as a business,
   no written confirmation from Apify needed.
2. Answered 6 Oct 2026: yes, prepaid usage expires each billing period.
3. Answered 6 Oct 2026: the parsebird IrishJobs page now says proxy and
   compute are included.
3. Is there any independent success-rate data from the last 90 days for
   Dami's LinkedIn Actors?

## Sources

- Deep research rounds 1 and 2 (5 and 6 October 2026; private, not published), reports G1, C2, C3, C5, C10 and G9, plus both
  corroboration rounds.
- https://apify.com/pricing, accessed 6 October 2026.
- https://docs.apify.com/legal/general-terms-and-conditions, accessed 6
  October 2026.
- https://apify.com/dami_studio/linkedin-post-search-scraper, accessed 6
  October 2026.
- https://apify.com/bebity/linkedin-jobs-scraper, accessed 6 October 2026.
- https://apify.com/parsebird/jobs-ie-scraper and
  https://apify.com/parsebird/irishjobs-scraper, accessed 6 October 2026.
- https://help.apify.com/en/articles/11079614-reaching-platform-limits,
  accessed 5 October 2026 (G1).
- https://github.com/apify/actors-mcp-server, accessed 5 October 2026 (G9).
- Earlier note: ~/agents/capabilities/web/README.md, section
  "Other services retained from September research".
