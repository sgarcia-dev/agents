---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [E16c]
purpose: One-source digest feeding the spec compendium.
---

# Isaac HW3 (Session 2) (E16c)

**What it is:** A live homework walkthrough and Q&A led by Isaac, with contributions from Hamel. Published on Hamel Husain's channel on 2025-07-03. The metadata gives 4,921 seconds, about 82 minutes. [Watch the video](https://youtu.be/1d5aNfslwHg).

**Capture status:** Full auto-generated transcript. Caption fragments were joined without word changes. No source chapters were supplied. The capture contains spoken explanations, not the notebook, displayed code or charts. Exact code identifiers cannot always be recovered.

Caption uncertainty: “Shrea” and “Treya” likely mean Shreya, while “Hamill,” “Haml” and “Hamilton” likely mean Hamel. These are guesses supported by the packet context. “GPT40” likely means GPT-4o, but the capture does not confirm its spelling. Script and library names below retain the caption spelling rather than silently repairing it.

## The point in three sentences

Build a model-based judge for one specific failure, here whether a recipe follows a requested dietary restriction. Human labels, separate datasets and careful inspection matter more than copying a finished solution. Measure the judge's mistakes and uncertainty before using its labels to estimate performance on new traces, meaning recorded application runs.

## Key ideas

- Reuse application code when generating evaluation responses. Otherwise the experiment may measure a different system from the one users encounter. “you want to minimize the differences between what your production application is doing and what these experiments are doing.” [00:04:09]
- Synthetic labels, labels produced by another model, are a shortcut that needs human checking. Isaac permits them as a starting point; Hamel advises beginners to label manually so the judge learns their standard rather than another model's mistakes. “it's a proxy and it adds noise” [00:08:16]
- Separate training examples, development data and final test data. Training examples can go into the prompt; development data supports repeated inspection and changes; test data checks performance on less familiar cases. “You need to know how well does this do and stuff that I haven't seen before.” [00:09:19]
- Check the number of failures in every split, not just its total size. Stratified splitting means keeping roughly the same pass/fail proportions across sets; labeling more data is another practical option. “I've got a 100 examples in the training set, but I've only got one failure.” [00:12:06]
- Looking at a test mistake can change future prompt decisions even without copying the case. The optional-cheese example shows how a dairy-free test case quietly becomes an idea for an instruction or example. “Oh, it's recommending optional cheese.” [00:20:10]
- Choose prompt examples because they teach something the judge misses. A chicken recipe marked nonvegetarian may teach less than a subtle ingredient case; start without examples if the instructions already work. “think about the things that it's likely to be confusing or unclear and add examples based on that” [00:27:46]
- Examples should resemble the judge's actual inputs and include the label and a sound explanation. Long traces may require shorter examples, but the reasoning needs deliberate human review. “you want to show examples that look exactly like what the LLM judge is going to see when it comes time to grade things.” [00:29:37]
- Measure both directions of error. Here a positive means a dietary violation: true positive rate is the share of actual violations caught; true negative rate is the share of compliant responses correctly accepted. “what could happen if they go wrong.” [00:38:39]
- Perfect test results warrant inspection of the pipeline, realistic examples and domain expertise. They do not establish perfect production behavior. “is my evaluation broken?” [00:34:47]
- There is no universal acceptable accuracy or uncertainty threshold. Hamel also corrects the discussion's drift toward product accuracy: this stage measures the judge's accuracy. “we're talking about the accuracy of the LM judge and not the accuracy of your product at this point.” [00:45:06]
- A confidence interval is a range showing uncertainty in an estimate. Bootstrapping, repeatedly resampling the labeled data with replacement, illustrates how the measured rate varies; it cannot cover every missing case or external change. “There's things outside the data.” [00:58:08]
- Apply the same judge prompt and input fields to new traces. On labeled test data, compare its answer with the known label; on unlabeled production data, only its answer is available, so the demonstration uses bias correction to account for measured judge errors. “When we do it on production, all we have is what the judge said the label is.” [01:11:15]
- Build separate judges for separate failure modes, meaning distinct ways the product can fail, and add them gradually. Using a judge as a runtime self-critic changes the application and requires evaluating that changed system. “you want different judges for different failure modes.” [01:13:38]
- Prioritize by frequency and consequence. An unclear cooking instruction and a recipe violating an allergy constraint have different user effects even if the first happens more often. “not every failure mode is equal.” [01:18:42]
- Refresh datasets when real users reveal unexpected behavior. Reusing a test set is practical, but synthetic prelaunch queries may require substantial revision. “There's always something surprising about how the users end up actually asking questions or using something” [01:17:02]

## How to do it (concrete steps, checklists, templates)

1. Choose the narrow task, dietary adherence, and start from queries, raw traces or labeled traces depending on how much of the homework you want to implement. Generate chatbot responses using the application's backend code. [00:00:51], [00:03:33]
2. Create pass/fail labels. The supplied labeler also emits high, medium or low confidence. Manually label data first to learn the cases; if using generated labels, inspect at least a sample and replace unreliable labels manually. Hamel recommends manual labels at the outset. [00:05:16]–[00:08:37]
3. Split the data. Isaac's simple example assigns random values below 0.15 to training, below 0.55 to development, and the remainder to test, giving 15%, 40% and 45%. Inspect set sizes and pass/fail counts. [00:09:19]–[00:12:27]
4. If the data seems too small, label more. As a stability check, remove 15% or 20%, repeat the experiment and see whether results change. Consider stratified splitting to preserve class proportions. [00:12:58]–[00:15:32]
5. Start with a judge prompt defining restrictions and evaluation criteria. Add selected training examples for confusing cases rather than automatically choosing random ones. Match the expected query/response inputs, include the label and carefully written reasoning, and inspect synthetic queries too. [00:25:05]–[00:33:21]
6. Evaluate on development and test data. Inspect both error directions and write down their user consequences, such as missed allergy violations versus unnecessary rejection or retry delay. Review suspiciously perfect results. [00:33:30]–[00:41:52]
7. Estimate uncertainty. In the demonstration, resample the same number of observations with replacement, calculate each sample's success rate and repeat 10,000 times. Remove the bottom and top 2.5% of rates to obtain the middle 95% interval. Label more if its width prevents a useful decision. [00:49:22]–[01:00:30]
8. Run the same judge on new traces with the same prompt and fields: query, dietary restriction and response. The full evaluation uses a library for corrected metrics. The transcript explains the purpose of correction but does not provide a reliable formula or complete implementation. [01:07:18]–[01:11:24]
9. Use the judge as a tracked evaluation metric, add further judges one at a time, and revise datasets as production usage changes. Choose the next failure using both frequency and impact. [01:14:13]–[01:21:00]

## Tools, code and commands named

- Caption spellings: `dietary queries.csv`, `generate traces.py`, `label.py`, `split data.py`, `develop judge.py`, `run full evaluation.py`, `judge prompt txt`, and “test predictions JSON.” [00:01:29], [00:03:33], [00:05:01], [00:13:46], [00:25:05], [01:07:18], [01:09:04]. These are spoken names, not verified executable paths.
- Backend “utils” and “git agent response” are mentioned as production imports. The latter likely garbles a function name, but its exact identifier is unavailable. [00:03:40], [00:04:16]
- “GPT40,” “scikitlearn,” `numpy` and “judgy” appear in the captions. No package versions or runnable commands are supplied. “judgy” is described as handling corrected metrics; its spelling is uncertain. [00:05:16], [00:22:51], [00:54:51], [01:07:18]
- A book is named “statistics unlocking the power of data,” with authors described as “lock lock and lock.” The formal title and author list are not confirmed. [00:52:38]
- Kaggle, Discord and CI/CD pipelines are mentioned. CI/CD means automated build, test and delivery pipelines. [00:16:07], [01:14:07], [01:21:05]

## Numbers and strong claims

- The displayed judge has 100% true positive rate and 75% true negative rate. These are results on the shown dataset, not production guarantees. [00:33:30]–[00:38:39]
- The bootstrap example starts with 850 passes and 150 failures, an 85% rate. After 10,000 resamples, the stated middle 95% range is 82.7%–87.2%. [00:49:22]–[00:50:57]
- A later comparison gives an 85% rate with 20 labels and a 70%–100% interval, versus 1,000 labels and an 82.8%–87.1% interval. These are illustrative results; the transcript does not expose all calculation details. [00:58:42]–[01:00:02]
- The final evaluation covers 2,400 previously unevaluated traces. Its final success rate is not stated in the capture. [01:07:18]
- Bootstrapping is called better “in almost every case.” This is Isaac's broad opinion, not a demonstrated general result. Hamel later explicitly limits what an interval can tell you. [00:48:43], [00:58:08]
- “you're almost always missing something” when accuracy is perfect is practitioner advice, not a statistical theorem. [00:37:03]
- The bias-correction explanation first assumes a judge is 90% accurate, then later says it is wrong 90% of the time. That is inconsistent as captured, possibly a verbal slip or caption error. Do not derive a correction rule from these numbers. [01:07:48], [01:11:24]

## Compared with the deep research report

The report does not discuss this video directly. Its relevant sections are 3.2, on the Recipe Chatbot repository, and 2.3, on Hamel's judge methodology.

- **Supported:** The report describes “progressive exercises, worked notebooks, and linked video walkthroughs” and calls HW3 “Implementing model-based evaluation.” This capture supplies that walkthrough, beginning “This is homework three.” [00:00:00]
- **Supported:** The report recommends “Choose one narrow failure mode, label examples yourself” Hamel's contribution reinforces manual labeling and alignment with the user's judgment: “you want like your own labels.” [00:07:23]
- **Added detail:** The report's code-and-data framing does not explain the gap between a finished notebook and the actual iterative work. Isaac says “eval isn't a static process.” [00:00:06] The supplied synthetic labeler and random prompt examples are demonstrations, not instructions to trust labels or select examples blindly.
- **Added detail:** The video makes test contamination concrete through optional cheese, explains both judge error rates, demonstrates uncertainty by resampling and shows how the same prompt reaches unlabeled production traces. [00:20:10], [00:34:09], [00:38:39], [00:50:57], [01:09:26]
- **Added nuance:** It permits practical test-set reuse, distinguishes judge accuracy from product accuracy and prioritizes separate judges by frequency and user consequence. [00:16:07], [00:45:06], [01:13:38], [01:18:42]
- **Wrong or overstated:** No direct contradiction is established by this capture. It does not independently verify the report's claims about other homework assignments, repository contents or course access.

## Fit for the user's agent workspace

- (inference) Begin with one worker failure, such as exceeding the packet's scope. Define a separate pass/fail judge for it before attempting an overall worker score.
- (inference) Record actual worker runs through the same harness used for real work, so evaluation does not quietly change execution behavior.
- (inference) Hand-label a first batch of runs. Use a stronger model's labels as suggestions that need checking, rather than treating model strength as proof of correctness.
- (inference) Keep examples used in judge prompts separate from development and final test cases. Select subtle scope or completion errors that teach the intended standard.
- (inference) Compare accepting bad work with rejecting good work. Their costs differ: accepting an unauthorized edit may matter more than requiring another review of correct work.
- (inference) Track uncertainty alongside judge agreement. Expand the labeled set when the observed range could change a model-selection decision.
- (inference) Keep cost measurement alongside this process. The video does not teach how to combine token cost, completion quality and scope compliance into one worker-value score.

## Best parts to read or watch first

- [00:03:33]–[00:08:37], about 5 minutes: production code reuse and the disagreement over automatic ground-truth labeling.
- [00:19:44]–[00:22:37], about 3 minutes: a memorable example of test-set contamination.
- [00:25:05]–[00:32:56], about 8 minutes: selecting useful examples and writing their reasoning.
- [00:33:30]–[00:41:52], about 8 minutes: interpreting judge errors and their user effects.
- [00:48:13]–[00:52:38], about 4.5 minutes: the basic bootstrap demonstration. Then [00:56:27]–[01:00:18], about 4 minutes, for limits and sample size.
- [01:07:18]–[01:17:02], about 10 minutes: production scoring, separate judges and dataset refresh. Read [01:17:41]–[01:21:00], about 3 minutes, for prioritization.
