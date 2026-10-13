---
created_at: 2026-10-06
updated_at: 2026-10-06
model: claude-opus-5-5
doc_type: spec
status: researched
scope: Job-data APIs (TheirStack, Fantastic.jobs, Techmap, Adzuna, Jooble, JSearch/OpenWebNinja, Coresignal, People Data Labs, Himalayas)
purpose: What each job-data API or aggregator covers, what it costs, whether an individual can use it, and the role we give it.
related:
  - path: ../spec.md
    why: Owning spec and the provider table.
  - path: ../shared/rules.md
    why: Rules a provider must pass, including terms and data protection.
  - path: ../sites/ats-feeds.md
    why: Free employer feeds stay the backbone; these APIs only find more employers.
  - path: ../sites/stepstone-ireland.md
    why: Jobs.ie and IrishJobs.ie gap these APIs might or might not fill.
  - path: ../sites/indeed.md
    why: Indeed has no read API; some aggregators carry its listings.
---

# Job-data APIs

Paid and free services that sell job postings gathered from many boards
and employer career sites. Free public employer feeds (ATS feeds) stay the
backbone. A paid aggregator only helps to find employers we do not already
watch, or to fill a board we cannot read. None is proven to carry Jobs.ie
or IrishJobs.ie today.

Sources: deep research round 1 (5 October 2026; private, not published), reports G7 Part B, C4 and G2, plus the 6 October
corroboration. Lines marked "not rechecked" come only from a report.
G7 cost figures are for 1,000 / 10,000 / 50,000 records a month.

## Status

- **Role of the group:** discovery only. First candidates: TheirStack (find
  companies), Techmap (cheap broad feed), Himalayas (free remote roles).
  Fantastic.jobs is the runner-up. The rest: skip. No aggregator is
  verified to carry IrishJobs.ie or Jobs.ie (round 2).
- **LinkedIn content:** TheirStack and Fantastic.jobs both index LinkedIn
  jobs. If the user accepts proposal P10 (no LinkedIn-derived data from
  any source), filter LinkedIn-sourced records out of their results or
  query only non-LinkedIn sources. See
  [linkedin.md](../sites/linkedin.md).
- **Allowed today:** no account, no purchase, no free-tier signup, no
  pilot. Each needs a user decision in
  `~/agents/specs/web-scraping-site-access/DECISIONS.md`.
- **Last checked:** 6 October 2026: TheirStack pricing and sources,
  Techmap's Ireland page and Fantastic.jobs' developer docs (round 1 and
  round 2 corroboration). Others are report-only.

## Providers

### TheirStack

- **Status:** first paid candidate, to find companies, not as a feed.
- **Covers:** global jobs with country filter; sources include Indeed,
  LinkedIn, Workday, iCIMS, SmartRecruiters (Vendor claim, G7). Full
  description, source URL and resolved original URL when known. Says it
  covers "over 360k websites" (Vendor claim, C4).
- **Price:** API plan $49 a month for 1,500 credits; unused credits roll
  over for 12 months. Confirmed 6 Oct 2026 at
  https://theirstack.com/en/pricing (Official doc). 1 credit per job, 3
  per company, for API credits. In-app "company credits" are sold
  separately ($109 for 1,000). Free 200 API credits a month; $100 for
  5,000, $169 for 10,000, $400 for 50,000 (C4 and C9, not rechecked).
  TheirStack's own FAQ also says "paid plans begin at 90€" (report C8),
  which contradicts its $49 card; Bright Data's blog said $59. Trust the
  pricing page.
- **Sources:** its list includes "StepStone" with no country detail, so
  the Irish Stepstone boards are not confirmed (checked 6 Oct 2026,
  https://theirstack.com/en/our-data).
- **Limits:** 4 requests a second, 500 results per page (6 Oct check).
- **Individual eligibility:** self-serve plans (G7). Not stated otherwise.
- **Reliability:** says most jobs appear within 24 hours (Vendor claim).
  No Irish sample found.
- **Label:** Official doc (price confirmed).

### Fantastic.jobs

- **Status:** runner-up; useful only if it adds ATS platforms we miss.
- **Covers:** "Indexes new ATS jobs every hour from 56 ATS platforms",
  plus "job board listings from LinkedIn ..., Wellfound, and Y
  Combinator". No Irish board. Every request needs a Bearer key. Vendor
  claim, checked 6 Oct 2026 (round 2), https://developer.fantastic.jobs/llms.txt.
  Ireland estimate 39k to 48k postings a month, all jobs (Vendor claim,
  G7). Useful for employer-direct jobs, including remote.
- **Price (three routes, all 5 Oct 2026, not rechecked):**
  - Direct API from $95 a month; 7-day trial with 500 jobs
    (https://fantastic.jobs/api, G7).
  - RapidAPI "Job Posting Feed": Basic $0 (5 requests), Pro $95 (150
    requests), Ultra $195 (1,000 requests), up to 500 jobs per request (C4).
  - Apify actor from $4 per 1,000 jobs
    (https://apify.com/fantastic-jobs/career-site-job-listing-api, C4, G7).
- **Label:** Vendor claim and Official doc, not rechecked.

### Techmap (JobDataFeeds)

- **Status:** cheapest broad feed to test, per G7. Not proven.
- **Covers:** 68,136 Irish postings from 52 sources in September 2026, all
  jobs, "collected continuously from job boards, ATS career pages, and
  aggregators" (Vendor claim, confirmed 6 Oct 2026,
  https://jobdatafeeds.com/data/countries/ie). Its portal list did not
  return names, so Jobs.ie and IrishJobs coverage is still not found. Its
  own volume figures disagree (about 64k, 92k and 122k a month on
  different pages). Daily files arrive "with a two-day delay" (AWS
  listing, report C8).
- **Price:** "Free Basic plan: 100 requests = 1,000 job postings per
  month"; feed $400 a month; historical dataset $4,800 one-off (checked
  6 Oct 2026). RapidAPI, up to 10 records per request. Overage is charged, not blocked: the free tier is not a spend
  cap. G7 works out $0 / $29 / $99 (https://api.techmap.io/errors-and-billing,
  5 Oct 2026, not rechecked).
- **Caveat:** "active" listings are not rechecked; expiry is assumed
  (posting date plus 30 days) (Official doc, G7).
- **Label:** Official doc and Vendor claim, not rechecked.

### Himalayas API

- **Status:** free remote-job source; worth adding when a decision allows.
- **Covers:** remote jobs with country filters, full description,
  application link, expiry date. Daily refresh. No authentication; browse
  pages hold 20 jobs; rate limit unpublished (https://himalayas.app/api,
  5 Oct 2026, G7, not rechecked).
- **Price:** free.
- **Label:** Official doc, not rechecked.

### JSearch (OpenWebNinja, also on RapidAPI)

- **Status:** skip for Ireland. It is built on Google for Jobs results,
  and Google Jobs does not cover Ireland (checked 6 Oct, see
  [google-jobs.md](../sites/google-jobs.md)).
- **Price:** direct 200 requests a month free; $0.005 per request; $25 a
  month for 10,000 requests; $150 for 200,000
  (https://www.openwebninja.com/api/jsearch, 5 Oct 2026, G2, not
  rechecked). RapidAPI prices not found; RapidAPI adds $1 per GB over 10
  GB.
- **Label:** Official doc, not rechecked.

### Coresignal

- **Status:** skip. Cost and email-domain trial rule do not fit.
- **Covers:** multi-source jobs, sources include a professional network,
  Indeed and Glassdoor (G7).
- **Price:** 7-day, 2,000-credit trial tied to company email domains. G7
  works out $49 / $199 / $1,000 (https://docs.coresignal.com/pricing, 5
  Oct 2026, not rechecked).
- **Individual eligibility:** personal email acceptance not found.
- **Label:** Official doc, not rechecked.

### Adzuna

- **Status:** skip. Ireland is not in its documented country list
  (https://developer.adzuna.com/swagger/spec/test2.json, G7, confirmed by
  the 6 October corroboration).
- **Other:** descriptions cut to 500 characters; 2,500 calls a month.

### Jooble

- **Status:** skip. Free allowance is 500 requests per key for the key's
  whole life, not monthly. Returns snippets and Jooble links, not full
  text. Irish signup asks for website, email and phone
  (https://ie.jooble.org/api/about, G7, not rechecked).

### People Data Labs

- **Status:** out of scope here. It enriches people and companies, not
  job listings. Mentioned in this research only as a people-data
  candidate with provenance concerns (report G5, not rechecked).

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | TheirStack: "1 credit per job, 3 per company" applies to everything. | That applies to API credits. In-app company credits are a separate product ($109 for 1,000). | theirstack.com/en/pricing, read 6 Oct 2026 |
| 2026-10-06 | Google Jobs via SerpApi or JSearch can cover Ireland. | Ireland is on neither Google's nor SerpApi's country list. | 6 October corroboration |
| 2026-10-06 (round 2) | Fantastic.jobs covers 54 ATS platforms (G7). | Its docs now say 56. | developer.fantastic.jobs, round 2 |

## Open questions

1. Does any aggregator ingest Jobs.ie or IrishJobs.ie? Round 2 found no
   source list that names them. The free test: query Techmap's free tier
   or TheirStack's free credits for Irish software jobs from the last 7
   days and look for irishjobs.ie or jobs.ie source URLs.
2. How many Irish employers does TheirStack reveal that the ATS list
   misses? Answer: a one-week coverage test.
3. Does Techmap's free tier allow a hard local cap before overage? Answer:
   billing docs plus our own request counter.

## Sources

- https://theirstack.com/en/pricing (read 6 Oct 2026)
- https://fantastic.jobs/api, https://rapidapi.com/fantastic-jobs-fantastic-jobs-default/api/job-posting-feed-api/pricing, https://apify.com/fantastic-jobs/career-site-job-listing-api (5 Oct 2026)
- https://api.techmap.io/errors-and-billing, https://jobdatafeeds.com/data/countries/ie (5 Oct 2026)
- https://himalayas.app/api (5 Oct 2026)
- https://www.openwebninja.com/api/jsearch (5 Oct 2026)
- https://docs.coresignal.com/pricing (5 Oct 2026)
- https://developer.adzuna.com/swagger/spec/test2.json (5 Oct 2026)
- https://ie.jooble.org/api/about (5 Oct 2026)
- https://theirstack.com/en/our-data, https://developer.fantastic.jobs/llms.txt (read 6 Oct 2026, round 2)
- Deep research rounds 1 and 2 (5 and 6 October 2026; private, not published), reports G7, C4, C8, C9, G2, G5; both corroboration rounds.
