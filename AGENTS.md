# Timeln Skills — Agent Instructions

This repo ships two skill packs for AI coding agents. Both follow the [skills.sh](https://skills.sh) standard: each skill is a `SKILL.md` file inside its own folder, organised by category.

## Layout

```
skills/
├── thinking-os/      # 6 memory skills + 1 TTS engine (Timeln MCP)
└── consulting-os/    # 11 consulting pursuit skills (human-in-the-loop pipeline)
```

Each skill folder is self-contained: `SKILL.md` plus its own templates, references, and scripts.

## How skills work

Each `SKILL.md` has YAML frontmatter:

- `name` — skill identifier (slug)
- `description` — trigger phrases used for discovery, not a workflow summary
- `allowed-tools` — which MCP tools the skill may call
- `license` — MIT

## thinking-os — memory layer

Six recall skills grounded in the user's Timeln second brain via a hosted MCP server, plus one local TTS engine.

**Rigid skills** (follow output shape exactly): `timeln-quickly`, `timeln-shipped`, `timeln-decided`, `timeln-warned`.
**Flexible skills** (adapt depth to context): `timeln-find`, `timeln-plan`.
**Local engine** (no MCP): `timeln-podcast`.

All memory skills require the hosted Timeln MCP. If MCP tools are unavailable, instruct the user to set up the server (see any SKILL.md or the root README).

## consulting-os — pursuit pipeline

Eleven skills orchestrated by `consult-pipeline` through stages CAPTURE → RESEARCH → FRAME → DESIGN → INTEGRITY → ARCHITECT → BUILD → REVIEW → PACKAGE → PURSUE → DELIVER → CLOSE → SUMMARY. Human checkpoints are mandatory at every stage. Memory skills from thinking-os run at every stage — never duplicated.

Slash commands live at `.claude-plugin/commands/cos-*.md` and provide stage-by-stage entrypoints (`/cos-plan`, `/cos-pursue`, `/cos-resume`, etc.).

## Anti-hallucination is non-negotiable

Every memory skill has hard rules against fabrication. If Timeln returns nothing, the skill must say so plainly — never supplement with training-data guesses. Every claim cites a Timeln doc. Treat "no record" as the correct answer when memory is empty.

For consulting skills: every claim about shipped work or precedent must trace to `timeln-shipped`, `timeln-decided`, or a labeled public source. The integrity gate (`consult-integrity`) blocks the pipeline when this rule is violated.

## Security

Never echo the user's Timeln API token. Never call infrastructure directly — go through the MCP.
