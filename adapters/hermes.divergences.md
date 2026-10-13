---
created_at: 2026-09-17
updated_at: 2026-10-01
model: deepseek-v4.1-flash
doc_type: adapter
purpose: Record Hermes-specific choices and limitations that must be revisited during each Hermes-owned reconciliation.
related:
  - path: ./hermes.md
    why: Defines the current Hermes mapping.
  - path: ../capabilities/connectors.md
    why: Defines the portable MCP registry considered here.
---

# Hermes-Specific Decisions

## Decisions confirmed 2026-09-17

- **Global agents workspace skills:** not mirrored wholesale into global Hermes. On 2026-10-01 six task/search loaders point to canonical skills; the already-present `browser-use` loader remains. `skills.external_dirs` and `skills.auto_load` stay empty. These loaders do not change other harnesses' native configuration or authorize automatic delegation.
- **Global agents workspace registry `playwright`:** generic managed Playwright was declined on 2026-09-17. Separate `playwright_extension` and `playwright_cdp` entries were later configured for selected browser routes; keep their identities and verification tiers separate rather than claiming the generic connector was installed.
- **Global agents workspace registry `chrome-devtools`:** not configured in global
  Hermes. The user declined to add it.
- **Global agents workspace registry `figma`:** not configured in global Hermes.
  The user declined to add it.
- **Global agents workspace registry `git`:** not configured in global Hermes. The
  user declined to add it.
- **Global agents workspace registry `github`:** not configured in global Hermes.
  The user declined to add it.
- **Global Hermes bridges:** its browser automation, terminal, computer use, and
  the `gh` tool stay local to Hermes. They are not candidates for promotion into
  the global agents workspace, and they are not substitutes for the declined
  registry connectors.
- **Global Hermes worker tiers:** all six cells are recorded in `hermes.md` as
  disabled or unsupported-with-reason. No cell resolves to an inherited model, and
  no generic subagent stands in for a maintained role.
- **Global Hermes default model:** intentionally not recorded. The user rotates it
  regularly, so it is configuration rather than a workspace preference.
- **Model selection:** current choices, limits, and field notes live only in
  `~/agents/ai-models/delegation-briefing.md`. A previous local
  blanket model prohibition was retired with the skill cleanup.
- **Workspace familiarity is the reason this adapter exists.** The user's stated
  priority is that Hermes knows the workspace structure, its artifacts and specs,
  how to contribute to it, how to read from it, and how the separate private repo
  relates to it.
- **Legacy integration pattern:** no legacy endpoint, connector, or role-level MCP
  record is retained.
- **Harness call procedure:** the global agents workspace `task-*` skills and
  their capability guides own launch permissions and scope. The dated Hermes
  caller-side copy was removed because it conflicted with current guidance.
- **cmux left unwired:** `cmux` is installed and running, and its own documentation
  covers driving agent terminals and using an integration named `hermes-agent`. The
  user has not asked for it to be connected, so no cmux hooks were installed and
  `cmux.json` was left unedited. Keep it local and unconnected until the user
  decides otherwise.

## Open Items Needing a User Decision

- **`delegate_task` role mappings:** the global Hermes native child pin is live,
  but it does not implement maintained task-explore/execute roles. Do not infer
  those roles from a global child model.
- **Where harness call mechanics belong:** resolved 2026-10-01. The global
  agents workspace `task-*` skills and capability guides are canonical; global
  Hermes `codex`, `claude-code`, and `opencode` are thin local overrides of
  bundled skills, not separate recipes.
- **Whether Hermes should use cmux.** Left unwired pending a decision, as recorded
  above.

## Revisit During the Next Hermes-Owned Reconciliation

- Re-list global Hermes MCP servers and bridges, then surface any new external
  integration individually for a promote-or-keep-local choice.
- Recheck live model identifiers against the briefing and provider roster before launch.
- Recheck that the `agents-workspace` skill is still a thin loader.
- Run a small read-only live profile smoke only if the user asks for one.
- Re-read the workspace `task-*` skill and capability guide before any CLI launch.
- Confirm no cmux hooks or `cmux.json` edits appeared without a user decision.
