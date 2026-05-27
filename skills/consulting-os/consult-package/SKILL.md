---
name: consult-package
description: >
  Trigger on "package for exec", "consult deliverable pack", "appendix vs main deck",
  "client-ready consulting doc", "strip placeholders proposal", "readout structure".
  Assembles exec layer vs detail, removes placeholders, runs consistency pass.
  Produces client-facing artifact + lint report (inline `consult-consistency-lint` or separate).
license: MIT
---

# Consult Package -- Client-Ready Pack

Split executive storyline from detail; strip placeholders; align narrative ↔ gates ↔ acceptance ↔ commercial ↔ architecture; attach lint report.

## Inputs

| Input | Required |
|---|---|
| `consult-frame` through `consult-commercial` outputs | yes |
| Architecture reference (from `arch-diagrams` or user paste) | recommended |

Prefetch skills as needed before packaging: `timeln-quickly` for verbatim quotes in Q&A appendix only when user asks.

## Workflow

1. **Executive layer (≤2 pages or ≤10 slides outline)**
   - Primary decision, definition of good, recommended option, why this sequence in 5 bullets max, top 3 risks, next step to sign.
2. **Detail layer**
   - Full arc (abbreviate if duplicate), gate table, acceptance matrix, commercial section -- as appendix headings matching source order.
3. **Architecture insert**
   - One placement only (exec summary pointer + full diagram in appendix). Caption: layers, shared vs optional, explicit non-claims.
4. **Placeholder strip** -- replace `TBD` with either resolved text or `Open: ...` with owner; remove `lorem` and template stubs.
5. **Consistency** -- run the same checks as `consult-consistency-lint`; embed **Lint summary** at end of artifact or ship as sibling block.
6. **Verification checklist** (tick only when true):
   - [ ] Frame decision appears in exec opening
   - [ ] Every gate phase has acceptance
   - [ ] Diagram elements map to named deliverables or labeled out-of-scope
   - [ ] Commercial assumptions have failure impact
   - [ ] No orphan placeholders in exec layer

## Output -- exactly this shape

```
## Pack -- <client or "TBD"> -- <YYYY-MM-DD>

### Executive summary
...

### Recommendation & risks
...

### Next step to sign
...

---

### Appendix A -- Arc
...

### Appendix B -- Gates
...

### Appendix C -- Acceptance
...

### Appendix D -- Commercial
...

### Appendix E -- Architecture
<embed or path note>

---

### Lint summary
<paste consult-consistency-lint Summary + Critical/Warning counts + top 5 FINDING rows or "clean">

### Verification
- [ ] ...
```

## Rules

- If lint shows **critical** findings, top of exec summary must include **Open consistency items** (bullet list of IDs) -- do not bury.
- Do not add new scope in packaging; only reorganize and clarify.
- One architecture story -- if multiple diagrams exist, pick reference; list alternates under Appendix E as `superseded -- do not use` or merge user direction.

## Common failure modes

| Mistake | Fix |
|---|---|
| Appendix is longer than main + unreadable | Collapse tables; keep full tables in second artifact if user requests |
| Exec layer repeats appendix verbatim | Exec = decisions; appendix = evidence |
| Lint never run | Block ship; run embedded `consult-consistency-lint` |

## Pairing

| Step skill | Role in pack |
|---|---|
| consult-frame | Exec opening + scope |
| consult-arc | Exec storyline + App A |
| consult-gates | App B; informs exec risks |
| consult-acceptance | App C |
| consult-commercial | App D |
| arch-diagrams | App E |
| consult-consistency-lint | Lint summary + gate on criticals |
