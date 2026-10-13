---
created_at: 2026-10-13
updated_at: 2026-10-13
model: gpt-6.1-sol (high)
doc_type: spec
purpose: A shared YouTube transcript and visual-evidence capability for research agents across all harnesses.
related:
  - path: ./AGENTS.md
    why: Layout, source preservation and refresh rules.
  - path: ./STATE.md
    why: Current tests, proposals, blockers and next steps.
  - path: ./DECISIONS.md
    why: The choices the user actually made.
  - path: ./SOURCES.md
    why: Evidence ledger, capture limits and weak claims.
  - path: ../web-scraping-site-access/spec.md
    why: Sibling capability for reading public web platforms.
---

# YouTube extraction

Get a faithful transcript, and inspect visuals when speech alone misses the evidence, so Claude Code, Codex, OpenCode, Hermes and Gemini research agents can read and cite a video. The short answer on 13 October 2026: use a shared cache and paced `youtube-transcript-api` requests, then Firecrawl when local access is blocked. Keep `yt-dlp` for metadata, media and a conditional caption retry. Our home IP began returning blocks within about 10 to 15 minutes and about 20 requests across three batches. Firecrawl still returned five transcripts, but without timestamps. No portable implementation or paid fallback has been selected. The chain below is a proposal based on those tests.

## Start Here

- **Status:** [STATE.md](STATE.md), what works now and what remains open.
- **Brief:** Y00, the original request and candidate routes.
- **Decisions:** [DECISIONS.md](DECISIONS.md), scope and evidence layout.
- **Verify:** [T01 results](tests/2026-10-13-transcript-method-bakeoff.md), the local route test; [Gemini CLI test](tests/2026-10-13-gemini-cli-video-test.md), one visual clip.
- **Sources:** [SOURCES.md](SOURCES.md), captures, digests and trust limits.

## What the capability does

Given one YouTube URL or ID, retrieve available captions before generating speech text. Preserve the original words and timing. Return an inspectable JSON record and readable Markdown. Record metadata separately from spoken content. Add a visual pass only when slides, code, charts or demonstrations matter to the research question. Extraction and later summarization are separate operations.

The final record has four outcomes. A usable transcript can still have unknown completeness or lack timestamps; those are explicit quality fields.

| Outcome | Meaning | Next step |
|---|---|---|
| `transcript_ok` | Actual spoken text was returned and passed content checks. | Save it, assess completeness and caption type, then read the relevant passages. Add visuals if needed. |
| `no_captions` | Caption inventory or a specific error confirms no suitable captions. | Check other available languages. If none fit, obtain audio and transcribe only if the video warrants it. |
| `blocked` | No usable transcript could be retrieved. A reason code distinguishes IP blocks, rate limits, page-only output, setup faults and temporary errors. | Fix setup or wait for a transient failure. For an IP block, stop local caption attempts and use a non-local route. |
| `video_unavailable` | Evidence identifies deletion, privacy or another access restriction. | Stop unchanged retries. Record the restriction and seek another public source. |

An empty body, HTTP 200 or exit code zero proves none of these on its own. A missing requested language is not proof that every caption track is absent. An IP-block error is not proof that a video is unavailable. T01 observed exit-zero errors and successful watch-page scrapes without transcripts. Its no-captions case was an instrumental music video, not a spoken-video transcription test.

## Evidence levels

- **Observed (O):** a dated run on this machine. It proves only the recorded result and conditions.
- **Documented (D):** an interface, limit or price in a captured project or vendor document. It has not necessarily worked here.
- **Claimed (C):** marketing, author opinion, a community report or an unmeasured assessment. Attribution matters.
- **Proposal (P):** our recommended use or design, inferred from the evidence. It is not a user decision.

All route-table statements carry these labels. Prices and limits are capture-time facts from **2026-10-13**, not live quotes. Tests outrank the report and vendor reliability claims. The [ledger](SOURCES.md) owns the full source list.

## The block timeline

The coordinating root supplied these batch finish times, local clock on 2026-10-13. Capture `methods_tried` fields and T01 supply the individual run measurements.

| Batch | Finished | Result and evidence |
|---|---|---|
| E03, one video | 09:05 | **O:** `youtube-transcript-api` returned 2,861 auto-caption fragments in 2.533 seconds. `yt-dlp` eventually wrote original and translated English VTT in 11.084 seconds. Firecrawl returned page text, not a transcript. E03. |
| V01, seven YouTube videos | 09:09 | **O:** all seven transcripts worked through `youtube-transcript-api`, 0.98 to 1.27 seconds each. Track-list and metadata requests also worked. E16a to E16g are linked in [SOURCES.md](SOURCES.md#tests-run-here). |
| T01, nine videos across routes | 09:15 | **O:** transcript API: two transcripts, six IP-block errors, one no-captions result. `yt-dlp`: no subtitle files; eight captioned videos returned HTTP 429, and the ninth had no captions. Firecrawl: five untimed transcripts, two page-only responses, two service 429s. Metadata worked for all nine. [T01](tests/2026-10-13-transcript-method-bakeoff.md). |

**O, root chronology:** the same home IP went from working to blocked within about 10 to 15 minutes and about 20 requests. That is the corrected estimate, not the earlier rough estimate of an hour. **P, interpretation:** modest bursts can exhaust local access. This is not a measured safe-request threshold. It does not prove that the final nine-video batch alone caused the block. T01's first transcript request was already blocked at 09:09:23, and two later requests still succeeded. E03 and V01 also made track-list, metadata and other calls, so exact request accounting is incomplete.

**We do not yet know how long the block lasts.** Retest after several quiet hours. The implementation needs a shared cache, rate limiting and a non-local fallback. All harnesses on the same IP must share that request budget. Firecrawl worked while local caption routes were blocked. Its separate service limit also needs backoff: T01 saw account counters of 11 and 12 requests/minute, with retry delays of 14 and 13 seconds. Those counters include traffic the worker could not attribute to its own batch.

The initial shorthand that E03's routes all worked means successful calls, metadata and local captions. It does not mean Firecrawl returned a transcript. Likewise, T01 did not observe nine subtitle 429s: it observed eight, plus a confirmed no-captions video.

## Route table

| Route | What it returns | Setup | Cost | Tested here? | Known failure modes | Best use |
|---|---|---|---|---|---|---|
| [youtube-transcript-api](digests/Y01-youtube-transcript-api.md) | **D:** existing caption segments with text, start/duration seconds; API exposes language and generated status. **O:** CLI timed JSON. | **D:** Python package; `YouTubeTranscriptApi().fetch(ID)` or CLI. No browser/key for direct use. | **D:** open-source local route; no service fee stated. Proxy and runtime costs extra, unpriced here. | **O:** E03 and V01 success; T01 2/9 transcripts, six IP blocks, one no-captions result. | **O:** CLI errors in stdout with exit 0. **D:** missing tracks, cloud/high-volume IP blocks, undocumented interface changes; cookie authentication currently unavailable. | **P:** first paced caption request on a healthy IP; preserve API track metadata. |
| [yt-dlp](digests/Y02-yt-dlp.md) | **D:** subtitles, metadata, audio/video; section downloads. **O:** E03 VTT, T01 metadata, Gemini test clip. | **D:** install package/executable; supported JS runtime plus compatible EJS challenge scripts for full YouTube support. Media conversion/sections need ffmpeg; audio extraction also needs ffprobe. | **D:** local open-source route; no service fee stated. Compute/bandwidth unpriced. | **O:** T01 metadata 9/9; subtitles 0/9. E03 VTT succeeded earlier. | **O:** eight caption HTTP 429s; runtime/impersonation warnings. **D:** simulation prevents file writes; upstream, token and access constraints. **O:** runtime override was not tested. | **P:** metadata and media; conditional caption fallback for a route-specific failure, not repeated IP-block retries. |
| [Firecrawl](digests/Y05-firecrawl.md) | **O:** five plain transcripts without cue times; also page-only Markdown and one audio URL. **D:** audio/video signed URLs. | **D:** hosted REST/SDK with configured access. **C:** glossary CLI/plugin transcript recipe. **O:** REST v2 used here. | **D:** base scrape 1 credit; audio/video each 5 credits/page. **O:** T01 response metadata reported these charges. Subscription total not measured. | **O:** T01 five transcripts, two page-only, two 429; audio URL 1/1. | **O:** cached watch pages masqueraded as success; service rate limits. **D:** default two-day cache, media URL expiry one hour. Full transcript timing/coverage unproved. | **P:** first existing non-local fallback; validate spoken text and record missing timestamps. |
| [Supadata](digests/Y03-supadata.md) | **D:** timed JSON chunks in milliseconds or text; native captions, generated speech text, asynchronous jobs. | **D:** signup/key; `/v1/transcript`, `x-api-key`; `mode=native`, `auto` or `generate`. | **D:** 100 free credits/month; native 1 credit, generation 2/minute. Basic $5/month billed $60/year; Pro $17/3,000 credits/month. | **D:** captured docs only. **C:** dependability claims, no local run. | **D:** default `auto` can incur generation charges; charged unavailable/native responses, no-speech and timeout charges; job expiry; public completed-media restrictions. | **P:** benchmark as a dedicated fallback, with native mode first and explicit generation budget. |
| [TranscriptAPI](digests/Y04-transcriptapi.md) | **D:** caption JSON with start/duration seconds, text option, optional metadata; discovery endpoints. No captured audio-transcription route. | **D:** signup/Bearer key; `/api/v2/youtube/transcript`; MCP and skill options documented separately. | **D:** 100 trial credits; $5/month for 1,000; 1/success including provider cache hits; annual $54/year. Top-up conditions apply. | **D:** captured docs only. **C:** never-blocked and speed/volume claims. | **D:** `no_captions`, `video_unavailable`, language errors; bot/network 408, service 429, credit exhaustion. | **P:** benchmark when timed captions are needed and local extraction is blocked. |
| [Apify Actors](digests/Y06-apify-scrapecreators.md) | **D:** Hypebridge dataset records, status, optional full text and timed segments. **C:** other Actors advertise other capabilities. | **D:** Apify account; choose an Actor, supply IDs/URLs, limit items and concurrency; export dataset. | **D:** Hypebridge Free event $1/1,000 successful transcripts plus start event. Captured README and pricing tab disagree on paid plans/start units. | **D:** listing/schema only; no YouTube Actor run here. | **D:** `no_transcript`, unavailable/invalid IDs, language preference not guaranteed; schema naming conflicts. **C:** platform uptime is not Actor reliability. | **P:** separately test a chosen Actor for bounded batches; do not transfer one Actor's price or features to all. |
| [ScrapeCreators](digests/Y06-apify-scrapecreators.md) | **D:** JSON caption text and segments with millisecond strings; language and cache/credit fields. | **D:** signup/key; GET `/v1/youtube/video/transcript`; `x-api-key`, URL; optional language/original-audio/cache controls. | **D:** $47/25,000 credits; live transcript 1 credit, eligible cache hits 0; 100 initial credits. | **D:** partial docs only. **C:** general 98.2% success claim, not transcript-specific. | **D:** language/original-audio mismatch can return null; alternate error tabs missing from capture. Bot/access recovery unknown. | **P:** candidate when the broader social API is useful; test before selecting. |
| [Gemini API video input](digests/Y07-gemini-video-understanding.md) | **D:** generated audio/visual answers from public YouTube URLs or local video uploads; static or selective inspection. No validated verbatim export. | **D:** Google API client/key; video URI plus prompt. Files API for downloaded media. | **D + calculation:** captured Gemini 3.8 Flash 2026 Standard input rates imply about $0.27/low-resolution hour or $0.81/high-resolution hour; prompt, answer and thinking cost extra. | **D:** official examples only; direct API route not tested here. | **D:** direct URL excludes private/unlisted videos; sampling misses fast events; timeouts and lost follow-up context. Inline-size guidance conflicts. | **P:** targeted visual pass with measured tokens and timestamps; keep interpretations apart from captions. |
| [Gemini CLI](tests/2026-10-13-gemini-cli-video-test.md) | **O:** bounded local video inspected with frames and audio; URL web fetch returned HTML bootstrap. | **O:** `agy` run downloaded 09:56 to 16:51 via `yt-dlp`, then used `view_file` on a 15.18 MB WebM clip. | **O:** about eight minutes reported; no token use or monetary cost recorded. | **O:** one worker-written test record; frame accuracy not independently scored. **C:** stated 100 MB tool limit was not tested. | **O:** direct page fetch supplied no frames; captions blocked/429 while clip download worked. Full-video limits and download reliability unknown. | **P:** visual inspection of an acquired clip. This does not prove direct YouTube API input works in the CLI. |
| [Whisper-style local transcription](digests/Y10-hacker-news-threads.md) | **C:** new speech text from audio; variants mention timing/speaker features. No shared output schema validated here. | **C:** obtain audio, model weights and a local runner such as faster-whisper or whisper.cpp; hardware/settings vary. | **C:** no hosted API fee for local runs; compute, model download and wall time unmeasured here. Historical hosted prices are separate. | **C:** community reports only; no local speech-transcription test. | **C:** names/numbers, silence hallucinations, slow models; audio acquisition can still be blocked. Speed/silence edits risk timing accuracy. | **P:** missing-caption recovery after obtaining playable audio; test technical-word accuracy and timing. |
| [youtube-mcp-cli](digests/Y11-hermes-skill-agent-reach-youtube-mcp-cli.md) | **D:** plain/timestamped text and saved Markdown, caption search, metadata JSON, media downloads. Transcript JSON not documented. | **D:** Node >=18; `npx @umbertotancorre/youtube-cli transcript ID`; MCP alternative. **C:** automatic bundled media dependencies. | **D:** MIT/local, no API key stated; operating cost unpriced. | **D:** README only; no local run. **D, capture:** 33 GitHub stars and no stable release published at capture. | **D:** public content only, no auth/paywall/age-gate bypass. Missing captions, bot blocks and retries not specified. | **P:** optional interface trial; it does not establish an independent escape from local blocking. |
| [YouTube.js / youtubei.js](digests/Y08-adoption-stats-and-youtubejs.md) | **D:** internal YouTube API client. **C, Y00:** transcript candidate; captured README gives no transcript method/schema. | **D:** `npm install youtubei.js@latest`, `Innertube.create`; linked prerequisites not captured. | **D:** MIT; no extraction fee or operating price documented. | **D:** README/release evidence only; no local run. | **D:** internal interface and parser fixes. Specific caption/IP failure behavior not captured. **P:** treat upstream changes as a risk. | **P:** later TypeScript integration only after obtaining an actual transcript recipe and result. |
| [Hermes youtube-content skill](digests/Y11-hermes-skill-agent-reach-youtube-mcp-cli.md) | **D, captured code:** JSON video ID/count/duration/full text, optional timestamped text. Actual `main()` omits language and segment objects shown in its example. | **D:** prepared isolated helper environment, `youtube` extra, activation/import check; Python `fetch_transcript.py`. | **D:** no monetary rate documented; underlying local library and later model use unpriced. | **D:** captured code/skill only; installed readiness not checked. | **D, code:** passes fetch errors through, can emit empty success; no block-aware or audio fallback. Default retry does not search every language. | **P:** reuse its validate-then-transform workflow; adapt output and fallback before sharing it across harnesses. |
| [Agent-Reach](digests/Y11-hermes-skill-agent-reach-youtube-mcp-cli.md) | **D:** toolkit selects tools; no wrapper layer. **C, issue #566:** captions, bounded OpenCLI fallback, then audio transcription. | **D:** repository install and environment setup; doctor checks; issue route adds browser/OpenCLI dependencies and ffmpeg/Groq for audio. | **C:** free-tool claim, possible proxy cost; transcription quotas and actual YouTube cost not established. | **C:** opposing reporter/maintainer tests, not ours. **D:** READMEs captured. | **C:** bot checks, empty HTTP/exit-zero results, Windows path failures. Maintainer reported fixes and a three-attempt OpenCLI cap. | **P:** borrow bounded retries/content validation; a broad toolkit is optional for this narrow capability. |

## Recommended fallback chain

This is **P**, not a deployed workflow or approved purchase.

1. Normalize the URL/ID and check a shared cache for the requested language, caption type and timing quality. Reuse successful evidence across harnesses. Do not replace a timed source with weaker untimed text.
2. If local access is healthy, make one paced `youtube-transcript-api` request. Prefer original-language manual captions when available; keep automatic-caption provenance. Validate returned JSON and non-empty speech text even if exit status is zero.
3. For a route-specific failure with no IP/rate-limit evidence, try correctly configured `yt-dlp` subtitles once. Keep metadata collection separate. Do not combine `--dump-json` simulation with a caption-file test; E03 required a separate write invocation.
4. On IP blocking or local caption 429s, pause local caption work across all harnesses and go to Firecrawl. Require spoken content, not descriptions, chapters, a transcript button or a postprocessor flag. On a cached page-only result, a single fresh `maxAge: 0` probe is a documented option to test, after service backoff. It has not been tested here. Stop if still unusable.
5. If Firecrawl fails, or exact quote timing is required, benchmark a dedicated managed route. Supadata native and TranscriptAPI are the best-documented candidates in this packet, not measured winners. Keep any current spending cap; record actual credits and cost. Selection is open in [STATE.md](STATE.md).
6. For confirmed missing captions, obtain playable audio and use a separately budgeted speech-to-text pass. Firecrawl returned an audio URL for the no-captions video; download and transcription remain untested. `yt-dlp` clip download also worked in the Gemini record despite caption failures, but that is not a general audio-access guarantee.
7. If visuals matter, inspect only the relevant clip or frames. The Gemini CLI clip route has one local record; direct Gemini API video input is documented but untested here. Save the inspected ranges and distinguish visual interpretation from quoted speech.

The portable wrapper should serialize local caption requests, coordinate per-IP and per-provider budgets, cache evidence and stop a batch at the first block. Provider 429s should respect the returned retry delay and a bounded retry count. No safe requests/minute value or local unblock timer has been measured. Set a conservative configurable limit during implementation, then test it; do not label that initial setting safe.

## Output contract

The proposed portable interface writes **JSON + Markdown**, plus preserved raw backend output. JSON is the machine record. Markdown is a readable rendering with the same provenance and limitations. This contract is a requirement for a future implementation, not a description of every route's native output.

| Fields | Rule |
|---|---|
| `schema_version`, `video_id`, `url`, `captured_at` | Version the schema; normalize to a canonical watch URL; use a capture time with timezone. |
| `title`, `channel`, `duration_seconds`, `metadata_source` | Populate only from retrieved metadata. Use null for unknown values. Caption fetching alone does not supply all of these. |
| `outcome`, `reason_code`, `error` | One of the four outcomes above; preserve specific errors and distinguish local IP blocking from provider limits. Never store keys, cookies or signed-URL credentials. |
| `source`, `language`, `requested_languages`, `transcript_type`, `translated_from` | Name the backend and actual track. Type: `manual`, `auto_generated`, `speech_to_text` or `unknown`. Translation is explicit; never infer manual status from a preferred default. |
| `segments`, `full_text` | Segments have `start`, `duration`, `text`, all timing in seconds. Preserve words and fractional times. For untimed text, use an empty segment array and real `full_text`. Never manufacture timings. |
| `quality` | Record `completeness` (`full`, `partial`, `unknown`, `none`), `timestamps_available`, first/last cue start and last cue end, duration comparison, gaps and validation notes. Unknown measurements are null. |
| `methods_tried` | Per attempt: route/version/settings, start time, elapsed seconds, result, exit/HTTP code, warnings, cache status and measured charge. Redact authentication and temporary signed URL parameters. |
| `raw_files`, `markdown_file`, `visuals` | Relative paths to evidence and rendering. Visual records include model/tool, prompt, original-video ranges, clip offset, answer, uncertainty and measured usage when available. |

For example, a validated untimed result may look like this. Placeholders illustrate the schema and are not an extraction result.

```json
{
  "schema_version": 1,
  "video_id": "VIDEO_ID",
  "url": "https://www.youtube.com/watch?v=VIDEO_ID",
  "captured_at": "2026-10-13T09:15:00+01:00",
  "title": null,
  "channel": null,
  "duration_seconds": null,
  "metadata_source": null,
  "outcome": "transcript_ok",
  "reason_code": null,
  "error": null,
  "source": "firecrawl",
  "language": null,
  "requested_languages": ["en"],
  "transcript_type": "unknown",
  "translated_from": null,
  "segments": [],
  "full_text": "Actual returned speech text goes here.",
  "quality": {
    "completeness": "unknown",
    "timestamps_available": false,
    "first_start": null,
    "last_start": null,
    "last_end": null,
    "coverage": null,
    "gaps": null,
    "validation_notes": ["Spoken content present; time coverage not measured."]
  },
  "methods_tried": [],
  "raw_files": [],
  "markdown_file": "VIDEO_ID.md",
  "visuals": []
}
```

Markdown begins with source URL/title, capture date, route, language, caption type, completeness and timing/visual limits. Render timed passages with `[hh:mm:ss]` and a YouTube `t=` link. Keep fractions in JSON. Untimed passages cite a real file heading or passage without an invented moment. Put visual notes and summaries in separate sections and label them as generated analysis.

**Where files go:** for this spec, approved source captures belong in `sources/`, digests in `digests/`, and measurements in `tests/`. Add new capture versions instead of changing old ones. A consuming research spec uses its own approved source layout. General generated research outputs follow [artifact-authoring.md](../../conventions/artifact-authoring.md), under root `artifacts/` or `projects/<repo>/artifacts/`. Do not create an artifact root inside this spec. A disposable shared cache should live outside durable source captures; its configured location and lifetime are still proposals in STATE.md. Private source material follows the companion repository's own guidance.

## Research quality rules

- **Complete?** Confirm speech content and the beginning/end against video duration when known. Inspect large gaps, truncation and suspiciously short text. Last-cue coverage is a useful warning signal, not proof that every word survived. T01's two timed successes reached roughly 99.7% and 100% by last-cue start; no cross-route overlap score was available. Firecrawl time coverage remains unknown.
- **Manual or automatic?** Save selected-track metadata when available. The V01 records identify six automatic captions and one manual track. T01's CLI JSON did not establish which track it chose where both existed. Automatic captions require extra care with technical terms, names and numbers; manual captions are still source text, not a measured accuracy guarantee.
- **Visuals needed?** Ask whether the claim depends on an unspoken slide, graph, code block or demonstration. A transcript may support the spoken argument while leaving that evidence unread. Inspect a bounded visual range and report exactly what was inspected. One clip is not full-video analysis.
- **Timestamps?** Keep source timing units and convert explicitly. Supadata/ScrapeCreators use milliseconds; the Python library and TranscriptAPI use seconds. For a clipped visual pass, add the clip's original-video offset. Do not equate model-generated timestamps with validated caption timing.
- **Faithful text?** Preserve raw output before joining fragments or removing rolling duplicates. Log transformations. Do not silently rewrite claims, technical names, numbers or speaker labels. Keep summaries and prose cleanup apart from the transcript.
- **Citation strength?** Quote retrieved source text with its actual timestamp or passage pointer. Treat generated speech text and visual descriptions as fallible analysis until checked. Metadata-only results support metadata claims, not claims about what the speaker said.
- **Budget?** Record provider mode and usage. A cache hit can still be billed. Supadata defaults to `auto`, which can move from one-credit captions to two-credit/minute generation. Avoid implicit paid generation in the portable contract.

## What the report got wrong or overstated

These corrections concern Y00. Preserve it as the original brief.

| Report statement or omission | Evidence and correction |
|---|---|
| Local extraction for modest workloads, with cloud IPs the main warning | **O:** E03/V01 worked, then our home IP returned six block errors in T01. The corrected root timeline is about 10 to 15 minutes/about 20 requests. Home execution is not a reliability guarantee. |
| Default library → yt-dlp → managed chain | **O:** T01 local caption routes failed together. **P:** skip a routine yt-dlp caption retry once local IP/rate blocking is known; move to a non-local route. Keep yt-dlp's metadata/media roles. |
| Managed-service rankings such as best or excellent | **D/C:** documented interfaces and seller/community claims, no local comparative trials for Supadata, TranscriptAPI, Apify or ScrapeCreators. The report itself says its rankings are not measured success rates. |
| Supadata Basic described as $5/month without commitment detail | **D, Y03b:** billed $60/year, annual-only. **D, Y03c:** default `auto`, charged native-unavailable results, jobs and timeout/no-speech charges also matter. |
| Firecrawl explicitly documents transcript extraction | **C, Y05b:** glossary recipe lacks a timed-caption contract. **O:** T01 confirms actual text on five videos, but no timestamps; two cached watch pages were unusable. Its general scraping coverage benchmark is not a YouTube-caption benchmark. |
| Gemini URL support called preview | **D, Y07:** captured URL section does not establish that status. API video input and CLI local-file inspection are separate routes. No direct Gemini API test was run here. |
| Hermes may need nothing added | **D, Y11a:** environment preparation is required. Captured helper code omits the language/segments fields promised by its introductory example and has no block-aware fallback. Installation readiness was not checked. |
| Audio transcription as the last recovery step | **O:** only an audio URL was returned in T01; download and speech transcription were not tested. **C:** community pipelines need accessible audio first and do not prove immunity to download blocks. |
| Adoption and anecdotal quality imply a reliable choice | **D:** package counts support popularity. **C:** TubeStoevsky's 98 to 99% semantic accuracy has no scoring method in the capture. Neither validates full transcript fidelity here. |

The report correctly separates captions, speech transcription and visuals; suggests a cache and JSON/Markdown; and warns that page text may not contain a complete transcript. Those parts remain useful.

## Open questions

- How long does the local block last, and what paced workload is sustainable across harnesses?
- Would explicit Node/Deno plus compatible EJS change subtitle results, or leave the same HTTP 429? T01 cannot attribute the 429 to its runtime warning.
- Can fresh Firecrawl scrapes recover the two cached page-only results? Does it provide complete original-language text or any usable timing through another documented route?
- Which managed fallback succeeds on our videos, at what actual cost, with what caption provenance and timing?
- Can we download Firecrawl audio and recover accurate, timed technical speech from a no-captions spoken video? The music example cannot answer that.
- How accurate are the Gemini clip's visual details? Does direct Gemini API video input work here, with measured cost and enough coverage for the research question?
- Where should the shared cache live, how should freshness be handled, and what minimal CLI/skill interface will all five harnesses use?
