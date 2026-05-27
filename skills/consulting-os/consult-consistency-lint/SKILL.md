---
name: consult-consistency-lint
description: >
  Trigger on "consult lint", "consistency pass", "diagram vs narrative",
  "broken promises across docs", "cross-artifact check", "scope drift lint".
  Read-only diff across frame, arc, gates, acceptance, commercial, architecture
  artifact. NOT rewriting copy (use consult-package), NOT drawing diagrams
  (use arch-diagrams).
license: MIT
---

# Consult Consistency Lint -- Cross-Artifact Diff

Flag inconsistencies: text vs diagram, missing acceptance for a phase, duplicated/conflicting scope, option drift.

## Inputs

| Input | Required |
|---|---|
| Latest `consult-frame`, `consult-arc`, `consult-gates`, `consult-acceptance`, `consult-commercial` | yes |
| Architecture artifact (Mermaid, draw.io path, image, or bullet list from `arch-diagrams`) | optional |

## Workflow

1. **Phase coverage** -- every phase in gates has exactly one acceptance row; flag orphans either direction.
2. **Option alignment** -- MVP/Pilot/Full names and definitions match across arc, gates, commercial; flag renamed or missing options.
3. **Scope strings** -- in/out scope in frame must not reappear as promised deliverables unless explicitly in acceptance; flag contradictions.
4. **Decision thread** -- arc "thread" sentence must match frame primary decision; flag mismatch.
5. **Diagram vs text** -- for each box/layer in the architecture artifact, map to a noun in arc or acceptance; unmapped diagram elements or unmapped promises in text get **FINDING**.
6. **Commercial vs gates** -- durations/options must reference the same phased path; flag phases with no timebox or timebox with no phase.
7. **Placeholder scan** -- `TBD`, `TODO`, `unknown -- confirm`, `lorem`, angle brackets; list file/section if known from paste titles.

## Output -- exactly this shape

```
## Lint -- <client or "TBD"> -- <YYYY-MM-DD>

**Summary**
- Critical: <n>
- Warning: <n>

**Findings**
| ID | Severity | Where | Issue | Suggested fix |
|---|---|---|---|---|
| L1 | critical | ... | ... | ... |

**Clean checks passed**
- <bullet list of checks that passed>
```

Severity: `critical` = would embarrass in client readout or breaks contract intent; `warning` = clarity or internal consistency.

## Rules

- Do not invent architecture elements -- if no diagram supplied, skip diagram checks and note `skipped -- no architecture artifact`.
- If an input artifact is missing, list as `missing -- <skill name>` and skip dependent checks.
- Suggested fix is one line each; no full rewrites.

## Common failure modes

| Mistake | Fix |
|---|---|
| Nitpicking tone differences | Only flag semantic or commitment drift |
| Auto-resolving conflicts | Report -- let owner choose |
| Missing diagram treated as pass | Must emit skipped line |
