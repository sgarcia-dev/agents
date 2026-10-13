---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [E16f]
purpose: One-source digest feeding the spec compendium.
---

# How to Automate AI Evals (Correctly) (E16f)

**What it is:** Shreya Shankar presents a live error-discovery demo, introduced by Hamel Husain on his channel. Published 2026-07-03. Video, 27 minutes 19 seconds. [Watch](https://youtu.be/tqUDjc1HzO4).
**Capture status:** Full transcript. Frontmatter says manual captions, joined without word changes, despite several garbled terms. No missing transcript portion is declared. The capture does not reproduce slides, interface screenshots, skill code, exact shell commands, or the skill's source link. Several paragraphs span minutes: references below use their recorded starting timestamp, not an invented sentence-level time.

## The point in three sentences

Human review discovers what good output means for a particular product. AI can build the review interface, organize that feedback, and find more examples of failures the human has identified. Keep revisiting the data, save what you learn, and choose evaluation effort based on the consequences of failure.

## Key ideas

- Evaluation measures application quality, not just model capability. A trace is a record of an agent's behavior; a failure mode is a recurring kind of mistake. “systematic ways to measure the quality of your application.” [00:00:56]
- Product judgment cannot be recovered from logs alone. The agent needs the preferences and requirements that the developer has not yet stated. “What good means for your product is living in your head.” [00:01:01]
- The course teaches a repeating cycle: analyze failures, measure how common they are, then improve the product. AI is less suited to discovering unstated preferences than to applying known criteria or helping improve prompts. “error analysis, measure, and then improve.” [00:01:01]
- An open-ended request to evaluate all logs can miss subjective failures, invent priorities, and repeat work on every batch. Save failure definitions in memory or code so later runs reuse them. “persist intermediates of the life cycle.” [00:05:10]
- Ask AI to help with specific parts of the workflow. Its review interface should make differences in the data visible, such as coloring messages by assistant, system, or user role. “design a visual encoding.” [00:05:10]
- The review app has three views: one output at a time, a map of the dataset, and progress across discovered failures. A taxonomy is the organized set of failure categories built from human notes. “a trace viewer, so one-by-one trace viewer.” [00:05:10]
- Sampling reduces review fatigue, but the AI's choice of features and groups can be wrong. Clustering means grouping similar records; embeddings are numerical representations of content, and need not be the right representation for every task. “you can't assume that the clustering or that the sample selection is perfect.” [00:10:05]
- Collect feedback beside the relevant text, while the preference is fresh. The live reviewer flags colons, sentence fragments, and contrastive phrasing, rather than filling in a predefined scoring rubric. “I highlight the text” [00:15:08]
- The agent should react to annotations during review, not merely generate an app and disappear. In the demo it fails to monitor feedback until Shreya prompts it again. “It's supposed to use the monitor tool.” [00:16:51]
- Human notes can reveal requirements missing from the original prompt. Organizing those notes is work the AI can handle. “I thought the AI should simply know.” [00:18:25]
- Seek breadth across different failures and depth through several examples of each. Repeated exposure can reveal patterns that were invisible on the first pass. “trying to optimize for both breadth and depth” [00:18:38]
- Apply each new failure definition to records already reviewed as well as new records. The human accepts or rejects suggestions; the agent is not asked to invent new categories in this workflow. “It's not changing the taxonomy.” [00:20:51]
- Set the accuracy requirement for the application context. Use an assistant to explore worst cases, such as broken citations or leaked private information, then decide what checks and runtime protections are needed. “reason about worst-case scenarios up front.” [00:20:51]

## How to do it (concrete steps, checklists, templates)

The skill's described sequence is:

1. Load a sample and understand the fields, structure, and repeated content. [00:05:10]
2. Choose visual representations that help the reviewer see meaningful differences. Role colors are one example. [00:05:10]
3. Build a review app with a single-record viewer, dataset map, and progress view. The progress view includes a tree map of failures, a display of grouped categories. [00:05:10], [00:10:05]
4. Group records and choose representative samples from each group. Treat the chosen features and sample coverage as fallible. [00:10:05]
5. Have the human review those samples and give open-ended annotations. Keep the agent monitoring feedback and organizing a failure taxonomy. Cover different failure types and gather several examples per type. [00:10:05]

During and after review:

- Highlight the relevant passage and record the concern beside it. Save annotations to a file. [00:15:08], [00:16:51]
- Check that monitoring actually works. In this demo, Shreya asks why the agent is not using the instructed monitor tool. [00:16:51]
- Revisit previously reviewed records when a new pattern becomes clear. Repeated use of “matters” is the example. [00:19:59], [00:20:33]
- Ask the agent to find instances of human-defined failures in reviewed and unreviewed records. Accept or reject its suggestions. It may miss instances. [00:20:51]
- Repeat both loops: across the dataset, and across possible failures within a record. Preserve the definitions rather than rediscovering them on every run. [00:20:51], [00:05:10]
- Use measured prevalence to prioritize improvements. Options named are adding prompt instructions, switching models, and fine-tuning. Implementation details for measurement and improvement are outside this talk. [00:04:57], [00:05:10]
- Separately, supply traces, an application description, or code to an assistant and reason through worst-case user outcomes. Work backward to evaluation and guardrail needs. [00:20:51], [00:26:14]

## Tools, code and commands named

- Claude Code, Codex, and Claude. No model identifiers or versions are given. [00:05:10], [00:20:51]
- LangChain, Braintrust, and Arize, mentioned as automated-evaluation vendors. Their capabilities are described broadly, not tested individually here. [00:01:01]
- Error Discovery skill, named in the video description. The transcript calls it an error analysis skill and says it is open source and changing frequently. No install command or source URL is captured. [00:10:05], [00:26:14]
- JSON input, an S3 bucket, shell commands, a server, and an HTML app. No exact executable commands are included. [00:05:10], [00:10:05]
- K-means, embeddings, t-SNE, UMAP, and PCA. K-means on embeddings was an earlier skill design, not a required method. The comparison around PCA is garbled, so the capture does not establish a recommended projection method. [00:10:05], [00:15:08]
- “monitor tool”, with no API or implementation details. [00:16:51]
- Caption cautions: “LangChain Smith” and “Grass site” are uncertain names. “emails”, “approve”, and “scale” appear to mean evals, improve, and skill in context; these are guesses. “Amel” and “Himel” likely refer to Hamel, based on the introduction. “Antariksha Dasgupta” is captured as a research collaborator but is not independently confirmed. [00:01:01], [00:05:10], [00:20:51], [00:25:34], [00:26:14]

## Numbers and strong claims

- First installment of a 12-part AI product engineering series. [00:00:00]
- Demo dataset: 33 AI-generated blog articles, with 21 selected for review and six clusters shown. These are demo counts, not recommended sample sizes. [00:10:05], [00:15:08]
- Generated interface took about five minutes; the displayed duration is described as 4 minutes 42 seconds. A single live-demo observation. [00:14:13]
- “80% of issues in the data are often caused by 20% of failure modes.” A practitioner heuristic, not a demonstrated statistical result here. [00:01:01]
- Output quality is called the biggest barrier to productionizing agents, attributed to an annual report; more than half of internet articles are said to sound AI-generated. Both are unverified secondhand claims with uncertain source names in the captions. [00:01:01]
- General coding agents are said to be more exhaustive at finding failures than some dedicated platforms. This is preliminary work with no results table, dataset details, or benchmark method in the capture. The broad claim that vendor tools are mainly prompts is opinion. [00:20:51], [00:25:34]
- Internal summaries are presented as tolerating lower accuracy than customer-facing applications. This is contextual advice, not a universal rule for internal systems. [00:20:51]

## Compared with the deep research report

The report does not mention this video directly. Its relevant sections are 2.1 on the field guide, 3.2 on Recipe Chatbot, and 3.3 on evals-skills.

- **What it gets right:** The report says the discovery workflow builds an interface “while you supply the judgments and explanatory notes.” The video makes that division visible: “It's much easier for me to say what I think” and have the agent apply it across traces. [00:20:51]
- **What the video adds:** The report describes “inspecting real data, identifying failure patterns, building useful review interfaces”. The demo specifies the three views, inline annotations, saved feedback, live monitoring, and rechecking earlier records. Its key addition is “Loop over them to surface new failure modes.” [00:25:34]
- **What needs qualification:** The report names `error-discovery` as a useful starting point. The video shows that the skill and generated UI need supervision: “You do need to coax and cajole as we go on.” [00:16:51] It also shows why the agent's sampling and suggestions cannot be treated as exhaustive.
- **Recipe-chatbot relationship:** The report highlights `homeworks/hw2/` for “Inspecting failures and organizing them into categories.” This video adds a live illustration of that kind of method, but on writing outputs: “these are just the actual essays that are finally generated by the LLM.” [00:10:05] It does not demonstrate Recipe Chatbot or verify any of its assignment contents.
- **No direct contradiction established:** The supplied video supports the report's human-led approach. It does not cover judge-prompt validation, evaluator runners, repository maintenance, or the report's course-access claims, so it cannot confirm or refute those details.

## Fit for the user's agent workspace

- (inference) Review real worker outputs before designing a large checklist. Capture unstated preferences as concrete notes on examples.
- (inference) Keep failure definitions and example references in durable files so cheap workers can reuse them across batches.
- (inference) Use a small review interface to show the worker output and relevant context together, with inline notes and visible review progress.
- (inference) Let workers find more instances of defined failures. Keep the root or human responsible for adding categories and deciding priorities.
- (inference) Recheck earlier runs whenever a new scope or quality failure becomes clear. A completed first review does not settle every criterion.
- (inference) Match review effort to consequences. Use worst-case analysis for workers with wider authority, rather than giving every task the same quality bar.
- (inference) Do not infer cost effectiveness from this demo. It reports interface build time, but no token costs, worker-model comparison, or cost-per-correct-result measure.

## Best parts to read or watch first

- [00:08:11] to [00:11:12], about 3 minutes: skill workflow and review interface design. These are chapter boundaries; the transcript groups much of this explanation under [00:05:10].
- [00:15:10] to [00:19:31], about 4 minutes 21 seconds: live annotations, the monitoring failure, and the evolving taxonomy.
- [00:19:31] to [00:22:53], about 3 minutes 22 seconds: revisiting records and applying human-defined failures across examples.
- [00:25:48] to the end, about 1 minute 31 seconds: three rules and the continuing role of human judgment.
