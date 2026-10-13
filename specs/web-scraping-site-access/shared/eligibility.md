---
created_at: 2026-10-06
updated_at: 2026-10-06
model: claude-opus-5-5
doc_type: spec
status: active
scope: Which data providers will serve an individual, and the user's options
purpose: One place for the question that blocks every paid route (proposal P1). Which providers' terms accept a private individual in Ireland, what the two research reports disagree on, and the options for the user to choose from.
related:
  - path: ../spec.md
    why: Owning spec and provider table.
  - path: ../DECISIONS.md
    why: Proposal P1 waits on this.
  - path: ./legal.md
    why: Irish consumer law and misrepresentation, in more depth.
  - path: ../providers/apify.md
    why: Apify terms in full.
  - path: ../providers/bright-data.md
    why: Bright Data terms in full.
  - path: ../providers/reefapi.md
    why: ReefAPI terms and operator gaps.
---

# Who will serve an individual

Every paid route here runs through a provider. The research question is
simple: will the provider's own terms accept a private person in Ireland
with no registered business? This file answers it per provider and lays
out the user's options. **Decided 6 October 2026 (P1):** the user chose to
sign up as a business ("simple as that"); see
[DECISIONS.md](../DECISIONS.md).
This is not legal advice.

## Short answer (6 October 2026)

- **Say no to individuals in writing:** Apify, Bright Data, ScrapingBee,
  ScraperAPI (one of its two terms pages), Oxylabs (company KYC).
- **Accept individuals:** the official X API ("hobbyists"), SerpApi (no
  business clause), Firecrawl ("the person or entity", but it restricts
  commercial use), Decodo (licence names personal use; not rechecked in
  round 2), ReefAPI (no business clause, but no named operator).
- **Unknown:** TwitterAPI.io, SocialData, RedditAPIs.com, ScrapeCreators,
  Data365, EnsembleData, TheirStack, Zyte, ScrapingDog. Their terms on
  individuals were not found.
- Free official routes need no provider at all: Hacker News, Bluesky,
  Mastodon, employer job feeds, and Arctic Shift for Reddit.

## Provider table

Labels: Official doc unless marked. "Checked" means read on 6 October 2026
in the round 2 corroboration.

| Provider | Accepts an individual? | Exact words | Terms date | File |
|---|---|---|---|---|
| Apify | No on paper; any adult can sign up | "The Services are intended for business use only and are not designed, marketed, or suitable for consumers." "Personal Accounts must be created by humans, and you must be at least 18 years old." | Effective 9 July 2026, checked | [apify.md](../providers/apify.md) |
| Bright Data | No | "Personal projects, such as scraping for a hobby or a side project, are not approved." KYC only for "registered businesses" with a company email domain. Licence "solely for the purpose of Client's internal business operations". | Licence modified 17 June 2026, checked | [bright-data.md](../providers/bright-data.md) |
| ScrapingBee | No | "Use of the API or the Services for personal purposes is strictly forbidden." | 15 July 2024, checked | [scraping-apis.md](../providers/scraping-apis.md) |
| ScraperAPI | Conflicting | scraperapi.com: "This Platform is for use by businesses and not consumers". A Traject Data copy: for "individuals who purchase a Subscription", "personal use". | 10 and 18 Nov 2025, checked | [scraping-apis.md](../providers/scraping-apis.md) |
| Oxylabs | Effectively no | "Every customer has to answer a KYC questionnaire"; "Only 75% of customers are approved"; asks for a registered company name. | Undated, checked | [scraping-apis.md](../providers/scraping-apis.md) |
| X official API | Yes | Pay-per-use is "designed for hobbyists, commercial prototyping"; company wording applies only "on behalf of a company". Verified phone needed. | 27 April 2026, checked | [x.md](../sites/x.md) |
| SerpApi | Yes, no business clause | Users must be "at least the age of majority"; may "refuse service to anyone". | Undated, checked | [serpapi.md](../providers/serpapi.md) |
| Firecrawl | Yes as a party; commercial use limited | Agreement with "the person or entity"; may not "Use the Services for any commercial purposes except as expressly authorized by Firecrawl". | 5 Nov 2024, checked | Page reader; see [capabilities/web](../../../capabilities/web/README.md) |
| Decodo | Yes | Licence names research, personal and commercial use. | Report G2, not rechecked | [scraping-apis.md](../providers/scraping-apis.md) |
| ReefAPI | Yes on paper | No business clause; "You are solely responsible for how you use the data you retrieve". No company named anywhere. | 16 Sep 2026, checked | [reefapi.md](../providers/reefapi.md) |

No public report was found of any of these providers closing an
individual's account for not being a business (report C5). "Not found" is
not proof it never happens.

## The disagreement: can the user sign up to Apify honestly?

Both round 2 reports quote the same Apify clause and the same Irish law.
They reach different views.

- **Report C5: yes, as a professional user.** "Personal Account" is just
  Apify's login for any human. Apify does not define "business use".
  Tracking what developers discuss, done by a working software developer,
  is research for one's profession. On that reading the use is linked to
  the profession, so the user is not a consumer and fits the clause. Sign
  up as what you are, a software developer doing professional research; never claim to be a hobby or private user.
- **Report C10: risky, because on the stated purposes the user is a
  consumer.** Under the Consumer Rights Act 2022, a consumer is "an
  individual acting for purposes that are wholly or mainly outside that
  individual's trade, business, craft or profession", and the trader must
  prove otherwise (s.2(3); Legal, checked 6 Oct 2026). If the main
  purposes are personal projects and personal research, ticking
  "business" is a false statement that induced the contract, which is the
  classic basis for misrepresentation. The realistic outcome is account
  closure without refund, not a lawsuit.
- **What would settle it** (round 2 corroboration W05):
  - Which purpose is the main one, by share of use.
  - Whether the research feeds paid or professional work (consulting,
    writing, an employer).
  - What Apify's signup form actually asks the user to declare.
  - Whether Apify defines "business use" anywhere else.
  - A written answer from Apify itself.
- **Two points both reports agree on:** a vendor's label does not decide
  consumer status, and being a consumer does not force a vendor to keep
  serving you.

## Sole trader registration

- Registering for income tax as a sole trader with Revenue is free;
  registering a business name costs €20 online. It brings a yearly Form 11
  return and preliminary tax. Official doc (Citizens Information) and
  Independent report, report C5, not rechecked.
- It does not give a company email domain, so it does not meet Bright
  Data's KYC on its own.
- Both reports say: register only for real trading (for example
  freelance work). Registering just to pass a vendor's gate makes the
  "business" claim itself weak. Inference, reports C5 and C10.

## Options for the user (P1)

Not ranked as a recommendation; each has a cost.

| Option | What it means | Unlocks | Cost or risk |
|---|---|---|---|
| A. Ask Apify first | The user emails legal@apify.com (the notice address in s.16.5.2), describes the use plainly, and keeps the reply. Report C5 drafted the question. | A clear yes or no for the largest actor marketplace | One email; outward contact is the user's call |
| B. Professional-user signup | Sign up to Apify describing the use as professional research, never as hobby or private use. | Apify actors (Irish boards, long-tail sites) | Misrepresentation risk if the main purpose is personal (C10); account closure; consumer rights given up |
| C. Individual-friendly providers only | Use only routes whose terms accept individuals: free official APIs, Arctic Shift, the official X API, SerpApi or Brave for discovery, ReefAPI free credits, Decodo if rechecked. | Most social sources; not the Irish boards' actors | ReefAPI has no named operator; Irish boards stay on email alerts |
| D. Real business | Register as a sole trader only if the user starts genuine freelance or consulting work, then sign up honestly as that business. | Apify and possibly others; not Bright Data without a company domain | Tax filings; only honest if the trading is real |
| E. No paid providers | Free official routes, alerts and employer feeds only. | Everything free | Gaps: Irish boards beyond three alerts each; no X at all |

## Sources

- Deep research round 2 (6 October 2026; private, not published),
  reports C5 and C10, and the round 2 corroboration (W03, W05).
- Primary pages are linked in each provider file.
