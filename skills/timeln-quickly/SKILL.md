---
name: timeln-quickly
description: >
  Trigger on "quickly: X", "quickly recall X", "what did I say about X",
  "what did they say about X", "find the quote on X", "remind me -- X",
  "did [name] mention X", "what was the number for X", "what date did I
  commit to X". Use when the user needs a one-breath answer mid-call or
  mid-pitch. NOT for exploration (use timeln-find) or planning (use timeln-plan).
compatibility: "Requires the Timeln MCP. See timeln-find/SKILL.md for one-time setup (signup at timeln.app, API token, MCP config block)."
license: MIT
allowed-tools: mcp__timeln__whoami, mcp__timeln__query_knowledge, mcp__timeln__search_documents, mcp__timeln__get_document
metadata:
  openclaw:
    homepage: https://github.com/Timelnapp/skills
    install:
      - kind: npx
        package: skills
        args: ["add", "timelnapp/skills"]
---

# Timeln Quickly -- One Breath, One Citation

Hotkey for mid-call recall. One sentence or one quote. One citation. No synthesis.

## When to use

User is mid-call, mid-pitch, mid-dispute. They need the answer faster than they can read a paragraph. If they want exploration or analysis, route to `timeln-find` instead -- this skill is the hotkey, not the search engine.

## Mode detection

Pick mode from the query phrasing -- do not ask:

| Phrasing | Mode |
|---|---|
| "what did **I** say / mention / quote / commit / promise" | **Fact** |
| "what's the **X** for Y" / "remind me the **price/date/name**" | **Fact** |
| "what did **they / X / Acme / Sarah** say" | **Quote** |
| "find the quote", "did they mention", "their words on" | **Quote** |

Ambiguous? Default to **Fact**.

## Workflow

1. Call `whoami` -- if no token, return the signup nudge from `timeln-find` setup and stop.
2. Call `query_knowledge(question="<the user's exact question>")`.
3. If the top hit has a clear answer, return it in the format below. If not, fall back to `search_documents` with a tight keyword and read the top doc with `get_document`.
4. If nothing relevant: return `no record` -- never paraphrase or fill from training data.

## Output -- exactly this shape

**Fact mode:**
```
<one sentence — the answer, nothing else>
— "<doc title>", <YYYY-MM-DD>
```

**Quote mode:**
```
"<verbatim line — no paraphrase, no edits>"
— <speaker if known>, "<doc title>" <YYYY-MM-DD>
```

**No record:**
```
no record
```

## Rules

- **One sentence or one quote.** Never both. Never bullets. Never a header.
- **Verbatim in quote mode.** If the source paraphrases, say so: `paraphrased from notes` on its own line under the citation. Never present a paraphrase as a quote.
- **One citation.** Doc title + date. If multiple sources match, pick the most recent and ignore the rest -- this is a hotkey, not a search.
- **Multi-part questions:** split into two `timeln-quickly` hits. Do not merge.
- **No record beats a guess.** If unsure, say no record.
- Never echo the API token.

## Common failure modes

| Rationalization | Why it's wrong |
|---|---|
| "I'll add a brief explanation for context" | This is a hotkey, not a search. One sentence max. The user is mid-call. |
| "The quote isn't exact so I'll paraphrase" | Mark it `paraphrased from notes`. Never present a paraphrase as a quote. |
| "I found two good answers, I'll show both" | Pick the most recent. One answer only. |
| "Memory is thin so I'll supplement from training data" | Say `no record`. Fabrication defeats the entire purpose. |
| "The user probably wants more detail" | They don't. They said "quickly". Respect the constraint. |

**This is a rigid skill.** Follow the output shape exactly. No improvisation.
