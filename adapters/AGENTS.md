# Adapters

Use this folder for tool adapter guidance. Adapters translate Agents workspace
concepts into one AI runtime's native files, settings, prompts, agents, skills,
commands, MCP servers, permissions, hooks, or plugins.

## Belongs Here

- Platform-neutral adapter contract and lifecycle guidance.
- Tool-specific mapping docs when a tool is intentionally onboarded.
- Notes about unsupported concepts, manual setup, and generated or copied native
  wrappers.
- Drift findings that explain how native config differs from Agents workspace
  source of truth.

## Does Not Belong Here

- Canonical skill or role behavior. Use `../skills/` and `../roles/`.
- Tool-native config files unless the user explicitly asks to store them here.
- Credentials, tokens, or private runtime secrets.

## Current Guidance

Read `adapter-contract.md` before creating or updating any adapter doc. Adapter
work should initialize or align a tool from the Agents workspace; it should not
redefine the workspace inside a tool-specific file.

Use `INDEX.md` as the lightweight registry for intentionally maintained adapters.
Keep per-tool mapping details in files such as `opencode.md`, `codex.md`, and
`cursor.md`.
Do not create full adapter manifests unless the user explicitly asks for
machine-readable adapter inventory.

## How the Canonical File Loads

The canonical instruction file is `~/agents/AGENTS.md`. Agents may read it directly
or through the `~/.agents/AGENTS.md` adapter symlink; they are the same file (same
inode). Statements about `~/.agents/...` describe the thin adapter layer that
points at canonical `~/agents` sources; they are maintenance invariants, not
instructions to load a different file. Canonical edits and commits happen in the
`~/agents` git repo.

## Cross-Tool Adapter Discovery

`~/.agents/` is the de facto cross-tool discovery layer for runtimes that can load
shared user instructions or skills from a stable home-directory path. It is an
adapter layer, not the source of truth.

- **`~/.agents/AGENTS.md` MUST symlink to `~/agents/AGENTS.md`** (same inode) so
  tools loading the adapter path receive full canonical guidance. A separate thin
  redirect file is not an acceptable substitute; treat a non-symlinked adapter copy
  as drift.
- Keep `~/.agents/skills/*` thin: they point back to canonical source files under
  `~/agents/skills/` and may carry only minimal tool-discovery metadata.
- When a tool supports `~/.agents/`, document that support in the relevant adapter
  mapping instead of copying skill or role behavior into tool-owned config.
- After meaningful edits under `~/.agents/` (excluding the symlinked `AGENTS.md`),
  run `git status` there and create a semantic commit; do not leave adapter changes
  dirty silently.
- Machine-local instructions for a repo whose root `AGENTS.md` is generated and
  git-tracked are applied as a never-committed working-tree edit protected by
  `git update-index --skip-worktree`, never merged into tracked content by the
  generator; see `../conventions/agents-local-overlay.md`.
