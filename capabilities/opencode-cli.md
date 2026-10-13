---
created_at: 2026-09-28
updated_at: 2026-09-29
model: openai/gpt-6-sol
doc_type: capability
purpose: Compatibility pointer to the maintained OpenCode V2 CLI bridge reference.
related:
  - path: ./connectors.md
    why: Portable awareness inventory of external bridges.
  - path: ../skills/task-opencode/SKILL.md
    why: Reusable procedure for non-OpenCode callers.
  - path: ./opencode/STATE.md
    why: Current entry point for the maintained OpenCode capability folder.
---

# OpenCode CLI bridge

The maintained reference now lives in the OpenCode capability folder:

- [Current status](opencode/STATE.md)
- [CLI, models, costs, permissions, and verified behavior](opencode/cli.md)
- [Capture, monitoring, questions, resuming, and cancellation](opencode/sessions.md)
- [The caller's procedure](../skills/task-opencode/SKILL.md)

This file is retained so older links resolve. The 2026-09-28 artifact is dated
test evidence, not the live reference: its subagent override uses obsolete V1
permission syntax. Do not copy that example into a V2 run.
