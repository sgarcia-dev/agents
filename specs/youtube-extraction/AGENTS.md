---
created_at: 2026-10-13
updated_at: 2026-10-13
model: gpt-6.1-sol (high)
doc_type: guidance
purpose: Working rules for the YouTube extraction spec and its preserved evidence.
related:
  - path: ./spec.md
    why: Capability behavior and the entrypoint for route selection.
  - path: ./STATE.md
    why: Current results, proposals and next steps.
  - path: ./SOURCES.md
    why: Capture inventory and evidence limits.
  - path: ./DECISIONS.md
    why: User-approved scope and evidence layout.
---

# YouTube extraction: how to work here

This spec owns a general research capability: retrieve faithful YouTube speech
text and inspect visuals when the research question needs them. All harnesses
can consume it. It is a sibling of
[web scraping site access](../web-scraping-site-access/spec.md).

Read [spec.md](spec.md), then [STATE.md](STATE.md). Open only the route digest,
capture or test needed for the task. The root workspace instructions still apply.

## Layout and authority

- `spec.md`: behavior, four outcomes, route comparison, proposed fallback chain
  and output contract. Its Start Here block is the navigation entrypoint.
- `STATE.md`: current truth, active proposals, blockers and next steps.
- `DECISIONS.md`: choices the user actually made. Do not promote an inference
  or recommendation into a decision.
- `SOURCES.md`: evidence ledger, capture limits, freshness and weak claims.
- `sources/`: verbatim source captures (not published in the public snapshot; see the URLs in `SOURCES.md`). **Never edit existing captures**, even
  to fix an error, change frontmatter or improve formatting.
- `digests/`: explanations of source captures, with source IDs and links.
- `tests/`: our measured results, commands, versions, errors and output checks.

Do not create `artifacts/` here. The source/digest/test layout is the user's
explicit choice, recorded in [DECISIONS.md](DECISIONS.md). General generated
research reports still follow
[artifact-authoring.md](../../conventions/artifact-authoring.md).

## How to add a source

- Capture the actual linked source, not a search snippet or another summary.
  Keep its words and code unchanged. Assign a new stable ID and descriptive
  filename. Use separate IDs or suffixes for distinct pages/files.
- Add capture frontmatter: `source_url`, `title`, `author`, `published`,
  `captured_at`, `capture_method`, `methods_tried`, `completeness` and
  `capture_notes`. Unknown is valid. State missing tabs, deleted comments,
  omitted sections and collection errors plainly.
- Inspect code blocks, tables, final sections and comment pagination. Record
  the actual capture scope; full capture is not proof of route reliability.
- Preserve raw extraction JSON or subtitle files when available. Check that
  no key, cookie or signed-URL credential enters this shared repository.
- Add one ledger row per capture file with ID, title, URL, method, completeness
  and word count. Use the standard evidence groups in
  [memory-files.md](../../conventions/memory-files.md).
- Put interpretation in a linked digest. Correct unsupported claims in
  `spec.md` and `SOURCES.md`; leave the source capture untouched.

## How to add a test

- Make the test bounded and dated. Record host/runtime/tool versions, video
  IDs, language, caption inventory, commands/settings, attempt times with
  timezone, elapsed time, exit/HTTP codes, warnings and actual charge.
- Pace requests and check the shared cache first. Coordinate all harnesses
  using the same IP and provider account. Stop local caption work on a block.
  The 2026-10-13 timeline supports caution, not a known safe numeric limit.
- Require actual speech text. Exit zero, HTTP 200, metadata, a caption button
  or a YouTube postprocessor flag does not prove a transcript.
- Keep no captions, IP blocking, provider rate limits, unavailable content and
  setup failures distinct in measurements. Record empty or partial outputs.
- Save readable results and machine-readable measurements in `tests/`. Keep
  raw outputs inspectable; identify any temporary storage and retention limit.
  Remove authentication data from saved diagnostics.
- Measure words, cue times, duration comparison and selected caption type when
  available. Untimed text has unknown coverage. An audio URL is not a verified
  download; a playable file is not a validated speech transcript.
- For visual work, record acquisition route, inspected clip, original-video
  offset, model/tool, prompt and usage. Label unscored visual details. Do not
  claim whole-video analysis from a bounded clip.
- Add the test to `SOURCES.md`, update current truth in `STATE.md`, and change
  route labels only to the level the result supports. Do not count a report
  and its JSON as two independent trials.

## How to refresh

- Recheck only the stale claim or failing route needed for the current task.
  A price refresh and a reliability test answer different questions.
- Create a new dated capture or test file. Never overwrite prior evidence.
  Link old and new versions in the ledger, with which one should be used now.
- Update the affected digest, route claim and state. Mark vendor promises as
  Claimed, interfaces/prices as Documented, our dated runs as Observed, and
  recommended behavior as Proposal.
- When results disagree, prefer this machine's measured results for local
  behavior. Preserve conditions and conflicting reports; do not invent a
  universal winner from one run.
- Read both write-time conventions before updating durable documents. Use
  relative Markdown links and concise frontmatter with `path`/`why` links.
  Keep proposals in STATE and record a decision only when the user makes it.

This spec does not establish that a provider has been purchased, a harness is
configured or an untested route is ready. Current readiness belongs in STATE.
