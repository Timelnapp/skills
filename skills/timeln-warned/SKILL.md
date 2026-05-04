---
name: timeln-warned
description: Anti-hallucination skill -- before recommending a tech approach, surface the user's own past failures, retros, post-mortems, and "lessons learned" notes on that topic from Timeln. Replaces Claude's generic "best practices" with the user's actual scars. Trigger on "what bit me on X", "have I been burned by X", "gotchas with X", "what went wrong last time with X", "warn me about X", "any retros on X", "past incidents with X", or any moment where the user is about to commit to an approach and wants a sanity check against their own history. Returns up to 3 ranked failures with one-line summaries and source pointers. If memory has nothing, says "no past incidents on file" -- never invents pitfalls from training data.
compatibility: "Requires the Timeln MCP. See timeln-find/SKILL.md for one-time setup."
license: MIT
allowed-tools: mcp__timeln__whoami, mcp__timeln__query_knowledge, mcp__timeln__search_documents, mcp__timeln__get_topic_entities, mcp__timeln__get_document
metadata:
  openclaw:
    homepage: https://github.com/Timelnapp/skills
    install:
      - kind: npx
        package: skills
        args: ["add", "timelnapp/skills"]
---

# Timeln Warned -- Your Scars, Surfaced

Before you (or Claude) recommend X, check whether X has hurt you before. Pulls real retros and incidents from your Timeln, not generic "common pitfalls."

## When to use

- About to recommend a stack/library/pattern to a client or in a chat with Claude.
- Pre-architecture decision -- gut-check against your own history.
- Any phrasing that sounds like "what could go wrong with X."

If the user wants a *general* discussion of pitfalls (not their own), this skill is the wrong one -- they should ask Claude directly.

## Workflow

1. Call `whoami`. If no token, return the signup nudge and stop.
2. Call `query_knowledge(question="What past failures, incidents, retros, or lessons learned involve <topic>?")`.
3. Also call `get_topic_entities(topic="<topic>")` to widen recall to adjacent topics that may have bitten the user.
4. Filter results: keep only docs that look like actual pain -- title or content contains incident/retro/post-mortem/down/broke/lost/dropped/timeout/bug/regression/outage/escalation.
5. Rank by severity signal strength + recency. Cap at 3.
6. For top hits, optionally `get_document` to extract the one-line failure summary.

## Output -- exactly this shape

```
1. <one-line description of what broke> — <Mon YYYY>
   — "<doc title>"
2. <one-line description of what broke> — <Mon YYYY>
   — "<doc title>"
3. (no third match)
```

If no hits at all:
```
no past incidents on file for <topic>
```

## Severity ranking

Higher severity = surface higher. Signal weights (rough):

- Words like "outage", "down", "data loss", "incident" -> high.
- "Regression", "bug", "broke", "failed" -> medium.
- "Annoying", "tricky", "had to work around" -> low (skip if competing with higher-severity hits).

## Rules

- **No fabrication.** If the user has no retros on a topic, say so. Do not synthesize "common gotchas" from training data -- that defeats the entire point.
- **One line per failure.** Specific (what broke, in what context). Not "Redis had issues."
- **Cap at 3.** If there are more, pick the 3 most severe + recent.
- **Cite the source.** Doc title only -- the user clicks through if they want the full retro.
- Never echo the API token.
