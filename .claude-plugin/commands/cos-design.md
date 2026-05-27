# /cos-design — Stage 3 DESIGN

Run arc → gates → acceptance → commercial in order. Timeln before each sub-step:

| Step | Timeln | Skill | Output |
|------|--------|-------|--------|
| Arc | `timeln-shipped`, `timeln-warned` | `consult-arc` | `02-arc.md` |
| Gates | `timeln-decided` | `consult-gates` | `03-gates.md` |
| Acceptance | `timeln-warned` | `consult-acceptance` | `04-acceptance.md` |
| Commercial | `timeln-decided`, `timeln-shipped` | `consult-commercial` | `05-commercial.md` |

**Checkpoint:** User picks option → `option_selected`, `checkpoints.option_picked`.

Then run `/cos-integrity` (gate 3.5).
