---
created_at: 2026-10-13
model: gpt-6.1-sol (low)
doc_type: digest
source_ids: [E15a, E15b, E15c]
purpose: One-source digest feeding the spec compendium.
---

# Inspect AI: home, Agent Bridge and Sandboxing (E15)

**What it is:** Three Python framework documentation pages: [Inspect](https://inspect.aisi.org.uk/), [Agent Bridge](https://inspect.aisi.org.uk/agent-bridge.html), and [Sandboxing](https://inspect.aisi.org.uk/sandboxing.html). The home capture names the UK AI Security Institute as author and credits development to it and Meridian Labs. The other captures have unknown authors. Publication dates are unknown; the home page's software citation says May 2024. Captured October 13, 2026. About 8,800 words including code, roughly 40 to 50 minutes with examples, estimated here.

**Capture status:** All three frontmatters say full. These are verbatim Quarto documentation sources, with relative links and source syntax retained. E15c expands five included files covering execution, the environment interface, container limits and sample concurrency. No missing text is declared. Each capture warns that source may differ from deployed documentation and says rendered HTML was fetched for verification. Linked tutorials, external agent examples and screenshot contents are not supplied as text.

## The point in three sentences

Inspect combines task inputs, an answering agent and a scoring rule into a runnable evaluation with logs. Its bridges let existing Python or sandboxed CLI agents call models through Inspect, but the evaluation controls model routing and many request settings. A sandbox isolates only work sent through its interface, so network access, host tools and generation settings need explicit attention when comparing workers.

## Key ideas

- **Separate inputs, execution and grading.** A dataset supplies prompts and expected answers; a solver produces answers; a scorer grades them. A solver can be one model call or an agent using tools over many turns. Quote: "An Inspect evaluation is a Task that brings together three things:" (E15a, Hello, Inspect).

- **A simple answer check differs from an agent task.** SimpleQA uses model grading, meaning another model judges free-form answers against a target. The capture-the-flag example gives an agent shell and todo tools, permits three attempts, and checks whether its answer contains the flag. Quote: "Agent evaluations require the model take actions rather than just answer a question." (E15a, Agent: CTF Challenge).

- **Existing agents can use Inspect's model layer.** The Python bridge runs in the evaluation process. The sandbox bridge runs the agent behind a local proxy, a service that forwards its API requests. Quote: "these agents can be written in any language" (E15b, Overview).

- **Requested model names can hide the actual model.** The sandbox bridge checks aliases, then a resolver, then uses the evaluation model for other names. This includes background calls unless mapped separately; `requested_model` records what the agent asked for. Quote: "These calls are served by the eval's model unless you map the names." (E15b, Models).

- **Reasoning effort is not automatically preserved.** The bridge normally drops client generation settings, including token limits, sampling controls and reasoning effort. Inspect's resolved model settings and provider defaults apply; prompts, tools, response format, stop sequences and seed are still forwarded. Quote: "by default the bridge does not forward client generation parameters" (E15b, Generation Config).

- **Provider tools are a separate network grant.** Web search, fetch, provider code execution and remote MCP servers can act outside the sandbox. MCP is the tool connection protocol used here. The sandbox bridge withholds these capabilities unless granted, while ordinary agent function tools are not withheld. Quote: "all media content (images, audio, video, and documents) in a request to a sandbox bridge must be an inline `data:` URI" (E15b, Granted Capabilities).

- **Host tools normally require a matching model proposal.** A bridged host tool gets one execution with the proposed, approved or modified arguments. Transport retries need the model to propose another call. Quote: "Bridged tools execute only for calls the model proposed in a bridged generation, once per proposal." (E15b, Execution Contract).

- **Codex code mode changes that contract.** When the model writes JavaScript that calls MCP tools, its proposal is the outer `exec` call. The bridge cannot match the inner calls, so these servers need `require_proposal=False`; approval then reviews the outer script. Quote: "the bridge no longer guarantees that they run only for calls the model made" (E15b, Execution Contract).

- **Tool descriptions affect permissions.** Matching usually uses the served description rather than renamed tool names. Identical or empty descriptions can allow a proposal to grant one execution of each indistinguishable tool. Quote: "give bridged tools distinct docstrings to keep matching one-to-one" (E15b, Matching a Proposal).

- **Approval is applied before the agent sees a call.** Rejected calls and explanations go back to the model, which generates a replacement response. Model calls still appear in Inspect logs. Quote: "the rejected call and an explanation are replayed to the model" (E15b, Tool Approval).

- **Creating a sandbox does not move all code into it.** Python tools, agents and scorers still run in the evaluation process. Only work requested through `sandbox()` runs inside the container. Quote: "Provisioning a sandbox does not automatically run tools, agents or scorers in the container." (E15c, Example: File Listing).

- **Each sample gets its own environment and setup.** Sample files are copied first, then its setup script runs. Expected interface errors can reach the model for recovery; unexpected infrastructure errors fail the sample. Quote: "each sample gets its own sandbox *instance*, even if the sandbox is defined at Task level" (E15c, Per Sample Setup / Sandbox).

- **Custom Docker configuration can restore internet access.** Generated configuration disables networking. A custom Compose file replaces it, so explicitly retain `network_mode: none` unless networking is needed. This restriction does not cover the evaluation process or provider tools. Quote: "It does not restrict network access from the evaluation process or model provider." (E15c, Docker Configuration / Task Configuration).

- **Successful execution can return incomplete output.** Built-in providers discard the beginning of oversized output streams and keep the trailing part. File reads instead raise a size-limit error. Quote: "have the command write to a file and read it with `read_file()`" (E15c, Sandbox Limits).

- **Concurrency affects recovery as well as speed.** Separate controls govern sandboxes, subprocesses, samples and model connections. Too many active samples can delay writing completed samples to logs. Quote: "less total recoverable samples in the case of an interrupted task" (E15c, Resource Management / Max Samples).

## How to do it (concrete steps, checklists, templates)

These are separate source workflows, kept in their source order.

**Start and run a task, E15a:**

- Install `inspect-ai`; optionally install the Inspect VS Code Extension.
- Install the chosen provider's Python package and set its API key in the environment.
- Define a `@task` function returning `Task(dataset=..., solver=..., scorer=...)`. The SimpleQA example loads `codelion/SimpleQA-Verified`, split `train`, and maps `problem` to `input` and `answer` to `target` with `FieldSpec`.
- Run `inspect eval simpleqa.py --model openai/gpt-5`, then `inspect view`.
- For the CTF example, use `json_dataset("challenges.json")`, `react()` with `bash()` and `todo_write()`, `attempts=3`, `includes()` and `sandbox="docker"`.
- Alternatively call Python `eval(simpleqa(), model="openai/gpt-5")`.

**Bridge an existing agent, E15b:**

- For an in-process Python agent, use its usual supported provider connector with model name `inspect`. Run it inside `agent_bridge(state)`, convert messages where needed, and return `bridge.state`.
- For a sandboxed agent, install it in the sandbox and configure its API base URL to localhost port 13131. Wrap its invocation in `sandbox_agent_bridge(state)` and run it with `sandbox().exec()`. The example reads the actual port from `bridge.port`, extracts input with `user_prompt()` and checks execution success.
- Grant required provider capabilities explicitly. To expose chosen host tools, pass `BridgedToolsSpec` objects through `bridged_tools` and use the returned `bridge.mcp_server_configs`.
- Map additional model names with `model_aliases` or `model_resolver`. Do not expose grader or monitor roles as aliases the agent can call.
- If agent generation settings should govern, pass `forward_generation_config=True`. Set service tier, storage and provider tool options in the evaluation configuration.
- Add `ApprovalPolicy` entries when required. Use `transcript().info(...)` for additional transcript information.

The sandbox invocation example omits `await` before `sandbox().exec()`, while E15c declares that method async and awaits it in the file-listing example. This digest preserves the distinction rather than presenting the bridge snippet as tested code.

**Prepare and operate sandboxes, E15c:**

- Implement tools using `await sandbox().exec(...)`; return successful output or raise `ToolError` with stderr. Specify a sandbox at sample, task or evaluation level.
- Use `exec`, `exec_remote`, `write_file`, `read_file` or optional `connection` methods. Disable `timeout_retry` for commands whose repeated side effects could change results.
- Bind a sandbox type and optional config path. Evaluation-level type binding outranks task, which outranks sample; a sample's config file takes precedence when its type matches the enclosing type. Dynamic configuration can use `SandboxEnvironmentSpec`, `ComposeConfig` and `ComposeService`.
- Set sample `files` and then `setup`. Prefix a file key with a named environment, such as `victim:flag.txt`, when needed.
- Install supported Docker Engine and Compose versions. Supply a `Dockerfile` or `compose.yaml` when the default image is insufficient. Set CPU, memory and network limits explicitly.
- For prebuilt images, use `--sandbox-prebuilt`. Required images must already exist or startup fails before samples run.
- For multiple environments, the default is a service named `default`, then one with `x-default: true`, then the first service. Use `sandbox("victim")` or `sandbox_default("victim")` to select another.
- Allow automatic cleanup, or retain environments with `--no-sandbox-cleanup` to inspect them. Clean them later with `inspect sandbox cleanup docker`.
- Tune `max_sandboxes`, `max_subprocesses`, `max_samples` and container limits. Use tracing and `inspect trace anomalies` to investigate stuck or failed commands.

## Tools, code and commands named

- Framework/API: `inspect-ai`, `Task`, `@task`, `Sample`, `FieldSpec`, `hf_dataset`, `json_dataset`, `generate()`, `use_tools()`, `react()`, `model_graded_qa()`, `includes()`, `match()`.
- Agent integration: OpenAI Agents SDK, Pydantic AI, LangChain, Claude Code, Codex CLI, Gemini CLI, OpenCode, Antigravity's `call_mcp_tool`, Inspect SWE, `AsyncOpenAI`, `Agent`, `AgentState`, `agent_bridge()`, `sandbox_agent_bridge()`, `messages_to_openai()`, `get_model()`, `BridgedToolsSpec`, `MCPServerConfigStdio`.
- Provider installation commands: `pip install openai`, `pip install anthropic`, `pip install google-genai`, `pip install torch transformers`. Environment names: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`, `HF_TOKEN`.
- Bridge addresses: `OPENAI_BASE_URL=http://localhost:13131/v1`, `ANTHROPIC_BASE_URL=http://localhost:13131`, `GOOGLE_GEMINI_BASE_URL=http://localhost:13131/v1beta`.
- Sandbox types/packages: `docker`, `local`, `k8s` / `inspect-k8s-sandbox`; `daytona` and `modal` / `inspect-sandboxes`; `ec2` / `inspect_ec2_sandbox`; `proxmox` / `inspect_proxmox_sandbox`; `vagrant` / `inspect_vagrant_sandbox`; `openshell` / `inspect-openshell-sandbox`. `local` provides no isolation.
- Operations: `inspect eval ctf.py --sandbox-prebuilt`, `inspect eval ctf.py --no-sandbox-cleanup`, `inspect sandbox cleanup docker inspect-task-ielnkhh`, `docker exec -it inspect-task-ielnkhh-default-1 bash -l`, `inspect trace anomalies`.
- Images: `inspect-tool-support`, `ctf-agent-environment:1.0.0`, `python:3.12-bookworm`. Documentation aids: `inspect-skills`, `llms.txt`, `llms-guide.txt`, Copy Page. No Inspect package version is specified.

## Numbers and strong claims

- E15a, Welcome / Getting Started: over 200 prebuilt evaluations and over 20 model providers. These are catalogue claims, not evidence of evaluation quality.
- E15a, LLM Assistance: documentation index about 2k tokens; full guide about 185k tokens.
- E15b, Sandbox Bridge: proxy defaults to port 13131. It listens only inside the sandbox, rejects browser preflight requests and accepts only `application/json` bodies. These are stated security properties, not independently tested here.
- E15b, Bridged Tools: default tool-result limit 16KB; content-list results are not truncated. Matching a Proposal accepts certain truncated descriptions agreeing for at least 64 characters, with a short trailing marker.
- E15b, Request Settings: `previous_response_id` requests fail with HTTP 400. An OpenAI computer-tool request also fails with 400 when the evaluation disables provider storage.
- E15c, Environment Interface / Sandbox Limits: default reads 100MB and execution output 10MB. The read-method error text calls its limit 100 MiB. Example overrides are `209715200` and `20971520` bytes. Advisory execution retries allow no more than two retries, each with a timeout below 60 seconds.
- E15c, Installation: Docker Engine at least 24.0.6; Compose at least 2.21.0, or 2.22.0 when pulling sandbox images. More than 30 concurrent containers prompts advice to configure address pools.
- E15c, Max Sandboxes / Max Subprocesses: Docker defaults to twice the processors available to the evaluation; subprocess concurrency defaults to that processor count. Effective container CPU limits count instead of host totals.
- E15c, Environment Binding: prose says two built-in environments and six external ones, but the table lists two built-ins and seven external environment types. The capture is internally inconsistent here.
- E15a, Welcome: making evaluations easy to write and reuse is promotional positioning. The examples illustrate the design but do not measure ease, cost savings or worker quality.

## Compared with the deep research report

Comparison is limited to E00 section 3.5, the Inspect-specific passage.

- **Right:** The report calls out "custom tasks and scorers" and "detailed logs". E15a defines dataset, solver and scorer; E15b says "All model calls are captured" (Transcript).
- **Right:** The report says Inspect supports "Claude Code, Codex CLI, and Gemini CLI". E15b Overview names all three as sandboxed CLI agents. Detailed Claude Code and Codex demonstrations are linked, not included in these captures.
- **Right, but incomplete:** The report says to "record the bridge’s model-routing behavior". E15b Models explains that unmatched names "also goes to the eval's model" and records `requested_model`. Generation Config adds another comparison variable: "reasoning effort/tokens/summary" are dropped by default.
- **Overstatement if read as blanket isolation:** The report's "controlled execution environments" needs E15c's qualification: "only work that it requests through the `sandbox()` interface runs in the container" (Example: File Listing). Host code and provider tools remain separate routes to outside resources.
- **Important omissions:** The report omits provider capability grants, inline-media requirements, one-execution host-tool grants, description-based matching and the Codex code-mode exception. E15b explicitly says the code-mode proposal is "the `exec` call" (Execution Contract). It also omits custom Compose networking, incomplete execution output and concurrency/recovery tradeoffs.
- **Recommendation, not source fact:** The report says "Learn this later". The captures provide introductory examples but do not prescribe that learning order. They also do not give a complete cost-accounting method or workspace-specific scope scorer.

## Fit for the user's agent workspace

- (inference) Adapt dataset/solver/scorer separation to bounded worker packets. Define task completion and staying within scope as separate grading criteria; the captures do not supply those rubrics.
- (inference) Try one existing CLI worker through the sandbox bridge before rebuilding its behavior as a native Inspect agent. The linked examples are starting points, not captured setup instructions.
- (inference) Record requested and resolved models, aliases, reasoning settings and `forward_generation_config` beside each comparison. Otherwise cheap background calls may become calls to the main model and effort settings may change.
- (inference) Keep grader and monitor models out of reachable aliases. Give every exposed host tool a distinct description and treat `require_proposal=False` as a deliberate expansion of access.
- (inference) Preserve `network_mode: none` in custom Compose files for offline tasks, while separately checking provider grants and host tools. Container settings alone do not enforce workspace scope.
- (inference) Read transcripts for failures before relying on aggregate scores. Use explicit file reads for large structured results so output truncation cannot quietly distort grading.
- (inference) Use Inspect when repeatable environments and CLI execution justify Python integration. Skip large documentation dumps initially; the index can route to relevant pages. These captures do not establish whether that integration is worth its cost for this workspace.

## Best parts to read or watch first

Times are reading estimates, not source timings. All pointers refer to text.

- E15a, Hello, Inspect: SimpleQA and CTF examples, 5 to 7 minutes. Learn the three task parts and the difference between answer and action evaluations.
- E15b, Models and Generation Config, 4 to 6 minutes. Read before comparing model tiers or reasoning effort.
- E15b, Granted Capabilities and Bridged Tools / Execution Contract, 7 to 10 minutes. Read before giving sandboxed workers host or provider tools, especially Codex code mode.
- E15c, Example: File Listing and Docker Configuration / Task Configuration, 5 to 7 minutes. Establish exactly what is isolated and how custom configuration changes networking.
- E15c, Sandbox Limits and Resource Management, 4 to 6 minutes. Avoid incomplete outputs and understand the throughput/recovery tradeoff.
