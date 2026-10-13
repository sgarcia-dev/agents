---
created_at: 2026-07-07
updated_at: 2026-07-07
model: claude-opus-4.8
doc_type: convention
purpose: Define how machine-local instructions are added to a generated, git-tracked root AGENTS.md without risking accidental commits.
related:
  - path: ../AGENTS.md
    why: Canonical routing and bootstrap requirements.
---

# Local Overlay Convention (never-committed)

How to add machine-local agent instructions to a repository whose root
`AGENTS.md` is generated and git-tracked, without ever committing local content
into that tracked file.

## Rejected approach

A prior design merged a gitignored `AGENTS.local.md` into the generated tracked
`AGENTS.md` on `make generate`. **This is rejected.** Baking local content into a
git-tracked file makes it possible to accidentally commit personal overlay into
the shared repo, which is unacceptable. Do not build or revive that pipeline.

## Approach: never-committed working-tree edit

- Edit the generated root `AGENTS.md` in the working tree directly, adding a
  short, high-signal note (for example, a pointer to private project memory).
- Never commit that edit. Protect it with:

```bash
git update-index --skip-worktree AGENTS.md
```

- Apply the same protection to any other generated, locally-customized tracked
  files (for example, agent tool configs) that must survive branch switches.

## Recoverable source (required)

`skip-worktree` state is per-clone `.git/index` state, is not shared, and can be
cleared by some git operations. So the working-tree edit is disposable and MUST
be recoverable:

- Store the verbatim overlay text and the list of protected files in committed
  Agents workspace project memory (`projects/<repo>/AGENTS.md` plus a
  `projects/<repo>/artifacts/system/` snippet).
- If the local edit is lost or the flag is cleared, re-apply from that source and
  re-set `skip-worktree`.

## Recovery on branch switch / pull

When switching branches or pulling changes that upstream-regenerated a protected
file (git may report no local change because of `skip-worktree`):

```bash
git update-index --no-skip-worktree AGENTS.md   # unprotect
git checkout <branch> / git pull                 # take latest tracked version
# re-apply the overlay note on top of the latest version (local additions win)
git update-index --skip-worktree AGENTS.md       # re-protect
git ls-files -v AGENTS.md                         # verify (an `S` flag = skip-worktree)
```

Never discard the local overlay silently; always re-apply it on top of the latest
version with local additions taking priority.

## Reference implementation

Keep the verbatim local overlay and protected-file list in the applicable project
memory so a lost working-tree edit can be restored without relying on an older
checkout or external system.
