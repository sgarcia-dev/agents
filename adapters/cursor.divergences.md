---
created_at: 2026-07-07
updated_at: 2026-09-15
model: gpt-5.6-terra
doc_type: adapter
purpose: Record current Cursor-specific decisions that must reappear during each own-runtime reconciliation.
related:
  - path: ./cursor.md
    why: Current Cursor mapping and temporary migration status.
---

# Cursor Divergences

Older connector, endpoint, browser, and project-specific entries were retired
from this active ledger because they no longer represent usable workspace
behavior. Git history retains the prior records.

| Item | Status | Next sync action |
|---|---|---|
| Native configuration | pending own-runtime audit | Enumerate all differences against the current workspace roots. |
| Connector and browser-tool extras | pending own-runtime audit | Remove legacy organization-specific entries or ask whether an unrelated extra should remain local. |
| Fast, high, and orchestration mappings | temporarily disabled | Keep disabled until the user changes the spending decision. |
