---
name: consult-arc
description: >
  Trigger on "solution arc", "current state target state", "consult narrative",
  "storyline for proposal", "MVP pilot full as risk", "sequencing rationale".
  Builds one arc: as-is → target capability → why this order, with options tied to
  risk reduction. NOT the frame card (use consult-frame), NOT gate tables
  (use consult-gates), NOT diagrams (use arch-diagrams).
license: MIT
---

# Consult Arc -- Solution Story

One coherent narrative: current state → target capability → why this sequence; options framed as risk reduction.

## Inputs

| Input | Required |
|---|---|
| Frame card from `consult-frame` | yes |
| Capability target or constraints from source | yes |

Optional: `timeln-shipped` / `timeln-find` for proof and analogs -- one line each, no fake past work.

## Workflow

1. **Current state** -- 3-6 bullets: what exists today (people, data, systems, process). No blame tone.
2. **Target capability** -- one paragraph: what the org can **do** after engagement, not tool names unless source names them.
3. **Sequencing rationale** -- ordered list: what you prove first vs later; each step names **risk removed** or **decision unlocked**.
4. **Options** -- exactly three rows unless source forbids: MVP, Pilot, Full. Each: intent, primary risk reduced, what you explicitly **do not** claim yet.
5. **Single-thread check** -- one sentence: "This arc answers: <primary question from frame>."

## Output -- exactly this shape

```
## Arc -- <client or "TBD"> -- <YYYY-MM-DD>

**Current state**
- ...

**Target capability**
<short paragraph>

**Why this sequence**
1. ... → reduces: ...
2. ...

**Options (risk-reduction framing)**
| Option | Intent | Risk reduced | Not claiming yet |
|---|---|---|---|
| MVP | | | |
| Pilot | | | |
| Full | | | |

**Thread**
This arc answers: "<primary decision / question>".
```

## Rules

- Options are not feature shopping lists -- every cell must tie to risk or decision.
- If MVP/Pilot labels do not fit, rename rows to match source language but keep three graduated commitment levels max.
- Do not duplicate phasing gates -- stop at narrative; phase mechanics go to `consult-gates`.

## Common failure modes

| Mistake | Fix |
|---|---|
| "We will implement X, Y, Z" in options | Reframe as risk removed and decision proven |
| Target = vendor name | Rewrite as capability; put vendor in a note only if cited |
| Two arcs for two audiences | One arc; `consult-package` splits audience later |
