---
created_at: 2026-10-13
model: gpt-6.1-sol (medium)
doc_type: digest
source_ids: [E13, E13z]
purpose: One-source digest feeding the spec compendium.
---

# Eval Skills (E13, with archived E13z)

**What it is:** A repository of Markdown procedures for coding agents building application-specific LLM evaluations. The archived README names Shreya Shankar and Hamel Husain as joint maintainers of the successor. Individual capture frontmatter lists author and publication date as unknown. Captured 2026-10-13. This packet contains two READMEs, nine skill files and one review-loop reference, 1,600 lines including capture metadata. Allow roughly 45–65 minutes to study the packet, an estimated reading time. [Maintained repository](https://github.com/ai-evals-course/evals-skills); [archived predecessor](https://github.com/hamelsmu/evals-skills).

**Capture status:** All twelve captures say full, obtained through `gh-api-raw`. Eleven say capture notes: none. E13z records GitHub archived status as true and the redirect to the maintained repository. No missing text is declared. Linked papers, videos, course content, images, and other repository files are outside this packet.

## The point in three sentences

Read complete runs and let a knowledgeable human discover concrete failures before writing automated checks. Use code for rules that can be checked directly, and a narrowly focused model judge for rules requiring interpretation. Test that judge against separate human-labeled examples before trusting its decisions or reported success rates.

## Key ideas

- Start from the user's situation. `evals-start` routes existing pipelines to audit, unlabeled traces to discovery, known failures to code or judges, and absent traces to synthetic input generation. Quote: "This file holds only routing." (`evals-start`, closing paragraph.)
- Discovery precedes evaluator design. A trace is a record of the input, intermediate work, tool calls and output; reviewing it reveals failures specific to the application. Quote: "You should only write evals after doing this step." (Maintained README, The error-discovery skill.)
- The human supplies judgments; the agent organizes them. During discovery, reviewers highlight text and leave notes without choosing predefined categories. Quote: "No quality labels, no dropdowns, no structured forms. Free-text notes only." (`error-discovery`, Phase 3, Content view design.)
- Alternate broad coverage with detailed inspection of a discovered failure. The agent revisits old records because the reviewer's understanding changes, called criteria drift. Quote: "Agent suggestions are not ground truth." (`review-loop`, Depth mode.) Suggestions require human acceptance or dismissal.
- Discovery sampling is for finding different failures. Combine cluster representatives, examples near the center of groups of similar records, with random picks. Quote: "The goal is discovering failure modes, not estimating how common they are." (`error-discovery`, Phase 4.)
- Review design depends on the task. The separate `build-review-interface` skill collects whole-trace Pass/Fail labels, notes and uncertain cases; it differs from span-based discovery. Quote: "Trace-level annotation (not span-level) as the default" (`build-review-interface`, Design Checklist.)
- Human-readable presentation matters. Render prose, code, tables and tool calls in their natural forms while retaining the whole trace. Discovery specifically warns against hiding potentially important messages by role. Quote: "Do not mute content by role." (`error-discovery`, Phase 2, Opacity / saturation.)
- Write one code check per objective failure. Return both its result and reason, test known good, bad and borderline cases, and inspect mistakes on actual traces. Quote: "Choose the check from the failure rule." (`write-code-eval`, after Examples.)
- Each model judge needs one criterion, binary definitions, labeled examples and structured output. A few-shot example is a labeled demonstration included in the prompt. Quote: "Each judge checks exactly one thing." (`write-judge-prompt`, opening.) The critique comes before the verdict and should cite concrete evidence.
- Separate prompt examples from development and final measurement. Data leakage means letting the examples used to teach or tune the judge also determine its reported performance. Quote: "Any example used in the judge prompt must be excluded from dev and test sets." (`write-judge-prompt`, Rules for selecting examples.)
- Measure both directions of judge error. TPR is the fraction of human Pass labels the judge also passes; TNR is the fraction of human Fail labels it also fails. Quote: "Run the judge **exactly once** on the held-out test set." (`validate-evaluator`, Step 6.) A held-out set is reserved for final measurement.
- Correct aggregate rates for measured judge errors. Rogan-Gladen correction estimates the underlying pass rate from the observed rate and test-set TPR/TNR; a confidence interval gives a range of uncertainty. Quote: "A point estimate alone is not enough." (`validate-evaluator`, Step 8.)
- Synthetic inputs should vary along plausible failure-prone dimensions. Have the user approve combinations first, then generate natural-language queries in a separate step. Quote: "Dimensions (Step 1) must target anticipated failures, not arbitrary variation." (`generate-synthetic-data`, Prerequisites.)
- RAG, retrieval-augmented generation, retrieves documents before producing an answer. Evaluate finding the right documents separately from using them correctly. Quote: "Fix retrieval first." (`evaluate-rag`, Prerequisites.)
- Audit actual evidence and keep it current. Inspect failure analysis, evaluator design, judge validation, human review, labeled data and pipeline hygiene. Quote: "Re-run error analysis after every significant change." (`eval-audit`, Pipeline Hygiene.)

## How to do it (concrete steps, checklists, templates)

These are separate workflows. Route to the relevant one rather than executing every skill in sequence.

### Route and audit

1. Match the situation using `evals-start`; tell the user the chosen skill and why. If no row clearly fits, ask.
2. For audit, gather traces, evaluator configurations, prompts, labels and experiment results. Use a connected observability MCP server, a bridge to monitoring tools, or local files.
3. Inspect the six areas in their listed order: error analysis, evaluator design, judge validation, human review, labeled data, pipeline hygiene.
4. Report problems by impact. For each, give a title, Status (`Problem exists`, `OK`, or `Cannot determine`), a short specific explanation, and Fix referencing an action or skill. Omit areas without problems.
5. If nothing exists, obtain real traces or generate inputs and run the full pipeline. Complete error discovery before recommending evaluators or dashboards.

### Discover failures interactively

1. Inspect 5–10 records across the dataset. Identify fields, content type, message roles, logical groups and dimensions that vary. Consider plausible failures without imposing a fixed taxonomy, a list of failure categories.
2. Design the visual encoding before coding. Use color for categories, spacing for hierarchy, typography for content type, and containers for related tool calls and results. Mute only redundant content.
3. Build a single-file HTML app served by Python `http.server`. Provide content, map and progress views, inline notes, aligned margin notes, distinct agent suggestions, autosave and a `localStorage` backup.
4. Extract and normalize suitable features. Use KMeans or similar, targeting 6–10 clusters. For datasets over 50 records, choose 15–25 initial items: about 60–70% cluster representatives and 30–40% random samples. Remove duplicates.
5. Start the server, open the app and explain reviewing. Monitor `error_discovery_data/annotations.json` by reading and comparing content every two seconds. Use Claude Code's Monitor tool with `persistent: true`, or a background polling script and log elsewhere. Do not use filesystem events.
6. Read all annotations after changes. Assign notes to modes, maintain `{mode_name: {description, count, example_ids, example_quotes[]}}`, publish patterns and track coverage.
7. After about five distinct human-annotated records, the source prescribes one background subagent per failure mode to scan all records. Give it the definition and example quotes; collect `{record_id, text, start, end}` suggestions. Revisit reviewed records and add suggested unreviewed records to the sample. Humans confirm every suggestion.
8. Add samples from coverage gaps plus random picks. Encourage re-review as criteria change. Report confirmed and suggested counts separately, coverage, and whether new failures are still appearing. Suggest stopping or narrowing focus when discoveries slow.

For a non-interactive run such as `codex exec` or `claude -p`, build and smoke-test the app, stop the server and provide a later launch command. Do not claim the human review loop ran or the server remains running. These instructions describe the captured workflow; no review session was run for this digest.

### Collect labels in a separate review interface

1. Load JSON/CSV traces and display one at a time in native formats. Make all intermediate steps accessible, even when collapsed. Strip raw HTML before rendering and disable markdown images if they could track reviewers.
2. Add Pass, Fail, Defer, notes, navigation, a trace counter, ID lookup and autosave to CSV/SQLite/JSON. Add category controls only after categories are established. Keep sampling in a separate script; start with random sampling.
3. Implement shortcuts: arrow keys navigate; `1` passes; `2` fails; `D` defers; `U` undoes; `Cmd+S` saves; `Cmd+Enter` saves and advances.
4. Use Playwright screenshots to inspect layout, readability and responsiveness. Test labels and notes, defer, buttons and shortcuts, counter updates, persistence after reload and access to collapsed content.

### Generate missing test inputs

1. Identify likely failures from user knowledge, feedback or traces. Start with three application-specific dimensions.
2. Draft 20 combinations, called tuples, and revise with the user until realistic.
3. Use an LLM to generate more combinations without duplicates; the provided prompt requests ten at a time.
4. In a separate prompt, turn each combination into a realistic query using an application description and hand-written example.
5. Reject awkward, mismatched or repetitive queries. Optional realism scoring uses 1–5 and discards below 3.
6. Run queries through the full pipeline and save complete traces. Aim roughly for 100 diverse traces, then discover failures.

For real data, this skill recommends grouping by dimensions and sampling each group. Use synthetic data to fill underrepresented groups, and avoid it when nobody can judge realism.

### Write and validate evaluators

For code: state the observed failure rule and required fields, implement in the project's language/framework, return a result and reason, then test known and borderline cases. If the check substitutes for human judgment, compare against human labels.

For a judge:

1. Establish one failure mode from error analysis. Obtain at least 20 human Pass and 20 human Fail examples. Exhaust code checks first.
2. Define the task and explicit Pass/Fail boundary. Add clear Pass, clear Fail and borderline examples from training data only.
3. Enforce output containing `critique` before `result`, with `result` restricted to Pass or Fail. Supply only the context needed for this criterion.
4. Start with the most capable available model; reduce cost after alignment is established. If the task prompt omitted the desired instruction, fix the prompt before adding a judge.

For validation:

1. Obtain about 100 domain-expert labels, roughly half Pass and half Fail. Split into training 10–20%, development 40–45%, and test 40–45%. Training supplies prompt examples; development supports repeated tuning; test remains unseen.
2. Run on development data. Compute TPR and TNR separately, then inspect every disagreement. False Pass means excessive leniency; False Fail means excessive strictness.
3. Adjust definitions, training examples or edge rules; split broad criteria if needed. Repeat until stable, targeting both rates above 90%, with both above 80% as the stated minimum.
4. Run once on test data. Record final TPR/TNR. If further work is needed, use new development data rather than tuning to this test set.
5. For an aggregate production rate, apply `theta_hat = (p_obs + TNR - 1) / (TPR + TNR - 1)`, where `p_obs` is the observed judge Pass fraction. Clip to [0, 1]; the correction is invalid near a zero denominator.
6. Compute a bootstrap confidence interval, repeatedly resampling validation examples, or use `judgy`. Pin dated model versions and revalidate after prompt/model changes or unexpectedly wider intervals.

### Evaluate retrieval separately

1. Read end-to-end traces and identify retrieval versus generation failures.
2. Pair realistic questions with relevant document chunks. Curate manually, generate fact/question pairs from chunks, or create harder questions using similar chunks as distractors. Retain synthetic questions rated 4–5 for realism.
3. Measure first-pass Recall@k, the fraction of relevant documents retrieved among the first k results. For reranking, ordering retrieved candidates, use Precision@k, the relevant fraction of those results; MRR, how early the first relevant result appears; or NDCG@k, which rewards useful results higher in the list.
4. If retrieval limits performance, test chunk size/overlap combinations and re-index each time. Use natural boundaries and add title/heading context where fixed sizes split related information.
5. Evaluate generation faithfulness to retrieved context and relevance to the question. For questions needing two chunks, measure whether both appear in the first k results and classify which retrieval step missed.

## Tools, code and commands named

- Maintained installation: `npx skills add https://github.com/ai-evals-course/evals-skills`; one skill: `npx skills add https://github.com/ai-evals-course/evals-skills --skill error-discovery`; updates: `npx skills check`, `npx skills update`.
- Archived commands, historical only: `/plugin marketplace add hamelsmu/evals-skills`, `/plugin install evals-skills@hamelsmu-evals-skills`, `/plugin update evals-skills@hamelsmu-evals-skills`, and `/evals-skills:error-analysis`. E13z also lists installation from its old URL. Its banner redirects to the maintained URL.
- Python stdlib `http.server`; HTML; JSONL/CSV/JSON; CSV/SQLite/JSON label storage; `localStorage`; `marked.js`; `highlight.js`; Prism via CDN; Playwright; KMeans; K-means; PCA or UMAP, methods producing a two-dimensional map.
- Discovery files: `samples.json`, `annotations.json`, `graph.json`, `patterns.json`, `suggestions.json`, all under `error_discovery_data/`. GET and POST endpoints for `/api/samples`, `/api/annotations`, `/api/patterns`, `/api/suggestions`; GET `/api/graph` and `/`.
- Phoenix, Braintrust, LangSmith, Truesight; OpenAI `response_format`; Anthropic tool definitions; Instructor; Outlines.
- `sklearn.model_selection.train_test_split`, `sklearn.metrics.confusion_matrix`, NumPy; `pip install judgy`; `from judgy import estimate_success_rate`. The split code uses `random_state=42` and produces approximately 15%/45%/40%.
- Metrics explicitly named include ROUGE, BERTScore, cosine similarity, embedding distance, Cohen's Kappa, TPR/TNR, Recall@k, Precision@k, MRR, NDCG@k and Two-hop Recall@k. No concrete dependency or model versions are specified; validation requests a dated snapshot such as `<model>-<YYYY-MM-DD>`.

## Numbers and strong claims

- The maintained README cites experience helping 50+ companies and teaching thousands of students (opening). This is promotional background, not evidence of skill effectiveness.
- Discovery's 6–10 clusters, 15–25 samples and 60–70%/30–40% mix are operational defaults (Phase 4). About five annotated records precede the first scan (`review-loop`, Depth mode). These are procedural heuristics.
- About 100 traces is a rough saturation target, where new examples stop revealing new failure categories (`generate-synthetic-data`, Step 6; `eval-audit`, Labeled Data). Validation requests about 50 Pass and 50 Fail; below 60 labels, intervals are said to become wide (`validate-evaluator`, Practical Guidance). These are source guidance, not universal guarantees.
- Typical prompts use 2–4 demonstrations; performance is said to plateau after 4–8 (`write-judge-prompt`, Rules for selecting examples). No supporting experiment appears in the capture.
- Both TPR and TNR above 90% are targets, above 80% the stated minimum (`validate-evaluator`, Step 5). The example corrects 400 judge passes among 500 runs from 80% to 85% using TPR 0.92/TNR 0.88 (Step 7). Its bootstrap defaults to 2,000 resamples for a 95% interval (Step 8).
- "Improving TPR narrows the confidence interval more than improving TNR." (`validate-evaluator`, Practical Guidance.) This is a strong claim without supporting derivation or experiment in the capture. Its displayed denominator contains both rates symmetrically; the text does not establish this comparison.
- Retrieval suggests k=1–2 for factual lookups and k=5–10 for synthesis (`evaluate-rag`, Choosing k). Its chunk-size table uses 128/256/512 tokens and overlaps up to 256; it is labeled an example search grid, not a reported benchmark.
- "LLMs can ignore irrelevant content but cannot generate from missing content." (`evaluate-rag`, Retrieval Metrics.) Treat this as the source's rationale for prioritizing recall, not proof that irrelevant context is harmless.

## Compared with the deep research report

Only E00 section 3.3 was read for this comparison.

- Right: the report describes "validating evaluators against human labels". The validation skill explicitly says "Calibrate an LLM judge against human judgment." It also correctly identifies discovery as an interface-assisted process where the user supplies judgments.
- Right: its archival caveat says the older repository "is archived and redirects readers to the maintained repository above". E13z capture notes confirm archived status; its README says "This repository is deprecated."
- Right, with limits: the report says "This is not a replacement for an evaluation runner". The files provide procedures and small code examples, not a captured general-purpose runner. The maintained README places "production monitoring, regression suites, and cost" beyond these skills.
- Overstated as starting guidance: the report names discovery, judge writing and validation as "The most relevant starting points". The current README instead says "**evals-start** is the entry point." Judge writing requires discovered failures and human labels; validation requires an existing judge. The trio is useful to study, but not three interchangeable entry points. No other direct factual error is evident in this section.
- Left out: the code-check route. The source says "Exhaust code-based options before reaching for a judge" (`write-judge-prompt`, Prerequisites). This matters for an engineer who can implement schema and execution checks.
- Left out: distinct review modes, sampling for discovery rather than prevalence, re-review, human confirmation of suggestions, and the non-interactive stopping rule. The report's phrase "supply the judgments and explanatory notes" captures the principle but omits the workflow.
- Left out: split proportions, both error rates, correction and uncertainty, model pinning, synthetic input review and RAG diagnosis. The source's "A point estimate alone is not enough" adds a practical limit absent from the report.

## Fit for the user's agent workspace

- (inference) Copy the routing table into an evaluation entry procedure. Start with exported worker traces; use synthetic tasks only when real examples are missing or leave coverage gaps.
- (inference) Adapt objective checks to observed failures such as malformed outputs, forbidden file changes or missing required evidence. Use the project's TypeScript tools, as `write-code-eval` requests the project's language and framework.
- (inference) Let the root organize your review notes into a provisional list of failures. Keep discovery notes separate from later criterion-specific Pass/Fail labels, and keep agent suggestions unconfirmed until you review them.
- (inference) Adapt the source's one-subagent-per-mode scan to your bounded worker policy. Give a scanning worker a small record slice and clear failure examples rather than unrestricted authority over the corpus. The captured workflow's agents propose annotations; they do not define acceptable work independently.
- (inference) Use narrow validated judges for failures such as an explanation failing to support its conclusion. Measure catching bad work and retaining good work separately, then compare cheaper judge options after validation.
- (inference) Preserve model versions and separate prompt, development and test examples in plain-text workspace records. Re-run discovery after changing worker instructions or models because old checks may miss new failures.
- (inference) Add cost and latency tracking separately to decide whether a worker was worth its cost. The README names cost as outside these skills; this packet supplies no worker-value formula or ready-made budget evaluator.
- (inference) Use RAG evaluation only where workers retrieve workspace documents. Distinguish failure to fetch the relevant instruction from failure to follow an instruction already available.

## Best parts to read or watch first

Estimated reading times, not source-provided durations:

- Maintained README, Why skills for evals, then `evals-start` routing table: 3–4 minutes. Establish where to begin and avoid the archived entry instructions.
- `error-discovery`, Phases 1 and 4, then `review-loop`, The two modes and Key principles: 5–7 minutes. Learn what humans do, how samples are chosen, and why earlier records get revisited.
- `write-code-eval`, complete file: 1–2 minutes. The shortest practical route for objective failures.
- `write-judge-prompt`, The Four Components and Anti-Patterns: 5–7 minutes. Read before writing a subjective judge.
- `validate-evaluator`, Steps 1–7 and Practical Guidance: 7–10 minutes. Prioritize splits, separate error rates and final measurement; inspect Step 8 code when implementing aggregate reporting.
- `build-review-interface`, Feedback Collection and Testing: 3–4 minutes. Useful when moving from discovery to labeled validation examples.
- If document retrieval matters, `evaluate-rag`, Retrieval Metrics and Diagnosing Failures by Metric Pattern: 4–6 minutes.

The README links Shreya's walkthrough, but this packet contains no video capture or duration. It cannot support a timestamp-based viewing recommendation.
