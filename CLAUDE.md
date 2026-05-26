# Timeln Skills

This repo contains 6 skills that ground an AI agent in the user's real Timeln memory via a hosted MCP server.

## Skills

- `timeln-find` — open-ended search + synthesis over memory (MECE + PARA)
- `timeln-plan` — convert recent saves into a ranked action plan (6-framework cascade)
- `timeln-quickly` — one-breath mid-call recall (one sentence or one quote)
- `timeln-shipped` — proof of actually-shipped work with artifact pointers
- `timeln-decided` — past decisions with stated rationale and rejected alternatives
- `timeln-warned` — past failures, retros, and post-mortems

## Key rules

- Every skill goes through the Timeln MCP. Never call infrastructure directly.
- Never fabricate data. If MCP returns nothing, say so.
- Never echo the user's API token.
- Skills in `skills/` follow the skills.sh standard — each has a `SKILL.md` with YAML frontmatter.
