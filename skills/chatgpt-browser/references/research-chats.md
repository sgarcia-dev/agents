# ChatGPT website: start many research chats without waiting

Load `~/agents/skills/chatgpt-browser/SKILL.md`. Use this when the user has a batch of long research prompts to start in one or more projects and does not want the agent to wait for each answer. Sending is an account write: require authorization for the prompts and projects, and resolve the mode before composing. A request to execute a prompt pack authorizes its ordinary chat/project actions; do not ask again for those actions.

Observed 2026-10-05 by a Claude in Chrome browser agent at a 1288x947 viewport. Coordinates below are hints for that layout only. Take one screenshot first and re-find each control if anything looks different. Merged from a claude.ai account skill named `chatgpt-browser-research`.

## Find your way around

- The left rail shows icons only. Home is the top icon (about 17,17). **Projects** is the folder icon (about 17,230). If the user has not pinned it, it sits under the rail's `⋯` (More) menu. Clicking Home also opens a flyout sidebar with a `Projects >` entry.
- The Projects page has Search and **+ Create** at the top right (about 1075,30). Each row has `⋯`, a pin, and a square-pencil icon at the far right (about x=1100) that **opens the project page**. Clicking the project name only expands its chats in place.
- **+ Create** opens a dialog with the name field already focused. Type the name, then click **Create project** (about 764,538). It lands on the new project page, which reloads the page. The sidebar `New project` route in `projects.md` also works.
- The project page has a `New chat in <project>` composer at the top, then the Chats and Sources tabs.
- Inside a chat, the project name at the top left (about 200,17) goes back to the project page. The chat's top-right `⋯` has no Rename (only Pin, Plugins, View files).

## Mode: ask the user first

Follow the **Required research-mode confirmation** gate in `~/agents/skills/chatgpt-browser/SKILL.md` before every new run or batch. Always ask the user to choose native ChatGPT Deep research, standard Chat at **Extra high**, or standard Chat at **6 Pro**, and wait for the answer. Ask once per run, even when the initial request or referenced pack already names a mode; then apply the confirmed choice throughout that run. Explain the user's preferred tradeoff of source variety versus reasoning depth without claiming a guaranteed quality ranking. Never infer the selected tool from a prompt's “DEEP RESEARCH BRIEF” heading.

In the 2026-10-05 run the agent did **not** use `@deep-research` or the Deep research toggle. It used a normal chat with the effort slider at its rightmost setting, **6 Pro**. That chat searched the web on its own; `Searching N websites…` appeared within about 20 seconds.

- The composer's model pill (it shows `Pro`) opens the Thinking effort slider. The setting stayed the same across chats and projects, so check it once per session. As `conversations.md` says, the label is not proof of the backend model.
- A chat-mode answer is not an embedded Deep research report. When authoring new prompts, follow the size and stopping rules in `~/agents/skills/browser-deep-research-prompts/SKILL.md` (a bounded question, a cap, a time target); do not demand maximum length. A chat answer in the reply is fine, and a file is only needed if the user asks for one; preserve exact supplied prompts when executing a pack. Export that with the generated-document route in `export.md`. If the model replied in plain text instead, use the single-response route.

## Paste long prompts quickly

Use the runtime's supported multiline insertion or fill capability on the **visible** composer. Do not require synthetic page scripts or clipboard events: some controllers permit only read-only page evaluation. Where scripting is allowed, the paste-event route under "Inserting a long prompt" below is tested. The page can contain a hidden home composer and a hidden textarea fallback. Bind the visible editable element by its live accessible name or visibility, and check that no user draft or attachment would be overwritten.

Read the local prompt directly into the controller when supported, rather than copying it through tool output. Compare the full visible editor text with the source string before sending; report only the equality result and length. Preserve line breaks and all prompt wording. When the user requests exact prompts, do not append a downloadable-file instruction solely because the selected mode changed. Choose the appropriate export route later.

## Loop for each prompt (about 30 seconds each)

1. On the exact project page, insert and compare the prompt. Check the selected Chat mode and authorized effort; a previously observed Pro setting can persist across projects, but inspect each composer for unexpected changes.
2. Click the live Send control once. On an ambiguous return, inspect the current conversation before retrying.
3. Observe for up to the requested startup window. Require a new conversation URL, echoed user turn and an active responding/thinking/search indicator. Search or plan text is stronger evidence that research is underway; responding alone proves processing started. Do not wait for the answer. This is a deliberate exception to step 5 of `conversations.md`; the finished answer is checked later, at export time. Record the conversation ID against its prompt code privately before leaving.
4. Click the breadcrumb to return to the same project page for the next prompt. Keep the whole batch in one project; open or create another only if the pack itself names a second project. Never create a project per prompt, and reuse an existing project with the same name instead of making a duplicate.

Batch deterministic actions only when fresh UI checks still separate decisions. Project creation and navigation can return before the composer is hydrated; wait for its live editable control before insertion. In the Chrome extension, large batches that mixed a project creation with a long paste sometimes failed. If that happens, take a screenshot and redo only the paste, after checking that nothing was sent twice.

If ChatGPT asks clarifying questions, reply once: "No clarifications. Proceed with the brief as written and state any assumptions in the report." Never sign up for or buy anything a prompt mentions.

## Rename the chats at the end

- ChatGPT gives each chat a short title within about a minute of sending.
- The project page's chat list is stale after sending. Reload it, or arrive fresh through the Projects page's open icon.
- Hover the row, click its `⋯` (about x=854), click **Rename** (about 55 px below the row), select all, type the title, and press Return. The new name can take about a second to show.
- Rows sat at about y=188, 231 and 274 (about 43 px apart). The newest chat is at the top, so the order is the reverse of sending. Match each row by the preview text under its title, not by position alone, then reload once to confirm every name.

## Additional observed controls, 2026-10-05

A second run used normal Chat with the model pill menu visibly showing **6 Pro**, at the rightmost **Pro, 5 of 5** power setting. Seven exact prompts were inserted through the runtime's supported editable-field fill, compared before Send, and started across three projects. No Deep research tool was selected. This verifies the UI setting and startup, not completed research quality or backend model identity.

Project chat rows were list items containing a conversation link and a button named `Actions for <current title>`. Bind the row by its exact conversation ID/href before invoking its actions; do not rely on sending order or a generated title. The menu's **Rename** opened a **Rename chat** dialog with **Chat title** and **Save**. The supported keyboard activation opened an otherwise hover-hidden row action in this run. Reload the project independently and require the new title on the same conversation link. Older inline rename/Return behavior above remains a dated observation, not a requirement.

Keep private prompt text, project IDs and generated titles out of shared evidence. A skill update should retain only general controls, verification outcomes and dated limits. Preserve unrelated edits and commit only this task's safely separable changes.

## Deep research with an effort level, observed 2026-10-09

A Claude in Chrome agent ran one prompt four ways in one project: Deep research at Extra High, Deep research at Pro, Chat at Extra High and Chat at Pro. All four started. This proves the UI settings and startup, not report quality or backend model.

- **Deep research is a composer tool, not a model.** Open the composer `+` button; **Deep research** ("Get a detailed report") is in the **Add** section. It shows as a blue `Deep research` pill at the start of the editor. In the chat list preview it appears as `[$deep-research](app://connector_openai_deep_research)`, which is a reliable way to tell Deep research chats apart afterwards.
- **The pill does not carry over.** It was gone on the project page after every send. The effort setting did carry over. Turn Deep research on again for every Deep research chat, and turn nothing off for a Chat run (just check the pill is absent).
- **Effort works with Deep research on.** The pill opens a `Thinking effort` popover with a 5-stop slider. Stop 4 is **Extra High**, stop 5 is **Pro**. Clicking the label (`Pro >`) opens a model list (GPT-6 checked, GPT-5.6 Sol, GPT-5.5 "Leaving on October 14"). GPT-6 at Pro is what the user calls "6 Pro". Read the label after moving the slider; do not count stops blind.
- **Deep research shows a plan card first.** After about 15 seconds it posts a plan with **Edit**, **Cancel** and **Start**, plus a countdown of about 40 to 60 seconds. If left alone it starts by itself (one run did). Clicking **Start** starts it at once. Proof of a real start: the first plan step gets a check mark, a progress bar and `Researching…` appear, and the button changes to **Update**. A reply saying "Deep Research has started working" can appear before the plan is accepted, so it is not proof on its own.
- **Standard Chat start proof:** a `Searching …` line or `Thinking` header plus a short plan message within about 20 seconds.

### Composer details that broke older steps

- On project pages the editor was `.ProseMirror[contenteditable=true]` with accessible name `New chat in <project>`. It had **no** `#prompt-textarea` id. Bind by visibility and accessible name.
- A hidden second composer exists, with its own `Send` button. Two `Send` buttons were found; use the one with a visible size.
- After inserting a long prompt the editor grows and **Send moves to the bottom of the box**. The old Send spot becomes a **Collapse** button. Re-find Send after inserting. (One click hit Collapse; nothing was sent.)
- When checking the editor text for a Deep research pill, do not search for the words "Deep research": a prompt can contain them. Compare the editor text with `"Deep research " + prompt` instead, or check the pill element.

### Inserting a long prompt (tested route)

With a controller that allows page scripting, this worked four times with an 8,479-character prompt: store the prompt once in the tab's `sessionStorage` (it survives project/chat navigation in that tab), check its SHA-256 against the local file, put the caret at the end of the visible editor, and dispatch a `paste` `ClipboardEvent` whose `DataTransfer` holds the text. Line breaks were kept, and the editor text equalled the source exactly (plus `Deep research ` when the pill was on). Clear the stored copy when done. Controllers without page scripting should use their own multiline fill.

### Renaming

The row's `Actions for <title>` button did not open its menu from a script `click()`. Focusing it and sending a real **Enter** key did. Then **Rename** → **Rename chat** dialog → select all → type → read the input value back → **Save**. Bind each row by its conversation ID in the link. A fresh reload showed all four new titles.

### More controls and pitfalls, observed 2026-10-09 (second run)

- **Hidden tab, stale screenshots.** The working tab can report `document.visibilityState = "hidden"`. Then screenshots and the Deep research plan card stop updating; after clicking Start the card looked unchanged. Confirm state by reloading the conversation URL, not by waiting on the card.
- **Start sometimes needs a second click.** One Deep research Start click did nothing; the second worked. Reload and check before clicking again, so it is not started twice.
- **Effort button.** Its position shifts with the pill and the current label. The first click often only shows a "Thinking effort" tooltip; click again. Read the label after moving the slider.
- **Rename menu.** Hover the row first, then focus its `Actions for <title>` button (bound by conversation ID) and send a real Return. Rows reorder after each rename, so never bind by position.
- **Claude in Chrome tab group.** Closing the empty tab that `createIfEmpty` made can drop your working tab out of the controlled group, leaving an orphan tab you cannot close. Keep that first tab until the end. Page `sessionStorage` is per tab, so a prompt stored there must be stored again in a new tab, and cleared from any tab you leave behind.
