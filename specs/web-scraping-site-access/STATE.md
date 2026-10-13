---
created_at: 2026-10-06
updated_at: 2026-10-12
model: claude-opus-5-5
doc_type: state
status: first pilot done (7 October 2026); P10, P12, P13 open
scope: Reading public platforms and choosing data providers
related:
  - path: ./spec.md
    why: Shared model, route table and provider table.
  - path: ./DECISIONS.md
    why: User rules and the proposals waiting for the user.
  - path: ./SOURCES.md
    why: Bundles and weak claims to avoid.
---

# Web scraping site access: state

## What is true now (7 October 2026, after the first pilot)

- **12 October 2026: first full read of a job alert mailbox**, with the
  jobs it listed followed to their pages under a user rule: never open
  tracking links, employer site first, board pages last, per-site caps
  (2 a minute; 1 a minute and 30 an hour on high-risk boards). What each
  board's email holds: [shared/email-alerts.md](shared/email-alerts.md).
  Rule: [DECISIONS.md](DECISIONS.md).

- **First pilot done, 7 October 2026** (bundle: private, not published).
  Observed tests passed for Hacker News, Reddit comment trees through
  Arctic Shift, employer job feeds on six systems (including Workday and
  keyless SmartRecruiters), Bluesky reads and Jetstream, Mastodon hashtags, Lobsters and DEV, and X's
  free syndication endpoint for known tweets. Each site file has an
  "Observed test (7 October 2026)" section. All free, no blocks.
- **Apify tested** (free plan, $5 a month cap). 11 capped runs cost $0.27: real data from Reddit
  (harshmaur), X search, LinkedIn jobs, Glassdoor, Indeed, IrishJobs and
  Jobs.ie (Black Falcon). memo23's StepStone Actor returned nothing but
  charged its start fee. Actors are now chosen from Apify Store data
  (monthly users, rating, 30-day success rate), not research mentions.
- No collector, schedule or paid plan exists yet.
- Two social research rounds (44 reports, 5 October), deep research round
  1 (13 reports) and round 2 (6 Claude reports, C5 to C10) were checked
  against primary sources on 6 October in two corroboration rounds (about
  60 and about 130 claim checks). The results are in the site, provider and
  shared files. Wrong claims, including two of our own round 1
  corrections that turned out wrong, are in [SOURCES.md](SOURCES.md).
- **Round 3, what real users say** (10 ChatGPT reports, G10 to G19, 6
  October; about 60 claims checked against primary pages). Each site and
  provider file has a "What users say (round 3)" section. Headlines:
  Apify has the most user support, with the risk in single Actors and
  unpredictable bills; TwitterAPI.io leads for X, on thin evidence;
  Bright Data is solid but overbuilt and business-only; ScrapeCreators
  has a few real users but terms that let it expire credits; ReefAPI and
  SociaVault have no independent users; no vendor is trusted for
  LinkedIn. No report could read X posts, and review sites are partly
  paid or invited.
- **Free routes:** Hacker News, Bluesky reads and the Jetstream live
  stream, Mastodon hashtag and account timelines, employer job feeds, and
  the Arctic Shift archive for Reddit.
- **Need a separate research account (P6):** Bluesky search (anonymous
  search is now refused) and Mastodon post search (anonymous search
  returns no posts).
- **X:** the official pay-per-use API accepts an individual and has a
  hard spending limit; about $25 for 5,000 posts (P12).
- **Threads:** excluded by the user (P11).
- **Reddit:** official API closes to new requests on 31 Oct 2026; route
  order is now Arctic Shift, a paid vendor, then search discovery.
- **LinkedIn:** excluded for direct reads. Whether to buy LinkedIn data
  from vendors is open (P10), to be judged from genuine user opinions.
- **Jobs:** Google Jobs does not cover Ireland; Glassdoor is part of
  Indeed. Alerts are the low-risk route to the boards but are capped (30
  per Indeed email, three IrishJobs alerts). Workday is the biggest gap
  in employer feeds.
- **Rules:** own requests run from home behind the user's VPN, one request
  every 5 to 15 seconds per site; robots.txt, ai.txt and CAPTCHAs do not
  stop a run (user decisions). Raw text is kept 30 days.
- **Vendors:** the user decided to sign up to Apify as a business (P1).
  Which providers to pay long term is open (P13).

## Decided on 6 October 2026

The user answered P1 to P15 (see [DECISIONS.md](DECISIONS.md)). Still open:
P10 (LinkedIn vendor data), P12 (X route) and P13 (providers and budget).
The user-opinion research they waited on is done (round 3). The
proposals below are the agent's; the user decides.

## Proposals for the open choices (agent's, 6 October 2026)

- **P12, X route.** Test TwitterAPI.io first with a small top-up (unused
  top-ups are refundable on request within 30 days), and the official
  API under a $1 spending limit, on the same three known threads. Keep
  whichever returns more of the replies. Official stays the fallback.
  Why: users favour TwitterAPI.io, it is about 30 times cheaper, but
  nobody has measured reply completeness.
- **P13, providers and budget.** Paid core: Apify (free tier first,
  Starter at $19 only after measuring cost per 1,000 items) and the X
  route from P12. Free core: Arctic Shift, Hacker News, Bluesky,
  Mastodon, employer feeds. Free credits only: ScrapeCreators (then the
  smallest pack, if it passes), SociaVault, ReefAPI. Not now: Bright Data
  (business-only, overbuilt here), RedditAPIs.com (only if Arctic Shift
  fails), ScrapFly (only for a measured fetch gap). Budget: about $20 to
  $30 a month. Every paid run gets a money cap.
- **P10, LinkedIn vendor data.** Keep it excluded. Users report missing
  posts and empty profile fields, vendors keep being sued or shut, and
  LinkedIn's terms reach bought data. Jobs come from employer feeds and
  alerts. If the user wants one test anyway: a single capped run of the
  curious_coder jobs Actor (no cookies, jobs only, no profiles).

## Action items, in priority order

1. **The user creates accounts** (agents never register): the job boards
   used for alerts, an X and a Bluesky research account, Apify (as a
   business) and ReefAPI.
2. **Alert mailbox setup:** labels and filters so alert emails stay out of
   the main inbox.
3. **Board profiles and alerts:** a browser agent inspects each site,
   proposes, then sets up as many alert emails as the site allows.
   LinkedIn is form filling only (see DECISIONS.md).
4. **Done 7 October 2026: pilot part 1** (Tier 0: Hacker News, Reddit
   through Arctic Shift, job feeds, Bluesky, Mastodon, Lobsters, DEV, X
   syndication). Next: turn the passing routes into a small reader (the
   social research setup), and propose which ones get a thin adapter in
   the web-search skill (AGENTS.md, "Relation to web search").
5. **Partly done 7 October 2026: pilot part 2.** Apify Actors tested
   (10 items each). Still to do: ReefAPI free credits; the Black Falcon
   two-run incremental test; overlap between the boards, Indeed, LinkedIn
   jobs and the employer feeds.
6. **Email digest:** a read-only reader over the alert mailbox labels that
   turns alerts into one digest, matched against employer feeds.
7. **Done 6 October 2026:** the user-opinion investigation (round 3).
   Next is the user's answer on P10, P12 and P13 (proposals above).
8. **Pilot additions from round 3:** X syndication and batch Arctic
   Shift lookups done 7 October (both work; Arctic Shift's timeout answer
   is HTTP 422, not 429). Still to do: the incremental test, now Black
   Falcon only (parsebird has 1 monthly user).
9. **Leads, not yet evaluated:** YouTube (official Data API, 1 unit per
   comments call, 10,000 units a day, plus yt-dlp) has no site file yet;
   add one only if YouTube becomes a research need.

## Next action

Items 1 to 3 are the user's. The user also answers
P10, P12 and P13 (proposals above). Items 4 and 5 continue when the user says go. Record each pilot's scope and results by
[shared/evaluation.md](shared/evaluation.md) and mark the route "piloted" in its site file.

## Time-sensitive dates

| Date | What |
|---|---|
| 30 Oct 2026 | EDPB web scraping guidelines consultation closes. |
| 31 Oct 2026 | Reddit stops accepting new public API requests. |
| 13 Nov 2026 | Reddit RSS feeds end. |
| 30 Nov 2026 | Reddit migration bounty registration closes. |
| 1 Jan 2027 | Google Custom Search JSON API ends for existing customers. |
| 12 Jan 2027 | Reddit starts removing unregistered API access. Re-test Reddit sources. |
| March 2027 | Reddit's remaining public API access ends. Re-test Reddit sources, Arctic Shift first. |
| 5 Apr 2027 | Next court date in Reddit v SerpApi. |
