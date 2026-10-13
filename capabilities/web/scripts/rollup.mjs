#!/usr/bin/env node
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

const tools = ['http', 'headless-chrome', 'codex', 'claude-code', 'gemini', 'opencode', 'hermes', 'parallel', 'firecrawl', 'exa'];
const categories = ['job-boards', 'ats', 'company-careers', 'recruiter-firms', 'contacts', 'social', 'gov-legal', 'docs-tech', 'news', 'general'];
const expected = { best: 'good', good: 'good', ok: 'partial', weak: 'bad', bad: 'bad', untested: null };
const usage = 'node ~/agents/capabilities/web/scripts/rollup.mjs [--observations /absolute/observations.jsonl] [--compatibility /absolute/compatibility.jsonl] [--days 30] [--as-of YYYY-MM-DD] [--json]';
const keyOf = r => [r.tool, r.op, r.category].join('/');
function validDate(value) {
  if (typeof value !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(value) || new Date(value).toISOString().slice(0, 10) !== value) throw new Error('invalid YYYY-MM-DD date');
  return Date.parse(value);
}
function combination(r) {
  if (!tools.includes(r.tool) || !['search', 'fetch'].includes(r.op) || !categories.includes(r.category)) throw new Error('unknown tool, operation or category');
}
async function lines(file) {
  return (await readFile(file, 'utf8')).split('\n').flatMap((line, i) => {
    if (!line.trim()) return [];
    try { return [JSON.parse(line)]; } catch { throw new Error(`invalid JSON on line ${i + 1} of ${file}`); }
  });
}
try {
  const flags = {}, args = process.argv.slice(2);
  if (args.includes('--help')) { console.log(usage); process.exit(0); }
  for (let i = 0; i < args.length; i++) {
    const flag = args[i];
    if (!['--observations', '--compatibility', '--days', '--as-of', '--json'].includes(flag) || flags[flag] !== undefined) throw new Error('unknown or duplicate CLI flag');
    if (flag === '--json') flags[flag] = true;
    else { if (!args[i + 1] || args[i + 1].startsWith('--')) throw new Error('missing CLI flag value'); flags[flag] = args[++i]; }
  }
  const days = Number(flags['--days'] ?? 30);
  if (!Number.isSafeInteger(days) || days < 1) throw new Error('days must be a positive integer');
  const asOf = flags['--as-of'] ?? new Date().toISOString().slice(0, 10);
  const end = validDate(asOf), start = end - (days - 1) * 86400000;
  const observations = flags['--observations'] ?? fileURLToPath(new URL('../observations.jsonl', import.meta.url));
  const compatibility = flags['--compatibility'] ?? fileURLToPath(new URL('../compatibility.jsonl', import.meta.url));
  const verdicts = new Map(), groups = new Map();
  for (const r of await lines(compatibility)) {
    combination(r); validDate(r.updated);
    const fields = ['tool', 'op', 'category', 'verdict', 'why', 'evidence', 'updated'];
    if (Object.keys(r).length !== fields.length || fields.some(k => !(k in r)) || !Object.hasOwn(expected, r.verdict) || typeof r.why !== 'string' || !r.why.trim() || !Array.isArray(r.evidence) || r.evidence.some(e => typeof e !== 'string' || !e.startsWith('~/agents/') || e.includes('..'))) throw new Error('invalid compatibility row');
    if (verdicts.has(keyOf(r))) throw new Error('duplicate compatibility row');
    verdicts.set(keyOf(r), r);
  }
  for (const r of await lines(observations)) {
    combination(r); const stamp = validDate(r.date);
    const fields = ['date', 'tool', 'op', 'category', 'outcome', 'note', 'by'];
    if (Object.keys(r).length !== fields.length || fields.some(k => typeof r[k] !== 'string' || !r[k].trim()) || !['good', 'partial', 'bad'].includes(r.outcome) || !/^[a-z0-9][a-z0-9._-]{0,119}$/.test(r.by) || r.note.length > 2000 || /[\r\n\x00-\x1f]/.test(r.note) || /@|https?:\/\/|(?:\/Users\/|\/private\/|\/tmp\/)|agents[-]private|\+\d[\d ()-]{6,}/i.test(r.note)) throw new Error('invalid observation');
    const key = keyOf(r);
    if (!groups.has(key)) groups.set(key, { tool: r.tool, op: r.op, category: r.category, all: { good: 0, partial: 0, bad: 0 }, recent: { good: 0, partial: 0, bad: 0 }, recentRuns: new Set() });
    const group = groups.get(key); group.all[r.outcome]++;
    if (stamp >= start && stamp <= end) { group.recent[r.outcome]++; group.recentRuns.add(r.by); }
  }
  const rows = [...groups.values()].sort((a, b) => keyOf(a).localeCompare(keyOf(b))).map(group => {
    const verdict = verdicts.get(keyOf(group))?.verdict ?? 'untested';
    const total = Object.values(group.recent).reduce((a, b) => a + b, 0);
    const disagree = total - (expected[verdict] ? group.recent[expected[verdict]] : 0);
    return { ...group, recentRuns: group.recentRuns.size, verdict, disagree, flag: disagree >= 3, reason: disagree >= 3 ? (expected[verdict] ? 'Three or more recent outcomes differ from the verdict; review the sources.' : 'Three or more recent outcomes provide evidence for an untested row; review it.') : null };
  });
  const result = { asOf, days, since: new Date(start).toISOString().slice(0, 10), flagged: rows.filter(r => r.flag).length, rows };
  if (flags['--json']) console.log(JSON.stringify(result, null, 2));
  else {
    console.log(`Observations through ${asOf}; recent window ${result.since} to ${asOf} (${days} days).`);
    console.log('tool / operation / category | all good/partial/bad | recent good/partial/bad | verdict | disagreement | review');
    for (const r of rows) console.log(`${keyOf(r)} | ${r.all.good}/${r.all.partial}/${r.all.bad} | ${r.recent.good}/${r.recent.partial}/${r.recent.bad} | ${r.verdict} | ${r.disagree} | ${r.flag ? 'REVIEW' : '-'}`);
    console.log(`${result.flagged} row(s) flagged. No verdicts or files changed. Repeated runs and mixed hosts need human judgment.`);
  }
} catch (error) { console.error(`rollup: ${error.message}\n${usage}`); process.exitCode = 1; }
