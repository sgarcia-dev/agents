---
created_at: 2026-10-09
updated_at: 2026-10-09
model: claude-opus-5-5
doc_type: benchmark_log
purpose: Dated log of every hosted-research benchmark run, with numbers, scores and lessons.
related:
  - path: ./spec.md
    why: Rules and verdicts these runs support.
  - path: ./STATE.md
    why: Planned runs and next action.
---

# Browser deep research benchmark log

Newest first. Each entry: setup, numbers, scores, lessons, what changed.
Personal topic details and full reports are kept in a private repo.

## Planned (not run yet)

- **Claude Research at higher effort** (High or Extra) on one sensitive
  question, to see whether effort closes the gap with 6 Pro.

## Round 3 field notes, 2026-10-09 to 10 (not a benchmark)

A real overnight run, not graded: 15 prompts (4 Chat 6 Pro, 10 Chat Extra
High, 1 Claude Research), all kept to the short prompt shape.

- **Short prompts held up.** No run looped or stalled. Every Extra High
  run finished, most in 10 to 20 minutes.
- **Chat modes gave route prices, not group totals.** Three fare prompts
  (one per month, for a group, one way) returned only per-adult
  prices for single legs. A browser run on a flight search site gave
  totals for the whole group on every day checked. For group fares, use
  the search site; use research prompts for the rules.
- **A same-provider check would have missed a timing rule.** The Claude
  cross-check ranked first a route that the 6 Pro run showed breaks an
  airline's transfer-time limit, because Claude did not check the
  schedule. Give rules questions the schedule or numbers to test against.
- **Runner pitfalls:** Send clicks can do nothing in a hidden tab; ChatGPT
  replaces custom chat titles once a run finishes (track runs by
  conversation id, not title); Extra High still often has two end-turn
  messages (export the first).

## B3, 2026-10-09 17:36 to 18:00: four task types, five modes

**Task:** four slim prompts (254 to 406 words, 20-minute target, full https
link per claim, no scripts), one project per provider:
- Q1 product facts: how ChatGPT's research modes differ (docs first, label
  DOCUMENTED / TESTED / INFERENCE).
- Q2 ranked list: 10 to 15 most in-demand AI skills for a senior front-end
  engineer, ranked by demand evidence.
- Q3 single detailed rules question (a multi-step official
  process timeline), with an existing answer key.
- Q4 risk question (realistic consequences), partial
  answer key.
ChatGPT ran all four in Chat 6 Pro, Chat Extra High and Deep research at
Extra High (12 runs). Claude Research ran Q3 and Q4 on Opus 5.5 Low and
Sonnet 5.5 Medium (4 runs). Scored by four Opus 5.5 medium scorers, 8 to
10 live spot checks each.

**Overall scores (0 to 100)**

| Question | Chat 6 Pro | Chat Extra High | Deep research | Claude Opus low | Claude Sonnet med |
|---|---|---|---|---|---|
| Q1 product facts | 88 | 83 | 32 | n/a | n/a |
| Q2 ranked list | 89 | 83 | 35 | n/a | n/a |
| Q3 legal rules | 82 | 76 | 25 | 68 | 63 |
| Q4 legal risk | 82 | 88 | 25 | 86 | 83 |
| Average | 85 | 83 | 29 | 77 | 73 |

**Category averages per mode** (ChatGPT over Q1 to Q4, Claude over Q3
and Q4 only, so compare Claude with care)

| Category | Chat 6 Pro | Chat Extra High | Deep research | Claude Opus low | Claude Sonnet med |
|---|---|---|---|---|---|
| Accuracy | 89 | 85 | 36 | 78 | 73 |
| Self-checking | 91 | 86 | 31 | 79 | 79 |
| Discovery | 80 | 84 | 24 | 79 | 78 |
| Source quality | 88 | 85 | 26 | 78 | 72 |
| Following the brief | 84 | 80 | 41 | 85 | 80 |
| Usefulness | 83 | 83 | 28 | 78 | 74 |
| Average run time | 7.7 min | 6.1 min | 6.6 min | 5.8 min | 7.2 min |

**Character of each mode**
- 6 Pro: most careful (best self-checking and sources); can over-hedge
  and mark things "unknown" that evidence supports.
- Extra High: best discovery; finds what others miss; looser on the brief
  (long answers, leaked UI markup once, a ranking that contradicted its
  own advice, overreached on one legal route).
- Claude Opus Low: best at following the brief and plainest to act on;
  deep quotes; but stated two rules confidently and wrongly.
- Claude Sonnet Medium: most new angles on the risk question; weaker
  sources (wiki, document-sharing sites), one stale item.
- Deep research: low on everything; worst on sources; labelled stale
  facts as documented.
- Shared blind spot: no run covered the two biggest decision points in
  the Q3 answer key. The generic rubric did not measure coverage, which is
  why question-specific criteria were added to the procedure.

**Numbers:** every run finished in 5 to 10 minutes; none stalled. 6 Pro
6 to 9 min, 20 to 53 distinct links. Extra High 5 to 7 min, 10 to 25
links. Deep research 5.5 to 9.5 min, 10 to 19 links, model label
`deep-research-mini` again. Claude 5 to 7.5 min, 128 to 313 sources read,
26 to 37 cited.

**Lessons**
- Slim prompts made every mode fast. The long runs in B1 were the prompt.
- Deep research failed on every task type, including the single questions
  it was supposed to suit: stale 2025 facts presented as current, a wrong
  tax rule, a misread queue, "Strong" evidence that was a staffing blog.
- 6 Pro and Extra High are close (85 vs 83). Extra High won the legal-risk
  question; 6 Pro won where detailed official rules mattered.
- Claude Research read 10 times more sources but did not score higher.
  It repeated an outdated rule from the shared answer key that 6 Pro and
  Extra High corrected. First pass: Opus Low beat Sonnet Medium on both
  questions (the re-grade below splits them).
- A benchmark with an answer key also audits the key: Q3 found a stale
  claim in the user's own notes, confirmed against official records.
- Export notes: Extra High chats can hold a second, partial end-turn
  message (export the first, complete one); 6 Pro text carries citation
  markers to convert from `content_references`; Deep research plan-step
  statuses can look stale even when the report is complete, so do not use
  them to say it "stopped early".
- OpenAI's own docs still recommend Deep research for broad lists. Our
  tests disagree for this account.

**Re-grade (same evening, rubric v2).** Four Opus scorers re-read all 16
reports: 12 to 15 claims checked per run, a decision-point checklist
written before reading, overclaims vs over-hedges, worst error, source
mix, freshness, minutes per unique point, a merge test of every pair.

| Measure | Chat 6 Pro | Chat Extra High | Deep research | Claude Opus low | Claude Sonnet med |
|---|---|---|---|---|---|
| Precision (claims checked right) | 100, 100, 100, 100% | 90, 88, 93, 100% | 40, 20, 42, 40% | 88, 93% | 79, 93% |
| Checklist coverage (of 12) | 9, 11, 9.5, 10 | 9, 10, 10, 10.5 | 4, 3, 3, 4.5 | 8.5, 9 | 8, 11 |
| Overclaims / over-hedges (sum) | 0 / 7 | 4 / 4 | 25+ / 0 | 4 / 1 | 4 / 2 |
| Decision-changing errors | 0 | 0 | 4 (one per question) | 1 (Q3) | 1 (Q3) |
| Minutes per unique verified point | 1.0 to 1.7 | 0.6 to 1.4 | 5.6 or n/a | 1.0 to 1.3 | 0.8 to 1.2 |
| Re-graded overall | 91, 89, 82, 83 | 87, 83, 80, 90 | 31, 35, 25, 28 | 69, 83 | 65, 87 |

ChatGPT columns list Q1, Q2, Q3, Q4; Claude columns Q3, Q4.

What the re-grade added:
- 6 Pro made no wrong claim in 57 checks. Its only failure type is
  omission and over-hedging (6 of 14 risks marked "unknown" on Q4).
- Extra High found the most new sources but was weaker at turning them
  into one consistent answer (Q2 ranking), and once used ChatGPT account
  memory (knew a date the prompt never gave).
- Claude was the most efficient at new findings; Sonnet Medium covered
  the most of the Q4 checklist (11 of 12). Both Claude runs made the same
  decision-changing error on Q3: a correct rule with its deadline dropped
  in the headline.
- Merge test: 6 Pro plus Extra High added 0 to 1.5 checklist items. The
  only full-coverage pair was Extra High plus Claude Sonnet (Q4). On Q3
  every pair capped at 10.5 of 12, because the prompt never asked about
  the two biggest trade-offs.
- Three of five runs said "there is no expedite route"; an official
  route exists. Negative claims were the riskiest claim type.
- The answer key was wrong once and missing a whole topic (tax) once.

**Changed by the re-grade:** spec prompt rules 10 to 17, Claude and
pairing sections, fit guide tweaks, grading checks; skill prompt checklist
and pairing advice.

**Changed:** spec verdict table (Deep research "do not use", Claude row
added, allowance note), skill mode table and Claude effort note, chatgpt-
browser export reference (three export pitfalls).

## B2, 2026-10-09 15:01 to 15:28: slim company list (G1 v2)

**Task:** list 20 to 40 big-name tech companies hiring in two
target regions. 7 columns, one source per row, about 20 minutes,
"deliver what you have" rule, no scripts, answer in the reply. About 500
words (B1 was about 1,400). New project.

| | DR at Extra High | DR at Pro | Chat Extra High | Chat 6 Pro |
|---|---|---|---|---|
| Time | 14 min | 11 min | 22 min, no stall | 20 min, no stall |
| Report model label | deep-research-mini | deep-research-mini | gpt-6-thinking | gpt-6-pro |
| Plan finished | No (step 2 of 5) | No (step 2 of 5) | n/a | n/a |
| Rows | 10 | 4 | 24 | 25 (5 marked Watch) |
| Unique source links | 11 | 4 | 0 (placeholders) | 76 |
| Spot check | not checked | not checked | 1 of 3 right, 2 roles closed | 5 of 6 right, 1 closed (already flagged) |
| Names not in B1 | 1 | 0 | 13 | 7 |

**Lessons**
- The slim shape fixed the long runs and the stall: 6 Pro 65 to 20
  minutes, Extra High stall to 22 minutes.
- 6 Pro stayed accurate with real links.
- Extra High's source column came out as unresolved placeholders like
  `<Link url={turn362330view0.url.uri}>`. They could not be mapped back to
  URLs from the conversation's search results (different id format).
- Both Chat runs listed outsourcing firms; the slim prompt had dropped the
  exclusion. Extra High drifted to small, non-big-name firms.
- Asking for "ideally a current posting" made models chase postings;
  closed postings made rows stale. Root cause of the drift, found after
  the run with the user.
- Deep research did not improve and returned fewer rows.

**Changed:** spec rules 4, 5 and 6; skill notes on keeping filters.

## B1, 2026-10-09 08:58 to about 10:30: big company list (G1 v1)

**Task:** list 100+ big-name tech companies "as complete as possible",
11 columns (including culture, office policy and recent news),
a dated and labeled link for every claim, 8 sections, "length is wanted,
do not cut short". About 1,400 words. Four modes, one project.

| | DR at Extra High | DR at Pro | Chat Extra High | Chat 6 Pro |
|---|---|---|---|---|
| Time | 10 min | 7 min | about 41 min, then stalled with no reply | 65 min 32 s |
| Report model label | deep-research-mini | deep-research-mini | gpt-6-thinking | gpt-6-pro |
| Plan finished | No (steps 3 to 5 skipped) | No (steps 4 to 5 skipped) | report built, reply never sent | yes |
| Rows | 4 plus an "(others)" filler | 43, about 15 with real evidence | 140 | 150 |
| Sources | 8 unique | 10 unique | 202 records, 253 links | 498 records, 603 links |
| Spot check | 2 of 2 wrong | 4 of 4 wrong | 4 of 5 right, 1 role closed | 8 of 9 right, 1 understated |

**Scores (0 to 100, list task)**

| Category | Chat 6 Pro | Chat Extra High | Deep research |
|---|---|---|---|
| Accuracy | 90 | 60 | 20 |
| Checking its own claims | 90 | 55 | 20 |
| Finding new or unusual leads | 70 | 85 | 25 |
| Source quality | 90 | 55 | 20 |
| Following the brief | 80 | 50 | 20 |
| Reliability | 85 | 50 | 45 |
| Speed | 50 | 65 | 85 |
| Allowance (assumed) | 30 | 65 | 60 |
| Overall for list research | 85 | 65 | 25 |

Scores cover B1 and B2 together. Allowance is assumed, not checked.

**Lessons**
- Deep research effort setting had no effect on the report model.
- Deep research stopped early and stretched few sources (one Indeed page
  cited for 10 companies), with factual errors (an acquisition that did not
  happen, wrong headquarters).
- The Deep research page header said "0 citations, 0 searches" although
  the report had citations. Do not trust that header.
- Both Chat runs built scripts and source databases. Extra High looped on
  self-verification and stalled; its finished file was recovered from the
  chat workspace.
- The two Chat lists overlapped little (83 shared of 207 total), so a
  second Chat sweep adds real value.
- The conversation data can lag a running chat by many minutes; check the
  live page too.

**Changed:** slim prompt shape (spec rules 1 to 3, 7, 8); runner checks
at about 25 minutes and a 15-minute stall rule; export routes documented.
