---
created_at: 2026-10-06
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: spec
status: piloted
scope: Mastodon
purpose: How agents can read Mastodon: routes per operation, costs, rules and open questions.
related:
  - path: ../spec.md
    why: Owning spec, shared model and the route table.
  - path: ../shared/rules.md
    why: Access, legal and data rules every route must pass.
  - path: ../shared/accounts.md
    why: When a separate research account is allowed, and how to run one.
  - path: ../providers/apify.md
    why: Mastodon Actors exist but add nothing over the free API.
  - path: ../providers/mcp-servers.md
    why: Mastodon MCP wrapper and its token needs.
---

# Mastodon

Mastodon is a network of separate servers, each with its own free API.
The best route is polling public hashtag timelines on 3 to 5 large servers,
for $0 and with no account. Keyword search for posts needs a user token,
and even then it only finds posts whose authors opted in (about 8 to 10
percent of active accounts). There is no network-wide search: every search
or thread only shows what one server knows. Mastodon communities have
pushed back hard on researchers before, so polite-reader rules apply.

## Status

- **Verdict:** Use the official per-server API, hashtag timelines first. No paid provider is needed.
- **Allowed today:** hashtag and account timelines need no account. A Mastodon research account is low priority (P6: "diminishing returns"). Not in the first pilot.
- **Last checked:** 6 October 2026, primary-source check of the search, timelines, streaming and rate-limit docs, issue #1848 and the 4.2.0 release notes (round 1 and round 2 corroboration). Observed test on 7 October 2026 (below).

## Observed test (7 October 2026)

- **Hashtag timelines passed on 3 of 5 servers** (mastodon.social,
  hachyderm.io, fosstodon.org). infosec.exchange and mstdn.social answer
  HTTP 422 "This method requires an authenticated user". #hiring and
  #getfedihired gave 240 rows, 115 unique posts by `uri`, from about 39
  origin servers; 40 posts cover 2 to 3 days. W06_mastodon record (private, not published).
- **Anonymous search returns no posts** (HTTP 200, empty), as the docs say.
- **Threads:** status context on the origin server returned 26 replies
  where `replies_count` said 15, and 14 against 13. Use context for counts.
- Per-tag RSS works (20 items, remote posts included). Paging was not
  properly tested.

## Routes by operation

| Operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence |
|---|---|---|---|---|---|---|
| discover | Hashtag timelines polled on 3 to 5 large servers, deduped by URI | v2 search with a user token and `read:search` (opted-in posts only). Anonymous v2 search returns accounts and hashtags, never posts. | $0 | No for hashtags; yes for keyword search | Official doc | High |
| retrieve | Status lookup on the post's origin server | Search with `resolve` (needs a token) | $0 | No | Official doc | High |
| thread | Status context on the origin server | Same call with a `read:statuses` token for bigger trees | $0 | No; token raises limits | Official doc | Medium |
| monitor | Poll hashtag and account timelines, or per-tag RSS | Streaming (needs a user token since 4.2) | $0 | No for polling | Official doc | High |

## Facts that decide the route

### Search

- v2 search: "OAuth: Public (without resolve or offset), or User token + read:search". Changelog: "4.0.0 - no longer requires a user token." Up to 40 results per type. Official doc, checked 6 Oct 2026, [search](https://docs.joinmastodon.org/methods/search/).
- The same page (last updated 1 June 2026) says statuses need a search backend and a signed-in request: "full text search is not available to unauthenticated users". Official doc, checked 6 Oct 2026 (round 2).
- A Mastodon maintainer confirmed it on the project tracker: "This is expected, full text search is not available for unlogged users, only hashtag-based search". Official maintainer comment, [documentation issue #1848](https://github.com/mastodon/documentation/issues/1848), checked 6 Oct 2026.
- Since 4.2.0, full-text search covers only opted-in posts: "Add full-text search of opted-in public posts", in a new `public_statuses` index. Official doc, [v4.2.0 release](https://github.com/mastodon/mastodon/releases/tag/v4.2.0), checked 6 Oct 2026.
- Coverage is small: Mastodon's CTO said "between 8% and 10% of active accounts have opted into Mastodon's search". Independent report (Fediverse Report, "Last Week in Fediverse, ep 84"), cited in report C7, not rechecked.
- What this means: hashtag timelines are the better trend signal, with or without a token. Inference.

### Timelines, threads, limits

- Hashtag and public timelines: "Public. Requires app token + read:statuses if the instance has disabled public preview". Up to 40 posts per call. Official doc, page dated 19 Aug 2026, checked 6 Oct 2026, [timelines](https://docs.joinmastodon.org/methods/timelines/).
- mastodon.social requires sign-in for its public (global) timeline. Vendor claim (Apify Actor notes), report C1, not rechecked.
- Streaming: "4.2.0 - changed to require a User token, removing Public and App token access". This covers public and hashtag streams. Official doc, checked 6 Oct 2026, [streaming](https://docs.joinmastodon.org/methods/streaming/); the 4.2.0 release notes say "Remove anonymous access to the streaming API".
- Status context: anonymous gives 40 ancestors, 60 descendants, depth 20. With a token: up to 4,096 each way, unlimited depth. Still limited to what the server knows. Version 4.5 fetches missing replies in the background, so a second call can return more. Official doc, report G3, not rechecked, [statuses](https://docs.joinmastodon.org/methods/statuses/).
- Rate limit baseline: "All endpoints and methods can be called 300 times within 5 minutes", per account and per IP; servers can override. The page was last updated November 2022, so read the `X-RateLimit-*` response headers. Official doc, checked 6 Oct 2026, [rate limits](https://docs.joinmastodon.org/api/rate-limits/).
- Account and tag RSS exist (`/tags/{tag}.rss`); availability follows server settings. Official doc, report G3, [network features](https://docs.joinmastodon.org/user/network/). Not tested.
- Tokens come from registering an app on the chosen server. No central review; each server governs sign-ups. Official doc, report G3, [tokens](https://docs.joinmastodon.org/client/token/).
- Paid options add nothing: Apify Actors from $0.44 to $5 per 1,000 records wrap the same public endpoints. Vendor claim, reports G1 and G3. See [apify.md](../providers/apify.md).
- Mastodon.py (stable 2.2.2) is a maintained client, not an index. VitexSoftware's MCP server (v1.0.5, 11 Sep 2026) needs an instance token and defaults to read-only. Project doc, reports G3 and G9, not rechecked. See [mcp-servers.md](../providers/mcp-servers.md).

### Community norms (why polite matters here)

- A university dataset of scraped Mastodon posts was removed from Harvard Dataverse in 2020 after an open letter; the stated reason was that entries "allow identification of personal information". Independent report, cited in report C7 ([open letter](https://www.sunclipse.org/wp-content/downloads/2020/01/open-letter.html)), not rechecked.
- A 2025 study found that in 2023, "31 out of the 4,371 identified instances explicitly stated in their guidelines that they do not consent to being indexed or researched". Independent report, [arXiv 2505.07606](https://arxiv.org/html/2505.07606), cited in report C7, not rechecked.
- Some users tag their profiles `#nobot`, `#nosearch` or `#noindex`. Independent report (German National Library workshop deck, cited in C7).

## Rules and risks for this site

- No single platform contract. Read each chosen server's `/about` rules before polling it, and skip servers that forbid research or indexing. The software license is not a license to users' posts. Inference, reports G3 and C7. See [shared/rules.md](../shared/rules.md).
- **Polite reader rules** (proposed, from report C7; Inference):
  - Read public posts only. Never store followers-only or direct posts.
  - Skip accounts whose name or bio has `#nobot`, `#nosearch` or `#noindex`, or whose account entity says `"discoverable": false` or `"noindex": true`.
  - For anything keyword-based, use only posts with `"indexable": true`.
  - Send a clear User-Agent with a contact URL. Poll each tag a few times a day at most.
  - Keep summaries, not copies. Never publish a dataset.
  - If a token account is approved, set the bot flag and say what it does in the bio. See [shared/accounts.md](../shared/accounts.md).
- Streaming sends delete and update events; a polling collector must recheck instead. Official doc, report G3.
- Servers can switch off public preview or block a client at any time.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | Round 1 correction: "v2 search is public since 4.0, so the token claim in C1 and G3 is wrong". | **Reversed.** C1 and G3 were right in practice. The endpoint answers without a token, but anonymous calls return accounts and hashtags only. Post search needs a user token. | Official doc, [search](https://docs.joinmastodon.org/methods/search/) (updated 1 June 2026); maintainer comment, [issue #1848](https://github.com/mastodon/documentation/issues/1848); round 2 corroboration W01 |

## Open questions

1. Which 3 to 5 servers give the best engineering and AI coverage with public preview on, and do their rules allow research reading? A pilot and a read of each `/about` page would answer.
2. What do hachyderm.io, fosstodon.org and infosec.exchange say about bots and research? Not found in round 2.
3. Answered 6 Oct 2026: anonymous v2 search returns no posts.

## Sources

- Deep research rounds 1 and 2 (5 and 6 October 2026; private, not published), reports G3, G1, G9, C1, C2 and C7, plus both corroboration rounds. Our old notes had no Mastodon file.
- Primary pages, accessed 6 Oct 2026: [search](https://docs.joinmastodon.org/methods/search/), [timelines](https://docs.joinmastodon.org/methods/timelines/), [streaming](https://docs.joinmastodon.org/methods/streaming/), [rate limits](https://docs.joinmastodon.org/api/rate-limits/), [v4.2.0 release](https://github.com/mastodon/mastodon/releases/tag/v4.2.0), [issue #1848](https://github.com/mastodon/documentation/issues/1848).
- Research bundles: see [SOURCES.md](../SOURCES.md).
