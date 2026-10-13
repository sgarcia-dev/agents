---
created_at: 2026-10-09
updated_at: 2026-10-09
model: claude-opus-5-5
doc_type: decisions
purpose: Durable choices for hosted-research prompts, mode choice and benchmarks, with rejected alternatives.
related:
  - path: ./spec.md
    why: The rules these decisions produce.
  - path: ./BENCHMARKS.md
    why: Evidence behind each decision.
---

# Decisions

## 2026-10-09: bound every research prompt

- **Decision:** ranges, a time target and a "deliver what you have" rule in
  every prompt; list prompts 20 to 40 items. The user agreed that giving up
  some completeness is the price of usable, finishing runs.
- **Why:** B1 runs hung or ran long; the user has seen this many times on
  ChatGPT and Claude. B2 proved the fix.
- **Rejected:** keeping "as complete as possible" and fixing only the mode
  choice (B2 showed the prompt mattered more than the mode).

## 2026-10-09: company-level evidence for company lists

- **Decision:** when the user picks companies, ask for company-level
  evidence, not job postings.
- **Why:** the user never asked for roles; postings caused drift, slow runs
  and stale rows. Live roles are found separately.

## 2026-10-09: Chat at 6 Pro is the default for list research

- **Decision:** 6 Pro by default; Extra High as an optional second sweep;
  Deep research not recommended for lists.
- **Rejected:** Deep research for wide sweeps (the old skill guidance). In
  four runs it used `deep-research-mini`, stopped early and used few
  sources.
- **Open:** whether Deep research fits single-question research (B3).

## 2026-10-09: benchmarks are a side capability, logged in this spec

- **Decision:** the skill's default stays "write the prompts"; a benchmark
  is offered, not run by default. Every run is logged in `BENCHMARKS.md`
  and may update the rules and verdicts here.
- **Why:** the user wants to keep tuning prompt shape and mode choice
  with evidence.
- **Rejected:** a log inside the skill (skills hold procedure, not growing
  evidence); logging in `ai-models/` (that folder holds API model data;
  these results are as much about prompt shape as about models).

## 2026-10-09: do not rely on a model's description of itself

- **Decision:** claims such as "6 Pro delegates to sub-agents" are not
  used as evidence; test behavior instead.

## 2026-10-09: Deep research is not used in this account

- **Decision:** do not recommend native Deep research for any task type.
- **Why:** B3 tested the task types it was meant to suit (product facts,
  single questions). It scored 25 to 35 on all four, behind every other
  mode, and always ran `deep-research-mini`.
- **Rejected:** keeping it for "single questions" (B3 Q3 and Q4 were
  exactly that, and it scored lowest).

## 2026-10-09: Claude Research is the cross-check, not the main run

- **Decision:** ChatGPT Chat 6 Pro runs the research; Claude Research
  repeats only critical or sensitive questions.
- **Why:** in B3, Claude (Opus Low, Sonnet Medium) read far more sources
  but scored 63 to 86, below or level with 6 Pro and Extra High.
- **Open:** Claude at higher effort is untested.

## 2026-10-09: never use ChatGPT Deep research (user rule)

- **Decision:** the user set this as a standing rule with no exceptions:
  never use or offer ChatGPT's Deep research mode.
- **Why:** lowest score on every task type in B1 to B3; always ran
  `deep-research-mini`.

## 2026-10-09: a scored mode-fit report before every pack

- **Decision:** after the size question, the skill scores each option
  (ChatGPT Extra High, ChatGPT 6 Pro, Claude Research) 0 to 100 for fit per
  prompt, with why, risk and cost, recommends one (or a split), and waits
  for the user's explicit choice.
- **Why:** the modes differ in style (careful vs explorer, plain legal
  answers) more than in overall score, and Claude's 5-hour rolling window
  makes each Claude run a real cost. The user wants to decide informed.
- **Rejected:** a fixed default mode with no report (hides the trade-off);
  asking with no recommendation (pushes the analysis onto the user).

## 2026-10-09: no more benchmark runs for now

- **Decision:** stop at B3. Re-scoring existing reports with the finer
  measures, Claude at higher effort, and repeat runs for noise are noted
  but not scheduled.
- **Why:** Claude runs cost the user's 5-hour window, and B3 answered the
  practical question (which mode for which job).
