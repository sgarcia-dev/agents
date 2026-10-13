---
created_at: 2026-09-30
updated_at: 2026-09-30
model: anthropic/claude-opus-5-5
doc_type: architecture
purpose: How the engine is built. What code does, what models do, the run folder, the evidence record, citation checking, workers, and how each harness plugs in. Reconciled from five outside reports and a Hermes self-audit on September 30, 2026. Proposal; nothing is built yet.
related:
  - path: ./spec.md
    why: The loop, rules, and status this design implements.
  - path: ./stage-prompts.md
    why: The model side of each stage.
  - path: ./budget-tiers.md
    why: The numbers the helper enforces.
  - path: ./models-and-plans.md
    why: Which model runs each slot and what each plan allows.
  - path: ./skill-proposal.md
    why: How a skill would package this design.
  - path: ../../hermes-internet-deep-research/spec.md
    why: Hermes pieces this design borrows (citation ledger, bundles, worker packet).
---

> Historical, 2026-10-01: This prototype is parked. It is not current policy or a build plan. Current web facts and decisions: [capabilities/web](../../../capabilities/web/README.md) and [web decisions](../../../capabilities/web/DECISIONS.md).

# Architecture

**One sentence:** a small helper program does everything that can be counted
or checked, and models only make judgment calls.

All five outside reports and the Hermes self-audit reached this independently.
A prompt that says "use at most 10 searches" is a request, not a limit. Hermes
proved it: its research skill says "20 searches, 25 reads", but nothing stops
search 21 (Hermes report, section 3 (private, not published)).

## The three parts

| Part | What it is | Who edits it |
|---|---|---|
| **Prompts** | One Markdown prompt per stage, with `{budget}` placeholders. See [stage-prompts.md](./stage-prompts.md). | You, rarely |
| **Config** | One YAML file: tiers, model per slot, provider order, caps. See [engine.example.yaml](./engine.example.yaml). | You, when a plan or price changes |
| **Helper** | A small command-line program (working name `dr`). It searches, reads pages, counts, stores evidence, and renders citations. Any harness can call it through its shell. | Code, built once |

Why a command-line helper and not only MCP: every harness here (Claude Code,
Codex, OpenCode, Hermes) can run shell commands, but each sets up MCP
differently. MCP search servers stay optional extras (Claude report, section 10).

## Who does what

| Work | Done by | Why |
|---|---|---|
| Count searches, reads, rounds, dollars; refuse past a cap | Helper | A model cannot be trusted to stop itself |
| Normalize URLs, drop repeat URLs and exact repeat queries | Helper | Mechanical |
| Cache pages, save page snapshots with line numbers | Helper | Needed to check quotes later |
| Check that a quote really appears in the saved page | Helper | Exact text match |
| Turn `[[E12]]` markers into numbered citations and a source list | Helper | The model never writes a URL |
| Write the receipt | Helper | From its own counters |
| Pull evidence from one page | Cheap model, called by the helper | High volume, narrow task |
| Write queries, pick which results to open, select evidence for the writer | Cheap model | Narrow tasks with small outputs |
| Brief and plan, gap check and stop, splitting work across workers | Smart model | Mistakes here waste the whole run |
| Write the report | Writer model | Quality shows here |
| Check that each cited sentence is supported | Smart model (cheap once tested) | Needs judgment about scope and wording |

The expensive model never sees raw pages. It sees evidence records only. That
is the single biggest saving (ChatGPT cost report, section 9, lever 1). Related
evidence, for a different technique: Anthropic measured an 84% token cut from
context editing (clearing old tool results from the chat) in a 100-turn web
search test (verified (private, not published)).
Both point the same way: stale page text in context is the main waste.

## The run folder

Every run is one folder. Nothing important lives only in a chat.

```text
runs/<run-id>/
  brief.json        the question, requirements (R1..), sub-questions (Q1..), assumptions
  coverage.json     status of each requirement (see below)
  ledger.json       budget caps, reservations, and every counter
  queries.jsonl     every query sent: text, provider, result count, errors
  sources/          one saved snapshot per page read, with line numbers
  sources.jsonl     one line per source: id, URL, title, fetched time, route, hash, status
  evidence.jsonl    one line per evidence record (schema below)
  report.md         the writer's draft with [[E12]] markers
  audit.json        the citation check results
  final.md          rendered report with numbered citations and the receipt
```

These are the four stores the ChatGPT internals report asks for (sources,
evidence, coverage, budget; section 12.3), laid out as files the way NVIDIA
AI-Q and Anthropic do. Anthropic: subagent output goes "to a filesystem to
minimize the 'game of telephone'" (verified).

## Helper commands (proposed)

| Command | Does | Counts against |
|---|---|---|
| `dr init <tier> "<question>"` | Makes the run folder and ledger from config | nothing |
| `dr gather Q2 --searches N --reads M` | Runs one sub-question's inner loop with the cheap model: write queries, search, pick, read, extract. Returns a short digest of new evidence | the searches and reads it uses |
| `dr search "<query>" --q Q2` | Runs one query through the provider list; stores results | 1 search |
| `dr read <result-id or URL> --q Q2` | Fetches the page, saves a snapshot, calls the cheap model to pull evidence, checks quotes, appends records | 1 read, cheap tokens |
| `dr status` | Prints budget left, coverage, and the no-gain counter | nothing |
| `dr reserve <worker> --searches N --reads M` | Sets aside part of the shared budget for one worker | reserved, then released |
| `dr render` | Checks markers, builds numbered citations and the source list | nothing |
| `dr check` | Runs the mechanical checks (below) | nothing |
| `dr receipt` | Writes the receipt | nothing |

`dr gather` is the main command. It keeps the whole search-and-read inner loop
out of the expensive agent's chat. The agent sees one short digest per
sub-question instead of every result list and page. This matters because
harness overhead (the agent resending its chat every turn) is the largest
cost on a pay-per-use API; see [budget-tiers.md](./budget-tiers.md).
`dr search` and `dr read` stay available for manual, one-off steps.

These match the four operations Hermes proposed for any harness: `search`,
`fetch`, `record_claim`, `verify_report`, with "one atomic run budget across
adapters and workers" (Hermes report, section 9).

**Strict mode.** A cap only holds if every search goes through the helper. In
strict mode the harness's own search and page tools are switched off for the
run (for example `--disallowedTools WebSearch WebFetch` in Claude Code, or no
`--search` flag in Codex). Without strict mode, native searches still happen
and the receipt must count them as "not observed", not zero.

## Counting the right things

Different things cost different amounts, so the ledger counts them separately
(ChatGPT internals report, section 13.1; Hermes section 4):

- search queries (each query in a batch counts), and provider requests;
- page read attempts, successful reads, and unique pages;
- failed reads (paid readers can bill a 403 or 404 page);
- cache hits;
- model calls and tokens per slot, including reasoning tokens where shown;
- extra cash spent, and subscription usage where the plan shows it.

## The evidence record

One line in `evidence.jsonl`. Fields marked `*` are filled by the helper, never
the model. This merges ChatGPT's data contract, Claude's note format, and
Hermes's claim map (prompt merge report, section 4 (private, not published)).

| Field | Filled by | Meaning |
|---|---|---|
| `evidence_id`* | helper | `E1`, `E2`, ... stable for the run |
| `source_id`*, `url`*, `retrieved_at`*, `chunk_id`* | helper | Where it came from |
| `published_at` | model, `null` if the page does not say | A fetch date is not a publish date |
| `source_type`* | helper, from config rules | primary, secondary, vendor, forum, unknown |
| `question_ids` | model | Which sub-questions it helps |
| `claim` | model | One assertion, in plain words |
| `quote` | model | Exact words from the page, 40 words at most |
| `line_start`, `line_end` | model | Where the quote sits in the snapshot |
| `note_type` | model | observation, opinion, forecast, or marketing claim |
| `qualification` | model | Conditions, units, dates, or limits that change the meaning |
| `quote_valid`* | helper | The quote was found in the saved page |

Records the helper cannot validate are kept but marked, and the writer never
sees them. Search snippets are leads, not evidence: they can point at a page to
read, but they cannot be cited (ChatGPT prompt pack, stage 04; Hermes: "Search
results are discovery leads, not opened-page evidence").

## Coverage map

Each requirement in `coverage.json` has one status:

- `not_started`
- `partial`: some evidence, not enough.
- `supported`: one primary source (the party that owns the fact, for example a
  vendor's own price page), or two independent sources that agree. Copies of
  the same press release are one source, not several.
- `conflicted`: good sources disagree. Kept open and shown in the report.
- `unknown`: tried and not found. A legitimate result, not a reason to keep
  searching.

This replaces "the model feels done". The gap check reads this file; the
helper tracks how many rounds in a row added no new `supported` item or
resolved conflict (the no-gain counter).

## Citations: four layers of checking

The ChatGPT internals report separates three meanings of "verified"; Hermes's
own test adds a fourth lesson.

| Layer | Question | Done by | Example of a failure it catches |
|---|---|---|---|
| 1. Reference integrity | Does every `[[E12]]` exist in the evidence file? | Helper | A made-up source number |
| 2. Quote validity | Is the quote really in the saved page? | Helper | A paraphrase passed off as a quote |
| 3. Claim support | Does the quote support the sentence (numbers, scope, dates, strength)? | Smart model audit | "Price is $5" cited to a page that says "$5 per 1,000" |
| 4. Source quality | Is the source reliable, current, and independent? | Gap check and writer, stated openly | A vendor marketing claim reported as fact |

**Layers 1 and 2 alone are not enough.** Hermes ran its own `verify` checker
on a deliberately false sentence ("the moon is made of cheese") cited to a
real source, and it passed. It also passes a report with no citations at all
(Hermes report, section 7). That is why layer 3 is a separate model call on
the original page text, not on the note.

The audit uses five verdicts: supported, partial, unsupported, contradicted,
unverifiable. Partial is not a pass. The helper, not the auditor, decides
whether the report can ship, and says in the receipt how many claims were
checked when a cap cut the audit short.

## Workers

- **Default is one loop, no workers.** LangChain's own prompt says "Bias
  towards single agent" (verified). Anthropic's multi-agent setup beat a single
  agent by 90.2% but used about 15x the tokens of a chat, and the comparison
  was not at equal cost (verified; ChatGPT internals report, section 14.1).
- **Workers only for breadth questions** at medium and above: the question
  splits into independent parts (one per product, country, or approach).
- **Shared budget with reservations.** Before a worker starts, the helper
  reserves its share from the one global ledger and releases what it did not
  use. Without this, parallel workers each see the same budget left and
  overspend (ChatGPT internals report, section 13.3).
- **Self-contained brief:** one objective, what is out of scope, the budget,
  known URLs to skip, the output path, and when to stop. Workers do not see
  the main chat.
- **Workers write evidence records to the run folder** and return a short
  summary plus their counts. The main agent merges from the files, never from
  the summary alone (Hermes: worker summaries are trimmed at 24,000
  characters).
- Workers never start other workers.

## How each harness plugs in

The smart and writer slots run as the harness's own model (the agent reading
the skill). The cheap slot is called by the helper (`dr gather`, `dr read`)
through a pay-per-use API by default, so page text never enters the
expensive chat and the same cheap model works in every harness.

| Harness | Smart and writer slot | Cheap slot | Strict-mode switch | Workers |
|---|---|---|---|---|
| Claude Code | Session model | Helper, pay-per-use API | `--disallowedTools WebSearch WebFetch` | Native subagents |
| Codex CLI | Session model | Helper, pay-per-use API | Omit `--search` | Parallel `codex exec` runs, or none |
| OpenCode | Session model (Go or ChatGPT login) | Helper, pay-per-use API | Per-agent tool settings (unverified) | Agents with their own model |
| Hermes | Main model | Helper, pay-per-use API | Unverified | `delegate_task`, one model for all children |

Routing the cheap slot through an OpenCode Go model is possible but carries a
terms-of-service risk for batch use; see
[models-and-plans.md](./models-and-plans.md).

Details on which cheap models are allowed where, and the plan rules that
matter (OpenCode Go asks for "typical coding agent traffic"), are in
[models-and-plans.md](./models-and-plans.md).

## What to borrow from Hermes

From the Hermes self-audit (private, not published)
(sections 9 and 10):

- **Borrow:** the citation ledger script (`sources.py`, standard-library
  Python) as a starting point for `dr`'s source list, with one ledger per run,
  not one shared profile ledger; the coverage map with a "what would disprove
  this" question; the small search health check before a big sweep; the
  worker `REPORT.md` bundle layout; the worker brief template.
- **Do not borrow as guarantees:** automatic stage order, search caps, cost
  totals, fresh re-opens (a re-read within 20 minutes hits the cache), or its
  `verify` result as proof that claims are supported.

## Failure modes at scale

Expected, not measured (ChatGPT internals report, section 13.5):

| At 200+ searches | Design answer |
|---|---|
| Workers rediscover the same pages | Shared URL list and query history in the helper |
| Repeated summaries drop dates and conditions | Keep the original quote and page; summarize by reference |
| Supervisor rereads everything | Short coverage updates; evidence stays on disk |
| Local caps multiply across workers | One global ledger with reservations |
| Many URLs trace back to one claim | Track source family; copies count once |
| Retries and blocked pages eat the budget | Failures count; per-provider retry caps |
| Page text tries to give orders | Page text is data; the reader call has no tools |

## What the September 30 reports changed here

This file is new. Before it, the spec said "a counter (a ledger file, or code
later)". Now the helper is the recommended design, the evidence record has a
fixed schema, citations are rendered by code, and checking has four layers.
The loop itself did not change.
