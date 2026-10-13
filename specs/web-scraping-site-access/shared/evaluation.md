---
created_at: 2026-10-06
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: spec
status: active
scope: Testing routes and adding platforms or providers
purpose: The decision rule for adding a platform or provider, how to test a route before trusting it, what to measure, and when to keep or drop a source.
related:
  - path: ../spec.md
    why: Owning spec and route table.
  - path: ./rules.md
    why: Rules a route must pass before any test.
  - path: ../STATE.md
    why: Which tests are proposed or approved.
  - path: ./email-alerts.md
    why: The email alert route, moved out of this file.
---

# Testing routes and adding sources

A route is only "working" after an Observed test: our own dated run with a
saved record. Research reports and vendor pages are where tests start, not
proof.

## Decision rule for adding a platform

Merged from reports G8 (section 4) and C3 and the 6 October checks.

1. **Purpose.** Write down what this platform adds that current sources
   miss. If nothing, stop.
2. **Permission check.** Read its terms, robots.txt and ai.txt. Look for a
   login wall or CAPTCHA. If it objects or needs a login to view, stop:
   email alerts only, or leave it out.
3. **Simplest route first.** Official API or open protocol, then RSS or
   public feeds, then email alerts, then search-engine discovery.
4. **Provider only if step 3 misses useful content.** One provider, no
   personal credentials, terms that accept our status, a hard spend cap
   (reports suggest a total budget of $25 to $100 a month).
5. **Test the four operations separately** (discover, retrieve, thread,
   monitor; or search and detail for jobs). Support for one says nothing
   about the others.
6. **Apply the data rules** in [rules.md](rules.md).
7. **Write the site file** from the template and add a row to the route
   table, with status "researched" until a test passes.
8. **Review monthly.** Keep a source only if its useful new finds are
   worth its cost and upkeep.

## Decision rule for adding a provider

1. It covers at least one platform where our free routes fail.
2. Its terms accept an individual customer, or the user has decided how to
   qualify. Quote the clause in the provider file and add a row to
   [eligibility.md](eligibility.md).
3. It does not collect from a platform whose terms forbid it even when
   logged out (Meta), and it is not a source of LinkedIn-derived data if
   proposal P10 is accepted.
4. It runs on its own servers and IPs and needs no cookies or accounts of
   ours.
5. It has a spend cap or prepaid credits, so a bug cannot run up a bill.
6. Failed or blocked calls are free, or the cost of failures is known.
7. Prefer one provider for many platforms over many single-platform
   subscriptions, but never on logo count alone.
8. Prefer a provider that says how it gets its data. A vendor that
   scrapes through residential proxies carries the platform's legal
   fight with it (Reddit v SerpApi).

## How to run a pilot (once the user approves one)

- **Scope it in writing:** platforms, operations, queries, date window,
  maximum items, maximum spend, where raw data is kept and when it is
  deleted. Record it in [DECISIONS.md](../DECISIONS.md).
- **Use free routes and free tiers first:** Arctic Shift for Reddit (no
  key), ReefAPI's 1,000 credits, Apify's $5 a month, RedditAPIs.com's
  $0.50, ScrapeCreators' 100 credits, SerpApi's 250 searches, Brave's $5
  monthly credit, X's spending limit set to $1 for a reply-completeness
  test (prices in the site and provider files).
- **Run from hosted infrastructure** where possible, so the home IP is not
  involved, and set the spend limit before the first call.
- **Keep a test record** for every run: date, route, provider, query,
  items returned, items billed, failures, cost charged, time taken.

## Choosing an Apify Actor

Added 7 October 2026, from the first Apify runs.

- **Rank by Store data, not by research mentions.** The public Store API
  (`https://api.apify.com/v2/store?search=<term>&sortBy=popularity`, no
  token) returns monthly users, rating, number of ratings, 30-day run
  outcomes and pricing. Our research had picked Actors with 1 monthly
  user. store_rank.py (private, not published) prints a ranked table.
- **Then check what users and Store data say against it.** Most users is
  not enough: the two most used X Actors are the $320 duplicate-rows case
  and the placeholder-tweet case. Look at the rating, the number of
  ratings and the 30-day success rate together.
- **Cap every run:** `maxItems`, `maxTotalChargeUsd`, `timeout` and
  `memory` on the run call. Apify's monthly usage figure lags behind
  runs, so it cannot serve as a live budget stop.
- **Drop personal fields** some Actors add (recruiter names, contact
  phones and emails) before storing anything (rules.md, rule 11).

## Test harness

Tests of our own requests use polite.py (private, not published): it
checks the VPN before and during a run, keeps 5 to 15 seconds between
requests per site, backs off on errors and logs every request. Workers
must run their scripts in the foreground: a background script dies when
an OpenCode session ends.

## What to measure

| Measure | Why |
|---|---|
| Useful new items per week | The point of a source. Raw counts mislead because job boards repeat the same listing 3 to 5 times (TheirStack and Lightcast vendor claims). |
| Recall on a known set | Pick 10 to 20 items we know exist (recent posts, known threads, known open jobs) and see how many the route finds. |
| Reply completeness | For thread routes, compare replies returned with replies visible on the page. |
| Freshness | Delay between an item's own timestamp and when the route returns it. |
| Cost per useful item | Including start fees, compute, proxy charges and failed calls. |
| Failure rate | Timeouts, empty results, blocks. A "succeeded" run status is not proof the data is right. |
| Upkeep | Hours spent fixing breakage per month. |

## Job sources: measure overlap before paying

From report C4. Run for one week before buying any job-board route:

1. Parse the alert emails or test results into records: company, title,
   location, source, job ID.
2. Match them against the employer feeds already read (normalized company
   name, fuzzy title match).
3. Sort the misses: company on a supported job system but not yet
   followed (fixable), company on an unsupported system, agency post,
   board-only post, or irrelevant re-post.
4. Coverage = matched / relevant unique listings. Report it before and
   after adding the fixable companies.
5. Pay for a board route only if coverage stays low after the fixes. C4
   suggests 90 percent as the bar.

## Email alerts as a route

Moved to its own file on 6 October 2026:
[email-alerts.md](email-alerts.md) (per-board limits, how to make
each email complete, what the terms say, and how to read the mailbox).
