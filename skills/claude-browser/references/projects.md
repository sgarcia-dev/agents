# Claude.ai website: project and Context lifecycle

Load `~/agents/skills/claude-browser/SKILL.md`. Exact-target account writes require authorization. An empty Recents pane is not a full project inventory; inspect project-scoped controls and coverage before making claims.

## Create and use a project

- `/projects` lists project cards; **New project** opens `input[placeholder='Name your project']` and **Create project**. Read back the name, submit once, and verify the new project URL and heading. Observed routes included `/project/<id>` and `/cowork/project/<id>`; use the **actual resulting pathname**, never invent a route. Project home contains Chat and Cowork `[role=radio]` modes, Recents and Context. Require the selected radio's `aria-checked=true` before sending.
- Project Chat and Cowork can coexist: an observed project retained one `/chat/<id>` and one `/cowork/cse_<id>` after reopening. Verify exact project breadcrumb, project-scoped Recents links, transcript and settled response. Global sidebar Recents may precede or differ from project Recents.

## Move an existing Chat without deletion

1. Open the **exact** existing `/chat/<id>`, check that it is safe to move and has no project breadcrumb. Bind `a[href='/chat/<id>']` to its own parent `button[aria-label^='More options for ']` in the sidebar, not a duplicate-title global button. Its menu `[data-testid='move-to-project-trigger']` showed `Add to project`; choose the exact project `[role=menuitemradio]`.
2. Reopen that same ID; require the project breadcrumb and row menu `Change project` / `Remove from project`. To undo, choose that exact row's **Remove from project**, not Delete. Reopen the same ID and require its surviving turns, no project breadcrumb, and `Add to project` restored. Project Recents did not always display an older moved chat, so breadcrumb/menu state is a stronger membership check than Recents alone. A header move route, arbitrary sensitive-chat move and Cowork-task move were not tested. Serialize mutations and read back before retrying a timeout.

## Project Context files

- In the exact project, a hidden `input[data-testid='project-doc-upload']` accepted `.txt` and `.md` in a synthetic test. The adapter's file-input method may upload without a native file chooser. Wait for Context cards **after independent reload**; a transient card does not prove persistence. For authorized synthetic test chat, check model/editor as in `~/agents/skills/claude-browser/references/conversations.md`, then verify response separately from file presence.
- To remove only known task files, select their Context card checkboxes by exact `aria-label` (`Select: <filename>, <extension>, <size>`), verify the selected count, then use `button[aria-label='Delete 2 selected items']` when two are selected. Reload and require no matching cards plus Context empty state, while the chat remains. Never select unrelated files. Upload/retention and retrieval-by-model are separate claims.

## Inventory coverage and API caution

The project Recents list is bounded UI evidence. A read-only network probe observed organization-scoped `GET /api/organizations/<org>/projects/<pid>/conversations_v2?limit=100&offset=0`, whose JSON uses **top-level** `data` and `pagination` (`total`, `limit`, `offset`, `has_more`). Page until the declared count and observed item count agree. Older `/conversations` returned a plain array, with an `include_archived=true` variant. An account-wide `/chat_conversations?limit=100&offset=N` array could cross-check project UUID membership. These are unversioned private endpoints: use only within an authorized existing session, check status/JSON schema on every page, never log auth or contents, and do not treat a parse failure or 404 as zero.

`GET .../projects/<pid>/docs` included **full document content**; for a names-only inventory project only `file_name`, `created_at`, `content_length`, `estimated_token_count` in memory and discard the content immediately. Cross-check UI Context count. No project-scoped Cowork task/session listing was proven; report Cowork inventory as **partial / not provable**, not zero, even when chat pagination succeeds. Independently reopen and repeat key counts before asserting completeness. An adapter with a short script timeout should page in bounded batches rather than collapsing partial results into success.
