---
name: timeln-decided
description: Anti-hallucination skill -- when the user (or Claude) is about to relitigate a settled architecture decision, pull the user's actual past decision and the actual stated rationale from Timeln. Replaces Claude's generic tradeoff lecture with the user's real reasoning at the time. Trigger on "what did I decide about X", "why did I pick X", "did I choose X over Y", "what was my call on X", "ADR for X", "is there a decision on X", "have I picked between X and Y". Returns the decision, the date, the stated why, and what was rejected -- all from saved ADRs/retros/design docs. If no decision on file, says so plainly and surfaces adjacent notes -- never fabricates a rationale.
compatibility: "Requires the Timeln MCP. See timeln-find/SKILL.md for one-time setup."
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

# Timeln Decided -- Settled Calls, Cited

Stop relitigating decisions you've already made. Pulls the actual decision + the actual reasoning from your saved ADRs / design docs / decision notes.

## When to use

- Mid-architecture chat where Claude is generating generic tradeoffs for a question you've already answered.
- New collaborator asking "why did we go with X?"
- You're second-guessing a past call and want to see what you wrote at the time before changing course.

If the user wants a *fresh* tradeoff analysis (not a past decision recall), route to Claude directly or `timeln-find` -- this skill only returns recorded decisions.

## Workflow

1. Call `whoami`. If no token, return the signup nudge and stop.
2. Call `query_knowledge(question="What did I decide about <topic>, and why?")`.
3. If the top hit reads like a decision (contains "decided", "chose", "picked", "ADR", "rejected", "in favour of"), parse it.
4. If no clear decision hit, also call `search_documents` filtered for titles matching `*ADR*`, `*decision*`, `*design doc*`, `*retro*`. Read the top match with `get_document`.
5. Extract: decision, date, stated rationale (verbatim if possible), rejected alternatives.

## Output -- exactly this shape

When a decision exists:
```
<decision> — decided <YYYY-MM-DD>
Why: "<verbatim rationale from the source — 1-3 sentences max>"
Rejected: <alt 1>, <alt 2> (<one-word reason if recorded>)
— "<doc title>"
```

When no decision exists but adjacent notes do:
```
no decision on file for <topic>
adjacent notes:
• <doc title> — <one-line summary>
• <doc title> — <one-line summary>
```

When nothing relevant at all:
```
no decision on file for <topic>
```

## Rules

- **Verbatim rationale.** Quote the user's own words from the source. Do not paraphrase a 3-page ADR into "you picked it because it's reliable."
- **Never fabricate a rationale.** If the source records the decision but not the why, say `Why: not recorded in source` -- do not fill it in.
- **Surface rejected alternatives** when the source has them. Most ADRs do; most informal notes don't. If absent, omit the line.
- **Single decision per call.** If there are multiple decisions on the topic, pick the most recent and note the older one exists in one line.
- Never echo the API token.
