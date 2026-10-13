---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [Y11a, Y11b, Y11c, Y11d]
source_files:
  - sources/Y11a-hermes-youtube-content-references-output-formats.md.md
  - sources/Y11a-hermes-youtube-content-scripts-fetch_transcript.py.md
  - sources/Y11a-hermes-youtube-content-SKILL.md
  - sources/Y11b-agent-reach-README_en.md
  - sources/Y11b-agent-reach-README.md
  - sources/Y11c-agent-reach-issue-566.md
  - sources/Y11d-youtube-mcp-cli-README.md
purpose: One-source digest feeding the spec compendium.
---

# Hermes skill, Agent Reach, and YouTube MCP/CLI (D-Y11)

**What it is:** Seven captures covering three tools and one field report. All were captured on 2026-10-13. Y11a is NousResearch's Hermes `youtube-content` skill, helper code, and output examples; the skill credits Teknium (teknium1), version 1.0.0. Publication dates are unknown. [Skill](https://github.com/NousResearch/hermes-agent/blob/main/skills/media/youtube-content/SKILL.md), [helper](https://github.com/NousResearch/hermes-agent/blob/main/skills/media/youtube-content/scripts/fetch_transcript.py), [examples](https://github.com/NousResearch/hermes-agent/blob/main/skills/media/youtube-content/references/output-formats.md). Y11b is Panniantong's [Chinese README](https://github.com/Panniantong/Agent-Reach) and [English README](https://github.com/Panniantong/Agent-Reach/blob/main/docs/README_en.md), dates unknown. Y11c is [issue #566](https://github.com/Panniantong/Agent-Reach/issues/566), opened by bluesxu on 2026-08-04, with two maintainer replies on 2026-08-06. Y11d is umbertotancorre's [YouTube MCP server and CLI README](https://github.com/umbertotancorre/youtube-mcp-cli), date unknown. Combined captures: 1,494 lines including metadata, code, and markup. No source gives a reading time.

**Capture status:** All seven frontmatters say full. Y11c includes all two comments. Y11d records 33 stars and no published stable release at capture. No omitted capture content is reported. Linked installation guides, package-management documentation, PR #575, and underlying CLI implementations are outside this packet.

## The point in three sentences

Hermes already has a small caption-fetching helper, but its real JSON output differs from its example schema. Agent Reach's issue shows why extraction needs a bounded fallback chain and checks for actual content: yt-dlp and OpenCLI each succeeded for one tester and failed for another. YouTube MCP/CLI offers convenient local interfaces, but this README provides no measured reliability evidence or transcription fallback.

## Key ideas

- Hermes separates extraction from writing summaries, chapters, threads, blogs, and quotes. The skill describes its purpose as "YouTube transcripts to summaries, threads, blogs." (Y11a SKILL, description).
- Hermes requires a prepared Python environment rather than ad hoc dependency repair. "below with the interpreter whose import check succeeded." (Y11a SKILL, Setup).
- The helper supports URL variants and raw IDs, plus an ordered language list. Its code says "Compatible with youtube-transcript-api v1.x." (Y11a helper, `fetch_transcript` docstring).
- The helper's introductory JSON example promises language and segment records, but `main()` emits neither. Its actual construction includes the exact code `"segment_count": len(segments)` (Y11a helper, `main`); segment text/start/duration records remain internal.
- Hermes tells the agent to check language and content before transformation. "confirm the output is non-empty and in the expected language." (Y11a SKILL, Workflow step 2). There is no dedicated bot-check, proxy, or audio fallback in the captured helper.
- Agent Reach organizes tool choice and installation while the agent invokes the underlying tools. "there is no wrapper layer." (Y11b English, Design Philosophy). This distinction matters when assigning responsibility for failures.
- Its README promises health checks, but the issue exposes limits. bluesxu reports "退出码 0 ≠ 拿到内容" (Y11c, P0-2, 2026-08-04), meaning exit code zero does not mean content was obtained.
- bluesxu's yt-dlp caption attempt returned "Sign in to confirm you're not a bot" (Y11c, P0-2, 2026-08-04). Switching four player clients did not fix that test.
- OpenCLI worked for the reporter, but was intermittent. bluesxu quotes "Caption URL returned empty response" (Y11c, P0-2, 2026-08-04) and reports roughly one-third to one-half of attempts failed before retries.
- The maintainer rejected universal replacement of yt-dlp. Panniantong reports "当前 yt-dlp 成功生成了 14.46 KiB 非空字幕" (Y11c, comment 2026-08-06T09:23:20Z), meaning current yt-dlp generated 14.46 KiB of non-empty captions.
- The resulting route was "yt-dlp → OpenCLI 最多 3 次 → 音频转写" (Panniantong, same comment), meaning yt-dlp, then OpenCLI at most three times, then audio transcription. The following comment says the fix merged to main.
- YouTube MCP/CLI exposes captions, metadata, caption search, and media downloads. "All locally. No API keys required." (Y11d, introduction). Local execution does not establish resistance to YouTube blocking.
- The new CLI has clear timestamped text interfaces. "Include [MM:SS] timestamps" (Y11d, CLI Commands). Only metadata is explicitly documented with a JSON flag.

## How to do it (concrete steps, checklists, templates)

### Hermes caption extraction

Follow the skill's setup order. First use a package-management-prepared source checkout and follow its linked isolated development-home procedure. That external procedure is not captured. Then:

```bash
source ./activate
python -c "import pm; pm.sync_venv(['youtube'], explicit=True)"
source ./activate
python -c "import youtube_transcript_api; print(youtube_transcript_api.__file__)"
```

On Windows the skill substitutes `. .\activate.ps1`. A different host or sandbox needs its own isolated helper environment. Do not install into Hermes with raw pip or project-discovering `uv run`.

The workflow is fetch, validate, chunk when needed, transform, verify:

```bash
python SKILL_DIR/scripts/fetch_transcript.py "URL" --text-only --timestamps
python SKILL_DIR/scripts/fetch_transcript.py "URL" --language tr,en
```

- Validate non-empty output and expected language. The written workflow says retry without `--language` if empty, then report likely disabled transcripts if still empty.
- Above roughly 50K characters, split into roughly 40K-character chunks with 2K overlap. Summarize each, then merge.
- Default to a summary if no format was requested. Re-read for coherence, timestamps, and completeness.
- Disabled captions: tell the user and suggest checking subtitles on the page. Private/unavailable video: relay the error and request URL verification. Missing language: retry without the language option and report the actual language. Missing dependency: repeat preparation and activation.

**Cost:** No monetary rate, API fee, latency, or compute estimate is given. Summary generation cost is also unstated.

**Output:** Default JSON contains `video_id`, `segment_count`, `duration`, and `full_text`; `--timestamps` adds `timestamped_text`. Plain mode prints full text, or one timestamped line per segment. Timestamps truncate fractional seconds and use `M:SS` or `H:MM:SS`. Duration is the last segment's start plus duration, not verified video metadata. The introductory schema includes `language` and `segments`, but the implementation does not emit them. The default library fetch is used when no language is specified; the code does not implement a search across every available language, despite the skill's retry wording.

**Failures and reliability:** Import failures exit 1 with stderr guidance. Fetch exceptions produce an error JSON object and exit 1, even in text-only mode. Empty segments can still yield a successful empty transcript. No specific IP-block or bot-check handling exists beyond passing through the exception text. No audio transcription route or measured success rate is supplied. Output-format examples are templates, not evidence of extraction success.

### Agent Reach and yt-dlp captions

The English README gives this manual setup:

```bash
pip install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto
```

Python 3.10+ is shown. The Chinese README says install this repository, not the unrelated same-name PyPI package. Installation includes yt-dlp and feedparser, checks Node.js, gh CLI, and mcporter, detects local versus server environments, and only installs system dependencies/configuration with explicit `--system`. Its skill route is `npx skills add Panniantong/Agent-Reach@agent-reach`. `agent-reach doctor` checks status. The default check does not register skill files; `--system` can.

**Cost:** The README claims all tools and APIs are free, with a possible server proxy around $1/month. The English proxy section narrows need to restricted networks; the Chinese README broadly says servers need proxies. Neither demonstrates a YouTube-specific proxy fix or gives transcription quotas.

**Output:** The English README presents `yt-dlp --dump-json URL` as a subtitle route, but provides no transcript schema or evidence that this command alone returns subtitle text. The issue tests `yt-dlp --write-sub --write-auto-sub`, producing subtitle files; their exact format and timestamp schema are not captured.

**Failures and reliability:** bluesxu, 2026-08-04, Windows 10/Git Bash/Chrome/Python 3.12/Agent Reach v1.5.0, reports bot checks, Chrome cookie decryption failure, four failed client variants, and empty direct caption responses. Panniantong, 2026-08-06, reports non-empty yt-dlp captions on one public test video. These are opposing observations, not population success rates. Search via `--flat-playlist` still worked for bluesxu, so a search test cannot prove caption health. No YouTube IP-block measurement appears; Reddit/Bilibili IP-block claims cannot be transferred to YouTube.

### OpenCLI captions and direct caption URL attempts

The reporter's environment had desktop Chrome plus the OpenCLI extension. No complete OpenCLI installation procedure is captured. The successful command was:

```bash
opencli youtube transcript "https://www.youtube.com/watch?v=VIDEO_ID" -f yaml
```

**Cost/output:** No OpenCLI price is stated. The reported YAML has `timestamp`, `speaker`, and `text`. One 13-minute video yielded 37 segments and about 14,000 characters. No JSON output example is given.

**Failures/reliability:** bluesxu reports roughly 1/3 to 1/2 failure frequency, expired caption URL parameters, and recovery with retries. Panniantong saw an empty OpenCLI response while yt-dlp succeeded. The maintainer's chain caps OpenCLI at three attempts and requires non-empty content.

The separate direct URL attempt extracted `captionTracks[0].baseUrl` from the page and fetched it. No full setup or command is supplied; cost is unstated. The result was HTTP 200 with zero body length. bluesxu attributes this to a missing `pot` proof-of-origin token, a token used to establish request origin. This is the reporter's explanation, not an independently verified fix. Output was empty; no usable timestamp or JSON result is evidenced.

### Audio transcription fallback

Panniantong's chain ends with audio transcription. The issue also compares direct Groq `whisper-large-v3` use in `transcribe.sh` with:

```bash
agent-reach transcribe <音频URL>
```

The placeholder means audio URL. The script requires `GROQ_API_KEY` or configured `groq_api_key`; `brew install ffmpeg` is mentioned as a prerequisite. The README calls Groq Whisper free for podcast transcription. No YouTube-specific audio-download-to-transcription recipe, model rate, quota, timestamp output, or JSON schema is captured.

bluesxu reports repeated HTTP 500 responses through the script but full-text success through `agent-reach transcribe` on the same audio. Windows failures involved interpreter discovery, POSIX paths passed to Windows Python, suppressed config-read errors, and missing `bc`. Panniantong says fixes added interpreter detection, `cygpath` conversion, removal of `bc`, and a unified transcription fallback for 5xx errors. Audio download can still fail before transcription; the packet supplies no demonstrated bot-check or IP-block solution for that stage.

### YouTube MCP/CLI

Requires Node >=18. MCP means a standard interface through which an agent calls tools. Run the server with `npx @umbertotancorre/youtube-mcp`, or configure command `npx` and arguments `["-y", "@umbertotancorre/youtube-mcp"]` in the chosen client. CLI setup and use:

```bash
npm install -g @umbertotancorre/youtube-cli
youtube-cli --help
youtube-cli transcript <url> --timestamps
youtube-cli transcript <url> --save
youtube-cli transcript <url> --language it
```

One-off use is `npx @umbertotancorre/youtube-cli transcript dQw4w9WgXcQ`. The README says npm installation automatically downloads yt-dlp and ffmpeg for media downloads.

**Cost/output:** MIT-licensed, local, no API key/account; no monetary cost, runtime, or bandwidth estimate. Transcripts are plain text, optionally `[MM:SS]` per segment, or saved Markdown. Caption search returns matching segments with timestamps. Metadata supports `--json`; transcript JSON is not documented. Video output is `.mp4`; audio includes `.mp3`, `m4a`, `flac`, and `opus`. Downloads go to the platform's Downloads directory.

**Failures/reliability:** Only public data is supported. The README says it does not bypass authentication, paywalls, or age gates. Missing captions, IP blocks, bot challenges, retry policy, and speech transcription are not addressed. No user reports or extraction benchmarks appear. The capture's 33 stars and lack of stable release describe maturity, not correctness.

## Tools, code and commands named

- Hermes: `youtube-content` 1.0.0, `fetch_transcript.py`, `youtube-transcript-api` v1.x, `YouTubeTranscriptApi().fetch`, `pm.sync_venv`, `--language`/`-l`, `--timestamps`/`-t`, `--text-only`.
- Agent Reach: v1.5.0 in the report, `agent-reach doctor --json`, `check-update`, `agent-reach install --env=auto --system`, `--safe`, `--dry-run`, `AGENT_REACH_LANG=en`, `agent-reach skill --install`. Suggested `doctor --probe` and a generic `agent-reach env` were not added by the maintainer.
- Caption attempts: `yt-dlp --cookies-from-browser chrome`, `--write-sub --write-auto-sub`, `--flat-playlist`; player clients `web_safari`, `tv_embedded`, `ios`, `mweb`; `opencli list`, `opencli <平台> --help`.
- Transcription: `transcribe.sh`, Groq, `whisper-large-v3`, ffmpeg, `GROQ_API_KEY`, `cygpath -w`, `python3/python/py -3`, `awk`, `bc`.
- MCP tools: `get_transcript`, `get_transcript_timed`, `download_transcript`, `download_transcript_timed`, `get_metadata`, `search_transcript`, `download_video`, `download_audio`. CLI also provides `youtube-cli metadata <url> --json`, `youtube-cli search <url> <query>`, and `youtube-cli download <url> --audio --format flac`.

## Numbers and strong claims

- Hermes Workflow: 50K-character threshold, 40K chunks, 2K overlap. Summary: 5 to 10 sentences; thread posts: under 280 characters. These are formatting instructions, not quality measurements.
- bluesxu, Y11c Summary/Environment: 15 channels tested, eight problems, on 2026-08-04. P0-1 reports eight null backend values. A latest-version check did not prove working extraction.
- bluesxu, P0-2: 13-minute video, 37 segments, about 14,000 characters; approximate 1/3 to 1/2 OpenCLI failure frequency. Attempt count and sampling method are absent.
- Panniantong, 2026-08-06T09:23:20Z: 14.46 KiB of non-empty yt-dlp captions, 436 tests passed. Next comment reports merge `3fc3c32` and green Python 3.10–3.13/wheel checks. These are maintainer reports; tests do not establish general live YouTube reliability.
- Y11b Current Tool Choices calls yt-dlp "still the best for YouTube" and cites 154K stars; Supported Platforms cites 148K and 1800+ sites. Best is opinion, and popularity/site coverage is not caption success evidence.
- Y11b's "Completely free" and Y11d's "Zero Setup" are marketing claims. Dependencies, environment preparation, and external service limits still need examination.
- Sponsor CoreClaw advertises YouTube collection, JSON/CSV, billing only for successful results, and a $3 trial. No setup, unit prices, timestamp details, failures, or reliability evidence are captured. It is advertising, not a validated extraction route.

## Compared with the deep research report

- **Right:** Y00 says Hermes provides "text/JSON output" and supports timestamps and languages. Y11a implements those options. Y00's conclusion that fallback strategy and standard output need improvement is consistent with the missing emitted segment/language fields and lack of audio fallback.
- **Right but incomplete:** Y00 says the issue documents "bot challenges and empty caption responses". bluesxu's P0-2 confirms both. Y00 leaves out the maintainer's opposing live result, the three-attempt cap, and the merged correction. The captured chain is "yt-dlp → OpenCLI 最多 3 次 → 音频转写" (Panniantong, 2026-08-06).
- **Overstated if read as installation evidence:** Y00 says "you may not need to add anything to Hermes". Y11a Setup still requires the isolated developer-home procedure, the `youtube` extra, reactivation, and an import check. A shipped skill does not prove a ready interpreter.
- **Right:** Y00 lists YouTube CLI/MCP as offering "transcripts, timestamps, metadata and downloads". Y11d documents all four. Its small-project caveat is supported by capture metadata; relative age cannot be verified because publication date is unknown.
- **Left out:** Y00 does not distinguish transcript text from metadata JSON, give Hermes's actual emitted schema, or note the README/issue disagreement about YouTube fallback routes. Y11b still shows yt-dlp with no fallback while the later issue comments describe the merged chain.
- Y00's Hermes community discussion is not among these captures. Its user reports cannot be independently checked within this packet.

## Fit for the user's agent workspace

- (inference) Copy Hermes's fetch, validate, transform, verify stages into a shared procedure. Keep extraction evidence separate from generated summaries.
- (inference) Define one transcript schema before reusing the helper. Preserve timed segments and actual language explicitly; the current helper does not emit them.
- (inference) Adapt the maintainer's bounded route: yt-dlp, OpenCLI up to three attempts, audio transcription. Record each attempted route and why it failed.
- (inference) Require meaningful non-empty transcript content. Do not accept successful search, HTTP 200, or an exit code as proof.
- (inference) Keep environment and dated test evidence beside routing decisions. These reports show that a universal winner cannot be inferred from one host.
- (inference) Consider the small CLI interface for several harnesses, but test captions locally before adopting it. The README alone cannot establish reliability.
- (inference) Skip broad Agent Reach installation if only YouTube extraction is needed. Its tool-selection pattern is useful independently of its many-platform setup.

## Best parts to read or watch first

Reading estimates below are inference; the sources supply none.

- Y11c P0-2 and both Panniantong comments: about 4 minutes. Read the failure report and correction together.
- Y11a helper `main()` and `fetch_transcript()`: about 3 minutes. Establish the actual output and error behavior.
- Y11a SKILL Setup, Workflow, Error Handling: about 3 minutes. Establish environment preparation and validation.
- Y11d MCP Tools and CLI Commands/Installation: about 2 minutes. Compare interfaces and output options.
- Y11b English Design Philosophy and Chinese Quick Start installation list: about 3 minutes. Understand routing responsibility and installation side effects.
