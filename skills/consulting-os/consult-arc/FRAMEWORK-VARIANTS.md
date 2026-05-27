# Framework variant validation rubric

Score each variant **1–5** or Yes/No. Used by stage 5 BUILD and `consult-red-team` exec scoring.

| # | Criterion | 1 (weak) | 5 (strong) |
|---|-----------|----------|------------|
| 1 | **Decision clarity** | Exec needs multiple reads | Yes/no in one read |
| 2 | **Hypothesis sharpness** | Implicit bet | Explicit, falsifiable bet |
| 3 | **Outcome measurability** | Vague success | Auditable acceptance criteria |
| 4 | **Stakeholder map** | Generic roles | Each role knows their job |
| 5 | **Commercial defensibility** | Hidden assumptions | Assumptions + if-false visible |
| 6 | **Technical credibility** | Hand-wavy stack | Architecture ↔ acceptance aligned |
| 7 | **Win differentiation** | Generic vendor | Clear why you vs DIY/alternatives |
| 8 | **Conversation script** | Cannot run a call from doc | 30-min call runnable from doc alone |

**Exec score (0–100):** average of criteria 1, 3, 5, 6 × 20.

## Standard variant stack

| Variant | Framework | Best for |
|---------|-----------|----------|
| V1 | Pyramid + SCQA + Hypothesis | Exec readout, steering committee |
| V2 | Issue tree + Driver tree + Stage gates | Scope defense, fee justification |
| V3 | MECE options + Scenario tradeoffs | Client comparing paths/vendors |
| V4 | Outcomes→Outputs→Activities + RACI + 7-S | Multi-stakeholder delivery |
| V5 | Win themes + Decision map + Compliance | Competitive pursuit, procurement |

## Merge template

| If you liked… | Pull into final pack |
|---------------|----------------------|
| V1 opening | Exec summary + cover email |
| V2 middle | Scope appendix + gate calendar |
| V3 options table | Recommended path slide |
| V4 RACI + outcomes | SOW roles + acceptance |
| V5 matrix + win themes | Pursuit deck + RFP response |
