# Kokoro engine

```bash
./setup.sh   # once: Python 3.11, espeak, venv
```

From skill root:

```bash
./render.sh /path/to/script.md timeln-podcast-2026-05-26
```

Writes `{slug}.mp3` to the current working directory. Uses `/tmp/timeln-podcast-{slug}/` during render (auto-deleted).
