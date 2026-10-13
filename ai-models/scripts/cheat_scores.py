#!/usr/bin/env python3
"""Offline compact score table from favorites.snapshot.json -> SCORES.md."""
import json
from pathlib import Path

DIR = Path(__file__).resolve().parent.parent / "data" / "2026-09-30"


def fmt(v, nd=2, suffix=""):
    return "N/A" if v is None else f"{v:,.{nd}f}{suffix}"


def main():
    models = json.loads((DIR / "favorites.snapshot.json").read_text())["models"]
    out = """---
doc_type: reference
updated_at: 2026-09-30
purpose: Compact cheat sheet of the key scores per configuration, taken from the snapshot.
related:
  - path: ./favorites.snapshot.json
    why: Machine-readable source of these numbers.
  - path: ./TABLE.md
    why: Full comparison table with the same values.
  - path: ../../scripts/cheat_scores.py
    why: Script that generates this file.
---

# Score cheat sheet

- Intelligence = Artificial Analysis Intelligence Index, higher is better.
- USD per task = average index cost per task.
- Output tokens per second = API speed. GPT models on a Codex subscription run 3 to 4 times slower; see subscription-speed.md.
- Hallucination % = share of WRONG answers that were guesses instead of "I don't know", lower is safer.
- AA-Omniscience = knowledge minus wrong answers, above 0 means more right than wrong.
- AA-LCR % = long-document reasoning, higher is better.
- Terminal-Bench % = command line and coding agent tasks.
- AutomationBench % = multi-step tool and workflow tasks.
- Input, output and cache-hit USD/1M = API list price per million tokens. Cache-hit price matters most for long agent runs, which resend the same context many times.
- N/A means the value is missing, not zero.
- \\* = website-only row captured later than the snapshot (no API cross-check; speed is the website first-party median).

| Configuration | Intelligence | USD per task | Output tokens per second | Hallucination % | AA-Omniscience | AA-LCR % | Terminal-Bench % | AutomationBench % | Input USD/1M | Output USD/1M | Cache-hit USD/1M |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
"""
    for m in models:
        hd, w = m["headline"], m["website"]
        b = w["benchmark_scores"]
        p = hd["price_usd_per_million_tokens"]
        h = w["omniscience_hallucination_fraction_of_noncorrect_responses"]
        vals = [
            fmt(hd["intelligence_index"], 1),
            fmt(hd["intelligence_index_cost_per_task_usd"], 4),
            fmt(hd["median_output_tokens_per_second"]),
            fmt(None if h is None else h * 100, 2, "%"),
            fmt(b["aa-omniscience"]["raw"]),
            fmt(b["aa-lcr-v1-1"]["percent"], 2, "%"),
            fmt(b["terminalbench-4-0"]["percent"], 2, "%"),
            fmt(b["automationbench-aa"]["percent"], 2, "%"),
            fmt(p["price_1m_input_tokens"]),
            fmt(p["price_1m_output_tokens"]),
            fmt(p["price_1m_cache_hit_tokens"]),
        ]
        star = "" if hd["source"] == "api" else "*"
        out += f"| {m['slug']}{star} | " + " | ".join(vals) + " |\n"
    (DIR / "SCORES.md").write_text(out)
    print(len(models), "rows")


main()
