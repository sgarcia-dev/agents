---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [Y06a, Y06b, Y06c, Y06d]
source_files: [sources/Y06a-apify-home.md, sources/Y06b-apify-hypebridge-youtube-transcript-scraper.md, sources/Y06c-scrapecreators-home.md, sources/Y06d-scrapecreators-youtube-transcript-docs.md]
purpose: One-source digest feeding the spec compendium.
---

# Apify and ScrapeCreators (Y06a–Y06d)

**What it is:** Four vendor web captures: Apify's marketplace homepage, Hypebridge's YouTube Transcript Scraper listing and configuration, ScrapeCreators' homepage, and its YouTube Transcript API reference. Hypebridge is the named Actor developer; the other captures have unknown authors. Publication dates are unknown. All were captured on 2026-10-13. The files total 2,897 lines, including repeated navigation, image links, and sample responses. Links: [Apify](https://apify.com/), [Hypebridge Actor](https://apify.com/hypebridge/youtube-transcript-scraper), [ScrapeCreators](https://scrapecreators.com/), [transcript reference](https://docs.scrapecreators.com/v1/youtube/video/transcript).

**Capture status:** Y06a is full main content, excluding navigation and footer. Y06b is full for the README, pricing table, eight input properties, and embedded input schema; the separate Output and API tabs are linked rather than captured. Y06c is partial: collapsed FAQ answers are missing. Y06d is partial: endpoint, headers, parameters, and the rendered 200 response are present, but alternate response and code tabs are not expanded. Capture-time HTTP 429 errors describe collection attempts, not failures of the transcript services.

## The point in three sentences

Hypebridge offers batch retrieval of existing public YouTube captions through an Apify Actor, a hosted task with inputs and dataset outputs. ScrapeCreators offers a single-video HTTP endpoint with explicit language selection, original-language checks, and free cached responses. Both document useful behavior, but neither capture proves extraction reliability on the user's videos, and Hypebridge's pricing descriptions conflict.

## Key ideas

- Apify is the hosting and marketplace layer, not one uniform transcript service. Its homepage calls it a “marketplace of ready-to-run tools for AI” (Y06a, opening paragraph); individual Actors need separate assessment.
- Hypebridge retrieves captions for public videos and Shorts. It says “One dataset record is produced per valid video input” (Y06b, listing introduction), including status for unavailable captions. There is no documented audio transcription fallback in this Actor.
- Hypebridge supports several input forms: watch, Shorts, share, embed, regional URLs, and bare video IDs. The README names “Bare 11-Character Video IDs” (Y06b, Supported URL Formats). Channel and playlist discovery are not documented for this Actor.
- Hypebridge exposes eight input controls and bounded parallel work. Its input tab says “Concurrent videos, from 1 to 15.” (Y06b, Max concurrency). The default is 10; the default processing limit is 100, with a maximum of 10,000.
- Hypebridge's language control is a preference, not a guarantee. The schema says “Automatic uses the URL market language; a matching caption track is not guaranteed.” (Y06b, Preferred language). This is weaker than the FAQ's broad supported-language wording.
- The diagnostic fallback classifies an empty response; it does not generate speech text. Its precise description is “Fetch a watch page once to classify an empty response.” (Y06b, Diagnose empty transcripts).
- Hypebridge documents payment for successful extraction and no item charge for missing captions. The pricing table says “Videos with disabled captions or errors are free ($0.00).” (Y06b, Pricing Breakdown). A separate Actor start event still exists.
- Hypebridge's output descriptions have a naming mismatch. The field table lists `scrapedAt`, while Sample Output uses `extractedAt`; the missing-transcript FAQ says “with an empty transcript array” (Y06b, Why is a transcript missing for a video?), although the successful sample names its array `segments`. Treat these as unresolved schema details.
- ScrapeCreators uses a simple API key header. Its homepage says “No OAuth dance, no SDK required.” (Y06c, One header. Every endpoint.). OAuth is an account authorization flow; the documented endpoint instead requires `x-api-key` and a video URL.
- ScrapeCreators' default caption choice considers original spoken language, then falls back when that metadata is uncertain. The reference says “prefers an auto-generated caption, otherwise the first caption track” (Y06d, Query Parameters, language). An explicit `language` overrides this unless `original_audio=true`.
- Original-language mode can deliberately return no transcript. The reference says “Takes precedence over language.” (Y06d, original_audio). If original audio cannot be reliably identified or matching captions are missing, transcript, text, and language are null, without a charge.
- ScrapeCreators distinguishes cached responses from live extraction. The homepage says “Cached result? Free.” (Y06c, Cache). The endpoint documents `cache_max_age`, zero-credit cache hits, and cache provenance fields; it does not establish that every repeat request is free without that control.
- Reliability claims need narrower interpretation than the headlines suggest. ScrapeCreators recommends “staying below 500 concurrent requests” (Y06c, No rate limits). Hypebridge has two total users, one monthly active user, and zero reviews in the capture; neither these counts nor platform uptime establish caption accuracy or extraction success.

## How to do it (concrete steps, checklists, templates)

### Route 1: Hypebridge through Apify Console

The README gives these steps in order:

1. Create a free Apify account.
2. Open YouTube Transcript Scraper and click Try for free.
3. Paste video URLs or IDs into YouTube video URLs or IDs.
4. Set Max items.
5. Optionally choose Preferred language and whether to include full text or segments.
6. Click Start, then download the dataset as JSON, CSV, Excel, XML, or HTML.

The single-video example uses `videoUrls`, `maxItems: 1`, `includeFullText: true`, and `includeSegments: true`. The text-only example sets `includeSegments: false`. The input schema also exposes `proxyCountry` with AUTO, US, IN, BR, JP, and DE, and enables `diagnosticFallback` by default.

**Cost per transcript:** The pricing tab lists Free $0.001, Starter $0.00089, Scale $0.00078, and Business $0.00067 per successful transcript. Monthly plan prices are $0, $19, $199, and $999, respectively, with spend allowances. All events lists an Actor Start charge of $0.00005 and included platform costs. The README instead describes that start charge as $0.00005/GB, calls the cheapest tier Gold, and gives Starter $49/month and Scale $499/month. The capture does not resolve these differences. The event rates alone are not the total cost of a paid plan or a run.

**Failure modes:** Documented statuses are `available`, `no_transcript`, `unavailable`, and `invalid_id`. Disabled captions with no automated captions yield `no_transcript` and no item charge. Exact triggers for other statuses, retry behavior, blocking recovery, and guaranteed language matching are not supplied.

**Output:** Dataset records include identity, URL, market, requested locale, status, segment and chapter counts, `chapters`, `segments`, and optional `fullText`. Sample segments include `index`, `chapter`, `timestamp`, numeric `startSeconds`, and `text`. Chapters carry title and segment start index. Resolve timestamp-field and empty-array naming conflicts before depending on them.

**Reliability evidence:** Input schema, sample output, and explicit failure statuses document the intended interface. No benchmark, live run result, or extraction success percentage is captured. The listing is community-maintained and has no reviews. Apify's homepage uptime claim is about the platform.

### Route 2: ScrapeCreators direct transcript API

The homepage says to sign up, obtain an API key, and make a first request. The endpoint requires GET `https://api.scrapecreators.com/v1/youtube/video/transcript`, the `x-api-key` header, and a `url` query parameter containing a video or Short URL. The captured cURL example leaves the key blank and omits the required URL, so it is not a complete runnable request.

Optional controls documented by the reference:

- `language`: caption language code such as `en`, `es`, `fr`, or `en-US`.
- `original_audio=true`: accept only captions matching reliably identified original speech; overrides `language`.
- `cache_max_age`: accept cached responses within `1d`, `3d`, `7d`, `14d`, or `30d`; otherwise fetch live.

**Cost per transcript:** A live returned transcript costs one credit. At $47/25,000 credits, that is $0.00188 per transcript. At $497/500,000 credits, it is $0.000994 per transcript. These are calculated unit rates assuming the purchased credits are used for this endpoint. Eligible cache hits cost zero. Specified language-related null outcomes cost zero. There are 100 initial free credits and up to 7,000 conditional bonus credits; paid credits do not expire. Enterprise pricing is custom.

**Failure modes:** Requested or identified original language without matching captions gives a null transcript and no charge. Strict original-audio mode also rejects uncertain original-language metadata. The page lists 400, 403, 404, and 500 tabs, but their bodies are absent: exact meanings, billing, retries, and recovery are not established. No speech-to-text fallback is documented.

**Output:** JSON includes `success`, `credits_remaining`, `credits_charged`, `videoId`, `type`, `url`, `transcript`, `transcript_only_text`, and `language`. Each sample transcript segment has `text`, string-valued `startMs` and `endMs`, and `startTimeText`. Cache hits add `cached: true` and `cached_at`. The rendered sample is illustrative and abbreviates the full text.

**Reliability evidence:** The reference documents selection and null behavior. The homepage advertises 98.2% success and 3.12s average response; the latter is labeled production data from the last 30 days. Neither is scoped to YouTube transcripts or accompanied by a test method. Testimonials are vendor-selected opinions, not controlled measurements.

### Other access paths and advertised Actors

Both homepages link MCP, CLI, and agent skills. MCP, Model Context Protocol, exposes services as agent tools. Apify supplies an HTTP MCP configuration at `https://mcp.apify.com` and `curl -s https://apify.com/agents.md`. ScrapeCreators supplies an MCP URL at `https://api.scrapecreators.com/mcp`, CLI and skill links, and API schemas. The captures do not give complete YouTube setup, commands, authentication, output behavior, or reliability evidence for those access paths. Separate per-transcript charges are not stated. Hypebridge's API tab is linked but its calling procedure is not captured.

Y06b's recommendation cards advertise additional extraction routes. These are marketing snippets, not full documentation:

| Actor | Advertised output or scope | Price evidence | Reliability evidence |
| --- | --- | --- | --- |
| `insight_api_labs/youtube-transcript` | Video details and transcript timestamps | Title says $1/month; unit cost unknown | 3.1 rating, 3 reviews |
| `akash9078/youtube-transcript-extractor` | Captions, Shorts, stream recordings, Premieres, 100+ languages | Missing | 205 shown users |
| `dz_omar/youtube-transcript-metadata-extractor` | Complete text, timestamps, metadata | Missing | 5.0, 15 reviews |
| `ytranscript/youtube-transcript` | Bulk text, spoken language, timed segments; claims audio transcription without captions | Missing | 2 shown users |
| `akash9078/youtube-full-channel-transcripts-extractor` | Channel or individual video captions | Missing | 5.0, 1 review |
| `easyapi/youtube-transcript-scraper` | Transcripts through multiple services | Missing | 61 shown users |
| `seemuapps/youtube-transcript-scraper` | Chosen-language text, JSON or CSV | Missing | 5.0, 1 review |
| `calm_builder/youtube-transcript-scraper` | Videos, Shorts, channels, playlists; TXT, SRT, timed segments | Missing | 21 shown users |
| `agentx/youtube-transcript` | Language, timed segments, metadata, translation into 133 languages | Starts at $0.3483 | 4.7, 4 reviews |
| `vistics/youtube-transcript-scraper-2-1000` | Transcript and additional information | Title says $2/1,000, equivalent to $0.002 each | 5.0, 13 reviews |

Setup and failure behavior are missing for every recommendation-card route. Ratings and user counts do not demonstrate extraction success. Their advertised features must not be attributed to Hypebridge.

## Tools, code and commands named

- Main extraction identifiers: `hypebridge/youtube-transcript-scraper`, GET `/v1/youtube/video/transcript`, `x-api-key`, and the parameters above. The endpoint path is `v1`; no client package versions are supplied.
- Apify names Python, JavaScript, TypeScript, Playwright, Puppeteer, Selenium, Scrapy, Crawlee, Cheerio, BeautifulSoup, LangChain, and LlamaIndex. Its example imports `PuppeteerCrawler` and `Dataset` from `crawlee`; this is generic page crawling code, not a YouTube transcript implementation.
- Apify names Zapier, GitHub, Google Sheets, Claude, n8n, MCP clients, Google Drive, and Slack as integrations.
- ScrapeCreators links `openapi.json`, `llms.txt`, `llms-full.txt`, MCP, CLI, and its agent skill. Its CLI illustration is `scrape-creators tiktok profile @charlidamelio`, not a YouTube command.
- The transcript reference names cURL, Node.js, Python, PHP, Go, and Java tabs; only cURL is rendered.

## Numbers and strong claims

- **Documented configuration:** Hypebridge accepts up to 10,000 inputs, processes 1–10,000 items, defaults to 100 items, and permits 1–15 concurrent videos (Y06b, Input/schema).
- **Pricing conflict:** README estimates roughly 5,000 free transcripts, 49,000 Starter transcripts, and 744,000+ Scale transcripts. Its plan prices differ from the pricing tab (Y06b, Approximate Results by Plan versus Pricing tab). These are vendor estimates, not measured yields.
- **Marketing:** Apify advertises 86,591 tools and 99.95% uptime (Y06a, opening heading and Enterprise-grade solution). Neither number measures this Actor's reliability.
- **Marketing/self-reported metrics:** ScrapeCreators advertises 10M+ daily requests, 98.2% success, 3.12s average response, no account-level rate or concurrency caps, and 24/7 monitoring (Y06c, opening metrics and Why ScrapeCreators). The same page recommends fewer than 500 concurrent requests.
- **Documented pricing:** ScrapeCreators lists $47 for 25,000 credits and $497 for 500,000 credits; the endpoint normally charges one credit, with the stated free exceptions (Y06c, Pricing; Y06d, Query Parameters).

## Compared with the deep research report

Comparison is limited to Y00's “What about Apify and ScrapeCreators?” section.

- **Right:** Y00 says “approximately $1 per 1,000 successfully extracted transcripts” Y06b's Free event rate is “$1.00 / 1,000”. Y00 correctly distinguishes competing Actors and avoids claiming that all have this rate.
- **Right:** Y00 says the “$47 pay-as-you-go package includes 25,000 credits”. Y06c's Freelance plan lists those figures and “Credits never expire”. Y06d establishes that one live returned transcript uses one credit.
- **Sound caution:** Y00 says to test “extraction success rates on your actual workload.” Y06b has zero reviews, and Y06c's “Success rate” metric is not transcript-specific. The captures support the need for testing, not a reliability ranking.
- **Too broad if used as route guidance:** Y00 suggests inexpensive Apify Actors for one-off transcripts. Y06b's “Actor Start” event and paid plan requirements qualify the cheapest advertised rate. No direct factual error is established, but the report leaves pricing conflicts unresolved.
- **Left out:** Y00's general comparison omits output schemas, Hypebridge's status model and language caveat, and ScrapeCreators' language precedence, null outcomes, and cache control. Y06d explicitly says “a returned transcript costs the usual 1 credit” and documents cache responses at “0 credits”. Those details affect cost and source-language correctness.

## Fit for the user's agent workspace

- (inference) Wrap one documented route in a bounded extraction procedure with explicit video inputs and recorded provider settings.
- (inference) Preserve timed segments for later source quotes. Convert timestamp units carefully: Hypebridge uses numeric seconds; ScrapeCreators samples use millisecond strings.
- (inference) Record null/status outcomes separately from worker failure. Missing captions can be an expected extraction result.
- (inference) Prefer explicit language rules for multilingual research. Hypebridge's market-based automatic choice is not evidence of original speech language.
- (inference) Record credit charge, cache provenance, plan, and run overhead when evaluating cost. Per-event headline prices are insufficient.
- (inference) Test actual videos before adopting either route. Track usable-text completeness and language correctness as well as HTTP or run success.
- (inference) Treat MCP, CLI, and skill links as later setup reading. Their existence does not establish a ready-to-run YouTube procedure in these captures.

## Best parts to read or watch first

Estimated reading times, not vendor-provided durations:

- Y06d, Query Parameters and rendered 200 response: 3–4 minutes. Best explanation of language selection, null results, costs, and time fields.
- Y06b, How to scrape YouTube transcripts, Input tab/schema, and Sample Output: 4–5 minutes. Gives the concrete batch procedure and controls.
- Y06b, Pricing Breakdown and captured Pricing tab: 2 minutes. Read both to see the conflicting plan descriptions.
- Y06c, Pricing, Cache, and No rate limits: 2–3 minutes. Separates credit packages from operating recommendations.
- Y06a, Easily connect with your AI agents: 1 minute. Shows the MCP configuration and quickstart fetch command, without transcript-specific setup.
