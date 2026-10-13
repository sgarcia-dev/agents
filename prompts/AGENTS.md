# Prompts

Use this folder for reusable prompt text that does not have a stronger home.
Canonical reusable procedures belong in `../skills/`; canonical reusable
specialist behavior belongs in `../roles/`.

## Belongs Here

- Human-invoked prompt snippets.
- Reusable prompt text that is not a full skill, role, workflow, adapter, or
  capability description.
- Legacy prompts kept for historical readability.

## Does Not Belong Here

- Repo-specific operating rules.
- Tool-specific agent frontmatter or permission config.
- Canonical role behavior. Use `../roles/`.
- Canonical workflow procedures. Use `../skills/`.
- Long implementation plans for one feature.

## Current Guidance

Keep this folder small. Do not recreate retired workflow-local skill or subagent
prompt trees here. Use `../skills/` for reusable procedures and `../roles/` for
portable specialist behavior.
