---
created_at: 2026-09-29
updated_at: 2026-09-29
model: openai-codex/gpt-6.1-sol
doc_type: capability-reference
purpose: Help agents choose Hermes tasks without mistaking installed skills for verified access.
related:
  - path: ~/agents/capabilities/hermes.md
    why: Routes and model choice.
  - path: ~/agents/capabilities/hermes/STATE.md
    why: Actual API toolset posture and task proof.
  - path: ~/agents/skills/browser-use/SKILL.md
    why: Browser identity, route choice and account verification.
---

# What to delegate to Hermes

This is a task-family menu, not a guarantee that every tool, account or backend
is available in every CLI/API/profile session. An installed skill is procedural
knowledge, not an account connection. Check current tools and prerequisites.
The official [tool reference](https://hermes-agent.nousresearch.com/docs/reference/tools-reference)
and [documentation index](https://hermes-agent.nousresearch.com/docs/llms.txt)
cover new families without copying every vendor schema into this workspace.

## Host, code and data

- **Terminal and processes:** execute commands/scripts, builds and tests; inspect
  system state; supervise foreground/background jobs. Tools `terminal` and
  `process_manage`. Specify repo/CWD, read/write paths, network scope and budget.
  Host processes and network are not constrained by the caller's sandbox.
- **Files and code:** search/read files, patch/write code and configuration,
  debug failures, review diffs, inspect Git, use `gh` where authenticated, and
  verify implementations. Tools `read_file`, `search_files`, `write_file`,
  `patch`; shell for test runners and Git. Review-only packets must prohibit
  writes. Concurrent edits need isolated worktrees and root-owned verification.
- **Data workflows:** Python tool orchestration with `execute_code`, JSON/CSV
  aggregation, extraction, analysis, charts, batch checks and generated artifacts.
  Ask for a real output file plus reproducible checks, not invented sample data.
- **Shared workspace work:** load portable skills/specs, produce scoped plans,
  research, implementation, verification or reconciliation under workspace rules.
  Explicit changes may include skill/doc updates; durable memory is not an
  automatic side effect of every delegated job.

## Research and browser operations

- **Public web research:** `web_search`/`web_extract`, source discovery and cited
  synthesis, arXiv/literature, market or competitor research, and YouTube
  transcript work using installed skills. Use native search and fetch by default. Read ~/agents/capabilities/web/README.md for tool choice. Load web-search only on explicit request or when the packet names it.
  Retrieval can fail; require actual page reads, source links and dated claims.
- **Browser automation:** DOM/accessibility/JS/CDP reads, navigation, forms,
  screenshots, extraction, downloads/uploads where controller-supported, and
  web-console verification. Signed-out, dedicated signed-in, extension, hosted
  and parallel routes have different identities. Use the shared `browser-use`
  skill and site skills for ChatGPT/Claude workflows. Each task must name
  authorized account/sites/actions, own its tabs, and verify cleanup.
- **Authenticated browser jobs:** useful when Hermes has a tested identity that
  the caller does not. No automatic Chrome-profile inheritance; verify account
  identity through that job's actual controller. Vault tools handle password,
  payment/address and MFA handoff without putting secrets into prompts. Human
  approvals, consent, passkeys and CAPTCHAs can prevent unattended completion.
- **Desktop/Mac GUI:** computer-use/accessibility controllers for native apps,
  browser chrome, file pickers and dialogs. Requires OS consent and a supported
  session/backend. Not implied by API browser availability; current API inventory
  disables `computer_use`. Do not use GUI work to bypass blocked shell access.

## Documents and creative output

- **Document processing and creation:** PDF extraction/OCR/editing/merging,
  DOCX, XLSX/CSV and PPTX, templates, source-grounded action-item extraction,
  meeting notes, research bundles, handoffs and external document packs.
  Installed skills provide procedures; local libraries/OCR tools and source
  access must be verified. Request absolute output paths and content checks.
- **Visual/code artifacts:** HTML prototypes/design systems, SVG architecture
  diagrams, infographics, p5.js and Manim animations through relevant skills.
  Confirm rendering dependencies and exercise the artifact. Design skills do
  not prove access to a designer service or desktop app.
- **Image/vision/audio/video:** image analysis and image generation when provider
  access exists; TTS, transcription, video analysis/generation and media
  conversion where enabled and supported. Some are paid services. The current
  API enables vision/image generation but disables TTS/video toolsets; this is
  inventory, not backend proof. Authorize any added service spend. Music prompts,
  GIF search and spectrogram workflows have their own prerequisites.

## Account and application workflows

- **Google Workspace, mail and files:** Gmail/Calendar/Drive/Docs/Sheets via the
  installed Google skill and its own authenticated CLI/API; IMAP/SMTP via
  Himalaya where configured; Notion, Obsidian, Airtable and Box through their
  selected integration. No inherited Claude/Codex/OpenCode connectors. Check
  exact account/tools first; scope private reads, sends, deletions and sharing.
- **Apple applications:** Notes, Reminders, iMessage and Find My via installed
  Mac skills/CLIs. Requires apps, permissions and owner authorization. Capability
  documentation does not grant personal-message or location access.
- **Social and collaboration:** Discord reading/posting/admin where enabled,
  X/Twitter via xurl, GitHub issues/PRs and other configured integrations. API
  Discord toolsets are currently disabled. Messaging delivery may use separate
  gateway routes; verify the recipient thread and never equate send with task
  execution. Server admin and public posting need specific consent.
- **Maps, travel and monitoring:** geocoding/routes/POIs and price/news monitors
  using relevant skills/services. Scheduling or ongoing surveillance requires
  explicit cadence, stop condition and delivery destination.
- **Home Assistant, Spotify, Feishu/Yuanbao and other optional integrations:**
  supported families in Hermes; not evidence of this owner's login or enabled
  access. Treat as optional until checked, not normal defaults.

## Context and ongoing work

- **Memory and session recall:** `session_search`, skills discovery/loading and
  durable memory tooling. Can use Hermes-owned context when authorized. It does
  not receive the caller's hidden conversation, and a fresh task does not equal
  resuming this thread. Restrict recall to the task, not unrelated private chats.
- **Scheduling and automation:** cron, jobs, webhooks, recurring goals/loops,
  alerts and delivery through the gateway where configured. Persistent execution
  needs explicit authorization and a runtime that stays online. A CLI child
  exiting is not a durable scheduler. Verify job definition and an actual run
  before claiming automation works. API jobs-admin feature is currently false.
- **Multi-agent work:** native isolated child contexts, bounded orchestration,
  optional kanban/profile coordination and external harness handoffs. Default
  delegated Hermes tasks must NOT spawn workers or call other harnesses. If the
  root authorizes workers, load
  [worker tiers](../../roles/task-worker-tiers.md), bound counts,
  ensure terminal workers do not delegate, and verify child artifacts yourself.
- **Hermes setup/troubleshooting:** inspect its own config/runtime/tools and
  implement explicitly authorized Hermes changes. Do not delegate another
  harness's native configuration edits through Hermes; that harness must own
  its `/sync-tool-adapter` run.

## Required Job Output

Request: result, absolute artifact paths, exact target/source links, changed
paths, real tool outcomes and checks, model/effort/provider evidence, session/run
handle, elapsed time, unresolved questions and a clear blocked/partial/completed
status. External writes require exact-target readback. For private jobs use
private outputs; do not ask for raw credentials, cookie state or broad transcript
exports. Treat all child text as a claim until its cited outputs are verified.
