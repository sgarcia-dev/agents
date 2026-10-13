---
doc_type: reference
updated_at: 2026-09-30
purpose: Keep future benchmark questions separate from accepted metric data.
related:
  - path: ../benchmarks.json
    why: Accepted mappings and candidate status.
  - path: ../sources/2026-09-30/browser/evaluations.txt
    why: Existing source descriptions without another web investigation. (raw data not published)
---

# Benchmark follow-ups

This is a discovery queue, not a claim that all candidates are supported. No new
benchmark research or collection was started during promotion.

| Need | Candidate | What is known from today's evidence | Next check |
|---|---|---|---|
| Long-document reasoning | AA-LCR v1.1 (accepted) | Saved lcr pass-rate and LCR evaluation entries are exposed in the snapshot | Tokenizer details remain unverified |
| Professional long-document work | GDP.pdf | Already supported; all-pass criterion on long real professional documents | Confirm document lengths before claiming a context limit |
| Instruction following | IFBench (dropped) | No values for any held configuration | Not a current candidate |
| Long-horizon workflow completion | APEX-Agents-AA (dropped) | No values for any held configuration | Not a current candidate |
| Knowledge work | AA-Briefcase v1.1 (accepted) | Saved evaluation score and JSON-LD confirm combined Elo, higher is better | Sonnet 5.5 low has no score; keep null |
| Much longer context, beyond 100k | RULER / LongBench v2 / InfiniteBench | Candidate names only; not verified in this run | Check primary sources, context ranges, reasoning vs retrieval vs generation, availability and licensing |
| Instruction adherence or generation at very long context | No accepted single benchmark yet | Hallucination metrics and retrieval tests do not establish this | Find evidence that instructions/deliverables remain correct at increasing context, not just needle retrieval |
| True elapsed time for long tasks | Own harness measurements | AA decode estimates omit tools/TTFT/overhead | Measure end-to-end successful-task time, retries, cost and correctness together |

Evidence anchors in `sources/2026-09-30/browser/evaluations.txt`: AA-LCR lines
171–177; GDP.pdf 126–139; APEX-Agents 82–89. IFBench wording should be read from
the retained source rather than reused from memory if its task count changes.

For any new metric record: source URL, version/date, task population, context
length/tokenizer, instruction/generation/retrieval distinction, harness/tool setup,
effort/fallback, score units/direction, missing-model coverage, cost/timing meaning
and evidence strength. Prefer an actual workload check over claiming a universal
model ranking from one benchmark. Freely readable results, API fields and licensed
datasets are different access questions.
