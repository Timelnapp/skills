#!/usr/bin/env python3
"""Patch misaki/espeak.py for phonemizer-fork compatibility."""

from pathlib import Path

ESPEAK_PY = Path(__file__).parent / ".venv/lib/python3.11/site-packages/misaki/espeak.py"

OLD = """EspeakWrapper.set_library(espeakng_loader.get_library_path())
# Change data_path as needed when editing espeak-ng phonemes
EspeakWrapper.set_data_path(espeakng_loader.get_data_path())"""

NEW = """EspeakWrapper.set_library(espeakng_loader.get_library_path())
# Change data_path as needed when editing espeak-ng phonemes
if hasattr(EspeakWrapper, "set_data_path"):
    EspeakWrapper.set_data_path(espeakng_loader.get_data_path())
else:
    EspeakWrapper.data_path = espeakng_loader.get_data_path()"""


def main() -> None:
    text = ESPEAK_PY.read_text(encoding="utf-8")
    if NEW.split("\n")[2] in text:
        print("misaki already patched")
        return
    if OLD not in text:
        raise SystemExit(f"Unexpected espeak.py content in {ESPEAK_PY}")
    ESPEAK_PY.write_text(text.replace(OLD, NEW), encoding="utf-8")
    print("patched misaki/espeak.py")


if __name__ == "__main__":
    main()
