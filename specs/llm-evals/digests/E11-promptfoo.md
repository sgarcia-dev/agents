---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [E11a, E11b, E11c]
purpose: One-source digest feeding the spec compendium.
---

# Promptfoo: getting started, coding agents and custom JavaScript providers (E11)

**What it is:** Three Promptfoo documentation pages. Author and publication date are unknown in all captures. Captured on 2026-10-13 as GitHub Markdown, with code examples and MDX, the site's Markdown extension. Links: [Getting started](https://www.promptfoo.dev/docs/getting-started/), [Evaluate Coding Agents](https://www.promptfoo.dev/docs/guides/evaluate-coding-agents/), [Javascript Provider](https://www.promptfoo.dev/docs/providers/custom-api/). No source reading time is given. Allow roughly 35 to 50 minutes to read all three with their code examples; this is a digest estimate.

**Capture status:** All three frontmatter records say full. Each contains the verbatim GitHub Markdown source, including original frontmatter and MDX. Capture notes report live-page length and final-section checks. Nothing is marked missing. Images are references to site assets, not embedded screenshots; linked provider and tracing documentation is outside this packet.

## The point in three sentences

Promptfoo runs combinations of prompts, providers and test cases, then checks outputs with assertions, meaning rules that decide whether a result passes. Coding-agent evaluations also need evidence about commands, permissions and changed files because the final response can describe work without proving it happened. A JavaScript or TypeScript provider can put an existing system behind this evaluation interface and return its output, actual prompt, usage, cost and metadata.

## Key ideas

- Start with a small configuration and inspect results before adding elaborate grading. Automatic assertions are optional: “Asserts are _optional_.” (E11a, Asserts.)
- The runner tests the combinations in the configuration, so adding models and cases increases calls. “This tests every prompt, model, and test case.” (E11a, Configuration, step 4.)
- Agent behavior depends on the runtime as well as the model. A runtime supplies file access, tools and state: “the agent harness determines what's possible.” (E11b, Why agent evals are different.)
- Intermediate actions affect cost and reliability even when final answers match. “Two agents might produce identical final outputs, but one read 3 files and the other read 30.” (E11b, Why agent evals are different.)
- Pick the provider for the boundary being tested. The Codex desktop alias starts a separate protocol process: “it does not attach to an already-running Codex Desktop app window or reuse Desktop UI state.” (E11b, Capability tiers.)
- A refactoring response is a report, not the edited artifact. “The agent's output is its final text response describing what it did, not the file contents.” (E11b, Refactoring with test verification.)
- Tracing records intermediate actions; a trajectory assertion checks that recorded path. “Assert the path when the path matters.” (E11b, Evaluation principles.) Use trace or metadata checks for commands, approval requests and tool use.
- Give editing runs separate starting files. “Set `copy_working_dir: true` to give each eval step a fresh copy instead:” (E11b, Isolated workspaces.) This prevents earlier runs from changing later tests.
- A fresh copy prevents interference but does not restrict filesystem access. “A workspace keeps calls from affecting each other, but it isn't a sandbox.” (E11b, Isolated workspaces.) The guide recommends containers for untrusted agents with shell access.
- A custom provider has a small interface. “At minimum, a custom provider must implement an `id` method and a `callApi` method.” (E11c, Provider Interface.) Its response can carry structured data as well as text.
- Failed calls must remain failures. “Return an `error` for failed requests.” (E11c, Provider Interface.) Missing, null or undefined output also fails; the literal strings `"null"` and `"undefined"` are graded as content.
- Preserve the prompt actually sent when the system rewrites inputs. It appears in the viewer and feeds prompt-based checks: “Shown as "Actual Prompt Sent" in the web UI” (E11c, Reporting the Actual Prompt, Display bullet).
- TypeScript providers run outside the frontend build pipeline. “Promptfoo loads TypeScript providers in Node.js, not through your frontend bundler.” (E11c, TypeScript Providers in Frontend Projects.) Imports must work in Node or the provider must be built first.
- Cost data requires care. The price helper reads an installed catalog: “This is a catalog lookup, not a complete billing calculator” (E11c, Looking up text-token prices). Prefer a reported total when available.
- Media should come from test variables rather than parsing a rendered prompt. “Always set `injectVar` explicitly when using media strategies.” (E11c, Handling Multimodal Content.) The default is the last prompt variable, which may be the question rather than the image.

## How to do it (concrete steps, checklists, templates)

### E11a: run the example, then change the configuration

1. After installing Promptfoo, create its translation example:

```bash
npx promptfoo@latest init --example getting-started
```

2. Configure the selected provider's credentials. The source shows `OPENAI_API_KEY` with a placeholder value.
3. Enter the example directory, run it, and open results:

```bash
cd getting-started
npx promptfoo@latest eval
npx promptfoo@latest view
```

Alternative setup routes are interactive `promptfoo init` and browser-based `promptfoo eval setup`.

The Configuration section then gives this order:

1. Add prompts to `promptfooconfig.yaml`, using `{{variable_name}}` placeholders.
2. Add providers, meaning the models or systems called by the runner.
3. Add input variables and optional assertions. The translation examples use `contains` and `icontains`, the latter checking text without case sensitivity.
4. Run `eval` from the configuration directory.
5. Review outputs with `view`.

Its examples follow with prompt quality, model quality, RAG quality and agent quality. RAG means generating answers using retrieved context. The prompt example combines an `llm-rubric`, a rule graded by another model, with a JavaScript length score. The RAG example checks factuality, answer relevance, context recall, context relevance and faithfulness to context. The agent example uses the OpenAI Agents SDK for dice rolls, inventory, scenes and character stats; install its dependencies with `npm install` before evaluation.

### E11b: verify coding work and intermediate actions

The guide presents four examples in this order:

1. **Security audit:** Use Codex SDK with `working_dir` and `output_schema`, a required JSON structure. Seed Python files with MD5 password hashing and sensitive payment logging. Check JSON, at least two findings and at least one high or critical severity. The example scores finding count; its displayed assertion does not match each finding against a specific seeded bug.
2. **Approval protocol:** Use `openai:codex-app-server:gpt-6-sol`, read-only access, on-request approvals and decline policies. Ask for `touch approval-check.txt`; inspect `metadata.codexAppServer.serverRequests` for a command approval request. This checks an event rather than whether the final explanation sounds plausible.
3. **Refactoring:** Ask Claude Agent SDK to replace MD5 with bcrypt and run pytest. Enable `Write`, `Edit`, `MultiEdit` and `Bash`, set `permission_mode: acceptEdits`, and use a copied workspace. The initial string assertion checks the response for bcrypt, tests and success. The guide then explains how to verify files or recorded actions instead.
4. **Multi-file implementation:** Request a Flask rate limiter, route decorators, tests and a Redis dependency. A model rubric scores all four at 1.0, two or three at 0.5, and otherwise 0.0, with a 0.75 pass threshold.

For trace checks, enable `tracing.enabled`, `otlp.http.enabled` and Codex `enable_streaming`. OTLP is the trace transport configured in the example. Use `trajectory:step-count` for a command matching `pytest*` with `min: 1`, plus a reasoning-step check. Where tool-oriented spans exist, use `trajectory:tool-used` or `trajectory:tool-sequence`.

For file checks, use an assertion file such as `file://check-workspace.js`. Read `context.providerResponse.metadata.workingDir` while assertions run. The sample checks that `user_service.py` contains bcrypt and no md5. `workspaceDiff` supplies a unified diff for cloned workspaces; an `agent-rubric` grader can inspect the same workspace.

Workspace modes are `true` for automatic clone or copy, `'git'` for a clean current-commit clone, and `'copy'` for a directory copy. Workspaces are deleted after the call's assertions. Claude Agent SDK, Codex SDK and OpenCode SDK support them. Responses are not cached in this mode. Only eval steps receive them; unsupported calls fail. Submodules and unresolved or external links are rejected. Linked worktree metadata can also prevent copying.

The final QA checklist calls for a plain-model baseline, at least one structured assertion, cost and latency thresholds, `--no-cache` during development, a disposable workspace for editing, trace or metadata checks where needed, and `--repeat 3` for stable prompts. Validate local configs before expensive runs:

```bash
npm run local -- validate config -c examples/openai-codex-app-server/promptfooconfig.yaml
npm run local -- eval -c examples/openai-codex-app-server/promptfooconfig.yaml --no-cache
```

The Safety section says to exclude production credentials, customer data and internal-system access. It offers ephemeral containers, read-only mounts, dummy keys and tool restrictions. Enable write, shell, MCP or custom permissions only when the test checks those behaviors.

### E11c: put a custom system behind the provider interface

Follow the page's example progression:

1. Choose CommonJS, ESM or TypeScript. Implement `id()` and async `callApi(prompt, context, options)` returning `output`.
2. Optionally initialize the provider from `options.id` and `options.config`. The API example uses `promptfoo.cache.fetchWithCache`.
3. Return `ProviderResponse` fields as needed: `error`, actual `prompt`, `tokenUsage`, `cost`, `cached`, conversation-ending fields, `guardrails` and `metadata`.
4. If estimating text cost, call `getModelPricing` with provider and exact model ID. Select long-context rates above the catalog threshold. Unknown or unpriced entries return `undefined`.
5. For guardrails, meaning policy checks, return `guardrails` beside `output`. Set `flagged` explicitly. Expected blocks are scorable output; guardrail failures return errors.
6. Read test inputs from `context.vars`, and full test information from `context.test`. Report dynamically generated prompts with the response's `prompt` field.
7. For TypeScript, implement `ApiProvider` using `ProviderOptions`, `ProviderResponse` and `CallApiContextParams`. Put aliases in `tsconfig.json` and run from the project root. Build frontend-dependent providers first if imports require browser globals, CSS or bundler plugins.

Optional later capabilities include embeddings, classification and media. Embedding cancellation requires `supportsEmbeddingCancellation = true` and forwarding `abortSignal`. Media forwarding differs by format: raw image bytes may need a data URL; audio requires remote generation; actual MP4 generation requires local FFmpeg. The page advises separate audio/video scans and logging media lengths or hashes rather than full payloads.

Finally, configure the provider through `file://./myProvider.mjs`, a display `label` and `config`. Multiple instances can use different settings. `linkedTargetId` links a local provider to a Promptfoo Cloud target and is identified as a Cloud feature.

## Tools, code and commands named

- Runner/install routes: `promptfoo`, `npx promptfoo@latest`, `npm install -g promptfoo`, `brew install promptfoo`, `promptfoo init`, `promptfoo eval`, `promptfoo view`, `promptfoo eval setup`. No fixed Promptfoo version is given.
- Example initializers: `npx promptfoo@latest init --example eval-self-grading`, `npx promptfoo@latest init --example compare-openai-models`, `npx promptfoo@latest init --example eval-rag`, `npx promptfoo@latest init --example openai-agents-basic`.
- Override command: `npx promptfoo@latest eval -r google:gemini-3.8-flash google:gemini-3.5-flash-lite`. Other named comparisons cover reasoning effort, temperature, open-source models and LLM chains.
- Runtime providers: `openai:codex-sdk`, `openai:codex-app-server`, `openai:codex-desktop`, `anthropic:claude-agent-sdk`, `opencode:sdk`, `openinterpreter`; libraries `@openai/codex-sdk`, `@anthropic-ai/claude-agent-sdk`; processes `codex app-server`, `interpreter app-server` using JSON-RPC, a structured request/response protocol.
- Exact model identifiers shown include `openai:gpt-6-sol`, `openai:gpt-6-luna`, `openai:gpt-6-astra`, `anthropic:claude-sonnet-5`, `gpt-5-mini`, `gpt-5`, `claude-3-haiku-20240307`, `text-embedding-3-small`. These are capture contents, not independently verified current recommendations.
- Assertion names include `contains`, `icontains`, `icontains-any`, `contains-json`, `is-json`, `javascript`, `llm-rubric`, `agent-rubric`, `cost`, `latency`, `guardrails`, `not-guardrails`, `moderation` and the trajectory assertions above.
- Other named tools: Node.js, Vite, Next.js, Webpack, GenAIScript, OpenAI Agents SDK, Ollama, Python, Go, Flask, Redis, bcrypt, pytest, Git LFS, FFmpeg and Winston. Configuration uses `promptfooconfig.yaml`, `tsconfig.json` and `https://promptfoo.dev/config-schema.json`.
- Cache APIs: `promptfoo.cache.getCache()`, `cache.set`, `cache.get`, `promptfoo.cache.fetchWithCache`. Media settings: `redteam.injectVar`, `PROMPTFOO_DISABLE_REMOTE_GENERATION=true`, `PROMPTFOO_DISABLE_REDTEAM_REMOTE_GENERATION=true`.

## Numbers and strong claims

- **60+ providers:** E11a, Configuration and Next steps. A product breadth claim; no inventory is included.
- **15 riddles, 45 model calls plus grading:** E11a, Model quality. Three configured models use low reasoning effort and `max_output_tokens: 2048`. Example thresholds are $0.15 and 60,000 ms per response. The source explicitly says these checks do not cap spending or stop slow requests.
- **About 1M tokens for Codex system context:** E11b, Security audit. An expectation stated without measurement evidence in this packet. The claim that a plain LLM will explain an audit rather than perform it is a baseline claim for a model without file access.
- **Git 2.41 minimum for cloning:** E11b, Isolated workspaces. Older Git makes automatic mode copy and explicit `'git'` mode fail. Diffs exceeding 100,000 characters are truncated.
- **$0.10–0.30 and 30–120 seconds:** E11b, Cost and latency. Illustrative security-audit estimates, not a measured benchmark. Its threshold example is $0.25 and 30,000 ms; the refactoring example uses $0.50.
- **“If a prompt fails 50% of the time, the prompt is ambiguous.”** E11b, Non-determinism. Treat as opinion or an overstrong diagnostic rule. The capture supplies no evidence that ambiguity is the only cause.
- **Token patterns reveal file reading:** E11b, Cost and latency and Evaluation principles. Treat as a heuristic, not proof. The same guide attributes high audit usage to system context.
- **Catalog limits:** E11c, Looking up text-token prices. Rates are USD per text token and omit live price updates, cache discounts, service tiers, regional changes, tools, audio and images.
- **Cache examples:** E11c, Cache System. `ttl: 3600` is seconds; the fetch timeout example is 5000 ms. These are sample settings.

## Compared with the deep research report

Comparison is limited to E00 section 3.1.

- **Right:** The report says “Custom providers let you evaluate an application boundary”. E11c says providers “integrate with any API or service not already built into promptfoo.” The interface supports that summary.
- **Right:** The report names “OpenCode SDK, Codex integrations, and Claude Agent SDK”. E11b explicitly lists those integrations and distinguishes their runtime boundaries and permissions.
- **Right:** The report says its commands are “not a complete agent-evaluation setup.” E11a introduces a translation example; E11b adds file, trace, permission and workspace checks.
- **Overstatement:** “Best first runner for your background” is the report's recommendation. These captures show Node/TypeScript integration and examples but do not compare Promptfoo against competing runners. No concrete factual error is evident in section 3.1.
- **Omitted:** The report mentions “permissions, and side effects” but not the operational warning “it isn't a sandbox” (E11b, Isolated workspaces), workspace lifetime or uncached editing runs.
- **Omitted:** Its broad claim about “assertions” leaves out the warning that agent output is “not the file contents” (E11b, Refactoring). The file and trace examples are central to verifying worker completion.
- **Omitted:** “JavaScript/TypeScript integration” does not capture the Node-versus-bundler constraint (E11c, TypeScript Providers in Frontend Projects), actual-prompt reporting, failure handling or incomplete catalog billing.

## Fit for the user's agent workspace

- (inference) Copy the YAML test-case structure for one bounded worker task. Keep task inputs and explicit success rules beside the runner config so a later session can understand the test.
- (inference) Compare complete runtime configurations, including permissions and working directories, rather than crediting every difference to the model. Include a plain-model baseline where file access matters.
- (inference) Adapt workspace assertions to check allowed file changes and required outputs. Use traces for claims such as ran tests or requested approval. A fluent completion report alone cannot establish scope compliance.
- (inference) Use a TypeScript provider if the existing worker interface does not fit a built-in integration. Return errors separately from ordinary refusals, preserve the actual prompt, and attach measured usage and cost when available.
- (inference) Repeat tasks to expose instability and use cost/latency thresholds as regression signals. A threshold assertion cannot enforce the user's spending budget before a request completes.
- (inference) Skip media and cloud linking for the first Markdown-worker evaluation. The packet provides no ready-made evaluator for this workspace's skills, worker-depth policy or durable-memory rules; those requirements need task-specific assertions.

## Best parts to read or watch first

Times below are digest estimates, not source-provided durations.

- **E11b, Refactoring with test verification + Isolated workspaces:** 8 to 12 minutes. Best explanation of why self-reports are insufficient and how to inspect real artifacts.
- **E11c, Provider Interface + TypeScript Implementation + TypeScript Providers in Frontend Projects:** 6 to 8 minutes. The shortest route from a TypeScript system to a runnable provider.
- **E11a, Running an example + Configuration:** 5 to 7 minutes reading, excluding installation and execution. Establishes the basic loop.
- **E11b, QA checklist + Evaluation principles:** 3 to 4 minutes. A compact set of checks for repeatable worker evaluation.
- **E11c, Looking up text-token prices + Reporting the Actual Prompt:** 3 to 5 minutes. Useful for comparing cost and explaining differences between configured inputs and actual calls.
