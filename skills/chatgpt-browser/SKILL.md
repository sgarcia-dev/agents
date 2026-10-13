---
name: chatgpt-browser
description: Use when navigating or automating the ChatGPT website, including conversation export, project management, and new chats.
created_at: 2026-09-29
updated_at: 2026-10-09
model: openai-codex/gpt-6-sol-900k
doc_type: skill
purpose: Portable, browser-controller-independent procedures for chatgpt.com.
related:
  - path: ../claude-browser/SKILL.md
    why: Parallel procedures for claude.ai.
---
# ChatGPT Website Automation

Use this skill for **chatgpt.com**, whether the website is controlled by a desktop app's browser agent, a Chrome extension, an accessibility driver, Playwright, CDP, or another browser adapter. It does not describe how to operate the ChatGPT desktop app, Codex, an extension panel, or any particular controller. The active runtime resolves authentication, browser identity, clicks, downloads, clipboard access, and cleanup. Read the browser-use contract at `~/agents/specs/browser-use/spec.md` and that runtime's adapter for its actual commands.

## Choose a workflow

- `~/agents/skills/chatgpt-browser/references/export.md`: export one response, a whole conversation, a generated document, or a deep-research report. These are **different artifacts**. A whole conversation uses an indexed folder under `~/Downloads` by default; start here for extraction.
- `~/agents/skills/chatgpt-browser/references/projects.md`: project directory, conversations, sources, add/move/remove, and independent readback.
- `~/agents/skills/chatgpt-browser/references/conversations.md`: create Chat or Work conversations, choose model/effort, select tools, and verify a sent turn.
- `~/agents/skills/chatgpt-browser/references/research-chats.md`: confirm the research mode, then start a batch of long prompts in projects without waiting for answers, paste long prompts quickly, and rename the chats afterwards.

## Required research-mode confirmation

Before every new ChatGPT research run or batch, **always confirm the mode with the user and wait for their answer before composing or sending research prompts**. This applies even when a prompt pack, earlier run or saved preference names a mode. One exception: if the user's own chat message for this run names the exact modes (tool and effort for each chat), that message is the confirmation; do not ask again. Ask once for the whole run; reuse the confirmed choice for every prompt in that run unless the user changes it. If the user's list differs from the pack (for example 4 modes instead of the pack's 3), follow the user and say so in the report.

Ask: “For this run, would you like native ChatGPT Deep research, or standard Chat at Extra high or 6 Pro?” Present all three choices. Since 2026-10-09 Deep research also has its own effort setting (Extra high or Pro), so ask which effort to pair with it. In the 9 October 2026 test, Deep research ran on deep-research-mini whatever effort was set. Explain the user's preferred tradeoff: native Deep research emphasizes source variety; standard Chat at Extra high or 6 Pro emphasizes depth of reasoning. Treat that as the user's selection guidance, not a guaranteed ranking of output quality.

Do not silently choose native Deep research because a file or heading says “deep research,” and do not silently substitute one standard Chat effort for the other. Verify the chosen live setting before sending. If it is unavailable, report that and ask which available option to use. This gate applies to starting research, not read-only exports or project maintenance.

## Export title preservation

During exports, do not rename chats unless the user explicitly requests it. Resolve missing batch codes through prompt/topic matching and record the mapping in the export index. Follow `references/export.md` for authorized title repairs and verification.

## Navigation pacing

Never trigger page navigation more than once every five seconds. Keep one shared navigation timestamp across all task tabs and both providers; wait until at least five seconds have elapsed before opening a page or chat, following a link that changes the page, reloading, going back/forward, or opening a tab to a URL. In-page actions such as expanding a project, scrolling, opening a report panel or menu, and copying may run faster when they do not navigate. This is the user’s rate-limit precaution, not a guarantee that rate limits cannot occur. Honor any longer user-specified delay.

## Common browser contract

1. Confirm the user authorized access to this account and the proposed writes. Work only in an authorized signed-in browser identity. Stop at login, MFA, or a permission prompt; the runtime's credential/approval procedure owns those. Do not infer identity from an accessible project alone.
2. Inventory the exact target, URL, mode, and preexisting state. Own only tabs you created and close/verify them even on failure; do not close or alter someone else's tab. Serialize account writes and shared clipboard or download-setting changes.
3. Reinspect the live DOM/accessibility tree. The selectors in the references are **observed in September 2026, not a stable public API**. Prefer exact role/name and target-local controls. React hydration, virtualized messages, and intercepted clicks make action returns insufficient evidence.
4. For a write, verify the target after an independent reload/reopen. On an ambiguous timeout, read back before retrying; never send, move, upload, or delete twice by assumption.
5. Keep transcript bytes, titles, project IDs, tokens, source contents, and download filenames out of shared logs and model-facing tool output. Store private exports in a restricted location, transfer browser downloads/clipboard bytes directly to files, and report only sanitized counts/status/limits. Never commit private exports to the shared Agents workspace.
6. Report the proven scope. Rendered transcript, copied turn, attached document, report artifact, project card list, and account-wide export are not interchangeable. Unexpanded content, attachments, hidden branches, and incomplete pagination must be named as omissions.

## Shared skill and adapter boundary

This is a **shared skill for many agent harnesses**, not a skill for one agent or browser driver. Each harness may have different access to tabs, page DOM, accessibility trees, frames, clipboard, downloads, file inputs, or native dialogs. The website workflow states the target, observed controls, evidence and completion checks. It must not require a particular harness, tool name, browser profile, machine-specific browser path, command, or permission mechanism. Paths in this skill that point to other shared skill files are navigation links, not assumptions about where a browser runs. An unavailable capability is a limit to report or a reason to use an equivalent authorized route, not permission to claim an unverified export.

A harness using this skill **may create a thin local wrapper** that links to this file and the relevant reference. Put its browser adapter, tool invocations, authentication handoff, capability limits and driver-specific fallbacks **in that wrapper**, not here. If the harness already supplies those mechanics naturally, no wrapper is required. Do not copy website selectors or procedures into the wrapper: one change to the canonical reference should benefit every agent. This boundary applies equally to agents controlling the website through a desktop app, an extension, or a direct browser tool; it does not turn this skill into instructions for operating those surfaces.

## Updating the shared skill

- Reobserve the live website and distinguish a tested result from an inference or recovery idea. Put site behavior, selectors, target binding, verification gates and known limits in the relevant reference above. Prefer a small correction to a duplicated procedure; preserve dated evidence and mark untested paths clearly.
- Keep controller-specific syntax, profile locations, timeouts and local environment details in the proposing agent's adapter. If a proposed step only works with one driver's feature, express the **capability and observable outcome** here; place the driver's implementation in its wrapper. Do not impose that capability on other agents.
- Any agent may suggest improvements at the end of a task, with the observation, failure mode and proposed change. When authorized to edit this shared workspace and the change is supported by evidence, update the canonical reference and verify its links and consistency. Otherwise propose it without silently changing shared instructions. Then adjust a local wrapper only if its mechanics changed. Do not treat a successful edit as a live website re-test.
