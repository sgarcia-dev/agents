---
created_at: 2026-10-06
updated_at: 2026-10-06
model: claude-opus-5-5
doc_type: spec
status: researched
scope: Social data APIs (TwitterAPI.io, SocialData, RedditAPIs.com, ScrapeCreators, Data365, EnsembleData, SociaVault, FxEmbed, xAI Grok X Search)
purpose: What each third-party social data API covers, what it costs, whether an individual can use it, and the role we give it.
related:
  - path: ../spec.md
    why: Owning spec and the provider table.
  - path: ../shared/rules.md
    why: Rules a provider must pass, including terms and data protection.
  - path: ../sites/x.md
    why: X routes that use TwitterAPI.io, SocialData, FxEmbed and Grok.
  - path: ../sites/reddit.md
    why: Reddit routes that use RedditAPIs.com and Data365.
  - path: ../sites/threads.md
    why: Threads routes that use ScrapeCreators and SociaVault.
---

# Social data APIs

Small third-party APIs that return posts, replies and profiles from X,
Reddit, Threads and similar networks. They run on the vendor's servers, so
our home IP stays out. None of them is the platform's own permission: a
vendor key is not an X or Reddit licence. All prices below are vendor or
official pages read by the research, not our own runs.

Sources: deep research round 1 (5 October 2026; private, not published), reports G2, G3, G4 and G9, plus the 6 October corroboration.
Lines marked "not rechecked" come only from a report.

## Status

- **Role of the group:** gap fillers per platform. None of them is
  sanctioned by the platform it reads. TwitterAPI.io is the cheap X
  option if the user accepts that; the official X API is the sanctioned
  one. RedditAPIs.com and ScrapeCreators are paid fallbacks behind the
  free Arctic Shift archive for Reddit. Threads vendors break Meta's
  terms (see [threads.md](../sites/threads.md)).
  The rest: skip.
- **Allowed today:** no account, no purchase, no free-credit signup, no
  pilot. Each needs a user decision in
  `~/agents/specs/web-scraping-site-access/DECISIONS.md`.
- **User opinion (round 3, 6 October 2026):** TwitterAPI.io has the most
  user support for X, though thin. ScrapeCreators has a few real users
  and one strong Reddit test, but its terms let it expire credits.
  SociaVault, RedditAPIs.com, Data365 and EnsembleData have too few
  recent opinions to judge. Per-provider detail below.
- **Last checked:** 6 October 2026, by reading vendor pages in three
  check rounds. No API calls.

## Providers

### TwitterAPI.io (X)

- **Status:** pilot candidate for X discovery and replies.
- **Covers:** X search, replies, thread context, webhook rules. Search and
  reply pages commonly return 20 items (Vendor claim, G3, not rechecked).
- **Price:** $0.15 per 1,000 tweets; minimum $0.00015 (15 credits) per
  call, empty calls included; list calls $0.0015. Confirmed 6 Oct 2026 at
  https://twitterapi.io/pricing (Vendor claim). Free tier: one request per
  five seconds (G3, not rechecked).
- **Individual eligibility:** self-serve key, no X cookies (G3, not
  rechecked). Terms, operator and KYC: not found (report C5).
- **How it gets data:** not stated. Its homepage says "TwitterAPI.io
  bypasses the need for Twitter's approval process", so it is not
  reselling the official API under X's approval. X can block it at any
  time. Vendor claim plus Inference, report C7.
- **Reliability:** no independent benchmark of reply recall found.
  States it is not affiliated with X (G9).
- **What users say (round 3, 6 Oct 2026):** the user-opinion reports
  (G10, G16) rank it the best X route at our volume. The evidence is
  thin: its Trustpilot page shows 21 reviews at 4.5, mostly from
  one-review accounts dated August 2025 to January 2026
  (https://www.trustpilot.com/review/twitterapi.io, checked 6 Oct 2026).
  One Reddit user lost all results for a few days in October 2025, cause
  unknown. An integration notes that advanced-search pagination can
  repeat results and that `since:` and `until:` behave badly, so time
  windows by timestamp are safer (G16, not rechecked).
- **Minimum charge and refunds:** the 15-credit minimum applies even
  when a call returns nothing, but "waived for bulk data responses".
  Unused top-up credits "do not expire and remain refundable upon
  request" within 30 days of purchase
  (https://twitterapi.io/refund-policy, checked 6 Oct 2026).
- **Label:** Vendor claim (price, minimum and refund rule confirmed).
  Reply completeness unverified.

### SocialData (X)

- **Status:** skip, or X-only supplement.
- **Covers:** X search, profiles, timelines, threads. Its comments
  endpoint returns top-level comments only, not replies to them (Vendor
  claim, G3). REST plus an official MCP (G2).
- **Price:** "$0.0002 per tweet or user profile returned (or $0.2 per
  1000 items)"; "up to 3 requests per minute without incurring any
  charges" (https://docs.socialdata.tools/getting-started/pricing/,
  checked 6 Oct 2026, round 2). Monitoring: $0.0069 per hour per account,
  and $0.0002 per keyword run even when empty (G3, not rechecked).
- **Individual eligibility:** online signup without an X account (G2).
  Terms make the customer warrant the extraction is authorised
  (https://socialdata.tools/legal/terms-and-conditions, G2).
- **Reliability:** a June 2025 Reddit post says SocialData told the
  poster that "X has taken down their API"; it came back later
  (https://www.reddit.com/r/BlueskySocial/comments/1l8uag0/, Independent
  report, one user's account). When credits run out, calls fail with
  HTTP 402 and fetch nothing, so it stops rather than overbills
  (https://github.com/paperclipai/paperclip/issues/4261). Its fair-use
  rule bills empty requests beyond 3 a minute. Checked 6 Oct 2026.
- **Label:** Vendor claim (price confirmed), one independent outage report.

### FxEmbed (X and Bluesky)

- **Status:** free experimental probe only, never a production route.
- **Covers:** X and Bluesky search, single posts, conversations, account
  feeds and RSS. API v2 documents 1,000 requests per minute per IP
  (https://docs.fxembed.com/api/introduction/, G3, not rechecked).
- **Price:** no payment step for public calls; production tariff not found.
- **Individual eligibility:** hosted public calls need no key. Self-hosting
  wants X `auth_token` and `ct0` cookies, which our rules forbid.
- **Reliability:** no service guarantee. Conversation paging is broken:
  page 2 of a conversation returns HTTP 404, issue open since 18 May 2026
  (https://github.com/FxEmbed/FxEmbed/issues/2087, checked 6 Oct 2026).
  So it cannot read long reply threads.
- **Label:** Official doc (project docs), not rechecked.

### xAI Grok X Search (X)

- **Status:** different kind of tool: question-style X research through a
  model, not a raw feed.
- **Covers:** X keyword and semantic search, user search and thread
  context through the Responses API tool (G9).
- **Price:** "$5 / 1k posts $10 / 1k profiles", plus model tokens.
  "every post returned by a search or thread fetch, including parent and
  quoted posts, counts", so cost is hard to predict. Confirmed on
  https://docs.x.ai/developers/pricing (page dated 29 Sep 2026, checked
  6 Oct 2026, round 2).
- **Individual eligibility:** API key, no X session (G9). xAI's terms on
  storing X Search output were not found.
- **Limits:** at most 20 handles per call in `allowed_x_handles` (or in
  `excluded_x_handles`, not both), so it cannot follow hundreds of
  accounts (https://docs.x.ai/developers/tools/x-search, checked 6 Oct
  2026). When the X index returns nothing, the model can still answer in
  plausible prose; one agent project marks such answers "unsourced" and
  refuses to treat them as X results (G16, Hermes docs, not rechecked).
  Use it to analyse, never as the raw feed.
- **Label:** Official doc.

### RedditAPIs.com (Reddit)

- **Status:** paid fallback behind Arctic Shift for Reddit. Its own page
  says it scrapes with "residential proxy rotation included" and "no
  developer-app review", which is supply-chain exposure (see
  [reddit.md](../sites/reddit.md)).
- **Covers:** reads, deep comment search, alert plans (G4). Its pages
  disagree on endpoint count (31 on /docs, 59 on /pricing).
- **Price:** "Reads cost $0.002 per call", billed "per call rather than
  per row returned"; "$0.50 in free credits and no card on file"; "the
  smallest top-up is $10"; deep comment search $0.02 per call; alert
  plans $19 or $49 a month. About $10 for 5,000 calls (Inference).
  Checked 6 Oct 2026 (round 2) at https://redditapis.com/docs and
  https://www.redditapis.com/pricing (Vendor claim). Operator per report
  C6: Aligned Consulting LLC (not rechecked). Polling 20 communities every five minutes
  is about 172,800 calls, or $345.60 a month (G4 arithmetic, Inference).
- **Individual eligibility:** self-serve, no app approval (Vendor claim).
- **Reliability:** no independent full-tree benchmark. Round 3 found one
  short user mention and no real reviews (G10, G18). Too few opinions to
  judge.
- **Label:** Vendor claim (confirmed 6 Oct).

### ScrapeCreators (multi-social)

- **Status:** Threads candidate; possible social gap filler.
- **Covers:** Reddit, Threads, YouTube, LinkedIn public posts (found
  through Google's index, not native search), Bluesky profiles and posts.
  On X: profiles, user posts, single posts, and now keyword search through
  Google's index: `/v1/twitter/search/posts`, 1 credit per request
  (https://docs.scrapecreators.com/v1/twitter/search/posts, checked 6 Oct
  2026). Its user-tweets endpoint returns about 100 popular tweets, not the
  latest ones (G14, not rechecked). YouTube comments cap at about 1,000
  top and 7,000 new (G14, not rechecked). Threads search returns 10
  results per call (G3). REST plus hosted MCP.
- **Price:** "Start with 100 free credits. Claim up to 7,000 more."
  Freelance $47 for 25,000 credits; Business $497 for 500,000; "Credits
  never expire"; "1 credit === 1 request (for most endpoints)"; cached
  results cost 0. No $10 pack exists. Checked 6 Oct 2026 (round 2),
  https://scrapecreators.com/ (Vendor claim).
- **How it gets data:** calls itself an "unofficial Reddit API" and does
  not say how it collects (report C6).
- **Operator:** Web Scraping Guy LLC, Texas law (terms effective 29 June
  2026, https://scrapecreators.com/terms, checked 6 Oct 2026).
- **Individual eligibility:** self-serve, no card for the free credits.
  Terms on individuals: not found (report C5).
- **Caveat, credits:** the homepage says "No expiring credits", but the
  terms say "Credits may expire or be discontinued at our discretion",
  refunds are "at our sole discretion", and "Upon termination, unused
  credits may be forfeited" (checked 6 Oct 2026). The terms govern, so
  buy the smallest pack only.
- **Caveat, reviews:** it pays affiliates 20% of referrals' spend for 12
  months on a page headed "Get paid to shill Scrape Creators"
  (https://scrapecreators.com/affiliates), and gives up to 7,000 bonus
  credits partly for "honest feedback on G2". Treat G2 scores and
  recommendation posts as possibly paid.
- **What users say (round 3):** about four independent users, all
  positive on price and ease (G14, G17). The strongest test: a 2,907-comment
  Reddit thread came back as "full nested comment trees"
  (https://github.com/mvanhorn/last30days-skill/issues/589, 17 Jun 2026,
  checked). One integration hit an HTTP 500 after auth (issue #882 in the
  same repository, not rechecked). One commenter says it, like Apify, hits
  rate limits and IP bans at scale.
- **Outages:** its status page logs Google blocking its search route on
  4 March 2026 ("Google is blocking us"), with DuckDuckGo as backup
  (https://scrapecreators.com/status, checked 6 Oct 2026). Its LinkedIn
  and X search both rely on that Google layer.
- **Label:** Official doc and Vendor claim; a few independent users.

### SociaVault (multi-social)

- **Status:** challenger to ScrapeCreators when X search and replies matter.
- **Covers:** X search, posts and paged replies; Reddit search and
  comments; Threads; LinkedIn via Google discovery; YouTube comments.
  Bluesky advertised but endpoints not found. Official MCP (G2, G9).
- **Price:** 50 free credits; packs $29 for 6,000, $79 for 20,000, $199
  for 75,000, $399 for 200,000; some endpoints cost more than one credit
  (https://sociavault.com/pricing, 5 Oct 2026, not rechecked).
- **Operator and terms:** Ziddec, Inc., Wilmington, Delaware address.
  "Credits never expire once purchased"; refunds for "less than 10% of
  purchased credits consumed", under a "14-Day Money-Back Guarantee"
  (https://sociavault.com/terms and https://sociavault.com/refund-policy,
  checked 6 Oct 2026). A cleaner billing story than ScrapeCreators.
- **Individual eligibility:** self-serve, no card.
- **Reliability:** no independent user evidence; one incentivized G2
  review (January 2026). Its own 2026 report says "LinkedIn endpoints had
  real availability and reliability problems" and that it once hid a
  LinkedIn endpoint from its docs; it also counts "a response that
  succeeds and returns an empty result" as a success
  (https://sociavault.com/labs/reports/social-data-demand-2026, checked
  6 Oct 2026). Its official MCP lists no Bluesky tools (G14).
- **Label:** Official doc; no independent users. Free test only.

### Data365 (X, Reddit, Threads)

- **Status:** skip. Minimum spend far too high for our volume.
- **Price:** €300 a month for one platform and 500,000 credits; €850 for
  three platforms (https://data365.co/pricing, 5 Oct 2026, not rechecked).
- **Individual eligibility:** 14-day trial through a form; terms speak of
  internal business use (G2). Unclear.
- **What users say (round 3):** good data quality on Trustpilot and a
  small G2 set, all five-star; one Reddit user calls it "very expensive"
  (G10, not rechecked). Our skip stands on price.
- **Label:** Vendor claim, not rechecked.

### EnsembleData (Reddit, Threads, YouTube, X reads)

- **Status:** skip. Daily quotas suit steady workloads, not occasional runs.
- **Price:** trial 50 units a day; $100 a month for 1,500 units a day;
  allowances reset daily (https://ensembledata.com/pricing, 5 Oct 2026,
  not rechecked).
- **Individual eligibility:** terms allow individuals (G2). Terms say it
  uses no cookies or fake accounts.
- **What users say (round 3):** positive but stale: its Trustpilot
  reviews are from 2024 and 2025, none in the last 12 months (G10, not
  rechecked).
- **Label:** Official doc, not rechecked.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | A report put low-end Reddit cost at $0.40 for 5,000 reads. | At RedditAPIs.com's own rate, 5,000 reads cost about $10, with a $10 minimum top-up. | 6 October corroboration, redditapis.com guide |
| 2026-10-06 | Grok X Search at $5 per 1,000 posts was treated as checked. | Not confirmed; the page opened showed no X Search price. | 6 October corroboration |
| 2026-10-06 (round 2) | Our line above: Grok price not confirmed. | Confirmed on xAI's pricing page. | https://docs.x.ai/developers/pricing, round 2 corroboration W01 |
| 2026-10-06 (round 2) | SocialData $0.40 per 1,000 (report G3). | $0.20 per 1,000. | SocialData pricing page, round 2 |
| 2026-10-06 (round 2) | RedditAPIs.com has 38 endpoints. | Its own pages say 31 and 59. | RedditAPIs.com docs and pricing, round 2 |
| 2026-10-06 (round 2) | ScrapeCreators has a $10 "Solo Dev" plan (a third-party review cited in report C5). | No such pack on its pricing; tiers are Free, $47, $497 and Enterprise. | scrapecreators.com, round 2 |
| 2026-10-06 (round 3) | Our line: ScrapeCreators has no X keyword search (G2). | It now has `/v1/twitter/search/posts`, through Google's index. | docs.scrapecreators.com, round 3 check V4 |
| 2026-10-06 (round 3) | TwitterAPI.io has 32 Trustpilot reviews at 4.6 (G16). | 21 reviews at 4.5. | trustpilot.com, round 3 check V3 |
| 2026-10-06 (round 3) | TwitterAPI.io charges its minimum on every call. | Waived for bulk data responses. | twitterapi.io/pricing, round 3 check V3 |

## Open questions

1. How complete are TwitterAPI.io replies against X's own conversation
   search? A cheap route is worthless if replies drop silently. Answer:
   an Observed test on known threads.
2. Will ScrapeCreators actually expire bought credits? Its terms allow it
   (checked 6 Oct 2026). Answer: written vendor reply, or buy only the
   smallest pack.
3. Who runs TwitterAPI.io and SocialData, and do their terms accept an
   individual? Not found in round 2.
4. Answered 6 Oct 2026: RedditAPIs.com scrapes through residential
   proxies; SocialData is $0.20 per 1,000; Grok X Search price confirmed.

## Sources

- https://twitterapi.io/pricing (read 6 Oct 2026)
- https://docs.socialdata.tools/getting-started/pricing/ (5 Oct 2026, via G2 and G3)
- https://docs.fxembed.com/api/introduction/ (5 Oct 2026, via G3)
- https://docs.x.ai/developers/tools/x-search and https://docs.x.ai/developers/pricing (5 Oct 2026, via G9)
- https://www.redditapis.com/pricing and https://www.redditapis.com/guides/reddit-api-complete-2026 (read 6 Oct 2026)
- https://scrapecreators.com/ and https://scrapecreators.com/terms (5 Oct 2026, via G2)
- https://sociavault.com/pricing (5 Oct 2026, via G2)
- https://data365.co/pricing (5 Oct 2026, via G2 and G4)
- https://ensembledata.com/pricing (5 Oct 2026, via G2)
- https://redditapis.com/docs, https://redditapis.com/reddit-scraper, https://scrapecreators.com/ (read 6 Oct 2026, round 2)
- https://twitterapi.io/refund-policy, https://www.trustpilot.com/review/twitterapi.io, https://docs.scrapecreators.com/v1/twitter/search/posts, https://scrapecreators.com/terms, https://scrapecreators.com/affiliates, https://scrapecreators.com/status, https://sociavault.com/terms, https://sociavault.com/refund-policy, https://sociavault.com/labs/reports/social-data-demand-2026, https://github.com/FxEmbed/FxEmbed/issues/2087, https://docs.x.ai/developers/tools/x-search (all read 6 Oct 2026, round 3 checks)
- Deep research rounds 1 to 3 (5 and 6 October 2026; private, not published), reports G2, G3, G4, G9, C5, C6, C7, and the round 3 user-opinion reports G10, G14, G16 to G18; all corroboration rounds.
