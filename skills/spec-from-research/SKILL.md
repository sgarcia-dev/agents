---
name: spec-from-research
description: Use when the user hands over one or more deep research reports and wants a spec per topic, with a verbatim copy of every linked source, one digest per source, and a compendium plus an implementation guide.
created_at: 2026-10-13
updated_at: 2026-10-13
model: claude-sonnet-5-5
doc_type: skill
purpose: Turn a deep research report into a durable spec folder (verbatim sources, digests, superdocs, spec files) by delegating capture, digest, synthesis and review to bounded workers.
related:
  - path: ./references/capture-rules.md
    why: Rules every capture worker follows (tools write the text, fetch ladder, special routes, file format).
  - path: ./references/digest-rules.md
    why: Digest template and style rules with a placeholder for the reader.
  - path: ./references/packets.md
    why: Packet templates for each step and the launcher pattern.
  - path: ~/agents/ai-models/delegation-briefing.md
    why: Picks the model, effort and worker count (sections 1 to 3; "Blocking step" in section 2).
  - path: ~/agents/roles/task-worker-tiers.md
    why: Packet size, enabled roles and worker limits.
  - path: ~/agents/conventions/memory-files.md
    why: Spec Folder Organization: what spec.md, SOURCES.md, DECISIONS.md and STATE.md own.
  - path: ~/agents/conventions/artifact-authoring.md
    why: Frontmatter and location rules for generated files, including the review file.
  - path: ~/agents/capabilities/web/README.md
    why: Web tool strengths and fetch ladders; keep the capture ladder in line with it.
  - path: ~/agents/skills/research/SKILL.md
    why: Sibling skill for read-only investigation that does not build a spec.
  - path: ~/agents/skills/web-search/SKILL.md
    why: Rules for the optional gap web search in multi-topic mode.
  - path: ~/agents/skills/browser-deep-research-prompts/SKILL.md
    why: Rules for the deep research prompts written in multi-topic mode.
---

# Spec From Research

The root plans, delegates and checks. Workers do the capture, digest, synthesis
and review. You do not read the web or write the big documents yourself.

## When to use

- The user gives you a deep research report (a file in `~/Downloads` or a path)
  and asks for a spec, a source library, or "everything it links to".
- Use `research` instead when the user wants an answer, not a spec.
- Use `plan-create` instead when the goal is a code change, not a knowledge base.

## Inputs

- One or more reports. For one report on one topic, the report becomes one spec.
  For several reports that span several topics, use "Several reports or several
  topics" below. Do not pick the specs up front.
- The reader: who the user is, what they will do with the topic, what "fit"
  means for their workspace. Ask once if you cannot tell. Write it into
  `digest-rules.md` as the reader section.
- The user's ask for the superdocs, in their words. Keep it for the guide packet.
- Read before you start: `ai-models/delegation-briefing.md` (sections 1 to 3),
  `roles/task-worker-tiers.md`, `conventions/memory-files.md` ("Spec Folder
  Organization") and `conventions/artifact-authoring.md`.

## Resulting folder

```
specs/<topic>/
  spec.md                    router with Start Here
  STATE.md  SOURCES.md  DECISIONS.md  AGENTS.md
  COMPENDIUM.md              every source, glossary, method, agreements, tools
  IMPLEMENTATION-GUIDE.md    recommendation first, depth by time budget
  sources/                   verbatim captures: <P>00-report, <P>01-..., <P>12b-...
  digests/                   one digest per capture group
  tests/                     real tests, when the topic allows them
```

`<P>` is one letter per topic (for example `E`, `Y`). `00` is the report copy.
Other topics may need different superdocs; keep the compendium and change the
guide to fit the user's ask. Global or cross-project topics go in root `specs/`.
Project topics go in `projects/<project>/specs/`.

## Procedure

Set up `<SCRATCH>` first (the session scratchpad). Copy the two rules files from
`references/` into it and fill the placeholders. Keep raw dumps and scripts out
of the spec.

### 1. Intake

- Copy each report into `sources/<P>00-<slug>.md` with capture frontmatter
  (source path, `captured_at`, `completeness`, notes).
- Check: `cmp` the copy against the original (byte-identical body).
- Move the Downloads original to the Trash only after the check and after the
  files are in place.

### 2. Extract and group links

- List every URL in the report with a script, in order, with the report line.
- Group them into packets: 1 to 3 URLs, or one repo or one site. Give each group
  an ID and the exact output file names. No two packets share a path.
- Check: every URL is in exactly one packet. Write the grouping to
  `<SCRATCH>/plan.md`.

### 3. Capture, hop 1

- Send one capture worker per packet (`references/packets.md`, capture packet).
  Run 10 to 15 at once, each in its own background shell. Pick the cheap tier
  for your harness from the briefing.
- The key rule: tools write the text to disk, workers never retype it
  (`references/capture-rules.md`).
- Check after each worker: files exist, frontmatter is complete, `completeness`
  is honest, no cookie wall or error page, word count is plausible. Read the
  one-line-per-file report. Retry a failed packet once, narrower.
- YouTube: space video captures out. About 20 transcript requests in 10 to 15
  minutes gets a home IP blocked. Fall back to Firecrawl (it returns untimed
  text). Run one paced video worker at a time. A VPN with a fresh exit IP
  restored transcripts at once after the home IP was blocked, but that exit was
  also blocked after about 17 requests in about 10 minutes from two workers
  pacing 20 seconds apart. See
  YouTube extraction state (private, not published).

### 4. Second hop, then stop

- Collect the follow-up links workers reported. Pick the ones that carry real
  weight (key videos, articles the sources lean on). Capture them with the same
  packets, IDs continuing the series.
- Stop at two hops. Write every third-hop link into `SOURCES.md` under "Links not
  captured". Do not chase them.

### 5. Digest round

- One digest worker per capture group (`references/packets.md`, digest packet,
  `references/digest-rules.md`). Run them in parallel, cheap tier.
- Check: the digest exists, follows the template, best parts first. Grep 3
  quotes per digest in the capture. A digest with a bad quote goes back once.
  Put partial or failed captures in the digest header, not in the middle.

### 6. Superdocs

- Run the compendium and the implementation guide in parallel from the digests
  (`references/packets.md`). Both are blocking steps: use the fast tier.
- Tests in this step: if the topic allows a real test (a tool you can run, a
  method you can compare), run it now and save results in `tests/`. Measured
  results outrank the report. Feed them to both superdocs before they finish, or
  fix the docs after.
- Check: every capture group has a compendium entry, the guide opens with the
  recommendation, and both state what they could not cover.

### 7. Spec files

- One worker (fast tier) writes `spec.md` (router with Start Here), `STATE.md`,
  `SOURCES.md` (ledger), `DECISIONS.md` and `AGENTS.md`, following
  `conventions/memory-files.md`.
- `DECISIONS.md` holds only decisions the user actually made. If they made none,
  it says so. Do not invent decisions.
- Check: the ledger counts match `sources/` and `digests/`; every link resolves.

### 8. Review

- One review worker (fast tier) checks quotes, 25 random citations, coverage,
  relative links, workspace paths and style, with scripts where possible
  (`references/packets.md`, review packet). It writes a review file under
  `artifacts/reviews/` and fixes small errors in place.
- Check: read the review counts. Re-run the quote check yourself on a sample.
  Anything unresolved goes to the user in the final report.

### 9. Commit

- Follow the Git Completion Gate in the kernel `AGENTS.md`. Commit the spec,
  push, and report the hash. Commit the superdocs only after review.

## Several reports or several topics

Use this mode when the reports span several topics. The single-report procedure
above still describes capture, digest and review. What changes is the order:
the library first, the specs after. Packet templates are in
[references/packets.md](./references/packets.md); the digest additions are in
[references/digest-rules.md](./references/digest-rules.md).

### Library first

- Do not pick specs up front. Build one shared library at the project level:
  `sources/` and `digests/`, one ID series (`A01`, `A02`, ...), with `A00a`,
  `A00b` for the reports themselves.
- Decide the specs only after the digests exist.
- Digest template additions for this mode: a themes field with a fixed list
  fitted to the user's goals, a "Related sources" section, and a comparison
  against every report.
- Name each digest file from the digest's H1 title, not from the first capture
  file. The first file alphabetically was often a CHANGELOG or CONTRIBUTING
  file.

### Relationship mapping round

- Run many cheap-tier mappers in parallel, each on a slice of about 10 digests.
- Each mapper writes one table row per source: themes, the workspace parts it
  would change, related IDs and how they relate, and the best spec home. It also
  writes clusters, tensions, and overlaps with existing workspace specs.
- Give each mapper a short overview file of the existing specs, skills and
  roles. Build it by script.

### Architecture step (blocking)

- One fast-tier architect reconciles the mapper outputs into `ARCHITECTURE.md`.
  This is a judgment step. See "Blocking step" in section 2 of the briefing.
- It holds: the spec list with "owns" and "does not own"; every source primary
  in exactly one spec; an ID-to-spec table; glossary ownership; how the specs
  link; which existing specs stay or move (default: leave and link); and a
  writer brief per spec (emphasis, stages, files to read, tensions, missing
  topics).
- The root reads it fully. The root records overrides in a "section 0, root
  acceptance notes" at the top, so writers see them.

### Per-spec pipeline

A small dispatcher script drives it. Each spec moves on as soon as its own
inputs are done.

1. Compendium and implementation guide drafts.
2. Gap web search (below).
3. Revise the drafts, and write the research prompts, in parallel.
4. Review.

Then write a project glossary. Then run one cross-spec final review that also
writes a `ROADMAP.md`: one adoption order across all the specs.

Each implementation guide uses stages of rising effort. Stage 1 is a few hours
with no new infrastructure. The last stage is peak performance with the highest
adoption cost. Every stage ends with a "Measure" line that points at the spec
that owns measurement.

### Gap web search

- It comes AFTER the drafts, not before. The gaps are only known once the specs
  take shape. This was the user's call on 2026-10-13.
- Run it only on an explicit user request, following
  [web-search](../web-search/SKILL.md).
- Reserve an ID range per spec (for example `A80` to `A89`) so parallel workers
  never collide.
- Capture the new sources verbatim and digest them like the rest. Write the
  findings into a report under the project's `artifacts/investigations/`.

### Deep research prompts

- Per spec, write 1 to 3 ready-to-run prompts in `RESEARCH-PROMPTS.md`, for
  questions web search could not settle. Follow the rules in
  [browser-deep-research-prompts](../browser-deep-research-prompts/SKILL.md).
- They are proposals. The user picks size and mode later through that skill.

### Root checks that worked

- A script that checks every quote of 6 or more words in every digest against
  that group's captures plus the report text, after stripping code spans. On one
  run it checked 510 quotes and found near zero real misses.

### Operations

- Before you kill and relaunch a worker, stop the dispatcher first. Otherwise it
  treats the killed worker as finished.
- In zsh, a glob that matches nothing aborts the command. Wait loops should
  count files with `find`, not `ls` globs.

## Worker routing

- Pick every model, effort and count from the briefing. Never name a model in
  this skill or in a packet; use the briefing and the harness mapping.
- Parallel fan-outs (capture, digest) go to the cheap tier. Slow is fine because
  nothing waits on one worker.
- Blocking steps (superdocs, spec files, review) go to the fast tier. See
  "Blocking step" in section 2 of the briefing. A slow model cost 20 or more
  minutes per blocking step.
- Capacity errors are normal. The launcher retries with backoff
  (`references/packets.md`, launcher pattern).
- Workers are terminal. They do not spawn workers or call other AI CLIs.
- Ask every worker to print `PROGRESS n/total` and to end with one line per
  file: `path | completeness | method | words | notes`.

## Stop rules

- Two hops of links, no more.
- One retry per failed packet. Then record it in `SOURCES.md`.
- No third-party logins, paywall tricks or bot-wall bypasses. A blocked page is
  `completeness: failed` with the reason.
- Do not write conclusions into the spec that the sources do not support. Mark
  inference as inference.
- Do not turn user preferences into decisions. Ask, or leave them open.

## Final report

Reply in plain words, short:

- Status and spec path.
- Counts: sources captured (full, partial, failed), digests, third-hop links
  left, tests run.
- Where to start: the one file to open first and the first action to take.
- What the report got wrong or missed, top 3.
- Decisions the user must make.
- Anything unresolved from the review.
- Any model or speed problem worth adding to the briefing's field notes.
- `Agents commit: <hash> (pushed)`.
