---
doc_type: state
created_at: 2026-10-09
updated_at: 2026-10-09
status: active
scope: hosted research prompts, mode choice and benchmarks
related:
  - path: ./spec.md
    why: Rules and verdicts.
  - path: ./BENCHMARKS.md
    why: Run log.
---

# Browser Deep Research State

## Now (9 October 2026, about 19:00)

- Three benchmarks done. B3 (four task types, ChatGPT and Claude) settled
  the verdict: Chat 6 Pro default, Extra High close second, Deep research
  do not use, Claude Research as a cross-check. A deep re-grade the
  same evening added prompt rules 10 to 17 and the pairing findings. See `BENCHMARKS.md`.
- Skills updated: browser-deep-research-prompts (mode table, Claude
  effort), chatgpt-browser export reference (three new export pitfalls).

## Next actions, in order

1. Resume pending private research packs with the skill's new flow: size
   question, mode-fit report, user approval, then run.
2. Not scheduled (user decision, 9 October 2026, to save Claude usage):
   re-score B3's existing reports with the finer measures; Claude Opus at
   High on a rules question and a list; a repeat 6 Pro and Extra High run
   to measure noise; a "run both and merge" test.
3. After any future run: update `BENCHMARKS.md`, the fit guide, the skill,
   then commit and push.

## Open questions

- 6 Pro weekly cap: still no official number (OpenAI help, checked
  9 October 2026). Press: 100 a week on new Pro $200 plans; a blog says 50
  on Pro $100 (unverified). Check in the account before big batches.
- `deep-research-mini` is what every Deep research run here reported, at
  any effort. OpenAI says only "latest model by default" (legacy models
  selectable); its Enterprise rate card lists `o4-mini-deep-research`.
  Whether a full model can be chosen is still unknown.
- Verified mode facts (models, search, caps, timing) are condensed in the
  mode report (private, not published).
- Extra High placeholder links (B2) did not recur in B3: likely a one-off.

## How runs were done (for resuming)

- Runner: a Sonnet sub-agent (`task-execute-high`) with Claude in Chrome,
  given exact mechanics from the chatgpt-browser references. Exports: same,
  via the signed-in API and the clipboard route. Root keeps scoring.
- B3 used Opus 5.5 medium scorers (one per question) for judgment and
  Sonnet runners for browser work.
