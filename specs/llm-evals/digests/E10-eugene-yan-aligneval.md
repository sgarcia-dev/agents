---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [E10]
purpose: One-source digest feeding the spec compendium.
---

# AlignEval: Building an App to Make Evals Easy, Fun, and Automated (E10)

**What it is:** Eugene Yan's article, published 2024-10-27. A 14-minute read with screenshots, code, a development checklist, and embedded demos. [Original article](https://eugeneyan.com/writing/aligneval/).

**Capture status:** Full, according to the capture frontmatter. Main article, code blocks, task lists, further reading, and citation were captured and compared against independently fetched HTML. The file links to images and videos; it does not contain video transcripts or the text inside screenshots. No missing article content is declared.

## The point in three sentences

Start by inspecting real model outputs and labeling them, rather than inventing evaluation criteria in advance. Write a simple pass/fail evaluator, meaning an LLM that judges another model's output, and measure its agreement with your human labels. Improve it on a development subset, then check it on unseen test examples before trusting the improvement.

## Key ideas

- Human expectations need calibration too. Criteria should reflect actual outputs and recurring defects, rather than assumptions about what models ought to do. Quote: "calibrate human criteria to AI output" (Align AI to human. Calibrate human to AI. Repeat.).
- Generic criteria can distract from useful checks. Yan criticizes broad helpfulness scores, rare spelling defects, and expectations beyond the technology's abilities. Quote: "evaluating actual defects that occur with moderate frequency" (Align AI to human. Calibrate human to AI. Repeat.).
- Keep the review data simple and traceable. The CSV pairs context with generated output and uses an identifier to connect judgments back to the original example. Quote: "Lets you match labeled and evaluated samples to your data" (Getting started: Upload some data, `id` description).
- Begin with human inspection. Binary means only two possible judgments, pass or fail; Yan argues this makes labeling quicker and less demanding. Quote: "In labeling mode, our only job is to look at the data." (Labeling mode: Look at the data).
- Do not confuse the interface's minimum with enough evidence. Evaluation opens after 20 labels, but Yan recommends seeing more examples before defining criteria. Quote: "I suggest aiming for 50-100 before writing criteria and running evals." (Labeling mode: Look at the data).
- Judge one dimension at a time. Start with a short definition of pass and fail, then refine it by inspecting the evaluator's explanations and predictions. Quote: "Evaluate on a single dimension and return either 0 (pass) or 1 (fail)." (Evaluation mode: Write criteria, evaluate the evaluator).
- Supply only the fields the judgment needs. Factual checks usually require input and output; tone or style checks can use output alone. Quote: "Focusing solely on the output reduces token cost and latency while potentially improving performance." (Evaluation mode: Write criteria, evaluate the evaluator).
- Measure the judge against human labels. The app reports sample size, precision, recall, F1, Cohen's κ, and correct or incorrect positive and negative counts. The capture names these measures but does not explain their formulas. Quote: "evaluate our LLM-evaluators against the labeled data" (Evaluation mode: Write criteria, evaluate the evaluator).
- Repeated runs can produce different scores. Yan attributes this to stochasticity, meaning variation in model responses, and recommends more labels for stability. Quote: "the metrics can fluctuate a lot, even when we rerun the same LLM-evaluator" (Evaluation mode: Write criteria, evaluate the evaluator).
- Separate improvement from testing. The development set is the subset used to improve the evaluator; the test set is unseen data used to check the result. Quote: "the improved LLM-evaluator is evaled on the unseen test set" (Optimization mode: Semi-automated improvements 🤞).
- Small splits can mislead. Overfitting means improving on development examples without carrying that improvement to new examples. Quote: "the LLM-evaluator may overfit on the dev set and fail to generalize to the test set" (Optimization mode: Semi-automated improvements 🤞).
- Collect varied examples that resemble real use. Yan calls for both pass and fail labels, varied inputs and outputs, and examples similar to production data. Quote: "To be representative is to be similar to real-world examples." (Optimization mode: Semi-automated improvements 🤞).
- Cheap evaluators are worth considering, but the claim is task-specific. Yan chose small models for binary judgments and a free app. Quote: "good enough for binary classification LLM-evaluators" (Behind the scenes: How AlignEval was built).
- Make the evaluator's response easy to parse. The implementation uses a schema, meaning a declared output shape, for gpt-4o-mini and XML tags for claude-3-haiku. Quote: "define the desired output schema using Zod (JavaScript) or Pydantic (Python)" (Behind the scenes: How AlignEval was built).

## How to do it (concrete steps, checklists, templates)

The article's workflow, in order:

- Upload a CSV with `id`, `input`, `output`, and `label`. `input` is the context supplied to the generating model. `output` is its result. Labels use **0 for pass and 1 for fail**. If needed, use the linked `fib50.csv` sample from the Factual Inconsistency Benchmark.
- Compare input and output and label examples as pass or fail. Keep an open mind and delay formal criteria until familiar with the data. Evaluation mode unlocks at 20 rows; Yan recommends 50-100 labels before writing criteria and evaluating.
- Write criteria for one dimension. The described starting prompt uses two sentences defining pass and fail. Its actual wording appears in a screenshot, not in the captured text, so it cannot be reproduced here.
- Select `gpt-4o-mini` or `claude-3-haiku`. Select both input and output for context-dependent checks, or output only when sufficient.
- Click Evaluate. Inspect explanations, predictions, and the displayed metrics. Refine criteria after reviewing the results. Aim for at least 50 labels, which also unlocks optimization.
- Click Optimize. The app splits labels into development and test sets. It runs `n` trials to improve F1 on development data, keeping the chosen model and fields, then evaluates the improved judge on unseen test data. F1 is a classification score combining precision and recall; the source gives no formula or target score.
- If development and test scores diverge, label more diverse, representative data. The article also suggests combining scores from several evaluators, called an ensemble. It does not specify an aggregation rule.

The text describes the optimization loop, but does not give its internal prompt-generation algorithm, a value for `n`, or a full implementation recipe.

## Tools, code and commands named

- Evaluation app and repository: [AlignEval](https://aligneval.com/), [eugeneyan/align-app](https://github.com/eugeneyan/align-app). The capture includes an update saying it is integrated with LangSmith; the linked integration article is not captured here.
- Models: `gpt-4o-mini`, `claude-3-haiku`, planned `claude-3.5-haiku`, and `gpt-4` in the PoLL comparison. No model snapshot identifiers are supplied.
- Data and research: `fib50.csv`, Factual Inconsistency Benchmark, PoLL, Llama2, and Who Validates the Validators. The article explicitly says optimization is not `dspy`.
- Frontend choices tried: FastHTML, Next.js, SvelteKit, FastAPI + HTML. The selected stack uses TypeScript and Next.js, with Python + FastAPI behind it. Cursor helped with implementation.
- Output handling: OpenAI structured output, Zod, Pydantic, `EvaluationResponse`, `explanation`, and `prediction`. The JavaScript code restricts the prediction string to `'0'` or `'1'`; the shown Python class declares only `prediction: str`, without the same restriction.
- Claude's prompt requests reasoning inside `<sketchpad>` and a binary result inside `<prediction>`. Those are prompt-defined XML tags, rather than the schema approach shown for OpenAI.
- Hosting and storage: Railway, SQLite, Postgres, Redis. Alternatives discussed include Dokku, Coolify, Vercel, and Hetzner. Exact deployment commands: `railway link`, then `railway up`.
- Development checklist names `label-app`, `label-hpo`, `definitions.ts`, `data.ts`, `actions.ts`, `component.tsx`, `ui`, and `page.tsx`. Stripe payment buttons remained unfinished. No framework or library versions are given.

## Numbers and strong claims

- **14 minutes:** Article reading time, shown near the title.
- **20 labels:** Unlock evaluation. **50-100 labels:** Author's recommended preparation before writing criteria. **At least 50 labels:** Unlock optimization and improve score stability. These are app thresholds and practical advice, not demonstrated universal sample requirements (Labeling mode; Evaluation mode).
- **50 articles, two summaries each:** Description of the sample data, one summary factually consistent and the other inconsistent (Getting started).
- **F1 0.571 → 0.722 at development trial 5 → 0.727 on test:** One reported optimization example. The initial score's split is not specified in the prose (Optimization mode).
- **25 examples per split, 50 total:** The small-data example used to explain development/test disagreement (Optimization mode).
- **Three smaller evaluators beat gpt-4:** Reported PoLL result. The capture does not supply benchmark details or establish that this applies to arbitrary tasks (Optimization mode).
- **99.9% XML success:** Yan's experience-based claim, without a denominator or test method in the capture. Treat as anecdotal (Behind the scenes).
- **2-3x faster component work and bug fixes with Cursor:** Author's experience, not a controlled productivity result (Behind the scenes).
- **One to two minutes per Railway update:** Author's deployment experience (Behind the scenes).
- **Binary labels are faster and more accurate:** Author's argument with supporting links, but no measured comparison in this capture (Labeling mode).
- **Small models are cheap, fast, and sufficient:** Task-specific author opinion. No prices, latency table, or evaluation results for these model choices are provided (Behind the scenes).
- **Easy, fun, automated:** Promotional framing in the title. The workflow still requires human labels, criteria, and checking. The optimization section describes an early beta and leaves its mechanism mostly unspecified.

## Compared with the deep research report

Only the report's section 2.4 about this source was read.

- **Right:** The report describes "collecting human labels, defining criteria, and aligning automated evaluation with those labels". The source's opening sequence includes "Look at the data and label samples as pass or fail." Both correctly put human review inside the workflow. The report's approximately 14-minute estimate matches the capture.
- **Right:** The report says "Your frontend background is directly useful here." The source describes "my first TypeScript app" and a Next.js frontend. This is a reasonable fit assessment, rather than a measured result.
- **No clear factual error:** The report's short summary is supported. Its heading "Best visual, application-building walkthrough" is an editorial ranking; this capture cannot establish that it is best among resources.
- **Adaptation should be explicit:** The report's exercise proposes "output and tool evidence on the other" side of a worker review screen. The source describes "a comparison between input and output fields". Tool traces, explanations attached to human decisions, and agent acceptance review are additions by the report.
- **Left out:** The report does not mention the recommendation to label 50-100 examples before defining criteria, or the single-dimension restriction. Source: "Evaluate on a single dimension" (Evaluation mode).
- **Left out:** Development/test separation, small-sample variation, and overfitting receive no treatment in section 2.4. Source: "the improved LLM-evaluator is evaled on the unseen test set" (Optimization mode). These matter even if the user never builds a review interface.
- **Left out:** Output-only judging, schema differences, cheap model choices, and the unspecified optimization mechanism. The report highlights the interface more than these practical constraints.

## Fit for the user's agent workspace

- (inference) Copy the data-first sequence for bounded workers. Review actual task packets and outputs before deciding which recurring failures deserve automated checks.
- (inference) Adapt `id`, `input`, `output`, and `label` into a small review dataset. Use the identifier to find the corresponding worker run. Preserve the article's 0=pass, 1=fail convention consistently.
- (inference) Use separate judgments for job completion and staying in scope. The source's single-dimension rule argues against collapsing these into one vague quality score.
- (inference) Include task instructions and relevant evidence when judging completion or scope. Reserve output-only checks for properties that can be judged from the response itself.
- (inference) Compare a cheap judge against human labels before adopting it. Treat the named models as choices described in this article, rather than a current model recommendation.
- (inference) Keep unseen cases for checking prompt improvements. A higher development score alone should not decide whether a worker evaluator is ready.
- (inference) Start with a CSV and simple review view; adapt the Next.js interface if review becomes cumbersome. The article does not require adopting its full hosting stack.
- (inference) Add a separate cost assessment for the question of whether a worker was worth its cost. This source discusses evaluator token savings, but does not provide worker cost accounting, task-value measures, or agent tool-use evaluation.

## Best parts to read or watch first

Times below are estimated reading budgets, not durations supplied for individual sections.

- **Align AI to human. Calibrate human to AI. Repeat.**, about 2 minutes. Read for the reason to delay criteria until after inspection.
- **Labeling mode** and **Evaluation mode**, about 3 minutes together. Read for thresholds, binary decisions, field selection, and checking the judge.
- **Optimization mode**, about 2 minutes. Read for development/test separation and why small splits can mislead.
- **Behind the scenes**, schema snippets and model selection, about 2 minutes. Useful for implementing parseable evaluator responses in TypeScript or Python.
- The embedded **AlignEval: A app that makes evals fun, easy, and semi-automatic** demo is linked in Optimization mode. The article says it labels 50 rows. Duration and timestamps are not available in the capture, so no viewing-time estimate or transcript-based recommendation can be given.
