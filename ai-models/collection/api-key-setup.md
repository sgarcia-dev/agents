---
created_at: 2026-09-30
updated_at: 2026-09-30
model: openai/gpt-6.1-sol
doc_type: reference
purpose: Adapt the user's API-key README into a hidden-input smoke-test procedure.
related:
  - path: ~/agents/ai-models/collection/API.md
    why: Authentication, quota and coverage limits.
---

# API key setup

You already have a key; there is no need to regenerate it. If needed later, [key management](https://artificialanalysis.ai/api-key-management-redirect) belongs to an organisation. Choose the correct organisation. Regeneration revokes the old key.

## Hidden-input test

Run this from your own Terminal:

```bash
bash ~/agents/ai-models/scripts/enter-key-and-test.command
```

The prompt hides typing and pasting. The key stays in that shell's environment for the collector child, then is unset. It is not saved to disk, added to command history, printed, or passed as a command argument.

The launcher makes at most ten Free catalogue page requests, stops on authentication/quota/errors, validates all pages, resolves the four current favorites at medium using exact effort-specific slugs, and stages results in a timestamped ignored `ai-models/cache/` directory. It does not buy a plan, bypass a paid endpoint, create an account, or test Pro. API-only refresh does not update website fields; review before publishing a dated snapshot. Agents must not open Terminal automatically: the human runs this when a fresh authenticated call is needed.

After completion, tell the calling agent “the API test is ready”. Share the result folder, **not the key**. The agent can inspect `run.json`, `catalog.json` and `favorites.json` without seeing credentials. If it fails, report the HTTP status and quota metadata; do not paste request headers.

## Future runs

Set `ARTIFICIAL_ANALYSIS_API_KEY` in the environment of the process that runs the collector. An export in another Terminal does not automatically reach an already-running agent. The six-hour cache lets later lookups run without the key until a refresh is needed.

This installation does not persist the secret or configure dotenv loading. Never assume Claude Code, Codex, OpenCode and Hermes share credentials or automatically load `.env.local`. Configure each tool in its own session if persistent environment loading is desired.

Do not type a literal key into an `export ...` command, source code, prompts, committed files or browser JavaScript. Avoid `curl -v`, shell tracing and commands that put the key in the process argument list. The bundled Python collector sends the key only in the HTTPS header to the fixed API origin and rejects redirects.

## Quota and failures

Docs checked September 30, 2026: Free 100, Pro 500 requests per fixed 24-hour window, Commercial custom. Keys share quota within the documented scope. Cache the full catalogue; do not make a request per favorite model.

- 401: missing, invalid or revoked key. Stop and verify organisation/key locally.
- 403: endpoint not covered. Free uses `/api/v2/language/models/free`, not `/language/models`.
- 429: quota exhausted. Respect `Retry-After` and `X-RateLimit-Reset`.
- Malformed/incomplete pagination: keep the previous cache, report failure.

Official source: https://artificialanalysis.ai/data-api/docs
