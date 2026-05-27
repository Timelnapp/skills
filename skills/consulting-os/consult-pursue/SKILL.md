---
name: consult-pursue
description: >
  Trigger on "pursue client", "pitch email", "follow up proposal", "call script
  proposal", "consult pursue", "cos pursue", "/cos-pursue {client} for {topic}".
  Post-pack pursuit: cover email, 30-min call script, objection stubs. Cold-start
  mode when only client + topic given — synthesizes pack from public research.
  Uses timeln-shipped and timeln-quickly. NOT packaging (consult-package), NOT
  frame (consult-frame).
license: MIT
---

# Consult Pursue -- Post-Pack Pursuit

Turn the shipped pack into client-facing pursuit artifacts.

Two modes — pick from inputs (do not ask unless ambiguous):

| Mode | When | Pack source |
|------|------|-------------|
| **Standard** | `{Client}-Engagement-Proposal-Pack.md` exists | Existing pack |
| **Cold-start** | User gives **client + topic only**; no pack, no Input brief | Synthesize from public research + Timeln |

---

## Inputs

| Input | Standard | Cold-start |
|---|---|---|
| `{Client}-Engagement-Proposal-Pack.md` | yes | **create** from template |
| `engagement-passport.yaml` (`option_selected`) | yes | **create/update** — default `POC` unless pack says otherwise |
| **`timeln-shipped`** on engagement topic | run before write | run before write |
| **`timeln-quickly`** on client names, dates, numbers | run before write | run — expect `no record`; use public stats only, label source |

Templates: `cold-start/` (see **`cold-start/EXAMPLES.md`** for folder layout)

Showcases: `examples/ho-brothers/` · `examples/vodafone-portugal/`

---

## Cold-start workflow (client + topic only)

Run in order when pack or Input brief is missing:

1. **Slug** — infer `{slug}`: lowercase, hyphenated (`Vodafone Portugal` → `vodafone-portugal`). Create `prospects/{slug}/` from `../consult-pipeline/prospect-template/` if missing.

2. **Public research** — web search: incumbent products, public metrics, partners, regional initiatives. Write `prospects/{slug}/00-research-public.md` (template: `cold-start/00-research-public.md`). Every claim → source URL or `assumption`.

3. **Synthesized pack** — if no pack exists, write `prospects/{slug}/{Client}-Engagement-Proposal-Pack.md` from `cold-start/proposal-pack-synthesized.md`:
   - Header must include `(synthesized)` and `Public research only — no client transcript or RFP on file`
   - Primary decision = **next-phase** pitch (extend incumbent stack, not replace)
   - Default options: A Discovery / **B POC** ✓ / C stretch (voice or scale)
   - Do **not** invent fees — `TBD after access workshop`
   - Do **not** invent contact names — `TBD`

4. **Passport** — set `stage: PURSUE`, `option_selected: POC` (or pack selection), `source_mode: cold_start`, record `timeln_pulls`.

5. **Prefetch** — `timeln-shipped` + `timeln-quickly` (same as standard).

6. **Pursue artifacts** — email + call script (below). Label proof: `timeln-shipped` | `from pack only` | `public source`.

7. **Say to user:** folder path (`prospects/{slug}/` — single folder, all artifacts), what was synthesized vs verified, upgrade path (`/cos-research` when brief arrives).

### Cold-start folder layout (single folder — mandatory)

Everything in **`prospects/{slug}/`** only. No `Output/{Client}-Engagement/` for cold-start.

```
prospects/{slug}/
├── engagement-passport.yaml
├── README.md                           # optional index
├── Input/                              # optional — briefs when they arrive
├── 00-research-public.md
├── {Client}-Engagement-Proposal-Pack.md
└── pursue/
    ├── email.md
    └── call-script.md
```

Passport paths are **relative to slug root** (see `cold-start/EXAMPLES.md`). Full pipeline (stages 1–6) may add `Output/{Client}-Engagement/` later when upgrading — do not nest cold-start files there first.

---

## Prefetch (mandatory — both modes)

1. **`timeln-shipped`** — top 3 proof points for credibility paragraph
2. **`timeln-quickly`** — decision owner name, timeline quotes, budget signals if any

If `no record`, omit client-specific quotes; use pack or public sources only — never fabricate Timeln results.

---

## Standard workflow

1. **Cover email** (≤250 words): primary decision, recommended option, one proof line from timeln-shipped, next step, attachment pointer.
2. **30-min call script**: opening (2 min), decision recap (5 min), recommendation walk (10 min), risks + assumptions (5 min), close + ask (5 min), Q&A stubs (3+).
3. **Objection stubs** (max 5): objection → response → proof pointer — in call-script §Objection stubs.

---

## Output -- write to `pursue/`

Use templates under `cold-start/pursue/` when cold-start.

### `pursue/email.md`

```
## Subject
...

## Body
...

## Proof used (timeln-shipped)
- ...

## Attachments
- ...
```

### `pursue/call-script.md`

```
## Call script -- <client> -- <YYYY-MM-DD>

**Attendees:** ...
**Goal:** ...

### Opening (2 min)
...

### Decision recap (5 min)
...

### Recommendation (10 min)
...

### Risks & assumptions (5 min)
...

### Close (5 min)
**Ask:** ...

### Q&A stubs
| Question | Response | Source |
|---|---|---|

### Objection stubs (internal prep)
| Objection | Response | Proof |
|---|---|---|
```

---

## Rules

- Do not add scope beyond pack (standard) or synthesized pack (cold-start).
- Proof claims must match timeln-shipped, be labeled `from pack only`, or `public source` with URL.
- Email must reference exec summary decision in first paragraph.
- Cold-start packs and emails must state assumptions explicitly; never present synthesis as client-validated fact.
- If Timeln MCP unavailable: note in passport `timeln skipped — no MCP`; use filesystem use cases + public research only.

---

## Common failure modes

| Mistake | Fix |
|---|---|
| Greenfield chatbot pitch when client already has SuperTOBi / Copilot / etc. | Research incumbent stack; pitch **next phase** (agentic, eval, BSS tool use) |
| Inventing €/$ fees or contact names | TBD + role placeholders |
| Skipping `00-research-public.md` in cold-start | Always write — pursue cites public stats from here |
| Nesting cold-start under `Output/{Client}-Engagement/` | Write flat under `prospects/{slug}/` — see `cold-start/EXAMPLES.md` |
| Treating saved articles as shipped work | timeln-shipped filter: `para_category == project` + delivery language only |
