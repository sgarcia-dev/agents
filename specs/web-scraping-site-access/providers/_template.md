---
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
model: <model id>
doc_type: spec
status: <researched | trial | in use | rejected>
scope: <Provider name>
purpose: What <Provider> covers, what it costs, whether an individual can use it, and its role here.
related:
  - path: ../spec.md
    why: Owning spec and the provider table.
  - path: ../shared/rules.md
    why: Rules a provider must pass, including terms and data protection.
---

# <Provider>

<Two to four sentences: what it is, what it is good for here, the role we
give it, and the biggest caveat.>

## Status

- **Role:** <primary / gap filler / fallback / discovery only / skip / pending>
- **Accepts an individual customer:** <yes / no / unclear>, with the quote.
- **Allowed today:** <no account, no purchase, no pilot unless DECISIONS.md says so>
- **Last checked:** <date and how>

## What it covers

| Platform | Product or endpoint | What it returns | Account or cookies needed | Label |
|---|---|---|---|---|

## Pricing

- Unit, free tier, smallest paid plan, billing quirks (rollover, failed
  calls, start fees, proxy or compute extras). Each with date and link.
- Worked cost at about 5,000 and 50,000 records a month (label: Inference).

## Signup, terms and data protection

- Individual or business only (quote), identity checks (KYC), payment
  methods, data processing agreement, whether it keeps or reuses collected
  data, who operates it and where.

## Reliability evidence

- Independent reviews, outage or breakage reports, lawsuits. Vendor
  claims kept separate.

## Agent integration

- REST, SDKs, MCP server, webhooks, schedules, spend caps.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|

## Open questions

1. <Question, why it matters, what would answer it.>

## Sources

- <Primary URL, access date.>
