---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [Y07, Y07b]
source_files: [sources/Y07-gemini-api-video-understanding.md, sources/Y07b-gemini-api-pricing.md]
purpose: One-source digest feeding the spec compendium.
---

# Gemini API video understanding and pricing (Y07, Y07b)

**What it is:** Google AI for Developers documentation and pricing tables. Individual authors and publication dates are unknown in both captures. Both pages say last updated 2026-10-09 UTC; captured 2026-10-13. Y07 is 1,413 lines with 38 code samples across language tabs. Y07b is 1,268 lines of pricing and notes. Reading time is not supplied. Links: [video understanding](https://ai.google.dev/gemini-api/docs/video-understanding), [pricing](https://ai.google.dev/gemini-api/docs/pricing).

**Capture status:** Both full according to frontmatter. Y07 preserves every exposed code tab and restores code from HTML after the extractor introduced backslashes. Y07b retains the full pricing page, including final Notes. Linked setup, billing, file registration, and token guides are not included. These are vendor documents, not user reports or measured extraction trials.

## The point in three sentences

Gemini can answer questions about public YouTube videos directly, using audio and visuals rather than requiring a separate subtitle extraction step. Static processing samples the full video at a fixed rate; agentic processing lets the model choose which parts to inspect. A 60-minute static input to Gemini 3.8 Flash costs approximately $0.27 at low resolution or $0.81 at high resolution under the captured 2026 Standard rates, before prompt, output, and thinking tokens.

## Key ideas

- Direct YouTube input is documented, with a public-access restriction. “You can only upload public videos (not private or unlisted videos).” Location: Y07, Pass YouTube URLs, Limitations.
- Video answers can use both sound and images. “processing information from both the **audio and visual** streams.” Location: Y07, Extract detailed insights from video. This describes content understanding, not a promise of a verbatim transcript.
- File uploads are intended for long or reusable inputs. “The File API accepts video file formats directly.” Location: Y07, Upload a video file. Upload, wait for processing, then send the returned URI.
- The page disagrees with itself about inline size. Its opening table says “< 100MB”, but the detailed inline section says “shorter videos under 20MB total request size.” Location: Y07, input-method table and Pass video data inline. Preserve this conflict rather than silently choosing a single documented maximum.
- Static sampling can miss brief visual events. “note that it may miss details in videos with rapid motion or quick scene changes.” Location: Y07, Extract detailed insights from video. FPS means frames per second.
- Agentic mode selects material based on the question. “loading only the content it needs based on the prompt.” Location: Y07, Agentic video understanding, mode table. It supports Gemini 3.8 Flash, 3.6 Flash, and 3.5 Flash Lite.
- Adaptive processing has a vendor performance claim, without a benchmark method here. “Up to 88% more token-efficient and ~7% higher quality on long-form content.” Location: Y07, Agentic video understanding, mode table. Treat this as a vendor claim, not independent reliability evidence.
- Long synchronous requests can fail while the backend retries. “unexpected `401 Unauthorized` or timeout errors.” Location: Y07, Technical details about videos, Timeouts for long requests. Streaming or background execution is the stated remedy.
- Follow-up requests can silently lose video context. “While omitting them does not currently return an API error, the video context is lost”. Location: Y07, Multi-turn video conversations. Stateless requests must resend every returned step.
- Timestamps are supported in prompts and can be requested in answers. “Include timestamps for salient moments.” Location: Y07, Extract detailed insights from video, prompt example. The page does not demonstrate a validated timestamped transcript or subtitle export.
- Clipping and custom FPS apply only to static mode. “These customization options are only supported when processing the video in `"static"` mode.” Location: Y07, Customize video processing.
- Thinking is billable output. “Output price (including thinking tokens)”. Location: Y07b, Gemini 3.8 Flash tables. A cheaper input estimate alone does not establish a cheaper complete adaptive run.

## How to do it (concrete steps, checklists, templates)

### Common setup and output

The captures link to Get API key and instantiate `GoogleGenAI` from `@google/genai`, or `genai.Client()` in Python. REST samples pass `GEMINI_API_KEY` through `x-goog-api-key`. They do not give package installation commands or full key and billing setup instructions.

Requests use `gemini-3.8-flash` and `interactions.create`. SDK examples print `interaction.output_text`. REST returns a JSON response envelope, with text inside response steps. That is not evidence that the generated answer itself follows a JSON schema. No SRT, VTT, word alignment, or guaranteed complete transcript format is shown. The detailed technical guidance says to place the prompt after a single video part, although several earlier examples put text first.

### Route 1: Public YouTube URL

1. Create the API client.
2. Add a video input with `type: "video"` and `uri` equal to the YouTube watch URL.
3. Add a text instruction, such as a three-sentence summary.
4. Call `interactions.create` and read `output_text`.

Cost: model tokens, with the static hour estimates below. Free-tier YouTube allowance is eight hours daily. Paid tier has no limit based on video length, but context limits still matter. Gemini 2.5 and later accept up to ten videos per request; older models accept one.

Failure modes: private and unlisted videos are excluded. IP blocks, bot checks, missing captions, regional restrictions, and their error codes are not covered. The page does not establish that this route bypasses those problems. Output is generated text, with timestamps only if requested. Reliability evidence consists of official examples and stated support, with no success rate or independent trial results.

### Route 2: Uploaded video through Files API

1. Supply a local video file to `files.upload`, with its media type where shown.
2. Poll `files.get` while processing, with five-second waits in the main examples.
3. Use the file URI and media type as the video input.
4. Add the task prompt and call `interactions.create`.
5. Read the answer text. JavaScript and REST examples detect `FAILED` processing explicitly.

Cost: model token rates apply; no distinct upload fee is stated in these captures. The opening table gives 20GB paid and 2GB free file limits. The guide recommends Files API for requests above 20MB, significant duration, or reuse.

Failure modes: file processing can fail; some language examples wait for `ACTIVE` without a separate failure exit. Long request timeouts and visual sampling omissions also apply. The source gives no YouTube download procedure, so this is not a documented solution for obtaining a blocked YouTube file. IP blocks, bot checks, and caption availability during acquisition are unaddressed. Output and reliability evidence are the same kind as Route 1: generated text and vendor examples, not measured transcript fidelity.

### Route 3: Inline video bytes

1. Read a local video file.
2. Encode the bytes as base64, a text representation of binary data.
3. Send a video part with `data` and `mime_type: "video/mp4"`, alongside the prompt.
4. Read `output_text`.

Cost: model tokens; no separate inline surcharge is stated. Intended for short, one-off videos, not a 60-minute input. Failure modes include the conflicting 100MB table and 20MB detailed request guidance; no size-error example is supplied. Acquisition, IP blocks, bot checks, and missing captions are not discussed. Output is text, with no shown transcript schema. Reliability evidence is code examples only.

### Route 4: Cloud Storage Registration and other linked inputs

The opening table names Cloud Storage Registration for persistent, reusable files, with 2GB per file and no storage limits. It links to file-input methods for registration, external URLs, and Google Cloud files. Setup steps, registration permissions, storage charges, error handling, and working examples are absent from these captures. Model input costs still apply if processed as video, but the captures cannot establish the complete route cost. Output guarantees, bot/IP/caption behavior, and measured reliability are not provided. Do not treat a table entry as a complete extraction recipe.

### Processing option: Agentic mode

This is a processing option on a video part, not a separate acquisition route.

1. In the demonstrated upload example, upload and poll the long video until processing completes.
2. Set `processing: "agentic"` on its video input.
3. Set `background: true` for a long task.
4. Poll `interactions.get(interaction.id)` while status is `in_progress`, with five-second waits.
5. Read `output_text`; inspect `interaction.steps` for `processing_call` and `processing_result` to confirm adaptive inspection occurred.

The guide also recommends streaming. Steps record requested segments or transcripts and their results, followed by `model_output`; they need no client response. Cost depends on loaded frames, audio, transcripts, and navigation thinking. Quality and savings claims are vendor claims without supplied test data. For follow-ups, use `previous_interaction_id`, or resend every response step through `step_list`; those resent steps contribute to input tokens.

### Static controls and timestamp prompts

Set `processing` to an object with `type: "static"`. The clipping example uses `start_offset: 1200` and `end_offset: 1500`. The FPS example uses `fps: 0.5`, one frame every two seconds. For questions about moments, use `MM:SS`, such as `00:05`. For timed descriptions, use the source prompt: “Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.”

### User-report evidence gap

Neither capture includes user reports, author names, dates of field reports, bot-check experiences, or IP-block experiences. There are therefore no user reports to quote with author and date. The documentation's page update date is not a user-report date.

## Tools, code and commands named

- APIs: Interactions API (recommended on the page), `generateContent API` (linked alternative), Files API, Cloud Storage Registration.
- SDK names: `@google/genai`, `GoogleGenAI`, `from google import genai`, `google.golang.org/genai`, `com.google.genai.Client`. No SDK version is pinned.
- Model identifiers used or discussed for adaptive video: `gemini-3.8-flash`, Gemini 3.6 Flash, Gemini 3.5 Flash Lite.
- REST tools and variables: `curl`, `jq`, `base64`, `file -b --mime-type`, `wc -c`, `GEMINI_API_KEY`.
- REST paths: `/upload/v1beta/files`, `/v1beta/interactions`, `/v1beta/interactions/$id`, under `https://generativelanguage.googleapis.com`.
- Supported media types: `video/mp4`, `video/mpeg`, `video/mov`, `video/avi`, `video/x-flv`, `video/mpg`, `video/webm`, `video/wmv`, `video/3gpp`.

## Numbers and strong claims

### Cost of a 60-minute YouTube video to Gemini 3.8 Flash

Assumptions: one full-video static pass, 1 FPS, no cache, Standard paid tier, USD. This is an input estimate, not a fixed complete-request price.

Y07, Technical details about videos, gives “66” tokens per low-resolution frame, “258 tokens per frame” otherwise, and “Audio: 32 tokens per second.” It includes metadata and rounds totals to “Approximately 100 tokens per second of video at default (low) media” resolution, or “approximately 300 tokens per second of video at high media” resolution.

Y07b, Gemini 3.8 Flash, first table, labels prices “Paid Tier, per 1M tokens in USD”. Input rates are “$0.75 through December 31, 2026.” and “$1.50 starting January 1, 2027.” Output, including thinking, is “$3.75 through December 31, 2026.” and “$7.50 starting January 1, 2027.” Unlike some other model tables, this Flash table does not split audio into a separate rate.

- Duration: 60 × 60 = 3,600 seconds.
- Low-resolution frames: 3,600 × 66 = 237,600 tokens. Audio: 3,600 × 32 = 115,200. Subtotal: 352,800 tokens before metadata.
- Low-resolution rounded estimate: 3,600 × 100 = 360,000 tokens. Cost through 2026: 360,000 / 1,000,000 × $0.75 = **$0.27**. From 2027: × $1.50 = **$0.54**.
- Higher-resolution frames: 3,600 × 258 = 928,800 tokens. Add audio: 1,044,000 before metadata.
- Higher-resolution rounded estimate: 3,600 × 300 = 1,080,000 tokens. Cost through 2026: 1,080,000 / 1,000,000 × $0.75 = **$0.81**. From 2027: × $1.50 = **$1.62**.

The high-resolution estimate needs a context check: Y07 says a 1M-token context supports “up to 1 hour long at high media” resolution, while its rounded hour estimate exceeds 1M. These approximate claims do not establish that every full high-resolution hour will fit.

For 2026 Standard, total cost is approximately video input cost + prompt tokens × $0.75 / 1M + (answer and thinking tokens) × $3.75 / 1M. For example, 1,000 combined answer/thinking tokens add $0.00375. Their actual count is unknown.

The subsequent Flash tables follow the displayed Standard, Batch, Flex, Priority tab order. Batch and Flex list $0.375 input and $1.875 output through 2026; low-resolution hour input arithmetic is 0.36 × $0.375 = $0.135. Priority lists $1.35 input and $6.75 output; 0.36 × $1.35 = $0.486. These are table-rate calculations, not proof that the demonstrated Interactions request supports each service mode. Free-tier input and output are free subject to limits; the page distinguishes free content use for product improvement from paid content not used for that purpose.

Agentic cost cannot be calculated from duration alone. Y07b Notes says usage is “variable based on the content loaded by the model rather than” full video length. Applying the maximum advertised 88% input reduction to 360,000 tokens would yield 43,200 tokens and $0.0324 input, but that is an illustrative arithmetic result, not a forecast. Navigation thinking and loaded material must be counted from the actual run.

Other relevant claims: Y07 gives up to three hours at low resolution for a 1M context, and added timestamps every second in static processing. Y07b names Gemini 3.5 Transcribe with speaker separation and word timestamps at an estimated blended ~$0.005/min, but provides no YouTube extraction or setup recipe for it. Pricing for generation models such as Veo and Omni is not the price of this video-understanding route.

## Compared with the deep research report

Comparison is limited to Y00's Gemini section.

- Right: Y00 says “Google's Gemini API can process public YouTube URLs directly as video inputs.” Y07 supplies the direct `uri` examples and limits access to “public videos”. Its audio-and-visual explanation and selective timeline discussion are supported.
- Unsupported in this capture: Y00 calls URL support “a preview feature.” Y07's Pass YouTube URLs section does not label it preview. That status cannot be established from this capture.
- Reasonable caution, not measured proof: Y00 says it “doesn't necessarily give you a faithful, reusable transcript.” Y07 demonstrates summaries and timed descriptions, not a fidelity-tested transcript export. Its What's next section acknowledges outputs “that are inaccurate,” but neither capture measures transcript errors.
- Left out: Y00 gives no cost arithmetic, public/unlisted distinction, eight-hour free limit, ten-video limit, inline-size conflict, processing failure handling, or silent follow-up context loss. Y07 explicitly says omitted steps mean “the video context is lost”.
- Left out: Y00's sample uses default static processing. Y07's adaptive setting is `"processing": "agentic"`; its long-task remedy is background execution or streaming. These choices change cost, latency, and failure behavior.

## Fit for the user's agent workspace

- (inference) Use this route when slides, diagrams, or demonstrations contain evidence that captions cannot express.
- (inference) Store the question, model, mode, resolution, answer, timestamps, and measured token use with an extraction result so later workers can judge cost and coverage.
- (inference) Test public URL success and timed-answer accuracy before making this a dependable fallback. Official examples do not establish field reliability.
- (inference) Compare adaptive and static answers on known events, including fast scene changes and small slide text. Measure missed evidence and total cost, including thinking.
- (inference) Keep generated interpretation separate from quoted speech. This capture does not justify presenting a summary as a verbatim transcript.
- (inference) Add failure exits and a bounded polling policy when adapting the examples. Several loops lack a timeout or complete failure handling.

## Best parts to read or watch first

Times below are reading estimates, not source-provided durations.

- Y07, Pass YouTube URLs, JavaScript example and Limitations: about two minutes for the simplest route and access rules.
- Y07, Technical details about videos: about four minutes for token arithmetic, context limits, resolution, and timeouts.
- Y07b, Gemini 3.8 Flash, first pricing table: about two minutes for rates and their January 2027 change.
- Y07, Choose a processing mode, Set the processing mode, Response steps, and Multi-turn video conversations: about five minutes using only the JavaScript tab for adaptive execution and context preservation.
