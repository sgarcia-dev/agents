---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [E16a]
purpose: One-source digest feeding the spec compendium.
---

# Isaac HW 1 & 2 (Session 1) (E16a)

**What it is:** A live homework walkthrough led by Isaac, with Hamel answering questions. Published on Hamel Husain's channel on 2025-07-03. Video, 3,892 seconds, or 1:04:52. [Watch](https://youtu.be/h9oAAAYnGx4).
**Capture status:** Full auto-generated captions. Fragments were joined without word changes. No chapters were supplied. The capture contains spoken discussion, not the displayed code, chat messages, or the separate open-coding demonstration mentioned during the session. Names and tool spellings can be garbled. Isaac's surname is not supplied.

## The point in three sentences

Start with a reasonable prompt for a specific audience, then use actual responses to discover what needs changing. Create varied but realistic test queries, record runs, write notes on failures, and group those notes into useful categories. Keep the tools simple, inspect AI-generated data and analysis yourself, and study complete agent runs before reducing failures to smaller tests.

## Key ideas

- Define quality for an audience you understand. Beginner cooks need explicit measurements, serving sizes, times, and temperatures; professional chefs may need something else. “who's the audience?” [00:01:07]
- A prompt is a starting hypothesis, not a finished specification. Reviewing failures can reveal that your desired behavior was wrong, such as forbidding follow-up questions when a request has conflicting constraints. “The answer comes afterwards when you start to do the error analysis”. [00:04:13]
- Prompt management does not require a separate service. Editing a string in code, trying it in a notebook, or exposing an administrative view are all options. “just replace the prompt in the code”. [00:09:11]
- Add complexity only when observed problems justify it. Splitting content generation and styling into two prompts is one possible experiment, not the recommended default. “I would start simple” [00:13:46]
- Examples should explain something that instructions alone cannot easily express. The initial handful of queries is a warm-up, not a required stage or sample size. “You shouldn't just add samples examples for the sake of it”. [00:18:16]
- Synthetic data means generated examples rather than collected user requests. Choose dimensions, the aspects of a request that may affect the answer, then generate combinations. “I wanted to test it with a diverse set of user scenarios”. [00:23:24]
- Review every generated combination before expanding it into queries. A tuple, a bundle with one value from each dimension, can be implausible or expose a product decision. “just because it generated a tupole doesn't mean it makes sense”. [00:24:14]
- Realistic requests can still contain contradictions. Decide whether to keep such cases, ask for clarification, or substitute something; revisit exclusions if real users later ask those questions. “what should the product do here?” [00:25:01]
- Generated queries need realistic language as well as varied content. Add typos, informal grammar, incomplete sentences, urgency, and varied styles; users may omit dimensions entirely. “is every user really going to specify every single one of these categories reliably? Probably not”. [00:27:35]
- Logging actual product use can expose failures that backend calls miss. Isaac chooses automatic trace capture so he can keep using the interface, including checking whether Markdown renders. A trace is the recorded sequence of a run. “I wanted to be an actual user of my product”. [00:32:22]
- Open coding means writing free-text observations on responses. Axial coding means grouping those observations into failure categories. AI can help group and analyze notes, but its category names still need inspection. “does this category even make sense” [00:39:44]
- Annotation software should make inspection easier. Use a spreadsheet if it is readable; build a small interface when it helps, and try a round before adding highlighting. “do the simplest thing for you” [00:33:57]
- Use AI to create time for careful review. Isaac uses Cursor for a well-defined analysis notebook but does more of the scenario selection manually. “So I have more time to look at the details, not so I don't have to”. [00:41:16]
- An LLM-as-a-judge, a model used to score another model's work, should not depend on reviewer comments that will disappear in production. Comments can improve its prompt, but feeding them into test-time scoring changes what you are testing. “It's like a judge with a helper” [00:55:52]
- For agents, inspect full traces and record the first failure. Only simplify to a single-step test after confirming that it reproduces the observed failure. “stop at the first failure and take note of that and move on”. [00:57:35]

## How to do it (concrete steps, checklists, templates)

1. **Homework one: choose the audience and write a starting system prompt.** The walkthrough locates it in “backend utils.py”. Specify useful behavior for that audience. Think through the requirements yourself, even if AI helps write them. [00:00:35]–[00:05:47]
2. **Write and run a few plausible user queries.** Think about both what users ask and how they phrase it. Check data handling: the demonstrated CSV, a comma-separated table, accidentally splits a query containing commas into extra columns. Quote the query field as discussed. [00:15:06]–[00:17:44]
3. **Homework two: define dimensions.** Isaac uses dietary preferences or restrictions, purpose or occasion, available time, ingredient base, and meal time. He asks a model for 50 unique combinations, each containing a value from every dimension. [00:20:27]–[00:24:06]
4. **Inspect and edit the combinations.** Comment out scenarios you judge unrealistic. Keep plausible conflicts when you want to test how the product handles them. Isaac excludes some breakfast and timing combinations based on his own judgment; these exclusions are not universal rules. [00:24:14]–[00:26:34]
5. **Turn selected combinations into realistic queries.** Start with a simple generation prompt, inspect the wording, then ask for varied style, sentence structure, typos, informal grammar, context, and urgency. Put the queries in a list. [00:26:58]–[00:28:20]
6. **Run the bot and save the responses.** Isaac chooses automatic logging of interface use rather than programmatic backend calls. His simple implementation creates an annotation traces directory and saves timestamp-named JSON files. The spoken walkthrough does not provide a complete runnable implementation. [00:31:18]–[00:35:59]
7. **Read each response and write open-code notes.** His annotation interface shows the question and response, with progress marks. Revisit the system prompt when you need to distinguish a missed instruction from a requirement you have not settled. [00:36:24]–[00:38:08]
8. **Group the notes into categories and inspect patterns.** Assign specific failure modes, possibly more than one per response. Check AI-generated groupings against the examples, then explore category counts and combinations to decide what to improve. [00:39:05]–[00:41:16]
9. **Repeat the cycle.** Refine or version datasets over time. Major product changes can invalidate old examples and require a new dataset. [00:51:08]–[00:52:48]

Later questions add three adaptations:

- For a document-answering chatbot with no clear query dimensions, gather PDFs and ask a model for plausible questions about their contents. This is a proposed bootstrap method, not a demonstrated implementation. [00:43:55]
- For multi-step agents, log the entire run, inspect the first failure, and then build a smaller reproduction if it preserves the error. Include poorly specified requests and clarification behavior when they matter to the product. [00:56:58]–[01:01:06]
- If you lack examples of a particular failure, annotate more. Search or filter for relevant topics rather than always sampling randomly. Continue if the extra review changes your understanding or improves the judge. [01:02:28]–[01:03:07]

## Tools, code and commands named

Spellings below follow the capture. Corrections marked as guesses are not verified against code or video frames.

- “backend utils.py”, “system prompt field”, “homeworks”, and “homework two solution walkthrough”. The capture does not establish a precise backend file path. [00:00:00], [00:00:35], [00:21:56]
- Python, Jupyter notebook, GitHub, VS Code, “cursor”/Cursor, and “command K” to convert pasted combinations into valid Python tuples. [00:08:21]–[00:08:33], [00:22:01], [00:30:31]
- `datetime.now`, JSON files, an “annotation traces directory”, and “trace underscore” plus a timestamp. No exact directory spelling, timestamp format, shell command, or complete logging function is captured. [00:33:08]–[00:33:57]
- CSV, Excel, Google Docs; Markdown, HTML, JSON, and XML bracket tags. [00:11:02]–[00:11:53], [00:16:05], [00:38:08]
- “fast HTML”, “Monster UI”, Streamlit, Gradio, Shiny, and “R shiny”. FastHTML is a likely intended spelling, a caption-normalization guess. [00:36:24]–[00:37:05], [00:48:25]
- “Phoenix”, then later “Fenix” and “Brain Trust”, for trace inspection. The later spellings may mean Phoenix and Braintrust, guesses. [00:33:57], [00:57:35]
- “fast API”, “Nex.js”, React, “Ginga templates”, and “replet”. Possible intended spellings are FastAPI, Next.js, Jinja templates, and Replit, all guesses. These are framework choices discussed, not dependencies required by the homework. [00:46:39], [00:47:50]–[00:48:25]
- OpenAI and Anthropic prompting guides; an unnamed prompting book attributed to “John Barryman”. The author spelling is uncertain and the title is not captured. [00:07:22], [00:11:02]
- “Isaac solutions branch”, main branch, Maven studio portal, and Discord. No exact solution branch identifier or software versions are given. [00:36:09], [00:43:12]–[00:43:37]

## Numbers and strong claims

- **About 10 starting queries:** a suggested warm-up, explicitly not a required number. [00:18:45]–[00:18:54]
- **50 unique combinations:** Isaac's generation request, not a general batch-size recommendation. Larger outputs can become repetitive and require multiple calls. [00:23:46], [00:28:23]
- **About 135 lines of code:** the annotation app's stated size, not a verified code count. [00:36:24]
- **Timestamp uniqueness down to the millisecond:** accepted for Isaac's small application because it does not do concurrency. Not presented as a safe identifier scheme for larger systems. [00:33:32]–[00:33:51]
- **10 hallucination failures from about 100 reviewed cases:** a participant's hypothetical question, not a measured result or a prescribed judge dataset size. [01:01:42]–[01:02:16]
- **Review 10, 15, or 20% more:** Isaac's practical stopping heuristic, not a statistical guarantee. Stop when more review adds no useful information or improvement. [01:03:07]
- **“Beans aren't keto”:** the speakers' simplified example of conflicting constraints. Later discussion acknowledges variation in carbohydrate amounts and bean types. Treat it as their product example, not nutritional guidance. [00:24:24], [00:44:54]
- **A generated annotation app would be acceptable and might look better:** Isaac's opinion about “replet”, not a demonstrated comparison. [00:48:25]

## Compared with the deep research report

The report's Recipe Chatbot section does not discuss this video directly. This comparison concerns what the walkthrough adds to that section, rather than checking a claimed summary of the video.

- **Supported:** The report describes “progressive exercises, worked notebooks, and linked video walkthroughs”. This capture shows a starting prompt and queries in homework one, followed by synthetic query generation, logging, annotation, and category analysis in homework two. Isaac says, “I did this in a Jupyter notebook”. [00:22:01]
- **Supported but incomplete:** The report calls homework two “Inspecting failures and organizing them into categories”. The walkthrough supplies the preparation that makes that possible: audience selection, reviewed combinations, realistic wording, and usable logging. “Please look at everything on this stage” is Hamel's warning before generated combinations become more data. [00:28:23]
- **Useful qualification:** The report prioritizes homework five for “Investigating agent traces and failure patterns”. This earlier session already explains complete-trace review and first-failure annotation. “You should try to simulate an actual trace and only simplify after you observe an error” [00:58:34]. The report's ordering remains reasonable, but readers need not wait for homework five to encounter that principle.
- **Important additions:** The video explains why reviewer comments should not become hidden help for an automated judge, why AI-generated categories need human interpretation, and why tools should earn their complexity. It illustrates the method associated with Hamel and Shreya through concrete decisions by Isaac and Hamel. Shreya is mentioned in a participant's question, but this capture does not establish her as a speaker.
- **No demonstrated factual error:** This transcript does not verify the report's claims about later assignment contents, repository access, or course pricing. It also does not demonstrate cost accounting or a complete automated judge implementation.

## Fit for the user's agent workspace

- (inference) Start with acceptable behavior for one worker role you can judge yourself. Let inspected runs expose gaps in the packet or role instructions.
- (inference) Adapt the scenario dimensions to your own packets and permitted actions. Review combinations before asking a cheap model to expand them into task examples.
- (inference) Save full worker runs and find the first failure. A bad final artifact may follow an earlier missed instruction or tool error.
- (inference) Use a small Markdown or JSON review process first. Build a TypeScript annotation interface when reading and comparing runs becomes cumbersome.
- (inference) Keep human notes for developing criteria, but test an automated judge with the information it will actually receive on new worker runs.
- (inference) Delegate well-defined analysis or formatting so you have more time to inspect examples. Check category labels and their meaning yourself.
- (inference) Add cost and latency fields separately if evaluating value for money. This video gives no method for measuring whether a worker was worth its cost.

## Best parts to read or watch first

- **[00:20:27]–[00:30:25], about 10 minutes:** dimensions, generated combinations, realism checks, and conversion to natural user queries.
- **[00:31:18]–[00:41:16], about 10 minutes:** simple trace capture, annotation interface, and human inspection of AI-generated categories.
- **[00:53:08]–[00:56:23], about 3 minutes:** why comments can make judge testing unlike production use.
- **[00:56:28]–[01:01:41], about 5 minutes:** full agent traces, first failures, smaller reproductions, and clarification cases.
- **[01:01:42]–[01:04:20], about 3 minutes:** finding more failure examples and deciding when more annotation stops helping.
