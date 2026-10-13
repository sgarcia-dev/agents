---
created_at: 2026-10-06
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: spec
status: piloted
scope: Reddit
purpose: How agents can read Reddit (the public website as a data source): routes per operation, costs, rules and open questions.
related:
  - path: ../spec.md
    why: Owning spec, shared model and the route table.
  - path: ../shared/rules.md
    why: Access, legal and data rules every route must pass.
  - path: ../providers/social-apis.md
    why: RedditAPIs.com and ScrapeCreators facts used by a route here.
  - path: ../providers/reefapi.md
    why: ReefAPI facts used by a route here.
  - path: ../providers/apify.md
    why: Apify plans and Reddit Actors used by a route here.
---

# Reddit

Reddit is useful for hands-on experience, technical debates and job
market mood. Its official public API is closing, and logged-out `.json`,
old Reddit and RSS are closed or closing. The best route today is three
layers: the free Arctic Shift archive for known communities and full
comment trees, a pay-per-call vendor (RedditAPIs.com or ScrapeCreators) as
a swappable fallback, and a search API with `site:reddit.com` for
discovery across all of Reddit. Expected cost is $0 to $30 a month. The
caveat that matters most: none of these is Reddit's permission, and
nobody knows which of them still works after March 2027.

Reddit here means the public website as a data source. No Reddit internal
systems or former-company material are used or referenced.

## Status

- **Verdict:** Arctic Shift first (free), one paid vendor as a fallback, Brave Search API for cross-Reddit discovery. Re-test every source in January and March 2027. Treat the official API as closed for new projects.
- **What users say (round 3, 6 October 2026):** the user-opinion report (G18) lands where round 2 did: Arctic Shift as the free main route, one tested Apify Actor as the paid fallback, search engines for discovery. User support is strong for Arctic Shift, Apify and Google-style discovery, weak for RedditAPIs.com and ScrapeCreators. Detail under "What users say" below.
- **Allowed today:** approved as the second pilot, after Hacker News (P9, 6 October 2026), through Arctic Shift. The user skipped Brave Search. No vendor, account or collector is active yet.
- **Last checked:** 6 October 2026, primary-source check of Reddit's posts, Arctic Shift's API docs, vendor pages, Brave and Google search API pages, and court reporting (round 1 and round 2 corroboration). Observed test on 7 October 2026 (below).

## Timeline (dated)

| Date | What happens | Label | Source |
|---|---|---|---|
| 29 to 30 May 2026 | Logged-out `.json` endpoints start returning 403 (user reports and vendors; no Reddit statement found). An r/apify thread dated 30 May says "Since yesterday, I can't get Apify scrape Reddit"; a later comment reports 403 on every logged-out `.json` call (comment not readable on recheck). | Independent report and Vendor claim (rounds 2 and 3) | [RedditAPIs.com](https://redditapis.com/reddit-scraper), [r/apify thread](https://www.reddit.com/r/apify/comments/1ts2u8z/blocked_reddit_scraping/) |
| 30 Jun 2026 | old.reddit.com moves behind login; later only accounts that used it in the last six months, moderators exempt. | Independent report, checked 6 Oct | [The Verge](https://www.theverge.com/tech/959779/reddit-old-log-in), [PPC Land](https://ppc.land/reddit-to-halt-public-data-api-access-in-march-2027-as-14-000-apps-register) |
| Week of 28 Sep 2026 | New comment IDs change and may no longer be in order. Store IDs as text. | Official doc (from G4, not rechecked) | [r/redditdev comment ID post](https://www.reddit.com/r/redditdev/comments/1whal6a/upcoming_changes_to_the_comment_id_endpoint/) |
| 30 Sep 2026 | Reddit announces the API move to the Developer Platform and the end of RSS. | Official doc | [r/redditdev migration post](https://www.reddit.com/r/redditdev/comments/1wubcvf/moving_data_api_apps_to_the_developer_platform/) |
| 31 Oct 2026 | "New requests for public API access will no longer be accepted." | Official doc, checked 6 Oct | same post |
| 10 Nov 2026 | Reddit posts a progress update. | Official doc, checked 6 Oct | same post |
| 13 Nov 2026 | RSS support ends. No replacement outside communities you moderate. | Official doc, checked 6 Oct | [r/modnews post](https://www.reddit.com/r/modnews/comments/1wubgvt/continuing_our_infrastructure_updates_whats/) |
| 30 Nov 2026 | Registration for the migration bounty closes. | Official doc, checked 6 Oct | r/redditdev migration post |
| 12 Jan 2027 | Reddit starts removing API access for apps and users who have not registered. | Official doc, checked 6 Oct | r/redditdev migration post |
| 23 Feb 2027 | Reddit posts another update. | Official doc, checked 6 Oct | r/redditdev migration post |
| March 2027 | "Remaining public API access will end in March 2027." | Official doc, checked 6 Oct | r/redditdev migration post |

Reddit's post says nothing about price. Social Media Today wrote that the
move "will make all Reddit data access paid only". That is a news claim
Reddit's own text does not make. Do not repeat it.

## Observed test (7 October 2026)

- **Arctic Shift comment trees passed.** 3 known threads came back
  complete (no `more` stubs) and within 6 percent of the live counts:
  359 against 339 (the extra are removed and deleted comments the archive
  keeps), 35 against 35, 236 against 231. The newest archived comment
  matched the newest live one on all three. W02_reddit-arctic-shift record (private, not published).
- **Batch lookup works but strains the server:** 100 of 100 comment IDs
  in one call, after two HTTP 500s and a 120-second wait.
- **Keyword search is unreliable.** "Ireland" in r/cscareerquestions
  answered HTTP 422 "Timeout. Maybe slow down a bit" on every try;
  "Apify" in r/webscraping worked on the second try. Plain subreddit
  listings (no keyword) worked. Use listings plus a local keyword filter,
  and stop after 2 or 3 timeouts. Note the timeout is a 422, not a 429.
- **Paid fallback (Apify):** harshmaur/reddit-scraper returned 3 posts and
  20 comments for one search for about $0.02; trudax/reddit-scraper-lite
  returned 1 post and no comments for the same search, despite having the
  most users (and only 86 percent of its runs succeeding in the last 30
  days). Fallback is harshmaur. A01_apify record (private, not published).

## Routes by operation

Operations: **discover** (keyword or topic search), **retrieve** (one known
item by URL or ID), **thread** (a known item with all replies), **monitor**
(follow accounts, tags, communities or saved searches over time).

| Operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence |
|---|---|---|---|---|---|---|
| discover (across Reddit) | Brave Search API, `site:reddit.com <keyword>` | ScrapeCreators or RedditAPIs.com search | Brave about $20 at 5,000 queries ($5 per 1,000 less a $5 monthly credit); $0 at 1,000 | Brave key (card on file) | Official doc (vendor page) | Medium: freshness and coverage unknown |
| discover (known communities) | Arctic Shift post search inside one subreddit | RedditAPIs.com search | $0 | None | Project doc | Medium |
| retrieve | Arctic Shift ID lookup (up to 500 IDs) | RedditAPIs.com post read ($0.002 per call) | $0; fallback about $10 | None; fallback vendor key | Project doc; Vendor claim | Medium |
| thread | Arctic Shift comment tree (up to 25,000 comments; tested 7 Oct 2026) | Apify `harshmaur/reddit-scraper` (tested 7 Oct 2026), ScrapeCreators post comments (1 credit) or RedditAPIs.com | $0; fallback $0.002 per call | None; fallback vendor key | Project doc; Vendor claim | Medium (no full-tree test yet; archive vote scores lag) |
| monitor | One Arctic Shift query per subreddit per day | Same calls through a paid vendor when Arctic Shift lags | $0 (about 600 calls a month for 20 subreddits); fallback about $1.20 | None | Inference from project and vendor docs | Medium |
| history | Arctic Shift API or monthly dumps | PullPush (data ends May 2025) | $0 | None | Project doc; Independent report | Medium |
| official | Approved Data API | Devvit | $0, but closed to new requests from 31 Oct 2026 | Reddit account plus approval | Official doc | High (that it is closed) |

After March 2027, keep the same design and add a weekly freshness check
that asks each source for its newest record. If Arctic Shift falls behind,
move thread and monitor to the paid vendor (about $10 a month at 5,000
calls). Inference, report C6.

Provider details live in the provider files:
[social-apis.md](../providers/social-apis.md),
[reefapi.md](../providers/reefapi.md),
[apify.md](../providers/apify.md).

## Facts that decide the route

### Official access

- The Responsible Builder Policy says: "You must request access and get explicit approval before accessing any Reddit data through our API." It points non-commercial developers to Devvit, needs written approval for commercial use, bans getting round limits and bans AI training without approval. Official doc, checked 6 Oct 2026. [Responsible Builder Policy](https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy)
- The Data API Wiki gives "100 queries per minute (QPM) per OAuth client id", averaged over 10 minutes, for eligible free access. Anonymous traffic does not get that rate. New requests go through a support ticket ("To request, please contact us here"). Official doc, checked 6 Oct 2026. [Data API Wiki](https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki)
- With requests closing 31 October 2026 and all public access ending March 2027, even an approved key buys only a few months. Treat the official route as closed for new projects. Inference.
- Reddit's published commercial price is unknown. Third-party claims of $0.24 per 1,000 calls and a $12,000 minimum are not accepted. No official self-serve paid tier for individuals was found. Report claim (G4), not rechecked.
- The migration guide confirms the Devvit direction and admits capability gaps and exceptions. An outside search client may not move across unchanged. Official doc, 5 Oct 2026. [Migration guide](https://developers.reddit.com/docs/guides/migrate/public-api)
- Devvit's HTTP Fetch Policy reviews each domain, rarely allows personal domains and says "the only AI providers we allow are OpenAI and Google Gemini". Official doc, checked 6 Oct 2026, [HTTP Fetch Policy](https://developers.reddit.com/docs/capabilities/server/http-fetch-policy).
- Devvit is built for apps installed in communities, with code and data on Reddit's servers, TypeScript only. No official text was found on searching across subreddits or exporting data. Reddit staff told one large app developer there was "no direct route because of the compute involved". It is the wrong base for an outside research reader. Independent report (PPC Land) plus Inference, report C6.
- Reddit for Researchers gives five years of history with a six-month delay, through BigQuery, and needs an academic affiliation. Not an option here. Official doc (G4), not rechecked. [Reddit for Researchers](https://support.reddithelp.com/hc/articles/49381918834964-Reddit-for-Researchers-Program)
- Reddit's data-partner directory is a better rights lead than assuming an archive is licensed. Eligibility and small-user pricing are unknown. Official doc, 5 Oct 2026. [Data partners](https://www.business.reddit.com/solutions/data-partners-overview)
- Reddit's RSS reason, quoted: "RSS is now a common surface for large-scale scraping and automated abuse". Official doc, checked 6 Oct 2026. [r/modnews post](https://www.reddit.com/r/modnews/comments/1wubgvt/continuing_our_infrastructure_updates_whats/)

### Arctic Shift (free archive, the new first choice)

- Free, run by one volunteer (GitHub user ArthurHeitmann): "Remember, this is a free service, so be considerate." No login is mentioned in the API docs. Project doc, checked 6 Oct 2026, [API README](https://github.com/ArthurHeitmann/arctic_shift/blob/master/api/README.md).
- Base URL `https://arctic-shift.photon-reddit.com`; status page at `status.arctic-shift.photon-reddit.com`. Endpoints: post and comment ID lookup (up to 500 IDs), post and comment search, comment tree (`/api/comments/tree?link_id=…`, limit up to 25,000, `parent_id` for one branch), subreddit search and rules, user search, interaction counts, and `rss` or `jsonfeed` output. Search returns up to 100 results per call (`limit=auto` for 100 to 1,000). Keywords support AND, phrases, OR and NOT. Project doc, same page.
- Keyword search works only inside one subreddit or one user, and not for very active subreddits. Independent report (Xpoz, a competitor), report C6; the exact limit text was not seen on the README in round 2.
- Limits and terms: "Rate limits are calculated dynamically based on server load and request complexity"; on a 429, read `X-RateLimit-Reset`. "No uptime or performance guarantees". No terms of use. Removal requests can delete data. The project says to use the monthly dumps for bulk work. Project doc, same page.
- Freshness: "the only free archive we tested that is genuinely current", with a record retrieved 22 seconds after posting (THINKPOL test, 30 July 2026, a competitor). Vantage OSINT listed it "Active" on 28 Sep 2026. Independent report, checked 6 Oct 2026, [THINKPOL](https://think-pol.com/blogs/reddit-archive-search), [Vantage](https://vantageosint.com/tools/reddit-arctic-shift).
- Unknowns: where its live data comes from (not stated; a third party says the official API), and whether it keeps collecting after March 2027. The project says nothing about the closure. This is the key risk. Not found in round 2.
- Archive vote scores lag fresh content by about 36 hours. Independent report (CrawlForge), report C6.
- Load: users report "504 gateway timeouts or server busy errors" (r/OSINTExperts, 2 Oct 2026, from the author of a rival front end). The maintainer traced one tool's failures to 100+ requests fired at once, which made "65% of post id requests fail"; the tool switched to batches of up to 500 IDs and the maintainer said "Looks good now" (https://github.com/zuxu4n/Rosint/issues/9, Sep to Oct 2026, checked 6 Oct 2026). Lesson: batch IDs, one request at a time, back off on 429.
- Score sorting across all of Reddit is not available; issue #56 asking for it is open, and the maintainer puts reliability first (https://github.com/ArthurHeitmann/arctic_shift/issues/56, checked 6 Oct 2026).

### Third-party APIs (vendor claims)

- RedditAPIs.com: "Reads cost $0.002 per call", billed "per call rather than per row returned", "$0.50 in free credits and no card on file", "the smallest top-up is $10", "Credits never expire". 5,000 calls cost about $10. Deep comment search is $0.02 per call. The vendor's own pages disagree on endpoint count (31 on /docs, 59 on /pricing). Vendor claim, checked 6 Oct 2026 (rounds 2 and 3). [docs](https://redditapis.com/docs), [pricing](https://www.redditapis.com/pricing). Round 3 found one short user mention, no reviews.
- **How RedditAPIs.com gets data:** "residential proxy rotation included" and "no developer-app review". So it scrapes Reddit through residential proxies rather than using an API licence. That is the conduct Reddit is suing SerpApi and Oxylabs over, and our rule 12 rejects residential proxies for our own use. Buying from it is supply-chain exposure. Vendor claim, [reddit-scraper](https://redditapis.com/reddit-scraper); Inference.
- ScrapeCreators: an "unofficial Reddit API" that does not say how it gets data. 100 free credits, $47 for 25,000, "Credits never expire", "1 credit === 1 request (for most endpoints)", cached results free. Comments page with a cursor. Vendor claim, checked 6 Oct 2026, [ScrapeCreators](https://scrapecreators.com/), [Reddit API](https://scrapecreators.com/reddit-api).
- None of the vendors checked says it holds a Reddit licence. Pick on price and how easy they are to swap. Inference, report C6.
- ReefAPI: "Start free with 1,000 credits, no card"; Pro $15 a month for 10,000 credits. Vendor claim, checked 6 Oct 2026. [ReefAPI pricing](https://reefapi.com/pricing)
- ReefAPI caps: 500 comments and depth 50 per comments call, load-more costs 3 credits and takes up to 100 IDs, about 5 requests a second per key. Timed-out and blocked calls are free. Its payment pages disagree on card versus crypto (see [reefapi.md](../providers/reefapi.md)). Vendor claim (G4), not rechecked. [ReefAPI Reddit docs](https://reefapi.com/docs/reddit)
- ReefAPI can serve from `live`, `arctic`, `pullpush` or `auto` sources. Pin `live` when freshness matters. Vendor claim (G4), not rechecked.
- Apify Actors seen 5 Oct 2026 (vendor claims, not rechecked unless marked): ClearPath at $2.99 per 1,000 posts plus $0.99 per 1,000 comments, full expansion off by default; Harsh Maur "from $1.50 / 1,000" saved results ($2.00 undiscounted; checked 6 Oct 2026); The Mine Works at $1.50 per 1,000 posts with 500 comments per post and depth 10, no `more` expansion; bovi at $1.98 per 1,000 records, built on the Arctic Shift archive; Trudax's Reddit Scraper Lite is live, "from $3.40 / 1,000", 46,110 users, 4.57 stars, 96.7% runs succeeded (checked 6 Oct 2026). Reports G4, G1 and G18. [ClearPath](https://apify.com/clearpath/reddit-post-comments-bulk-scraper), [Harsh Maur](https://apify.com/harshmaur/reddit-scraper), [The Mine Works](https://apify.com/themineworks/reddit-scraper), [bovi](https://apify.com/bovi/reddit-scraper)
- Bright Data: "5,000 free credits every month", one credit per record, then "$1.50 per 1,000 records" pay as you go as of September 2026. In a competitor's test it returned 397 comments of a 1,183-comment post. Its terms exclude personal projects (see [bright-data.md](../providers/bright-data.md)). Official doc (vendor FAQ), checked 6 Oct 2026, [FAQ](https://docs.brightdata.com/products/scrapers/scrapers-library/faqs); Independent report (lobstr.io).
- Data365 (EUR 300 a month minimum) was also listed. Vendor claim (G4), not rechecked.
- Some Apify Actors just resell archive access: logiover's "Reddit Historical Archive Scraper" queries "the Arctic-Shift archive ... with PullPush.io as a fallback". Calling Arctic Shift directly is free. Vendor claim, report C6.

### What users say (round 3, 6 October 2026)

From report G18 (and G10, G12); decision-driving lines checked 6 Oct 2026.

- **Arctic Shift:** the most recommended free source, often paired with
  PullPush as fallback in OSINT tools. Complaints are timeouts under load,
  partly caused by tools that flood it. No terms and no guarantees.
- **Apify Reddit Actors:** about 6 users say they work; per-Actor testing
  needed. Harsh Maur has an issue titled "(Urgent) Overcharged due to
  actor start event twice". One production project found that a
  multi-subreddit run let the first subreddit eat the whole budget, so it
  runs one subreddit per run (dkships/llm-moods, G12, not rechecked).
  Some Actors only wrap the free archive.
- **Discovery:** users say "searching Reddit via Google is still
  infinitely better" than Reddit's own search (r/TechNook, 31 Aug 2026).
  For an agent that means a search API (see Search-engine discovery), not
  scraping Google.
- **RedditAPIs.com, ScrapeCreators:** one or two mentions each. Too few
  to judge. ScrapeCreators did return a 2,907-comment thread as full
  nested trees in one public test (see
  [social-apis.md](../providers/social-apis.md)).
- **Bright Data:** one positive AWS Marketplace review for social data in
  general; a competitor's test found shallow reply depth. Overbuilt here.
- **Self-hosting the dumps:** about 10 TB of SQLite for all of Reddit (HN,
  2026). Wrong size for about 5,000 items a month.
- **Not found:** any case of Reddit banning or writing to a data buyer.
- **New, free:** ReddInt (browser tool over Arctic Shift and PullPush with
  failover) and Rosint (user-history front end on Arctic Shift). Both are
  promoted by their authors; no independent reviews.

### Archives

- Arctic Shift: see its own section above.
- PullPush: it answers requests, but "its dataset stopped taking in new content in May 2025" (THINKPOL test, 30 July 2026; a competitor), about 1,000 requests an hour, with 502 and 429 errors seen. One other report said it had new data in September 2026; not found on recheck. History only. Independent report, checked 6 Oct 2026, [THINKPOL](https://think-pol.com/blogs/reddit-archive-search), [PullPush](https://pullpush.io/).
- Academic Torrents monthly dumps (about 3.97 TB from 2005) exist, but Reddit "began moving against" public dumps in July 2026. Independent report (THINKPOL), report C6, not rechecked.

### Search-engine discovery

- **Brave Search API:** "$5 per 1,000 requests" and "$5 in free credits every month". A card is needed even on the free plan. Brave uses its own index, so it does not touch Reddit. Report C6 says the old free plan ended 12 Feb 2026 and the credit needs attribution; not seen on recheck. Official doc (vendor page), checked 6 Oct 2026, [Brave Search API](https://brave.com/search/api/). General search tools belong to [capabilities/web](../../../capabilities/web/README.md).
- **Google Custom Search JSON API** is "closed to new customers", and existing customers have until 1 January 2027. Not available to us. Official doc, checked 6 Oct 2026, [overview](https://developers.google.com/custom-search/v1/overview).
- **Avoid Google-scraping APIs for Reddit** (SerpApi and similar): that is exactly the pattern in Reddit v SerpApi. Court record plus Inference, report C6.

### Reading full threads

- An initial comment response is not the whole tree. Every `more` placeholder must be expanded; `/api/morechildren` takes up to 100 IDs and allows one request at a time. Official doc (G4), not rechecked. [Reddit API reference](https://www.reddit.com/dev/api/)
- A `more` stub, a depth cap or a missing cursor means the thread is partial. Monitoring also needs overlap windows, deduplication, deletion checks and failure alerts. Inference.
- Native search supports quoted phrases, Boolean operators and fields such as `author:`, `subreddit:`, `title:`, `selftext:`, `flair:`, `site:` and `url:`. Official doc, 5 Oct 2026. [Search help](https://support.reddithelp.com/hc/en-us/articles/19696541895316-Available-search-features)
- Cost trap: polling 20 communities every five minutes is 172,800 calls a month, about $345.60 at $0.002. Hourly polling is 14,400 calls, about $28.80. Inference from vendor price (G4).

### Practical starter

- Candidate communities: r/LocalLLaMA, r/MachineLearning, r/ExperiencedDevs, r/programming and tool-specific ones. Example query: `subreddit:LocalLLaMA (quantization OR inference) AND benchmark`. Relevance not measured. Inference.
- For jobs, check every opening with the employer. Keep `[Hiring]` posts apart from candidate posts, scams and pay anecdotes. Inference.

## Rules and risks for this site

- General rules: [shared/rules.md](../shared/rules.md). No logins or own cookies for scraping. Keep the home IP away.
- The Data API Wiki requires removing deleted content and deleted-account details. It strongly recommends deleting stored data within 48 hours; that is a recommendation, not a universal deadline. Official doc (G4), not rechecked.
- A vendor key does not show Reddit authorized the vendor's collection or your storage. Written upstream permission for any vendor was not found. Inference (G4).
- Reddit v SerpApi: on 31 July 2026 the court largely denied the motions to dismiss from SerpApi and Perplexity, and held that CAPTCHA and bot-detection can count as access controls. Perplexity, a buyer of SerpApi output, stays in as a defendant, so buyers of scraped data can be drawn in. At a 1 October 2026 conference the judge told Oxylabs "he is unlikely to grant their motion to dismiss" and let discovery go ahead; next dates 5 April 2027 and 27 October. Court record and Independent report, checked 6 Oct 2026. [Lexology](https://www.lexology.com/library/detail.aspx?g=a4fa98e5-85cf-4f8a-a98d-2d9d2ccc7c53), [Loeb](https://www.loeb.com/en/insights/publications/2026/08/reddit-v-serpapi-llc), [Inner City Press](https://www.innercitypress.com/sdny194engelmayerredditperplexityicp100126.html), [CourtListener docket](https://www.courtlistener.com/docket/71720563/reddit-inc-v-serpapi-llc)
- Reddit v Anthropic was sent back to state court on 30 March 2026; contract and tort claims can proceed. Independent report (C3), not rechecked.
- Do not scrape Reddit pages or public `.json` directly. Logged-out `.json` now answers 403, old Reddit needs a login, and getting round either would be getting round a block. Inference; see the timeline.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | C1: Reddit costs "~$0.40" for 5,000 items | About $10 to $15. $0.002 x 5,000 = $10, and the first purchase is $10 anyway. | 6 October corroboration; [RedditAPIs.com pricing](https://www.redditapis.com/pricing) |
| 2026-10-06 | Social Media Today: Reddit data access becomes "paid only" | Reddit's post says nothing about price. | [r/redditdev post](https://www.reddit.com/r/redditdev/comments/1wubcvf/moving_data_api_apps_to_the_developer_platform/) |
| 2026-10-06 | C3: all four defendants' motions in Reddit v SerpApi "predominately denied" | Only SerpApi and Perplexity were ruled on 31 July. On 1 October the judge said Oxylabs' motion is unlikely to succeed; no written ruling yet. | [CourtListener docket](https://www.courtlistener.com/docket/71720563/reddit-inc-v-serpapi-llc), [Inner City Press](https://www.innercitypress.com/sdny194engelmayerredditperplexityicp100126.html) |
| 2026-10-06 | Best live route is a third-party Reddit API (round 1, our route table). | Arctic Shift is free and current for known communities and threads; a vendor is the fallback. | Round 2 corroboration W02 |
| 2026-10-06 | RedditAPIs.com has 38 endpoints (our file). | Its own pages say 31 and 59. | [docs](https://redditapis.com/docs), [pricing](https://www.redditapis.com/pricing) |
| 2026-10-06 (round 3) | Trudax's Reddit Actor is deprecated (our file, G1). | Trudax Reddit Scraper Lite is live: from $3.40 per 1,000, 46,110 users. | Actor page, round 3 check V6 |
| 2026-10-06 (round 3) | Harsh Maur costs $1.80 per 1,000 (G1). | From $1.50 per 1,000 ($2.00 undiscounted). | Actor page, round 3 check V6 |
| 2026-10-06 (round 3) | Arctic Shift limits score sorting to one subreddit or author (G18). | No score sorting exists; the scoped version is a user's open request (#56). | GitHub issue, round 3 check V6 |
| 2026-10-06 | C1: access closes "in phases through March 2027" | One start date (12 Jan 2027) and one end (March 2027). Close enough. | r/redditdev post |
| 2026-10-05 | Older advice: create a free OAuth or PRAW app | Approval is required, and requests close 31 Oct 2026. | Responsible Builder Policy |
| 2026-10-05 | Older advice: an anonymous 10 QPM rate | Not corroborated. | Data API Wiki |

## Open questions

1. Does Arctic Shift's live intake depend on Reddit's public API, and has its maintainer planned for March 2027? This decides whether the free layer survives. Watch the project's GitHub.
2. How complete is an Arctic Shift comment tree against the count on the page, for three large threads? A free pilot would answer.
3. How fresh and complete is Brave for `site:reddit.com` queries? 50 test queries on the free credit would answer.
4. What does ReefAPI's Reddit engine collect from, and does its card checkout work? Not found in round 2.
5. What does Reddit's User Agreement say about logged-out automated reading? Not found (reddit.com could not be fetched).
6. Answered 6 Oct 2026: RedditAPIs.com scrapes through residential proxies; Devvit is not a fit for an outside reader and allows only OpenAI and Gemini as AI providers; Arctic Shift is current; PullPush is history only.

## Sources

- Reddit posts and help pages linked above, read 5 and 6 October 2026.
- Earlier notes: [reddit.md](../../../capabilities/web/social/reddit.md) and the bundles social search discovery (private, not published) and follow-up (private, not published).
- Deep research rounds 1 and 2 (5 and 6 October 2026; private, not published), reports G4, G1, C1, C3 and C6, plus both corroboration rounds.
- Research bundles: see [SOURCES.md](../SOURCES.md).
