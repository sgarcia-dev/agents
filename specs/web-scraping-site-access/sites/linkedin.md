---
created_at: 2026-10-06
updated_at: 2026-10-07
model: claude-opus-5-5
doc_type: spec
status: excluded
scope: LinkedIn
purpose: How agents could read LinkedIn public posts, profiles, company pages and jobs, what it would cost, and why it stays excluded for now.
related:
  - path: ../spec.md
    why: Owning spec, shared model and the route table.
  - path: ../shared/rules.md
    why: Access, legal and data rules every route must pass.
  - path: ../DECISIONS.md
    why: The user rule that keeps LinkedIn excluded.
  - path: ../providers/apify.md
    why: Apify facts used by the Dami, HarvestAPI and Bebity routes.
  - path: ../providers/bright-data.md
    why: Bright Data facts used by the posts, company and jobs routes.
  - path: ../providers/social-apis.md
    why: ScrapeCreators facts used by the known-post route.
---

# LinkedIn

LinkedIn is useful for professional AI and engineering posts, company news
and hiring signals. Agents never read LinkedIn directly and never use the
user's LinkedIn account or cookies. The cheapest no-login third-party route
is an Apify post-search Actor at about $0.90 per 1,000 posts. But the User
Agreement bans using LinkedIn information obtained "whether directly or
through third parties (such as search tools or data aggregators or
brokers)", and that binds anyone who holds a LinkedIn account. So buying
LinkedIn data from a vendor is a contract risk to the user's own account.
Whether to buy LinkedIn data from vendors is open (P10): the user wants
the options judged first from genuine user opinions, not vendor sites.

## Status

- **Verdict:** excluded for direct reads. Third-party LinkedIn data is
  researched but proposed to be excluded too (P10).
- **What users say (round 3, 6 October 2026):** no vendor earns trust as
  a LinkedIn source. HarvestAPI and Bright Data work but drop data;
  Dami, ReefAPI and SociaVault have no independent users; vendors keep
  getting sued or shut. The user-opinion report (G17) suggests: employer
  job feeds for jobs, Google-index routes only as cheap experiments, tiny
  prepaid balances, never a session. Detail under "What users say" below.
- **Allowed today:** excluded, per [DECISIONS.md](../DECISIONS.md). The user
  rule: agents never read LinkedIn and never use the user's account or
  cookies ("don't want to get banned"). A no-login third-party route needs
  a separate user decision (P10, open). This also covers multi-site
  vendors' LinkedIn engines (ReefAPI lists LinkedIn Jobs) and job APIs
  that index LinkedIn (Fantastic.jobs, TheirStack).
- **Last checked:** 6 October 2026, by both corroboration rounds. The
  User Agreement was read through a Wayback Machine snapshot of 6 October
  2026. No linkedin.com page opened, no vendor called.

## Observed test (7 October 2026)

- **User-directed test of two no-cookie LinkedIn jobs Actors** (7 Oct
  2026): curious_coder/linkedin-jobs-scraper (17,709 monthly users, 4.59
  from 141 ratings) and valig/linkedin-jobs-scraper (4,491 users) each
  returned 10 real Irish jobs with full descriptions, for about $0.02 in
  all. valig includes the recruiter's name, which must be dropped. No
  posts or profiles were read. Ongoing vendor use is still P10. A01_apify record (private, not published).

## Routes by operation

Keep these apart. Posts, profiles and company pages, and Jobs are separate
operations with separate suppliers. "Account risk to the user" means risk to
the user's own LinkedIn account. A vendor API key is not a LinkedIn account.

### Public posts

| Operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence | Allowed today |
|---|---|---|---|---|---|---|---|
| discover | Apify Dami post search (no login; finds posts through Google's index) | HarvestAPI post search (price displays conflict; report G9) | about $4.50, fits Apify's $5 free credit | Account risk to the user: none direct (Apify token only) | Vendor claim | Medium (recall not measured) | excluded; a no-login third-party route needs a separate user decision |
| retrieve | Bright Data Posts "collect by URL" | ScrapeCreators one-credit lookup | $0 inside Bright Data's 5,000 free records | Account risk to the user: none direct | Vendor claim | Medium | excluded; a no-login third-party route needs a separate user decision |
| thread | HarvestAPI comments Actor (up to 5 replies per comment) | Dami comments Actor (10 top-level comments, no replies) | not measured | Account risk to the user: none direct | Vendor claim | Low (no full-thread route) | excluded; a no-login third-party route needs a separate user decision |
| monitor | Dami profile-posts or company-posts Actors, $0.90 per 1,000 | Bright Data "discover by company URL" | about $4.50, or $0 on Bright Data free | Account risk to the user: none direct | Vendor claim | Medium | excluded; a no-login third-party route needs a separate user decision |

### Profiles and company pages

| Operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence | Allowed today |
|---|---|---|---|---|---|---|---|
| retrieve | Bright Data or ScrapeCreators company details (report G5) | HarvestAPI company-details Actor | not normalized; G5 gives about $19 at 2,000 for HarvestAPI | Account risk to the user: none direct | Vendor claim, not rechecked | Low | excluded; a no-login third-party route needs a separate user decision |

People profiles are personal data. G5 lists people-data vendors (People
Data Labs, Coresignal, EnrichLayer) as candidates only, with unclear
provenance (Vendor claim, not rechecked). No profile route is proposed.

### LinkedIn Jobs

| Operation | Best route | Runner-up | Cost at ~5,000 items a month | Account needed | Label | Confidence | Allowed today |
|---|---|---|---|---|---|---|---|
| search | Apify Bebity or HarvestAPI LinkedIn Jobs (no cookies) | Job-alert emails, as a sample to spot gaps | about $5 to $7.50 | Account risk to the user: none direct for Actors; alerts exist on the user's own account | Vendor claim | Medium | excluded; a no-login third-party route needs a separate user decision |
| detail | Employer ATS page (the hiring system's own job page), matched by company and title | Bebity full description; Bright Data job "collect" | $0 for ATS | Account risk to the user: none | Inference | High for ATS | ATS pages follow their own site rules; the LinkedIn side is excluded; a no-login third-party route needs a separate user decision |

## Facts that decide the route

- **No official read API for other people's posts or for jobs.** The
  [Posts API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api)
  and [Community Management](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/community-management-overview)
  APIs are permission-scoped and vetted. `r_member_social` is closed to new
  requests; `r_member_social_feed` is for select developers. The Job Posting
  API feeds jobs into LinkedIn and is "not accepting new partners" (G6 2.1,
  page updated 3 June 2026). Official doc.
- The [Comments API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/comments-api)
  returns nested comments only within its access rules. Official doc.
- **Dami post search:** [$0.90 per 1,000 posts](https://apify.com/dami_studio/linkedin-post-search-scraper)
  on the free plan, down to $0.87 on Business. "Account needed: None from
  you." About 90 posts per phrase, 20 phrases and 1,000 posts per run. Each
  run start costs $0.003 more, so batch phrases. "The free plan's $5 a month
  covers about 5,500" posts. It finds posts through Google's index, so it is
  weak on very new posts. Vendor claim, checked 6 October 2026.
- **Dami comments:** the [comments Actor](https://apify.com/dami_studio/linkedin-post-comments-scraper)
  returns at most 10 top-level comments, no replies, approximate ages. Price
  conflicts in the source: from $0.57 per 1,000 in Store metadata, $0.60
  flat in the README. Vendor claim, 5 October 2026.
- **HarvestAPI:** jobs at $1 per 1,000 plus $0.001 per run. Its
  [comments Actor](https://apify.com/harvestapi/linkedin-post-comments)
  returns up to 5 replies per comment and about 1,000 root comments per post
  at most. Vendor claim (G1), not rechecked. Post search is listed "from
  $1.50 / 1,000 posts", and LinkedIn returns "up to 400-500 posts per
  query", so split queries. Profile search is $0.10 per search page of up
  to 25 results, and that Actor uses HarvestAPI's own LinkedIn accounts,
  which "LinkedIn periodically blocks". Vendor claims, checked 6 Oct 2026
  (round 3).
- **Bebity Jobs:** [rebuilt in September 2026](https://apify.com/bebity/linkedin-jobs-scraper),
  pay per result, "no LinkedIn account, no cookies, no login required", from
  $1.00 per 1,000. Returns 42 fields, including the recruiter name, which is
  personal data. Vendor claim, checked 6 October 2026.
- **Bright Data posts:** [5,000 records a month free, no card](https://brightdata.com/products/web-scraper/linkedin/post),
  then $1.50 per 1,000 records; Scale is $499 a month for 384,000 records,
  then $1.30 per 1,000. The free records are shared across Bright Data
  products. Bright Data says personal projects are not approved (see
  [bright-data.md](../providers/bright-data.md)).
  Vendor claim, checked 6 October 2026.
- The [Bright Data Posts API](https://docs.brightdata.com/api-reference/web-scraper-api/social-media-apis/linkedin/posts)
  types `top_visible_comments` as a number, not comment text. Its
  structured LinkedIn extractors "may return cached results", refreshed
  "on a rolling basis" (Bright Data blog, checked 6 Oct 2026). The
  "November 2025" start date in G2 was not found on any page. Two Reddit
  users got the experience field back empty, and Bright Data's own sample
  responses show empty experience and position.
- **Job-alert emails are sampled.** One observed alert said 22 new jobs
  matched but listed only 5, with no description. Good only for finding
  gaps. LinkedIn allows 20 active alerts (G6 and C8, not rechecked; agents
  do not open LinkedIn Help). Observed once.
- **Many LinkedIn jobs mirror employer ATS postings,** so match by company
  and title before paying for a jobs Actor. Inference (C1).
- **Apify terms** (effective 9 July 2026) say business use only. See
  [apify.md](../providers/apify.md).
- A comment count is not comment text. A search result is not a full post.

### What users say (round 3, 6 October 2026)

From reports G10, G12, G15 and G17; the decision-driving lines were
checked on 6 October 2026.

- **HarvestAPI (on Apify):** the most used, about 8 people across Apify
  issues. Complaints: missing known posts, random LinkedIn 500 errors that
  change counts, runs that stall or ignore caps, an empty result billed
  $0.002. One user said their own LinkedIn account was "restricted three
  times this week" while also using the "No Cookies" reactions Actor; the
  cause is unproven and the vendor closed the issue by email. Usable as a
  tested fallback, not a single source.
- **Bright Data:** jobs look good on known URLs in one benchmark run by
  an affiliate site; profiles come back with empty experience fields; no
  real reviews of the posts scraper. See
  [bright-data.md](../providers/bright-data.md).
- **Bebity Jobs:** users report irrelevant and incomplete results before
  the September 2026 rebuild; the rebuild resets the evidence.
- **curious_coder LinkedIn Jobs (Apify):** 168K users and 4.6 stars from
  141 ratings, no cookie field; Store numbers only. The report's first
  pick for a jobs test.
- **Dami, ReefAPI LinkedIn Jobs, SociaVault:** no independent users.
  SociaVault's own 2026 report admits LinkedIn reliability failures.
  ReefAPI's own test says LinkedIn's guest search bottoms out near 451
  unique postings per query (vendor, not rechecked).
- **PhantomBuster** has real users but needs the user's `li_at` cookie.
  Excluded by our rules.
- **ProAPIs customers:** one customer says about $450 of credits was
  refunded when the API shut (Trustpilot, 26 Dec 2025, not rechecked).
- **Buyers:** no case found from 2024 to 6 October 2026 of a passive,
  no-login data buyer being sued, sent a demand, or banned for buying.
  Enforcement has hit suppliers and logged-in automation tools (for
  example a browser extension whose users' accounts were restricted).
  Absence of reports, not proof.

## Rules and risks for this site

- General rules: [shared/rules.md](../shared/rules.md).
- No agent reads LinkedIn pages, the guest jobs endpoint, or LinkedIn search
  directly, even through a search API. No Actor that asks for an `li_at`
  cookie, ever.
- A no-cookie route that runs on the provider's servers removes direct risk
  to the user's account. It does not remove contract risk. **User
  Agreement section 8.2** (effective 3 November 2025) says you may not
  "Copy, use, display or distribute any information (including content)
  obtained from the Services, whether directly or through third parties
  (such as search tools or data aggregators or brokers), without the
  consent of the content owner". The agreement binds anyone who creates an
  account or uses the Services. So a user who holds a LinkedIn account,
  for example for job hunting, is bound by this clause for LinkedIn data
  bought from a vendor. Official doc, read through a [Wayback snapshot](https://web.archive.org/web/20261006060200/https://www.linkedin.com/legal/user-agreement),
  6 Oct 2026 (round 2); Inference for the conclusion, report C10.
- Realistic outcomes for an individual buyer: restriction or closure of
  the user's own LinkedIn account; a GDPR complaint, since the data names
  people; and the vendor vanishing overnight, as Proxycurl's customers
  found. The only customer known to be sued is Perplexity, a large company,
  in Reddit v SerpApi. Inference, report C10.
- **Alert emails from LinkedIn** are a separate case. Parsing an email in
  your own inbox is not accessing the Services, but section 8.2's "use ...
  any information ... obtained from the Services" could arguably reach the
  parsed content. Low risk for private use, untested. Whether to parse
  LinkedIn alerts is part of P10. Inference, reports C8 and C10.
- **Developer AI Policy:** it bans "member data obtained via our Marketing
  APIs" as AI input. It says the rules "don't apply to data ... not retrieved
  via the LinkedIn Marketing APIs". So it does not cover Apify or Bright Data
  output. [Policy page](https://learn.microsoft.com/en-us/linkedin/marketing/developer-ai-policy).
  Official doc, checked 6 October 2026.
- **Vendors get shut down.** The vendor going dark, or being told to delete
  data, is a real risk:
  - hiQ: consent judgment and data deletion, December 2022 (C1, C3).
  - Proxycurl: shut down 4 July 2025 after a settlement with LinkedIn
    ([Nubela post](https://nubela.co/blog/goodbye-proxycurl/)). Judgment
    entered 25 July 2025 per a [secondary source](https://gtm-api.com/proxycurl-alternative).
    Court order not seen.
  - Kaspr: the [CNIL closed its order on 4 March 2026](https://www.cnil.fr/en/closure-order-issued-against-kaspr).
    Kaspr "chose to delete its database and cease all data collection on
    LinkedIn". Official doc.
  - ProAPIs: final judgment on consent "Signed by Judge P. Casey Pitts on
    9/16/2026": a permanent ban on scraping, selling LinkedIn data and
    using fake accounts, plus deletion of scraped data. It also bars the
    defendants from encouraging "others to use third-party products that
    scrape LinkedIn". No customers were named. Court record, [CourtListener
    docket 5:25-cv-08393](https://www.courtlistener.com/docket/71527603/linkedin-corporation-v-proapis-inc/),
    checked 6 Oct 2026 (round 2); scope per The Record and Sigma Law Group.
    Round 3 read the judgment itself: it bars "Encouraging any third
    parties to use or assisting any third parties with using any service
    or product ... that ... scrapes or makes use of scraped LinkedIn
    Data", and requires that defendants have "Permanently deleted all
    LinkedIn Data" (judgment PDF, docket entry 36). It binds the
    defendants only, not their customers or third parties like us.
  - hiQ: on 4 Nov 2022 the court found that "hiQ breached LinkedIn's User
    Agreement both through its own scraping of LinkedIn's site and using
    scraped data". Court record via report C10.
- Zyte's acceptable-use policy forbids LinkedIn scraping (G2). Exclude it.
- No case was found of LinkedIn banning a customer's personal account just
  for buying vendor data (G5). Not found is not proof of safety.
- Post text and profiles name real people. GDPR applies. Keep only what is
  needed.

## Corrections log

| Date | Wrong or overstated claim | What is true | Evidence |
|---|---|---|---|
| 2026-10-06 | C3: never put LinkedIn data into an LLM. | The Developer AI Policy covers only data from LinkedIn's Marketing APIs. | Policy page, 6 October corroboration |
| 2026-10-06 | G5, C3: Proxycurl was under an injunction to delete data and notify customers. | A settlement is confirmed. Injunction terms rest on secondary sources; the order was not seen. | Nubela post; gtm-api.com |
| 2026-10-06 | Old note: Bright Data gives 5,000 monthly credits. | The product page says 5,000 records a month, no card, shared across products. | Bright Data post page, 6 October |
| 2026-10-06 | G6: Bebity costs $1.50 per 1,000 (Free) and $1.25 (Starter). | The live page says "from $1.00 / 1,000". Both may fit; confirm the plan table. | Bebity page, 6 October |
| 2026-10-06 | C1: alert emails rank last; C4, G6: safest baseline. | Read-only mail access never touches LinkedIn, but alerts live on the user's account and are sampled. User decides. | 6 October corroboration |
| 2026-10-06 (round 3) | Bright Data serves cached profile fields "since a November 2025 policy change" (G2). | Caching confirmed; no page gives that date. | Bright Data blog, round 3 check V5 |
| 2026-10-06 (round 3) | HarvestAPI profile search costs $50 per 1,000 profiles (G17). | $50 per 1,000 search-page results; full profiles are $8 per 1,000. | Actor page, round 3 check V2 |
| 2026-10-06 (round 3) | The ProAPIs judgment's "encouraging others" clause could reach our own recommendations (G17). | It binds the defendants only. | Judgment PDF, round 3 check V5 |
| 2026-10-06 | Proxycove: ProAPIs judgment dated 21 or 23 September 2026. | Signed 16 September 2026. | CourtListener docket, round 2 corroboration W05 |
| 2026-10-06 | "No direct exposure" for a buyer of no-login vendor data (our framing). | Section 8.2 reaches data obtained "through third parties" for anyone who holds an account. | User Agreement (Wayback snapshot), round 2 corroboration W05 |

## Open questions

1. Has LinkedIn ever acted against an individual end customer of a
   scraping vendor? None found in round 2. The clause itself is now
   confirmed (see Rules).
2. Did the Proxycurl judgment (N.D. Cal. 3:25-cv-00828) make customers
   delete data? Not found; the ProAPIs judgment named no customers.
3. What share of recent relevant posts does Google-indexed discovery (Dami,
   ScrapeCreators) catch, and how late? Test with known recent posts.
4. What does a current job-alert email contain, and do narrow alerts avoid
   sampling?
5. What share of LinkedIn tech jobs are missing from public ATS feeds? This
   sets whether a paid jobs Actor is needed at all.
6. Answered in [shared/eligibility.md](../shared/eligibility.md):
   what Apify's business-use-only terms mean for a personal user.

## Sources

- Microsoft Learn pages linked above, read 5 and 6 October 2026.
- Apify, Bright Data, CNIL, Nubela pages linked above, read 6 October 2026.
- Deep research rounds 1 and 2 (5 and 6 October 2026; private, not published), reports G1, G2, G5 (main), G6, C1, C3, C8 and C10;
  and both corroboration rounds.
  Report-only claims are marked "not rechecked".
- Earlier notes: [linkedin.md](../../../capabilities/web/social/linkedin.md)
  and follow-up corrections (private, not published).
- Research bundles: see [SOURCES.md](../SOURCES.md).
