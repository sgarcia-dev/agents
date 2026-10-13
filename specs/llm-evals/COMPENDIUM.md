---
created_at: 2026-10-13
model: GPT-6 (reasoning effort not exposed)
doc_type: compendium
purpose: Teach application and agent evaluation through every captured source, with evidence, limits, and a practical learning path.
related:
  - path: ./spec.md
    why: Owns the evaluation requirements and serves as the planned topic entrypoint.
  - path: ./IMPLEMENTATION-GUIDE.md
    why: Companion guide for applying these lessons to the Agents workspace.
  - path: ./SOURCES.md
    why: Companion evidence ledger for source trust and capture status.
  - path: ./digests/
    why: Detailed source summaries used to prepare this synthesis.
---

# LLM and agent evals compendium

## 1. How to use this document

- Read the whole document in about 60–75 minutes; part 1 takes under a minute and part 2 about 3 minutes.
- Read part 3 in about 15 minutes as a glossary; read part 4 in about 10 minutes for the method.
- Read part 5 in about 7 minutes for agents and part 6 in about 4 minutes for source differences.
- Read part 7 in about 7 minutes for tools; scan part 8 in about 15 minutes to choose originals.
- Read part 9 in about 3 minutes for report corrections and part 10 in about 4 minutes for the learning path; these are estimates.

## 2. Evals in one page

An eval is a way to check whether an AI system does useful work. You give it a task, observe what happens, and decide whether the result meets the task's requirements. For someone who knows software testing, the familiar part is the input and the check. The less familiar part is that the same input can produce different answers, actions, and failures across runs. [E01 §The structure of an evaluation; E08 lesson 2]

A large language model, or LLM, generates responses from the instructions and context it receives. In an application, that model is only one part of the system. Your prompts, retrieved documents, tools, permissions, memory, and code affect the result. An agent adds a loop: choose an action, use a tool, inspect the result, and decide what to do next. Evaluate that whole combination when deciding whether a worker is useful. [E08 lessons 2–3; E11b §Why agent evals are different]

Keep three questions separate:

| Question | What you need | Example for a bounded worker |
| --- | --- | --- |
| What should it do? | A task contract with success rules and allowed actions. | Fix the named bug, edit the allowed files, and run the required checks. |
| What did it do? | A trace, the ordered record of messages, tool calls, results, and changes. | It read the packet, edited a file, attempted a check, and wrote a final message. |
| Was that OK? | A grader, the check that turns evidence into a judgment. | Independent tests pass, file scope was respected, and the explanation matches the evidence. |

The three-question framing comes from the starting report. Its application to workers is a proposed design. E01 supports the distinction between task, transcript, and outcome. A transcript records the run. An outcome is what actually exists afterward, such as a changed file or a database reservation. A claim of completion does not establish that outcome. [E00 §First, what you are trying to learn; E01 §The structure of an evaluation]

Start by reading actual runs. Write what went wrong in plain language. Then group repeated problems and choose what to fix. A vague helpfulness score can hide a concrete failure, such as offering a service the business does not provide. A factually accurate answer can also fail the user's goal. In the podcast's apartment example, saying no suitable apartment exists is accurate, but ending the conversation can lose a lead that should reach a human. [E03 00:17:18–00:24:38; E07 §The Error Analysis Process]

Use code when the rule is clear. Code can check valid JSON, file boundaries, test results, or a required value. Use a human when the standard is still being discovered. Use an LLM judge, another model that grades work, when a known criterion needs interpretation and repeated manual review is costly. That judge must be checked against trusted human labels. Model strength alone does not prove grading quality. [E06 §What model or LLM should I use to build automated evals?; E09 §Step 5]

For this workspace, three separate questions are useful: did the worker finish, did it stay within scope, and what did the accepted work cost? This is an inference from the sources, not a supplied worker framework. A correct artifact can accompany an unauthorized action. A cheap call can become expensive after failed attempts and retries. Keep those facts visible rather than hiding them in one quality number. [E00 §Compare configurations, not anecdotes; E06 §How do I evaluate agentic workflows?]

The useful loop is simple: inspect, define a failure, fix it, replay cases, and inspect again. Add automated graders where they help. Keep known successes as regression tests. Keep harder cases to expose capability limits. Sample fresh runs because an old test set cannot reveal every new failure. [E01 §Capability vs. regression evals and roadmap; E06 §Production & Deployment]

## 3. Glossary

Definitions below explain the technical terms used across this collection. Source IDs lead to the catalogue in part 8. Tool names are compared in part 7. A source can use a term differently; the label convention and convergence notes below are especially important.

### Systems, runs, and evidence

- **Application or product eval:** A check of the whole system against a user's task. It includes more than the base model. [E06 §What are AI Evals?]
- **Model benchmark:** A shared task set used to compare models. A good benchmark result does not establish that your application works. [E06 §Model benchmarks]
- **Agent:** A system that chooses actions, uses tools, and continues based on their results. Its surrounding code affects what it can do. [E01 §Introduction; E08 lesson 3]
- **Agent harness:** The runtime that gives the model tools, context, and an execution loop. An evaluation compares this runtime and the model together. [E01 §The structure of an evaluation]
- **Evaluation harness or runner:** Code that runs tasks, captures evidence, applies graders, and summarizes results. Promptfoo and Inspect are examples. [E01 §The structure of an evaluation]
- **Task or test case:** One input with success criteria and, for an agent, a starting environment. [E01 §The structure of an evaluation]
- **Trial:** One attempt at a task. Repeated trials can take different paths and have different outcomes. [E01 §The structure of an evaluation]
- **Suite or dataset:** A collection of tasks or examples used together. A suite also includes the checks applied to them. [E01 §The structure of an evaluation; E08 lesson 11]
- **Trace or transcript:** The record of a run's messages, actions, tool results, and intermediate work. Check the tool's definition because some traces cover only part of a session. [E06 §What is a trace?]
- **Span:** One recorded operation inside a trace. Spans can nest to show a tool call inside a larger agent run. [E08 lesson 5]
- **Session or thread:** The connected interaction across turns, sometimes across several agents. A shared ID helps reconstruct the whole interaction. [E06 §Multi-agent trace logging; E12 optional Phoenix assignment]
- **Outcome or state:** The result that exists in the environment after the run. A final message and an actual state change are separate evidence. [E01 §The structure of an evaluation]
- **Tool call and arguments:** A request to an external function and the values supplied to it. Choosing the correct tool can still fail if the arguments are wrong. [E08 lesson 7]
- **Router and skill:** The router selects work; a skill performs a capability, possibly using several code or model steps. This course use of skill differs from a Markdown SKILL.md procedure. [E08 lesson 3; E13 README]
- **Memory or shared context:** Information retained for later agent steps. Missing or wrong context can cause downstream failures. [E08 lesson 3]
- **Observability and instrumentation:** Observability lets you inspect internal behavior; instrumentation records it in code. Automatic model-call tracing and manual application spans can work together. [E08 lessons 5–6]
- **OpenTelemetry, OTEL, and OTLP:** OpenTelemetry supplies common tracing concepts and libraries; OTLP transports telemetry. [E08 lesson 5; F01c §Quick Start]
- **Trace context and traceparent:** Data passed between operations to connect them to the same trace. `traceparent` is the header used in the Promptfoo custom-provider example. [F01c §Instrument Your Provider]
- **Generation round versus protocol turn:** A model generation is one internal response; a client protocol turn can contain several generations. Counts from different runtimes need not mean the same thing. [F01c §Turn marker spans]
- **Multimodal:** Handling several forms of input, such as text, images, or audio. The captures describe media transport but do not supply a general media-quality rubric. [E11c §Handling Multimodal Content; E08 lesson 14]

### Learning from failures

- **Error analysis or error discovery:** Read runs, identify failures, group them, and investigate what caused them. Discovery finds what to measure before measurement estimates its frequency. [E06 §Error Analysis & Data Collection]
- **Failure mode:** A recurring kind of failure with a clear definition and examples. [E13 §write-judge-prompt]
- **Open coding:** Write free-form notes on observed problems before choosing categories. [E03 00:17:18–00:29:35; E16b]
- **Axial coding:** Group those notes into meaningful failure categories. Check model-proposed groups against the original notes. [E03 00:31:39–00:46:06]
- **Taxonomy:** The resulting set of named categories. It can change as review reveals new patterns. [E07 §The Error Analysis Process]
- **Annotation, label, and critique:** An annotation records a review; a label records the decision; a critique explains it. Preserve reasons so another reviewer can understand the standard. [E09 §Step 3]
- **Domain expert and benevolent dictator:** A person who understands the work and has final authority over ambiguous quality decisions. The phrase is advice to avoid needless committees, not a reason to ignore other user groups. [E03 00:27:16; E09 §Step 1; F01a §Phase 1]
- **Rubric or criterion:** A written rule for judging work. A criterion is one condition; a rubric can contain several. [E06 §Do I need a reference answer or rubric before annotating data?]
- **Ground truth or gold labels:** Trusted reference judgments used to check an evaluator. They can still contain mistakes or outdated requirements. [F01d §Bad Data and Labels]
- **Reference answer or solution:** A known acceptable answer or artifact. An executable reference solution also checks whether the task and graders are fair. [E01 roadmap Step 2]
- **Criteria drift:** The standard changes as people inspect outputs and understand their needs better. Update definitions and affected labels together. [E07 §Understanding Criteria Drift]
- **Theoretical saturation:** More review stops revealing useful new failure types. It is a stopping heuristic, not proof of full coverage. [E03 00:29:39–00:31:33]
- **Upstream failure and error cascade:** An earlier mistake causes later failures. Start there when diagnosing a multi-step run. [E16e 00:01:00; E06 §How do I debug multi-turn conversation traces?]
- **Transition failure matrix and heatmap:** A table of last-success and first-failure pairs; a heatmap uses color to show counts. Counts suggest where to inspect, but do not prove a cause. [E12 HW5; E16e]
- **Slice or dimension:** A subset defined by a relevant property, such as task type or scenario. Comparing slices helps locate failures hidden by a total score. [E09 §Step 6]
- **Clustering:** Grouping similar records to find varied examples to inspect. An automated cluster can miss an important distinction. [E13 §error-discovery; E16f 00:10:05]
- **K-means, PCA, UMAP, and t-SNE:** Methods named for grouping or displaying records. K-means groups records; the others are used for lower-dimensional views, and this collection does not establish a best choice. [E13 §error-discovery; E16f]
- **Random, targeted, and active sampling:** Random sampling gives broad checks; targeted sampling seeks known risks; active sampling uses current labels to choose informative examples. Keep some random examples to catch blind spots. [E06 §How can I efficiently sample production traces for review?]
- **Prevalence:** How common a failure is among the runs you care about. A deliberately difficult test set cannot establish production prevalence. [E06 §What is the best approach for generating synthetic data?]
- **Selection bias:** A sample differs from the population in a way that distorts conclusions. Voluntary feedback and selected failed traces are examples to watch. [E08 lesson 7; E12 HW5]
- **Dogfooding:** Using your own product and learning from it. It is especially useful when the developer is also the domain expert. [E03 01:09:57–01:18:23]
- **Capability funnel:** Stages from basic function to solving the user's whole problem. Executing a query is a lower bar than returning useful results. [E07 §Experiments vs. Features]

### Graders, validation, and statistics

- **Grader or evaluator:** A check that assigns a decision or score to evidence. Code, models, and humans can each fill this role. [E01 §Types of graders for agents]
- **Code-based or deterministic eval:** Code applying an explicit rule. Deterministic means it repeats the same result on the same input, not that its rule is correct. [E01 §Types of graders; E13 §write-code-eval]
- **LLM-as-judge or model-based eval:** A model applies grading instructions to another system's output or trace. Validate it against the human standard it should follow. [E09 §Step 5]
- **Classifier:** A system assigning examples to labels, such as Pass and Fail. LLM judges, Jev, and traditional classifiers still need validation. [E06 §Can I use Jev for evals?]
- **Binary versus Likert scoring:** Binary uses two decisions, usually pass/fail; a Likert scale uses ordered ratings such as 1–5. The method sources prefer clear binary criteria with explanatory text. [E06 §Why do you recommend binary evaluations?]
- **Partial credit and continuous score:** Partial credit records completed parts; continuous scoring permits values within a range. Neither automatically represents a probability. [E01 roadmap Step 5; E14 §Trajectory LLM-as-judge]
- **Unknown or Defer:** A separate status when evidence or judgment is insufficient. Keep it distinct from a confirmed pass. [E01 roadmap Step 5; E13 §build-review-interface]
- **Critique shadowing:** Teach a judge from an expert's explanations and compare its decisions with that expert. Review and repair the application throughout the process. [E09 §Recap of Critique Shadowing]
- **Few-shot and zero-shot:** Few-shot prompts include labeled demonstrations; zero-shot prompts apply instructions without those examples. [E09 §Start with Expert Examples; E06 §Can I use Jev for evals?]
- **Train, development, and test sets:** Train examples can teach the prompt; development examples guide revisions; hidden test examples check the final version. Here train need not mean updating model weights. [E09 §How do you validate an LLM judge against human labels?]
- **Held-out and unseen data:** Data reserved from prompt examples or tuning. State which kind of separation applies. [E09 §Step 6 and validation FAQ]
- **Data leakage or test contamination:** Teaching or tuning with examples later used to claim independent performance. Even noticing a test mistake can shape the next prompt. [E13 §write-judge-prompt; E16c 00:19:44–00:22:37]
- **Overfitting and generalization:** Overfitting improves familiar examples without helping new ones; generalization is carrying the learned rule to new examples. [E10 §Optimization mode]
- **Confusion matrix:** A table crossing human labels with judge predictions. It shows correct decisions and both error directions. [E03 00:58:21–01:00:48]
- **True positive, true negative, false positive, and false negative:** Correct and incorrect decisions for the class called positive and its opposite. Name the positive class before using these terms. [E06 §How do I know if I can trust my automated eval?; E13 §validate-evaluator]
- **TPR and TNR:** True positive rate measures correctly identified positives; true negative rate measures correctly identified negatives. E06 makes errors positive, while E13 and E12 HW3 make passes positive, so their operational meanings reverse. [E06 validation answer; E13 validation Step 3; E12 HW3 §Key Metrics]
- **Failure recall and good-output acceptance:** The fraction of actual failures caught and the fraction of good outputs passed. These plain names avoid confusion over positive labels. [Synthesis of E06 and E13]
- **Accuracy or raw agreement:** The fraction of all decisions matching reference labels. An always-pass judge can score highly while missing every rare failure. [E03 00:58:54–00:59:10; E09 validation FAQ]
- **Precision, recall, and F1:** Precision asks how many flagged cases are real; recall asks how many real cases were caught; F1 combines both. Specify which class is being measured. [E05b §Important Note on Using Agreement; E10 §Evaluation mode; F01d §Unverified Judges]
- **Cohen's kappa and inter-annotator agreement:** Measures used to compare reviewers or labels. Sources disagree about whether kappa belongs in judge validation; E13 reserves it for human reviewers. [E10 §Evaluation mode; E13 validation Step 3]
- **Calibration or alignment:** Checking and improving agreement with the intended human standard. In these guides it does not mean a model's probability estimates are calibrated. [E07 §Maintaining Trust In Evals]
- **Confidence interval:** A range expressing uncertainty around an estimate. It does not cover every missing task type or future change. [E16c 00:56:27–01:00:18]
- **Bootstrap:** Repeatedly resample observed examples to estimate variation. Its usefulness depends on what the original data represents. [E16c 00:49:22–00:58:08]
- **Stratified split and class imbalance:** A stratified split preserves label proportions; imbalance means one label is much more common. Check both label counts in every validation split. [E16c 00:09:19–00:15:32]
- **Observed and corrected success rate:** Observed rate counts judge passes; corrected rate accounts for measured judge errors. They are different quantities. [E12 HW3 §Key Metrics]
- **Rogan-Gladen correction:** The rate adjustment shown in E13 using observed pass fraction and test-set TPR/TNR. Its denominator must not be near zero, and it does not repair missing coverage. [E13 validation Steps 7–8; E16c]
- **pass@k and pass^k:** pass@k asks whether at least one of k attempts succeeds; pass^k asks whether all k succeed. The first measures chances to find a solution; the second measures consistency. [E01 §How to think about non-determinism]
- **Capability and regression evals:** Capability cases expose limits; regression cases protect established behavior. A solved capability case can later become a regression case. [E01 §Capability vs. regression evals]
- **Saturation of a suite:** Most solvable tasks already pass, so the suite has little room to show gains. Keep regression coverage and add useful harder cases. [E01 roadmap Step 7]
- **Convergence:** In E08, similarity of path lengths to the shortest observed completed path. In E09, agreement of judge and expert after iteration; these are different uses. [E08 lesson 9; E09 §Keep Iterating on the Prompt]
- **A/B test and experiment:** An A/B test compares product variants with users; an offline experiment replays examples through named system variants. [E05b §Level 3; E08 lesson 11]
- **Eval-driven development:** Using measured behavior to guide changes. Known exact rules can be tested first, while unknown subjective failures require discovery. [E06 §Should I practice eval-driven development?]

### Inputs, retrieval, runtime, and cost

- **Synthetic data:** Constructed examples rather than observed user requests. Generate realistic inputs, then run the actual system to obtain outputs. [E07 §Guidelines for Using Synthetic Data]
- **Dimensions, tuples, scenarios, and personas:** Dimensions vary meaningful properties; a tuple picks values; a scenario describes circumstances; a persona describes a user. These are design aids, not universal required categories. [E09 §This taxonomy is not universal; E13 §generate-synthetic-data]
- **RAG:** Retrieval-augmented generation finds information before generating an answer. Evaluate finding information and using it separately. [E06 §How should I approach evaluating my RAG system?]
- **Retriever, chunk, and reranker:** A retriever finds candidates; a chunk is a document section; a reranker reorders candidates. Changing chunk size requires rebuilding the corresponding index. [E13 §evaluate-rag]
- **BM25, semantic search, and hybrid search:** BM25 uses keyword matching; semantic search uses representations of meaning; hybrid search combines approaches. The retrieval walkthrough tests BM25 and query rewriting. [E12 HW4; E16d]
- **Embedding:** A numerical representation of content used for search or grouping. Similarity does not by itself establish factual correctness. [E16f 00:10:05; E06 §Are similarity metrics useful?]
- **Recall@k, Precision@k, and MRR:** Recall@k measures relevant items found in the first k results; Precision@k measures their relevant share; mean reciprocal rank rewards an early first relevant result. HW4 uses one known source recipe, so its recall becomes a target-found check. [E06 RAG answer; E12 HW4]
- **NDCG@k and two-hop recall:** NDCG rewards useful items near the top; two-hop recall checks retrieval of both pieces needed for a combined answer. [E13 §evaluate-rag]
- **Groundedness, faithfulness, relevance, and coverage:** Groundedness or faithfulness asks whether evidence supports the answer; relevance asks whether it addresses the question; coverage asks whether required content is present. Define each for the task. [E01 §Evaluating research agents; E06 RAG answer]
- **C|Q, A|C, and A|Q:** Context relevant to question, answer faithful to context, and answer relevant to question. These separate RAG checks. [E06 RAG answer]
- **ROUGE, BLEU, BERTScore, and cosine similarity:** Measures of text overlap or similarity named in this collection. They do not replace checks of specific product failures. [E06 similarity answer; F01d §Generic Metrics]
- **Query rewriting, expansion, and decomposition:** Restate a search, add related terms, or split it into smaller searches. Preserve the user's constraints when changing the query. [E16d 00:30:47–00:41:13]
- **Trajectory match modes:** Strict checks ordered calls; unordered permits another order; superset permits extra calls while checking required ones; subset checks permitted calls without requiring all of them. Argument matching has its own controls. [E14 §Agent trajectory match]
- **Graph trajectory, node, and interrupt:** A graph trace records visited steps, called nodes; an interrupt pauses work for outside input. E14 has separate graph and message evaluators. [E14 §Graph trajectory]
- **N-1 testing:** Replay real conversation history and test the next response. It helps isolate context-dependent failures. [E06 §How do I debug multi-turn conversation traces?]
- **Guardrail versus eval:** A guardrail can block or alter a live request; an eval usually measures behavior afterward. Sharing a check does not make their latency or error trade-offs equal. [E06 §What’s the difference between guardrails & evaluators?]
- **Red teaming, prompt hacking, and hallucination:** Red teaming seeks failures deliberately; prompt hacking attempts to redirect behavior; hallucination is unsupported or invented content. [E02 comment 41030485; F01c §Red Team Tracing]
- **Isolation versus sandbox:** Isolation separates trials; a sandbox restricts access. A copied workspace isolates files between runs without confining shell access. [E11b §Isolated workspaces]
- **Fixture:** The prepared files or environment a task starts from. Inspect supports sample files and setup scripts before execution. [E15c §Per Sample Setup, Files and Script]
- **Provider, custom provider, solver, and scorer:** A provider calls a model or system; a custom provider wraps your system; Inspect's solver executes work and its scorer grades it. [E11c §Provider Interface; E15a §Hello, Inspect]
- **Agent bridge, proxy, and model alias:** A bridge forwards agent model calls through the evaluator; a proxy forwards requests; an alias maps a requested model name to a configured model. Record requested and resolved names. [E15b §Overview and Models]
- **Generation settings, temperature, and reasoning effort:** Request options controlling generation or reasoning. Inspect's bridge drops many client settings by default, so a configured effort may not be the tested effort. [E15b §Generation Config]
- **MCP, SDK, and CLI:** MCP connects tools; an SDK is a programming library; a CLI is a command-line interface. Integrating one does not prove that another runtime behaves identically. [E11b §Capability tiers; E15b §Bridged Tools]
- **Schema, JSONL, CSV, YAML, and structured output:** A schema defines allowed fields; JSONL stores one JSON record per line; CSV is a table; YAML commonly stores configuration. Structured output constrains shape, not truth. [E02; E11; E12]
- **CI/CD and monitoring:** CI/CD runs checks around code changes and releases; monitoring inspects live behavior over time. Production discoveries should feed repeatable tests. [E06 production answer; E08 lesson 14]
- **Cache and prompt caching:** A response cache can reuse a prior result; prompt caching can reduce repeated prompt processing. Replaying a cached answer is not a fresh agent trial. [E11b §Isolated workspaces; E09 resources; F01c §Caveats]
- **Latency, tokens, and concurrency:** Latency is time taken; tokens are model-processing units; concurrency is simultaneous work. Resource contention can change latency and failure patterns. [E01 examples; E15c §Resource Management]
- **Cost threshold and cost per accepted task:** A threshold can flag an expensive completed call; cost per accepted task includes failed work and retries in total spend. The latter is E00's proposed workspace measure, not a validated formula from the practical guides. [E11a §Model quality; E00 §Compare configurations]
- **Fine-tuning, reward model, and RLHF:** Fine-tuning trains further on examples; a reward model predicts a quality signal; RLHF uses human feedback in training. E16g discusses these beyond its demonstrated review loop. [E05b §Fine-Tuning; E16g 00:44:45–00:49:01]
- **Ensemble, prompt optimization, and continual in-context learning:** An ensemble combines graders; optimization searches prompt variants; continual in-context learning supplies examples dynamically. All still need evaluation of the resulting behavior. [E10 §Optimization mode; E09 §How to Optimize the LLM Judge Prompt?]

- **Exact, regex, and fuzzy matching:** Compare literal text, a pattern, or approximate text. These can reject a valid variation when the expected format is too strict. [E01 §Types of graders]
- **Static analysis, fail-to-pass, and pass-to-pass:** Static analysis checks code without running its behavior. Fail-to-pass checks a repaired failure; pass-to-pass checks that working behavior remains intact. [E01 §Types of graders and Evaluating coding agents]
- **Ablation:** Remove one input or context element and compare results. It tests whether that element helps the judge. [E06 §How much context should I give a LLM judge?]
- **Hyperparameter and grid search:** A configurable design choice, such as chunk size, and systematic testing of combinations. Re-index when changing retrieval chunks. [E06 chunk-size answer; E13 §evaluate-rag]
- **Bias and redaction:** Bias systematically distorts judgments or samples; redaction removes sensitive information. Hiding a field in the viewer does not remove it from stored traces. [E06 sensitive-trace answer; F01c §Span Details Panel]

## 4. The method, step by step

This is a synthesis, not a checklist copied from one author. The common sequence is human inspection, clear failures, selective automation, validated measurement, and repeated use. E09 starts with broad expert outcome review and critique shadowing before specialized judges. E13 routes directly to a narrow check when a failure is already understood. Both routes need actual evidence and a human standard. [E09 §§Steps 3–7; E13 §evals-start]

### Step 1. Choose one task and make its outcome observable

**Do:** Pick work you perform often enough to inspect. Write the input, responsibilities, allowed actions, success conditions, and stopping rules. Identify the artifact or state that proves success. For coding, include a prepared environment and executable acceptance checks. For research, identify the required facts and evidence standard. [E01 §§Evaluating coding agents, Evaluating research agents; E06 §How should I evaluate a coding agent?]

For a bounded worker, a useful initial contract might say which files can change, what behavior must result, and which verification must run. This is a workspace adaptation. Let the packet describe every condition that a grader later enforces. If the grader expects a particular filename, disclose it. A hidden requirement makes the score unfair. [E00 §Start with one role; E01 roadmap Step 2]

**Why:** A model can produce persuasive text without completing the user's task. Clear outcomes let the root verify completion independently. [E01 §The structure of an evaluation]

**Common mistakes:** Starting with a model leaderboard; writing an overall intelligence score; checking a filename never requested; expecting an exact prose answer when several answers are acceptable.

**Best teaching:** E01, The structure of an evaluation and roadmap Step 2, about 5 minutes. E06, coding-agent and agentic-workflow answers, about 5 minutes. E16a, 00:01:07–00:05:47, explains how audience changes the standard.

### Step 2. Capture real runs and enough context to judge them

**Do:** Keep the input, instructions, model responses, tool calls, arguments, results, and final artifact together. Record versions and run IDs. Trace the outer session first, then add detail where failures are hard to explain. If the work crosses agents or human handoffs, keep the sequence connected until the user's need is resolved. [E08 lessons 5–6; E06 §§What is a trace?, How do I evaluate sessions with human handoffs?]

For worker comparisons, record the tested model, effort, harness, prompt or skill version, fixture, permissions, elapsed time, and usage. That record is an inference combining E00's proposed design with E01's system-level evaluation and E15's routing caveats. Without it, differences can be attributed to the wrong cause.

**Why:** Seeing only the final answer hides missing lookups, bad arguments, failed commands, and unsupported completion claims. [E11b §Refactoring with test verification]

**Common mistakes:** Designing a large logging platform before inspecting a few runs; omitting tool results; treating a tool name as evidence of successful execution; mixing evaluator calls into the target's trace.

**Best teaching:** E08 lessons 5–6, 20 minutes of video. E16e, 00:31:49–00:37:09, about 5 minutes, explains incremental logging. E08 lesson 8 explains suppressing judge instrumentation; F01c describes target and grading spans kept in one execution trace. Either approach needs clear attribution.

### Step 3. Read examples yourself and write open notes

**Do:** Begin with diverse real runs, including successful and awkward ones. Read the user-visible outcome, then inspect internal steps when needed. Write a short, specific note that a new reviewer could understand. Include missing features and bad product decisions even when they are not model faults. Diagnose the cause later. [E06 §§Why is error analysis important?, Should I record problems that aren’t the model’s fault?; E09 §Examples of Good Critiques]

For multi-step traces, start with the earliest failure that matters. A wrong context selection can explain several bad later steps. For a single output, several independent notes can be useful. The recipe walkthrough explicitly distinguishes those cases. [E16b 00:24:04–00:24:12]

**Why:** Reading outputs reveals requirements you did not know to write. A generic model reviewer cannot discover all your unstated preferences. [E16f 00:01:01 and 00:18:25]

**Common mistakes:** Asking AI to define all quality rules from logs; forcing notes into a taxonomy too early; counting every downstream symptom as a separate cause; outsourcing the learning loop.

**Best teaching:** E03, 00:09:56–00:31:39, about 22 minutes. E16b, 00:01:47–00:03:56, about 2 minutes. E06, examples-needed answer, distinguishes discovery from validation.

The sources offer different starting numbers. E01 proposes 20–50 initial tasks. E06 proposes roughly 100 diverse discovery traces and at least 30 manual reviews. E09 starts around 30 discovery examples. These numbers describe different stages and practical heuristics. Continue while examples change your understanding. None proves a precise production reliability rate. [E01 roadmap Step 0; E06 §How many examples do I need?; E09 §How many examples do you need?]

### Step 4. Group notes, check the groups, and prioritize

**Do:** Group related notes into named failure modes. Give each a clear definition and examples. A model can suggest groups or map notes to them, but the expert reviews both. Include an unclassified option so new problems can emerge. Count confirmed examples and keep severity visible. [E03 00:31:39–00:46:06; E12 HW2]

For agent failures, a last-success/first-failure matrix can reveal where to inspect next. Return to the records behind large cells. The matrix is a guide to hypotheses, not a diagnosis by itself. [E16e 00:21:34–00:30:53]

**Why:** Specific categories point to changes. A broad label such as capability limitations does not tell you whether to fix a prompt, a tool, retrieval, or a handoff. [E03 00:35:30]

**Common mistakes:** Trusting invented model categories; treating suggested labels as confirmed; prioritizing only by count; reporting a percentage without saying what was counted.

**Best teaching:** E03 grouping chapter, about 15 minutes. E16b, 00:27:22–00:31:11, about 4 minutes. E13 review-loop, The two modes and Key principles, about 4 minutes.

### Step 5. Fix clear defects before building expensive judges

**Do:** Repair obvious missing instructions, broken code, or unusable inputs. Replay the affected examples and check neighboring behavior. Choose an automated evaluator only when the issue will recur, requires continued improvement, or has enough consequence to justify it. [E09 §Step 4; E06 §Should I build automated evaluators for every failure mode?]

**Why:** The goal is better behavior. A missing prompt instruction can often be fixed before building a classifier around its consequences. A judge that adds little learning can become recurring cost without recurring value. [E03 01:05:09–01:08:46]

**Common mistakes:** Writing a judge for every note; choosing another model before investigating the cause; fixing one issue without checking regressions. E16g's model comparison shows one error disappearing while another increased. [E06 §How much time should I spend on model selection?; E16g 00:59:47–01:00:19]

**Best teaching:** E09 Step 4 and Do You Really Need This?, about 3 minutes. E03, 01:00:51–01:09:57, about 9 minutes.

### Step 6. Add code checks for objective rules

**Do:** State one failure rule and identify the evidence it needs. Implement it in the existing project's language. Return the result and the reason. Check known good, bad, and borderline examples. If a heuristic stands in for a human judgment, compare it against human labels. [E13 §write-code-eval]

For file edits, inspect actual files and independent tests. For permitted actions, inspect recorded operations and arguments. For a citation, code can verify that the cited ID was retrieved, but that alone does not prove the document supports the claim. Split the objective and interpretive checks. [E13 §write-code-eval; E11b §Refactoring with test verification]

**Why:** Code is cheap, repeatable, and easy to debug for explicit conditions. Its limits are equally explicit. [E01 §Types of graders]

**Common mistakes:** Checking words in the completion message; assuming schema validity proves correctness; confusing deterministic behavior with accurate rules; letting an agent modify protected grading evidence.

**Best teaching:** E13 write-code-eval, about 2 minutes. E11b Refactoring with test verification and Isolated workspaces, about 10 minutes. E05b Step 1 gives a JavaScript assertion example.

### Step 7. Build a narrow judge when interpretation remains

**Do:** Choose one discovered criterion. Write clear Pass and Fail definitions. Supply the needed inputs and evidence. Add carefully reviewed training examples, including confusing boundaries, when they help. Require structured output with a critique before the decision. [E13 §write-judge-prompt; E09 §Start with Expert Examples]

Collect labels for that criterion, rather than borrowing an unrelated overall quality score. Human notes teach the judge during development, but they should not become extra test-time help unless new real runs will contain that same information. [E16a 00:53:08–00:56:23]

**Why:** A narrow judgment makes errors actionable and gives the human a standard to validate. Full context is useful for human discovery; each automated judge only needs context relevant to its question. [E06 §How much context should I give a LLM judge?]

**Common mistakes:** Asking for quality from 1 to 100; giving every judge the entire trace; treating another model's labels as ground truth; selecting easy demonstrations that do not teach the boundary.

**Best teaching:** E13 Four Components and Anti-Patterns, about 6 minutes. E16c, 00:25:05–00:32:56, about 8 minutes. E09's critique-shadowing example provides a broader starting route.

### Step 8. Validate the evaluator separately from the application

**Do:** Divide criterion-specific human labels into prompt examples, development examples, and a hidden final test. Tune on development. Inspect disagreements for missing evidence, bad labels, and unclear rules. Freeze the prompt before checking test performance. Record the judge model and version. [E09 validation FAQ; E13 validation Steps 1–6]

Use plain operational names: failure recall and good-output acceptance. Report their counts and denominators. E06 calls a failure positive; E13 calls a pass positive. Both TPR and TNR matter, but their names reverse meaning across those sources. [E06 validation answer; E13 validation Step 3]

The common split guidance is roughly 10–20% for prompt examples and the rest divided between development and test. Label counts need enough passes and failures to expose both error directions. Do not turn a rough total count into a universal sufficient sample size. E13's capture asks for 30–50 examples of each class across development and test combined; E06 and E09 give more demanding per-set guidance when possible. [E13 validation Step 1; E06 validation answer; E09 validation FAQ]

**Why:** Improving the judge on familiar cases can overfit. Judge accuracy is a separate result from product success. [E10 §Optimization mode; E16c 00:45:06]

**Common mistakes:** Reporting development results as final; reusing test mistakes to tune without reserving new test data; treating perfect small-sample scores as production guarantees; hiding the always-pass baseline.

**Best teaching:** E09 validation FAQ, about 4 minutes. E16c, 00:19:44–00:22:37 and 00:33:30–00:41:52, about 11 minutes combined. E13 validation Steps 1–6, about 7 minutes.

### Step 9. Replay system variants fairly and report useful differences

**Do:** Use common tasks, equivalent starting states, and the real application path. Change one variable where practical. Repeat trials, inspect failures, and report results by criterion. Record quality, scope failures, steps, time, and cost separately. [E00 §Compare configurations; E01 roadmap Step 4; E08 lesson 12]

Verify a known acceptable solution against graders. Include known bad evidence to see whether the suite can reject it. Separate application failures from grader defects and infrastructure errors. [E01 roadmap Steps 2, 5–6; E00 diagnostic-suite design]

When a model judge estimates an aggregate pass rate, distinguish observed passes from corrected estimates. E13 provides `theta_hat = (p_obs + TNR - 1) / (TPR + TNR - 1)` with Pass as positive. The example changes 80% observed passes to 85% using TPR 0.92 and TNR 0.88. Treat that as an illustration. A correction cannot fix unrepresentative inputs or a changed judge. Its near-zero denominator is an explicit limit. [E13 validation Steps 7–8]

**Why:** A useful comparison explains what improved, what regressed, and what the change cost. A lone average or successful demonstration cannot do that.

**Common mistakes:** Replaying cached responses as new trials; mixing fixture states; comparing changed datasets as though they were identical; treating a corrected point estimate as certain.

**Best teaching:** E08 lessons 11–12, 22 minutes. E01 non-determinism section, about 3 minutes. E16c, 00:48:13–01:00:18, about 12 minutes for uncertainty and its limits.

### Step 10. Use checks in CI and review fresh runs

**Do:** Run useful cheap checks around relevant changes. Schedule more expensive replay and review according to risk, cost, and how often they find failures. Keep established successes in regression tests and difficult tasks in capability tests. Add production failures after review. Retire expensive checks that stop earning their cost. [E05b §The Types Of Evaluation; E06 §§How often should I run my evals?, What should I do when my gold dataset becomes stale?]

Production monitoring uses new data and usually runs asynchronously. Preserve some random review beside outliers and alerts. Revalidate a judge after changing its prompt or model. Review whether user expectations, tools, and test coverage have changed. [E06 production and sampling answers; E13 validation Practical Guidance]

**Why:** CI catches known failures. Fresh traces reveal new ones. A passing frozen suite protects past behavior but does not prove future usefulness. [E01 roadmap Steps 7–8; E08 lesson 14]

**Common mistakes:** Making every eval a live guardrail; removing all human review after initial alignment; comparing scores across revised datasets without noting the revision; running a suite without an owner.

**Best teaching:** E06 CI/CD, guardrail, and review-frequency answers, about 6 minutes. E08 lesson 14, 6 minutes. E01 roadmap Steps 7–8, about 4 minutes.

## 5. Agent-specific evaluation

### Check the result, then the path needed to explain it

An agent can return a good-looking answer after failed actions. A browser confirmation can appear without the expected database state. A coding agent can say tests passed without proving that it executed the right tests. Begin with the actual outcome. Then check the path where it carries a requirement or explains a failure. [E01 §§Computer use agents, Evaluating coding agents; E11b §Refactoring with test verification]

For this workspace, completion, authority, and efficiency should remain separate checks. This is an inference from E06's authorization guidance and E01's graders. Passing an acceptance test proves one behavior. It does not prove that the worker stayed within the packet, used permitted tools, or reported accurately. Conversely, using allowed tools does not prove that the task was completed.

Useful evidence has several layers:

| Layer | What to check | What it cannot prove alone |
| --- | --- | --- |
| Final artifact or state | The requested behavior or result exists. | Whether the path respected every required boundary. |
| Tool choice | The right operation was selected. | Whether it received the right inputs. |
| Tool arguments | Paths, IDs, amounts, and constraints are correct. | Whether execution succeeded. |
| Tool result | The operation returned the expected result. | Whether all later work used it correctly. |
| Authorization and preconditions | The action was permitted and required checks happened. | Whether the requested final outcome exists. |
| Final report | The explanation matches verified evidence. | Evidence that the claimed operations happened. |

E06 illustrates checking a cancellation tool's name, order ID, successful response, and changed order status separately. E08's shipping example selects the right function but confuses an order number with a tracking ID. These are distinct failures and should produce different fixes. [E06 §How do I evaluate agentic workflows?; E08 lesson 7]

### Allow valid routes and enforce meaningful boundaries

E01 recommends outcome grading over brittle expected paths. AgentEvals supplies path matching because some contracts really concern required or permitted actions. Choose the rule to match the obligation. [E01 roadmap Step 5; E14 §Agent trajectory match]

- Use strict order when a precondition must precede an action.
- Use unordered matching when all calls matter but their order does not.
- Use superset matching for required calls when extra work is acceptable.
- Use subset matching for permitted calls, while checking task completion separately.
- Keep exact argument matching for values carrying scope or meaning; relax it only for harmless differences.

These are applications of E14's documented modes. A whole reference trajectory can still be too strict for a flexible task. For a worker, checking a required bootstrap read before a write may be appropriate. Requiring the same incidental searches as a reference run may reject valid work. The latter examples are workspace inferences.

AgentEvals gives both reference-free model judging and reference comparisons. Neither comes with a validated rubric for the user's worker policy. Its graph utilities apply to LangGraph threads, including interrupted and resumed work. They are not a universal exporter for every CLI harness. [E14 §§Trajectory LLM-as-judge, Graph trajectory]

### Repeat runs and report the kind of reliability you need

A task can pass once and fail later. Keep the distribution of results rather than choosing the nicest transcript. E01's pass@k counts finding at least one success in k attempts. Its pass^k counts all k attempts succeeding. Retry-assisted capability and dependable first-attempt operation answer different questions. [E01 §How to think about non-determinism]

E01 illustrates that 75% per-trial success gives about 42% success across all three trials under the example's multiplication model. This is a teaching calculation, not an observed rate for a particular worker. Real runs can share infrastructure or state failures, which is one reason the source insists on clean environments. [E01 non-determinism section and roadmap Step 4]

Promptfoo's checklist proposes repeated runs and uncached development tests. E08's final experiment warns that a small prompt change did not clearly help and some other scores fell. Repeat equivalent cases when a single result could change the decision. There is no universal repeat count in this collection. [E11b §QA checklist; E08 lesson 12]

### Separate reset, access limits, and protected grading

A clean workspace prevents trials from contaminating each other. A sandbox restricts what the agent can access. They solve different problems. Promptfoo's `copy_working_dir` creates a workspace per evaluation call and removes it after assertions. File assertions must run while that workspace exists. A copied directory is explicitly not a sandbox. [E11b §Isolated workspaces]

Inspect gives each sample its own sandbox instance. Yet Python tools, solvers, and scorers remain in the evaluation process unless their operations use the sandbox interface. A container attached to a task does not move all execution inside it. [E15c §Example: File Listing and Per Sample Setup / Sandbox]

Inspect's generated Docker configuration disables networking. A custom Compose configuration replaces that default, so it must retain the intended network restriction explicitly. Provider web tools and host-side bridged tools can reach resources outside the sandbox. Review those routes separately. [E15c §Docker Configuration; E15b §Granted Capabilities and Bridged Tools]

Protected tests and grading evidence should stay outside the agent's edit authority. This design follows E00's illustrative grader and E01's warning about grader loopholes. A system that can rewrite its own success evidence may appear to improve while doing worse work.

### Treat routing and effort as part of the tested configuration

Inspect's sandbox bridge checks aliases, then a resolver, and otherwise serves calls with the configured evaluation model. This includes requests using unexpected model names. Background calls intended for a cheap model can therefore use the main evaluation model. The transcript records `requested_model`; compare it with the model that actually served the call. [E15b §Models]

The bridge also drops many client generation settings by default, including temperature, token limits, and reasoning effort. The resolved Inspect settings and provider defaults govern instead. `forward_generation_config=True` changes that behavior. Record the choice before comparing model tiers or reasoning budgets. [E15b §Generation Config]

Host-tool integration has another distinction. Normally one model proposal grants one execution of a matching bridged tool with approved arguments. For Codex code mode, the model proposes an outer `exec` script, not each inner MCP call. The capture explains why those servers need `require_proposal=False`, which removes the inner-call proposal guarantee. Approval then reviews the outer script. This is a documented integration limit, not evidence that every CLI exposes the same behavior. [E15b §Execution Contract]

### Diagnose long runs and parallel work

Read the overall outcome before assigning blame to a branch. Preserve the full ordered interaction, including root packets and worker returns where available. First-failure review prevents one cascade from becoming many apparently independent defects. Independent branches can have several first failures, so keep the raw evidence even when the first analysis selects one important problem. [E06 §How do I debug multi-turn conversation traces?; E16e 00:17:59–00:20:54]

Recipe Chatbot HW5 teaches a concrete diagnostic: count last-success/first-failure pairs and inspect a heatmap. Its 96 traces are selected failures with labels already supplied. The exercise reveals the distribution of those failures, not the agent's total failure rate. You need all relevant attempts and usage denominators to estimate that. [E12 HW5 §§What You'll Do, Data Provided; E16e 00:31:49–00:32:44]

Convergence in the agent course measures path length against the shortest observed completed run. It cannot identify an unnecessary step present in every run. Use it to inspect variation within similar completed tasks, alongside an independent outcome check. It is not proof of an optimal path or adequate quality. [E08 lesson 9]

### Interpret trace metrics before comparing cost

Promptfoo tracing distinguishes generation markers from protocol turns. Codex SDK and app-server turn markers cannot establish whether inner calls were batched. Subagents have their own turns; cache hits have no new generation turn. Define the measured unit before claiming one harness is more efficient. [F01c §Turn marker spans and Caveats]

For worker value, E00 proposes total spend divided by accepted tasks, including failures and retries. That is a useful workspace measure, but this collection does not supply a complete audited cross-harness billing implementation. Promptfoo can carry reported cost and usage; its installed text-price catalogue omits several billing factors. Inspect routing can change which model incurred the spend. Keep measured totals separate from estimates and unknown values. [E00 §Compare configurations; E11c §Looking up text-token prices; E15b §§Models, Request Settings]

## 6. Where the sources agree and where they disagree

Agreement here means recurring advice across the captures. It is not a survey of the whole industry. Several sources share authors and examples, so repeated statements are not independent studies.

| Topic | Agreement | Difference or limit | Practical reading |
| --- | --- | --- | --- |
| Start with data | E03, E06, E07, E09, E13, and F01d all require human inspection. | E01 also converts known manual checks directly into tasks. | Discover uncertain standards; automate known clear rules. |
| Meaning of eval | All seek evidence about useful behavior. | E01 focuses on automated development tests; E03 uses eval for a broader process; E02 contains unit-test shorthand. | Say whether you mean a check, a suite, or the whole learning loop. |
| Binary judgments | E06, E07, E09, and E13 prefer clear Pass/Fail criteria. | E01 allows partial credit; E14 exposes continuous scores; E13 permits realism ranking for data curation. | Binary labels per criterion can coexist with progress and ranking measures. |
| What a judge should cover | All require a human standard and enough context. | E09 starts with broad outcome critique shadowing; E13 rejects a judge spanning several dimensions. | Broad human discovery first; choose the automation scope after learning the failures. |
| Matching paths | E01 accepts multiple valid routes. | E14 provides strict matching; E11 and F01c show path assertions. | Enforce paths only where order or action is part of the contract. |
| Judge metrics | Sources warn that raw agreement hides rare failures. | E05b and F01d recommend precision/recall; E13 prefers TPR/TNR and restricts kappa to humans; E10 displays all of them. | Choose the measure for the decision and state its class definition. |
| Positive label | Each source can compute both error directions. | E06 and E16c make errors positive; E12 HW3, E13, and F01a make passes positive. | Label failure recall and good-output acceptance explicitly. |
| Accuracy threshold | All require checking judge mistakes. | E13 gives 90% targets and 80% minimums; E06 and E16c make acceptability consequence-dependent. | Skill defaults are not universal acceptable error rates. |
| Human and code labels | All treat them as reference evidence. | E08 calls them fully accurate in places; F01d stresses bad labels and E01 warns about grader defects. | A reference judgment or program can be wrong. Inspect disagreements. |
| Sampling | Diverse examples help discovery; fresh runs matter. | E13 synthetic-data guidance favors stratified real-data sampling; E06 insists on random examples too. | Coverage-oriented samples find risks; preserve random samples for broader checks. |
| Example counts | All offer manageable starts. | Counts refer to discovery, validation, or replay; the split targets also vary. | Name the stage and count each label, not just total rows. |
| Similarity scores | Method guides favor task-specific failures. | E08 lesson 13 proposes semantic similarity for judge explanations; E06 and F01d warn about generic similarity. | Similar wording is not enough to validate a task-specific decision. |
| Tools and languages | Existing scripts and simple viewers can work. | F01d favors Python; E16g demonstrates TypeScript; E11 supports Node integration. | The method does not require changing your familiar stack. |
| Production checks | CI and fresh-run monitoring complement each other. | A live guardrail can act before delivery; an offline evaluator usually cannot. | Evaluate any added guardrail as a system change. |
| Starting report | E00 correctly favors application tasks and independent state checks. | Its duration, judge starting sequence, and copyable-code framing need correction. | Use E00 as a proposal and follow captures for source facts. |

The judge-scope disagreement is real but limited. E09's complete guide first aligns an expert and a broad outcome judge, then analyzes unseen errors and adds specialized judges. E13 begins narrow once a failure mode is known. E00's narrow-judge exercise is sensible after discovery, but it is not E09's opening sequence. [E09 §§Step 3, Step 7; E13 §write-judge-prompt; E00 §2.3]

The metrics disagreement includes a naming problem and a methodological preference. Switching Pass and Fail changes which operational quantity is TPR. Separately, E13 chooses TPR/TNR because its correction formula uses them. E05b and F01d emphasize precision/recall for understandable failure detection. Those measurements answer related but different questions; no capture proves one pair always replaces the other. [E13 validation Step 3; E05b §Important Note; F01d §Unverified Judges]

The proposed sample sizes are not a coherent statistical standard. The sources give heuristic discovery batches, UI unlock counts, and larger judge-label targets. Some captures also differ about whether desired class counts apply per split or across splits. Coverage, label balance, uncertainty, and the decision at stake should explain the chosen size. [E06 examples-needed answer; E10 §Labeling mode; E13 validation Step 1]

Tool documentation sometimes makes stronger claims than its own examples establish. Promptfoo's guide says a prompt failing half the time is ambiguous, but that is not a complete diagnosis. E08's fully accurate human/code reference claim overlooks mistaken criteria or implementations. E13's claim that improving TPR narrows intervals more than improving TNR rests on one remark about the shrinking denominator, with no derivation. Keep those as source opinions, not governing rules. [E11b §Non-determinism; E08 lessons 7 and 13; E13 validation Practical Guidance]

## 7. Tools and code compared

Setup effort and fit below are inferences based on the captured architecture. Cost describes known sources of expense, not current prices. No installs or experiments were run for this document. The captured examples are dated evidence, not verified present-day compatibility or model recommendations.

| Tool or code | Language | What it is for | Setup effort, inference | Cost evidence | Fit for a TypeScript engineer running CLI agents, inference |
| --- | --- | --- | --- | --- | --- |
| Promptfoo [E11; F01c] | Node.js, JavaScript/TypeScript, YAML | Replay cases across providers; assertions; results and trace viewer. | Low for a text example; moderate for actual CLI adapters and artifact checks. | Can record cost and latency; assertions flag completed calls; no billing guarantee. | Strong first runner candidate because custom providers wrap the existing system. |
| Inspect AI [E15] | Python; sandboxed agents can use any language | Dataset, solver, scorer, logs, sandboxes, external-agent bridge. | Moderate to high for CLI, container, routing, and tool setup. | Model and environment costs; bridge settings can change them; no cost comparison here. | Useful when clean environments and controlled CLI execution justify Python integration. |
| AgentEvals [E14] | TypeScript and Python | Message and graph trajectory matching and model judging. | Low to moderate for a normalized trace; extra work for each harness exporter. | Rule matching has no judge call; model-based matching incurs model calls. | Useful library for required, allowed, and ordered actions; needs outcome checks too. |
| evals-skills [E13] | Markdown procedures; small code examples | Route discovery, review, code checks, judge writing, validation, and retrieval analysis. | Low to study; moderate to adapt workflow and review UI. | Agent and judge usage; README leaves production cost and regression suites beyond these skills. | Fits skills-based work; it is not a general evaluation runner. |
| Recipe Chatbot [E12; E16a–e] | Python backend/notebooks; HTML/CSS/JS frontend | Worked exercises for prompts, discovery, judges, retrieval, and failure transitions. | Moderate to run the app; HW5 analysis needs no new model calls. | Calls for chatbot, synthetic inputs, and judges; supplied data can reduce exercise cost. | Best as a learning project whose method can be copied without copying the stack. |
| AlignEval / align-app [E10; F01b] | TypeScript/Next.js frontend; Python/FastAPI backend in article | Human labeling and binary judge validation/optimization. | Low to read; moderate to run or adapt the full app. | Small-model and field-selection cost rationale; no price or latency table. | Useful review UI example; README is frontend only and does not supply the whole service. |
| Phoenix [E08; E12 optional assignment] | Python labs; telemetry integrations | Trace/span/session review, annotations, datasets, and experiments. | Moderate for meaningful nested tracing. | No audited cost schedule in these captures. | Copy the trace structure; adoption is optional if local logs are already usable. |
| judgy [E12 HW3; E13 validation] | Python | Adjust observed success rates using measured judge errors and report uncertainty. | Moderate statistical integration after label validation. | No model call required for the arithmetic itself; no package price claim here. | A separate statistics layer, not a worker runner or quality definition. |
| Simple scripts and a custom viewer [E05b; E07; E16g] | Existing stack, including TypeScript | Assertions, trace review, labels, and a narrow experiment loop. | Low initial effort; maintenance rises with features. | Existing model calls and review labor; no proven free system. | Sensible starting point when the runner is already available. |

Promptfoo's custom provider exposes `id()` and `callApi()`. A response can include output, errors, the actual prompt, usage, cost, and metadata. Use errors for failed requests. Preserve actual prompts if an adapter rewrites inputs. Node loads the provider outside a frontend bundler, so browser globals, CSS imports, and bundler-only aliases need a build step or separation. [E11c §§Provider Interface, Reporting the Actual Prompt, TypeScript Providers in Frontend Projects]

Inspect's bridge is the strongest infrastructure lesson in this collection because it makes routing and execution boundaries explicit. It is also more work than its introductory task example suggests. Sandboxes, network grants, host tools, and generation settings need separate configuration. This is a fit assessment, not a benchmark proving Inspect better than another runner. [E15b; E15c]

AgentEvals teaches small matching rules, but several README examples have visible defects. The TypeScript README contains `satisifes`, undefined variables in a graph example, and Python `json.dumps` inside TypeScript. Learn the intended matching behavior and repair or validate code before reuse. The package implementation was not tested in this packet. [E14b §§Unordered match, Graph trajectory strict match, Evaluate]

### Other named tools and what this collection establishes

The following list covers the remaining tool families named by the sources. A mention alone is insufficient for a setup, price, or comparative recommendation.

- **Braintrust, LangSmith, Langfuse, Arize AX, Humanloop, HoneyHive, and Truesight:** Tracing, review, or evaluation platforms named in E01, E05b, E06, E09, and E13. E01 describes some roles, and F01c gives Braintrust and Langfuse trace lookup details; this collection does not provide complete onboarding or comparable cost evidence.
- **Harbor, Inspect SWE, and openai/evals:** Harbor is described as container-based evaluation infrastructure in E01's appendix; Inspect SWE supplies linked CLI bridge examples in E15; openai/evals is a pointer in E02. Implementation depth differs, so do not treat them as equally captured tutorials.
- **ChainForge, TheoremQA, and applied-llms.org:** Community pointers in E02. Language, setup, pricing, and agent-workspace fit remain unestablished by that thread.
- **Claude Code, Codex, OpenCode, Gemini CLI, Open Interpreter, Hermes, and Antigravity:** Runtime targets or workspace tools, not interchangeable graders. E11 documents several provider boundaries; E15 describes CLI bridging and tool-name handling; E00 names the user's broader workspace. No capture mentions Hermes or supplies a Hermes eval adapter; it is listed only because it is a workspace harness.
- **OpenAI Agents SDK, Claude Agent SDK, Pydantic AI, LangChain, LangGraph, Google ADK, Swarm, and A2A:** Agent-building libraries or protocols named in examples and discussion. E14 gives graph-specific integration; E08 demonstrates decomposition; the others have varying amounts of linked or spoken detail.
- **Jev, BERT, logistic regression, DSPy, and GEPA:** Classifier or optimization alternatives named in E06 and E09. No controlled comparison supports replacing a validated judge with any of them automatically.
- **Jupyter, marimo, pandas, NumPy, scikit-learn, seaborn, matplotlib, DuckDB, rank-bm25, and LiteLLM:** Data inspection, statistics, database, retrieval, or model-access tools used in exercises. Study the relevant task first; these are not required dependencies for a TypeScript implementation. [E08; E12; E13; E16d–e]
- **FastHTML, MonsterUI, Streamlit, Gradio, Panel, Shiny, Next.js, FastAPI, SvelteKit, React, Tailwind, Zod, and Pydantic:** Review-app or structured-output building blocks. The sources favor clear domain rendering and short review actions, rather than proving one framework best. [E05b; E07; E10; F01b]
- **Cursor, Lovable, Replit, Julius, Hex, spreadsheets, and pivot tables:** Authoring or analysis aids named in the method examples. Some video spellings are uncertain. Treat the human inspection workflow as the supported lesson, rather than a productivity claim about each tool. [E03; E07; E16a–d]
- **Metabase, Postgres, Airtable, SQLite, Redis, Weights & Biases, GitHub Actions, and GitLab CI:** Storage, charts, or automation named in examples. E16g demonstrates TypeScript checks with existing CI and review tools; no full portable deployment recipe is captured.
- **Railway, Vercel, Dokku, Coolify, and Hetzner:** Hosting choices discussed by E10. Only Railway has short deployment commands there; the others are alternatives, not evaluated implementations.
- **Docker, Kubernetes, Daytona, Modal, EC2, Proxmox, Vagrant, and OpenShell:** Environment options listed by Inspect. Local execution supplies no isolation; configuration and provider availability are captured documentation claims. [E15c]
- **Jaeger, Grafana Tempo, Honeycomb, Vercel AI SDK, OpenInference, OpenLLMetry, FFmpeg, Instructor, and Outlines:** Trace transport/viewing, instrumentation, media, or schema tools named in F01c, E08, E11c, and E13. Review the captured integration before assuming support across all harnesses.
- **pytest, Vitest/Jest, ruff, mypy, bandit, and ordinary assertions:** Executable checks used or illustrated for behavior, types, code quality, or evaluator integration. They prove the tested conditions, not every acceptance requirement. [E01; E14]

Public benchmark names include SWE-bench Verified, Terminal-Bench, HumanEval, MMLU, GPQA Diamond, Aider Polyglot, BrowseComp, WebArena, OSWorld, CORE-Bench, and tau-family support benchmarks. They are selection and context references. The captures do not make them a replacement for private tasks reflecting the user's actual tools, packets, and authority. [E01; E06]

## 8. Every source, one entry each

Every file in `sources/` (verbatim captures, not published in this snapshot) has an entry below, including redirects, raw captions, archived files, and failed captures. E16 and F01 are bundles with an entry per constituent. Counts include capture metadata, code, and repeated navigation; they are not clean prose lengths. Reading budgets are estimates except source-stated durations. Entries name the capture by file name; original links point to the public source.

### E00. Starting research report

**Type and length:** Generated brief; about 15 minutes reading.

**Capture status:** Full local export; recommendations are leads, not primary evidence.

**The point:** Focus on application and agent tasks, with independent checks of actual results. The proposed worker design and resource ranking need to be assessed against the captures.

**Best parts first:** First, what you are trying to learn and How I would apply this, about 8 minutes.

**Digest:** No standalone digest; use the other digests’ E00 comparisons.

**Capture files:**

- LLM evals learning path for an agent workspace: 3,347 capture words; full.

### E01. Demystifying evals for AI agents ([original](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents))

**Type and length:** Anthropic article, January 9, 2026; about 30 minutes.

**Capture status:** Full text, code, tables, and figure captions; linked images are not transcribed.

**The point:** An agent evaluation tests the model and the system that gives it tools, then checks both its execution record and the resulting state. Useful suites start with real failures, clear success criteria, clean environments, and graders checked against human judgment.

**Best parts first:** The structure of an evaluation and non-determinism, about 6 minutes; roadmap Steps 2–6, about 10 minutes.

**Digest:** [source digest](digests/E01-anthropic-demystifying-evals.md).

**Capture files:**

- Demystifying evals for AI agents: 6,208 capture words; full.

### E02. Ask HN: consensus on unit testing LLM prompts ([original](https://news.ycombinator.com/item?id=41019748))

**Type and length:** Question and five comments, July–August 2024; about 3 minutes.

**Capture status:** Full thread; linked readings are not included.

**The point:** The question asks how to test prompts and catch regressions when prompts or models change. Replies suggest structured output, a manually scored spreadsheet, Hamel Husain's evaluation article, and several tools.

**Best parts first:** Comment 41030485, about 1 minute; comments 41021139 and 41034521, about 1 minute.

**Digest:** [source digest](digests/E02-hn-41019748.md).

**Capture files:**

- Ask HN: What's the consensus on "unit" testing LLM prompts?: 590 capture words; full.

### E03. Lenny podcast with Hamel Husain and Shreya Shankar ([original](https://www.youtube.com/watch?v=BsWxPI9UM4c))

**Type and length:** Podcast, September 25, 2025; 1:46:33.

**Capture status:** Full automatic captions, metadata, and raw JSON; names and screen details need caution.

**The point:** Evals are the whole process of systematically measuring and improving an AI application, including reading its real logs. Start with a domain expert’s observations, group actual failures, and automate only the checks worth maintaining.

**Best parts first:** 00:09:56–00:31:39, about 22 minutes; 00:54:45–01:09:57, about 15 minutes.

**Digest:** [source digest](digests/E03-E04-lennys-podcast-hamel-shreya.md).

**Capture files:**

- Why AI evals are the hottest new skill for product builders | Hamel Husain & Shreya Shankar: 22,485 capture words; full.
- Raw English captions: 2,861 timestamped fragments; E03 sidecar.

### E04. Published Lenny episode page and transcript ([original](https://www.lennysnewsletter.com/p/why-ai-evals-are-the-hottest-new-skill))

**Type and length:** Newsletter page for the same 1:46:33 episode.

**Capture status:** Partial article; public transcript and show notes included, paid takeaways excluded.

**The point:** The published transcript provides another rendering of the same podcast and helps clarify caption errors. It does not supply missing paid takeaways or independent evidence for repeated anecdotes.

**Best parts first:** Show notes, about 3 minutes; validation discussion corresponding to 00:54:45–01:00:51, about 4 minutes reading.

**Digest:** [source digest](digests/E03-E04-lennys-podcast-hamel-shreya.md).

**Capture files:**

- Why AI evals are the hottest new skill for product builders | Hamel Husain & Shreya Shankar (creators of the #1 eval course): 23,688 capture words; partial.

### E05. Your AI Product Needs Evals ([original](https://hamel.dev/evals/))

**Type and length:** Hamel Husain article, March 29, 2024; about 20 minutes.

**Capture status:** E05 is the empty redirect; E05b is the full article; images are linked and confidential prompt fields omitted.

**The point:** Use application-specific assertions, human/model review, and later real-user experiments. Reuse traces and review tools for debugging and training-data curation.

**Best parts first:** Step 1 through Step 3, about 7 minutes; Automated Evaluation w/ LLMs and agreement warning, about 5 minutes.

**Digest:** [source digest](digests/E05-hamel-your-ai-product-needs-evals.md).

**Capture files:**

- Redirect: 55 capture words; full.
- Your AI Product Needs Evals: 4,272 capture words; full; [original](https://hamel.dev/blog/posts/evals/).

### E06. AI Evals: Everything You Need to Know ([original](https://hamel.dev/blog/posts/evals-faq/))

**Type and length:** Hamel and Shreya FAQ, September 2026; about 75–90 minutes.

**Capture status:** Full answers and footnotes; media are linked.

**The point:** Look at real sessions before deciding what quality means or which tests to build. Turn recurring failures into cheap code checks or narrowly focused judges validated against human decisions.

**Best parts first:** Examples-needed, trusting automated evals, and agentic-workflow answers, about 10–12 minutes.

**Digest:** [source digest](digests/E06-hamel-shreya-evals-faq.md).

**Capture files:**

- AI Evals: Everything You Need to Know: 18,568 capture words; full.

### E07. A Field Guide to Rapidly Improving AI Products ([original](https://hamel.dev/blog/posts/field-guide/))

**Type and length:** Hamel Husain article, March 24, 2025; about 30 minutes.

**Capture status:** Full article; embedded demonstrations are not transcribed here.

**The point:** Improve AI by reading its actual interactions, finding repeated failures and testing fixes against those failures. Make review easy, let domain experts change prompts directly, and generate realistic test inputs when real usage is scarce.

**Best parts first:** The Error Analysis Process and review-tool checklist, about 5 minutes; synthetic data and Maintaining Trust, about 10 minutes.

**Digest:** [source digest](digests/E07-hamel-field-guide.md).

**Capture files:**

- A Field Guide to Rapidly Improving AI Products: 6,503 capture words; full.

### E08. Evaluating AI Agents ([original](https://www.deeplearning.ai/courses/evaluating-ai-agents))

**Type and length:** DeepLearning.AI/Arize course with John Gilhuly and Aman Khan; listed 2h36m, 15 videos, 6 code examples.

**Capture status:** Full course page and all 15 public transcripts; login notebooks, quiz answers, and appendix code absent. Digest covers only lessons 1–12.

**The point:** Trace a sales-data agent and compare router, skill, and trajectory checks through repeatable experiments. Later lessons add judge experiments and production feedback, while convergence remains a measure of observed paths.

**Best parts first:** Lessons 5–8, 49 minutes; lessons 9–12, 36 minutes; lessons 13–15, 11 minutes.

**Digest:** [source digest](digests/E08-deeplearning-ai-evaluating-ai-agents.md).

**Capture files:**

- Evaluating AI Agents: 1,303 capture words; full.
- Introduction: 926 capture words; full; [original](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/sqkza/introduction).
- Evaluation in the time of LLMs: 1,715 capture words; full; [original](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/gz8ys/evaluation-in-the-time-of-llms).
- Decomposing agents: 1,531 capture words; full; [original](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/hvoxa/decomposing-agents).
- Lab 1: Building your agent: 3,628 capture words; full; [original](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/pag5y/lab-1%3A-building-your-agent).
- Tracing agents: 1,241 capture words; full; [original](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/uymu6/tracing-agents).
- Lab 2: Tracing your agent: 3,698 capture words; full; [original](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/njjlv/lab-2%3A-tracing-your-agent).
- Adding router and skill evaluations: 2,714 capture words; full; [original](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/x3i1d/adding-router-and-skill-evaluations).
- Lab 3: Adding router and skill evaluations: 3,738 capture words; full; [original](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/yx7uz/lab-3%3A-adding-router-and-skill-evaluations).
- Adding trajectory evaluations: 1,338 capture words; full; [original](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/xdfwr/adding-trajectory-evaluations).
- Lab 4: Adding trajectory evaluations: 2,238 capture words; full; [original](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/an0wh/lab-4%3A-adding-trajectory-evaluations).
- Adding structure to your evaluations: 1,830 capture words; full; [original](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/a2c54/adding-structure-to-your-evaluations).
- Lab 5: Adding structure to your evaluations: 3,518 capture words; full; [original](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/fob86/lab-5%3A-adding-structure-to-your-evaluations).
- Improving your LLM-as-a-judge: 1,124 capture words; full; [original](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/f63n9/improving-your-llm-as-a-judge).
- Monitoring agents: 1,371 capture words; full; [original](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/y5v5y/monitoring-agents).
- Conclusion: 392 capture words; full; [original](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/ugje9/conclusion).

### E09. Using LLM-as-a-Judge For Evaluation: A Complete Guide ([original](https://hamel.dev/blog/posts/llm-judge/))

**Type and length:** Hamel Husain article, October 29, 2024; about 30–40 minutes.

**Capture status:** Full article, examples, and FAQ; linked resources and media are not transcribed.

**The point:** Start by having a trusted subject expert judge actual AI interactions as pass or fail and explain each decision. Build an automated judge from those examples, then test whether it reproduces the expert's decisions on separate examples.

**Best parts first:** Step 3 and critiques, about 6 minutes; validation FAQ, about 4 minutes; Step 7 and Do You Really Need This?, about 3 minutes.

**Digest:** [source digest](digests/E09-hamel-llm-judge.md).

**Capture files:**

- Using LLM-as-a-Judge For Evaluation: A Complete Guide: 7,828 capture words; full.

### E10. AlignEval: Building an App to Make Evals Easy, Fun, and Automated ([original](https://eugeneyan.com/writing/aligneval/))

**Type and length:** Eugene Yan article, October 27, 2024; source-stated 14-minute read.

**Capture status:** Full prose/code; screenshot text and embedded demos are not captured.

**The point:** Start by inspecting real model outputs and labeling them, rather than inventing evaluation criteria in advance. Write a simple pass/fail evaluator, meaning an LLM that judges another model's output, and measure its agreement with your human labels.

**Best parts first:** Labeling and Evaluation modes, about 3 minutes; Optimization mode, about 2 minutes; schema snippets, about 2 minutes.

**Digest:** [source digest](digests/E10-eugene-yan-aligneval.md).

**Capture files:**

- AlignEval: Building an App to Make Evals Easy, Fun, and Automated: 3,010 capture words; full.

### E11. Promptfoo documentation bundle ([original](https://www.promptfoo.dev/docs/getting-started/))

**Type and length:** Three documentation pages; about 35–50 minutes with code.

**Capture status:** Full raw Markdown/MDX; linked provider documentation is not captured.

**The point:** Promptfoo runs combinations of prompts, providers and test cases, then checks outputs with assertions, meaning rules that decide whether a result passes. Coding-agent evaluations also need evidence about commands, permissions and changed files because the final response can describe work without proving it happened.

**Best parts first:** E11a example/configuration, about 6 minutes; E11b refactoring/workspaces, about 10 minutes; E11c interface/Node constraints, about 8 minutes.

**Digest:** [source digest](digests/E11-promptfoo.md).

**Capture files:**

- Getting started: 2,176 capture words; full.
- Evaluate Coding Agents: 2,772 capture words; full; [original](https://www.promptfoo.dev/docs/guides/evaluate-coding-agents/).
- Javascript Provider: 2,128 capture words; full; [original](https://www.promptfoo.dev/docs/providers/custom-api/).

### E12. Recipe Chatbot learning repository ([original](https://github.com/ai-evals-course/recipe-chatbot))

**Type and length:** Eleven README/index files at snapshot e08dec0; exercise duration unknown.

**Capture status:** Full listed files, not full implementation; notebook index has first Markdown cells only; video index holds pointers.

**The point:** Start by defining expected behavior, collecting realistic queries, and reading the resulting conversation records. Turn observed mistakes into named failure categories, then build a narrow model judge and measure its mistakes against human labels.

**Best parts first:** HW2 Part 2, about 3 minutes; HW3 Steps/Key Metrics, about 5 minutes; HW5 Data/Steps, about 4 minutes.

**Digest:** [source digest](digests/E12-recipe-chatbot.md).

**Capture files:**

- Recipe Chatbot - AI Evaluations Course: 562 capture words; full.
- Annotation Tool: 350 capture words; full; [original](https://github.com/ai-evals-course/recipe-chatbot/blob/main/annotation/README.md).
- Homework Assignment 1: Write a Starting Prompt: 856 capture words; full; [original](https://github.com/ai-evals-course/recipe-chatbot/blob/main/homeworks/hw1/readme.md).
- Homework 2: Recipe Bot Error Analysis: 564 capture words; full; [original](https://github.com/ai-evals-course/recipe-chatbot/blob/main/homeworks/hw2/README.md).
- Homework 3: LLM-as-Judge for Recipe Bot Evaluation: 1,254 capture words; full; [original](https://github.com/ai-evals-course/recipe-chatbot/blob/main/homeworks/hw3/README.md).
- Homework 4: Recipe Bot Retrieval Evaluation: 721 capture words; full; [original](https://github.com/ai-evals-course/recipe-chatbot/blob/main/homeworks/hw4/README.md).
- Homework 5: Failure Transition Heat-Map: 555 capture words; full; [original](https://github.com/ai-evals-course/recipe-chatbot/blob/main/homeworks/hw5/README.md).
- Homework: Phoenix Tracing Integration for Recipe Chatbot: 925 capture words; full; [original](https://github.com/ai-evals-course/recipe-chatbot/blob/main/homeworks/optional/phoenix-integration/README.md).
- Lesson 6: Custom Failure Mode Inspection Interface: 405 capture words; full; [original](https://github.com/ai-evals-course/recipe-chatbot/blob/main/lesson-7/README.md).
- Notebook index: 370 capture words; full.
- Video walkthrough links: 510 capture words; full.

### E13. Eval Skills and archived predecessor ([original](https://github.com/ai-evals-course/evals-skills))

**Type and length:** Two READMEs, nine skills, and review-loop reference; about 45–65 minutes.

**Capture status:** Full listed files; E13z archived and redirects to maintained repo; external media not captured.

**The point:** Read complete runs and let a knowledgeable human discover concrete failures before writing automated checks. Use code for rules that can be checked directly, and a narrowly focused model judge for rules requiring interpretation.

**Best parts first:** Maintained README/evals-start, about 4 minutes; write-code-eval, about 2 minutes; judge-writing/validation, about 15 minutes.

**Digest:** [source digest](digests/E13-evals-skills.md).

**Capture files:**

- Eval Skills: 571 capture words; full.
- Build a Custom Annotation Interface: 861 capture words; full; [original](https://github.com/ai-evals-course/evals-skills/blob/main/skills/build-review-interface/SKILL.md).
- Error Discovery Skill: 2,386 capture words; full; [original](https://github.com/ai-evals-course/evals-skills/blob/main/skills/error-discovery/SKILL.md).
- Review Loop: 945 capture words; full; [original](https://github.com/ai-evals-course/evals-skills/blob/main/skills/error-discovery/review-loop.md).
- Eval Audit: 1,360 capture words; full; [original](https://github.com/ai-evals-course/evals-skills/blob/main/skills/eval-audit/SKILL.md).
- Evals Start: 303 capture words; full; [original](https://github.com/ai-evals-course/evals-skills/blob/main/skills/evals-start/SKILL.md).
- Evaluate RAG: 1,154 capture words; full; [original](https://github.com/ai-evals-course/evals-skills/blob/main/skills/evaluate-rag/SKILL.md).
- Generate Synthetic Data: 796 capture words; full; [original](https://github.com/ai-evals-course/evals-skills/blob/main/skills/generate-synthetic-data/SKILL.md).
- Validate Evaluator: 1,422 capture words; full; [original](https://github.com/ai-evals-course/evals-skills/blob/main/skills/validate-evaluator/SKILL.md).
- Write a code evaluator: 285 capture words; full; [original](https://github.com/ai-evals-course/evals-skills/blob/main/skills/write-code-eval/SKILL.md).
- Write LLM-as-Judge Prompt: 1,188 capture words; full; [original](https://github.com/ai-evals-course/evals-skills/blob/main/skills/write-judge-prompt/SKILL.md).
- Eval Skills for AI Coding Agents: 502 capture words; full; [original](https://github.com/hamelsmu/evals-skills).

### E14. AgentEvals ([original](https://github.com/langchain-ai/agentevals))

**Type and length:** Combined, TypeScript, and Python READMEs; about 20–30 minutes for one language.

**Capture status:** Full raw READMEs, including duplicate material and code defects; implementation absent.

**The point:** AgentEvals checks an agent's trajectory, the intermediate messages, tool calls, or graph steps in a run. It offers rule-based comparison with a reference run and LLM-as-judge evaluation, where another model grades the run.

**Best parts first:** TypeScript subset/superset and arguments modes, about 7 minutes; model judge, about 5 minutes.

**Digest:** [source digest](digests/E14-agentevals.md).

**Capture files:**

- 🦾⚖️ AgentEvals: 6,375 capture words; full.
- 🦾⚖️ AgentEvals: 4,210 capture words; full; [original](https://github.com/langchain-ai/agentevals/blob/main/js/README.md).
- 🦾⚖️ AgentEvals: 3,901 capture words; full; [original](https://github.com/langchain-ai/agentevals/blob/main/python/README.md).

### E15. Inspect AI documentation bundle ([original](https://inspect.aisi.org.uk/))

**Type and length:** Python framework home, Agent Bridge, and Sandboxing; about 40–50 minutes.

**Capture status:** Full Quarto source; sandbox includes expanded supporting files; source can differ from deployed docs; linked CLI examples absent.

**The point:** Inspect combines task inputs, an answering agent and a scoring rule into a runnable evaluation with logs. Its bridges let existing Python or sandboxed CLI agents call models through Inspect, but the evaluation controls model routing and many request settings.

**Best parts first:** Home examples, about 6 minutes; bridge Models/Generation Config, about 5 minutes; sandbox Example/Docker Configuration, about 7 minutes.

**Digest:** [source digest](digests/E15-inspect-ai.md).

**Capture files:**

- Inspect: 1,315 capture words; full.
- Agent Bridge: 3,507 capture words; full; [original](https://inspect.aisi.org.uk/agent-bridge.html).
- Sandboxing: 4,007 capture words; full; [original](https://inspect.aisi.org.uk/sandboxing.html).

### E16. Video bundle

**Type and length:** Seven captured videos plus an unavailable Loom pointer; durations appear per entry.

**Capture status:** Captions are present for E16a–g; E16h failed.

**The point:** These demonstrations make review and diagnosis concrete. They preserve spoken lessons rather than complete displayed code.

**Best parts first:** E16b’s grouping segment, about 8 minutes, then E16e’s diagnostic segment, about 16 minutes.

**Files and digests:** Listed under each sub-entry below.

#### E16a. Isaac HW 1 & 2 (Session 1) ([original](https://youtu.be/h9oAAAYnGx4))

**Type and length:** Video, July 3, 2025; 1:04:52.

**Capture status:** Full automatic captions; displayed code and chat not captured.

**The point:** Start with a reasonable prompt for a specific audience, then use actual responses to discover what needs changing. Create varied but realistic test queries, record runs, write notes on failures, and group those notes into useful categories.

**Best parts first:** 00:20:27–00:41:16, about 21 minutes; 00:53:08–01:01:41, about 9 minutes.

**Digest:** [source digest](digests/E16a-video-recipe-chatbot-hw1-hw2-code-walkthrough.md).

**Capture files:**

- Isaac HW 1 & 2 (Session 1): 11,597 capture words; full.

#### E16b. Open & Axial Coding: Isaac and Hamel ([original](https://youtu.be/AKg27L4E0M8))

**Type and length:** Video, July 3, 2025; 35:34.

**Capture status:** Full automatic captions; displayed notebook and recipe content not fully captured.

**The point:** Open coding means reading outputs and writing free-text notes about what went wrong. Axial coding means grouping those notes into named failure categories, checking the groups, and counting them.

**Best parts first:** 00:01:47–00:03:56, about 2 minutes; 00:27:22–00:35:26, about 8 minutes.

**Digest:** [source digest](digests/E16b-video-isaac-hamel-open-axial-coding.md).

**Capture files:**

- Open & Axial Coding - Isaac & Hamel Walkthrough: 5,023 capture words; full.

#### E16c. Isaac HW3 (Session 2) ([original](https://youtu.be/1d5aNfslwHg))

**Type and length:** Video, July 3, 2025; 1:22:01.

**Capture status:** Full automatic captions; no full code/charts; spoken correction example is inconsistent.

**The point:** Build a model-based judge for one specific failure, here whether a recipe follows a requested dietary restriction. Human labels, separate datasets and careful inspection matter more than copying a finished solution.

**Best parts first:** 00:19:44–00:22:37, about 3 minutes; 00:33:30–00:41:52, about 8 minutes; 00:48:13–01:00:18, about 12 minutes.

**Digest:** [source digest](digests/E16c-video-recipe-chatbot-hw3-llm-judge-solution.md).

**Capture files:**

- Isaac HW3 (Session 2): 13,932 capture words; full.

#### E16d. Isaac HW 4 (Session 3) ([original](https://youtu.be/GMShL5iC8aY))

**Type and length:** Video, July 3, 2025; 47:52.

**Capture status:** Full automatic captions; full notebook, prompts, and charts absent.

**The point:** Evaluate retrieval, the step that finds information for a model, before blaming the model's final answer. Inspect the source data, test queries, retrieved results, and rewritten queries so that a metric measures useful product behavior.

**Best parts first:** 00:10:25–00:18:57, about 9 minutes; 00:21:34–00:26:17, about 5 minutes; 00:30:47–00:36:59, about 6 minutes.

**Digest:** [source digest](digests/E16d-video-recipe-chatbot-hw4-retrieval-eval-solution.md).

**Capture files:**

- Isaac HW 4 (Session 3): 8,853 capture words; full.

#### E16e. Isaac Homework 5 (Session 4) ([original](https://youtu.be/z1oISsDUKLA))

**Type and length:** Video, July 18, 2025; 54:00.

**Capture status:** Full automatic captions; heatmap/code absent and speaker names uncertain.

**The point:** An agent's later errors may all come from one earlier mistake, so start by finding where the run first broke. Count pairs of last successful step and first failed step in a transition matrix, a table showing how often each pair occurs.

**Best parts first:** 00:17:59–00:20:54, about 3 minutes; 00:21:34–00:37:09, about 16 minutes.

**Digest:** [source digest](digests/E16e-video-recipe-chatbot-hw5-failure-analysis-solution.md).

**Capture files:**

- Isaac Homework 5 (Session 4): 9,780 capture words; full.

#### E16f. How to Automate AI Evals (Correctly) ([original](https://youtu.be/tqUDjc1HzO4))

**Type and length:** Shreya Shankar demo on Hamel’s channel, July 3, 2026; 27:19.

**Capture status:** Full captions marked manual; garbled terms, coarse paragraph timestamps, and no skill code/screenshots.

**The point:** Human review discovers what good output means for a particular product. AI can build the review interface, organize that feedback, and find more examples of failures the human has identified.

**Best parts first:** Published chapter 00:15:10–00:22:53, about 8 minutes; final rules from 00:25:48, about 2 minutes.

**Digest:** [source digest](digests/E16f-video-shreya-error-discovery-walkthrough.md).

**Capture files:**

- How to Automate AI Evals (Correctly): 6,425 capture words; full.

#### E16g. Data and DevOps Tools for Evaluating and Productionizing LLMs ([original](https://www.youtube.com/watch?v=B_DMMlDuJB0))

**Type and length:** Vanishing Gradients with Hamel, Emil, and Hugo, November 4, 2023; 1:04:40.

**Capture status:** Full automatic captions; demonstrations are spoken descriptions; filename differs from captured title.

**The point:** Build an improvement loop around recorded conversations, human review, and tests for failures you actually observe. Rechat demonstrates this with Lucy, an assistant that calls functions to perform real estate tasks, using existing TypeScript infrastructure and a custom review interface.

**Best parts first:** 00:23:20–00:35:36, about 12 minutes; 00:55:11–01:01:34, about 6 minutes.

**Digest:** [source digest](digests/E16g-video-hamel-your-ai-product-needs-evals-talk.md).

**Capture files:**

- Data and DevOps Tools for Evaluating and Productionizing LLMs: 12,870 capture words; full.

#### E16h. Unavailable Recipe Chatbot Phoenix Loom ([original](https://www.loom.com/share/30e5dced1afa467e8714d515694bb3b0))

**Type and length:** Video pointer; title, author, date, and duration unknown.

**Capture status:** Failed; Loom reports unavailable, and no transcript or usable metadata exists.

**The point:** This file records a failed attempt to capture the linked tracing video. The written Phoenix assignment is available, but cannot establish the missing video’s contents.

**Best parts first:** No video segment available; E12 optional Phoenix assignment, about 8 minutes.

**Digest:** None; E12 covers the written tracing assignment.

**Capture files:**

- unknown: 228 capture words; failed.

### F01. Follow-up bundle

**Type and length:** Four written sources; reading budgets appear per entry.

**Capture status:** F01a is partial; F01b–d are full text captures.

**The point:** These sources add method, frontend, tracing, and data-quality detail. Their capture limits differ.

**Best parts first:** F01d’s pitfalls, about 6 minutes, then F01c’s tracing caveats, about 4 minutes.

**Files and digest:** Listed under each sub-entry below; all share the F01 digest.

#### F01a. Building eval systems that improve your AI product ([original](https://www.lennysnewsletter.com/p/building-eval-systems-that-improve))

**Type and length:** Hamel and Shreya guide, September 9, 2025; public portion about 15 minutes.

**Capture status:** Partial public Phases 1–2; Phase 3 and later paid material unavailable.

**The point:** Find recurring failures in real interactions before choosing metrics. Use code for clear rules and a human-validated model judge for judgments.

**Best parts first:** Phase 1, about 5 minutes; judge validation/metrics, about 4 minutes; Agentic workflows, about 2 minutes.

**Digest:** [source digest](digests/F01-follow-up-articles.md).

**Capture files:**

- Building eval systems that improve your AI product: 3,591 capture words; partial.

#### F01b. ALIGN Eval Frontend ([original](https://github.com/eugeneyan/align-app))

**Type and length:** Repository README; under 2 minutes.

**Capture status:** Full README only; implementation and backend absent.

**The point:** ALIGN Eval is a prototype frontend for building and improving model evaluators. It tests prompts against labeled data and offers semi-automatic optimization.

**Best parts first:** What is ALIGN Eval? and Tech Stack, about 1 minute.

**Digest:** [source digest](digests/F01-follow-up-articles.md).

**Capture files:**

- ALIGN Eval Frontend: 223 capture words; full.

#### F01c. Promptfoo Tracing ([original](https://www.promptfoo.dev/docs/tracing/))

**Type and length:** Technical reference; about 25–35 minutes with code.

**Capture status:** Full raw docs; linked providers/examples absent.

**The point:** Tracing records the operations behind each answer. Promptfoo uses these records for workflow assertions, grading, debugging, and adversarial testing.

**Best parts first:** Quick Start/workflow assertions, about 5 minutes; turn markers/Caveats, about 4 minutes; redaction scope, about 5 minutes.

**Digest:** [source digest](digests/F01-follow-up-articles.md).

**Capture files:**

- Tracing: 5,301 capture words; full.

#### F01d. The Revenge of the Data Scientist ([original](https://hamel.dev/blog/posts/revenge/))

**Type and length:** Hamel Husain article, March 26, 2026; about 8 minutes.

**Capture status:** Full article/footnotes; video and slides linked, not transcribed.

**The point:** Calling a model API does not remove the need for sound measurement. Many evaluation mistakes repeat old mistakes in data collection, experiments, and classifier testing.

**Best parts first:** Generic Metrics/Unverified Judges, about 3 minutes; experimental design/labels, about 3 minutes.

**Digest:** [source digest](digests/F01-follow-up-articles.md).

**Capture files:**

- The Revenge of the Data Scientist: 1,885 capture words; full.

## 9. What the deep research report got wrong or missed

E00 is mostly sound as a learning proposal. The issues below distinguish factual correction, an overstatement, and an omission. Source rankings such as best first runner are recommendations, not findings from a comparative study.

- **Wrong course duration:** E00 §2.2 gives 2 hours 16 minutes. The captured E08 course page gives 2h36m. The captures do not explain the difference, so use the captured value and avoid guessing why it changed. [E00 §2.2; E08 §Course Outline]
- **Wrong sequence if its exercise is presented as E09's method:** E00 §2.3 begins with one narrow failure and a judge. E09 first uses expert overall outcome labels and critiques, fixes obvious errors, aligns a judge, and adds specialized judges in Step 7. The exercise works after discovery; it should not replace that discovery. [E09 §§Steps 3–7]
- **Overstated copyability of TypeScript examples:** E00 §3.4 recommends AgentEvals as reusable TypeScript examples. The capture contains a misspelled `satisifes`, undefined variables, and Python `json.dumps` in TypeScript. The ideas are useful; the snippets need checking before execution. [E14b §§Unordered match, Graph trajectory strict match, Evaluate]
- **Incomplete starting guidance for evals-skills:** E00 §3.3 highlights discovery, judge writing, and validation. The maintained README identifies `evals-start` as the entrypoint, and its routing table includes audit and code checks. Those routes depend on what evidence already exists. [E13 README; E13 §evals-start]
- **Missed label convention conflict:** E00 warns about accepting bad work and rejecting good work without explaining that source TPR/TNR names reverse. E06 treats errors as positive; E12 HW3 and E13 treat passes as positive. A combined implementation must define the labels explicitly. [E06 validation answer; E12 HW3 §Key Metrics; E13 validation Step 3]
- **Underexplained judge validation:** E00 mentions hidden examples but omits the full prompt/development/test process, class counts, test contamination, uncertainty, and aggregate-rate correction. E09 and E13 provide the details; E16c shows how noticing optional cheese in a test case contaminates future revisions. [E09 validation FAQ; E13 validation; E16c 00:19:44–00:22:37]
- **Underexplained repeated trials:** E00 recommends repeated attempts but omits the difference between finding one success and getting every attempt right. That distinction matters when deciding whether cheap workers are dependable. [E01 §How to think about non-determinism]
- **Underexplained isolation:** E00 recommends clean states and controlled environments. Promptfoo's copy is not a sandbox; Inspect only confines work sent through its sandbox interface. Provider and host tools remain separate routes. [E11b §Isolated workspaces; E15b §Granted Capabilities; E15c §Example: File Listing]
- **Incomplete model-comparison warning:** E00 §3.5 mentions model routing. Inspect also drops client effort and sampling settings by default, and unmatched background model requests can use the evaluation model. Record both routing and generation configuration. [E15b §§Models, Generation Config]
- **Incomplete HW5 description:** E00 §3.2 calls it failure-pattern analysis, which is fair, but does not say the supplied data contains only failures and classification is already complete. It teaches a diagnostic view, not full reliability measurement or label validation. [E12 HW5 §§What You'll Do, Data Provided]
- **Missing convergence limit:** E00 §2.2 names trajectory evaluation without explaining that the course compares completed paths to the shortest observed path. A wasteful step shared by every run remains invisible. [E08 lesson 9]
- **Missing real versus captured-code boundary:** E00 describes public worked notebooks. E12's local index captures only introductory cells, and E08 lab notebooks require login. Full transcript capture is not a complete code capture. [E12 notebook-index metadata; E08 lab capture notes]
- **Missing review details that prevent drift:** The field guide, FAQ, and later demo emphasize clear domain rendering, revisiting reviewed examples, and confirmed versus suggested labels. E00's small reviewed batch is a starting deliverable, not a completed or permanent taxonomy. [E07 §Maintaining Trust; E13 review-loop; E16f]
- **Missing evidence limits around endorsement and cost:** E02 has five comments, not a popularity survey. Most captures provide no worker cost-per-success method; E00's proposed measure is an adaptation, not something demonstrated by every recommended guide. [E02; E00 §Compare configurations]

## 10. Suggested learning path

Follow the stages in order. Reading and exercise budgets below are estimates for planning, not measured completion times. The deliverables are workspace adaptations. Stop adding infrastructure when the current setup lets you inspect failures, test a change, and explain the result.

- **Stage 1. Understand the task and evidence.** Read part 2, then E01's structure and roadmap Step 2, about 10 minutes. Spend 20–30 minutes writing a contract for one frequent worker role. **Deliverable:** one page naming the input, allowed actions, success rules, stop conditions, and evidence needed to prove completion. Include both must-do and must-not-do cases.
- **Stage 2. Learn to inspect without premature categories.** Watch E03 00:09:56–00:31:39, about 22 minutes, or read E07's error-analysis section and E16b's short examples, about 8 minutes. Spend 45–90 minutes reviewing available runs. Start small, then continue while new patterns appear. **Deliverable:** trace IDs and specific open notes, including uncertain product requirements and the first important upstream failure.
- **Stage 3. Build an actionable failure list.** Watch E03 00:31:39–00:46:06, about 15 minutes, or study E12 HW2 and E13's review-loop, about 8 minutes. Spend 30–60 minutes grouping and checking notes. **Deliverable:** a short taxonomy with definitions, confirmed examples, counts, severity, and an unclassified category. Keep AI suggestions separate until reviewed.
- **Stage 4. Add the first useful code checks.** Read E13 write-code-eval and E11b refactoring/workspace sections, about 12 minutes. Spend 45–90 minutes connecting two or three checks to actual artifacts and recorded actions. Use an existing runner if available. **Deliverable:** repeatable checks that pass known acceptable evidence, reject known bad evidence, and return a reason. A final-message keyword check is insufficient for completion.
- **Stage 5. Practise one multi-step diagnosis.** Choose E12 HW5 plus E16e 00:21:34–00:37:09, about 20 minutes of study, with 30–60 minutes for analysis. If retrieval is the recurring problem, substitute HW4 and E16d's query/source inspection segments. **Deliverable:** a transition table or retrieval result table, two concrete hypotheses, and inspected traces supporting or rejecting them. State what denominator is missing before making rate claims.
- **Stage 6. Validate one judge only if manual review needs scaling.** Read E09's critiques and validation FAQ, then E13's judge prompt and validation steps, about 25 minutes. Label and review criterion-specific examples; budget at least a focused half-day, with more time for difficult standards. **Deliverable:** one criterion, human labels, separate prompt/development/test sets, a frozen prompt, model/version, and both failure recall and good-output acceptance with counts. If labels are insufficient or the standard still changes, keep human review as the result.
- **Stage 7. Run one controlled worker comparison.** Read E11c's provider interface, actual-prompt, and price limits, about 8 minutes. For sandboxed CLI work, also read E15b's Models and Generation Config before running, about 5 minutes. Budget 1–2 hours for setup and inspection, plus actual agent runtime. **Deliverable:** equivalent tasks and starting states, repeated trials, requested/resolved models, quality and scope results, time, measured or estimated cost, and a reason to accept or reject the proposed change.
- **Stage 8. Keep a small working feedback loop.** Read E06's CI/CD and monitoring answers and E08 lesson 14, about 10 minutes. Spend 30–60 minutes assigning suite ownership and deciding which checks run around changes versus sampled review. **Deliverable:** a regression set, a separate harder capability set, review cadence, judge revalidation triggers, and a rule for adding newly confirmed failures. Revisit the definitions when requirements change.

The full E08 course is an optional guided practice route at 2h36m, plus notebook work. It can replace some study in Stages 4–5 if Python and Phoenix are useful teaching aids. It does not replace reviewing the user's own worker runs. E16g is an alternative TypeScript-oriented example: its 00:23:20–00:35:36 segment shows assertions and existing infrastructure without requiring a Python migration. [E08 course page; E16g]

The first useful milestone is a replayable comparison with inspectable evidence. You should be able to name the failure, show the run that exposed it, explain the check, and see whether a change helped without hiding another regression. A dashboard becomes useful only when it makes those decisions easier. [Synthesis of E00, E07, and E16g]
