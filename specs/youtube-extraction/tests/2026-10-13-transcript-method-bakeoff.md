---
created_at: 2026-10-13
model: gpt-6
doc_type: test_result
purpose: Measure transcript extraction routes on nine real YouTube videos from a home Mac.
related:
  - path: ./2026-10-13-transcript-method-bakeoff.json
    why: Per-run commands, errors, durations, metadata and measurements.
---

# YouTube transcript method bake-off

## Setup

Ran on macOS-26.6.2-arm64-arm-64bit. Python 3.11.12. The operator identified this as a home Mac. No network address or IP classification was independently checked.

Tool versions, captured with `--version`:

- uv: `uvx 0.12.15 (d35f1f270 2026-09-15 aarch64-apple-darwin)`.
- ytdlp: `2026.08.19`.
- yta: `youtube_transcript_api, version 1.2.4`.
- node: `v26.9.0`.
- Firecrawl: REST `POST https://api.firecrawl.dev/v2/scrape`. No local CLI was used, so there is no `--version` result. The hosted server did not expose a software version.

The Firecrawl key came from `FIRECRAWL_API_KEY` and was never printed. No brew install, agent, other AI CLI or git command was run. Scripts and unmodified responses are in the assigned T01 raw folder, whose absolute path is in the JSON. The two requested result files are the only workspace writes.

Commands:

```text
uvx --from youtube-transcript-api youtube_transcript_api <ID> --format json
uvx yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs en.* --sub-format vtt -o <raw-subtitle-directory>/%(id)s.%(ext)s <URL>
POST /v2/scrape {"url": "<URL>", "formats": ["markdown"]}
POST /v2/scrape {"url": "<short-video-URL>", "formats": ["audio"]}
uvx yt-dlp --dump-json --skip-download <URL>
```

Within each route the nine videos ran serially without a deliberate delay. Metadata ran while the markdown batch was finishing to select the shortest video for audio. No retry, cookies, proxy, runtime override or package upgrade was used.

Wall times include process startup. No run hit the local 120-second timeout. A transcript counts as success only when text was returned. HTTP 200 and exit code 0 alone do not count. No audio was downloaded or transcribed.

## Results

| Video | API transcript | yt-dlp subtitles | Firecrawl markdown | Metadata |
|---|---|---|---|---|
| BsWxPI9UM4c | IP blocked / 1.526s | 429 / 2.210s | page only / 0.935s | OK / 2.138s |
| h9oAAAYnGx4 | transcript / 0.943s | 429 / 1.542s | untimed text / 8.455s | OK / 1.127s |
| AKg27L4E0M8 | IP blocked / 1.039s | 429 / 1.838s | untimed text / 5.877s | OK / 1.294s |
| 1d5aNfslwHg | IP blocked / 1.218s | 429 / 1.547s | untimed text / 8.818s | OK / 1.254s |
| GMShL5iC8aY | IP blocked / 1.336s | 429 / 1.787s | untimed text / 8.147s | OK / 1.217s |
| z1oISsDUKLA | IP blocked / 1.080s | 429 / 1.543s | untimed text / 8.981s | OK / 1.093s |
| tqUDjc1HzO4 | transcript / 0.933s | 429 / 2.695s | page only / 0.791s | OK / 2.316s |
| B_DMMlDuJB0 | IP blocked / 1.095s | 429 / 1.770s | 429 / 0.299s | OK / 1.741s |
| 3ssL8vx7Xhg | no captions / 1.013s | no captions / 1.666s | 429 / 0.323s | OK / 1.563s |

Audio on `3ssL8vx7Xhg` (134 seconds): audio URL / 13.948s. HTTP 200, API success true, one URL string hosted on `storage.googleapis.com`. The URL was not tested for downloadability.

Transcript API: 2/9 transcripts. yt-dlp subtitles: 0/9 files. Firecrawl markdown: 5/9 transcripts, 2/9 pages only, 2/9 rate-limit errors. Metadata: 9/9 success. Audio: 1/1 URL returned.

### Per-run transcript measurements

Last timestamp means the start of the final segment. Coverage is that timestamp divided by metadata duration. API segment ends are also in JSON. Words use lowercased Unicode tokens with internal apostrophes retained. A dash means unavailable or not applicable. Failed transcript routes have zero returned segments and words. Firecrawl transcript lines have no cue times, so segment count and coverage are unavailable. Metadata and audio are not transcripts.

| Video | Route | Outcome | Wall s | Caption type | Segments | Words | First s | Last s | Coverage |
|---|---|---|---:|---|---:|---:|---:|---:|---:|
| BsWxPI9UM4c | yta | ip_blocked | 1.526 | - | 0 | 0 | - | - | - |
| BsWxPI9UM4c | subs | rate_limited | 2.210 | auto | 0 | 0 | - | - | - |
| BsWxPI9UM4c | scrape | page_only | 0.935 | - | 0 | 0 | - | - | - |
| BsWxPI9UM4c | meta | metadata | 2.138 | auto | - | - | - | - | - |
| h9oAAAYnGx4 | yta | transcript | 0.943 | auto | 1623 | 11347 | 0.160 | 3890.480 | 1.000 |
| h9oAAAYnGx4 | subs | rate_limited | 1.542 | auto | 0 | 0 | - | - | - |
| h9oAAAYnGx4 | scrape | untimed_transcript | 8.455 | unknown | - | 11345 | - | - | - |
| h9oAAAYnGx4 | meta | metadata | 1.127 | auto | - | - | - | - | - |
| AKg27L4E0M8 | yta | ip_blocked | 1.039 | - | 0 | 0 | - | - | - |
| AKg27L4E0M8 | subs | rate_limited | 1.838 | auto | 0 | 0 | - | - | - |
| AKg27L4E0M8 | scrape | untimed_transcript | 5.877 | unknown | - | 4738 | - | - | - |
| AKg27L4E0M8 | meta | metadata | 1.294 | auto | - | - | - | - | - |
| 1d5aNfslwHg | yta | ip_blocked | 1.218 | - | 0 | 0 | - | - | - |
| 1d5aNfslwHg | subs | rate_limited | 1.547 | auto | 0 | 0 | - | - | - |
| 1d5aNfslwHg | scrape | untimed_transcript | 8.818 | unknown | - | 13671 | - | - | - |
| 1d5aNfslwHg | meta | metadata | 1.254 | auto | - | - | - | - | - |
| GMShL5iC8aY | yta | ip_blocked | 1.336 | - | 0 | 0 | - | - | - |
| GMShL5iC8aY | subs | rate_limited | 1.787 | auto | 0 | 0 | - | - | - |
| GMShL5iC8aY | scrape | untimed_transcript | 8.147 | unknown | - | 8649 | - | - | - |
| GMShL5iC8aY | meta | metadata | 1.217 | auto | - | - | - | - | - |
| z1oISsDUKLA | yta | ip_blocked | 1.080 | - | 0 | 0 | - | - | - |
| z1oISsDUKLA | subs | rate_limited | 1.543 | auto | 0 | 0 | - | - | - |
| z1oISsDUKLA | scrape | untimed_transcript | 8.981 | unknown | - | 9441 | - | - | - |
| z1oISsDUKLA | meta | metadata | 1.093 | auto | - | - | - | - | - |
| tqUDjc1HzO4 | yta | transcript | 0.933 | manual_or_auto | 331 | 5987 | 0.000 | 1634.360 | 0.997 |
| tqUDjc1HzO4 | subs | rate_limited | 2.695 | manual_or_auto | 0 | 0 | - | - | - |
| tqUDjc1HzO4 | scrape | page_only | 0.791 | - | 0 | 0 | - | - | - |
| tqUDjc1HzO4 | meta | metadata | 2.316 | manual_and_auto | - | - | - | - | - |
| B_DMMlDuJB0 | yta | ip_blocked | 1.095 | - | 0 | 0 | - | - | - |
| B_DMMlDuJB0 | subs | rate_limited | 1.770 | auto | 0 | 0 | - | - | - |
| B_DMMlDuJB0 | scrape | rate_limited | 0.299 | - | 0 | 0 | - | - | - |
| B_DMMlDuJB0 | meta | metadata | 1.741 | auto | - | - | - | - | - |
| 3ssL8vx7Xhg | yta | no_captions | 1.013 | - | 0 | 0 | - | - | - |
| 3ssL8vx7Xhg | subs | no_captions | 1.666 | none | 0 | 0 | - | - | - |
| 3ssL8vx7Xhg | scrape | rate_limited | 0.323 | - | 0 | 0 | - | - | - |
| 3ssL8vx7Xhg | meta | metadata | 1.563 | none | - | - | - | - | - |
| 3ssL8vx7Xhg | audio | audio_url | 13.948 | - | - | - | - | - | - |

Caption type for failed subtitle downloads describes available tracks, not downloaded content. Route 1 JSON does not name its selected track. For `tqUDjc1HzO4`, both English manual and auto tracks exist, so the returned track type is not independently confirmed. Firecrawl does not identify caption provenance.

### Metadata

| Video | Title | Duration s | Manual caption languages | Auto language entries | Chapters |
|---|---|---:|---|---:|---:|
| BsWxPI9UM4c | Why AI evals are the hottest new skill for product builders \| Hamel Husain & Shreya Shankar | 6393 | none | 178 | 24 |
| h9oAAAYnGx4 | Isaac HW 1 & 2 (Session 1) | 3892 | none | 157 | 0 |
| AKg27L4E0M8 | Open & Axial Coding - Isaac & Hamel Walkthrough | 2134 | none | 157 | 0 |
| 1d5aNfslwHg | Isaac HW3 (Session 2) | 4921 | none | 157 | 0 |
| GMShL5iC8aY | Isaac HW 4 (Session 3) | 2872 | none | 157 | 0 |
| z1oISsDUKLA | Isaac Homework 5 (Session 4) | 3240 | none | 157 | 0 |
| tqUDjc1HzO4 | How to Automate AI Evals (Correctly) | 1639 | en | 180 | 12 |
| B_DMMlDuJB0 | Data and DevOps Tools for Evaluating and Productionizing LLMs | 3880 | none | 157 | 11 |
| 3ssL8vx7Xhg | Happy and Fun Pop Background Music For Videos | 134 | none | 0 | 0 |

The JSON records every chapter and every caption language. Automatic entries can include translated tracks; these counts do not represent distinct spoken languages. `B_DMMlDuJB0` also advertised `live_chat`, which is not a manual caption track.

## Overlap check

Tokenize lowercase words; greedily match each route-1 word to the next same token after the previous match in route 2. Unmatched tokens do not advance the cursor. Divide matched tokens by route-1 token count.

| Video | Route 1 words | Route 2 words | Share | Result |
|---|---:|---:|---:|---|
| h9oAAAYnGx4 | 11347 | - | - | Route 2 produced no subtitle file. |
| tqUDjc1HzO4 | 5987 | - | - | Route 2 produced no subtitle file. |
| AKg27L4E0M8 | - | - | - | Route 2 produced no subtitle file. Route 1 also returned an IP-blocking error. |

All three checks were attempted by the analysis script. No paired text was available, so there is no overlap score and no evidence from this run that routes 1 and 2 return the same text. No extra retrieval was made to replace a failed baseline run.

## No-captions case

`3ssL8vx7Xhg`, “Happy and Fun Pop Background Music For Videos”, is 134 seconds long. It was the first result from the following search:

```text
uvx yt-dlp --flat-playlist --dump-json "ytsearch10:short instrumental music no talking"
uvx yt-dlp --list-subs --skip-download https://www.youtube.com/watch?v=3ssL8vx7Xhg
```

Search took 1.212s. The candidate check took 1.217s and returned:

```text
3ssL8vx7Xhg has no automatic captions
3ssL8vx7Xhg has no subtitles
```

The metadata dictionaries for both manual subtitles and automatic captions were empty. Route 1 said subtitles were disabled; route 2 exited 0 but produced no file. Firecrawl markdown was rate limited, so it provides no evidence about this video’s transcript. Firecrawl audio returned a URL.

## Failures and warnings

### Transcript API

Every route-1 invocation exited 0. Seven printed errors instead of JSON. Exact stdout errors follow:

`BsWxPI9UM4c`:

```text
Could not retrieve a transcript for the video https://www.youtube.com/watch?v=BsWxPI9UM4c! This is most likely caused by:

YouTube is blocking requests from your IP. This usually is due to one of the following reasons:
- You have done too many requests and your IP has been blocked by YouTube
- You are doing requests from an IP belonging to a cloud provider (like AWS, Google Cloud Platform, Azure, etc.). Unfortunately, most IPs from cloud providers are blocked by YouTube.

Ways to work around this are explained in the "Working around IP bans" section of the README (https://github.com/jdepoix/youtube-transcript-api?tab=readme-ov-file#working-around-ip-bans-requestblocked-or-ipblocked-exception).


If you are sure that the described cause is not responsible for this error and that a transcript should be retrievable, please create an issue at https://github.com/jdepoix/youtube-transcript-api/issues. Please add which version of youtube_transcript_api you are using and provide the information needed to replicate the error. Also make sure that there are no open issues which already describe your problem!
```

`AKg27L4E0M8`:

```text
Could not retrieve a transcript for the video https://www.youtube.com/watch?v=AKg27L4E0M8! This is most likely caused by:

YouTube is blocking requests from your IP. This usually is due to one of the following reasons:
- You have done too many requests and your IP has been blocked by YouTube
- You are doing requests from an IP belonging to a cloud provider (like AWS, Google Cloud Platform, Azure, etc.). Unfortunately, most IPs from cloud providers are blocked by YouTube.

Ways to work around this are explained in the "Working around IP bans" section of the README (https://github.com/jdepoix/youtube-transcript-api?tab=readme-ov-file#working-around-ip-bans-requestblocked-or-ipblocked-exception).


If you are sure that the described cause is not responsible for this error and that a transcript should be retrievable, please create an issue at https://github.com/jdepoix/youtube-transcript-api/issues. Please add which version of youtube_transcript_api you are using and provide the information needed to replicate the error. Also make sure that there are no open issues which already describe your problem!
```

`1d5aNfslwHg`:

```text
Could not retrieve a transcript for the video https://www.youtube.com/watch?v=1d5aNfslwHg! This is most likely caused by:

YouTube is blocking requests from your IP. This usually is due to one of the following reasons:
- You have done too many requests and your IP has been blocked by YouTube
- You are doing requests from an IP belonging to a cloud provider (like AWS, Google Cloud Platform, Azure, etc.). Unfortunately, most IPs from cloud providers are blocked by YouTube.

Ways to work around this are explained in the "Working around IP bans" section of the README (https://github.com/jdepoix/youtube-transcript-api?tab=readme-ov-file#working-around-ip-bans-requestblocked-or-ipblocked-exception).


If you are sure that the described cause is not responsible for this error and that a transcript should be retrievable, please create an issue at https://github.com/jdepoix/youtube-transcript-api/issues. Please add which version of youtube_transcript_api you are using and provide the information needed to replicate the error. Also make sure that there are no open issues which already describe your problem!
```

`GMShL5iC8aY`:

```text
Could not retrieve a transcript for the video https://www.youtube.com/watch?v=GMShL5iC8aY! This is most likely caused by:

YouTube is blocking requests from your IP. This usually is due to one of the following reasons:
- You have done too many requests and your IP has been blocked by YouTube
- You are doing requests from an IP belonging to a cloud provider (like AWS, Google Cloud Platform, Azure, etc.). Unfortunately, most IPs from cloud providers are blocked by YouTube.

Ways to work around this are explained in the "Working around IP bans" section of the README (https://github.com/jdepoix/youtube-transcript-api?tab=readme-ov-file#working-around-ip-bans-requestblocked-or-ipblocked-exception).


If you are sure that the described cause is not responsible for this error and that a transcript should be retrievable, please create an issue at https://github.com/jdepoix/youtube-transcript-api/issues. Please add which version of youtube_transcript_api you are using and provide the information needed to replicate the error. Also make sure that there are no open issues which already describe your problem!
```

`z1oISsDUKLA`:

```text
Could not retrieve a transcript for the video https://www.youtube.com/watch?v=z1oISsDUKLA! This is most likely caused by:

YouTube is blocking requests from your IP. This usually is due to one of the following reasons:
- You have done too many requests and your IP has been blocked by YouTube
- You are doing requests from an IP belonging to a cloud provider (like AWS, Google Cloud Platform, Azure, etc.). Unfortunately, most IPs from cloud providers are blocked by YouTube.

Ways to work around this are explained in the "Working around IP bans" section of the README (https://github.com/jdepoix/youtube-transcript-api?tab=readme-ov-file#working-around-ip-bans-requestblocked-or-ipblocked-exception).


If you are sure that the described cause is not responsible for this error and that a transcript should be retrievable, please create an issue at https://github.com/jdepoix/youtube-transcript-api/issues. Please add which version of youtube_transcript_api you are using and provide the information needed to replicate the error. Also make sure that there are no open issues which already describe your problem!
```

`B_DMMlDuJB0`:

```text
Could not retrieve a transcript for the video https://www.youtube.com/watch?v=B_DMMlDuJB0! This is most likely caused by:

YouTube is blocking requests from your IP. This usually is due to one of the following reasons:
- You have done too many requests and your IP has been blocked by YouTube
- You are doing requests from an IP belonging to a cloud provider (like AWS, Google Cloud Platform, Azure, etc.). Unfortunately, most IPs from cloud providers are blocked by YouTube.

Ways to work around this are explained in the "Working around IP bans" section of the README (https://github.com/jdepoix/youtube-transcript-api?tab=readme-ov-file#working-around-ip-bans-requestblocked-or-ipblocked-exception).


If you are sure that the described cause is not responsible for this error and that a transcript should be retrievable, please create an issue at https://github.com/jdepoix/youtube-transcript-api/issues. Please add which version of youtube_transcript_api you are using and provide the information needed to replicate the error. Also make sure that there are no open issues which already describe your problem!
```

`3ssL8vx7Xhg`:

```text
Could not retrieve a transcript for the video https://www.youtube.com/watch?v=3ssL8vx7Xhg! This is most likely caused by:

Subtitles are disabled for this video

If you are sure that the described cause is not responsible for this error and that a transcript should be retrievable, please create an issue at https://github.com/jdepoix/youtube-transcript-api/issues. Please add which version of youtube_transcript_api you are using and provide the information needed to replicate the error. Also make sure that there are no open issues which already describe your problem!
```

### yt-dlp subtitles

All eight captioned videos failed while downloading their first selected English subtitle track. Exact error lines:


`BsWxPI9UM4c`:

```text
ERROR: Unable to download video subtitles for 'en': HTTP Error 429: Too Many Requests
```

`h9oAAAYnGx4`:

```text
ERROR: Unable to download video subtitles for 'en-orig': HTTP Error 429: Too Many Requests
```

`AKg27L4E0M8`:

```text
ERROR: Unable to download video subtitles for 'en-orig': HTTP Error 429: Too Many Requests
```

`1d5aNfslwHg`:

```text
ERROR: Unable to download video subtitles for 'en-orig': HTTP Error 429: Too Many Requests
```

`GMShL5iC8aY`:

```text
ERROR: Unable to download video subtitles for 'en-orig': HTTP Error 429: Too Many Requests
```

`z1oISsDUKLA`:

```text
ERROR: Unable to download video subtitles for 'en-orig': HTTP Error 429: Too Many Requests
```

`tqUDjc1HzO4`:

```text
ERROR: Unable to download video subtitles for 'en': HTTP Error 429: Too Many Requests
```

`B_DMMlDuJB0`:

```text
ERROR: Unable to download video subtitles for 'en-orig': HTTP Error 429: Too Many Requests
```

Unique warnings from subtitle and metadata runs, copied exactly:

```text
WARNING: The extractor specified to use impersonation for this download, but no impersonate target is available. If you encounter errors, then see  https://github.com/yt-dlp/yt-dlp#impersonation  for information on installing the required dependencies
WARNING: [youtube] Incomplete data received in embedded initial data; re-fetching using API.
WARNING: [youtube] No supported JavaScript runtime could be found. Only deno is enabled by default; to use another runtime add  --js-runtimes RUNTIME[:PATH]  to your command/config. YouTube extraction without a JS runtime has been deprecated, and some formats may be missing. See  https://github.com/yt-dlp/yt-dlp/wiki/EJS  for details on installing one
WARNING: [youtube] unable to extract yt initial data; please report this issue on  https://github.com/yt-dlp/yt-dlp/issues?q= , filling out the appropriate issue template. Confirm you are on the latest version using  yt-dlp -U
```

The missing runtime warning appeared in all nine subtitle runs and all nine metadata runs. Node was installed but yt-dlp enabled only deno by default; no runtime override was tested. Metadata and caption inventory extraction worked despite the warning. The observed caption download error was HTTP 429. This run cannot determine whether enabling a runtime or impersonation would change that error.

### Firecrawl

The last two markdown calls returned HTTP 429. Exact service errors:

`B_DMMlDuJB0`:

```text
Rate limit exceeded. Consumed (req/min): 11, Remaining (req/min): 0. Upgrade your plan at https://firecrawl.dev/pricing for increased rate limits or please retry after 14s, resets at Tue Oct 13 2026 08:11:11 GMT+0000 (Coordinated Universal Time)
```

`3ssL8vx7Xhg`:

```text
Rate limit exceeded. Consumed (req/min): 12, Remaining (req/min): 0. Upgrade your plan at https://firecrawl.dev/pricing for increased rate limits or please retry after 13s, resets at Tue Oct 13 2026 08:11:11 GMT+0000 (Coordinated Universal Time)
```

Seven markdown responses had HTTP 200 and API success true, but two were watch pages without actual transcript text. Both pages offered “Show transcript”; the returned markdown did not contain the spoken content. The first included this exact embedded page error:

```text
Error 401 (Bad Request)!!1

**401.** That’s an error.

The server cannot process the request because it is malformed. It should not be retried. That’s all we know.
```

Those two page-only responses were cache hits from 2026-10-11. All five real transcript responses were cache misses and had `postprocessorsUsed: ["youtube"]`. The five transcripts were readable speech under `## Transcript`, with no timestamps.

### Blocking across the batch

Route 1 reported IP blocking on the first call, succeeded on the second, then reported blocking on calls three through six, succeeded on seven, and reported blocking on eight. Call nine reported disabled subtitles. This does not show blocking newly triggered by running nine videos. yt-dlp subtitle downloads returned 429 from the first captioned video onward, while all metadata requests still succeeded. Firecrawl markdown calls eight and nine hit the service limit. Their counters were 11 and 12 consumed requests per minute, exceeding this worker’s nine-call budget count; this run cannot attribute all account traffic to this worker. The subsequent audio request succeeded. No literal “Sign in to confirm you’re not a bot” error was observed.

## Findings

1. The transcript API returned two timed transcripts, but six captioned videos produced IP-blocking errors on this home Mac.
2. Transcript API errors exited with code 0 and appeared in stdout. A caller must inspect the returned content.
3. yt-dlp advertised English captions but downloaded no subtitle files. Every captioned video returned HTTP 429.
4. Metadata worked for all nine videos, including titles, durations, chapters and caption inventories.
5. The JavaScript warning did not prevent metadata extraction. Its effect on subtitle downloads remains untested.
6. Firecrawl returned five real transcripts as plain text. It provided no timestamps or measured time coverage.
7. Two successful Firecrawl responses were cached watch pages without transcripts. HTTP 200 and a “Show transcript” label were insufficient.
8. Firecrawl rate limited the final two markdown calls. Account-wide counters prevent attributing the threshold solely to this nine-call batch.
9. The confirmed no-captions video yielded an audio URL from Firecrawl. No transcription quality or audio downloadability was measured.
10. Word overlap could not be measured because yt-dlp produced no paired text.

Agents commit: not created because Packet T01 explicitly prohibited git. Owning spec/state files were left to the coordinating session; this worker wrote only its two requested test-result files.
