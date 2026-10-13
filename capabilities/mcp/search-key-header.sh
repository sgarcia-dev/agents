#!/bin/bash
# Prints one search MCP server's auth header as JSON, for Claude Code's
# headersHelper (see the internet-deep-research MCP setup notes).
# Reads the key from its env var, else from the macOS Keychain entry that
# search-keys-setup.sh created, so it works even when Claude Code started
# from an old terminal tab or the Dock. Prints nothing secret to stderr.
set -euo pipefail
case "${1:-}" in
  parallel)  var=PARALLEL_API_KEY;  svc=parallel-api-key;  hdr=Authorization; pre="Bearer " ;;
  exa)       var=EXA_API_KEY;       svc=exa-api-key;       hdr=x-api-key;     pre="" ;;
  firecrawl) var=FIRECRAWL_API_KEY; svc=firecrawl-api-key; hdr=Authorization; pre="Bearer " ;;
  *) echo "usage: $0 parallel|exa|firecrawl" >&2; exit 2 ;;
esac
key="${!var:-}"
[ -n "$key" ] || key="$(security find-generic-password -a "$USER" -s "$svc" -w 2>/dev/null || true)"
[ -n "$key" ] || { echo "no $var in env or Keychain" >&2; exit 1; }
printf '{"%s":"%s%s"}\n' "$hdr" "$pre" "$key"
