#!/bin/bash
# One-time, all-harness step for the internet-deep-research MCP setup.
# Stores the Parallel, Exa, and Firecrawl API keys in the macOS Keychain and
# makes every zsh export them. Touches no AI tool config.
# Keys are typed at a hidden prompt, so they never land in shell history,
# process lists, or any file.
set -euo pipefail

for pair in PARALLEL_API_KEY:parallel-api-key EXA_API_KEY:exa-api-key FIRECRAWL_API_KEY:firecrawl-api-key; do
  var="${pair%%:*}"; svc="${pair##*:}"
  echo "Paste $var (hidden, asked twice):"
  security add-generic-password -U -a "$USER" -s "$svc" -w
done

marker="# search-mcp-keys"
if ! grep -qF "$marker" ~/.zshenv 2>/dev/null; then
  cat >> ~/.zshenv <<'EOF'

# search-mcp-keys: read from the macOS Keychain
export PARALLEL_API_KEY="$(security find-generic-password -a "$USER" -s parallel-api-key -w 2>/dev/null)"
export EXA_API_KEY="$(security find-generic-password -a "$USER" -s exa-api-key -w 2>/dev/null)"
export FIRECRAWL_API_KEY="$(security find-generic-password -a "$USER" -s firecrawl-api-key -w 2>/dev/null)"
EOF
fi

# Show only lengths, never the keys.
zsh -c 'for v in PARALLEL_API_KEY EXA_API_KEY FIRECRAWL_API_KEY; do echo "$v: ${#${(P)v}} chars"; done'
