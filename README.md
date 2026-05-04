<p align="center">
  <img src="docs/ascii-banner.svg" alt="TIMELN SECOND BRAIN" width="760" />
</p>

<h1 align="center">Timeln Skills</h1>

<p align="center">
  <em>6 hotkeys that ground your AI in your real memory — no hallucinations, just facts.</em>
</p>

<p align="center">
  <a href="https://timeln.app/download/skill"><img alt="Docs" src="https://img.shields.io/badge/docs-timeln.app-ea580c?style=flat-square" /></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-black?style=flat-square" /></a>
  <a href="https://modelcontextprotocol.io"><img alt="MCP" src="https://img.shields.io/badge/MCP-compatible-6366f1?style=flat-square" /></a>
  <a href="https://claude.com/claude-code"><img alt="Claude Code" src="https://img.shields.io/badge/Claude%20Code-ready-d97706?style=flat-square" /></a>
  <a href="https://timeln.app/signup"><img alt="Get Timeln" src="https://img.shields.io/badge/Try%20on-timeln.app-ea580c?style=flat-square" /></a>
</p>

<p align="center">
  <img src="docs/demo.gif" alt="Demo" width="720" />
</p>

```bash
npx skills add timelnapp/skills
```

> All skills live in [`skills/`](skills/) — compatible with any agent that follows the [skills.sh](https://skills.sh) standard.

**The 6 skills:**
- **`timeln-find`** — Open-ended search + synthesis over your memory. Ask anything, get grounded answers.
- **`timeln-plan`** — Turn N days of Timeln saves into one ranked action plan (PARA → MECE → RICE → Eisenhower → GTD → 4DX).
- **`timeln-quickly`** — One-breath fact or quote, mid-call hotkey. No latency, no paraphrase.
- **`timeln-shipped`** — Proof of past work (repos, docs, case studies) ready to paste mid-pitch.
- **`timeln-decided`** — Pull past decisions + actual rationale. Stops you relitigating settled calls.
- **`timeln-warned`** — Surface your past failures/retros. Anti-hallucination armor for recommendations.

---

## What is this?

Six Claude Code / Cursor skills that wire your agent to your real Timeln memory. Every skill:
- **Grounds output in real data** — no training-data guesses, no fabrication. If memory doesn't have it, the skill says so.
- **Built for moments that matter** — fast enough for mid-call recalls, citations built-in, output shaped for the moment (fact, quote, artifact link, ranked list).
- **Anti-hallucination armor** — fills the gaps where Claude alone is forced to invent. Decisions, failures, proof points, all from *your* actual history.

How it works:
- **Hosted Timeln MCP** — a single Model Context Protocol server bridges your agent to the Timeln REST API. No Python, no local daemon.
- **Your Timeln account** — where the real data lives (documents, knowledge graph, metadata).
- **Each skill has a tight spec** — one job, one output shape, hard rules against fabrication.

No Timeln account? Skills load, but tools return a friendly *"sign up at timeln.app"* nudge. One signup at **[timeln.app/signup](https://timeln.app/signup)** and everything lights up.

---

## 60-second install

### 1 — Sign up & grab a token

1. **[timeln.app/signup](https://timeln.app/signup)** — free, Google SSO, no credit card.
2. Save a few links with the [Chrome extension](https://chromewebstore.google.com/) or paste them into the dashboard.
3. **[app.timeln.app](https://app.timeln.app) → Settings → API Tokens → Create**. Copy the `tln_...` token (shown once).

### 2 — Add the skill to your agent

```bash
npx skills add timelnapp/skills
```

Claude Code and Cursor both auto-discover `SKILL.md` files in these folders:
- Claude Code: `~/.claude/skills/`
- Cursor: `~/.cursor/skills/` (or `.cursor/skills/` inside a project)

### 3 — Point your agent at the hosted MCP

#### Claude Code — `~/.claude.json`

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

#### Cursor — `~/.cursor/mcp.json`

Same JSON as above.

Restart your agent. Type `/mcp` to confirm `timeln` is listed with a green dot.

### 4 — Try it

Pick a skill and trigger it with a natural phrase:

- **`timeln-find`:** "what should I learn today?" / "connect my ideas" / "based on my past data..."
- **`timeln-plan`:** "plan my saves" / "what should I do this week?"
- **`timeln-quickly`:** "quickly: timeline for Acme?" / "what did they say about SOC2?"
- **`timeln-shipped`:** "have I built X before?" / "case study on X"
- **`timeln-decided`:** "why did I pick Postgres?" / "ADR for database"
- **`timeln-warned`:** "what bit me on Redis?" / "gotchas with pub/sub"

---

## How each skill works

| Skill | Input | Output | Latency | Use case |
|---|---|---|---|---|
| **timeln-find** | Natural question | Synthesis + MECE/PARA gaps + optional D3 graph | ~3-5s | "What should I focus on?" / exploration |
| **timeln-plan** | Window (7/30/N days) | 6-stage HTML pipeline (PARA → RICE → Eisenhower → GTD → 4DX) | ~5-10s | Weekly planning, engagement reviews |
| **timeln-quickly** | "fact?" or "quote?" | One sentence + citation | <1s | Mid-call, mid-pitch, under pressure |
| **timeln-shipped** | Topic | Up to 3 hits (project + artifact link) | <2s | Sales / "have you done this?" |
| **timeln-decided** | Topic | Decision + rationale + rejected alts | <2s | Architecture chat, re-onboarding |
| **timeln-warned** | Topic | Up to 3 past failures + links | <2s | Pre-recommendation gut-check |

For detailed examples and workflows, see each skill's `SKILL.md` file in `skills/`.

---

## MCP tools exposed

| Tool | Purpose |
|---|---|
| `whoami` | Confirm token, return email + plan. |
| `get_recent_docs(window)` | Docs from the last "weekly" or "monthly" window. |
| `search_documents(limit, offset)` | Paginated list of all your documents. |
| `get_document(doc_id)` | Single document by id. |
| `query_knowledge(question)` | Natural-language query over your KG + docs. |
| `get_topic_entities(topic)` | Entities + sources connected to a topic. |
| `ingest_text(text, title?)` | Add plain text to your Timeln library. |
| `ingest_url(url, title?)` | Add a public URL. |

All tools forward the bearer token from the `Authorization` header.

---

## Self-hosting the MCP (optional)

Prefer to run the MCP in-process instead of calling the hosted one? It's a single Python file:

```bash
pip install -r mcp/requirements.txt
```

Then use this config instead:

```json
{
  "mcpServers": {
    "timeln": {
      "command": "python",
      "args": ["/absolute/path/to/skills/mcp/server.py"],
      "env": { "TIMELN_API_TOKEN": "tln_YOUR_TOKEN_HERE" }
    }
  }
}
```

See [`mcp/README.md`](mcp/README.md) for env vars and SSE transport details.

### Self-hosting Timeln itself

Pointing at a self-hosted Timeln backend? Override the base URL on either transport:

- **Hosted MCP** → not applicable; use self-host option below.
- **Local MCP** → set `TIMELN_API_BASE_URL=https://your-timeln.example.com` in the `env` block.

---

## Which skill for which moment?

| Moment | Use this |
|---|---|
| Mid-call, client asks "what timeline did we agree on?" | `timeln-quickly` |
| Client says "have you done this before?" | `timeln-shipped` |
| Pre-architecture chat: "should we use X?" | `timeln-warned` + `timeln-decided` |
| Monday morning: what should I focus on this week? | `timeln-plan` or `timeln-find` |
| Exploring a topic, learning from past work | `timeln-find` |
| Proving you've shipped work in a proposal | `timeln-shipped` |
| Relitigating a settled decision | `timeln-decided` |
| About to recommend something, want to sanity-check | `timeln-warned` |

---

## License

MIT — see [LICENSE](LICENSE).
