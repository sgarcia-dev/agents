---
name: claude-browser
description: Use when navigating or automating the Claude.ai website, including transcript export, projects, and new Chat or Cowork sessions.
created_at: 2026-09-29
updated_at: 2026-09-29
model: openai-codex/gpt-6-sol-900k
doc_type: skill
purpose: Portable, browser-controller-independent procedures for claude.ai.
related:
  - path: ../chatgpt-browser/SKILL.md
    why: Parallel procedures for chatgpt.com.
---
# Claude.ai Website Automation

Use for **claude.ai**, regardless of whether a desktop app's browser agent, Chrome extension, accessibility driver, Playwright, CDP, or another adapter controls the page. This is **not** an instruction for operating the Claude desktop app, Claude Code, an extension side panel, or the browser controller itself. Read the browser-use spec and the active runtime's browser adapter for authentication, driver calls, file/clipboard transfer, and tab cleanup.

## Choose a workflow

- `~/agents/skills/claude-browser/references/export.md`: one response, ordinary/Cowork transcript, embedded document, Markdown card, or research panels. A whole conversation uses an indexed folder under `~/Downloads` by default.
- `~/agents/skills/claude-browser/references/projects.md`: project inventory, creation, move/remove, and Context file lifecycle.
- `~/agents/skills/claude-browser/references/conversations.md`: start a Chat or Cowork session, inspect model/effort, send once, and verify completion.

## Navigation pacing

Never trigger page navigation more than once every five seconds. Keep one shared navigation timestamp across all task tabs and both providers; wait until at least five seconds have elapsed before opening a page or chat, following a link that changes the page, reloading, going back/forward, or opening a tab to a URL. In-page actions such as expanding a project, scrolling, opening a report panel or menu, and copying may run faster when they do not navigate. This is the user’s rate-limit precaution, not a guarantee that rate limits cannot occur. Honor any longer user-specified delay.

## Common browser contract

1. Obtain authorization for the signed-in account and for every write. Work in the browser identity the user authorized. Stop at login/MFA/permission prompts and follow the runtime's credential and approval workflow. A sidebar does not prove the account email.
2. Inventory the exact URL, target ID, current project/mode and preexisting state. Keep ownership of only task-created tabs and verify their cleanup on success or failure. Serialize account writes and use exact row-local controls, not titles alone.
3. Reobserve the hydrated page and target after each action. Selectors here are **September 2026 observations**, not a stable API. Claude virtualizes long transcripts; a successful click, visible tail, or URL transition alone is not proof of a complete export or durable write.
4. Independently reopen or reload exact targets before claiming persistence. After an ambiguous timeout, read back first; do not resend, move, delete or upload twice blindly.
5. Keep private text, titles, IDs, URLs, document bytes, cookies and file names out of shared logs/model-facing output. Transfer clipboard/download bytes directly to access-restricted private files, restore shared clipboard/download settings, and report only sanitized metadata. Do not commit private exports to the shared Agents workspace.
6. Name limits: native turn Copy, rendered transcript, document download, research-panel snapshot, Context cards and account-wide coverage are separate things. Do not call a panel's visible text a complete source or conversation archive.

## Shared skill and adapter boundary

This is a **shared skill for many agent harnesses**, not a skill for one agent or browser driver. Each harness may have different access to tabs, page DOM, accessibility trees, frames, clipboard, downloads, file inputs, or native dialogs. The website workflow states the target, observed controls, evidence and completion checks. It must not require a particular harness, tool name, browser profile, machine-specific browser path, command, or permission mechanism. Paths in this skill that point to other shared skill files are navigation links, not assumptions about where a browser runs. An unavailable capability is a limit to report or a reason to use an equivalent authorized route, not permission to claim an unverified export.

A harness using this skill **may create a thin local wrapper** that links to this file and the relevant reference. Put its browser adapter, tool invocations, authentication handoff, capability limits and driver-specific fallbacks **in that wrapper**, not here. If the harness already supplies those mechanics naturally, no wrapper is required. Do not copy website selectors or procedures into the wrapper: one change to the canonical reference should benefit every agent. This boundary applies equally to agents controlling the website through a desktop app, an extension, or a direct browser tool; it does not turn this skill into instructions for operating those surfaces.

## Updating the shared skill

- Reobserve the live website and distinguish a tested result from an inference or recovery idea. Put site behavior, selectors, target binding, verification gates and known limits in the relevant reference above. Prefer a small correction to a duplicated procedure; preserve dated evidence and mark untested paths clearly.
- Keep controller-specific syntax, profile locations, timeouts and local environment details in the proposing agent's adapter. If a proposed step only works with one driver's feature, express the **capability and observable outcome** here; place the driver's implementation in its wrapper. Do not impose that capability on other agents.
- Any agent may suggest improvements at the end of a task, with the observation, failure mode and proposed change. When authorized to edit this shared workspace and the change is supported by evidence, update the canonical reference and verify its links and consistency. Otherwise propose it without silently changing shared instructions. Then adjust a local wrapper only if its mechanics changed. Do not treat a successful edit as a live website re-test.
