---
created_at: 2026-07-07
updated_at: 2026-07-07
model: claude-opus-4.8
doc_type: spec
purpose: Define current Agents workspace behavior for global bootstrap resolution and never-committed local overlays on generated project AGENTS.md files.
related:
  - path: ../../AGENTS.md
    why: Canonical bootstrap and routing rules this spec formalizes.
  - path: ../../conventions/agents-local-overlay.md
    why: Convention describing the never-committed overlay + skip-worktree procedure.
  - path: ../../adapters/adapter-contract.md
    why: Adapter symlink and drift rules that satisfy the resolution requirement.
---

# Agents Bootstrap Spec

Current durable behavior for how agent sessions resolve global guidance and how
machine-local instructions attach to generated, git-tracked project `AGENTS.md`
files.

## Requirements

### Requirement: Global adapter resolves to canonical guidance

The cross-tool adapter entrypoint at `~/.agents/AGENTS.md` MUST resolve to the
same inode as canonical `~/agents/AGENTS.md` via symlink or documented equivalent
direct resolution. A separate thin redirect file is drift.

#### Scenario: Tool loads global instructions

- **WHEN** an agent tool reads `~/.agents/AGENTS.md` at session start
- **THEN** it MUST receive the full canonical workspace guidance, including the
  Non-Negotiable Bootstrap section and the rule to read repo-local `agents/AGENTS.md`.

### Requirement: Canonical guidance is self-aware about dual load paths

Canonical `~/agents/AGENTS.md` MUST describe itself as loadable via two
equivalent paths (direct `~/agents/AGENTS.md` and the `~/.agents/AGENTS.md`
symlink, same inode) and MUST NOT instruct the reader to load the other path.

#### Scenario: Agent reads the file via the adapter symlink

- **WHEN** an agent loads the file as `~/.agents/AGENTS.md`
- **THEN** the bootstrap instructions MUST be unambiguous and MUST NOT imply a
  separate canonical file still needs loading.

### Requirement: Private project memory is loaded via the repo-local symlink

When a source repository has a repo-local `agents/AGENTS.md` (typically a symlink
to private project memory), reading it MUST be mandatory scoped guidance after
global and project-root bootstrap, and it supersedes the generated project-root
`AGENTS.md`.

#### Scenario: Session starts in a repo with private project memory

- **WHEN** an agent begins work in a repo whose `agents/` symlink resolves to
  Agents workspace project memory
- **THEN** the agent MUST read that project-memory `AGENTS.md` and treat it as
  superseding the generated project-root `AGENTS.md`.

### Requirement: Never-committed local overlay on generated AGENTS.md

Machine-local instructions for a repo whose root `AGENTS.md` is generated and
git-tracked MUST be applied as a never-committed working-tree edit protected by
`git update-index --skip-worktree`. They MUST NOT be merged into tracked content
by the code-generation pipeline.

#### Scenario: Local overlay applied

- **WHEN** a developer adds machine-local instructions to a generated tracked
  `AGENTS.md`
- **THEN** the edit MUST remain uncommitted and MUST be protected by
  `skip-worktree`.

#### Scenario: Auto-prepend pipeline rejected

- **WHEN** considering an `AGENTS.local.md` file physically merged into tracked
  `AGENTS.md` by `make generate`
- **THEN** that approach MUST NOT be used, because it makes accidentally
  committing local overlay into tracked `AGENTS.md` possible.

### Requirement: Recoverable source and skip-worktree registry

The canonical text of any never-committed overlay and the list of
skip-worktree-protected files MUST be stored in committed Agents workspace
project memory so they can be re-applied if the working-tree edits are lost.

#### Scenario: Local edits lost or skip-worktree cleared

- **WHEN** skip-worktree state is cleared or a checkout/pull discards the local edits
- **THEN** an agent MUST recover by re-applying the committed overlay text and
  re-setting skip-worktree, following the documented recovery procedure.

#### Scenario: Branch switch or pull with upstream regeneration

- **WHEN** switching branches or pulling changes that upstream-regenerated a
  protected file (even if `git status` reports no local change due to skip-worktree)
- **THEN** the agent MUST surgically re-apply the local overlay on top of the
  latest version with local additions taking priority, rather than discarding it.
