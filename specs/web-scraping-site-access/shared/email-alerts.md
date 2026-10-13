---
created_at: 2026-10-06
updated_at: 2026-10-12
model: claude-opus-5-5
doc_type: spec
status: active
scope: Job alert emails as a route to job boards
purpose: How to use job alert emails as the low-risk route to Indeed, Glassdoor, IrishJobs.ie and Jobs.ie, per-board limits, how to make each email complete, what the terms say, and how to read a mailbox safely.
related:
  - path: ../spec.md
    why: Owning spec and the route table.
  - path: ./rules.md
    why: Rules every route must pass.
  - path: ./accounts.md
    why: Board accounts needed for alerts (proposal P7).
  - path: ./evaluation.md
    why: The overlap test that tells whether a paid board route is worth it.
  - path: ../sites/indeed.md
    why: Indeed-specific facts.
  - path: ../sites/stepstone-ireland.md
    why: IrishJobs.ie and Jobs.ie facts.
---

# Job alert emails as a route

Every big job board refuses automated reading, but every one will email
new jobs to an account holder. Reading those emails in a mailbox the user
controls is the lowest-risk way to see board-only jobs. Alerts are capped
samples, not full feeds, so the design goal is many narrow alerts, each
small enough that its email lists every match. Alerts are a gap detector
next to employer job feeds ([ATS feeds](../sites/ats-feeds.md)), not a replacement for them.

Board accounts and alerts were set up by the user (7 October 2026) and a
first full reading of an alert mailbox ran on 11 October 2026 (see
"Observed run" below). No scheduled digest exists yet. See
[DECISIONS.md](../DECISIONS.md).

## Per-board limits (checked 6 October 2026)

| Board | Account needed | Alert limit | Jobs per email | Frequency | Label |
|---|---|---|---|---|---|
| Indeed | Yes: "You must be signed in to your Indeed account to create job alerts." | Not found | "capped at 30 results per notification" | Daily or weekly; "You won't get a job alert email if there are no new jobs" | Official doc ([help](https://support.indeed.com/hc/en-us/articles/204488890-Starting-Stopping-and-Managing-Job-Alerts), checked 6 Oct 2026). The 30 cap is from Indeed's "I only see 30 results" article via a search snippet (report C8); the page refused a direct fetch. |
| Glassdoor | Yes; Indeed logins work | "a maximum of 10 job alerts per day" (a creation limit; no total cap found) | Not found | Daily or weekly; weekly starts a week later | Official doc ([help](https://help.glassdoor.com/articles/en_US/Article/Job-Alerts-on-Glassdoor), search excerpt, 6 Oct 2026) |
| IrishJobs.ie | Yes (a jobseeker account is created with the first alert) | "narrowed down to three" | Not found | "Job Alerts emails will be sent daily." Instant alerts switch off after 45 days without a search. | Official site (article dated March 2023, checked 6 Oct 2026, [notice](https://www.irishjobs.ie/careeradvice/get-ready-for-the-all-new-irishjobs/)) |
| Jobs.ie | Yes ("the Job Alerts section of your account") | Not found; same Stepstone group account, so probably three | Not found | Daily | Official site, report C8; not rechecked (page moved) |
| LinkedIn | Yes | 20 at once (LinkedIn Help, per report C8) | Truncated: a real sample listed 5 of "22 new jobs" | Daily or weekly | Report C8 only. Agents never read linkedin.com, so this was not rechecked. Whether to parse LinkedIn alerts at all is part of proposal P10. |

Glassdoor runs on Indeed's feed ("a comprehensive feed delivered to the
Indeed Platform, which includes ... Glassdoor", Indeed Apply terms, report
C8), so 2 to 4 Glassdoor alerts are enough as a cross-check.

## Design: make every email complete

- **Narrow alerts.** One role family per place: for example one
  job title in one city, plus remote variants. Inference, report C8.
- **Truncation detector.** Compare the "N new jobs" headline with the
  number of job cards in the email. If fewer are listed, split that alert.
  Inference, report C8.
- **IrishJobs and Jobs.ie get three alerts each**, which is too few to be
  complete. That is why [stepstone-ireland.md](../sites/stepstone-ireland.md)
  keeps a paid actor as a candidate.
- **Filter out "recommended jobs" emails.** Indeed sends those separately
  and they can be switched off (Indeed Terms of Service, 17 July 2026,
  report C8). They are not alert results.
- **Dedupe** on normalised company, title and city across all sources,
  then match against employer feeds. Inference.

## What the terms say about reading alert emails

- No board's terms that were read forbid parsing alert emails delivered
  to your own inbox. Official doc for what was read; Inference for the
  conclusion (report C8, IrishJobs terms rechecked 6 Oct 2026).
- Indeed's "Site" definition includes "email messages, notifications, and
  other messages", and the job seeker licence is for the "personal,
  non-commercial purpose of seeking employment". The only explicit
  automation ban read covers Indeed Apply. So parsing alerts for one's
  own job search sits inside the licence. Official doc (Indeed ToS, last
  updated 17 July 2026, via report C8) plus Inference.
- IrishJobs: "Content on the IrishJobs.ie website can be downloaded for
  personal non-commercial use" (section 16), but 4.5.2 needs "prior
  written permission" for other use and 4.8.3 bans competing use. Sharing
  or publishing the data leaves the safe zone. Official doc, checked
  6 Oct 2026, [terms](https://www.irishjobs.ie/about/terms-and-conditions).
- **Following the links is different.** An automated request to a job
  page or tracking link is software accessing the board's site, which the
  terms cover. It also exposes the home IP and can cost employers money,
  because Indeed bills some employers per click. So agents never open
  alert links. Store title, company, location, job ID and the raw URL; a
  person opens links by hand. Inference, reports C8 and C10.
- **Updated 11 October 2026 (user rule):** agents still never open the
  tracking links, but may read the job itself: employer site first, board
  page by clean job-id URL only as a last resort, under per-site caps. See
  [DECISIONS.md](../DECISIONS.md#2026-10-11-following-jobs-from-alert-emails-user-rule).

## Reading the mailbox

- Use a dedicated mailbox or label for alerts, read-only access, and only
  the alert senders.
- Gmail API: `gmail.readonly` is a restricted scope ("If you store
  restricted scope data on servers (or transmit), then you must go
  through a security assessment"). Google's verification is not needed
  for a personal-use app: "An app is considered to be for personal use if
  it's not shared with anyone else or will be used by fewer than 100
  people (all of whom are known personally to you)." Official doc,
  checked 6 Oct 2026, [scopes](https://developers.google.com/workspace/gmail/api/auth/scopes),
  [OAuth policies](https://developers.google.com/identity/protocols/oauth2/policies).
- Apps left in "Testing" status get 7-day authorisations, so tokens
  expire weekly. Independent report, report C10, not rechecked.
- Google's Limited Use rules restrict passing restricted-scope data to
  third parties. Read them before sending email text to an AI service.
  Not checked in round 2.
- Legal and account risk of reading your own alert emails: low (report
  C10). Risk starts when software follows the links.

## Observed run (11 October 2026)

One real mailbox of alert emails, read in full, plus a sample of the
listed jobs followed to their pages under the 2026-10-11 rule in
[DECISIONS.md](../DECISIONS.md#2026-10-11-following-jobs-from-alert-emails-user-rule).
Run detail is private, not published. Observed test unless marked.

**What each board's email contains**

| Board | Jobs per email | Truncated? | Salary | Description | Job id in email | Links |
|---|---|---|---|---|---|---|
| LinkedIn | 5 to 6 cards | Yes, often: most digests list fewer cards than the headline (up to "30+") | Rarely, only in the preview line | None | Yes, `/jobs/view/<id>` | Tracking query on every link |
| Indeed alert | Up to about 20 | No: headline matches cards | Often | Short snippet | `jk=` only in some emails | Very long opaque tracking links |
| Indeed "match" | 1 | No | Sometimes | Short snippet | No | Opaque tracking links; language follows the account's country |
| Glassdoor | About 7 to 10 | Unknown: no headline count; subject "and N more" undercounts | Rarely | None | Sometimes (`jobListingId`) | Tracking links |
| IrishJobs | 10 | No | Range or "Not disclosed" | One line, cut off | No | Tracking token changes every email |

**Lessons**

- **LinkedIn truncation is the main loss.** A digest shows about six jobs
  whatever the headline says. Narrow alerts are the only fix inside email.
- **Heavy repeats.** Many cards are repeats: about 1.8 cards per distinct
  job overall. Glassdoor and IrishJobs repeat the same jobs daily across
  alerts (several cards per distinct job). Dedupe on company,
  title and city.
- **Same sender, non-job mail.** Glassdoor sends community posts, terms
  notices and "how is your search going" mail from the alert address; LinkedIn
  and Indeed send "alert created" mail (Indeed's also lists jobs).
- **IrishJobs matches OR terms loosely**, so query wording barely steers
  results. Inference from the result mix.
- **Following jobs worked without touching tracking links.** Web search
  found an employer page for most jobs; about 94 percent of page reads
  succeeded. The route that won most often was Codex, then Claude, then
  Gemini, Parallel, and one-offs for Firecrawl, ATS JSON and headless
  Chrome. Codex cannot read
  JavaScript-only pages (Ashby, Workday, iCIMS); the next routes can.
  Clean board URLs from the job id worked for LinkedIn, Indeed and
  IrishJobs as a last resort, signed out, under the caps.
- **Answers to the old open questions:** question 1 is answered by the
  table above. Questions 2 and 3 were not tested.

## Open questions

1. Is the IrishJobs three-alert limit still current? The notice is from
   2023.
2. What is the Jobs.ie alert sender and limit?
3. Does any LinkedIn alert setting raise the six-card limit per digest?

## Sources

- Deep research round 2 (6 October 2026; private, not published),
  reports C8 and C10, and the round 2 corroboration (W04, W05).
- Primary pages listed inline, accessed 6 October 2026.
