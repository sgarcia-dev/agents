---
created_at: 2026-10-13
updated_at: 2026-10-13
model: gpt-6.1-sol (high)
doc_type: sources
purpose: Evidence ledger for YouTube extraction, with capture limits and local measurements.
related:
  - path: ./spec.md
    why: Behavior, route table and the proposed fallback chain.
  - path: ./STATE.md
    why: Current tests and open implementation choices.
  - path: ./AGENTS.md
    why: How to add evidence without changing verbatim sources.
  - path: ./DECISIONS.md
    why: User-approved evidence layout.
---

# YouTube extraction: sources

## Source Hierarchy

- **Observed:** our dated local runs and capture `methods_tried` fields decide
  what worked here. Keep commands, versions, timings and output checks.
- **Documented:** captured project/vendor interfaces, limits and prices describe
  intended behavior. They do not prove a successful extraction here.
- **Claimed:** seller metrics, maintainer opinions and community accounts are
  attributed leads. A disclosed service representative is not an independent
  reliability witness.
- **Generated:** Y00 and digests help readers navigate evidence. When they
  conflict with a capture or local test, use the underlying evidence.

Note: the `sources/` folder (verbatim third-party copies) is not part of the public snapshot. Capture IDs below are plain text, and the URL column points to the original public page where one exists.

All 38 source captures and 11 digests were captured or written on 2026-10-13.
Words below count whitespace-separated tokens in the whole saved file, including
frontmatter, code and navigation. They measure file size, not original prose
length. Full means the collector's stated capture scope was complete, not that
linked pages, interactive tabs or extraction reliability were verified. Prices
and limits are snapshots; refresh before relying on them for a new purchase.

## Repo Guidance

| File | Authority |
|---|---|
| [Memory files](../../conventions/memory-files.md) | Spec navigation, evidence subsection labels and which file owns each truth. |
| [Artifact authoring](../../conventions/artifact-authoring.md) | Frontmatter and generated-output locations; no nested artifact roots. |
| [Local guidance](AGENTS.md) | User-approved source/digest/test layout and preservation rules. |

## Related Specs

| File | Relation and limit |
|---|---|
| [Web scraping site access](../web-scraping-site-access/spec.md) | Sibling for public-platform access. Its provider pilots do not prove YouTube extraction. |
| [LLM evals](../llm-evals/spec.md) | Consumer with E03/E16 captures. Only recorded extraction methods support measurements here. |

## External / Canonical Docs

External project docs, vendor interfaces, pricing pages and adoption snapshots.
Reliability slogans remain Claimed even in official docs. Captured helper code
establishes emitted fields, not a working installation on this machine.

| ID / capture | Title | URL | Capture method | Completeness | Words |
|---|---|---|---|---|---:|
| Y01a | youtube-transcript-api | [source](https://github.com/jdepoix/youtube-transcript-api) | `gh-api-raw-readme` | full | 2,631 |
| Y02a | yt-dlp | [source](https://github.com/yt-dlp/yt-dlp) | `gh-api-github-raw` | full | 19,338 |
| Y02b | External JS Scripts Setup Guide | [source](https://github.com/yt-dlp/yt-dlp/wiki/EJS) | `curl-raw-github-wiki-markdown` | full | 1,208 |
| Y03a | Supadata: Video Transcript API for YouTube, TikTok & Instagram | [source](https://supadata.ai/) | `firecrawl-v2-markdown` | full | 694 |
| Y03b | Supadata Pricing: Free Tier, Plans from $5/mo \| Video Transcript API | [source](https://supadata.ai/pricing) | `firecrawl-v2-markdown` | full | 784 |
| Y03c | Get YouTube, TikTok, Instagram, X (Twitter), Facebook transcript \| Supadata | [source](https://docs.supadata.ai/get-transcript) | `firecrawl-v2-markdown` | full | 1,813 |
| Y04a | YouTube Transcript API with Search, Channels & Playlists \| TranscriptAPI | [source](https://transcriptapi.com/) | `firecrawl-v2-markdown` | full | 2,220 |
| Y04b | YouTube Transcript API Reference \| TranscriptAPI.com | [source](https://transcriptapi.com/docs/api/) | `firecrawl-v2-markdown` | full | 7,677 |
| Y05a | Firecrawl \| Web Data API for AI Agents | [source](https://www.firecrawl.dev/) | `parallel-extract-full-content` | full | 3,305 |
| Y05b | How to extract YouTube transcript in Claude Code \| Firecrawl Glossary | [source](https://www.firecrawl.dev/glossary/web-scraping-apis/how-to-extract-youtube-transcript-in-claude-code) | `parallel-extract-full-content` | full | 665 |
| Y05c | How to Use Firecrawl's Scrape API: Complete Web Scraping Tutorial | [source](https://www.firecrawl.dev/blog/mastering-firecrawl-scrape-endpoint) | `parallel-extract-full-content` | full | 7,807 |
| Y05d | Scrape \| Firecrawl | [source](https://docs.firecrawl.dev/features/scrape) | `firecrawl-v2-markdown` | full | 6,896 |
| Y06a | Apify: Marketplace of ready-to-run tools for AI | [source](https://apify.com/) | `firecrawl-v2-markdown` | full | 1,116 |
| Y06b | YouTube Transcript Scraper · Apify | [source](https://apify.com/hypebridge/youtube-transcript-scraper) | `firecrawl-v2-markdown + HTTP/markdownify + embedded-JSON` | full | 2,786 |
| Y06c | Social Media Scraping API | [source](https://scrapecreators.com/) | `parallel-extract-full-content` | partial | 2,345 |
| Y06d | YouTube Transcript API | [source](https://docs.scrapecreators.com/v1/youtube/video/transcript) | `HTTP/markdownify` | partial | 1,916 |
| Y07 | Video understanding - Interactions API \| Google AI for Developers | [source](https://ai.google.dev/gemini-api/docs/video-understanding) | `firecrawl-v2-markdown+html-code-preservation` | full | 4,803 |
| Y07b | Gemini Developer API pricing  \|  Gemini API  \|  Google AI for Developers | [source](https://ai.google.dev/gemini-api/docs/pricing) | `firecrawl-v2-markdown` | full | 11,628 |
| Y08a | youtube-transcript-api | [source](https://pypistats.org/packages/youtube-transcript-api) | `pypistats-json-api-python-markdown` | full | 2,712 |
| Y08b | youtube-transcript | [source](https://www.npmjs.com/package/youtube-transcript) | `npm-registry-and-downloads-api-python-markdown` | full | 162 |
| Y08c | YouTube.js | [source](https://github.com/LuanRT/YouTube.js) | `gh-api-raw-readme-and-json-python-markdown` | full | 442 |
| Y11a-skill | SKILL.md | [source](https://github.com/NousResearch/hermes-agent/blob/main/skills/media/youtube-content/SKILL.md) | `gh-api-raw` | full | 617 |
| Y11a-formats | references/output-formats.md | [source](https://github.com/NousResearch/hermes-agent/blob/main/skills/media/youtube-content/references/output-formats.md) | `gh-api-raw` | full | 224 |
| Y11a-helper | scripts/fetch_transcript.py | [source](https://github.com/NousResearch/hermes-agent/blob/main/skills/media/youtube-content/scripts/fetch_transcript.py) | `gh-api-raw` | full | 406 |
| Y11b-zh | README.md | [source](https://github.com/Panniantong/Agent-Reach) | `gh-api-raw` | full | 1,422 |
| Y11b-en | Agent Reach | [source](https://github.com/Panniantong/Agent-Reach/blob/main/docs/README_en.md) | `gh-api-raw` | full | 2,643 |
| Y11d | youtube-mcp-cli README | [source](https://github.com/umbertotancorre/youtube-mcp-cli) | `gh-api-raw` | full | 671 |

### Capture limits that matter

- Y03 pages are full main-content captures without navigation/footer. The
  documentation-fetch retry after 429 is not a transcript API trial.
- Y04 full pages omit linked MCP setup pages. Its docs admit bot-detection errors.
- Y05b is a glossary recipe; Y05d has the technical media contract. Y05c's
  REST-only audio wording conflicts with its SDK example and Y05d.
- Y06b preserves README, pricing and input schema, not separate Output/API
  tabs. Its plan/start-charge and output-field descriptions conflict.
- Y06c lacks collapsed FAQ answers. Y06d lacks alternate response/code tabs.
  Their exact error and retry contracts are incomplete.
- Y07/Y07b are pages, not API tests. Inline-size guidance and the rounded
  high-resolution hour/context estimate have unresolved conflicts.
- Y08 measures downloads/stars, not users or extraction successes. YouTube.js's
  linked prerequisites and transcript method are not captured.
- Y11a's introductory helper schema differs from `main()` output. Y11b's
  README chain differs from later issue comments. Y11d does not document
  transcript JSON or an audio-transcription fallback.

## Verification / Runbooks

### Tests Run Here

These are frozen measurements, not a reusable runner. T01 Markdown and JSON
are the same batch, not independent replications. The Gemini file is a
worker-written record without independent frame scoring.

| ID / file | Run and capture method | Result / completeness limit | Words |
|---|---|---|---:|
| [T01-M](tests/2026-10-13-transcript-method-bakeoff.md) | Local uvx caption/metadata commands; Firecrawl REST v2; Markdown analysis | Nine videos; two API transcripts, six IP blocks, one no-captions. Eight subtitle 429s plus no-captions; no subtitle files. Five untimed Firecrawl transcripts. No transcription/overlap score. | 3,854 |
| [T01-J](tests/2026-10-13-transcript-method-bakeoff.json) | Machine-readable commands, timings, errors, metadata and response charges | Full saved T01 measurement record; raw-response paths reference temporary scratch storage. Not itself the full raw transcript bundle. | 10,893 |
| [G01](tests/2026-10-13-gemini-cli-video-test.md) | Gemini CLI agy: yt-dlp section download then native view_file | One 09:56 to 16:51 clip, 15.18 MB, about eight minutes; frames/audio reported. Page fetch had no frames. Accuracy, monetary cost and full-video limits unscored. | 1,151 |

Earlier real extraction runs live in the consuming spec. Only their first
30 lines and `methods_tried` frontmatter were reviewed for this packet. These
rows do not imply full-video analysis by this spec writer.

| ID / capture | Video URL | Capture method / timing | Completeness stated in capture |
|---|---|---|---|
| E03 | [video](https://www.youtube.com/watch?v=BsWxPI9UM4c) | youtube-transcript-api JSON, 2.533s initial; yt-dlp metadata and later VTT 11.084s; Firecrawl page-only | Full automatic captions; endpoint/duration compared. |
| V01 / E16a | [video](https://youtu.be/h9oAAAYnGx4) | API 1.06s; track list 0.80s; metadata 1.28s | Full, automatic. |
| V01 / E16b | [video](https://youtu.be/AKg27L4E0M8) | API 1.24s; track list 0.74s; metadata 1.80s | Full, automatic. |
| V01 / E16c | [video](https://youtu.be/1d5aNfslwHg) | API 1.17s; track list 0.78s; metadata 1.29s | Full, automatic. |
| V01 / E16d | [video](https://youtu.be/GMShL5iC8aY) | API 1.27s; track list 0.65s; metadata 1.34s | Full, automatic. |
| V01 / E16e | [video](https://youtu.be/z1oISsDUKLA) | API 0.98s; track list 0.87s; metadata 1.22s | Full, automatic. |
| V01 / E16f | [video](https://youtu.be/tqUDjc1HzO4) | API 1.13s; track list 0.93s; metadata 2.47s | Full, manual; T01 later left selected-track type uncertain. |
| V01 / E16g | [video](https://www.youtube.com/watch?v=B_DMMlDuJB0) | API 1.16s; track list 0.80s; metadata 1.39s | Full, automatic. |
| E16h, outside YouTube | [video](https://www.loom.com/share/30e5dced1afa467e8714d515694bb3b0) | yt-dlp failed; Firecrawl reported unavailable | Failed Loom capture; not one of V01's seven YouTube successes. |

**Root-supplied chronology, Packet S3 (2026-10-13):** batch finish times were E03
09:05, V01 09:09, T01 09:15, local clock, on the same home IP. Blocking appeared
within about 10 to 15 minutes and about 20 requests. This comes from the
coordinating root's instruction; no separate batch-finish log was provided.
T01 JSON records individual starts, including an IP-blocked request at
09:09:23. Its last media attempt began at 09:11:19; that is not the root's
packet finish time. Exact network-request count, triggering call and recovery
time are unknown. Do not retain the earlier rough hour estimate.

## Generated Reference / Companion Docs

### Original brief capture

Copied from the user's deep-research export. It is a lead list and proposal,
not a primary reliability source.

| ID / capture | Title | URL | Capture method | Completeness | Words |
|---|---|---|---|---|---:|
| Y00 | YouTube extraction for LLM agents | private ChatGPT deep research export (not published) | `file copy, body byte-identical to the Downloads original` | full | 3,081 |

### Digests

Summaries of the named captures, not fresh tests or independent corroboration.
Word counts include frontmatter.

| Digest | Captures | Main use | Words |
|---|---|---|---:|
| [Y01](digests/Y01-youtube-transcript-api.md) | Y01a, Y01b | API fields, track preference, IP blocks/proxy caveats. | 2,057 |
| [Y02](digests/Y02-yt-dlp.md) | Y02a, Y02b | Subtitle/metadata/media operations; runtime/EJS setup. | 2,672 |
| [Y03](digests/Y03-supadata.md) | Y03a to Y03c | Modes, commitments, asynchronous jobs and charges. | 2,267 |
| [Y04](digests/Y04-transcriptapi.md) | Y04a, Y04b | Timed output, errors, languages and billed cache hits. | 2,294 |
| [Y05](digests/Y05-firecrawl.md) | Y05a to Y05d | Glossary claims versus technical media/caching contracts. | 2,872 |
| [Y06](digests/Y06-apify-scrapecreators.md) | Y06a to Y06d | Actor-specific schema/prices; partial endpoint evidence. | 2,478 |
| [Y07](digests/Y07-gemini-video-understanding.md) | Y07, Y07b | Video input modes, limits and calculated input costs. | 2,604 |
| [Y08](digests/Y08-adoption-stats-and-youtubejs.md) | Y08a to Y08c | Popularity and incomplete client setup evidence. | 1,749 |
| [Y09](digests/Y09-reddit-threads.md) | Y09a to Y09f | Attributed pipelines, blocking and fidelity disputes. | 2,899 |
| [Y10](digests/Y10-hacker-news-threads.md) | Y10a, Y10b | Caption-first deployments; historical transcription anecdotes. | 2,981 |
| [Y11](digests/Y11-hermes-skill-agent-reach-youtube-mcp-cli.md) | All seven Y11 captures | Actual helper fields, bounded fallback reports and CLI interfaces. | 2,579 |

## Historical / Stale

### Community Evidence

Context, not current route guarantees. Historical prices/timings retain their
original dates. Creator posts and service pitches are not independent
comparisons. Read issue replies as well as the opening failure report.

| ID / capture | Title | URL | Capture method | Completeness | Words |
|---|---|---|---|---|---:|
| Y01b | Cloud IP blocking in 2026: Webshare vs Supadata vs alternatives? | [source](https://github.com/jdepoix/youtube-transcript-api/issues/593) | `gh-api-issue-and-paginated-comments` | full | 392 |
| Y09a | I got tired of watching YouTube to learn things, so I built a tool that turns any video into a transcript, summary, and knowledge graph | [source](https://www.reddit.com/r/ClaudeAI/comments/1sdyw75/) | `arctic-shift-api` | partial | 2,405 |
| Y09b | Built a fully local YouTube transcript + analysis pipeline | [source](https://www.reddit.com/r/LocalLLM/comments/1s4zc9d/) | `arctic-shift-api` | full | 229 |
| Y09c | Built a CLI tool that turns YouTube transcripts into clean literary prose so I don't have to sit through 40-minute videos. Works     with local LLMs / Ollama | [source](https://www.reddit.com/r/LocalLLM/comments/1wu6z2v/) | `arctic-shift-api` | full | 1,031 |
| Y09d | How to avoid IP bans when using youtube-transcript-api to fetch YouTube video transcripts? | [source](https://www.reddit.com/r/LocalLLaMA/comments/1mfij9a/) | `arctic-shift-api` | partial | 567 |
| Y09e | Blueprint: How I feed YouTube video context into the AI Agent node effectively | [source](https://www.reddit.com/r/n8n/comments/1qbtdkp/) | `arctic-shift-api` | full | 477 |
| Y09f | Youtube video summaries | [source](https://www.reddit.com/r/hermesagent/comments/1uds2r1/) | `arctic-shift-api` | full | 436 |
| Y10a | OpenAI charges by the minute, so speed up your audio | [source](https://news.ycombinator.com/item?id=44381640) | `algolia-api-html-to-markdown-python` | full | 15,077 |
| Y10b | Show HN: YouTube MCP, give any AI agent access to YouTube | [source](https://news.ycombinator.com/item?id=48198790) | `algolia-api-html-to-markdown-python` | full | 303 |
| Y11c | v1.5.0 实测 15 个渠道：YouTube 字幕路由已失效、doctor 对登录态平台给不出后端、transcribe.sh 在 Windows 完全不可用（8 个问题，附本地修复验证） | [source](https://github.com/Panniantong/Agent-Reach/issues/566) | `gh-api-json-to-markdown` | full | 1,006 |

- Y09a: 34 captured comments versus archived count 19, one removed body.
  Y09d: 10 versus four, two removed bodies. Both are partial.
- Y09f is marked full but has six comments versus archived count five. Counts
  are snapshots; the mismatch does not establish complete current discussion.
- Y10a captures story 44376989 and 225 descendants, though the requested URL
  points to comment 44381640. Y10b has three descendants; none establishes a
  successful independent extraction.
- Y01b has one reply. Its universal cheaper-proxy statement is an opinion.
  Y09d includes a disclosed TranscriptAPI representative.
- Y11c has a reporter's failure and a maintainer's opposing live result. The
  later bounded chain is stronger guidance than its README, but was not rerun here.

## Weak Claims To Avoid

- Home IPs are safe for modest batches. E03/V01 succeeded, then local blocks
  appeared within about 10 to 15 minutes/about 20 requests.
- Exactly 20 requests caused the block, T01 alone caused it, or recovery takes
  a known interval. None was measured.
- Every E03 route returned a transcript, or all nine T01 videos returned
  subtitle 429s. Firecrawl was page-only in E03; T01 had eight caption 429s
  and one video without captions.
- Exit zero, HTTP 200, caption inventory or `postprocessorsUsed: youtube`
  proves a transcript. T01 has counterexamples.
- Fixing yt-dlp's runtime fixes the 429. That intervention was not tested;
  metadata already worked despite the warning.
- Firecrawl's five transcripts are complete/timestamped. They were untimed;
  coverage was unmeasured. Its page benchmark is not a caption benchmark.
- A returned audio URL proves playable audio, good transcription or recovery
  from every block. T01 did not download or transcribe it.
- Gemini CLI accepts YouTube URLs like Gemini API, a clip proves whole-video
  analysis, or exact visual text in the worker record was independently checked.
- Gemini URL input is preview based on Y07, or video-input estimates are the
  total bill. Preview status is unsupported; output/thinking cost extra.
- Supadata Basic is a cancel-any-month $5 plan, or default calls cost one
  credit. Basic is billed annually; `auto` can generate at two credits/minute.
- TranscriptAPI never gets blocked, cached transcripts are free, or it generates
  missing captions. Docs admit bot errors, bill cache hits and give no generation route.
- Every Apify Actor costs $1/1,000 or has Hypebridge's behavior. Actors differ;
  its own price/schema conflicts and run overhead remain unresolved.
- ScrapeCreators' general success rate establishes YouTube performance. Its
  error capture is partial and no local test exists.
- Hermes needs no setup or emits the example's full segment schema. Captured
  setup and helper code contradict those assumptions.
- Agent-Reach health checks, downloads, stars or endorsements prove live caption
  reliability. None replaces a dated extraction run.
- LLM prose cleanup preserves every technical claim, or accelerated/trimmed
  audio retains correct source timestamps. No fidelity study is captured.
