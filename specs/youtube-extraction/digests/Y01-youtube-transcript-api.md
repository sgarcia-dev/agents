---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [Y01a, Y01b]
source_files: [sources/Y01a-youtube-transcript-api-README.md, sources/Y01b-youtube-transcript-api-issue-593.md]
purpose: One-source digest feeding the spec compendium.
---

# YouTube Transcript API README and cloud blocking issue (Y01)

**What it is:** Y01a is the full repository README for [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api). Its author and publication date are unknown in the capture. It is Python API and command-line documentation, roughly a 15-minute read. Y01b is [issue #593](https://github.com/jdepoix/youtube-transcript-api/issues/593), opened by belwalshubham on May 2, 2026, with one reply from jdepoix on May 5. It takes about two minutes to read.

**Capture status:** Both captures are marked full. Y01a contains the full raw README plus repository metadata. Y01b contains the issue body and all comments, 1 of 1. No missing capture content is reported. Neither provides measured extraction success rates or a production benchmark.

## The point in three sentences

This Python library fetches existing YouTube captions, including automatic captions, and returns text with start times and durations. Direct requests can work locally but fail from cloud IP addresses, while rotating residential proxies are the maintainer's recommended workaround. The interface is undocumented, cookie authentication is currently broken, and neither proxy reliability nor managed-service reliability is established by measured results here.

## Key ideas

- No browser is needed for the library route. The opening description says it “does not require a headless browser”, meaning a browser running without a visible window. Location: Y01a, introduction.
- Supply the video ID rather than its full URL. “Pass in the video ID, NOT the video URL.” Location: Y01a, API.
- Output retains segment timing and transcript metadata. The example includes `text`, `start`, `duration`, `video_id`, language and `is_generated`; “a list of dictionaries” describes `to_raw_data()`. Location: Y01a, API.
- Language order is a fallback order, with English the default. “It's a list of language codes in a descending priority.” Location: Y01a, Retrieve different languages.
- Manual captions take priority when both types exist in the requested language. The README says it “always chooses manually created transcripts over automatically created ones”. Location: Y01a, List available transcripts.
- Translation uses YouTube's subtitle translation feature. “returns a new translated” describes the `Transcript` returned by `translate()`. Location: Y01a, Translate transcript. This is not a documented route for transcribing audio without captions.
- Cloud and high-volume self-hosted requests can be blocked. The issue reports “Works locally” and “Blocked on AWS”. Location: Y01b, Direct usage (no proxy).
- Webshare's free offering did not solve this user's problem. “Free plan only provides **datacenter proxies**” and the residential endpoint attempt returned “407 Proxy Authentication Required”. Location: Y01b, Webshare (residential proxies).
- Proxies remain blockable. “YouTube can always block the IP of your” proxy is the README's warning. Location: Y01a, Using other Proxy solutions. Rotating addresses are recommended, not guaranteed.
- Age-restricted access is currently unavailable through the documented cookie mechanism. “this feature is currently not available.” Location: Y01a, Cookie Authentication. The later CLI cookie command does not establish that authentication works.
- Managed services trade infrastructure work for an external dependency and cost. The issue author reports “No blocking issues”; jdepoix says self-managed library plus Webshare “will always be cheaper”. Location: Y01b, Managed APIs and sole comment. These are user experience and maintainer opinion, not comparative measurements.
- YouTube changes can break every library-backed route. “This code uses an undocumented part of the YouTube API”. Location: Y01a, Warning.

## How to do it (concrete steps, checklists, templates)

### Direct Python route

1. Install with `pip install youtube-transcript-api`.
2. Import `YouTubeTranscriptApi`, create an instance and call `ytt_api.fetch(video_id)`.
3. For language selection, pass `languages=['de', 'en']`. Even a single language must be a list.
4. Optionally set `preserve_formatting=True` to retain HTML italics and bold.
5. Call `ytt_api.list(video_id)` to inspect available tracks. Select with `find_transcript`, `find_manually_created_transcript` or `find_generated_transcript`, then call `transcript.fetch()`.
6. For translation, select a track, call `transcript.translate('de')`, then fetch the returned track.
7. For JSON, use `JSONFormatter().format_transcript(transcript)`, then write the string to a UTF-8 file. `indent=2` is supported.

**Cost:** No extraction fee or paid library requirement is stated. The project is described as open source and displays an MIT licence badge. Local runtime cost is not quantified.

**Output:** `FetchedTranscript` contains snippets with text, start and duration, plus video ID, language, language code and generated-caption status. It supports iteration, indexing and length. `to_raw_data()` returns segment dictionaries. Named formatters produce JSON, pretty print, text, WebVTT or SRT. CSV is mentioned as a possible format, but no built-in CSV formatter is listed.

**Failures and reliability:** Y01b reports local success and AWS failure for the same code. Y01a warns about `RequestBlocked` and `IpBlocked`, cloud IP blocks, excessive requests and changes to the undocumented interface. Captions and an appropriate language track must be available; the capture gives no missing-caption exception name or audio transcription fallback. Bot-check handling is not documented. No sample size, throughput limit or success percentage is supplied.

### Webshare rotating residential route

Follow the README's order:

1. Create a Webshare account.
2. Purchase a “Residential” package suitable for the workload. Do not choose “Proxy Server” or “Static Residential”.
3. Open Proxy Settings and obtain the proxy username and password.
4. Import `WebshareProxyConfig` from `youtube_transcript_api.proxies`.
5. Pass `proxy_config=WebshareProxyConfig(proxy_username="<proxy-username>", proxy_password="<proxy-password>")` to `YouTubeTranscriptApi`.
6. Fetch normally. Rotation is the default and needs no further configuration.
7. Optionally set `filter_ip_locations=["de", "us"]` to restrict countries. The README says nearby locations can reduce latency and country selection can work around location restrictions.

**Cost:** A paid residential package is required in these instructions. No price, bandwidth allowance or per-transcript cost appears. The README discloses referral links supporting the project.

**Output:** The same timestamped library output and formatters as direct Python.

**Failures and reliability:** The free-tier residential endpoint `p.webshare.io:80` returned HTTP 407 for the issue author. Paid proxies can still be blocked and do not add captions or restore broken authentication. Bot-check handling is not explained. The README author says Webshare was most reliable after testing providers; the May reply endorses rotating residential proxies. Neither gives test conditions, paid-tier success rates or long-term production evidence.

### Other proxy route

1. Set up a generic HTTP/HTTPS/SOCKS proxy.
2. Import `GenericProxyConfig`.
3. Configure `http_url="http://user:pass@my-custom-proxy.org:port"` and `https_url="https://user:pass@my-custom-proxy.org:port"` in the API constructor.
4. Fetch normally. The README recommends a rotating pool for reliability.

**Cost:** Provider and hosting costs are unspecified. **Output:** The same timestamped library output. **Failures:** Proxy IPs can be blocked; static proxies are said to be banned after extended use. Missing captions, age restrictions and interface changes remain relevant. No bot-check procedure or provider comparison data is supplied. **Reliability evidence:** A general maintainer recommendation, without a demonstrated working alternative provider.

### Command-line route

The CLI is another interface to the library, not separate reliability evidence.

1. After installation, run `youtube_transcript_api <first_video_id> <second_video_id> ...`.
2. Add `--languages de en` for language preference.
3. Add `--exclude-generated` or `--exclude-manually-created` when needed.
4. Request JSON and write it to disk:

```sh
youtube_transcript_api <first_video_id> <second_video_id> ... --languages de en --format json > transcripts.json
```

5. Use `--languages en --translate de` for translation, or `youtube_transcript_api --list-transcripts <first_video_id>` to list tracks.
6. Escape an initial hyphen in an ID, as in `youtube_transcript_api "\-abc123"`.
7. For purchased Webshare residential proxies, add `--webshare-proxy-username "username" --webshare-proxy-password "password"`. For generic HTTP/HTTPS proxies, add `--http-proxy http://user:pass@domain:port --https-proxy https://user:pass@domain:port`.

**Cost:** Follows the selected direct or proxy route. **Output:** Printed results, with an explicit JSON option; library timing fields are documented, but no complete CLI JSON example is shown. **Failures and reliability:** The same library warnings apply. The documented `--cookies /path/to/your/cookies.txt` option conflicts with the current cookie-authentication limitation and should not be treated as a working age-restriction solution.

### Hosted services named

- **Supadata:** Y01b reports reliable use with no blocking issues and extra cost. The maintainer suggests it when users do not want to manage proxies. Setup steps, pricing, timestamps, JSON schema, missing-caption behavior and bot-check handling are absent.
- **SerpApi, TranscriptAPI.com and Dumpling AI:** Y01a links these sponsors as hosted choices. It supplies no setup instructions, cost figures, output formats, failure handling or reliability evidence for them. Their presence is promotion, not a comparative test.

## Tools, code and commands named

- Package: `youtube-transcript-api`. Capture metadata: latest release `v1.2.4`, published `2026-01-29T09:07:48Z`. The README install command does not pin that version.
- Python names: `YouTubeTranscriptApi`, `FetchedTranscript`, `FetchedTranscriptSnippet`, `TranscriptList`, `Transcript`, `WebshareProxyConfig`, `GenericProxyConfig`, `requests.Session`, `Session`.
- Formatter names: `Formatter`, `JSONFormatter`, `PrettyPrintFormatter`, `TextFormatter`, `WebVTTFormatter`, `SRTFormatter`; `json.dumps()` is used by the JSON formatter.
- Request customization: `http_client=http_client`, `http_client.headers.update({"Accept-Encoding": "gzip, deflate"})` and `http_client.verify = "/path/to/certfile"`. A shared session can share cached cookies, headers and certificate settings. This is not proof that login authentication works.
- Contributor tools: Poetry and poe. Commands: `poetry install --with test,dev`, `poe test`, `poe coverage`, `poe format`, `poe lint`, `poe precommit`.
- Infrastructure named: AWS, Google Cloud Platform, Azure, Webshare and generic HTTP/HTTPS/SOCKS proxies. Selenium is mentioned as a browser-based alternative, without setup instructions.

## Numbers and strong claims

- **8,452 repository stars:** Y01a capture notes. Adoption evidence, not extraction reliability.
- **One issue comment:** Y01b capture notes. A small evidence base for production recommendations.
- **“most reliable option”:** Y01a, Working around IP bans. Maintainer opinion about rotating residential proxies; no benchmark supplied.
- **“will always be cheaper”:** Y01b, jdepoix comment. Strong cost opinion based on hosted providers also paying proxy and hosting costs. No numerical comparison supports the universal claim.
- **“407 Proxy Authentication Required”:** Y01b, Webshare. A specific reported free-tier failure, not a YouTube bot-check result.
- **No service guarantee:** Y01a, Warning says there is “guarantee that it won't stop working tomorrow”. The maintenance promise is best effort.

## Compared with the deep research report

- **Right:** Option A uses `YouTubeTranscriptApi().fetch(...)`, `to_raw_data()` and CLI JSON output. The report says “structured and timestamped”; Y01a's API example includes `start` and `duration`. The report's “undocumented YouTube interface” limitation matches Y01a's “undocumented part of the YouTube API”.
- **Right:** The report says residential proxies “remain an economical way to maintain access”. Y01b calls them the “most reliable and cheapest way”. It also accurately describes hosted services as easier for users who want to avoid proxy management.
- **Overstated or unverified here:** “Extremely fast” and “Best lightweight solution” are report assessments, with no timing or comparison benchmark in Y01a/Y01b. “Free” does not cover purchased residential proxies. The reported 15.8 million monthly PyPI downloads cannot be checked from these captures; roughly 8,500 stars agrees with the captured 8,452.
- **Left out:** The free-tier Webshare trap, HTTP 407, the exact residential-package requirement, proxy configuration, broken cookie authentication, manual-caption preference and ordered language fallback. Y01a says cookie authentication is “currently not available”; that affects route selection.
- **Output contract gap:** The report's proposed common schema includes `title` and `channel`. Y01a's documented `FetchedTranscript` contains video ID, language and caption-type metadata, without those fields. Additional metadata retrieval would need separate evidence.
- **Missing captions:** The report proposes a “Whisper-based transcription” fallback. These two sources do not document that route, its setup or its reliability. They also do not establish Supadata's missing-caption transcription behavior.

## Fit for the user's agent workspace

- (inference) Use the CLI's JSON option as a shared interface across harnesses. Keep segment timing for later source citations.
- (inference) Start with a small local extraction trial. A successful local run does not establish cloud readiness.
- (inference) Keep IP blocks, proxy authentication failures and missing tracks as distinct outcomes so workers can choose the next action.
- (inference) Record language and generated-caption status alongside segments. Raw segment dictionaries alone omit the surrounding transcript metadata.
- (inference) Treat paid residential proxies as an optional deployment dependency, with cost and observed success tracked separately.
- (inference) Skip cookie authentication as a promised working route until another source establishes a fix.
- (inference) Treat hosted APIs as candidates needing their own setup and output evidence. Sponsor links and one user's success report are insufficient for selecting a production service.

## Best parts to read or watch first

- Y01b, “What we tried” and jdepoix's reply: about 2 minutes. Fastest explanation of local versus cloud behavior, the Webshare free-tier failure and the managed-service tradeoff.
- Y01a, “API” through “List available transcripts”: about 4 minutes. Fetching, timing fields, languages and caption types.
- Y01a, “Working around IP bans” and its two proxy subsections: about 4 minutes. Exact proxy setup and its limits.
- Y01a, “Cookie Authentication” and “Warning”: under 1 minute. Two limitations that should affect the spec.
- Y01a, “Using Formatters” and “CLI”: about 4 minutes. Portable output and command examples. Reading times are estimates, not source-provided durations.
