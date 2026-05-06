<p align="center">
  <img src="docs/ascii-banner.svg" alt="TIMELN SECOND BRAIN" width="760" />
</p>

<h1 align="center">Timeln Skills</h1>

<p align="center">
  <em>A complete second-brain methodology for your AI agent — grounded in your real memory, not training data.</em>
</p>

<p align="center">
  <a href="https://timeln.app/download/skill"><img alt="Docs" src="https://img.shields.io/badge/docs-timeln.app-ea580c?style=flat-square" /></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-black?style=flat-square" /></a>
  <a href="https://modelcontextprotocol.io"><img alt="MCP" src="https://img.shields.io/badge/MCP-compatible-6366f1?style=flat-square" /></a>
  <a href="https://claude.com/claude-code"><img alt="Claude Code" src="https://img.shields.io/badge/Claude%20Code-ready-d97706?style=flat-square" /></a>
  <a href="https://timeln.app/signup"><img alt="Get Timeln" src="https://img.shields.io/badge/Try%20on-timeln.app-ea580c?style=flat-square" /></a>
</p>

<!-- Demo GIF: add docs/demo.gif to enable
<p align="center">
  <img src="docs/demo.gif" alt="Demo" width="720" />
</p>
-->

## Quickstart

Give your agent a second brain: [Claude Code](#claude-code), [Cursor](#cursor).

```bash
npx skills add timelnapp/skills
```

> All skills live in [`skills/`](skills/) — compatible with any agent that follows the [skills.sh](https://skills.sh) standard.

## How It Works

It starts from the moment you need your AI to know something real — something from *your* history, not its training data.

Instead of hallucinating a plausible answer, the agent reaches into your Timeln memory through a hosted MCP server. It pulls real documents, real knowledge-graph nodes, real decisions you recorded. Every answer comes with a citation. If the memory doesn't have it, the skill says so plainly — no fabrication, no filler.

There are six skills, each built for a specific moment:

1. **Exploring a topic** — `timeln-find` searches your memory, applies MECE gap analysis and the PARA framework, and returns sharp, actionable insight. Optionally renders an interactive D3 knowledge graph.

2. **Planning your week** — `timeln-plan` takes your recent saves and runs them through a 6-framework cascade (PARA → MECE → RICE → Eisenhower → GTD → 4DX). Output is a single HTML pipeline artifact with every filtering decision visible.

3. **Recalling a fact mid-call** — `timeln-quickly` is the hotkey. One sentence or one verbatim quote, one citation, under a second. No synthesis, no paragraphs.

4. **Proving you've shipped** — `timeln-shipped` surfaces actually-delivered work with artifact pointers (repo URL, doc title, demo link) ready to paste mid-pitch. Distinguishes shipped projects from saved articles.

5. **Recalling a past decision** — `timeln-decided` pulls the actual decision, the stated rationale, and the rejected alternatives from your saved ADRs and design docs. Stops your agent from relitigating settled calls with generic tradeoff lectures.

6. **Checking your scars** — `timeln-warned` surfaces your own past failures, retros, and post-mortems before you commit to an approach. Your actual history, not "common pitfalls."

Because the skills trigger on natural phrases, you don't need to do anything special. Say "quickly: what timeline did we agree on?" mid-call, or "have I built this before?" in a pitch, and the right skill fires automatically.

---

## Installation

### Claude Code

```bash
npx skills add timelnapp/skills
```

Skills are auto-discovered from `~/.claude/skills/`.

### Cursor

```bash
npx skills add timelnapp/skills
```

Skills are auto-discovered from `~/.cursor/skills/` (or `.cursor/skills/` inside a project).

### Connect the MCP Server

Both agents need the hosted Timeln MCP. Add to `~/.claude.json` (Claude Code) or `~/.cursor/mcp.json` (Cursor):

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

No Python, no local daemon — the MCP is hosted.

### Get Your Token

1. **[timeln.app/signup](https://timeln.app/signup)** — free, Google SSO, no credit card.
2. **[app.timeln.app](https://app.timeln.app) → Settings → API Tokens → Create**. Copy the `tln_...` token (shown once).
3. Restart your agent. Type `/mcp` to confirm `timeln` is listed with a green dot.

No Timeln account? Skills load, but tools return a friendly *"sign up at timeln.app"* nudge. One signup and everything lights up.

---

## What's Inside

### Recall (rigid skills — follow the output shape exactly)

| Skill | Trigger phrases | Output | Latency |
|---|---|---|---|
| **timeln-quickly** | "quickly: X", "what did they say about X", "remind me -- X" | One sentence + citation | <1s |
| **timeln-shipped** | "have I built X before?", "case study for X", "proof of X" | Up to 3 hits (project + artifact link) | <2s |
| **timeln-decided** | "why did I pick X?", "ADR for X", "what was my call on X" | Decision + rationale + rejected alts | <2s |
| **timeln-warned** | "what bit me on X?", "gotchas with X", "any retros on X" | Up to 3 past failures + links | <2s |

### Synthesis (flexible skills — adapt depth to the question)

| Skill | Trigger phrases | Output | Latency |
|---|---|---|---|
| **timeln-find** | "search my memory", "connect my ideas", "based on my past data..." | Synthesis + MECE/PARA gaps + optional D3 graph | ~3-5s |
| **timeln-plan** | "plan my saves", "what should I do this week?", "cascade my last 30 days" | 6-stage HTML pipeline (PARA → RICE → Eisenhower → GTD → 4DX) | ~5-10s |

Every skill has hard rules against fabrication. If memory doesn't have it, the skill says so — never invents.

---

## Which Skill for Which Moment?

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

## MCP Tools

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

## Philosophy

- **Real data over training data** — every answer must cite a source from the user's memory. If there's nothing, say so.
- **One job per skill** — each skill has a single purpose, a single output shape, and hard rules. No Swiss-army-knife skills.
- **Moments over features** — skills are designed around real moments (mid-call, mid-pitch, Monday planning) not abstract capabilities.
- **Anti-hallucination as identity** — fabrication isn't a quality issue, it's a trust violation. Every skill treats "no record" as the correct answer when memory is empty.

---

## Contributing

1. Fork the repository
2. Create a branch for your work
3. Follow the skill template (YAML frontmatter → When to use → Workflow → Output shape → Common failure modes → Rules)
4. Each skill must include an anti-rationalization table — list specific ways an agent might cut corners, with rebuttals
5. Submit a PR

See any `SKILL.md` file in `skills/` for the template.

---

## License

MIT — see [LICENSE](LICENSE).

---

## Community

- **Issues**: https://github.com/Timelnapp/skills/issues
- **Timeln**: [timeln.app](https://timeln.app) — sign up free, start saving
