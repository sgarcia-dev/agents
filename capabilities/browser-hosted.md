---
created_at: 2026-09-29
updated_at: 2026-09-29
model: openai-codex/gpt-6-sol
doc_type: capability
purpose: Compare hosted browsers and self-hosted browser services without assuming login portability.
related:
  - path: ./connectors.md
    why: Bridge registry and posture.
  - path: ../skills/browser-use/references/hosted.md
    why: Portable private-session verification procedure.
---
# Hosted and browser-service bridges

Hosted browser providers expose APIs, SDKs, CDP endpoints or MCPs. A self-hosted service such as Camofox exposes an API backed by local containers. Neither is automatically a local Chrome session; each has its own browser process, profile storage, cost and human-login viewer. Treat provider accounts and profile IDs as private credentials/identifiers, not shared repository material.

**Browser Use Cloud:** Named browser sessions can isolate public tasks, but the historically installed Hermes provider started browsers without binding a saved `profileId`. A separately implemented direct-API helper explicitly bound a saved profile; Google Account and LinkedIn passed a stopped/new-browser check in that pilot, while ChatGPT did not. Do not present the direct helper as native support or infer that a named session has a login. Onboard by checking the current provider SDK/API and the target harness's actual create call for explicit profile binding, then test on a low-stakes account after a full stop/new-browser cycle.

**Camofox:** A loopback-only, keyed container can expose multiple user identities and a visible login viewer. Separate user IDs do not make separate browser processes; a crash or fingerprint can be shared. The local public five-identity pilot survived restart and cleanup, but one ChatGPT login did not persist after container restart despite saved state. For a human login, checkpoint through the service's authenticated session storage-state route while active, restart, and check the site's account-only control. A prior pinned v1.17.0 Dockerfile needed the post-install hook and imports copied before package install; check upstream before reuse.

**Other hosted contexts:** Browserbase, Browserless, Kernel and similar services are candidates, not installed/verified defaults. Inspect current docs for profile concurrency, persistence, billing and termination semantics before suggesting commands. No service may solve CAPTCHA or site rules by policy assertion.

**Onboard/verify:** Decide owner-approved provider and data handling, establish a private key handoff, configure only the active harness, create one public session and verify navigation, then (only if approved) perform a visible human sign-in and explicit save/restart/account-only check per target site. Track exact provider browser IDs and stop only sessions this job created; read back stopped status and zero owned active sessions to avoid billing leaks. A down local gateway cannot be reached merely because the browser is in the cloud.
