---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [Y08a, Y08b, Y08c]
source_files: [sources/Y08a-pypistats-youtube-transcript-api.md, sources/Y08b-npm-youtube-transcript.md, sources/Y08c-youtubejs-README.md]
purpose: One-source digest feeding the spec compendium.
---

# Adoption statistics and YouTube.js (Y08a, Y08b, Y08c)

**What it is:** Three captures taken on October 13, 2026. Y08a is a [PyPI statistics snapshot](https://pypistats.org/packages/youtube-transcript-api), with unknown author and publication date, containing three recent download totals and 376 daily rows. Y08b is Kakulukian's [youtube-transcript npm README](https://www.npmjs.com/package/youtube-transcript), publication date unknown, plus a weekly download response. Y08c is LuanRT's [YouTube.js README](https://github.com/LuanRT/YouTube.js), publication date unknown, plus repository metadata and the September 22, 2026 release notes. Allow roughly five minutes for the prose and selected statistics; reading every daily row takes longer.

**Capture status:** All three are marked full. Y08a includes all recent fields and all 376 overall rows. Y08b includes the complete registry README and weekly downloads response. Y08c includes the complete raw README, star count, latest release metadata and release body. Linked documentation, prerequisites, issue discussions and user reports are not included. Full capture does not mean full operational documentation.

## The point in three sentences

These captures support substantial package download counts and a sizable YouTube.js star count. The npm transcript package gives a short extraction example, while YouTube.js only shows installation and client creation. None supplies a transcript success rate, an attributed user reliability report, or evidence about IP blocks, missing captions and bot checks.

## Key ideas

- Python package downloads are substantial, but this capture is statistics rather than a usage guide. The monthly row is "| last_month | 15839443 |" (Y08a, recent_downloads).
- The Python snapshot separates daily counts with and without mirrors. It includes "| without_mirrors | 2026-10-12 | 534326 |" (Y08a, overall_downloads). Do not add the two categories as though they were separate user populations.
- The npm transcript package was created for Node.js use. Kakulukian writes, "I wanted to extract a transcript from a youtube video but there was only a python script so I created this to do it in node." (Y08b, opening paragraph; publication date unknown).
- Its author explicitly warns about maintenance risk. "This package use unofficial YTB API so it can be broken over the time if no update appears." (Y08b, opening paragraph; Kakulukian, date unknown). This is an author warning, not a dated user failure report.
- The npm example accepts either a video identifier or a URL. Its entire extraction call is "fetchTranscript('videoId or URL').then(console.log);" (Y08b, Usage).
- Its return type is an array delivered asynchronously. The signature contains "Promise<TranscriptResponse[]>" (Y08b, Methods). The capture does not define the response fields, timing units or JSON serialization.
- YouTube.js accesses an internal API, meaning an interface used by YouTube itself. It describes itself as "A JavaScript client for YouTube's internal API." (Y08c, introductory HTML). This establishes its scope, not transcript reliability.
- YouTube.js advertises several runtime environments: "Works on Node.js, Deno, modern browsers, and more." (Y08c, introductory HTML). Minimum runtime versions are not given in the capture.
- YouTube.js setup depends on documentation outside this packet. "Before installing, make sure your environment meets the [prerequisites](https://ytjs.dev/guide/getting-started.html#prerequisites)." (Y08c, Installation). Those prerequisites remain unverified here.
- The latest captured release shows maintenance work. One fix is "**Session:** Adjust JSPB parsing logic" (Y08c, 18.1.0, Bug Fixes). The notes name a parsing fix but do not explain JSPB or show a transcript test result.
- The project states its independence from YouTube: "This project is not affiliated with, endorsed, or sponsored by YouTube or any of its affiliates or subsidiaries." (Y08c, Disclaimer). Do not present it as an official supported YouTube interface.

## How to do it (concrete steps, checklists, templates)

### Route coverage for the YouTube spec

| Route | Setup supported by this packet | Cost evidence | Failure modes | Output and reliability evidence |
| --- | --- | --- | --- | --- |
| youtube-transcript-api, Python | No installation or extraction steps in Y08a | No license or pricing information captured | IP blocks, missing captions and bot checks are not covered | No transcript output shown. Download counts measure package distribution, not successful extraction |
| youtube-transcript, Node.js | Install with npm, Yarn or pnpm; import fetchTranscript; call it with video ID or URL | MIT license stated; no service fee, proxy cost or running cost stated | Author warns that its unofficial API can break without updates. Specific IP, caption and bot-check failures are not covered | Promise of TranscriptResponse array. Fields, timestamps and JSON output are not documented. Weekly downloads are adoption evidence only |
| YouTube.js / youtubei.js | Check linked prerequisites; install package; import Innertube; create client | MIT license stated; no service fee, proxy cost or running cost stated | No IP-block, missing-caption or bot-check behavior documented. Release notes contain parser and session fixes | Client initialization only. No transcript method, timestamps or JSON schema shown. Stars and release notes do not establish extraction success |

An MIT license does not establish zero operating cost. These captures do not provide enough information to price an extraction workflow.

### youtube-transcript steps, in source order

1. Choose one installation command: `npm i youtube-transcript`, `yarn add youtube-transcript`, or `pnpm add youtube-transcript`.
2. Import and invoke the function as shown:

```js
import { fetchTranscript } from 'youtube-transcript';

fetchTranscript('videoId or URL').then(console.log);
```

3. Consult the listed signature for the optional `TranscriptConfig` argument. The capture gives no option definitions or error-handling example.

### YouTube.js steps, in source order

1. Check the linked prerequisites. Their actual contents are absent.
2. Select the installation command for your environment from the commands below.
3. Initialize the client:

```ts
import { Innertube } from 'youtubei.js';
const innertube = await Innertube.create(/* options */);
```

4. Read the linked Guide and API Documentation for detailed usage. The packet does not supply the next transcript extraction step.

### User reports

There are no user reports in these three files. No dated user quote about success, IP blocks, missing captions or bot checks can be supplied. Kakulukian's warning above is attributed, but its publication date is unknown. LuanRT's release notes are dated September 22, 2026; they are project maintenance records, not user reports.

## Tools, code and commands named

- Y08a: `youtube-transcript-api`; PyPI statistics recent and overall JSON APIs, where JSON is a structured data format. No Python installation command or package version is captured.
- Y08b: `youtube-transcript`, Node.js, npm, Yarn, pnpm, `fetchTranscript`, `TranscriptConfig`, `TranscriptResponse`, `Promise<TranscriptResponse[]>`, and MIT.
- Y08c installation commands: `npm install youtubei.js@latest`, `yarn add youtubei.js@latest`, `npm install github:LuanRT/YouTube.js`, and `deno add npm:youtubei.js@latest`.
- Y08c deprecated Deno import: `import { Innertube } from 'https://deno.land/x/youtubei/deno.ts';`. The source explicitly labels this route deprecated.
- Y08c: `Innertube.create(/* options */)`, YouTube.js Guide and API Documentation at `https://ytjs.dev`, GitHub issues and contribution guidelines, Discord, and MIT.
- Captured release: `v18.1.0`. Installation uses `@latest`, rather than pinning that version.
- Release identifiers include `thumbnail_overlays`, `content_type`, `attributionText`, `HowThisWasMadeSectionView`, `VideoTitleHeaderView`, `/player/heartbeat`, `target_duration_dec`, `target_duration_sec`, `playability_status_memo`, `IPlayerHeartbeatResponse`, `PlayerInterstitial`, `InterstitialView`, and `attachmentRuns`. These are release details, not a transcript response schema.

## Numbers and strong claims

- Y08a, recent_downloads: 534,326 last-day downloads; 3,511,656 last-week downloads; 15,839,443 last-month downloads. The recent table does not state calendar boundaries or a mirror category.
- Y08a, overall_downloads: 376 rows across two categories, covering April 8 through October 12, 2026. On October 12, counts are 534,795 with mirrors and 534,326 without mirrors. These are separate views, not additive counts.
- Y08b, Last-week downloads: 185,344 downloads from October 5 through October 11, 2026.
- Y08c, Repository metadata: 5,376 GitHub stars. No active-user or download total is captured as a numeric value.
- Y08c, Latest release: v18.1.0, published `2026-09-22T19:21:01Z`, with prerelease and draft both `False`.
- Y08c's runtime compatibility statement is a project claim, not independently tested evidence in this packet. No marketing success-rate claim appears.

## Compared with the deep research report

Only the adoption table and YouTube.js entry in Y00 were read for this comparison.

- **Right:** The report's "15.8 million PyPI downloads in the preceding month" agrees with Y08a's "| last_month | 15839443 |". Its "Approximately 185,000 weekly npm downloads" agrees with Y08b's 185,344 row. Its "Approximately 5,400 GitHub stars" agrees with Y08c's 5,376.
- **Right:** The report warns, "GitHub stars are not active users, and package downloads include automated installations." This is the appropriate limit on interpreting these adoption indicators. The captures do not provide active-user counts.
- **Not verifiable here:** The report also lists "Approximately 8,500 GitHub stars" for the Python package. Y08a contains only download statistics, so this packet cannot confirm that number.
- **Interpretation beyond this packet:** The report calls YouTube.js an "Established TypeScript library" and says "Greater implementation complexity; susceptible to upstream changes". Y08c supports internal-API access and a TypeScript initialization example. It does not measure comparative complexity or directly document upstream transcript failures. Y08b, a different package, explicitly says its API "can be broken over the time if no update appears."
- **Left out:** The relevant report passages omit the npm extraction example, optional configuration signature, MIT licenses, YouTube.js prerequisite dependency, deprecated Deno import, and dated release fixes. They also do not establish transcript response fields or success rates. These gaps matter before selecting a working extraction route.

## Fit for the user's agent workspace

- (inference) Keep adoption evidence separate from reliability evidence in the spec. A downloaded package may still fail on the worker's network or target video.
- (inference) Try the short npm example as a candidate for a TypeScript worker, but require a captured response before defining timestamps or JSON fields.
- (inference) Give a worker an explicit extraction method before assigning YouTube.js work. Client creation alone is not a complete task recipe.
- (inference) Record the chosen package version. The documented `@latest` commands do not preserve a fixed setup for later evaluation.
- (inference) Leave IP-block, missing-caption, bot-check and operating-cost fields marked unknown until another source or an authorized test supplies evidence.
- (inference) Do not choose the Python route from this packet alone. It supports popularity, while its setup and output contract need a different capture.

## Best parts to read or watch first

- Y08b, opening warning, Installation, Usage and Methods: about one minute. This is the only executable transcript example in the packet.
- Y08c, Installation and Basic Usage: about one minute. Learn exactly where the captured setup stops.
- Y08c, Latest release and Bug Fixes: about one minute. See dated maintenance evidence without treating it as a reliability benchmark.
- Y08a, recent_downloads, and Y08b, Last-week downloads: under one minute. Use these for adoption numbers; inspect overall_downloads only when daily history matters.
