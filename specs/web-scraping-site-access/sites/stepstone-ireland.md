---
created_at: 2026-10-06
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: spec
status: researched
scope: IrishJobs.ie and Jobs.ie (Stepstone Group Ireland)
purpose: How agents can read IrishJobs.ie and Jobs.ie: routes per operation, costs, rules and open questions.
related:
  - path: ../spec.md
    why: Owning spec, shared model and the route table.
  - path: ../shared/rules.md
    why: Access, legal and data rules every route must pass.
  - path: ../providers/apify.md
    why: Apify plans and billing for the parsebird actors.
  - path: ../providers/job-data-apis.md
    why: Aggregators that might one day cover these boards.
  - path: ./ats-feeds.md
    why: Employer feeds that cover most product-company jobs.
---

# IrishJobs.ie and Jobs.ie

Two Irish job boards run by the same company, Stepstone Group Ireland,
with the same blocking and identical terms. They matter because Irish
SMEs, public bodies and agency posts with no employer named often appear
only here. Both refuse plain requests, and no verified aggregator names
either board as a source. Alerts are capped at three per account. The
cheapest paid route is a small Apify actor at about $5 a month, which now
says proxy and compute are included. The terms allow personal,
non-commercial downloading.

## Status

- **Verdict:** alerts plus a careful paid pilot are both reasonable; the
  legal risk is low, the technical blocking is the problem.
- **Allowed today:** needs pilot permission, per [DECISIONS.md](../DECISIONS.md).
- **Last checked:** 6 October 2026, actor pages, terms and the alert
  notice checked in both corroboration rounds. Apify test on 7 October 2026 (below).

## Observed test (7 October 2026)

- **Apify test passed for Black Falcon, failed for memo23.** Ranked by
  Store use, Black Falcon leads (IrishJobs 46 monthly users; Jobs.ie 14);
  parsebird's IrishJobs Actor has 1 user and was dropped.
  blackfalcondata/irishjobs-scraper returned 10 real Dublin jobs with
  4,600 to 8,100 character descriptions (about $0.007);
  blackfalcondata/jobs-ie-scraper returned 10 real Dublin and Galway jobs
  (about $0.02). memo23/stepstone-group-scraper returned 0 jobs and still
  charged its $0.05 start fee. Black Falcon returns contact names and
  phones, which must be dropped. The two-run incremental test is still to
  do. A01_apify record (private, not published).

## Routes by operation

| Operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence |
|---|---|---|---|---|---|---|
| search (Jobs.ie) | Apify `blackfalcondata/jobs-ie-scraper` (14 monthly users; tested 7 Oct 2026, 10 real jobs for about $0.02) | Site alert emails | About $5 ($1.10 per 1,000 plus start fee and platform usage) | No for the actor | Observed test | Medium |
| search (IrishJobs) | Apify `blackfalcondata/irishjobs-scraper` (46 monthly users; tested 7 Oct 2026, 10 real jobs). parsebird was dropped: 1 monthly user | Alert emails to a jobseeker account (three alerts) | About $5 ($0.99 per 1,000 on Free, $0.79 Gold); README says compute and Irish residential proxy are included | No for the actor | Vendor claim (checked 6 Oct) | Medium |
| detail | Actor with details enabled (full description) | Open by hand | Included in per-job price | No | Vendor claim | Medium |
| monitor | Actor incremental mode, or daily alerts | Jobs.ie `postedWithinDays` filter | As above | Alerts: likely yes | Vendor claim | Medium |

## Facts that decide the route

- **Same owner.** Both run by Stepstone Group Ireland, with identical
  terms (Official doc, C3 and G7; confirmed in the 6 October
  corroboration).
- **Blocking.** Both return 403 to plain requests. One actor page says an
  Irish residential proxy is needed "to get past Akamai" (Vendor claim,
  C1, not rechecked). G7 could not confirm which bot vendor is used.
- **No feed.** IrishJobs' robots.txt lists old disallowed paths such as
  `/JobSearch/RSS.aspx`; that is not a supported feed (Official doc, G7,
  not rechecked). Current RSS: Not found.
- **Small sites.** One actor's full Jobs.ie scrape returned 3,385 rows on
  6 September 2026 for $3.39 (Vendor claim, C1, not rechecked).
- **Both parsebird actors route through an Irish residential proxy**
  (checked 6 October). Jobs.ie offers `postedWithinDays` (1, 3, 7 or 14)
  and an agency-versus-direct filter.

### Actor prices (paid option, needs pilot permission)

- **Jobs.ie, parsebird:** "Free | $0.99 ... Gold | $0.79" per 1,000, and
  "A small platform Actor start fee also applies" per run
  (https://apify.com/parsebird/jobs-ie-scraper, checked 6 October 2026).
  On the Free plan the price is **$0.99 per 1,000, not $0.79** (C1 quoted
  the Gold price). About $5 a month.
- **IrishJobs, parsebird:** $0.99 per 1,000 on Free, $0.79 on Gold
  (https://apify.com/parsebird/irishjobs-scraper, checked 6 October 2026).
  The README now says "Compute and Irish residential proxy costs are
  included in the event price", matching the header "You are not charged
  for the Apify platform usage". The earlier conflict is resolved on the
  page; a pilot should still read the invoice. It has 1 user and no
  reviews, which is a reliability risk.
- **getascraper/ireland-jobs-feed** covers both boards in one run. Its
  own page gives three prices ($2.25, $3.00 and $4.20 per 1,000) and it
  has 2 users. Vendor claim, checked 6 Oct 2026.
- More Apify actors for IrishJobs, all Vendor claims from report C8, not
  rechecked: scrapersdelight from $0.60, automation-lab $1.01,
  parsing_machine $1.05, abotapi $1.20, unfenced-group $1.40 ("proxy-free",
  which may mean datacenter IPs), blackfalcondata $1.45, memo23
  (Stepstone group, 15 boards) from $1.50, fatihtahta $4.00 (IrishJobs,
  Jobs.ie or NIJobs).
- If proxy were billed: Apify residential proxy is "$8 / GB" (Official
  doc, checked 6 Oct 2026). Report C8 estimated about 2 GB a month for
  200 new jobs a day with details, so up to about $16 extra. Inference.
- Older alternatives (Vendor claims, not rechecked): Black Falcon Data actors
  ($1.10 per 1,000 for Jobs.ie, $1.45 for IrishJobs, plus start fee and
  platform usage, G1); `s7_studio` from $1.05 and `memo23` from $1.45 for
  IrishJobs (C1); `jupri/stepstone-scraper` names both domains but Irish
  output is unverified (G7).
- **What users say (round 3, 6 October 2026):** nothing about any Irish
  board Actor. Report G12 found no user report for either parsebird
  Actor or for Black Falcon's. Store numbers on 6 Oct 2026: parsebird
  IrishJobs 1 user; Black Falcon IrishJobs 155 total and 43 monthly
  users; Black Falcon Jobs.ie 43 and 14. G12 would test Black Falcon
  first for IrishJobs on adoption alone. But Black Falcon bills Apify
  platform usage on top of its $1.45, while parsebird includes compute
  and proxy, so the per-1,000 prices are not comparable. Black Falcon's
  Jobs.ie Actor has incremental mode but no posted-within time window.
  Checked against the Actor pages, 6 Oct 2026.
- Plan and billing details live in
  [apify.md](../providers/apify.md).

### Recency and cost plan (user decision P5, 6 October 2026)

The user chose the Apify actors on two conditions: results must be
recent, and caching should keep cost down. How the actors meet both
(Vendor claims from the actor pages, checked 6 October 2026; Inference for
the plan):

- **Recent:** run once a day. The IrishJobs actor has an incremental mode
  that returns only jobs that are "NEW, UPDATED, REAPPEARED, or EXPIRED"
  since the last run. The Jobs.ie actor has `postedWithinDays` (1, 3, 7 or
  14); use 1 for a daily run.
- **Cheap:** `maxResults` is the number of billed rows, so cap it. In
  incremental mode only changed jobs are billed, which is the actor's own
  form of caching. On our side, keep every job ID already seen, and fetch
  details only for new IDs (the IrishJobs actor fetches one detail page
  per job when `includeDetails` is on, its default).
- **Expected cost:** about 200 new tech jobs a day across both boards is
  about 6,000 billed rows a month, about $5 to $6 at $0.79 to $0.99 per
  1,000. One full Jobs.ie scrape (3,385 jobs) cost $3.39, so a first
  backfill is cheap too.
- **First run:** 50 jobs with a hard cap, then read the run's usage page
  to confirm the real cost before scheduling.
- **Unproven (round 3):** that incremental mode bills only new or changed
  rows. G12 says this needs a two-run test: run, run again the next day,
  and compare billed rows. Also run parsebird and Black Falcon side by
  side on the same 50 jobs, since neither has user reviews.

### Email alerts

The shared design and mailbox rules are in
[shared/email-alerts.md](../shared/email-alerts.md).
Board-specific facts:

- **Three alerts, daily.** "the number of Job Alert emails you can create
  will be narrowed down to three"; "Job Alerts emails will be sent
  daily." Official site, article dated March 2023, checked 6 Oct 2026,
  [notice](https://www.irishjobs.ie/careeradvice/get-ready-for-the-all-new-irishjobs/).
  A 2013 post said ten; the newer notice wins.
- Alerts go out "during the period of time immediately after Job Ads are
  first uploaded" (terms 11.1.7), which is good for freshness. Instant
  alerts switch off after 45 days without a search on the site. Official
  doc, checked 6 Oct 2026; report C8.
- The jobseeker account is group-wide: deleting it deletes data "for all
  job boards of the The Stepstone Group UK and for NIJobs.com" (terms
  4.1.1). Official doc, report C8.
- Jobs.ie: daily alerts by sector and keyword, set in the account's Job
  Alerts section. Max count Not found; the shared group account suggests
  the same three. Official site, report C8; Inference.
- Contents and jobs per email: Not found for both. Do not assume full
  descriptions.
- Three alerts cannot cover every senior role, so alerts here are a
  sample. Agents must never open tracking links or job pages
  automatically. Board accounts are proposal P7.

### Aggregators

- No verified aggregator names IrishJobs.ie or Jobs.ie as a source.
  TheirStack lists "StepStone" with no country detail; Fantastic.jobs
  names only LinkedIn, Wellfound and Y Combinator as boards; Techmap
  counts 52 Irish sources but its portal names did not load. Vendor
  claims, checked 6 Oct 2026 (round 2). See
  [job-data-apis.md](../providers/job-data-apis.md).
- Agency share: one IrishJobs "Senior Software" search showed 33 of 77
  ads (43 percent) from agencies (report C9, snapshot undated). Many
  agency ads hide the employer, so ATS feeds miss them.

## Rules and risks for this site

- C3 rates personal reading of these boards as **low risk**: no explicit
  scraping clause, and "Content on the IrishJobs.ie website can be
  downloaded for personal non-commercial use" (section 16). But 4.5.2
  says "our prior written permission is required for any such use or
  removal of the Content", and 4.8.2 and 4.8.3 ban competing use "as
  determined by us at our sole discretion". A third-party actor still
  "removes" content, so personal use is the best argument, not a clear
  permission. Official doc,
  https://www.irishjobs.ie/about/terms-and-conditions, metadata date
  23 October 2025, checked 6 October 2026 (round 2).
- The terms claim to bind any "unregistered user of the Website" on first
  access (clauses 1.1 to 1.2). There are competition clauses (C3).
- Residential proxies are not allowed for our own requests (see
  [shared/rules.md](../shared/rules.md)).
  An actor that uses its own proxy pool is a provider route and still
  needs pilot permission.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | C1: Jobs.ie actor "from $0.79" as the working price | $0.79 is Gold; Free is $0.99 per 1,000 plus a start fee | https://apify.com/parsebird/jobs-ie-scraper |
| 2026-10-06 | C1: IrishJobs actor $0.99 per 1,000 covers the blocking | README said compute and Irish residential proxy are billed separately; pricing header said the opposite | https://apify.com/parsebird/irishjobs-scraper |
| 2026-10-06 (round 2) | Our note above: proxy may be billed on top | README now says "Compute and Irish residential proxy costs are included in the event price" | Same page, round 2 corroboration W04 |

## Open questions

1. What do IrishJobs and Jobs.ie alert emails contain (full description
   or snippet, job ID)? One real email would answer.
2. Do Techmap's free tier or TheirStack's free credits return any record
   whose source URL is irishjobs.ie or jobs.ie? A free query would prove
   or disprove aggregator coverage.
3. What does one small actor run really cost, and does incremental mode
   really bill only changed rows? Two runs of 50 jobs a day apart on the
   Apify free tier would answer (P1 settled; needs the pilot).
4. Answered 6 Oct 2026: alerts are three per account and daily; the
   parsebird page now says proxy is included; no aggregator is verified
   to carry these boards.
5. How much do IrishJobs and Jobs.ie overlap? Both belong to Stepstone,
   but no dataset measures it (G12). A one-week run of both would answer.

## Sources

- https://apify.com/parsebird/jobs-ie-scraper (checked 6 October 2026)
- https://apify.com/parsebird/irishjobs-scraper (checked 6 October 2026)
- https://www.irishjobs.ie/about/terms-and-conditions (checked 6 October 2026)
- https://apify.com/jupri/stepstone-scraper (via G7)
- Deep research rounds 1 and 2 (5 and 6 October 2026; private, not published), reports C1, C3, C8, C9, G1, G7, and both
  corroboration rounds.
- Research bundles: see [SOURCES.md](../SOURCES.md).
