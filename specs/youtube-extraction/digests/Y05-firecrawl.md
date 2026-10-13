---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [Y05a, Y05b, Y05c, Y05d]
source_files: [sources/Y05a-firecrawl-home.md, sources/Y05b-firecrawl-youtube-transcript-in-claude-code.md, sources/Y05c-firecrawl-mastering-scrape-endpoint.md, sources/Y05d-firecrawl-docs-youtube-or-audio.md]
purpose: One-source digest feeding the spec compendium.
---

# Firecrawl: transcript claims and documented media extraction (Y05)

**What it is:** Four Firecrawl-owned web pages, about 18,673 captured words including navigation, code and footers. Y05a is the [product homepage](https://www.firecrawl.dev/), author and publication date unknown. Y05b is the [Claude Code YouTube transcript glossary entry](https://www.firecrawl.dev/glossary/web-scraping-apis/how-to-extract-youtube-transcript-in-claude-code), author unknown, updated April 6, 2026. Y05c is Bex Tuychiev's [Scrape API tutorial](https://www.firecrawl.dev/blog/mastering-firecrawl-scrape-endpoint), published September 9, 2025 according to metadata, updated May 4, 2026 on the page. Y05d is the [Scrape documentation](https://docs.firecrawl.dev/features/scrape), author and publication date unknown. None gives a reading time.

**Capture status:** All four frontmatters say full, captured October 13, 2026. Y05a-c retain main content, tables, code, final sections and footers, with raw HTML inspected. Their Firecrawl capture attempts failed with HTTP 429, and Exa omitted links and command placeholders; Parallel supplied the successful captures. Y05d was captured successfully through Firecrawl, with Exa and raw HTML verification. Its audio examples and final Zero Data Retention section are retained. Some Y05c code is flattened, and examples contain empty selectors or values. These are limitations of the supplied text despite its full status.

## The point in three sentences

Firecrawl's glossary claims that its CLI and Claude plugin extract YouTube transcripts, but supplies no transcript sample or timestamp guarantee. Its technical docs specify audio and video extraction as temporary downloadable media URLs, with separate transcription needed to turn audio into text. These captures support trying an existing Firecrawl integration, but do not establish reliable, complete, timestamped YouTube caption extraction.

## Key ideas

- **The direct transcript claim comes from a glossary page.** Y05b says the CLI writes Markdown to disk, while the plugin returns content inline. It gives commands, but no resulting transcript, caption source, language selection or timed segment format. Quote: "Two Firecrawl integrations give it YouTube transcript extraction with different trade-offs:" (Y05b, opening).
- **File output is the main agent-workflow benefit.** Workers can read or search selected portions instead of carrying the whole transcript in their context, the text available to the model. Quote: "Claude Code can then read, grep, or summarize the file without loading the full text into the context window." (Y05b, CLI paragraph).
- **Automatic rendering is a vendor claim, not caption reliability evidence.** The glossary promises adaptation to dynamic pages without showing a test. Quote: "Both handle JavaScript rendering and page structure changes automatically." (Y05b, closing paragraph).
- **Audio extraction returns media, not words.** The docs describe MP3 output accessed through a signed URL, a download link with an expiry. Quote: "The `audio` format extracts audio from supported websites (e.g. YouTube) as MP3 files and returns a signed Google Cloud Storage URL." (Y05d, Audio extraction).
- **Video extraction is also documented.** It returns a signed URL for best-quality video, rather than captions or a transcript. The precise container, resolution and selection controls are not specified here. Quote: "Video extraction costs 5 credits per page (1 base + 4 additional)." (Y05d, Video extraction).
- **The blog contradicts itself about audio access.** Its early sections say audio is REST-only, meaning available only through direct HTTP requests. Later it demonstrates Python SDK audio extraction; Y05d explicitly supplies Python, Node and cURL examples. Quote: "Audio extraction is currently REST-only." (Y05c, Ways to use Firecrawl scrape). Preserve this conflict instead of treating the blog restriction as current fact.
- **JSON extraction structures available page content.** A schema, a definition of fields and types, controls the result's shape. It does not prove that full captions were obtained or that inferred values are accurate. Quote: "Schema-locked extraction guarantees the output shape." (Y05c, Prompt with schema).
- **Prompt-only JSON can break downstream code.** The blog shows how names and wrappers may vary between calls. Quote: "Field names and the wrapping structure can drift between runs." (Y05c, Prompt-only).
- **Successful API calls can contain failed page loads.** Check the API response and the target page status separately. Quote: "There are two separate status layers in a scrape response" (Y05d, Response metadata and status codes).
- **Caching changes freshness and speed, not the base charge.** The docs specify a default two-day cache window. The blog calls the cache opt-in while also stating a default, so use the docs' clearer description. Quote: "Firecrawl serves results from cache by default" (Y05d, Caching and maxAge).
- **Browser interaction is a general fallback, with no YouTube recipe.** Actions run before scraping; Interact keeps a browser session alive across calls. The examples concern login, search and shopping, not opening YouTube's transcript panel. Quote: "The `actions` flow is stateless" (Y05c, Using actions to prepare a page before scraping).
- **Open source does not imply the hosted service's capabilities.** The homepage says hosted infrastructure is proprietary. The docs also mention that audio/video depend on their service, in a comparison with product extraction, but give no complete media self-hosting setup. Quote: "Firecrawl's hosted version features Fire-engine, our proprietary infrastructure" (Y05a, FAQ: hosted versus open-source).

## How to do it (concrete steps, checklists, templates)

### Route 1: CLI transcript to a Markdown file

Y05b gives this order:

1. Install with `npx -y firecrawl-cli@latest init --all --browser`.
2. Get a free API key at Firecrawl.
3. Run `firecrawl scrape <YouTube URL>`.
4. Read, search or summarize the resulting Markdown file.

**Output:** File on disk, claimed to contain the transcript. No filename, explicit output-path flag, sample content, timestamps, JSON segment structure, subtitle provenance or language controls are given.

**Cost:** Y05b gives no route-specific charge. Y05c/d specify a 1-credit base scrape, but do not confirm that this transcript path always uses only one ordinary scrape. The calling model's token cost is not quantified.

**Failure modes:** Caption availability, private or restricted videos, long-video truncation, rate limits and region restrictions are not addressed for this route. The glossary gives no fallback sequence when a normal scrape returns only page text.

**Reliability evidence:** A vendor assertion and commands. No successful transcript sample, test set or full-caption comparison. The capture failures show HTTP 429 can occur when capturing ordinary Firecrawl pages, not a measured YouTube failure rate.

The general docs give a different CLI setup: `npm install -g firecrawl`, then `firecrawl login`. Their usage example is `firecrawl https://firecrawl.dev`; multiple formats use `--format markdown,html,links --pretty` and return JSON. The blog instead names `firecrawl-cli`. These captures do not resolve the package or command differences.

### Route 2: Claude plugin, inline transcript or agent-assisted extraction

Y05b gives this order:

1. Install with `claude plugin install firecrawl@claude-plugins-official`.
2. Use `/firecrawl:scrape <URL>` for inline transcript output.
3. For edge cases, use `/firecrawl:agent "Extract the full transcript from [URL]"`.

**Setup:** A free API key is mentioned for both integrations. No plugin-specific authentication instructions are supplied.

**Output:** Inline chat content. No transcript example, timestamp contract or JSON schema. The agent command's exact output structure is absent.

**Cost:** No plugin-specific total is given. Y05a says Agent is in preview, with five free daily runs and dynamic pricing. That does not establish the cost or billing mapping of the plugin's agent command. Ordinary scrape pricing is 1 credit before add-ons.

**Failure modes and reliability:** The source says the agent handles edge cases autonomously, but names no edge cases, recovery actions or measured success rate. Inline content can use thousands of tokens for long videos according to Y05b, without a measured total. No reliability evidence beyond the vendor claim.

### Route 3: Extract audio, then transcribe elsewhere

Y05c's general setup is: sign up, choose a plan, copy the dashboard API token to `.env`, install `firecrawl-py`, `python-dotenv` and `pandas`, then use `load_dotenv()` and create `Firecrawl()`. Y05d's Python and Node examples say no key is needed to start, with a key enabling higher rate limits; they do not give the keyless quota.

The media flow in Y05c/d is:

1. Call `scrape` on the YouTube URL with `formats=["audio"]`, or POST the equivalent JSON to `https://api.firecrawl.dev/v2/scrape`.
2. Read `doc.audio` from the SDK response. The docs say SDKs return the data object directly; direct HTTP calls return the enclosing payload.
3. Save the returned MP3 locally or to storage before the link expires.
4. Send the file to Whisper, Deepgram or another speech-to-text service, as Y05c suggests.
5. Use the resulting transcript for summaries, search or another agent.

**Output:** MP3 download URL, not transcript text. The blog shows a Google Cloud Storage URL with `X-Goog-Expires=3600`; the docs list one-hour expiry. No timestamped transcript JSON, SRT, VTT, speaker labels or speech-to-text response format is specified. Those belong to the separate transcription stage, whose setup is not supplied.

**Cost:** 5 Firecrawl credits per page, plus an unspecified separate transcription cost. No duration-based Firecrawl charge or media length limit is given here.

**Failure modes:** Link expiry is explicit. Only supported sites are promised. The docs' self-hosting comparison says absent media service support can yield warnings and missing media fields, without a full setup guide. They do not list YouTube-specific restriction errors, timeout limits or retry rules for audio.

**Reliability evidence:** Python, Node and HTTP examples in Y05d; one illustrative signed MP3 URL in Y05c. Neither source provides a tested set of videos, download verification, transcript accuracy or long-video coverage.

### Route 4: Extract video for later processing

Y05d gives Python, Node and HTTP examples using the same setup as audio. Request `formats=["video"]`, then read `doc.video`.

**Output:** Signed Google Cloud Storage URL for best-quality video, expiring after one hour according to Scrape Formats. No captions, timestamps, transcript or exact video format is specified.

**Cost:** 5 credits per page. Later video processing costs are absent.

**Failure modes and reliability:** The same documented expiry and media-service dependency apply. Supported websites are not exhaustively listed. Code examples establish the interface, but no sample completed download or YouTube success rate is supplied.

### General interfaces and processing helpers

These are documented tools around extraction, not additional proven YouTube transcript routes:

- **MCP:** The blog says to connect the Firecrawl MCP server to Claude Desktop or Cursor and let the model call `firecrawl_scrape`. MCP is a tool connection for an AI client. Exact server installation, authentication and YouTube output are not supplied. Normal scrape charges apply to the endpoint, but no complete model-plus-tool cost is given.
- **Structured JSON:** Supply a prompt and optional schema inside a `json` format object. Results appear in `json`; total cost is 5 credits for one JSON scrape. Y05c demonstrates Hacker News, and Y05d company information. Neither demonstrates timed YouTube captions. Prompt-only field drift and inferred values are documented risks.
- **Actions / Interact:** For actions, provide an ordered list of click, write and wait steps before scraping. For Interact, scrape first, read the scrape ID, call `interact()` with prompts or code, then `stop_interaction()`. Outputs include page content, action results or interaction output, with no YouTube timestamp contract. Y05c prices Interact at 2 credits/minute for code or 7 for AI prompts, plus the initial scrape, prorated by second. The examples prove only general page interaction; no YouTube panel selectors or successful recovery are shown.
- **Batch:** Supply URLs and formats to `batch_scrape()` for results, or `start_batch_scrape()` for an immediate job ID. Poll with `get_batch_scrape_status()` or `/batch/scrape/{id}`. Inspect completion, data, errors and pagination. Jobs expire after 24 hours. Charges follow the requested formats; no YouTube-specific batch guarantee is given.
- **Alexandria:** Y05d describes third-party tool calls with `provider`, `capability` and `options`, per-tool pricing and per-item errors. It shows podcast search, not a YouTube transcript provider. Do not infer a supported YouTube extraction route from the catalogue's existence.

The docs' response-check order is: confirm API HTTP 200 and `success: true`, then check `data.metadata.statusCode`. They treat target 2xx or 304 as a clean load. Their freshness guidance says to bypass cache with `maxAge: 0` when necessary, then inspect content and source status. This still does not verify transcript completeness.

## Tools, code and commands named

- Firecrawl `/scrape`, `/crawl`, `/search`, `/interact`, `/parse`, `/v2/batch/scrape`, `firecrawl_scrape`, Firecrawl MCP server, CLI and Claude plugin.
- Install commands: `npx -y firecrawl-cli@latest init --all --browser`, `claude plugin install firecrawl@claude-plugins-official`, `npm install -g firecrawl`, `firecrawl login`. Y05c's flattened installation block names `npm install -g firecrawl-cli`.
- SDK packages: `firecrawl-py`, `firecrawl`, `python-dotenv`, `pandas`; schema tools Pydantic `BaseModel`, `Field`, `model_json_schema()` and Zod `z.object`.
- `FIRECRAWL_API_KEY`, `load_dotenv()`, `Firecrawl`, `scrape`, `batch_scrape`, `start_batch_scrape`, `get_batch_scrape_status`, `batchScrape`, `interact`, `stop_interaction`.
- Python/Node Playwright, Bash, agent-browser, Whisper, Deepgram, S3 and Google Cloud Storage. No fixed SDK version is supplied; `@latest` is the only CLI version selector.

## Numbers and strong claims

- **Documented pricing, Y05d Usage and media sections:** Base scrape 1 credit; JSON, question, highlights, audio and video each add 4 credits per page per applicable format. Audio-only and video-only calls cost 5 credits. PDF parsing adds 1 per PDF page. Enterprise Zero Data Retention adds 1 per page; screenshots with that option fail.
- **Homepage billing claims, Y05a FAQ:** 1,000 free credits/month, no card required. A $5 paid-plan top-up buys 1,000 Hobby, 2,000 Standard, 2,500 Growth or 5,000 Scale credits. Subscription prices are absent. No-result scrapes are said to be uncharged; returned 403/404 pages cost 1 credit. These are vendor billing statements, not independently verified charges.
- **Documented expiry and cache:** Media URLs one hour; screenshots 24 hours; batch jobs 24 hours. Default `maxAge` is 172800000 ms, two days. Cache-only misses return 404 `SCRAPE_NO_CACHED_DATA`. Fresh scrapes are described as slower and more likely to fail (Y05d, Caching and maxAge).
- **Marketing benchmark, Y05a Built for Performance:** 96% coverage versus Puppeteer's 79% and cURL's 75% on the vendor's 1,000-URL `firecrawl/scrape-content-dataset-v1`, run January 13, 2026. P95 latency is 3,387 ms, the value at the 95th percentile. No YouTube subset, caption definition or raw test results appear here.
- **Marketing efficiency:** Homepage claims 93% fewer input tokens. Blog claims up to 100x fewer tokens for question output and shows a roughly 35x summary reduction on TechCrunch. These concern page processing, not complete YouTube transcript fidelity.
- **Marketing/opinion:** Y05c calls audio the cheapest entry point to transcription, without a price comparison. Adoption counts and homepage testimonials are not extraction-quality evidence.

## Compared with the deep research report

Comparison is limited to Y00's Firecrawl section, not its other providers.

- **Right:** Y00 says the guide recommends file output for selective reading. Y05b says the CLI produces a "File on disk" and lets Claude read or search it. The command and April 6 update match.
- **Right:** Y00 says audio extraction "retrieves a signed URL for extracted audio". Y05d's audio section specifies MP3 and a signed Google Cloud Storage URL. It is a separate media step before transcription.
- **Right:** Y00 warns that "A tool returning YouTube page text is not necessarily returning the complete transcript." Y05b provides no sample transcript, and Y05d's format list specifies media extraction without a transcript format. Y00's request to validate timestamps and completeness is justified.
- **Overstated source status:** Y00 says "Firecrawl explicitly documents extracting YouTube transcripts through its CLI". This is supported by a vendor glossary claim, not a detailed technical caption contract. Y05b calls the CLI output a transcript; Y05d describes scrape as getting a URL's content. Keep those evidence levels separate.
- **Left out:** The blog says "Audio extraction is currently REST-only" but also shows SDK audio code. Y00 reproduces that Python route without noting the conflict. Y05d supplies explicit SDK support, so the Python example is supported by the docs even though the blog is inconsistent.
- **Left out:** Media cost is 5 credits, URLs expire in one hour, video extraction exists, page-status checks are separate from API success, and CLI setup differs across captures. Y00's convenience assessment is an opinion, not evidence of reliability.

## Fit for the user's agent workspace

- (inference) Trial the CLI file route with existing access, but require content checks before declaring a transcript complete.
- (inference) Keep raw captions or transcripts on disk and give small workers only the passages they need. Preserve source URLs and any actual timing data alongside summaries.
- (inference) Record direct transcript extraction and audio-plus-transcription as separate routes. They have different costs and outputs.
- (inference) Test caption completeness, timestamps, languages, restricted videos and long videos explicitly. These captures leave all those questions open.
- (inference) Use a schema for repeatable JSON records, but never let requested timestamp fields substitute for evidence that timing data exists.
- (inference) Track missing media fields, warnings, page status, credit usage and URL expiry. API success alone is insufficient.
- (inference) Treat the CLI package differences and blog REST-only contradiction as setup checks. Skip assumptions that a self-hosted clone reproduces hosted media extraction.

## Best parts to read or watch first

Reading estimates below are inference, not times supplied by the sources.

- Y05b, entire main entry from its title to the update date: about 2 minutes. It contains both direct transcript commands and the file-versus-chat choice.
- Y05d, Audio extraction, Video extraction and the corresponding Scrape Formats entries: about 3 minutes. These define the actual media outputs, prices and expiry.
- Y05d, Response metadata and status codes, then Caching and maxAge: about 4 minutes. Read before designing success checks.
- Y05c, Audio extraction with the audio format, plus Ways to use Firecrawl scrape: about 3 minutes. Compare the SDK example with the REST-only statement.
- Y05a, billing FAQ and Built for Performance: about 3 minutes. Separate cost claims and general benchmarks from YouTube evidence.
