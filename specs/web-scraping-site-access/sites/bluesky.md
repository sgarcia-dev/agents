---
created_at: 2026-10-06
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: spec
status: piloted
scope: Bluesky
purpose: How agents can read Bluesky: routes per operation, costs, rules and open questions.
related:
  - path: ../spec.md
    why: Owning spec, shared model and the route table.
  - path: ../shared/rules.md
    why: Access, legal and data rules every route must pass.
  - path: ../shared/accounts.md
    why: When a separate research account is allowed, and how to run one.
  - path: ../providers/apify.md
    why: Bluesky Actors used as paid fallbacks.
  - path: ../providers/reefapi.md
    why: ReefAPI's Bluesky engine, a fallback for search.
  - path: ../providers/social-apis.md
    why: FxEmbed and ScrapeCreators facts.
  - path: ../providers/mcp-servers.md
    why: Bluesky MCP wrappers and their account needs.
---

# Bluesky

Bluesky is a free, low-noise source for engineering and AI discussion. The
official API is the best route and costs $0. Post and thread reads, author
feeds and the Jetstream live stream work without an account. Keyword
search without signing in was refused every time in the latest independent
recheck (25 September 2026), so search needs an app password on a separate,
bot-labelled account. The user approved one (P6); the user creates it.

## Status

- **Verdict:** Use the official API. Paid scrapers are a fallback only.
- **Allowed today:** a research account is approved (P6, second after X) and the user creates it. Bluesky is not in the first pilot (P9: Hacker News, then Reddit).
- **Last checked:** 6 October 2026, primary-source check of the search lexicon, issue #32, bsky-docs #332, the Jetstream v2 announcement, the bots page and the Community Guidelines (round 1 and round 2 corroboration). Observed test on 7 October 2026 (below).

## Observed test (7 October 2026)

- **Anonymous reads passed.** Thread reads at depth 1000 returned every
  direct reply within 2 percent of `replyCount` (154 of 157, 99 of 102,
  76 of 76) plus the nested replies below them (up to 10 levels).
  `replyCount` counts direct replies only. `getPosts` returned 10 of 10
  posts in one call. Replies listed as hidden by a threadgate still came
  back. W05 record (private, not published).
- **Anonymous search is refused:** HTTP 403 with an HTML page, not JSON,
  as the file says. Search needs the research account (P6).
- **Jetstream passed:** no key, a steady stream of about 2,900 posts a
  minute (30,000 in 9.5 minutes); a local keyword filter kept 219. Use
  `wantedCollections` and filter locally.

## Routes by operation

| Operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence |
|---|---|---|---|---|---|---|
| discover | `searchPosts` signed in with an app password through the account's PDS | Jetstream live with a local keyword filter. Anonymous `searchPosts` is not a fallback (refused in the latest recheck). | $0 | Separate account for search | Official doc; Independent report | Medium-high |
| retrieve | Anonymous post lookup on the public AppView | FxEmbed | $0 | No | Official doc | High |
| thread | Anonymous `getPostThread` | FxEmbed conversations | $0 | No | Official doc | Medium: depth is not completeness |
| monitor | Poll `getAuthorFeed` and saved searches with overlap and dedupe | Jetstream v2 live (no key) with a local filter | $0 plus own compute | No for feeds; yes for search | Official doc; Inference | Medium-high |

## Facts that decide the route

### Search

- The [searchPosts lexicon](https://github.com/bluesky-social/atproto/blob/main/lexicons/app/bsky/feed/searchPosts.json) says search "may require authentication (eg, not public) for some service providers". The cursor "may not necessarily allow scrolling through entire result set". `hitsTotal` may be rounded. Official doc, checked 6 Oct 2026.
- Filters: author, mentions, language, linked domain or URL, tags (all must match), top or latest, inclusive `since` and exclusive `until`. 1 to 100 results per page, default 25. Date filters use `sortAt`, which can differ from `createdAt`. Query grammar is not specified; Lucene syntax is suggested. Official doc, 5 Oct 2026, same lexicon.
- Anonymous search **nearly always fails**. Issue #32 found 403 on the first page in 24 of 25 probes on 25 Sep 2026. A mid-thread comment saw 403 then 200, but the later recheck the same day says "the 403 is no longer intermittent": every query got 403 on both `api.bsky.app` and `public.api.bsky.app`, from two unrelated networks. The maintainer shipped app-password search in v0.4.0. Independent report, checked 6 Oct 2026 (round 2), [issue #32](https://github.com/cyanheads/bluesky-mcp-server/issues/32).
- A Bluesky staff comment in 2025 called the 403 deliberate: "AppView is deliberately returning 403 to decrease load". Independent report, [bsky-docs issue 332](https://github.com/bluesky-social/bsky-docs/issues/332), checked 6 Oct 2026. No official Bluesky changelog or blog post on anonymous search was found (report C7).
- Signed-in search runs as the account: the AppView drops posts that are in a block relationship with the search account. Independent report, issue #32.
- A 5 Feb 2026 developer report saw 403 on `public.api.bsky.app` while another AppView host worked. Independent report, report G3, not rechecked, [Raymond Camden](https://www.raymondcamden.com/2026/02/05/building-a-bluesky-sentiment-dashboard-with-alpine-and-chrome-ai).
- A May 2025 statement restricts anonymous cursors. Independent report, [bsky-docs issue 296](https://github.com/bluesky-social/bsky-docs/issues/296).
- Profiles, author feeds and `searchActors` still return 200 without sign-in. Independent report, report C1, not rechecked.
- Signed-in requests go through the account's PDS (home server) or proxy. Do not attach a bearer token to the public cached AppView host. Official doc, [API directory](https://bsky.network/docs/api-directory/), 5 Oct 2026.
- `createSession` on bsky.social returned `ratelimit-policy: 10;w=86400`: about 10 logins a day. Create the session once and reuse it. Independent report, [issue #32](https://github.com/cyanheads/bluesky-mcp-server/issues/32), checked 6 Oct 2026.
- An app password can be revoked and cannot manage the account. Independent report, report C1, not rechecked.

### Posts, threads and limits

- [getPostThread](https://github.com/bluesky-social/atproto/blob/main/lexicons/app/bsky/feed/getPostThread.json) needs no sign-in. Reply depth defaults to 6 and parent height to 80; both go up to 1,000. These are depth limits, not proof of every branch. Official doc, 5 Oct 2026.
- The 3,000 requests per 5 minutes figure is a hosted PDS limit, not a public AppView search limit. AppView limits are not numbered. Official doc, [rate limits](https://bsky.network/docs/rate-limits/), 5 Oct 2026.

### Jetstream (live and replay)

- Bluesky's 13 Aug 2026 announcement: "The live tail remains open and unauthenticated, it's only when you request an archive that we require a token." It adds: "We have no plans to introduce an auth requirement for the live stream." Official doc, [Introducing Bluesky Protocol Services](https://atproto.com/blog/introducing-bluesky-protocol-services), checked 6 Oct 2026.
- Jetstream v2 is run by Bluesky PBC and offers live tail, replay and snapshots. Live needs no key. Filters are collections (up to 100) and DIDs (up to 10,000), not keywords. Delivery is at least once, so dedupe and handle deletes. Official doc, [Jetstream](https://bsky.network/docs/jetstream), 5 Oct 2026.
- Replay and snapshots need an HTTP key from `bsky.network/account`. "Usage is metered in bytes, not requests." No price or quota size is published; a used-up quota answers 429 with Retry-After. Archive events are compacted, so replay is not a complete history (independent connector note, report C7). Official doc, page dated 3 Sep 2026, checked 6 Oct 2026, [replay](https://bsky.network/docs/jetstream-replay/).
- Hitting the replay limit returns 429 "byte limit exceeded" with Retry-After; resume with an HTTP Range request. Official doc, checked 6 Oct 2026, same page.
- Thirty-six hours is the hosted live lookback, not archive retention. Official doc, 5 Oct 2026.
- The v2 live endpoint is `wss://jetstream.us-east.bsky.network/xrpc/network.bsky.jetstream.subscribeEvents`, not the legacy `/subscribe` path. This is a reference, not an instruction to connect.

### Paid and third-party options (fallbacks)

- **Apify inn_corp Bluesky Post Search:** $1 per 1,000 posts plus $0.005 per successful search, including zero-result searches. No login. It notes Bluesky "refuses anonymous search from datacenter IPs" and runs on Apify Proxy. Vendor claim, reports G1 and C2, 5 Oct 2026, not rechecked, [Actor](https://apify.com/inn_corp/bluesky-post-search).
- **Apify s0rgcl:** $1 per 1,000 records plus a start fee and platform usage. **Lexis Solutions:** $0.92 per 1,000 posts plus $0.004 per run. **fatihtahta all-in-one:** $1.49 per 1,000 results. Vendor claim, reports G1 and G3, 5 Oct 2026, not rechecked. See [apify.md](../providers/apify.md).
- Avoid the ethanteague Actor: it searches "under your own account credentials". Vendor claim, report C2.
- **Bright Data:** $1.50 per 1,000, 5,000 free a month advertised. Vendor claim, report G3, not rechecked.
- **ReefAPI** has a Bluesky engine. Vendor claim, reports C1 and C2. See [reefapi.md](../providers/reefapi.md).
- **FxEmbed** documents Bluesky search, posts, conversations and account RSS. No production promise. Project doc, report G3, not rechecked, [FxEmbed](https://docs.fxembed.com/api/introduction/).
- Tools that claim anonymous search may be "quietly routing your queries through someone else's account". Independent report, report C1, not rechecked.
- Native Bluesky RSS for accounts was reported in January 2024; current behavior is not tested. Independent report, [OpenRSS](https://openrss.org/blog/bluesky-has-launched-rss-feeds).

## Rules and risks for this site

- Use a separate account, never the user's personal one, if search sign-in is approved. Do not pass an app password as a query credential to a public host. See [shared/rules.md](../shared/rules.md) and [shared/accounts.md](../shared/accounts.md).
- A second account is allowed by the rules as long as it is not used to evade enforcement. The Community Guidelines say: "Do not create new accounts or use alternative methods to evade bans, suspensions, or other enforcement actions". No rule against a second account was found. Official doc, [Community Guidelines](https://bsky.social/about/support/community-guidelines), via report C10.
- Bots should self-label: "As a best practice, bot accounts should identify themselves by adding a self-label to their profile." Login limits are far lower than write limits, so save and reuse the session. Official doc, [bots](https://docs.bsky.app/docs/starter-templates/bots), checked 6 Oct 2026.
- AI reuse: Bluesky said in November 2024 that it cannot enforce its no-training stance outside its own systems. The "User Intents for Data Reuse" proposal (0008) has not shipped. A private summary is far from the 2024 case where a 1 million post dataset was pulled after backlash. Do not publish datasets. Independent report and Official doc (proposal), report C7.
- [Developer guidelines](https://bsky.network/docs/developer-guidelines/) require deletion handling. [Terms](https://bsky.social/about/support/tos) keep content ownership with users; they are not a reuse license. Official doc, 5 Oct 2026.
- The 1 Sep 2026 [content visibility declaration](https://bsky.network/blog/content-visibility-declaration) is about broad algorithmic recommendation, not a training license. Official doc, report G3.
- Stop cleanly at a 403. Do not use bypass tricks.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | Round 1 correction: anonymous search fails "often but not always" (we had marked report C1's "effectively always fails" as overstated). | **Reversed.** C1 was close to right. The latest recheck in the same issue found every query refused from two networks. Treat anonymous search as unavailable. | Independent report, [issue #32](https://github.com/cyanheads/bluesky-mcp-server/issues/32); round 2 corroboration W01 |
| 2026-10-06 | "Anonymous search reliability is unresolved" (old notes). | Treat anonymous search as unreliable and plan for signed-in search; anonymous post and thread reads still work. | 6 October corroboration |
| 2026-10-05 | Jetstream is stream-only with no history (earlier Claude and Gemini reports). | v2 has replay and snapshots, key-gated and byte-metered. | Official doc, [replay](https://bsky.network/docs/jetstream-replay/) |
| 2026-10-05 | 3,000 requests per 5 minutes applies to search. | That is a PDS limit; AppView limits are not numbered. | Official doc, [rate limits](https://bsky.network/docs/rate-limits/) |
| 2026-10-05 | Gemini's RSS "verified live" claim. | Not verified; no payload was kept. | Earlier follow-up reconciliation (private, not published) |

## Open questions

1. Does Jetstream replay have a published byte price or free quota? Still not found after round 2. Matters only for a backfill; the free live tail covers monitoring.
2. Does native RSS still work, and how many items does it return? A pilot would answer.
3. Do any independent AT Protocol AppViews offer anonymous post search? Not found in round 2.
4. Answered 6 Oct 2026: no official statement on anonymous search exists; a collector must hold an app password for search.

## Sources

- Old notes migrated: [~/agents/capabilities/web/social/bluesky.md](../../../capabilities/web/social/bluesky.md); earlier bundles social search discovery (private, not published) and follow-up (private, not published).
- Deep research rounds 1 and 2 (5 and 6 October 2026; private, not published), reports G3, G1, G9, C1, C2, C7 and C10, plus both corroboration rounds.
- Primary pages, accessed 5 and 6 Oct 2026: [searchPosts](https://github.com/bluesky-social/atproto/blob/main/lexicons/app/bsky/feed/searchPosts.json), [getPostThread](https://github.com/bluesky-social/atproto/blob/main/lexicons/app/bsky/feed/getPostThread.json), [Bluesky API guide](https://bsky.network/docs/bluesky-api/), [Jetstream replay](https://bsky.network/docs/jetstream-replay/).
- Research bundles: see [SOURCES.md](../SOURCES.md).
