#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

find_python311() {
  if [[ -n "${PYTHON:-}" ]]; then
    if "$PYTHON" -c 'import sys; exit(0 if sys.version_info[:2] == (3, 11) else 1)'; then
      echo "$PYTHON"
      return
    fi
    echo "PYTHON=$PYTHON is not 3.11" >&2
    exit 1
  fi
  for cmd in python3.11 python3; do
    if command -v "$cmd" >/dev/null 2>&1; then
      if "$cmd" -c 'import sys; exit(0 if sys.version_info[:2] == (3, 11) else 1)'; then
        command -v "$cmd"
        return
      fi
    fi
  done
  echo "Python 3.11 not found. Install 3.11 or set PYTHON=/path/to/python3.11" >&2
  exit 1
}

if ! command -v espeak >/dev/null 2>&1; then
  echo "espeak required. macOS: brew install espeak" >&2
  exit 1
fi

PY="$(find_python311)"
rm -rf .venv
"$PY" -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
pip uninstall -y phonemizer 2>/dev/null || true
pip install phonemizer-fork
python patch_misaki.py
python -c "from kokoro import KPipeline; print('Kokoro ready')"

echo "Setup complete. From skill root: ./render.sh <script.md> [slug]"
