#!/bin/bash
set +x
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
exec bash "$HERE/../../../ai-models/scripts/enter-key-and-test.command"
