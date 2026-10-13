#!/usr/bin/env python3
"""Offline value ratings from favorites.snapshot.json -> VALUE.md."""
import json
from pathlib import Path

DIR = Path(__file__).resolve().parent.parent / "data" / "2026-09-30"


def div(a, b):
    return a / b if a is not None and b else None


def fmt(v, nd=2):
    return "N/A" if v is None else f"{v:,.{nd}f}"


def main():
    models = json.loads((DIR / "favorites.snapshot.json").read_text())["models"]
    rows = []
    for m in models:
        h = m["headline"]
        iq = h.get("intelligence_index")
        if iq is not None and h["source"] != "api":
            iq = round(iq, 1)  # match the API's one-decimal index
        price = h.get("price_usd_per_million_tokens") or {}
        pin, pout = price.get("price_1m_input_tokens"), price.get("price_1m_output_tokens")
        task = h.get("intelligence_index_cost_per_task_usd")
        total = h.get("intelligence_index_total_cost_usd")
        blend = (3 * pin + pout) / 4 if pin is not None and pout is not None else None
        rows.append((m["slug"] + ("" if h["source"] == "api" else "*"), iq, task, total, blend,
                     div(iq, task), div(iq, total), div(iq, blend)))
    rows.sort(key=lambda r: (r[5] is None, -(r[5] or 0)))
    out = """---
doc_type: reference
updated_at: 2026-09-30
purpose: Rough value-for-money ratings per configuration, computed offline from the snapshot.
related:
  - path: ./favorites.snapshot.json
    why: Machine-readable source of these numbers.
  - path: ./TABLE.md
    why: Full comparison table for the same configurations.
  - path: ../../scripts/value_ratings.py
    why: Script that generates this file.
---

# Value ratings

Rows marked * are website-only supplements captured later than the snapshot (no API cross-check). These numbers come from index benchmark averages, not from your own workload. Models that use a lot of tokens cost more per task than their price per million tokens suggests, so the per-task column is the fairer cost view. The score is a rough guide to value for money. It is not a quality ranking. N/A means the value is missing, not zero.

Columns: points per task dollar = intelligence / index USD per task (ranked by this). Points per index dollar = intelligence / whole-index USD. Blended price = (3 x input + output) / 4 per million tokens. Points per blended dollar = intelligence / blended price.

| Rank | Configuration | Intelligence | Index USD/task | Points per task dollar | Whole-index USD | Points per index dollar | Blended USD/M | Points per blended dollar |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
"""
    for i, r in enumerate(rows, 1):
        rank = str(i) if r[5] is not None else "N/A"
        out += (f"| {rank} | {r[0]} | {fmt(r[1],1)} | {fmt(r[2],4)} | {fmt(r[5])} | "
                f"{fmt(r[3])} | {fmt(r[6],3)} | {fmt(r[4])} | {fmt(r[7])} |\n")
    (DIR / "VALUE.md").write_text(out)
    for r in rows:
        print(r[0], fmt(r[5]))


main()
