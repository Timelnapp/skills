---
status: accepted
---

# Local Kokoro engine bundled in the skill package

Timeln Podcast must produce an MP3, while sibling skills (timeln-find, timeln-plan) only need the hosted Timeln MCP. We considered script-only publish with user-provided TTS, optional engine, and waiting for a hosted Timeln render API. We chose an all-in-one bundle: `engine/` ships with the skill, and the user runs `setup.sh` once (Python 3.11, espeak, ffmpeg, ~500MB venv) before the first render.

This trades zero-dependency signup for install friction. It is hard to reverse without either shipping a hosted render path or dropping MP3 from the skill promise. Registry `compatibility` must state the full **System requirements** up front so users are not surprised after installing an MCP-only skill.
