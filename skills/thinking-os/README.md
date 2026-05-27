# Thinking OS

Six memory skills + a local TTS engine, all grounded in your real Timeln second brain via the hosted MCP server. Every answer comes with a citation. If memory has nothing, the skill says so — no fabrication, no filler.

## Skills

### Memory & recall

- **[timeln-find](./timeln-find/SKILL.md)** — Open-ended search + synthesis over Timeln memory. Applies MECE gap analysis and the PARA framework; optionally renders an interactive D3 knowledge graph.
- **[timeln-plan](./timeln-plan/SKILL.md)** — Convert recent saves into a ranked action plan via a 6-framework cascade (PARA → MECE → RICE → Eisenhower → GTD → 4DX). Outputs one HTML pipeline artifact with every filtering decision visible.
- **[timeln-quickly](./timeln-quickly/SKILL.md)** — One-breath mid-call recall. One sentence or one verbatim quote, one citation, under a second. No synthesis.
- **[timeln-shipped](./timeln-shipped/SKILL.md)** — Proof of actually-shipped work with artifact pointers (repo URL, doc title, demo link). Distinguishes shipped projects from saved articles.
- **[timeln-decided](./timeln-decided/SKILL.md)** — Past decisions with stated rationale and rejected alternatives. Pulled from your saved ADRs and design docs — stops agents from relitigating settled calls.
- **[timeln-warned](./timeln-warned/SKILL.md)** — Past failures, retros, and post-mortems. Your actual scars, not "common pitfalls."

### Output

- **[timeln-podcast](./timeln-podcast/SKILL.md)** — Generate podcast-quality narration from any text using local Kokoro TTS. Ships its own Python engine (no network calls) and a single `render.sh` entrypoint.

## Routing cheat sheet

| Situation | Skill |
|-----------|-------|
| Mid-call, client asks "what timeline did we agree on?" | `timeln-quickly` |
| Client says "have you done this before?" | `timeln-shipped` |
| Pre-architecture chat: "should we use X?" | `timeln-warned` + `timeln-decided` |
| Monday morning: what should I focus on this week? | `timeln-plan` or `timeln-find` |
| Exploring a topic, learning from past work | `timeln-find` |
| Relitigating a settled decision | `timeln-decided` |
| Narrate a doc, generate audio briefing | `timeln-podcast` |

## Pairing with `consulting-os`

Every `consulting-os` pipeline stage invokes one or more of these skills. See the [Skill map in consulting-os/README.md](../consulting-os/README.md) for the stage-by-stage matrix.

## Requirements

The six memory skills require a free [Timeln account](https://timeln.app/signup) and an API token. The MCP server is hosted — no local install. `timeln-podcast` runs entirely locally (Python + Kokoro).
