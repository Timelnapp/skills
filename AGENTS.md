# Timeln Skills — Agent Instructions

This repo provides 6 skills for AI coding agents. Each skill connects to the user's real memory via the Timeln MCP server.

## How skills work

Each skill is a `SKILL.md` file in `skills/<name>/` with YAML frontmatter defining:
- `name` — skill identifier
- `description` — trigger phrases (used for skill discovery, NOT workflow summary)
- `allowed-tools` — which MCP tools the skill may call

## Anti-hallucination is non-negotiable

Every skill has hard rules against fabrication. If the user's Timeln memory doesn't contain the answer, the skill must say so plainly. Never supplement with training-data guesses.

## Skill types

**Rigid skills** (follow output shape exactly): `timeln-quickly`, `timeln-shipped`, `timeln-decided`, `timeln-warned`

**Flexible skills** (adapt depth to context): `timeln-find`, `timeln-plan`

## MCP dependency

All skills require the hosted Timeln MCP server. If MCP tools are not available, instruct the user to set up the server (see any SKILL.md for setup instructions).
