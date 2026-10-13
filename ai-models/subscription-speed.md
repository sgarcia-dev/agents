---
doc_type: reference
updated_at: 2026-09-30
purpose: Measured output speed by access route (API vs subscription), because Artificial Analysis speeds are API speeds.
related:
  - path: ./delegation-briefing.md
    why: Cheat sheet that uses this to pick fast options.
  - path: ./SELECTION.md
    why: Deeper model notes.
---

# Speed: API vs subscription

Source: a chart the owner received on September 30, 2026. The publisher and
method are not recorded, so treat it as unverified outside this chart. It shows
7 runs per row of about 2,500 to 3,300 output tokens. Speed is output tokens per
second. "First token" is the wait before the first word. Bold rows in the chart
were the Fast service tier.

| Route | Model | Tokens per second | First token (s) |
|---|---|---:|---:|
| OpenAI API | GPT-6 Sol Fast | 216 | 3.9 |
| OpenAI API | GPT-6.1 Sol Fast | 118 | 4.7 |
| OpenAI API | GPT-6 Astra Fast | 105 | 4.8 |
| OpenAI API | GPT-6 Sol | 91 | 7.4 |
| OpenAI API | GPT-6.1 Sol | 73 | 11.0 |
| OpenAI API | GPT-6 Astra | 46 | 17.5 |
| Codex CLI, subscription | GPT-6 Astra Fast | 75 | 8.5 |
| Codex CLI, subscription | GPT-6.1 Sol Fast | 46 | 12.5 |
| Codex CLI, subscription | GPT-6 Sol Fast | 44 | 6.6 |
| Codex CLI, subscription | GPT-5.6 Sol Fast | 42 | 4.8 |
| Codex CLI, subscription | GPT-6 Astra | 36 | 11.6 |
| Codex CLI, subscription | GPT-6.1 Sol | 22 | 11.2 |
| Codex CLI, subscription | GPT-6 Sol | 21 | 1.9 |
| Codex CLI, subscription | GPT-5.6 Sol | 21 | 7.4 |
| Anthropic API | Opus 5.5 | 113 | 3.7 |
| Anthropic API | Fable 5.1 | 85 | 8.7 |
| Claude Code, subscription | Opus 5.5 | 97 | 2.0 |
| Claude Code, subscription | Fable 5.1 | 96 | 1.1 |

What it shows:

- Codex on a subscription is about 3 to 4 times slower than the OpenAI API for
  Sol (GPT-6.1 Sol 22 vs 73, GPT-6 Sol 21 vs 91). Astra loses less (36 vs 46).
- Claude Code on a subscription is close to the Anthropic API (Opus 97 vs 113).
- The Fast tier roughly doubles Codex subscription speed (GPT-6.1 Sol 22 to 46).
- On Codex, GPT-6 Sol and GPT-6.1 Sol run at the same speed (21 and 22), but GPT-6
  Sol answers far sooner (1.9 s vs 11.2 s to first token). That likely explains why
  GPT-6 Sol feels faster.
- GPT-6 Astra and Fable 5.1 appear here but are not in our model data.
- Luna, Gemini and the OpenCode Go models are not in this chart.

Artificial Analysis measures API speed, so its tokens-per-second numbers for GPT
models overstate what a Codex subscription gives.
