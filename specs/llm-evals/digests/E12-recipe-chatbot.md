---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [E12]
purpose: One-source digest feeding the spec compendium.
---

# Recipe Chatbot: AI Evaluations Course (E12)

**What it is:** A Python-oriented learning repository with five progressive homework assignments, an annotation interface, four notebook walkthroughs, and optional tracing work. Author and publication date are unknown in the captures. [Repository](https://github.com/ai-evals-course/recipe-chatbot). No course duration or video runtimes are supplied.

**Capture status:** All eleven captures say `full`, from repository snapshot `e08dec0`, captured on 2026-10-13. This means full captured README text and full indexes, not full course content. The notebook index explicitly includes only the first Markdown cell of each of four notebooks. Remaining cells, implementation files, datasets, referenced course sections, and video transcripts are absent from this packet. The video index preserves six video URLs and one student portal link without resolving login access.

## The point in three sentences

Start by defining expected behavior, collecting realistic queries, and reading the resulting conversation records. Turn observed mistakes into named failure categories, then build a narrow model judge and measure its mistakes against human labels. Evaluate retrieval separately, count where agent pipelines fail, and add tracing when you need to inspect running conversations.

## Key ideas

- Make the starting prompt concrete about role, required behavior, forbidden behavior, creativity, and response structure. HW1 says, "Be specific." Location: Part1, Response Rules.
- Generate test queries from dimensions that matter, then review whether combinations and wording resemble real requests. HW2 asks, "Review the queries. Do they sound realistic?" Location: Part 1, Step 3.
- Open coding means writing free-form observations before assigning categories. HW2 says, "Note patterns, errors, and anything unusual." Location: Part 2, Step 2.
- A taxonomy is a set of named failure categories. Build it from observations, with a title, one-sentence definition, and examples; the assignment also permits hypothetical examples. "Group your observations into failure modes." Location: HW2, Part 2, Step 3.
- Keep manual review simple. The annotation tool stores free-form notes and categorical labels in each trace JSON file, then advances to the next record. "Press Save (or Ctrl+Enter) to save and advance to the next trace" Location: Annotation Tool, Workflow.
- A model judge is an LLM asked to decide whether another model's response meets a criterion. HW3 focuses on dietary adherence but permits another HW2 failure category: "You'll need to define your own criteria and generate your own traces." Location: What You Get, Alternative.
- Human labels come before judge tuning. Train examples go into the prompt, development examples guide revisions, and test examples measure the final judge. "Report final TPR and TNR on your Test set" Location: HW3, Step 4. TPR measures correctly accepted adherent recipes; TNR measures correctly rejected non-adherent recipes.
- Judge pass rate and estimated system success rate are different outputs. HW3 uses `judgy` to account for judge errors and report uncertainty. "True adherence rate accounting for judge errors" Location: Key Metrics, Corrected Success Rate. The capture does not provide the correction formula or its assumptions.
- RAG means retrieving information to support generation. HW4 evaluates the retrieval component with queries tied to the recipe that supplied the relevant fact. "Save with the source recipe ID for evaluation" Location: Step 2.
- BM25 is the keyword-based retrieval method used here. Test whether the source recipe appears near the top, then inspect which query types work poorly. "Compare baseline BM25 with agent-enhanced retrieval and report improvements." Location: HW4, Optional: Query Rewrite Agent.
- A transition matrix counts pairs of pipeline states. HW5 pairs the last successful state with the first failed state, separating tool argument construction from tool execution. "All classification work has already been done for you." Location: What You'll Do. This exercise teaches analysis of supplied labels, not how to produce reliable labels.
- HW5's records are selected failures. "Every conversation trace contains one failure." Location: What You'll Do. Its heatmap shows the distribution of those failures, not the success rate of all agent runs.
- Session tracing connects turns and child operations into one conversation. The Phoenix assignment carries a session ID from frontend to backend and into tracing contexts. "Ensuring the session ID is included in every chat request" Location: Part 2, Step 3, Your Task.
- The inspection lesson offers CSV conversion today and describes additional interface work as future work. "Interactive web interface for marking additional failure modes" Location: Lesson 6, Future Features. Do not treat this as evidence of a finished inspection application.

## How to do it (concrete steps, checklists, templates)

### Start the application, then do HW1

1. Clone the repository, enter it, run `uv sync`, and activate `.venv`.
2. Copy `env.example` to `.env` and set model names and API keys.
3. Start the backend with the README command listed below and open `http://127.0.0.1:8000`.
4. Replace `backend/system_prompt.md`. Define role and objective, always/never rules, a safety clause, permission to invent or substitute recipes, and output formatting. The suggested layout is a level-two recipe heading, a 1-3 sentence description, `### Ingredients`, `### Instructions`, and optional notes or tips.
5. Add at least ten diverse queries with unique IDs to `data/sample_queries.csv`. Include cuisines, dietary restrictions, ingredients, meal types, time constraints, skill levels, and ambiguity.
6. Run the bulk test, confirm a new JSON result exists, and inspect responses. HW1 supplies an optional prompt to generate a self-contained HTML viewer.

### HW2: discover failure categories

1. Pick 3-4 query dimensions, each with at least three values.
2. Ask an LLM for 15-20 combinations and discard unrealistic ones.
3. Ask for natural language queries from 5-7 combinations and review realism. Alternatively, use the provided query/response file.
4. Run the bot and save full conversation traces, meaning records of the conversation and its operations.
5. Read traces and write open coding notes.
6. Group observations into failure modes. Use the taxonomy template: title, one-sentence definition, and 1-2 observed or well-reasoned hypothetical examples.
7. Optionally track `Trace_ID`, `User_Query`, `Full_Bot_Trace_Summary`, `Open_Code_Notes`, and one 0/1 column per failure mode in a spreadsheet.

The annotation interface adds a concrete review sequence: open the trace list, select a conversation, write notes, select or create a category, then save. Annotations are saved in place. Its JSON fields include `request`, `response`, `id`, `open_coding`, and `axial_coding_code`. Axial coding means grouping observations into categorical labels. A supplied Python example converts JSONL, one JSON object per line, into individual trace files.

### HW3: build and check a judge

Choose full implementation, supplied raw traces, or supplied labeled examples. Then follow the assignment's order:

1. For the first two options, label 100-200 traces Pass or Fail.
2. Split labels into Train 10-20%, Dev 40%, and Test 40-50%.
3. Write a judge prompt with the task, criterion, clear Pass/Fail definitions, 2-3 examples from Train, and a JSON output format containing reasoning and the label.
4. Run on Dev, measure TPR and TNR, and refine. Report final TPR and TNR on Test.
5. Judge 500-1000 new traces.
6. Use `judgy` to report raw pass rate `p_obs`, corrected success rate `θ̂`, a 95% confidence interval, and 1-2 paragraphs interpreting the result. A confidence interval expresses uncertainty around the estimated rate; this capture calls it a range and supplies no calculation details.

The dietary reference is attributed to OpenAI o4 in the source. Its examples are assignment criteria, not independently established dietary guidance in this packet.

### HW4: evaluate retrieval

1. Download and clean recipe data, parsing ingredients, steps, tags, and nutrition. Combine text fields for indexing and save JSON. Or start with the supplied processed recipes.
2. Extract salient facts with an LLM, generate realistic questions requiring those facts, and retain source recipe IDs. Or start with supplied synthetic queries.
3. Build a `rank-bm25` index from recipe name, ingredients, and steps. Return top-k results with scores.
4. For each query, search and check the source recipe's rank. Report Recall@1, Recall@3, Recall@5, and MRR. Here Recall@k checks whether that target appears among the first k results. MRR means Mean Reciprocal Rank, averaging the inverse target rank.
5. Report overall results, stronger and weaker query types, and improvement ideas.
6. Optionally extract keywords, rewrite queries, or add synonyms with an LLM. Compare against baseline BM25.

### HW5: locate pipeline failures

1. Inspect the supplied 96 labeled traces and state list.
2. Count each `(last_success_state, first_failure_state)` pair.
3. Plot rows as last success and columns as first failure. The starter script writes `results/failure_transition_heatmap.png`.
4. Ask which states fail most, whether failures cluster around arguments or execution, and whether uncommon transitions are surprising.
5. Deliver the PNG and a short findings write-up.

The ten states, in listed order, are `ParseRequest`, `PlanToolCalls`, `GenCustomerArgs`, `GetCustomerProfile`, `GenRecipeArgs`, `GetRecipes`, `GenWebArgs`, `GetWebInfo`, `ComposeResponse`, and `DeliverResponse`. No new LLM calls or data generation are required.

### Optional Phoenix tracing, then inspection

After the referenced production-monitoring lesson:

1. Add Phoenix dependencies, install them, and launch `phoenix serve`.
2. Generate frontend session IDs using a timestamp and random string. Include the ID in chat requests and update it from server responses.
3. Create `backend/tracing.py`, instrument LiteLLM, call `register()` with a project name and auto-instrumentation, and return a tracer.
4. Add session IDs to request/response objects in `backend/main.py`. Create a `chat_turn` span, a recorded operation, with agent kind and input/output attributes. Propagate the session through `using_session()` and call `get_agent_response` inside that context.
5. Run the chatbot, try several conversations, and verify Spans, Traces, and Sessions groupings in Phoenix. Then try annotation and adding traces to a dataset.

Separately, the lesson under `lesson-7/` says to install dependencies, run CSV conversion, and inspect the resulting spreadsheet. Its columns include trace ID, persona, failure mode/category, initial query, conversation messages, tool calls, and overall success.

## Tools, code and commands named

The application uses FastAPI, LiteLLM, HTML/CSS/JS, and a FastHTML annotation tool. Learning materials use Jupyter notebooks and Python. Retrieval uses `rank-bm25`; judge correction uses [`judgy`](https://github.com/ai-evals-course/judgy). Tracing names Arize Phoenix, `arize-phoenix-otel`, `openinference-instrumentation-litellm`, `openinference-instrumentation`, `LiteLLMInstrumentor`, `register()`, `using_session()`, and `SpanAttributes`. No dependency versions are pinned in these captures.

Exact command forms supplied include:

```bash
git clone https://github.com/ai-evals-course/recipe-chatbot.git
cd recipe-chatbot
uv sync
source .venv/bin/activate
cp env.example .env
uv run uvicorn backend.main:app --reload --reload-include '*.md'
uv run python scripts/bulk_test.py
cd annotation
uv run python annotation.py
cd homeworks/hw2
jupyter notebook hw2_walkthrough.ipynb
uv pip install -r requirements.txt
uv pip install rank-bm25 tqdm litellm python-dotenv
uv pip install numpy matplotlib seaborn
cd homeworks/hw5
python analysis/transition_heatmaps.py
pip install -r requirements.txt
phoenix serve
uvicorn backend.main:app --reload
cd lesson-7
python scripts/convert_traces_to_csv.py
```

These are source commands for different working directories, not one sequential script. The root README also names `python annotation/annotation.py` and `python scripts/bulk_test.py`.

Environment variables: `MODEL_NAME`, `MODEL_NAME_JUDGE`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `PHOENIX_COLLECTOR_ENDPOINT`, and `PHOENIX_ENDPOINT`. Example model strings are `openai/gpt-5-chat-latest`, `anthropic/claude-3-sonnet-20240229`, `openai/gpt-5-mini`, and `anthropic/claude-3-haiku-20240307`. These are captured examples, not model recommendations.

## Numbers and strong claims

- HW2, File Structure: 250 query/response pairs are offered as a starting point. Its generation targets are 3-4 dimensions, at least three values each, 15-20 combinations, and 5-7 query conversions.
- HW3, What You Get versus Option 2: the source says approximately 2000 traces, then approximately 2400 raw traces. It also lists 60 challenging queries and 101 labeled examples. Preserve the differing approximations rather than inventing one exact total.
- HW3, Our Results: raw success `0.857` (85.7%), corrected success `0.926` (92.6%), 95% interval `[0.817, 1.000]`, and correction `0.069` (6.9 percentage points). The claim that judge bias was successfully accounted for is the source's interpretation. This packet lacks the underlying calculations needed to verify it.
- HW4, Dataset and Starting Points: 180K+ recipes in the full dataset; supplied subsets have 200 recipes and 200 queries. The dataset is attributed to Majumder et al. (2019), EMNLP-IJCNLP 2019.
- HW4, Expected Results: Recall@5 of 60-80% and MRR of 0.4-0.7 are stated as typical. These are unverified expectations in this capture, not measured results for the user's system.
- HW5, Data Provided: 96 traces and ten canonical states. Inspection lesson, Usage Example: 118 failed-conversation rows from a differently named input path. The captures do not reconcile these datasets.
- Root README, Course Philosophy: "Industry-standard techniques" is promotional wording, not evidence of a standard. HW3's claim that labeling is undervalued is practitioner opinion.
- Naming mismatch: the `lesson-7/README.md` capture calls itself Lesson 6. Its interactive interface and integration features are explicitly future work.

## Compared with the deep research report

Only E00 section 3.2, about this repository, was read for this comparison.

- **Right:** E00 says "progressive exercises, worked notebooks, and linked video walkthroughs". E12's Running Homework Walkthroughs says "self-contained Jupyter notebook walkthrough" and lists HW2-HW5. The notebook index confirms four notebook introductions; the video index confirms links. This packet cannot verify the omitted solution code or video content.
- **Right:** E00 recommends HW2 for "Inspecting failures and organizing them into categories." E12 says "Find and categorize the ways your Recipe Bot fails." Its HW3 and retrieval summaries also match the assignments.
- **Too broad if read as a complete tracing exercise:** E00 describes HW5 as "Investigating agent traces and failure patterns." That is fair, but E12 narrows the task: "All classification work has already been done for you." It also supplies only failed traces. HW5 does not teach labeling from scratch or estimate overall agent reliability.
- **Omitted:** E00 does not explain the split, judge-error correction, or uncertainty reporting. E12 explicitly asks for "Raw pass rate (p_obs)" and "95% Confidence Interval" alongside the corrected rate.
- **Omitted:** E00 leaves out the annotation workflow, optional Phoenix session tracing, and inspection lesson's unfinished features. E12 marks "Bulk annotation tools" under Future Features. No direct factual error in E00's short repository description is established by these captures.

## Fit for the user's agent workspace

- (inference) Copy HW2's observation-first workflow for a batch of bounded worker runs. Define failure categories after reading outputs and operation records.
- (inference) Adapt test dimensions to packet size, task type, permission scope, output format, and harness. Review generated cases for realism before using them.
- (inference) Reuse the annotation fields and spreadsheet pattern. A plain JSON/CSV review workflow fits the workspace before a hosted interface is needed.
- (inference) Adapt HW3 to one criterion, such as whether the worker stayed within its packet. Human labels and held-out test examples should precede trust in automated judging.
- (inference) Adapt HW5's argument-versus-execution distinction to worker stages. Include successful runs separately if the goal is a success rate, since this homework contains only failures.
- (inference) Save HW4 for evaluating search or memory retrieval. Its source-ID check is a starting exercise, while this packet gives no method for judging multiple equally useful documents.
- (inference) Skip Phoenix initially unless conversation grouping becomes difficult. The captures give no cost-per-task, token accounting, latency comparison, or worker value-for-money procedure; that part of the user's objective remains uncovered.

## Best parts to read or watch first

Times below are digest reading estimates, not source-provided durations. Exercise completion times and video runtimes are unknown.

- **HW2, Part 2: Find and Categorize Errors**, about 3 minutes. Read the review and taxonomy sequence first. [Coding video](https://youtu.be/AKg27L4E0M8), runtime unavailable.
- **HW3, Steps and Key Metrics**, about 5 minutes. Most useful for understanding why a judge needs its own evaluation. Then read Our Results, about 1 minute. [Walkthrough](https://youtu.be/1d5aNfslwHg), runtime unavailable.
- **HW5, Data Provided, Pipeline State Taxonomy, and Steps**, about 4 minutes. A small analysis exercise with no new model calls. [Walkthrough](https://youtu.be/z1oISsDUKLA), runtime unavailable.
- **Annotation Tool, Data Format and Workflow**, about 3 minutes. Concrete fields and review controls worth adapting.
- **HW4, Steps and Optional: Query Rewrite Agent**, about 4 minutes when retrieval becomes relevant. [Walkthrough](https://youtu.be/GMShL5iC8aY), runtime unavailable.
- **Phoenix, Steps 3-6**, about 8 minutes if session tracing is needed. Code includes TODOs, so it is an implementation assignment. [Overview video](https://www.loom.com/share/30e5dced1afa467e8714d515694bb3b0), runtime unavailable.
