---
created_at: 2026-10-06
updated_at: 2026-10-06
model: claude-opus-5-5
doc_type: spec
status: researched
scope: Google Jobs (Google for Jobs search panel)
purpose: How agents can read Google Jobs results: not a route for Ireland; usable for listed countries through a SERP API.
related:
  - path: ../spec.md
    why: Owning spec, shared model and the route table.
  - path: ../shared/rules.md
    why: Access, legal and data rules every route must pass.
  - path: ../providers/serpapi.md
    why: SerpApi prices and limits.
---

# Google Jobs

Google's jobs panel gathers listings from many boards and employer sites.
**It is not a route for Ireland:** Google's own list of supported
countries leaves Ireland out, and so does SerpApi's. For countries on the
list, a SERP API (a service that returns Google results as data) can
read it.

## Status

- **Verdict:** excluded for Ireland; usable for listed countries.
- **Allowed today:** not for Ireland. Other countries need pilot
  permission, per [DECISIONS.md](../DECISIONS.md).
- **Last checked:** 6 October 2026, primary-source check in the
  6 October corroboration.

## Routes by operation

| Operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence |
|---|---|---|---|---|---|---|
| search (Ireland) | None | none | n/a | n/a | Official doc | High |
| search (listed countries) | SerpApi `google_jobs` engine | ScrapingDog or SearchAPI.io | See [serpapi.md](../providers/serpapi.md) | API key only | Official doc (pricing, via C4) | Medium |
| detail | Follow the source link by hand or via the ATS feed | none | $0 | No | Inference | Medium |
| monitor | Scheduled SERP queries (listed countries) | none | Per search | API key only | Inference | Low |

## Facts that decide the route

- Google's JobPosting page (last updated 8 September 2026) lists exactly
  14 European countries: "Austria, Belarus, Belgium, Denmark, France,
  Germany, Greece, Italy, Netherlands, Portugal, Russia, Spain,
  Switzerland, United Kingdom". **Ireland is not listed** (Official doc,
  https://developers.google.com/search/docs/appearance/structured-data/job-posting,
  checked 6 October 2026).
- SerpApi's Google Jobs country list has gb, uk, de, fr, nl and others but
  **no `ie`** (Official doc, https://serpapi.com/google-jobs-countries,
  checked 6 October 2026).
- No first-hand evidence either way of a jobs panel on google.ie. The
  only hit was a 2022 SEO-vendor page about search interest, not proof.
- SerpApi's status page reported "low success rates for the Google Jobs
  API" (Official doc, status page, checked 6 October 2026).
- Other engines (Vendor claims or Independent reports, C4, not
  rechecked): ScrapingDog Google Jobs API, 5 credits per request, Lite
  $40 a month; SearchAPI.io Developer $40 a month for 10,000 searches.
  Serper and DataForSEO Google Jobs support or pricing: Not found.
- JSearch (OpenWeb Ninja) advertises Indeed among its Google Jobs
  sources; that does not prove Irish coverage (Vendor claim, G6).

## Rules and risks for this site

- Use only through a SERP API on the provider's servers, never scraping
  Google from the home connection. See
  [shared/rules.md](../shared/rules.md).
- Google results repeat jobs from other boards. Deduplicate against ATS
  feeds before any paid analysis.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | C1: use SerpApi Starter ($25 a month) with `gl=ie` for Google Jobs in Ireland | Ireland is on neither Google's nor SerpApi's list; the $25 plan is dropped | Google JobPosting page (8 Sep 2026); serpapi.com/google-jobs-countries |

## Open questions

1. Does google.ie show a jobs panel at all? One free `gl=ie` query on
   SerpApi's free tier would settle it. Do not pay for it on current
   evidence.

## Sources

- https://developers.google.com/search/docs/appearance/structured-data/job-posting (checked 6 October 2026)
- https://serpapi.com/google-jobs-countries (checked 6 October 2026)
- Deep research round 1 (5 October 2026; private, not published),
  reports C1, C4, G6, and the 6 October corroboration.
- Research bundles: see [SOURCES.md](../SOURCES.md).
