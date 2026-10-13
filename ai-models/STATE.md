---
doc_type: state
updated_at: 2026-10-13
status: active
scope: ai-models
related:
  - path: ~/agents/ai-models/README.md
    why: Human and agent entrypoint.
  - path: ~/agents/ai-models/collection/README.md
    why: Fast path for adding models and maintaining sources.
  - path: ~/agents/ai-models/collection/benchmark-backlog.md
    why: Benchmark questions retained for future work.
---

# Current state

**Local task benchmark, 12 October:** Document-tailoring pilot (report private, not published) complete: eight parallel runs; 0–100 category scores, reference costs, timings and sensitivity analysis. Same-family judge and one sample per role/configuration limit conclusions. Claude replay packets were executed in the 13 October comparison below. The owner now intends Sol medium/high by role importance, with an orchestrator supervising production. Mixed-effort production has not been benchmarked; global delegation defaults unchanged.

**Local task benchmark, 13 October:** Claude comparison (report private, not published) added Opus 5.5 medium/high and Sonnet 5.5 high with a second blind judge. Sol high still best; Claude drafts lost on one inherited statistic; Opus high was worse and costlier than Opus medium; Sonnet high is the best-value Claude setup. Delegation defaults unchanged.

## What is complete

- This folder is the source of truth. Promotion was explicitly approved by the
  owner; no dependency on Downloads remains in the working scripts.
- Twenty-five selected configurations. Original ten: medium/low for Sol 6.1,
  Opus 5.5, Sonnet 5.5; medium/low/high/xhigh for Luna 6 (default medium, no
  fallback). Added September 30 from saved data, no new API calls: GPT-6 Sol
  low/medium; GPT-5.6 Luna high/xhigh (separate from GPT-6.1 Sol and GPT-6 Luna);
  the OpenCode Go set at their defaults: MiMo V2.6 Flash (no levels), DeepSeek
  V4.1 Flash (max), GLM 5.3 Flash (max), Qwen 3.8 Flash as `qwen3-8-flash-next`,
  Muse Spark 1.3 (xhigh); plus GLM 5.3, Qwen 3.8 Max, MiMo V2.6 Pro, Kimi K3
  (max) as single default entries. No-effort and max-effort models are now allowed.
- Benchmarks added: AA-LCR pass-rate and AA-Briefcase Elo (Sonnet low has no
  Briefcase score). IFBench and APEX-Agents skipped: no values for target models.
- October 1: added GPT-6.1 Sol high (26 configurations; default stays medium)
  from saved data, and input/output/cache-hit price columns to `SCORES.md`.
- `README.md` now lists where each model comes from and its best harness. `SELECTION.md`
  holds value (from `scripts/value_ratings.py` and `VALUE.md`, our own division of
  index score by index cost, since Artificial Analysis publishes only the charts),
  reliability groups and the sensitive-work rule for Muse Spark (assumed contributor model).
- Muse Spark 1.3 has a cheap Contributor price (data used for training) that the
  owner uses; the AA price is the default version. `opencode-go-limits.md` holds
  the Go $10 limits for tracked models. Sonnet low cost is a labeled estimate in
  `SELECTION.md` only, not in the data.
- October 1: `delegation-defaults.md` became `delegation-briefing.md`, the only
  place that chooses models for native workers (all tiers), orchestrators, CLI
  bridges and web search, per harness. Each model has a card (strengths, failures,
  alternatives) and four labels (cost, skill, guessing, speed) that set worker
  counts and deadlines; `roles/task-worker-tiers.md` no longer has fixed counts.
  Skills and adapters point there instead of naming models. Decisions that day:
  Sonnet stays medium; Codex execute moves to Sol 6.1 low, Codex high workers to
  Sol 6.1 medium, Codex orchestrator to Sol 6.1 high; OpenCode workers move to Go
  models (GLM 5.3 Flash, MiMo V2.6 Pro, GLM 5.3); Claude orchestrator to Opus
  medium (applied). Codex, OpenCode and Hermes were synced the same day in their own CLI
  sessions; every changed role passed a one-line live smoke. The rules live in
  `specs/model-delegation/spec.md`. A four-worker audit then removed leftover
  model picks from capability docs, adapters and the adapter contract. Still
  open: 14 Hermes-local skills hold old delegation and model advice; Hermes will
  clean them in its own session (handoff in a private folder, not published).
- Gemini 3.8 Flash medium and high added (25 configurations, 477 checks). `SELECTION.md`
  has a best-for-delicate-work ranking and the Gemini rows. Gemini operates through
  the owner's Google AI subscription via Antigravity CLI (`agy`). Gemini 3.8 Flash is
  established as the only usable Gemini model. All other accessible models (Pro defaults
  to 3.1, ancient; older Flash versions like 3.7) are rejected as abysmally bad. Gemini 4
  will require fresh tests and indexing upon release.
- `data/2026-09-30/SCORES.md` (from `scripts/cheat_scores.py`, run after the build) is a
  compact score table with metric glossary. The delegation briefing reads it alongside.
- `subscription-speed.md` records a received chart: Codex subscription Sol speed is about
  a third of API speed, Claude Code is near API speed. Artificial Analysis speeds are API
  speeds. The cheat sheet carries a warning and revised fast picks. Owner rule: no Fast tier
  (about double cost) except for Luna. Chart source unverified.
- Rebuild passes 439 checks and 16 tests, 23 models, zero network calls. One
  check was a half-cent tie (MiMo V2.6 Pro input $0.435 on the site, $0.43 in
  the API); the matcher now accepts either direction on an exact tie only.
- Complete Free API snapshot: 686 rows, fetched September 30 at
  `2026-09-30T16:45:49.835224+00:00`, version 4.3, four page requests. The successful
  key was not retained. Last captured remaining quota 96 is not a live reading.
- Saved public website Flight payload includes detailed configuration rows,
  per-evaluation scores/cost/tokens and most decode-time estimates. Website
  methodology label v4.3.2 is retained separately from API version precision.
- Deterministic extraction, compact snapshot, generated master table, local
  querying, original API client/tests and full archived experiment evidence
  are all here. No new remote collection was needed for promotion.
- Promotion passed 182 extraction checks, 14 API-client tests, exact metric/hash
  preservation and a relocated-folder test. Registry-only addition of another
  reasoning level was tested offline in a temporary copy; published selection is
  still ten rows. Local extract+build took about 0.11 seconds, querying about
  0.03 seconds. See `data/2026-09-30/promotion-verification.json`.

## 2026-10-07 (round 5): the briefing is each tool's worker scorecard

- `roles/task-worker-tiers.md` no longer says how capable a tier is; the names
  only hint. It sends every root to its tool's part of briefing section 3.
- Each tool's part of section 3 now has the same six lines: against your root,
  regular takes, never give regular, move up to high when, give back to the
  root when, how many at once. Worker model cards end with a "Tell the worker"
  line the root copies into packets. A reading guide at the top says which
  sections each reader needs.
- Kept as one file on purpose (about 560 lines). Revisit if it passes about
  1,000 lines or one tool's part passes about 100.
- Later the same day: the block's first line became "How the tiers compare"
  and its last "How much to delegate". `sync-tool-adapter` and briefing
  section 8 now require the block in the same run as any worker or
  orchestrator model change. Claude Code, Codex, OpenCode and Gemini each
  synced their own worker descriptions to point at their block (Codex,
  OpenCode and Gemini in their own CLI sessions). Their corrections were
  applied: Codex root is GPT-6.1 Sol medium and Codex caps four active agents;
  OpenCode pins no root model (usually Sol low). Hermes was not synced.
- October 8 checks: all four Claude Code workers reported their new models
  (Haiku 5.5, Sonnet 5.5) and both execute workers wrote a test file. Gemini's
  move of its worker files to `~/.gemini/config/agents/` fixed the October 5
  launch failure: a fresh session launched `task-explore`. Not yet shown:
  whether Gemini workers use their own model pin or the parent's. Headless
  `claude -p --agent task-explore` passed once given the saved token (Claude
  Code's shell does not pass it through; see `capabilities/claude-cli.md`).

## 2026-10-07 (round 4): Claude Code workers moved to Haiku and Sonnet

- Owner decision: `task-explore` and `task-execute` on Haiku 5.5 high;
  `task-explore-high` and `task-execute-high` on Sonnet 5.5 high;
  `task-orchestrator` stays Opus 5.5 medium. Applied by `sync-tool-adapter` in
  Claude Code. Static change: the session that made it still ran the old agent
  files, and the headless CLI login had expired, so the live check waits for a
  fresh session.
- Briefing: Claude Code rows, dispatch guidance, `task-claude` default (Sonnet
  high through `--agent task-explore-high` or `task-execute-high`, Haiku high
  for short checkable jobs, Opus medium for hard ones) and a "Claude for web
  search" table (small searches Haiku high, medium searches Sonnet high).
- Open: the saved root default is Opus at high effort, the briefing says low.
  Left for the owner.

## 2026-10-07 (round 3): cheap tier audit, Haiku 5.5 vs GPT-6 Luna vs GPT-5.6 Luna

- AA website capture extended with the GPT-5.6 Luna page, which still carries
  the old 696-model list. Both Luna families now have every effort including
  max; GPT-6 Luna was re-scored up 0.4 to 0.8 points, so all Luna rows come
  from October 7. 43 configurations, 671 checks, 16 tests pass.
- Three Codex workers (GPT-6.1 Sol medium) and one Gemini run from the root
  tested the owner's three Luna claims. Results in `SELECTION.md` (cheap tier
  audit) and `EFFORTS.md` (Luna section). Short form: Luna 6 max is cheap but
  no more reliable than xhigh on long runs; Luna 5.6 finishes more coding tasks
  at 2 to 4.6 times the cost; Luna recall holds to 128K at high effort and
  falls after. Haiku beats Luna on terminal, coding and computer use and
  guesses far less; Luna knows more and handles tool workflows better.
- Briefing: Luna, Luna max, Luna 5.6 and Haiku cards, Codex notes, two job rows
  and a field note updated. No role changed: Codex `task-explore` stays Luna
  xhigh; the audit supports that.

## 2026-10-07 (round 2): effort sweet spots for Haiku, Sonnet, Opus, Sol

- AA website capture extended: every Sonnet 5.5 effort refreshed (low now has
  an index, costs at the new $0.10 cache price), Opus 5.5 high/xhigh/max and
  GPT-6.1 Sol xhigh/max added. 39 configurations, 656 checks, 16 tests pass.
  Extractor now takes several payloads per date and per-configuration
  `website_source`. New generated `data/2026-09-30/EFFORTS.md`
  (`scripts/effort_curves.py`) and written guide `EFFORTS.md`.
- Five Codex workers (GPT-6.1 Sol medium, one topic each) gathered non-AA
  evidence: CursorBench, Cognition FrontierCode, VulcanBench, Haiku and Sonnet
  system cards, Claude Code docs. Reports in `evidence/2026-10-07/codex-*.md`.
- Sweet spots: Haiku high (revised from xhigh), Sonnet high, Opus medium,
  Sol medium. Briefing section 6 is now a job to model-and-effort table.
- (Applied in round 4, with `task-execute` on Haiku too by the owner's call.)
  Proposal was: `task-explore` to Haiku 5.5 high, both high workers to Sonnet
  5.5 high, orchestrator stays Opus medium.

## 2026-10-07: Claude Haiku 5.5 added

- Five configurations (low, medium, high, xhigh, max) from one public model page
  payload, website-only, no API key. 31 configurations, 561 extraction checks,
  16 tests pass. Existing rows unchanged. `offline_extract.py` now accepts
  `"website_source": "<date>"` models; tables mark them `*`.
- (Superseded by round 2: default is now high.) Decision: registry default **xhigh**.
  It is the last step before cost per point triples and the only level that
  matches Sonnet 5.5 medium. high when speed matters, medium for bulk lookups,
  never max. Codex research (Anthropic guidance, CursorBench) leaned medium or
  high, so confidence is moderate. Full table and gotchas in `SELECTION.md`.
- Biggest gotcha: Haiku costs 5 times more above 100K-token prompts, and AA
  priced it at the short rate. Its value holds only for short-context work.
- Sonnet 5.5 cache reads fell to $0.10 on October 7. The September 30 Sonnet
  rows predate this; they were not changed.
- The delegation briefing has a Haiku card but **no role uses it**. Mapping it
  to Claude Code `task-explore` or `task-execute` is the owner's call.
- Evidence: `evidence/2026-10-07/` (two Codex reports, one Gemini note with the
  root's verdict, prompts and run telemetry). The in-Codex Gemini child failed
  silently; Gemini was rerun from the root.

## Constraints and gaps

- Sonnet low aggregate Intelligence Index/cost/tokens/time unavailable; individual
  benchmark scores exist. Luna medium headline speed/index time unavailable;
  hundredK-prompt performance is separate and must not replace it.
- AA time/task is weighted decode estimate excluding TTFT/overhead. Actual
  elapsed agent-task completion remains unknown for all models.
- Claude measurements use adaptive reasoning and default fallback.
- No scheduled job or general live website collector exists. The offline replay
  parser is tested on the saved payload, not certified against future site changes.

## Exact next action after compaction

Ask the owner
whether the root default should be Opus low (briefing) or high (saved
setting). Otherwise wait for the owner's next model request; change the
briefing first (its section 8). Not yet tested: nested orchestration in Codex and OpenCode, Claude
Code's orchestrator at its new medium effort. First use
`scripts/list_configurations.py --search <name>` against the retained catalogue.
If the exact records exist, add confirmed UUID/slug/effort entries to
`favorites.json` and rebuild offline. Do not repeat the web investigation.

AA-LCR is done. For further benchmark expansion, check IFBench's instruction-following relevance and context lengths. Very
long-context instruction following/generation and true long-horizon wall-clock
performance remain open questions in `collection/benchmark-backlog.md`.

## 2026-10-01 web consolidation

Delegation briefing section 4 retains web helper model and effort choices and points tool facts to ~/agents/capabilities/web/README.md. Section 9 records the GLM 5.3 allowance lesson: default to GLM 5.3 Flash, include a fallback model, and save raw output with scripts. No model data or native configuration changed.
