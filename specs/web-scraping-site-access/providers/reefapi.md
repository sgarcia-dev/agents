---
created_at: 2026-10-06
updated_at: 2026-10-06
model: claude-opus-5-5
doc_type: spec
status: researched
scope: ReefAPI
purpose: What ReefAPI covers, what it costs, whether an individual can use it, and its role here.
related:
  - path: ../spec.md
    why: Owning spec and the provider table.
  - path: ../shared/rules.md
    why: Rules a provider must pass, including terms and data protection.
  - path: ../providers/mcp-servers.md
    why: ReefAPI hosted MCP and the shared MCP security rules.
  - path: ../sites/reddit.md
    why: ReefAPI is a candidate third-party Reddit route.
  - path: ../sites/x.md
    why: X coverage is claimed but disputed.
  - path: ../sites/threads.md
    why: Threads coverage is claimed but disputed.
  - path: ../sites/linkedin.md
    why: LinkedIn Jobs endpoints; no LinkedIn posts.
  - path: ../sites/indeed.md
    why: Indeed search and detail endpoints.
---

# ReefAPI

ReefAPI sells one API key and one credit pool for hundreds of live data
"engines", including Reddit, Bluesky, Hacker News, LinkedIn Jobs and
Indeed. It has the cleanest terms of the four providers for an
individual: no business-only clause. But no page names the company
behind it (third-party listings say Türkiye, founded 2026), its own pages
disagree on card versus crypto payment, and there is no independent
evidence that it works well. Its role is a trial with free credits only.

## Status

- **Role:** trial candidate (free credits only). The round 3 user-opinion
  report (G13, 6 October 2026) reached the same verdict on its own: "safe
  to try with free credits only". It found no independent customer at all.
- **Accepts an individual customer:** yes on paper. The terms (updated 16
  September 2026) have no business-only clause. They say "You are solely
  responsible for how you use the data" and ban "competing
  bulk-redistribution". https://reefapi.com/terms (Official doc, checked 6
  October 2026). But no operator is named, and its payment pages
  conflict (see Signup). The 1,000 free credits need no payment.
- **Allowed today:** no account, no purchase, no pilot. No decision yet.
- **Last checked:** 6 October 2026, by reading the homepage, pricing,
  compare, terms, privacy and about pages, its Apify profile, its MCP
  repository and two directory listings (round 1 and round 2
  corroboration).

## What it covers

All coverage below is the vendor's own catalogue. None of it is tested.
The reports disagree on X, Threads and LinkedIn posts.

| Platform | Product or endpoint | What it returns | Account or cookies needed | Label |
|---|---|---|---|---|
| Reddit | Search, post detail, comment trees, `load_more_comments` (3 credits) | Posts and comments; live and archive modes | No | Official doc (G2, not rechecked) |
| Bluesky | Search, profiles, posts, threads | Posts and threads | No | Official doc (G2, not rechecked) |
| Hacker News | `/hackernews/v1/stories` and search | Stories, comments, users | No | Official doc (G2, C2, not rechecked) |
| X | Search, lookup, timelines, replies | Posts | No | Disputed: C2 and G2 say yes; another report found no evidence |
| Threads | Profiles, posts, replies | Posts | No | Disputed: G2 says partial, keyword search not found |
| LinkedIn Jobs | 6 endpoints, 1 to 2 credits | Job search and detail; recruiter PII dropped | No | Vendor claim (C2, not rechecked) |
| Indeed | Search and detail | Jobs; Ireland coverage not shown | No | Official doc (G2), partial for Ireland |
| Glassdoor | Company to open jobs | Employer, reviews, salaries; job search not established | No | Disputed (G2, G9) |
| LinkedIn posts, Mastodon, Jobs.ie, IrishJobs.ie, Google Jobs | none | Not found | n/a | Official doc (C2, G2) |

- Engine count drifts across its own pages: from 192 to 384 APIs, and
  AlternativeTo says "150+" (both corroboration rounds). It looks like
  fast catalogue growth with stale page builds. Vendor claim plus
  Inference, report C5.
- The jobs category says "metered per result, recruiter-PII dropped. 17
  APIs · 75 ep". It also lists Stack Overflow, GitHub and Product Hunt
  engines, which matter for developer-trend research. Vendor claim,
  report C5.
- How it gets data (vendor pages, report C5): some engines scrape with
  "rotating proxies and pacing"; "cache hits cost nothing", so some
  answers are stored copies; some wrap public APIs (the HN demo); personal
  data is redacted unless `include_pii` is set. Nothing says which engines
  use which method.
- **LinkedIn Jobs engine:** calling it is not reading LinkedIn ourselves,
  but it is LinkedIn-derived data. Whether to use it is open (P10). See
  [linkedin.md](../sites/linkedin.md).
- Reddit archive mode exists, but the claim that it uses Arctic Shift and
  PullPush was not found on current pages (G2, not rechecked).

## Pricing

- **Plans** (https://reefapi.com/pricing, checked 6 October 2026, Official
  doc): Pro $15 a month for 10,000 credits, Ultra $50, Enterprise $200,
  and Custom. Yearly billing is 50% off. "Credits that never expire."
  Its comparison page also lists "Mega | $100 / mo | 125,000 credits",
  which the pricing page does not; treat Mega as unconfirmed
  (https://reefapi.com/compare/scraperapi-alternative, checked 6 Oct
  2026). SourceForge says 2,000 free credits a month, against ReefAPI's
  own 1,000; trust ReefAPI's page.
- **Free tier:** 1,000 credits at signup, no card (Official doc).
- **Top-ups:** $1.72 per 1,000 credits on Pro (6 October corroboration).
  G2 also lists $1.15 and $0.77 on higher plans (not rechecked).
- **Unit:** "light calls cost 1 credit, heavier ones cost more". Reddit
  `load_more_comments` costs 3 (Official doc).
- **Failures:** timeouts and blocked calls are not charged (6 October
  corroboration). One exception in the terms: "Verified SHEIN NOT_FOUND
  responses on product/detail and price cost 4 credits", while the
  refund page still says failed requests "never consume credits"
  (https://reefapi.com/terms, https://reefapi.com/refunds, checked 6 Oct
  2026). Small, but it shows its own pages drift apart.
- **Worked cost** (Inference, C2 and G2): about $15 a month at 5,000
  records if each record costs 1 to 2 credits. About $50 to $100 at
  50,000 records. Real cost depends on credits per record, which is
  unknown until tested.

## Signup, terms and data protection

- **Individual:** no business-only clause (see Status).
- **KYC:** none mentioned. Instant API key (Official doc, C2).
- **Payment: its own pages conflict.** The homepage says "New — pay by
  credit card" and "pay by card or crypto". The pricing page says
  "Payments are in crypto today (USDT & other coins) — card payments are
  coming soon", yet also "Card plans renew automatically · crypto
  payments are one-off". Billing goes through an unnamed "Merchant of
  Record". A subset of engines is sold on RapidAPI, which takes cards.
  Vendor claim, checked 6 Oct 2026 (round 2). Only a checkout attempt
  would settle it.
- **Operator:** not named in the terms, privacy page or about page.
  AlternativeTo lists "Origin: Türkiye" and SourceForge "Founded: 2026".
  These listings are often filled in by the vendor, so they are a weak
  but real signal. No legal entity, address or WHOIS registrant found.
  Independent report, checked 6 Oct 2026 (round 2).
- **Do not confuse it** with REEF Technology, reef.com, Reef.Tools or
  workfromreef.com, which are unrelated (report C5).
- **Data protection:** no DPA or GDPR terms found. Compliance is placed on
  the customer (Official doc). As data controller we would be sending it
  queries about people, so this matters.

## Reliability evidence

- **What users say (round 3, 6 October 2026):** nothing. Reports G10, G13
  and G17 searched Reddit, Hacker News, X, Trustpilot, G2, Product Hunt
  and others and found zero independent customer reports. The only
  Reddit praise traced back to an account whose profile says it runs
  ReefAPI; that account sometimes discloses this and sometimes recommends
  ReefAPI as if it were an ordinary user (G13; we could not open the
  profile on 6 Oct 2026 to confirm). Do not count Reddit mentions of
  ReefAPI as user evidence.
- One self-published outage: its Vinted search route broke for about 25
  hours after Vinted changed an upstream route (ReefAPI's own Vinted
  comparison page, G13, not rechecked). Judge each engine, not the gateway.
- Its Hacker News engine takes the same parameters as the free public
  Algolia HN API, so it is very likely a wrapper (G13, Inference). Use
  Algolia directly.
- Its MCP endpoint is alive: independent probes logged it up in August
  2026, and one monitor shows 98.4% uptime over 30 days (G13, not
  rechecked).
- No independent reviews. No Trustpilot or G2 profile; SourceForge says
  "hasn't been reviewed yet" (C2, not rechecked). A 6 October search found
  only directories and VerifyMCP.
- Its Apify publisher profile: "Joined June 2026", 84 total users, 24
  monthly users, "97% runs succeeded" (vendor number, checked 6 October).
- VerifyMCP gave the hosted MCP a trust score of 80 out of 100, scanned 20
  September 2026. It flagged that no tool declares a destructive hint
  (Independent report, checked 6 October).
- A ReefAPI-written study found the median LinkedIn job result was 15
  days old. The authors flag their own conflict of interest (C2, not
  rechecked).
- No lawsuits found.

## Agent integration

- REST: every call is POST to `https://api.reefapi.com/<api>/v1/<action>`
  with an `{ok, data, meta, error}` envelope (C2, not rechecked).
- No first-party Node SDK found. Plain `fetch` is enough (G2).
- Hosted MCP at https://reefapi.com/mcp with five tools: `search_engines`,
  `get_catalog`, `get_engine_schema`, `get_action_schema`, `call_engine`.
  Discovery tools need no key (G9 and 6 October corroboration). Repo
  https://github.com/reefapi/reefapi-mcp created 23 June 2026, 1 star.
- A playground with a shared demo key lets you try endpoints before
  signup (C2, not rechecked).
- Webhooks, schedules, spend caps: not found. Crypto prepay is itself a
  hard cap.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | A "Mega $100 for 125k" plan exists (C2) | Not on the pricing page (Pro $15, Ultra $50, Enterprise $200, Custom), but listed on ReefAPI's own comparison page. Unconfirmed, not wrong. | https://reefapi.com/pricing, https://reefapi.com/compare/scraperapi-alternative, round 2 |
| 2026-10-06 | MCP repo has 4 GitHub stars (C2) | 1 star | https://github.com/reefapi/reefapi-mcp, checked 6 Oct 2026 |
| 2026-10-06 | Apify profile shows 76 users and over 99% success (C2) | 84 total users and 97% runs succeeded | https://apify.com/reefapi, checked 6 Oct 2026 |
| 2026-10-06 | Pay by card or crypto (C2); our round 1 correction said "crypto only". | Its homepage says card or crypto; its pricing page says crypto only for now. Both claims are on ReefAPI's own pages. | https://reefapi.com/, https://reefapi.com/pricing, round 2 |
| 2026-10-06 | No authoritative terms found (C3) | Terms exist, updated 16 Sep 2026, with no company named | https://reefapi.com/terms, checked 6 Oct 2026 |
| 2026-10-06 (round 3) | Failed or blocked requests are never charged (refund page). | The terms charge 4 credits for a verified SHEIN NOT_FOUND. | https://reefapi.com/terms, round 3 check V4 |
| 2026-10-06 | Turkey-based (C2) | Only directory listings say so (AlternativeTo: Türkiye; SourceForge: founded 2026). ReefAPI's own pages name no operator or country | https://alternativeto.net/software/reefapi/about/, round 2 |

## Open questions

1. Who legally operates ReefAPI, and what are its DPA and GDPR terms?
   Still not found after round 2. Report C5 suggests asking through the
   contact form; that is an outward message, so it is the user's call.
2. How many credits per call does each target engine cost, and what does
   it return? The free 1,000 credits would settle it (proposal P9).
3. Is there any independent uptime or success-rate data from the last 90
   days?
4. Do the top-up rates apply to monthly plans or only annual ones?

## Sources

- Deep research rounds 1 and 2 (5 and 6 October 2026; private, not published), reports C2, C5, G2 and G9, plus both corroboration
  rounds.
- https://reefapi.com/, https://reefapi.com/privacy and
  https://reefapi.com/compare/scraperapi-alternative, accessed 6 October
  2026.
- https://reefapi.com/pricing, accessed 6 October 2026.
- https://reefapi.com/terms, accessed 6 October 2026.
- https://reefapi.com/about, accessed 6 October 2026.
- https://apify.com/reefapi, accessed 6 October 2026.
- https://github.com/reefapi/reefapi-mcp, accessed 6 October 2026.
- https://reefapi.com/reddit-api and https://reefapi.com/apis/jobs,
  accessed 5 October 2026 (G2).
- Earlier note:
  ~/agents/artifacts/handoffs/26-10-05_22-39__handoff__social_research_and_scraper_options_gpt-6-1-sol.md
  (calls ReefAPI a "permission-cleared test" candidate).
