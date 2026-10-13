---
created_at: 2026-10-06
updated_at: 2026-10-11
model: claude-opus-5-5
doc_type: decisions
purpose: User rules, accepted choices, and proposals waiting for the user, for reading public platforms.
related:
  - path: ./spec.md
    why: Owning spec and route table.
  - path: ./STATE.md
    why: Current status and what is blocked on these decisions.
  - path: ./shared/rules.md
    why: The rules in full, with evidence.
---

# Web scraping site access: decisions

Three kinds of entry: **user rules** (set by the user, not to be changed by
an agent), **accepted** (clear from evidence, low stakes, reversible) and
**proposed** (waiting for the user; agents treat them as "not allowed yet").

## User rules

- **No logins, own cookies or fake accounts for scraping.** Standing rule.
- **Agents never read LinkedIn.** Standing rule, also in the web capability
  ("LinkedIn remains excluded from the shared web search/fetch workflow").
  The user's reason: "don't want to get banned."
  Collection and pipelines never touch LinkedIn.
- **Keep the home IP away from sites that block bots; polite pacing.**
  Standing rule.
- **Hard caps on paid tools; never raise a limit without the user.**
- **No account, purchase, connector, scheduled collection or pilot without
  an explicit user decision.** The first pilot ran on 7 October 2026 (see
  the entry below and [STATE.md](STATE.md)).
- **2026-10-05: scraping is a research capability.** Judge platforms and
  providers on coverage, cost and reliability across all research uses,
  not only the job search. Explore multi-site providers such as Apify and
  ReefAPI even where the job case looks weak.

## 2026-10-11: following jobs from alert emails (user rule)

For alert-email triage (11 October 2026) the user
set how agents may read the jobs an alert email lists. This narrows the
earlier "agents never open alert links" line in
[shared/email-alerts.md](shared/email-alerts.md) and makes a scoped
exception to rule 2 in [shared/rules.md](shared/rules.md).

- **Never open the tracking links** in the email. Store them as data.
- **Employer site first.** Find the same job on the employer's careers
  page or ATS by web search, then read that page.
- **Board pages only as a last resort**, through a clean URL built from
  the job id. This includes LinkedIn and other restricted boards (user:
  "allow linked in pages, as well as other restricted sites, but as a last
  resort").
- **Caps per site:** at most 2 page reads a minute on normal sites; on
  high-risk sites (LinkedIn, Indeed, Glassdoor, IrishJobs, Jobs.ie,
  StepStone and similar) 1 a minute and at most 30 an hour. Every route
  attempt counts, including hosted readers that fetch on our behalf.
- **Route order** (user): Codex, Claude, Gemini, Parallel, Firecrawl, then
  headless reading (employer ATS JSON, headless Chrome), then a full
  browser.

Observed results and lessons are in [shared/email-alerts.md](shared/email-alerts.md)
under "Observed run (11 October 2026)".

## 2026-10-07: Tier 0 pilot and first Apify runs (user directed)

The user approved the Tier 0 set ("lets try all of that with the default
tier 0 set") and asked for a minimal Apify test that "doesn't drain" the
free $5. Scope as run:

- **Tier 0, free, no accounts:** Hacker News, Reddit through Arctic
  Shift, employer job feeds (Greenhouse, Lever, Ashby, Workable, Workday,
  SmartRecruiters), Bluesky anonymous reads and Jetstream, Mastodon
  hashtags, Lobsters and DEV, and X's syndication endpoint. Known-item
  tests, 5 to 15 seconds between requests per site, every request from the
  home machine behind the VPN (checked before and during each run; the
  run stops if the home provider shows). Reddit, X and careers pages were
  read through Parallel's servers, except the X syndication endpoint.
  Done by eight OpenCode GLM 5.3 Flash workers, one site each, at the
  user's request.
- **Apify:** the user created a free account. The user asked that Actors be chosen by Store popularity,
  rating and monthly users, "the 1-2 most popular scrapers for each
  tool", naming Reddit, LinkedIn, Glassdoor, X and IrishJobs. 11 runs,
  each capped (10 items, $0.05 to $0.12, 5 minutes); total $0.27.
- **LinkedIn:** the user named LinkedIn, so two no-cookie LinkedIn
  **jobs** Actors ran once. Posts and profiles were not run: the popular
  post Actors use the vendor's LinkedIn accounts and return named
  people's posts (rule 11). This is a one-off test; P10 (ongoing vendor
  use) stays open.

Results: the bundle (private, not published) and each site file's "Observed
test (7 October 2026)" section. Raw responses stay in a temporary folder
for 30 days at most (rule 11) and are not in Git.

## 2026-10-06: renamed again, to web-scraping-site-access (user directed)

The user found "web-scraping" too general: it suggests web scraping as a
whole, while this spec is about specific sites. The agent offered
`site-access`; the user proposed `web-scraping-site-access` and chose it.
"web-scraping" keeps the spec findable by anyone looking for scraping
work; "site-access" says it is per site and covers every route (official
APIs, alerts, vendors), not only scrapers. Path:
`specs/web-scraping-site-access/`, title "Web scraping: site access".

The user also asked whether this overlaps `specs/internet-deep-research`.
It does not: that spec now keeps standalone research apps, their funding
and history, and general search and page-reading facts live in
`capabilities/web`. This spec answers "how do we get data out of this
particular site". Where the two touch (Brave for finding Reddit threads,
for example) one file owns the fact and the other links to it.

## 2026-10-06: renamed from platform-access to web-scraping (user directed; name delegated) (superseded the same day)

The user found "platform" unclear: it did not say the spec is about
getting access to websites. They offered "web site access", "web
scraping", "web scraping per site strategies" and similar, and left the
choice to the agent. Chosen: `specs/web-scraping/`, titled "Web scraping:
per-site access". It is short, says the main job, and pairs with
`capabilities/web` and the `web-search` skill. The spec still covers
official APIs, email alerts and paid providers, not only scrapers.
Rejected: "website" (too broad), "web-site-access" (hides that this is
about scraping), "web-scraping-per-site-strategies" (too long for a
path). All links in the workspace were repointed;
report bodies were left untouched.

The user also set the direction for later: this spec will tie closely to
the web capability, and a route that proves solid gets a lightweight
adapter into the web-search skill instead of staying research only. The
promotion rule is in [AGENTS.md](AGENTS.md).

## 2026-10-06: one spec, one file per site and per provider (accepted, user directed)

The user said the capabilities folder "is going to get stretched thin and
won't scale" and asked for "one spec per site, a spec for shared things".
This spec replaces `capabilities/web/social/` as the home for platform and
provider facts. Each site and provider gets one file from a template; a
file that outgrows about 300 lines becomes its own folder. General search
and page-reading tools stay in `capabilities/web/`. The old social files
are now pointers.

Rejected: a folder per site from day one (too much ceremony for files of
100 to 200 lines); keeping providers in `capabilities/` (they are data
sources we evaluate, not bridges we have wired; when one is wired, its
wiring goes to `capabilities/connectors.md`).

## 2026-10-06: Google Jobs is not a route for Ireland (accepted, evidence)

Google's JobPosting page (updated 8 September 2026) lists 14 European
countries and Ireland is not one; SerpApi's Google Jobs country list has
no Ireland entry. Report C1's plan to pay SerpApi $25 a month for Irish
Google Jobs is dropped. Google Jobs can still serve countries on the list.

## 2026-10-06: Glassdoor is not read separately (accepted, evidence)

Glassdoor merged into Indeed, Inc. on 1 July 2026, has no API
partnerships, and its terms ban automated agents without written
permission. Indeed routes and employer feeds cover its listings. Reverse
only if company reviews or salaries become a research need.

## 2026-10-06: Reddit's official Data API is closed for new projects (accepted, evidence)

Reddit's own post: new public API requests close 31 October 2026, removal
starts 12 January 2027, remaining access ends March 2027. Do not build on
it. See [sites/reddit.md](sites/reddit.md).

## 2026-10-06: Reddit route order is Arctic Shift, then a paid vendor, then search discovery (accepted, evidence)

Round 2 found that the free Arctic Shift archive is current, needs no
key, and serves full comment trees and per-community search. The paid
vendors scrape (RedditAPIs.com says it uses residential proxies) and none
holds a Reddit licence. So the order is: Arctic Shift first, one paid
vendor as a swappable fallback, and a search API for cross-Reddit
discovery. Using any of them still needs pilot permission (P9). Rejected:
a paid vendor as the first route (round 1 view), Devvit (built for apps
inside communities; only OpenAI and Gemini allowed as AI providers).

## 2026-10-06: plan as if GDPR applies (accepted, evidence)

Our round 1 rules said a private research tool "very probably" falls under
the GDPR household exemption. The Court of Justice reads the exemption
narrowly and excludes activity "directed outwards from the private
setting" (Ryneš C-212/13; Lindqvist C-101/01; Jehovan todistajat C-25/17,
checked 6 October 2026). Collecting strangers' posts on a schedule
probably falls outside it. Any collector is designed for data
minimisation, short retention and a written record. See
[shared/legal.md](shared/legal.md).

## 2026-10-06: shared files for cross-site analysis (accepted, user directed)

The user asked for in-depth analysis to be added "as information takes
shape". Round 2 produced four cross-site topics that did not fit one site
or provider file, so each got a file under `shared/`: `legal.md` (moved
out of `rules.md`, which now keeps only the rules), `eligibility.md`
(which providers accept an individual, and the P1 options), `accounts.md`
(research and alert accounts) and `email-alerts.md` (the alert route,
moved out of `evaluation.md`). Rejected: growing `rules.md` past 300 lines
with legal detail.

## 2026-10-06: user decisions on proposals P1 to P15

The user answered the proposals in one message on 6 October 2026. Their
words are quoted where they set a rule. Where they delegated, the agent's
choice is marked "delegated" and can be changed by the user at any time.

| # | Topic | Decision | Effect |
|---|---|---|---|
| P1 | Business-only vendors | "Let's just sign up as a business, simple as that." | Apify (and similar vendors) may be used. The user creates the account. |
| P2 | Residential proxies and anti-detect tools | Delegated. Not used for our own requests; the user's VPN masks the home IP instead. | Rule 12 stays. Vendors may use their own proxies. |
| P3 | Stop rule | Delegated, with the user's override below: errors back off and retry; rate limits wait as asked; a CAPTCHA or login wall skips that page and continues the run. | Rule 7 rewritten. |
| P4 | robots.txt, ai.txt, CAPTCHA | User: "I'm going to be ignoring any robots.txt, AI.txt, and captchas ... Don't stop at that." | Rule 5 rewritten. No paid CAPTCHA-solving service (delegated: cost, and it is the riskiest act legally). |
| P5 | IrishJobs and Jobs.ie | Use the Apify actors, provided results are recent and caching keeps cost down. | Route changes from headless Chrome to Apify. See [stepstone-ireland.md](sites/stepstone-ireland.md). |
| P6 | Research accounts | Delegated, with the user's ranking: "X is the most useful", then Bluesky, then Mastodon ("diminishing returns"). | X and Bluesky accounts, created by the user. Mastodon later, if ever. |
| P7 | Board alert accounts | Yes, and high priority: the user creates the accounts; a browser agent fills each profile and sets up as many alerts as each board allows; mailbox labels keep alerts out of the inbox. | An email digest follows. |
| P8 | Retention | Delegated: raw text kept 30 days, summaries until the research purpose ends, then everything deleted. | Rule 11 updated. |
| P9 | First pilot | Yes, high priority, in this order: Hacker News, Reddit (Arctic Shift), then Apify and ReefAPI free tiers. Skip Brave Search. | Pilot scope set; runs when the user says go. |
| P10 | LinkedIn data from vendors | Not decided. First evaluate the options using genuine user opinions from social media, not vendor sites. | Waits on the social research setup and a follow-up investigation. |
| P11 | Threads | "Let's deprecate threads." | Threads excluded. |
| P12 | X route | Not decided. Gather user opinions first. | Waits on the same follow-up investigation. |
| P13 | Providers and budget | Not decided. Needs a genuine analysis of each provider's reputation from social media (Reddit first): Apify, ScrapeCreators, ReefAPI, TwitterAPI.io, Bright Data. | Follow-up investigation, after Reddit is readable. |
| P14 | Where collectors run | The user's home machine, behind the user's VPN, in a private window with no cookies. | Rule 4 rewritten. |
| P15 | Solicitor | No. | Dropped. |
| | Pacing | "No more than one request every 5 to 15 seconds" per site, out of "empathy for the load on those sites". | Rule 6 rewritten. |

**Why social media comes first.** The user pointed out that vendor
reviews on vendors' own sites can be manipulated, and that genuine user
opinion lives on Reddit, Hacker News and X. So reading those platforms is
the missing pillar, and it is needed before choosing providers (P10, P12,
P13). Reddit first: "by far, and it's not even close, the biggest social
media that we could leverage to get genuine user opinions."

## Still open

| # | What is needed |
|---|---|
| P10 | Evaluate LinkedIn data options from genuine user opinions. |
| P12 | Choose an X route from genuine user opinions. |
| P13 | Choose providers and a budget from a reputation analysis of each. |
