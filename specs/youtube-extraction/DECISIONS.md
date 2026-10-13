---
created_at: 2026-10-13
updated_at: 2026-10-13
model: gpt-6.1-sol (high)
doc_type: decisions
purpose: Only the user's accepted scope and evidence-layout choices for this spec.
related:
  - path: ./spec.md
    why: Capability behavior and recommended routes.
  - path: ./STATE.md
    why: Implementation proposals and choices still open.
  - path: ./AGENTS.md
    why: How to apply the evidence-layout decisions.
---

# YouTube extraction: decisions

## 2026-10-13: YouTube extraction is its own spec

The user asked for a separate YouTube extraction spec, not a section inside
another spec.

## 2026-10-13: Verbatim sources stay inside the spec

Store verbatim copies of every linked source inside this spec under `sources/`,
not under `artifacts/`.

## 2026-10-13: Digests live in digests/

Store source digests under `digests/`, apart from the verbatim sources.

## 2026-10-13: Tests live in tests/

Store this workspace's measured extraction results under `tests/`.

Implementation and provider proposals live in [STATE.md](STATE.md). They are
not accepted decisions.
