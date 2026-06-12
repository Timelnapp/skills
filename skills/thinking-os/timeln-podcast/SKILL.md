---
name: timeln-podcast
description: >
  Trigger on "weekly podcast", "timeln podcast", "podcast from my saves",
  "turn my saves into audio", "listen to my saves". Produces one educational
  deep-dive MP3 from Timeln saves (default: last 7 days) — teaches the topics
  you captured, not a tour of what you saved. Full pipeline: pull, curriculum,
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

Turn **Timeln saves** into **one educational deep-dive MP3**. Saves are source material —
like papers fed to NotebookLM. The episode **teaches the topics** so the listener learns
something they didn't know. It does **not** narrate what was saved or why.

**Outcome test:** After listening, could the user explain the mechanism behind a topic from
their saves to someone else? If the script only says "you saved X about Y," it failed.

**Deliverable:** `{slug}.mp3` in the shell **working directory** when `render.sh` runs (default slug: `timeln-podcast-{YYYY-MM-DD}`). Report the absolute path in chat.

**Requires shell** for `engine/setup.sh` and `render.sh` (not listed in `allowed-tools`).

---

## Setup (once)

```bash
cd .agents/skills/timeln-podcast/engine && ./setup.sh
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
- Cluster saves by **topic** (not by date saved).
- For each candidate topic cluster, `get_document` on the richest saves — read full content,
  not titles. You need mechanisms, stats, and examples to teach from.

Optional: `query_knowledge` / `get_topic_entities` for depth on concepts.

**Topic selection:** Pick **1–3 topics** with enough substance for a 4–6 minute deep dive each.
Do not try to cover every save. Depth over breadth.

### 2 — Curriculum (show file)

**When N ≥ 5:** write a **curriculum file** (show file) wherever the workspace implies.

This is a **lesson plan**, not a save-connection map. Include:

- **Episode thesis** — the one idea the episode teaches (about the topics, not about saving)
- **Topic picks** — 1–3 topics selected for deep dive, with rationale
- Per topic: **learning objective**, **concept ladder** (foundation → mechanism → example → limitation), **key mechanisms to teach**, **worked example** (stat/scenario from save content), **skeptic question**
- **Metaphor spine** — one image tying topics together
- **Substantive bridges** — how topics connect as ideas (not "user saved both")
- Mermaid optional — only if it helps map concepts, not saves

**When N < 5 (thin week):** skip curriculum file. Pick the one richest topic; teach it deeply. Go to step 3.

### 3 — Script (TTS)

Write **TTS script** (workspace-implied path) as a **two-host NotebookLM-style
conversation**. Template: `references/tts-script-template.md` — **read the full
file before drafting**, especially the "NotebookLM craft" section (reverse-engineered
from a reference deep-dive episode).

**Format (non-negotiable):**

- Every spoken line begins with `HOST_A:` or `HOST_B:`.
- `HOST_A` = curious learner. Asks the questions a student would ask, restates in plain English, pushes back. Voice: `af_heart` (warm female).
- `HOST_B` = teacher. Explains mechanisms, walks through examples, names the insight. Voice: `am_michael` (warm male).
- Section headers stay as `## [COLD OPEN]`, `## [SEGMENT 1 — …]`, `## [THE BIG PICTURE]`, `## [OUTRO]`. The extractor only renders content after the cold open.
- No mermaid, no show bible, no production notes in this file.

**NotebookLM craft — the patterns that make it sound real:**

1. **Metaphor spine.** One central image from the through-line; return to it at transitions and in the outro (full circle).
2. **Progressive disclosure.** Relatable hook → stakes → foundation → problem → insight → open edge. Never dump the conclusion first.
3. **Micro-turns.** 2–4 seconds per cue. One clause per turn. Split comma splices and double-idea turns.
4. **Reaction beats.** Standalone turns: "Yeah." "Okay." "Wait, really?" "That's wild." At least one every 30–45 seconds.
5. **Jargon: name → react → explain.** HOST_B names it; HOST_A reacts to the *name*; HOST_B explains; HOST_A restates simpler.
6. **Numbers as dialogue.** Walk stats through interactively ("Which sounds like an A." → "Until you compound it."). Spell long-form.
7. **Skeptic loops.** HOST_A pushes back before accepting a big claim ("Wait, let me push back…" / "Why isn't everyone doing this?"). One per major segment.
8. **Analogies on every abstract claim.** "It's basically like…" / "To put that into perspective…" Listeners can't see the words.
9. **Conversational transitions.** "Which brings us to…" / "But that brings us to the next big question." Never "Chapter one" / "Segment two."
10. **Outro: summarize → callback → lingering question.** Not an action-item list. End on an open frontier the listener will notice next week.

**Educational depth (non-negotiable):**

- **Teach the topic, not the save.** The episode is about on-policy distillation, world models,
  agent harnesses — not "what you bookmarked this week."
- **Banned in spoken lines:** "you saved", "your saves", "you bookmarked", "what your saves
  are telling", "that's why you saved this", save counts as narrative frame.
- **Provenance at most once:** optional single line in cold open ("something you captured
  recently on X"), then teach. Never mention saves again.
- **Per segment:** foundation → mechanism → worked example → limitation. Pull from `get_document`
  content — mechanisms, stats, named concepts, failure modes.
- **1–3 topics, 4–6 min each.** Do not tour every save. Pick clusters with enough substance.
- **Name tension when ideas disagree.** Each host takes one side on the *concept*, then resolve.

**Target length:** 12–18 minutes. Educational depth needs more time than a save tour.

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
cd .agents/skills/timeln-podcast
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
| Format | Two-host educational deep dive (NotebookLM-style) |
| Topics per episode | 1–3 (depth over breadth) |
| Thin week | N < 5 → skip curriculum file, one deep topic |

---

## Do not

- Fabricate saves or source content
- Skip curriculum when N ≥ 5
- Route text-only questions here (use timeln-find)
- Store MP3 inside the skill package
- **Narrate saves** — "you saved X", "your week of saves", "what you captured" (meta-commentary)
- **Headline-summary only** — must teach mechanisms from full `get_document` content
- **Tour every save** — pick 1–3 topics and go deep; breadth kills learning
- Write monologue prose without `HOST_A:` / `HOST_B:` tags
- Write paragraph-length turns — split to micro-turns (one clause each)
- Use "Chapter one" / "Segment two" lecture transitions
- Open with save count or save inventory — open with the topic's universal hook
- List action items in the outro — land on learning callback + frontier question
- Dump stats in one turn — walk numbers through dialogue
- Skip skeptic loops — pushback before big claims is what builds trust

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
