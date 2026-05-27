#!/usr/bin/env bash
# Print engagement passport status for a prospect folder.
# Usage: ./scripts/passport-status.sh [path-to-prospect-folder]

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="${1:-}"

if [[ -z "$DIR" ]]; then
  echo "Usage: $0 <prospect-folder>"
  echo "Example: $0 \"$ROOT/prospects/ho-brothers\""
  exit 1
fi

PASSPORT="$DIR/engagement-passport.yaml"
if [[ ! -f "$PASSPORT" ]]; then
  echo "No engagement-passport.yaml in $DIR"
  exit 1
fi

echo "=== Engagement passport ==="
echo "Folder: $DIR"
grep -E '^(client|slug|stage|option_selected|revision_loop):' "$PASSPORT" || true
echo ""
echo "Checkpoints:"
grep -A 20 '^checkpoints:' "$PASSPORT" | grep -E '^\s+\w' || true
echo ""
echo "Timeln pulls:"
grep -A 50 '^timeln_pulls:' "$PASSPORT" | grep 'skill:' || echo "  (none recorded)"
