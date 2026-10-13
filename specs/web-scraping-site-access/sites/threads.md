---
created_at: 2026-10-06
updated_at: 2026-10-06
model: claude-opus-5-5
doc_type: spec
status: excluded
scope: Threads
purpose: How agents can read Threads: routes per operation, costs, rules and open questions.
related:
  - path: ../spec.md
    why: Owning spec, shared model and the route table.
  - path: ../shared/rules.md
    why: Access, legal and data rules every route must pass.
  - path: ../shared/legal.md
    why: Meta's terms on automated collection and what they mean here.
  - path: ../providers/apify.md
    why: No-login Threads Actors.
  - path: ../providers/social-apis.md
    why: ScrapeCreators and EnsembleData facts.
  - path: ../providers/reefapi.md
    why: ReefAPI lists a Threads engine.
  - path: ../providers/mcp-servers.md
    why: Threads MCP wrappers and their account needs.
---

# Threads

Threads is Meta's text network. It is the weakest of the four social sites
for agents, and today it has **no route open to us**. Official search of
other people's posts needs Advanced Access, and Meta requires Business
Verification for that, which an individual without a registered business
cannot pass. Meta's terms (Threads takes in Instagram's) ban automated
collection without express permission "regardless of whether" you are
logged in, so the no-login vendor Actors break Meta's terms, not just sit
in a grey zone. Vendor routes also see only 20 to 30 top replies.

## Status

- **Verdict:** Excluded. The user decided on 6 October 2026 (P11): "Let's deprecate threads", as it is small and not worth it. The research below is kept in case that changes.
- **Allowed today:** no (excluded).
- **Last checked:** 6 October 2026, primary-source check of Meta's keyword search and permissions pages, the Instagram Terms and the Threads terms (round 1 and round 2 corroboration). Vendor prices are not rechecked.

## Routes by operation

| Operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence |
|---|---|---|---|---|---|---|
Every vendor route below breaks Meta's terms on automated collection (see Rules). They are listed for completeness, not as options.

| Operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence |
|---|---|---|---|---|---|---|
| discover | None open to us. Official `keyword_search` needs Advanced Access, which needs Business Verification. | No-login Apify Actor or ScrapeCreators search (against Meta's terms) | Official $0 but out of reach; vendors about $5 to $13 | Meta app, Threads account and a verified business | Official doc; Vendor claim | High that the official route is closed |
| retrieve | None open to us. | ScrapeCreators post endpoint or Mine Works Actor (against Meta's terms) | Per request or per post | Vendor key | Vendor claim | Low |
| thread | None. `threads_read_replies` only covers threads the app user owns. | futurizerush replies Actor (against Meta's terms; logged-out subset only) | From $2.50 per 1,000 results | Vendor key | Official doc; Vendor claim | High that the official route is closed |
| monitor | Follow federated Threads accounts from a Mastodon server (only accounts that turned on federation). | Vendor polling (against Meta's terms) | $0 | None for reading a Mastodon server's view | Official doc plus Inference | Medium |

## Facts that decide the route

### Official API

- Keyword search uses `threads_basic` and `threads_keyword_search`. "If your app has not been approved for the threads_keyword_search permission, the search will be performed only on posts owned by the authenticated user." Official doc, checked 6 Oct 2026, [keyword search](https://developers.facebook.com/docs/threads/keyword-search).
- **Business Verification blocks an individual.** Meta's permissions reference: "Business Verification ... is required for all apps making requests for Advanced Access". Searching public posts needs Advanced Access for `threads_keyword_search`. Meta never says "individuals cannot apply", but Business Verification needs a legal business. Official doc, checked 6 Oct 2026 (round 2), [permissions](https://developers.facebook.com/docs/permissions); Inference for the conclusion.
- Replies: `threads_read_replies` is "to get replies to a thread owned by the app user". So the official API cannot read replies under other people's posts. Official doc, same page.
- Review time: no official figure. Forum anecdotes cite review over a month and Business Verification "stuck in review for over 60 days". Independent report (anecdote), report C7.
- Cap: "A user can send a maximum of 2,200 queries within a rolling 24-hour period." Queries with no results do not count. The limit is per user across all apps. Up to 100 results per call. Official doc, checked 6 Oct 2026, same page.
- Signup needs a Meta developer account, a Threads-use-case app, a Threads account and OAuth. No review time, sole-developer rule or public price is published. Official doc, report G3, not rechecked, [get started](https://developers.facebook.com/documentation/threads/get-started).
- Long-lived tokens last 60 days and can be refreshed after 24 hours. Official doc, report G3, not rechecked, [tokens](https://developers.facebook.com/documentation/threads/get-started/long-lived-tokens).
- A 2 Sep 2026 forum post reports a developer-registration loop at phone verification. Independent report, report G3, [Meta forum](https://communityforums.atmeta.com/discussions/Questions_Discussions/developer-registration-loop-final-submit-bounces-back-to-phone-verification-sms-/1382124).

### Vendor routes (all against Meta's terms; prices not checked against a primary source)

- **Reply completeness is poor everywhere.** ScrapeCreators' own write-up tells readers to ask for "themes in the nine comments retrieved" from a post with 4,795 replies. EnsembleData says Threads "returns at maximum the 20-30 most popular replies". Vendor claims, report C7; ScrapeCreators confirmed 6 Oct 2026, EnsembleData not found on recheck.
- Newer Apify Actors (report C7, 5 to 6 Oct 2026, Vendor claim): scrapersdelight keyword search "$1 per 1,000 posts, no per-run fee"; fetch_cat replies from $0.11 per 1,000 replies plus a start fee (4 users); logical_scrapers search $1.99 to $2.49 per 1,000; headply notes "Threads rate-limits single IP addresses quickly".

- **Apify The Mine Works:** $1.80 per 1,000 posts plus $0.002 per start. No login. Posts, profiles, keyword and hashtag search, monitoring. Vendor claim, report G1, 5 Oct 2026, [Actor](https://apify.com/themineworks/threads-scraper).
- **Apify futurizerush Threads Scraper:** $2.50 per 1,000 records plus $0.005 per start. No login. "Replies" means the user's own reply posts, not a full discussion. Vendor claim, report G1, [Actor](https://apify.com/futurizerush/meta-threads-scraper).
- **Apify futurizerush replies Actor:** from $2.50 per 1,000 results, 20 URLs per run, 10 to 300 replies per post (default 50), nested replies off by default, logged-out subset only. It flags `is_public_subset`. Rating 1.8/5 from two reviews. Vendor claim, report G3, [Actor](https://apify.com/futurizerush/threads-replies-scraper).
- **Apify burbn search Actor:** from $5 per 1,000 results; login need not confirmed. Vendor claim, report G3.
- Report C1 named headply or scrapersdelight Actors, with about 18 to 25 posts per request and a ceiling near 50 to 70 unique posts per keyword. Price not found. Vendor claim, report C1, not rechecked.
- **ScrapeCreators:** 100 free credits, then $47 for 25,000 credits. Bills per request, not per post. Search returns 10 results per call. The post endpoint can mix in "related posts", so a parser must not treat all of them as replies. Vendor claim, report G3, not rechecked, [ScrapeCreators](https://scrapecreators.com/), [post docs](https://docs.scrapecreators.com/v1/threads/post).
- **EnsembleData:** $100 a month for 1,500 units a day; too dear for small use. Vendor claim, report G3. See [social-apis.md](../providers/social-apis.md).
- **Bright Data:** $1.50 per 1,000; no keyword search or reply text found. Vendor claim, report G3.
- **ReefAPI** lists Threads in its catalogue. Vendor claim, reports C2 and G9. See [reefapi.md](../providers/reefapi.md).
- **Fediverse:** accounts that federate can be followed from a Mastodon server. Only those accounts, no global search. Official doc plus Inference, report G3.
- No native Threads RSS was found. Inference, report G3.

## Rules and risks for this site

- **Meta bans automated collection, logged in or not.** The Threads Terms of Use "supplement and amend the Instagram Terms of Use", which say you may not access or collect information "in an automated way without our express permission, regardless of whether such automated access or collection is undertaken while logged-in to an Instagram account." Official doc, checked 6 Oct 2026 (round 2), [Instagram Terms](https://help.instagram.com/581066165581870), [Threads Terms](https://help.instagram.com/769983657850450). So a vendor's no-login Actor is still collection Meta forbids. See [shared/legal.md](../shared/legal.md).
- Court record: Meta lost against Bright Data on logged-off scraping in January 2024 (US). That shows the terms may not bind a logged-off scraper in the US; it does not make collection permitted, and the risk sits with whoever runs or buys it. Court record via report C6; Inference.
- Never attach the user's Instagram or Threads login to private or reverse-engineered clients. See [shared/rules.md](../shared/rules.md).
- Meta's storage, deletion and AI-use terms for Threads API data were not fully retrieved. Treat them as unknown, not permitted.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | Search cap is 500 queries per 7 days (socialcrawl.dev, cited in report C1). | 2,200 queries per rolling 24 hours; empty results do not count. | Official doc, [keyword search](https://developers.facebook.com/docs/threads/keyword-search), 6 October corroboration |
| 2026-10-06 | Best route is a no-login Apify Actor or ScrapeCreators (report C1, round 1 corroboration, our route table). | Those routes break Meta's terms, which ban automated collection even when logged out. No route is open to an individual. | Official doc, [Instagram Terms](https://help.instagram.com/581066165581870); round 2 corroboration W01 and W05 |
| 2026-10-06 | Vendor scraping of Threads is a "terms grey zone" (report C1). | It is an express terms breach; only enforceability is uncertain. | Same |

## Open questions

1. Does Meta give individuals any path to Business Verification, or exempt Threads keyword search from it? Not found in round 2. A yes would reopen the free official route.
2. How many useful engineering accounts on Threads federate to the fediverse? That decides whether the Mastodon side door is worth anything.
3. Answered 6 Oct 2026: an individual without a business very likely cannot get `threads_keyword_search` approved.

## Sources

- Deep research rounds 1 and 2 (5 and 6 October 2026; private, not published), reports G3, G1, G9, C1, C2, C7 and C10, plus both corroboration rounds. Our old notes had no Threads file.
- Primary pages, accessed 6 Oct 2026: [Meta keyword search](https://developers.facebook.com/docs/threads/keyword-search), [permissions](https://developers.facebook.com/docs/permissions), [Instagram Terms](https://help.instagram.com/581066165581870), [Threads Terms](https://help.instagram.com/769983657850450).
- Research bundles: see [SOURCES.md](../SOURCES.md).
