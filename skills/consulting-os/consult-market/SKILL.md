---
name: consult-market
description: >
  Trigger on "find similar clients", "lookalike accounts", "who else would buy
  this", "market research for this use case", "expand after a win", "consult
  market", "cos market", "/cos-market". Manual seed (industry + size + use case)
  → ranked top-5 lookalike target list with why-it-fits rationale and
  verified-or-labeled contacts. Uses timeln-find; optional Apollo/Clay/Exa.
  NOT outreach (use consult-pursue), NOT framing (use consult-frame).
license: MIT
---

# Consult Market -- Lookalike Target List

After a win, find the **next 5 companies** in the same industry and size who would buy the same use case. One job: a ranked, sourced target list — not outreach, not a pitch.

## Inputs (manual — ask if missing)

| Input | Required | Notes |
|---|---|---|
| **Industry / vertical** | yes | e.g. "regional telco", "DTC supplements" |
| **Company size band** | yes | revenue, headcount, or both — e.g. "200–2,000 staff" |
| **Use case** | yes | one line on what was sold/won — the buyer's reason to care |
| Region / geography | optional | default: same region as the win |
| Exclusions | optional | the won client, named competitors, do-not-contact list |

No `engagement-passport.yaml` needed. If the user points at a won proposal pack, use it only to sharpen the use-case one-liner — do not require it.

## Data sources (degrade gracefully)

1. **`timeln-find`** — analogous engagements / accounts already in memory. Run first; cite titles only.
2. **Web + Exa** — public firmographics, recent buying signals (funding, hires, product launches, regulatory pressure, RFPs). Every company → source URL.
3. **Apollo / Clay** — *only if connected* — firmographic filtering and verified contacts. If absent, skip silently; do not block.

If Timeln MCP is unavailable, note `timeln skipped — no MCP` and continue with web + Exa only. Never fabricate memory results.

## Workflow

1. Confirm the three required inputs; restate the use case in one buyer-centric sentence.
2. `timeln-find` for accounts/engagements that match the vertical + use case.
3. Web/Exa (and Apollo/Clay if present) to build a candidate pool; filter to the size band and region.
4. Score each candidate 0–3 on four axes — **industry match, size match, use-case fit, signal recency** — and keep the **top 5**.
5. For each kept company write a one-line **why-it-fits** tied to the won use case (not generic firmographics).
6. Add the **best-fit contact**: name + role + LinkedIn/company URL. Email only if a verified source returns it. Otherwise mark `not verified — enrich`. **Never guess or pattern-build emails.**
7. Write the markdown table, then the CSV (always) and offer XLSX via the `xlsx` skill. Save to the path the user names (default `./lookalikes/{use-case-slug}-targets.md` + `.csv`).

## Output -- exactly this shape

```
## Lookalike targets -- <use case> -- <YYYY-MM-DD>

**Seed:** <industry> · <size band> · <region> · use case: <one line>
**Sources:** timeln-find | web/Exa | Apollo/Clay (if used)

| # | Company | Why it fits (vs use case) | Industry | Size | Buying signal (date + source) | Contact (name · role) | Contact detail | Score /12 |
|---|---------|---------------------------|----------|------|-------------------------------|-----------------------|----------------|-----------|
| 1 | | | | | | | verified / not verified — enrich | |

**Scoring:** industry + size + use-case fit + signal recency, each 0–3.

**Excluded / parked**
- <company> — <reason>

**Next step:** `/cos-pursue {company} for {use case}` to draft outreach (cold-start).
```

CSV columns mirror the table (one row per company). Confidence = the /12 score.

## Rules

- Top 5 only — tight beats wide. Park extras under "Excluded / parked" with a reason.
- Every company carries a **source URL** or a `timeln-find` title; no unsourced names.
- Contact emails are **verified-source-only**. No domain-pattern guessing, ever.
- `why-it-fits` must reference the won use case, not just "same industry".
- Do not write outreach copy here — hand off to `consult-pursue`.
- If a signal can't be found for a candidate, keep it but score signal-recency 0 and say `no recent signal`.

## Common failure modes

| Mistake | Fix |
|---|---|
| Generic "same vertical" rationale | Tie why-it-fits to the buyer's reason for the won use case |
| Guessed emails (`first.last@`) | `not verified — enrich`; only verified-source emails go in |
| 20-company dump | Score, keep top 5, park the rest |
| Listing the won client or its direct competitor | Honor exclusions; default-exclude the won client |
| Drifting into a pitch | Stop at the list; point to `/cos-pursue` |
