---
created_at: 2026-10-06
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: spec
status: piloted
scope: Employer ATS job feeds (Greenhouse, Lever, Ashby, Workable, SmartRecruiters, Teamtailor, Personio, Recruitee, Workday)
purpose: How agents can read employer job feeds from applicant tracking systems: endpoints, paging, pacing, company discovery and open questions.
related:
  - path: ../spec.md
    why: Owning spec, shared model and the route table.
  - path: ../shared/rules.md
    why: Access, legal and data rules every route must pass.
  - path: ../providers/job-data-apis.md
    why: TheirStack and Fantastic.jobs, used to find companies.
  - path: ../providers/serpapi.md
    why: SERP API for search-operator company discovery.
  - path: ../providers/apify.md
    why: Apify per-ATS actors (not needed; they wrap the same feeds).
  - path: ./indeed.md
    why: Board alerts used as a gap detector against these feeds.
---

# Employer ATS feeds

An ATS (applicant tracking system) is the hiring software an employer
uses. Most of them publish the employer's open jobs through a free,
keyless public endpoint meant for careers pages. These feeds are the
backbone of job discovery: free, low risk, with full descriptions. A
private consumer already reads some employer feeds. Paid aggregators help
only to find employers we do not already watch. The biggest gap is
Workday, which most large multinationals in Cork and Dublin use; it has a
public but undocumented endpoint.

## Status

- **Verdict:** best route for employer jobs. Free, official or
  community-documented, low risk.
- **Allowed today:** yes for public feeds at polite rates, per
  [DECISIONS.md](../DECISIONS.md). Paid discovery tools need permission.
- **Last checked:** 6 October 2026, reports C4 and C9 plus both
  corroboration rounds (Lever README, Workday write-ups and robots.txt,
  Eightfold, Oracle, BambooHR and SmartRecruiters docs). Observed test on
  7 October 2026 (below).

## Observed test (7 October 2026)

- **Passed on six systems, 11 employers,** keyless, every request HTTP
  200, no blocks: Greenhouse (Anthropic 643 jobs, LearnUpon 14), Lever
  (Dun & Bradstreet 107 against 111 on the page), Ashby (Ashby 66 against
  67, Wayflyer 19), Workable (Fenergo 21), Workday (Workday 378, AIG 479,
  Pluralsight 15) and SmartRecruiters (Version1 40, Arista 15 Irish
  jobs). Every feed carried full descriptions. W03_ats-feeds-a record (private, not published), W04_ats-feeds-b record (private, not published).
- **SmartRecruiters needs no key** for public postings (open question
  answered by test).
- **Lever:** Dun & Bradstreet's EU host answered 404 and the global host
  worked, so try EU first, then global.
- **Location sits in a different field per system:** Greenhouse
  `location.name` plus `offices`; Lever `categories.location`; Ashby
  `location` plus `secondaryLocations` (13 Ashby jobs list Ireland only
  there); Workable top-level `city` and `country`. Each system needs its
  own location reader.
- **Workday traps:** `total` is only right on page 1; on 2 of 3 tenants an
  offset past the end returns page 1 again, so stop on a short page or a
  repeated job ID. `searchText: "Ireland"` overcounts multi-location jobs
  (35 against 31 on the country filter); use the country facet. The detail
  GET worked after stripping the locale prefix from `externalPath`.
- Careers pages are not ground truth either: counts move by tens within
  hours, and Workable's page filters by the visitor's location. Track jobs
  by ID.

## Routes by operation

| Operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence |
|---|---|---|---|---|---|---|
| search | Public feed per company (one request per board per night) | TheirStack to find companies | $0 | No | Official doc (6 ATSs), community docs (Workday, Workable) | High |
| detail | Same feed (most return full text), or the job URL | none | $0 | No | Official doc | High |
| monitor | Nightly feed poll, diff by job ID | Personio advises hourly sync for its customers | $0 | No | Inference | High |

## Facts that decide the route

All from deep research round 1 (5 October 2026; private, not published), report C4, "not rechecked" unless the 6 October
corroboration says so.

| ATS | Endpoint (GET unless noted) | Paging | Limits or terms | Label |
|---|---|---|---|---|
| Greenhouse | `https://boards-api.greenhouse.io/v1/boards/{token}/jobs?content=true` | Whole board in one call | No published limit. Only the apply POST needs auth | Official doc (https://docs.greenhouse.io/job-board.html) |
| Lever | `https://api.lever.co/v0/postings/{site}?mode=json`; **EU accounts use `api.eu.lever.co`** | `skip`, `limit`; location, team, commitment filters | No published limit. Unlisted jobs are not returned | Official doc (https://github.com/lever/postings-api) |
| Ashby | `https://api.ashbyhq.com/posting-api/job-board/{name}?includeCompensation=true` | Whole board; has `isRemote` | No published limit | Official doc (https://developers.ashbyhq.com/docs/public-job-posting-api) |
| Workable | `https://www.workable.com/api/accounts/{slug}?details=true` (redirects to `apply.workable.com/api/v1/widget/accounts/{slug}`) | Whole board; has `telecommuting` | Not found | Official doc (https://workable.readme.io/reference/jobs-1) |
| SmartRecruiters | `https://api.smartrecruiters.com/v1/companies/{id}/postings?country=ie&limit=100&offset=0` | Max 100 per page; `q` and `country` filters | "The Customer API limit is 10 requests per second". The reference lists an `x-smarttoken` key or OAuth scheme; OAuth is "only required" for internal postings. It never says outright that public reads need no key (checked 6 Oct 2026) | Official doc (https://developers.smartrecruiters.com/docs/endpoints, https://developers.smartrecruiters.com/reference/v1listpostings) |
| Teamtailor | `https://{careersite}/jobs.rss?per_page=200&offset=0` | Default 100; `offset`, `per_page` | Not found | Official doc (Teamtailor support RSS guide) |
| Personio | `https://{company}.jobs.personio.de/xml?language=en` (some use `.com`) | Whole feed, XML; no job URL, build it from the id | Employer must enable the feed | Official doc (Personio support) |
| Recruitee | `https://{company}.recruitee.com/api/offers/` | Whole board with descriptions | Still answers on the recruitee.com subdomain when a custom domain is used | Official doc (careers-site API) |
| Workday | POST `https://{tenant}.wd{N}.myworkdayjobs.com/wday/cxs/{tenant}/{site}/jobs` with `{"appliedFacets":{},"limit":20,"offset":0,"searchText":"…"}`; detail GET `…/wday/cxs/{tenant}/{site}{externalPath}` | `limit` 20 at most, step `offset` by 20 | `total` only on page 1; 2,000-result cap per search. No published terms or rate limit. Mastercard's robots.txt does not block `/wday/cxs/` (checked 6 Oct 2026) | Independent report |
| Eightfold | Careers-site route `GET https://{tenant-host}/api/apply/v2/jobs?domain={employer-domain}&start={n}&num=10`; some tenants answer only on `/api/pcsx/search` with the same parameters | `start`; 10 per page whatever `num` asks | Undocumented. The official Eightfold API is separate and needs the customer's OAuth ("API v2 uses OAuth 2.0 authentication") | Independent report (GitHub PRs, report C9); Official doc for the OAuth API (https://apidocs.eightfold.ai/docs/getting-started) |
| Oracle Recruiting Cloud | `GET https://{host}.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitions?finder=findReqs;siteNumber={CX_n}` plus `limit`, `offset`, keyword and facet variables | `limit`, `offset` | Documented, but Oracle says "the service endpoints in this resource category are only for Oracle internal use" (checked 6 Oct 2026). Anonymous use is from implementers only | Official doc (https://docs.oracle.com/en/cloud/saas/human-resources/farws/api-recruiting-ce-job-requisitions.html); Independent report |
| BambooHR | `GET https://{slug}.bamboohr.com/careers/list`; detail `/careers/{id}/detail` | Whole board in one call | "needs no credentials"; "The endpoint is not a documented API" (it is the careers widget's own call). A bad slug redirects to bamboohr.com, which can look like a 200 | Independent report (https://github.com/plin-code/job-boards-bamboohr, checked 6 Oct 2026) |

- **Workday details** (Independent reports, rechecked in round 2 where
  marked):
  - "`limit` hard-caps at 20". Some write-ups get HTTP 400 above 20,
    others HTTP 200 with an empty list, so treat an empty first page as
    "check again", not "no jobs". Confirmed at FetchSmith, 6 Oct 2026.
  - "Page further in and `total` silently becomes `0`", so read `total`
    from offset 0 only. Confirmed at FetchSmith, 6 Oct 2026.
  - Each search stops at 2,000 results, and "Offsets past the ceiling
    come back as the first twenty postings again, forever". Stop on the
    first-page total, a short page or a repeated job ID. Report C9
    (glitchbound posts), not rechecked.
  - **Filter to Ireland with facets, not text.** The first response lists
    facets such as `Location_Country` with opaque IDs. Find the "Ireland"
    value once per tenant, cache it, and send it in `appliedFacets`. An
    Irish slice will rarely reach 2,000. `searchText` is fuzzy. Report C9;
    Inference.
  - No department field. Job pages also carry JSON-LD. Report C9.
  - Some employers hide Workday behind their own domain (Salesforce,
    Fidelity), so find the tenant from a job URL, not the careers domain.
  - The endpoint may change without notice. Keep to about one request
    every few seconds.
- **Lever EU host: confirmed.** The official README names "the instances
  we support: `global` (default) and `EU`" (checked 6 Oct 2026). A
  developer PR adds that a company lives on one host only and the other
  answers 404 (report C9, not in the README). So on a 404 from
  `api.lever.co`, retry `api.eu.lever.co` and store the host per company.
- **Eightfold:** tenants often serve from their own domains (for example
  `apply.careers.microsoft.com`), so detect it by URL path, not host.
  Report C9.
- **iCIMS:** no public feed found. Its job pages carry schema.org
  `JobPosting` JSON-LD, so a reader over known job URLs is the fallback.
  Report C9.
- **Workable cross-customer search** at
  `jobs.workable.com/api/v1/jobs?query=…` returns 20 jobs per page and
  helps find Workable employers by location (Vendor claim, Apify actor
  docs, via C4).

### ATSs with no known public feed

iCIMS, SuccessFactors, Taleo, Rippling, Avature, Phenom, Jobvite, HiBob,
Comeet and in-house careers sites (Big Tech mostly runs its own). Jobs
there are reachable only through boards, alerts, JSON-LD on job pages or
a paid aggregator. One Apify actor claims JazzHR and Breezy coverage,
which suggests public feeds exist, but no endpoint was shown (report C9).

### Irish employers by ATS (summary)

Report C9 looked for live job URLs for 104 Irish tech employers on
5 October 2026. 46 had evidence: Greenhouse 15 (mostly Dublin scale-ups
and US SaaS offices), Workday 14 (mostly large multinationals, many in
Cork), Ashby 7 (AI and newer firms), Lever 4, SmartRecruiters 2,
Eightfold 2, iCIMS 1, Oracle 1. For the other 58, including most Big
Tech, no ATS evidence was found. Evidence came from search results, not
pages opened one by one. Independent report. The employer-level table
and a private reader's to-do list are private, not published.

**Build order for new readers** (Inference, report C9): Workday first
(most Irish employers, medium effort); then Eightfold (medium effort);
then BambooHR (lowest effort, suits small Irish firms); Oracle only after
deciding on its "internal use" note; iCIMS last (JSON-LD fallback).

### Company discovery

Free methods (C4, C9):

- **Seed lists.** The open-source "unlisted" project ships Greenhouse,
  Ashby and Lever lists of 11,881 companies from `kalil0321/ats-scrapers`
  (MIT licence) (Independent report,
  https://github.com/ShalomHunukumbura/unlisted). Other GitHub
  aggregators carry starter slug lists.
- **Check slugs exist.** Greenhouse, Ashby and Lever return a clean 404
  for unknown tokens. Reject boards with zero jobs; empty leftover boards
  are common.
- **Search operators,** run by hand or through a SERP API, to harvest
  slugs (not jobs): `site:boards.greenhouse.io OR
  site:job-boards.greenhouse.io "Dublin"`, `site:jobs.lever.co Ireland`,
  `site:jobs.ashbyhq.com "Remote" EMEA`, `site:apply.workable.com
  Ireland`, `site:jobs.smartrecruiters.com Dublin`, `site:*.teamtailor.com
  Ireland`, `site:*.recruitee.com Ireland`, `site:myworkdayjobs.com
  Dublin`.
- **Alert loop.** When a board alert names a company that no feed
  matches, find that company's ATS and add the slug. C4 calls this the
  highest-yield loop (Inference). No such loop exists yet.
- **Name lists, then slugs.** Take names from Built In Dublin, IDA and
  Enterprise Ireland lists or board browsing, find each ATS slug with a
  `site:` search, and keep a slug only if its feed returns at least one
  Irish or EMEA-remote job. Report C9; Inference.
- **Open datasets.** `kalil0321/ats-scrapers` (MIT) added 551 validated
  Greenhouse employers in September 2026 and covers Workday,
  SuccessFactors, Oracle and iCIMS too. One author measured 3,916 Workday
  boards. Independent report, report C9, not rechecked.

Paid (see [job-data-apis.md](../providers/job-data-apis.md)):
TheirStack $49 a month for 1,500 API credits, credits roll over for 12
months (checked 6 October 2026); 4 requests a second, 500 results per
page. Fantastic.jobs Apify actor from $4 per 1,000 jobs (Vendor claim).
Apify per-ATS actors are not needed: they wrap the same free endpoints.

### Ghost jobs

Greenhouse's 2024 report says "18–22% of the jobs posted on the
Greenhouse platform are classified as ghost jobs" in a given quarter
(Vendor claim, via C4). Feeds include stale roles, so score older
postings lower.

## Rules and risks for this site

- Polite pacing (Inference, C4): one request per board per night, an
  identifying User-Agent, no parallel bursts. Throttle Workday to about
  1 request a second. Stay under SmartRecruiters' 10 requests a second.
- These feeds serve data the employer chose to publish for embedding.
  Low risk. General rules in
  [shared/rules.md](../shared/rules.md).

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | C4: Workday max 20, `total` resets to 0, 2,000 cap, as fact | Only `limit: 20` seen at the source; the rest unconfirmed | 6 October corroboration |
| 2026-10-06 (round 2) | Our line above: `total` reset unconfirmed | Confirmed by FetchSmith; the 2,000 cap is still from one author only | Round 2 corroboration W04 |
| 2026-10-06 (round 2) | BambooHR has no known public feed (C4, our file) | Its careers widget endpoint is public and keyless, but undocumented | https://github.com/plin-code/job-boards-bamboohr |
| 2026-10-06 (round 2) | Oracle's "internal use" note covers only a related resource (report C9 open question) | It covers the whole `recruitingCEJobRequisitions` category, including `findReqs` | Oracle docs, round 2 corroboration W04 |
| 2026-10-06 | C4: TheirStack "1 credit per job, 3 per company" as the only credit type | Applies to API credits; the pricing page also sells in-app company credits ($109 for 1,000) | https://theirstack.com/en/pricing |

## Open questions

1. What do Workday's terms say about the `/wday/cxs/` path? Robots.txt
   does not block it for Mastercard; the terms were not read.
2. Is Oracle's "only for Oracle internal use" note a bar on anonymous
   reading of a public careers site, or a support disclaimer? Decide
   before building an Oracle reader.
3. Which ATS do Google, Meta, Apple, Amazon, TikTok, MongoDB and the
   larger Irish scale-ups use? Open one Dublin posting each.
4. Does Greenhouse run an EU board host like Lever? Not found.
5. How much of the board inventory is already in ATS feeds? C4 found no
   direct study; its one-week overlap test (alerts against feeds) would
   measure it.
6. Answered 6 Oct 2026: Lever has an EU host; Workday is the largest
   Irish gap; no aggregator is verified to carry the Irish boards.

## Sources

- Endpoint docs linked in the table (via C4, accessed 5 October 2026).
- https://theirstack.com/en/pricing (checked 6 October 2026)
- https://github.com/ShalomHunukumbura/unlisted (via C4)
- Deep research rounds 1 and 2 (5 and 6 October 2026; private, not published), reports C4 and C9, and both corroboration rounds.
- Research bundles: see [SOURCES.md](../SOURCES.md).
