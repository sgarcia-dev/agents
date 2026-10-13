---
created_at: 2026-10-06
updated_at: 2026-10-06
model: claude-opus-5-5
doc_type: spec
status: active
scope: Access, legal and data rules for every platform route
purpose: The rules every route must pass, the risk ladder, a short Irish and EU legal picture, vendor terms, and data handling. Not legal advice.
related:
  - path: ../spec.md
    why: Owning spec and route table.
  - path: ../DECISIONS.md
    why: Which rules the user set and which are proposed.
  - path: ./evaluation.md
    why: How to test a route once it passes these rules.
  - path: ./legal.md
    why: The legal background behind these rules, in depth.
  - path: ./eligibility.md
    why: Which providers accept an individual.
  - path: ./accounts.md
    why: The one exception to rule 1, run honestly.
---

# Access, legal and data rules

These rules apply to every route in this spec. The user decided them on
6 October 2026 (see [DECISIONS.md](../DECISIONS.md)); where the user delegated,
the rule says so. This is not legal advice. The legal background, with
sources, is in [legal.md](legal.md). Several rules below go further
than that background advises; that is the user's informed choice.

## The rules

1. **No logins or own cookies for scraping.** (User rule.) Collection runs
   signed out. Never paste a session cookie into a third-party tool or
   actor. Accounts the user creates are used only for their sanctioned
   purpose: an API key, a Bluesky app password, job alerts and the
   jobseeker profile. How to run a research account:
   [accounts.md](accounts.md).
2. **Agents never read LinkedIn directly.** (User rule: "don't want to get
   banned".) No direct requests, no browser automation on LinkedIn, no
   logged-in tools. Buying LinkedIn data from a vendor is not decided yet
   (P10): the options are evaluated first from genuine user opinions. See
   [sites/linkedin.md](../sites/linkedin.md).
   Scoped exception (user rule, 11 October 2026): when following jobs from
   alert emails, a signed-out LinkedIn job page may be read as a last
   resort, at most 1 a minute and 30 an hour. See
   [DECISIONS.md](../DECISIONS.md#2026-10-11-following-jobs-from-alert-emails-user-rule).
3. **Signed out, no accounts, no CAPTCHA solving services.** Collection
   never logs in to get past a login wall, and never buys a CAPTCHA-solving
   service (delegated choice: cost, and paid solving is the act most
   likely to be argued as getting round a security measure; see
   [legal.md](legal.md)).
4. **Own requests run from the home machine, behind the user's VPN.** (User
   decision P14.) Signed out, in a private browser context with no cookies.
   A VPN moves any block onto the VPN's address instead of the home IP. It
   does not prevent blocks: VPN addresses are shared and are often flagged
   by bot protection already. Where a site keeps blocking, use a provider
   that runs on its own infrastructure (for example an Apify actor) rather
   than fighting the block.
5. **robots.txt and ai.txt are not stop signals.** (User decision P4: "I'm
   going to be ignoring any robots.txt, AI.txt, and captchas ... Don't stop
   at that.") A CAPTCHA does not stop the run: skip that page, wait
   longer before the next request to that site, and carry on with other
   work. Record skipped pages so they can be read another way.
6. **Pacing: one request every 5 to 15 seconds per site.** (User rule:
   "no more than one request every 5 to 15 seconds", out of "empathy for
   the load on those sites".) Randomise the gap inside that range, one
   request at a time per site, and honour Retry-After when it asks for
   longer.
7. **Back off on errors.** (Delegated.) Temporary error: retry up to three
   times with growing gaps. Rate limit (429): wait as long as the site
   asks. CAPTCHA or login wall: skip the page (rule 5). If a site refuses
   every request for a whole run, mark it blocked in the run report and
   move it to a provider route.
8. **Official and open routes first.** Official API or open protocol, then
   RSS and employer feeds, then email alerts, then a paid provider, then
   our own requests. Cheapest and most robust first.
9. **Vendors.** (User decision P1.) Business-only vendors such as Apify
   may be used; the user signs up as a business. A vendor still does not
   move legal risk off us, and platforms have sued vendors' customers
   (Reddit v SerpApi). Which vendors to pay is open (P13). See
   [eligibility.md](eligibility.md).
10. **Hard caps on anything paid.** (User rule.) Spend limits set before
    the first call; never raise a limit without the user.
11. **Keep it private and small.** (Delegated, P8.) Nothing collected is
    published or shared. Raw text is kept 30 days; summaries and links
    until the research purpose ends; then everything is deleted. No profiles of
    named people; no face matching. See "Data handling".
12. **No residential proxies and no anti-detect tools for our own
    requests.** (Delegated, P2.) The VPN is the mask. Vendors may use their
    own proxy networks.

## Risk ladder

Lowest risk first. "Allowed today" reflects the rules above and the gates
in [DECISIONS.md](../DECISIONS.md).

| Route | Legal risk | Account risk | Allowed today |
|---|---|---|---|
| Official API used within its terms | Low | Low (key tied to us) | After pilot permission |
| Open protocol (Bluesky AT Protocol, HN Firebase) | Low | None | After pilot permission |
| RSS feeds, public employer job feeds | Low | None | Yes, with polite pacing |
| Email alerts in an inbox the user controls | Low | Normal account terms | Yes (P7); the user creates the board accounts |
| Search-engine discovery, then a page reader | Low to medium | None | Yes for public pages, never LinkedIn |
| Third-party API or actor on provider IPs, no cookies | Medium: terms, supply-chain suits | Low | Yes for the pilot (P9) and the Irish boards (P5); which vendors to pay long term is open (P13) |
| Own plain HTTP from home, behind the VPN | Low on friendly sites; medium on hostile ones | VPN IP bans | Yes, with rules 4 to 7 |
| Headless browser from home, behind the VPN | Medium to high on hostile sites (looks like dodging bot checks) | VPN IP bans | Yes, with rules 4 to 7; prefer a provider where a site keeps blocking |
| Residential proxy, anti-detect | High | Medium | No (P2, delegated) |
| Logged-in scraping, own cookies | High | Very high | Never |

## The legal picture in brief

The full picture, with sources, is in
[legal.md](legal.md). In one paragraph: polite, logged-out
reading of pages that do not block us is low criminal risk; getting round
a block is the risky act. Do not rely on the GDPR household exemption for
collecting strangers' posts; plan as if GDPR applies. Website terms can
bind a scraper, and terms bind account holders much more strongly. A
buyer of scraped data can be drawn into a platform's lawsuit.

## Vendor terms

Which providers accept a private individual, with exact quotes, and the
user's options, are in
[eligibility.md](eligibility.md). In short: Apify, Bright Data,
ScrapingBee and Oxylabs are for businesses; the official X API, SerpApi,
Firecrawl and ReefAPI accept individuals; many smaller vendors are
unknown. No paid scraping vendor is used until the user decides (P1).

## Data handling

- Keep the minimum: link, IDs, timestamps, a short summary. Drop
  usernames, photos and sensitive content (health, politics, religion,
  sexuality) unless the task needs them.
- Delete raw post text after 30 days (P8). Keep summaries, links and
  trend counts until the research purpose ends, then delete everything. Short retention does not make GDPR go away, but it is
  what GDPR asks for if it applies.
- Strip emails and phone numbers at collection, and drop usernames,
  handles and profile links unless the task needs them (EDPB Guidelines
  03/2026, para 38, by analogy).
- Keep a one-page record of purpose, sources, lawful basis (legitimate
  interest), retention and deletion. If the household exemption does not
  apply, this is the accountability evidence. **Proposed** (report C10).
- Honour deletions where a platform's terms require it. X requires
  deleting or updating stored content "as soon as reasonably possible"
  and within 24 hours of a request; Reddit asks API users to remove
  deleted content. Store IDs and summaries rather than full text where
  possible, so a weekly recheck stays cheap.
- Do not build profiles of named people. Do not collect profile photos.
- Before sending collected posts to an AI service, use one whose API
  terms say it does not train on inputs, with the shortest retention
  available. X bans using its content to train a foundation or frontier
  model, so this matters for X data in particular.
- Filter out special-category content (health, politics, religion,
  sexuality) before sending anything to an AI service (EDPB Guidelines
  03/2026, paras 68 to 74, by analogy; report C10).
- Nothing collected is published, shared in a public dashboard or sold.

## Questions for a solicitor

Twelve questions, and what a first consultation costs, are in
[legal.md](legal.md).

## Sources

- Section 2, 2017 Act: https://www.irishstatutebook.ie/eli/2017/act/11/section/2/enacted/en/html (checked 6 Oct 2026)
- EDPB Guidelines 03/2026 PDF: https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_2020603_webscraping_v1_en_0.pdf (checked 6 Oct 2026)
- Reddit v SerpApi ruling summary: https://www.lexology.com/library/detail.aspx?g=a4fa98e5-85cf-4f8a-a98d-2d9d2ccc7c53 and docket https://www.courtlistener.com/docket/71720563/reddit-inc-v-serpapi-llc (checked 6 Oct 2026)
- Google v SerpApi: https://mlq.ai/news/googles-dmca-case-against-serpapi-narrows-after-court-rejects-claims-over-uncopyrighted-search-results (checked 6 Oct 2026)
- X v Bright Data stay: https://legalnewsfeed.com/2025/06/23/x-corp-and-bright-data-near-settlement-in-data-scraping-antitrust-case (checked 6 Oct 2026)
- LinkedIn Developer AI Policy: https://learn.microsoft.com/en-us/linkedin/marketing/developer-ai-policy (checked 6 Oct 2026)
- Vendor terms: see [eligibility.md](eligibility.md).
- Research: deep research rounds 1 and 2 (5 and 6 October 2026; private, not published), reports C3, C5, C10, G8, G5 section 3 and G1 section 4, and both corroboration rounds. See [SOURCES.md](../SOURCES.md).
