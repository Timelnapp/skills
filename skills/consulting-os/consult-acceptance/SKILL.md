---
name: consult-acceptance
description: >
  Trigger on "acceptance criteria", "consult acceptance", "success criteria",
  "signoff matrix", "deliverables per phase", "primary path fallback", "definition of done".
  Per-phase deliverables, measurable criteria (tech + business/ops), owner, primary path + fallback.
  NOT commercial terms (use consult-commercial), NOT gate questions (use consult-gates).
license: MIT
---

# Consult Acceptance -- Acceptance Matrix

Map each gate phase to deliverables, measurable success, sign-off, and fallbacks under uncertainty.

## Inputs

| Input | Required |
|---|---|
| Gate table from `consult-gates` | yes |

Optional: `timeln-warned` -- fold real past failures into fallback rows only when sourced; otherwise `unknown -- workshop`.

## Workflow

1. For **each phase row** in the gate table, add:
   - **Deliverables** -- nouns (artifacts, systems states, tests passed), not tasks.
   - **Technical success** -- measurable or binary checks.
   - **Business / ops success** -- how the business knows value landed.
   - **Sign-off owner** -- named role; align with gate owner or explain delta.
   - **Primary path** -- default path if no surprises.
   - **Fallback** -- what you do if the primary path fails technical or data reality; must stay inside scope of the phase.
2. Flag **missing measurability** with `TBD metric -- propose in workshop`.
3. If a phase has no plausible fallback, write **none -- escalate / stop** instead of soft language.

## Output -- exactly this shape

```
## Acceptance -- <client or "TBD"> -- <YYYY-MM-DD>

| Phase | Deliverables | Technical success | Business/ops success | Sign-off | Primary path | Fallback |
|---|---|---|---|---|---|---|
| ... | | | | | | |

**Global gaps**
- <rows needing client input>
```

## Rules

- Every phase from `consult-gates` gets exactly one matrix row unless merged explicitly in gates.
- Do not promise numbers the source did not provide -- use `TBD` with how you will derive them.
- Fallback is not scope expansion -- it is a scoped pivot.

## Common failure modes

| Mistake | Fix |
|---|---|
| Success = "complete phase 2" | Replace with checks a third party could verify |
| One generic sign-off for all | Per-phase owners or explicit "same as gate owner" |
| Fallback = "add more people" | Tie fallback to data, scope trim, or alternate design inside phase |
