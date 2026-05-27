---
name: consult-red-team
description: >
  Trigger on "red team proposal", "devil's advocate proposal", "stress test
  proposal", "consult red team", "win themes challenge", "cos red team".
  Multi-perspective review: client exec, procurement, technical skeptic,
  devil's advocate. Feeds timeln-warned scars into DA. NOT lint
  (consult-consistency-lint), NOT integrity (consult-integrity).
license: MIT
---

# Consult Red Team -- Multi-Perspective Proposal Review

Stress-test the engagement pack before ship. Anti-sycophancy: Devil's Advocate concedes only when severity ≥ 4 (1–5 scale).

## Inputs

| Input | Required |
|---|---|
| Latest frame through commercial + architecture pointer | yes |
| `lint-report.md` if exists | recommended |
| Framework variant index + chosen merge | recommended |
| **`timeln-warned`** on primary technical bet | run before review |

## Prefetch (mandatory)

1. **`timeln-warned`** — topic = primary technical path from arc (e.g. "GPU fine-tuning FSI transcripts")
2. Pass top scars into Devil's Advocate section verbatim

## Four perspectives

| Perspective | Question | Output |
|---|---|---|
| **Client exec** | Can I say yes/no in one read? | Score 0–100 + 3 bullets |
| **Procurement** | Are assumptions, out-of-scope, and commercial gaps visible? | Findings table |
| **Technical skeptic** | Does architecture + acceptance hold under audit? | Findings table |
| **Devil's advocate** | What kills this deal? Use timeln-warned scars. Concede only if severity ≥ 4 | BLOCK / ALLOW + severity |

Scoring rubric for exec perspective: reuse `../consult-arc/FRAMEWORK-VARIANTS.md` criteria (decision clarity, measurability, commercial defensibility, technical credibility) — average × 20 for 0–100.

## Verdict

- **BLOCK** — DA severity ≥ 4 on any show-stopper, OR exec score < 60
- **ALLOW** — otherwise; warnings ship with pack

## Output -- exactly this shape

```
## Red team -- <client> -- <YYYY-MM-DD>

**Verdict:** BLOCK | ALLOW
**Exec score:** <0-100>

### Client exec
- ...
**Score rationale:** ...

### Procurement
| Finding | Severity | Suggested fix |
|---|---|---|

### Technical skeptic
| Finding | Severity | Suggested fix |
|---|---|---|

### Devil's advocate
**Severity (1-5):** n
**Scars from timeln-warned:**
- ...
**Challenge:** ...
**Concede?** yes (≥4) | no

### Merge recommendation
<one line if variants exist>
```

## Rules

- Do not resolve lint/integrity conflicts — reference finding IDs.
- DA must cite timeln-warned when available; if no record, say so — do not invent failures.
- BLOCK triggers pipeline revision loop (max 2).
