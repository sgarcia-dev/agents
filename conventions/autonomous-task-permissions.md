---
created_at: 2026-09-30
updated_at: 2026-09-30
model: openai-codex/gpt-6.1-sol
doc_type: convention
purpose: Keep authorized routine tasks and workers non-interactive without expanding their authority.
related:
  - path: ~/agents/AGENTS.md
    why: Always-on authority and cross-provider delegation gate.
  - path: ~/agents/roles/task-worker-tiers.md
    why: Worker scope, depth and tier rules.
  - path: ~/agents/adapters/adapter-contract.md
    why: Each harness owns and verifies its native implementation.
---

# Autonomous Task Permissions

Owner decision, 2026-09-30: routine authorized work should run without sandbox or
permission prompts by default. Do not repeatedly ask for authorization already
contained in the task. This is a permission posture, not permission to choose a
new task, disclose private data, or invoke another provider.

## Immediate adoption

Read this before onboarding, adapter sync or remote/autonomous work. A current
instruction such as "apply this permission policy", "enable these routine
permissions now" or the bootstrap prompt below authorizes this harness to apply
the documented routine defaults to its own root, orchestrator and supported
subagents, without another approval round. Merely finding this file or asking
for an audit does not authorize editing security settings.

Apply this focused permission bootstrap before the rest of an authorized full
onboarding audit; do not delay it behind model interviews, MCP inventories or
worker smoke campaigns. Keep this file canonical; native settings and per-tool
launch syntax belong in that harness's adapter. No new installs/authentication,
model changes, disabled connector enablement or other harness edits are implied.

## Routine work

Preapprove public internet search, fetch, scraping, shell HTTP, and task-scoped
local reads and writes under `~/Downloads`, `~/agents`, `~/agents-workspace`
(the workspace alias), and the separate private repo. Its own guidance still
wins. A directory grant does not authorize deleting unrelated files, executing
untrusted downloads, or copying private material into the shared repository.
Other task-selected checkouts may be authorized by the user's task too.

Use the harness's supported full-access/non-interactive default for root sessions,
explicitly requested cross-provider CLI tasks, and enabled default/high workers.
Use sandboxing only when requested or for concrete high-risk work, not merely
because a task writes a file or runs a shell. Document any managed-policy limit.

Routine command families are preapproved when installed and used for the task:

- Shells/scripts: `bash`, `sh`, `zsh`, `fish`, `env`, task scripts and absolute
  executable paths; pipes, redirects and command composition are covered.
- Languages/runners: `node`, `nodejs`, `python`, `python3`, `uv`, `ruby`, `perl`,
  `bun`, `deno`, `tsx`, `ts-node`, and task-selected installed compilers/runtimes.
- Dependencies/build/tests: `npm`, `npx`, `pnpm`, `yarn`, `pip`, `pip3`, `pipx`,
  `poetry`, `pytest`, `make`, `cmake`, `ninja`, `go`, `cargo`, `rustc`,
  `java`, `javac`, `mvn`, `gradle`, `dotnet`, `ruff`, `eslint`, `prettier`,
  `tsc`, and task-authorized package setup through installed managers such as
  `brew`. Tool availability does not authorize unrelated installs or upgrades.
- Version control: `git` and already-authenticated `gh`; routine status/diff/log,
  clone/fetch/pull, task branches/worktrees, staging/commits, merges/rebases and
  task-authorized push/PR work. Do not change repository visibility, permissions,
  unrelated history or force-push shared branches without specific authority.
- HTTP/data/files: `curl`, `wget`, `jq`, `yq`, `rg`, `grep`, `find`, `ls`, `cat`,
  `head`, `tail`, `sed`, `awk`, `sort`, `uniq`, `wc`, `diff`, `patch`, `tee`,
  `mkdir`, `cp`, `mv`, `touch`, `tar`, `zip`, `unzip`, `gzip`, checksums and
  cleanup of the task's own disposable files. Preserve unrelated data.
- Authorized bridges: `codex`, `claude`, `opencode`, `hermes` and other explicitly
  requested installed harness CLIs. Command access is not delegation consent.

These are examples, not a closed list or a grant for every argument. Each
harness may still require dedicated file/search tools instead of shell equivalents.

Node.js is the runtime normally invoked as `node`; do not create a `node.js`
command or install another interpreter merely to whitelist it. Broad supported
shell access covers installed interpreters, package runners and task scripts,
including absolute executable paths; it is not restricted to these examples.
Avoid a growing command-by-command list when a supported non-interactive mode covers
routine work. Interpreter or shell allow rules grant arbitrary execution; they
are not path confinement, and must never be advertised as such. Command access
does not authorize an unrequested cross-provider handoff.

## Delegation and workers

Cross-provider delegation requires an explicit user request naming the target or
approving the chain. Skill discovery, a failed tool, or cheaper pricing is not
consent. This applies to all task bridges and every nested caller. Ordinary
native worker delegation follows the worker-tier policy; it does not require a
fresh user approval for each in-scope packet once the root task authorizes it.

Preserve explicit models, bounded packets, worker counts, disabled fast tiers,
and terminal leaves. Full technical access does not change role scope:
`task-explore` and `task-explore-high` may read sources and create new reports
only in their assigned output directory. Execute workers change only their
packet's allowed paths. Do not grant recursive delegation to remove prompts.
Use compatible native controls when they do not block required reporting,
network, or routine checks. When technical confinement is unavailable under full
access, record that scope is prompt-enforced and checked by the root, not sandbox
-enforced. Do not claim a technical read-only guarantee that was removed.

## Orchestrator access

`task-orchestrator` receives the same broad access as roots, or the least
restrictive posture its native subagent interface supports. Do not impose a
special shell deny, interpreter allowlist or routine ask rules on it. Routine
scripts, HTTP, assigned artifacts and already enabled MCP tools must not require
another permission round. Preserve managed-policy and platform limits; never
promise that external restrictions cannot block a call.

Keep exactly one child layer below the orchestrator: only tier-enabled named
explore/execute leaves, no generic agents, peer/nested orchestrators or provider
CLI handoffs. Leaves remain terminal. Broader command access must not remove
supported child-name/depth controls. Document any boundary that is behavioral
rather than technically enforced; do not substitute a generic agent for a mapped
orchestrator. Existing models, disabled fast tiers, task scope, account-side-effect
authority and parent-owned final Git acceptance remain unchanged.

## MCP and connected tools

Preapprove task-scoped use of already configured and enabled MCP tools, including
public research connectors. Remove obsolete ask rules that stall routine work;
retain deliberate denies for excluded actions. Permission approval is separate
from connector installation, on/off posture, authentication, funding, and tool
selection. Do not install or enable a disabled connector, change OAuth grants,
remove cost caps, or activate a signed-in browser merely to make it prompt-free.
Existing connector choices and budgets remain in force.

An account connector may expose send/share/delete/admin tools. Research permission
does not authorize these actions. Preserve exact tool/action controls where
supported, and document limits rather than claiming broad MCP trust prevents
external side effects. Never copy credentials into prompts, reports or commits.

## High-risk boundary

Stop for genuinely missing authority before destructive or unrelated deletion,
credential export, unrequested sending/sharing/publishing, billing or account
administration, privilege escalation, security-control changes, or operating-system
and system-owned file changes. A current explicit instruction to apply this
policy authorizes only its described permission changes. Merely loading this
file is not a standing grant for unrelated security changes. Do not fabricate answers to missing scope questions.

Sandbox high-risk work when supported, or keep it blocked pending a concrete
user instruction. Do not disable macOS privacy controls, managed enterprise
policy, provider limits, authentication, or secret-handoff safeguards.

## Adapter implementation and all-access flags

Each harness must document a **Permissions and unattended execution** section:

- Persistent default settings and their exact location/scope; project overrides,
  required reload/new session and any user-only onboarding toggle.
- Root, normal orchestrator and every enabled leaf's effective access/tool
  inheritance; disabled tiers stay disabled. Available MCP tools and approval
  mode are separate: a tool allowlist must not silently exclude enabled MCP.
- Exact supported approval/bypass and sandbox controls, with a copyable remote/
  headless launch example. Record whether each flag removes asks, sandboxing,
  explicit denies, or none of those; never infer meaning from a "YOLO" label.
- Native child-name/depth controls, terminal leaves, and any instruction-only
  boundary. Account/tool exceptions and platform/managed-policy limits remain
  explicit. Missing support is reported, not replaced by a generic agent.
- Configured/static-checked/live-tested status, using evidence already available.

Known launch controls from the existing mappings, not universal flag names:

- Codex: `--yolo` / `--dangerously-bypass-approvals-and-sandbox`;
  persistent `approval_policy = "never"`, `sandbox_mode = "danger-full-access"`.
- Claude Code: `--dangerously-skip-permissions`; persistent
  `defaultMode: bypassPermissions` and supported role `permissionMode` settings.
  Retained exact ask rules are not automatically approved by bypass.
- OpenCode V2: `--auto` preapproves asks, **not explicit denies**. Use supported
  persistent permission rules too; a command-line flag alone does not repair a
  denied orchestrator tool. CLI override/server scope belongs in its adapter.
- Other/new harnesses, including Anti-gravity: inspect only that harness's
  existing controls/help. Record actual supported syntax or "unsupported";
  never invent a `YOLO` / "dangerously allow all" flag. If a human must flip a
  UI setting, name that one action and what remains pending.

Use the strongest supported all-access launch mode for an explicitly authorized
unattended task that needs it. It does not authorize new task scope, private-data
export, recursion, provider handoffs or removal of OS/managed safeguards. A remote
job must not silently sit on an approval form: resolve setup before launch or
return the exact unavoidable blocker. Do not promise prompts can never recur.

## Apply, bounded checks and recovery

For a permission-only apply, inspect only the relevant own-harness controls,
privately back up edited files, preserve unrelated settings, apply supported
persistent rules and read back the changed keys with a syntax check. Target one
short pass, at most two minutes per harness; stop and report a concrete blocker
rather than starting an unbounded audit or retry loop. The complete adapter audit
remains separate. Record models and child limits without launching workers merely
to inspect them. Use own-harness private backups, not an unread private repository.

No live tests by default for a permission-only update. If the user requests them,
agree a small finite test budget first; use a fresh session without temporary
bypass masking saved defaults. One harmless file/shell/HTTP or enabled public MCP
check may establish the specific behavior being claimed. Never test by sending,
sharing, deleting account content or touching OS files. Saved config is not proof
of runtime inheritance; label untested behavior honestly.

Retain session IDs, exact commands, logs and a finite timeout. A permission denial
is failure evidence even if the CLI exits zero. Resume the same session after a
bounded repair where supported; avoid repeated blind restarts. Report configured,
live-tested, unsupported, and still-blocked states separately. A future version
or project override may need reconciliation; do not promise that prompts are
impossible forever.

## Copyable onboarding / permission-only prompt

> Read `~/agents/AGENTS.md` and
> `~/agents/conventions/autonomous-task-permissions.md`. Apply this permission
> policy now to your own harness's persistent root, orchestrator and enabled
> subagent settings before routine work. Preapprove the documented paths,
> command families, Git, HTTP and enabled MCP tools. Preserve task/account
> authority, disabled tiers and exactly one terminal-leaf layer below the
> orchestrator. Do not ask again for already-authorized routine access. Back up
> only edited settings, do a short syntax/readback check, and document your
> exact unattended/all-access flags, inheritance, reload needs and unavoidable
> limits in your adapter. No live smoke campaign, installs, connector enablement
> or model changes. Stop with a specific blocker if a human-only switch is needed.
