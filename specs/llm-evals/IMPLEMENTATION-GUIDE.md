---
created_at: 2026-10-13
model: "GPT-6 (Codex; exact model identifier and reasoning effort unavailable)"
doc_type: guide
purpose: Recommend the smallest useful worker evaluation loop for this workspace, with staged implementation budgets and concrete untested designs.
related:
  - path: ./spec.md
    why: Owns the LLM evals area's current scope and navigation.
  - path: ./COMPENDIUM.md
    why: Explains the evaluation concepts and source lessons behind this guide.
  - path: ./SOURCES.md
    why: Owns source IDs, capture status, and evidence links.
  - path: ../../AGENTS.md
    why: Owns workspace authority, privacy, routing, and worker boundaries.
  - path: ../../INDEX.md
    why: Routes the proposed files to their existing workspace homes.
  - path: ../../roles/task-worker-tiers.md
    why: Defines the worker contract being evaluated and current tier availability.
  - path: ../../ai-models/delegation-briefing.md
    why: Sections 1 to 3 own current model choices and task suitability.
  - path: ../../ai-models/AGENTS.md
    why: Defines model-data ownership and rules for unavailable measurements.
  - path: ../../ai-models/README.md
    why: Establishes the permanent model-comparison data home and billing distinctions.
  - path: ../../skills/AGENTS.md
    why: Defines ownership of the proposed portable evaluation procedure.
  - path: ../../skills/model-bakeoff/SKILL.md
    why: Provides the existing entry point for controlled model comparisons.
  - path: ../../workflows/model-bakeoff/AGENTS.md
    why: Owns comparison isolation, timing, verification, and cleanup.
  - path: ../../workflows/model-bakeoff/templates/
    why: Supplies task, contestant, evaluation, and cleanup formats to reuse.
  - path: ../../specs/spec-workflow/spec.md
    why: Defines fresh phases, acceptance, and durable change requirements.
  - path: ../../workflows/spec-workflow/AGENTS.md
    why: Defines how a later serious implementation would run.
  - path: ../../conventions/artifact-authoring.md
    why: Owns generated result locations and Markdown naming.
  - path: ../../conventions/memory-files.md
    why: Owns later promotion of accepted evidence into durable memory.
---

# LLM evals implementation guide

## 1. Recommendation first

**Recommendation, inference:** Build one portable `worker-evals` skill around your existing model-bakeoff workflow.
Start with one role, `task-execute`, in Codex, on small TypeScript edits.
Review saved runs first. Turn observed failures into five to ten reusable cases.
Check actual files, scope, and verification with code.
Add a local promptfoo suite when replaying those cases manually becomes tedious.
Add one human-validated judge only for a failure that code cannot decide.
Keep Inspect AI for a later need for controlled CLI environments.
**Today's first step:** Review five recent `task-execute` runs and write one concrete failure note per flawed run.

### How to read this guide

An **eval** is a repeatable way to check whether an AI system did its assigned job. A **trace** is the recorded sequence of messages, tool calls, and results. A **judge** is another model asked to apply written grading rules. An eval of a worker measures its model, instructions, tools, and harness together. It does not isolate model intelligence. [E01]

Every proposed design, schedule, threshold, and action below is marked **inference**. It is a recommendation for this workspace, not a result demonstrated by a source. Source claims carry IDs such as [E09] or [E13 validate-evaluator]. Find their captures through [SOURCES.md](./SOURCES.md). Read [COMPENDIUM.md](./COMPENDIUM.md) for the wider explanation.

This guide proposes future implementation. It installs nothing, creates no skill, and changes no model mapping. The source captures are dated October 13, 2026. The local observability experiment is dated October 5. Neither establishes that every integration will work unchanged when you build.

## 2. Depth levels by time budget

**Inference:** Treat these as time boxes with useful stopping points. The estimates assume you already have readable runs and can launch the maintained role. Missing logs or an unavailable role can consume the whole budget. Finish a smaller complete loop if that happens. Do not claim the schedule is a forecast from the sources.

### Two hours: learn one failure and preserve one check

**Goal, inference:** Find a worker mistake you care about, reproduce it, and retain a way to notice it again.

**Steps, inference:**

- Spend 15 minutes selecting five recent small editing tasks. Include a success, a failure, and a case with incomplete evidence. Use sanitized records or keep sensitive review in a separate private repo.
- Spend 35 minutes reading each packet beside the trace, changed files, and root verification. Write free-text observations first. Record the earliest useful explanation of failure.
- Spend 20 minutes deciding one rule. For example: the worker changed a neighboring file outside its allowed paths. State the rule clearly in the replay packet.
- Spend 30 minutes making a tiny fixture, a copy of the input files, and a code check. A before/after file inventory can catch unexpected writes. Run the check on a known correct result and a deliberately wrong result.
- Spend 20 minutes replaying one task, reviewing its evidence, and recording the outcome. If execution cannot fit, evaluate a saved run and state that no live replay occurred.

**Deliverables, inference:** One short review table, one case, its fixture, one check, and one result with evidence pointers. The review table needs run ID, task, observation, acceptability, and reason. It can be CSV. Any generated Markdown report belongs under `artifacts/audits/` according to [artifact-authoring.md](../../conventions/artifact-authoring.md).

**What you learn:** Whether the worker's final message reflects what happened. You also learn whether your existing logs are sufficient to check the rule. This implements the sources' advice to inspect real outputs and use simple code checks. [E07] [E13 write-code-eval]

**Stop here if, inference:** You only use workers occasionally, manual acceptance takes minutes, and this one check catches your main repeated problem. A small manual process can be useful without a judge. [E09]

### One day: a repeatable suite for one role

**Goal, inference:** Replay five to ten representative tasks through the real worker route and compare the results with a known baseline.

**Steps, inference:**

- Spend the first hour reviewing more runs and revising the failure definition. Treat the two-hour exercise's findings as provisional.
- Spend 90 minutes curating five to ten cases with clear success rules. Include work that should proceed, work that should stop, and a case where a harmless alternate solution should pass.
- Spend 90 minutes implementing a small TypeScript runner or custom promptfoo provider. Choose the route that preserves the maintained role and observed model settings. Do not recreate the worker as a bare chat prompt.
- Spend an hour adding file, schema, behavior, and trace checks. Preserve complete results before deleting trial directories.
- Spend an hour running the baseline. Repeat the three most failure-prone cases three times if time and quota allow. Record failures and missing evidence separately.
- Spend the remaining time reviewing failures and writing a portable skill entry point. Have the root author its rules. Document the exact launch and replay commands that actually worked.

**Deliverables, inference:** A versioned case set, fixture files, a runner configuration, a trace normalizer for one harness, code checks, a draft skill, and a dated audit result. The result shows case-level outcomes, observed runtime identity, time, usage, and available cost information.

**What you learn:** Which known failures recur, which assertions unfairly reject valid work, and whether this role is useful on this task class. Repeated trials expose variation that a single good run hides. A fixture reset prevents one run from changing another's starting state. [E01] [E11b]

**Stop here if, inference:** Most acceptance rules are objective and manual review covers the remaining few. Keep the judge out of the critical path. The suite can protect small edits without measuring every aspect of worker quality.

### One week, part-time: useful comparisons and one calibrated judge

**Goal, inference:** Spend roughly six to ten focused hours making the suite useful for a real model or prompt decision. Judge validation is a separate effort and may extend beyond the week.

**Steps, inference:**

- Session one, about 90 minutes: review fresh runs. Grow toward 20 to 30 cases if you have enough distinct examples. Keep ordinary tasks beside edge cases. Mark synthetic cases explicitly.
- Session two, about two hours: improve one-harness capture and result preservation. Verify timeouts, missing output, unavailable settings, and incomplete traces produce visible statuses.
- Session three, about 90 minutes: compare the baseline with one candidate on the same cases. Change one variable, such as reasoning effort or the role prompt. Keep fixtures and checking rules fixed.
- Session four, about two hours: if a repeated failure needs interpretation, collect your own criterion-specific labels and critiques. Draft one judge using training examples only. If you lack labels, continue manual review.
- Session five, about one to two hours: inspect disagreements, report case counts and uncertainty, and write a decision about the candidate. Record what additional evidence would change that decision.

**Deliverables, inference:** A comparison report, a stable baseline, expanded cases, human labels, and either a validated narrow judge or a clear statement that judge validation remains unfinished. Add a small review interface only if reading logs is slowing you down. A spreadsheet is enough to begin. [E07]

**What you learn:** Whether the proposed change reduces a specific failure without creating others. You also learn how well a judge matches your standards, rather than assuming a stronger model defines those standards. [E09]

The judge dataset needs enough good and bad examples. E13 suggests about 100 labeled traces per failure mode, with roughly balanced classes. E09 distinguishes an initial discovery batch from a larger validation dataset. These are practical guides, not guarantees of certainty. [E13 validate-evaluator] [E09]

**Stop here if, inference:** One role and one harness answer the current decision. Expand to another harness only when you have a question that requires it. A completed comparison matters more than collecting integrations.

### Ongoing practice: every model, role, or prompt change

**Goal, inference:** Catch known regressions while continuing to discover failures your current checks miss.

**Steps, inference:**

- Before a change, record the old instructions, case version, fixture version, harness version, and resolved runtime profile. Preserve the baseline results.
- Run code checks on the relevant cases after every material model, role, or prompt change. Replay live workers for changes that affect behavior. Rechecking saved outputs alone cannot test a changed worker.
- For promotion candidates, run the full role suite and repeat risky cases. Apply any validated judge to the subset that needs it.
- Review new failures, new disagreements, and a small random sample of passes. Add real incidents to the regression suite after making their requirements explicit.
- Revalidate the judge after its prompt or model changes. Revisit calibration when the worker's tasks or output distribution change substantially.
- Record the accepted decision and its limits. Keep harder capability cases separate from cases protecting established behavior.

**Deliverables, inference:** A dated result for each meaningful change, a concise failure log in the run evidence, maintained case versions, and an explicit promotion or rejection decision. Use the existing planning and reconciliation process when implementation becomes serious durable work. [spec-workflow/AGENTS.md](../../workflows/spec-workflow/AGENTS.md)

**What you learn:** Whether previous strengths survive change and where current tests stop being informative. Anthropic separates regression tests, which protect established behavior, from capability tests, which expose limits. It also recommends continuing transcript review. [E01]

**Stop here if, inference:** This loop gives you enough evidence to make worker choices. Add scheduled monitoring or continuous integration only when the manual trigger is being missed or the run volume warrants it.

## 3. Is a skill enough?

**Answer, inference:** Yes, a skill is enough to start a useful manual eval practice. A skill alone is insufficient for repeatable execution, evidence capture, and automated grading. Pair it with saved cases and a few scripts. Add promptfoo when it saves effort. Extend model-bakeoff for comparisons. Defer Inspect until you need its environment controls.

Your workspace already separates procedure, behavior, bridges, and composed workflows. A skill belongs in `skills/`; worker behavior belongs in `roles/`; runtime wiring remains with each adapter. [skills/AGENTS.md](../../skills/AGENTS.md) [INDEX.md](../../INDEX.md)

| Option | What the captured material provides | Fit here, inference | Main weakness here, inference |
|---|---|---|---|
| One portable skill | Your workspace's on-demand procedure format | Fastest way to make review, replay, and reporting repeatable across sessions | Prose cannot capture missing events or execute assertions by itself |
| Selected E13 skills | Discovery, code-check writing, judge writing, validation, and audit procedures | Borrow proven workflow structure and retain your own authority rules | Direct installation brings assumptions about interfaces, tools, and delegation that need adaptation |
| promptfoo suite | Cases, providers, assertions, results viewer, and agent integrations [E11a] [E11b] | Familiar TypeScript integration and cheap local checks | Needs a provider that tests the actual maintained worker route |
| Inspect AI | Dataset, agent execution, scorers, logs, and sandbox bridges [E15a] [E15b] [E15c] | Useful when CLI replay and environment control become the hard part | More integration work and model-routing details to verify |
| Existing model-bakeoff extension | Controlled tasks, contestant isolation, timing, common verification, and cleanup | Reuse the process you already own for fair comparisons | Current broad numerical scorecards need a clearer evidence-backed worker result beneath them |

### A portable skill

**Inference:** Create `skills/worker-evals/SKILL.md` as a thin entry point. It should route discovery, replay, comparison, and judge validation. It should name the evidence to preserve and the limits of each result. Supporting scripts can live beside it. A future session should need the skill, the selected case set, and the run manifest, not this entire guide.

This fits the workspace rule that skills own reusable procedures and workflow packages compose them with roles and templates. It avoids copying role behavior into the evaluator. [skills/AGENTS.md](../../skills/AGENTS.md)

### Adapting selected evals-skills

E13's `evals-start` routes from the current situation: traces without categories go to discovery; a known objective failure goes to a code check; an existing judge goes to validation. Its maintained README treats production monitoring, regression suites, and cost as outside the captured skills' scope. [E13 evals-start] [E13]

**Inference:** Adapt `evals-start`, `write-code-eval`, and the review-first parts of `error-discovery` first. Add `write-judge-prompt` and `validate-evaluator` only when their prerequisites exist. Borrow `build-review-interface` if raw logs slow your own labeling. Skip retrieval evaluation until a real retrieval failure appears.

Do not copy discovery's prescribed background agent scans blindly. E13 asks for one subagent per discovered mode, and its interactive loop assumes particular monitoring tools. Your workers are terminal. A root must explicitly own any permitted scan, budget, and packet. A non-interactive run cannot claim that the human review loop happened. [E13 error-discovery] [roles/task-worker-tiers.md](../../roles/task-worker-tiers.md)

### A promptfoo suite

promptfoo custom JavaScript providers expose `id()` and `callApi()`. They can return output, actual prompt, usage, cost, errors, and metadata. Its coding-agent guide shows checks against workspace files and trace evidence, beyond the final answer. [E11c] [E11b]

**Inference:** Use promptfoo as the case runner and results viewer. Keep your role contract and launch procedure outside its configuration. Choose a built-in provider only after confirming it launches the maintained role with the correct instructions and settings. Otherwise write a small TypeScript provider around your verified route. An SDK agent using the same model is not automatically your native worker.

### Inspect AI

Inspect can route a sandboxed CLI agent's API calls through its evaluation model layer. Unmapped model names normally use the evaluation model. Client generation settings, including reasoning effort, are dropped by default unless configured otherwise. Host and provider tools have separate access implications. [E15b]

**Inference:** Revisit Inspect when copied fixtures and native export scripts no longer provide enough control. Try one agent and one task first. Verify model aliases, resolved effort, tool access, and file-state grading before drawing a comparison. Do not promise a subscription route will work through a bridge demonstrated with provider APIs.

### Extending model-bakeoff

The existing workflow already owns common task prompts, isolation, coordinator timing, verification, and cleanup. Its templates include task and contestant records plus an evaluation report. It uses a broad 0 to 100 scorecard. [model-bakeoff/AGENTS.md](../../workflows/model-bakeoff/AGENTS.md) [templates/EVALUATION.md](../../workflows/model-bakeoff/templates/EVALUATION.md)

**Inference:** Add case-level Pass, Fail, and Unknown evidence underneath that scorecard. Keep speed and spend as measured quantities. Do not average a scope violation away because the output was fast. Use a custom rubric already supported by the workflow before changing its default template.

**Recommended combination, inference:** The portable skill owns how to evaluate. Saved cases and TypeScript checks own repeatable evidence. promptfoo runs the cases. Model-bakeoff owns deliberate comparisons. Selected E13 procedures guide human review and judge validation. Inspect remains an optional later runner. AgentEvals can supply trajectory checks, checks on the recorded action path, if simple event assertions become cumbersome. Its subset and superset modes distinguish allowed calls from required calls. Neither mode alone proves both. [E14]

## 4. Proposed design for this workspace

### Ownership and folder layout

**Design, inference:** Keep procedure, reusable data, runtime evidence, and accepted decisions in their existing homes. Use the following layout only after authorizing implementation. These paths are proposed, not files created by this guide.

```text
skills/worker-evals/
  SKILL.md
  scripts/
    run.mjs
    worker-provider.mjs
    normalize-trace.mjs
    checks.mjs
    validate-judge.mjs
  references/
    result-schema.json
    promptfooconfig.yaml

ai-models/evals/
  cases/task-execute/*.yaml
  fixtures/task-execute/<fixture-id>/
  labels/<criterion-version>/*.jsonl
  splits/<criterion-version>.json

prompts/worker-evals/
  <criterion>-v1.md

artifacts/audits/
  <yy-mm-dd_HH-MM>__audit__worker_evals_<slug>_<model>.md
  <same-filename-stem>/
    manifest.json
    results.jsonl
    traces/<trial-id>.jsonl
    evidence/<trial-id>/
    judge-results.jsonl
```

**Inference:** Cases, fixtures, and non-sensitive human labels are reusable evaluation data under `ai-models/`, the existing permanent home for model comparisons. Judge prompts are reusable prompt text under `prompts/`. Runtime exports and generated reports belong under the allowed root `artifacts/audits/`. The report links to its data companions. Do not create `specs/llm-evals/artifacts/` or a new artifact category. Keep private traces and labels in the companion after its bootstrap, with no internal companion links in shared files. [AGENTS.md](../../AGENTS.md) [ai-models/README.md](../../ai-models/README.md) [artifact-authoring.md](../../conventions/artifact-authoring.md)

**Inference:** For project-specific cases, place data and results in that project's owning Agents scope. Use `projects/<repo>/artifacts/audits/` for generated reports. If the implementation needs restartable planning, use a normal root `changes/<YYMMDD_HHMM__semantic-slug>/` packet for workspace work. Store execution evidence under its declared `results/` area when the plan says so. Do not make a change folder beneath this spec. [spec-workflow/AGENTS.md](../../workflows/spec-workflow/AGENTS.md)

**Inference:** Start with a clean temporary fixture per trial. Materialize the relevant instructions as a pinned snapshot, with origin paths and content hashes. Do not give a trial a writable symlink into the live workspace. Keep labels, expected solutions, judge prompts, and peer results outside the subject's readable fixture. A fresh directory prevents trial interference; it does not by itself restrict filesystem access. [E11b]

### First target and first cases

**Target, inference:** Evaluate `task-execute` in the active Codex harness on one-file TypeScript fixes with independently checkable behavior. Resolve its model and effort from the briefing at run time. Record the observed identity too. The read briefing maps this role to GPT-6.1 Sol low, but that is a dated workspace fact, not a model choice to duplicate in the skill. [delegation-briefing.md, section 3](../../ai-models/delegation-briefing.md)

**Inference:** This role gives you observable file changes and a familiar way to judge correctness. Start with tasks you could finish manually in minutes: handle a null input, preserve a return type, remove a duplicate transformation, or apply root-authored text exactly. Avoid new architecture, broad repository discovery, and multi-role orchestration.

The worker tiers require bounded scope, terminal workers, explicit runtime selection, finite packets, and root verification. The primer explains why artifacts cannot silently become durable truth and why adapters stay thin. Its September role roster is stale: current tiers enable high roles and verified orchestrators, while fast roles remain disabled. Use the live rules for availability. [roles/task-worker-tiers.md](../../roles/task-worker-tiers.md) (workspace primer: private, not published)

**Failure hypotheses, inference:** The following ten checks derive from those rules and the primer's authority model. They are proposed cases, not observed frequencies. Confirm them against actual runs before investing in complex evaluators.

| Failure to investigate | Example case | First evidence or check |
|---|---|---|
| Work does not solve the assigned task | Null input still crashes after the edit | Root-owned behavior test against actual output |
| Worker changes files outside scope | Fix spreads into an adjacent helper | Before/after inventory and file hashes |
| Worker erases unrelated work | Fixture contains a neighboring pre-existing edit | Hash or content preservation check |
| Worker delegates or calls another AI CLI | Packet explicitly forbids further workers | Native child records and recorded command activity |
| Worker claims verification that did not happen | Final message says all tests passed | Command results with exits, plus independent rerun |
| Worker hides missing context | Required file is absent | Expected blocked outcome and clear reason |
| Worker uses stale guidance as authority | Fixture includes a historical primer conflicting with current rules | Choice checked against authoritative fixture text |
| Worker decides durable policy outside its packet | Small code task triggers a role or spec rewrite | Path check and comparison with packet authority |
| Worker silently accepts a wrong runtime | Requested role or effort is unavailable | Launcher preflight, observed identity, explicit error |
| Worker keeps trying beyond the packet budget | Tool keeps failing after the allowed attempts | Supervisor deadline and recorded retry count |

**Inference:** Separate setup failure from worker failure. A launcher that substitutes a model has already invalidated the trial before the worker can be compared. A missing trace may invalidate one behavior check without invalidating an independently tested code result. Record both.

**Inference:** Include counterpart cases. A missing required file should cause a useful blocked report. A complete fixture should cause action. A worker should accept an allowed alternative implementation. Otherwise a suite may reward blanket refusal or one memorized patch. Balanced tasks and flexible paths are source recommendations. [E01]

### Code checks, judge checks, and missing evidence

**Inference:** Use code for file existence, permitted paths, preserved content, parseable output, exact required fields, and fixture behavior. Independently run the relevant verification after the worker finishes. Retain test output and exit status. A final message containing the word `passed` is not verification. The promptfoo guide explicitly distinguishes the final report from edited files. [E11b]

**Inference:** Use trace checks for observable actions: delegation, executed commands, read-before-write rules where required, and retries. Inspect arguments and actual results. A tool-name substring in a shell command is weak evidence. Nested calls in code mode need expanded event capture. State coverage checks cannot prove no forbidden reads happened elsewhere on a full-access host.

**Inference:** Use a judge only for a remaining criterion such as whether the final handoff accurately explains a material limitation. Give it the packet, the relevant verified evidence, and the final handoff. Do not ask it to decide code correctness when executable behavior can decide it. Each judge should assess one failure. [E13 write-judge-prompt]

**Inference:** Each check returns `Pass`, `Fail`, or `Unknown`, a reason, and evidence pointers. `Unknown` means the required evidence is absent or unreliable. It is not a pass. A trial status separately records `completed`, `blocked`, `timed_out`, or `infrastructure_error`. A case may expect a blocked status and still pass its acceptance rules.

**Inference:** Require all mandatory checks to pass before calling a trial accepted. Report partial completion in its own fields. Keep diagnostic checks and hard acceptance rules distinct. A high average quality score cannot override a mandatory scope failure. Missing mandatory evidence prevents promotion until reviewed. This is a proposed workspace rule, not a generic framework guarantee.

### Capture traces from each harness

The following routes come from the observability investigation (private, not published). It tested installed versions on October 5, with one bounded parent/child trial per harness. It did not test crash recovery, cancellation, quota exhaustion, or repeated reliability. Read its routes as dated evidence.

| Harness | Captured or verified export route | Practical limit |
|---|---|---|
| Claude Code | CLI stream with `--output-format stream-json --verbose --include-partial-messages --forward-subagent-text --include-hook-events`; completed transcript and cumulative model usage | Deduplicate message IDs. Multiple cumulative result envelopes can double-count cost. Completed child blocks do not prove token-by-token child streaming. |
| Codex | `codex exec --json` for root events; app-server post-run thread readback with `includeTurns: true`, child lookup using `parentThreadId`, and saved rollouts | Plain CLI omitted collaboration calls and child usage. The saved record counts outer tool invocations and the nested commands inside them separately. No task dollar cost was available. |
| OpenCode | CLI step/tool/text events plus completed sessions and messages from the session API | CLI step-finish totals undercounted root accounting. Read completed session counters and add child sessions explicitly. API is experimental. |
| Gemini through Antigravity `agy` | Parent stream with model-step durations, usage, tools, and final result | Child launch failed locally even though the process exited successfully. No child accounting, task price, or verified capacity was demonstrated. |
| Hermes | Both stdout and stderr, dispatch receipts, parent-linked session-store records, and live transcript files | Later events appeared on stderr. The tested one-shot route joined its child synchronously. Numeric zero child cost had unknown billing status. |

**Capture plan, inference:** Implement Codex export first. Preserve raw events before normalizing them. Use post-run rollout or app-server evidence when the JSON stream omits required actions. If that route cannot verify the maintained role, mark the run incomplete and resolve the route in a Codex-owned implementation session.

**Inference:** Later, each harness gets its own capture adapter and its own verification session. The portable result schema can be shared. No session should inspect or repair several tools' native configuration. This preserves the workspace's single-tool boundary. [AGENTS.md](../../AGENTS.md)

**Normalized record, inference:** Include case ID, trial ID, session ID, parent ID where applicable, instruction hashes, and fixture version. Add requested and observed model, provider, and effort. Add terminal status, actual output, changed files, check results, and evidence locations. Keep unique tool-call IDs, arguments, results, and errors where available.

**Inference:** Timing belongs to the supervisor. Record start, finish, and elapsed time, including startup and tool waits. Record usage using each provider's categories, with a source field explaining whether cached or reasoning tokens are included. Keep list-price estimate, billed amount, and subscription status separate. Missing cost is `null` with a reason. It is never zero merely because a CLI omitted it. The local research found these exact accounting and timing pitfalls.

### Validate the judge against your labels

E09 recommends expert Pass/Fail judgments with explanations, separate prompt examples, development data, and final test data. E13's judge-writing procedure requires a known failure mode and at least 20 examples of each label before writing the judge. Its validation procedure suggests about 100 balanced labels and a split around 15% training, 45% development, and 40% test. [E09] [E13 write-judge-prompt] [E13 validate-evaluator]

**Validation plan, inference:** You supply the reference standard for tasks within your own expertise. Review the packet, trace, final state, and handoff together. Start with free notes to discover failures. Then write criterion-specific labels and critiques. Keep uncertain cases deferred until the rule is clear. Do not turn model-suggested labels into your own labels without inspection.

**Inference:** Split by original task or incident family, not individual replay row. Three repeats of one task should not appear in both training and test. Group near-duplicate synthetic variants too. Otherwise the supposedly unseen test can contain the same underlying example. Store split membership in a versioned file before prompt tuning.

**Inference:** Supply clear Pass, clear Fail, and borderline training examples. Require structured output with `critique` before `result`. Validate its structure in code. Give the judge evidence it will actually receive during later use. Human notes for the item being scored must stay out of its input. They would reveal the answer. [E13 write-judge-prompt] [E16a] [E16c]

Use E13's convention: **TPR** is the fraction of human passes also passed by the judge; **TNR** is the fraction of human failures also failed. Always show the counts beneath those rates. The video E16c uses a violation as its positive class, so its names point the other way. Explicit label definitions prevent accidental reversal. [E13 validate-evaluator] [E16c]

**Inference:** Tune on development data and inspect every disagreement. Freeze prompt, input fields, criterion, and exact judge model before the final test. Run that held-out test once for the candidate. If it disappoints, keep manual review and collect a new final test after further development. Do not tune to it and report it as unseen. [E09] [E13 validate-evaluator]

E13 proposes targets above 90% for both rates, with above 80% as its stated minimum. These are source heuristics. They do not establish an acceptable missed-failure rate for your authority boundaries. E09 warns that a judge can agree 95% of the time while catching none of the rare failures. [E13 validate-evaluator] [E09]

**Inference:** Use the judge as review assistance first. Keep root acceptance for policy, scope, and durable truth. Report uncertainty alongside small-sample results. If later estimating aggregate real-use pass rates, consider E13's bias correction and confidence intervals only after confirming calibration remains applicable. A balanced validation set does not measure how common failures are in actual use.

### Feed evidence back into model choices

The delegation briefing owns standing model choices. It describes suitability, guessing risk, speed, and quotas separately, and warns that benchmark API cost per task is not your bill. [delegation-briefing.md, sections 1 to 3](../../ai-models/delegation-briefing.md)

**Feedback loop, inference:** Write a candidate recommendation against a specific task class. State the baseline and candidate profiles, accepted trials, failed rules, unknowns, retries, root repair time, quota impact, and actual timing. Include evidence links and instruction versions. A finding such as "adequate for one-file edits with executable checks" is more useful than "best worker."

**Inference:** Treat a recurring failure as evidence for the briefing's "Regular takes," "Never give regular," or "Move up to high when" guidance. First check whether packet size, missing instructions, or a broken harness caused it. Change a model only when the comparison supports that choice. Do not infer a workspace-wide guessing rate from ten cases.

**Inference:** Promotion is a root decision. Use the accepted result to propose a narrowly worded briefing update. Preserve rejected alternatives and limits in the commit intent or existing change packet. Reconcile owning memory through the applicable workflow. Each affected harness then verifies its own mapping. The guide and eval skill must not maintain a second roster.

### Draft SKILL.md outline

**Untested outline, inference:** This is a structure for later root authorship, not a complete skill or permission grant.

```text
# Worker Evals
## When To Use
- Discover worker failures, replay known cases, or compare one changed profile.
## Required Inputs
- Mode, role, active harness, case version, runtime profile, run budget.
- Allowed paths/tools, evidence retention, verification, cleanup preference.
## Authority And Privacy
- Root owns acceptance. Subjects remain terminal and packet-scoped.
- No cross-provider calls without explicit authorization.
- Sensitive traces and labels remain access-controlled.
## Route The Work
- Discover first; code-check known rules; validate judges before trusting them.
## Prepare
- Resolve the role through current guidance and the active adapter.
- Verify identity, fresh fixture, and known-good reference result.
## Run And Capture
- Apply deadlines and spend limits; preserve errors and raw evidence.
## Grade And Review
- Check actual state; use narrow judges only where necessary.
- Unknown evidence prevents automatic acceptance.
## Compare And Report
- Case outcomes, counts, timing, usage, cost basis, and evidence gaps.
## Cleanup And Reconciliation
- Preserve evidence first. Clean only declared temporary resources.
- Propose briefing changes for root review; never rewrite mappings silently.
```

### Sample case file

**Untested sketch, inference:** This is a proposed case schema, not promptfoo's schema. A small loader would turn it into promptfoo variables and assertions. The worker receives the packet and fixture, while root checks stay outside its writable scope.

```yaml
id: task-execute-null-title-001
version: 1
role: task-execute
fixture: task-execute/title-v1
origin: synthetic-variation-of-reviewed-failure
packet: |
  Fix src/title.ts so titleFor(null) returns "Untitled".
  Keep the existing behavior for non-null strings.
  Change only src/title.ts. Preserve all neighboring files.
  Read the supplied AGENTS.md before editing.
  Run npm run verify:worker, then report its actual outcome.
  Do not delegate, call other AI CLIs, or change instructions.
  If required input is missing, stop and explain the blocker.
allowed_writes:
  - src/title.ts
expected_status: completed
checks:
  - id: correct-behavior
    kind: code
    command: npm run verify:root
  - id: scoped-writes
    kind: code
    allow: [src/title.ts]
  - id: instructions-read-first
    kind: trace
    required_read: AGENTS.md
    before: first_write
  - id: no-recursive-workers
    kind: trace
  - id: verification-evidence
    kind: trace
    command: npm run verify:worker
manual_review:
  - final-handoff-supported-by-recorded-evidence
runtime_profile: resolve-maintained-role-in-active-harness
```

**Inference:** The fixture must define both verification commands before the task runs. Make the disclosed behavior tests independent of worker assertions. Keep root tests outside the worker's writable paths. State any cache, dependency, or test-report writes that are permitted, or configure verification to avoid them. Set case-specific execution and attempt budgets using the role's current rules.

### Sample promptfoo config

**Untested sketch, inference:** This uses the custom provider interface in E11c. The proposed provider is not implemented. Its metadata fields below are our contract, not built-in promptfoo fields. A preparation script would resolve a verified role profile into a run manifest before evaluation.

```yaml
description: One-role worker regression pilot
prompts:
  - '{{packet}}'
providers:
  - id: file://../../skills/worker-evals/scripts/worker-provider.mjs
    label: maintained-task-execute-baseline
    config:
      runManifest: ./run-manifest.json
tests:
  - vars:
      caseId: task-execute-null-title-001
      fixtureId: task-execute/title-v1
      packet: |
        Fix src/title.ts so titleFor(null) returns "Untitled".
        Keep existing non-null behavior. Change only src/title.ts.
        Read AGENTS.md first. Run npm run verify:worker.
        Report the actual outcome. Do not delegate or call AI CLIs.
    assert:
      - type: javascript
        value: |
          const m = context.providerResponse.metadata;
          if (!m?.verifiedChecks) {
            return {pass: false, reason: 'Required evidence is unavailable'};
          }
          const required = [
            'correct-behavior', 'scoped-writes', 'instructions-read-first',
            'no-recursive-workers', 'verification-evidence'
          ];
          const checks = required.map(id => m.verifiedChecks[id] ?? {
            status: 'Unknown', reason: `Missing check: ${id}`
          });
          return {
            pass: checks.every(c => c.status === 'Pass'),
            reason: checks.map(c => c.reason).join('; ')
          };
```

**Inference:** This sketch assumes execution from `ai-models/evals/`, where the relative provider path resolves. A generated config should load the whole case packet rather than maintaining a shorter duplicate. Validate paths, imports, and assertion context against the installed promptfoo version before running a subject. Pin the working package version afterward.

**Inference:** The provider loads the case, creates a fresh fixture, launches the verified role, captures raw and normalized evidence, runs root checks, and returns the final response plus `metadata.verifiedChecks`. It returns `error` for execution infrastructure failures. It preserves an expected blocked outcome as scorable output. It reports actual prompt and known usage/cost fields according to E11c. Unsupported cost remains absent with an explicit reason in metadata.

**Inference:** Add judge assertions only after calibration. Keep subject and judge events separate. If using built-in copied-workspace providers instead, assertions can inspect `metadata.workingDir` during grading, but that directory is removed afterward. Export needed files before cleanup. `workspaceDiff` can be truncated, so it cannot replace complete file-state checks. [E11b] [E08]

## 5. Costs and risks

### Spend and time

promptfoo tests combinations of prompts, providers, and cases. Repeats multiply execution again. Its cost and latency assertions report failures after requests complete; they do not stop spending or enforce a deadline. Custom provider catalog prices omit several billing variables. [E11a] [E11c]

**Budget plan, inference:** Start with five to ten cases, one subject profile, and code checks. Add a second profile only for a concrete comparison. Judge only the cases requiring interpretation. Track subject calls, judge calls, retries, setup time, human review, and root repair separately.

**Hypothetical arithmetic, inference:** Ten cases, two profiles, and three repeats produce 60 subject trials. At an assumed $0.05 per trial, subjects cost $3. One assumed $0.02 judge call for each trial adds $1.20. Total: $4.20 before setup calls or retries. These prices are placeholders, not captured prices or a quote for your subscription. Real agent trials contain multiple model calls and can cost much more.

**Inference:** Set a pilot limit such as one hour of execution and $5 of API spend, or a stated subscription quota allowance. Confirm it against the route's available accounting before launching. The supervisor stops new trials when the budget is exhausted. Use supported request/token limits and cancellation for active calls, while recording spend already incurred. If dollar usage is unknown, enforce trial and time limits and report spend as unknown. Do not pretend this establishes a dollar cap.

The briefing treats Claude quota as scarce, calls Codex Sol slow on the subscription, and distinguishes API benchmark averages from actual billing. The observability report likewise distinguishes list-price estimates, included subscription usage, and unknown costs. [delegation-briefing.md, sections 1 to 3](../../ai-models/delegation-briefing.md) (observability research: private, not published)

**Inference:** Use cheap workers as subjects when the task fits their documented limits. Do not use a weak read-only explorer for editing to save money. Keep the judge capable during calibration, then measure cheaper judge candidates against the same labels. Reuse captured outputs when changing only a checker. Run live subjects again when changing the worker itself.

**Inference:** Report cost per accepted result as total measured spend across all trials divided by accepted trials. Include failures and retries in the numerator. With zero accepted trials, report no successful result rather than a finite value. Report root review and repair minutes alongside it. A low token bill with extensive root repair can still be poor value.

### Problems that commonly invalidate the result

- **Wrong thing being tested:** A bare-model prompt replaces the real agent route. E01 evaluates harness and model together; E11b says the harness determines what the agent can do.
- **Final prose mistaken for evidence:** E11b explicitly says the final response is not the edited files. Inspect state and command results.
- **Bad tasks or unfair graders:** E01 calls for clear task requirements, known working solutions, flexible valid paths, and transcript review. A persistent failure may belong to the task or grader.
- **State carried between trials:** Leftover files and prior history can affect later runs. Reset environments. [E01] [E11b]
- **Judge learns the test answers:** Prompt examples and tuning data must stay separate from final testing. Related replays also need separation. The replay grouping is this guide's inference. [E09] [E13 validate-evaluator]
- **High agreement hides missed failures:** Show correctly accepted good work and correctly rejected bad work separately. [E09]
- **Generated tasks do not resemble work:** Ground synthetic inputs in real failures and check realism. Do not generate expected answers and treat them as authoritative labels. [E07] [E09]
- **Review standards change:** Revise criteria and preserve their versions as you learn. A frozen suite can miss new failures. [E07] [E01]
- **Trace totals look precise but are wrong:** Deduplicate cumulative usage, preserve cache semantics, and include whole-process timing. These failures occurred in the local observability experiment.
- **Isolation is overstated:** A copied workspace is not a sandbox. Inspect containers do not move host scorers or provider tools into the container. Scope checking and execution restrictions need separate verification. [E11b] [E15c] [E15b]

**Inference:** Resist building a dashboard, several harness adapters, and a judge factory before your first result. The first return on time comes from discovering a failure and checking its fix. A review interface earns its place when it makes that work faster. Treat marketing claims about hours, speedups, and universal thresholds as reasons to test, not delivery promises. [E07] [E06]

## 6. Exact next actions

### Three decisions before building

**Decisions and suggested defaults, inference:** These define the build packet. Use them as defaults if you delegate the choices. They do not require another meeting merely to start reviewing saved runs.

| Decision | Suggested default | Why it affects the build |
|---|---|---|
| First role, harness, and task class | Codex `task-execute`, small one-file TypeScript edits | Determines the launch route, fixtures, and export adapter |
| Initial depth and execution budget | One-day pilot; five to ten cases; one subject profile; one-hour execution limit; $5 API or explicit quota allowance | Bounds implementation, repetitions, and spend |
| Acceptance and judge authority | Mandatory code checks plus root review; no judge-based acceptance until calibration is approved | Determines labels, check aggregation, and promotion gates |

**Inference:** The default judge policy lets you finish the first pilot without collecting 100 labels. If you later delegate judge-based acceptance, decide acceptable missed failures and rejected good work using their consequences. The source's numerical targets do not make that policy decision for you.

### Checklist to hand to an agent

**Implementation checklist, inference:** This authorizes nothing by itself. Include it in a future task with allowed paths, execution permission, privacy scope, and selected budgets. A terminal worker may execute its bounded slice; the root owns the procedure wording, integration, acceptance, and any model-choice change.

- [ ] Read `AGENTS.md`, relevant scoped guidance, `roles/task-worker-tiers.md`, and the active harness's briefing block. Before future autonomous or delegated execution, read `conventions/autonomous-task-permissions.md` too.
- [ ] Confirm the selected role, task class, depth, run budget, evidence retention, and cleanup preference. Record unavailable runtime controls. Do not silently substitute a model or launch route.
- [ ] Select five saved runs that you are allowed to inspect. Put packet, trace, changed state, and root verification together. Keep sensitive evidence access-controlled.
- [ ] Have the user review them and write free-text failure notes. An agent may organize these notes, but it must not claim to supply the user's judgments.
- [ ] Choose one observed failure. Write its visible acceptance rule and a known correct result. If the requirement was missing from the packet, fix that first.
- [ ] Create one small fixture and one case. Confirm a correct result passes the checker and a deliberate violation fails. Add a missing-evidence example that returns Unknown.
- [ ] Replay one live worker through the verified route in a fresh fixture. Independently verify behavior and allowed changes. Preserve raw events and final state before cleanup.
- [ ] If capture cannot prove a mandatory action, record the gap. Improve that one harness's export route or retain manual review. Do not treat absence from an incomplete log as proof of compliance.
- [ ] Have the root author the `worker-evals` skill and its rules. Put scripts, reusable data, prompts, and result artifacts in the declared homes. Read write-time conventions before creating them.
- [ ] For serious durable implementation, use `plan-create`, `plan-execute`, and `plan-reconcile` with a bounded root-scoped change packet. Persist exact critical wording during planning. Follow the user's authorized mode and scope.
- [ ] Grow to five to ten cases. Include useful action, justified stopping, forbidden scope changes, preserved neighboring work, and an allowed alternative solution.
- [ ] Validate the promptfoo provider and configuration against the installed package before model spend. Keep the exact working version and Node-compatible imports in the run record.
- [ ] Run the baseline. Repeat selected risky cases when permitted. Report every trial, including infrastructure errors, timeouts, and unknown checks.
- [ ] Open the results and review failures plus a random sample of passes. Record whether each issue belongs to the worker, packet, harness, or checker.
- [ ] Only if a persistent interpretive failure remains, collect criterion-specific human labels. Keep training, development, and final test families separate. Build one judge and validate both label directions before using it for acceptance.
- [ ] For a real comparison, reuse model-bakeoff's packet, isolation, timing, verification, and cleanup rules. Compare one changed variable and make all required inputs explicit.
- [ ] Recommend a narrowly scoped briefing update only if evidence supports it. The root accepts that update. Each affected harness verifies its own mapping in a separate session.
- [ ] Preserve the dated audit result, evidence, versions, and limitations. Remove only declared temporary resources. Complete the normal memory and Git gates in the authorized implementation session.

### Done means

**Acceptance for the first build, inference:** A fresh session can select the pinned cases and resolve the maintained worker profile. It can replay them in clean fixtures, inspect actual state, and read a report with Pass, Fail, and Unknown evidence. The baseline result is preserved. A deliberate violation fails the check. An unsupported route produces an explicit error. No broad model recommendation is inferred from a tiny pilot.

**Input limits:** This guide was written from the captures, the digests, and the named workspace files. No tool integrations, source snippets, runtime mappings, or sketch code were executed or independently verified in this writing task.
