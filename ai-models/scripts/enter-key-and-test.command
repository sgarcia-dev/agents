#!/bin/bash
set +x
set -euo pipefail
umask 077
HERE="$(cd "$(dirname "$0")" && pwd)"
trap 'unset ARTIFICIAL_ANALYSIS_API_KEY' EXIT
if [ ! -t 0 ]; then
  printf 'Run this script in your own interactive Terminal. Do not paste a key into chat.\n' >&2
  exit 1
fi
printf 'Artificial Analysis API key (hidden input): '
IFS= read -r -s ARTIFICIAL_ANALYSIS_API_KEY
printf '\n'
if [ -z "$ARTIFICIAL_ANALYSIS_API_KEY" ]; then
  printf 'No key entered. Nothing requested.\n' >&2
  exit 1
fi
export ARTIFICIAL_ANALYSIS_API_KEY
OUT="$HERE/../cache/refresh-$(date +%Y%m%d-%H%M%S)-$$"
python3 "$HERE/model_data.py" --refresh --max-pages 10 \
  --model claude-opus-5-5-medium --model gpt-6-1-sol-medium --model claude-sonnet-5-5-medium --model gpt-6-luna-medium \
  --output "$OUT"
printf '\nResults: %s\nThis is an API refresh only. Review before publishing; website fields are not refreshed. Do not share the key.\n' "$OUT"
