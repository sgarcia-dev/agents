---
created_at: 2026-09-30
updated_at: 2026-09-30
model: anthropic/claude-opus-5-5
doc_type: proposal
purpose: How a skill should package the engine, how it relates to the existing research and web-search skills, the build order with acceptance tests, and what stays out. Proposal only; the user asked not to create the skill yet.
related:
  - path: ./spec.md
    why: The engine the skill would run.
  - path: ./ARCHITECTURE.md
    why: The helper and run folder the skill calls.
  - path: ./stage-prompts.md
    why: The prompts the skill would ship.
  - path: ../../../skills/web-search/SKILL.md
    why: Tool choice for single lookups; the engine's provider list follows it.
  - path: ../../../skills/research/SKILL.md
    why: General read-only investigation skill; shares the artifact contract.
  - path: ../../../skills/research-deep/SKILL.md
    why: Multi-round investigation skill; could call this engine for its web parts.
---

> Historical, 2026-10-01: This prototype is parked. It is not current policy or a build plan. Current web facts and decisions: [capabilities/web](../../../capabilities/web/README.md) and [web decisions](../../../capabilities/web/DECISIONS.md).

# Skill proposal

**September 30, 2026:** superseded by the simple
[web-search-advanced skill](../../../skills/web-search-advanced/SKILL.md).
Kept as prototype history. The proposal below is not the current skill design.

**Status: proposal. No skill has been created.** The user asked to hold off
and review this first.

## The short version

One **prototype helper skill**, that runs a sized web research
run from any harness:

```text
/prototype-helper medium "How do open deep research systems cap cost?"
/prototype-helper small "..." searches=20 reads=25 usd=2 profile=best
```

It is thin. The skill's `SKILL.md` tells the agent the order of stages and
when to call the helper. The helper (`dr`) does all counting, fetching,
storing, and citation rendering. The prompts live next to it as files.

## Why this name (decided September 30, 2026)

- The original helper skill name read as "the bigger web-search", the same way
  `research-deep` is the bigger `research` in this workspace.
- It avoids the phrase "deep research", which most tools already use for
  their own mode (Claude Code's `/deep-research`, ChatGPT and Gemini deep
  research), so nobody confuses the two.
- `web-search` stays the quick-lookup skill: native search only, tiny budget.

## Explicit invocation only

This skill can spend real money and plan usage, so **it never runs unless
the user asks for it by name.** No agent, skill, or workflow may start it on
its own, and `web-search` must never escalate into it silently; it may only
suggest it. Each harness adapter must enforce this where it can (in Claude
Code, `disable-model-invocation: true` in the skill's frontmatter), and the
`SKILL.md` says it in its first line.

## How it fits with existing skills

| Skill | Job | Relation to the prototype helper skill |
|---|---|---|
| `web-search` | Quick lookups: native search only, about 5 searches, paid tools only when named | Suggests the prototype helper skill when a question needs more; never starts it |
| `research` | Broad read-only investigation of anything (code, memory, web), with one artifact | May call the prototype helper skill for a web-heavy question. Unchanged |
| `research-deep` | Multi-round investigation with root review between rounds | Same; a round can be one prototype helper run. Unchanged |
| `task-codex`, `task-opencode`, `task-claude` | Hand a task to another harness's CLI | The engine does not need them; each harness runs the engine itself |

The prototype helper skill writes its run as a normal research bundle under
`artifacts/investigations/`, following the
[artifact rules](../../research/spec.md): `RESEARCH.md` as the entry, the run
folder beside it.

## What the agent does, step by step

What `SKILL.md` would say, in order:

1. **Preflight.** Check the helper exists, load the config, pick the tier and
   profile. Refuse a "subscriptions" run if `ANTHROPIC_API_KEY` is set. In
   strict mode, confirm the harness's own web tools are off for this run.
2. **Cost preview.** Print the caps, the profile, and the estimated extra
   cash and plan usage from [budget-tiers.md](./budget-tiers.md). Ask before
   starting only if the tier is large or xl, or the estimate is above
   `max_usd`. Otherwise start.
3. **Brief** (stage 1). Ask the user at most one question, only if the
   answer changes the plan.
4. **Rounds.** For each open sub-question, call `dr gather`. After each
   round, run the gap check (stage 5) on `dr status`. Continue, finish, or
   finish in limited mode.
5. **Workers** (stage 6), only for BREADTH questions at medium and above.
   Each worker gets a reserved budget and writes to the same run folder.
6. **Write** (stages 7 and 8). The writer uses `[[E12]]` markers.
7. **Check.** `dr render` and `dr check` (mechanical), then the audit (stage
   9), then one repair pass (stage 10), then `dr check` again.
8. **Deliver.** `dr receipt`, write `RESEARCH.md`, give the user the path and
   the three-line answer, and follow the workspace's commit rules for
   artifacts.

## What ships in the skill folder

```text
skills/<former-prototype-helper>/
  SKILL.md            the steps above, under about 150 lines
  prompts/            stage 0-10 prompts from stage-prompts.md, one file each
  scripts/dr          the helper (Python, standard library plus one HTTP client)
  config.example.yaml copy of engine.example.yaml
```

The spec folder stays the owner of design truth; the skill folder holds the
runnable copy. Harness wiring (slash command, allowed tools, strict-mode
flags) goes through `sync-tool-adapter`, one harness per session, per the
Single-Tool Boundary.

## Build order, with tests that prove each step

| Phase | Build | Done when |
|---|---|---|
| 1 | `dr init`, `dr search`, `dr read` (fetch and snapshot only), ledger, receipt | A tiny run refuses search number 6 and read number 7, and the receipt counts match the query and source logs exactly |
| 2 | Cheap-model extraction in `dr read`, quote check, evidence file | A planted fake quote is rejected; a real quote passes; a blocked page returns "unusable", not notes |
| 3 | `dr gather`, coverage file, gap check prompt, no-gain counter | A small run on a known question stops by itself with "finish" or "finish_limited" and a correct coverage file |
| 4 | Writer, `dr render`, `dr check` | An unknown `[[E99]]` fails the check; the source list is built only from stored URLs |
| 5 | Audit and repair | Hermes's "moon is made of cheese" test: a false sentence cited to a real source is caught as unsupported (Hermes's own `verify` passes it) |
| 6 | Money cap and profiles | A run with `max_usd: 0.05` stops before the next paid call; a subscriptions run refuses with `ANTHROPIC_API_KEY` set |
| 7 | Workers with reservations | Two parallel workers never exceed the shared cap, tested with a cap smaller than their combined asks |
| 8 | One harness adapter | The first harness runs tiny, small, and medium on three known questions with receipts saved |

Then the quality check: 10 to 20 of the user's real questions, graded
without knowing the tier, on factual accuracy, citation accuracy,
completeness, source quality, and tool efficiency (Anthropic's rubric,
verified; they started with "about 20 queries").

## What stays out of the skill

- No model names in prompts. Models live in the config by slot.
- No provider keys. Keys stay in each provider's existing setup.
- No automatic paid spillover from a subscription.
- No recursive workers, and no hand-off to another harness's CLI from inside
  a run.
- No "verified" label on a report unless the audit covered its claims; the
  receipt says how many were checked.

## Update after the user's answers (September 30, 2026)

- **Two skills, one contract.** `web-search` stays the quick-lookup skill,
  capped at tiny and native-only by default; the prototype helper skill is deep research
  (small default). Both read tiers and provider order from this spec. This
  changes `web-search`'s current default (native plus Parallel); not applied
  until the user says yes.
- **Codex as a search engine.** The helper's first search provider is
  `codex exec --search`, so the engine runs end to end on the ChatGPT plan's
  search alone. Paid providers are opt-in.
- **First runtime: OpenCode.** GPT 6.1 Sol main agent through OpenCode's
  ChatGPT login; DeepSeek V4.1 Flash or Muse Spark 1.3 Go subagents for
  gather and read; Codex for search. Built by a Codex session (GPT 6.1 Sol,
  low) driven from Claude Code, to save Claude usage.

## Open choices for the user (original list)

These also appear in [DECISIONS.md](./DECISIONS.md):

1. The prototype helper skill's original name.
2. The first harness to build for.
3. Whether the cheap slot may use OpenCode Go despite its batch-use terms.
4. Where the helper's code lives: inside the skill folder (proposed), or its
   own small repository if it grows past a few hundred lines.
