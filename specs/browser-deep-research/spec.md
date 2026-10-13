---
created_at: 2026-10-09
updated_at: 2026-10-09
model: claude-opus-5-5
doc_type: spec
purpose: Own how we write research prompts for the ChatGPT and Claude websites, which research mode to use for which job, and the side benchmark capability that keeps both choices honest.
related:
  - path: ./STATE.md
    why: What is true now, the planned benchmarks and the next action.
  - path: ./BENCHMARKS.md
    why: Dated log of every benchmark run, its numbers and its lessons.
  - path: ./DECISIONS.md
    why: Choices made, with rejected alternatives.
  - path: ./SOURCES.md
    why: Where the evidence and procedures live.
  - path: ../internet-deep-research/spec.md
    why: Sibling spec for agent-run search and fetch tools (not the hosted websites).
  - path: ../browser-use/spec.md
    why: Browser safety and identity contract the runners follow.
---

# Browser Deep Research Spec

We often ask the ChatGPT and Claude websites to do research for us, run by a
browser agent. This spec owns three things: **how to write those prompts so
runs finish and stay accurate**, **which research mode fits which job**, and
**a side benchmark capability** we use to test and improve both. Results are
logged in `BENCHMARKS.md` every time, so the advice changes with the evidence.

## Start Here

- Status and next action: [STATE.md](./STATE.md)
- Benchmark log and lessons: [BENCHMARKS.md](./BENCHMARKS.md)
- Decisions: [DECISIONS.md](./DECISIONS.md)
- Writing prompt packs (procedure): [browser-deep-research-prompts skill](../../skills/browser-deep-research-prompts/SKILL.md)
- Running and exporting on chatgpt.com: [chatgpt-browser skill](../../skills/chatgpt-browser/SKILL.md), especially `references/research-chats.md` and `references/export.md`
- Sources: [SOURCES.md](./SOURCES.md)

## Scope

In scope: research run on the **hosted websites** (chatgpt.com, claude.ai)
by a browser agent, the prompts we write for them, mode choice, export, and
benchmarking. Out of scope: agent-run search and fetch tools and APIs (see
`../internet-deep-research/`), and any website automation details (they live
in the skills).

## Behavior: how research prompts must be written

These rules come from measured runs (see `BENCHMARKS.md`, B1 and B2). The
skill holds the procedure; this spec holds the rules and the why.

1. **Bounded scope with a stopping rule.** Every prompt states a range (for
   list prompts, for example 20 to 40 items, stop at the top), a time target
   (about 20 minutes) and: "If you are running long, stop and deliver what
   you have, and list what you did not check. A shorter, accurate list is
   better than a long one." Never write "as complete as possible" or
   "length is wanted".
   *Why:* an unbounded 100+ row prompt made Chat 6 Pro run 65 minutes,
   Chat Extra High stall without replying, and Deep research quit early.
   The slim version cut 6 Pro to 20 minutes with no stall.
2. **Completeness comes from splitting, not from one prompt.** A big topic
   becomes several capped prompts (one or two sub-groups each), merged
   later.
3. **Sweep first, depth later.** A list (sweep) prompt asks only for what
   the user needs to pick items: about 5 to 7 columns, one source per row.
   Deep checks (culture, interview style, policies, per-claim dated and
   labeled evidence) go in a later depth prompt about the picked items.
4. **Ask at the level the user decides at.** If the user picks
   *companies*, ask for company-level evidence (offices, legal entities,
   hiring regions, careers page, job board system), **not job postings**.
   *Why:* asking for "current postings" made models chase open roles,
   pulled in small unknown firms that happened to have one, slowed runs,
   and produced rows that went stale when postings closed. A separate
   system can find live roles.
5. **Keep the filters when slimming.** Keep hard exclusions (for example
   staffing and outsourcing firms) and the group's main filter (big name,
   great culture, fast growth) **ahead of** "has a route". *Why:* the slim
   rerun lost both, and outsourcing firms and off-brief companies crept in.
6. **Evidence rule scaled to the prompt type.** Sweep: "one source per row,
   a full https link, with its date if shown". Depth: "date and link every
   number; label each claim". Always: "Write Not found instead of guessing".
   *Why:* per-claim evidence on every row multiplies work; one chat run
   emitted unresolved link placeholders when links were not demanded
   explicitly.
7. **Chat modes write the answer directly.** "Do not build scripts,
   spreadsheets or databases. Write the answer directly." Answer in the
   reply as Markdown unless a file is needed. *Why:* on the big prompt both
   Chat runs built scripts and source databases and looped on
   self-verification.
8. **Short prompts.** About 400 to 600 words. Background about the user is
   cheap and useful; long rule and column lists are not.
9. **Skip lists are fine.** Listing names to skip worked: neither Chat
   report re-listed a known company.

Rules 10 to 17 come from the B3 re-grade (four task types, every run
checked claim by claim). **They are a menu, not a checklist.** Each one
fixed a specific failure, but adding all of them would recreate the
overloaded prompt that made B1 runs hang and drift. Rule 18 limits them.

10. **Ask for the decision points the user did not ask about.** Add: "List
    any decision points I did not ask about that would change what I
    should do." *Why:* the prompt's framing set the coverage ceiling. On
    the permit question no run, and no pair of runs, raised the two
    biggest trade-offs, because the prompt only asked about speed.
11. **Negative claims must say where they looked.** Add: "For any claim
    that something does not exist or is not allowed, say where you
    searched." *Why:* "there is no X" was the riskiest claim type. Three of
    five runs said "no expedite route" from one FAQ line; two found the
    route in parliamentary answers.
12. **Keep conditions attached to rules.** Add: "For each rule, say when it
    stops applying to me (dates, status), and keep those conditions in the
    summary and tables." *Why:* both Claude runs stated a rule correctly in
    the body, then dropped its deadline in the headline. That was the only
    decision-changing error outside Deep research.
13. **Date sources; flag old ones.** Add: "Give each source's date. Mark
    anything older than 12 months as historical unless a current page
    repeats it. Flag official pages that contradict each other." *Why:*
    stale facts stated as current were the main failure of Deep research,
    and official pages themselves were stale twice.
14. **Likelihoods get a best estimate, not "unknown".** Add: "For
    likelihoods, give a best estimate with a confidence level. Use 'not
    found' only for facts." *Why:* "say not found instead of guessing" made
    6 Pro mark 6 of 14 risks "unknown" where evidence supported "low".
15. **Rankings: one dataset, and demand separate from advice.** Add: "Rank
    inside one comparable dataset. Give 'measured ranking' and
    'recommended order' separately." *Why:* "rank by evidence" made Extra
    High rank generic SQL above the AI skills it then told the user to
    learn first.
16. **Label every number as published or estimated.** Add: "In tables,
    mark each number as published (with link) or your estimate." *Why:*
    the runs that did this were easiest to act on; the ones that did not
    put guesses in tables that read as facts.
17. **Point to non-obvious sources.** Name the less obvious places worth
    checking for the topic: pricing and rate-card pages, deprecation
    notices, system cards, parliamentary answers, statutes, live examples
    (for hiring questions, 2 or 3 live ads per market). *Why:* the most
    valuable finds came from exactly these, not from the main help page.
18. **Rule budget: keep prompts simple.** Pick at most 2 of rules 10 to
    17 per prompt, the ones that match its main risk (rules question: 11
    and 12; risk question: 14; ranking: 15; anything you will decide on:
    10). Keep the prompt at about 400 to 600 words with no more than about
    6 rule lines in total. An add-on should replace a weaker line, not pile
    on. Checks that need no instruction (source dates, published vs
    estimated numbers, negative claims) are done by the grader or the
    reader instead. *Why:* every extra instruction competes for the
    model's attention, so more rules mean each one is followed less
    reliably, and the long B1 prompt (about 1,400 words) caused the hangs
    and drift. **Known flaw:** rules 10 to 17 have not been tested as
    prompt lines. They come from what went wrong in B3, not from a run
    that showed adding them helps. If results get worse or runs slow down,
    suspect prompt length first. Test with and without them in the next
    benchmark.

## Behavior: which mode for which job (current verdict)

**Hard rule: never use ChatGPT Deep research. No exceptions.** In 8 runs
over three benchmarks it ran `deep-research-mini`, scored lowest on every
task type (lists, product facts, legal rules, legal risk), stated stale
facts as current and cited few sources. Reopen only if the user asks and
the model label stops saying "mini". (OpenAI's help page says Deep research
uses "the latest model by default" but names none; its Enterprise rate card
lists `o4-mini-deep-research`. Checked 9 October 2026.)

The options are ChatGPT Chat at Extra High, ChatGPT Chat at 6 Pro, and
Claude Research (model and effort chosen). Evidence: B1 to B3, one run per
mode per question, so gaps under about 5 points may be noise.

### The two ChatGPT modes have different styles, not different quality

Their overall scores are close (B3: 85 vs 83). The useful difference is
how each works:

| | Chat 6 Pro: the careful one | Chat Extra High: the explorer |
|---|---|---|
| Precision (B3 re-grade, 12 to 15 claims checked per run) | 100% on all four questions (57 of 57 checks right) | 88 to 100% |
| Habit | Says less, checks more, hedges when unsure | Says more, commits to a view, sometimes overreaches |
| Wins when | Overreach is costly (detailed official rules) | Committing is rewarded (realistic odds, judgment calls) |
| Fails by | Over-hedging: marks things "unknown" that evidence supports | Overclaiming: a route that does not apply, a ranking that contradicts its own advice |
| Method | One consistent dataset or method; digs into odd official corners (rate cards, statutes) | More, and more varied, sources (press, independent tests); finds leads others miss; weaker at turning them into one consistent answer |
| Speed and cost | About 7 to 9 min (slim prompt); scarcest allowance | About 5 to 7 min; lighter allowance |

They reach different parts of the web: in B1 their company lists shared
only 83 of 207 names. For important decisions, running both and merging is
likely better than either alone (hypothesis, not yet tested).

### Claude Research

- **Precision:** 79 to 93% of checked claims right, below 6 Pro (100%)
  and close to Extra High.
- **Most efficient at new findings:** 0.8 to 1.3 minutes per verified
  point no other run had, the best of any mode. Sonnet at Medium covered
  the most of the legal-risk checklist (11 of 12) and found the real
  dilemma none of the ChatGPT runs named.
- **Its failure is specific:** it states a rule correctly, then drops the
  rule's condition (a deadline, a status) in the headline, and it trusts a
  single official line for "there is no X". On the permit question both
  runs made the same decision-changing error this way. That is a
  reasoning and checking failure, not a search failure: it read 128 to 313
  sources a run. Prompt rules 11 and 12 target it.
- **Weaker source mix:** more blogs, wikis and document-sharing sites.
- **Model:** split result. Opus Low won the rules question (69 vs 65),
  Sonnet Medium won the risk question (87 vs 83). No clear winner.
- Untested: higher effort, and any discovery or list task.

### Running two modes on one question

- A second run adds facts and depth, rarely coverage. Same-provider pairs
  (6 Pro plus Extra High) added 0 to 1.5 checklist items of 12.
- The only pair that covered a full checklist mixed providers (Extra High
  plus Claude Sonnet). Mixed pairs look more complementary (one data
  point).
- When every run misses the same thing, a second run will too. A targeted
  follow-up prompt on the gap is worth more than another full run.
- Pairs bring conflicts to resolve ("no route" vs "there is a form").
  Check those live.

### Cost of each option

- **ChatGPT:** no short rolling window. 6 Pro has a weekly cap OpenAI does
  not publish (press: 100 a week on new Pro $200 plans). On Pro $100, 6 Pro
  shares one weekly allowance with GPT-5.6 Sol Pro; on Pro $200, hitting the
  cap switches to GPT-5.6 Thinking at Medium. Extra High is lighter and has
  no published cap. Plus gets neither Extra High nor 6 Pro in Chat. (OpenAI
  help, checked 9 October 2026; details and links in the
  mode report (private, not published).)
- **Claude:** a 5-hour rolling usage window on top of a weekly limit. One
  Research run at Low uses about 5 to 15% of the window (sometimes 20%)
  and can take up to an hour under load; Medium or High adds roughly 20
  to 50% (user estimates, 9 October 2026). Many Claude runs can block the
  user's other Claude work for hours, so ask before proposing more than
  one or two.

### Choosing a mode (fit guide)

Starting fit scores (0 to 100) for the mode-fit report. Adjust for the
specific prompt and say why.

| Task type | Extra High | 6 Pro | Claude Research (Opus Low) |
|---|---|---|---|
| Decision on detailed official rules (legal, immigration, tax) | 75 | 90 | 70 (watch dropped conditions) |
| Risk or judgment ("realistic odds") | 90 | 75 (over-hedges) | 85 (most new angles) |
| Discovery: lists, leads, companies | 85 | 85 | 50 (untested) |
| Ranked list backed by data | 80 | 90 | 55 (untested) |
| Current product or market facts | 80 | 85 | 60 (freshness risk) |
| Quick fact check | 85 | 60 (overkill) | 40 (window cost) |

**The prompt matters more than the mode.** Before blaming a mode for
hanging, check whether the prompt has a finish line.

## Behavior: the benchmark side capability

Benchmarks are **optional**. The default flow writes prompts only. At the
"how many prompts" step the skill also offers: "Run a quick benchmark
first?" A benchmark:

1. Uses one prompt, identical bytes, in each chosen mode, in one project
   per benchmark. Names chats `<code>-<MODE>` (for example `B3-PRO`).
2. Records for each run: send time, finish time, model labels (from the
   conversation data), whether it stalled (no change for 15 minutes), plan
   completion, output size, row count, unique sources.
3. Exports every result (routes in the chatgpt-browser export reference)
   to one Downloads folder per benchmark.
4. Scores each run 0 to 100 on six common categories: accuracy (spot
   check about 8 to 10 claims against live pages or an answer key),
   self-checking, discovery (items others missed), source quality,
   following the brief, usefulness. Also, written BEFORE the runs, 2 to 4
   question-specific criteria (for example "covers each decision point in
   the answer key", "uses data from the last 12 months", "likelihoods
   match the evidence"). Speed, allowance and reliability come from run
   data. For more nuance, also measure: precision (correct claims out of
   claims checked) versus unique correct points; overclaims versus
   over-hedges; worst error and its severity (would it change a
   decision); freshness; source mix; coverage of a decision-point
   checklist written before reading any run; minutes per unique point;
   a style profile; and a merge test (coverage of each pair of runs).
   Grading checks that proved their worth: check negative claims ("there
   is no X") first; for the 2 or 3 claims that drive the decision, check
   the reasoning, not only that the link exists; open each run's main
   source and look for what it left out; check that summaries keep the
   body's conditions; do not count citations as quality. An answer key
   ages: re-check every disagreement live, and list what the key does not
   cover so good extra content earns credit. Note when a run used account
   memory (it is then not blind). Report the full category table per
   question, a category-average table per mode, and one strength and one
   weakness per run. Never report only an overall number: it hides where
   modes differ.
5. Appends a dated entry to `BENCHMARKS.md`: setup, numbers, scores,
   lessons, and any rule or verdict it changes. Then updates this spec and
   the skill if a rule or verdict changed, and `STATE.md`.
6. Keeps personal topic details out of this shared spec. Personal results
   stay in a private repo.

**Interpreting results:** two runs per mode on one task type is a strong
first read, not a ranking. Re-test a verdict on a new task type before
generalising it. Do not trust a model's description of its own internals
as evidence (for example "6 Pro uses sub-agents"); test behavior instead.

## Non-goals

- Proving backend model identity beyond ChatGPT's own labels.
- Automating benchmarks end to end; a human picks topics and modes.
