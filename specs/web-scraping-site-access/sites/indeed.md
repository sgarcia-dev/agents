---
created_at: 2026-10-06
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: spec
status: researched
scope: Indeed (Ireland and worldwide)
purpose: How agents can read Indeed job listings: routes per operation, costs, rules and open questions.
related:
  - path: ../spec.md
    why: Owning spec, shared model and the route table.
  - path: ../shared/rules.md
    why: Access, legal and data rules every route must pass.
  - path: ./glassdoor.md
    why: Glassdoor merged into Indeed on 1 July 2026 and is covered here.
  - path: ./ats-feeds.md
    why: Employer feeds that hold most of the same jobs, with no scraping.
  - path: ./google-jobs.md
    why: Google Jobs is not a route for Ireland.
  - path: ../providers/apify.md
    why: Apify actor facts for the paid option.
  - path: ../providers/bright-data.md
    why: Bright Data Indeed scraper facts.
---

# Indeed

Indeed is the largest general job board, and Glassdoor is now part of it.
There is no official read API. The best route today is alert emails sent
to an inbox the user controls, read without opening any links. A paid
Apify actor is a possible later option, but Indeed's own terms ban
automated access, so it needs pilot permission and a terms review first.

## Status

- **Verdict:** alerts first; scraping is not allowed by default. Most
  relevant jobs are better read from employer ATS feeds.
- **Allowed today:** no scraping. Alerts and the actor both need a user
  decision, per [DECISIONS.md](../DECISIONS.md).
- **Last checked:** 6 October 2026, research reports plus both
  corroboration rounds (primary-source checks of the help centre). Apify test on
  7 October 2026 (below).

## Observed test (7 October 2026)

- **User-directed Apify test passed.** valig/indeed-jobs-scraper (4,003
  monthly users, $0.10 per 1,000) and borderline/indeed-scraper (2,597
  users, $5 per 1,000) each returned 10 real Dublin jobs with full
  descriptions, for about a start fee each. Ongoing use is still a user
  decision. A01_apify record (private, not published).

## Routes by operation

| Operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence |
|---|---|---|---|---|---|---|
| search | Alert emails to the user's inbox, parsed without opening links | Apify Indeed actor (paid option, needs pilot permission and a terms review) | $0 for email; about $2.50 to $15 on Apify | Yes, an Indeed account for alerts | Official doc (alerts need sign-in); Vendor claim (actor prices) | Medium |
| detail | Open by hand when an alert job is not found in the ATS feeds | Apify actor detail output | $0 by hand | No for reading by hand | Inference | Medium |
| monitor | Saved-search alerts, many narrow ones | Scheduled actor runs (needs permission) | $0 | Yes | Inference | Medium |

## Facts that decide the route

- **No official read API.** Indeed's job-posting docs cover employer and
  ATS integrations (Job Sync, XML publishing), not reading the job corpus
  (Official doc, overview updated 2 October 2026,
  https://docs.indeed.com/job-postings). A Publisher JavaScript Plugin
  exists but needs a partnership and an account representative (Official
  doc, https://docs.indeed.com/indeed-plus/publisher-js-plugin).
- **The old Publisher API is gone.** The timeline (sign-ups closed 2020,
  deprecated 2023, off in 2024) comes only from a vendor blog, so treat the
  dates as a Vendor claim (https://jobspipe.dev/blog/indeed-api-key,
  checked 6 October 2026).
- **Indeed has an app inside ChatGPT** for job seekers who connect an
  account. No batch API sits behind it that a nightly job could use
  (Official doc plus Inference, G6 report, not rechecked).
- **RSS is not dependable.** Feedly lists Indeed among boards without RSS
  (Independent report, C1 report, not rechecked).
- **Indeed blocks plain requests.** Actor pages say a browser plus
  residential proxies are needed (Vendor claim, C1 report, not
  rechecked). C3 reports that Indeed may ask for a login from page 2
  (Independent report, not rechecked).
- **Most listings likely copy employer ATS postings.** Indeed's own
  publishing integrations are how ATS jobs reach it (Official doc). What
  may exist only on Indeed: agency posts, small firms with no ATS, and
  employers on ATSs with no public feed (Inference, report C4). See
  [ats-feeds.md](ats-feeds.md).

### Email alerts

The shared design, terms reading and mailbox rules are in
[shared/email-alerts.md](../shared/email-alerts.md).
Indeed-specific facts:

- **Account needed.** "You must be signed in to your Indeed account to
  create job alerts." Daily or weekly; "You won't get a job alert email
  if there are no new jobs available that match your search." "You may
  be unable to create job alerts when searching internationally."
  Official doc, checked 6 Oct 2026 (round 2),
  https://support.indeed.com/hc/en-us/articles/204488890-Starting-Stopping-and-Managing-Job-Alerts.
- **30 jobs per email.** "Indeed Job Alerts are capped at 30 results per
  notification. To show all matches for your search ... click the all
  jobs link." Official doc via a search snippet (report C8); the page
  refused a direct fetch on 6 Oct 2026. Keep each alert under 30 new
  matches a day.
- **Contents.** In a sample from another country (deep research round 1,
  5 October 2026, private, not published, report C4): one job per
  "match" email, about every 3 days, with title, company, location, job
  type, work mode, benefits, salary in the preview and `cts.indeed.com`
  tracking links. The footer says not to forward the email. What Irish
  saved-search alerts contain is **not verified**.
- An open-source Gmail parser extracts title, company, location, work
  type and link from Indeed alerts (Independent report,
  https://github.com/chien-liu/googlesheet-add-on-auto-job-alert, G6, not
  rechecked).
- Full-description delivery is not documented (Not found). Use alerts
  as a **gap detector** (to find jobs the ATS feeds missed), not a full
  source.
- **Terms on parsing alerts.** Indeed's "Site" includes its "email
  messages", and the job seeker licence covers the "personal,
  non-commercial purpose of seeking employment". The automation ban that
  was read covers Indeed Apply, not reading. Parsing your own alerts fits
  the licence; following the links does not. Official doc (ToS, 17 July
  2026, via report C8) plus Inference.
- **Agents must never open the tracking links or job pages
  automatically.** Store title, company, location and job ID; match them
  against ATS feeds; a person opens unmatched items by hand.
- Whether to use alerts tied to the user's own Indeed account (or a
  separate job-search account, as C1 suggests) is a **user decision**.

### Paid option: Apify actors

Paid option, needs pilot permission and a terms review. Do not run it
before alerts are tried. Candidates (all Vendor claims, not rechecked
unless noted):

- `misceres/indeed-scraper` (maintained by Apify): C1 says "from $3.00 /
  1,000"; G1 says $5 per 1,000 on Starter and $6 on Free. G6 says its
  input schema lists `IE`; G1 could not find explicit Ireland support.
  The `externalApplyLink` field may return an Indeed redirect, so test it.
- `borderline/indeed-scraper`: $5 per 1,000, documents country `ie` (G1).
  G1 rates it the better first Ireland test.
- `leadproof/indeed-jobs`: $0.0005 per job plus $0.005 per run start (C1).
- Bright Data's Indeed scraper runs on its own servers; the corroboration
  noted a free 5,000 records a month (Vendor claim, G7). See
  [bright-data.md](../providers/bright-data.md).
- TheirStack lists Indeed among its sources (Vendor claim, report C8), so
  an aggregator query can stand in for some Indeed listings. See
  [job-data-apis.md](../providers/job-data-apis.md).

## Rules and risks for this site

- Indeed's Irish terms ban unapproved automated access, "including
  scraping and agentic access", and getting around blocks (Official doc,
  https://ie.indeed.com/legal, G6 report, not rechecked).
- C3 rates Indeed and Glassdoor scraping as medium risk and says avoid it
  entirely; use alerts. C1 recommends Apify actors. **We follow C3**
  (6 October corroboration): alerts only, unless a solicitor or Indeed
  says otherwise.
- A provider-hosted actor changes the technical exposure (our IP is not
  used), not the permission question (Inference, G6).
- Never scrape Indeed from the home connection. See
  [shared/rules.md](../shared/rules.md).

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | Publisher API dates (2020, 2023, 2024) stated as fact (C1) | The dates come from a vendor blog only | https://jobspipe.dev/blog/indeed-api-key, 6 October corroboration |
| 2026-10-06 | C1: Apify actor is the first route for Indeed | Alerts first; actor is a paid option needing permission and a terms review | Indeed and Glassdoor terms; C3; 6 October corroboration |

## Open questions

1. What do Irish Indeed alert emails contain beyond title, company and
   link (full description, salary, job key)? Look at one real email.
2. What share of Irish senior software roles on Indeed are agency posts
   with no employer named? ATS feeds can never cover these. One IrishJobs
   snapshot showed 33 of 77 senior software ads from agencies (report
   C9, undated, one board only).
3. Answered 6 Oct 2026: the terms that were read do not forbid parsing
   your own alerts; alerts carry at most 30 jobs each; no aggregator
   fully replaces alerts, though TheirStack lists Indeed as a source.

## Sources

- https://docs.indeed.com/job-postings (via G6, not rechecked)
- https://ie.indeed.com/legal (via G6, not rechecked)
- https://jobspipe.dev/blog/indeed-api-key (checked 6 October 2026)
- https://apify.com/misceres/indeed-scraper, https://apify.com/borderline/indeed-scraper (via C1, G1, G6)
- Deep research rounds 1 and 2 (5 and 6 October 2026; private, not published), reports C1, C3, C4, C8, C9, G1, G6, G7, and both
  corroboration rounds.
- Research bundles: see [SOURCES.md](../SOURCES.md).
