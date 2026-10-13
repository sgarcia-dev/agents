---
doc_type: guide
updated_at: 2026-10-13
purpose: The one place that says which model each worker, orchestrator and CLI bridge uses, and what that model is good and bad at. Read before any delegation.
related:
  - path: ~/agents/specs/model-delegation/spec.md
    why: The rules this file serves (ownership, no copies, change path). (private, not published)
  - path: ~/agents/ai-models/data/2026-09-30/SCORES.md
    why: The numbers behind every claim here, including token prices. (raw data not published)
  - path: ~/agents/ai-models/SELECTION.md
    why: Longer notes on value and reliability.
  - path: ~/agents/ai-models/subscription-speed.md
    why: Why Sol is slow on the Codex subscription.
  - path: ~/agents/ai-models/opencode-go-limits.md
    why: Request limits that cap how many Go workers can run.
  - path: ~/agents/roles/task-worker-tiers.md
    why: Worker roles, packet rules and the worker-count rules that use the labels here.
---

# Delegation briefing

Read this before you hand work to anyone else: a native worker (`task-explore`,
`task-execute` and their high versions), a `task-orchestrator`, a CLI bridge
(`task-codex`, `task-claude`, `task-opencode`, `task-gemini`, `task-hermes`), a
Hermes `delegate_task` subagent, or a web-search helper.

**Do not just read the model name and launch.** The model decides how small the
packet must be, how many workers you can afford, how much you can trust the
result, and whether you should tell the user a different route would work
better. Read your harness's row and that model's card.

**Read only what you need.** Sections 1 and 2, your own tool's part of section
3, and the cards in section 5 for the models that part names. Section 4 only
when handing work to another tool or doing web search. Sections 6 to 9 only
when picking or changing a model. Each tool's part starts with its own heading
(`### Claude Code`, `### Codex` and so on), so jump straight to it.

**This file is the only place that chooses models.** Skills and adapters may
show flag syntax and record whether a mapping was live-checked, but they must not
pick or repeat a model choice. If your native agent file disagrees with this
file, tell the user. Do not quietly pick one.

Numbers come from the September 30, 2026 snapshot. Dollars per task are the
Artificial Analysis benchmark average on API prices, a way to compare models, not
your real bill. On subscriptions the real limit is quota.

## 1. Before every dispatch, answer five questions

1. **Which model will actually run?** Look up your harness in section 3.
2. **How much can I trust it?** Check its guessing label. High guessing means you
   re-check every claim against the source yourself.
3. **How small must the packet be?** A weak model gets one exact question or one
   mechanical edit. A strong one can take a bounded sequence of steps.
4. **How many at once?** Use section 2. Cost sets the count; a quota limit can
   lower it.
5. **Should I tell the user?** If the best model for this job lives in another
   harness, or the only model you have is a poor fit, say so before launching.
   Cross-harness bridges still need the user's go-ahead.

## 2. Labels and what they mean for dispatch

Each model card in section 5 carries four labels.

| Label | Values | What it decides |
|---|---|---|
| Cost | cheap, mid, premium | How many run at once |
| Skill | weak, solid, strong | How big and how coupled the packet can be |
| Guessing | low, medium, high | What jobs it may get and how hard you check |
| Speed | fast, normal, slow (on the route you use) | Deadlines |

**Cost.** Cheap: about $0.15 per task or less, or a Go model with thousands of
requests per 5 hours. Mid: up to about $0.60 on a non-Claude plan. Premium: any
Claude model (the Claude Max weekly limit is the scarcest budget the owner has)
or over $1 per task.

**Skill.** From the Intelligence Index and Terminal-Bench. Weak: under 36 or
under 15% Terminal-Bench. Strong: 47 or more. Solid: in between.

**Guessing.** From the hallucination rate (how often a wrong answer was a guess
instead of "I don't know"). Low: under 35%. Medium: 35% to 60%. High: over 60%.
Opus is high here even though it is strong: it knows a lot, but when it is wrong
it rarely admits it.

### How many workers at once

These replace the fixed counts. Default and high workers are still separate
pools (see `roles/task-worker-tiers.md`), and a user's explicit count still wins.

| Worker cost | Usual count | Ceiling (very hard task or user asks for max) |
|---|---|---|
| cheap | 3 to 8 | 10 |
| mid | 2 to 4 | 5 |
| premium | 1 to 3, start at 2 | 4, only when the user asks |

Then adjust:

- **High guessing:** you may still run many, but only give packets you can check
  quickly (quote this line, does this file contain X, run this command). Never
  give it judgment calls, edits that need reasoning, or durable memory.
- **Quota cap:** a model with few requests per 5 hours caps the count no matter
  its cost (GLM 5.3: at most 2; Kimi K3 and Qwen 3.8 Max: 1).
- **Slow:** double the deadlines in `roles/task-worker-tiers.md` (a regular run
  is checked at 6 minutes, cancelled at 8). Slow is not failure; silence past the
  doubled deadline is.
- **Blocking step:** when one step must finish before the next phase can start (a synthesis doc, spec files, a final review), speed matters more than price. Use the fast, solid tier for your harness (in Claude Code: Sonnet 5.5 high; Opus 5.5 medium when the step needs real judgment) and keep slow cheap models for wide parallel fan-outs. Owner decision 2026-10-13.
- **Never fill a pool to hit a number.** The count is a ceiling for the
  independent packets you actually have.

### Orchestrator rule

A `task-orchestrator` runs one step above that harness's high workers, but never
on the most expensive setting. It needs better judgment than its workers, not
the priciest model.

## 3. What runs where

Each tool below has the same six-line block, so a root can read only its own
section. `roles/task-worker-tiers.md` sends every root here for how capable each
tier really is; the tier names alone do not say. Every tool with workers must
have all six lines, and a worker or orchestrator model change is not done until
its block matches (section 8).

- **How the tiers compare:** each tier's model and score side by side (regular,
  high, orchestrator, root), and how far below the root each worker sits.
- **Regular takes** and **Never give regular:** the line between the tiers.
- **Move up to high when** and **Give back to the root when:** the two step-ups.
- **How much to delegate:** a lot or a little, why (cost, quota, speed), and
  the count per pool from section 2.

**Status** says whether the tool's native files match this table. "Pending sync"
means the decision is made but that tool's own `sync-tool-adapter` session has
not applied it yet; until then the old mapping (shown) is what actually runs.

### Claude Code (Claude Max subscription)

| Role | Model and effort | Labels | Status |
|---|---|---|---|
| Root default | Opus 5.5 low | premium, solid, high guessing, fast | live |
| `task-explore`, `task-execute` | Haiku 5.5 high | premium (lightest Claude), solid, medium guessing, fast | applied 2026-10-07 (was Sonnet 5.5 medium); live-checked 2026-10-08 (each worker reported its model; both execute workers wrote a test file) |
| `task-explore-high`, `task-execute-high` | Sonnet 5.5 high | premium, solid, high guessing, fast | applied 2026-10-07 (was Opus 5.5 low); live-checked 2026-10-08 (each worker reported its model; both execute workers wrote a test file) |
| `task-orchestrator` | Opus 5.5 medium | premium, strong, high guessing, fast | live: applied 2026-10-01 (was Opus low), not yet run-tested |

Owner decision, October 7: Haiku for the regular workers, Sonnet for the high
ones, Opus stays on the orchestrator. Each runs at its effort sweet spot
(`EFFORTS.md`):

- **Haiku high** is the lowest Haiku effort that does not skip checks or claim
  untested work is done, and where broad search stops collapsing (WANDR 13% at
  medium, 37% at high). It beats Sonnet medium on CursorBench (42.3% vs 39.2%)
  at under half the cost. xhigh adds a few points but waits about 87 s before
  any text and can end a reply inside hidden thinking.
- **Sonnet high** is the biggest jump on every Sonnet test (CursorBench 39% to
  48%, FrontierCode 37% to 49%) and beats the old Opus low on every measure at
  about the same cost. xhigh costs more than twice as much for about Opus
  medium's score.
- **Opus medium** stays: the biggest Opus jump, and the orchestrator needs
  judgment above its Sonnet workers.

- **How the tiers compare:** regular is Haiku 5.5 high (38), high is Sonnet 5.5
  high (47), the orchestrator is Opus 5.5 medium (51), and the root is Opus 5.5
  (42 at low, 51 at medium). Sonnet high is close to Opus medium on coding and
  review and guesses about as often (65% vs 68% of misses). Haiku is a clear
  step down and misreads files more often, but guesses less (45%).
- **Regular takes:** codebase discovery, lookups, review questions, summaries of
  named files, one small edit with a test that decides. Under about 100K tokens.
- **Never give regular:** findings the root will build on without re-checking,
  edits with no real test, multi-step tool workflows (AutomationBench 34% vs
  Sonnet's 55%), anything past 100K tokens (Haiku's price goes up 5 times).
- **Move up to high when:** any of the above, multi-file changes, terminal-heavy
  work, longer agent runs.
- **Give back to the root when:** a packet failed at Sonnet high, or needs
  architecture, an unclear root cause, or a judgment call. There is no Opus
  worker. An Agent tool `model: opus` override runs Opus at the file's high
  effort, which costs more than medium; use it only when the user asks.
- **How much to delegate:** a little. Every Claude model draws on the same
  weekly limit, so delegate to save root context or to run things in parallel,
  not to save money. 1 to 3 per pool, start at 2. For a big cheap fan-out, tell
  the user Codex Luna or OpenCode Go workers cost far less.

Risks accepted with this decision: Haiku 4.5 was rejected for `task-explore` on
September 22 because discovery feeds the root's reasoning, and Anthropic's own
audit says Haiku 5.5 still misreads file contents, omits things and claims work
is done more often than Sonnet 5.5. So the root re-checks any Haiku finding it
builds on, and Haiku edits need a test that decides. Haiku still costs Claude
quota, so the usual count stays 1 to 3; for a big cheap fan-out, tell the user
Codex Luna or OpenCode Go workers would cost far less.

Sonnet low: AA now scores it (35.9, $0.35 per task). Haiku high scores higher
for a quarter of the price, so low stays unused.

### Codex (OpenAI $100 subscription)

| Role | Model and effort | Labels | Status |
|---|---|---|---|
| `task-explore` | GPT-6 Luna xhigh | cheap, weak, high guessing, fast | live |
| `task-execute` | GPT-6.1 Sol low | cheap, solid, medium guessing, slow | live 2026-10-01, smoke-tested |
| `task-explore-high`, `task-execute-high` | GPT-6.1 Sol medium | mid, strong, medium guessing, slow | live 2026-10-01, smoke-tested |
| `task-orchestrator` | GPT-6.1 Sol high | mid, strong, medium guessing, slow | live 2026-10-01, smoke-tested (nesting not tested) |

- **How the tiers compare:** regular explore is GPT-6 Luna xhigh (35, guesses
  on 82% of misses), regular execute is GPT-6.1 Sol low (42), high workers are
  Sol medium (48), and the orchestrator is Sol high (50). The saved Codex root
  is GPT-6.1 Sol medium, so the high workers are the root's own model and
  effort: delegating to them saves context, not quality. Regular execute is
  one effort below the root; Luna is far weaker.
- **Regular takes:** explore (Luna): bulk lookups and greps you can check,
  summaries you will verify, under about 100K tokens. Execute (Sol low): small
  edits, careful lookups, search.
- **Never give regular:** Luna never edits or runs terminal work (8%
  Terminal-Bench) and gets no judgment calls. No Luna packet past 100K tokens:
  recall falls after 128K and Codex compaction has looped on long runs.
- **Move up to high when:** anything past a lookup that needs reasoning, coupled
  edits, or a result the root will build on. Sol low costs only about 3 times
  Luna, so step up early.
- **Give back to the root when:** the job needs architecture or judgment, or is
  time-sensitive: Sol runs about 22 tokens per second with an 11-second start on
  the subscription, so tell the user Claude Code is about 4 times faster.
- **How much to delegate:** a lot for lookups, less for reasoning. Luna is
  cheap: 3 to 8 checkable lookups at once. Sol workers 2 to 4, with doubled
  deadlines and fewer rounds, because every Sol run is slow on the subscription.
  Codex itself allows only four active agents including the root: at most
  three workers, or two while an orchestrator runs. That limit wins over the
  counts above.

Luna xhigh stays the explorer effort (October 7 audit): max scores higher on AA
but did no better on long agent runs.

### OpenCode (Go $10 plan for Go models)

| Role | Model and effort | Labels | Status |
|---|---|---|---|
| `task-explore`, `task-execute` | GLM 5.3 Flash | cheap, solid, low guessing, slow | live 2026-10-01, smoke-tested |
| `task-explore-high` | MiMo V2.6 Pro | cheap, solid, medium guessing, slow | live 2026-10-01, smoke-tested |
| `task-execute-high` | GLM 5.3 | premium on Go quota (220 per 5 h), solid, low guessing, normal | live 2026-10-01, smoke-tested |
| `task-orchestrator` | GPT-6.1 Sol medium (OpenAI subscription) | mid, strong, medium guessing, slow | live |

Why Go models: OpenCode workers on OpenAI models just spend the Codex quota
again, and OpenAI task workers through OpenCode were failing on September 30.
The Go models are paid for already and the GLM models guess least of anything we
track.

- **How the tiers compare:** regular is GLM 5.3 Flash (42, guesses on 28% of
  misses), explore high is MiMo V2.6 Pro (46), execute high is GLM 5.3 (45), and
  the orchestrator is GPT-6.1 Sol medium (48). OpenCode pins no root model; the
  usual root is GPT-6.1 Sol low (42), and a session may run a Go model instead.
  Against a Sol low root the high workers score a little higher and the regular
  worker about the same; against Sol medium or Opus they are weaker. Either way
  the Go workers guess far less. Trust them more than their scores suggest; ask
  less of their knowledge.
- **Regular takes:** GLM 5.3 Flash: careful reading, reconciliation, artifacts,
  small edits.
- **Never give regular:** knowledge-heavy questions (it knows less than Sol or
  Claude) or anything time-sensitive (45 tokens per second).
- **Move up to high when:** explore: many files or long documents to read and
  report (MiMo V2.6 Pro, best long reading in the Go set; check its facts).
  Execute: edits that need more agent skill (GLM 5.3).
- **Give back to the root when:** hard reasoning or design, or GLM 5.3's quota
  runs out (then GLM 5.3 Flash, or ask the user about Sol medium).
- **How much to delegate:** a lot. The Go models are already paid for. GLM 5.3
  Flash and MiMo 3 to 8 at once, with generous deadlines. GLM 5.3 at most 2 (220
  requests per 5 hours). Never give private files to Muse Spark (see its card).

### Gemini (Google AI subscription, `agy`)

| Role | Model and effort | Labels | Status |
|---|---|---|---|
| Root default | Gemini 3.8 Flash high | mid, solid, medium guessing, fast | live (user decision 2026-09-30) |
| `task-explore`, `task-execute` | Gemini 3.8 Flash medium | mid, solid, medium guessing, fast | live |
| High workers, orchestrator | none | | unsupported by user decision |

- **How the tiers compare:** regular workers are Gemini 3.8 Flash medium (40);
  the root is the same model at high, about a point higher. There is no high
  tier and no orchestrator.
- **Regular takes:** reading, search, summaries. Good knowledge and long reading.
- **Never give regular:** multi-step tool work or agent tasks (20%
  Terminal-Bench).
- **Move up to high when:** there is no high tier. Keep the job in the root.
- **Give back to the root when:** the job needs tool work or judgment; if it is
  big, tell the user another tool fits better.
- **How much to delegate:** a little. Delegation buys parallel reading, not a
  different skill. 2 to 4 at once (mid cost, its own quota pool).

Gemini 3.8 Flash is the only usable Gemini model. Never use Gemini Pro (latest
is 3.1, far behind) or older Flash versions. Gemini 4 needs fresh tests here
before use.

### Hermes Agent (OpenAI subscription via `openai-codex`, plus Go models)

Hermes has no task-explore or task-execute roles. It has one `delegate_task`
subagent, and `delegation.model` sets a single model for all of them.

| Role | Model and effort | Labels | Status |
|---|---|---|---|
| Main model (root and task-hermes default) | GPT-6 Sol medium | mid, solid, medium guessing, normal (starts in about 2 s) | live 2026-10-01, smoke-tested |
| Step up for hard analysis or review | GPT-6.1 Sol medium | mid, strong, medium guessing, slow (about 11 s to start) | pinned per task, nothing to sync |
| `delegate_task` subagents | GLM 5.3 Flash (Go) | cheap, solid, low guessing, slow | live 2026-10-01, smoke-tested |

Why: Hermes is a heavy app that makes many tool calls, and each call waits for
the model to start answering. GPT-6 Sol starts in about 2 seconds on the
subscription; GPT-6.1 Sol takes about 11 (measured in Codex, not yet in
Hermes). GPT-6 Sol medium is also better at multi-step tool work (58% vs 53%
AutomationBench than Sol 6.1 low). Delegated subagents get slow, cheap and
honest GLM 5.3 Flash: good for brute-force or parallel jobs where waiting is
fine.

- **How the tiers compare:** the one subagent type runs GLM 5.3 Flash (42,
  guesses on 28% of misses) under a GPT-6 Sol medium root (40, 57%). About as
  smart as the root and far more honest, but slow. There is no high tier and no
  orchestrator.
- **Regular takes:** the one `delegate_task` subagent type: brute-force or
  parallel jobs where waiting is fine, careful reading, reconciliation.
- **Never give regular:** time-sensitive or knowledge-heavy work.
- **Move up to high when:** there is no high tier. Pin GPT-6.1 Sol medium for
  that one task, or keep it in the root.
- **Give back to the root when:** design or judgment calls.
- **How much to delegate:** a lot, for parallel, brute-force or reading jobs
  where waiting is fine. 3 to 8 at once.

Other choices for one task: MiMo V2.6 Pro for heavy reading (slow, cheap).
Muse Spark 1.3 Contributor for fast public web research only; it trains on
your data, so it must never be the global delegation model and never sees
private files. Avoid Luna and DeepSeek Flash for driving Hermes: they guess too
much to run a long tool loop.

### Cursor

No maintained workers. See its adapter.

## 4. CLI bridges and web search

For `task-codex`, `task-claude`, `task-opencode` and `task-gemini`. Start cheap,
go up only when the task needs it.

| Bridge | Default | Step up | Hard tasks |
|---|---|---|---|
| Codex | GPT-6.1 Sol low (Luna xhigh only for explicit bulk lookups) | GPT-6.1 Sol medium | GPT-6.1 Sol high |
| Claude Code (`task-claude`) | Sonnet 5.5 high, as `--agent task-explore-high` or `task-execute-high` | Opus 5.5 medium (no agent) | Opus 5.5 high (no agent), only after medium missed something |
| OpenCode | GLM 5.3 Flash | GLM 5.3 | GPT-6.1 Sol medium |
| Gemini | Gemini 3.8 Flash medium | Gemini 3.8 Flash high (rare, costs about a third more) | none |
| Hermes | GPT-6 Sol medium (`openai-codex`) | GPT-6.1 Sol medium | GPT-6.1 Sol high |

**Why Sonnet high is the `task-claude` default.** Other harnesses already have
cheap workers (Luna, GLM 5.3 Flash), so a handoff to Claude is for quality:
careful review, reasoning, research the root will build on. Sonnet high is
Claude's best value at that level. Step down to Haiku 5.5 high (`--agent
task-explore` or `task-execute`) only for a short, checkable job that needs
Claude specifically, such as a Gmail or Drive lookup or a small search with
quoted links. Step up to Opus 5.5 medium for architecture, ambiguous root-cause
work, or a packet Sonnet high already got wrong. Past about 100K tokens of
context, never pick Haiku: it costs 5 times more there.

**Claude for web search.** Both sizes keep the web reference's ladders and
budgets; only the model changes.

| Search size | Claude Code native worker | `task-claude` | Why |
|---|---|---|---|
| Small: one fact or a few pages, links quoted, the caller checks | `task-explore` (Haiku 5.5 high) | `--agent task-explore` | Haiku guesses less than Sonnet high (45% vs 65%), and high is where its search stops collapsing |
| Medium: several sources compared, conflicts settled, or results the root will build on | `task-explore-high` (Sonnet 5.5 high) | `--agent task-explore-high` | About 7 points higher on HLE with tools; holds up when fetched pages push context past 100K |
| Large or deep research | the root, or Codex Sol medium on request | Opus 5.5 medium | Needs judgment across many sources |

Never run Haiku below high for search: wide research scores 13% at medium and
37% at high (WANDR). Ask every search worker for source links and dates on
each claim, because every Claude model guesses on a large share of its misses.

Web tool strengths, costs, ladders and compatibility live in [the web reference](../capabilities/web/README.md). Ordinary lookups use native tools without a skill. Launch flags stay in each task skill.

Retained web helper model choices: Codex uses GPT-6.1 Sol low. Gemini uses Gemini 3.8 Flash medium; its September benchmark ran at high, while October medium search scores are provisional. Public-page-only OpenCode reading may use Muse Spark 1.3. Public-page-only Hermes reading may use Muse Spark 1.3, otherwise GPT-6 Sol medium. Muse never receives private material. These choices stay model-owned here.

## 5. Model cards

Each card: what it is good for, where it fails, how to use it, and what to use
instead. A worker model's card ends with "Tell the worker": one line the root
copies into every packet for that model, aimed at its main failure. Numbers: intelligence / dollars per task / Terminal-Bench / guessing rate.

**GPT-6 Luna xhigh** (34.6 / $0.04 / 8% / 82%). cheap, weak, high guessing, fast.
Good for: bulk lookups you can check, quick greps, summaries you will verify,
multi-step tool workflows (AutomationBench 48%, above Haiku's 36%). Fails at:
edits and terminal work, judgment, anything that must be right. It knows a fair
amount (44% knowledge accuracy, above Haiku) but guesses on 4 of 5 misses, and
hid a broken search tool 29% of the time (Sol 2%). Recall falls past about 128K
tokens. Use: many workers, packets under 100K, check everything. Instead: GLM
5.3 Flash when the answer must be right; Sol low for edits; Haiku high in
Claude Code for the same price with far less guessing.
Tell the worker: "Quote the exact line for every claim. If you cannot find it,
say not found; do not guess."
**Luna max** (38.1 / $0.07 / 13% / 77%): only for one short, hard question; on
long agent runs it timed out more and did no better than xhigh.
**GPT-5.6 Luna** is older, costs 2 to 4.6 times more per task and guesses more
(92%), but finishes more coding tasks (19 vs 12 of 23 at max). Fallback only:
for coding, Sol low is better at a similar price.

**GPT-6.1 Sol low** (42.1 / $0.13 / 31% / 52%). cheap, solid, medium guessing,
slow on Codex. Good for: small edits, careful lookups, search. Fails at: speed
(22 tok/s, 11 s first token on the subscription); still guesses half the time
when wrong. Instead: Opus low in Claude Code when speed matters.
Tell the worker: "Run the check and paste its output. Say what you did not verify."

**GPT-6.1 Sol medium** (47.8 / $0.21 / 48% / 52%). mid, strong, slow on Codex.
Best value for real coding and reasoning. Same speed problem, more tokens, so
even slower in wall-clock time. Verify facts. Instead: Opus medium when speed
matters and budget allows.
Tell the worker: "Cite file and line for each finding, run the checks you were
given and paste the output. Stop at the listed scope."

**GPT-6.1 Sol high** (50.2 / $0.32 / 52% / 49%). mid, strong, slow. Matches Opus
medium on intelligence at about a quarter of the price and guesses less. Use for
orchestration and hard reasoning when time is not tight. In one independent
legacy-rewrite test it passed every task for no more than medium cost. xhigh
(51.0 / $0.39) and max (51.8 / $0.72) add under a point each and wait 2 to 5
minutes before visible output: skip them.

**GPT-6 Sol** (low 33.9 / $0.13, medium 39.8 / $0.25 / 19% / 57%). mid, solid,
medium guessing, starts answering in 1.9 s. Weaker than GPT-6.1 Sol but much
quicker to start, which is why it is Hermes's main model. Elsewhere a fallback.

**Claude Opus 5.5 low** (42.3 / $0.55 / 31% / 68%). premium, solid, high
guessing, fast (about 97 tok/s on the subscription). Same intelligence as Sol low
at about 4 times the price, but about 4 times faster. Fails at: admitting it
does not know; check its factual claims. Use: 1 to 3 at a time.

**Claude Opus 5.5 medium** (51.2 / $1.34 / 53% / 68%). premium, strong, fast.
Opus's sweet spot: the jump from low is the biggest of any family. Expensive:
use for the orchestrator and hard root work, not routine workers. Same
guessing caveat. **high** (53.6 / $1.82 / 57%) for ambiguous repo work when
medium missed something. **xhigh and max** (56.0 / $3.46, 57.6 / $5.98) tie or
lose to high on CursorBench and a legacy-rewrite test, wait 2 to 12 minutes
before visible text, and fall back to Opus 4.8 more often: skip them.

**Claude Sonnet 5.5 medium** (40.8 / $0.48 / 30% / 51%). premium, solid, fast
(about 97 tok/s, 4.5 s to first text). Guesses less than Opus, knows less. Half
the price of Opus for input, output and, since October 7, cache hits ($0.10).
Good for: small, specified edits with a real test, fast answers. Fails at:
subtle bugs (missed one that high found), long agent tasks (can check in early).

**Claude Sonnet 5.5 high** (46.8 / $0.88 / 44% / 65%). premium, solid, fast
(12 s to first text). Claude Code's high workers since October 7. Sonnet's
sweet spot: the biggest jump on every test
(CursorBench 39% to 48%, FrontierCode 37% to 49%). Good for: investigation,
review, bug hunting, multi-file changes, longer agent runs. Beats Opus low on
every measure at about the same CursorBench cost. Fails at: guesses more when
wrong than medium (65% vs 51%); ask for file and line evidence. **xhigh**
(51.9 / $2.01 / 57%) only after a high attempt fails; about Opus medium's score
and cost. **max**: never; got worse on FrontierCode from extra review agents
and out-of-scope edits. Sonnet low (35.9 / $0.35): no job; Haiku high is better.
Tell the worker: "Give file and line for every finding. Mark guesses as guesses.
Do not edit outside the listed files."

**Claude Haiku 5.5 high** (37.8 / $0.08 / 22% / 45%). premium on the Max plan
(the lightest Claude, exact quota weight unpublished), solid, medium guessing,
fast output (about 140 tok/s) but hidden thinking means about 26 s before the
first visible text on hard prompts. Claude Code's regular workers since
October 7. Haiku's sweet spot. Good for: codebase
discovery, lookups, review questions, research, summaries of supplied files.
Beats Sonnet medium on CursorBench (42.3% vs 39.2%) for under half the cost.
Fails at: reading files faithfully (Anthropic's audit ranks Sonnet 5.5 strictly
better on misreading, omissions and false "done"); multi-step tool workflows
(AutomationBench 34% vs Sonnet medium 55%); long context (5 times the price over
100K tokens, so Sonnet is cheaper on long agent runs); refusals have no
fallback. **medium** for one named lookup the caller checks (can skip checks);
**low** only for routing; **xhigh** (41.2 / $0.12) for hard short-context coding
or agent tasks, but about 87 s to first text and replies can end inside hidden
thinking; **max** never. Instead: Sonnet for edits and anything the root will
not re-check, GLM 5.3 Flash when it must not guess, Luna xhigh for cheaper
checkable bulk lookups. Against Luna at the same AA score (Luna max), Haiku
high does about twice the terminal work (22% vs 13%) and guesses far less (45%
vs 77%). Evidence: `EFFORTS.md`, `SELECTION.md` cheap tier audit.
Tell the worker: "Read each file fully before answering. Run the test and paste
its output; do not say done without it. List anything you skipped."

**GLM 5.3 Flash** (41.8 / $0.25 / 33% / 28%). cheap on Go (6,320 requests per
5 h), solid, low guessing, slow (45 tok/s). The most honest model we track. Good
for: careful reading, reconciliation, artifacts, small edits. Fails at: speed;
knows less than Sol or Claude. Use: many workers, generous deadlines.
Tell the worker: "Answer only from the files given; say so when they do not cover it."

**GLM 5.3** (44.8 / $2.01 / 42% / 30%). premium on Go quota, solid, low guessing. Honest and good at agent tasks, but only
220 Go requests per 5 hours. At most 2 at once. Instead when quota runs out: GLM
5.3 Flash, or ask the user about Sol medium.
Tell the worker: "Finish in as few steps as you can; you have a small request
budget. Save what you read with a script or a file write, never copy it by hand.
Run the test and paste its output."

**MiMo V2.6 Pro** (46.3 / $0.13 / 35% / 41%). cheap on Go (3,250 per 5 h), solid,
slow (42 tok/s). Best long-document reading in the Go set (86% AA-LCR). Good for:
reading many files and reporting. Knowledge score is low (+8), so check facts.
Tell the worker: "Cite the file for each point. Do not add facts from memory."

**Muse Spark 1.3 Contributor** (45.1 / 31% guessing, 144 tok/s). Fast and fairly
honest, and the most Go requests of any model. **Its data is used for training:
public web material only, never private files or specs.** Not usable as a
workspace worker for that reason.

**Gemini 3.8 Flash medium** (39.8 / $0.93 / 20% / 52%). Fast, good knowledge and
long reading, weak at agent tasks. Its own quota pool. Fine for reading and
search; avoid multi-step tool work. High costs about a third more for one point.
Tell the worker: "Read and report only. Quote the source for each point. Do not
start multi-step tool work; stop and report instead."

**Cheap throwaway models.** MiMo V2.6 Flash and Qwen 3.8 Flash: cheap and slow
with negative knowledge scores. DeepSeek V4.1 Flash: the fastest (209 tok/s) but
guesses 96% of the time. Throwaway or easily checked work only, never artifacts
or reconciliation.

**Expensive for what they give.** Qwen 3.8 Max (honest, slow, $5.41 per task) and
Kimi K3 (best long reading, 110 Go requests per 5 h). Use only on request.

## 6. Pick by job

Pick the row, then the cheapest harness you are allowed to use. Efforts follow
[`EFFORTS.md`](EFFORTS.md). Claude Code options
assume the role table above (regular workers Haiku high, high workers Sonnet
high); when you choose a model directly (for example the
Agent tool's `model` field), use these.

| Job | Claude Code | Codex / OpenCode | Why |
|---|---|---|---|
| One named-file or symbol lookup you will check | Haiku medium | Luna xhigh (Codex), GLM 5.3 Flash (OpenCode) | Cheapest that is reliable enough |
| Codebase discovery, "where is X and how is it used" | Haiku high (`task-explore`) | Sol 6.1 low | Haiku high beats Sonnet medium on coding reads |
| Findings the root will build on without re-checking | Sonnet high (`task-explore-high`) | Sol 6.1 medium | Sonnet reads files more faithfully than Haiku |
| Review, bug hunting, root-cause investigation | Sonnet high; Opus medium if ambiguous | Sol 6.1 high | Only high-effort runs found the subtle bugs |
| Small, specified edit with a real test | Haiku high (`task-execute`) | Sol 6.1 low | Close to Sonnet on scoped coding; the test decides |
| Multi-file change, feature, refactor | Sonnet high | Sol 6.1 medium or high | Biggest jump on every coding test is Sonnet medium to high |
| Failed once at high, hard coding | Sonnet xhigh or Opus medium | Sol 6.1 high | Both about the same score and cost |
| Long autonomous agent run | Opus medium or Sonnet high, with milestones | Sol 6.1 medium | Haiku costs 5 times more past 100K tokens; Luna recall falls past 128K |
| Packet likely past 100K tokens of context | Sonnet high, or split it | Sol 6.1 medium, or split it | Neither cheap model holds up there |
| Multi-step tool or business workflow, checked | Haiku high | Luna xhigh | Luna does these better than Haiku (AutomationBench 48% vs 34%) |
| Orchestration, architecture, hard reasoning | Opus medium | Sol 6.1 high | Highest value at the top tier |
| Must not invent facts | not Claude alone: check it | GLM 5.3 Flash or GLM 5.3 | Lowest guessing; Claude guesses 44% to 68% |
| Artifacts, reconciliation, reading specs | Sonnet high, verify | GLM 5.3 Flash or GLM 5.3, else Sol 6.1 medium | Lowest guessing |
| Long documents | Opus medium | MiMo V2.6 Pro, Gemini 3.8 Flash | Best AA-LCR |
| Wide fact gathering across many sources | Haiku high at least, Sonnet high better | Sol 6.1 medium | Haiku collapses below high (WANDR) |
| Routing, classification | Haiku low | Luna xhigh | Cheapest |
| Time-sensitive | Sonnet medium (4.5 s to first text) | DeepSeek Flash for throwaway | Haiku and Opus wait longer; Sol is slow on Codex |
| Public web research | Section 4 and `capabilities/web/README.md` | same | Quote and link every fact |
| Private material | any Claude | not Muse Spark | Contributor trains on data |

Never default to max on any model, and avoid xhigh on Opus and Sol.

## 7. Fallbacks

On a rate limit or missing model, a worker may try one model from the same row,
once, and must tell the caller what it switched to and why. Never move up a price
row silently, and never to a model whose card says to avoid that job.

| Row | Interchangeable models |
|---|---|
| Cheap, simple | GPT-6 Luna xhigh, GPT-5.6 Luna xhigh, MiMo V2.6 Flash, Qwen 3.8 Flash |
| Cheap, careful | GLM 5.3 Flash, MiMo V2.6 Pro, Muse Spark 1.3 (public only) |
| Fast | GPT-6 Sol low, DeepSeek V4.1 Flash (throwaway only), Muse Spark 1.3 (public only) |
| Mid | GPT-6.1 Sol low or medium, Claude Opus 5.5 low, Claude Sonnet 5.5 medium or high, Claude Haiku 5.5 high, GLM 5.3 |
| Hard | GPT-6.1 Sol high, Claude Opus 5.5 medium |

Each subscription has its own limits, so switching provider is the usual way
past a rate limit. Stay on each model's best harness: GPT on Codex, Claude on
Claude Code, Go models on OpenCode. Fast service tier is off (about double cost)
except for Luna.

## 8. Changing a model choice

1. Edit only this file: the row in section 3 or 4 and the model's card. When the
   change touches `task-explore`, `task-execute`, their high versions or
   `task-orchestrator`, also rewrite that tool's six-line block in section 3
   (how the tiers compare, what each takes, how much to delegate) and make sure
   the new worker model's card has a "Tell the worker" line. Mark the row
   "pending sync". Note the change in `STATE.md`.
2. In each affected tool, run `sync-tool-adapter` in that tool's own session. It
   makes the native agent files match this file, checks them live, flips the
   row to "live", and corrects that tool's block if the live check disagrees.
3. Do not copy model names into skills or adapter prose. Point here.

## 9. Field notes

Real problems seen in use. Add one dated line when a model lets you down, so the
next agent knows without the user repeating it.

- 2026-09-30: OpenAI models used as OpenCode task workers were failing.
- 2026-09-30: GPT-6.1 Sol feels sluggish on the Codex subscription (about a third
  of API speed). Measured in `subscription-speed.md`.
- 2026-10-01 (owner's experience, from Hermes memory): GPT-6 Luna feels less
  reliable than GPT-5.6 Luna at the same effort, even though the benchmarks
  show GPT-6 Luna guessing less (82% vs 92%). Watch both before trusting either.
- 2026-10-01: Hermes had its own model guidance in several places; it now
  points here.
- 2026-10-01: Worker counts used to be the same for every tool, so roots ran the
  same number of Opus workers as Luna workers. Counts now follow section 2.

- 2026-10-07: A Codex CLI child told to start Gemini (`agy`) in the background
  with `&` got empty output files and no process; the job most likely died when
  the shell call returned. Run a Gemini child in the foreground, or launch it
  from the root harness instead.
- 2026-10-07: Sonnet 5.5 cache reads dropped from $0.20 to $0.10 per million.
  Sonnet rows were refreshed from the AA website the same day.
- 2026-10-07 (owner's experience, checked by a three-way audit): GPT-6 Luna
  degrades on long work. Recall test: holds to 128K at high, then 76% at 192K
  and 26% at 512K. GPT-5.6 Luna does finish more coding tasks (19 vs 12 of 23
  at max) at 2 to 4.6 times the cost. Luna 6 max is cheap ($0.07 per AA task)
  but no more reliable than xhigh on long runs. `SELECTION.md`, cheap tier audit.
- 2026-10-07: Effort names do not line up across families. Sonnet high is
  about Sol medium; Opus medium is about Sonnet xhigh and Sol high. Compare by
  score and cost, never by effort name (`EFFORTS.md`, cross-model ladder).
- 2026-10-01: One OpenCode GLM 5.3 worker spent the whole Go 5-hour allowance in about 20 minutes by hand-copying web pages; default OpenCode workers to GLM 5.3 Flash, give every packet a fallback model, and have workers save raw output with scripts, not by hand.
- 2026-10-13: Three GPT-6.1 Sol high writers on the Codex subscription each took 20+ minutes on blocking synthesis steps in a spec build, and the next phase waited. The owner keeps Sol for parallel fan-outs of many workers and wants blocking steps on faster Claude workers (section 2, Blocking step).
- 2026-10-13: In a 300-file spec build on the Codex subscription, GPT-6.1 Sol at low effort finished about 70 capture packets (1 to 3 URLs each) in 1 to 5 minutes each, and about 80 digests in about 5 minutes each, with 50 to 70 running at once and no capacity retries. Sol at high effort took about 15 to 20 minutes per 8,000 to 14,000 word document with 14 running in parallel, which is acceptable for parallel fan-outs. The one blocking judgment step (spec architecture across 82 sources) ran on Opus 5.5 in about 7 minutes.
