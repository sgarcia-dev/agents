---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [E07]
purpose: One-source digest feeding the spec compendium.
---

# A Field Guide to Rapidly Improving AI Products (E07)

**What it is:** Hamel Husain, March 24, 2025. A practical blog article drawing on consulting work, with screenshots, illustrative Python code and linked demonstrations. About 6,452 captured Markdown words, roughly 26 to 32 minutes to read (estimate). [Original article](https://hamel.dev/blog/posts/field-guide/).

**Capture status:** Full, according to the capture frontmatter. Main article, resources and footnotes were captured and checked against live HTML: 6,544 visible-text words versus 6,452 Markdown words. Images and videos are linked, but their contents are not transcribed in this file. No article-text omission is declared.

## The point in three sentences

Improve AI by reading its actual interactions, finding repeated failures and testing fixes against those failures. Make review easy, let domain experts change prompts directly, and generate realistic test inputs when real usage is scarce. Keep automated evaluation tied to human judgment, and plan bounded experiments before promising uncertain capabilities.

## Key ideas

- Start with error analysis, meaning inspection and grouping of actual failures. Generic scores can improve while the user's task still fails. Quote: “When everything is important, nothing is.” Location: section 1, The Most Common Mistake: Skipping Error Analysis.
- Build failure categories from observations rather than imposing broad labels first. The NurtureBoss team wrote notes, used a language model to group them, then counted labeled conversations. Quote: “let metrics naturally emerge.” Location: Bottom-Up vs. Top-Down Analysis.
- A useful viewer puts the interaction and its supporting context together. Review friction discourages people from examining subtle failures. Quote: “Show all context in one place.” Location: section 2, data annotation tool checklist.
- Make judgments quick without losing explanation. Pair simple buttons with open notes, filters and keyboard navigation. Quote: “One-click correct/incorrect buttons beat lengthy forms.” Location: section 2, data annotation tool checklist.
- Let domain experts edit and test prompts themselves. Engineers translating expert slide decks into prompts adds an unnecessary handoff. Quote: “prompts are just English.” Location: section 3, Empower Domain Experts To Write Prompts.
- Test prompt edits inside the actual application, including its data retrieval, tools and business logic. A standalone prompt playground is only a starting point. Quote: “admin versions of their actual user interface that expose prompt editing.” Location: Build Bridges, Not Gatekeepers.
- Use precise language people understand. Explain the specific behavior being added rather than hiding it behind the word agent. Quote: “Being specific helps everyone understand what’s actually happening.” Location: Tips For Communicating With Domain Experts.
- Synthetic data means generated test inputs. Cover capabilities, situations and user types, then check that the inputs really exercise the intended cases. Quote: “A way to verify that generated queries actually trigger intended scenarios”. Location: A Framework for Generating Realistic Test Data.
- Generate inputs rather than model-written expected answers, and respect actual system limits. Otherwise the test data can inherit the generating model's limitations. Quote: “Generate user inputs, not outputs”. Location: Guidelines for Using Synthetic Data.
- Criteria drift means your definition of acceptable work changes as you review outputs. Treat that as learning and reconcile differing stakeholder standards. Quote: “They treat evaluation criteria as living documents”. Location: Understanding Criteria Drift.
- Prefer pass/fail with a written critique over unclear numerical scales. The decision tracks acceptability; the explanation records nuance and can teach a model evaluator through examples. Quote: “did this output achieve its purpose or not?” Location: Favor Binary Decisions Over Arbitrary Scales.
- A model evaluator, also called an LLM-as-a-judge, needs repeated comparison with human labels. Simple ordering and formatting changes can bias its judgments. Quote: “regularly check how well these automated evaluations align with human judgment.” Location: Measure Alignment Between Automated Evals and Human Judgment.
- Reduce review effort only after understanding agreement and disagreement patterns. Keep humans focused on weak areas and continue calibration, meaning repeated checks against their judgments. Quote: “particularly focusing on areas where alignment is weakest.” Location: Scaling Without Losing Trust.
- Plan experiments with time limits and decision points. A capability funnel means stages of increasing usefulness, from an output that runs to one that solves the user's problem. Quote: “time-box your exploration, establish clear decision points”. Location: Experiments vs. Features.
- Evaluation infrastructure makes experiments interpretable; sharing failed experiments makes their lessons available. Copilot used existing repository tests for offline completion checks, while Eugene Yan describes short weekly updates and informal sharing. Quote: “In my fifteen-fives, I document my failures and my successes.” Location: Build a Culture of Experimentation Through Failure Sharing.

## How to do it (concrete steps, checklists, templates)

The article's sequence is inspection, review tools, expert prompt editing, generated test data, trustworthy judging, then experiment planning.

**1. Inspect and categorize failures.** In the NurtureBoss example:

- Read actual conversation logs and write open-ended notes about undesired behavior, one conversation per spreadsheet row.
- Use a language model to build a taxonomy, meaning a set of failure categories, from those notes.
- Map rows to categories and count each issue, using tools such as pivot tables.
- Build tests for the failures found and measure improvement on those tests.

**2. Build the review interface.** The source's checklist, in order:

- Show all context together.
- Make correct/incorrect feedback easy.
- Capture open-ended feedback.
- Enable fast filtering and sorting, for example by channel or property.
- Add hotkeys for navigation and annotation.

Use a familiar framework. A spreadsheet is an acceptable start; a custom application can follow as needs grow.

**3. Enable expert prompt work.** Start with a playground that supports prompts, example datasets and comparisons. Then expose prompt editing in an admin version of the actual product interface. Describe changes in concrete language suited to the audience.

**4. Generate realistic test data.** Identify features, scenarios and user personas. The example defines property search, market analysis, scheduling and follow-up; exact, multiple, zero and invalid matches; and four buyer types. Prepare varied underlying data and verify that it can support each scenario.

The illustrative `generate_search_query(scenario, persona, listing_db)` retrieves listings using a persona's price range and preferred areas. It rejects a multiple-match case with fewer than two listings and a no-match case with any listings. It then asks a model to generate a natural-language query using the customer description, scenario and actual listings. This is explicitly illustrative pseudo-code, not a complete runnable implementation.

Ground cases in actual listing IDs and addresses, schedules, booking restrictions and local details. Run the inputs through the assistant and log the interactions. When there is no production database, the article permits generating the underlying data too, while saying that detailed synthetic-database construction is outside its scope.

The synthetic-data checklist, in order:

- Diversify features, scenarios and personas.
- Generate user inputs, not expected responses.
- Incorporate real system constraints.
- Verify coverage by running cases and checking what they trigger.
- Start simple, then add complexity.

**5. Establish and maintain trustworthy judgments.** Favor binary decisions, add detailed critiques, then compare automated results with human judgments. AlignEval's workflow is to upload data, label examples good/bad, compare model judges with those labels, inspect disagreements, refine criteria and measure improvement.

To scale, retain this order: start with high human involvement; study where automated and human judgments agree; sample informative cases, especially weak areas; maintain regular calibration. The source does not provide a sampling formula or mandatory review percentage.

**6. Plan experiments and communicate progress.** The query capability funnel progresses through valid syntax, execution without errors, relevant results, matching user intent and an optimal query that solves the problem. Establish evaluation infrastructure so each experiment has measurable results. Time-limit data feasibility, technical feasibility and prototype work, with clear proceed or pivot decisions. Share failures and successes through short updates and regular discussion.

## Tools, code and commands named

- Review and development: Excel Pivot Tables, spreadsheets, Cursor, Loveable, FastHTML, MonsterUI, python and PowerPoint. These are examples or author preferences, not a required stack.
- Prompt playgrounds: Arize, Arize Phoenix, Langsmith and LangSmith (both spellings appear), Braintrust.
- Judge alignment: Eugene Yan's AlignEval.
- Example applications: Nurture Boss/NurtureBoss, Rechat's Lucy, Honeycomb Query Assistant, GitHub Copilot.
- Illustrative Python names: `features`, `scenarios`, `personas`, `generate_search_query`, `listing_db.get_sample_listings`, `persona.price_range`, `persona.preferred_areas`, `persona.description`, `format_listings`, `generate_with_llm`, `ValueError`. The dimension lists use `multiple matches` and `no matches`, while checks use `multiple_matches` and `no_matches`; another reason to treat this as illustration.
- Referenced reading: “Who Validates the Validators?”, “Your AI Product Needs Evals”, “Creating a LLM-as-a-Judge That Drives Business Results”, “What We’ve Learned From A Year of Building with LLMs”, and the course “AI Evals For Engineers & PMs”. These linked resources were not read for this digest.
- No install commands, shell commands or package versions are supplied. GPT-4 appears in an example about unreliable self-grading, not as a recommended evaluator version.

## Numbers and strong claims

- Introduction: experience helping **30+ companies**. Author's self-reported basis for the advice.
- Section 1: a **10% helpfulness-score improvement** despite unresolved user problems. Anecdotal warning, not a controlled result.
- The Error Analysis Process: date handling failed **66%** of the time; reported success rose from **33% to 95%**. Case-study claim; the capture gives no sample size or uncertainty and does not explain the rounding difference.
- Bottom-Up vs. Top-Down Analysis: **three issues accounted for over 60%** of problems. They were conversation flow, handoffs and rescheduling. Case-study claim without a denominator.
- Section 2: viewers enable **10x faster** iteration and can be built **in hours**. Broad promotional/opinion claims; no comparative study is given.
- Understanding Criteria Drift: completely determining criteria before human judging is said to be impossible. Strong claim attributed to the cited research; this capture does not establish a universal proof.
- Enhance Binary Judgments With Detailed Critiques: example critiques reportedly yield **15-20% higher agreement**. Author observation; no study setup or explanation of relative percentage versus percentage points.
- Measure Alignment: Honeycomb reached **>90% agreement after three iterations**. Specific case report, not a universal trust threshold; the captured text does not explain its agreement calculation.
- Experiments vs. Features: Eugene's example allocates **two weeks** to data feasibility, **one month** to technical feasibility and **six weeks** to an A/B-testable prototype. An example schedule, not an instruction to use those exact durations.
- The Foundation: Copilot ran **thousands of experiments**. Historical practitioner account without a detailed count.
- Failure Sharing: a weekly **fifteen-five** takes **15 minutes to write and five to read**. A proposed communication practice.
- A Better Way Forward: **two-week updates**, **two to three months** with no success, then a solution within **a month**, with a breakthrough addressing **80%** of the problem. Anecdote, not a forecast.
- Section 6 and Conclusion: counting experiments is presented as the key roadmap measure, and principles are said to apply regardless of domain, team size or stack. Broad author opinion, not demonstrated general validity.

## Compared with the deep research report

Read only E00's field-guide entry, its field-guide-linked diagnostic advice and its Inspect-stage row.

- **Right:** E00 says the guide covers “inspecting real data, identifying failure patterns, building useful review interfaces”. E07 directly supplies these practices, including “Show all context in one place.” E00's framing as an engineering feedback loop is fair.
- **Right:** E00 advises “Do not invent a large taxonomy before seeing your data.” E07 says to “let metrics naturally emerge.” The report's exercise of writing notes and grouping failures accurately adapts the bottom-up process.
- **Overstatement or wrong detail:** No clear factual error in these excerpts. “Best practical methodology” is E00's recommendation, not a comparison proven by E07. E00 proposes “manually examine 20–30 real runs”; E07 says “After annotating dozens of conversations”. The precise batch size is the report's own starting suggestion, not the guide's rule, and E00 appropriately limits the statistical claim.
- **Important omissions:** The entry and linked exercise concentrate on inspection. E07 also says “Generate user inputs, not outputs” and “Verify scenario coverage”, which prevent misleading generated tests. It covers direct expert prompt editing inside the application, changing criteria, pass/fail plus critiques, recurring human/model agreement checks and careful review sampling.
- **Important omission:** E00's Inspect row ends with a reviewed batch and failure list. E07 goes further into planning: “time-box your exploration, establish clear decision points”. It adds progressive capability stages, evaluation infrastructure and sharing failed experiments. These make the guide more than an initial labeling exercise.

## Fit for the user's agent workspace

- (inference) Start with actual worker runs and open notes. Derive failure categories such as misunderstood task or incorrect handoff from observed examples rather than assuming a universal rubric.
- (inference) A small TypeScript viewer could show the task packet, instructions, tool activity, outputs and reviewer notes together. Use the user's familiar stack; the Python preference is incidental.
- (inference) Let the user edit role and skill instructions while replaying realistic packets through the actual harness. An isolated prompt test can miss tool and workflow effects.
- (inference) Generate task inputs across worker responsibilities, situations and user styles. Use fixture repositories with known contents, and verify that the intended failure situation really exists.
- (inference) Judge completion with pass/fail and a concrete explanation. Keep reviewer labels and revisit unclear standards before trusting a cheap model judge.
- (inference) Run bounded comparisons of instruction or model changes and record lessons from failures. Adapt the experiment cadence rather than copying the article's multi-month schedule.
- (inference) Add separate cost and scope checks for this workspace. E07 does not supply cost-per-task accounting, worker authorization tests, cross-harness replay rules or a ready-made agent evaluator.

## Best parts to read or watch first

Reading times below are estimates for the captured text, not source-provided timings.

- **The Error Analysis Process + Bottom-Up vs. Top-Down Analysis:** 2 to 3 minutes. The shortest path from vague dissatisfaction to specific tests.
- **Section 2, A Simple Data Viewer:** 3 minutes. A directly usable interface checklist.
- **A Framework for Generating Realistic Test Data + Guidelines for Using Synthetic Data:** 4 to 5 minutes. Read the grounding checks, not just the dimension lists.
- **Understanding Criteria Drift + Creating Trustworthy Evaluation Systems + Scaling Without Losing Trust:** 6 to 8 minutes. Read before relying on a model judge.
- **Experiments vs. Features + The Foundation: Evaluation Infrastructure:** 3 to 4 minutes. Useful for deciding what a first evaluation project should promise.
- **Linked error-analysis videos:** the Jacob example and live walkthrough are linked in section 1. Their durations and contents are not available in this capture, so no watch-time estimate is justified.
