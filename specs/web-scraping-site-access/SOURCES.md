---
created_at: 2026-10-06
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: sources
purpose: Evidence ledger for web scraping site access: research bundles, how much to trust each kind of source, and claims we found to be wrong.
related:
  - path: ./spec.md
    why: Owning spec.
  - path: ./STATE.md
    why: Current status.
  - path: ./DECISIONS.md
    why: Choices that rest on this evidence.
---

# Web scraping site access: sources

Site and provider files cite their own primary URLs. This file holds the
bundles, the trust order and the list of claims to avoid.

## Source hierarchy

When sources disagree, trust them in this order:

1. Official doc, statute or court record, read directly and dated.
2. Observed test: our own dated run with a saved record. (None yet.)
3. Independent report: news, reviews, public issue trackers.
4. Vendor claim: a provider's own page about itself or a rival.
5. A research report's inference.

A deep research report is a map of where to look, not evidence by itself.
Promote a decision-driving claim only after checking its primary source.

## Bundles

In date order. Shared bundles are linked; private ones are named only.

- **September 2026, web search and fetch landscape:**
  report (private, not published).
  Early service list (SerpAPI, Bright Data, Apify and others). Prices
  there are superseded by the provider files.
- **5 October 2026, social search discovery** (24 reports, six packets):
  RESEARCH.md (private, not published).
- **5 October 2026, social search follow-up** (20 reports; LinkedIn,
  Reddit, X, HN, Bluesky), with the pilot proposal and reconciliation:
  RESEARCH.md (private, not published),
  PILOT_PROPOSAL.md (private, not published),
  PHASE2_RECONCILIATION.md (private, not published).
- **5 October 2026, handoff on social research and scraper options:**
  handoff (private, not published).
  Its open items are folded into the site and provider files.
- **5 October 2026, deep research round 1** (13 reports: 9 ChatGPT, G1 to
  G9; 4 Claude Research, C1 to C4). Private, not published. Topics: G1 Apify, G2
  multi-site providers, G3 X/Bluesky/Threads/Mastodon, G4 Reddit/HN/forums,
  G5 LinkedIn without login, G6 LinkedIn/Indeed/Glassdoor jobs, G7 Irish
  boards and job-data APIs, G8 build/buy/side doors, G9 MCP tools, C1 best
  route per platform, C2 four providers compared, C3 legal and account
  risk in Ireland, C4 jobs without the big boards.
- **6 October 2026, corroboration** (6 reader reports, one per platform
  group, about 60 primary-source checks). Same private bundle. Its
  accepted results are in the site and provider files' facts and
  Corrections logs.
- **6 October 2026, deep research round 2** (6 Claude Research reports):
  C5 providers that accept individuals, C6 Reddit after the API closes,
  C7 sanctioned routes for X, Bluesky, Threads and Mastodon, C8 job alert
  emails and aggregators, C9 the Irish employer job-system map, C10 legal
  and account lines. Same private bundle, filed byte for byte.
- **6 October 2026, round 2 corroboration** (5 reader reports, about 130
  claim checks against primary sources). Same private bundle. It reversed
  two of our own round 1 corrections (Bluesky, Mastodon) and withdrew our
  household-exemption line. Its accepted results are in the site,
  provider and shared files.
- **6 October 2026, round 3: what real users say** (10 ChatGPT reports,
  G10 to G19, standard Chat at Extra high; G11, G17 and G18 are reruns in
  a recovery project after the first chats stalled). Same private bundle,
  filed byte for byte. Topics: G10 provider reputation compared, G11
  Apify as a platform, G12 the Apify Actors we would use, G13 whether
  ReefAPI is legitimate, G14 ScrapeCreators and SociaVault, G15 Bright
  Data for a small user, G16 X routes, G17 LinkedIn data without login,
  G18 Reddit after the API closes, G19 tools missing from our list. Each
  report was summarized against this spec by one reader, and about 60
  decision-driving claims were checked against primary pages in six
  check reports. Accepted results are in the site and provider files
  under "What users say (round 3)". Caveats: X posts could not be read
  in any report, so X opinion rests on Trustpilot and GitHub; G14 has no
  real URLs (only ChatGPT citation markers); review sites are partly
  paid or invited (Apify, Bright Data, ScrapeCreators).

- **7 October 2026, first pilot** (8 OpenCode probe records, W01 to
  W08, plus 11 capped Apify runs, A01): Observed tests for Hacker News,
  Reddit via Arctic Shift, employer job feeds, Bluesky, Mastodon,
  Lobsters, DEV, X syndication and Apify Actors. Every record was
  recounted from raw files by the root agent:
  RESEARCH.md (private, not published). Raw responses were kept outside Git.

## Related specs and docs

- [capabilities/web](../../capabilities/web/README.md):
  general search and page readers (Parallel, Exa, Firecrawl, harness
  search), ladders, compatibility verdicts.
- [specs/internet-deep-research](../internet-deep-research/spec.md):
  research tools and the standalone research app.
- [specs/browser-use](../browser-use/spec.md):
  browser routes and safety.
- [skills/browser-deep-research-prompts](../../skills/browser-deep-research-prompts/SKILL.md):
  how the deep research rounds are written and exported.

## Weak claims to avoid

Each was in a research report, an older note or our own round 1 work,
and failed a 6 October check. The site, provider or shared file holds the
detail. When our own correction turns out wrong, it is listed here too.

| Claim | What is true | File |
|---|---|---|
| Use SerpApi Google Jobs for Ireland (C1, $25 a month). | Google Jobs and SerpApi both leave Ireland out. | [google-jobs.md](sites/google-jobs.md) |
| Our round 1 correction: anonymous Bluesky search fails only "intermittently". | The latest recheck found it refused every time, from two networks. C1's "effectively always fails" was close to right. | [bluesky.md](sites/bluesky.md) |
| Our round 1 correction: Mastodon v2 search is public, so no token is needed. | The endpoint answers, but anonymous calls return no posts. Post search needs a token and covers only opted-in posts. C1 and G3 were right. | [mastodon.md](sites/mastodon.md) |
| Threads keyword search allows 500 queries a week. | 2,200 per rolling 24 hours (Meta docs). | [threads.md](sites/threads.md) |
| X's read cap might be 2 million a month. | 3 million per billing cycle (X docs, 2 Oct 2026). | [x.md](sites/x.md) |
| Reddit at about $0.40 for 5,000 reads (C1). | About $10 at RedditAPIs.com's own rate and minimum top-up. | [reddit.md](sites/reddit.md) |
| Reddit data access will become "paid only" (news). | Reddit's own post does not say so. | [reddit.md](sites/reddit.md) |
| Never put LinkedIn data into an LLM (C3). | LinkedIn's Developer AI Policy covers only data from its Marketing APIs. Our own rule still excludes LinkedIn reads. | [linkedin.md](sites/linkedin.md) |
| Bright Data first, for one account across platforms (G2, G6, G9). | Bright Data's docs say personal projects "are not approved". | [bright-data.md](providers/bright-data.md) |
| Apify as the paid access layer, no caveat (G1). | Apify's terms say "business use only". | [apify.md](providers/apify.md) |
| ReefAPI takes card or crypto; has a $100 Mega plan; 4 MCP stars, 76 users, over 99 percent success (C2). | Its own pages disagree on payment and on the Mega plan, so neither is settled; 1 star; 84 users; 97 percent. | [reefapi.md](providers/reefapi.md) |
| Apify Starter costs $29 or $39 (older reviews). | $19 a month ($17 on annual billing). | [apify.md](providers/apify.md) |
| Jobs.ie actor costs $0.79 per 1,000 (C1). | $0.99 on the free plan; $0.79 is the Gold plan; plus a start fee. | [stepstone-ireland.md](sites/stepstone-ireland.md) |
| All four Reddit v SerpApi defendants lost their motions on 31 July 2026 (C3). | SerpApi's and Perplexity's motions were largely denied; Oxylabs' was separate. | [shared/rules.md](shared/rules.md) |
| Proxycurl was ordered by injunction to delete data (G5, C3). | A settlement and shutdown are confirmed; the injunction terms rest on secondary sources. | [linkedin.md](sites/linkedin.md) |
| Indeed's Publisher API timeline (closed 2020, deprecated 2023, dark 2024) as fact. | A vendor blog's account; no Indeed source. The conclusion (no route) stands. | [indeed.md](sites/indeed.md) |
| Our round 1 rule: a private research tool "very probably" falls under the GDPR household exemption. | The Court of Justice reads it narrowly; collecting strangers' posts is probably outside it. Plan as if GDPR applies. | [shared/legal.md](shared/legal.md) |
| Our round 1 rule: Irish courts held website terms binding on a screen-scraper (Ryanair v Billigfluege). | Jurisdiction only; no court ruled on whether scraping broke the terms. | [shared/legal.md](shared/legal.md) |
| Threads vendor scraping is a terms "grey zone" (C1); best Threads route is a no-login actor (round 1). | Meta's terms ban automated collection even logged out; official search needs Business Verification. No route is open to an individual. | [threads.md](sites/threads.md) |
| Buying LinkedIn data from a no-login vendor carries no direct exposure (round 1 framing). | LinkedIn's s.8.2 reaches data obtained "through third parties" for anyone with an account. | [linkedin.md](sites/linkedin.md) |
| The best live Reddit route is a third-party Reddit API (round 1). | Arctic Shift is free and current; vendors are the fallback. RedditAPIs.com scrapes through residential proxies. | [reddit.md](sites/reddit.md) |
| SocialData costs $0.40 per 1,000 tweets (G3). | $0.20 per 1,000. | [x.md](sites/x.md) |
| X's usage page still says a 2 million cap (C7). | Both the pricing and usage pages say 3 million. | [x.md](sites/x.md) |
| Oracle's "only for Oracle internal use" note covers only a related resource (C9). | It covers the whole job requisitions category, including the search finder. | [ats-feeds.md](sites/ats-feeds.md) |
| BambooHR has no public job feed (C4). | Its careers widget endpoint is public and keyless, though undocumented. | [ats-feeds.md](sites/ats-feeds.md) |
| The IrishJobs actor bills residential proxy on top (round 1, from its README). | Its README now says proxy and compute are included. | [stepstone-ireland.md](sites/stepstone-ireland.md) |
| LinkedIn's ProAPIs judgment was dated 21 or 23 September 2026 (secondary sources). | Signed 16 September 2026 (court docket). | [linkedin.md](sites/linkedin.md) |
| ScrapeCreators has a $10 "Solo Dev" pack (a review cited in C5). | No such pack; Free, $47, $497 and Enterprise. | [social-apis.md](providers/social-apis.md) |
| TwitterAPI.io has 32 Trustpilot reviews at 4.6 (G16). | 21 reviews at 4.5, mostly one-review accounts. | [social-apis.md](providers/social-apis.md) |
| No verified phone is needed for the X API (G16, from the getting-access page). | The Developer Agreement requires one. | [x.md](sites/x.md) |
| X v Bright Data settled on 23 June 2025; our line said "reported paused". | 30 customer subpoenas allowed 13 June 2025; joint dismissal filed 27 June; closed 1 July 2025. | [bright-data.md](providers/bright-data.md) |
| Bright Data caches LinkedIn profile fields "since November 2025" (G2). | Caching confirmed; the date is not on any page found. | [linkedin.md](sites/linkedin.md) |
| ScrapeCreators has no X keyword search (G2, our file). | `/v1/twitter/search/posts` exists, through Google's index. | [social-apis.md](providers/social-apis.md) |
| ScrapeCreators credits never expire (its homepage). | Its terms let it expire or forfeit credits. | [social-apis.md](providers/social-apis.md) |
| The Apify Bluesky Actor no longer charges for zero-result searches (G12). | Successful zero-match searches are still charged. | [apify.md](providers/apify.md) |
| HarvestAPI profile search costs $50 per 1,000 profiles (G17). | $50 per 1,000 search-page results; full profiles $8 per 1,000. | [apify.md](providers/apify.md) |
| The ProAPIs judgment could reach our own recommendations (G17). | It binds the defendants only. | [linkedin.md](sites/linkedin.md) |
| Reddit praise for ReefAPI is user evidence. | It traces to an account that says it runs ReefAPI (G13). | [reefapi.md](providers/reefapi.md) |
| Any route "works" because a report or vendor says so. | No route here has an Observed test yet. | [STATE.md](STATE.md) |

- **"parsebird's Actors are the Irish boards route"** (rounds 1 and 2):
  they have 1 monthly user on the Apify Store; Black Falcon leads and was
  tested instead (7 Oct 2026, A01).
- **"Bluesky thread counts do not match replyCount"** (worker W05's first
  reading): `replyCount` counts direct replies only; direct replies
  matched within 2 percent (7 Oct 2026, checker's note in W05).
- **"Algolia's HN tree lags its index"** (worker W01): not proven; the gap
  may be flagged comments the tree leaves out (checker's note in W01).

## Historical and stale

- `capabilities/web/social/*.md` (5 October 2026): migrated into this spec
  on 6 October 2026; the files are now pointers. Git history keeps the
  originals.
