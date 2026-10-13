---
created_at: 2026-10-13
updated_at: 2026-10-13
model: gpt-6.1-sol (high)
doc_type: state
status: evidence collected; local blocking observed; portable implementation proposed
scope: YouTube transcripts and visual evidence for research across all harnesses
purpose: Current measured results, unbuilt work, proposals and next steps.
related:
  - path: ./spec.md
    why: Outcomes, route comparison and proposed output contract.
  - path: ./AGENTS.md
    why: How to preserve sources and add fresh evidence.
  - path: ./DECISIONS.md
    why: User decisions, distinct from the proposals here.
  - path: ./SOURCES.md
    why: Test records, captures, digests and evidence limits.
---

# YouTube extraction: state

## What is true now (13 October 2026)

- YouTube extraction is its own general research spec. Claude Code, Codex,
  OpenCode, Hermes and Gemini are consumers. The user approved the evidence
  layout in [DECISIONS.md](DECISIONS.md).
- The report is among 38 source captures; 11 digests and three local test files are
  indexed in [SOURCES.md](SOURCES.md). Captures are preserved, including
  partial sources and conflicting claims. Local tests outrank vendor claims.
- **The home IP block is the main finding.** Root-measured batch finish times,
  local clock on 2026-10-13: E03 **09:05**, V01 **09:09**, T01 **09:15**.
  E03 fetched one timed transcript in **2.533 seconds** and later wrote VTT.
  V01 fetched **7/7** transcripts. T01 got **2/9** through the transcript API,
  with **six IP-block errors** and one no-captions result. Local blocking
  appeared within **about 10 to 15 minutes and about 20 requests**, not the
  earlier rough hour estimate. This is an approximate chronology, not a
  measured safe threshold. T01 was already blocked on its first request.
- T01's `yt-dlp` wrote **0/9** subtitle files: **eight HTTP 429s** on captioned
  videos and one no-captions result. Metadata worked **9/9**. Its missing JS
  runtime warning did not stop metadata. No runtime override was tested, so
  it is not established as the cause of subtitle 429s.
- Firecrawl worked while local caption routes were blocked: **five untimed
  transcripts**, two cached page-only responses and two service 429s. Actual
  spoken text must be checked. Its rate-limit counters included other account
  traffic. E03's Firecrawl calls also returned pages without a transcript;
  the shorthand that all E03 routes worked does not mean all got captions.
- Firecrawl returned an audio URL for a 134-second no-captions music video
  in 13.948 seconds. The file was not downloaded or transcribed. This is not
  evidence about speech-to-text accuracy on spoken videos.
- The [Gemini CLI record](tests/2026-10-13-gemini-cli-video-test.md) reports
  frames and audio from a downloaded 09:56 to 16:51 clip. Direct web fetch
  returned HTML, not frames. The run took about eight minutes. Its visual
  details were not independently scored; cost and full-video coverage are
  unknown. Direct Gemini API YouTube input was not tested.
- **We do not yet know how long the IP block lasts.** No delayed recovery
  test or safe pacing limit has been measured.

## VPN exit observation (13 October 2026)

- The home IP was blocked at about 09:15.
- At about 10:41 a VPN exit IP (a French datacenter) returned a full timed
  transcript in 2.8 seconds.
- Two paced workers then captured 8 single videos and 9 playlist videos with
  timed captions. They paced requests 20 seconds apart.
- That exit IP was also blocked after about 17 requests in about 10 minutes.
- The playlist worker then waited 5 minutes and fell back to Firecrawl, which
  returns untimed text.
- Reading: a fresh exit IP works at once, but two workers at 20 seconds apart
  still hit the limit. Run one paced video worker at a time.

## What is not built yet

- No portable CLI/skill with a common JSON + Markdown contract, shared cache,
  cross-harness request budget or automatic fallback has been built here.
- No dedicated managed transcript route has been tested or selected. Supadata,
  TranscriptAPI, Apify Actors and ScrapeCreators remain candidates.
- No local speech-to-text pipeline has been validated. No direct Gemini API
  video trial, timestamp-fidelity benchmark or scored visual test exists here.
- The captured Hermes skill shows a useful workflow, but its installation
  readiness was not checked. Its emitted JSON needs adaptation for the spec.

## Proposals

- **Placement:** treat this spec as a sibling of
  [web scraping site access](../web-scraping-site-access/spec.md), serving Claude
  Code, Codex, OpenCode, Hermes and Gemini equally. The user has not decided this.
- **Chain:** cache → paced `youtube-transcript-api` → conditional `yt-dlp`
  captions only without block evidence → Firecrawl → tested managed fallback.
  Confirmed no captions branch to audio/transcription; visual questions branch
  to bounded video inspection. See [spec.md](spec.md#recommended-fallback-chain).
- Build a small shared CLI and thin harness skills. Serialize local caption
  traffic across harnesses, retain source timing and stop the batch on a block.
  Decide cache location, lifetime and initial conservative pacing during that
  work; no safe numeric rate is established.
- Try existing Firecrawl access before selecting another paid service. Keep
  generation explicit and record usage. Supadata native and TranscriptAPI
  have detailed caption contracts; neither is a measured winner here.

## Next steps

1. After several quiet hours, retest a previously blocked captioned video.
   Record exact times, then plan a small paced test. Do not rerun a burst.
2. Test `yt-dlp` with an explicitly enabled supported JS runtime and compatible
   EJS. Test one fresh Firecrawl scrape for a cached page-only result after
   provider backoff. Keep the two questions separate.
3. Build the portable CLI/skill with cache, rate limiting, content checks and
   the proposed JSON/Markdown output. Preserve raw evidence.
4. Decide whether a dedicated paid fallback is needed. If so, compare capped
   native-caption runs on the same videos, including timing and actual charges.
5. Test playable audio and transcription on a spoken video without captions.
   Check technical words and timestamps. Score a visual clip and, if useful,
   separately trial direct Gemini API video input with measured usage.

6. Measure how long a block lasts, and whether rotating VPN exits is a
   dependable fallback. Record exit location, request count, pacing and the time
   of the first block for each exit.

## Blockers and limits

- Local caption access may still be blocked; recovery duration is unknown.
- Firecrawl text lacks timestamps and measured completeness. Its account-wide
  service limit needs coordination as well as local IP pacing.
- Managed-service reliability, transcription quality and visual accuracy lack
  comparative measurements. Provider selection and cache policy remain open.
