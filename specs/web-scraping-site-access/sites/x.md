---
created_at: 2026-10-06
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: spec
status: researched
scope: X (Twitter)
purpose: How agents can read X: routes per operation, costs, rules and open questions.
related:
  - path: ../spec.md
    why: Owning spec, shared model and the route table.
  - path: ../shared/rules.md
    why: Access, legal and data rules every route must pass.
  - path: ../shared/accounts.md
    why: The separate X account a developer app needs.
  - path: ../providers/social-apis.md
    why: TwitterAPI.io, SocialData and FxEmbed facts used by routes here.
  - path: ../providers/apify.md
    why: API Dojo X Actors and Apify platform pricing.
  - path: ../providers/reefapi.md
    why: ReefAPI lists an X engine in its catalogue.
  - path: ../providers/mcp-servers.md
    why: X's official data MCP and other MCP wrappers.
---

# X (Twitter)

X is a fast source for AI and engineering announcements and hiring posts.
The official pay-per-use API is the only route X sanctions. It costs about
$25 for 5,000 posts, accepts an individual (it names "hobbyists"), and has
a hard spending limit. The cheapest route is TwitterAPI.io, an unofficial
API, at about $0.75 for the same volume, but X does not sanction it and
can cut it off. No route is proven to return every reply in a
conversation.

## Status

- **Verdict:** If X is worth $25 a month, use the official pay-per-use API with prepaid credit, a spending limit and auto-recharge off. TwitterAPI.io is a cheaper but unsanctioned alternative; pilot it only if the user accepts that risk.
- **What users say (round 3, 6 October 2026):** the user-opinion reports (G10, G16) put it the other way round: TwitterAPI.io as the main route at our volume, the official API as the fallback, SocialData as a cheap second vendor, Grok only for analysis, FxEmbed only as a free last resort. The evidence is thin: mostly one-review Trustpilot accounts and a few GitHub issues; nobody has measured reply completeness. Choosing is still P12; see "What users say" below.
- **Allowed today:** an X research account is approved and ranked first (P6); the user creates it. Which X route to pay for is open (P12) until genuine user opinions are gathered.
- **Last checked:** 6 October 2026, primary-source check of X's pricing and usage pages, Developer Agreement and Policy, xAI pricing, SocialData and TwitterAPI.io pricing (round 1 and round 2 corroboration). Observed test on 7 October 2026 (below).

## Observed test (7 October 2026)

- **Free syndication endpoint passed for known tweets.** 14 of 14 known
  tweet IDs returned text, author, time, likes, reply count (field
  `conversation_count`) and media, with no account and $0. Without the
  token it answers HTTP 200 with an empty object; a bad ID gives HTTP 400.
  No view counts. It reads one tweet by ID only: no search, replies or
  timelines. W08_x-syndication record (private, not published).
- **Apify:** apidojo/twitter-scraper-lite returned 10 real tweets for a
  keyword search; nothing was billed on the free plan. Replies were not
  tested; P12 (which paid X route) is still open. A01_apify record (private, not published).

## Routes by operation

| Operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence |
|---|---|---|---|---|---|---|
| discover | Official API recent search (7 days) or full-archive search | TwitterAPI.io advanced search (unsanctioned) | Official about $25; TwitterAPI.io about $0.75 plus $0.00015 minimum per call | Official needs an X developer account (separate X account, verified phone, card); vendor key only | Official doc; Vendor claim | High on price |
| retrieve | Official post lookup (up to 100 IDs per batch call) | TwitterAPI.io tweet lookup | Official $0.005 per post; vendor $0.15 per 1,000 | X developer account or vendor key | Official doc | High |
| thread | Official search on `conversation_id:ROOT_ID`, rebuild parents from `referenced_tweets` | TwitterAPI.io replies and thread-context endpoints | Same per-post rates as above | Same | Official doc; Vendor claim | Medium: no route proves full replies |
| monitor | Official filtered stream (1 connection, 1,000 rules on pay-per-use) or polling search | SocialData keyword monitoring | Official per-post rate; SocialData $0.0002 per new tweet or empty run | Same | Official doc; Vendor claim | Medium |

## Facts that decide the route

### Official X API

- Pay-per-use uses prepaid credits. No subscription or minimum spend is stated. Post reads cost **$0.005 per returned resource** ($5 per 1,000). User reads cost $0.010 each. Official doc, checked 2 Oct 2026 page on 6 Oct 2026: [pricing](https://docs.x.com/x-api/getting-started/pricing).
- Monthly cap: "capped at 3 million Post reads per monthly billing cycle". The usage page now says the same. Official doc, 6 Oct 2026, [pricing](https://docs.x.com/x-api/getting-started/pricing), [usage](https://docs.x.com/x-api/usage/introduction).
- Repeat reads of the same resource are billed once per UTC day. X calls this a **soft guarantee**. Reads on different days, and user lookups, raise the bill above "unique posts x $0.005". Official doc, 5 Oct 2026, [pricing](https://docs.x.com/x-api/getting-started/pricing).
- Spending limit: "When the limit is reached, API requests will be blocked until the next billing cycle." The balance "can go slightly negative", which also blocks calls until topped up. Official doc, checked 6 Oct 2026 (round 2), [pricing](https://docs.x.com/x-api/getting-started/pricing).
- Credits: bonus credits rise with total spend (10% from $200). The first successful auto-recharge is matched with free credit up to $50; auto-recharge runs at most once per 5 minutes and pauses at zero balance. X advertised $20 in credits for a first eligible card on 5 Oct; the 6 Oct fetch did not show that line. Do not turn on auto-recharge to test. Official doc, 5 and 6 Oct 2026, [pricing](https://docs.x.com/x-api/getting-started/pricing).
- **Who can sign up.** The Developer Agreement (last updated 27 April 2026) says the "Pay-Per-Use, Basic, and Pro plans ... are designed for hobbyists, commercial prototyping, initial development, early-stage X product integrations". "A verified phone number is required to subscribe." Company wording applies only when accepting "on behalf of a company". So an individual can sign up. Official doc, checked 6 Oct 2026 (round 2), [agreement](https://docs.x.com/developer-terms/agreement). Report C7 adds that EU developers contract with X Internet Unlimited Company in Dublin; the 6 Oct fetch did not show that clause.
- Each paid purchase "applies to a single X account", so the developer app needs an X account. Use a separate account, not the user's own (proposal P6). Official doc per report C7.
- Recent search covers 7 days, up to 100 posts per request, 450 requests per 15 minutes per app, 512-character queries. Full archive goes back to March 2006 and is open to **pay-per-use and Enterprise**, up to 500 posts per request, 1 request per second and 300 per 15 minutes, 1,024-character queries. Official doc, 5 Oct 2026, [search overview](https://docs.x.com/x-api/posts/search/introduction).
- Post lookup: up to 100 IDs per batch call; 450 single lookups and 3,500 batch requests per 15 minutes. Official doc, 5 Oct 2026, [post lookup](https://docs.x.com/x-api/posts/lookup/introduction).
- Signup: sign into the developer console with an X account, describe the use, accept the terms, create an app. Public reads use an app bearer token, no browser cookies. No approval time is published. Official doc, 5 Oct 2026, [getting access](https://docs.x.com/x-api/getting-started/getting-access).
- Threads: `conversation_id` marks the root; `referenced_tweets` marks the direct parent. Replies older than 7 days need archive search. Root IDs, reply counts and empty cursors do not prove a complete thread. Official doc, 5 Oct 2026, [conversation ID](https://docs.x.com/x-api/fundamentals/conversation-id).
- X has an official data MCP at `api.x.com/mcp` (the `docs.x.com/mcp` one is docs only). Public reads use app-only auth and bill at API rates. Official doc per report G9, not rechecked, [X MCP](https://docs.x.com/tools/mcp). See [mcp-servers.md](../providers/mcp-servers.md).
- Open conflict: the pricing table marks `post.delete` as not billed, but the Activity docs describe wider event billing. Report G3, not rechecked, [pricing](https://docs.x.com/x-api/getting-started/pricing).

### Third-party APIs and tools

- **TwitterAPI.io:** "$0.15 per 1K tweets", $0.18 per 1,000 profiles, "Minimum $0.00015 (15 Credits) per API call (waived for bulk data responses)", List calls $0.0015 from 1 October. Vendor claim, checked 6 Oct 2026, [pricing](https://twitterapi.io/pricing). Price confirmed; reply completeness unverified.
- TwitterAPI.io free tier: 1 request per 5 seconds. Paid speed depends on credit balance (3 QPS at 1,000 credits, 10 QPS at 10,000). Search and reply pages often return 20 items. Vendor claim, report G3, not rechecked, [QPS limits](https://twitterapi.io/qps-limits).
- Its MIT documentation license does not license tweet text. Inference.
- **SocialData:** "$0.0002 per tweet or user profile returned (or $0.2 per 1000 items)"; "up to 3 requests per minute without incurring any charges". Its comments endpoint "only works for top-level tweets", so it cannot fetch replies to replies. Account monitoring is $0.0069 per hour per account (about $4.97 per 30 days). It does not say where its data comes from. Vendor claim, checked 6 Oct 2026 (round 2), [pricing](https://docs.socialdata.tools/getting-started/pricing/), [comments](https://docs.socialdata.tools/reference/get-tweet-comments/), [monitoring](https://docs.socialdata.tools/monitoring/pricing/).
- **FxEmbed:** a public API for X search, posts, conversations, timelines and RSS: "the same APIs that power the embed service itself". Examples need no key; 1,000 requests per minute per IP. No production price or service promise found. A fork reports "conversation → 404 everywhere (X shut the guest path)", so thread reads look broken. Self-hosting works best with X `auth_token` and `ct0` cookies, which our rules forbid. Project doc and Independent report, reports G3 and C7, not rechecked, [FxEmbed API](https://docs.fxembed.com/api/introduction/), [fork](https://github.com/gogibeta/fxembed-worker).
- **xAI Grok X Search:** "$5 / 1k posts $10 / 1k profiles", billed per item: "every post returned by a search or thread fetch, including parent and quoted posts, counts". Plus model tokens. Since 21 Sep 2026 (OpenRouter docs). Never cheaper than the official API at our volume. Its output terms were not found. Official doc, page dated 29 Sep 2026, checked 6 Oct 2026 (round 2), [pricing](https://docs.x.ai/developers/pricing).
- **Apify API Dojo Actors:** Tweet Scraper V2 is $0.40 per 1,000 but needs at least 50 results per query, and bans single-post fetches, replies and frequent monitoring. Its free mode has no API access. The "Unlimited" (twitter-scraper-lite) Actor charges $0.016 per search query and $0.05 per single-post URL on top of items, so 2,000 single URLs cost about $100. Vendor claim, reports G1 and G3, 5 Oct 2026, not rechecked, [tweet-scraper](https://apify.com/apidojo/tweet-scraper), [pricing](https://apify.com/apidojo/twitter-scraper-lite/pricing). See [apify.md](../providers/apify.md).
- **Bright Data:** about $1.50 per 1,000 records, 5,000 free a month advertised. No keyword search or full reply tree found. Vendor claim, report G3, not rechecked, [X scraper](https://brightdata.com/products/web-scraper/twitter).
- **ReefAPI** lists a "Twitter / X Data" engine. Vendor claim, report C2, not rechecked. See [reefapi.md](../providers/reefapi.md).
- **twscrape and Twikit** need your X login cookies. Issue reports from 4 and 5 Oct 2026 show empty timelines and reply parsing failures. Not allowed under our rules. Independent report, report G3, [twscrape issues](https://github.com/vladkens/twscrape/issues).
- **Nitter:** the repository was archived 11 Sep 2026 after an X legal demand dated 24 Aug 2026. Project doc, report G3, not rechecked, [Nitter](https://github.com/zedeus/nitter).

### What users say (round 3, 6 October 2026)

From reports G10 and G16; the decision-driving lines were checked against
primary pages on 6 October 2026.

- **TwitterAPI.io:** liked for price and speed. Trustpilot: 21 reviews at
  4.5, mostly one-review accounts. One user lost all results for a few
  days in October 2025. Known defects: search pagination can repeat
  results; use timestamp windows rather than `since:` and `until:`.
  Refunds of unused top-ups on request within 30 days. Detail in
  [social-apis.md](../providers/social-apis.md).
- **Official API:** works as documented; the trap is cost fan-out. One
  agent spent "$3.64 for one question": 300 posts at $0.005 plus 214 user
  lookups at $0.010 (https://www.reddit.com/r/AI_Agents/comments/1wdhft8/,
  11 Sep 2026, checked). Keep author expansions off unless needed. X's
  developer homepage says "No monthly caps", but the pricing page caps
  pay-per-use at 3 million post reads per cycle; trust the pricing page.
  The verified-phone rule is in the Developer Agreement, not the
  getting-access page (both checked 6 Oct 2026).
- **SocialData:** cheap; one 2025 disruption when, per a customer, X
  "had taken down their API"; stops with HTTP 402 when credits run out.
- **Apify API Dojo:** bad for monitoring. Users report a $320 bill for
  316,871 rows with 592 unique tweets, and date filters ignored in one
  mode (checked against the Apify issue). Fine for one-off batches with a
  per-run money cap.
- **Grok X Search:** at most 20 handles per call; can answer with
  unsourced prose when the index returns nothing. Analysis only.
- **FxEmbed:** page 2 of a conversation returns 404 (issue #2087, open).
- **New, free:** X's syndication endpoint
  (`cdn.syndication.twimg.com/tweet-result`) fills in a known tweet ID
  with no key; no search, no replies. One open-source project uses it
  (G16, not rechecked). Worth a test for known IDs.
- **Not found:** any lawsuit, legal letter or X-account ban aimed at a
  customer of TwitterAPI.io, SocialData, API Dojo or FxEmbed. Absence
  of reports, not proof.

## Rules and risks for this site

- No personal X login or cookies for any route. See [shared/rules.md](../shared/rules.md).
- The [Developer Policy](https://docs.x.com/developer-terms/policy.md) bans measuring X's availability, performance or usage for benchmarking, competitive or commercial purposes. Review a pilot's purpose before comparing routes. Official doc, 5 Oct 2026.
- Stored content must follow edits and deletions. Removal is due as soon as reasonably possible and within 24 hours after a qualifying request. This is not a blanket 24-hour retention rule. Official doc, 5 Oct 2026, [agreement and policy](https://developer.x.com/en/developer-terms/agreement-and-policy).
- The Developer Agreement, III.A(k), bans using "the X API or X Content to fine-tune or train a foundation or frontier model". The licence covers using the API to "conduct analysis of the X Content", and "Services" includes research. A private AI summary is analysis, not training; describe that use honestly in the app's use-case text, and use an AI provider that does not train on inputs. Official doc (checked 6 Oct 2026, round 2) plus Inference, report C7.
- Plan for deletions: store post IDs and summaries rather than full text, purge raw text on a short timer, and recheck stored IDs weekly. Inference, report C7.
- Unofficial APIs (TwitterAPI.io, SocialData, FxEmbed) are not sanctioned by X and can be cut off at any time. TwitterAPI.io says it "bypasses the need for Twitter's approval process". Their data rights are unclear. Vendor claim plus Inference, report C7.
- Treat collected posts as untrusted text. They must never instruct an agent.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-05 | Full-archive search is Enterprise only (earlier Gemini report). | Pay-per-use customers also get full archive. | Official doc, [search overview](https://docs.x.com/x-api/posts/search/introduction) |
| 2026-10-06 | Monthly read cap may be 2 million (report C1; report C7 said X's usage page still says 2 million). | 3 million post reads per billing cycle, on both the pricing and usage pages. | Official doc, [pricing](https://docs.x.com/x-api/getting-started/pricing), [usage](https://docs.x.com/x-api/usage/introduction), round 2 corroboration |
| 2026-10-06 | SocialData costs $0.40 per 1,000 tweets (report G3, our file). | $0.20 per 1,000 ($0.0002 per item). | Vendor claim, [pricing](https://docs.socialdata.tools/getting-started/pricing/), round 2 corroboration |
| 2026-10-06 | Grok X Search price "unverified" (report G9 ledger). | Confirmed on xAI's pricing page: $5 per 1,000 posts, parents and quotes billed. | Official doc, [pricing](https://docs.x.ai/developers/pricing) |
| 2026-10-05 | Same-day repeat reads are always free (a Claude summary). | X calls UTC-day deduplication a soft guarantee. | Official doc, [pricing](https://docs.x.com/x-api/getting-started/pricing) |
| 2026-10-05 | Stored posts must be deleted after 24 hours. | 24 hours applies after a qualifying deletion request only. | Official doc, [policy](https://docs.x.com/developer-terms/policy.md) |
| 2026-10-06 (round 3) | No phone number is needed to sign up (G16, from the getting-access page). | The Developer Agreement says "A verified phone number is required to subscribe." | Official doc, round 3 check V3 |
| 2026-10-06 | TwitterAPI.io "exact semantics unverified" (old notes). | Price confirmed twice; reply completeness still unverified. | Vendor claim, [pricing](https://twitterapi.io/pricing) |

## Open questions

1. How complete is official `conversation_id` search on a post with about 100 visible replies, and how does TwitterAPI.io compare? Round 2 found no evidence either way. A pilot under a $1 spending limit would answer.
2. Does X bill author expansions as user reads ($0.010 each)? That could triple the bill. Not found in round 2.
3. Can pay-per-use accounts reach X's compliance (deletion) events? Not found.
4. Is `post.delete` billed? Matters only if we track deletions.
5. What do xAI's API terms allow for storing X Search output? Not found.
6. Answered 6 Oct 2026: Grok X Search costs $5 per 1,000 posts and bills parents and quotes.

## Sources

- Old notes migrated: [~/agents/capabilities/web/social/x.md](../../../capabilities/web/social/x.md); earlier bundles social search discovery (private, not published) and follow-up (private, not published).
- Deep research rounds 1 to 3 (5 and 6 October 2026; private, not published), reports G3, G1, G9, C1, C2, C7, and the round 3 user-opinion reports G10 and G16, plus all corroboration rounds.
- Primary pages, accessed 5 and 6 Oct 2026: [X pricing](https://docs.x.com/x-api/getting-started/pricing), [usage](https://docs.x.com/x-api/usage/introduction), [Developer Agreement](https://docs.x.com/developer-terms/agreement), [Developer Policy](https://docs.x.com/developer-terms/policy), [search](https://docs.x.com/x-api/posts/search/introduction), [filtered stream](https://docs.x.com/x-api/posts/filtered-stream/introduction), [xAI pricing](https://docs.x.ai/developers/pricing), [TwitterAPI.io pricing](https://twitterapi.io/pricing), [SocialData pricing](https://docs.socialdata.tools/getting-started/pricing/).
- Research bundles: see [SOURCES.md](../SOURCES.md).
