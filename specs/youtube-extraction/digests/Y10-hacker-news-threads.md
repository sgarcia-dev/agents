---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [Y10a, Y10b]
source_files: [sources/Y10a-hn-44381640.md, sources/Y10b-hn-48198790.md]
purpose: One-source digest feeding the spec compendium.
---

# Hacker News: audio transcription and YouTube MCP (Y10)

**What it is:** Two captured Hacker News discussions. Y10a is “OpenAI charges by the minute, so speed up your audio”, submitted by georgemandis on 2025-06-25. It contains 225 descendant comments across 1,367 capture lines. The requested [comment 44381640](https://news.ycombinator.com/item?id=44381640) belongs to story 44376989. Y10b is [“Show HN: YouTube MCP, give any AI agent access to YouTube”](https://news.ycombinator.com/item?id=48198790), submitted by umbertotancorre on 2026-05-19, with three descendant comments. Reading estimates below are digest estimates, not source measurements.

**Capture status:** Both captures say full. Y10a retains all 225 descendants returned by Algolia, including empty items, and the entire containing story rather than just the requested comment. Y10b retains all three returned descendants. The linked blog, repositories, pricing pages and example outputs are not captured here. Full discussion capture does not mean those linked materials were inspected.

## The point in three sentences

Extract available captions before paying to transcribe audio, but expect missing captions shortly after upload and formatting problems in some subtitle files. Audio transcription offers several local and hosted fallbacks, while speeding up audio has promising anecdotes rather than a completed accuracy study. The local YouTube MCP advertises convenient agent tools, but its tiny announcement thread does not establish resistance to YouTube blocking or reliable operation across videos.

## Key ideas

- Caption extraction can avoid downloading media. banana_giraffe, 2025-06-25, item 44381640: “You can use yt-dlp to get the transcripts.” Their command requests English captions in `json3` and also accepts playlist or channel URLs.
- Caption availability is a separate failure from access failure. rob, 2025-06-25, item 44379137: “we found that these automatic ones were never available though.” Their 1 to 3 hour council videos were processed within roughly 5 to 30 minutes of upload, which they offered as the likely explanation.
- A real deployment checks captions before transcribing. rob, 2025-06-25, item 44379336: “we do a check first and use youtube-transcript-api if there's an automatic one available”. This is stronger implementation evidence than a general tool recommendation.
- Server downloads can need additional session material. rob, 2025-06-25, item 44379137: “Runs smoothly every day.” The surrounding report says their Linode deployment passes cookies and a proof-of-origin token, called a “po token”, to yt-dlp. They had not regenerated them in over a month; this is one deployment, not a guaranteed expiry interval.
- The subtitle route has weak evidence about IP blocking. banana_giraffe, 2025-06-25, item 44382408: “Last time I ran this at scale was a couple of months ago”. They thought YouTube was less concerned about subtitle requests than bulk video downloads, but explicitly said the information might be outdated.
- Correct words do not guarantee usable subtitle structure. 55555, 2025-06-25, item 44379409: “Every sentence is repeated twice.” They also reported overlapping timestamp ranges. On 2025-06-26, item 44384176, they clarified: “It’s just the formatting that’s awful.” Their linked example was not English, and they did not know whether English was affected.
- Speeding audio may reduce billed duration and fit upload limits. georgemandis, 2025-06-25, item 44376990: “It worked quite well (Up to 3x speeds) and was cheaper and faster”. This describes a 40-minute talk and a reported 25-minute cap at that time, not a universal present-day limit.
- Speed has an accuracy cost that the thread does not measure. pbbakkum, 2025-06-25, item 44382153, identifies themselves as working on OpenAI's APIs: “there's probably a measurable decrease in transcription accuracy that worsens as you deviate from 1x speed.” The proposed formal tests were not completed in this capture.
- Local transcription has practical user evidence. godot, 2025-06-26, item 44389042: “On my m1 mac laptop it takes me about 30 seconds to run it on a 3-minute audio file.” On 2025-06-29, item 44414660, they confirm those times were with faster-whisper and a Python script.
- Silence removal needs its own quality check. w-m, 2025-06-25, item 44378345: “I measured only that the input file got shorter”. Their next comment corrects the original filter because padding was applied at the end rather than each cut. jwrallie separately reports fewer Whisper hallucinations after removing silence, meaning invented transcript text during quiet sections.
- Video-aware transcription can add information captions omit. mt_, 2025-06-25, item 44382623: “ask it to transcribe the video with speaker labels”. Their Google AI Studio suggestion also includes slide content and body language, explained on 2025-06-26, item 44384694. No benchmark accompanies it.
- MCP, a protocol for exposing tools to an AI client, wraps several YouTube operations. umbertotancorre, 2026-05-19, item 48198790: “No YouTube API key. No account. No signup.” This is the author's setup claim, not proof that every public video works without authentication.
- A CLI was announced after the MCP launch. umbertotancorre, 2026-05-21, item 48228577: “CLI available:”. The preceding claim that it would use fewer tokens is an expectation, not a measured comparison.
- Summaries serve selection better than complete learning. georgemandis, 2025-06-25, item 44380436: “There are so many more interesting ideas in there that resonated with me that the summary (unsurprisingly) skipped over.” Their later full viewing changed their assessment of the talk.

## How to do it (concrete steps, checklists, templates)

### Caption-first extraction

banana_giraffe gives this command in Y10a, item 44381640. The capture wraps it in stray literal backticks; the executable command below retains its command text:

```sh
./yt-dlp --skip-download --write-sub --write-auto-sub --sub-lang en --sub-format json3 <youtube video URL>
```

- Provide a video URL. The same command can receive a playlist or channel URL.
- Request subtitles and automatic subtitles, skip the media download, select English, and request `json3`.
- Cost: vjerancrnjak calls automatic-caption downloads free of charge, 2025-06-25, item 44378546. Installation steps, rate limits and operating costs are not supplied.
- Output: `json3` subtitle file. The capture contains no sample JSON or schema. Other comments report timestamped subtitle files, but do not establish this command's exact timestamp fields.
- Failures: captions may not exist yet; subtitle text can repeat with overlapping timing. IP blocking is raised as a question and answered only with an explicitly dated anecdote. No bot-check error or tested proxy solution is documented for this command.

### Deployed caption check, then hosted audio transcription

rob's sequence, Y10a items 44379137, 44379019 and 44379336:

1. Check available automatic captions with `youtube-transcript-api`, an unofficial API client.
2. If absent, download the highest-quality audio with yt-dlp.
3. On the remote Linode server, log into YouTube using a “clean” account and extract `cookies.txt` with their Python script.
4. Generate a “po token” using `iv-org/youtube-trusted-session-generator`; pass both session inputs to yt-dlp. They usually omit both when running at home.
5. Transcribe with Whisper through Groq. Fall back to Replicate or Deepgram when Groq errors.

Cost at the report date: roughly $0.02/hour for Groq `distil-large-v3`, $0.04/hour for `whisper-large-v3-turbo`, compared with roughly $0.36/hour through OpenAI. Server and backup-provider costs are unspecified. Output format, timestamp support and speaker labels are unspecified. Reliability evidence is daily operation for over a month without regenerating session inputs. Groq errors and unavailable captions are explicit failures. The server workaround suggests access constraints, but the comment does not quote an IP-block or bot-check error. The follow-up question about creating new accounts monthly is unanswered.

### Download audio, speed it up, transcribe through OpenAI

The thread describes `yt-dlp → ffmpeg → curl`, followed by `gpt-4o-transcribe`. The full script and cost breakdown are in the linked blog, not this capture. Do not invent missing install, authentication or request commands.

Cost: shorter audio was reported cheaper; exact paid totals are absent. karpathy's LLM-produced summary says roughly a third less cost and little quality loss, but it is a summary of the post, not an independent test. Output: dajonker reports a single continuous text result without conversation turns for their Dutch phone-call test. No JSON schema or timestamp guarantee is given. Failures: reported length cap, degraded accuracy at higher speeds, and names or places transcribed incorrectly in a separate comparison. This route still needs downloadable audio; it does not itself solve YouTube access failures. yashasolutions asks how to retain proper subtitle time codes, with no answer in the capture.

### Local Whisper routes

- **Python and faster-whisper:** Download model weights and run a local script. godot reports an M1 result and later confirms the library; meerab's VideoToBe.com pipeline uses yt-dlp, local OpenAI Whisper, then S3 storage and a custom viewer. No API fee is reported, but hardware and storage costs are not quantified. File format and timestamps are unspecified for these implementations. Tepix cites `int8, batch=8` and a 13-minute audio run in 51 seconds on CPU, without naming the CPU. No controlled reliability study is provided. Slow large-model execution on an older Intel Mac is a contrasting report from rob.
- **whisper.cpp with preprocessing:** jwrallie says normalize audio and remove silence, optionally using Audacity. They report improved quality and shorter processing, without exact settings or a sample transcript. No API pricing, output schema or timestamp behavior is specified. Silence-associated hallucinations are the reported failure; caption absence is irrelevant once audio is obtained.
- **Whisper.app:** ProllyInfamous reports a free drag-and-drop Apple Silicon installation, days of cassette audio processed, and text used to find timestamps worth listening to. Exact export format and timing accuracy are absent. This is local-audio evidence, not a demonstrated YouTube download route.
- **Browser Whisper:** dataviz1000 reports a Chrome extension using `huggingface/transformers.js`, OpenAI Whisper and WebGPU, a browser GPU interface. They call it free and describe ongoing local transcription. Setup code, model version, output format and failure measurements are absent. “It works perfect!” is an unmeasured author claim, item 44379634, 2025-06-25.

All local options need audio supplied separately. None establishes immunity to YouTube IP blocks or bot checks.

### Other hosted or video-aware routes

| Route | Setup actually stated | Cost stated | Output and reliability evidence | Failures or missing evidence |
|---|---|---|---|---|
| Google AI Studio YouTube input | Paste link; request transcript, speaker labels and visual clues | Not stated for this suggestion | mt_ describes the workflow; no output sample | No access, caption, IP or bot-check tests |
| Gemini summarization | Ask Gemini to summarize YouTube video | pottertheotter calls it free | “I do it all the time with YouTube videos.”, 2025-06-26, item 44383717 | Summary, not proven verbatim transcript; timing and JSON unspecified |
| Gemini 2.5 Pro audio | Upload audio to GCS, Google Cloud Storage; process it | Pro price absent; Flash described as cheaper | dajonker reports hour-plus Dutch calls and correctly labeled speakers, 2025-06-26, item 44385605 | Flash number errors; OpenAI name/place errors; not a YouTube access test |
| Manual YouTube transcript | Copy transcript below video | No price supplied for copying | pottertheotter's suggestion | No procedure when captions are absent; format and timing unspecified |
| Upload audio to YouTube | Use ffmpeg to make black-screen MP4; upload; use YouTube transcription; rebuild with Gemini Pro 2.5 | Claimed free YouTube transcripts; Gemini cost absent | appleaday1 says “This works VERY well for my needs.”, 2025-06-25, item 44378400 | No caption-delay, upload-limit, privacy or format evidence |
| Contentflow | Extract transcript with `contentflow.megalabs.co`; pass it to an LLM | Called free | isubkhankulov recommends identifying speakers, 2025-06-25, item 44382511 | No install, supported-input, format or failure details |
| NotebookLM | Use built-in text/video summarization | Called free by niutech, 2025-06-30, item 44418204 | Suggestion only | No extraction steps, transcript export or timing evidence |

The audio-to-YouTube command in item 44378400 uses `ffmpeg`, `-f lavfi`, `color=c=black:s=1920x1080:r=5`, WAV input, `libx264`, `-preset medium`, `-tune stillimage`, `-crf 28`, AAC at `192k`, `yuv420p`, and `-shortest`. It creates `file_you_upload_to_youtube_for_free_transcripts.mp4`; it does not show transcript retrieval commands.

### YouTube MCP and announced CLI

Y10b's sole setup command:

```sh
npx @umbertotancorre/youtube-mcp
```

The author says yt-dlp and ffmpeg are bundled automatically. Connect through an MCP-compatible client; no client configuration example is included. The server claims eight tools, summarized as full transcripts with optional timestamps, Markdown transcript download, metadata, caption search, and video/audio download. Cost is free, MIT licensed, with local execution and no key or account. JSON response structure, caption languages, unavailable-caption fallback and error handling are absent. No commenter reports successfully extracting a video. IP blocks, missing captions and bot checks are not tested or discussed. The CLI repository is announced, but no CLI command appears in this capture.

## Tools, code and commands named

- Extraction: `yt-dlp`, `youtube-transcript-api`, `cookies.txt`, `iv-org/youtube-trusted-session-generator`.
- Transcription: OpenAI Whisper, `openai-whisper`, `faster-whisper`, `whisper.cpp`, `whispercpp`, `Whisper.app`, Whisper “turbo”, `whisper large v3`, `distil-large-v3`, `whisper-large-v3-turbo`, `gpt-4o-transcribe`. georgemandis also writes `gpt-4o-transcription`; retain that distinction as source wording.
- Hosts named: Groq, Replicate, Deepgram, Deepinfra, Fal, Cloudflare Workers AI, Hugging Face's Inference API, Lemonfox.ai, speechischeap.com, soniox.com.
- Other models and interfaces: Gemini 2.0 Flash Lite, Phi 4 Multimodal, Gemini 2.5 Pro/Flash, Google AI Studio, NotebookLM, Audacity, Cursor, `huggingface/transformers.js`, WebGPU, VideoToBe.com, Contentflow.
- Agent integration: `@umbertotancorre/youtube-mcp`, `umbertotancorre/youtube-mcp-cli`, Claude, ChatGPT, OpenClaw. No package versions are pinned.
- Preprocessing: ffmpeg `silenceremove` and `apad`. w-m's corrected filter is `silenceremove=start_periods=1:stop_periods=-1:stop_duration=0.15:stop_threshold=-40dB:detection=rms`. It is proposed as a possible fix, not validated transcription code.
- Experimental model change: conjecTech suggests subsampling encoder context after a block in `whisper/model.py`. The supplied `x = x[,,::2]` is tentative source code, not a verified executable patch.

## Numbers and strong claims

- georgemandis, item 44376990: 40-minute talk, 25-minute cap, success up to 3x. Personal report, not an accuracy measurement.
- w-m, item 44378345: 39m31s reduced to 31m34s with silence removal. Duration measured; transcript quality explicitly untested. Original padding logic later corrected.
- rob, items 44379019/44379137: historical Groq $0.02 to $0.04/hour versus OpenAI $0.36/hour; daily server operation for over a month. No invoices or uptime logs provided.
- pzo, item 44380182, 2025-06-25: Cloudflare `whisper-large-v3-turbo` around $0.03/hour. Recommendation without a usage report.
- Tepix, item 44378872: 13 minutes in 51 seconds on CPU with faster-whisper `int8, batch=8`. Hardware and accuracy unspecified.
- godot, items 44389042/44414660: 3-minute audio in about 30 seconds on M1. The 5 to 10 minute estimate for a 40-minute talk is explicitly a guess.
- conjecTech, item 44384893, 2025-06-26: nearly double throughput with a relative roughly 4% increase in WER, word error rate. No test dataset or runnable demonstration is supplied.
- ilyakaminsky, item 44380550: speechischeap.com has a claimed 24-hour per-file limit. Commercial self-report; real-time diarization is later said unavailable, item 44501440.
- Lemonfox's speed, price and availability claims and raluk's soniox accuracy claim are promotional opinions without comparative evidence here.
- Y10b: eight tools, automatic dependency bundling, no credentials and free operation are author claims. Three descendant comments provide no independent reliability evidence.

## Compared with the deep research report

Only the report's Y10-linked passages were read: “B. yt-dlp remains a community staple” and the YouTube CLI/MCP entry in “5. Other tools worth knowing”.

- **Right:** The report says yt-dlp extracts subtitles “without downloading the actual video”. The captured command includes `--skip-download`. Its claim about playlist/channel URLs is directly supported by banana_giraffe's “playlist or channel URL”, item 44381640.
- **Right:** The report lists transcripts, timestamps, metadata and downloads for MCP/CLI. The MCP announcement explicitly offers “fetch full transcript, with or without timestamps”. The CLI's existence is supported by the later “CLI available:” comment.
- **Not established by these captures:** The report supplies `npx @umbertotancorre/youtube-cli transcript` and says “It also supports timestamped output and Markdown exports.” Y10b supplies only the MCP launch command and CLI repository announcement. Those CLI details may come from another source, but cannot be confirmed from this packet. “Small, relatively new project” is consistent with an announcement and sparse thread, not a measured adoption finding.
- **Overstated if treated as reliability evidence:** “yt-dlp remains a community staple” is broader than the specific captured deployment and recommendations. The subtitle-scale report warns its information is out of date. No source establishes present-day blocking behavior.
- **Important omissions:** The report's short HN section omits unavailable early captions, server cookies/token setup, Groq backup providers, duplicated subtitle sentences, overlapping timestamps, and the untested accuracy/time-code effects of speeding audio. Compare the report's convenient extraction framing with rob's “Sometimes groq errors out” and 55555's “Every sentence is repeated twice.”

## Fit for the user's agent workspace

- (inference) Copy the caption-first decision order, and record whether failure means missing captions, blocked access or unusable output. These require different fallbacks.
- (inference) Store the extraction route, capture time, requested language and original output alongside Markdown. This preserves evidence when a cheap worker cleans repeated captions.
- (inference) Use local transcription as a fallback candidate on existing hardware. Measure actual completion time and important-word accuracy before adopting the thread's speed claims.
- (inference) Evaluate extraction and summarization separately. georgemandis's proposed text comparison, repeated-run variance and theme checks suggest useful tests, but are not completed results.
- (inference) Treat 2x or 3x audio as an experiment. Require source time-code verification before letting workers cite the resulting timestamps.
- (inference) Try the CLI/MCP on a bounded video set before depending on it across harnesses. The thread does not supply a client configuration, response schema or failure contract.
- (inference) Keep free-service and hosted-price claims dated. The captures support historical reports, not current cost estimates.
- (inference) Use summaries to choose what deserves full reading or viewing. The discussion itself demonstrates meaningful omissions from an initially satisfactory summary.

## Best parts to read or watch first

- Y10a, fallinditch branch, items 44378501 through 44382408: caption command, playlist support, server session setup and IP-block uncertainty. About 4 minutes.
- Y10a, rob branch, items 44379019 through 44384523: caption-first deployment, Groq prices, fallback providers and hardware tradeoffs. About 4 minutes.
- Y10a, 55555, items 44379409 and 44384176: repeated text and overlapping subtitle timestamps. About 1 minute.
- Y10a, pbbakkum/georgemandis, items 44382153 and 44384158: accuracy warning and proposed tests. About 2 minutes.
- Y10a, w-m, items 44378345 and 44378587: silence-removal command and its correction. About 2 minutes.
- Y10b, entire thread: MCP setup and CLI announcement. About 2 minutes. No linked repository review is included.
