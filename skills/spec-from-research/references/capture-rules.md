---
created_at: 2026-10-13
model: claude-sonnet-5-5
doc_type: reference
purpose: Capture rules the root hands to every capture worker when building a spec from a research report.
related:
  - path: ../SKILL.md
    why: The procedure that uses these rules (step 3).
  - path: ./packets.md
    why: Capture packet template that tells the worker to read this file.
  - path: ~/agents/capabilities/web/README.md
    why: Tool strengths and fetch ladders for the harness; keep the ladder below in line with it.
---

# Capture rules

The root copies this file into the run scratch folder and fills the three
placeholders: `<SCRATCH>` (scratch folder for raw files), `<SPEC>` (the spec
folder) and `<TODAY>` (capture date, YYYY-MM-DD). Then each capture packet says
"read and follow `<SCRATCH>/capture-rules.md` exactly".

---

You are one capture worker. Your job: save a VERBATIM Markdown copy of each URL
in your packet into the folder your packet names. You do not summarize, judge or
rewrite. You never spawn agents and never call another AI CLI. Do not run git;
the caller commits.

## Golden rule: tools write the text, never you

- Every byte of page text must reach the file through a command that writes
  straight to disk (curl, an API call, a script, `gh`, `uvx ...`).
- Never retype, paraphrase or "clean up" page text by hand.
- You may only write the frontmatter header and short bracketed notes such as
  `[capture note: comments truncated by API at 500]`.
- If tool output needs conversion (HTML to Markdown, JSON to Markdown), do it
  with a script (`python3 -I`, `jq`), not by hand.
- Keep scratch files (raw HTML, JSON, scripts) under `<SCRATCH>/raw/<packet id>/`.
  Never put scripts or raw dumps in the spec folder.
- Never print API keys.

## Fetch ladder for ordinary web pages (stop at the first full result)

1. Firecrawl REST, env `FIRECRAWL_API_KEY`:
   `curl -s https://api.firecrawl.dev/v2/scrape -H "Authorization: Bearer $FIRECRAWL_API_KEY" -H 'Content-Type: application/json' -d '{"url":"<URL>","formats":["markdown"],"onlyMainContent":true}'`
   Take `.data.markdown` with `jq` into the file. If main-content mode drops real
   content (tables, code, FAQ sections), retry with `"onlyMainContent":false`.
2. Exa contents, env `EXA_API_KEY`:
   `curl -s https://api.exa.ai/contents -H "x-api-key: $EXA_API_KEY" -H 'Content-Type: application/json' -d '{"urls":["<URL>"],"text":true,"livecrawl":"always"}'`
   Take `.results[0].text`.
3. Parallel extract, env `PARALLEL_API_KEY`: `POST https://api.parallel.ai/v1beta/extract`
   with header `x-api-key` and body `{"urls":["<URL>"],"full_content":true,"objective":"full page text"}`.
   Check the response shape. Add a `parallel-beta` header only if the API asks.
4. Plain fetch: `curl -sL -A 'Mozilla/5.0'` to a raw HTML file, then
   `uvx --from trafilatura trafilatura --markdown --with-metadata -i <file>`
   (or `--formatting --links`) to convert.
5. Headless Chrome for JavaScript pages:
   `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --virtual-time-budget=15000 --dump-dom <URL> > page.html`,
   then trafilatura as in step 4.

Paid tools: at most 3 Firecrawl calls and 3 Exa calls per URL.

## Special routes (use these first for these sites)

- GitHub repo README: `gh api repos/<o>/<r>/readme -H 'Accept: application/vnd.github.raw'`.
  Other files: `gh api repos/<o>/<r>/contents/<path> -H 'Accept: application/vnd.github.raw'`.
  For many files a shallow clone into your scratch folder is fine. Copy only
  the files the packet asks for.
- GitHub issue with comments: `gh api repos/<o>/<r>/issues/<n>` and
  `gh api --paginate repos/<o>/<r>/issues/<n>/comments`, rendered to Markdown by
  a script (author, date, body for each).
- GitHub wiki page: `https://raw.githubusercontent.com/wiki/<o>/<r>/<Page>.md`.
- Docs sites: look for the Markdown or `.qmd` source in the project's GitHub repo
  and fetch that raw file. It is cleaner than the rendered page.
- Hacker News: `https://hn.algolia.com/api/v1/items/<id>` returns the full
  comment tree. Convert to nested Markdown with a script (author, date, text
  from HTML, nesting shown by `>` quotes or heading level).
- Reddit (`www.reddit.com` JSON returns 403 here): Arctic Shift API.
  Post: `https://arctic-shift.photon-reddit.com/api/posts/ids?ids=<id>`.
  Comments: `https://arctic-shift.photon-reddit.com/api/comments/tree?link_id=<id>&limit=9999`.
  Render with a script. If it fails, try the fetch ladder on `https://old.reddit.com/...`.
- PyPI stats: `https://pypistats.org/api/packages/<pkg>/recent` and `/overall`.
- npm: `https://registry.npmjs.org/<pkg>` (readme field) and
  `https://api.npmjs.org/downloads/point/last-week/<pkg>`.
- YouTube transcripts, in this order:
  1. `uvx youtube-transcript-api <video id>`
  2. `yt-dlp --write-auto-subs --skip-download` (convert the subtitle file with a script)
  3. Firecrawl scrape of the watch page.
  YouTube rate-limits a home IP after about 20 transcript requests in 10 to 15
  minutes. Space video captures out. If you hit a block, wait, then fall back to
  step 3. Record title, channel and publish date from the page, not from memory.
- PDFs and arXiv: fetch the PDF with curl, convert with a script
  (`uvx --from pymupdf4llm ...` or `pdftotext`), and say the method in the file.

Add a route here when you find a better one for a site you meet often.

## Output file format (one file per URL unless the packet says otherwise)

Path: the folder and file name your packet gives. Content:

```
---
source_url: <exact URL>
title: <page title as shown by the source>
author: <if the page states it, else unknown>
published: <if the page states it, else unknown>
captured_at: <TODAY>
capture_method: <tool that produced the body, e.g. firecrawl-v2-markdown>
methods_tried: <ordered list, with the failure reason for each failed one>
completeness: full | partial | failed
capture_notes: <what is missing and why, e.g. paywall, login, truncated>
---

<verbatim body>
```

If every route fails, still write the file with `completeness: failed`, the
methods tried and their errors, and an empty body.

## Check before you finish

For each file:

- Confirm the body is not a cookie wall, login wall, bot challenge or error page.
- Compare its length with the raw HTML text length.
- Spot-check that the last section of the real page is present.
- Confirm the file starts with the frontmatter block and the body came from a tool.

## Final message (your last message is your report)

- One line per file: `<path> | <completeness> | <capture_method> | <words> words | <notes>`.
- Then a list of follow-up links worth capturing that you saw (for example videos
  linked from a README), one line each saying why it matters.
- Print `PROGRESS n/total` after each URL you finish.
