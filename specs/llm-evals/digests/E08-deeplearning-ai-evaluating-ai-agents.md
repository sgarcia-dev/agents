---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [E08]
purpose: One-source digest feeding the spec compendium.
---

# Evaluating AI Agents (E08)

**What it is:** A beginner video course with coding labs from DeepLearning.AI and Arize AI, taught by John Gilhuly and Aman Khan. Publication date is unknown. The captured page says updated July 16, 2026, 2h36m, 15 video lessons and 6 code examples. [Course page](https://www.deeplearning.ai/courses/evaluating-ai-agents).

**Capture status:** Full course page and full public transcripts for lessons 1–12, according to their frontmatter. Lab notebooks are absent because access requires login. The course-page capture notes say lessons 13–15 were left uncaptured by the packet's 12-transcript limit. This digest covers only the assigned captures. Transcripts have no timestamps and contain some transcription errors, so locations below use lesson titles and topic descriptions. No executable notebook code or package versions can be verified here.

## The point in three sentences

Evaluate the application you are building, including its decisions and intermediate work, rather than relying on a model benchmark or its final answer alone. Record each run, then use code checks, a separate judging model, or human labels to evaluate the router, skills and execution path. Put representative examples and evaluators into repeatable experiments so changes to prompts, models or logic can be compared and regressions found.

## Key ideas

- Model evaluation and application evaluation answer different questions. Your prompts, tools, memory and routing are part of what must be tested: "the LLM is just a part of" the overall application. Location: lesson 2, Evaluation in the time of LLMs, model versus system evaluation.
- Keep representative cases and rerun them after changes. A small prompt edit can help one case and hurt another: "remember to respond politely" is the example edit. Location: lesson 2, regressions.
- Break an agent into a router, skills and shared memory/state. A skill can contain several model or code steps: "entire LLM applications can be thought of as skills". Location: lesson 3, Decomposing agents, skills.
- A trace records one complete run; a span records one step inside it. Nested spans help locate failures and supply evaluation data: "one trace is made of multiple spans". Location: lesson 5, Tracing agents, trace structure.
- Combine automatic tracing of model calls with manual tracing of agent logic. Start outside and work inward: "start from the outermost layer that you want to trace". Location: lesson 6, Lab 2: Tracing your agent, manual tracing.
- Choose the evaluator to match the question. Code checks compare known results or validate formats; a judging LLM handles open-ended qualities; humans provide labels and feedback: "how qualitative versus quantifiable or quantitative is the metric". Location: lesson 7, Adding router and skill evaluations, choosing techniques.
- Judge prompts need explicit criteria and discrete labels, such as correct/incorrect. The course rejects vague numeric scales: "score this response on a scale from 1 to 100." Location: lesson 7, judging labels, presented as the approach to avoid.
- Evaluate tool selection separately from argument extraction. Selecting shipping lookup is sensible, but treating an order number as a tracking ID is wrong: "it succeeded in the function calling task" while parameter extraction failed. Location: lesson 7, order-status example.
- Check intermediate results as well as full skills. SQL generation, SQL execution, analysis clarity and code execution can each need a different check: "one single part of the skill". Location: lesson 7, example agent evaluations.
- Keep judging calls out of the agent traces being evaluated. Otherwise automatic instrumentation also records the evaluator: "turn off tracing for everything happening inside here". Location: lesson 8, Lab 3: Adding router and skill evaluations, suppressing tracing.
- A trajectory is the sequence of decisions and actions. Shorter successful paths can reduce calls, cost and latency: "efficiency matters in this case". Location: lesson 9, Adding trajectory evaluations, why paths matter.
- The course's convergence measure compares similar completed runs with the shortest observed path. It cannot detect a wasteful step repeated in every run: "an unnecessary step every time for every query in your test set". Location: lesson 9, convergence limits.
- An experiment combines examples, a task running a version of the agent, and evaluators. Expected outputs make additional checks possible: "certain code-based evals do require an expected output". Location: lesson 11, Adding structure to your evaluations, dataset design.
- Repeat experiments because a small set and variable responses can mislead. The final lab's prompt change did not clearly improve SQL and other scores fell: "it's always good to do multiple runs of each experiment". Location: lesson 12, Lab 5: Adding structure to your evaluations, comparing V2.

## Per-lesson digest

### 1. Introduction, 3m

The course introduces evaluation-driven development, meaning using measured failures to decide what to improve. Its running example is a sales-data assistant with database lookup, analysis and visualization tools. It will evaluate each part, the router's choices and arguments, and the path through the whole system. The introduction also distinguishes output quality from avoiding loops or unnecessary repeated work.

### 2. Evaluation in the time of LLMs, 7m

Model benchmarks describe a model's performance on benchmark tasks; application evaluations test the combined system. LLM responses vary even for the same prompt, and relevance or coherence may require judgments beyond exact matching. Agents add reasoning, routing and actions. The travel-booking example asks whether the right tool, parameters, context and final response were used. Maintain representative cases and feed real usage back into development to catch regressions.

### 3. Decomposing agents, 6m

The router chooses a skill and decides whether to continue or return to the user. Skills can include model calls, code and external services. Shared memory/state holds context, configuration and previous messages. The example uses GPT-4o-mini function calling, SQL generation and execution, one analysis call, and two visualization calls. Separating chart configuration from code generation narrows each task. The lesson presents simpler routers as more consistent but less capable.

### 4. Lab 1: Building your agent, 16m

Build and test the three tools before wiring them into the router. Load a local Parquet sales file with pandas, prepare a DuckDB table, generate SQL and execute it. Add analysis, then use pydantic and Structured Output to constrain chart type, axes and title before generating Python. Define tool and parameter descriptions, dispatch calls in a loop, and append tool results with matching call IDs. The agent returns visualization code; the lesson advises an enclosed environment when executing generated code.

### 5. Tracing agents, 4m

Observability means seeing what happens inside an application. Record prompts, responses, token use and surrounding operations as nested traces and spans. OpenTelemetry supplies the tracing concepts and instrumentation conventions. Phoenix receives and displays traces and later supplies evaluation data. Manual code blocks or decorators identify application steps; automatic instrumentation captures calls through supported libraries. The value is both debugging a single run and collecting examples across many runs.

### 6. Lab 2: Tracing your agent, 16m

Connect to a Phoenix project and endpoint, enable automatic OpenAI instrumentation, and obtain a tracer for manual spans. Wrap the whole run, then router iterations, tool dispatch and tools. Add inputs, outputs and status. Use decorators for complete functions and a code block for a portion such as SQL execution. Inspect the trace after initial instrumentation and again after adding detail. Separate SQL generation from execution so a database problem can be located independently.

### 7. Adding router and skill evaluations, 12m

The lesson compares code checks, LLM judges and human labels, including labor costs and selection bias in voluntary user feedback. Judges should receive the relevant inputs, outputs, criteria and tool definitions, then return named labels. Router checks cover both tool choice and arguments. Suggested skill checks include SQL correctness, analysis clarity and entity correctness, meaning preserving what identifiers refer to, and runnable visualization code. Claims that human labels are deterministic or offer 100% accuracy are the lesson's assertions, not demonstrated results.

### 8. Lab 3: Adding router and skill evaluations, 17m

Run sample questions and export the relevant spans from Phoenix. Match dataframe column names to judge-template variables, preserve span IDs, classify rows, add numeric scores and upload evaluations. Use GPT-4o for tool-calling judgment and suppress tracing of judge calls. Check visualization code by executing it and catching exceptions. Add custom clarity and SQL judge prompts. The lab scores clarity from top-level agent outputs, so that check is broader than an isolated analysis-tool evaluation.

### 9. Adding trajectory evaluations, 5m

Measure paths as well as answers because extra calls can add latency, cost and variation. Run related queries that should need the same path, count steps, and use the minimum observed length as the reference for convergence. The score runs from 0 to 1; 1 means every included run follows that minimum length. Exclude incomplete or errored runs. The reference is observed, not proof of the best possible path, and shared unnecessary steps remain invisible to this measure.

### 10. Lab 4: Adding trajectory evaluations, 9m

Create a Phoenix dataset of variations on average items per transaction. Define a task that runs the agent and returns its messages and path length. Run an experiment, read its outputs, calculate the minimum length, and apply a path-length evaluator. This lab counts messages, including system and user messages, so consistent counting matters. Its displayed minimum is five and displayed convergence is one, but the instructor says results vary between runs. Notebook code is not included in the capture.

### 11. Adding structure to your evaluations, 7m

Build representative examples, run agent variants, evaluate them, and compare results. Start with manually constructed cases and add live examples later. Include expected outputs where possible. Test prompts, tool descriptions, router logic, skill structure or models. A component dataset must include that component's actual inputs: the analysis tool needs both a question and retrieved data. A dashboard can show each experiment against all evaluators, exposing changes that improve one part and harm another.

### 12. Lab 5: Adding structure to your evaluations, 15m

Combine a question dataset with expected SQL results and generated SQL, an agent task, and five evaluators. Judge tool calls, clarity and entity correctness; compare SQL-result numbers with expected numbers; execute generated visualization code. Average tool-call scores when a run contains multiple calls. Seven tasks produce 35 evaluator applications. Then change the SQL prompt, rerun as V2 and compare. The change does not clearly help. Repeat runs and use the Phoenix playground for direct prompt comparisons.

## How to do it (concrete steps, checklists, templates)

The captured course gives this sequence:

1. Build the sales assistant's lookup, analysis and visualization tools. Test each directly. Add the router's tool definitions, system prompt, message history and dispatch loop. Return tool results using their corresponding call IDs. Location: lab 1.
2. Connect Phoenix tracing. Enable automatic model-call instrumentation, wrap the outer run and then add router, tool and internal-step spans. Set inputs, outputs and status, and inspect the result. Location: lab 2.
3. Run example queries and export spans for the component being evaluated. Filter by span kind, name, attributes or prompt content. Preserve the span ID and make dataframe headers match evaluator variables. Location: lab 3.
4. For router judging, supply the user's question, chosen call and all tool definitions. Define correct/incorrect labels, ask for explanations, suppress evaluator tracing and map labels to 1/0 scores. Upload the results and inspect incorrect cases. Location: lab 3.
5. Add runnable-code, response-clarity and SQL-generation checks. Export each check's relevant outputs and upload labels against the original spans. Location: lab 3.
6. Build similar queries for convergence. Run them through a task that returns messages and path length, find the minimum among completed runs, evaluate lengths against that reference and view results. Use a consistent definition of a step. Locations: lesson 9 and lab 4.
7. Create a broader dataset with questions and available expected outputs. Define a task and evaluators, run them together, inspect scores and individual cases, change the agent, and rerun as a named variant. Repeat experiments and add new live cases over time. Locations: lesson 11 and lab 5.

Judge-template ingredients, not a recovered executable prompt: task instructions; question and observed output/call; allowed labels; definitions of those labels; and, for router checks, all available tool definitions. The transcripts describe the templates but do not reproduce complete notebook text.

## Tools, code and commands named

- Agent and data: Python, OpenAI library/client, GPT-4o-mini, Pandas/pandas, Json, duckDB/DuckDB, pydantic, Parquet, SQL, OpenAI function calling and Structured Output. Location: lessons 3–4.
- Tracing: Arize Phoenix, OpenTelemetry/OTEL, Open Inference, OpenAI instrumentor, LlamaIndex and LangChain. The transcript spells a distributed-routing framework as "line graph" and also names OpenAI swarm; that spelling is not enough to verify the intended framework name. Locations: lessons 3, 5–6.
- Literal tracing notation includes `@tracer.chain` and escaped `start\_as\_current\_span`. Other methods are often spoken as words rather than written identifiers. Location: lab 2.
- Evaluations: Phoenix evals, `nest\_asyncio` in the capture, LLM classify, span query, dropna, rails, log evaluations, run experiment, evaluate experiment, create evaluator and the Phoenix playground. These are transcript names, not verified API signatures. Locations: labs 3–5.
- Judge-model examples: GPT-4o and Claude3.5 Sonnet. GPT-4o is used for router judgment in lab 3. These are course examples, not a current model recommendation. Location: lesson 7 and lab 3.
- Benchmarks mentioned: MMLU and "human eval". Retrieval augmented generation, shortened to RAG, means retrieving context before generating a response. Locations: lessons 2–3.

No installation commands, package versions or full executable listings are supplied in these captures.

## Numbers and strong claims

- Course page, Course Outline and summary: 2h36m, 15 video lessons, 6 code examples and 1 PRO graded assignment. The captured list contains 17 entries when quiz and appendix are included. Page update: July 16, 2026; initial publication unknown.
- Lesson 7: judges are "never going to be 100% accurate". Its contrasting advice to use humans or code when needing 100% accuracy, and description of human labels as deterministic, are strong teaching assertions without validation evidence here.
- Lesson 7: "only really the best models actually align closely with human judgment". Opinion/general claim; the capture supplies model examples but no comparison data.
- Lesson 11: start with "1 or 2 examples" from each input type. This is a starting heuristic, not a demonstrated sufficient sample size. Lab 5 separately advises repeated runs.
- Lesson 9: convergence lies between 0 and 1; 1 means all included paths match the observed minimum. Six versus 11 steps is an illustrative efficiency comparison, not measured savings.
- Lab 4: 17 agent runs, an expected minimum path length of five messages and a displayed score of one. Example results vary across executions.
- Lab 5: seven tasks and five evaluations per case, totaling 35 evaluations. This is not necessarily 35 model calls because some evaluators use code and tool-call judging may score multiple calls.
- Course page: becoming able to "systematically evaluate them, and improve their performance" is a course promise, not measured learner-outcome evidence. Free access "for a limited time" is a captured access statement, not a verified current offer.

## Compared with the deep research report

Only section 2.2 about this course was used for this comparison.

- **Right:** The report identifies the instructors, Arize collaboration, Python requirement and progression through "individual components, execution trajectories, and structured experiments". The course page agrees: "Run structured experiments" and evaluate skills and router decisions. Its emphasis on tracing and component diagnosis fits the labs.
- **Wrong or outdated:** The report says "2 hours 16 minutes"; the captured course page says "2h36m". The captures do not explain the difference.
- **Sensible interpretation:** The report calls the observability stack "a teaching vehicle". The captures use Phoenix throughout, but lesson 7 says evaluator techniques apply to both agents and other LLM applications. Treat portability as an interpretation, not evidence that every harness integration is provided.
- **Important omissions:** The report's phrase "trajectory evaluation" leaves out the specific convergence method and its blind spot. Lesson 9 explicitly warns about "an unnecessary step every time". It also omits distinct parameter-extraction failures, discrete judge labels, suppressing judge traces, span-ID linkage and repeated experiments.
- **Access detail:** The report says "Enrollment is account-based". Lab capture notes more specifically state "Notebook content is not included; notebook access requires login." Public transcripts were available for this packet, but it cannot substitute for the missing code. Certificate value is the report's advice, not a claim verified by these transcripts.

## Fit for the user's agent workspace

- (inference) Treat the root's choice of worker or skill as a routing decision. Separately check the packet arguments and context sent to that worker, since the right worker can receive the wrong inputs.
- (inference) Record each bounded worker run with its packet, output and internal actions where the harness exposes them. This adapts traces and spans without requiring a Phoenix migration.
- (inference) Use code for measurable requirements such as output format and required files. Use explicit judge labels for whether a worker answered the task and stayed within its assigned scope. Scope grading is an adaptation; the example course does not implement it.
- (inference) Keep a small representative packet dataset with expected results where possible. Run it unchanged when comparing worker models, prompts or skill instructions, and inspect failures rather than relying only on averages.
- (inference) Track successful output separately from calls, steps and latency when asking whether a cheap worker was worth its cost. The course motivates cost through fewer calls but gives no pricing or cost-per-success calculation.
- (inference) Apply convergence only within similar task families and with successful completion checked separately. Matching the shortest observed run does not establish correct work or prove an optimal delegation policy.
- (inference) Skip copying the Python sales agent as the workspace architecture. Copy its decomposition and experiment discipline, then implement checks against the workspace's real Markdown and TypeScript work.

## Best parts to read or watch first

Times are displayed video durations, not estimated transcript-reading times. Lesson headings provide locations because timestamps are absent.

- **Adding router and skill evaluations, lesson 7, 12m:** evaluator choice, label design and the order-ID/tracking-ID failure.
- **Tracing agents, lesson 5, 4m; Lab 2, lesson 6, 16m:** the trace/span model and how to instrument nested steps.
- **Adding trajectory evaluations, lesson 9, 5m; Lab 4, lesson 10, 9m:** convergence, its limitations and consistent message counting.
- **Adding structure to your evaluations, lesson 11, 7m; Lab 5, lesson 12, 15m:** representative datasets, expected results and comparing changes across multiple evaluators.
- **Lab 3, lesson 8, 17m:** exporting/filtering spans, preserving IDs, suppressing judge traces and inspecting incorrect cases.
