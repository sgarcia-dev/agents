#!/usr/bin/env python3
"""Discover exact candidates offline without sending a catalogue to a model."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--search', required=True, help='Literal name/slug substring; discovery only')
    args = parser.parse_args()
    registry = json.loads((ROOT/'favorites.json').read_text())
    catalog = json.loads((ROOT/'sources'/registry['snapshot_date']/'api/catalog.json').read_text())
    needle = args.search.casefold()
    found = [{k: row[k] for k in ['id','slug','name']}
             for row in catalog['data'] if needle in row['name'].casefold() or needle in row['slug'].casefold()]
    print(json.dumps({'fetched_at':catalog['fetched_at'],'discovery_only':True,
                      'count':len(found),'configurations':found},indent=2))


if __name__ == '__main__':
    main()
