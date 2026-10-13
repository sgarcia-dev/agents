---
created_at: 2026-10-13
updated_at: 2026-10-13
model: claude-sonnet-5-5
doc_type: decisions
purpose: The choices the user made when starting the LLM evals spec, with the reason for each.
related:
  - path: ./spec.md
    why: Owning spec.
  - path: ./STATE.md
    why: Current status and open decisions.
  - path: ./AGENTS.md
    why: How the layout decisions below show up in daily work.
  - path: ../../ai-models/delegation-briefing.md
    why: Owns worker model policy; section 2 "Blocking step" holds the 13 October worker rule.
---

# LLM evals: decisions

Only decisions the user made are listed. Proposals in the guide (for example the first role, the budget and judge authority) are not decisions; they are in [STATE.md](STATE.md) as open questions.

## 2026-10-13

- **Start a new LLM evals spec, seeded from a ChatGPT deep research report.** The report is kept as E00. Its claims are leads; each linked source was captured so claims can be checked against the originals.
- **Store a verbatim copy of every linked source inside the spec, under `sources/`, not under `artifacts/`.** Reason: this material is specific to this spec.
- **Digest every source, then feed the digests into two superdocs.** One digest per source or small group. Superdoc 1, the [compendium](COMPENDIUM.md), covers every source. Superdoc 2, the [implementation guide](IMPLEMENTATION-GUIDE.md), gives steps by time budget (2 hours, 1 day, 1 week, ongoing).
- **Split YouTube extraction into its own spec.** It lives in [../youtube-extraction/spec.md](../youtube-extraction/spec.md); this spec only uses its results (the video transcripts E03 and E16a to E16g).
- **Choose the cheapest workers that do the job; the root only orchestrates.** Capture, digest and writing workers ran on Codex with GPT-6.1 Sol at low, medium or high effort, matched to the packet. The root planned, delegated and checked.
- **Keep Sol for wide parallel fan-outs, and run sequential blocking steps on faster Claude workers (Sonnet 5.5 high; Opus 5.5 medium when the step needs judgment).** The spec files and the review of this spec were the first steps run that way. Policy lives in [../../ai-models/delegation-briefing.md](../../ai-models/delegation-briefing.md), section 2, "Blocking step"; it is not restated here.
- **Capture method: tools write the text to disk; nothing is hand-copied.** Each capture file carries frontmatter naming the original URL, the method, what was tried and what is missing. Where a tool could not give the full page, the capture says so (partial or failed) rather than being patched by hand.
- **Link-following stops at two hops.** The report's links were hop one; links found inside those captures were hop two (the F01 group). Links found only inside hop-two material were recorded, not fetched. They are listed in [SOURCES.md](SOURCES.md#found-but-not-captured-third-hop).
