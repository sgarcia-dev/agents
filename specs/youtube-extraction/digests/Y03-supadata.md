---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [Y03a, Y03b, Y03c]
source_files: [sources/Y03a-supadata-home.md, sources/Y03b-supadata-pricing.md, sources/Y03c-supadata-transcript-api-docs.md]
purpose: One-source digest feeding the spec compendium.
---

# Supadata homepage, pricing and transcript API (Y03)

**What it is:** Three vendor pages: [homepage](https://supadata.ai/), [pricing](https://supadata.ai/pricing), and [transcript documentation](https://docs.supadata.ai/get-transcript). The homepage and pricing name Dumpling Software as author; the documentation author is unknown. Publication dates are unknown. All were captured on 2026-10-13. These are product copy, pricing tables and API instructions, about 10 to 15 minutes of reading combined (estimate).

**Capture status:** All three captures are marked full. Main-content extraction excluded navigation and footers. Capture notes say each was compared with raw HTML and its final content section was present. Pricing retains all seven plans and table columns. Documentation retains all code tabs and three tables. Its first capture attempt received HTTP 429 Too Many Requests; a retry succeeded. That is a documentation-fetch event, not evidence of transcript API failure. Linked error, integration, batch and translation pages are not included.

## The point in three sentences

Supadata provides one authenticated HTTP endpoint for existing captions and AI-generated transcripts across YouTube and several other platforms. Existing captions cost one credit, while generated transcripts cost two credits per video minute, and the default mode can silently move a request into that more expensive route. The captures document useful formats and operational limits, but offer no measured extraction success rate or independent, dated user reports.

## Key ideas

- The service covers captions supplied by people or generated automatically, with generation as a fallback. Quote: "AI-generated fallback when none exist" (Y03a, What's in the Box? → Video Transcripts).
- The interface uses a shared key and format across platforms. Quote: "One API key, one response format." (Y03a, Video transcript and metadata APIs).
- Existing-caption extraction can be selected explicitly to avoid AI charges. Quote: "To fetch only existing transcripts and avoid costs tied to AI generation, use" followed by `mode=native` (Y03c, Query Parameters).
- The default route tries captions and then generates a transcript when unavailable. Quote: "Default: `auto`." (Y03c, Query Parameters, mode row). File URLs always use generation.
- Plain text is optional. The default returns transcript chunks with start times and durations in milliseconds. Quote: "Default: false" (Y03c, Query Parameters, text row).
- Processing can return a job identifier rather than a finished transcript. Quote: "The API can return either a transcript result directly (HTTP 200) or a job ID for asynchronous processing (HTTP 202)." (Y03c, Response Format).
- Empty output does not necessarily indicate failure. Quote: "Such requests are still charged according to the media duration." (Y03c, Response Format, no-speech paragraph).
- Access restrictions are explicit. Quote: "Only publicly accessible videos can be transcribed." (Y03c, Video Accessibility). Login, membership, privacy, age verification and heavy geographic restrictions can prevent access.
- Ongoing streams are excluded. Quote: "Only complete media can be transcribed." (Y03c, Live Streams).
- A requested language is a preference, not a guarantee. Quote: "When `mode = generate`, the `lang` parameter is ignored and the transcript is generated in the language of the video." (Y03c, Languages).
- A client timeout does not cancel the charge. Quote: "if your app times out before receiving a response, the request will still count towards your credit usage." (Y03c, AI Transcription Time).
- Monthly credits expire rather than accumulate. Quote: "No, credits do not roll over to the next month." (Y03b, Frequently Asked Questions → Do credits roll over to the next month?).

## How to do it (concrete steps, checklists, templates)

### Shared setup and request flow

1. Sign up and obtain an API key from the dashboard. The homepage offers a no-signup demonstration, but authenticated API use requires signup.
2. For restricted-looking videos, try an incognito/private browser window without signing in. The documentation proposes this as an accessibility check.
3. Send `GET https://api.supadata.ai/v1/transcript` with an `x-api-key` header and a required `url` query parameter. The docs recommend encoding the video URL.
4. Choose optional `lang`, `text`, `chunkSize` and `mode`. `chunkSize` sets the maximum characters per chunk only when `text=false`.
5. Handle either HTTP 200 transcript data or HTTP 202 containing `jobId`.
6. For a job, request `/v1/transcript/{jobId}` until `completed` or `failed`. The recommended interval is one second. Store results within one hour of completion; later retrieval returns `404 Not Found`.
7. Check credit usage through dashboard history or the `x-billable-requests` response header. For HTTP 202, the header is an estimate that is reconciled on completion. Polling reports zero and has no credit charge.

The captured cURL request is:

```bash
curl -X GET 'https://api.supadata.ai/v1/transcript?url=https://youtu.be/dQw4w9WgXcQ' \
  -H 'x-api-key: YOUR_API_KEY'
```

This example inherits `mode=auto`; it is not a caption-only request.

### Extraction routes and their limits

| Route | Setup after shared steps | Cost | Output | Failures and reliability evidence |
| --- | --- | --- | --- | --- |
| Existing captions | Set `mode=native`; supply a public video URL. | 1 credit per native transcript. A 206 Transcript Unavailable response also costs 1 credit. | JSON with timestamped chunks by default, or a text string inside JSON with `text=true`; language fields included. | Missing captions cannot fall back to generation in this mode. Access restrictions and live streams apply. No success-rate measurement, IP-block handling or bot-check procedure is supplied. |
| Captions with AI fallback | Set `mode=auto`, or omit mode. | Existing transcript: 1 credit. Missing-caption generation: 2 credits per video minute. | Same transcript formats, potentially preceded by a JSON job identifier. | Missing captions trigger generation rather than making the request cheap. Access restrictions still apply. The vendor documents fallback behavior but supplies no measured recovery rate. |
| Forced AI transcription | Set `mode=generate` for a public platform video. | 2 credits per video minute. No speech still incurs duration-based charges. | JSON text or timestamped chunks, immediately or through an asynchronous job. Generation uses the video's language. | Videos over 20 minutes automatically use jobs. Even shorter platform requests can switch to a job while processing. Generation may take about 100 seconds before returning a job or result. No accuracy benchmark or bot/IP guarantee is supplied. |
| Public audio/video file | Supply a publicly accessible file URL. Mode is always `generate`. The capture gives no upload procedure. | 2 credits per generated minute. | Same JSON formats and possible job flow. | Maximum 750 MB and 12 hours; exceeding either returns `invalid-request`. Platform requests' in-flight switch to jobs does not apply to file URLs. File-specific success rates are absent. |
| Batch transcripts | Pro or above; `/v1/youtube/transcript/batch` is named. Request setup is not captured. | Pricing lists 1 credit per batch video. Generation billing within batches is not explained. | Not captured. | Batch error behavior, timestamps, response schema and reliability are not captured. |
| Transcript translation | Pro or above; `/v1/youtube/transcript/translate` is named. This is an additional language route, not a documented substitute for extraction. | 30 credits per transcript minute. | Not captured. | Setup, supported languages, errors and reliability are not captured. |

For the first four routes, restricted videos can return `404 Not Found` for nonexistent/private content or `403 Forbidden` for authentication/restriction. Job status can be `queued`, `active`, `completed` or `failed`; failed jobs contain error details. A linked error catalogue is outside these captures. No retry policy for transcript failures, IP blocks, CAPTCHA or other bot checks is provided.

### Output contract and a documentation inconsistency

With `text=true`, JSON has `content` as a string, `lang`, and `availableLangs`. With `text=false`, `content` is an array of objects containing `text`, `offset`, `duration` and `lang`. Both timing fields are milliseconds. No SRT or VTT subtitle-file output is documented here.

The job REST example and prose place `content`, `lang` and `availableLangs` directly on the completed response. The SDK examples access `jobResult.result` in JavaScript and `job.result.content` in Python. The capture does not reconcile these different shapes. The Quick Start response also shows a text string even though the bare cURL request omits `text=true`, while the parameter table says the default is false.

## Tools, code and commands named

- JavaScript/TypeScript: `@supadata/js`, `Supadata`, `supadata.transcript(...)`, `supadata.transcript.getJobStatus(...)`. The job-result example requires `@supadata/js >= 1.5.0`.
- Python: `supadata`, `Supadata`, `SupadataError`, `supadata.transcript(...)`, `supadata.transcript.get_job_status(...)`. Job polling requires `supadata >= 1.7.0`.
- HTTP: `curl -X GET`, `x-api-key`, `x-billable-requests`, `/v1/transcript`, `/v1/transcript/{jobId}`.
- Named integrations: TypeScript SDK, Python SDK, Model Context Protocol, n8n, Zapier, Make, ActivePieces. No installation or configuration commands are captured.
- Related endpoints: `/v1/web/crawl`, `/v1/youtube/video/batch`, `/v1/youtube/transcript/batch`, `/v1/youtube/transcript/translate`. Documentation discovery: `/llms.txt`.
- File formats: MP4, WEBM, MP3, FLAC, MPEG, MPGA, M4A, OGG, WAV.

## Numbers and strong claims

Pricing below is from Y03b, plan table and cards. Prices are USD before taxes. Basic is annual-only; the other paid plans also offer discounted yearly variants.

| Plan | Credits/month | Listed price | Requests/second | Auto Recharge |
| --- | ---: | --- | ---: | --- |
| Free | 100 | Free | 1 | N/A |
| Basic | 300 | $5/month, billed $60/year | 10 | $10 per 1,000 credits |
| Pro | 3,000 | $17/month | 10 | $10 per 1,000 credits |
| Mega | 30,000 | $47/month | 50 | $10 per 5,000 credits |
| Giga | 300,000 | $297/month | 100 | $20 per 20,000 credits |
| Supa | 1,000,000 | $897/month | 100 | $20 per 20,000 credits |
| Enterprise | Any | Custom; table says `$Best` | TBD | TBD |

- Y03b, Auto Recharge: reaching the plan limit stops requests until upgrade or Auto Recharge. Paid plans can enable automatic credit purchases.
- Y03b, Credit usage: extraction is 5 credits per minute, minimum 5. This is a separate listed charge; the captured transcript documentation does not describe that extraction endpoint.
- Y03c, Pricing: native transcripts cost 1 credit; generated transcripts cost 2 credits/minute. A 60-minute generated transcript therefore uses 120 credits (calculation), exceeding the Free plan's monthly allowance.
- Y03c, Polling Guidelines and AI Transcription Time: one-second polling, one-hour result retention, automatic jobs above 20 minutes and generation latency up to about 100 seconds.
- Y03a, Get Started/closing call to action: "Get Started in 2 Minutes" and "Get your API key in 30 seconds." These are marketing timing claims, not measured setup evidence.
- Y03a, FAQ → What about rate limits?: "We handle the traffic intelligently to ensure your requests succeed without overwhelming source servers." This is a vendor claim without a method, success rate or explicit IP-block guarantee.

The only user-style reports are vendor-published testimonials under Y03a, Trusted by Makers Who Ship:

- Sarah Chen, AI Maker, date not supplied: “Finally, an API that just works without the BS.”
- Mark T., Solopreneur, date not supplied: “Saved me weeks of development time.”

Neither gives tested videos, scale, failure counts or a verification link. There are no independent, dated user reports in these captures. Homepage customer logos do not establish extraction reliability.

## Compared with the deep research report

Comparison is limited to the Supadata references and Option C in Y00.

- **Right:** Y00's endpoint and API-key header match Y03c. Its statement "It returns structured transcript data with timestamps." agrees with Y03c's default chunk output, including "Start time in milliseconds" in Response Format.
- **Right:** Y00 says "AI-generated transcripts cost two credits per video minute." Y03c states "1 generated transcript minute = 2 credits" (Pricing). Its 60-minute/120-credit example is consistent.
- **Incomplete pricing:** Y00 lists Basic as $5 in a monthly-allowance table. Y03b specifies "$5/mo billed annually ($60/year)". The annual-only commitment matters. Y00 also omits larger plans, request rates, recharge and paid-only batch/translation access.
- **Reliability not demonstrated:** Y00 calls managed APIs "a more dependable service" and ranks Supadata "Best managed all-rounder". Y03a offers only broad claims such as "Reliable" and undated testimonials. These captures cannot substantiate comparative dependability or avoidance of proxy maintenance. Y00 does qualify its rankings as recommendations rather than measured success rates.
- **Important omissions:** Y00 says Supadata supports transcription when captions are absent, but omits that `auto` is the default. Y03c says "Default: `auto`." It also omits charged 206 responses, asynchronous processing, retention expiry, timeout charges, no-speech charges, restrictions and language fallback.
- **Evidence outside scope:** Y00 cites a maintainer discussion about proxies and hosted services. That discussion is not among the three supplied captures, so its attribution and claims cannot be checked here.

## Fit for the user's agent workspace

- (inference) Use the HTTP endpoint behind one shared capability so each harness uses the same transcript contract.
- (inference) Default that capability to `native` when predictable spending matters. Make generation an explicit choice with a duration-based budget.
- (inference) Preserve timestamped JSON for source citations; derive readable text separately.
- (inference) Handle both direct results and jobs, and save completed results before the one-hour expiry.
- (inference) Record selected mode, returned language and billed credits alongside the result so worker evaluations can compare quality and cost.
- (inference) Verify the REST and SDK response shapes before implementing a TypeScript wrapper because the captured examples differ.
- (inference) Evaluate on representative videos before selecting this as a reliable fallback. These pages describe behavior but do not measure reliability.

## Best parts to read or watch first

- Y03c, Query Parameters and Pricing: 2 minutes (estimate). Explains mode choice and the main cost trap.
- Y03c, Response Format, Getting Job Results and Polling Guidelines: 3 minutes (estimate). Covers timestamps, jobs, charged empty output and expiry.
- Y03c, Video Accessibility, Live Streams, Languages and Latency: 2 minutes (estimate). Covers eligibility, language surprises and timeouts.
- Y03b, plan table, Auto Recharge and Advanced endpoints: 2 minutes (estimate). Covers annual billing, capacity and batch access.
