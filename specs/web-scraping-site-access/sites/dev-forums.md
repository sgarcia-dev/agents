---
created_at: 2026-10-06
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: spec
status: piloted
scope: Developer forums (Lobsters, Stack Exchange, GitHub Discussions, DEV/Forem, Discourse, Hugging Face)
purpose: How agents can read developer forums: routes per operation, costs, rules and open questions.
related:
  - path: ../spec.md
    why: Owning spec, shared model and the route table.
  - path: ../shared/rules.md
    why: Access, legal and data rules every route must pass.
  - path: ../providers/apify.md
    why: Apify plan prices, mentioned only because a Lobsters Actor exists.
---

# Developer forums

These forums carry deep technical talk: Lobsters, Stack Exchange, GitHub
Discussions, DEV/Forem, Discourse forums (such as PyTorch and Hugging Face
Forums) and Hugging Face Hub discussions. Each has its own free API or
feed, so no paid provider is needed. The caveat that matters most is
permission to store, not price: DEV's terms may block a kept copy.

Most rows rest on deep research round 1, report G4. The 6 October
corroboration did not reopen these sources, so most facts are "not
rechecked".

## Status

- **Verdict:** Use each forum's own API or feed. Start with GitHub Discussions, Stack Exchange and DEV after Hacker News.
- **Allowed today:** needs pilot permission, per [DECISIONS.md](../DECISIONS.md). No token, key or collector exists.
- **Last checked:** 5 October 2026, research reports and earlier source reads. 6 October corroboration took the G4 rows as given.

## Observed test (7 October 2026)

- **Lobsters and DEV passed.** Lobsters tag RSS, `hottest.json` and story
  JSON worked; trees were complete (14 of 14, 19 of 19, and 19 against 18
  where one deleted comment ships in the JSON but not in `comment_count`).
  DEV tag lists worked; its comments endpoint returns the whole nested
  tree in one call (22 of 22, 15 of 15, 28 of 29); article detail carries
  the full body. 15 requests, all HTTP 200, $0. W07_dev-forums record (private, not published).
- Stack Exchange and GitHub Discussions were not tested (they need keys).

## Routes by operation

Operations: **discover** (keyword or topic search), **retrieve** (one known
item by URL or ID), **thread** (a known item with all replies), **monitor**
(follow accounts, tags, communities or saved searches over time).

| Forum and operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence |
|---|---|---|---|---|---|---|
| Lobsters: discover, monitor | Tag RSS | Public HTML search | $0 | None | Official doc plus Inference | Medium |
| Lobsters: retrieve, thread | Story JSON, low rate | Ask maintainers for an export | $0 | None | Official doc (source code) | Medium |
| Stack Exchange: all | Official API with an app key | Data dumps (history) | $0 within quota | App key, no user login | Official doc (G4) | Medium |
| GitHub Discussions: all | GraphQL with a separate machine account | Webhooks, only on repos you control | $0 | GitHub machine account and token | Official doc (G4) | Medium |
| DEV/Forem: retrieve, thread, monitor | Public Forem API | Tag RSS | $0 | None for public reads | Official doc plus Inference | Low to medium |
| Discourse: all | Per-forum JSON | Category or latest RSS | $0 where allowed | Usually none | Inference (G4) | Low |
| Hugging Face Hub: retrieve, thread, monitor | Hub API with `token=False` | None | $0 | None | Inference (G4) | Low |

## Facts that decide the route

### Lobsters

- Reading and search need no invite. Tag feeds exist, single or combined. The About page offers research query help; no public full dump was found. Official doc (G4), not rechecked. [Lobsters About](https://lobste.rs/about)
- Story JSON includes comments with `short_id`, `parent_comment` and edit and deletion flags. Build the tree from `parent_comment`, not indentation. Official doc (source code, G4), not rechecked. [stories_controller.rb](https://raw.githubusercontent.com/lobsters/lobsters/master/app/controllers/stories_controller.rb)
- Source code rate limits: 4 a second, 30 a minute, 100 per 10 minutes and 400 an hour per IP, plus bot handling. The deployed edge may differ. Official doc (source code, G4), not rechecked. [rack_attack.rb](https://raw.githubusercontent.com/lobsters/lobsters/master/config/initializers/rack_attack.rb)
- Earlier workers disagreed on whether JSON exists. G4 reads it from source code. No documented JSON contract was found. Inference.
- One claim said `noai` metadata forbids all scraping and RSS is the only allowed route. Not established; do not repeat it. An open endpoint is not permission either.
- A hosted [Lobsters Actor](https://apify.com/parseforge/lobsters-scraper) exists with no verified price or thread guarantee. Prefer the feed. Vendor claim, 5 Oct 2026.

### Stack Exchange

- Default keyed quota is 10,000 requests a day. Above 30 requests a second per IP counts as abuse. Obey `backoff`. Do not repeat the same request more than once a minute. Official doc, 5 Oct 2026. [Throttle docs](https://api.stackexchange.com/docs/throttle)
- Ban responses have undefined HTTP and text behavior, not a guaranteed 429. Without user auth, apps share an IP quota by key. A worker's "300 a day anonymous" claim was not corroborated. Official doc, 5 Oct 2026.
- `/search/advanced` searches questions by site, tag, title, body and date. It is not a comment search. Official doc. [Advanced search](https://api.stackexchange.com/docs/advanced-search)
- For a full discussion, fetch all answers, then comments on the question and on every answer. Pages hold up to 100 results; loop until `has_more` is false. Official doc (G4), not rechecked. [API docs](https://api.stackexchange.com/docs)
- Data dumps: latest visible release June 2026. In April and May 2026 staff confirmed delays and download failures. History only, not live. Independent report (G4), not rechecked. [Q1 2026 dumps thread](https://meta.stackexchange.com/questions/418152/could-we-have-an-eta-on-the-q1-2026-data-dumps)
- Content is CC BY-SA. Keep attribution and `content_license`. API terms on caching and AI use could not be read. Official doc plus Inference (G4).

### GitHub Discussions

- GraphQL covers repository discussions, categories, bodies, comments, replies and search. Comments and each comment's replies need their own cursors. Official doc. [Discussions GraphQL guide](https://docs.github.com/en/graphql/guides/using-the-graphql-api-for-discussions)
- About 5,000 points an hour per user token (a point is not a post). 1 to 100 nodes a page, 500,000 nodes per query, 100 concurrent requests and 2,000 points a minute as secondary limits. Official doc (G4), not rechecked. [GraphQL limits](https://docs.github.com/en/graphql/overview/rate-limits-and-query-limits-for-the-graphql-api)
- GitHub allows one extra free machine account; the human owner stays responsible. This route needs an account, so it does not meet a "no account at all" rule. Official doc (G4), not rechecked. [GitHub Terms](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service)
- No native Discussions RSS was found. Release and commit feeds do not cover Discussions. Start with repositories actually used. Inference.

### DEV / Forem

- `/api/comments?a_id=ARTICLE_ID` with no `page` returns the full tree. `per_page` max is 1,000, per instance. Official doc (G4), not rechecked. [Forem API v1](https://developers.forem.com/api/v1)
- No full-text search API was found. Articles filter by tag and user. Official doc (G4).
- Source code limits: 3 a second and 30 a minute per IP or key. dev.to may differ. Official doc (source code, G4), not rechecked. [rack_attack.rb](https://raw.githubusercontent.com/forem/forem/main/config/initializers/rack_attack.rb)
- The API landing page warns of the V0 move and an Accept header that varies by endpoint. Official doc, 5 Oct 2026. [Forem API](https://developers.forem.com/api)
- DEV's terms give temporary personal, non-commercial viewing rights, ban mirroring and require deleting downloads when the licence ends. A permanent copied database is a permission question. Official doc (G4), not rechecked. [DEV terms](https://dev.to/terms)

### Discourse forums

- Priority forums: [PyTorch Forums](https://discuss.pytorch.org/) and [Hugging Face Forums](https://discuss.huggingface.co/). Both were reachable on 5 Oct 2026. Inference (G4).
- Full topic: fetch `/t/{id}.json`, compare posts with `post_stream.stream`, then fetch missing IDs. Mega-topics return `isMegaTopic` and `lastId` instead, so they need a separate path. Official doc (source code, G4), not rechecked. [topics.rb](https://raw.githubusercontent.com/discourse/discourse_api/main/lib/discourse_api/api/topics.rb), [post_stream_serializer_mixin.rb](https://raw.githubusercontent.com/discourse/discourse/main/app/serializers/post_stream_serializer_mixin.rb)
- Limits, storage and AI rules are set by each forum operator, not by Discourse. Inference.

### Hugging Face Hub discussions

- `get_repo_discussions` and `get_discussion_details` cover models, datasets and Spaces. Use `token=False` to avoid a saved personal token. Official doc (G4), not rechecked. [HfApi reference](https://huggingface.co/docs/huggingface_hub/v2.1.1/en/package_reference/hf_api)
- Rate table dated September 2025: 500 requests per five minutes per IP anonymous, 1,000 for a free user. Read the `RateLimit` headers instead. Official doc (G4), not rechecked. [HF rate limits](https://huggingface.co/docs/hub/rate-limits)
- No site-wide discussion search was found. Discover repos first. Details return an event stream; filter by type. Official doc plus Inference (G4).

## Rules and risks for this site

- General rules: [shared/rules.md](../shared/rules.md). No personal cookies or tokens; use a separate account only where one is required.
- A software licence (Lobsters, Discourse, HN) is not a content licence. Inference.
- Hugging Face says creators keep ownership; a model's licence does not cover its discussion comments. Official doc (G4), not rechecked. [HF terms](https://huggingface.co/terms-of-service)
- Mark minimized, deleted and unavailable comments as states. Never call a part-fetched thread complete. Inference.
- Jobs on these forums are leads only. Check with the employer.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-05 | Stack Exchange anonymous limit is 300 requests a day | Not on the official throttle page. Unresolved. | [Throttle docs](https://api.stackexchange.com/docs/throttle) |
| 2026-10-05 | Lobsters `noai` tag bans all scraping; RSS is the only route | Not established. | [Lobsters About](https://lobste.rs/about) |
| 2026-10-05 | Apify Starter is $29 or $49 | Starter was $19 on 5 Oct 2026; see the provider file. | [apify.md](../providers/apify.md) |

## Open questions

1. What do the DEV/Forem terms say about keeping a private copy for personal use? This is the one forum where terms may block storage. Ask DEV or read the terms in full.
2. Do selected Discourse operators and Lobsters allow a kept cache and AI summaries? Check each operator's policy, or ask Lobsters maintainers.
3. Which Stack Exchange API terms apply to caching and AI use? The legal pages could not be read on 5 October.

## Out of scope here

Mastodon has its own file:
[mastodon.md](mastodon.md).

## Discord (discovery only)

Migrated from the 5 October forums note. Discord's
[Server Discovery](https://support.discord.com/hc/en-us/articles/360023968311-Server-Discovery)
finds public communities by keyword or category (Official doc, 5 Oct
2026). That is not message search. Server membership, channel visibility,
bot installation and message-content permission are separate gates. No
public message archive, RSS feed or sanctioned global message search was
found, and Discord's [developer policy](https://github.com/discord/discord-api-docs/blob/main/developers/policies/developer-policy.mdx)
was not read in depth. Use Discord only to find communities; any reading
of messages needs a separate, human-authorized route. Do not scrape
messages.

## Sources

- Official pages linked above, read 5 October 2026.
- Earlier notes: [forums.md](../../../capabilities/web/social/forums.md) and the discovery bundle (private, not published).
- Deep research round 1 (5 October 2026; private, not published), report G4, plus the 6 October corroboration.
- Research bundles: see [SOURCES.md](../SOURCES.md).
