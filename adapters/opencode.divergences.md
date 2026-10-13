---
created_at: 2026-09-15
updated_at: 2026-10-07
model: gpt-6.1-sol
doc_type: adapter
purpose: Record approved intentional differences in the new-machine OpenCode setup.
related:
  - path: ./opencode.md
    why: Describes the current OpenCode mapping.
  - path: ./adapter-contract.md
    why: Defines how intentional differences are recorded and revisited.
---

# OpenCode Approved Divergences

This record starts with the new-machine OpenCode setup from 2026-09-15. Earlier
OpenCode decisions and environment-specific history were intentionally removed;
they do not describe the current machine.

| Difference | Decision | Rationale |
|---|---|---|
| Global OpenCode advanced research uses Parallel for unavailable native search or fetching. | User-approved 2026-09-30. | Native search is supported but disabled; native fetching works. Keep native fetching, announce any fallback, and count Parallel calls under the canonical advanced-search limits. No other provider, helper, or permission change is implied. |
| Global OpenCode has an explicit-only advanced-search loader and a thirteenth procedure command. | User-approved 2026-09-30. | OpenCode's native autoinvoke metadata hides the loader from automatic advertisement; the command passes arguments unchanged. |
| Twelve applicable discovered skills now have native slash commands. | User-directed 2026-09-29, superseding the seven-command choice from 2026-09-15. | Make the user's skills discoverable under `/` as well as by the model. Do not add a self-delegating `task-opencode` command or copy built-in and externally synced skills into native wrappers. |
| Default/high workers have one explicit model pair across explore and execute. | User-selected 2026-09-29; latest request replaces GPT 6 Sol with GPT 6.1 Sol, preserving Low reasoning. | Defaults remain `openai/gpt-5.6-luna#xhigh`; high tiers use `openai/gpt-6.1-sol#low`. Replacement roster and resolved-agent preflight passed; earlier high-tier live checks do not verify 6.1. Execute wrappers still ask before edit or shell; mutation remains untested. |
| Changeable root model baseline and GPT 6 deprecation in global OpenCode. | User-directed 2026-09-29. | Usual root baseline may be `openai/gpt-6.1-sol#low`, escalating to Medium or High for difficult tasks; the user may switch it. Documented only, without pinning native root settings. GPT 6 Sol is deprecated by this user for slowness, not declared retired by the provider. |
| Historical Sol-low orchestrator selection; current Medium reasoning preserved during GPT 6 replacement. | Historical nested-dispatch verification 2026-09-25; GPT 6 deprecation requested 2026-09-29. | Current orchestrator resolves to `openai/gpt-6.1-sol#medium`; roster and resolved-agent preflight passed but new-model nested dispatch is pending. Fast stays disabled. Earlier CLI subagent launch fell back to default; current per-call model override is exposed but role/permission preservation is unverified. |
| Six retained MCP connectors (`playwright`, `chrome-devtools`, `jev-browser`, `figma`, `git`, `github`) remain unconfigured; browser MCPs default off pending a specific identity choice. | Original five user-deferred 2026-09-15; Jev added to the shared registry 2026-09-29. | No signed-in browser identity was selected here. Leave any tool-side login or permission expansion for a separate decision; awareness-only CLI/API/desktop routes are not installs. |
| Parallel, Exa, and Firecrawl are configured and on in global OpenCode. | User-requested 2026-09-29; approval posture updated by the user's later same-day direction to avoid harness prompts in remote loops. | Parallel and Exa search/fetch and Firecrawl search/scrape run without prompts; other Firecrawl tools remain denied. Keys are referenced through environment variables, not stored values. Vendor dashboard costs remain unverified. |
| Routine full-host permission default for root and default/high workers. | Owner-authorized migration 2026-09-30 supersedes routine execute ask posture. | External directories now allow; execute edit/shell asks removed. All four maintained leaves deny child delegation. Explore source-read-only/create-only reporting and execute path scope are prompt-enforced, not sandbox-enforced. Environment-file safeguards and deliberate MCP exclusions remain. Root and both high workers passed fresh checks; default Luna mappings are static-only pending version confirmation. Original run timed out; same-session recovery finished documentation without repeating checks. |
| Normal orchestrator broad shell access. | Owner-authorized follow-up 2026-09-30; configured/static-only, not runtime-tested. | Changed the native `shell:*` deny to allow, covering installed interpreters, package runners and absolute paths without a command list. Routine file/network/enabled-MCP access inherits V2 defaults and global rules. Preserved the deny-all child rule plus exactly four enabled explore/execute leaf IDs, terminal leaf denies, direct canonical loaders, models, disabled fast tiers, environment-file safeguards, MCP exclusions and account/privacy authority. Native patch success confirms the single deny-to-allow edit. No explicit post-edit parse/readback receipt returned before the bounded timeout; no workers, smoke, restart or Git actions. Shell access is not technical path confinement or prevention of CLI handoffs; those authority boundaries remain behavioral. |

## 2026-10-07: briefing corrections reported, not applied

The 2026-10-07 worker-tier pass in OpenCode found two things wrong on the
briefing side. This run may not edit `ai-models/delegation-briefing.md`, so the
exact replacement text is recorded here for the owner. Evidence: live
`opencode api get /api/agent` on 2026-10-07 shows the primary agents (`build`,
`plan`) carry no model, so global OpenCode pins no root model; the documented
root preference is `openai/gpt-6.1-sol#low` (user-confirmed 2026-09-29, above);
and the session that ran the sync itself ran `opencode-go/glm-5.3-flash`.

1. In the OpenCode block (section 3), replace the sentence
   "Go workers are weaker than a Sol or Opus root but guess far less." with:
   "OpenCode pins no root model: the usual root baseline is GPT-6.1 Sol low
   (42), and a session may run a Go model instead. Against that Sol low root
   the high workers score a little higher (MiMo 46.3 and GLM 5.3 44.8 vs 42.1)
   and the regular worker is about equal (41.8 vs 42.1), and the Go workers
   still guess far less." The sentence after it ("Trust them more than their
   scores suggest...") stays as is.
2. The GLM 5.3 card in section 5 is missing its "Tell the worker" line (GLM 5.3
   Flash and MiMo V2.6 Pro have one). Proposed addition at the end of the card,
   after "Instead when quota runs out: GLM 5.3 Flash, or ask the user about Sol
   medium.": "Tell the worker: 'Save anything you read with a script or a file
   write, do not hand-copy it, and stop when the packet is done.'" This targets
   the 2026-10-01 field note about a GLM 5.3 worker burning the 5-hour allowance
   by hand-copying web pages.

## OpenCode-only items awaiting a promotion-or-keep-local decision

Observed 2026-09-30: global OpenCode default explore/execute use
`openai/gpt-6-luna#xhigh`, not the Luna 5.6 favorite recorded September 29.
Confirm the preference before changing settings or claiming fresh live verification.
The September 30 permission migration preserved these mappings; both high cells
were live-verified on `openai/gpt-6.1-sol#low`. The September 29 model-pair row
above is historical, including its now-superseded execute ask description.

The global agents workspace does not define the following OpenCode-native or
externally synced surfaces as portable roles, skills, or commands. They remain
tool-local by default; none was promoted or given a new approval in this run.
List them again on the next sync until the user decides each item.

- Built-in global OpenCode primary agents: `build`, `plan`.
- Built-in global OpenCode child agents: `explore`, `general`.
- Built-in global OpenCode hidden maintenance agents: `compaction`, `summary`, `title`.
- Built-in global OpenCode commands: `init`, `review`; the Exa MCP also exposes
  `exa:web_search_help` as a prompt command.
- Built-in global OpenCode skills: `opencode`, `report`.
- Externally synced global OpenCode skills: `docs`, `import-memory`, `morning`,
  `skill-creator`, `docx`, `pdf`, `pptx`, and `xlsx`. These are visible in the
  live registry, but this sync did not inspect or edit their source harness.
- Global OpenCode's Code Mode, `browser` tool, native `webfetch`, and installed
  `agent-browser` CLI are runtime bridges, not additions to the curated MCP
  set. On 2026-09-29 the native browser was disconnected, while a separate
  isolated CLI browser completed public docs search and cleanup. That is not
  signed-in or native-browser verification. Public Parallel search worked when
  general-purpose browser search engines challenged or returned bad results.

The older enabled `jev-browser` observation is not current: it is now in the
global agents workspace registry but absent in OpenCode's MCP list. Its
earlier enablement and login identity were not adopted by this run.

Revisit these items in the next OpenCode `sync-tool-adapter` run.
