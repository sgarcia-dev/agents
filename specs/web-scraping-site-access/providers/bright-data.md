---
created_at: 2026-10-06
updated_at: 2026-10-06
model: claude-opus-5-5
doc_type: spec
status: researched
scope: Bright Data
purpose: What Bright Data covers, what it costs, whether an individual can use it, and its role here.
related:
  - path: ../spec.md
    why: Owning spec and the provider table.
  - path: ../shared/rules.md
    why: Rules a provider must pass, including terms and data protection.
  - path: ../providers/mcp-servers.md
    why: Bright Data MCP server and the shared MCP security rules.
  - path: ../sites/linkedin.md
    why: LinkedIn posts, profiles and jobs scrapers.
  - path: ../sites/x.md
    why: X profile and post scraper.
  - path: ../sites/reddit.md
    why: Reddit scraper.
  - path: ../sites/indeed.md
    why: Indeed scraper and free records.
  - path: ../sites/threads.md
    why: Threads profiles and posts, partial.
---

# Bright Data

Bright Data is a large, long-running web data company. Its Scraper API
returns structured records for LinkedIn, X, Reddit, YouTube and job
sites, with 5,000 free records a month. It has the strongest track record
and legal record of the four providers. But its docs say it serves
business use cases only and that personal projects are not approved. So
it is a fallback, and only if there is a genuine business use.

## Status

- **Role:** fallback only with a genuine business use. Round 3 user
  opinion (G10, G15, 6 October 2026) agrees: a real, solid company that
  will not vanish with prepaid money, but "a little too much" for a small
  project; best kept for one hard target at a time, never the default.
- **Accepts an individual customer:** no. Docs: "Bright Data is a B2B
  platform and supports business-related use cases only. Personal
  projects ... are not approved."
  https://docs.brightdata.com/proxy-networks/residential/network-access
  (Official doc, checked 6 October 2026). The general FAQ goes wider:
  "Bright Data is a service for enterprise customers who want to collect
  public web data from the Internet, and is not designed for private
  users." https://docs.brightdata.com/general/faqs (Official doc, checked
  6 October 2026 by the root). So the restriction is not limited to
  residential proxies.
- **Allowed today:** no account, no purchase, no pilot. No decision yet.
- **Last checked:** 6 October 2026, by reading the free-tier, KYC and
  network-access docs and the LinkedIn posts product page (6 October
  corroboration).

## What it covers

| Platform | Product or endpoint | What it returns | Account or cookies needed | Label |
|---|---|---|---|---|
| LinkedIn posts | Posts scraper, "collect by URL" and "discover by company URL" | Post text, comment count, `top_visible_comments` only | No | Official doc |
| LinkedIn profiles | Profiles scraper | Profile; structured extractors "may return cached results", refreshed "on a rolling basis". Two Reddit users (March and October 2026) got the experience field back empty, and Bright Data's own sample responses show empty experience and position | No | Official doc for caching; the "November 2025" date in G2 is unverified |
| LinkedIn Jobs | Jobs scraper | Search and detail | No | Official doc (G2) |
| X | X scraper | Public profiles and posts; keyword search and replies not found | No | Official doc (G2), partial |
| Reddit | Reddit scraper | Discovery and discussions | No | Official doc (G2, not rechecked) |
| YouTube | YouTube scraper | Videos and comments | No | Official doc (G2) |
| Indeed, Glassdoor | Job scrapers | Jobs; Indeed Ireland not shown | No | Official doc (G2), partial for Ireland |
| Threads | Scraper | Profiles and posts, not full discussions | No | Official doc (G2), partial |
| Google Jobs | SERP API | Search results | No | Official doc (G2); Google Jobs does not cover Ireland |
| Jobs.ie, IrishJobs.ie | none | Not found | n/a | C2, G2 |

## Pricing

- **Free tier:** "5,000 free credits per month... No credit card"
  (https://docs.brightdata.com/general/account/billing-and-pricing/free-tier,
  checked 6 October 2026, Official doc). The LinkedIn posts page says "5K
  records per month". Treat it as 5,000 records shared across products.
  Free accounts hard-stop when credits run out. MCP calls draw from the
  same pool (6 October corroboration).
- **Pay as you go:** "$1.5/1K record" for successful delivered records
  (https://brightdata.com/products/web-scraper/linkedin/post, checked 6
  October 2026, Official doc). No subscription needed. The Scraper API
  FAQ confirms "5,000 free credits every month", one credit per record,
  and "As of September 2026, pay as you go is $1.50 per 1,000 records"
  (https://docs.brightdata.com/products/scrapers/scrapers-library/faqs,
  checked 6 Oct 2026, round 2).
- **Scale plan:** $499 a month for 384,000 records, then $1.30 per 1,000
  (C2, not rechecked).
- **Other units:** datasets, SERP requests and browser traffic ($8 per GB
  on the MCP) are billed differently (G2, G9, not rechecked).
- **Worked cost** (Inference): 5,000 records a month is $0 inside the free
  tier. 50,000 records is about $67.50 (45,000 paid at $1.50 per 1,000).

## Signup, terms and data protection

- **Business only:** see the quote under Status. This is the blocker, not
  KYC.
- **KYC:** "The Bright Data Web Unlocker API works without KYC" and "KYC
  applications are accepted only from registered businesses"
  (https://docs.brightdata.com/scraping-automation/web-unlocker/kyc-and-access,
  checked 6 October 2026). Residential proxies need business KYC with a
  corporate email domain. Unlocker without KYC still blocks paths that
  `robots.txt` disallows (6 October corroboration).
- **Suspension:** older, undated forum threads describe accounts disabled
  for being "non-company" (Independent report, C2, low quality, not
  rechecked). Newer Trustpilot reviews (July and August 2026) describe KYC
  document demands for an ordinary US LLC and a use case disabled after a
  compliance review (G10, G15, not rechecked). One Hacker News user says
  they used residential proxies "without ever having KYC'd", so
  enforcement is uneven (G15).
- **Licence is for business operations.** Bright Data grants use
  "solely for the purpose of Client's internal business operations"
  (https://brightdata.com/license, page modified 17 June 2026, checked
  6 Oct 2026, round 2). A private research or job-search use does not
  fit that wording.
- **Terms put risk on the customer:** the client "will defend Bright Data
  against any claim" that its use breaks IP or privacy law (C3).
- **It keeps and reuses your data:** "Bright Data may retain data Client
  has collected and may use it for its own purposes in its sole
  discretion." So it is not purely our processor for scraped personal
  data, even though a DPA exists. Official doc, checked 6 Oct 2026
  (round 2). The agreement also allows suspension, identity and use-case
  checks, and legally compelled disclosure (G2).
- **KYC while pending:** "You can use all other Bright Data products and
  services, including ISP proxies, Datacenter proxies and the Web
  Unlocker API, while your KYC request is being processed." The
  business-only rule still applies. Official doc, checked 6 Oct 2026
  (round 2).
- **Refusals:** in 2021 Bright Data said it "refused 736 potential
  customers" whose use cases failed KYC; those were businesses. A
  developer review says its KYC is "tuned for massive corporations".
  Vendor press release and Independent report, report C5, not rechecked.
- **AUP:** bans collecting non-public or login-gated data (G2).

## Reliability evidence

- **Court record:** Meta v Bright Data, summary judgment for Bright Data on
  23 January 2024: Meta's terms do not bar logged-off scraping of public
  data (C2, C3). X v Bright Data (N.D. Cal. 3:23-cv-03698): claims
  dismissed 9 May 2024; amended claims allowed November 2024. On 13 June
  2025 the court let X serve "an additional 30 customer subpoenas" on
  Bright Data's customers. The parties filed a joint dismissal with
  prejudice on 27 June 2025 and the case closed on 1 July 2025
  (https://www.courtlistener.com/docket/67637345/x-corp-v-bright-data-ltd/,
  entries 343 and 353 to 357, Court record, checked 6 Oct 2026). These
  wins do not authorise what customers do, and the subpoenas show that
  customers can be pulled into the vendor's lawsuit.
- Trustpilot 4.4 from 1,025 reviews, with Trustpilot's note "This
  company invites their customers to review, whether positive or
  negative" (checked 6 Oct 2026 through Trustpilot's own excerpts; the
  page itself blocked our fetch). So the score is not a random sample.
  G2 4.7 from 342, partly seller-invited (C2, G17).
- **What users say (round 3):** about 24 scored opinions, mostly
  Trustpilot (G15). Good: consistent results, "Zero dropped tasks". Bad:
  price, KYC friction, Facebook workflows that "stop working for 1-4
  days", a founder "charged for unsuccessful queries" when a blocked page
  counted as a result (Capterra, 25 Sep 2025), and refund experiences
  that range from granted to refused. One competitor's Reddit test got
  397 comments against about 784 live, two reply levels deep, and 291
  records billed (Lobstr, a rival vendor, not rechecked). Its Python SDK
  had a bug where CSV export dropped fields missing from the first record:
  keep raw JSON (G15, not rechecked).
- A 23 July 2026 review noted weak social-scraper filtering; a 7 August
  2026 review noted company-document friction at onboarding (Independent
  report, G2, not rechecked).

## Agent integration

- REST, official JavaScript and Python tooling, webhook delivery, and
  "set monthly spend limits" (Official doc, C2 and G2).
- Bright Data MCP (https://github.com/brightdata/brightdata-mcp): tools
  include `web_data_linkedin_posts`, `web_data_x_posts`,
  `web_data_reddit_posts` and `web_data_linkedin_job_listings`. Latest
  release v2.11.3, 17 September 2026, which fixed credential redaction in
  logs (Official doc, G9). Not a first pick here because of the
  personal-project ban. See
  ~/agents/specs/web-scraping-site-access/providers/mcp-servers.md.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | Add Bright Data first (G2, G9) | Docs say personal projects are not approved. Fallback only | docs.brightdata.com network-access page, checked 6 Oct 2026 |
| 2026-10-06 | Scraper APIs "reportedly need no KYC", so signup is fine (C2) | True for Unlocker, but the business-only rule is the real blocker | KYC and network-access docs, checked 6 Oct 2026 |
| 2026-10-06 (round 3) | X v Bright Data "reported paused in June 2025 while the parties settle" (our line, from news). | 30 customer subpoenas allowed 13 June 2025; joint dismissal filed 27 June; case closed 1 July 2025. | CourtListener docket, round 3 check V5 |
| 2026-10-06 (round 3) | LinkedIn profile fields cached "since a November 2025 policy change" (G2). | Caching is confirmed; the November 2025 date is not on any page found. | Bright Data blog, round 3 check V5 |
| 2026-10-06 | 5,000 monthly "credits" (earlier note) | Product page says 5,000 records; shared across products | https://brightdata.com/products/web-scraper/linkedin/post, checked 6 Oct 2026 |

## Open questions

1. Will Bright Data approve a sole trader with no company domain? Round
   2 found no answer; its KYC wants a "registered business" and a company
   email domain, and its licence is for "internal business operations".
   Treat it as no for this user unless a real business exists.
2. Answered 6 Oct 2026: the business-only line is in the general FAQ and
   the licence, not only on the proxy page.
3. Is X v Bright Data closed? The court record was not checked.

## Sources

- Deep research rounds 1 and 2 (5 and 6 October 2026; private, not published), reports C2, C3, C5, C6, G2 and G9, plus both
  corroboration rounds.
- https://docs.brightdata.com/proxy-networks/residential/network-access,
  accessed 6 October 2026.
- https://docs.brightdata.com/scraping-automation/web-unlocker/kyc-and-access,
  accessed 6 October 2026.
- https://docs.brightdata.com/general/account/billing-and-pricing/free-tier,
  accessed 6 October 2026.
- https://brightdata.com/products/web-scraper/linkedin/post, accessed 6
  October 2026.
- https://brightdata.com/license, accessed 5 October 2026 (C3, G2).
- https://brightdata.com/pricing/mcp-server, accessed 5 October 2026 (G9).
- Earlier note: ~/agents/capabilities/web/README.md, row
  "Bright Data Web Unlocker".
