# Timeln Plan — {{WINDOW}}

**{{TOTAL_SAVES}} saves** processed through 6 frameworks · generated {{GENERATED_AT}} · account: {{ACCOUNT}}

---

## Stage 1 — PARA · sort signal

**Input:** {{TOTAL_SAVES}} documents from {{WINDOW}} (titles + summaries + topics)

**Decision rule:** Project = ship date or customer-visible output. Area = ongoing theme. Resource = will reference within 30 days. Everything else → archive or drop.

**Pass through:**

| Bucket | Count | Treatment |
|--------|------:|-----------|
{{PARA_TABLE_ROWS_MD}}

{{PARA_FLAGS_MD}}

**→ {{PARA_PASS_COUNT}} meaningful saves pass forward**

---

## Stage 2 — MECE · remove overlap

**Input:** {{PARA_PASS_COUNT}} categorised saves with topic tags

**Decision rule:** Group all saves into exactly 4 non-overlapping clusters. Each save belongs to one cluster only. Cross-cluster saves reveal execution gaps.

**Pass through — 4 distinct clusters:**

{{MECE_CLUSTERS_MD}}

**Dropped at this stage:** {{MECE_DROPPED_MD}}

**→ 4 clusters → crystallised into actionable bets**

---

## Stage 3 — RICE · score & rank

**Input:** one bet per cluster ({{RICE_BET_COUNT}} total)

**Formula:** RICE = (Reach × Impact × Confidence) ÷ Effort
- R, I scored 1–10 · C scored 0.3–1.0 · E scored 1–10 (higher = more work)

**Pass through — ranked:**

| Rank | Bet | R | I | C | E | Score |
|-----:|-----|--:|--:|--:|--:|------:|
{{RICE_ROWS_MD}}

**→ ranked bets + commitments → placed into 4 quadrants**

---

## Stage 4 — Eisenhower · map urgency

**Input:** {{RICE_BET_COUNT}} RICE-ranked bets + committed items + floating Area saves = {{EISEN_TOTAL}} items

**Decision rule:** Urgent + Important → Q1. Important, not urgent → Q2 (deep work). Urgent, not important → Q3 (batch). Neither → Q4 (drop).

**Pass through:**

### Q1 · do now · {{Q1_COUNT}} items
{{Q1_ITEMS_MD}}

### Q2 · schedule · {{Q2_COUNT}} items
{{Q2_ITEMS_MD}}

### Q3 · batch · {{Q3_COUNT}} items
{{Q3_ITEMS_MD}}

### Q4 · drop · {{Q4_COUNT}} items
{{Q4_ITEMS_MD}}

**→ Q1 + Q2 pass forward · Q3 + Q4 exit the system here**

---

## Stage 5 — GTD · next action

**Input:** {{GTD_COUNT}} items from Q1 + Q2

**Decision rule:** Each item must become one physical action in `verb + object + where` format. If you can't write it that way, it's still a project — break it down.

**Pass through:**

{{GTD_ACTIONS_MD}}

**→ {{GTD_COUNT}} concrete next actions enter the accountability layer**

---

## Stage 6 — 4DX · stay accountable

**Input:** {{GTD_COUNT}} next actions + bottleneck diagnosis: *{{BOTTLENECK}}*

**Decision rule:** One WIG only. Two lead measures, predictive and within direct control. Weekly 15-min scoreboard.

**Pass through:**

> **WIG (lag measure):** {{WIG_TEXT}}

- **Lead 1:** {{LEAD_1}}
- **Lead 2:** {{LEAD_2}}

*Cadence:* {{CADENCE}}

---

**Pipeline summary:** {{TOTAL_SAVES}} saves → {{GTD_COUNT}} actions → 1 WIG
