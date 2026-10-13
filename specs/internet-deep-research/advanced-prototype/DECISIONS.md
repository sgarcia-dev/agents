---
created_at: 2026-09-30
updated_at: 2026-09-30
model: anthropic/claude-opus-5-5
doc_type: decisions
purpose: Choices for the internet deep research engine after reconciling five outside reports, a Hermes self-audit, and six verification runs on September 30, 2026. What is settled, what changed, how the reports' disagreements were resolved, what was rejected, and what the user still decides.
related:
  - path: ./spec.md
    why: The spec these decisions shape.
  - path: ./SOURCES.md
    why: Evidence behind each choice.
  - path: ./skill-proposal.md
    why: Skill packaging choices that are still open.
---

> Historical, 2026-10-01: This prototype is parked. It is not current policy or a build plan. Current web facts and decisions: [capabilities/web](../../../capabilities/web/README.md) and [web decisions](../../../capabilities/web/DECISIONS.md).

# Decisions

**September 30, 2026:** superseded by the simple
[web-search-advanced skill](../../../skills/web-search-advanced/SKILL.md).
Kept as prototype history. The choices below are not the current build plan.

"Settled" means the evidence points one way and the design now assumes it.
None of it is tested by our own runs yet. Any item can reopen when receipts
arrive.

## Settled

1. **One loop, fixed stages.** Brief, rounds of gather and gap check, write,
   check, receipt. Every system studied uses this skeleton (all reports).
2. **Code enforces limits; prompts only explain them.** A helper program
   counts searches, reads, rounds, and dollars and refuses past a cap. All
   five reports and the Hermes self-audit agree; Hermes shows the failure
   mode (its "20 searches" is a guideline nothing enforces). *Changed:*
   draft v0 left "instructions only or a script" open. Now: a script.
3. **Two hard limits: max searches and max extra cash.** Searches bound
   exploration; cash bounds retries, reasoning, and paid tools (ChatGPT cost
   report). Default cash cap $1. *Changed:* v0 had searches only, with an
   optional dollar cap defaulting to none.
4. **Max searches stays the main dial.** Other caps follow from the tier
   unless overridden. Rejected: breadth and depth knobs (the dzhng formula
   turns breadth 10, depth 4 into 510 searches) and a token budget as the
   main dial (hard to reason about, and you cannot meter tokens inside most
   harnesses; Claude report).
5. **Three model slots: cheap, smart, writer.** Query writing moved to
   cheap; the citation audit moved to smart. See
   [models-and-plans.md](./models-and-plans.md).
6. **The expensive model never sees raw pages.** The helper runs the
   search-and-read inner loop with the cheap model (`dr gather`) and hands
   back evidence records. This also cuts harness overhead, the biggest cost
   on pay-per-use APIs.
7. **Evidence records with exact quotes, checked by code.** Every note
   carries a quote and line numbers; the helper confirms the quote is on the
   saved page. Snippets are leads, never citable evidence. *Changed:* v0 let
   picks record "snippet facts" and made quotes optional.
8. **The writer cites evidence IDs; code renders citations.** `[[E12]]`
   markers, numbered by the helper. The model never writes a URL.
9. **Citation checking has four layers,** and the semantic one (does the
   quote support the sentence?) is a separate model call on the original
   page text. Hermes's own checker passes a false claim cited to a real
   source, which proves the mechanical layers are not enough.
10. **Stop rules:** any hard cap; the 80% exploration floor; two rounds in a
    row with no new supported requirement or resolved conflict; all critical
    requirements supported or openly unknown. "Supported" means one primary
    source or two independent sources that agree. *Changed:* v0 counted "new
    facts"; now progress means supported requirements, and copies count once.
11. **One loop by default; workers only for breadth questions at medium and
    above, with reserved shares of one budget.** LangChain's prompt says
    "Bias towards single agent"; Anthropic's multi-agent gain came at about
    15x chat tokens and was not cost-matched (verified).
12. **Default cheap slot is a pay-per-use API (DeepSeek V4.1 Flash), not
    OpenCode Go.** It costs about 8 cents per medium run, and Go's terms make
    heavy batch extraction a policy risk. *Changed:* v0 defaulted the cheap
    slot to OpenCode Go.
13. **Default profile is `subscriptions`:** cheap slot on a pay-per-use API;
    smart and writer are the harness's own model on a ChatGPT or Claude plan.
    That puts harness overhead on flat-fee usage.
14. **Config in one YAML file, no secrets.**
15. **Harness-agnostic through a shell helper, not MCP.** Every harness can
    run shell commands; MCP setup differs per harness.
16. **LDR is not a backend option for now.** No official native Mac app
    exists (only pip, Docker, and a web UI on port 5000; verified), and its
    default strategy is now `langgraph-agent`, which resets any iteration
    limit below 10 to 50 (verified). We found no per-run search cap of the
    kind this engine is built around (our reading, not a verified absence). It
    remains a reference and a possible quality baseline. *Changed:* v0 left
    this open.
17. **Reuse neighbor specs.** Provider setup and funding order live in
    [internet-deep-research](../spec.md); artifact rules
    in [research](../../research/spec.md); Hermes wiring in
    [hermes-internet-deep-research](../../hermes-internet-deep-research/spec.md).

## Where the reports disagreed, and what we chose

| Topic | Claude report | ChatGPT reports | Hermes | Chosen | Why |
|---|---|---|---|---|---|
| Tier sizes | tiny 3-5, large ~300, xl ~1,000 | tiny 3, large 150, xl 300 (cost report); tiny 4, small 20, large 80, huge 240 (internals report) | standard lane 20 searches, 25 reads | tiny 5, small 12, medium 50, large 200, xl 500 | Closest to the user's original ask; all are estimates |
| Reserve for finishing | stop under 15% left; forced answer at 85% | reserve about 20% | none enforced | explore until 80% | Jina's code uses 85%; both ChatGPT reports say 20% |
| Snippet facts | allowed (P3) | not evidence | "discovery leads, not evidence" | not evidence | Snippets cannot be quote-checked |
| Compression | rewrite notes into a digest | select IDs only | n/a | select IDs only | Rewriting lets conditions and URLs drift |
| Citations | carry from first note; `[n]` by the model | `[[E123]]` rendered by code | ledger IDs rendered by script | `[[E12]]` rendered by code | Model never touches URLs |
| Query writing | cheap | cheap | main model | cheap | Gap check already decides what to search |
| Citation audit | mid model | code plus cheap first pass | mechanical only | smart, cheap after testing | Needs judgment about scope and wording |
| Workers at large | 10-15 | 4 | runtime allows 10 | 2-4 | Bias to one loop; Claude's own advice caps at 5 |
| Rounds versus queue | FIFO gap queue | flat priority queue | model judgment | rounds cap kept; gap check picks the next items by priority | A rounds cap is easy to count; the priority order lives in the gap check |
| DeepSeek V4.1 Flash price | $0.15 / $0.60 | $0.0198 / $0.396 | n/a | both are real routes (DeepSeek direct vs OpenRouter main listing); estimates use $0.15 / $0.60 | Verified on vendor pages |
| OpenCode Go limits | $12 per 5 h, $30 per week, $60 per month | per-model allowance, 20% per 5 h, 50% per week | n/a | per model | Verified; Claude's numbers are one $60 model's limits |
| Jina effort budgets | 300K / 750K / 1.5M | 1M default | n/a | low 100K, medium 500K, high 1M (API default is medium); the `getResponse()` function itself defaults to 1M | Verified in `app.ts` and `agent.ts` |

## Rejected

- **Adopt an existing framework (LangChain, GPT Researcher, LDR) as the
  engine.** Ties the design to one codebase and its model support.
  LangChain's open_deep_research was archived on August 21, 2026 (verified).
  Their prompts and settings are still borrowed.
- **Token budget as the main dial** (Jina). Kept as a reported number.
- **Multi-agent by default.** See settled item 11.
- **Minimum tool-call rules** ("Execute a MINIMUM of five distinct tool
  calls", in Anthropic's cookbook worker prompt, which also says "under 5"
  for simple tasks; both verified). They force waste on simple questions.
- **Recursive breadth and depth trees.** Work is hard to predict and does not
  go to the most important gap.
- **A separate "simulated expert interview" stage (STORM) for every run.**
  Too much overhead for narrow questions. Its idea (plan from several
  perspectives) can live in the brief prompt later.

## Decided by the user (September 30, 2026)

1. **Keep the original engine name** (now Internet Deep Research Advanced Prototype).
2. **Save Claude Code usage: delegate the build.** The user's weekly Claude
   limits are low. The first runtime is **OpenCode**: GPT 6.1 Sol main agent
   (ChatGPT login), cheap subagents on Go models (DeepSeek V4.1 Flash or Muse
   Spark 1.3), and Codex CLI as the search engine. The helper is built by a
   Codex CLI session (GPT 6.1 Sol, low effort) that Claude Code drives.
   Hermes is not driven from here; if used, it gets a handoff file and the
   user runs it.
3. **Go models may do the cheap work, through OpenCode itself** (subagents
   or `opencode run`), which is normal OpenCode client traffic. The helper
   must not call Go's API directly. This replaces settled item 12's default
   for the OpenCode runtime; the pay-per-use API stays the default elsewhere.
4. **Defaults split by purpose.** A quick web search defaults to tiny. Deep
   research defaults to small; medium only when asked; large and xl rarely.
5. **Native search first.** The driver's own search (Codex or Claude) and
   SearXNG come first. Parallel, Firecrawl, and Exa join only when the user
   asks for them or for "deep research" with scraping. The engine must run
   end to end on Codex search alone or Claude search alone.

6. **Two skills.** `web-search` is quick lookups: native search only, about
   5 searches, paid tools only when named (applied to the skill on September
   30). The deep engine is a separate **prototype helper skill**
   (chosen over `research-web` to avoid confusion with other tools' "deep
   research" modes). It runs **only when the user explicitly asks** for it.
7. **Build phase 1 of the helper now,** delegated to Codex (GPT 6.1 Sol,
   low). Blocked on September 30: Claude Code's auto mode refused to launch
   the Codex build session; the user can run the command from the handoff
   file or allow it.

## Earlier open items (answered above or folded in)

1. **Spec and skill names.** Spec renamed to the original engine name
   (user's suggestion). Skill working name was the prototype helper skill. Alternative for
   the spec: `web-research-engine`, which avoids near-collision with
   `internet-deep-research`.
2. **First harness to build for.** Recommendation: Claude Code for building
   and testing the helper (native subagents; the `--disallowedTools` flag for
   strict mode is already used by the web-search skill),
   then Codex for everyday runs on the ChatGPT plan. Hermes and OpenCode
   after, one per session.
3. **May the cheap slot use OpenCode Go?** Recommendation: no for batch
   extraction; yes for Go models as the smart slot when OpenCode is the
   harness.
4. **Default tier.** Recommendation: small, with the key-research rule
   (about 15 searches, 20 to 30 reads) for questions you mark important.
5. **Default cash cap.** Recommendation: $1 per run; raise per run.
6. **Where the helper lives.** Recommendation: the former helper skill's scripts folder
   until it grows past a few hundred lines.
