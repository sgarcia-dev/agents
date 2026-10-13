---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [Y09a, Y09b, Y09c, Y09d, Y09e, Y09f]
source_files:
  - sources/Y09a-reddit-claudeai-1sdyw75.md
  - sources/Y09b-reddit-localllm-1s4zc9d.md
  - sources/Y09c-reddit-localllm-1wu6z2v.md
  - sources/Y09d-reddit-localllama-1mfij9a.md
  - sources/Y09e-reddit-n8n-1qbtdkp.md
  - sources/Y09f-reddit-hermesagent-1uds2r1.md
purpose: One-source digest feeding the spec compendium.
---

# YouTube extraction reports from six Reddit threads (Y09)

**What it is:** Six archived Reddit posts and their captured comments. Reading times below are estimates for the captures, not source measurements.

| ID | Author, UTC publication date | Topic and link | Capture length |
| --- | --- | --- | --- |
| Y09a | ElectronicPlan8497, 2026-04-06 13:28:52 | [YouTube to knowledge graph](https://www.reddit.com/r/ClaudeAI/comments/1sdyw75/) | Post + 34 comments, about 8 minutes |
| Y09b | LeadingDonut517, 2026-03-27 09:32:51 | [TubeScribe local pipeline](https://www.reddit.com/r/LocalLLM/comments/1s4zc9d/) | Post, no comments, about 1 minute |
| Y09c | TomatilloHonest425, 2026-09-30 14:50:48 | [TubeStoevsky prose pipeline](https://www.reddit.com/r/LocalLLM/comments/1wu6z2v/) | Post + 7 comments, about 4 minutes |
| Y09d | Anas_M1nt, 2025-08-02 05:24:17 | [Transcript API IP bans](https://www.reddit.com/r/LocalLLaMA/comments/1mfij9a/) | Post + 10 comments, about 2 minutes |
| Y09e | nikhonit, 2026-01-13 14:53:39 | [n8n transcript blueprint](https://www.reddit.com/r/n8n/comments/1qbtdkp/) | Post + 2 comments, about 2 minutes |
| Y09f | maxx4455, 2026-06-23 20:10:44 | [Hermes video summaries](https://www.reddit.com/r/hermesagent/comments/1uds2r1/) | Post + 6 comments, about 2 minutes |

**Capture status:** Y09a and Y09d are partial. Y09a has 34 captured comments against an archived count of 19, with one removal marker. Y09d has 10 against 4, with two removal markers. The deleted bodies are unavailable; the count mismatches do not identify which other material is missing. Y09b, Y09c, Y09e and Y09f are marked full. Y09f still has a count mismatch, 6 captured against 5. All counts and scores are archived snapshots. Linked repositories, examples, videos and service documentation were not captured here and were not inspected.

## The point in three sentences

The recurring route is to fetch existing captions and use audio transcription when captions are absent. Local extraction can encounter IP bans, bot detection and cookie maintenance, while managed services offer an alternative with little independent reliability evidence in these captures. Keep original captions separate from summaries or rewritten prose, because attractive output and claimed accuracy do not prove that details survived.

## Key ideas

- Caption extraction and speech recognition are different stages. ElectronicPlan8497 describes the missing-caption fallback as “Whisper (local, no API key) as fallback for videos without subtitles” (Y09a, post, Under the hood, 2026-04-06).
- Persistent files are a central benefit of the knowledge graph tool. Its stated outputs are “raw transcript, summary.md, graph.html (open in browser)” (ElectronicPlan8497, Y09a post, 2026-04-06). A graph represents entities and their relationships.
- Obsidian export was reported shipped, rather than merely requested. “Update: shipped. `--obsidian` flag is live.” (ElectronicPlan8497, Y09a comment oerbzns, 2026-04-07). The same comment specifies one Markdown file per entity, tags/source/author frontmatter and links between related concepts.
- TubeScribe separates extraction, local analysis and storage. “YouTube → transcript extraction (Whisper fallback if needed) → local LLM via LM Studio → SQLite (FTS5 for search)” (LeadingDonut517, Y09b post, 2026-03-27). FTS5 is the named text-search component.
- TubeStoevsky addresses repeated automatic caption lines before rewriting them. “The custom SRT parser deduplicates progressive updates into a clean continuous stream.” (TomatilloHonest425, Y09c post, Rolling subtitles, 2026-09-30). SRT is the subtitle format used here.
- Long generated outputs can fail independently of YouTube fetching. “Many local LLM proxies and gateways hang or drop connection on monolithic 2,000+ word outputs.” (TomatilloHonest425, Y09c post, Gateway hangs, 2026-09-30). The stated remedies are streaming and an HTTP compression setting.
- Detail preservation is disputed, not established. A reader asks whether “the LLM quietly trims those anyway” (lulzxdxdxd, Y09c comment pd0lzui, 2026-09-30). The creator initially responds with confidence and plans for longer tests, then reports a two-hour example without a scoring method.
- IP bans are a reported failure, not just a hypothetical concern. “i keep having ip ban or a ban from requests to youtube-transcript-api” (Anas_M1nt, Y09d post, 2025-08-02). SofeyKujo recommends “rotating residential proxies” (comment n6hcbmo, same date), meaning changing the network address through household-network intermediaries.
- Managed API claims need attribution. “Full disclosure, I work on TranscriptAPI.” (scheemunai_, Y09d comment otxbxqc, 2026-06-26). Their claims about bypassing infrastructure maintenance come from a service representative.
- Browser scraping caused concrete workflow problems for one n8n user. Puppeteer “kept timing out on longer videos” and HTML extraction “broke constantly” (nikhonit, Y09e post, I tried, 2026-01-13). These are individual reports without logs or failure rates.
- Hermes discussion distinguishes captions, audio and full video. “Pull video and analyze it via AI (expensive)” (Mugen0815, Y09f comment oteemck, 2026-06-23) is a cost opinion, not a price comparison.
- Still images plus a transcript are a proposed intermediate route. “extract images from video every N seconds or cluster semantically. De-dupe.” (cornelln, Y09f comment othm9oz, 2026-06-24). No implementation or measured savings accompany the suggestion.

## How to do it (concrete steps, checklists, templates)

### Y09a: youtube-to-knowledge, captions then local Whisper

- **Setup and order:** Requires Claude Code; the post says Windows, macOS and Linux are supported. Paste a YouTube link and run `/process <url>`. Use yt-dlp + YouTube Transcript API first, local Whisper for missing subtitles, then Claude Code entity extraction and NetworkX + PyVis graph generation. Add `--obsidian` for entity files. Installation commands and dependencies are not supplied.
- **Cost:** No API key for local Whisper. No total processing price, Claude Code price or hardware requirement is given. The author's claim that no data leaves the machine is not independently demonstrated by the capture.
- **Failure modes:** Missing subtitles have a named fallback. A later comment points to youtube-skills for rate limits, without setup or results. No IP-block or bot-check recovery procedure is supplied for this tool. Local audio transcription still needs access to the audio; the capture does not show download-block handling.
- **Output:** Raw transcript, `summary.md`, `graph.html`; optional entity Markdown with YAML frontmatter and wikilinks. No transcript schema, JSON output or implemented timestamp guarantee is given. WhisperX word-level timestamps were discussed as useful; a later “Merged” comment does not specify exactly which features landed.
- **Reliability:** Creator reports 40+ processed videos and a few minutes for a 30-minute video. No independent success rate or controlled benchmark. Claims that the fallback works regardless of subtitles do not establish immunity to download failures.

### Y09b: TubeScribe, local model and searchable storage

- **Setup and order:** Supply a video or playlist to TubeScribe. Extract transcripts, fall back to Whisper, analyze through LM Studio, and store in SQLite FTS5. Creator tested Qwen 3.5 9B; other models are said to depend on RAM. No installation or execution commands are supplied.
- **Cost:** “No API keys, no cloud.” Hardware cost and runtime are absent.
- **Failure modes:** Missing captions have Whisper fallback. IP bans, bot checks, download failures and recovery are not covered.
- **Output:** Searchable storage, quick-to-deep summaries, timestamped key quotes, basic speaker identification, tags and Q&A. No export schema or JSON format is specified.
- **Reliability:** One creator report of testing with a named model, no comments or comparative results.

### Y09c: TubeStoevsky, subtitle cleanup then prose

- **Setup and order:** Fetch subtitles through `yt-dlp`, clean timecodes and repeated lines, then run three LangChain stages: prose, concise title, Markdown subheadings. Use an OpenAI-compatible completions endpoint, local Ollama / vLLM or a named cloud provider.

```sh
export LLM_API_KEY='xxxxxx'
uvx tubestoevsky --model gpt-4o-mini <URL>
```

The post also supplies this local invocation, with spacing normalized here:

```sh
LLM_BASE_URL="http://localhost:11434/v1" LLM_API_KEY="ollama" uvx tubestoevsky --model qwen3.8-27b <URL>
```

- **Cost:** Creator says GPT Luna would cost roughly a few cents in API usage. No token count, video length or price schedule accompanies that estimate. Local hardware cost is unspecified.
- **Failure modes:** Repeated subtitles are parsed away. Gateway hangs are addressed with streaming and `Accept-Encoding: identity`. No missing-caption speech-recognition fallback, IP-block handling or bot-check procedure is described. A reported proper-name error remains in the two-hour example.
- **Output:** Matching `.srt`, `.txt`, `.md` files. Timecodes are cleaned out of the prose route; the capture does not establish timestamp preservation in the final Markdown. No JSON output is named.
- **Reliability:** Creator links a two-hour test and claims high accuracy. The linked files and evaluation method are outside the capture. No independent test confirms preservation of all details.

### Y09d: direct caption fetching and suggested alternatives

- **Direct library setup:** Start with the library description section “Working around IP bans (RequestBlocked or IpBlocked exception)”. Commenters suggest rotating residential proxies, changing browser information, cookies and randomized waits. No working configuration, price, output schema or measured success rate is supplied. Missing-caption handling is absent.
- **Selenium suggestion:** Rotate user agents, wait random intervals and use a transcript website without captcha. A user agent identifies the client to a website. The website is unnamed; there is no test or output format. This is a bot-check workaround suggestion, not evidence of success.
- **TranscriptAPI setup:** Its representative specifies GET to `https://transcriptapi.com/api/v2/youtube/transcript?video_url=<url>` with a Bearer token, an authentication token. The source escapes the underscore in Markdown. Claimed output is clean JSON; no fields or timestamp guarantee are shown. Price and missing-caption behavior are absent. Claimed benefits are managed infrastructure and no YouTube Data API v3 quota; no independent reliability result is given.
- **Apify and Supadata:** Commenters name these alternatives. One links `https://apify.com/practicaltools/apify-youtube-transcribe`; another says to use `https://supadata.ai`. No setup steps, costs, caption fallback, block handling, output schema or reliability measurements are supplied.

### Y09e: n8n managed transcript workflow

- **Setup and order:** YouTube Trigger, On new video → HTTP Request GET to TranscriptAPI → AI Agent using Claude, with system prompt “Read this transcript and summarize...”. The post names Claude 3.5. It does not include an importable workflow JSON or full authentication settings.
- **Cost:** No service or model price is given. Elhadidi calls a linked workflow free, not the underlying API or model usage.
- **Failure modes:** Replaces Puppeteer timeouts, fragile HTML extraction and official-node caption difficulties involving OAuth permissions and quotas. OAuth is the account permission mechanism mentioned here. No API failure, missing-caption or bot-check recovery is shown.
- **Output:** Claimed instant JSON with Music and Applause tags cleaned out, followed by a LinkedIn post or summary. No response fields, timestamp behavior or measured latency.
- **Reliability:** One first-person account says it does not crash on long videos. Elhadidi reports using a similar HTTP-to-AI workflow on 2026-01-14. Neither supplies measured success rates.

### Y09f: Hermes captions, audio and visual routes

- **Captions:** Mugen0815 says Hermes supports only the first route out of the box, prefaced with “Afaik”. No command, output format or price is given. ImNotDoomed reports “It works pretty well for me.” (comment ote7trh, 2026-06-23). k0b0 reports blocking in OpenCode and suggests cookies; they explicitly are not using Hermes. This does not prove Hermes uses yt-dlp.
- **Audio transcription:** Download audio and transcribe with AI, for example Whisper. No setup details, cost, timestamp format or tested reliability. Missing captions motivate this route elsewhere in the packet, but this comment provides no download-block remedy.
- **Full video analysis:** Download and analyze video with AI. Described as expensive without prices, commands, output schema or tests. Missing visual information in captions is not quantified.
- **Images plus transcript:** Extract periodic or semantically grouped images, remove duplicates, then combine with transcript. Claimed cheaper than video analysis, without measurements. No tool, schema, missing-caption handling or access-failure recovery is supplied.
- **Apify:** No_Path_5239 says “J'utilise Apify pour récupérer le transcript.” (comment ovoc59e, 2026-07-05), reporting use to retrieve the transcript. No configuration or reliability detail.

### Other routes mentioned briefly in Y09a

NotebookLM is reported free with up to 50 sources by bnm777 (2026-04-06), with no extraction procedure, format or failure analysis. fast-transcriber.com is called paid; no price or measured speed is given. beyondtube.pro is suggested for channel bulk imports, without setup or pricing. PreparationIcy4723 reports polling public playlists into a graph and skill Markdown files, but supplies no code or failure handling. scriptoss is described as emailing full transcripts on new channel uploads; cost, timestamps and reliability are absent. Vaivox is mentioned in a discussion of dubbing and understanding, not documented as an extraction route. youtube-skills is suggested for rate limits without implementation details. None of these mentions establishes a tested fallback.

## Tools, code and commands named

- Y09a: yt-dlp, YouTube Transcript API, Whisper, Claude Code, NetworkX, PyVis, faster-whisper, whisperX / WhisperX, Obsidian, NotebookLM, Gemini, GPT, Vaivox; `/process <url>`, `--obsidian`; repositories `velmighty/youtube-to-knowledge` and `ZeroPointRepo/youtube-skills`.
- Y09b: TubeScribe, LM Studio, SQLite, FTS5, Qwen 3.5 9B; repository `omkartphatak/tubescribe`.
- Y09c: TubeStoevsky, LangChain, Ollama, vLLM, OpenAI, DeepSeek, uvx, `uv tool install tubestoevsky`, `pip install tubestoevsky`, `gpt-4o-mini`, `qwen3.8-27b`, Splash runtime, GPT Luna; MIT license; repository `iiw/tubestoevsky` and PyPI package `tubestoevsky`. Model names are preserved as written, not verified.
- Y09d: youtube-transcript-api, RequestBlocked, IpBlocked, Selenium, Apify, Supadata, TranscriptAPI, YouTube Data API v3.
- Y09e: n8n, Puppeteer node, Official YouTube node, HTML Extract, HTTP Request, YouTube Trigger, AI Agent node, Claude 3.5, TranscriptAPI.
- Y09f: Hermes, yt-dlp, OpenCode CLI, Whisper, Gemini, Apify. No software release versions are supplied beyond the model/API identifiers above.

## Numbers and strong claims

- **Y09a post, 2026-04-06:** 30-minute video in a few minutes; 40+ searchable videos. Creator reports, without timing conditions. “everything runs locally (no data leaves your machine)” (comment oem6lyw) is a creator privacy claim, not demonstrated.
- **Y09a comment oem5tqp:** NotebookLM free and up to 50 sources. User report at that date, not verified current pricing or limits.
- **Y09c post:** 2,000+ word outputs can hang gateways. Creator engineering report, not a universal limit.
- **Y09c comment pd7c9bm, 2026-10-01:** About 50 t/s, tokens per second, on an MBP M5 Pro 64GB with Splash. About 10 t/s with Ollama/Qwen 27b on a non-high-end Mac is explicitly an expectation. The creator says they do not use Ollama. Few-cents API cost is an estimate.
- **Y09c comment pd66j78, 2026-10-01:** Two-hour example claims “98–99% semantic accuracy” and approximately 95% verbatim match. Creator claim with no scoring method in the capture. The example still changes Buc-ee's to Bess's. Treat the quality language as promotional, not a validated benchmark.
- **Y09e post:** “the JSON returns instantly” is an unmeasured speed claim. **Y09f comment othm9oz:** images plus transcript “costs much less” is an unquantified opinion.

## Compared with the deep research report

Only the relevant parts of Y00, section 2 were read, including the Y09c paragraph in subsection B.

- **Right, caption fallback:** The report says “Local Whisper when subtitles are unavailable.” Y09a says “Whisper (local, no API key) as fallback for videos without subtitles”. Its summary of TubeScribe's LM Studio and SQLite FTS5 pipeline also matches Y09b.
- **Right, caption cleanup:** The report describes “removal of duplicated captions” for the September post. Y09c says its parser “deduplicates progressive updates”.
- **Right, reliability caveat:** The report warns that creator posts do not show services are “objectively more reliable.” Y09d's TranscriptAPI comment explicitly discloses “I work on TranscriptAPI.”
- **Overstated, workload split:** The report says “Hosted automation and production workloads increasingly justify managed APIs.” These captures show one n8n workflow and several suggestions, not a production trend or comparative reliability study.
- **Potential overreach, Hermes:** “including within OpenCode workflows” matches k0b0's report. However, the report's Hermes framing must not turn that into a Hermes failure: k0b0 says “I'm using this without hermes agent”. Mugen0815's support claim is qualified with “Afaik”.
- **Left out:** Obsidian export shipping, timestamped TubeScribe quotes, TubeStoevsky's three files and gateway fixes, its unverified accuracy claims and remaining name error, the n8n OAuth/quota complaint, missing workflow JSON, and the images-plus-transcript suggestion. For example, Y09c explicitly says “Outputs matching .srt, .txt, and .md side-by-side.” These details affect setup and output requirements more than a general endorsement does.

## Fit for the user's agent workspace

- (inference) Separate extraction from the agent that summarizes. The local tools and n8n route demonstrate that the same transcript can feed different analysis stages.
- (inference) Preserve raw captions alongside cleaned text and Markdown. TubeStoevsky's multiple outputs provide a useful shape, but its accuracy claims need checks against originals.
- (inference) Distinguish missing captions, blocked fetching and model-output failures. Whisper, cookies/proxies and streaming address different reported problems.
- (inference) Require explicit timestamp fields in the eventual output contract. Only TubeScribe clearly promises timestamped quotes; JSON alone is not evidence of timestamps.
- (inference) Evaluate preservation of numbers, names and tangents before trusting prose conversion. The reported brand-name error is a concrete test case category.
- (inference) Treat managed services as candidates for testing, not proven reliability upgrades. Capture success/failure rates, elapsed time and actual cost before choosing one.
- (inference) Adapt entity Markdown export only when it helps the existing workspace. Automatic skill-file creation and visual graphs are ideas in these threads, not validated replacements for curated instructions.

## Best parts to read or watch first

- Y09d post and comments n6hcbmo / otxbxqc, about 2 minutes: actual IP-ban complaint, proxy suggestion and disclosed managed-service pitch.
- Y09c post and comments pd0lzui / pd66j78, about 3 minutes: exact commands, output files, gateway remedies and the unresolved fidelity question.
- Y09e post, about 1 minute: ordered workflow and concrete failures of earlier extraction attempts.
- Y09a Under the hood and comment oerbzns, about 1 minute: fallback route and shipped Markdown export.
- Y09b entire post, about 1 minute: concise local-storage design with timestamped quotes.
- Y09f comments oteemck / otegpmi / othm9oz, about 1 minute: route choices, carefully attributed blocking report and image sampling idea. Linked videos and repository examples have no verified reading or watching time in these captures.
