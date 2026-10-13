---
created_at: 2026-10-13
model: gpt-6.1-sol (medium)
doc_type: digest
source_ids: [E06]
purpose: One-source digest feeding the spec compendium.
---

# AI Evals: Everything You Need to Know (E06)

**What it is:** Hamel Husain and Shreya Shankar's written reference, published September 18, 2026, modified September 21. It has 60 questions and about 18,017 words of main text. [Original FAQ](https://hamel.dev/blog/posts/evals-faq/).
**Capture status:** Full. The capture frontmatter reports all answers checked against raw HTML, no missing text spans, and both footnotes retained. Media are linked; scripts and styles are excluded.

## The point in three sentences

Look at real sessions before deciding what quality means or which tests to build. Turn recurring failures into cheap code checks or narrowly focused judges validated against human decisions. Keep reviewing new data, because products, users, and your own standards change.

## Key ideas

Each bold question below is also the location of its following verbatim quote.

### Getting Started & Fundamentals

- **What are AI Evals?** Product evals test the whole application against user needs. Public benchmarks only help select a starting model. Quote: "Each eval checks one behavior on relevant examples".

- **What is a trace?** A trace records the complete session across users, agents, tools, and retrieved data. Vendor definitions differ. Quote: "It includes every step across all agents".

- **What’s a minimum viable evaluation setup?** Start with one expert and a notebook or small review interface. Review 20-50 outputs for 30 minutes after significant changes. Quote: "not infrastructure".

- **How much of my development budget should I allocate to evals?** Treat evaluation as development work. Spend most effort understanding failures and justify costly judges by their value. Quote: "Expect most of your effort to go toward understanding failures".

- **Will today’s evaluation methods still be relevant in 5-10 years given how fast AI is changing?** Better models still need checks that they solve the right problem. Requirements become clearer through observing outputs. Quote: "you still need to verify they’re solving the right problem".

- **How do I make the case for investing in evaluations to my team?** Win support with real failures, their frequency, fixes, and avoided impact. Share an error log weekly or monthly. Quote: "Let results instead of methods lead the conversation".

### Error Analysis & Data Collection

- **Why is "error analysis" so important in AI evals, and how is it performed?** Error analysis means reviewing traces to discover failures. Write free-text notes, group related failures, count them, and refine the categories. Quote: "Do not skip error analysis".

- **Do I need a reference answer or rubric before annotating data?** A reference answer shows a correct response; a rubric lists judging criteria. Let both evolve after seeing real examples. Quote: "Writing a rubric before you review examples can get in the way".

- **Should I record problems that aren’t the model’s fault?** Record every problem affecting usefulness, including missing features. Diagnose causes after prioritizing problems. Quote: "write down anything that makes the product less useful".

- **How many examples do I need for an eval?** Separate discovery, evaluator validation, and repeatable test sets. Discovery starts with 100 diverse traces; judgment checks need 100-200 labels per failure. Quote: "Coverage determines the final size".

- **How do I surface problematic traces for review beyond user feedback?** Start with random traces, then stress tests if few issues appear. Use existing checks and unusual trace signals to guide further review. Quote: "create queries that deliberately test your prompt constraints".

- **How often should I re-run error analysis on my production system?** Repeat after major changes and incidents. Suggested cycles are 2-4 weeks with 100+ fresh traces, plus 10-20 outliers weekly. Quote: "Adjust frequency based on system stability and usage growth".

- **What should I do when my "gold" eval dataset becomes stale?** Refresh examples as users and products change. Reduce costly checks that stop finding problems; changed datasets break direct score comparisons. Quote: "its scores may no longer be directly comparable with older scores".

- **What is the best approach for generating synthetic data?** Define variation dimensions and write 20 combinations manually. Generate more combinations, turn them into queries separately, then run the actual system. Quote: "Synthetic data cannot tell you how common a failure is in production".

- **Are there scenarios where synthetic data may not be reliable?** Synthetic examples are risky for specialized documents, low-resource languages, high-stakes work, underrepresented groups, and cases you cannot validate. Quote: "synthetic data can mislead or mask issues".

- **How can I do evals when traces contain sensitive data?** Prefer permitted real traces, then authorized experts, then checked redaction or editing. Use synthetic data last. Quote: "There is no replacement for looking at real interactions".

- **How do I approach evaluation when my system handles diverse user queries?** Let observed failures determine evaluation priorities. Predetermined query categories can hide shared problems across very different requests. Quote: "let your system’s actual behavior guide where you invest evaluation effort".

- **How can I efficiently sample production traces for review?** Mix random sampling, clustering, unusual metrics, classifiers, and feedback. Active learning uses current labels to choose useful next examples. Quote: "Keep some random traces in every batch".

### Evaluation Design & Methodology

- **Why do you recommend binary (pass/fail) evaluations instead of 1-5 ratings (Likert scales)?** Prefer pass/fail over 1-5 ratings. Separate binary subchecks can show gradual improvements without ambiguous score boundaries. Quote: "Binary evaluations force clearer thinking and more consistent labeling".

- **How do I combine my evals into a single metric?** Report the share of examples passing every check, with drill-down by failure. Group by theme or release severity before considering complex weights. Quote: "An example passes only if it passes every check".

- **Should I practice eval-driven development?** Usually discover failures before writing evaluators. A precise, known constraint can justify writing its test before implementation. Quote: "Write evaluators for errors you discover, not errors you imagine".

- **Should I build automated evaluators for every failure mode I find?** Fix missing prompt instructions first. Use cheap assertions before building judges for persistent failures requiring repeated iteration. Quote: "Only build expensive evaluators for problems you’ll iterate on repeatedly".

- **What model or LLM should I use to build automated evals?** Use code for objective conditions and validated classifiers for judgment. Start with a capable judge, then measure cheaper alternatives against human labels. Quote: "First check whether you can test the condition with code assertions".

- **Can I use Jev for evals?** Jev is a classifier, like a pass/fail LLM judge. Validate it identically and compare accuracy, cost, and speed rather than assuming it is best. Quote: "No single classifier is best for every eval".

- **How do I know if I can trust my automated eval?** Keep training, development, and final test examples separate. Measure failure recall and correct passes; repeated development tuning can overfit. Quote: "Here, “positive” means an error is present".

- **What should I do when I can’t get my LLM judge to agree with human reviewers?** Inspect disagreements for unclear criteria, missing context, or bad labels before prompt tuning. Build one judge per specific failure. Quote: "we recommend building a separate judge for each type of failure".

- **Should I use "ready-to-use" evaluation metrics?** Generic quality scores can create false confidence. They can still guide exploration for human review. Quote: "they can still help you find traces to inspect".

- **Are similarity metrics (BERTScore, ROUGE, etc.) useful for evaluating LLM outputs?** Similarity scores usually miss product failures. They remain useful for retrieval and output diversity. Quote: "They have utility in domains like search and recommendation".

- **Can I use the same model for both the main task and evaluation?** Using the application model as judge is usually acceptable if held-out human labels show agreement. Try another model when alignment fails. Quote: "what ultimately matters is how well your judge aligns with human judgments".

- **How much context should I give a LLM judge?** Supply only evidence needed for the specific failure. Remove context one piece at a time to test its value; add trace-search tools only when necessary. Quote: "Do not give every judge the same full trace by default".

- **How do we evaluate a model’s ability to express uncertainty or "know what it doesn’t know"?** Test both answerable and unanswerable questions. Passing requires appropriate answers and refusals, rather than blanket refusal. Quote: "a roughly equal number of answerable and unanswerable questions is a good starting point".

### Human Annotation & Process

- **How many people should annotate my LLM outputs?** Give one domain expert final quality authority when practical. With multiple reviewers, label independently, discuss disagreements, revise rules, and relabel. Quote: "Then relabel affected examples".

- **How can I make AI outputs easier for people to evaluate?** Design outputs for verification: show intermediate facts, source links, and conflicting evidence. Reduce review friction and investigate careless approvals. Quote: "surface intermediate outputs users can check before a final result".

- **Should product managers and engineers collaborate on error analysis? How?** Engineers and product managers build shared context first. Then empower an expert to judge actual outcomes with visible evidence. Quote: "Has an appointment been made?".

- **Can I help with evals if I’m not a domain expert?** Non-experts can find obvious flow, logging, ambiguity, and interface problems. Observe expert reasoning and leave specialized judgments to them. Quote: "Watch what they check and which evidence they need".

- **How do I evaluate outputs in a language I don’t speak?** Translation alone cannot establish quality. Use a reviewer who understands language and cultural context; otherwise acknowledge limited assessment. Quote: "Translation often loses meaning".

- **Should I outsource annotation & labeling to a third party?** Keep core error analysis close to the product team. External help fits mechanical tasks, tasks without product context, or experts brought into the process. Quote: "you often break the feedback loop".

- **How do you review a trace that is really large?** Focus first on upstream failure and reveal details as needed. Extract relevant evidence with original locations and validate extraction with an expert. Quote: "Quality is more important than quantity".

- **What parts of evals can be automated with LLMs?** Use LLMs for proposed groupings, category mapping, prompt suggestions, and label analysis. Humans retain initial review, taxonomy validation, trusted labels, and root-cause judgment. Quote: "Use LLMs to scale what you’ve learned".

- **Should I stop writing prompts manually in favor of automated tools?** Manual prompt writing helps clarify requirements. Optimize automatically after trustworthy evals exist; optimizing known metrics does not discover new failures. Quote: "Good writing is good thinking".

### Tools & Infrastructure

- **Should I build a custom annotation tool or use something off-the-shelf?** The authors prefer custom review tools, with shared context and product-specific rendering. Large distributed annotation teams may justify existing platforms. Quote: "Build a custom annotation tool".

- **What makes a good custom interface for reviewing LLM outputs?** Render familiar outputs, show progress and hotkeys, support search and grouping, and surface likely failures with actions. Add only features worth their maintenance. Quote: "Keep your annotation interface minimal".

- **What gaps in eval tooling should I be prepared to fill myself?** Expect to supply pattern discovery, AI assistance, application-specific evaluators, and usable bulk export plus annotation write-back APIs. Quote: "Be prepared to build most of your evaluators from scratch".

- **What should an internal eval platform standardize across teams?** Standardize review, sampling, and evaluator validation processes. Let teams choose metrics and interfaces; start with one team and use case. Quote: "Comparing eval scores across projects only makes sense when the checks and test data are comparable".

- **What’s your favorite eval vendor?** There is no preferred vendor. The author commonly encounters Langsmith, Arize, and Braintrust and values support over feature comparisons. Quote: "I have no favorite vendor".

- **How should I version and manage prompts?** Version prompts with code in Git. Experiment through the actual application, using notebooks where Python access permits or an integrated environment otherwise. Quote: "versioned, reviewed, and deployed atomically with the application code".

- **What should go in the system prompt vs. the user prompt?** Try both placements experimentally. Put stable rules in system prompts and task data and examples in user prompts; prefer user prompts when unclear. Quote: "Move instructions between prompts and measure which produces better results".

### Production & Deployment

- **How are evaluations used differently in CI/CD vs. monitoring production?** Continuous integration and deployment tests catch known regressions on curated examples. Production monitoring samples live traces asynchronously and adds new failures back into regression tests. Quote: "track confidence intervals for production metrics".

- **How often should I run my evals?** Choose frequency from cost, whether tests still reveal failures, and business impact. Reproduce hypothetical failures before investing; try cheaper evaluators. Quote: "There are no bright-line rules".

- **What’s the difference between guardrails & evaluators?** Guardrails check in the response path and can intervene before users see output. Evaluators usually measure afterward; inline judges need acceptable latency and reliability. Quote: "they do not block the original answer".

- **Can my evaluators also be used to automatically *fix* or *correct* outputs in production?** Only evaluators meeting response-time, cost, and error-rate constraints should become production guardrails. Compare blocking good outputs with allowing bad ones. Quote: "Error Rate Trade-offs".

- **How much time should I spend on model selection?** Switch models when failure analysis identifies model limitations. Model selection is not the default first improvement. Quote: "Does error analysis suggest that your model is the problem?".

### Domain-Specific Applications

- **Is RAG dead?** Retrieval-augmented generation supplies relevant context. Criticism of naive vector retrieval for coding does not invalidate keyword, agentic, or hybrid search. Quote: "how to retrieve effectively".

- **How should I evaluate a coding agent?** Use public coding benchmarks for broad agents and product tests for narrow workflows. Build private tasks with working environments and executable tests, then add code-quality and interaction checks. Quote: "Each task needs a working environment and code-based tests".

- **How should I approach evaluating my RAG system?** Evaluate retrieval first with search metrics and query-document pairs. Then validate generation judges against human labels and add domain-specific failures. Quote: "debug retrieval first using IR metrics".

- **How do I choose the right chunk size for my document processing tasks?** For bounded answers, use a large relevant chunk with distraction caveats. For exhaustive extraction or summaries, process smaller sections then aggregate; tune experimentally. Quote: "global context for local focus".

- **How do I debug multi-turn conversation traces?** Judge the whole conversation, inspect user-visible failures first, then technical steps. Preserve cross-agent order and reproduce the simplest failure; test real conversation prefixes when needed. Quote: "Annotate only the first failure in the trace at first".

- **How do I evaluate sessions with human handoffs?** Trace through human resolution, not merely handoff. Record reasons, transferred context, waiting, human actions, and outcome; measure necessity, quality, and rate. Quote: "The trace continues until the user’s need is resolved or the session ends".

- **How do I evaluate complex multi-step workflows?** Log the complete workflow and measure outcome plus efficiency. Diagnose by stage and use a matrix of last success versus first failure to locate problems. Quote: "Early stage improvements have more impact since errors cascade in LLM chains".

- **How do I evaluate agentic workflows?** First measure end-to-end success, then diagnose steps in failing workflows. Check tools, arguments, results, changed state, authorization, retained constraints, milestones, and efficiency separately. Quote: "Also test authorization and preconditions".

## How to do it (concrete steps, checklists, templates)

These procedures preserve the source’s local order.

### Discover failures, then build evals

1. Gather representative session traces; generate synthetic inputs if real data is unavailable.
2. Review at least 30 traces yourself. Write open-ended notes, initially focusing on the first failure. This is open coding.
3. Group notes into distinct failure categories and count them. This is axial coding. Review the agent's proposed groups.
4. Let the agent find similar or informative traces. Accept or reject suggestions and refine categories until new reviews stop changing your understanding, called theoretical saturation. Start with roughly 100 diverse traces and continue while learning.
5. Fix obvious prompt and product bugs. Choose code checks for objective failures and judges for important, persistent judgment tasks.
6. Assemble repeatable examples covering workflows and confirmed failures. Add production discoveries over time.

### Validate a judgment-based evaluator

1. Collect trusted human pass/fail labels for one failure, usually 100-200 examples.
2. Split into training examples for the prompt, development examples for iteration, and an untouched final test. Suggested shares: 10-20%, 40-45%, and 40-45%. Aim for 30-50 passing and 30-50 failing examples in each development and test set when possible.
3. Inspect disagreements and fix missing evidence, labels, or unclear instructions before trying automated prompt tuning.
4. Track true positive rate, the fraction of actual failures caught, and true negative rate, the fraction of good outputs correctly passed. Here a positive means a failure.
5. Check the untouched test once development finishes. A much worse test result can indicate overfitting, learning tuning examples' peculiarities rather than the underlying rule. If overfit, revise and reserve a new untouched test.
6. Compare cheaper models after establishing agreement. Choose acceptable missed failures and false alarms according to their costs.

### Generate synthetic inputs

1. Define likely failures and useful dimensions of variation.
2. Write 20 tuples manually, each choosing one value per dimension.
3. Generate more tuples, then turn them into queries in a separate prompt. Use all combinations then filter when most are valid; generate directly when many are invalid.
4. Fix obvious prompt omissions, then run queries through the full system and review traces.
5. Compare with real data as it arrives. Synthetic cases do not estimate production prevalence.

### Diagnose agent workflows

1. Define a precise success rule and judge the complete outcome.
2. Record the first upstream failure; identify frequently failing workflows.
3. Diagnose steps: tool choice, arguments, error handling, retained constraints, efficiency, and milestones.
4. Check tool name, arguments, result, and resulting state separately. Verify permission and preconditions too.
5. Make a transition failure matrix: rows are last successful states; columns are first failing states. Investigate concentrations of failures.
6. Reproduce the smallest case that still fails. Use multiple turns only when context causes the problem; N-1 testing supplies real prior turns and tests the next response.

## Tools, code and commands named

- Benchmarks: GPQA Diamond, Terminal-Bench, MMLU, SWE-bench, Aider Polyglot, HumanEval. Conversation clustering research: Clio.
- Coding and interfaces: Claude, Codex, Claude Code, Cursor, Lovable, FastHTML. Analysis: Jupyter, Julius, Hex.
- Classifiers and tuning: Jev from TypeSafe, BERT, logistic regression, GEPA. Other metrics: BERTScore, ROUGE, cosine similarity, Cohen’s Kappa, Inter-Annotator Agreement (IAA).
- Retrieval: Recall@k, relevant documents found in the first k results; Precision@k, relevant share of those results; MRR, how highly the first relevant result ranks. Relationship checks: C|Q, context relevance to question; A|C, answer faithfulness to context; A|Q, answer relevance to question.
- Platforms and storage: Langsmith (also LangSmith), Arize, Braintrust, Git, GitHub, Desktop app. Linked plugin: ai-evals-course/evals-skills.
- Concrete examples: monitor watches annotations.json; cancel_order is checked alongside its order ID, success response, and changed state. N-1 testing replays conversation prefixes. No installation command or versioned SDK recipe is supplied.
- Scheduling examples: GPT-6 Astra on max reasoning and medium reasoning, Fable 5, GPT-6 Luna. These are illustrations, not model comparisons.

## Numbers and strong claims

- Introduction: questions come from teaching "5,000+ engineers and PMs". Promotional context. The authors call these "sharp opinions" and say "They are not universal truths".
- Minimum setup: 30 minutes reviewing 20-50 outputs after significant changes. Discovery: at least 30 manual annotations, roughly 100 diverse traces, and continue while learning. These are heuristics, not statistical guarantees.
- Budget FAQ: "60-80% of our development time" went to error analysis and evaluation. Practitioner experience, not a budget rule. Its 100% versus 70% pass-rate comparison argues for useful challenges, not a target score.
- Example-count FAQ: 100-200 labels per judge failure; split and class-count guidance appears above. Repeatable sets often grow to 100+ examples. These quantities serve different purposes.
- Review-frequency FAQ: 100+ fresh traces per cycle, commonly 2-4 weeks, plus 10-20 weekly. Adjust to stability, growth, changes, and incidents.
- Combined-score FAQ: 80 examples passing every check out of 100 yields 80%. An illustration, not a reported result.
- Judge-debugging FAQ: at least 50 passing and 50 failing examples recommended. Validation examples: 8 of 10 failures caught gives TPR 80%; 95 of 100 good outputs passed gives TNR 95%. No universal acceptable threshold is given.
- Custom-tool FAQ: "iterate ~10x faster" is an observation without study details. Its linked example handles 400+ results per query. Treat the speed claim as opinion.
- Tooling-gaps FAQ: 3x and 80% increases are illustrative patterns a tool might discover. Scheduling examples are also explicitly illustrative.
- Agent-workflow FAQ: 12 GenSQL → ExecSQL failures versus 2 DecideTool → PlanCal failures. Counts guide investigation; the text supplies no transition denominators for comparing failure rates.
- Advice against generic quality metrics, for one expert, and for custom tools is practitioner opinion. Preserve exceptions for retrieval metrics, multiple domains, and distributed annotators.
- Repeated 25% course-discount offers are marketing, separate from the method.

## Compared with the deep research report

Only section 1.4 about this FAQ was read for this comparison.

- Right: the report describes a "Free, extensive reference article" and says "Use this as a reference". The source offers curated paths and says "Browse the questions that interest you".
- Right: its summary includes "starting small, human review, binary versus numerical scoring" and guardrails. Its infrastructure takeaway matches "not infrastructure" in the minimum-setup answer.
- Wrong or overstated: no factual error is evident in this short section. Its instruction to "read the first three resources" is the report's reading-order advice; the source instead offers paths tailored to different needs.
- Left out: separate data stages, the first 30 manual reviews, one-failure judges, train/dev/test separation, TPR/TNR, and non-LLM classifiers. The source says "keep training, development, and test data separate to avoid overfitting" in the Jev answer.
- Left out: verification interfaces, evolving criteria, sampling limits, evaluator retirement, coding benchmarks versus narrow product tests, outcome checks, authorization, and transition matrices. The agent answer says "Also test authorization and preconditions". 

## Fit for the user's agent workspace

- (inference) Review real bounded-worker sessions yourself. Note incomplete work, scope breaches, missing checks, and avoidable effort; let observed failures determine categories.
- (inference) Give each run a trace ID and preserve ordered root, worker, and tool events. Include resulting files and verified outcome beside the final message.
- (inference) Use code assertions for objective packet requirements, file boundaries, schemas, and task outputs. Reserve validated judges for failures requiring judgment.
- (inference) Keep completion and authorization as separate checks. A correct edit can fail the packet if it touched an unauthorized file or skipped a precondition.
- (inference) Compare models on the same private tasks and environments. Measure outcome plus steps, seconds, tokens, and resource cost; this FAQ gives no formula for deciding whether a worker was worth its cost.
- (inference) A small TypeScript review interface could show packet, trace, diff, outcome evidence, labels, and notes together. Add hotkeys and filtering when they save time.
- (inference) Version prompts and examples with the workspace. Refresh tests as skills and expectations change; cross-harness scores need comparable checks and examples.

## Best parts to read or watch first

Times are rough digest-author reading estimates, not source-provided durations. Linked video durations are not captured.

- **Minimum viable setup**: about 1 minute. Starting point.
- **Error analysis** and **How many examples do I need?**: about 6-8 minutes. Failure discovery and separate data needs.
- **Trusting automated evals** and **Judge disagreement**: about 5-6 minutes. Validation, false alarms, and debugging.
- **Coding agents**, **Multi-turn traces**, and **Agentic workflows**: about 8-10 minutes. Most useful for bounded workers.
- **Good custom review interfaces**: about 3 minutes. Frontend opportunities.
