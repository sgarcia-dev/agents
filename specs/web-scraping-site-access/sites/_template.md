---
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
model: <model id>
doc_type: spec
status: <researched | piloted | live | excluded | deferred>
scope: <Site name>
purpose: How agents can read <Site>: routes per operation, costs, rules and open questions.
related:
  - path: ../spec.md
    why: Owning spec, shared model and the route table.
  - path: ../shared/rules.md
    why: Access, legal and data rules every route must pass.
  - path: ../providers/<provider>.md
    why: <Provider> facts used by a route here.
---

# <Site>

<Two to four sentences: what this platform is useful for, the best route
today, the cost, and the one caveat that matters most.>

## Status

- **Verdict:** <one line>
- **Allowed today:** <yes / needs pilot permission / excluded>, per [DECISIONS.md](../DECISIONS.md).
- **Last checked:** <date>, <how: research report, primary-source check, observed test>.

## Routes by operation

Operations: **discover** (keyword or topic search), **retrieve** (one known
item by URL or ID), **thread** (a known item with all replies), **monitor**
(follow accounts, tags, communities or saved searches over time). Job
boards use **search** and **detail** instead of thread.

| Operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence |
|---|---|---|---|---|---|---|

## Facts that decide the route

- <Fact, with date, label and link.>

## Rules and risks for this site

- <Terms quotes, account risk, legal notes specific to this site. Link to
  shared/rules.md for the general rules.>

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|

## Open questions

1. <Question, why it matters, what would answer it (research prompt or
   pilot).>

## Sources

- <Primary URL, access date.>
- Research bundles: see [SOURCES.md](../SOURCES.md).
