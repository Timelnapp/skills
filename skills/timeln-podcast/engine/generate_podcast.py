#!/usr/bin/env python3
"""Generate two-host podcast audio from a tagged script using Kokoro-82M.

Reads a markdown script where every spoken line begins with HOST_A: or
HOST_B:, extracts per-turn (speaker, text) pairs, and renders each turn with
the assigned voice. Output is a single WAV (then mp3 by render_podcast.sh).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

SAMPLE_RATE = 24000

# Pauses tuned for natural dialogue cadence.
PAUSE_WITHIN_TURN_SEC = 0.18        # between chunks inside the same turn
PAUSE_BETWEEN_TURNS_SEC = 0.42      # speaker A -> B (or repeat speaker, new turn)
PAUSE_BETWEEN_SEGMENTS_SEC = 0.95   # cold open -> segment 1, etc.

from extract_script import extract_speakable_text
from tts_normalize import sentences


def chunk_text(text: str, max_chars: int = 320) -> list[str]:
    """Short utterances per chunk for natural-sounding dialogue."""
    utterances = sentences(text)
    chunks: list[str] = []
    current: list[str] = []
    size = 0

    for utt in utterances:
        if size + len(utt) + 1 > max_chars and current:
            chunks.append(" ".join(current))
            current = [utt]
            size = len(utt)
        else:
            current.append(utt)
            size += len(utt) + 1

    if current:
        chunks.append(" ".join(current))
    return chunks


def _silence(seconds: float) -> np.ndarray:
    return np.zeros(int(SAMPLE_RATE * seconds), dtype=np.float32)


def generate_audio(
    segments: list[tuple[str, list[tuple[str, str]]]],
    output_dir: Path,
    voices: dict[str, str],
    speed: float,
    lang_code: str,
) -> Path:
    from kokoro import KPipeline

    output_dir.mkdir(parents=True, exist_ok=True)
    pipeline = KPipeline(lang_code=lang_code)

    rendered_chunks: list[np.ndarray] = []
    chunk_idx = 0

    for seg_i, (seg_title, turns) in enumerate(segments):
        safe_title = re.sub(r"[^\w\-]+", "_", seg_title)[:40]
        if not turns:
            continue
        print(f"\n▶ Segment: {seg_title} ({len(turns)} turns)")

        for turn_i, (speaker, text) in enumerate(turns):
            voice = voices.get(speaker, voices["A"])
            chunks = chunk_text(text)
            print(
                f"  Turn {turn_i + 1}/{len(turns)} "
                f"[HOST_{speaker} -> {voice}] ({len(chunks)} chunks)"
            )

            turn_parts: list[np.ndarray] = []
            for ch_i, chunk in enumerate(chunks):
                out_path = (
                    output_dir
                    / f"{chunk_idx:03d}_{safe_title}_{speaker}_{ch_i:02d}.wav"
                )
                print(
                    f"    -> {out_path.name} "
                    f"({len(chunk)} chars, voice={voice})"
                )

                generator = pipeline(
                    chunk,
                    voice=voice,
                    speed=speed,
                    split_pattern=r"\n+",
                )

                parts = []
                for _, _, audio in generator:
                    parts.append(np.asarray(audio, dtype=np.float32))

                if not parts:
                    print("    ⚠ No audio for chunk, skipping")
                    continue

                combined = np.concatenate(parts)
                sf.write(str(out_path), combined, SAMPLE_RATE)
                turn_parts.append(combined)
                chunk_idx += 1

            if not turn_parts:
                continue

            # Stitch this turn together with tight within-turn pauses.
            within = _silence(PAUSE_WITHIN_TURN_SEC)
            stitched: list[np.ndarray] = []
            for j, part in enumerate(turn_parts):
                stitched.append(part)
                if j < len(turn_parts) - 1:
                    stitched.append(within)
            rendered_chunks.append(np.concatenate(stitched))

            # Pause before the next turn (skip if this is the last turn of the
            # last segment).
            is_last_turn = turn_i == len(turns) - 1
            is_last_segment = seg_i == len(segments) - 1
            if not (is_last_turn and is_last_segment):
                if is_last_turn:
                    rendered_chunks.append(
                        _silence(PAUSE_BETWEEN_SEGMENTS_SEC)
                    )
                else:
                    rendered_chunks.append(_silence(PAUSE_BETWEEN_TURNS_SEC))

    if not rendered_chunks:
        raise RuntimeError("No audio generated")

    final_audio = np.concatenate(rendered_chunks)
    final_path = output_dir / "full.wav"
    sf.write(str(final_path), final_audio, SAMPLE_RATE)
    print(f"\n✓ Full podcast: {final_path}")
    print(
        f"  Duration: {duration_sec(final_path):.1f}s "
        f"({duration_sec(final_path) / 60:.1f} min)"
    )
    return final_path


def duration_sec(path: Path) -> float:
    info = sf.info(str(path))
    return info.duration


from paths import build_workspace, default_slug, sanitize_slug


def main() -> int:
    parser = argparse.ArgumentParser(description="Kokoro two-host podcast generator")
    slug_default = default_slug()
    parser.add_argument("--input", type=Path, required=True, help="TTS script markdown")
    parser.add_argument("--slug", type=str, default=slug_default, help="Episode slug")
    parser.add_argument(
        "--work-dir",
        type=Path,
        default=None,
        help="Build workspace (default: /tmp/timeln-podcast-{slug})",
    )
    parser.add_argument(
        "--output-wav",
        type=Path,
        default=None,
        help="Final concatenated WAV (default: {work-dir}/full.wav)",
    )
    parser.add_argument(
        "--voice-a",
        default="af_heart",
        help="Kokoro voice for HOST_A (curious/reflective host)",
    )
    parser.add_argument(
        "--voice-b",
        default="am_michael",
        help="Kokoro voice for HOST_B (insight host)",
    )
    parser.add_argument(
        "--voice",
        default=None,
        help="Single-voice fallback (renders everything in this voice).",
    )
    parser.add_argument("--lang", default="a", help="a=American English")
    parser.add_argument(
        "--speed",
        type=float,
        default=0.96,
        help="Slightly slower than 1.0 for clarity; bump to 1.0 for snappier dialogue",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print extracted text only")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Input not found: {args.input}", file=sys.stderr)
        return 1

    markdown = args.input.read_text(encoding="utf-8")
    segments = extract_speakable_text(markdown)

    if args.dry_run:
        total = 0
        for title, turns in segments:
            print(f"\n=== {title} ({len(turns)} turns) ===")
            for sp, text in turns:
                total += len(text)
                print(f"  HOST_{sp}: {text[:200]}...")
        print(f"\nTotal: {len(segments)} segments, {total} chars")
        return 0

    if args.voice:
        voices = {"A": args.voice, "B": args.voice}
    else:
        voices = {"A": args.voice_a, "B": args.voice_b}

    slug = sanitize_slug(args.slug)
    work_dir = args.work_dir or build_workspace(slug)
    work_dir.mkdir(parents=True, exist_ok=True)

    generate_audio(segments, work_dir, voices, args.speed, args.lang)

    out_wav = args.output_wav or (work_dir / "full.wav")
    built = work_dir / "full.wav"
    if out_wav != built and built.exists():
        import shutil

        shutil.copy2(built, out_wav)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
