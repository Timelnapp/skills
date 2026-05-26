"""Path helpers for timeln-podcast render (skill-local; no fixed artifact root)."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent


def default_slug(d: date | None = None) -> str:
    d = d or date.today()
    return f"timeln-podcast-{d.isoformat()}"


def sanitize_slug(slug: str) -> str:
    slug = slug.strip()
    if not slug:
        return default_slug()
    return re.sub(r"[^\w\-]+", "-", slug).strip("-") or default_slug()


def build_workspace(slug: str) -> Path:
    """Ephemeral OS temp dir; deleted by render_podcast.sh after MP3 is copied."""
    return Path("/tmp") / f"timeln-podcast-{sanitize_slug(slug)}"


def deliverable_mp3(slug: str, cwd: Path | None = None) -> Path:
    """Final MP3 in the shell CWD when render.sh runs."""
    return (cwd or Path.cwd()) / f"{sanitize_slug(slug)}.mp3"
