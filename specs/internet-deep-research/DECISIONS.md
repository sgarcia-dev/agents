---
created_at: 2026-09-30
updated_at: 2026-09-30
model: openai/gpt-6.1-sol
doc_type: decisions
purpose: User decisions that simplify advanced web searching while retaining the larger design as reference.
related:
  - path: ./spec.md
    why: Owning spec and navigation.
  - path: ./web-search-advanced.md
    why: Simple skill design.
  - path: ./advanced-prototype/spec.md
    why: Parked prototype and retained research.
---

> Historical decisions and evidence. For current generic web facts, use ~/agents/capabilities/web/README.md.

# Decisions

## September 30, 2026: keep it simple

1. **Instructions, not a program.** Use `web-search-advanced` for bounded
   web research. The eight-phase helper plan was too complex to maintain.
   Reject the helper and config file for the current skill. Visible counts
   are useful, but are not mechanically enforced hard caps.
2. **Explicit invocation only.** The user must name the skill. Quick
   `web-search` may suggest it but never start it. Avoid the phrase deep
   research in the skill name to prevent confusion with vendor modes.
3. **Native tools by default.** The current agent searches and reads pages.
   Named providers and helpers are opt-in experiments. Each named provider
   gets the full limit, not a shared fraction. This makes comparisons useful.
4. **Small default, medium only when asked.** Use 12 searches, 15 reads,
   two rounds; medium uses 50 searches, 60 reads, three rounds. User numbers
   override presets. Stop early when answered or no new evidence appears.
5. **One spec, with a nested prototype.** Keep tool and provider reference
   together with the simple skill design. Keep the larger design under
   `advanced-prototype/`. Hermes stays separate. Do not discard its research
   or treat the prototype as the current plan. The user decides when to
   rebuild, and any rebuild must be much simpler to maintain.
6. **Delete phase 1 code, retain history.** Commit `93258d64` keeps the
   helper implementation. Do not carry runnable code for a parked design.
7. **One report and receipt.** Add `artifacts/web-searches/` for these
   reports, so counts, evidence, conflicts, and gaps are easy to find.

## 2026-10-01: Web reference moved

Generic search and fetch facts, tool quality, ladders and current routing decisions now live in [capabilities/web](../../capabilities/web/README.md) and [its decisions](../../capabilities/web/DECISIONS.md). This file retains dated history. Earlier provider defaults and budgets are not current policy. Hermes setup and research workflow retain their own spec.
