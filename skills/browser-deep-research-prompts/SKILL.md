---
name: browser-deep-research-prompts
description: Use when the user wants a set of deep research prompts (to learn how to proceed on a topic) that browser agents run in the ChatGPT and Claude websites, then export into one grouped folder in ~/Downloads. Always asks how many prompts, then gives a scored mode-fit report (ChatGPT Extra High, ChatGPT 6 Pro, Claude Research) and waits for approval. Never uses ChatGPT Deep research.
created_at: 2026-10-05
updated_at: 2026-10-09
model: claude-opus-5-5
doc_type: skill
purpose: Write ready-to-paste deep research prompt packs with fire-and-forget start files and separate export files for browser agents.
related:
  - path: ../chatgpt-browser/SKILL.md
    why: Website steps and export details for chatgpt.com.
  - path: ../claude-browser/SKILL.md
    why: Website steps and export details for claude.ai.
---

# Browser deep research prompts

Use when the user wants to learn more before deciding something, and wants
ChatGPT (Chat at Extra High or 6 Pro) and Claude Research (on the websites,
run by a browser agent such as a Chrome extension) to do the reading.

**Never use ChatGPT's Deep research mode. No exceptions.** It scored lowest
on every task type tested (spec, B1 to B3). Do not offer it, even if an
older pack or reference mentions it. You write the prompts and
the runner files. You do not run the research yourself.

## 0. Ask first: how many, and on which provider

Rules and the current mode verdict live in
the browser-deep-research spec; its
`BENCHMARKS.md` holds the evidence. Read the spec's mode table before
recommending a mode.

**Optional benchmark.** When asking the size, also offer: "Run a quick
benchmark first?" (one prompt in several modes, scored and logged). Only
run one if the user says yes; follow the spec's benchmark section and log
the result in its `BENCHMARKS.md`.

Every report uses the user's ChatGPT or Claude quota, so never pick the size
yourself. Before writing any prompt, propose three sizes and wait for the
user's choice:

| Size | Typical shape |
|---|---|
| Short | 1 to 3 topics on ChatGPT. Claude copies only where the fit report favours Claude and the user's 5-hour window allows. |
| Medium | About 4 to 6 ChatGPT prompts, plus Claude copies of the 1 or 2 most critical ones. |
| Complete | About 8 to 10 ChatGPT prompts, plus 2 or 3 Claude prompts on only the critical or sensitive questions. |

For each size, list the topics you would cover and which ones would get a
Claude copy, so the user can move topics in or out.

### Mode-fit report (required, then wait for approval)

After the user picks the size, and before writing any prompt, give a short
report that scores each option 0 to 100 for fit, per prompt (or per group
of similar prompts):

| Option | Notes |
|---|---|
| ChatGPT Chat at **Extra High** | The explorer. Finds leads others miss, commits to a view, faster, lighter allowance. Can overreach; check before acting. |
| ChatGPT Chat at **6 Pro** | The careful one. Most accurate, best sources, flags doubt. Can over-hedge. Scarcest ChatGPT allowance. |
| **Claude Research** (say the model and effort; default Opus at Low) | Plain, decision-ready answers that follow the brief; most new angles per minute; strong on legal and risk questions. Can drop a rule's conditions in its summary. Opus Low and Sonnet Medium each won one B3 question. Costs the 5-hour window. |

Score from the spec's "Choosing a mode" guide: the task type, how costly a
wrong claim is, whether fresh sources matter, and cost (time and allowance).
For each option give the score, one line on why it fits, one line on the
main risk, and its cost. Then recommend one option per prompt, plus a split
when the decision is important enough to pay for two runs. A second run
adds facts more than coverage, and in B3 mixed-provider pairs (a ChatGPT
chat plus Claude) complemented each other better than 6 Pro plus Extra
High. If every run is likely to miss the same thing, suggest a targeted
follow-up prompt instead of a second full run.

**Ask about Claude's window.** Claude has a 5-hour rolling usage window on
top of a weekly limit; ChatGPT does not. One Claude Research run at Low uses
about 5 to 15% of the window (sometimes 20%) and can take up to an hour
under load; Medium or High adds roughly 20 to 50% more (user estimates, 9
October 2026). Before proposing more than one Claude run, ask whether the
user has other Claude work planned in the next 5 hours.

Wait for the user's explicit choice of mode for each prompt. If the user
already named modes, still show the report, point out any mismatch, and ask
"keep or switch?".

The user decides the count, the split and the research type. Only then
write the prompts. The browser agent that runs the pack confirms the type
again before starting, as the `chatgpt-browser` skill requires.

## 1. Write the prompts

- **One project per provider for the whole pack.** The user hates project
  spam. Put every ChatGPT prompt in one ChatGPT project and every Claude
  prompt in one Claude project. If a project for the same topic already
  exists, reuse it instead of creating a new one.
- **Split only in rare cases.** Add a second project only when the pack is
  large, its prompts fall into massively different subjects, and each
  project would still hold more than 3 or 4 prompts. Never make a project
  per prompt or per small category. When you do split, say why in the
  README.
- **ChatGPT prompts** (codes `G1`, `G2`...): keep each prompt narrow.
- **Claude prompts** (codes `C1`, `C2`...): either the same topic as a
  ChatGPT prompt (a second opinion) or a sharper version of a critical
  question.
- Name the project after the topic, for example `<Topic> research`.
- Each prompt must stand alone. A fresh chat sees only that prompt, so each
  one repeats the background it needs. Include, in order:
  1. Who the user is and what they are building or deciding (only details
     the user is fine sharing; ask if unsure).
  2. The question.
  3. What is already known, with a date, marked "verify and correct it".
     This makes the research build on past work instead of repeating it.
  4. Numbered points to cover, concrete enough to answer (names, volumes,
     prices, limits).
  5. Rules: do not ask clarifying questions, state assumptions; write "Not
     found" instead of guessing; plus the evidence rule for the prompt
     type (below).
  6. Size and stopping rule (required in every prompt): a range (for list
     prompts, for example 20 to 40 items, and stop at the top of the
     range), a time target (about 20 minutes), and this sentence: "If you
     are running long, stop and deliver what you have, and list what you
     did not check. A shorter, accurate list is better than a long one."
  6b. At most 2 add-on lines from spec rules 10 to 17, picked for the
     prompt's main risk (rule 18): a rules question gets "for any 'there
     is no X', say where you searched" and "say when each rule stops
     applying to me, and keep that in the summary"; a risk question gets
     "give likelihoods as a best estimate with confidence"; a ranking gets
     "rank inside one dataset; give measured ranking and recommended order
     separately"; a decision gets "list decision points I did not ask
     about". Keep the prompt simple: about 400 to 600 words and about 6
     rule lines in total. Prompt length hurts results more than a missing
     rule does.
  7. Output format: ask for a complete answer to a bounded question. Give
     it a short summary first, one table, a short "look at these first"
     list, and "what I did not check". Do not say that length is wanted.
     In chat modes, tell the model: "Do not build scripts, spreadsheets or
     databases. Write the answer directly." Chat-mode answers come in the
     reply as Markdown, not as a downloadable file, unless the user asks
     for a file.
- **Keep each prompt small.** Aim for about 400 to 600 words. Keep the
  user background short. Background about the user is cheap, but a long
  list of rules and columns is not.
- **Simplicity check before sending.** Read the prompt once as the model
  will. If it is over about 600 words, has more than about 6 rule lines,
  or spells out steps the model can work out itself, cut it or split it.
  Overlong, over-explicit prompts are what sent Extra High runs into
  loops in past benchmarks. When unsure, choose the shorter prompt.
- **Live prices are fine to ask for.** ChatGPT Chat modes can look up
  current prices, such as flight fares (the user confirmed this in
  October 2026). Ask for the price, the date it was checked and a link.
  Keep each prompt to one route and one date range, and say fares move.
- **Completeness comes from splitting, not from one big prompt.** For a
  big topic, write several prompts. Give each one or two sub-groups and its
  own cap. Never write "as complete as possible" in a prompt. Unbounded
  scope with no stopping rule is what made runs hang.
- **Ask at the level the user decides at.** If the user picks companies,
  ask for company-level evidence (offices, legal entities, regions, key
  facts), not individual listings. Asking for "current listings" made models
  chase open items, drift to small firms and return stale rows.
- **Split wide list-building from deep checking.** A list (sweep) prompt
  asks only for the columns the user needs to pick items (about 5 to 7),
  with one source per row. Deep checks (culture,
  policies, per-claim dated and labeled evidence) go in a later depth
  prompt about the items the user picked.
- **When you slim a prompt, keep its filters.** Keep the hard exclusions
  (for example staffing and outsourcing firms) and the group's main filter
  (big name, great culture, fast growth) ahead of "has a matching listing".
  In the 9 October 2026 slim rerun, dropping these let outsourcing firms
  and small unknown companies into a big-brand list. Ask for "a full https
  link" per row: one chat run returned unresolved link placeholders.
- **Measured effect (9 October 2026).** The slim shape (20 to 40 rows, 7
  columns, one source per row, stopping rule) cut Chat 6 Pro from 65 to 20
  minutes and stopped an Extra high stall (22 minutes). Deep research did
  not improve.
- **Scale the evidence rule to the prompt type.** List prompts: "one source
  per row (the best link, with its date if shown)". Depth prompts: "date
  and link every number; label each claim (Official doc, Vendor claim,
  Independent report, Your inference)". Per-claim evidence on every row of
  a long list multiplies the work and stalls the run.
- No placeholders. Plain English. Put each prompt in a `text` code block with
  no backticks inside, so it pastes cleanly.

## 2. Write four runner files

Save the pack as one folder: `README.md` plus

| File | What the browser agent does |
|---|---|
| `01-chatgpt-start.md` | Opens the pack's one project (creating it only if it does not exist yet), starts every ChatGPT prompt in its own new chat in the mode the user approved (Chat at 6 Pro or Extra High; never Deep research; see `~/agents/skills/chatgpt-browser/references/research-chats.md`), renames each chat to its code and title, and stops. It does not wait for results. |
| `02-chatgpt-export.md` | Run about 25 minutes after the start. Exports each finished report, reports which are still running. Safe to paste again. If a chat has shown no change for 15 minutes, treat it as stalled, recover any file it wrote from its workspace (see `~/agents/skills/chatgpt-browser/references/export.md`), and do not resend before checking. |
| `03-claude-start.md` | Same as 01, for Claude with Research on. |
| `04-claude-export.md` | Same as 02, for Claude. |

Start files hold the prompts themselves, so the agent needs only that one
file. One small wait is allowed: after sending, watch for up to a minute and
answer any clarifying questions with "No clarifications. Proceed with the
brief as written and state any assumptions in the report."

All runner files must require at least five seconds between page navigations across all tabs and both providers, including opening chats or URL-bearing tabs, reloads and back/forward actions. In-page actions may run faster if they do not navigate. Include this rule verbatim in start and export instructions.

All runner files tell the agent: no new messages beyond the prompts, never
sign up for or buy anything the research mentions, and finish with one line
per code (started / exported with file name / still running / failed).

## 3. Exports: one grouped folder, readable names

- Pick one folder name for the pack: `~/Downloads/deep-research-<topic-slug>-<yymmdd>/`.
- Create `chatgpt/` and `claude/` subfolders inside that one grouped folder. Export files tell the agent to save in the matching provider subfolder, named `<code>-<short-title>.md`
  (for example `G1-apify-coverage.md`), using the chat reply's native Copy
  or the signed-in API export (chat modes answer in the reply). If a chat wrote an `.md` file card anyway, export that
  file. See the export references in
  `~/agents/skills/chatgpt-browser/references/export.md` and
  `~/agents/skills/claude-browser/references/export.md`.
- If chats lack the requested code prefix, match their original briefs and report topics before assigning codes, and record that mapping without renaming chats during export.
- Browser agents often cannot pick a folder or file name. The fallback is to
  save to `~/Downloads` with the default name. That is fine.
- When the user says the exports are done, the local agent tidies up: finds
  the new files in `~/Downloads`, matches each to its code by its title or
  first heading, moves it into the pack folder with the readable name, and
  writes a `README.md` there listing code, title, file and status. Leave
  anything it cannot match where it is and say so.

## 4. Where the pack goes

- The shared workspace `artifacts/docs/` when the prompts hold nothing
  personal; a separate private repo when they mention personal details.
- Folder name: `<yy-mm-dd_HH-MM>__prompt_pack__<snake_title>_<model>/`.
  Follow the artifact authoring convention for frontmatter.
- Commit and push the pack. Give the user the full path of every file.

## 5. After the research

When the exports are grouped, compare them with what was already known, and
give the user one short answer: what to do next, with cost and risk. Keep
seller claims apart from tested facts.
