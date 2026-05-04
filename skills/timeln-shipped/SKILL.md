---
name: timeln-shipped
description: Mid-pitch proof-of-work lookup. When a client/prospect asks "have you done this before?" -- surface the user's actually-shipped past work matching the topic, with artifact pointers (repo URL, doc title, demo link) ready to paste into the chat. Distinguishes shipped projects from articles the user merely saved. Trigger on "have I shipped X", "have I built X before", "show me proof of X", "case study for X", "past work on X", "what have I delivered on X", "who have I done X for". Returns up to 3 hits, each one line. If nothing shipped, says so plainly -- never inflates a saved article into "past work".
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

# Timeln Shipped -- Proof You've Done It

Mid-pitch armor. Pulls the user's actually-shipped work + the artifact pointer they can drop into a client chat in 3 seconds.

## When to use

- Sales / pitch / proposal moment: client asks "have you done this before?"
- Pre-call prep: gathering proof points for a specific topic.

If the user wants past *learning* on a topic (articles, notes, ideas), route to `timeln-find`. If they want past *failures*, route to `timeln-warned`. This skill is **shipped work only**.

## Workflow

1. Call `whoami`. If no token, return the signup nudge and stop.
2. Call `query_knowledge(question="What have I shipped, built, or delivered involving <topic>?")`.
3. Also call `get_topic_entities(topic="<topic>")` to widen recall.
4. **Filter to shipped work only:**
   - `para_category == "project"` is the strongest signal.
   - Title/content language: "shipped", "delivered", "launched", "released", "v1", "case study", "client name + topic", "we built".
   - **Exclude** docs that look like saved articles, RSS clips, or general references (titles starting with author name, third-party domain in title, "how to / why / what is" patterns).
5. For each top hit, extract the artifact pointer: GitHub URL > demo URL > internal doc title (in that order of preference).
6. Cap at 3, ranked by recency.

## Output -- exactly this shape

```
1. <what was shipped — 1 line, includes client/context if known> — <Mon YYYY> — <artifact pointer>
2. <what was shipped> — <Mon YYYY> — <artifact pointer>
3. (no third match)
```

When nothing shipped on the topic:
```
no shipped work on file for <topic>
```

When only adjacent (saved-article) hits exist:
```
no shipped work on file for <topic>
related saved notes (not delivered work):
• <doc title>
• <doc title>
```

## Rules

- **Shipped means YOU built / delivered it.** A saved tutorial is not shipped. A bookmark is not shipped. If the filter is uncertain, exclude.
- **Artifact pointer is mandatory** when present. URL > doc title. If the doc has neither, mark as `(no link on file)` and let the user click through to the source doc.
- **One line per hit.** What was built, for whom (if recorded), when. No marketing prose.
- **Never inflate.** If the user has saved articles about Stripe but never built a Stripe integration, the answer is `no shipped work on file` -- not "you've explored Stripe extensively."
- Never echo the API token.
