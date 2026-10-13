---
created_at: 2026-09-29
updated_at: 2026-09-29
model: anthropic/claude-opus-5-5
doc_type: guide
purpose: Tells agents which search and fetch provider to use (Parallel, Exa, Firecrawl), when to escalate, how to explain it, what each costs, and the signs that a tool is the wrong one.
related:
  - path: ~/agents/specs/internet-deep-research/spec.md
    why: Owning spec and entrypoint.
  - path: ~/agents/capabilities/web/tools/parallel.md
    why: How the three providers are connected and gated in each harness.
  - path: ~/agents/capabilities/web/README.md
    why: Design background, the ~$15 plan, and the bakeoff.
  - path: ~/agents/capabilities/mcp/parallel.md
    why: Parallel tools, costs, and quirks in full.
  - path: ~/agents/capabilities/mcp/exa.md
    why: Exa tools, costs, and quirks in full.
  - path: ~/agents/capabilities/mcp/firecrawl.md
    why: Firecrawl tools, costs, and quirks in full.
---

# Provider usage for agents

Moved to: [README.md](../../capabilities/web/README.md).

2026-10-01: Web facts and routing moved to the shared capability home after checking destination coverage. This file is a compatibility pointer. Its older instructions are superseded.

Read [README.md](../../capabilities/web/README.md), [DECISIONS.md](../../capabilities/web/DECISIONS.md).
