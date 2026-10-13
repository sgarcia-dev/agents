#!/usr/bin/env python3
"""Query the saved favorites without credentials, network, or max substitution."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    registry = json.loads((ROOT/'favorites.json').read_text())
    parser.add_argument('--model', choices=list(registry['models']), required=True)
    parser.add_argument('--effort', help='Exact effort; defaults to that favorite\'s configured effort')
    args = parser.parse_args()
    snapshot = json.loads((ROOT/'data'/registry['snapshot_date']/'favorites.snapshot.json').read_text())
    favorite = registry['models'][args.model]
    effort = args.effort or favorite['default_effort']
    configured = [c for c in favorite['configurations'] if c['effort'] == effort]
    if len(configured) != 1:
        parser.error('That exact effort is not configured; no fallback used')
    slug = configured[0]['slug']
    matches = [m for m in snapshot['models'] if m['slug'] == slug]
    if len(matches) != 1:
        parser.error('That exact configuration is not in this snapshot; no fallback used')
    if matches[0]['id'] != configured[0]['id'] or matches[0]['effort'] != effort:
        parser.error('Snapshot identity/effort differs from registry; no fallback used')
    print(json.dumps(matches[0], indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
