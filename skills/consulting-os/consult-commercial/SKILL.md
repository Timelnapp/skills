---
name: consult-commercial
description: >
  Trigger on "consult commercial", "SOW section", "mobilization", "duration and options",
  "assumptions access env people", "proposal to kickoff", "cadence escalation",
  "roles RACI consulting". Commercial wrapper: timeboxes, assumptions, path to kickoff.
  NOT acceptance matrix (use consult-acceptance), NOT exec polish (use consult-package).
license: MIT
---

# Consult Commercial -- Commercial Pack Section

Duration, options, assumptions, path from proposal → SOW → kickoff: roles, cadence, escalation.

## Inputs

| Input | Required |
|---|---|
| Gate table from `consult-gates` | yes |
| Acceptance matrix from `consult-acceptance` | yes |

Optional: `timeln-shipped`, `timeln-decided` for precedent duration or past access assumptions -- cite or `no record`.

## Workflow

1. **Duration** -- per option if still open (MVP/Pilot/Full), else single track. Use ranges with drivers (unknowns listed).
2. **Commercial options** -- align names to `consult-arc`; what is included / excluded per option (short bullets).
3. **Assumptions** -- access (systems, data, people), environments, locations, security reviews, legal; mark **dependency** vs **working assumption**.
4. **Mobilization** -- proposal → SOW → kickoff checklist; pre-kickoff deliverables from client side.
5. **RACI-lite** -- who decides, who does daily work, who escalates; match gate/acceptance owners where possible.
6. **Cadence** -- standing meetings, reporting, written status; **escalation** path (when to pause billing / stop work) if appropriate.
7. **Change control** -- one paragraph: how scope/time shifts propagate (reference gates).

## Output -- exactly this shape

```
## Commercial -- <client or "TBD"> -- <YYYY-MM-DD>

**Duration**
- Option ...: <range> -- drivers: ...

**What’s in / out by option**
- MVP: in ... / out ...
- ...

**Assumptions**
| Assumption | Type (dependency / working) | If false |
|---|---|---|
| | | |

**Path: proposal → SOW → kickoff**
1. ...
2. ...

**Roles**
| Role | Name / team | Responsibility |
|---|---|---|
| | | |

**Cadence & escalation**
- Cadence: ...
- Escalation: ...

**Change control**
<short paragraph>
```

## Rules

- Do not contradict acceptance deliverables -- if tension, flag under **Global gaps** in output: `conflict: ...`.
- No rates unless user supplies; use `pricing -- client to supply`.
- Assumptions without an "if false" row are incomplete.

## Common failure modes

| Mistake | Fix |
|---|---|
| Copy-paste full SOW | Keep section-level; legal text belongs with counsel |
| Assumptions list without failure impact | Add "If false" column |
| Roles list without escalation | Add who pulls the cord when gates fail |
