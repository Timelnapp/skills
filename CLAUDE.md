# Timeln Skills

Two skill packs organised by category, both following the skills.sh standard.

## Skill packs

### `skills/thinking-os/` — memory & recall

Six skills grounded in the user's Timeln second brain via hosted MCP, plus a local TTS engine.

- `timeln-find` — open-ended search + synthesis (MECE + PARA)
- `timeln-plan` — ranked action plan from recent saves (6-framework cascade)
- `timeln-quickly` — one-breath mid-call recall (one sentence or one quote)
- `timeln-shipped` — proof of actually-shipped work with artifact pointers
- `timeln-decided` — past decisions with stated rationale and rejected alternatives
- `timeln-warned` — past failures, retros, post-mortems
- `timeln-podcast` — local Kokoro TTS narration engine (no network)

### `skills/consulting-os/` — pursuit pipeline

Skills for solo-founder consulting work, orchestrated by `consult-pipeline` with mandatory human checkpoints at every stage. Memory skills from `thinking-os` run at every stage — no duplicate memory layer. Plus `consult-market` — a standalone post-win skill that finds the next 5 lookalike accounts for a won use case.

Slash commands at `.claude-plugin/commands/cos-*.md`: `/cos-plan`, `/cos-pursue`, `/cos-market`, `/cos-resume`, and one per pipeline stage. Setup steps in `skills/consulting-os/docs/SETUP.md`.

## Key rules

- Memory skills go through the Timeln MCP. Never call infrastructure directly.
- Never fabricate data. If MCP returns nothing, say so plainly.
- Never echo the user's API token.
- Every skill folder is self-contained: `SKILL.md` + its own templates, references, scripts.
- The category-folder layout follows [mattpocock/skills](https://github.com/mattpocock/skills).
