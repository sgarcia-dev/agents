---
created_at: 2026-10-06
updated_at: 2026-10-06
model: claude-opus-5-5
doc_type: spec
status: deferred
scope: Facebook
purpose: How agents could read public Facebook Pages, groups and posts, what it would cost, and why it is deferred.
related:
  - path: ../spec.md
    why: Owning spec, shared model and the route table.
  - path: ../shared/rules.md
    why: Access, legal and data rules every route must pass.
  - path: ../providers/apify.md
    why: Apify facts used by the Posts and Groups Actors.
  - path: ../providers/bright-data.md
    why: Bright Data facts used by the Facebook product.
---

# Facebook

Lowest priority for AI and engineering news and tech jobs. Possible niche
use: local meetups, employer Pages and a few public communities. Official
routes exist but need app review or research-institution status. Deferred
until one named public source keeps adding something missing elsewhere.

## Status

- **Verdict:** deferred. No pilot.
- **Allowed today:** no. Deferred until a specific, justified source set exists, per [DECISIONS.md](../DECISIONS.md).
  No account, private group, cookie or bypass in any case.
- **Last checked:** 5 October 2026, research reports and primary-source
  reads. Not part of the 6 October corroboration.

## Routes by operation

| Operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence |
|---|---|---|---|---|---|---|
| discover | General web index (existing search tools) | Apify Facebook Posts Actor | search cost only; Actor from $2 per 1,000 | None | Vendor claim | Low |
| retrieve | Apify Posts Actor or Bright Data | Approved Graph Page access | about $7.50 to $10 | None (Graph needs an app and review) | Vendor claim | Low |
| thread | None established | Apify or Bright Data comments | not measured | None | Vendor claim | Low |
| monitor | Apify scheduled Actor on chosen Pages | Bright Data URL discovery | about $10 | None | Vendor claim | Low |

## Facts that decide the route

- [Page Public Content Access](https://developers.facebook.com/documentation/development/features-reference/page-public-content-access)
  (updated 1 July 2026) allows Pages Search and public Page posts and
  comments for approved uses. Needs App Review and business verification.
  Not arbitrary keyword post search. Official doc.
- [Meta Content Library](https://developers.facebook.com/docs/content-library-and-api/get-access)
  is for not-for-profit academic or public-interest research institutions,
  reviewed by CASD. No fee once approved; output rules apply. A personal
  workflow does not qualify. Official doc. See also the
  [overview](https://transparency.meta.com/en-gb/researchtools/meta-content-library).
- The Groups API was removed in 2024 ([TechCrunch](https://techcrunch.com/2024/02/05/meta-cuts-off-third-party-access-to-facebook-groups-leaving-developers-and-customers-in-disarray/)).
  Independent report.
- [Apify Facebook Posts Scraper](https://apify.com/apify/facebook-posts-scraper):
  from $2 per 1,000 posts. [Groups Actor](https://apify.com/apify/facebook-groups-scraper):
  from $2.60 per 1,000 posts, a separate product. Vendor claim, 5 October 2026.
- [Bright Data Facebook posts](https://brightdata.com/products/web-scraper/facebook/posts):
  $1.50 per 1,000 records; Scale $499 a month for 384,000, then $1.30 per
  1,000 ([pricing](https://brightdata.com/pricing/web-scraper)). Free grant
  terms in [bright-data.md](../providers/bright-data.md).
  Vendor claim.
- The unofficial `facebook-scraper` project warns of missing fields,
  one-page group limits and blocking. No current reliability proof.

## Rules and risks for this site

- General rules: [shared/rules.md](../shared/rules.md).
- No private groups, cookies, personal-account automation, contact
  collection or anti-bot bypass.
- A supplier calling itself "compliant" is not permission. No legal
  conclusion about logged-out scraping was reached.
- Facebook job posts are leads only. Confirm on the employer's own page.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-05 | Gemini: $0.75 per 1,000 requests, $500 minimum, $29 Apify Starter. | Not supported. Bright Data's rate card says $1.50 per 1,000 records. | Earlier note |
| 2026-10-05 | Gemini: plain HTTP never works; logged-out scraping is legally safe. | Both overstated. | Earlier note |
| 2026-10-05 | Content Library allows no export ever. | Approved outputs exist, under conditions. | Meta overview |

## Open questions

1. Does any named public Facebook source add something our other sources
   miss? If not, stay deferred.
2. Bright Data free grant: records or credits for Facebook? Check before
   any budget.

## Sources

- Meta, TechCrunch, Apify and Bright Data pages linked above, read 5 October 2026.
- Earlier note: [facebook.md](../../../capabilities/web/social/facebook.md).
- Research bundles: see [SOURCES.md](../SOURCES.md).
