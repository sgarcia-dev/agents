---
created_at: 2026-10-06
updated_at: 2026-10-06
model: claude-opus-5-5
doc_type: spec
status: active
scope: Separate research accounts and board accounts
purpose: When an account is the platform's own sanctioned route, which account each platform would need, and how to run one honestly. Nothing here is approved; proposals P6 and P7 decide it.
related:
  - path: ./rules.md
    why: Rule 1 (no logins or own cookies for scraping) and its one exception.
  - path: ../DECISIONS.md
    why: Proposals P6 (research accounts) and P7 (board accounts for alerts).
  - path: ./email-alerts.md
    why: How board accounts would be used.
  - path: ./legal.md
    why: Platform terms on accounts and automated collection.
---

# Research and alert accounts

Our standing rule is no logins, own cookies or fake accounts for scraping.
The one exception is an account that **is** the platform's own sanctioned
route: an API key, an app password, a developer app, or an alert
subscription. Those are not scraping; they are how the platform asks to
be read. Even so, each needs a user decision before it exists (proposals
P6 and P7 in [DECISIONS.md](../DECISIONS.md)).

## Per platform

| Platform | Account needed for | Sanctioned route | Rules that matter | Worth it? |
|---|---|---|---|---|
| Bluesky | Keyword search only (reads need none) | App password on a separate account; create one session and reuse it (`createSession` allows about 10 a day) | Guidelines ban accounts used "to evade bans, suspensions, or other enforcement actions"; no rule against a second account found. Bots should self-label. Official doc, checked 6 Oct 2026 | Yes, if Bluesky search matters |
| Mastodon | Keyword search for posts; streaming; bigger threads | User token with `read:search` on one server | Each server's own rules; some forbid research or bots. Set the bot flag; never post AI summaries from it. Official doc and report C7 | Only on a server whose rules allow it; hashtags need no account |
| X | Any official API use | Developer app on an X account, verified phone, card, prepaid credit | "Each purchase of a Paid Service applies to a single X account"; pay-per-use is for "hobbyists" and prototyping. Official doc, checked 6 Oct 2026 | Yes, if X is worth about $25 a month |
| Threads | Official keyword search | Meta developer app plus Threads account | Searching other people's posts needs Business Verification. Official doc, checked 6 Oct 2026 | No: the account alone unlocks nothing useful |
| Reddit | Official API | Registered app with approval | Requests close 31 Oct 2026; access ends March 2027 | No |
| LinkedIn | Nothing; agents never read LinkedIn | n/a | Holding a LinkedIn account is what makes the User Agreement's third-party clause bind the user (see [linkedin.md](../sites/linkedin.md)) | No research account |
| Indeed, Glassdoor | Job alert emails | Jobseeker account; Glassdoor accepts Indeed logins | Alerts need sign-in; 30 jobs per email on Indeed | Yes for alerts (P7) |
| IrishJobs.ie, Jobs.ie | Job alert emails | Jobseeker account, group-wide across Stepstone boards | Three alerts per account | Yes for alerts (P7) |
| Mailbox | Reading alerts | Dedicated mailbox or label; read-only OAuth app for personal use | `gmail.readonly` is restricted; personal-use apps (fewer than 100 known users) skip Google verification | Yes, if alerts are approved |

## How to run a research account honestly

- **Separate, never the user's own.** A new account made only for this
  purpose, with its own email address.
- **Truthful profile.** Say it is an automated, read-only research
  account. Set the platform's bot flag or self-label where one exists
  (Bluesky, Mastodon).
- **Read only.** Never post, reply, follow, like or message from it. If
  a platform's API requires a follow to read, do not use that route.
- **Never to evade enforcement.** If a platform limits or bans the
  account, stop. Do not create another one.
- **One per platform.** No sock puppets, no rotation between accounts.
- **Credentials stay private.** App passwords, tokens and API keys live
  only in a secret store, never in this repository, in prompts or in logs.
- **Revocable.** Prefer app passwords and scoped tokens that can be
  revoked without touching the account itself.
- **Respect the session limits.** Create a session once, save it, refresh
  it; do not log in on every run.

## Sources

- Deep research rounds 1 and 2 (5 and 6 October 2026; private, not published), reports C1, C7, C8 and C10, and both corroboration rounds.
- Platform pages are linked in each site file.
