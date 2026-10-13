---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [Y04a, Y04b]
source_files: [sources/Y04a-transcriptapi-home.md, sources/Y04b-transcriptapi-docs-api.md]
purpose: One-source digest feeding the spec compendium.
---

# TranscriptAPI homepage and API reference (Y04)

**What it is:** Two provider pages: [homepage](https://transcriptapi.com/) and [API reference](https://transcriptapi.com/docs/api/). Both captures list author and publication date as unknown. Captured 2026-10-13. The files contain 665 and 2,559 lines, including navigation, examples, and embedded image data. No reading time is supplied.
**Capture status:** Both marked full. Linked MCP setup pages are not included. Full capture means the pages were captured, not that the service was tested. Local evidence: Y04a, Y04b.

## The point in three sentences

TranscriptAPI is a hosted service for fetching YouTube captions and discovering videos, channels, and playlists. It offers REST requests, MCP connections, and installable agent skills, with 100 trial credits and paid usage after that. Its docs provide useful output and error contracts, but neither capture proves independent reliability or offers an audio transcription fallback for videos without captions.

## Key ideas

- This is separate from the similarly named Python package. The provider hosts the extraction infrastructure. Quote: "TranscriptAPI is a hosted REST API" (Y04a, FAQ: Is TranscriptAPI the same as youtubetranscriptapi?).
- A Google key is unnecessary. You authenticate to TranscriptAPI and spend its credits. Quote: "You do not need a Google or YouTube Data API key" (Y04a, FAQ: Does it use my YouTube Data API quota?).
- REST output can retain timing or remove it. Even text mode is shown inside a JSON response, with a string in `transcript`. Quote: "Segments with `text`, `start`, `duration`" (Y04b, include_timestamp behavior matrix).
- Select caption tracks with an ordered language list. Plain language codes prefer manual captions and normally fall back to automatic captions. Quote: "Up to 10 codes." (Y04b, language parameter).
- Manual-only selection is available. `language_fallback=false` suppresses automatic fallback for plain codes, while explicit `asr` requests still select automatic captions. Quote: "human-made captions only" (Y04b, language_fallback parameter).
- Caption discovery is free in credits, subject to account requirements. It can still return 404 for a video without captions. Quote: "spending a transcript credit" (Y04b, YouTube Video Info, rendered text).
- Paid cached responses still cost a credit. Local caching therefore matters for repeated worker use. Quote: "Credits are deducted in real-time only when a request is successfully returned." (Y04b, When Credits Are Charged).
- Channel and playlist listing return video records, not every transcript. Following pages and then fetching each transcript are separate operations. Quote: "Each page costs 1 credit." (Y04b, Search Within Channel).
- Channel sorting changes which videos appear as well as their order. The unsorted uploads playlist mixes Shorts and long videos, while a sorted Videos tab excludes Shorts and includes flagged membership videos. Quote: "These are different **sets**, not one list in two orders." (Y04b, Sorting).
- Use error codes to distinguish missing captions from unavailable videos. Quote: "Branch on `code`, not on `detail`" (Y04b, 404 error codes).
- Bot detection remains a documented failure. Quote: "Temporary failure (bot detection, network) - retry in 1-5s" (Y04b, Error Handling, 408 row). This limits the homepage's agent-skill claim "never blocked, no manual setup" (Y04a, Agent Skills).
- Production volume is provider-reported evidence, not a measured success rate. Quote: "49ms median response time. 15M+ transcripts served last month." (Y04a, 500K+ Transcripts Processed Daily).

## How to do it (concrete steps, checklists, templates)

### Route 1: REST caption extraction

1. Get a free API key through signup, then the API Keys dashboard.
2. Make a request with a Bearer token, the key carried in the Authorization header:

```sh
curl -X GET "https://transcriptapi.com/api/v2/youtube/transcript?video_url=dQw4w9WgXcQ" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

3. Choose a language with `language=de,en,asr`, or inspect available languages free through `/youtube/info` first. Accepted video inputs include the full YouTube URL, shortened URL, or 11-character ID.
4. Set output parameters as needed. `format=json` and `include_timestamp=true` are defaults. `send_metadata=true` adds title, channel name and URL, and thumbnail URL.

| Parameters | Value of `transcript` in the JSON response |
| --- | --- |
| `format=json`, timestamps on | Segment array with text, start seconds, duration seconds |
| `format=json`, timestamps off | Segment array with text only |
| `format=text`, timestamps on | String with lines such as `[123.45s] text` |
| `format=text`, timestamps off | Concatenated transcript string |

Responses also contain `video_id`, resolved `language`, `length_seconds`, and `lengthText`. The length fields can be null for live streams and a rare fallback extraction path. The capture does not explain that fallback path. `X-Cache-Status` reports `HIT`, `PARTIAL-HIT`, or `MISS`.

**Cost:** One credit per successful transcript, including provider cache hits. Failure responses consume no credits. The same REST route is used by cURL, Python, Node.js, browser applications through a backend, and named automation products. These are client choices, not separately evidenced extraction systems.

**Failure modes:** `404/no_captions` means no captions exist. `404/video_unavailable` covers deleted, private, nonexistent, or unplayable videos. Neither should be retried unchanged. `404/no_transcript_for_requested_languages` supplies available languages for a revised request. Invalid credentials, exhausted credits, and invalid inputs produce 401, 402, and 400/422 respectively. Retry 408 and 503 after 1 to 5 seconds; retry 429 after `Retry-After`. The docs prescribe increasing delays and at most 2 to 3 retries, while also saying not to retry more than twice within 3 seconds. Persistent 500 errors call for support.

**IP blocks and bot checks:** The homepage promises relief from YouTube blocks, but gives no IP-block statistics or proxy setup steps. The metadata docs mention a provider-managed proxied production path for player details. Bot detection is explicitly included in 408 errors. No CAPTCHA or cookie procedure is supplied.

**Reliability evidence:** Response examples, error documentation, and homepage production-volume claims. No independent test, uptime history, or extraction success denominator appears.

### Route 2: YouTube MCP

MCP is a tool connection protocol for AI clients. The homepage gives this Claude Code installation command:

```sh
claude mcp add --transport http transcript-api https://transcriptapi.com/mcp
```

It also supplies universal JSON configuration:

```json
{
  "url": "https://transcriptapi.com/mcp"
}
```

Then ask the assistant to summarize a video or find videos and summarize them. The FAQ says Claude and ChatGPT use OAuth account authorization, while OpenAI Agent Builder uses an API key. Client-specific setup steps are in linked pages outside this packet.

**Cost:** The same credits as REST. **Output:** Transcript access is advertised, but these captures do not show a complete MCP transcript result or its timestamp controls. Y04b names `get_youtube_transcript` and says its error text ends with `(code: no_captions)` or `(code: video_unavailable)`. Homepage demo shorthand uses `get_transcript`, so do not assume all displayed names are canonical tool names.

**Failures and reliability:** Missing-caption and unavailable-video errors are explicitly mapped to MCP. Route-specific handling for IP blocks, bot checks, rate limits, and retries is not shown. No separate MCP reliability measurements appear.

### Route 3: Agent Skills

The homepage gives two install choices:

```sh
npx clawhub@latest install youtube-full
npx skills add ZeroPointRepo/youtube-skills --skill youtube-full
```

The first is for OpenClaw. The second is for Claude Code, Cursor, and Windsurf. After installation, ask for a video summary or playlist transcripts. The provider says the agent creates an account and gets an API key on first use, with 100 free credits.

**Cost:** Trial credits, then the underlying service pricing. No separate skill fee is stated. **Output:** The page demonstrates requests for summaries and transcripts but does not specify the skill's stored-file format, raw transcript schema, or timestamp options.

**Failures and reliability:** The skill still depends on TranscriptAPI. No skill-specific recovery steps for missing captions, IP blocks, or bot checks appear. The claim of never being blocked is marketing, with no skill test results in the packet. The captured docs acknowledge bot detection and missing captions in the underlying API.

### Discovery routes feeding extraction

All REST paths below use the same API key and base URL. Their outputs are JSON discovery records, not timestamped caption segments. Fetch each chosen video's transcript separately. The general API error policy applies, but the captures provide no per-endpoint IP-block or bot-check measurements.

| Route and setup inputs | Cost | Output and limitations |
| --- | --- | --- |
| `/youtube/search`: `q`, optional type and filters, then continuation | 1/page | About 20 records/page; caption flags; homepage `limit` examples are absent from the reference parameter table |
| `/youtube/channel/search`: channel plus query, then continuation | 1/page | About 30 video records/page |
| `/youtube/channel/videos`: channel, optional tab and sort | 1/page | About 100 unsorted uploads or 30 sorted Videos-tab records/page; repeat tab and sort when paging |
| `/youtube/playlist/videos`: playlist ID or URL, then continuation | 1/page | About 100 video records/page, playlist metadata and indices |
| `/youtube/channel/latest`: channel | Free | Latest 15 RSS videos, publication timestamps and view counts; not caption timestamps |
| `/youtube/info`: video URL or ID | Free | Metadata and available caption languages; 404 if no captions or nonexistent video |
| `/youtube/channel/resolve`: handle, URL, or channel ID | Free | Canonical channel ID; valid UC IDs take a direct path |

For paginated routes, follow `continuation_token` until `has_more=false` or the token is null. Free endpoints require authentication and at least one active credit. The `/info` section also says an active plan is required.

Other documented data routes are `/youtube/video/metadata`, `/youtube/channel/info`, `/youtube/channel/playlists`, `/youtube/channel/posts`, and `/youtube/channel/sections`. Each costs one credit per request or page and is cached for five minutes. Metadata can work without captions; unavailable player details return `details.available=false` with a reason. Community and curated tabs can return empty lists when absent. They provide context, not an alternative transcript extraction route.

## Tools, code and commands named

- Base URL: `https://transcriptapi.com/api/v2`; transcript v1 is also mentioned for error-code compatibility.
- cURL; Python `requests` and `json`; JavaScript `fetch` and `URLSearchParams`; Node.js 18+; `node-fetch` for older versions; Swagger UI.
- n8n, Make, Zapier; ChatGPT, Claude, Claude Code, Cursor, VS Code, Windsurf, OpenClaw, OpenAI Agent Builder.
- `youtube-full`; `ZeroPointRepo/youtube-skills`; `clawhub@latest`; `skills add`; MCP endpoint `https://transcriptapi.com/mcp`.
- Deprecated aliases: `/youtube/video/info`, `channel_id`, `playlist_id`. Use the current documented paths and parameters.

## Numbers and strong claims

- Y04a, Monthly: $5/month, 1,000 credits/month, $2.50 per extra 1,000, 200 requests/minute.
- Y04a, Annual: $54/year, displayed as $4.50/month, 1,000 credits/month, $1.50 per extra 1,000, 300 requests/minute. Credits are monthly, not a stated annual pool.
- Y04a, Pricing Calculator: 10,000 monthly transcripts on annual pricing costs $18/month, or $1.80 per 1,000. This is a displayed estimate, not a benchmark bill.
- Y04a, Top-up credit expiry: credits last at least 30 days or until the subscription period ends, whichever is later. An active subscription is needed to use them.
- Y04b, Rate Limits: limits apply per account across all keys; annual and OpenClaw are listed at 300 requests/minute.
- Y04a, production section: 500K+ daily, 15M+ last month, 49ms median. Marketing claims with no measurement method or cache breakdown. The page labels youtubetotranscript.com and recapio.com as verified production users at roughly 11M and 2.8M transcripts/month.
- **User reports:** Neither capture includes an authored, dated user report. The customer labels above are provider statements, not quotations from those customers. No author or report date can be supplied.

## Compared with the deep research report

Comparison is limited to the TranscriptAPI paragraph and its ranking entry in Y00.

- **Right:** Y00 says "100 free credits to start." Y04a says "new accounts get 100 free credits, no card required" (FAQ). Its $5/1,000 pricing, successful-request charging, discovery endpoints, and MCP summary match the captures.
- **Overstated:** Y00's ranking calls it "Excellent managed alternative". Y04a supplies production-volume claims, but Y04b documents "Temporary failure (bot detection, network) - retry in 1-5s". The recommendation is an assessment, not demonstrated reliability.
- **Left out:** Y00 says "One credit per successful transcript request." Y04b adds "Cached responses" to charged requests (When Credits Are Charged). Y00 also omits annual pricing, top-up conditions, shared rate limits, free discovery account requirements, precise language selection, timestamp schemas, and caption-specific errors.
- **Left out:** Y00 says "Search, channel and playlist endpoints." Y04b says "Each page costs 1 credit." Bulk listing needs pagination and separate transcript calls. Sorting also changes channel coverage and roughly triples page costs.
- **Unproven rather than wrong:** Y00 says "both are inexpensive enough to benchmark". These captures establish listed prices, not the user's actual cost or a comparative extraction benchmark.

## Fit for the user's agent workspace

- (inference) Start with a small REST wrapper using Node.js fetch. Its documented JSON segments give cheap workers a predictable input with quote timestamps.
- (inference) Preserve resolved language and manual/automatic caption status alongside output. These affect how confidently a worker can quote the speaker.
- (inference) Cache successful results locally. Provider cache hits still consume credits.
- (inference) Record failures separately from worker summarization failures. Missing captions are a source limitation; bot detection and rate limits are infrastructure failures.
- (inference) Give playlist work explicit page and transcript budgets. A playlist listing is not one bulk transcript purchase.
- (inference) Treat MCP and skills as convenience options to test. Their setup and output details are less complete in this packet than REST's.
- (inference) Benchmark on representative videos before selecting this as the managed fallback. No dated user testimony or independent reliability result supports skipping that step.

## Best parts to read or watch first

Reading estimates below are inference, not source timings.

- Y04b, YouTube Transcript: 5 to 7 minutes. Covers parameters, language selection, and all four output combinations.
- Y04b, Error Handling and 404 error codes: 3 to 4 minutes. Establishes when to retry and when captions are unavailable.
- Y04a, One Plan. Every Feature Included, plus top-up expiry: 2 minutes. Covers the recurring cost and credit conditions.
- Y04b, Channel Videos (Paginated), especially Sorting: 3 minutes. Prevents incomplete catalogues and unexpected page costs.
- Y04a, API. MCP. Agent Skills.: 2 to 3 minutes. Gives installation commands and identifies missing linked setup detail.
