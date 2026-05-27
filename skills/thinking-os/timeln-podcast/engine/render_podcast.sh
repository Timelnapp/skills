#!/usr/bin/env bash
# Usage: ./render_podcast.sh <script.md> [slug]
set -euo pipefail

ENGINE_DIR="$(cd "$(dirname "$0")" && pwd)"
INPUT="${1:?Usage: ./render_podcast.sh <script.md> [slug]}"
SLUG="${2:-timeln-podcast-$(date +%Y-%m-%d)}"
WORK="/tmp/timeln-podcast-${SLUG}"
WAV="$WORK/full.wav"
MP3_TMP="$WORK/final.mp3"
MP3_OUT="$(pwd)/${SLUG}.mp3"
LOG="$WORK/generation.log"

if [[ ! -f "$INPUT" ]]; then
  echo "Input not found: $INPUT" >&2
  exit 1
fi

if [[ ! -d "$ENGINE_DIR/.venv" ]]; then
  echo "Run: cd $ENGINE_DIR && ./setup.sh" >&2
  exit 1
fi

cleanup() {
  rm -rf "$WORK"
}
trap cleanup EXIT

mkdir -p "$WORK"
source "$ENGINE_DIR/.venv/bin/activate"

if ! python "$ENGINE_DIR/generate_podcast.py" \
  --input "$INPUT" \
  --slug "$SLUG" \
  --work-dir "$WORK" \
  --output-wav "$WAV" \
  2>&1 | tee "$LOG"; then
  echo "Render failed. TTS script still at: $INPUT" >&2
  exit 1
fi

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "ffmpeg not found — WAV only: $WAV" >&2
  exit 1
fi

ffmpeg -y -loglevel error -i "$WAV" -codec:a libmp3lame -qscale:a 2 "$MP3_TMP"
cp -f "$MP3_TMP" "$MP3_OUT"

echo "✓ Timeln Podcast: $MP3_OUT"
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$MP3_OUT" 2>/dev/null | \
  awk '{printf "  Duration: %.1f min\n", $1/60}'
