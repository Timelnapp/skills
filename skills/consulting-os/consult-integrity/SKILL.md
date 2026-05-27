---
name: consult-integrity
description: >
  Trigger on "consult integrity", "integrity gate", "integrity check",
  "verify proposal claims", "hallucination check proposal", "cos integrity".
  Seven-mode failure checklist at gates 3.5 and 5.5. Uses timeln-quickly and
  timeln-shipped to verify quotes and proof claims. NOT lint (use
  consult-consistency-lint), NOT red team (use consult-red-team).
license: MIT
---

# Consult Integrity -- Proposal Integrity Gate

Catch integrity failures before architecture (3.5) and before ship (5.5). Human-in-the-loop — report only; do not auto-fix.

## Inputs

| Input | Required | Gate |
|---|---|---|
| `01-frame` through `05-commercial` | yes | 3.5 |
| Source transcript / brief in `Input/` | yes | 3.5 |
| Architecture artifact | yes | 5.5 |
| Framework variants + lint input | recommended | 5.5 |
| **`timeln-quickly`** output on client quotes | run before gate | both |
| **`timeln-shipped`** output on proof claims | run before gate | both |

## Prefetch (mandatory)

Before running checks, invoke:

1. **`timeln-quickly`** — for each direct client quote in frame/arc/commercial: `"what did they say about <topic>"`
2. **`timeln-shipped`** — for each "we've done / delivered / shipped" claim in arc/commercial/variants

Record prefetch results in the integrity report under `## Timeln verification`.

## Seven modes

| ID | Mode | Check | Critical when |
|---|---|---|---|
| I1 | **Citation integrity** | Client quotes trace to `Input/` or Timeln with doc title | Quote invents client language |
| I2 | **Proof integrity** | Shipped claims match `timeln-shipped` or marked `no record — remove or soften` | Fabricated past work |
| I3 | **Scope lock** | Out-of-scope in frame absent from deliverables/acceptance | Scope creep |
| I4 | **Option drift** | MVP/Pilot/Full (or chosen option) consistent arc → gates → commercial | Conflicting option names |
| I5 | **Metric fabrication** | Numbers in acceptance/commercial sourced or `TBD metric -- workshop` | Invented SLOs or lift % |
| I6 | **Stakeholder invention** | Named roles in gates/acceptance in source or `unknown -- confirm` | Fake gate owners |
| I7 | **Diagram orphan** | Each architecture box maps to arc noun or acceptance row; unmapped promises flagged | Diagram promises extra work |

Gate **3.5**: run I1–I6 (skip I7 if no diagram yet).
Gate **5.5**: run all I1–I7.

## Verdict

- **PASS** — zero critical findings
- **FAIL** — one or more critical; block next pipeline stage

Warnings do not block; list for user acknowledgment.

## Output -- exactly this shape

```
## Integrity -- <client> -- <YYYY-MM-DD>

**Gate:** 3.5 | 5.5
**Verdict:** PASS | FAIL

## Timeln verification
| Claim / quote | timeln skill | Result |
|---|---|---|
| "..." | timeln-quickly | match / no record / mismatch |
| We shipped X | timeln-shipped | cited / no record |

**Summary**
- Critical: <n>
- Warning: <n>

**Findings**
| ID | Mode | Severity | Where | Issue | Fix |
|---|---|---|---|---|---|
| IG1 | I1 citation | critical | 02-arc | Quote not in transcript | Remove or mark paraphrase |

**Clean checks passed**
- ...
```

## Rules

- Do not invent Timeln results — if MCP skipped, note `timeln skipped` and downgrade I1/I2 to warning unless source doc verifies.
- Suggested fix is one line; no full rewrites.
- FAIL at 3.5 blocks ARCHITECT; FAIL at 5.5 blocks PACKAGE.
