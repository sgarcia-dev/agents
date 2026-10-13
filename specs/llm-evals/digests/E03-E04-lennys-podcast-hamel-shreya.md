---
created_at: 2026-10-13
model: gpt-6.1-sol (medium)
doc_type: digest
source_ids: [E03, E04]
purpose: One-source digest feeding the spec compendium.
---

# Why AI evals are the hottest new skill for product builders (E03, E04)

**What it is:** Lenny Rachitsky interviews Hamel Husain and Shreya Shankar, September 25, 2025. A podcast with a live walkthrough of an apartment-management AI assistant. Video length: 01:46:33, about 107 minutes. [YouTube](https://www.youtube.com/watch?v=BsWxPI9UM4c) and [published episode page](https://www.lennysnewsletter.com/p/why-ai-evals-are-the-hottest-new-skill).

**Capture status:** E03 is full automatic English captions, spanning [00:00:00] to [01:46:31], with description and chapters. Words and speaker markers are not human-verified; screen contents are not independently captured. E04 is partial as an article: public preview, show notes, references, chapters and full public published transcript are present; the paid “My biggest takeaways from this conversation” section is excluded. These are two captures of one episode, not independent supporting sources. This digest uses E03 for content and locations, and E04 to clarify unclear caption words. Chapter labels can precede the actual discussion; the show notes’ tips chapter at [01:22:28] is out of order, while tips begin around [01:26:28].

## The point in three sentences

Evals are the whole process of systematically measuring and improving an AI application, including reading its real logs. Start with a domain expert’s observations, group actual failures, and automate only the checks worth maintaining. A model that judges another model needs its own validation against human labels, with separate attention to missed failures and false alarms.

## Key ideas

- **Evals are broader than unit tests.** They include discovering new user groups, user feedback, monitoring and experiments, as well as tests of required behavior. “Evals is a big spectrum of ways to measure application quality.” [00:08:38]

- **Look at data before choosing what to test.** An LLM, a large language model, can fail in ways its builders did not anticipate; writing tests from imagined requirements misses those problems. “You should start with some kind of data analysis to ground what you should even test.” [00:10:26]

- **A trace is the sequence of events in a run.** The Nurture Boss example includes instructions, customer messages, tool calls, returned data and responses; seeing only the final response would hide useful evidence. “it's a detailed log of everything that happened.” [00:13:53]

- **Correct facts can still produce a bad product experience.** The assistant accurately reports no suitable apartment, but ends a potential lead instead of handing it to a human; the recruiting-email example later shows the same distinction between correct fields and useful writing. “But with your product hat on, you know, that's not correct.” [00:18:42]

- **Open coding means writing free-form observations first.** Note the first upstream error, meaning the earlier failure that can cause later problems, rather than exhaustively labeling everything in a trace. “Don't worry about all the errors.” [00:22:18]

- **Humans supply missing business context.** An outside model may approve an offer of a virtual tour because it does not know that the business offers none; initial discovery is a poor place to substitute generic model judgment. “it's so important to make sure you are manually doing this yourself.” [00:24:38]

- **One trusted expert can keep review affordable.** The “benevolent dictator” is a person with relevant domain knowledge, often a product manager, rather than a committee deciding every label. “It should be the person with domain expertise.” [00:27:16]

- **Stop initial review when new failure types stop appearing.** They call this theoretical saturation, meaning more review no longer changes the next decisions; 100 traces is a starting suggestion, not a statistical guarantee. “It's when you are saturating or you're not uncovering any new types of notes” [00:30:42]

- **Axial coding means grouping observations into failure categories.** A model can propose groups after a human has written notes, but the human should refine vague labels into problems they can act on. “That's not actionable.” [00:35:30], about the proposed category “capability limitations”.

- **Preserve a way to detect incomplete categories.** Let automated classification choose “none of the above”, then inspect those notes and revise the groups rather than forcing every observation into an existing bucket. “my axial codes are not complete.” [00:43:40]

- **Counting helps prioritize, but severity matters too.** A pivot table, a spreadsheet summary by category, shows recurring problems; a less frequent but serious handoff failure may deserve priority. “it's not necessarily the count is the most important thing” [00:45:24]

- **Prefer code when it can check the behavior.** Formatting, JSON validity and response length can be checked cheaply; a model judge is more suitable for a narrow contextual decision such as whether a human handoff was required. “One is codebased which you should try to do if you can because they're cheaper.” [00:48:05]

- **Give each model judge one failure and a binary decision.** Binary means two possible outcomes, such as pass/fail; a general quality score hides what should change. “Is this good enough or not?” [00:52:47] They object to averages such as 3.2 versus 3.7 without a clear meaning.

- **Validate the judge, not just its prompt.** Compare its decisions with human labels and inspect both kinds of disagreement; high overall agreement can conceal a judge that never detects the rare error. “90% agreement might look good on paper but it might be misleading” [00:59:10]

- **Requirements change as people inspect outputs.** Criteria drift means the definition of good behavior changes with experience; Shankar’s study found even experienced developers could not write all their requirements in advance. “People's opinions of good and bad change as they review more outputs.” [01:04:21]

- **Maintain a small useful set and reuse it.** Fix obvious bugs directly; reserve costly judges for persistent or risky failures, then use the same checks in release tests and production monitoring. “You can't write an eval for everything.” [01:06:01]

- **The debate often mixes different meanings of evals.** Dogfooding, using your own product, can provide unusually direct feedback when developers are also domain experts; that situation does not generalize to every product. “coding agents are fundamentally very different than other AI products because the developer is the domain expert.” [01:13:22]

- **Make review easy and keep improving the product.** A purpose-built interface can hide repeated prompts, show channels and threads, and expose error counts; success is better behavior, not an impressive test collection. “if you see something that's wrong, just go fix it.” [01:30:14]

## How to do it (concrete steps, checklists, templates)

The demonstrated sequence is human discovery, assisted grouping, counting, selective automation, judge validation, then repeated use.

1. **Collect and inspect real traces.** Start with the instructions, conversation, tool requests, tool results and responses. Use an observability tool, software that records and displays application events, or another usable log viewer. The anonymized Nurture Boss assistant handles chat, text and voice, with tools and retrieval of stored information. [00:10:47]–[00:16:28]

2. **Have the domain expert write short notes.** Do not create a fixed taxonomy, a list of categories, yet. Capture the first upstream problem and move on. Keep enough detail for someone else to understand the note. Examples: should have handed off to a human; text messages fragment the conversation; offered a nonexistent virtual tour; transferred a call without telling the user. [00:17:18]–[00:29:35]

3. **Sample rather than reading everything.** Their suggested starting target is about 100 traces, but stop when review no longer uncovers materially new problems. Experience helps recognize that stopping point. [00:29:39]–[00:31:33]

4. **Export the notes and ask a model for groups.** The walkthrough exports a CSV, a table stored as comma-separated values, and uses Claude or ChatGPT to propose axial codes. The E03 description supplies this exact prompt, demonstrated around [00:33:13]:

   > Please analyze the following CSV file. There is a metadata field which has an nested field called z_note that contains open codes for analysis of LLM logs that we are conducting. Please extract all of the different open codes. From the _note field, propose 5-6 categories that we can create axial codes from.

   The mismatch between `z_note` and `_note` is in the source. Use the actual field in your export. They explicitly allow changing the prompt to request actionable categories or grouping by stage of the user’s experience. [00:36:05]

5. **Review and refine the categories yourself.** Compare each proposed group with its original notes. The refined examples include tour scheduling/rescheduling, human handoff/transfer, output formatting, conversation flow, and follow-up promises not kept. Broad categories are a starting point, not the finished result. [00:39:47]–[00:41:14]

6. **Map notes back to the final categories.** Use the revised list, not the model’s first proposal. In the demonstration, Google Sheets with Gemini classifies each note into a category. Include a “none of the above” choice and use those cases to revise the list. [00:41:35]–[00:43:54]

7. **Count and inspect.** Create a pivot table of category counts. Drill into examples where useful. Decide what to fix based on frequency, seriousness and whether the fix is obvious. The demonstration counts 17 conversation-flow issues; it does not provide a denominator sufficient for a failure-rate claim. [00:44:40]–[00:46:04]

8. **Fix easy problems; select worthwhile automated checks.** A missing instruction may only need a prompt edit. Code can test strings, formatting, JSON or length. Choose a model judge for a specific recurring problem that needs contextual judgment, such as human handoffs. [00:46:23]–[00:49:43]

9. **Write a narrow binary judge prompt.** An LLM may help draft it, but read and edit the result. The handoff example outputs true/false for a handoff error and lists situations requiring transfer: explicit requests for a human, policy requirements, sensitive resident issues, missing tool data, and same-day walk-ins or tours. The capture does not give the complete on-screen judge prompt. [00:54:44]–[00:55:58]

10. **Compare the judge with human labels.** In the sheet, column G contains the human judgment and column H the model’s judgment. Existing annotations provide a starting point; review more examples if needed. They mention splitting data so the check is not cheating, but do not teach an exact split or full validation protocol here. [00:56:22]–[00:58:10]

11. **Inspect the four combinations, then revise.** A confusion matrix is a table crossing the human answer with the judge’s answer. With true meaning error present, human true/judge false is a missed failure; human false/judge true is a false alarm. Review both disagreement groups and clarify the prompt. They acknowledge some disagreement is expected, despite later wording about reducing errors to zero; no universal acceptance threshold is given. [00:58:21]–[01:00:48]

12. **Reuse useful checks before releases and on real runs.** Add known failure examples to tests run when code changes. Apply judges to sampled production traces and track specific failure rates in dashboards. Their examples include daily sampling and weekly scheduled scripts, not a required cadence. [00:51:26], [01:07:47]–[01:08:46], [01:31:06]

13. **Ground experiments in discovered errors.** A/B testing means comparing two versions using a success measure. They welcome it when error analysis informs the hypothesis; they warn against testing imagined problems without examining actual runs. [01:16:24]–[01:18:06]

14. **Reduce review friction as the process becomes useful.** Consider a small custom web interface, with repeated system prompts hidden by default, channels and threads visible, and category counts built in. Continue reviewing, updating requirements and fixing behavior. [01:28:08]–[01:30:21]

## Tools, code and commands named

- **Application and log viewers:** Nurture Boss; Braintrust in the live demonstration; “Phoenix Arize” and “LangSmith” in E04’s published transcript, resolving E03’s unclear names. No preferred vendor is claimed. [00:10:53], [00:12:51]–[00:13:28]
- **Grouping and analysis:** Claude projects, ChatGPT, Julius AI, Jupyter notebooks, CSV exports, Excel formulas, Google Sheets, Gemini, and pivot tables. The captions describe formulas without capturing exact executable formulas. [00:32:39]–[00:45:18]
- **Checks and scheduling:** a Python function, JSON, markdown, string/length checks, true/false judge outputs, unit tests, CI, meaning automated integration checks, scripts, cron jobs, meaning scheduled commands, and dashboards. No complete runnable code, install command or pinned software version is provided. [00:46:39]–[00:51:26], [01:07:47], [01:31:06]
- **Other named references:** Andrew Ng’s “Carrying Out Error Analysis”; “Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences”; MMLU, “human eval,” cosine similarity and hallucination scores; Statsig. The generic scores are discussed critically, not recommended as ready-made product metrics. [00:38:21], [01:03:03]–[01:04:44], [01:18:23]–[01:22:43]
- **Coding and course references:** Claude Code, Cursor, Codex and Maven. E04 renders the cost discussion as “GPT-5,” “5-nano,” and “4-mini”; these are source names, not verified API identifiers. The episode advertises cost optimization in the course without demonstrating it. [01:23:11], [01:34:27]–[01:35:16]
- **Peripheral mentions:** Fin, Dscout and Mercury are sponsors. The closing recommendations include *Pachinko*, *Apple in China: The Capture of the World’s Greatest Company*, *Machine Learning*, and *Artificial Intelligence: A Modern Approach*. LennyBot and ElevenLabs concern course assistance or voice features, not demonstrated evaluation infrastructure. [01:36:13]–[01:41:48]

## Numbers and strong claims

- **About 100 reviewed traces:** a practical starting suggestion; they expressly say there is no magic number and mention smaller batches as experience-dependent examples. Not a sample-size proof. [00:29:39]–[00:31:18]
- **5–6 proposed categories:** the published grouping prompt asks for this range. It is not a requirement for all products. [00:33:13]–[00:34:30], E03 description.
- **17 conversation-flow issues:** count in the demonstration, not a production failure percentage. [00:45:05]
- **10% errors, 90% agreement:** an illustrative always-pass judge would agree 90% of the time while missing every error. This motivates inspecting both disagreement types. [00:58:54]–[00:59:10]
- **Four to seven judges:** Shankar’s reported experience, not a target number for every application. Prioritize persistent failures. [01:05:09]–[01:06:03]
- **Three to four initial days; roughly 30 minutes weekly afterward:** Shankar’s experience with initial review, labeling and a few judges. Lenny paraphrases setup as about a week. This is not a guarantee, and recurring effort is not zero. [01:30:37]–[01:31:47]
- **Custom interface built in a few hours:** Nurture Boss anecdote, not a general delivery estimate. [01:29:15]–[01:29:35]
- **“It's the highest ROI activity you can engage in.” and immediate enthusiasm:** practitioner opinion and promotional language, without measured return-on-investment evidence. [00:19:41], [01:29:46]
- **Claude Code’s internal monitoring and review:** Shankar explicitly says she does not know what the team does and is betting they use some form of evaluation. Treat those internal-process claims as conjecture. The episode supplies no comparative model-performance experiment. [01:12:57]–[01:13:22], [01:23:11]–[01:24:10]
- **Statsig acquisition implications:** speakers speculate about strategy and possible emphasis on product-specific metrics; they do not establish what the acquisition will change. [01:20:08]–[01:22:43]
- **Course scale and perks:** over 2,000 learners across 500 companies; number-one Maven course claims; a 160-page book, resolved from E04 because E03 says “a60page”; 10 months of assistant access; and 35% off with the spoken code “Lenny's List”. Promotional claims as of the episode, not independently checked. [00:01:49]–[00:02:46], [01:35:26]–[01:36:48]

## Compared with the deep research report

Only E00’s section 1.1 about this episode was read for this comparison.

- **Right: the learning sequence.** E00 describes “examining traces, to identifying recurring failures,” then choosing code or model evaluation. The episode says, “You should start with some kind of data analysis to ground what you should even test.” [00:10:26] The live walkthrough supports that summary.
- **Right: format, length and access boundary.** E00 says “approximately 107 minutes” and separates the public video from the newsletter’s paid takeaways. E03 gives 01:46:33; E04’s missing section is exactly the paid takeaways. This does not mean the published transcript itself is missing.
- **Slightly imprecise: the suggested ending.** E00 recommends watching through [01:00:51]. That finishes the main judge-validation discussion, but the product-requirements discussion begins there, and selective judge count and reuse follow at [01:05:09] and [01:07:41]. The focused recommendation is reasonable, but incomplete for those topics.
- **No material factual error found in this section.** Calling it the “Best first video” is E00’s recommendation, not a ranking proved by the episode.
- **Left out: judging the judge.** E00 points to the validation chapter but omits why aggregate agreement fails: “90% agreement might look good on paper but it might be misleading” [00:59:10]. Both disagreement types and the data-splitting caveat matter for implementation.
- **Left out: keeping the process affordable.** The one-expert approach, saturation rule, category refinement and “none of the above” option receive no treatment in E00’s short section. Neither does “You can't write an eval for everything.” [01:06:01]
- **Left out: changing criteria and coding-agent context.** “People's opinions of good and bad change as they review more outputs.” [01:04:21] The discussion also explains why developer dogfooding can collapse steps for coding products and warns against generalizing that experience. [01:13:22]–[01:16:22]

## Fit for the user's agent workspace

- **(inference) Copy the review-first sequence.** Sample actual bounded-worker runs, with the task packet, instructions, tool activity and deliverable visible. Write observed failure notes before inventing a large rubric.
- **(inference) Act as the first domain expert.** Your taste and scope expectations can anchor initial labels. Keep observations specific enough that another person or model can categorize them later.
- **(inference) Adapt the categories to your work.** Completion failures, scope violations and weak evidence are possible starting observations to look for, not categories established by this podcast. Let your runs decide the final list.
- **(inference) Use TypeScript checks for measurable requirements.** Adapt the source’s code-first advice to required files, expected structure or check results. Use a narrow model judge only where contextual judgment is necessary, then compare it with your own labels.
- **(inference) Track missed bad work separately from rejected good work.** Overall agreement would be especially misleading if most cheap-worker tasks already pass. The source gives the reason but no universal acceptable error rate.
- **(inference) Use validated quality checks before comparing cheaper models.** The course’s cost discussion supports the direction, but this episode gives no cost-per-task method, latency rubric or worker-value formula. Those need another source or your own design.
- **(inference) Keep coding dogfooding useful, but record it.** As a frontend engineer you can often judge code directly. A small trace viewer or Markdown review table could preserve that feedback across runs and harnesses; the episode does not prescribe an Agents workspace file schema.

## Best parts to read or watch first

- **[00:09:56]–[00:23:54], about 14 minutes:** real traces and first notes. Best concrete explanation of how accurate output still fails the product’s goal.
- **[00:23:54]–[00:31:39], about 8 minutes:** human context, one trusted expert and when to stop reviewing.
- **[00:31:39]–[00:46:06], about 14½ minutes:** model-assisted grouping, human refinement, fallback categories and counting. E04’s show notes preserve the grouping prompt.
- **[00:54:45]–[01:00:51], about 6 minutes:** validate a judge against human labels. Read this before trusting any automated worker score.
- **[01:00:51]–[01:09:57], about 9 minutes:** changing requirements, a small judge set and reuse in tests and monitoring.
- **[01:09:57]–[01:18:23], about 8½ minutes:** eval definitions, coding-agent dogfooding and experiments informed by actual errors.
- **[01:26:28]–[01:31:47], about 5½ minutes:** practical tips, review interfaces and the claimed ongoing time budget.
