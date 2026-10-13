---
created_at: 2026-10-13
updated_at: 2026-10-13
model: claude-sonnet-5-5
doc_type: sources
purpose: Evidence ledger for the LLM evals spec: every verbatim capture, every digest, links found but not captured, and claims to avoid.
related:
  - path: ./spec.md
    why: Router for the spec; this file owns the evidence list.
  - path: ./STATE.md
    why: Capture gaps and next steps.
  - path: ./COMPENDIUM.md
    why: Superdoc 1; one entry per source below.
  - path: ./IMPLEMENTATION-GUIDE.md
    why: Superdoc 2; cites these IDs.
  - path: ./DECISIONS.md
    why: Why captures live inside this spec and how they were made.
  - path: ../youtube-extraction/SOURCES.md
    why: Sibling ledger for the YouTube capture methods used here.
---

# LLM evals: sources

Captured 2026-10-13. 71 verbatim capture files, plus one raw transcript JSON. 68 are full, 2 are partial, 1 failed. Every capture is a text file written by a tool, with a frontmatter block that records the original URL, the method and what is missing. Nothing was copied by hand. Two files (the E12 notebook index and the E12 video links) are tool-extracted views of the repository, not copies of one page. The ledger below is built from those frontmatter blocks.

Note for this public snapshot: the capture files themselves (`sources/`) are not published. The Capture column below keeps their file names for reference, and the Original column gives the public URL of each source.

How to read it: IDs follow the scheme in [AGENTS.md](AGENTS.md) (E## from the starting report, F## from links found inside sources). "Words" counts the whole file, frontmatter included. "Completeness" is the capture's own statement, not a quality score. Many full captures record a check against the original in their `capture_notes` (for example E01, E05b and E06); read the capture's own frontmatter for the exact check. A full capture can still be auto-generated text (see the note under the video group).

Trust order: a captured page or repo beats the starting report (E00). E00 is a set of leads, and [section 9 of the compendium](COMPENDIUM.md#9-what-the-deep-research-report-got-wrong-or-missed) lists where it was off.

## Captures

### Research Brief

| ID | Title | Capture | Original | Method | Completeness | Words |
|---|---|---|---|---|---|---|
| E00 | LLM evals learning path for an agent workspace | E00-deep-research-report-llm-evals.md | local ChatGPT export, not a web page | file copy, body byte-identical to the Downloads original | full | 3,347 |

### Core Guides and Articles

| ID | Title | Capture | Original | Method | Completeness | Words |
|---|---|---|---|---|---|---|
| E01 | Demystifying evals for AI agents | E01-anthropic-demystifying-evals-for-ai-agents.md | [link](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | firecrawl-v2-markdown | full | 6,208 |
| E05 | Redirect page at the short URL for Your AI Product Needs Evals | E05-hamel-your-ai-product-needs-evals.md | [link](https://hamel.dev/evals/) | curl-html-python-htmlparser | full | 55 |
| E05b | Your AI Product Needs Evals | E05b-hamel-your-ai-product-needs-evals-post.md | [link](https://hamel.dev/blog/posts/evals/) | firecrawl-v2-markdown | full | 4,272 |
| E06 | AI Evals: Everything You Need to Know | E06-hamel-shreya-evals-faq.md | [link](https://hamel.dev/blog/posts/evals-faq/) | curl-html-markdownify | full | 18,568 |
| E07 | A Field Guide to Rapidly Improving AI Products | E07-hamel-field-guide-rapidly-improving-ai-products.md | [link](https://hamel.dev/blog/posts/field-guide/) | firecrawl-v2-markdown | full | 6,503 |
| E09 | Using LLM-as-a-Judge For Evaluation: A Complete Guide | E09-hamel-using-llm-as-a-judge.md | [link](https://hamel.dev/blog/posts/llm-judge/) | firecrawl-v2-markdown | full | 7,828 |
| E10 | AlignEval: Building an App to Make Evals Easy, Fun, and Automated | E10-eugene-yan-aligneval.md | [link](https://eugeneyan.com/writing/aligneval/) | firecrawl-v2-markdown | full | 3,010 |
| F01a | Building eval systems that improve your AI product | F01a-lenny-building-eval-systems-that-improve.md | [link](https://www.lennysnewsletter.com/p/building-eval-systems-that-improve) | firecrawl-v2-markdown | partial | 3,591 |
| F01d | The Revenge of the Data Scientist | F01d-hamel-revenge-of-the-data-scientist.md | [link](https://hamel.dev/blog/posts/revenge/) | firecrawl-v2-markdown | full | 1,885 |

### Courses and Video Transcripts

| ID | Title | Capture | Original | Method | Completeness | Words |
|---|---|---|---|---|---|---|
| E03 | Why AI evals are the hottest new skill for product builders - Hamel Husain & Shreya Shankar | E03-youtube-lennys-podcast-hamel-shreya-evals.md | [link](https://www.youtube.com/watch?v=BsWxPI9UM4c) | youtube-transcript-api-json; yt-dlp metadata | full | 22,485 |
| E04 | Why AI evals are the hottest new skill for product builders - Hamel Husain & Shreya Shankar (creators of the #1 eval course) | E04-lenny-newsletter-why-ai-evals-hottest-skill.md | [link](https://www.lennysnewsletter.com/p/why-ai-evals-are-the-hottest-new-skill) | firecrawl-v2-markdown + public-transcript-json | partial | 23,688 |
| E08 | Evaluating AI Agents | E08-deeplearning-ai-evaluating-ai-agents-course.md | [link](https://www.deeplearning.ai/courses/evaluating-ai-agents) | firecrawl-v2-markdown | full | 1,303 |
| E08-L01 | Introduction | E08-lesson-01-introduction.md | [link](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/sqkza/introduction) | firecrawl-v2-markdown | full | 926 |
| E08-L02 | Evaluation in the time of LLMs | E08-lesson-02-evaluation-in-the-time-of-llms.md | [link](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/gz8ys/evaluation-in-the-time-of-llms) | firecrawl-v2-markdown | full | 1,715 |
| E08-L03 | Decomposing agents | E08-lesson-03-decomposing-agents.md | [link](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/hvoxa/decomposing-agents) | firecrawl-v2-markdown | full | 1,531 |
| E08-L04 | Lab 1: Building your agent | E08-lesson-04-lab-1-building-your-agent.md | [link](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/pag5y/lab-1%3A-building-your-agent) | firecrawl-v2-markdown | full | 3,628 |
| E08-L05 | Tracing agents | E08-lesson-05-tracing-agents.md | [link](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/uymu6/tracing-agents) | firecrawl-v2-markdown | full | 1,241 |
| E08-L06 | Lab 2: Tracing your agent | E08-lesson-06-lab-2-tracing-your-agent.md | [link](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/njjlv/lab-2%3A-tracing-your-agent) | firecrawl-v2-markdown | full | 3,698 |
| E08-L07 | Adding router and skill evaluations | E08-lesson-07-adding-router-and-skill-evaluations.md | [link](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/x3i1d/adding-router-and-skill-evaluations) | firecrawl-v2-markdown | full | 2,714 |
| E08-L08 | Lab 3: Adding router and skill evaluations | E08-lesson-08-lab-3-adding-router-and-skill-evaluations.md | [link](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/yx7uz/lab-3%3A-adding-router-and-skill-evaluations) | firecrawl-v2-markdown | full | 3,738 |
| E08-L09 | Adding trajectory evaluations | E08-lesson-09-adding-trajectory-evaluations.md | [link](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/xdfwr/adding-trajectory-evaluations) | firecrawl-v2-markdown | full | 1,338 |
| E08-L10 | Lab 4: Adding trajectory evaluations | E08-lesson-10-lab-4-adding-trajectory-evaluations.md | [link](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/an0wh/lab-4%3A-adding-trajectory-evaluations) | parallel-extract | full | 2,238 |
| E08-L11 | Adding structure to your evaluations | E08-lesson-11-adding-structure-to-your-evaluations.md | [link](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/a2c54/adding-structure-to-your-evaluations) | parallel-extract | full | 1,830 |
| E08-L12 | Lab 5: Adding structure to your evaluations | E08-lesson-12-lab-5-adding-structure-to-your-evaluations.md | [link](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/fob86/lab-5%3A-adding-structure-to-your-evaluations) | parallel-extract | full | 3,518 |
| E08-L13 | Improving your LLM-as-a-judge | E08-lesson-13-improving-your-llm-as-a-judge.md | [link](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/f63n9/improving-your-llm-as-a-judge) | firecrawl-v2-markdown | full | 1,124 |
| E08-L14 | Monitoring agents | E08-lesson-14-monitoring-agents.md | [link](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/y5v5y/monitoring-agents) | firecrawl-v2-markdown | full | 1,371 |
| E08-L15 | Conclusion | E08-lesson-15-conclusion.md | [link](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/ugje9/conclusion) | firecrawl-v2-markdown | full | 392 |
| E16a | Isaac HW 1 & 2 (Session 1) | E16a-video-recipe-chatbot-hw1-hw2-code-walkthrough.md | [link](https://youtu.be/h9oAAAYnGx4) | youtube-transcript-api-json | full | 11,597 |
| E16b | Open & Axial Coding - Isaac & Hamel Walkthrough | E16b-video-isaac-hamel-open-axial-coding.md | [link](https://youtu.be/AKg27L4E0M8) | youtube-transcript-api-json | full | 5,023 |
| E16c | Isaac HW3 (Session 2) | E16c-video-recipe-chatbot-hw3-llm-judge-solution.md | [link](https://youtu.be/1d5aNfslwHg) | youtube-transcript-api-json | full | 13,932 |
| E16d | Isaac HW 4 (Session 3) | E16d-video-recipe-chatbot-hw4-retrieval-eval-solution.md | [link](https://youtu.be/GMShL5iC8aY) | youtube-transcript-api-json | full | 8,853 |
| E16e | Isaac Homework 5 (Session 4) | E16e-video-recipe-chatbot-hw5-failure-analysis-solution.md | [link](https://youtu.be/z1oISsDUKLA) | youtube-transcript-api-json | full | 9,780 |
| E16f | How to Automate AI Evals (Correctly) | E16f-video-shreya-error-discovery-walkthrough.md | [link](https://youtu.be/tqUDjc1HzO4) | youtube-transcript-api-json | full | 6,425 |
| E16g | Data and DevOps Tools for Evaluating and Productionizing LLMs | E16g-video-hamel-your-ai-product-needs-evals-talk.md | [link](https://www.youtube.com/watch?v=B_DMMlDuJB0) | youtube-transcript-api-json | full | 12,870 |
| E16h | (title not captured; Loom page unavailable) | E16h-loom-recipe-chatbot-phoenix-tracing.md | [link](https://www.loom.com/share/30e5dced1afa467e8714d515694bb3b0) | firecrawl-v2-markdown | failed | 228 |

Also stored: E03-youtube-lennys-podcast-hamel-shreya-evals.raw.json, the raw timed transcript behind E03 (not counted as a capture below; not published).

The E03 and E16 transcripts are YouTube automatic captions, not human-checked text. E05 holds only the short redirect page; the post itself is E05b. E04 and F01a are partial because of paywalls (see [STATE.md](STATE.md)). E16h failed.

### Tools and Code

| ID | Title | Capture | Original | Method | Completeness | Words |
|---|---|---|---|---|---|---|
| E11a | Getting started | E11a-promptfoo-getting-started.md | [link](https://www.promptfoo.dev/docs/getting-started/) | gh-api-raw-markdown | full | 2,176 |
| E11b | Evaluate Coding Agents | E11b-promptfoo-evaluate-coding-agents.md | [link](https://www.promptfoo.dev/docs/guides/evaluate-coding-agents/) | gh-api-raw-markdown | full | 2,772 |
| E11c | Javascript Provider | E11c-promptfoo-custom-javascript-provider.md | [link](https://www.promptfoo.dev/docs/providers/custom-api/) | gh-api-raw-markdown | full | 2,128 |
| E12 | Recipe Chatbot - AI Evaluations Course | E12-recipe-chatbot-README.md | [link](https://github.com/ai-evals-course/recipe-chatbot) | gh-api-repository-tarball | full | 562 |
| E12 | Annotation Tool | E12-recipe-chatbot-annotation-README.md | [link](https://github.com/ai-evals-course/recipe-chatbot/blob/main/annotation/README.md) | gh-api-repository-tarball | full | 350 |
| E12 | Homework Assignment 1: Write a Starting Prompt | E12-recipe-chatbot-homeworks-hw1-readme.md | [link](https://github.com/ai-evals-course/recipe-chatbot/blob/main/homeworks/hw1/readme.md) | gh-api-repository-tarball | full | 856 |
| E12 | Homework 2: Recipe Bot Error Analysis | E12-recipe-chatbot-homeworks-hw2-README.md | [link](https://github.com/ai-evals-course/recipe-chatbot/blob/main/homeworks/hw2/README.md) | gh-api-repository-tarball | full | 564 |
| E12 | Homework 3: LLM-as-Judge for Recipe Bot Evaluation | E12-recipe-chatbot-homeworks-hw3-README.md | [link](https://github.com/ai-evals-course/recipe-chatbot/blob/main/homeworks/hw3/README.md) | gh-api-repository-tarball | full | 1,254 |
| E12 | Homework 4: Recipe Bot Retrieval Evaluation | E12-recipe-chatbot-homeworks-hw4-README.md | [link](https://github.com/ai-evals-course/recipe-chatbot/blob/main/homeworks/hw4/README.md) | gh-api-repository-tarball | full | 721 |
| E12 | Homework 5: Failure Transition Heat-Map | E12-recipe-chatbot-homeworks-hw5-README.md | [link](https://github.com/ai-evals-course/recipe-chatbot/blob/main/homeworks/hw5/README.md) | gh-api-repository-tarball | full | 555 |
| E12 | Homework: Phoenix Tracing Integration for Recipe Chatbot | E12-recipe-chatbot-homeworks-optional-phoenix-integration-README.md | [link](https://github.com/ai-evals-course/recipe-chatbot/blob/main/homeworks/optional/phoenix-integration/README.md) | gh-api-repository-tarball | full | 925 |
| E12 | Lesson 6: Custom Failure Mode Inspection Interface | E12-recipe-chatbot-lesson-7-README.md | [link](https://github.com/ai-evals-course/recipe-chatbot/blob/main/lesson-7/README.md) | gh-api-repository-tarball | full | 405 |
| E12 | Notebook index | E12-recipe-chatbot-notebook-index.md | [link](https://github.com/ai-evals-course/recipe-chatbot) | gh-api-repository-tarball-python-json | full | 370 |
| E12 | Video walkthrough links | E12-recipe-chatbot-video-links.md | [link](https://github.com/ai-evals-course/recipe-chatbot) | gh-api-repository-tarball-python-url-extraction | full | 510 |
| E13 | Eval Skills | E13-evals-skills-README.md | [link](https://github.com/ai-evals-course/evals-skills) | gh-api-raw | full | 571 |
| E13 | Build a Custom Annotation Interface | E13-evals-skills-build-review-interface-SKILL.md | [link](https://github.com/ai-evals-course/evals-skills/blob/main/skills/build-review-interface/SKILL.md) | gh-api-raw | full | 861 |
| E13 | Error Discovery Skill | E13-evals-skills-error-discovery-SKILL.md | [link](https://github.com/ai-evals-course/evals-skills/blob/main/skills/error-discovery/SKILL.md) | gh-api-raw | full | 2,386 |
| E13 | Review Loop | E13-evals-skills-error-discovery-review-loop.md | [link](https://github.com/ai-evals-course/evals-skills/blob/main/skills/error-discovery/review-loop.md) | gh-api-raw | full | 945 |
| E13 | Eval Audit | E13-evals-skills-eval-audit-SKILL.md | [link](https://github.com/ai-evals-course/evals-skills/blob/main/skills/eval-audit/SKILL.md) | gh-api-raw | full | 1,360 |
| E13 | Evals Start | E13-evals-skills-evals-start-SKILL.md | [link](https://github.com/ai-evals-course/evals-skills/blob/main/skills/evals-start/SKILL.md) | gh-api-raw | full | 303 |
| E13 | Evaluate RAG | E13-evals-skills-evaluate-rag-SKILL.md | [link](https://github.com/ai-evals-course/evals-skills/blob/main/skills/evaluate-rag/SKILL.md) | gh-api-raw | full | 1,154 |
| E13 | Generate Synthetic Data | E13-evals-skills-generate-synthetic-data-SKILL.md | [link](https://github.com/ai-evals-course/evals-skills/blob/main/skills/generate-synthetic-data/SKILL.md) | gh-api-raw | full | 796 |
| E13 | Validate Evaluator | E13-evals-skills-validate-evaluator-SKILL.md | [link](https://github.com/ai-evals-course/evals-skills/blob/main/skills/validate-evaluator/SKILL.md) | gh-api-raw | full | 1,422 |
| E13 | Write a code evaluator | E13-evals-skills-write-code-eval-SKILL.md | [link](https://github.com/ai-evals-course/evals-skills/blob/main/skills/write-code-eval/SKILL.md) | gh-api-raw | full | 285 |
| E13 | Write LLM-as-Judge Prompt | E13-evals-skills-write-judge-prompt-SKILL.md | [link](https://github.com/ai-evals-course/evals-skills/blob/main/skills/write-judge-prompt/SKILL.md) | gh-api-raw | full | 1,188 |
| E13z | Eval Skills for AI Coding Agents | E13z-hamelsmu-evals-skills-archived-README.md | [link](https://github.com/hamelsmu/evals-skills) | gh-api-raw | full | 502 |
| E14 | AgentEvals (repo root README) | E14-agentevals-README.md | [link](https://github.com/langchain-ai/agentevals) | gh-api-raw | full | 6,375 |
| E14b | AgentEvals (JavaScript README) | E14b-agentevals-js-README.md | [link](https://github.com/langchain-ai/agentevals/blob/main/js/README.md) | gh-api-raw | full | 4,210 |
| E14c | AgentEvals (Python README) | E14c-agentevals-python-README.md | [link](https://github.com/langchain-ai/agentevals/blob/main/python/README.md) | gh-api-raw | full | 3,901 |
| E15a | Inspect | E15a-inspect-ai-home.md | [link](https://inspect.aisi.org.uk/) | gh-api-qmd-source | full | 1,315 |
| E15b | Agent Bridge | E15b-inspect-ai-agent-bridge.md | [link](https://inspect.aisi.org.uk/agent-bridge.html) | gh-api-qmd-source | full | 3,507 |
| E15c | Sandboxing | E15c-inspect-ai-sandboxing.md | [link](https://inspect.aisi.org.uk/sandboxing.html) | gh-api-qmd-source | full | 4,007 |
| F01b | ALIGN Eval Frontend | F01b-eugeneyan-align-app-README.md | [link](https://github.com/eugeneyan/align-app) | gh-api-raw | full | 223 |
| F01c | Tracing | F01c-promptfoo-tracing.md | [link](https://www.promptfoo.dev/docs/tracing/) | gh-api-raw | full | 5,301 |

### Community

| ID | Title | Capture | Original | Method | Completeness | Words |
|---|---|---|---|---|---|---|
| E02 | Ask HN: What's the consensus on "unit" testing LLM prompts? | E02-hn-41019748.md | [link](https://news.ycombinator.com/item?id=41019748) | hn-algolia-api-html-to-markdown | full | 590 |

## Digests

One digest per source (or small source group). Each digest uses the same template: three-sentence point, key ideas with quotes, steps, tools, numbers, comparison with E00, fit for the workspace. The effort column is the reasoning effort of the digest worker (model gpt-6.1-sol). Words include frontmatter.

| Source IDs | Digest | Title | Effort | Words |
|---|---|---|---|---|
| E01 | [E01-anthropic-demystifying-evals.md](digests/E01-anthropic-demystifying-evals.md) | Demystifying evals for AI agents (E01) | medium | 2,867 |
| E02 | [E02-hn-41019748.md](digests/E02-hn-41019748.md) | Ask HN: What's the consensus on "unit" testing LLM prompts? (E02) | low | 1,467 |
| E03, E04 | [E03-E04-lennys-podcast-hamel-shreya.md](digests/E03-E04-lennys-podcast-hamel-shreya.md) | Why AI evals are the hottest new skill for product builders (E03, E04) | high | 3,087 |
| E05, E05b | [E05-hamel-your-ai-product-needs-evals.md](digests/E05-hamel-your-ai-product-needs-evals.md) | Your AI Product Needs Evals (E05, E05b) | high | 2,393 |
| E06 | [E06-hamel-shreya-evals-faq.md](digests/E06-hamel-shreya-evals-faq.md) | AI Evals: Everything You Need to Know (E06) | medium | 3,978 |
| E07 | [E07-hamel-field-guide.md](digests/E07-hamel-field-guide.md) | A Field Guide to Rapidly Improving AI Products (E07) | high | 2,408 |
| E08 | [E08-deeplearning-ai-evaluating-ai-agents.md](digests/E08-deeplearning-ai-evaluating-ai-agents.md) | Evaluating AI Agents (E08) | low | 3,119 |
| E09 | [E09-hamel-llm-judge.md](digests/E09-hamel-llm-judge.md) | Using LLM-as-a-Judge For Evaluation: A Complete Guide (E09) | high | 2,387 |
| E10 | [E10-eugene-yan-aligneval.md](digests/E10-eugene-yan-aligneval.md) | AlignEval: Building an App to Make Evals Easy, Fun, and Automated (E10) | low | 2,191 |
| E11a, E11b, E11c | [E11-promptfoo.md](digests/E11-promptfoo.md) | Promptfoo: getting started, coding agents and custom JavaScript providers (E11) | high | 2,653 |
| E12 | [E12-recipe-chatbot.md](digests/E12-recipe-chatbot.md) | Recipe Chatbot: AI Evaluations Course (E12) | high | 2,622 |
| E13, E13z | [E13-evals-skills.md](digests/E13-evals-skills.md) | Eval Skills (E13, with archived E13z) | medium | 3,235 |
| E14, E14b, E14c | [E14-agentevals.md](digests/E14-agentevals.md) | AgentEvals (E14, E14b, E14c) | low | 2,112 |
| E15a, E15b, E15c | [E15-inspect-ai.md](digests/E15-inspect-ai.md) | Inspect AI: home, Agent Bridge and Sandboxing (E15) | high | 2,598 |
| E16a | [E16a-video-recipe-chatbot-hw1-hw2-code-walkthrough.md](digests/E16a-video-recipe-chatbot-hw1-hw2-code-walkthrough.md) | Isaac HW 1 & 2 (Session 1) (E16a) | low | 2,203 |
| E16b | [E16b-video-isaac-hamel-open-axial-coding.md](digests/E16b-video-isaac-hamel-open-axial-coding.md) | Open & Axial Coding - Isaac & Hamel Walkthrough (E16b) | low | 1,910 |
| E16c | [E16c-video-recipe-chatbot-hw3-llm-judge-solution.md](digests/E16c-video-recipe-chatbot-hw3-llm-judge-solution.md) | Isaac HW3 (Session 2) (E16c) | low | 2,094 |
| E16d | [E16d-video-recipe-chatbot-hw4-retrieval-eval-solution.md](digests/E16d-video-recipe-chatbot-hw4-retrieval-eval-solution.md) | Isaac HW 4 (Session 3) (E16d) | low | 1,964 |
| E16e | [E16e-video-recipe-chatbot-hw5-failure-analysis-solution.md](digests/E16e-video-recipe-chatbot-hw5-failure-analysis-solution.md) | Isaac Homework 5 (Session 4) (E16e) | low | 2,062 |
| E16f | [E16f-video-shreya-error-discovery-walkthrough.md](digests/E16f-video-shreya-error-discovery-walkthrough.md) | How to Automate AI Evals (Correctly) (E16f) | low | 1,877 |
| E16g | [E16g-video-hamel-your-ai-product-needs-evals-talk.md](digests/E16g-video-hamel-your-ai-product-needs-evals-talk.md) | Data and DevOps Tools for Evaluating and Productionizing LLMs (E16g) | low | 2,050 |
| F01a, F01b, F01c, F01d | [F01-follow-up-articles.md](digests/F01-follow-up-articles.md) | Follow-up articles (D-F01) | low | 3,583 |

## Related Specs

- [../youtube-extraction/spec.md](../youtube-extraction/spec.md): how the YouTube transcripts (E03, E16a to E16g) were pulled, which routes got blocked, and what to retry. Trust its test notes over any claim here about capture methods.
- [../../skills/model-bakeoff/SKILL.md](../../skills/model-bakeoff/SKILL.md): the existing comparison procedure the implementation guide proposes to extend.

## Found but not captured (third hop)

Link-following stopped at two hops (see [DECISIONS.md](DECISIONS.md)). These links appeared inside captured sources and were not fetched. Links that were captured later (for example Hamel's post, the Lenny episode page, the Recipe Chatbot videos, the DeepLearning.AI lessons 13 to 15, the AlignEval app, promptfoo tracing and the Revenge of the Data Scientist post) are left out. The "from" column is the source that linked it.

| From | Link | Why it might matter |
|---|---|---|
| E01 | [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | The agent patterns E01 assumes. Useful for naming what a worker is doing when you design checks. |
| E07 | [applied-llms.org](https://applied-llms.org/) | Production lessons from practitioners. Companion to the field guide. |
| E08 (conclusion) | [Course appendix: resources, tips and help](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/uo9j2/appendix---resources%2C-tips-and-help) | The one lesson of the course not captured. May list further reading and notebook help. |
| E09 | [Who Validates the Validators? (arXiv 2404.12272)](https://arxiv.org/abs/2404.12272) | The paper behind aligning a judge with human labels. Read before trusting any judge-accuracy number. |
| E11 | [promptfoo: sandboxed code evals](https://www.promptfoo.dev/docs/guides/sandboxed-code-evals) | Promptfoo's own copy of a workspace is not a sandbox (E11b). This guide may say what to use instead. |
| E13 | [hamel.dev notes on evals](https://hamel.dev/notes/llm/evals/) | Hamel's product-specific eval notes, linked from the skills repo. |
| E13z | [evals-skills questions.md (archived repo)](https://github.com/hamelsmu/evals-skills/blob/main/questions.md) | Free starter questions the archived README points to. |
| E14 | [langchain-ai/openevals](https://github.com/langchain-ai/openevals) | Companion package of general evaluators. May hold the judge prompts AgentEvals reuses. |
| E14 | [LangSmith evaluation concepts](https://docs.smith.langchain.com/evaluation/concepts) | Dataset and evaluator vocabulary from the vendor behind AgentEvals. |
| E15 | [Inspect: approval for bridged agents](https://inspect.aisi.org.uk/approval.html#bridged-agents) | How tool approval works when a CLI agent runs inside Inspect. Matters for Codex and Claude Code workers. |
| E15 | [Inspect: tracing](https://inspect.aisi.org.uk/tracing.html) | Diagnosing sandbox failures. Useful when a run fails for infrastructure reasons. |
| F01 | [Hamel conference talk (YouTube lA4MfpgF91Y)](https://www.youtube.com/watch?v=lA4MfpgF91Y) | Described as his complete conference talk. E16g is a different talk, so this may add content. |
| F01 | [promptfoo redteam-tracing-example](https://github.com/promptfoo/promptfoo/tree/main/examples/redteam-tracing-example) | A working tracing example for F01c. |
| E16 (video descriptions) | [Maven AI Evals course page](https://maven.com/parlance-labs/evals?promoCode=yt-2026) | The paid course behind E12 and E16. Course context only; a promo link, not teaching content. |

Two more items sit outside this table. The E12 video-links capture also holds a tracked student portal link (a Maven redirect URL) and an optional bonus lesson on AI-assisted homework; neither was followed. The follow-up scan also found Y-prefixed links; those belong to the [YouTube extraction spec](../youtube-extraction/SOURCES.md) and are not listed here.

## Weak claims to avoid

From [section 9 of the compendium](COMPENDIUM.md#9-what-the-deep-research-report-got-wrong-or-missed). Do not repeat these from E00.

- **Course length.** E00 says the DeepLearning.AI course takes 2h16m. The captured page says 2h36m. Use 2h36m. [E00 section 2.2; E08 course page]
- **"Start with one narrow failure and a judge."** That skips the discovery step E09 requires (expert labels, critiques, fixing obvious errors first). It works only after discovery. [E09 steps 3 to 7]
- **AgentEvals TypeScript snippets are copy-ready.** They are not. The capture has a misspelled `satisifes`, undefined variables and Python `json.dumps` in TypeScript. Treat them as ideas. [E14b]
- **Start with discovery, judge writing and validation in evals-skills.** The maintained entry point is `evals-start`, which routes to audit and code checks depending on what evidence exists. [E13 README; E13 evals-start]
- **"Accepting bad work and rejecting good work" needs no definition.** The sources reverse their TPR and TNR names: E06 treats errors as positive; E12 HW3 and E13 treat passes as positive. Define the labels before you compute anything. [E06; E12 HW3; E13 validate-evaluator]
- **Hidden test examples are enough to validate a judge.** The sources also need separate prompt, development and test sets, class counts, a contamination guard and an uncertainty note. [E09; E13; E16c 00:19:44 to 00:22:37]
- **Repeat runs fix flakiness.** The sources separate "one success in several tries" from "every try right". Cheap-worker reliability needs the second. [E01, non-determinism section]
- **A promptfoo or Inspect run is isolated.** Promptfoo's copied workspace is not a sandbox. Inspect confines only work that goes through its sandbox interface. [E11b; E15b; E15c]
- **Model routing is the only setup to record.** Inspect drops client effort and sampling settings by default, and unmatched background requests can use the evaluation model. Record both. [E15b]
- **HW5 measures reliability.** It uses failures only, already classified. It teaches a diagnostic view, not rates or label validation. [E12 HW5]
- **Trajectory evals find waste.** The course compares a run to the shortest observed path, so a wasteful step every run shares stays hidden. [E08 lesson 9]
- **The worked notebooks are captured.** E12's index has first cells only, and E08 lab notebooks need a login. A full transcript is not full code. [E12 notebook index; E08 labs]
- **A first reviewed batch is a finished taxonomy.** The sources say to keep revisiting reviewed examples and keep suggested labels apart from confirmed ones. [E07; E13 review-loop; E16f]
- **E02 shows what the community thinks.** It has five comments. It is a pointer, not a survey. Also, most captures give no cost-per-success method; E00's cost measure is its own adaptation. [E02; E00]
- **Anything from E03, E16 or other auto-captions is a human-checked quote.** Those transcripts are YouTube automatic captions; names and numbers can be wrong. Check the video before quoting a figure. [E03 capture notes]
