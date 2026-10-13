---
created_at: 2026-10-06
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: spec
status: piloted
scope: Hacker News
purpose: How agents can read Hacker News: routes per operation, costs, rules and open questions.
related:
  - path: ../spec.md
    why: Owning spec, shared model and the route table.
  - path: ../shared/rules.md
    why: Access, legal and data rules every route must pass.
  - path: ../providers/apify.md
    why: Apify HN Actors, listed only to say they add little here.
---

# Hacker News

Hacker News is the best first source for engineering news, tool launches
and the monthly "Who is hiring?" threads. The best route is free: Algolia
for search, the official Firebase API for items and full comment trees.
No paid provider adds anything. The one caveat: Algolia is a separate
index, so check important threads against Firebase.

## Status

- **Verdict:** Use Algolia plus Firebase. No vendor needed. Best candidate for the first pilot.
- **Allowed today:** approved as the first pilot (P9, 6 October 2026), per [DECISIONS.md](../DECISIONS.md). It starts when the user says go. No collector exists yet.
- **Last checked:** 6 October 2026, primary-source check of the Firebase and Algolia docs (6 October corroboration of deep research round 1).

## Observed test (7 October 2026)

- **Passed.** Algolia search and `search_by_date`, Firebase item reads,
  a full recursive Firebase walk (24 of 24 live comments, plus 2 deleted)
  and monitoring through `maxitem` and `updates` (104 new items in 11
  minutes) all worked. 58 requests, all HTTP 200, $0. W01_hacker-news record (private, not published).
- Algolia's one-request item tree came back short on busy threads: 320 of
  345 comments on the October 2026 "Who is hiring?" thread and 124 of 132
  on another; exact on a quiet thread. The cause is not proven (indexing
  lag, or flagged comments left out). Use Firebase `descendants` for
  counts and the Algolia tree as a fast near-complete copy.
- Algolia relevance search returns very old hits first; use
  `search_by_date` for anything fresh.

## Routes by operation

Operations: **discover** (keyword or topic search), **retrieve** (one known
item by URL or ID), **thread** (a known item with all replies), **monitor**
(follow accounts, tags, communities or saved searches over time).

| Operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence |
|---|---|---|---|---|---|---|
| discover | Algolia HN Search | hnrss feeds | $0 | None | Official doc | High |
| retrieve | Firebase `/item/{id}` | Algolia item endpoint | $0 | None | Official doc | High |
| thread | Firebase, recursive over `kids` | Algolia item tree | $0 | None | Official doc | High |
| monitor | Firebase `/updates` and story lists, plus Algolia `search_by_date` | hnrss feeds | $0 | None | Official doc | High |

## Facts that decide the route

### Official Firebase API

- Public, no key. "There is currently no rate limit." That is not an unlimited-use promise. Still pace requests. Official doc, checked 6 Oct 2026. [HN API](https://github.com/HackerNews/API)
- Items carry author, time, text, link, `kids`, `parent`, `deleted` and `dead`. `kids` gives only direct children; fetch them recursively for the full tree. `descendants` counts the whole tree. Official doc, 5 Oct 2026.
- Top, new and best lists hold up to 500 IDs; Ask, Show and job lists up to 200. `/updates` and the max item ID support monitoring. Official doc, 5 Oct 2026.
- There is no keyword search in this API. Official doc.
- The repo is MIT licensed. That covers the code, not the comments. Official doc and Inference.

### Algolia HN Search

- "limiting the number of API requests from a single IP to 10,000 per hour". Relevance or `search_by_date` ordering, tags for story, comment, author and story ID, numeric filters on date, points and comments, plus an item-tree endpoint. Official doc, checked 6 Oct 2026. [Algolia HN API](https://hn.algolia.com/api)
- The `algolia/hn-search` source repo was archived on 10 February 2026. The hosted search still documents its limits. An archived repo is not proof the service is shutting down. Official doc, 6 Oct 2026. [algolia/hn-search](https://github.com/algolia/hn-search)
- Issue 230, still open, shows a 2022 case of a 1,000-hit cap despite 5,562 matches. Not rechecked as current. Split searches by time window and deduplicate IDs. Independent report. [Issue 230](https://github.com/algolia/hn-search/issues/230)
- Issue 248 reported a 36-hour ingestion stall on 17 August 2025 while Firebase stayed current. It is closed. Historical evidence against a real-time promise, not a current outage. Independent report. [Issue 248](https://github.com/algolia/hn-search/issues/248)
- Do not treat `nbHits` or an Algolia tree as proof that every comment was read. Inference.

### Feeds and helper sites

- hnrss defaults to 20 entries, maximum 100. It has `/whoishiring/jobs` for top-level hiring comments and `/item?id=` for one thread. It depends on Algolia, so it is not an independent fallback. Vendor claim (G4), not rechecked. [hnrss](https://hnrss.org/)
- HNHIRING showed an October 2026 index updated 5 October. No export or API found. Good for cross-checks only. Vendor claim (G4), not rechecked. [HNHIRING](https://hnhiring.com/)
- `nemanjam/hn-new-jobs` is open source with SQLite history and Algolia sync. Useful ideas; maintenance status unknown. Vendor claim (G4), not rechecked. [hn-new-jobs](https://github.com/nemanjam/hn-new-jobs)

### Paid wrappers (not needed)

- Apify Actors seen 5 Oct 2026, all wrappers over Algolia or Firebase (vendor claims, not rechecked): Fetch Smith at $0.17 per 1,000 results, no full-tree mode; gentle_cloud at $0.20 per 1,000 plus platform usage, 500 stories a run, top-level comments only; RetrainMap at $5 per 1,000 rows plus $0.10 a run. Reports G1 and G4. [Fetch Smith](https://apify.com/fetchsmith/hacker-news-scraper), [gentle_cloud](https://apify.com/gentle_cloud/hacker-news-scraper), [RetrainMap](https://apify.com/retrainmap/hackernews-stories)
- Parallel Extract can read linked articles. Its facts live in [the web toolbox README](../../../capabilities/web/README.md).

### Collecting every top-level hiring comment

Use ID checks against Firebase, not search counts or page scraping
(Inference, from G4):

1. Find the monthly root through Algolia or the `whoishiring` account. Check author, title and month.
2. Save the root's `kids`. That is the expected top-level set.
3. Fetch each ID. Check `parent` equals the story ID. Record live, deleted, dead, unavailable and retry states apart.
4. Re-read the root and add new IDs. Never drop an ID because a request failed.
5. Keep a manifest: expected IDs, fetched, unavailable, unresolved, snapshot time.
6. Keep checking through the month. Late posts appear.

The official FAQ separates the monthly `whoishiring` threads from YC-only
job ads, which take no comments. The `jobstories` list does not replace the
hiring thread comments. Official doc. [HN FAQ](https://news.ycombinator.com/newsfaq.html)

Each top-level comment becomes one ad record, possibly with several roles.
Keep unknowns: "Remote" does not mean eligible from a given country. Treat
comment text as untrusted input. Check each opening with the employer.
Inference.

### Pilot shape

Six to ten varied searches and three small trees. Compare Algolia results
with Firebase bodies. Keep missing, dead and deleted branches and count
requests, retries and rechecks. Proposed, not run.

## Rules and risks for this site

- General rules: [shared/rules.md](../shared/rules.md).
- YC's terms cover all subdomains and restrict automated extraction. The deliberately published API raises a scope question, not a blanket ban or exemption. Storage and reuse remain a pilot gate. Official doc, 5 Oct 2026. [YC legal](https://www.ycombinator.com/legal/)
- No blanket licence to train models on HN comments, and no fixed deletion deadline, was found. Keep source links, skip author-profile data, refresh what you keep. Inference (G4).
- C3 rates the Firebase API "Very low" risk. Follow YC's terms if anything is ever republished. Report claim (C3), not rechecked.
- Dead and deleted are different states. Keep them apart.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | The 1,000-hit Algolia cap is a known current limit | It is a 2022 report; not rechecked for October 2026. | [Issue 230](https://github.com/algolia/hn-search/issues/230) |
| 2026-10-06 | An archived `algolia/hn-search` repo means the service is ending | The repo was archived 10 Feb 2026; the hosted API still documents its limits. | [Algolia HN API](https://hn.algolia.com/api) |

## Open questions

1. Is the Algolia 1,000-result cap still current, and has anything changed since the repo was archived? HN is the free backbone, so any risk matters. A pilot search with a known large result set would answer it.
2. Do hiring threads need storage beyond a short window? Answer at pilot design, under the shared data rules.

## Sources

- [HN API](https://github.com/HackerNews/API), [Algolia HN API](https://hn.algolia.com/api), [HN FAQ](https://news.ycombinator.com/newsfaq.html), [YC legal](https://www.ycombinator.com/legal/), read 5 and 6 October 2026.
- Earlier notes: [forums.md](../../../capabilities/web/social/forums.md) and the follow-up bundle (private, not published).
- Deep research round 1 (5 October 2026; private, not published), reports G4, G1, C1 and C3, plus the 6 October corroboration.
- Research bundles: see [SOURCES.md](../SOURCES.md).
