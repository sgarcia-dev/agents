---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [E14, E14b, E14c]
purpose: One-source digest feeding the spec compendium.
---

# AgentEvals (E14, E14b, E14c)

**What it is:** Three README captures from the LangChain AI GitHub repository: [combined README](https://github.com/langchain-ai/agentevals), [TypeScript README](https://github.com/langchain-ai/agentevals/blob/main/js/README.md), and [Python README](https://github.com/langchain-ai/agentevals/blob/main/python/README.md). Individual author and publication date are unknown in all three captures. Captured 2026-10-13. About 14,486 whitespace-separated words including code and metadata, with substantial duplication. Allow roughly 20 to 30 minutes for one language's walkthrough, an estimate rather than a source-provided duration.

**Capture status:** Full for all three. Each frontmatter says “Verbatim raw README; no content missing.” Linked documentation, package implementation, and screenshot contents are not supplied as separate captures. Full capture does not mean the examples are correct.

## The point in three sentences

AgentEvals checks an agent's trajectory, the intermediate messages, tool calls, or graph steps in a run. It offers rule-based comparison with a reference run and LLM-as-judge evaluation, where another model grades the run. Its most useful lesson is to choose exactly what must match: order, allowed tools, required tools, arguments, or overall reasoning.

## Key ideas

- Evaluate the path through the task. The package focuses on actions taken before the final answer, rather than offering a complete evaluation system for every output type. Quote: “or the intermediate steps an agent takes as it runs.” (E14, introduction.)
- Message traces have a common input format. Supply OpenAI-style messages or LangChain message objects, including tool names and arguments. Quote: “as a list of LangChain `BaseMessage` classes” (E14, Agent trajectory match.)
- Strict matching checks order and tool calls, while allowing prose differences. It suits workflows where a lookup must precede an action. Quote: “Note that it does allow for differences in message content:” (E14, Strict match.)
- Unordered matching permits a different route through the same tool calls. It does not establish a required before/after relationship. Quote: “the same tool calls in any order.” (E14b, Unordered match.)
- Superset matching checks required calls while allowing extra calls. Subset matching restricts calls to those in the reference, but by itself does not require all reference calls to occur. Quote: “an agent calling extra tools is still acceptable.” (E14, Subset and superset match.)
- Argument equality is a separate choice from trajectory equality. The default requires exact arguments; ignoring arguments or accepting a subset/superset changes what counts as the same call. Quote: “all tool call arguments are the exact same by default.” (E14, Tool args match modes.)
- Per-tool overrides allow selective tolerance. A field list limits which arguments must match; a comparator function can accept case differences for one tool. Quote: “a comparator function that takes two arguments and returns whether they are equal:” (E14c, Tool args match modes.)
- A model judge can work without an ideal reference run. A reference-aware prompt is also provided for comparing meaning rather than exact strings. Quote: “it doesn't require a reference trajectory.” (E14b, Trajectory LLM-as-judge.)
- Judge scoring can be changed. Continuous scoring returns a number between zero and one; choices restrict scores, a system prompt gives instructions, and example judgments guide the model. Quote: “examples of good and bad outputs.” (E14c, Trajectory LLM-as-judge.)
- Graph traces record visited nodes, the named steps in a graph-based agent. Their `results` and `steps` describe each turn, including interruptions and resumed work. Quote: “nodes visited rather than messages.” (E14, Graph trajectory.)
- Custom graph prompts need the combined conversation variable. Graph judges combine input and output into a `thread`; references use the same graph shape as outputs. Quote: “your prompt should also contain a `thread` input variable:” (E14c, Graph trajectory LLM-as-judge.)
- Graph strict matching checks the step sequence rather than the answer. Its example supplies an empty results list because results are not used for this check. Quote: “# not used for strict match” (E14c, Graph trajectory strict match, reference example.)
- Evaluators can feed an experiment history. LangSmith offers test-runner integration and dataset evaluation; the standalone quickstart calls an evaluator directly. Quote: “For tracking experiments over time” (E14b, LangSmith Integration.)

## How to do it (concrete steps, checklists, templates)

These are the source's procedures, in their presented order. They describe documentation examples, not code verified by this digest.

**Quickstart and installation**

- Install `agentevals` with the command for your language.
- For the model-judge quickstart, set `OPENAI_API_KEY`.
- Import the trajectory judge factory and `TRAJECTORY_ACCURACY_PROMPT`.
- Create the judge with `model: "openai:o3-mini"` in TypeScript or `model="openai:o3-mini"` in Python.
- Supply messages covering the user request, assistant tool call, tool result, and assistant answer. The supplied weather trace is fake; the README says to run your agent to get a real trace.
- Call the evaluator with `outputs` and inspect the score. Later examples show `key`, `score`, and `comment`; the Python quickstart instead labels its explanation `reasoning`.
- Installation then describes LangChain model integrations and the optional direct OpenAI client.

**Reference matching**

- Prepare actual `outputs` and expected `referenceOutputs` in TypeScript, or `reference_outputs` in Python.
- Create `createTrajectoryMatchEvaluator` or `create_trajectory_match_evaluator`.
- Select `strict`, `unordered`, `subset`, or `superset` according to the behavior being checked.
- Configure argument matching if exact equality is unsuitable. Tool-specific overrides take precedence over the general argument mode.
- Call the evaluator with both trajectories and inspect its Boolean score, a true/false result.

**Model judging**

- Create a trajectory judge with the accuracy prompt and a model.
- For reference comparison, use `TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE` and supply the reference trajectory.
- Customize the prompt and score using the listed parameters. Examples contain inputs, outputs, reasoning, and score.

**Graph evaluation**

- Set up a LangGraph agent with a tool, `MemorySaver`, and an interrupt, a pause for external input.
- Invoke the graph with a thread ID, then supply the answer that resumes the interaction. Python uses `Command(resume=...)`; the TypeScript example supplies another user message.
- Extract the thread trajectory using the provided utility.
- Pass extracted inputs and outputs to the graph judge.
- If customizing its prompt, include `{thread}` and use a graph-shaped reference when supplied.
- Alternatively, provide expected nested `steps` lists to the graph strict matcher.

**Async and experiment logging**

- For Python asynchronous calls, use the documented async factory convention and `await`; pass `AsyncOpenAI` as `judge` when using that client directly.
- For LangSmith test integration, follow the linked setup instructions and set `LANGSMITH_API_KEY` and `LANGSMITH_TRACING`.
- Create `test_trajectory.py` or `test_trajectory.eval.ts`. Log inputs, outputs, and references through the test integration, then call the evaluator.
- Run the supplied pytest or Vitest command. The README says feedback appears in the terminal and LangSmith experiment view.
- Alternatively, create a LangSmith dataset and call `Client.evaluate` or `evaluate` with a target function, dataset, and evaluators.

**Example defects to account for**

- E14b, Unordered match: “satisifes” is a misspelled TypeScript keyword. Actual arguments use `SF`, references use `San Francisco`, yet the displayed result is true without an argument override. That conflicts with the documented exact-argument default.
- E14b, Graph trajectory strict match: “outputs: trajectory.outputs,” and “referenceOutputs: referenceOutputs!,” use names not defined in that example. It defines `extractedTrajectory` and `referenceTrajectory` instead.
- E14b, Evaluate: “arguments: json.dumps({"city": "SF"}),” uses Python syntax inside TypeScript; `datasetName` is also not defined there.
- E14c, Quickstart: `json.dumps` appears without `import json`. Python Async Support imports the trajectory-specific factory but calls `create_async_llm_as_judge`, a different name. The graph custom-prompt example awaits a factory result created with the synchronous factory name.
- E14c, Pytest or Vitest/Jest: prose says a `feedback_key` was added, but the displayed constructor omits it. Several TypeScript result displays also use Python's capitalized `True`.

These defects are visible in the captures. Runtime behavior and repairs were not tested.

## Tools, code and commands named

No package versions are pinned in these captures.

- Installation: `npm install agentevals @langchain/core`; `pip install agentevals`; `npm install openai`; `pip install openai`.
- Environment: `export OPENAI_API_KEY="your_openai_api_key"`; `export LANGSMITH_API_KEY="your_langsmith_api_key"`; `export LANGSMITH_TRACING="true"`.
- Test commands: `vitest run test_trajectory.eval.ts`; `pytest test_trajectory.py --langsmith-output`.
- TypeScript evaluators/types: `createTrajectoryMatchEvaluator`, `createTrajectoryLLMAsJudge`, `FlexibleChatCompletionMessage`, `GraphTrajectory`, `createGraphTrajectoryLLMAsJudge`, `graphTrajectoryStrictMatch`, `extractLangGraphTrajectoryFromThread`.
- Python evaluators/utilities: `create_trajectory_match_evaluator`, `create_async_trajectory_match_evaluator`, `create_trajectory_llm_as_judge`, `create_async_trajectory_llm_as_judge`, `create_graph_trajectory_llm_as_judge`, `graph_trajectory_strict_match`, `extract_langgraph_trajectory_from_thread`. Async prose also names `trajectory_strict_match_async`; examples name `create_async_llm_as_judge` inconsistently.
- Prompts: `TRAJECTORY_ACCURACY_PROMPT`, `TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE`, `CUSTOM_PROMPT`.
- Model strings: `openai:o3-mini`, `o3-mini`, `gpt-4o-mini`. These are examples, with no model comparison evidence.
- Other named tools: `openevals`, OpenAI, `AsyncOpenAI`, LangChain, LangGraph, LangSmith, pytest, Vitest/Jest, `langsmith/vitest`, `langsmith/jest`, `langsmith/evaluation`, `@langchain/openai`, `@langchain/langgraph`, `zod`, `ChatOpenAI`, `MemorySaver`, `Command`, `interrupt`, `createReactAgent`, `create_react_agent`.
- Toy tool names: `get_weather`, `accuweather_forecast`, `get_fun_activities`, `search`.

## Numbers and strong claims

- Four trajectory modes: `strict`, `unordered`, `subset`, `superset`. (All captures, Agent trajectory match.) This is an API description, not benchmark evidence.
- Continuous scores range from 0 to 1, with `continuous` defaulting to `False`. (All captures, Trajectory LLM-as-judge.) The range does not establish a calibrated probability of success.
- The custom graph rubric says “Is perfectly efficient, with no more than one tool call”. (All captures, Graph trajectory LLM-as-judge.) This is an example grading rule and an opinion about efficiency, not a general performance standard.
- “All `agentevals` evaluators support Python” appears in Python Async Support, followed by the asyncio link and naming convention. This is a broad support claim, not verified by execution here.
- The introduction calls the package “a good conceptual starting point”. That is author opinion. No measured judge accuracy, latency, token cost, or cost per successful task is reported.

## Compared with the deep research report

Comparison is limited to E00 section 3.4.

- **Right:** E00 describes “subset/superset relationships” and “model-based trajectory evaluation”. E14 explicitly offers “`strict`”, “`unordered`”, “`subset`”, and “`superset`”, plus the trajectory judge. The summary covers the central choices accurately.
- **Right:** E00 says “Use strict ordering only when ordering is part of the contract.” E14's Strict match example describes “a company policy lookup tool before a tool that requests vacation time for an employee”. The recommendation follows the source's use case.
- **Overstated as copyable code:** E00's heading calls these “Best reusable TypeScript examples”. E14b contains “satisifes”, “outputs: trajectory.outputs,”, and Python `json.dumps` in TypeScript. They teach useful patterns, but are not uniformly ready to run. No comparative evidence establishes “Best”.
- **Workspace-specific inference:** E00 says “a worker must not delegate again”. E14 describes subset matching as checking that an agent “did not call any tools beyond the expected ones.” This supports an allowed-tool approach in principle. The README gives no native worker-depth check or adapter for the user's harnesses.
- **Left out:** E00 recommends “Small, explicit checks for meaningful behavioral constraints.” It omits argument defaults and per-tool comparators, reference-free judging, graph interruptions, async support, and test logging. E14's “a list of fields within the tool call that must match exactly” is especially useful for checking task scope without requiring every incidental argument to match.

## Fit for the user's agent workspace

- (inference) Start with TypeScript message traces from a few bounded worker runs. The supplied format offers a common representation, but adapters for Claude Code, Codex, OpenCode, Hermes, and Gemini are not provided.
- (inference) Use subset checks for an allowed-tool boundary and superset checks for required work. Neither alone proves both completion and scope compliance.
- (inference) Check delegation through recorded tool calls if delegation is exposed there. This checks recorded behavior; it does not enforce the worker boundary.
- (inference) Use strict matching where order matters, such as reading instructions before writing. Unordered matching cannot prove that precedence.
- (inference) Keep exact equality for scope-bearing arguments such as target paths. Apply custom comparators only where differences are harmless, as in the source's case example.
- (inference) Give a model judge a task-specific rubric, a short grading checklist, for sensible progression. Skip the example's one-tool limit for workers whose assigned task needs several tools.
- (inference) Track final deliverable quality and cost separately. These captures show trajectory scores and qualitative efficiency judgments, not a cost accounting method or proof that an artifact meets its requirements.
- (inference) Adopt graph extraction only if the worker system uses graph steps. Direct message evaluators provide a starting point without adopting LangGraph or LangSmith.

## Best parts to read or watch first

Times below are estimated reading times, not supplied by the sources.

- E14b: Subset and superset match, 3 minutes. Best starting point for required versus allowed tools.
- E14b: Tool args match modes, 4 minutes. Shows how to check meaningful arguments and allow specific harmless differences.
- E14b: Strict match and Unordered match, 5 minutes. Read the explanations, then inspect the example defects above.
- E14b: Trajectory LLM-as-judge, 5 minutes. Covers reference-free and reference-aware judgment.
- E14b: Pytest or Vitest/Jest, 4 minutes. Closest match to a frontend engineer's test workflow.
- E14c: Graph trajectory strict match, 3 minutes if graph traces matter. The Python example makes the expected step sequence clearer than the TypeScript version.
