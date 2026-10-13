---
created_at: 2026-10-13
updated_at: 2026-10-13
model: claude-sonnet-5-5
doc_type: agents
purpose: How agents work inside the LLM evals spec: layout, naming, and how to add a source.
related:
  - path: ./spec.md
    why: Router; read first.
  - path: ./STATE.md
    why: Current gaps and open decisions.
  - path: ./SOURCES.md
    why: Ledger to update when a source changes.
  - path: ../../skills/spec-from-research/SKILL.md
    why: The procedure that built this spec, including capture and digest rules.
  - path: ../youtube-extraction/spec.md
    why: How to pull YouTube transcripts for new video sources.
---

# LLM evals: how to work here

This spec teaches how to evaluate LLM apps and agents and proposes a small worker-evals loop for the Agents workspace. Read [spec.md](spec.md) first, then [STATE.md](STATE.md). Open [COMPENDIUM.md](COMPENDIUM.md) to learn and [IMPLEMENTATION-GUIDE.md](IMPLEMENTATION-GUIDE.md) to build. The procedure that created this folder is [skills/spec-from-research/SKILL.md](../../skills/spec-from-research/SKILL.md); use it again for the next research report.

## Layout

- `spec.md`: the router. Short.
- `STATE.md`: what exists, gaps, next steps, open decisions.
- `DECISIONS.md`: choices the user made. Not proposals.
- `SOURCES.md`: evidence ledger (every capture and digest), links not captured, weak claims to avoid.
- `COMPENDIUM.md`: superdoc 1. Teaches evals through every source, one entry each.
- `IMPLEMENTATION-GUIDE.md`: superdoc 2. Recommendation first, then steps by time budget.
- `sources/`: verbatim captures of the starting report and every linked page, repo file or video transcript. One file per page or file.
- `digests/`: one digest per source or small group, in a fixed template (point in three sentences, key ideas with quotes, steps, tools, numbers, comparison with the starting report, fit for the workspace).

## Rules

- **Sources are verbatim and never edited.** Do not fix typos, trim, reformat or add notes inside `sources/`. If a capture is wrong or incomplete, capture it again with a better tool and say why in its frontmatter.
- **Tools write the text.** Never retype or paste page text by hand. Use a fetch tool, API or script that writes the file to disk.
- **Every capture has frontmatter:** `source_url`, `title`, `author`, `published`, `captured_at`, `capture_method`, `methods_tried`, `completeness` (full, partial or failed) and `capture_notes` (what is missing, in plain words).
- **Videos:** follow [../youtube-extraction/spec.md](../youtube-extraction/spec.md). Transcripts here are automatic captions. Do not hammer YouTube from the home IP; the block timeline is in that spec.
- **Quotes must be exact.** Copy from the capture and confirm with grep before putting a quote in a digest or superdoc.
- **Label inference.** The guide marks designs and numbers as inference. Keep that when you edit.
- **Plain style:** short sentences, no em dashes, bullets start with "- ".
- The starting report (E00) is a set of leads. If a capture disagrees with it, the capture wins; log the disagreement in [SOURCES.md](SOURCES.md) "Weak claims to avoid" and in compendium part 9.

## Naming

- **E##:** a link from the starting report, numbered in the order the report first links it (E01 to E15). E00 is the report copy. E16 is the group of videos linked from E05, E12 and E13 (E16a to E16h).
- **Letters (E11a, E11b):** several captures from one source. Used when a source is a set of pages or videos (promptfoo docs, Inspect docs, AgentEvals READMEs, the videos E16a to E16g, the unavailable Loom E16h).
- **E05b:** the real post behind a redirect page (E05). **E13z:** the archived predecessor of E13.
- **E08-lesson-NN and E12-recipe-chatbot-*, E13-evals-skills-*:** files inside one course or repo keep the source ID and a descriptive tail.
- **F##:** a link found inside a captured source (hop two). F01a to F01d. Links found only inside hop two are not captured; they go in the SOURCES.md third-hop table.
- **Digest files:** `<ids>-<slug>.md` in `digests/`. Frontmatter `source_ids` and `source_files` point at the captures. Model line is `gpt-6.1-sol (<effort>)`.
- Large raw transcripts keep a `.raw.json` beside the capture (E03 only).

## How to add a source

1. **Capture** it with a tool into `sources/` under the next free ID (next E## if it is from a new report, F## if it came from reading a source). Fill the frontmatter honestly, including `completeness`. A paywall or login wall is `partial`; an unreachable page is `failed`.
2. **Digest** it: add `digests/<id>-<slug>.md` in the standard template, or add the source to its group's digest. Quote exactly; compare with E00 if E00 mentions it.
3. **Update the compendium:** add or edit the entry in part 8 ("Every source, one entry each"). Revise parts 3 to 7 only if the source changes what we know; then check part 9 and the learning path in part 10.
4. **Update [SOURCES.md](SOURCES.md):** add the table row (words include frontmatter) under the right group, add the digest row, and remove the link from the third-hop table if it was there.
5. **Update [STATE.md](STATE.md)** counts and gaps. Add a decision to [DECISIONS.md](DECISIONS.md) only if the user decided something.
6. If the new source changes the recommendation, edit the guide's section 1 and the "Current answer" in [spec.md](spec.md).

## Where outputs go

Generated reports about this spec go under the root `artifacts/` roots, not in this folder. Edits to `sources/` and `digests/` are covered above. Read [../../conventions/memory-files.md](../../conventions/memory-files.md) before changing STATE, DECISIONS or SOURCES.
