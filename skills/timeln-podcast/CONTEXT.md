# Timeln Podcast

A published agent skill that turns a window of Timeln saves into one spoken podcast episode called **Timeln Podcast**. The skill owns narration logic and TTS tooling; the user owns where (if anywhere) files land on disk.

## Language

**Timeln Podcast**:
The public name for what this skill produces — one narrated episode from the user's saves. Used in cold opens and docs.
_Avoid_: Monday Morning Lookup, Brain FM, second brain radio (personal/show brands).

**Episode**:
The single audio deliverable produced by one run of the skill (typically one MP3).
_Avoid_: Show, cast, feed (those imply ongoing series infrastructure).

**Deliverable**:
The final MP3 copied into the agent's current working directory when `render.sh` runs (e.g. `{slug}.mp3`), with that path reported in chat. No global install path like `~/.timeln/podcasts/`.
_Avoid_: Output directory, artifact root, registry-mandated folder.

**Working directory**:
The CWD of the shell that invokes `render.sh`. The deliverable MP3 is written here unless the user redirects the command.
_Avoid_: Workspace root, repo root (unless they coincide with CWD).

**Save**:
One ingested Timeln document the user captured in the chosen time window.
_Avoid_: Note, bookmark, clip (too generic).

**Lookup window**:
How far back to pull saves. Defaults to seven days (`weekly` on the MCP). User may override (e.g. `monthly`, or a custom range if they state it).
_Avoid_: Monday, this week (ambiguous without dates).

**Show file**:
The intermediate markdown that connects saves (graph, through-line, segments). Working material, not the TTS input. The agent may save it wherever the active workspace implies; the skill does not prescribe a path.
_Avoid_: Script, podcast doc (ambiguous with TTS script).

**TTS script**:
The speakable-only markdown fed to Kokoro. No mermaid, no show bible. Same placement rule as the show file — workspace-implied, not skill-mandated.
_Avoid_: Narration doc, voice file.

**Slug**:
A short episode identifier used only while generating (e.g. `timeln-podcast-2026-05-26`). Not a public URL or RSS id unless the user adds that later.
_Avoid_: weekly-lookup, monday-morning-lookup, Episode ID, GUID.

**Build workspace**:
Ephemeral directory under OS temp (e.g. `/tmp/timeln-podcast-{slug}/`) holding WAV chunks, logs, and concat WAV during render. Deleted after the MP3 is produced.
_Avoid_: Output dir, artifacts root, podcasts folder.

**Local engine**:
The bundled Kokoro stack under `engine/` in the skill package. Shipped all-in-one; first successful render requires `setup.sh` (Python 3.11, espeak, venv). Not optional for a complete episode.
_Avoid_: Hosted TTS, cloud render (not in v1).

**Skills registry**:
The public install surface `timelnapp/skills` (e.g. `npx skills add timelnapp/skills`), same monorepo as timeln-find, timeln-quickly, and timeln-plan.
_Avoid_: Private ops-only skill, standalone npm package (not v1).

**System requirements**:
Everything the registry `compatibility` block must state up front: Timeln account + API token (hosted MCP); for MP3 output also Python 3.11, espeak, ffmpeg, and ~500MB disk for the **Local engine** venv on first render.
_Avoid_: Hiding local deps in the body only, "works anywhere" without deps.

**Published package**:
What ships in `timelnapp/skills`: `SKILL.md`, `references/`, and `engine/` (scripts + `requirements.txt`). Not `engine/.venv/` — created locally via `setup.sh` after install.
_Avoid_: Committing venv, prebuilt binaries, platform-specific wheels in git.

**Development source**:
Canonical skill edits happen in `operations/.agents/skills/timeln-podcast/`. Publishing is a manual PR into `timelnapp/skills` per release — not the other way around.
_Avoid_: Treating the registry copy as authoritative, dual maintenance without PR discipline.

**Registry metadata**:
Published frontmatter mirrors timeln-find: `license: MIT`, hosted-MCP `allowed-tools`, `compatibility` with full **System requirements**, and `metadata.openclaw.install` via `npx skills add timelnapp/skills`. Shell for `setup.sh` / `render.sh` is documented in SKILL.md, not in `allowed-tools`.
_Avoid_: Apache 2.0 at skill layer, omitting install block, claiming MCP-only compatibility.

**Render failure**:
If **Local engine** setup or render fails, the run still succeeds partially: user gets the **TTS script** path in chat plus clear setup/fix instructions. No MP3 implied.
_Avoid_: Silent failure, returning a broken MP3 path, skipping the script when render fails.

**timeln-find** (sibling skill):
Open-ended search and synthesis over Timeln memory. Text output. Use when the user wants to read, explore, or ask questions — not listen.
_Avoid_: Routing "review my week" here if they want audio.

**timeln-plan** (sibling skill):
Turns recent saves into a ranked action plan (PARA / Eisenhower). Use when the user wants what to do — not a narrated episode.
_Avoid_: Combining plan output with podcast in one run without user ask.

**Podcast boundary**:
This skill applies when the user wants an MP3 (listen), and accepts: pull saves → connect (when enough material) → TTS script → local render. Not a shortcut for find with audio bolted on.
_Avoid_: Single-step "just read my saves aloud" when N ≥ 5.

**Thin week**:
When fewer than five saves fall in the **Lookup window** (N < 5), the agent skips the **Show file** and goes straight to the **TTS script**. When N ≥ 5, the **Show file** is required. Cold open must acknowledge a thin week when skipping.
_Avoid_: Fabricating connections, forcing mermaid for N < 5, skipping show file when N ≥ 5.

## Implementation status

Aligned with CONTEXT: `paths.py`, `render_podcast.sh`, `setup.sh`, `SKILL.md`, `references/tts-script-template.md` (2026-05-26).


## Example dialogue

**User:** Make my weekly podcast from Timeln.

**Agent:** I'll pull your last seven days of saves unless you want a different window. You'll get a Timeln Podcast MP3 in this working directory — I need Python 3.11 and espeak for the local engine on first run.

**User:** Just the last three days.

**Agent:** Using a three-day window. I count four saves — that's a thin week, so I'll skip the show file and go straight to a TTS script, then render.

**User:** Why can't timeln-find do this?

**Agent:** timeln-find is for reading and exploring in text. This skill is for listening: connect your saves, narrate them, and run Kokoro to produce the MP3.

