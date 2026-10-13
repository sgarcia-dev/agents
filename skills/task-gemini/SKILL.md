---
name: task-gemini
description: Use from a harness other than Gemini when the user wants to delegate a bounded task to Gemini / Antigravity CLI (agy) for fast Google model execution, structured output, or multimodal reasoning. Do not use from inside Gemini or silently delegate ordinary work.
created_at: 2026-09-30
updated_at: 2026-10-07
model: gemini-3.8-flash
doc_type: skill
purpose: Safely dispatch and supervise one bounded Gemini CLI task from another harness.
metadata:
  opencode/autoinvoke: false
related:
  - path: ~/agents/capabilities/gemini-cli.md
    why: Full capability reference with exact flags, models, outputs, and verified limits.
---

# Task Gemini

**Explicit user request only.** Loading this skill never authorizes an unprompted handoff. Read [`autonomous-task-permissions.md`](../../conventions/autonomous-task-permissions.md) for owner-approved non-interactive defaults, routine roots, and high-risk exceptions. Preserve bounded packet limits and non-recursive child depth.

Use this procedure only from a harness other than Gemini (such as Claude Code, Codex, OpenCode, or Hermes). Inside Gemini, use native tools and subagents instead.

The underlying reference with all command flags and test facts lives in [`capabilities/gemini-cli.md`](../../capabilities/gemini-cli.md). Read it before first use.

## Procedure

1. **Verify delegation is appropriate:** Use Gemini for tasks that benefit from fast token throughput, strong multimodal understanding, Google ecosystem search, or low-cost execution. Send heavy Anthropic reasoning to Claude Code or specialized coding tasks to OpenCode/Codex when appropriate.
2. **Confirm binary and working folder:** Ensure `~/.local/bin/agy` is reachable. Always execute from the folder containing the project files the task concerns. Check `git status --short` before mutating runs.
3. **Draft a self-contained packet:** State the exact goal, allowed paths, forbidden paths, required output shape, verification checks, and an explicit stop condition. Ask the child to print `PROGRESS n/total` (for example `PROGRESS 2/5`) as it finishes each step; the agent-watch Claude Code mod reads it to show progress and time left. The child CLI starts a new session and does not inherit the caller conversation.
4. **Pin model and effort explicitly.** Read [`delegation-briefing.md`](../../ai-models/delegation-briefing.md) first: section 4 for the
   Gemini default and step-up, section 5 for the Gemini card (which models are
   banned and why). Do not choose from memory. Flag form:
   `--model <id>-<effort> --effort <effort>` (for example
   `--model gemini-3.8-flash-medium --effort medium`). If you step up, say so in
   the report. Never omit the model flag or allow an unpinned default.
5. **Set non-interactive permissions:** In print mode (`-p`), tool permission prompts cannot be answered interactively. Include `--dangerously-skip-permissions` for authorized routine work. Scope is strictly governed by the packet prompt and allowed files, not by permission prompts.
6. **Block recursive delegation:** Tell the child prompt explicitly: "This is a single bounded worker run. Do not spawn subagents or delegate to other tools."
7. **Execute and capture structured output:**
   For web search and page reading, read [the Gemini web capability](../../capabilities/web/tools/gemini.md). Name native tools, allowed providers and no further hand-offs in the packet. Load web-search only if explicitly requested or named in the packet. Use `--output-format stream-json` and check actual tool events.
   Use final JSON for a simple result, or `--output-format stream-json` when
   live tool/model-step inspection or benchmarking is requested. Follow the
   capability's [telemetry and acceptance notes](../../capabilities/gemini-cli.md#telemetry-and-task-acceptance).
   Measure wall time independently. The simple-result invocation is:

   ```sh
   agy -p '<packet_prompt>' \
     --model gemini-3.8-flash-medium \
     --effort medium \
     --dangerously-skip-permissions \
     --output-format json \
     < /dev/null > "$RUN_LOG" 2> "$RUN_ERR"
   ```

8. **Parse results and inspect verification:**
   - Check process exit code.
   - Parse `status` from JSON (`SUCCESS` expected).
   - Extract `conversation_id` for inspection or follow-up turns.
   - Inspect failed tool steps even when the final status is `SUCCESS`. If an
     authorized task requires a child, verify it actually launched and completed;
     the October 5 test failed to launch `task-explore`. Do not rely on that
     local mapping until a Gemini-owned retest succeeds.
   - Verify file modifications and run required tests. A zero exit code alone is not acceptance.
9. **Handle questions or follow-up:** If the model returns an open question rather than a result, report it back to the user or caller root. To resume with the user's answer, run:

   ```sh
   agy -p '<answer>' \
     --conversation <conversation_id> \
     --dangerously-skip-permissions \
     --output-format json \
     < /dev/null
   ```

Report the exact model, reasoning effort, session ID, execution duration, changed files, and verified test results to the calling session.
