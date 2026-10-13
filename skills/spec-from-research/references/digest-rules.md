---
created_at: 2026-10-13
updated_at: 2026-10-13
model: claude-sonnet-5-5
doc_type: reference
purpose: Digest rules and template the root hands to every digest worker when building a spec from a research report.
related:
  - path: ../SKILL.md
    why: The procedure that uses these rules (step 5).
  - path: ./packets.md
    why: Digest packet template that tells the worker to read this file.
---

# Digest rules

The root copies this file into the run scratch folder and fills the placeholders:
`<READER>` (see below), `<REPORT_PATH>` (the report copy inside the spec's
`sources/`), `<TODAY>`, and `<MODEL_EFFORT>` (what the packet runs on). Then each
digest packet says "read and follow `<SCRATCH>/digest-rules.md` exactly".

---

You are one digest worker. You read the verbatim source capture(s) your packet
names and write ONE digest file. You never spawn agents, never call another AI
CLI, never search the web, and never run git. Answer only from the files given.
When they do not cover something, say so. Do not add facts from memory.

## Who the reader is

<READER>

The root fills this in with the user's context, in 4 to 8 lines:

- the user's job and skill level;
- the workspace or tools they work in;
- what they want to learn or decide from this topic;
- what "fit" means for them (what they would copy, adapt or skip);
- that they are very busy.

## Writing style (strict)

- Plain, simple English. Short sentences.
- Explain any technical term the first time, in a few words.
- No em dashes (use commas, colons or full stops).
- No hype words ("crucial", "robust", "leverage", "delve", "seamless").
- Bullets start with "- ".

## Output

Write to the path your packet gives. Format:

```
---
created_at: <TODAY>
model: <MODEL_EFFORT, as your packet names it; do not guess another name>
doc_type: digest
source_ids: [<ids>]
source_files: [<relative paths of the captures you read>]
purpose: One-source digest feeding the spec superdocs.
---

# <Source title> (<ID>)

**What it is:** author, date, format, length or reading/watching time, link.
**Capture status:** full / partial / failed, and what is missing (from the capture's frontmatter).

## The point in three sentences

## Key ideas
- Each idea in one or two sentences, then a short verbatim quote in quotation
  marks with its location (section heading, FAQ question, or [hh:mm:ss]
  timestamp). Aim for 6 to 15 ideas; more for long sources.

## How to do it (concrete steps, checklists, templates)
Only steps the source actually gives. Keep their order.

## Tools, code and commands named
Exact names, commands and versions as written in the source.

## Numbers and strong claims
Each with location. Mark the ones that look like marketing or opinion.

## Compared with the research report
The report is at <REPORT_PATH>. Read only its part about this source. List what
the report got right, what it got wrong or overstated, and what important
content it left out. Quote both sides briefly.

## Fit for the user's workspace
3 to 8 bullets, each marked "(inference)". What would they copy, adapt or skip.

## Best parts to read or watch first
Pointers by heading or timestamp, with how long each takes.
```

## Rules

- Best parts first: the reader may stop after the top of the file.
- Every quote must be copied from the capture exactly. Confirm each with `grep`
  (use a short, unique fragment of the quote).
- If the capture is `partial` or `failed`, say so in the first lines and digest
  only what exists. Do not fill gaps from memory.
- Length: as long as the source needs, usually 600 to 2,000 words. Up to 3,500
  for very long sources (FAQ, podcast transcript, full course).
- Print `PROGRESS n/total` as you go.
- Final message: the digest path, word count, and anything you could not do.

## Additions for several topics (library-first mode)

Use these when the reports span several topics and the specs are decided after
the digests exist. See "Several reports or several topics" in
[../SKILL.md](../SKILL.md).

- Add a `themes:` field to the frontmatter. Pick values only from a fixed list
  the root writes into the rules file, fitted to the user's goals.
- Add a section "## Related sources" after "Compared with the research report".
  List other source IDs this one agrees with, contradicts, builds on or
  duplicates, one line each. Use only IDs the packet gives you.
- "Compared with the research report" now covers every report in the library
  (`A00a`, `A00b`, ...), not one.
- The digest file name comes from the digest's H1 title, as a slug. Never name it
  after the first capture file. The first file alphabetically was often a
  CHANGELOG or CONTRIBUTING file.
