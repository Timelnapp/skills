---
name: consult-frame
description: >
  Trigger on "frame the engagement", "consult frame", "problem frame", "scope card",
  "definition of good", "what decision does this support", "in scope out of scope",
  "client brief → frame", "one-pager frame". Turns a brief or transcript into a
  structured engagement frame. NOT the solution arc (use consult-arc), NOT phasing
  gates (use consult-gates), NOT memory recall (use timeln-find / timeln-decided).
license: MIT
---

# Consult Frame -- Engagement Frame Card

Turn raw client input into one structured frame: decision, success definition, scope boundaries, stakeholders.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Brief, transcript, bullets, or notes | yes | Paste as-is if no file |
| Client / industry labels | if known | For naming only |

Optional prefetch (user may ask): `timeln-find` / `timeln-decided` for prior domain or settled calls -- cite titles only when using Timeln output.

## Workflow

1. Extract the **decision** the work supports (buy/build, fund phase, vendor pick, go/no-go, etc.). If multiple, pick the **primary**; list secondaries one line each.
2. Write **definition of good** -- observable outcome the client wants, not activity.
3. List **in scope** / **out of scope** as explicit bullets; flag **assumptions** that must hold or the frame is wrong.
4. Name **stakeholders**: decision owner, working team, approvers, blockers if mentioned.
5. Record **open questions** that block a firm frame (max 5).

## Output -- exactly this shape

```
## Frame -- <client or "TBD"> -- <YYYY-MM-DD>

**Primary decision:** <one sentence>

**Definition of good:** <one sentence>

**In scope**
- ...

**Out of scope**
- ...

**Assumptions**
- ...

**Stakeholders**
| Role | Name / team | Notes |
|---|---|---|
| Decision owner | |
| Delivery / working team | |
| Other | |

**Open questions**
1. ...
```

## Rules

- Do not write MVP/roadmap/phasing here -- frame only.
- If the source is silent on a section, write `unknown -- confirm` instead of inventing.
- One primary decision per card unless the source explicitly ties multiple decisions at the same level.

## Common failure modes

| Mistake | Fix |
|---|---|
| Bulleted features instead of "good" | Rewrite as outcome the exec would recognize as done |
| Scope creep in "good" | Move extra work to in-scope bullets or out-of-scope |
| Stakeholder = generic "business" | Replace with named role or `unknown -- confirm` |
