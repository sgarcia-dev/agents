# Web scraping site access: how to work here

This spec says how agents can read public platforms: social networks,
developer forums, job boards and employer job feeds. It also covers the
paid data providers that sit in front of them. It is a research
capability. Job search is one consumer, not the frame.

Read [spec.md](spec.md) first, then [STATE.md](STATE.md). Then open
only the site or provider file you need.

## Layout

- `spec.md`: the shared model (operations, route types, labels), the route
  table and the provider table. It is the router.
- `STATE.md`: what is true now, what is blocked, what comes next.
- `DECISIONS.md`: durable choices and the rules the user set.
- `SOURCES.md`: evidence ledger, research bundles, weak claims to avoid.
- `shared/rules.md`: access, legal and data rules every route must pass.
- `shared/legal.md`: the Irish and EU legal background behind the rules.
- `shared/eligibility.md`: which providers accept an individual, and the
  user's options for paying one.
- `shared/accounts.md`: when a research or alert account is allowed, and
  how to run one honestly.
- `shared/email-alerts.md`: job alert emails as a route to the boards.
- `shared/evaluation.md`: how to test a route and decide whether to add a
  platform or provider.
- A topic that cuts across several sites or providers gets its own
  `shared/<topic>.md` rather than being copied into each file.
- `sites/<site>.md`: one file per platform. Copy `sites/_template.md`.
- `providers/<provider>.md`: one file per data provider, or one file per
  small group of similar providers. Copy `providers/_template.md`.

## How to grow it

- **New platform:** add `sites/<name>.md` from the template, add one row to
  the route table in `spec.md`, and run the decision rule in
  `shared/evaluation.md` first.
- **New provider:** add `providers/<name>.md` from the template and one row
  to the provider table. A provider that matters for only one platform may
  live inside that site file instead.
- **A file gets too big** (over about 300 lines, or it needs its own state
  and decisions): turn it into a folder, `sites/<name>/spec.md` plus
  `STATE.md`, and keep the row in the route table pointing at it.
- Facts live in one place. The route table holds one line per site and a
  link; the site file holds the detail. Do not copy a price into several
  files; link to the file that owns it.

## Evidence rules

- Label every claim: Official doc, Vendor claim, Independent report, Court
  record, Observed test, or Inference. Keep vendor claims apart from tested
  facts.
- Every price, limit and quote carries a date and a link. A price keeps its
  unit, minimums and plan.
- Only an Observed test (our own run, with a dated record) proves that a
  route works. Research reports and vendor pages do not.
- When a claim turns out wrong, fix the line and add it to that file's
  Corrections log and to `SOURCES.md` "Weak claims to avoid". Do not edit
  the original research reports.
- Store new research under the root `artifacts/investigations/` (private,
  not published) and link the bundle from `SOURCES.md`. Do not put generated reports in this folder.

## Relation to web search, and promotion

- [capabilities/web](../../capabilities/web/README.md)
  and the `web-search` skill own general search and page reading. This
  spec owns the per-site routes and the providers. Everything here is
  research only until it is promoted.
- **Promotion.** When a route has an Observed test with a dated record,
  and the user agrees it is solid, expose it to everyday work through a
  thin adapter: a short entry in `capabilities/web` (and the web-search
  ladder, if it fits) that names the route, its gate and its spending cap,
  and links back here. The adapter holds no prices, rules or evidence;
  those stay in this spec. Record each promotion in `DECISIONS.md`.
- Until a route is promoted, the web-search skill does not call it.

## Boundaries

- Nothing here enables an API, connector, scraper, account, purchase,
  pilot or schedule. Each of those needs an explicit user decision,
  recorded in `DECISIONS.md`.
- Follow [shared/rules.md](shared/rules.md): no logins or own cookies for
  scraping, no LinkedIn reads by agents, home IP kept away from sites that
  block bots, hard caps on paid tools.
- Reddit here means the public website as a data source only.
- Keep personal details (job targets, inbox contents, private pipeline
  settings) out of this spec. They live in a separate private repo. Shared
  files may say that a private consumer exists.
- General search and page-reading tools (Parallel, Exa, Firecrawl, harness
  search) are owned by `~/agents/capabilities/web/README.md`.
  Link to them; do not duplicate their facts here.
