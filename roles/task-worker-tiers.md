---
created_at: 2026-07-06
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: role
purpose: Define portable regular and high worker selection, sizing, trust, runtime, and handoff rules.
related:
  - path: ./task-explore.md
    why: Base read-only worker role.
  - path: ./task-explore-high.md
    why: High-capability read-only overlay.
  - path: ./task-execute.md
    why: Base bounded mutation worker role.
  - path: ./task-execute-high.md
    why: High-capability mutation overlay.
  - path: ../adapters/adapter-contract.md
    why: Per-tool model and effort resolution.
  - path: ../ai-models/delegation-briefing.md
    why: Which model each tier runs per tool, its labels, and worker counts by cost.
---

# Task Worker Tiers

This file says which tiers exist and the rules that hold in every tool. It names no models and does not say how capable a tier is, because that depends on the tool.

**The tier names only hint at capability.** "Regular" means the cheaper model in this tool and "high" the stronger one. In one tool regular is a weak model you run by the dozen and never let edit; in another it is a capable model that costs real quota. Do not assume from the name. **Before every dispatch, read your tool's section of `~/agents/ai-models/delegation-briefing.md` (section 3).** It is the scorecard for the tool you are in: which model each tier runs, how it compares with the root model you are probably running, what each tier may and may not take, when to move up, and how many to run. Workers are supervised, terminal, non-recursive helpers. The root keeps architecture, decisions, integration, final verification, and durable truth.

The point of delegation is affordable parallelism and root-context economy. The root is an architect, not a rubber stamp: it examines suspicious worker claims and validates every result. A stronger worker buys bounded reasoning, not project ownership.

## Availability

| Wrapper | Status | Appropriate work |
|---|---|---|
| `task-explore` | enabled | One narrow read-only question you can check. How narrow: your tool's section of the briefing. |
| `task-execute` | enabled | One narrow edit or check with a clear pass or fail. How narrow: same. |
| `task-explore-high` | enabled | Bounded investigation or review. |
| `task-execute-high` | enabled | Bounded implementation or verification. |
| `task-explore-fast` | disabled | Do not launch. |
| `task-execute-fast` | disabled | Do not launch. |
| `task-orchestrator` | enabled where explicitly mapped and verified | One bounded phase or queue, with terminal leaf workers only. |
| `task-orchestrator-fast` | disabled | Do not launch. |

An adapter may mark an enabled wrapper **unsupported-with-reason** if its runtime cannot select an explicit model and preserve the role's permissions. That is not permission to substitute a generic or inherited-model agent. If the chosen tier is unavailable, keep the work in the root or use a different capable tool with its own verified adapter, not a silent downgrade.

## Pick the Cheapest Capable Worker

**First ask whether the packet is truly trivial.** Do it inline if dispatch costs more than the work. Otherwise prefer `task-explore` or `task-execute` when the packet is independent and you can check the result. Your tool's section of the briefing says what its regular model can safely take ("Regular takes" and "Never give regular"). Split independent work into separate packets; never split tightly coupled work just to fit a cheaper worker.

**Use `task-explore-high` or `task-execute-high` when the briefing's "Move up to high when" line applies**, or when the regular model in your tool cannot safely do the job. High is a stronger worker, not the root. A high worker gets a finite source list, explicit objective, stop condition, deadline, and one exclusive edit or report target. High is still bounded and supervised: broad project ownership, open-ended discovery, architecture, final integration, acceptance, and irreversible decisions stay with the root. If a task does not fit either tier, keep it in the root or redesign the work.

Do not use a high worker just because it exists. Do not force a regular worker onto a job its model cannot do just because it is cheaper. Price matters only after the model can do the job and you can check it. The root checks every important claim against sources, diffs or independent checks, and checks harder when the briefing labels the model high guessing. When a job fits neither tier, follow the briefing's "Give back to the root when" line.

## Size and Runtime

Size a packet before launch using the number of files/documents, expected input and output, tool calls, and open questions. Watch for a small-looking objective hiding a long workflow. A regular packet should target at most 40% of its model's context and stay below 50%; if context size is unknown, target at most 50,000 characters of *total working material* and treat 75,000 as a hard ceiling. Some models have a lower practical limit (price or recall drops past a size); the briefing names it. Stop or split when any limit is exceeded.

High still stays below 50% of its advertised context, with bounded source and action budgets. Do not hand high an entire repository. Require a richer handoff to preserve the reasoning it did within the packet.

A regular run should finish quickly. At about three minutes, investigate; at four minutes, cancel where possible unless a known external wait was declared. Double these for a model the delegation briefing labels slow. Treat an unexplained overrun as suspect and re-scope or perform the work in the root. High workers also need a finite deadline, and an overrun is failure evidence, not proof of care.

## Concurrency and Authority

Sequential is the default. Dispatch independent packets only, review the round,
then decide if another is worthwhile. When the user has not specified counts,
each dispatching root/phase session or enabled task-orchestrator uses two separate
concurrent pools:

- **Default workers** (`task-explore` and `task-execute` combined).
- **High workers** (`task-explore-high` and `task-execute-high` combined).

**How many per pool depends on the model, not the tier name.** Take the cost,
guessing, speed and quota labels of the model that pool runs on in your harness
from the delegation briefing, and use its count table: roughly 3-8 for cheap
models, 2-4 for mid, 1-3 for premium, lowered by quota caps. High guessing
limits what packets a model may get, not only how many. Zero is fine when no
worker is needed. The ceilings there are for exceptionally hard tasks or when
the user asks for the maximum, not ordinary targets.

When a tool's adapter maps only one pool, that pool's count is the whole
default for that tool.

These are separate pools: a demanding task can use both at once, each within its
own model-based count. These counts are guidance, not quotas or a native enforcement mechanism. Count both
explore and execute within their respective tier; do not multiply a pool by role
name. Each orchestrator gets an explicit leaf budget from its root. The root
counts direct and orchestrator-launched workers together; orchestration is not a
way to fan out without judgment. Different top-level sessions do not share an
Agents workspace counter. A stricter runtime or provider limit still wins.
Adapters must not turn these counts into native per-session or
global caps, so that a user request for more workers can always be honored.

An explicit user instruction for the number of agents in a session overrides
these suggested counts, including a higher count or a specified mix of default
and high workers. Follow that instruction without treating the guidance as a
hard cap; if the requested number is impossible or unsafe for the actual
independent packets, explain the concrete blocker. An override of counts does
not enable disabled roles, grant permissions, permit recursive leaves, or waive
packet scope and verification. Never fill either pool just to reach a number
when the user has not requested it. Workers never spawn, call, or coordinate
other workers. A root must not substitute a native/generic agent or let a worker
silently inherit the root model.

### CLI-launched child sessions (added 2026-09-28)

A session started through another harness's CLI (for example `task-opencode`,
`task-claude`, or `task-codex`) is a full harness that can start its own
subagents. Treat it as a worker, and count its subagents in the caller's budget.
Ten CLI children that each start ten subagents is a hundred agents.

- **Default: no subagents.** Launch every CLI child with subagents blocked and
  say so in its packet. Always block them when the child is one of several
  parallel children.
- **Allow subagents only when** the user explicitly asks or approves it, or the
  child is told to run a skill that needs delegation (`research`,
  `research-deep`, `plan-create`, `plan-execute`, `plan-reconcile`). Usually that
  means one or two children, not a fan-out.
- **When allowed, set a budget.** State in the packet that subagents are allowed,
  why, and the maximum count (default: that harness's normal worker range). The
  caller counts those subagents toward its own total.
- A CLI child never launches further CLI children (`task-opencode`,
  `task-claude`, or `task-codex`) unless the user explicitly asked for that chain.
- Blocking must be technical where the harness supports it, not just a sentence
  in the prompt. Each bridge guide lists the exact flag.

`task-explore` and `task-explore-high` are source-read-only except for new Markdown reports in their one assigned exclusive output directory. `task-execute` and `task-execute-high` mutate only the explicit packet scope. High grants reasoning capacity, not extra permissions or decision authority. Explicit user-invoked RoleDispatch may use any verified model on an enabled maintained wrapper while preserving its role and permissions; it does not change standing tier mappings.

Model choices, effort values and fallback policy live only in the delegation briefing. Each tool's adapter records how they are wired and whether they were live-checked, not a second copy of the choice. A portable role may hint the capability tier but never name a provider model. A `task-orchestrator` runs one step above its harness's high workers, never on the most expensive setting. An unavailable exact model or reasoning setting must be reported, not silently replaced.

## Non-Interactive Permission Posture

Apply `~/agents/conventions/autonomous-task-permissions.md` to both
root and enabled default/high workers. Routine file reporting, scoped execution,
public research, shell HTTP and already enabled MCP calls must not wait for user
permission. Native full-access defaults do not extend the role's write scope or
permit recursive leaves. Preserve explore's source-read-only/create-only-report
contract in prompts and root verification; record whether native controls enforce
it or the boundary is prompt-enforced. Do not claim sandbox confinement under a
full-access launch. Concrete high-risk work remains a separate approval boundary.

## High-Tier Handoff

In addition to its base role's report, high returns:

- the outcome against each acceptance criterion, with exact changed paths or source locations;
- important cross-source reasoning, contrary evidence, and rejected approaches;
- observed facts separated from inferences, assumptions, and unresolved questions;
- decisions within the packet, verification run and results, gaps and risks;
- the smallest continuation steps and what remains reserved for the root.

Account for assigned sources, including material omissions or unavailable items.
Record what would disprove the conclusion and enough exact paths or commands to
resume without repeating the investigation. Do not invent a numerical confidence
score from runtime. Include the consequences of any material packet-level decision.

Be selective. Do not paste raw transcripts or hide the conclusion in a long report. The root still checks the result before accepting it.

## Adapter Requirements

Each maintained adapter resolves all six `{task-explore, task-execute} x {default, fast, high}` cells explicitly as enabled with model/settings, disabled, or unsupported-with-reason. The high cells are enabled by this policy; each tool must verify its own mapping in its own `sync-tool-adapter` session. An unsupported high cell is honest; an old 'disabled' cell is stale. The fast cells and fast orchestrator remain disabled. The normal orchestrator requires an explicit model, native child allowlist, and verified delegation depth in each tool's own adapter; other tools must not infer support from this policy. No enabled cell may inherit the root model. Do not launch an unverified mapping or treat a mapping doc as proof of native execution.
