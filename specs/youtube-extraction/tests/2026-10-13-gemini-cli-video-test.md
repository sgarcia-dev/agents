---
created_at: 2026-10-13
model: Gemini 3.8 Flash (Medium)
doc_type: test_result
purpose: Can the Gemini CLI (agy) watch a YouTube video's frames, or only read text about it?
---

# Gemini CLI (agy) YouTube Video Extraction Test

## 1. Route Used and Frame Visibility

- **Route Used**: Two-step pipeline combining a local tool fetch with CLI multimodal inspection:
  1. Stream download of the requested segment via `uvx yt-dlp` (`--download-sections "*00:09:56-00:16:51"`), saving a 15.18 MB `.webm` file locally to `/tmp/segment_956_1651.mp4.webm`.
  2. Native multimodal inspection via the CLI's built-in `view_file` tool on the local video file.
- **Were Video Frames Seen?**: **Yes**. The CLI's `view_file` tool supports video files directly (up to 100 MB). It unpacked the video and supplied both full visual frames (webcam feeds, shared screens, browser tabs, code, UI text) and time-aligned audio transcripts into Gemini's context.
- **Direct YouTube URL Ingestion**: The CLI does not currently have a single-step native tool to pass a remote `youtube.com` URL directly into multimodal context without local downloading or proxying. Attempting to fetch the YouTube URL via `read_url_content` yielded only raw HTML/JS client bootstrap code.

---

## 2. Segment Description (00:09:56 to 00:16:51: Examining a Real AI Trace)

### Spoken Summary
Lenny Rachitsky introduces the transition from high-level eval concepts to concrete examples. Shreya Shankar and Hamel Husain explain why unit tests alone are insufficient for LLM applications due to stochasticity and expansive input/output surface areas. Hamel emphasizes starting with "error analysis"—grounding evaluation in actual user logs before writing automated tests. Hamel shares his screen to present a real-world case study from Nurture Boss, an AI leasing assistant company for multifamily apartment communities. He walks through their production system prompt (which Lenny notes is rarely shown publicly), explaining that the prompt acts as a contract, and walks step-by-step through an actual multi-turn customer trace loaded in Braintrust: an inquiry about 1-bedroom apartments with a study, tool execution, and the assistant's response.

### Visual Breakdown & On-Screen Display (with Timestamps)

- **00:09:56 – 00:10:14 (Offset 00:00 – 00:18)**:
  - *On Screen*: Shreya Shankar speaking on webcam (whiteboard background with math formulas/sketches), cutting to Lenny Rachitsky solo, then a three-way split (Lenny on left, Hamel Husain top right with glasses and dotted shirt, Shreya bottom right).
- **00:10:14 – 00:11:12 (Offset 00:18 – 01:16)**:
  - *On Screen*: Hamel Husain full-screen speaker view setting up the background context of error analysis versus traditional software engineering unit tests.
- **00:11:12 – 00:13:02 (Offset 01:16 – 03:06)**:
  - *On Screen*: Hamel shares his browser screen.
  - *Browser Tabs Visible*: `parlance-labs`, `Jeremy Lewi`, `LLM App Log Open...`, `Joshua Xu (he/him)...`, `New code search in...`, `Google Docs`, `RiversideFM: 23...`, `Nurture Boss`.
  - *Page Displayed*: Nurture Boss marketing website (`Conversational AI Solutions For Multifamily Teams`). Visible elements include:
    - Headline: "Conversational AI Solutions For Multifamily Teams"
    - Subhead: "It's time to ditch the busywork and let AI handle the heavy lifting..."
    - Stat badge: "83% Increase in Applications"
    - Partner logos: Bridge Property Management, Gross Residential, PEM, RPM Living, ZRS Management, Gallery, AOG Living, Dayrise Residential, WPM Real Estate Management.
    - Scrolled view: "Nurture Boss AI Powered Virtual Leasing Assistant" with feature list and mobile phone chat mockups.
- **00:13:02 – 00:14:06 (Offset 03:06 – 04:10)**:
  - *On Screen*: Hamel switches to an LLM observability tool (Braintrust).
  - *Workspace*: `parlance-labs / Jeremy Lewi` under the `Logs` tab.
  - *Left Pane*: Log table with rows tagged `root` and input JSON.
  - *Right Pane*: Trace detail view for trace ID `22312bba-5fa7-4f1f-b897-c81f34ee69be`.
  - *Code/Tool Schema*: Displays function definition for `scheduleATour` with properties (`appointmentDate`, `appointmentTime`, `bathCount`, `bedCount`, `email`, `firstName`, `lastName`, `phoneNumber`, `requirements`, `unit`) and note `_note: this should have triggered a handoff to a human`.
- **00:14:06 – 00:15:36 (Offset 04:10 – 05:40)**:
  - *On Screen*: Full-screen expanded trace view showing the system prompt in detail:
    - Heading sections: `[Role and Purpose]`, `[Context]`, `[Primary Objectives]`, `[Resident and Prospective Resident Interactions]`, `[Tour Scheduling]`, `[Applications]`, `[Professional Boundaries]`, `[Narrowing]`.
    - Specific text: "You are an AI assistant working as a leasing team member at Retreat at Acme Apartments..."
    - Inset: Lenny, Hamel, and Shreya react in camera boxes at bottom right as Lenny marvels at seeing a real production system prompt.
- **00:15:36 – 00:16:51 (Offset 05:40 – 06:55)**:
  - *On Screen*: Hamel scrolls down through the trace messages and tool calls:
    - User message: `"Hey I do actually! Do you have the one bedroom with study available? I saw it on the virtual tours"`
    - Tool invocation: `getIndividualInfoInformation` returning a customer record.
    - Tool invocation: `getCommunitiesAvailability` returning raw JSON array of available units (square footages, pricing: $1,350 and $1,375, availability dates).
    - Assistant response: Explaining that while several 1-bedroom units are available, none are specifically listed with a study.
    - Follow-up turn: User asks to be notified when a study is available; assistant politely notes lack of notification capability and directs to website.
    - Metadata footer at bottom showing `Expected: null` and trace ID hashes.

---

## 3. 5 Facts From the Segment That a Transcript Alone Would NOT Give You

1. **Exact Trace ID and Latency Metrics**: The Braintrust UI displays the exact trace identifier `22312bba-5fa7-4f1f-b897-c81f34ee69be`, timestamp `Feb 17 7:31:18 PM`, and latency `0.8588s` on screen.
2. **Specific Navigation and Workspace Breadcrumbs**: The browser tab bar reveals Hamel's active project workspace (`parlance-labs / Jeremy Lewi`) and surrounding open tabs (`RiversideFM: 23...`, `Joshua Xu (he/him)...`, `New code search in...`, `Google Docs`), none of which are mentioned in audio.
3. **Unspoken URLs in the Production System Prompt**: The system prompt on screen contains explicit hardcoded URLs that Hamel never speaks aloud: the maintenance URL `https://maint.acme.com/cross/SignIn/723` and the applications URL `https://www.acme.com/models`.
4. **Structured JSON Tool Payloads**: The video displays the exact tool definition parameters for `scheduleATour` (including typed fields `appointmentDate`, `appointmentTime`, `bathCount`, `bedCount`) and the exact JSON data returned by `getCommunitiesAvailability` (e.g., apartment square footages 738 and 844 sq ft, exact pricing $1,350 and $1,375).
5. **Customer Mockup and Partner Logos on Nurture Boss Website**: When visiting Nurture Boss's site, the video frames show the specific property management partner logos (PEM, RPM Living, ZRS Management, Gross Residential, Bridge Property Management) and the exact stat callout graphic ("83% Increase in Applications").

---

## 4. Time Spent and Errors Encountered

- **Total Time Spent**: Approximately 8 minutes.
- **Errors and Roadblocks Encountered**:
  1. **Direct Web Fetch (`read_url_content`)**: Calling `read_url_content` on the YouTube URL returned raw, unexecuted HTML script blocks (Polymer / InnerTube bootstrap) with zero video frames or transcript content.
  2. **`youtube-transcript-api`**: Encountered `youtube_transcript_api._errors.IpBlocked` (YouTube blocking direct automated scraper requests from host IP).
  3. **`yt-dlp` Subtitle Fetch**: Running `yt-dlp --write-auto-sub` encountered `HTTP Error 429: Too Many Requests` when trying to download caption files.
  4. **Video Stream Download Resolution**: `yt-dlp` stream extraction for the bounded clip (`--download-sections "*00:09:56-00:16:51"`) bypassed the caption ban and succeeded in downloading the 15.18 MB webm file.
  5. **Native Video Viewing**: Passing the downloaded clip into `view_file` succeeded immediately with full frame understanding and timestamped audio.
