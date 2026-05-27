# Consulting OS commands

Thin wrappers for **`consult-pipeline`** stages. Each command lists Timeln prefetch + consult skill.

| Command | Stage | Timeln skills |
|---------|-------|---------------|
| [/cos-plan](cos-plan.md) | 0 CAPTURE | timeln-plan (optional) |
| [/cos-research](cos-research.md) | 1 RESEARCH | find, decided |
| [/cos-frame](cos-frame.md) | 2 FRAME | find, quickly |
| [/cos-design](cos-design.md) | 3 DESIGN | shipped, warned, decided |
| [/cos-integrity](cos-integrity.md) | 3.5 / 5.5 | quickly, shipped |
| [/cos-architect](cos-architect.md) | 4 ARCHITECT | warned, decided |
| [/cos-variants](cos-variants.md) | 5 BUILD | shipped, find |
| [/cos-lint](cos-lint.md) | 5.5 REVIEW | warned |
| [/cos-ship](cos-ship.md) | 6 PACKAGE | quickly (optional) |
| [/cos-pursue](cos-pursue.md) | 7 PURSUE | shipped, quickly — **cold-start** if client+topic only |
| [/cos-resume](cos-resume.md) | any | per stage table |

Natural language: *"build a proposal for X"* → `/cos-plan`

Weekly: **`timeln-plan`** (not a cos command — solo ops cron)
