#!/usr/bin/env node
import { readFile, appendFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

const tools = ['http', 'headless-chrome', 'codex', 'claude-code', 'gemini', 'opencode', 'hermes', 'parallel', 'firecrawl', 'exa'];
const categories = ['job-boards', 'ats', 'company-careers', 'recruiter-firms', 'contacts', 'social', 'gov-legal', 'docs-tech', 'news', 'general'];
const usage = 'node ~/agents/capabilities/web/scripts/observe.mjs --tool TOOL --op search|fetch --category CATEGORY --outcome good|partial|bad --note "Generic finding" --by RUN-ID [--date YYYY-MM-DD] [--file /absolute/observations.jsonl]';
function date(value) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(value) || new Date(value).toISOString().slice(0, 10) !== value) throw new Error('date must be a real YYYY-MM-DD date');
}
function validate(row) {
  const fields = ['date', 'tool', 'op', 'category', 'outcome', 'note', 'by'];
  if (Object.keys(row).length !== fields.length || fields.some(k => typeof row[k] !== 'string' || !row[k].trim())) throw new Error('observation fields must be nonempty strings with no extra fields');
  date(row.date);
  if (!tools.includes(row.tool)) throw new Error('unknown tool');
  if (!['search', 'fetch'].includes(row.op)) throw new Error('op must be search or fetch');
  if (!categories.includes(row.category)) throw new Error('unknown category');
  if (!['good', 'partial', 'bad'].includes(row.outcome)) throw new Error('outcome must be good, partial or bad');
  if (!/^[a-z0-9][a-z0-9._-]{0,119}$/.test(row.by)) throw new Error('by must be a generic run id');
  if (row.note.length > 2000 || /[\r\n\x00-\x1f]/.test(row.note)) throw new Error('note must be one plain line, at most 2000 characters');
  if (/@|https?:\/\/|(?:\/Users\/|\/private\/|\/tmp\/)|agents[-]private|\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b|\+\d[\d ()-]{6,}/i.test(row.note)) throw new Error('note contains a URL, path or contact-like value; write a generic finding');
}
try {
  const args = process.argv.slice(2);
  if (args.includes('--help')) { console.log(usage); process.exit(0); }
  const flags = {};
  for (let i = 0; i < args.length; i += 2) {
    const key = args[i].replace(/^--/, '');
    if (!args[i].startsWith('--') || !['date', 'tool', 'op', 'category', 'outcome', 'note', 'by', 'file'].includes(key) || flags[key] !== undefined || args[i + 1] === undefined || args[i + 1].startsWith('--')) throw new Error('unknown, duplicate or missing CLI flag');
    flags[key] = args[i + 1];
  }
  const file = flags.file ?? fileURLToPath(new URL('../observations.jsonl', import.meta.url));
  delete flags.file;
  const row = { date: new Date().toISOString().slice(0, 10), ...flags };
  validate(row);
  let existing = '';
  try { existing = await readFile(file, 'utf8'); } catch (error) { if (error.code !== 'ENOENT') throw error; }
  if (existing && !existing.endsWith('\n')) throw new Error('existing log lacks final newline; repair it before appending');
  for (const [i, line] of existing.split('\n').entries()) if (line.trim()) {
    try { validate(JSON.parse(line)); } catch (error) { throw new Error(`invalid existing observation on line ${i + 1}: ${error.message}`); }
  }
  // One append operation keeps each ordinary observation together. Do not run a rollup during an active append.
  await appendFile(file, JSON.stringify(row) + '\n', 'utf8');
  console.log(`Appended one observation to ${file}`);
} catch (error) {
  console.error(`observe: ${error.message}\n${usage}`);
  process.exitCode = 1;
}
