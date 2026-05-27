---
name: timeln-podcast
description: >
  Trigger on "weekly podcast", "timeln podcast", "podcast from my saves",
  "turn my saves into audio", "listen to my saves". Produces one Timeln Podcast
  MP3 from Timeln saves (default: last 7 days). Full pipeline: pull, connect,
  TTS script, local render. NOT for text-only search (timeln-find) or action
  plans (timeln-plan).
compatibility: "Requires a free Timeln account (timeln.app/signup), API token, and hosted Timeln MCP. For MP3 output: Python 3.11, espeak, ffmpeg, and ~500MB disk for the local Kokoro venv on first render (run engine/setup.sh)."
license: MIT
allowed-tools: mcp__timeln__whoami, mcp__timeln__get_recent_docs, mcp__timeln__search_documents, mcp__timeln__get_document, mcp__timeln__query_knowledge, mcp__timeln__get_topic_entities
metadata:
  openclaw:
    homepage: https://github.com/Timelnapp/skills
    install:
      - kind: npx
        package: skills
        args: ["add", "timelnapp/skills"]
---

# Timeln Podcast

Turn **Timeln saves** into **one MP3** (Timeln Podcast). User listens; timeln-find is for reading.

**Deliverable:** `{slug}.mp3` in the shell **working directory** when `render.sh` runs (default slug: `timeln-podcast-{YYYY-MM-DD}`). Report the absolute path in chat.

**Requires shell** for `engine/setup.sh` and `render.sh` (not listed in `allowed-tools`).

---

## Setup (once)

```bash
cd .agents/skills/thinking-os/timeln-podcast/engine && ./setup.sh
```

Needs: Python 3.11, espeak, ffmpeg. macOS: `brew install espeak`.

---

## Workflow (4 steps)

### 1 — Pull

```
whoami
get_recent_docs(window="weekly")
```

- Default **lookup window:** 7 days (`weekly`). User may override (`monthly`, or stated range).
- Filter noise, duplicates, corrupted ingests. Count saves → **N**.

Optional: `query_knowledge` / `get_topic_entities` for connections.

### 2 — Connect (show file)

**When N ≥ 5:** write a **show file** wherever the workspace implies (skill does not prescribe a path).

Include: mermaid show bible, through-line, themed segments with bridges, graph bridge. Real saves only.

**When N < 5 (thin week):** skip show file. Say so in the cold open. Go to step 3.

### 3 — Script (TTS)

Write **TTS script** (workspace-implied path) as a **two-host NotebookLM-style
conversation**. Template: `references/tts-script-template.md` — read it before
drafting.

**Format (non-negotiable):**

- Every spoken line begins with `HOST_A:` or `HOST_B:`.
- `HOST_A` = curious / reflective. Asks the listener's question, restates ideas in plain English. Voice: `af_heart` (warm female).
- `HOST_B` = insight-driven. Brings the surprising angle, names the connection. Voice: `am_michael` (warm male).
- Section headers stay as `## [COLD OPEN]`, `## [SEGMENT 1 — …]`, `## [THE BIG PICTURE]`, `## [OUTRO]`. The extractor only renders content after the cold open.
- No mermaid, no show bible, no production notes in this file.

**Writing rules — apply every one of these:**

1. **One idea per turn.** A turn is 1–2 sentences, occasionally 3. Never a paragraph. If a save has two stats, split them across turns.
2. **React, don't narrate.** Drop in short reaction beats often — "Yeah." "Wait, really?" "Hmm." "Okay, say more." "That's wild." At least one reaction beat per minute of dialogue.
3. **Analogies for every abstract claim.** Listeners can't see the words. After any abstract concept, the next turn says "it's basically like…" with a concrete image (relay race, flywheel, recipe, thermostat).
4. **Ask the listener's question.** When something jargon-y appears, HOST_A asks the question the listener is already thinking. HOST_B answers in plain English.
5. **No "Chapter one / Segment two."** Transitions are conversational ("Okay so this connects to something else you saved this week…").
6. **Numbers spelled long-form.** "Eighty thousand dollars" not "$80k". "Ten to twenty-five percent" not "10–25%". "Five times" not "5x".
7. **Name tension when saves disagree.** Each host takes one side for a beat, then they resolve it or acknowledge it's open.
8. **"Your saves," "your week."** Listener is the saver. Second person. Never "the user."
9. **Cold open hooks — does not recap.** Open with the most surprising or contradictory observation from the week. Save count, if mentioned at all, goes in passing later.
10. **Outro lands on one thing.** One takeaway, phrased as a question or a single specific action. No action-item lists in audio.

**Target length:** ~10–14 minutes of dialogue (the back-and-forth eats more time than monologue, so segments can be tighter — aim for fewer, sharper turns rather than more turns).

**TTS hygiene:** pronunciation overrides live in `engine/tts_normalize.py`.

**Sanity check before render:**

```bash
cd engine && source .venv/bin/activate
python extract_script.py /path/to/script.md
```

Look at the printed output: every section should have a healthy mix of HOST_A and HOST_B turns (rough target: 45/55 either way, never one host dominating). If one host has 3× the turns of the other, the conversation isn't balanced — rewrite.

### 4 — Render

From skill root, with CWD = where the MP3 should land:

```bash
cd .agents/skills/thinking-os/timeln-podcast
./render.sh /path/to/script.md timeln-podcast-2026-05-26
```

Defaults: HOST_A → `af_heart`, HOST_B → `am_michael`, speed `0.96`. Override per-voice with `--voice-a` / `--voice-b` on `generate_podcast.py`. Build uses `/tmp/timeln-podcast-{slug}/` (deleted after success).

**Render failure:** return TTS script path + setup/fix steps. Do not claim an MP3 exists.

---

## Defaults

| Setting | Value |
|---------|--------|
| Lookup window | 7 days (`weekly`), overridable |
| Slug | `timeln-podcast-{date}` |
| Voice A (HOST_A) | `af_heart` (warm female, curious/reflective) |
| Voice B (HOST_B) | `am_michael` (warm male, insight-driven) |
| Speed | `0.96` |
| Format | Two-host conversational (NotebookLM-style) |
| Thin week | N < 5 → skip show file, keep two-host format |

---

## Do not

- Fabricate saves
- Skip connect when N ≥ 5
- Route text-only questions here (use timeln-find)
- Store MP3 inside the skill package
- Write monologue prose without `HOST_A:` / `HOST_B:` tags (the extractor will still render it, but in a single voice — defeats the format)
- Write paragraph-length turns. One idea per turn.
- Use "Chapter one" / "Segment two" lecture transitions
- Recap save count in the cold open — open with the surprising observation
- List action items in the outro — land on one thing

---

## Layout

```
timeln-podcast/
├── SKILL.md
├── CONTEXT.md
├── render.sh
├── references/tts-script-template.md
├── docs/adr/0001-local-kokoro-for-tts.md
└── engine/          # Kokoro; .venv gitignored
```

---

## Publish

Edit here in `operations/`. Release via manual PR to `timelnapp/skills`.

---

## Failures

| Problem | Fix |
|---------|-----|
| MCP auth | timeln.app → API token |
| Kokoro / setup | `engine/setup.sh` |
| No MP3 | Deliver script; see **Render failure** |
| Mispronunciation | `engine/tts_normalize.py` → re-render |
