---
created_at: 2026-10-13
updated_at: 2026-10-13
model: claude-sonnet-5-5
doc_type: reference
purpose: Short packet templates and the launcher pattern for the spec-from-research skill.
related:
  - path: ../SKILL.md
    why: The procedure that says when to send each packet.
  - path: ./capture-rules.md
    why: Rules every capture packet points to.
  - path: ./digest-rules.md
    why: Rules every digest packet points to.
  - path: ~/agents/ai-models/delegation-briefing.md
    why: Where to pick the model, effort and worker count for each packet.
---

# Packet templates

Placeholders the root fills in:

- `<SPEC>`: the spec folder, for example `specs/<topic>`.
- `<SCRATCH>`: the run scratch folder (rules, raw files, per-packet run folders).
- `<TODAY>`: the date.
- `<PREFIX>`: the topic's source letter, for example `E` or `Y`.
- `<model>` and `<effort>`: pick from `ai-models/delegation-briefing.md` for your
  harness. Parallel packets use the cheap tier. Blocking packets use the fast tier.

Every packet starts with the same three lines:

```
Packet <ID>. First read and follow <SCRATCH>/<rules file> exactly.
Working folder: ~/agents. You are one worker.
Do not spawn agents, call other AI CLIs, or run git. Write only the files named below.
```

Keep each packet short. Put shared rules in the rules file, not in the packet.

## Capture packet

```
Packet <ID>. First read and follow <SCRATCH>/capture-rules.md exactly.

Output folder: <SPEC>/sources
- <URL 1> -> <PREFIX><nn>-<short-slug>.md
- <URL 2> -> <PREFIX><nn>b-<short-slug>.md
(For a repo or site: the main README as <PREFIX><nn>-<slug>-README.md, plus each
listed doc as <PREFIX><nn>-<slug>-<path-with-dashes>.md. Do not capture
notebooks in full: write an index with each path and its first markdown cell.)
List every video or follow-up link you find in a file <PREFIX><nn>-<slug>-links.md
(URL, title if shown, where it was linked). Do not transcribe videos unless this
packet says so.
Print PROGRESS n/total after each URL.
```

Sizing: 1 to 3 URLs, or one repo or one site, per packet. Name the files in the
packet so two workers never write the same path.

## Digest packet

```
Digest packet D-<ID>. First read and follow <SCRATCH>/digest-rules.md exactly.
Working folder: ~/agents.

Read these captures fully:
- <SPEC>/sources/<file 1>
- <SPEC>/sources/<file 2>

Write the digest to: <SPEC>/digests/<ID>-<slug>.md
Your model line in the frontmatter: <model> <effort>.
```

One digest per capture group. A group is one source and its sub-files.

## Compendium packet (blocking, fast tier)

```
Packet S1: write the COMPENDIUM. Working folder: ~/agents.
Inputs: every file in <SPEC>/digests/, the report copy <PREFIX>00 in
<SPEC>/sources/, and the captures (open them to check any quote or number;
every quote must exist verbatim in a capture, confirm with grep).
Read <SCRATCH>/digest-rules.md for the reader and the style.
Output: <SPEC>/COMPENDIUM.md. Frontmatter: created_at, model, doc_type:
compendium, purpose, related (path + why) for ./spec.md,
./IMPLEMENTATION-GUIDE.md, ./SOURCES.md, ./digests/, ./sources/.
Parts:
1. How to use this document (read times).
2. The topic in one page, for a reader who knows the neighbouring field.
3. Glossary: every term the sources use, one or two plain sentences, with source IDs.
4. The method, step by step, with the sources that teach each step best.
5. Topic-specific deep part(s) the sources demand.
6. Where sources agree and disagree, including disagreements with the report.
7. Tools and code compared, with inferences marked.
8. Every source, one entry each, for EVERY capture group and sub-file:
   title and link, type and length, capture status, the point in two sentences,
   best parts with time, relative links to capture and digest.
9. What the report got wrong or missed, with evidence.
10. Suggested learning path with time per item and a deliverable per stage.
Use relative links. Cite sources inline by ID. Write in sections and save as
you go. Print PROGRESS n/10.
Final message: path, word count, sources not covered and why, and the 5 claims
you are least sure of.
```

Adjust parts 2, 4, 5 and 10 to the topic.

## Implementation guide packet (blocking, fast tier)

```
Packet S2: write the IMPLEMENTATION GUIDE. Working folder: ~/agents.
The ask, in the user's words: <paste the user's request, shortened>.
Inputs: <SPEC>/digests/ and sources (COMPENDIUM.md is written in parallel; link
to it as ./COMPENDIUM.md but do not wait). Read the workspace files that decide
fit: AGENTS.md, INDEX.md, roles/task-worker-tiers.md, skills/AGENTS.md,
<other files the root names>.
Read <SCRATCH>/digest-rules.md for the reader and the style.
Output: <SPEC>/IMPLEMENTATION-GUIDE.md. Frontmatter: created_at, model,
doc_type: guide, purpose, related.
Parts:
1. Recommendation first (10 lines max), with the single first step for today.
2. Depth levels by time budget (2 hours, 1 day, 1 week, ongoing): goal, steps,
   deliverables, what you learn, "stop here if".
3. Is a skill enough? Straight answer, options compared, a recommended combination.
4. Proposed design for this workspace: folder layout, first target, first
   checks, how results feed back, a draft SKILL.md outline, sketches marked untested.
5. Costs and risks, and how to keep them low.
6. Exact next actions as a checklist an agent can take.
Mark every inference. Cite sources by ID and workspace files by path.
Print PROGRESS n/6. Final message: path, word count, the decisions the user must
make before building, and any input you could not read.
```

## Spec files packet (blocking, fast tier)

```
Packet SP: write the spec files in <SPEC>. Working folder: ~/agents.
First read conventions/memory-files.md section "Spec Folder Organization" and
conventions/artifact-authoring.md.
Write:
- spec.md: one-paragraph summary, Start Here router (status, decisions, sources,
  COMPENDIUM.md, IMPLEMENTATION-GUIDE.md), then the topic's durable content.
- STATE.md: short and current (status, what ran, open questions, next step).
- SOURCES.md: the evidence ledger. One row per source: ID, URL, type, capture
  status, capture file, digest file. A section "Links not captured" for third-hop
  links. A section "Weak claims to avoid".
- DECISIONS.md: ONLY decisions the user actually made, with date and reason. If
  there are none, say so. Do not invent decisions.
- AGENTS.md: 10 lines or fewer. What the folder is and which file to read first.
Use the digests and the ledger numbers the root gives you: <counts>.
Final message: the paths and word counts.
```

## Review packet (blocking, fast tier)

```
Packet R1: check and fix the superdocs and spec files. Working folder:
~/agents. You may edit ONLY <the files the root names>, with small
in-place fixes. Never rewrite a section. Never touch <SPEC>/sources/.
Checks, with scripts where possible:
1. Quotes: extract every quoted string of 6+ words. grep the cited capture. Fix
   to the exact source text if the meaning holds, otherwise remove.
2. Citations: pick 25 factual claims (numbers, dates, names, features, prices).
   Check each against the cited capture. Fix or mark "(not in sources)".
3. Coverage: every capture group and sub-file in sources/ has an entry in the
   compendium. Every relative link in every doc resolves.
4. Workspace claims: every workspace path cited exists and says what the doc says.
5. Style: no em dashes, no hype words, split the 20 worst sentences over 35 words.
Output: a review file under artifacts/reviews/ following
conventions/artifact-authoring.md: counts per check, each fix (before -> after),
and anything unresolved.
Final message: counts and the 5 most serious problems.
```

## Multi-topic packets (library-first mode)

Used by "Several reports or several topics" in [../SKILL.md](../SKILL.md).

### Relationship mapper packet (cheap tier, parallel)

```
Packet M-<n>: map relationships. First read <SCRATCH>/digest-rules.md for the reader.
Working folder: ~/agents. You are one worker.
Do not spawn agents, call other AI CLIs, search the web, or run git.
Read these digests fully (about 10): <list>.
Read the overview of existing specs, skills and roles: <SCRATCH>/workspace-overview.md.
Write <SCRATCH>/maps/M-<n>.md with:
1. One table row per source: ID, themes, workspace parts it would change,
   related IDs and how they relate, best spec home.
2. Clusters of sources that belong together.
3. Tensions: sources that disagree.
4. Overlaps with existing workspace specs.
Mark inference as inference. Print PROGRESS n/total.
```

### Architect packet (blocking, fast tier)

```
Packet AR: write <PROJECT>/ARCHITECTURE.md from every file in <SCRATCH>/maps/.
Working folder: ~/agents. Read the overview of existing specs too.
Parts:
1. The spec list, each with "owns" and "does not own".
2. Every source primary in exactly one spec (a check table).
3. An ID-to-spec table.
4. Glossary ownership: which spec defines which term.
5. How the specs link to each other.
6. Which existing specs stay or move (default: leave and link).
7. A writer brief per spec: emphasis, stages, files to read, tensions, missing
   topics.
Final message: path, word count, the 5 judgments you are least sure of.
```

The root reads the file fully and adds "section 0, root acceptance notes" at the
top for any override. Writers read section 0 first.

### Dispatcher

A small script (one background shell) runs the per-spec pipeline: compendium and
guide drafts, gap web search (only if the user asked), revise and research
prompts in parallel, review. It starts each spec's next step when that spec's own
inputs are done, not when every spec is done. Before you kill and relaunch a
worker, stop the dispatcher first, or it treats the killed worker as finished.
In zsh, count output files with `find`, not `ls` globs.

### Guide stages

Tell every guide writer: use stages of rising effort. Stage 1 is a few hours with
no new infrastructure. The last stage is peak performance with the highest
adoption cost. End every stage with a "Measure" line that points at the spec
that owns measurement.

### Gap search, research prompt and final review packets

- Gap search (only on explicit user request): follow
  [web-search](../../web-search/SKILL.md). Give the worker its reserved ID range
  (for example `A80` to `A89`) and the gaps from the drafts. New sources are
  captured verbatim and digested. The findings report goes under
  `artifacts/investigations/`.
- Research prompts: per spec, 1 to 3 ready-to-run prompts in
  `RESEARCH-PROMPTS.md`, following
  [browser-deep-research-prompts](../../browser-deep-research-prompts/SKILL.md).
  They are proposals; the user picks size and mode later.
- Final review (blocking, fast tier): one worker reads all specs, writes the
  project glossary, and writes `ROADMAP.md` with one adoption order across specs.

# Launcher pattern

One background shell per worker. Never run workers in the root's foreground.

- Make a run folder per packet: `<SCRATCH>/runs/<ID>/` with `prompt.txt`,
  then `events.jsonl`, `stderr.log`, `final.txt` and `retries.log` written by the
  launcher.
- The launcher takes the packet ID and effort, runs the harness CLI headless with
  the prompt on stdin, writes JSON events to `events.jsonl`, and writes the last
  message to `final.txt`. For the exact flags, read the `task-*` skill for the
  harness you are launching (`skills/task-codex`, `task-claude`, `task-opencode`,
  `task-gemini`). Pass `<model>` and `<effort>` from the briefing.
- If `events.jsonl` contains "at capacity" (or the harness's equivalent
  overload text), wait `try * 40` seconds, log the retry and run again. Give up
  after 4 tries and report the packet as failed.
- Otherwise exit with the CLI's exit code.
- Start 10 to 15 cheap capture or digest workers at once, each in its own
  background shell. Respect the count rules in the briefing for premium workers.
  Check progress by reading `final.txt` and the last `PROGRESS` line in
  `events.jsonl`.

Skeleton (adapt the CLI line):

```
#!/bin/zsh
# usage: launch.sh <packet-id> <effort> <model>
R=<SCRATCH>/runs/$1
for try in 1 2 3 4; do
  <harness CLI headless command, model $3, effort $2, prompt from $R/prompt.txt,
   events to $R/events.jsonl, last message to $R/final.txt, stderr to $R/stderr.log>
  rc=$?
  if grep -q "at capacity" $R/events.jsonl; then
    echo "try $try: at capacity, retrying" >> $R/retries.log
    sleep $((try*40)); continue
  fi
  exit $rc
done
exit 1
```

Rules for the root while workers run:

- Do not read half-finished output. Wait for each worker's `final.txt`.
- Verify files on disk after each worker: the file exists, the frontmatter is
  present, `completeness` is honest, the word count is plausible.
- Re-run a failed packet once with a narrower packet, then record the failure in
  `SOURCES.md` instead of looping.
