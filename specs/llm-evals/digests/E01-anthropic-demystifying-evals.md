---
created_at: 2026-10-13
model: gpt-6.1-sol (medium)
doc_type: digest
source_ids: [E01]
purpose: One-source digest feeding the spec compendium.
---

# Demystifying evals for AI agents (E01)

**What it is:** Anthropic engineering article by Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, and Jiri De Jonghe, published January 9, 2026. A long practical guide with two illustrative YAML examples, four tables, and five figure captions. Allow roughly 30 minutes to read; this is an estimate, not a stated duration. [Original article](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).

**Capture status:** Full, according to its frontmatter. Both code blocks, all four tables, and all five figure captions were retained. The capture says the source HTML was checked for completeness. Images are linked, with captions preserved; no missing article text is reported.

## The point in three sentences

An agent evaluation tests the model and the system that gives it tools, then checks both its execution record and the resulting state. Useful suites start with real failures, clear success criteria, clean environments, and graders checked against human judgment. Repeated trials, separate capability and regression suites, and regular transcript review make scores useful for decisions rather than just reassuring numbers.

## Key ideas

- **Learn the parts before comparing scores.** A task is one test with inputs and success criteria; a trial is one attempt; a grader scores an aspect of that attempt; a suite groups tasks. Quote: “Each attempt at a task is a **trial**.” Location: “The structure of an evaluation.”

- **The tested agent includes its surrounding system.** The agent harness enables tool use; the evaluation harness runs trials, records steps, grades results, and aggregates scores. Quote: “we’re evaluating the harness _and_ the model working together.” Location: “The structure of an evaluation.”

- **A transcript and an outcome answer different questions.** The transcript records outputs, tools, intermediate results, and interactions; the outcome is the actual final environment state, such as a booking in a database. Quote: “The **outcome** is the final state in the environment at the end of the trial.” Location: “The structure of an evaluation.”

- **Combine graders according to what each can judge.** Code checks are cheap and repeatable but can reject valid variations; model judges handle open-ended work but vary and need human calibration; human experts provide reference judgments at greater cost. Quote: “Each grader evaluates some portion of either the transcript or the outcome.” Location: “Types of graders for agents.”

- **Keep capability and regression tests distinct.** Capability tests expose limits and start with low pass rates; regression tests protect established behavior and should pass nearly all the time, with successful capability tasks eventually moving into that suite. Quote: “Does the agent still handle all the tasks it used to?” Location: “Capability vs. regression evals.”

- **Coding correctness and coding quality need different checks.** Start with tests that verify the fix and preserve existing behavior, then use a clear model rubric, meaning written grading criteria, for code quality or interaction behavior. Quote: “with additional graders and metrics added only as needed.” Location: “Evaluating coding agents,” after its YAML example.

- **Conversation quality is part of task success.** A support agent may need to resolve the ticket, process the refund, stay within a turn limit, and communicate appropriately; a second model often plays the user. Quote: “the quality of the interaction itself is part of what you're evaluating.” Location: “Evaluating conversational agents.”

- **Research quality needs several lenses.** Groundedness means claims are supported by retrieved sources; coverage checks required facts; source quality checks authority; model rubrics assess coherence and completeness against task-specific standards. Quote: “research quality can only be judged relative to the task.” Location: “Evaluating research agents.”

- **Computer use needs actual state checks and efficiency measurements.** Page appearance alone may not prove an order exists; browser tool choice also trades token usage against speed, with different choices suited to text extraction and visual shopping. Quote: “confirming an order was actually placed, not just that the confirmation page appeared”. Location: “Computer use agents.”

- **One successful attempt does not establish reliability.** `pass@k` measures at least one success in k attempts; `pass^k` measures all k succeeding, so increasing k pushes the two measures in opposite directions. Quote: “pass@k for tools where one success matters, pass^k for agents where consistency is essential.” Location: “How to think about non-determinism in evaluations for agents.”

- **Task descriptions must disclose what graders require.** A hidden expected filepath can fail a correct solution; a reference solution, meaning a known working output that passes every grader, checks that the task is solvable. Quote: “Everything the grader checks should be clear from the task description”. Location: roadmap, Step 2.

- **Test when behavior should happen and when it should not.** A suite that only rewards searching can encourage needless searches; include both sides to avoid optimizing in one direction. Quote: “One-sided evals create one-sided optimization.” Location: roadmap, Step 3.

- **Reset each trial and examine the graders themselves.** Leftover files, cached data, shared resource limits, and previous trial history can inflate scores or produce related failures; model judges also need human comparison and permission to admit missing evidence. Quote: “Each trial should be “isolated” by starting from a clean environment.” Location: roadmap, Step 4.

- **Prefer valid outcomes to a prescribed route, and inspect failures.** Exact tool sequences can reject creative solutions; partial credit records meaningful progress, while transcript review separates agent mistakes from unfair grading. Quote: “Failures should seem fair”. Location: roadmap, Step 6; path flexibility and partial credit are in Step 5.

- **Maintain the suite and combine evaluation methods.** Saturation means an agent passes all solvable tasks, so the suite stops revealing improvements; automated tests also need real-use monitoring and human review to cover their blind spots. Quote: “An eval suite is a living artifact that needs ongoing attention and clear ownership to remain useful.” Location: roadmap, Step 8.

## How to do it (concrete steps, checklists, templates)

The article's roadmap has nine numbered steps, 0 through 8. This preserves their order.

- **Step 0: Start early.** Begin with 20-50 simple tasks from real failures. Early changes often have large effects that small suites can detect. More mature agents need larger or harder suites to detect smaller changes.
- **Step 1: Start with existing manual checks.** Convert release checks, common user tasks, bug reports, and support cases into tasks. Prioritize by user impact.
- **Step 2: Write unambiguous tasks and reference solutions.** Ask whether two domain experts would independently agree on pass or fail and could complete the task themselves. Make every checked requirement visible in the instructions. Run a known working solution through every grader. Investigate persistent zero scores for task or grader defects.
- **Step 3: Balance the problem set.** Include cases where each behavior is appropriate and inappropriate. The example tests both queries needing search, such as weather, and queries answerable from existing knowledge. Refine tasks and prompts over several rounds.
- **Step 4: Match production and stabilize the environment.** Use an agent setup that behaves roughly as it does in real use. Start every trial clean. Prevent leftover files, cached data, prior trial history, and resource exhaustion from distorting scores.
- **Step 5: Design graders thoughtfully.** Use deterministic checks, meaning checks that give the same result on the same input, where possible. Add model judges where needed and humans for validation. Prefer outcomes over rigid tool sequences. Award partial credit for multi-part tasks. Compare model judgments with experts, use structured criteria, allow `Unknown`, and consider a separate judge for each dimension. Check ambiguity, grading bugs, and harness limits. Prevent agents from passing through grader loopholes.
- **Step 6: Check transcripts.** Read records and grades from many trials. For each failure, establish whether the agent made a mistake or the grader rejected a valid answer. Build viewing tools and make review routine.
- **Step 7: Monitor saturation.** A 100% suite protects against regressions but cannot measure improvement. Review whether hard remaining tasks, unfair grading, ambiguous instructions, or harness constraints hide progress. Qodo's example shows why longer agent tasks may reveal gains missed by single-attempt coding tests.
- **Step 8: Establish ownership and ongoing contribution.** Give core infrastructure clear owners while domain and product experts contribute tasks and run evaluations. Define planned capabilities with evals before they work, then improve the agent until it meets them. Let people closest to users submit tasks as pull requests.

**The two illustrative templates:** These are theoretical examples, not a documented executable framework schema. The article explicitly warns that they show more grader types than most tasks need.

- **Coding:** `fix-auth-bypass_1` combines required tests for empty and null passwords, a code-quality rubric, static analysis, a security-log state check, and required tool calls. It tracks turns, tool calls, total tokens, and three latency measures. The practical default is unit tests plus a code-quality rubric.
- **Conversation:** The refund example checks empathy, explanation, and grounding in policy-tool results; resolved ticket and processed refund states; identity verification, refund amount, and confirmation tools; and a ten-turn cap. It tracks the same usage and latency measures. The practical guidance emphasizes model judges for communication and goal completion where several answers can be correct.
- **Scoring:** Combine grader results with weights and a threshold, require all graders to pass, or use a mixture. Multi-component tasks can receive partial credit.

**Use other methods in the stated lifecycle:** Run automated suites before launch and on agent changes or model upgrades. After launch, monitor unexpected failures and changing usage. Compare variants with real users once traffic is sufficient. Triage feedback continuously, sample transcripts weekly, and reserve structured human studies for subjective work or judge calibration. The article supplies no statistical testing procedure or fixed judge-calibration sample size.

## Tools, code and commands named

- **Agent systems:** Claude Code, Agent SDK, Claude.ai, Claude for Chrome, and Opus 4.5. The opening figure uses building an MCP server as its coding task. No SDK or CLI installation commands are provided.
- **Benchmarks:** SWE-bench Verified, Terminal-Bench, 𝜏2-bench, 𝜏-Bench, τ2-Bench, BrowseComp, WebArena, OSWorld, and CORE-Bench. The appendix names Terminal-Bench 2.0. Spelling and casing vary in the capture, including SWE-Bench Verified and Terminal Bench.
- **Coding example:** `deterministic_tests`, `llm_rubric`, `static_analysis`, `state_check`, `tool_calls`; `test_empty_pw_rejected.py`, `test_null_pw_rejected.py`, `prompts/code_quality.md`; command names `ruff`, `mypy`, `bandit`; tool names `read_file`, `edit_file`, `run_tests`; path pattern `src/auth/*`; expected log event `auth_blocked`.
- **Conversation example:** `prompts/support_quality.md`, `fetch_policy`, `verify_identity`, `process_refund`, `send_confirmation`, amount constraint `<=100`, and `max_turns: 10`. Expected states are `tickets: {status: resolved}` and `refunds: {status: processed}`.
- **Metric names in both examples:** `n_turns`, `n_toolcalls`, `n_total_tokens`, `time_to_first_token`, `output_tokens_per_sec`, `time_to_last_token`. Elsewhere the article names latency, token usage, cost per task, and error rates.
- **Framework appendix:** Harbor runs trials in containers and supplies standardized task/grader formats and a benchmark registry. Braintrust combines offline evaluation, live monitoring, and experiment tracking; its `autoevals` library supplies scorers. LangSmith supplies tracing, offline/online evaluation, and datasets with LangChain integration. Langfuse is described as a self-hosted open-source alternative. Arize supplies Phoenix for tracing, debugging, and offline/online evaluation, and AX as a SaaS offering. Simple scripts or custom frameworks are also acceptable. No installation commands or package versions are given.

## Numbers and strong claims

These are claims in the capture, not independently verified findings.

- **20-50 starter tasks:** roadmap, Step 0. Presented as practical guidance for early, large changes, not a universal sufficient sample size.
- **Nearly 100% regression pass rate:** “Capability vs. regression evals.” A target for established behavior; capability tests should start low.
- **75% per-trial success gives about 42% success across all three trials:** non-determinism section, `(0.75)³ ≈ 42%`. Its figure says both metrics coincide at k=1 and diverge sharply by k=10. Treat the figure as illustrative, not a result for every agent.
- **0% pass@100 usually signals a broken task for frontier models:** roadmap, Step 2. A strong author judgment, not proof that every unsolved task is defective.
- **CORE-Bench rises from 42% to 95% for Opus 4.5:** roadmap, Step 5. The account attributes this to grading/task fixes and a less constrained scaffold together. It is not evidence of a model-only gain or grader-only effect. The rounding example contrasts `96.12` with `96.124991…`.
- **SWE-bench growth is stated inconsistently:** “Evaluating coding agents” says 40% to above 80% in one year. Step 7 says scores started at 30% “this year” and are above 80%. Preserve the differing baselines; the January 2026 publication date makes the latter timeframe unclear.
- **Support turn limits differ:** conversational prose asks for fewer than ten turns; its YAML permits `max_turns: 10`. Both are illustrative, and the boundary needs clarification before reuse.
- **Bolt built its system in three months:** “Why build evaluations?” A customer anecdote, not a delivery estimate for another team.
- **Model upgrades take weeks without evals and days with them:** “Why build evaluations?” An author generalization with a promotional tone; no controlled comparison is supplied. The same section's claim of getting baselines and regression tests “for free” understates maintenance and measurement work discussed later.
- **DOM interaction is faster but uses more tokens; screenshots are slower but use fewer:** “Computer use agents.” A broad qualitative claim illustrated by Wikipedia extraction and Amazon shopping, not a measured rule for every browser task.

## Compared with the deep research report

Only E00 section 1.3 was read for this comparison.

- **Right:** E00 says it explains “tasks, repeated trials, graders, execution traces, and environmental outcomes.” E01 defines each and states that “model outputs vary between runs”. E00 also correctly distinguishes regression protection from capability limits; E01 says capability evals “should start at a low pass rate”.
- **Right:** E00 says “Independently verify the resulting state.” E01's matching example asks “whether a reservation exists in the environment’s SQL database.” E00's warning about an agent claiming tests passed is a sound paraphrase, not a quotation from E01.
- **Right:** E00 says “allow multiple valid execution paths”. E01 recommends grading “what the agent produced, not the path it took.”
- **Overstated application:** E00 says the user's workers can “delegate, and hand work to another phase.” That is E00's workspace framing, not established by E01. E01 mentions agents that “collaborate in multi-agent systems” only as a future area requiring adapted techniques. It gives no worker-delegation or handoff grading procedure.
- **Left out:** E00 names “repeated trials” but omits `pass@k` versus `pass^k`, the source's distinction between finding one solution and being consistently successful. It also omits reference solutions, balanced cases, clean trial environments, partial credit, `Unknown` judgments, and separate judges per dimension. E01's environmental requirement is explicit: “starting from a clean environment”.
- **Left out:** The report's summary does not cover the full ordered roadmap, saturation, grader/harness defects, or ongoing ownership. E01 cautions that “we do not take eval scores at face value” before inspecting details and transcripts. No factual contradiction was found in E00's core summary; it is substantially less complete than this source.

## Fit for the user's agent workspace

- **(inference)** Make each bounded worker packet a task with visible success criteria. Check the actual changed files and required behavior, alongside the worker's final message.
- **(inference)** Evaluate the model, role instructions, tools, and harness together. Re-run the same tasks when changing any of those components; a score belongs to the tested combination.
- **(inference)** Start with 20-50 real worker mistakes and manual root checks. Include both required actions and cases where a worker should refrain from an unnecessary action. This adapts the source's balanced-search example to scope discipline.
- **(inference)** Use code checks for file state, tests, and explicit scope constraints. Use a human-calibrated model rubric for judgment, communication, and avoidable over-engineering. Accept different valid tool paths unless the packet requires a particular action.
- **(inference)** Repeat representative tasks in clean environments. Track first-attempt success and consistency separately so occasional lucky passes do not justify a model replacement.
- **(inference)** Record tokens, latency, and cost per task beside quality. This supports cost comparisons, but the article supplies no cost-adjusted worker score or rule for deciding whether a worker was worth its price.
- **(inference)** Keep established worker tasks in a regression suite and harder tasks in a capability suite. Inspect failures before rewriting role instructions, especially when a filepath or grading threshold was never specified.
- **(inference)** Begin with simple scripts or a suitable existing framework. Skip building a broad platform first. The source supports task and grader quality over infrastructure, but does not prescribe a TypeScript implementation or a complete multi-agent eval design.

## Best parts to read or watch first

Estimated reading times, not durations stated by the source.

- **“The structure of an evaluation,” 3 minutes:** vocabulary and the distinction between the transcript, final state, agent harness, and evaluation harness.
- **“How to think about non-determinism in evaluations for agents,” 2 minutes:** `pass@k` and `pass^k`, with a concrete reliability example.
- **“Going from zero to one,” Steps 0-3, 4 minutes:** the smallest useful starting suite, realistic cases, clear criteria, and reference solutions.
- **“Design the eval harness and graders,” Steps 4-5, 5 minutes:** trial isolation, judge calibration, partial credit, and examples of misleading benchmark scores.
- **“Maintain and use the eval long-term,” Steps 6-8, 4 minutes:** transcript review, saturation, ownership, and eval-driven development.
- **“Evaluating coding agents,” 3 minutes:** the illustrative YAML and its warning to add graders only as needed. Read “Evaluating research agents,” another 2 minutes, for document-writing workers.
