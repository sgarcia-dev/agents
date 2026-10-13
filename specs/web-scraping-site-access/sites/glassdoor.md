---
created_at: 2026-10-06
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: spec
status: researched
scope: Glassdoor
purpose: How agents can read Glassdoor: do not read it separately; it is part of Indeed.
related:
  - path: ../spec.md
    why: Owning spec, shared model and the route table.
  - path: ../shared/rules.md
    why: Access, legal and data rules every route must pass.
  - path: ./indeed.md
    why: Glassdoor jobs are covered through Indeed.
  - path: ../providers/apify.md
    why: Apify actor facts, only if company reviews are ever needed.
---

# Glassdoor

Glassdoor legally merged into Indeed, Inc. on 1 July 2026 and now runs
under Indeed's terms. Do not read Glassdoor jobs separately: cover them
through [indeed.md](indeed.md).
Its terms ban automated agents without written permission.

## Status

- **Verdict:** do not read separately. Indeed and employer ATS feeds
  cover its jobs.
- **Allowed today:** no scraping, per [DECISIONS.md](../DECISIONS.md).
- **Last checked:** 6 October 2026, primary-source checks in the
  6 October corroboration.

## Observed test (7 October 2026)

- **User-directed Apify test:** valig/glassdoor-jobs-scraper (1,387
  monthly users) returned 10 real Irish jobs from glassdoor.com listings,
  so Glassdoor job search still serves listings after the merge. How much
  they duplicate Indeed was not measured. A01_apify record (private, not published).

## Routes by operation

| Operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence |
|---|---|---|---|---|---|---|
| search | None. Use Indeed alerts and ATS feeds | Glassdoor alert emails (user decision) | $0 | Yes, for alerts | Official doc + Independent report | High |
| detail | Open by hand | none | $0 | No | Inference | High |
| monitor | None separately | Glassdoor alerts | $0 | Yes | Inference | Medium |

## Facts that decide the route

- "Glassdoor legally merged into Indeed, Inc. on July 1" 2026 (Independent
  report, https://www.reworked.co/employee-experience/glassdoor-folds-into-indeed/,
  24 July 2026, and Wikipedia; checked 6 October 2026). New Glassdoor
  users have needed an Indeed login since November 2025.
- Glassdoor's terms were revised on 1 July 2026 to describe Indeed's role;
  applications through Glassdoor use Indeed services (Official doc, G6
  report, not rechecked).
- "Glassdoor no longer supports API partnerships" (Official doc,
  https://help.glassdoor.com/s/article/Glassdoor-API, updated 26 November
  2024, checked 6 October 2026).

### Email alerts

- Alerts are daily or weekly and need an account. "Job seekers can
  create a maximum of 10 job alerts per day" (a creation limit, not 10
  jobs per email). Remote is not an accepted alert location, and other
  search filters may not carry into alerts. Official doc, search excerpt
  of the help article checked 6 Oct 2026 (round 2); filters per G6.
- Indeed logins work on Glassdoor, and Indeed's partner terms describe "a
  comprehensive feed delivered to the Indeed Platform, which includes ...
  Glassdoor". So Glassdoor alerts mostly repeat Indeed. Use 2 to 4 as a
  cross-check at most. Official doc via report C8. Design and terms
  reading: [shared/email-alerts.md](../shared/email-alerts.md).
- Contents per email: Not found. Expect heavy filtering on our side.
- Agents must never open tracking links or job pages automatically.
- Whether to use alerts tied to the user's own account is a user
  decision. Indeed alerts likely cover the same jobs.

## Rules and risks for this site

- Glassdoor's terms (issued by Indeed, Inc.) forbid using "automated
  agents … to scrape, strip, or mine data … without our express written
  permission" (Official doc, https://www.glassdoor.com/about/terms/, via
  C3 search snippets, not rechecked).
- C1 lists an Apify Glassdoor actor as a runner-up (for example
  `bebity/glassdoor-jobs-scraper`, $0.35 per 1,000 jobs, G1, Vendor
  claim). We follow C3: no scraping. Only reconsider for company reviews,
  with pilot permission and a terms review.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|

## Open questions

1. Is "10 per day" Glassdoor's only alert limit? Not found.
2. Answered 6 Oct 2026 for Indeed (see indeed.md); Glassdoor's own terms
   on alert emails were only seen through a third party (report C8).

## Sources

- https://help.glassdoor.com/s/article/Glassdoor-API (checked 6 October 2026)
- https://www.reworked.co/employee-experience/glassdoor-folds-into-indeed/ (checked 6 October 2026)
- https://www.glassdoor.com/about/terms/ (via C3, G6)
- Deep research rounds 1 and 2 (5 and 6 October 2026; private, not published), reports C1, C3, C8, G1, G6, and both corroboration
  rounds.
- Research bundles: see [SOURCES.md](../SOURCES.md).
