# Consulting OS — Setup

## 1. Skills location

Skills live in `.agents/skills/`. Cursor loads them from the workspace automatically.

### Consult skills (local)

- `consult-pipeline`, `consult-frame`, `consult-arc`, `consult-gates`, `consult-acceptance`, `consult-commercial`, `consult-package`, `consult-consistency-lint`, `consult-integrity`, `consult-red-team`, `consult-pursue`, `consult-market`

### Timeln skills (GitHub — already in repo)

- `timeln-find`, `timeln-decided`, `timeln-shipped`, `timeln-warned`, `timeln-quickly`, `timeln-plan`

Locked in `skills-lock.json` from `timelnapp/skills`.

## 2. Timeln MCP (required for memory stages)

1. Sign up: https://timeln.app/signup
2. API token: Settings → API Tokens
3. Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "timeln": {
      "url": "https://timeln-mcp-production.up.railway.app/mcp",
      "headers": {
        "Authorization": "Bearer tln_YOUR_TOKEN_HERE"
      }
    }
  }
}
```

4. Restart Cursor. Verify: *"Call whoami on Timeln MCP."*

If MCP is down, pipeline continues with source docs only — Timeln sections marked `skipped`.

### Optional connectors (for `/cos-market`)

Connect **Apollo** or **Clay** for verified firmographics + contacts in the post-win lookalike search. If absent, `/cos-market` falls back to web/Exa and marks contacts `not verified — enrich` — never guessed.

## 3. New pursuit

```text
/cos-plan
```

Or: *"I want to build a proposal for {client} on {topic}"*

1. Creates `prospects/{slug}/` from `consult-pipeline/prospect-template/`
2. Drop transcript in `Input/`
3. Run stages via commands or full pipeline

### Cold-start pursue (no brief)

When you only have **client + topic**:

```text
/cos-pursue {Client} for {topic}
```

Optional folder scaffold only:

```bash
./consult-pursue/scripts/cos-pursue-scaffold.sh "Client Name" "topic" [slug]
```

Outputs under `prospects/{slug}/` (single folder). Example: [`consult-pursue/examples/vodafone-portugal/`](../consult-pursue/examples/vodafone-portugal/). Templates: [`consult-pursue/cold-start/`](../consult-pursue/cold-start/).

When a transcript arrives, run `/cos-research` and replace the `(synthesized)` pack.

## 4. Commands

| Command | Stage |
|---------|-------|
| `/cos-plan` | 0 CAPTURE |
| `/cos-research` | 1 |
| `/cos-frame` | 2 |
| `/cos-design` | 3 |
| `/cos-integrity` | 3.5 / 5.5 |
| `/cos-architect` | 4 |
| `/cos-variants` | 5 |
| `/cos-lint` | 5.5 |
| `/cos-ship` | 6 |
| `/cos-pursue` | 7 — standard (pack) or **cold-start** (client + topic) |
| `/cos-market` | post-win — top-5 lookalike target list |
| `/cos-resume` | any |

## 5. Weekly solo ops

Schedule **`timeln-plan`** (Monday) to rank pursuits — which slugs get pipeline time this week.

## 6. Legacy folders

Older engagements outside `prospects/{slug}/` remain valid. Add `engagement-passport.yaml` at the folder root and `/cos-resume` to continue.

## 7. Environment

| Variable | Effect |
|----------|--------|
| `COS_PASSPORT_RESET=1` | Restart pipeline at CAPTURE |
