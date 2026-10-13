---
created_at: 2026-10-06
updated_at: 2026-10-06
model: claude-opus-5-5
doc_type: spec
status: active
scope: Irish and EU legal picture for reading public platforms
purpose: The legal background behind the rules, in plain English, with each claim labelled and dated. Criminal law, data protection, contracts and platform terms, customer exposure, consumer law, and questions for a solicitor. Not legal advice.
related:
  - path: ./rules.md
    why: The rules this background supports.
  - path: ./eligibility.md
    why: Business-only vendors and the consumer question in detail.
  - path: ../DECISIONS.md
    why: Proposals that rest on this picture.
  - path: ../sites/linkedin.md
    why: LinkedIn's third-party clause and the vendor cases.
---

# Legal picture (Ireland and EU, October 2026)

**User decision, 6 October 2026:** the user chose to go further than this
background advises: robots.txt, ai.txt and CAPTCHAs do not stop a run, and
business-only vendors may be used. This file stays as the record of the
risks; the rules follow the user. See [DECISIONS.md](../DECISIONS.md).

This is research, not legal advice. It explains why the rules in
[rules.md](rules.md) are written the way they are. Labels: Legal
(statute or judgment text), Court record, Official doc, Independent
report, Inference. "Checked" means a primary source was read on
6 October 2026 in the round 1 or round 2 corroboration.

## Bottom line

- **Criminal law is the smallest risk** for polite, logged-out reading of
  pages that do not block us. No Irish or EU court has treated an IP
  block, rate limit, bot check or CAPTCHA as a "security measure", but
  the term is undefined, so deliberately getting round a block is the act
  most likely to be argued as an offence. Treat every block as a stop
  sign.
- **Data protection is the biggest practical risk.** Do not rely on the
  GDPR household exemption for collecting strangers' posts. Plan as if
  GDPR applies.
- **Contract and account risk is real**, mainly through platform terms
  that bind account holders (LinkedIn's third-party clause) or that ban
  automated collection even logged out (Meta).

## 1. Criminal law

- **The offence.** Section 2 of the Criminal Justice (Offences Relating to
  Information Systems) Act 2017: "A person who, without lawful authority
  or reasonable excuse, intentionally accesses an information system by
  infringing a security measure shall be guilty of an offence." Legal,
  checked, [s.2](https://www.irishstatutebook.ie/eli/2017/act/11/section/2/enacted/en/html).
- **"Security measure" is not defined.** Section 1 defines "data",
  "information system", "lawful authority" and others, but not "security
  measure". Legal, checked, [s.1](https://www.irishstatutebook.ie/eli/2017/act/11/section/1/enacted/en/html).
  An academic paper notes the gap was raised in a Dáil debate (report
  C10).
- **Prosecutions.** The first, and the only one found, was a man who
  exploited a parking app (Park Magic, Cork) for about €270 of free
  parking; he admitted "infringing a security measure" during "a
  temporary vulnerability". A classic hack, nothing like scraping.
  Independent report (Irish Examiner, 17 May 2022), checked.
- **No case on blocks or CAPTCHAs** was found in Ireland, Germany, France,
  the Netherlands or Denmark (report C10).
- **The EU Directive** (2013/40/EU, Art. 3) lets states exclude cases
  "which are not minor"; Ireland's s.2 has no such exception. Legal, per
  report C10, not re-fetched.
- **Other countries, for scale** (report C10, not rechecked unless noted):
  - Germany, § 202a StGB, covers data "not intended" for the reader and
    "specially protected". Public posts are intended for everyone, which
    makes it a poor fit for public scraping. Defence commentary: "reading
    open data is not punishable".
  - France, Article 323-1 Code pénal, punishes accessing **or staying in**
    a system fraudulently (the code text was checked). In the Bluetouff
    case (Cass. crim., 20 May 2015) a man was acquitted of access but
    convicted of staying in after he knew the owner did not want him
    there. A site that blocks your IP is saying exactly that. The case
    page itself could not be opened.
  - US: in Reddit v SerpApi (31 July 2026, pleading stage) the court held
    that CAPTCHA and bot detection can be DMCA "access controls" even
    when humans can see the same content. Not Irish law, but the EU has a
    similar anti-circumvention rule (InfoSoc Directive Art. 6) whose
    Irish reach was not researched. Court record via law-firm summary,
    checked.
- **What this means** (Inference): one polite, logged-out request to a
  public page is low risk. Rotating IPs, residential proxies, CAPTCHA
  solving or spoofing to get past a block is materially higher risk, and
  untested. Heavy traffic that degrades a site could fall under s.3
  (hindering a system).

## 2. Data protection (GDPR)

- **Public posts are personal data** when they name or identify people.
  Job ads with recruiter names are too.
- **Household exemption: do not rely on it.** GDPR does not apply to
  processing "by a natural person in the course of a purely personal or
  household activity" (Art. 2(2)(c)). The Court of Justice reads this
  narrowly:
  - Lindqvist (C-101/01, para 47): it covers "only ... activities which
    are carried out in the course of private or family life".
  - Ryneš (C-212/13, paras 29 and 33): the exception "must be narrowly
    construed", and an activity "directed outwards from the private
    setting of the person processing the data" is not purely personal.
  - Jehovan todistajat (C-25/17): note-taking by preachers going door to
    door was "directed outwards" and not covered.
  Legal, checked (curia and BAILII copies).
- **Applied here** (Inference, reports C10 and W05): none of these cases is
  about scraping. But collecting strangers' posts on a schedule is
  directed outward, even if nobody else sees the results. The job-search
  purpose is the closest to private life; technology research that feeds
  a career is further away. **Our earlier line, that a private research
  tool "very probably" falls under the exemption, was too confident and
  is withdrawn.**
- **Retention does not create the exemption.** No court, EDPB or Irish
  DPC text sets a retention period that makes processing "purely
  personal". Short retention helps only once GDPR applies (storage
  limitation). Not found (report C10).
- **If GDPR applies, the user is a small controller** (Inference, using
  EDPB material by analogy):
  - Lawful basis: legitimate interest, which needs a purpose, necessity
    and a balancing test (EDPB Guidelines 03/2026, para 47).
  - Transparency (Art. 14): the EDPB says the "disproportionate effort"
    exception "should not be routinely relied upon" outside research,
    archiving and statistics (para 27).
  - In practice: minimise at collection, delete raw text quickly, keep
    aggregates, keep a one-page record of purpose, sources, basis and
    retention. See [rules.md](rules.md), "Data handling".
- **AI providers are always bound.** Recital 18 says GDPR still applies to
  those "which provide the means for processing personal data" for
  household activities. Legal per report C10, not re-fetched.
- **EDPB Guidelines 03/2026 on web scraping** (adopted 7 July 2026,
  consultation to 30 October 2026) are written for scraping to train
  generative AI. Summarising is outside their stated scope, so they apply
  only by analogy. Key lines, checked:
  - Para 37: exclude sites "which clearly oppose the scraping of their
    content, through the use of technical measures, such as ... robots.txt
    or ai.txt files, or CAPTCHA".
  - Para 45: "the absence or non-applicability of a robots.txt file on a
    web site does not amount to consent".
  [PDF](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_2020603_webscraping_v1_en_0.pdf).
- **Sending posts to US AI services** is a transfer outside the EU if GDPR
  applies. The EU-US Data Privacy Framework stands: the General Court
  dismissed Latombe (T-553/23) on 3 September 2025. The appeal
  (C-703/25 P, lodged 31 October 2025) is pending. Court record, checked.
  Each AI provider's own DPA, DPF listing and retention settings were not
  checked.

## 3. Contracts and platform terms

- **Website terms can bind a scraper, at least for jurisdiction.**
  Ryanair v Billigfluege ([2010] IEHC 47; [2015] IESC 11) held that terms
  shown by a hyperlink bound a commercial screen-scraper well enough to
  give Irish courts jurisdiction. It was "not a full decision on the
  allegation of screen-scraping"; no court ruled on liability. Court
  record via commentary (Mondaq, vLex), checked. A private consumer who
  never clicked "agree" is a weaker case for the platform (Inference).
- **Contract can protect data that database law does not.** Ryanair v PR
  Aviation (CJEU C-30/14, 15 January 2015): a site whose data falls
  outside the Database Directive may still restrict use by contract.
  Legal via report C10, not re-fetched.
- **Holding an account makes terms far stronger** (clickwrap). Inference.
- **Terms that reach us even through a vendor or logged out:**
  - LinkedIn User Agreement s.8.2 (effective 3 November 2025): no copying
    or using information "obtained from the Services, whether directly or
    through third parties (such as search tools or data aggregators or
    brokers)". Binds anyone with a LinkedIn account. Official doc
    (archived copy), checked. See [linkedin.md](../sites/linkedin.md).
  - Instagram Terms, which Threads' terms incorporate: no automated
    collection "without our express permission, regardless of whether
    such automated access or collection is undertaken while logged-in".
    Official doc, checked. See [threads.md](../sites/threads.md).
  - X Developer Agreement: no training of "a foundation or frontier
    model"; delete stored content within 24 hours of a request. Official
    doc, checked. See [x.md](../sites/x.md).
  - Reddit's User Agreement on logged-out automated reading: not found
    (reddit.com blocks fetch tools).
- **US cases, for context:**
  - Meta lost against Bright Data on 23 January 2024 because its terms
    covered "your use" of its products, not logged-off scraping. Meta's
    current Instagram terms now say "regardless of whether ...
    logged-in", which reads as a response. Court record via reports C3
    and C6; Inference.
  - X v Bright Data was stayed for settlement in June 2025 (Independent
    report, checked in round 1).
  - Google's DMCA claims against SerpApi were dismissed on 20 July 2026,
    partly with leave to amend; Google amended on 10 August 2026. Court
    record via news, checked in round 1 and report C6.

## 4. Can a platform pursue the customer of a scraping vendor?

- **Only one customer is known to have been sued:** Perplexity, kept in
  Reddit v SerpApi as a buyer that allegedly set the scraping parameters.
  It is a large company. No individual end user has been named in any
  case found. Court record, checked.
- **Vendors get shut down and told to delete data:** hiQ (2022), Proxycurl
  (2025), Kaspr (CNIL order closed 4 March 2026), ProAPIs (consent
  judgment signed 16 September 2026, which also bars it from encouraging
  "others to use third-party products that scrape LinkedIn"). No
  customers were named. Court record and Official doc, checked. Details
  in [linkedin.md](../sites/linkedin.md).
- **For an individual, the realistic exposure** (Inference, report C10):
  restriction of their own platform account (if they hold one), a GDPR
  complaint, and the vendor vanishing with the data feed.

## 5. Consumer law and business-only vendors

- **Who is a consumer:** "an individual acting for purposes that are
  wholly or mainly outside that individual's trade, business, craft or
  profession"; the trader must prove otherwise. Consumer Rights Act 2022
  s.2 and s.2(3). Legal, checked, [s.2](https://www.irishstatutebook.ie/eli/2022/act/37/section/2/enacted/en/html).
- **A vendor's label does not change that**, but consumer status does not
  force the vendor to keep serving you either.
- **Claiming to be a business you are not** is the classic basis for
  rescission and damages for misrepresentation (Part V of the Sale of
  Goods and Supply of Services Act 1980; section text not re-verified).
  Report C10.
- **Mixed-purpose contracts:** for jurisdiction, the CJEU's Gruber test
  (C-464/01) treats a person as a consumer only if the business purpose is
  negligible; Schrems (C-498/16) lets status change as use changes. The
  Irish "wholly or mainly" test for substantive rights is wider. Legal via
  report C5, not re-fetched.
- The options for the user are in [eligibility.md](eligibility.md).

## 6. Database right, copyright and the AI Act

- **Database right:** a private tool reading listings for one person is
  very unlikely to harm a board's investment (CV-Online v Melons,
  C-762/19; Inference). Republishing full posts is not defensible.
- **Text and data mining:** EU copyright allows it, but rightsholders can
  opt out under Art. 4 of the DSM Directive. Context only (report C6).
- **AI Act:** deployer duties do not apply to purely personal,
  non-professional use (Art. 2(10)). The one hard line: no face
  recognition databases from scraped photos (Art. 5(1)(e)).

## Questions for an Irish solicitor

Worth asking only if the project goes beyond private use, or before a
paid vendor is chosen. First consultations listed by Irish firms cost
about €100 plus VAT to €250 including VAT; a technology and
data-protection specialist will likely cost more, often hourly. Ask for a
fixed fee for a one-hour review and send the questions first.
Independent report (firm price lists, undated), report C10.

1. Does "infringing a security measure" (2017 Act, s.2) cover an IP
   block, rate limit, bot check or CAPTCHA?
2. If a site blocks an IP and one more logged-out request is sent from
   another network, could that be "infringing"? Would "reasonable excuse"
   help?
3. Is there an Irish anti-circumvention rule (InfoSoc Art. 6) that could
   treat CAPTCHAs as "technological measures"?
4. Is collecting strangers' public posts for (a) a job search and (b)
   technology research a "purely personal or household activity"?
5. If not, what lawful basis fits best, and what does Art. 14
   transparency require of an individual controller?
6. Are AI API providers processors here, and is the DPF enough while
   C-703/25 P is pending?
7. Can LinkedIn enforce s.8.2's third-party clause in Ireland against an
   account holder for data bought from a vendor?
8. Are browsewrap terms binding on a consumer who never clicked "agree",
   after Ryanair v Billigfluege? Do the 2022 Act's unfair-terms rules
   touch anti-scraping clauses?
9. What is the exposure for signing up to a "business use only" vendor as
   an individual, and can prepaid fees be withheld?
10. Is parsing one's own job alert emails a breach of any board's terms,
    and is following the links different?
11. Is a separate, labelled research account on Bluesky or Mastodon a
    "fake account" in any legal sense, or only a terms question?
12. What records should be kept now to show good faith?

## Sources

- Deep research rounds 1 and 2 (5 and 6 October 2026; private, not published), reports C3, C5, C6, C10 and G8, and both corroboration
  rounds (round 2 W05 checked the legal quotes).
- Primary sources are linked inline.
