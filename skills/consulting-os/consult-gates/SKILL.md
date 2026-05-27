---
name: consult-gates
description: >
  Trigger on "lock phasing", "stage gates", "consult gates", "phase outcomes",
  "primary question per phase", "entry exit criteria", "gate table".
  Defines staged outcomes with one primary question per phase plus entry/exit.
  NOT acceptance metrics (use consult-acceptance), NOT personal save cascade
  (timeln-plan is parallel -- use its output as optional input only).
license: MIT
---

# Consult Gates -- Stage Gate Table

Break work into stages; each stage answers one primary question; gates have entry and exit.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Phasing hints from `consult-arc` | yes | Sequence + option (MVP/Pilot/Full) if chosen |
| `timeln-plan` artifact or stage list | optional | Import stage names / bets as raw material only -- rewrite for **client** phases |

## Workflow

1. Name **3-5 phases** max (merge weak phases). Order is linear unless source needs parallel -- if parallel, split rows and note dependency.
2. For each phase write:
   - **Primary question** -- exactly one yes/no or decidable question.
   - **Entry criteria** -- what must be true to start.
   - **Exit / outcome** -- what exists when the gate opens.
   - **Gate owner** -- role who says the gate passed; `unknown -- confirm` if missing.
3. Add **between-stage notes** only where ordering is controversial (one line: what must not happen out of order).

## Output -- exactly this shape

```
## Gates -- <client or "TBD"> -- <YYYY-MM-DD>

**Selected option:** MVP | Pilot | Full | mixed -- <note>

| Phase | Primary question | Entry | Exit / outcome | Gate owner |
|---|---|---|---|---|
| 1 ... | | | | |
| 2 ... | | | | |

**Sequencing locks**
- ...
```

## Rules

- Primary question is not a task list -- it is what the phase **decides**.
- If input from `timeln-plan` conflicts with `consult-arc`, prefer `consult-arc` for naming; pull content from plan only when clearly the same engagement.
- Do not add acceptance metrics here -- qualitative gate only; metrics go to `consult-acceptance`.

## Common failure modes

| Mistake | Fix |
|---|---|
| "Phase 2: build stuff" | Replace with the question phase 2 answers |
| Same owner for every gate | Split or name RACI per phase |
| More than one primary question in a row | Split phase or merge until one remains |
