---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [E05, E05b]
purpose: One-source digest feeding the spec compendium.
---

# Your AI Product Needs Evals (E05, E05b)

**What it is:** Hamel Husain's introductory article, published March 29, 2024. It explains application-specific evaluation through Lucy, Rechat's real estate assistant. [Read the article](https://hamel.dev/blog/posts/evals/). No reading time is supplied; allow roughly 20 minutes for the prose and examples, longer to study the code.

**Capture status:** Both captures are marked full. E05 captures an empty visible page with a JavaScript redirect to the destination article. Its author and publication date are unknown. E05b captures the full destination post, including tables, code, conclusion and four footnotes. Screenshots and diagrams are linked images, rather than transcribed data. The listing-data prompt deliberately omits confidential parameters, so that example cannot be reproduced fully from this capture.

## The point in three sentences

Measure whether your application does users' tasks, rather than treating general model benchmarks or a few promising examples as proof. Build cheap assertions first, then inspect recorded runs and align a model evaluator with human judgments. Reuse the same records, checks and review tools to debug failures and prepare training data.

## Key ideas

- Evaluation supports a repeated cycle of measuring quality, debugging and changing behavior. Improving prompts alone leaves the other two activities unsupported. Quote: "Many people focus exclusively on #3 above" (Iterating Quickly == Success).
- Growing feature coverage can expose conflicting prompt fixes. Lucy plateaued when one fix caused other failures, visibility remained weak and prompts became unwieldy. Quote: "Addressing one failure mode led to the emergence of others" (Case Study: Lucy, A Real Estate AI Assistant).
- The three evaluation levels differ in cost and cadence. Cheap assertions can run on every change; human/model review runs periodically; A/B tests compare product variants with real users after larger changes. Quote: "The cost of Level 3 > Level 2 > Level 1." (The Types Of Evaluation).
- A unit test here is a fast assertion about an LLM application's behavior. Organize assertions so they can also clean data or guide retries when a check fails. Quote: "these assertions should run fast and cheaply" (Level 1: Unit Tests).
- Break features into scenarios with observable outcomes. Lucy's listing finder checks whether a query returns one, several or no listings; a separate generic check catches exposed UUIDs, the identifiers attached to CRM records. Quote: "break down the scope of your LLM into features and scenarios" (Step 1: Write Scoped Tests).
- Synthetic inputs, examples generated rather than collected from users, can get testing started before launch. Update them as real failures appear and make them challenging while remaining representative. Quote: "You don’t need to wait for production data to test your system." (Step 2: Create Test Cases).
- An acceptable pass rate depends on which failures the product can tolerate. The article does not prescribe a universal threshold. Quote: "Your pass rate is a product decision" (Step 2: Create Test Cases).
- Track results together with test and prompt versions. Existing continuous integration, or CI, and analytics can be enough to start. Quote: "collect metrics along with versions of your tests/prompts outside your CI system" (Step 3: Run & Track Your Tests Regularly).
- A trace groups the events of a run, such as a conversation and its responses. Useful trace tools must support searching, filtering and reading the records. Quote: "tracing is a logical grouping of logs" (Logging Traces).
- Human review should show the domain context needed to understand what happened. Lucy's interface combines feature/scenario information, input origin, filters and links to the CRM and trace record. Quote: "You must remove all friction from the process of looking at data." (Looking At Your Traces).
- Start with good/bad labels instead of elaborate numerical scores. Read broadly at first, then sample more as repeated review yields fewer new lessons. Quote: "I often start by labeling examples as good or bad." (Looking At Your Traces). The stopping heuristic is "keep reading logs until you feel like you aren’t learning anything new" (Footnote 3).
- A model judge, an LLM that critiques another model's response, needs its own evaluation process. Compare its labels and reasons with a human's, improve its prompt and keep checking alignment. Quote: "You must maintain a mini-evaluation system to track its quality." (Automated Evaluation w/ LLMs).
- Raw agreement can hide errors when almost all examples have the same label. The article recommends precision and recall: how often the judge's selected cases are right, and how many actual cases it catches, for the class being measured. Quote: "using raw agreement is generally not recommended" (Important Note on Using Agreement as a Metric).
- Fine-tuning, training a model further on task examples, and RAG, supplying retrieved context, address different needs. Evaluation helps filter and correct training examples, while its records also support debugging. Quote: "Fine-tuning is best for learning syntax, style, and rules" (Fine-Tuning).

## How to do it (concrete steps, checklists, templates)

The article gives this order, while noting that the overall improvement process is not strictly linear.

1. **Write scoped tests.** Split a feature into scenarios. For the listing finder, use queries that should return exactly one result, multiple results or zero results. Add generic checks across features. The JavaScript `noExposedUUID` example removes text inside double curly braces, searches the remainder for UUID patterns and asserts zero matches.
2. **Create test cases.** Generate inputs that exercise those scenarios. The contact example requests 50 pairs of instructions: create a contact, then look up that contact. Execute both instructions and assert that the CRM returns exactly one result. Also run generic checks. Update the cases using human review and debugging observations.
3. **Run and track tests regularly.** Use the execution path with the least friction in the existing stack. Store results over time, plus test and prompt versions, outside CI for analysis. The example uses Metabase to visualize error frequency before and after a fix.
4. **Log traces before adding human/model evaluation.** Record the sequence of events. Choose a system where reviewers can search, filter and read runs. Rechat uses LangSmith; its LangChain integration records trace events automatically. LangSmith does not require LangChain.
5. **Build a useful review view.** Show the tool/feature and scenario, whether input was synthetic or real, filters for feature/scenario combinations, and links to the CRM and trace logger. For Lucy, make final output editable so a human can correct examples for training. Label good/bad and analyze those results over time.
6. **Read broadly, then sample.** Husain initially reads all test-case traces and user-generated traces. Over time, sampling reduces effort. Footnote 3 suggests reading until no new lessons emerge.
7. **Align a model evaluator with a human.** The spreadsheet contains `model response`, `model critique` and `model outcome`, a binary good/bad label. A human supplies their critique, outcome and desired response for 25-50 examples at a time. Use those differences to improve the evaluator prompt and track its quality. The example used raw agreement on a roughly balanced dataset; the article warns to use precision and recall generally.
8. **Keep checking the evaluator.** Use the most powerful model affordable for critique, maintain checks of its quality and periodically compare its judgments with a human's after initial alignment.
9. **Add A/B testing when ready.** Compare whether product variants cause desired user behaviors or outcomes. The article permits postponing this until the product is ready for real users and supplies no detailed experiment recipe.
10. **Reuse the infrastructure.** For training data, generate listing queries, filter responses through Level 1 assertions and Level 2 critiques, then review traces with the existing human interface. For debugging, search traces, flag bad behavior, locate the cause, change the system and test the fix.

The listing synthesis template asks for 50 natural-language searches using real city and neighborhood names, with a JSON array as output. Its allowed search parameters are omitted. Detailed RAG evaluation and a full fine-tuning procedure are outside this post's scope.

## Tools, code and commands named

- Testing/code: `pytest` (linked documentation path `en/8.0.x/`), JavaScript function `noExposedUUID`, `message.comment`, `replace`, `matchAll`, `expect`, `len(listing_array)`, regex and JSON code blocks. No package installation command or shell command is supplied. The pytest URL is a documentation version, not a stated project dependency.
- Execution and charts: GitHub Actions, GitLab Pipelines, Metabase and Excel.
- Tracing: LangSmith and LangChain. Footnote 2 names `arize`, `human loop`, `openllmetry` and `honeyhive` as other examples.
- Review interfaces: Gradio, Streamlit, Panel, Shiny, Shiny for Python and Lilac. Lilac is described as supporting semantic search and filtering, meaning search by meaning rather than only exact text.
- Other named resources: CodeSearchNet, GitHub CoPilot, Rechat, Lucy, Zillow, Eppo blog, Jason Liu's RAG article, Vanishing Gradients podcast, AI Evals For Engineers & PMs and a fine-tuning course. These are examples or links, not required components.
- No evaluator model name, model version, complete runnable test suite or TypeScript implementation is provided.

## Numbers and strong claims

- **Three levels, increasing cost:** Level 3 costs more than Level 2, which costs more than Level 1 (The Types Of Evaluation). This is the author's operational model, not a measured cost table.
- **Hundreds of unit tests:** Rechat maintains hundreds and updates them as new failures appear (Step 1: Write Scoped Tests). No exact count or results dataset is supplied.
- **50 generated inputs:** Both contact-case generation and listing synthesis request 50 examples (Step 2: Create Test Cases; Data Synthesis & Curation). These are prompt choices, not minimum sample-size requirements.
- **100% is not mandatory:** A perfect test pass rate is not required for every product (Step 2: Create Test Cases). This is product advice, not permission to ignore any particular failure.
- **Less than a day:** Lightweight review tools can be built in less than a day (Looking At Your Traces). Author experience/opinion; scope and effort evidence are absent.
- **25-50 human-reviewed examples per batch:** The colleague grades this many at a time (Automated Evaluation w/ LLMs). This describes one workflow, not sufficient statistical coverage for every judge.
- **About 50% failures:** The example dataset was roughly balanced, explaining its use of agreement (Important Note on Using Agreement as a Metric).
- **99% of fine-tuning labor is data assembly:** Quote: "99% of the labor involved with fine-tuning is assembling high-quality data" (Fine-Tuning). Strong opinion or rhetorical estimate, with no supporting measurement.
- **Failure and success claims:** Unsuccessful products "almost always" lack sound evaluation (Motivation), and the heading says "Eval Systems Unlock Superpowers For Free". These are broad experience-based and promotional claims. The body still describes substantial review, data and tooling work.
- **Course banner:** "Join 5,000+ engineers & PMs" and "25% off" appear in the navigation banner. Marketing, not evidence of evaluation effectiveness.

## Compared with the deep research report

Only E00's section 1.2 about this article was read for this comparison.

- **Right:** The report describes application-specific measurement and connects it to "human inspection, automated checks, and iteration". The article explicitly calls for "product evals tailored to your users’ tasks" (Motivation) and supplies the three-level workflow. The report's 2024 publication year matches March 29, 2024 in E05b.
- **Right:** The report says the value is "the development process, not a particular vendor’s dashboard". The article says "Use what you have first" (Conclusion), despite naming several tools.
- **Qualification:** "Best first article" is the report's ranking. The capture supports introductory suitability but cannot establish that ranking. The report's regression-testing analogy is useful interpretation, not a claim made in those exact terms by the source.
- **Added exercise:** E00 says "write five examples of behavior that would make you reject a worker’s output" and gives a file-citation failure. The article says to "Write lots of tests and frequently update them" (Conclusion), but does not give that five-example worker exercise. Treat it as the report author's adaptation.
- **Important omissions:** E00 does not explain the cost/cadence ordering, reusable assertions, paired create/look-up cases, trace-interface fields, binary labels, judge calibration or the warning about raw agreement. It also omits reuse for training data and debugging. The source's instruction to "maintain a mini-evaluation system" (Automated Evaluation w/ LLMs) is especially relevant before trusting automated worker grades.
- **Link handling:** E00 links to `/evals/`. E05 confirms that this is an empty redirect, and E05b supplies the actual article. This is a capture distinction, not a substantive error in the report's summary.

## Fit for the user's agent workspace

- (inference) Copy the feature/scenario method for bounded workers. Turn observed failures into checks such as an output file existing, required sections being present or the result staying within its assigned scope.
- (inference) Keep cheap deterministic checks separate from judgments about whether the work solves the task. Run the cheap checks frequently, then review the failures and uncertain successes.
- (inference) Adapt the trace view to show the task packet, harness, worker response, tool actions and resulting files together. The article's lesson is to remove the cost of reconstructing context during review.
- (inference) Begin human review with pass/fail plus a reason. Use those judgments to tune a separate model judge, and check both accepted failures and rejected successes before trusting it.
- (inference) Track prompt/test versions with outcomes when comparing worker settings. Cost and elapsed time could be added for the user's value-for-money question, but this article does not supply a cost-effectiveness formula.
- (inference) Start with existing scripts and a simple table or viewer. A new evaluation platform is not required by the article's method.
- (inference) Defer A/B testing and fine-tuning unless the workspace develops a concrete need for them. This source does not address multi-harness permissions, worker authority boundaries or a complete agent-specific scoring system.

## Best parts to read or watch first

Times below are reading estimates, not source-provided timings.

- **Step 1: Write Scoped Tests through Step 3: Run & Track Your Tests Regularly:** 6-8 minutes. The closest match to familiar engineering work, with JavaScript and paired test examples.
- **Looking At Your Traces, including How much data should you look at?:** 3-4 minutes. Read before designing a review interface or an elaborate scoring form.
- **Automated Evaluation w/ LLMs, including Important Note on Using Agreement as a Metric:** 4-5 minutes. The most useful section before asking a model to grade cheap workers.
- **Conclusion:** about 1 minute. A compact reminder of the workflow and the preference for simple tools.
