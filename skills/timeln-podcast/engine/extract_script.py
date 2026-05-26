#!/usr/bin/env python3
"""Extract speakable two-host script from podcast markdown.

Output shape:
    list[tuple[str, list[tuple[str, str]]]]
    -> [(section_title, [(speaker_code, text), ...]), ...]

Speaker codes: "A" (HOST_A, default voice af_heart)
               "B" (HOST_B, default voice am_michael)

Lines without a speaker tag inherit the most recent speaker in the section,
or default to "A" if none has been seen yet. This keeps the extractor
backwards compatible with older single-voice scripts.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


SKIP_CONTENT_SECTIONS = {
    "show bible",
}

STOP_SECTIONS = {
    "production notes",
    "source index",
}

SKIP_SEGMENT_KEYWORDS = (
    "sting",
    "music bed",
    "short break",
    "bed music",
    "sting out",
)

# Matches a speaker tag at the start of a line, with or without **bold**.
# Captures the letter (A/B) and the rest of the line.
SPEAKER_RE = re.compile(
    r"^\s*\**\s*HOST[_\- ]?([AB])\s*\**\s*:\s*(.*)$",
    re.IGNORECASE,
)


def _strip_markdown(text: str) -> str:
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"→", " to ", text)
    text = re.sub(r"—", ", ", text)
    text = re.sub(r"[^\S\n]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def clean_text(text: str, for_tts: bool = True) -> str:
    text = _strip_markdown(text)
    if for_tts:
        from tts_normalize import normalize_for_tts

        text = normalize_for_tts(text)
    return text


def normalize_section_title(line: str) -> str:
    title = line[3:].strip()
    title = re.sub(r"^\[|\]$", "", title)
    title = re.sub(r"\s*—.*$", "", title)
    title = re.sub(r"\s*—\s*\d+:\d+.*$", "", title)
    return title.strip().lower()


def should_skip_content(title: str) -> bool:
    return any(s in title for s in SKIP_CONTENT_SECTIONS)


def should_stop(title: str) -> bool:
    return any(s in title for s in STOP_SECTIONS)


def should_skip_section(title: str) -> bool:
    if should_skip_content(title):
        return True
    return any(k in title for k in SKIP_SEGMENT_KEYWORDS)


def is_skippable_line(stripped: str) -> bool:
    if not stripped:
        return False
    if stripped.startswith("|"):
        return True
    if stripped.startswith("# ") and not stripped.startswith("## "):
        return True
    if stripped.startswith("*Generated from"):
        return True
    if stripped.startswith("**[") and "MUSIC" in stripped.upper():
        return True
    if stripped.startswith("*[") and stripped.endswith("]*"):
        return True
    if stripped.startswith("**The through-line"):
        return False
    if stripped == "---":
        return True
    return False


def _parse_speaker(stripped: str) -> tuple[str, str] | None:
    """Return (speaker_code, remainder) if the line opens with a HOST_X tag."""
    m = SPEAKER_RE.match(stripped)
    if not m:
        return None
    return m.group(1).upper(), m.group(2).strip()


def extract_speakable_text(
    markdown: str,
) -> list[tuple[str, list[tuple[str, str]]]]:
    """Return [(section_title, [(speaker, text), ...]), ...].

    Each speaker turn is a single (speaker_code, normalized_text) pair.
    Adjacent lines from the same speaker are joined into one turn so the
    TTS engine can render them as a single continuous utterance.
    """
    segments: list[tuple[str, list[tuple[str, str]]]] = []
    current_title = ""
    current_turns: list[tuple[str, str]] = []
    last_speaker = "A"
    in_mermaid = False
    stopped = False
    started = False

    def append_turn(speaker: str, raw_text: str) -> None:
        text = clean_text(raw_text)
        if not text:
            return
        # Merge with previous turn if same speaker (handles multi-line turns).
        if current_turns and current_turns[-1][0] == speaker:
            prev_speaker, prev_text = current_turns[-1]
            current_turns[-1] = (prev_speaker, f"{prev_text} {text}".strip())
        else:
            current_turns.append((speaker, text))

    def flush_section() -> None:
        nonlocal current_turns
        if current_turns:
            segments.append((current_title, current_turns))
        current_turns = []

    for line in markdown.splitlines():
        if stopped:
            break

        stripped = line.strip()

        if stripped.startswith("```mermaid"):
            in_mermaid = True
            continue
        if in_mermaid:
            if stripped == "```":
                in_mermaid = False
            continue
        if stripped.startswith("```"):
            continue

        if stripped.startswith("## "):
            flush_section()
            title = normalize_section_title(stripped)
            if should_stop(title):
                stopped = True
                break
            if should_skip_section(title):
                current_title = title
                current_turns = []
                continue
            current_title = title
            # Reset last_speaker each section so a new segment doesn't inherit
            # the prior section's speaker on its first un-tagged line.
            last_speaker = "A"
            if "cold open" in title:
                started = True
            continue

        if not started:
            continue

        if should_skip_content(current_title):
            continue

        if is_skippable_line(stripped):
            continue

        parsed = _parse_speaker(stripped)
        if parsed is not None:
            speaker, remainder = parsed
            last_speaker = speaker
            if remainder:
                append_turn(speaker, remainder)
            continue

        # Untagged line: assign to last-seen speaker (or default "A").
        append_turn(last_speaker, stripped)

    flush_section()
    return segments


def _format_speaker_label(code: str) -> str:
    return f"HOST_{code}"


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python extract_script.py <script.md>", file=sys.stderr)
        return 1
    path = Path(sys.argv[1])
    segments = extract_speakable_text(path.read_text(encoding="utf-8"))
    total_chars = 0
    total_turns = 0
    speaker_counts: dict[str, int] = {"A": 0, "B": 0}
    for title, turns in segments:
        print(f"\n=== {title} ({len(turns)} turns) ===")
        for speaker, text in turns:
            speaker_counts[speaker] = speaker_counts.get(speaker, 0) + 1
            total_turns += 1
            total_chars += len(text)
            preview = text[:160] + ("..." if len(text) > 160 else "")
            print(f"  {_format_speaker_label(speaker)}: {preview}")
    words = total_chars / 5  # rough chars-per-word
    print(
        f"\nTotal: {len(segments)} segments, {total_turns} turns, "
        f"{total_chars} chars (~{int(words)} words, "
        f"~{words/130:.0f} min @130wpm)"
    )
    print(
        f"Turns by speaker: A={speaker_counts.get('A', 0)} "
        f"B={speaker_counts.get('B', 0)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
