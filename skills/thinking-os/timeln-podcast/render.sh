#!/usr/bin/env bash
# Usage: ./render.sh <script.md> [slug]
set -euo pipefail
SKILL_DIR="$(cd "$(dirname "$0")" && pwd)"
exec "$SKILL_DIR/engine/render_podcast.sh" "$@"
