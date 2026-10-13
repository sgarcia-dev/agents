---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [E16b]
purpose: One-source digest feeding the spec compendium.
---

# Open & Axial Coding - Isaac & Hamel Walkthrough (E16b)

**What it is:** A live walkthrough with Isaac and Hamel, published on Hamel Husain’s channel on 2025-07-03. Video length: 35 minutes 34 seconds. [Watch the video](https://youtu.be/AKg27L4E0M8).

**Capture status:** Full auto-generated transcript. Caption fragments were joined without word changes. No chapters were supplied. The capture contains spoken discussion, not screenshots, complete notebook code, or all displayed recipe outputs. Isaac’s surname is not supplied. Caption guesses are flagged below.

## The point in three sentences

Open coding means reading outputs and writing free-text notes about what went wrong. Axial coding means grouping those notes into named failure categories, checking the groups, and counting them. This exercise also reveals what the product should do, so people responsible for product decisions should help define failures before an automated evaluator is built.

## Key ideas

- Judge the output for a specific audience. For a beginner recipe app, cooking jargon, unclear quantities, and undefined textures can fail even when the recipe looks plausible. “Yeah, cuz we want this to be a beginner app.” [00:03:46]

- Write open-coding notes in complete sentences. This helps both a later model and your future self understand the observation without reconstructing it. “So, you're like writing complete sentences, which is good.” [00:02:37]

- A conflicting request may need clarification rather than abrupt rejection. With keto snacks containing beans, they consider asking which constraint matters most. “Maybe yeah follow-up questions to clarify what is important.” [00:05:13]

- Acceptable behavior needs an owner. They disagree about whether adjusting salt is too vague, while Isaac rejects an unspecified amount of cayenne. This is a product preference being worked out, not a universal cooking standard. “I'm okay with it with salt because adding salt is normal” [00:07:35]

- Patterns emerge quickly, but new failures can still appear. Unclear quantities recur before the reviewers encounter a separate problem: optional steps mixed into required instructions. “But this is a new one too. The optional step.” [00:09:41]

- Vary the requests you inspect. Isaac notices the synthetic requests contain too much detail and moves to shorter ones to broaden the examples. Synthetic here means constructed requests rather than observed user requests. “So, I added some at the end that didn't have as much.” [00:13:32]

- Error analysis can change the interface or product, not just the prompt. They discuss defaults, dietary buttons, a time slider, measurement preferences, and follow-up questions. “It's like, is your product really defined in the right way causing the experience that you want?” [00:15:23]

- Make requirements concrete enough to test. Isaac decides optional steps should occupy their own line, and checks the existing requirement to show serving size at the beginning. “not mixed in with required stuff.” [00:21:21]

- Single-turn outputs can receive several failure notes. For multi-turn conversations or systems with tool calls, Hamel instead says to start with the earliest causal failure, so later consequences do not distract from it. “This is just a single turn conversation. So, it's totally fine.” [00:24:12]

- Model-proposed categories need human checking. During notebook generation, they are unsure which data the model saw and whether some themes were invented. “I don't remember writing this.” [00:28:13]

- Inspect category meanings before counting them. Merge or delete categories as needed, and manually check model-assigned labels. The model’s label about needing more explicit instructions is later renamed to make its meaning clearer. “Maybe we need to combine two of them together or delete one or whatever.” [00:29:42]

- Use the observed failures to choose improvement work. They identify unclear instructions as a priority, then suggest changing the prompt before considering a model judge, a model that scores outputs against criteria. “But before we do that, let's iterate on the prompt” [00:30:19]

- Ten examples do not establish that discovery is finished. They are still deciding what counts as a failure, and many categories have only one or two examples. Theoretical saturation means reaching a point where further review stops revealing useful new themes; Hamel doubts they have reached it. “that's definitely a sign we didn't look at enough yet.” [00:31:11]

- Build the review tool as the need appears. Isaac first built only an open-coding box, changed the prompt after reviewing outputs, and then added category labels and navigation. “You can just build the tool that you just need today” [00:35:09]

## How to do it (concrete steps, checklists, templates)

1. Open a request and its response in the review interface. Keep the system prompt available for reference; here it is collapsed until needed. [00:00:00–00:00:34]
2. Read carefully for the intended user. Compare wording, measurements, steps, timing, and serving information with the intended experience. Record complete-sentence failure notes in the open-coding box. [00:00:53–00:03:56]
3. Continue across requests. Discuss uncertain judgments rather than assuming every plausible recipe passes. Include less detailed requests when the initial sample is too uniform. [00:04:18–00:19:46]
4. Record multiple problems for a single-turn response. For multi-turn or multi-component traces, start with the most upstream failure. [00:24:04–00:24:12]
5. Read the saved trace files and extract the open-coding notes. The demo uses ten annotated traces and asks a notebook agent to group and analyze the unstructured text. [00:24:38–00:27:22]
6. Inspect the proposed groups and their examples. Understand each category, combine or delete categories where appropriate, and count the resulting failures. Spot-check model labels; use manual labeling when necessary. [00:28:13–00:30:19]
7. Use the findings to choose a prompt improvement. They propose making recipes more explicit before building a model judge. Continue reviewing more examples because the demo sample is too small to settle the categories. [00:30:19–00:31:11]
8. Add the categories to the review UI when they become useful. Isaac saves a category in JSON, which makes it available in the next example’s dropdown. They also suggest having a model seed the JSON categories for human checking. [00:32:22–00:34:08]

The discussion mentions exploring failures that occur together, such as ambiguous language and technical jargon. It does not provide a full analysis procedure or validated evaluator prompt. [00:31:11–00:32:07]

## Tools, code and commands named

- A custom recipe-bot review interface: expandable system prompt, open-coding text box, axial-coding dropdown, previous/next/home navigation, and a dashboard. [00:00:10; 00:34:36]
- JSON trace files and, in the captions, “JSON L files”. The latter likely means JSONL, a line-based JSON format, but that spelling is a guess. [00:24:52; 00:25:35]
- “golden data set”, the dataset they ask the notebook agent to inspect. Its contents and schema are not reproduced. [00:25:56]
- “New cursor notebook agent.” Interpreting this as Cursor is a capitalization guess. [00:26:41]
- “Cloud Force on it.” This looks like a garbled model name. The exact model and version cannot be established from this capture. [00:26:50]
- “Analysis.b Y and B.” This appears to refer to a notebook filename, but its exact spelling cannot be recovered. [00:25:25]
- No complete executable commands, package versions, notebook cells, or installation instructions are captured. “LMS” and “LM” appear where the discussion seems to mean LLMs, language models; that expansion is a caption interpretation.

## Numbers and strong claims

- Video duration: 2,134 seconds, or 35:34. Location: capture metadata.
- Ten examples are reviewed for the demo. Both speakers say they would do more in real work; this is not a recommended sample size. [00:24:38; 00:30:19]
- The generated analysis reports five issues involving insufficiently explicit instructions. Treat this as a preliminary model-generated count, not a verified rate of failure. [00:28:37]
- Most failure categories have one or two examples. Isaac’s suggestion of one occurrence in fifty is a hypothetical question about rarity, not a measured frequency. [00:31:11]
- A thirty-minute request gets a baking step of twenty-five to thirty minutes, before preparation and oven preheating. They call this a failure. A separate fifteen-minute request has ten minutes of cooking plus preparation, which they judge potentially hectic rather than conclusively impossible. [00:12:56–00:13:25; 00:23:28–00:23:45]
- Product managers should be heavily involved in, or sometimes drive, evaluation. This is practitioner advice, not a measured result. [00:21:48]
- The suggestion that vegan requests trigger health information because of correlations in training data is speculation. They do not test that explanation. [00:14:35]

## Compared with the deep research report

The report does not mention this video directly. The comparison is therefore with its recipe-chatbot course description and related method advice, not a correction of a video summary. Shreya does not appear in this transcript, so it demonstrates Isaac and Hamel’s practice rather than documenting her own statements.

- **What it gets right:** Section 3.2 calls the repository a collection of “progressive exercises, worked notebooks, and linked video walkthroughs”. This source supplies a concrete example: Isaac describes adding features only after using the simpler interface, then says, “you can build stuff progressively as you go.” [00:35:09]
- **What it gets right:** Section 2.1 recommends a note explaining each failure and then grouping related failures. The demo follows that order and adds the requirement to inspect the categories: “make sure you understand all of them.” [00:29:20]
- **What it leaves out:** Product definition is part of the analysis itself. The report’s section 3.2 describes “Inspecting failures and organizing them into categories.” The walkthrough goes further: “it's not strictly about did the AI do the right thing.” [00:15:23] Decisions about audience, optional steps, defaults, and units can change what counts as failure.
- **What it leaves out:** Model-assisted grouping can introduce questionable themes, so category counts need checking. “I don't remember writing this.” [00:28:13] The demo also clarifies the single-turn versus upstream-failure rule. [00:24:12]
- **What is not established:** The report proposes “manually examine 20–30 real runs” in its diagnostic-suite section. This video supports starting with review, but supplies no endorsement of that exact range. Its ten-example demo remains unfinished: “I don't think we've hit the theoretical saturation necessarily.” [00:30:19]

No direct contradiction is established by this capture. It adds practical detail and limits to the report’s broad account of the method.

## Fit for the user's agent workspace

- (inference) Review completed worker runs with a free-text failure note before creating a fixed list of labels. Give later grouping models complete sentences.
- (inference) Define acceptable behavior for each worker role. A short answer may suit one task while omitting required evidence in another.
- (inference) For tool-using traces, identify the earliest failure that caused later mistakes. For a single final artifact, allow several independent failure notes.
- (inference) Treat model-generated categories and counts as drafts. Check their supporting runs before using them to change a role or skill.
- (inference) Build a small review screen with the packet, relevant instructions, output, and notes. Add category dropdowns after useful categories emerge.
- (inference) Use failures to revise task packets or workflow choices as well as prompts. Continue reviewing while acceptance criteria are still changing.
- (inference) This video gives no cost-evaluation method. Add cost and duration separately when assessing whether a worker was worth its expense.

## Best parts to read or watch first

- [00:01:47–00:03:56], about 2 minutes: clear open-coding examples and why complete sentences help.
- [00:13:32–00:19:46], about 6 minutes: sample variety, product decisions, and audience-specific judgments.
- [00:21:06–00:24:34], about 3.5 minutes: turning preferences into requirements and the upstream-failure rule.
- [00:27:22–00:31:11], about 4 minutes: questionable model grouping, category inspection, prompt iteration, and sample limits.
- [00:31:11–00:35:26], about 4 minutes: why more review is needed, category dropdowns, and building tools progressively.
