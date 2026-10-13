---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [E09]
purpose: One-source digest feeding the spec compendium.
---

# Using LLM-as-a-Judge For Evaluation: A Complete Guide (E09)

**What it is:** Hamel Husain's practical article, published 2024-10-29. The capture contains about 7,800 words, roughly 30 to 40 minutes of reading, estimated. [Original article](https://hamel.dev/blog/posts/llm-judge/).
**Capture status:** Full according to frontmatter. Article body, code blocks, FAQ, resources and subscription section are captured. No missing text is declared. Images remain linked; the diagram also has a text description. This digest uses the captured text, not independent inspection of those images or linked resources.

## The point in three sentences

Start by having a trusted subject expert judge actual AI interactions as pass or fail and explain each decision. Build an automated judge from those examples, then test whether it reproduces the expert's decisions on separate examples. The main benefit comes from finding and fixing failures through careful review, even if you never build a judge.

## Key ideas

- **Choose the person whose judgment sets the standard.** A principal domain expert is the person who understands the task and its users. An independent developer can fill this role, but leadership assumptions should still be checked against users. Quote: "If you are an independent developer, you should be the domain expert" (Step 1, Exceptions).
- **Cover realistic situations before scoring anything.** The example dimensions are features, scenarios and personas, meaning user profiles. Adapt them to the application rather than treating them as required categories. Quote: "This taxonomy (features, scenarios, personas) is not universal." (This taxonomy is not universal).
- **Generate inputs, then run the real system.** Synthetic data means artificially generated examples. The model can invent user requests, but the system under evaluation must produce its own responses and internal behavior. Quote: "we are only using LLMs to generate the user inputs" (Generating Data).
- **Begin with a binary decision and a useful explanation.** Binary means two possible labels. A critique preserves detail that a pass/fail label alone cannot convey. Quote: "Did the AI achieve the desired outcome?" (Step 3).
- **Write critiques that teach the standard.** Few-shot prompting means including example answers in a prompt. Explanations must be clear enough to serve as examples for the future judge. Quote: "it should be detailed enough that a new employee could understand it" (Examples of Good Critiques).
- **Give reviewers and judges the evidence they need.** Include relevant user metadata, system state and ways to check correctness. Quote: "All of this data needs to be presented on a single screen" (Make it easy for the domain expert to review data).
- **Fix obvious errors before automating review.** Review can already reveal the problems that a judge was meant to find. Quote: "fix them and go back to step 3" (Step 4: Fix Errors).
- **Expect criteria to become clearer during review.** Criteria drift means the standard changes as people inspect examples. Do not assume a complete rubric can be written first. Quote: "You cannot write a good judge prompt until you’ve seen the data." (The Hidden Power of Critiques).
- **Train the judge to explain before deciding.** The Honeycomb example supplies query-language information, guidelines and expert critiques. Its instruction is: "first write a detailed critique explaining your reasoning" (Start with Expert Examples).
- **Validate each label separately.** True positive rate and true negative rate measure how often the judge correctly identifies each class. Overall agreement can hide a complete failure to detect rare errors. Quote: "Raw agreement can be misleading when classes are imbalanced." (Keep Iterating on the Prompt Until Convergence With Domain Expert).
- **Keep prompt examples separate from validation examples.** Training examples can appear in the prompt; development examples guide revisions; test examples provide the final check. Quote: "Never place dev or test examples in the judge prompt." (FAQ: How do you validate an LLM judge against human labels?).
- **Use unseen interactions to locate product weaknesses.** Error analysis means examining failures to find patterns and causes. Group failures by meaningful dimensions, then inspect full traces, records of calls and intermediate steps. Quote: "You should calculate the error on unseen data only" (Step 6).
- **Add targeted judges after discovering the need.** Some failures can be checked with code. Quote: "don’t jump directly to using specialized LLM judges" (Step 7).
- **Repeat review and retain human involvement.** Review periodically and after material changes; investigate related errors while keeping some random sampling. Quote: "You just need a representative sample." (FAQ: How do you phase out human in the loop to scale this?).
- **A judge is optional when manual review is cheap.** An independent expert with available data can start reviewing directly. Quote: "it’s probably fine to just do error analysis without a judge" (Do You Really Need This?).

## How to do it (concrete steps, checklists, templates)

1. **Find the principal expert.** Use someone with real task expertise or someone who represents the target users. Establish whose standard the evaluation should reflect.
2. **Create a varied dataset.** Define relevant dimensions. Sample real interactions and, where useful, generate synthetic inputs. Use actual APIs and database information to make assumptions realistic. Generate inputs, feed them into the current AI system, capture responses, then store inputs, responses and metadata in a table. Continue until new failure types stop appearing.
3. **Ask the expert for pass/fail labels and critiques.** Show sufficient context on one screen. Start with around 30 examples for discovering failures and developing the rubric, the written judging rules. Keep reviewing until learning slows. Do not confuse this discovery sample with a judge-validation dataset.
4. **Fix obvious errors.** Return to expert review to verify the fixes. Repeat until the system is reasonably stable.
5. **Build and revise the judge.** The Honeycomb prompt puts domain information and guidelines before examples. Each example contains `<nlq>` for the natural-language request, `<query>` for the generated query, and `<critique>` containing JSON fields `critique` and `outcome`. The illustrated outcomes are `good` and `bad`, although the surrounding instructions call them pass/fail. Ask for an explanation before the decision. Compare judge and expert critiques in a spreadsheet containing request, generated query, critique and outcome. Revise the prompt and inspect disagreements.
6. **Validate the judge using the FAQ procedure.** Split human-labeled examples into training, development and test sets. Put only selected training examples in the prompt. Use development examples to find mistakes and revise the prompt. Keep test examples hidden until revisions are finished, freeze the prompt, then run the test set once. Measure correct detection of both labels rather than relying on overall agreement.
7. **Analyze failures on unseen data.** Apply the validated judge to real or synthetic interactions. Calculate failure rates by dimension. Inspect traces and classify causes manually in a spreadsheet. In the sample trace, the system retrieves valid order-number formats and advice for new users but omits both from its response. The author labels this `Missing User Education`.
8. **Fix failures and add tests.** Return to expert review. Try to write a test case for every fixed error. Use a code assertion where sufficient; create a specialized judge where judgment is needed. Repeat periodically and after material changes.

Prompt mistakes to check, in the source's order:

- No critiques.
- Critiques that are too terse.
- Missing external context used by the human reviewer.
- Too little variety in examples.

If alignment remains poor, check whether the system promises too much, the process was followed incorrectly, or the desired agreement is infeasible. The author recommends addressing the cause and using more human annotation when needed.

## Tools, code and commands named

- **Honeycomb**, **Query Assistant**, and **Phillip Carter** supply the worked judge example. Query fields include `breakdowns`, `calculations`, `filters`, `orders`, `limit`, and `time_range`. Prompt placeholders are `{{query_language_info}}`, `{{guidelines}}`, `{{user_input}}`, and `{{generated_query}}`.
- **DSPy** is a prompt optimizer the author says he has not had much luck with. **ALIGN Eval**, also written **Align Eval** in Resources, is Eugene Yan's recommended judge-building tool. These are personal assessments, not comparisons with measured results.
- **Continual In-Context Learning** supplies examples dynamically based on the item being judged. **prompt caching** is linked as help when prompts need many examples.
- The trace names `search_order_database` and `retrieve_context`. It contains `user_input`, `function_calls`, `llm_intermediate_steps`, and `final_response`. Its rendered array backslashes are capture formatting, so it should not be treated as ready-to-run JSON.
- Spreadsheets and a simple web app are review-interface options. **Hex** is named as a synthetic-data user. Resources name **Braintrust**, **Arize**, **Dosu**, **LangSmith**, **Langchain**, and **DeepLearningAI**, plus Andrew Ng's *Carrying Out Error Analysis (C3W2L01)* video.
- No installation commands, executable implementation, exact judge model ID or package versions are provided. Fine-tuning, adjusting a model using training data, is discussed but its implementation is outside the article's scope.

## Numbers and strong claims

- **Over 30 companies:** opening paragraph's claim about the author's evaluation work. Self-reported experience, not evidence of a universal success rate.
- **Around 30 examples:** discovery heuristic, not enough by itself to validate an automated judge (How many examples do you need?).
- **About 100 examples per failure mode; below 60 often gives wide confidence intervals:** validation guidance in the same section. Confidence intervals express uncertainty in an estimate. No supporting calculation is provided in the capture.
- **10 to 20% training, 40 to 45% each development and test; 30 to 50 of each label in each development/test set:** typical split and target counts (FAQ: How do you validate an LLM judge against human labels?). These are guidelines, not a promise that every dataset will support them.
- **Three iterations to exceed 90% agreement:** Honeycomb anecdote; the dataset had about 50% failures (Keep Iterating on the Prompt Until Convergence With Domain Expert). The author explicitly warns that results vary.
- **5% errors can yield 95% agreement while detecting none:** an always-Pass judge illustrates misleading overall agreement (validation FAQ).
- **75.0% and 68.0% failure rates:** illustrative new-user/no-match slices in the Step 6 table, with 20 and 25 examples. The 20-failure root-cause table assigns 8/6/4/2 cases, or 40/30/20/10%, to four causes (Classify Traces). These are teaching examples, not benchmark results.
- **3600 versus at least 36000 seconds:** the Honeycomb example critique says an hour-long query is insufficient for meaningful hourly patterns (Start with Expert Examples). This is the example expert's domain judgment, not a general rule for all time-series analysis.
- **15 minutes:** claim that manual classification can make useful progress quickly (Classify Traces). Practitioner opinion, not a measured time requirement.
- **Eight dimensions on a 1-5 scale means the requester is guessing:** categorical opinion (Don't stray from binary pass/fail judgments when starting out). The later FAQ accepts other judge uses, including ranking and model selection.
- **30% accuracy improvement:** appears in a linked Dosu/LangSmith resource title (Resources). It is not a result established by this article. Treat it as an unverified linked claim with promotional wording.

## Compared with the deep research report

Comparison is limited to E00, section 2.3.

- **Right:** E00 describes a process around "domain expertise, examples, explicit criteria, and comparison with human judgment". E09 directly supports this through expert critiques and instructions to "Test against expert judgments" (Recap of Critique Shadowing).
- **Right:** E00 warns against asking a stronger model to score workers and treating numbers as reliable. E09 similarly warns: "Raw agreement can be misleading when classes are imbalanced." The source supplies a concrete explanation and validation procedure.
- **Wrong in sequence:** E00's suggested exercise begins "Choose one narrow failure mode" and then builds a judge for it. E09's recommended starting method is overall outcome review followed by error analysis: "don’t jump directly to using specialized LLM judges" (Step 7). The exercise could follow that review, but does not represent the guide's initial sequence.
- **Left out:** E00's short summary omits discovery versus validation sample sizes and the training/development/test separation. E09 says "Never place dev or test examples in the judge prompt." These details materially affect whether the resulting scores can be trusted.
- **Left out:** E00 emphasizes when automated scoring becomes useful. E09 also says "it’s probably fine to just do error analysis without a judge" (Do You Really Need This?). It includes fixing obvious errors first, showing full context, inspecting traces, and reviewing again after model changes.

## Fit for the user's agent workspace

- (inference) Act as the principal expert for bounded frontend/TypeScript tasks within your expertise. Judge actual task packets and worker results, then write explanations that another reviewer could follow.
- (inference) Adapt dataset dimensions to worker task types and situations, such as ambiguous requirements or missing context. Personas may add little when workers serve a root agent rather than end users.
- (inference) Show the packet, relevant instructions, changes and verification evidence together. The source's context requirement suggests that judging only a final message would be incomplete.
- (inference) Define scope compliance explicitly before reusing the examples. The article passes a flight cancellation despite missing confirmation, but fails insecure billing assistance. Those illustrative labels do not establish the workspace's authority rules.
- (inference) Use a small manual review batch to find failures before paying for a judge. If review remains cheap, keep the manual process.
- (inference) Reserve hidden examples for validation and record errors on both labels. A stronger judge model still needs to prove agreement with your own standard.
- (inference) Track cost and time alongside quality if deciding whether a worker was worth using. The article discusses a judge's cost/latency budget, but supplies no worker return-on-cost formula or evaluation design.

## Best parts to read or watch first

Times below are reading estimates, not source-provided durations.

- **Step 3 and Examples of Good Critiques:** 5 to 7 minutes. Learn what labels and explanations should contain; inspect the debatable flight-cancellation example.
- **How many examples do you need? plus FAQ: How do you validate an LLM judge against human labels?:** 3 to 4 minutes. Separate failure discovery from trustworthy validation.
- **Start with Expert Examples through Keep Iterating on the Prompt Until Convergence With Domain Expert:** 5 to 7 minutes. Read the complete prompt and the warning about overall agreement.
- **Step 6, especially Classify Traces and Fix Your Errors, Again:** 4 to 6 minutes. Connect judgments to concrete changes and regression tests.
- **Do You Really Need This? and Step 7:** 2 to 3 minutes. Decide whether manual review is sufficient and when specialized judges become useful.
