---
name: role-dispatch
description: Launch an adapter-maintained role for one bounded run with an explicit model, reasoning level, and service class. Use when the user requests a custom model for a role, headless or inline role execution, or several independently monitored role runs.
created_at: 2026-08-17
updated_at: 2026-09-25
model: gpt-5.6-sol
doc_type: skill
purpose: Define portable one-run role-profile dispatch while preserving role and permission boundaries.
related:
  - path: ../../adapters/adapter-contract.md
    why: Defines the required per-tool one-run role mapping and verification contract.
  - path: ../../roles/task-worker-tiers.md
    why: Defines task-role availability, packet limits, and concurrency limits.
---

# Role Dispatch

Use the active tool's adapter mapping to launch one canonical role with an
explicit, one-run runtime profile. The profile may select a model, reasoning
level, service class, and adapter-required launch mode. It must not change the
role's behavior, prompt source, permissions, sandbox, authority, delegation
boundary, or stop conditions.

Before selecting any task role, read `../../roles/task-worker-tiers.md`. It is the
sole authority for availability and limits. Reject a disabled role or wrapper,
including any one-run profile, instead of launching it with a custom model.

## Required Inputs

Resolve these before launch:

- one adapter-maintained role and one bounded packet;
- the exact tool-local model identifier, reasoning level, and service class;
- an absolute working directory and expected repository identity when the task is
  checkout-bound;
- interaction mode, allowed actions, forbidden actions, completion boundary, and
  verification bar;
- a unique run ID, output or handoff destination, timeout, attempt limit, and
  parent return shape;
- concurrency limit and a written independence decision when more than one run is
  requested.

Do not inherit the parent model, guess an unavailable model name, or silently
substitute another profile. If the active adapter lacks a verified mapping for the
requested role or setting, report it unsupported and stop.

RoleDispatch is the explicit user-controlled exception to the normal non-frontier
worker model default. It may select any exact, verified harness model for any
maintained role, including `task-explore` and `task-execute`. It must still use the
maintained wrapper, preserve its permissions and behavior, and name the model
explicitly; inherited models and generic-agent fallback remain prohibited. A
one-run choice does not change the adapter's standing default, fast, or high tier
models.

## Adapter Resolution

Read only the active tool's mapping. Never inspect or edit another tool's native
configuration to complete a dispatch.

Fail closed if that mapping does not name the selectable maintained roles, exact
model-discovery and launch commands, a dated user-selected favorite model subset,
reasoning controls, standard and fast/priority service controls, capture and
cancellation commands, and verification status. Do not research these from
scratch during a dispatch; `sync-tool-adapter` owns collecting them with the user.

The adapter mapping must state whether the tool supports native per-dispatch
overrides, a headless or inline process, a temporary native profile, or no safe
mechanism. Follow its exact launch and verification recipe. An adapter-required
temporary mode change may make a role directly launchable, but it grants no new
tools or authority.

Apply the narrowest runtime override possible. Preserve the maintained role
wrapper and change only fields the mapping names for one-run profile selection.
Never use an auto-approval flag to bypass asks or denials.

## Root Ownership

The user-facing root owns launch, monitoring, cancellation, result inspection,
retry decisions, acceptance, and cleanup. A launched role does not become a peer
root and may not coordinate other top-level runs.

For every run:

1. Validate the role, profile, working directory, repository identity, packet,
   output path, and permission boundary.
2. Preflight the effective role before any model call. Verify its canonical prompt
   source, launch mode, permissions, sandbox/approval posture, child allowlist,
   delegation depth, and stop boundary. A mismatch is a launch rejection.
3. For a mutating role, capture the checkout's pre-run branch, status, and relevant
   diff so interrupted work can be classified.
4. Launch in the foreground through a process runner that enforces a finite
   deadline and can terminate and reap the whole process group. Assign a unique
   title or run identifier.
5. Capture structured events and stderr separately in unique restricted storage
   outside Git when the tool supports it.
6. Require a clean process exit, a terminal completion event, and the role's
   required durable output or final response.
7. Verify the actual role, model, reasoning variant, service class when exposed,
   working directory, repository identity, session identity, canonical prompt,
   permissions, child allowlist, and delegation depth against the request.
8. Inspect outputs, relevant diffs, mutation state, and verification evidence
   before acceptance.
9. Record failure without automatic retry when identity, permissions, structured
   output, cleanup, completion, or mutation state is uncertain.

A zero exit status or plausible final paragraph alone is not proof of success.
Classify launch rejection, identity mismatch, timeout, cancellation, nonzero exit,
malformed or incomplete event output, permission failure, output collision, child
failure, and unknown mutation state distinctly.

## Concurrency

Sequential is the default. The root may launch several role runs concurrently
only after it proves they are independent and gives each a unique run ID and
output destination.

- Read-only runs may share a checkout only when their outputs do not collide.
- Mutating runs must not share a checkout, branch, file set, runtime, or durable
  output. Use separately validated checkouts or run them sequentially.
- Do not retry a timed-out or interrupted mutation until the root inspects its
  checkout against the pre-run snapshot and classifies the resulting state.
- Use the active adapter's supported process-monitoring mechanism. Do not leave
  orphaned processes or hidden sessions waiting for user input. If the harness
  cannot enforce a deadline and confirm process cleanup, unattended mutating role
  dispatch is unsupported.

## Orchestrator Profiles

`task-orchestrator` may be selected only where the active adapter verifies its
explicit model, permissions, child allowlist, and delegation depth.
`task-orchestrator-fast` remains disabled. A one-run profile must preserve the
orchestrator's child budget and all role boundaries.

## Final Receipt

Return the run ID, role, requested and verified profile, status, canonical output
or handoff path, verification summary, any mutation state, and exactly one next
root action when work remains.
