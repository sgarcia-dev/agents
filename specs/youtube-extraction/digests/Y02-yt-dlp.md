---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [Y02a, Y02b]
source_files: [sources/Y02a-yt-dlp-README.md, sources/Y02b-yt-dlp-wiki-EJS.md]
purpose: One-source digest feeding the spec compendium.
---

# yt-dlp README and External JS Scripts Setup Guide (Y02)

**What it is:** Official project documentation: [yt-dlp README](https://github.com/yt-dlp/yt-dlp) and [External JS Scripts Setup Guide](https://github.com/yt-dlp/yt-dlp/wiki/EJS). Both captures record author and publication date as unknown. Captured 2026-10-13. Markdown reference material, about 20,500 words combined, mostly command options. Reading the relevant extraction and setup sections is more useful than reading every option.

**Capture status:** Both full. Y02a says the README was preserved byte-for-byte and independently matched the raw GitHub copy. Y02b includes the final Plugins section and developer API note. No missing sections are declared. Neither capture includes issue threads, dated user reports, extraction test results, or prices for running infrastructure.

## The point in three sentences

yt-dlp can download existing subtitles, extract structured metadata, and download audio or video. Full YouTube support requires both EJS, the external JavaScript challenge solver scripts, and a supported JavaScript runtime, a program that executes those scripts. These documents explain the supported setup and known limitations, but do not establish a measured success rate or promise that correct setup defeats every access block.

## Key ideas

- Captions are separate from media downloads. Combine the subtitle options with `--skip-download` to write related files while avoiding the video download. Quote: "Do not download the video but write all" (Y02a, Verbosity and Simulation Options, `--skip-download`; continued on the next line).
- Manual and automatic subtitles have separate switches. Neither is written by default, and available language tags can be inspected first. Quote: "Write automatically generated subtitle file" (Y02a, Subtitle Options, `--write-auto-subs`).
- Simulation is different from skipping media. Simulation prevents all disk writes, so it is unsuitable when the goal is to save captions. Quote: "Do not download the video and do not write" (Y02a, Verbosity and Simulation Options, `--simulate`; next line says anything to disk).
- Use a defined machine output for agent integration. Ordinary console messages may change; JSON and explicit print templates provide a clearer contract. Quote: "Your program should avoid parsing the normal stdout since they may change in future versions." (Y02a, Embedding yt-dlp).
- A Python extraction result needs conversion before JSON serialization. The source does not guarantee that `extract_info` returns a dictionary or a JSON-ready object. Quote: "pass it through `YoutubeDL.sanitize_info`" (Y02a, Embedding yt-dlp).
- YouTube challenge handling is now an external dependency. EJS replaces the old JSInterp and PhantomJS approach for YouTube. Quote: "To download from YouTube, yt-dlp needs to solve JavaScript challenges presented by YouTube using an external JavaScript runtime." (Y02b, introduction).
- Installation method determines whether EJS needs extra setup. Official bundled executables and the Unix zipimport binary include it; third-party packages may not. Quote: "No additional action required." (Y02b, Step 2 distribution table, official executable rows). A runtime still needs installation.
- Deno is the default enabled runtime. Node, QuickJS and Bun need explicit enabling; runtime priority can still select Deno if it is available. Quote: "Only \"deno\" is enabled" (Y02a, General Options, `--js-runtimes`; next line says by default).
- Runtime choices have different constraints. Deno restricts permissions, Node restricts some permissions, and Bun does not restrict them. Quote: "Scripts have full file system and network access." (Y02b, bun, Notes).
- EJS updates must remain compatible with yt-dlp. Installing an old companion package can cause yt-dlp to ignore it. Quote: "old versions will be ignored by yt-dlp." (Y02b, Option 1 warning).
- Stable releases can break as sites change. The project recommends nightly releases for regular users and requires trying nightly before reporting stable-release problems. Quote: "the latest `stable` release is often \"stale\" and prone to external breakage" (Y02a, Update).
- Reducing requests can reduce completeness. Skipping player requests may help with rate limits, but can lose formats or metadata. Quote: "they could cause issues such as missing formats or metadata." (Y02a, Extractor Arguments, youtube, `player_skip`).
- JavaScript challenges and PO tokens are distinct documented mechanisms. A Proof of Origin token has separate contexts for media URLs, player requests and subtitles. Quote: "`subs` (Subtitles)" (Y02a, Extractor Arguments, youtube, `po_token`). The captures give token syntax, not a full token acquisition procedure.
- A channel or playlist introduces completeness and scope concerns. Flat extraction can omit metadata, and channel URLs include shorts and live uploads. Quote: "some entry metadata may be missing" (Y02a, General Options, `--flat-playlist`).

## How to do it (concrete steps, checklists, templates)

### Shared setup, in the EJS guide's order

1. Install a supported JavaScript runtime. Put its executable in `PATH`, beside `yt-dlp.exe` on Windows, or specify its path with `--js-runtimes`.
2. Install or enable the EJS challenge solver scripts using the route appropriate to the yt-dlp distribution.

| Runtime | Setup and version | Documented limitations |
| --- | --- | --- |
| Deno | Minimum `2.3.0`; enabled by default. Optional `--js-runtimes deno:/path/to/deno`. Download `deno`, not `denort`. | Restricted permissions; supports npm EJS downloads. No success-rate evidence. |
| Node | Minimum `22.0.0`; enable `--js-runtimes node` or `--js-runtimes node:/path/to/node`. | Some permissions restricted. npm EJS download route is not supported by this guide. |
| QuickJS / QuickJS-NG | QuickJS minimum `2023-12-9`; all QuickJS-NG versions supported. Enable `--js-runtimes quickjs` or provide the executable path. | QuickJS before `2025-4-26` and QuickJS-NG before `0.12.0` can take several minutes. Temporary script files create a theoretical file-replacement risk between checking and using a file. Executable must be named `qjs`, or its full file path supplied. |
| Bun | `1.2.11` through `1.3.14`; enable `--js-runtimes bun`. | Deprecated; newer versions unsupported. Full filesystem/network access; no SOCKS proxy support for npm dependency downloads. |

The README gives runtime priority as Deno, Node, QuickJS, Bun. To choose a lower-priority runtime when Deno exists, pass `--no-js-runtimes` before enabling the other runtime.

| EJS installation route | Setup | Cost and failure evidence |
| --- | --- | --- |
| Official executables | EJS is already bundled in PyInstaller executables and the Unix zipimport executable. Install the runtime separately. | No per-request price documented. Bundling is a setup statement, not reliability testing. |
| PyPI companion package | `pip install -U "yt-dlp[default]"`. This installs and upgrades EJS with yt-dlp. | No price documented. Direct `yt-dlp-ejs` installation must match the supported version in that yt-dlp release's `pyproject.toml`; stale versions are ignored. |
| npm download | Supply `--remote-components ejs:npm`, optionally in configuration for automatic updates. Only Deno and Bun support it. | No price or success rate documented. Requires package downloads; Bun cannot use SOCKS proxies for this step. |
| GitHub download | Supply `--remote-components ejs:github`, optionally in configuration for automatic updates. | No price or success rate documented. May fail when GitHub/release assets are inaccessible, including an IPv6-only IP setup. |
| Alternative plugin | Guide names `yt-dlp-apple-webkit-jsi` by grqz. README describes plugin installation directories and pip installation; check loading with `--verbose`. | No price, exact plugin install command, or measured results supplied. Described as experimental and expected to work on most Apple devices. Only the base challenge-provider API is public; the EJS hook API is private and may break. |

Remote component fetching is disabled by default. The alternative plugin is a challenge-provider option, not a separate transcript service.

### Extraction routes and their outputs

The following switches and examples come from the README. They are not a source-provided end-to-end transcript recipe.

| Route | Setup and operation | Output and timestamps | Cost, failures and reliability evidence |
| --- | --- | --- | --- |
| Existing subtitles | Shared YouTube setup; inspect `--list-subs`; use `--write-subs`, select `--sub-langs`, choose `--sub-format`, and use `--skip-download` when only related files are needed. | Subtitle files. Source gives preferences such as `srt` and `ass/srt/best`; conversion supports `ass`, `lrc`, `srt`, `vtt`. No sample caption file or cue timestamp schema is captured. | No per-call charge documented; software licensing is stated. Missing-caption behavior, bot-check frequency and IP-block frequency are not quantified. Availability listing is documented, but completeness is not tested. |
| Automatically generated subtitles | Same setup; use `--write-auto-subs`, with language/format selection and `--skip-download`. Auto-translated subtitles can be skipped using youtube extractor argument `skip=translated_subs`. | Automatically generated subtitle files. No caption accuracy scores, cue samples or JSON transcript schema. | No documented price. Does not promise to generate new speech transcription when captions are absent. No evidence that it bypasses missing captions, IP blocks or all bot checks. |
| Metadata, descriptions and comments | Use `--dump-json` for each video, `--dump-single-json` for each URL, or `--write-info-json` for a file. `--write-description` saves descriptions; `--write-comments` retrieves comments into infojson. | JSON to stdout, `.info.json`, or `.description`. Metadata includes upload timestamps, duration, availability, URL and extraction epoch when available. These are not caption cue timestamps. Comment content is not the spoken transcript. | No documented per-call price. Fields are not guaranteed. `--ignore-no-formats-error` can extract metadata without downloadable formats but is experimental. Comments may require extra retrieval. No measured IP/bot reliability. |
| Audio download | Shared setup plus real `ffmpeg` and `ffprobe` binaries for `-x`. Select `--audio-format`; source's Python example selects `m4a/bestaudio/best` and `FFmpegExtractAudio` with `preferredcodec: m4a`. | Audio files, including `m4a`, `mp3`, `opus`, `wav` and other listed formats. No transcript text, speech timestamps or transcription JSON produced by this documented route. | No price documented; bandwidth, compute and transcription cost are not measured. Missing captions do not supply audio access. Missing dependencies, unavailable formats and access requirements remain relevant. No IP/bot success-rate evidence. |
| Video, sections, playlists and channels | Shared setup; `yt-dlp [OPTIONS] [--] URL [URL...]`; default best-quality selection. Merging audio/video and `--download-sections` require ffmpeg. Select playlist items or provide a specific channel tab to bound scope. | Media files; optional subtitle and metadata files. Sections use time ranges or chapters, with numeric `section_start` and `section_end` in seconds. Playlist JSON can be one line through `-J`. | No price documented. Default behavior skips unavailable fragments and continues to the next video after download errors. Live-from-start is experimental. Format, authentication and geography limits apply; no completeness benchmark or IP/bot success rate. |
| Python embedding | Import `YoutubeDL`; source example calls `extract_info(URL, download=False)`, then `sanitize_info` before `json.dumps`. Download examples use `ydl.download(URLS)`. | Serializable metadata after sanitization, or the same media files as CLI routes. No separate transcript format or improved access mechanism claimed. | No price or comparative reliability evidence. Shares extraction limitations. Raw return values need not be JSON serializable. |

For all routes, the source documents HTTP/HTTPS/SOCKS proxies, browser cookies, request delays and subtitle delays. It does not demonstrate that these fix an IP block or a sign-in/bot check. Some YouTube clients require authentication or PO tokens; changing clients is not a guaranteed bypass. The age-restriction workaround is explicitly described as working only sometimes.

## Tools, code and commands named

- Installation: binaries, pip and third-party package managers; `yt-dlp_macos` requires macOS `10.15+`. CPython `3.10+` and PyPy `3.11+` are supported.
- Updates: `yt-dlp -U`, `yt-dlp --update-to nightly`, and `python -m pip install -U --pre "yt-dlp[default]"`.
- Extraction controls: `--skip-download`, `--simulate`, `--list-subs`, `--write-subs`, `--write-auto-subs`, `--sub-langs "en.*,ja"`, `--sub-langs all,-live_chat`, `--sub-format`, `--convert-subs`, `--dump-json`, `--dump-single-json`, `--write-info-json`, `--write-comments`.
- Audio and media: `ffmpeg`, `ffprobe`, `-x`, `--audio-format`, `-f "bv+ba/b"`, `--download-sections "*10:15-inf"`, `--split-chapters`, `--print after_move:filepath`.
- Troubleshooting: `--verbose`, `--extractor-retries`, `--retry-sleep`, `--sleep-requests`, `--sleep-subtitles`, `--cookies-from-browser`, `--proxy`, `--extractor-args`, `jsc_trace`, `pot_trace`.
- Integration: `yt_dlp.YoutubeDL`, `extract_info`, `sanitize_info`, `download_with_info_file`, `devscripts/cli_to_api.py`, logger and `progress_hooks` examples.

## Numbers and strong claims

- Capture metadata: `197288` GitHub stars; latest release tag `2026.08.19`, dated `2026-08-19T23:48:43Z`. This is capture-time adoption/release evidence, not an extraction reliability measure.
- Introduction: support for thousands of sites. A project scope claim, not a count of tested YouTube caption cases.
- Update: stable is mostly monthly, nightly publishes on days with code changes, master after each push. Versions older than 90 days trigger an update warning. These describe maintenance policy.
- Download/Extractor Options: default download retries `10`, fragment retries `10`, file-access retries `3`, extractor retries `3`. Retries are controls, not proof of successful recovery.
- EJS runtime minimums and QuickJS delay thresholds appear in the setup table above. The claim of several-minute execution on older QuickJS versions is a documented warning without benchmark data.
- Deno is recommended; nightly is recommended for regular users. These are maintainer recommendations, not comparative experimental results.
- User reports: none in Y02a or Y02b. Author/date quotations cannot be supplied from these captures. grqz is named as a plugin author, not as the author of a dated success report.

## Compared with the deep research report

Comparison is limited to its yt-dlp discussion and Option B. Community reports mentioned there were not independently read in this packet.

- Correct capability summary: report says "This requests English subtitles without downloading the video." README supports this with subtitle switches and `--skip-download`, whose description continues with "related files". Metadata and audio routes are also documented.
- Correct dependency summary: report says "Deno is recommended." EJS guide labels Deno recommended and enabled by default; README calls EJS "Required for full YouTube support." The report also correctly warns that package-manager installations may lack EJS.
- Setup is incomplete: report's `brew install yt-dlp deno` and audio conversion note omit `ffprobe` and exact EJS/runtime compatibility details. README says audio conversion "requires ffmpeg and ffprobe". EJS warns "The version MUST be a supported version as per yt-dlp's pyproject.toml file."
- Timestamp assertion has limited support in this packet: report says "a `.vtt` subtitle file containing text and timestamps." README names `vtt` as a conversion target but supplies no VTT cue example or timing preservation test. Do not treat the report's usual-output claim as measured evidence from these captures.
- Reliability needs separate evidence: report says "bot challenges and empty caption responses" in an August 2026 Agent-Reach issue. Neither assigned capture contains that thread, its author, dated quotations or test results. The claim is unverified here, not disproved. EJS establishes JavaScript challenge handling, not universal bot-check recovery.
- Report's ranking "Free" and "Easy" needs qualification. README states licensing, not operating costs. EJS has several dependency routes, version constraints and network limitations. Ease is a judgment, not a documented benchmark.
- Important omissions: nightly guidance, stale-EJS rejection, Bun deprecation, Node enabling, runtime priority, GitHub IPv6 limitation, subtitle PO-token context, structured-output advice, Python sanitization and flat-playlist metadata gaps.
- Report mentions community subtitle recommendations dated June 25, 2025 and a September 2026 cleanup pipeline. This packet contains no original author/date quotations for either. The report's paraphrases cannot be presented as verbatim user reports.

## Fit for the user's agent workspace

- (inference) Build one bounded CLI procedure that records yt-dlp version, runtime, EJS route, requested language and actual output files. This makes setup failures distinguishable from content failures.
- (inference) Preserve raw subtitle files before any cleanup. Validate timing and caption completeness on real examples because this packet has no cue-level tests.
- (inference) Return JSON or explicit print templates to TypeScript workers. Keep ordinary console text as diagnostic output.
- (inference) Treat no captions, blocked access, missing dependencies and incomplete media as different outcomes. Do not send every failure directly to paid transcription.
- (inference) Prefer the documented Deno setup and a compatible EJS package for a reusable procedure. Skip Bun as a new default because the guide deprecates it.
- (inference) Bound playlist/channel scope explicitly. Check per-video results because continuing after errors can leave a partial batch.
- (inference) Keep adoption counts separate from reliability evidence. Add dated user reports and local extraction checks from other evidence packets before setting success-rate expectations.

## Best parts to read or watch first

Times below are estimated reading times, not source-provided durations.

- Y02b, Setup steps through Step 2: about 5 to 7 minutes. Read runtime and EJS choices together.
- Y02a, Subtitle Options plus Verbosity and Simulation Options: about 3 minutes. Resolves subtitle selection, disk writes and JSON output.
- Y02a, Extractor Arguments, youtube and youtube-ejs: about 5 minutes. Covers client defaults, PO tokens and request-skipping tradeoffs.
- Y02a, Update and Dependencies: about 4 minutes. Covers changing sites, nightly releases and required binaries.
- Y02a, Embedding yt-dlp and Extracting information: about 2 minutes. The most relevant integration advice for agent wrappers.
