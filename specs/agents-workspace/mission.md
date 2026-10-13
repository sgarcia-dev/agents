---
created_at: 2026-07-07
updated_at: 2026-08-25
model: claude-opus-4.8
doc_type: spec
purpose: Define the founding thesis of the Agents workspace - durable theory of the work plus a tool-agnostic operating contract - and the governing corollary that tools converge to the system and every divergence is reconciled, never silently absorbed.
related:
  - path: ../../AGENTS.md
    why: Kernel Purpose block is the short form of this spec.
  - path: ../../adapters/adapter-contract.md
    why: Reconciliation rules that operationalize the "workspace never bends to a tool" corollary.
  - path: ../../adapters/AGENTS.md
    why: Adapter-layer ownership and cross-tool discovery rules that keep tools thin.
  - path: ../../roles/task-worker-tiers.md
    why: Portable role/tier semantics that adapters resolve, an instance of tools converging to the system.
---

# Agents Workspace Mission

The durable purpose of this workspace. The kernel `AGENTS.md` Purpose block is the
short always-on form; this spec is the full grounding and the source that
reconciliation rules point back to.

## Thesis: one defense against two forms of the same loss

The workspace exists to defeat knowledge loss at a boundary. That loss shows up in
two guises that are really one problem, so they are solved as one thesis, not two
separate goals.

### 1. Theory loss at a session boundary (Naur)

Peter Naur's "Programming as Theory Building" (1985) argues that programming is
the construction of a *theory* in the minds of the people doing the work, not the
production of program text. In Naur's sense a theory is the operational grasp of
three things and the mapping between them:

1. the application domain / world — what matters and what counts as success;
2. the program — what the code actually does; and
3. the mapping — why the program is shaped this way, which tradeoffs were
   accepted, and what would have to change if the world changed.

The theory is what lets someone explain behavior in terms of intent, answer novel
questions without re-deriving everything, and extend or repair the system
coherently. Naur's sharp claim: the program text (code plus docs) is **not** the
theory. It is a lossy residue of the theory-building activity. Documentation is a
selective projection; it cannot capture tacit judgment, rejected alternatives, or
the "feel" for what a correct change looks like. When the theory-holders leave, the
system suffers "program death": it still runs, but it can no longer be coherently
evolved, because the living connection between intent and code is gone. Successors
must reconstruct a theory from artifacts — and risk building a plausible but wrong
one.

An LLM agent session is structurally the post-departure successor, with a steeper
handicap: **every fresh session begins with zero theory.** It has only the text
that fits in context. The codebase under-determines the theory in exactly Naur's
sense. So each session risks either expensive theory rebuilding from scratch or
confident action on a wrongly reconstructed theory. This reframes the real
bottleneck in AI-assisted work: not code generation, but **the persistence and
continuity of the theory of the system.** Faster code without durable theory only
accelerates theory drift.

The workspace's first job is therefore to externalize and durably maintain that
theory — decisions, rationale, state, rejected paths, and the intent↔code map — so
it outlives every session boundary and long tasks resume instead of restarting.
(Related: Ryle's knowing-how vs knowing-that, which Naur draws on; tacit vs
explicit knowledge; context rot / cold-start in agent sessions.)

### 2. Knowledge loss at a tool boundary (churn)

AI coding tooling turns over on a quarterly cadence: IDEs, models, and agent
paradigms all change independently and fast. Coupling a workflow tightly to one
tool imposes recurring costs — re-onboarding, proprietary lock-in of rules and
memory, config/prompt rewrites when features diverge, loss of accumulated tuning
when a product is deprecated, and the risk of betting your operating system on a
vendor's survival.

The inversion insight: the durable asset is the practitioner's **system** — the
instructions, decisions, standards, procedures, and accumulated project knowledge
— not any particular tool. So the winning move is to make tools onboard *to the
system* rather than re-onboarding the human to each tool. Tool-native knowledge
resets on every switch; system-native knowledge compounds. This is an application
of older durable ideas: plain text plus git longevity, vendor neutrality,
"own your data / own your knowledge base," and separating policy (what to do) from
mechanism (which runtime does it).

The workspace's second job is therefore to be the tool-agnostic operating
contract, kept in a neutral, plain-text, human-owned home, so accumulated
knowledge and standards are never held hostage to a single vendor's lifecycle.

### Why they are one thesis

Both guises are the same failure: knowledge evaporating at a boundary — a session
boundary or a vendor's end-of-life. A durable theory that only lived inside one
tool's proprietary memory would still die when that tool did; a tool-agnostic
contract with no persisted theory would still force every session to start blind.
The workspace must own both to defeat either.

## Repository boundary: shared core and private companion

The operating system spans two Git repositories with a one-way dependency:

- The coworker-visible workspace at `~/agents` owns shared conventions, skills,
  roles, workflows, and engineering memory.
- A separate access-controlled private repo owns sensitive personal,
  personnel, compensation, private-note, and credential-bearing memory.

The private companion may use and link to the shared operating contract. The
shared workspace may identify the companion root but must not depend on, list, or
summarize its internal content. Moving private content into the shared repository
requires explicit user approval and a fresh redaction review.

## Governing corollary: tools converge to the system

**Tools converge to this system; the system never bends to a tool.** Each runtime
is a thin, replaceable adapter over this source of truth. Native tool config
(rules, subagents, MCP servers, permissions, model choices) is an implementation
detail, never canonical.

The operational consequence, which the adapter contract and the sync-tool-adapter
workflow enforce:

- Every difference between a tool and this workspace is **surfaced and
  reconciled**, in both directions, and nothing is dropped silently.
- Anything a tool supports that the workspace does not is either **promoted** into
  the workspace or **recorded as an approved divergence**. There is no silent
  "noticed and moved on" state.
- Approved divergences are **re-surfaced on every run**, annotated as
  user-approved and expected — acknowledged, never silenced — so the system stays
  continuously aware of every place a tool differs from it.

## Requirements

### Requirement: The founding thesis is durable, not artifact-only

The two-losses thesis and its grounding MUST live in always-on or durable memory
(the kernel Purpose block plus this spec), not only in `artifacts/`, which the
workspace treats as non-current by default.

#### Scenario: An agent orients to the workspace

- **WHEN** an agent reads the kernel `AGENTS.md`
- **THEN** it MUST encounter the Purpose block stating the single thesis and the
  governing corollary, with a pointer to this spec for full grounding.

### Requirement: The workspace never bends to a tool

Native tool configuration MUST NOT become the source of truth, and every
tool/workspace difference MUST be reconciled rather than silently absorbed.

#### Scenario: A tool supports something the workspace does not

- **WHEN** adapter reconciliation finds a capability, skill, role, tier, or
  connector a tool has but the workspace lacks
- **THEN** it MUST be promoted to the workspace or recorded as an approved
  divergence, and approved divergences MUST be re-surfaced on subsequent runs
  rather than silenced.

### Requirement: The shared repository remains safe for coworker visibility

Sensitive personal, personnel, compensation, private-note, and credential-bearing
material MUST live in the access-controlled companion, not the shared repository.

#### Scenario: An agent encounters sensitive durable memory

- **WHEN** an agent needs to create or update sensitive durable memory
- **THEN** it MUST work in the private repo, follow that repository's root
  guidance, and keep shared references generic.
