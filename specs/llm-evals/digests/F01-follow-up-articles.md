---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [F01a, F01b, F01c, F01d]
purpose: Four-source digest feeding the spec compendium.
---

# Follow-up articles (D-F01)

## Source: Building eval systems that improve your AI product (F01a)

**What it is:** Hamel Husain and Shreya Shankar, September 9, 2025. Written guide in [Lenny's Newsletter](https://www.lennysnewsletter.com/p/building-eval-systems-that-improve). Reading time is not stated.
**Capture status:** Partial. Public preview covers Phases 1 and 2. Phase 3 and subsequent paid material are unavailable. Examples shown only in images are not transcribed.

### The point in three sentences

Find recurring failures in real interactions before choosing metrics. Use code for clear rules and a human-validated model judge for judgments. Diagnose conversation, retrieval and agent failures at the level where they occur.

### Key ideas

- Error analysis means reviewing failures and grouping them. Generic scores can miss the actual user problem: “You cannot know what to measure until you systematically find out how your product fails in specific contexts.” (Phase 1)
- Start with one person who knows the domain and owns the quality decision. Multiple domains or cultural contexts may require multiple reviewers and agreement checks: “a single principal domain expert as the arbiter of quality.” (Phase 1)
- Open coding means writing detailed notes before imposing categories. Record pass/fail and the reason: “The domain expert reviews each user interaction and writes a free-form critique” (Phase 1).
- Axial coding means grouping those notes into recurring failure types. A model can suggest groups, but the expert validates them: “Always have the human expert review and validate the LLM’s suggestions.” (Phase 1)
- Generic metrics have a limited discovery role. Sort examples by their scores and inspect both extremes: “Reviewing the highest _and_ lowest scoring examples can reveal surprising failure modes or unexpected successes” (A warning about off-the-shelf metrics).
- Use deterministic code checks for objective requirements. Reserve a model judge for qualities such as tone: “Use them whenever a clear rule can define success or failure.” (Phase 2)
- Binary labels force a decision while prose keeps the nuance. “The nuance is not lost; it is captured in the critique” (Establish ground truth).
- Separate prompt examples, development examples and untouched test examples. Otherwise the judge may fit familiar cases and fail on new ones: “Do not use your entire dataset to build and test your judge.” (Build and validate the judge)
- Check both success recognition and failure detection. TPR is the share of true passes recognized; TNR is the share of true failures caught: “it will never catch a single failure.” (Measure what matters, about an always-pass judge)
- Evaluate the whole conversation first, then test whether a failed request also fails alone. “try to reproduce the failure in a single turn.” (Multi-turn conversations)
- Retrieval-augmented generation, or RAG, retrieves documents before writing an answer. Measure retrieval separately from answer faithfulness and relevance: “Fix your retriever first.” (Retrieval-augmented generation)
- An agent's final failure needs a step-level diagnosis. A transition failure matrix counts failures between stages: “The rows of the matrix represent the last successful step, and the columns represent the step where the failure occurred.” (Agentic workflows)

### How to do it (concrete steps, checklists, templates)

- Appoint the domain expert. Start with about 100 randomly sampled interactions.
- For each interaction, record pass/fail and a critique explaining whether the user's main need was met. Give enough context and detail for a newcomer to understand.
- After dozens of reviews, group critiques into fewer than 10 primary failure modes. Validate model-suggested groups. Count categories to prioritize work.
- For each prioritized failure, choose a code check or a model judge.
- Label interactions by session with binary decisions and detailed critiques.
- Split labels into train, dev and test sets. Put train examples in the judge prompt, refine against dev, then measure on untouched test data.
- Measure TPR and TNR together. Choose acceptable mistakes based on the product's consequences.
- For conversations, judge the session and reproduce failures in one turn. For RAG, improve retrieval before generation. For agents, map failed traces onto the transition matrix.

The captured Phase 3 contains only its heading. No continuous-operation checklist or correction formula is available.

### Tools, code and commands named

Arize Phoenix, LangSmith, Braintrust, spreadsheets and pivot tables. Code-based evaluators check valid JSON, required keywords and execution success. No executable commands or software versions are supplied. AI Evals for Engineers & PMs is the promoted course.

### Numbers and strong claims

- About 100 interactions initially; fewer than 10 primary failure modes. Heuristics, not measured guarantees. (Phase 1)
- Train 10%–20%, dev 40%–45%, test 40%–45%. Suggested split ranges. (Build and validate the judge)
- A system succeeding 99% of the time lets an always-pass judge score 99% accuracy while catching no failures. Illustrative example. (Measure what matters)
- Retrieval depth examples: 3 to 5 documents for a simple fact; 10 to 20 for synthesis. Task-dependent suggestions. (RAG)
- A 95% pass rate across 1,000 examples and a 10% failure-to-pass mislabeling chance illustrate score correction. The promised mathematical appendix is unavailable. (Measure what matters)
- More than 2,000 trained PMs/engineers, leaders at over 500 companies, highest-grossing Maven course, and 25% discount. Promotional claims in the introduction.
- “the only way” to scale subjective evaluation and build trusted systems is strong author opinion, not evidence of exclusivity. (Phase 2 and Measure what matters)

### Compared with the deep research report

The report does not discuss this written article directly. Its related Lenny podcast summary describes “examining traces” and “identifying recurring failures” (§1.1), which match this article's “open coding” and “axial coding”. That is thematic agreement, not verification of the podcast from this capture. The report correctly separates paid newsletter material from a public video. This capture shows a different limit: “This post is for paid subscribers” at Phase 3. The related summary leaves out this article's explicit split ratios, TPR/TNR definitions, single-turn diagnostic and transition matrix. No direct-source factual error can be established.

### Fit for the user's agent workspace

- (inference) Start with actual bounded worker runs and label whether each packet's objective was met.
- (inference) Preserve a short explanation with each acceptance decision so future judges inherit the rationale.
- (inference) Use code to check required files and forbidden changes. Use a validated judge for explanation quality.
- (inference) Track failures between packet reading, execution, verification and reporting to locate weak stages.
- (inference) Keep cost measurements separate from quality judgments. This preview gives no cost-effectiveness formula.

### Best parts to read or watch first

- Phase 1: review and grouping method. Allow about 5 minutes, an estimate.
- Build and validate the judge, then Measure what matters: judge validation. Allow about 4 minutes, an estimate.
- Agentic workflows: transition matrix. Allow about 2 minutes, an estimate. Phase 3 is unavailable.

## Source: ALIGN Eval Frontend (F01b)

**What it is:** [Repository README](https://github.com/eugeneyan/align-app). Author and publication date are unknown in the capture. Short enough for about 1 minute, estimated.
**Capture status:** Full README only. It does not include the linked article, application behavior, backend or implementation files.

### The point in three sentences

ALIGN Eval is a prototype frontend for building and improving model evaluators. It tests prompts against labeled data and offers semi-automatic optimization. Its binary-classification scope also applies to prompts outside evaluation.

### Key ideas

- The repository supplies a frontend, not a full workflow description: “This is the frontend code” (Introduction).
- The game framing is intended to ease evaluator development: “A prototype game” (What is ALIGN Eval?). This is a product description, not usability evidence.
- Prompt quality is checked against known labels: “Tools to evaluate your prompts against labeled data” (What is ALIGN Eval?).
- Optimization has some human involvement: “Semi-automatic optimization” (What is ALIGN Eval?). The README does not explain the algorithm.
- Alignment is iterative in both directions: “align annotators with AI output, and AI with annotator input” (What is ALIGN Eval?).
- Binary classification means assigning one of two labels. The app's stated scope includes “any prompt that does binary classification!” (What is ALIGN Eval?).

### How to do it (concrete steps, checklists, templates)

- Start the development server using one of the commands below.
- Open `http://localhost:3000`.
- Share constructive feedback or report bugs on GitHub or X.

No install command, labeling procedure, evaluation protocol or optimization checklist is provided.

### Tools, code and commands named

`npm run dev`, `yarn dev`, `pnpm dev`, `bun dev`. Next.js with TypeScript, Tailwind CSS, `next/font`, Geist, ALIGN Eval, GitHub and X. No versions are stated.

### Numbers and strong claims

- Port 3000 is the local browser destination. (Getting Started)
- “easy and fun” is promotional wording, not measured evidence. (What is ALIGN Eval?)
- Beta status is stated. No benchmark, accuracy, cost or speed result is given. (Contributing)

### Compared with the deep research report

The report's §2.4 covers the linked article, not this README. Its phrase “aligning automated evaluation with those labels” agrees with the README's “evaluate your prompts against labeled data”. Its “approximately 14 minutes” applies to the article, not this capture. The README cannot confirm the report's visual walkthrough or detailed implementation discussion. The report's frontend fit is supported by “Next.js with TypeScript”; it omits the README's broader binary-classification scope and beta status. No direct contradiction is established.

### Fit for the user's agent workspace

- (inference) Borrow the labeled-example review interface idea for worker acceptance decisions.
- (inference) The named TypeScript stack is familiar enough to inspect later if a spreadsheet becomes awkward.
- (inference) Treat optimization claims as a reason to inspect the implementation, not proof that the resulting judge is valid.

### Best parts to read or watch first

- What is ALIGN Eval?: scope and limits, under 1 minute estimated.
- Getting Started and Tech Stack: commands and framework, under 1 minute estimated. The linked article is outside this capture.

## Source: Tracing (F01c)

**What it is:** [Promptfoo documentation](https://www.promptfoo.dev/docs/tracing/), captured from `site/docs/tracing.md`. Author and publication date are unknown. Long technical reference; reading time is not stated.
**Capture status:** Full document, including examples and original frontmatter. Linked provider guides and example repositories are not included.

### The point in three sentences

Tracing records the operations behind each answer. OpenTelemetry is the shared telemetry format; a span records one operation inside a trace. Promptfoo uses traces for workflow assertions, grading, debugging and adversarial testing.

### Key ideas

- Traces make intermediate behavior testable: “Check which tools ran, in what order, and with which inputs” (Overview).
- Each execution gets its own trace, with target and grading children: “Multi-turn tests keep their target requests and grading together in the same trace.” (Built-in Provider Instrumentation)
- Propagating `traceparent`, the W3C trace context, joins application work to the correct test: “Use this to create child spans” (Instrument Your Provider).
- Trajectory assertions check the path an agent took. Tool presence, arguments, sequence and goal success are illustrated: “you can evaluate what the agent actually did” (Assert on Traced Workflows).
- Raw-span assertions check counts, durations and errors. Exact attribute filters narrow checks: “All supplied attributes must match; missing attributes are excluded.” (Assert on Traced Workflows)
- Few turns do not prove tool batching. Check shared generation indices where exposed: “a low total turn count alone does **not** prove the tools were batched.” (Turn marker spans)
- Codex turn boundaries have a specific limit: “they cannot distinguish batched from sequential tool calls within that turn” (Turn marker spans).
- Subagent activity and cache hits complicate turn counts: “Subagents emit their own turns.” and “Cache hits emit no turn span.” (Caveats)
- Existing telemetry can be reused: “pull them from a tracing service you already use.” (Overview). Tempo, Braintrust and Langfuse have separate lookup requirements.
- Display redaction is different from storage redaction: “These settings do not change locally stored spans.” (Span Details Panel)
- Receiver redaction does not cover built-in provider spans: “are **not** filtered by `redactAttributes`” (Scope of redactAttributes).
- Adversarial tests can use internal evidence to improve attacks: “Traces are formatted and fed back to the attack strategy” (Red Team Tracing).

### How to do it (concrete steps, checklists, templates)

- Enable `tracing.enabled: true` and `otlp.http: {}` in `promptfooconfig.yaml`.
- Initialize the OpenTelemetry provider and exporter. The JavaScript example uses SDK 2.x constructor configuration with `spanProcessors`.
- Extract `traceparent`, create child spans, add attributes, record exceptions and error status, and end spans. Preserve a fallback when tracing is disabled.
- Run `promptfoo eval`, then `promptfoo view`. Open a result's magnifying glass and find Trace Timeline.
- Add assertions for tool use, arguments, sequence and goal success. Use raw-span checks for timing, counts and errors.
- Apply descriptive names and useful attributes. Use `SimpleSpanProcessor` in development and testing; `BatchSpanProcessor` in production.
- If traces are absent, check enablement, endpoint, trace context and provider logs, in that order.
- For red-team feedback, enable tracing under both `tracing` and `redteam.tracing`. Select attack/grading inclusion and optional span filters. Strategy-specific settings may override shared choices.

Minimal starter configuration from the source:

```yaml
tracing:
  enabled: true
  otlp:
    http: {}
```

### Tools, code and commands named

- Commands: `promptfoo eval`, `promptfoo view`, `DEBUG=promptfoo:* promptfoo eval`, `OTEL_LOG_LEVEL=debug promptfoo eval`, `--no-cache`.
- Assertions: `trajectory:tool-used`, `trajectory:tool-args-match`, `trajectory:tool-sequence`, `trajectory:goal-success`, `trace-span-count`, `trace-span-duration`, `trace-error-spans`, `javascript`, `is-refusal`.
- JavaScript packages: `@opentelemetry/api`, `@opentelemetry/sdk-trace-node`, `@opentelemetry/exporter-trace-otlp-http`, `@opentelemetry/resources`. Python package: `opentelemetry-exporter-otlp-proto-http`.
- Interfaces: `callApi`, `call_api`, `NodeTracerProvider`, `SimpleSpanProcessor`, `BatchSpanProcessor`, `TraceIdRatioBasedSampler`, `SpanStatusCode`, `resourceFromAttributes`.
- Environment settings: `PROMPTFOO_TRACING_ENABLED`, `PROMPTFOO_ENABLE_OTEL`, `OTEL_EXPORTER_OTLP_ENDPOINT`, `OTEL_SERVICE_NAME`, `OTEL_EXPORTER_OTLP_HEADERS`, `PROMPTFOO_STRIP_*`.
- Backends and frameworks: Jaeger, Grafana Tempo, Honeycomb, Braintrust, Langfuse, Vercel AI SDK, OpenAI Agents SDK, Google ADK. Langfuse Python SDK 4.7.0+, JavaScript SDK 5.4.0+, and ingestion header `x-langfuse-ingestion-version: 4` are specified.
- Automatic provider table: OpenAI, Anthropic, Azure OpenAI, AWS Bedrock, Google Vertex AI, Ollama, Mistral, Cohere, Huggingface, IBM Watsonx, HTTP, OpenRouter, Replicate, OpenAI-compatible and Cloudflare AI.
- Provider IDs include `anthropic:claude-agent-sdk`, `azure:foundry-agent`, `openai:agents`, `openai-agents`, `openai:codex-sdk`, `openai:codex-app-server`. Examples name `gpt-6-luna`, `gpt-4`, `claude-3`, `llama-3`, `gpt-4.1-mini`; these are source examples, not recommendations.
- Trace APIs: `GET /api/traces/:traceId`, `GET /api/traces/evaluation/:evaluationId`.

### Numbers and strong claims

- Default receiver: `127.0.0.1:4318`, accepting JSON and protobuf. SQLite is the only supported store. (Basic Configuration)
- Request/response attributes are truncated to 4KB. (GenAI Span Attributes)
- Default retention is 30 days only when a storage block exists. Omit it for indefinite retention; zero or less disables pruning. Pruning runs at the start of traced evals. (Basic Configuration)
- Sampling example retains 10%; Tempo example waits 3000ms and sets a 10000ms timeout. Examples, not universal settings. (Trace Sampling; Grafana Tempo)
- Older Langfuse ingestion may delay visibility by up to ten minutes. (Langfuse)
- Approximately 1–2ms overhead per span is a documentation claim with no benchmark method here. (Performance Impact)
- A tool-using task normally takes at least two internal model rounds. Codex protocol turns do not expose those rounds. (Turn marker spans)

### Compared with the deep research report

The report's §3.1 discusses Promptfoo generally, not this tracing page. “test cases, assertions” and “a local results viewer” are supported here by “Trace-aware assertions” and “Web UI visualization”. Its coding-agent integration claims have partial support in this page's provider rows, but OpenCode integration is not established by this capture. The report omits generation-versus-protocol turn distinctions, cache and subagent caveats, trace-backed assertions, external trace lookup and storage redaction limits. Its starter commands are outside this page's exact command examples; that is not a contradiction.

### Fit for the user's agent workspace

- (inference) Test both packet completion and tool behavior, including arguments and required ordering.
- (inference) Save trace/result IDs with worker evidence so a failure can be investigated later.
- (inference) Combine model identity, token usage and timing with quality results when comparing worker value. This page provides no price conversion formula.
- (inference) Avoid using Codex turn counts as evidence that a worker batched independent calls.
- (inference) Keep credential-bearing telemetry outside coworker-visible memory. Display masking alone does not establish safe storage.

### Best parts to read or watch first

- Quick Start and Assert on Traced Workflows: about 5 minutes estimated.
- Turn marker spans and Caveats: about 4 minutes estimated.
- Basic Configuration and Scope of redactAttributes: about 5 minutes estimated. Read before retaining real traces.

## Source: The Revenge of the Data Scientist (F01d)

**What it is:** Hamel Husain, March 26, 2026. [Annotated PyAI Conf presentation](https://hamel.dev/blog/posts/revenge/), with linked video and slides. Reading and video durations are not stated.
**Capture status:** Full article, including footnotes and Video & Slides. Embedded media are linked, not transcribed; slide images are not text captures.

### The point in three sentences

Calling a model API does not remove the need for sound measurement. Many evaluation mistakes repeat old mistakes in data collection, experiments and classifier testing. Humans must inspect outputs to discover what quality means for their product.

### Key ideas

- The harness includes measurement as well as tests and specifications: “a large portion of the harness is data science.” (The Harness Is Data Science). This is the author's thesis.
- Generic scores do not locate product failures: “you have no idea what is actually broken.” (Generic Metrics)
- Reduce friction in trace review, then record and prioritize failure types: “Code your own custom trace viewer” (Generic Metrics).
- A model judge is a classifier, a system predicting labels, and needs validation: “Get human labels, partition the data into train/dev/test” (Unverified Judges).
- Build examples from train, improve the prompt on dev and preserve test: “Keep a test set aside to confirm you haven’t overfit.” (Unverified Judges)
- Accuracy can conceal rare failures. Precision means how often flagged failures are real; recall means how many real failures are caught: “Use precision and recall.” (Unverified Judges)
- Synthetic examples should vary dimensions discovered in real logs: “Base the synthetic data off real data.” (Bad Experimental Design)
- Narrow binary checks support decisions better than vague scales: “Replace subjective scales with binary pass/fail on scoped criteria.” (Bad Experimental Design)
- Domain experts should label, while reviewers remain skeptical of label quality: “Data scientists don’t trust the data.” (Bad Data and Labels)
- Criteria drift means that reviewing outputs changes the standards used to assess them: “grading outputs helps users define their criteria.” (Bad Data and Labels)
- Models can implement plumbing, but the human must learn from outputs: “They cannot look at the data for you” (Automating Too Much). This concerns discovering human preferences, not a ban on model-assisted analysis.
- Additional pitfalls include vague questions, raw-JSON review interfaces and uncertainty-free scores: “Reporting uncalibrated scores without confidence intervals.” (Other Pitfalls)

### How to do it (concrete steps, checklists, templates)

The article orders its advice by pitfall, not as a complete implementation recipe:

- Inspect traces with a custom viewer. Note failures, categorize them and prioritize application-specific metrics.
- Collect human labels; split train/dev/test. Use train examples in prompts, refine on dev, confirm on test, and report precision/recall.
- Inspect production data before creating synthetic tests. Identify dimensions, vary them and inject edge cases.
- Reduce metric complexity. Make each criterion actionable and connected to a business outcome.
- Have domain experts label and inspect raw outputs, using that work to discover requirements.
- Use models for plumbing and evaluation boilerplate while preserving human review.

The final mapping connects these activities to data exploration, model evaluation, experimental design, data collection and production monitoring. No statistical formulas or runnable pipeline are supplied.

### Tools, code and commands named

Python, ROUGE, BLEU, Codex, OpenAI's harness engineering article, Andrej Karpathy's `auto-research` project, and the `evals-skills` plugin at `ai-evals-course/evals-skills`. RAG and LLM-as-judge are discussed. YouTube video and Google Slides are linked. No commands or software versions are given.

### Numbers and strong claims

- A failure occurring 5% of the time illustrates why accuracy can hide poor detection. (Unverified Judges)
- “Give me 50 test queries” is an example of weak synthetic-data prompting. (Bad Experimental Design)
- Five main pitfalls are covered, followed by a shorter list. (The Harness Is Data Science; Other Pitfalls)
- Looking at data is called the highest-return activity; Python is called the best toolset. Author opinions, not comparative measurements. (Generic Metrics; The Mapping)
- The page banner promotes 5,000+ engineers/PMs and 25% off. Marketing, not evidence about the evaluation method.

### Compared with the deep research report

No section discusses this article directly. The report's related judge guide (§2.3) asks how to know the evaluator is “itself evaluating correctly”; this article asks “how do you trust the judge?” The shared lesson is supported, but this capture cannot verify the separate judge guide. The article adds the five-pitfall framing, production-grounded synthetic data, skeptical label review and the mapping to established data-science practice. There is no direct summary here to identify as wrong or overstated.

### Fit for the user's agent workspace

- (inference) Treat each worker comparison as an experiment with representative packets and explicit acceptance criteria.
- (inference) Inspect traces before inventing an overall worker score.
- (inference) Label outputs personally when the criterion depends on the user's own expectations.
- (inference) Use synthetic packets to vary failure dimensions found in actual runs, rather than asking for generic tasks.
- (inference) Let cheap workers build review plumbing while the root keeps responsibility for quality decisions.

### Best parts to read or watch first

- Generic Metrics and Unverified Judges: about 3 minutes estimated.
- Bad Experimental Design and Bad Data and Labels: about 3 minutes estimated.
- The Mapping: about 1 minute estimated. Video & Slides links are available, but media duration and contents are not captured.
