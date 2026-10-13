---
created_at: 2026-10-13
updated_at: 2026-10-13
model: claude-sonnet-5-5
doc_type: state
status: sources captured and digested; two superdocs drafted; nothing built yet
scope: Learning LLM and agent evals, and a proposed worker-evals loop for the Agents workspace
related:
  - path: ./spec.md
    why: Router for this spec.
  - path: ./SOURCES.md
    why: Capture ledger, links not captured, weak claims.
  - path: ./DECISIONS.md
    why: What the user decided.
  - path: ./IMPLEMENTATION-GUIDE.md
    why: Section 6 holds the next actions and open decisions summarised here.
---

# LLM evals: state

## What exists now (13 October 2026)

- **71 verbatim captures** in `sources/` (not published in this snapshot), plus one raw timed transcript JSON for E03. 68 are full, 2 are partial, 1 failed. Full list: [SOURCES.md](SOURCES.md).
- **22 digests** in [digests/](digests/), one per source or small group, all written by gpt-6.1-sol at low, medium or high effort.
- **Two superdocs:** [COMPENDIUM.md](COMPENDIUM.md) (about 15,000 words, every source gets an entry) and [IMPLEMENTATION-GUIDE.md](IMPLEMENTATION-GUIDE.md) (about 7,000 words, steps for 2 hours, 1 day, 1 week and ongoing). Both are built from the digests and captures. A review on 2026-10-13 checked 42 claims against the captures, every link and the writing style, and fixed 7 small issues (review record: private, not published). The root read the guide's recommendation, skill verdict and folder layout and accepted them.
- **Spec files:** this file, [spec.md](spec.md), [SOURCES.md](SOURCES.md), [DECISIONS.md](DECISIONS.md), [AGENTS.md](AGENTS.md).
- **No tool or integration from the sources was run.** The guide says the same: its designs, sketches and sample configs are untested.

## Coverage gaps

Each gap is stated in the capture's own frontmatter. Nothing below is guessed.

- **E16h, the Loom video (failed).** The Recipe Chatbot optional Phoenix tracing walkthrough. Loom says the video "may have been deleted or archived by its creator." No title, transcript or metadata. E12 optional Phoenix homework README is the only text on it.
- **E04, Lenny episode page (partial).** The written section "My biggest takeaways from this conversation" is paywalled and left out. The full public transcript was captured by another route. The same episode as a YouTube video is E03.
- **F01a, "Building eval systems that improve your AI product" (partial).** Public preview only. Paywalled from "Phase 3: Operationalizing evals for continuous improvement" onward.
- **DeepLearning.AI lab notebooks (E08 labs 1 to 5).** The lesson pages and transcripts are captured in full; the notebooks need a login and are not included.
- **Recipe Chatbot notebooks (E12).** The notebook index holds the first markdown cells of the 4 notebooks only. The repo README files, homework files and video links are full.
- **Video transcripts are YouTube automatic captions** (E03, E16a to E16g). Original words are kept, but names and numbers can be wrong. Not human-checked.
- **E08 appendix lesson** (resources, tips and help) was not captured. It sits in the third hop.
- **Third-hop links (14).** Seen inside sources, not fetched, because link-following stopped at two hops. Listed with reasons in [SOURCES.md](SOURCES.md#found-but-not-captured-third-hop).
- **E02 is thin.** The Hacker News thread has 5 comments, so it is a pointer, not evidence of what the community thinks.
- **YouTube blocking.** The home IP began returning blocks after a burst of transcript requests. All E03 and E16 transcripts were saved before that. Refetching them later may fail; see [../youtube-extraction/STATE.md](../youtube-extraction/STATE.md).

## What is not built

- The `worker-evals` skill, its case files, fixtures, checks and runner. The guide's SKILL.md outline and sample promptfoo config are sketches.
- Any run of promptfoo, Inspect AI, AgentEvals or the evals-skills against our workers.
- Any model-mapping or briefing change. The guide proposes one only if evidence supports it, and each harness verifies its own mapping.
- A human-labelled set for a judge. None exists.

## Next steps

From [IMPLEMENTATION-GUIDE.md section 6](IMPLEMENTATION-GUIDE.md#6-exact-next-actions). All of these are proposals, none is authorized.

1. Review five recent `task-execute` runs and write one failure note per flawed run (the guide's first step, about 2 hours).
2. Pick one observed failure. Write its pass rule and a known good result. Build one tiny fixture and one code check that passes the good result and fails a deliberate violation.
3. Replay one live worker in a fresh fixture and check the real file changes.
4. Grow to five to ten cases, then add a local promptfoo suite if replay by hand gets tedious.
5. If the work becomes serious durable implementation, run it through `plan-create`, `plan-execute` and `plan-reconcile` with a bounded change packet.
6. Optional reading while waiting: the compendium's part 10 learning path.

## Decisions the user still has to make

From the guide's "Three decisions before building". The guide offers a default for each, so review of saved runs can start now.

| Decision | Suggested default (inference) |
|---|---|
| First role, harness and task class | Codex `task-execute`, small one-file TypeScript edits |
| Depth and run budget | One-day pilot, five to ten cases, one subject profile, one-hour execution limit, $5 of API use or an explicit quota allowance |
| Who can accept work | Mandatory code checks plus root review. No judge-based acceptance until a judge is calibrated and approved |

Open question inside the third decision: if you later let a judge accept work, you must decide how many missed failures and how many rejected good outputs you can live with. The sources give targets but do not make that call.
