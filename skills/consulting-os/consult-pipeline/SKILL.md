---
name: consult-pipeline
description: >
  Trigger on "consult pipeline", "cos pipeline", "new prospect workflow",
  "run engagement pipeline", "build proposal end to end", "resume engagement",
  "/cos-plan", "/cos-resume". Orchestrates CAPTURE through SUMMARY with mandatory
  human checkpoints. Invokes existing consult-* and timeln-* skills at each stage
  — never duplicates Timeln logic. NOT a substitute for single-stage skills when
  user only wants one artifact.
license: MIT
---

# Consult Pipeline -- Solo-Founder Engagement Orchestrator

Runs the full pursuit workflow: **CAPTURE → RESEARCH → FRAME → DESIGN → INTEGRITY → ARCHITECT → BUILD → REVIEW → PACKAGE → PURSUE → DELIVER → CLOSE → SUMMARY**.

Human decides at every checkpoint. Max **2 revision loops** between REVIEW and DESIGN. Reads/writes **`engagement-passport.yaml`** in the prospect folder.

## Required skills (invoke — do not reimplement)

| Layer | Skills |
|---|---|
| Consult build | `consult-frame`, `consult-arc`, `consult-gates`, `consult-acceptance`, `consult-commercial` |
| Consult quality | `consult-integrity`, `consult-consistency-lint`, `consult-red-team` |
| Consult ship | `consult-package`, `consult-pursue` |
| Timeln (every stage — see table below) | `timeln-find`, `timeln-decided`, `timeln-shipped`, `timeln-warned`, `timeln-quickly`, `timeln-plan` |
| Architecture | `arch-diagrams` (external) |

## Prospect folder layout

**Cold-start pursue** (`/cos-pursue` with client + topic only): all files flat under `prospects/{slug}/` — see `../consult-pursue/cold-start/EXAMPLES.md`.

**Full pipeline** (`/cos-plan`): nested under `Output/{Client}-Engagement/`:

```
prospects/{slug}/
├── engagement-passport.yaml
├── Input/                    # transcripts, RFPs, briefs
└── Output/
    └── {Client}-Engagement/
        ├── 00-research.md
        ├── 01-frame.md
        ├── 02-arc.md
        ├── 03-gates.md
        ├── 04-acceptance.md
        ├── 05-commercial.md
        ├── integrity-3.5.md
        ├── integrity-5.5.md
        ├── lint-report.md
        ├── red-team-report.md
        ├── {Client}-Engagement-Proposal-Pack.md
        ├── pursue/           # email, call script
        └── Framework-Variants/
```

Copy skeleton from `prospect-template/`.

## Engagement passport

Read at stage start; update `stage`, `artifacts`, `checkpoints`, `revision_loop`, `timeln_pulls` at stage end.

Env: `COS_PASSPORT_RESET=1` — ignore existing passport; start at CAPTURE.

Resume: read `stage` field; run from that stage forward unless user says restart.

## Timeln at every stage

Run the listed Timeln skill(s) **before** the consult skill for that stage. If MCP unavailable, note `timeln skipped — no MCP` in stage output and continue with source docs only — never fabricate Timeln results.

| Stage | Timeln skill(s) | Query / purpose |
|---|---|---|
| **0 CAPTURE** | `timeln-plan` | Optional: if user asks "what pursuits this week?", run cascade first; else skip |
| **1 RESEARCH** | `timeln-find` | Open synthesis: domain, client industry, analogous engagements |
| | `timeln-decided` | Settled calls on stack, delivery model, pricing patterns for this domain |
| **2 FRAME** | `timeln-find` | Stakeholder / industry context not in transcript |
| | `timeln-quickly` | Verbatim client quotes on decision, scope, constraints (Fact + Quote modes) |
| **3 DESIGN — arc** | `timeln-shipped` | Proof points for target capability and options |
| | `timeln-warned` | Past failures on proposed technical path |
| **3 DESIGN — gates** | `timeln-decided` | Prior phasing / gate patterns for similar engagements |
| **3 DESIGN — acceptance** | `timeln-warned` | Fold real past failures into fallback rows (per consult-acceptance) |
| **3 DESIGN — commercial** | `timeln-decided` | Precedent duration, access assumptions |
| | `timeln-shipped` | Precedent team shape / delivery evidence |
| **3.5 INTEGRITY** | `timeln-quickly` | Verify quoted client language against Timeln + source transcript |
| | `timeln-shipped` | Verify any "we've done X" claims in arc/commercial |
| **4 ARCHITECT** | `timeln-warned` | Gut-check architecture choices against past incidents |
| | `timeln-decided` | Prior ADRs on platforms, patterns named in diagram |
| **5 BUILD** | `timeln-shipped` | Credibility bullets for framework variants |
| | `timeln-find` | Analogous proposal structures / win themes from memory |
| **5.5 REVIEW** | `timeln-warned` | Feed real scars into `consult-red-team` Devil's Advocate |
| **6 PACKAGE** | `timeln-quickly` | Optional: verbatim quotes for Q&A appendix when user asks |
| **7 PURSUE** | `timeln-shipped` | Proof points for pitch email and call script |
| | `timeln-quickly` | Numbers, dates, names client mentioned |
| **8 DELIVER** | `timeln-quickly` | Mid-engagement recall (user invokes ad hoc) |
| | `timeln-decided` | Recall settled engagement decisions without relitigating |
| **9 CLOSE** | `timeln-find` | Capture learnings; suggest ingest titles for Timeln |
| **10 SUMMARY** | `timeln-plan` | Optional: feed closed pursuit into next week's cascade |

**Weekly (parallel, not a pipeline stage):** cron `timeln-plan` — ranks which prospects get pipeline time.

## Stage workflow

### 0 — CAPTURE

1. Create `prospects/{slug}/` from template if missing.
2. Initialize `engagement-passport.yaml` (`stage: CAPTURE`).
3. Place input in `Input/` (transcript, RFP, brief).
4. **Checkpoint:** "Is this a real pursuit worth framing?" → user yes/no.

### 1 — RESEARCH

1. **`timeln-find`** — domain + analog synthesis → section in `00-research.md`.
2. **`timeln-decided`** — prior decisions on domain → same file under `## Prior decisions`.
3. Write `00-research.md`; update passport `timeln_pulls`.
4. **Checkpoint:** "Enough context to frame?"

### 2 — FRAME

1. **`timeln-find`** — stakeholder/industry context.
2. **`timeln-quickly`** — client quotes on decision and scope.
3. Run **`consult-frame`** using Input + research + Timeln sections → `01-frame.md`.
4. **Checkpoint:** User approves frame card → set `checkpoints.frame_approved`.

### 3 — DESIGN

Run in order; each step reads prior artifacts + relevant Timeln output:

1. **Arc** — `timeln-shipped`, `timeln-warned` → **`consult-arc`** → `02-arc.md`
2. **Gates** — `timeln-decided` → **`consult-gates`** → `03-gates.md`
3. **Acceptance** — `timeln-warned` → **`consult-acceptance`** → `04-acceptance.md`
4. **Commercial** — `timeln-decided`, `timeln-shipped` → **`consult-commercial`** → `05-commercial.md`
5. **Checkpoint:** User picks option (MVP / Pilot / Full / custom) → `option_selected`.

### 3.5 — INTEGRITY (pre-architecture)

1. **`timeln-quickly`** + **`timeln-shipped`** — prefetch for gate.
2. Run **`consult-integrity`** gate `3.5` → `integrity-3.5.md`.
3. **BLOCK** if verdict FAIL — return to DESIGN.
4. **Checkpoint:** User acknowledges open items.

### 4 — ARCHITECT

1. **`timeln-warned`**, **`timeln-decided`** on components in scope.
2. Run **`arch-diagrams`** → layered, sequence, deployment artifacts in Output folder.
3. **Checkpoint:** "Diagram matches approved scope?"

### 5 — BUILD

1. **`timeln-shipped`**, **`timeln-find`** for variant credibility.
2. Generate framework variants per `../consult-arc/FRAMEWORK-VARIANTS.md`.
3. **Checkpoint:** User picks variant or merge map → record in passport.

### 5.5 — REVIEW

1. **`timeln-warned`** — scars for red team.
2. **`consult-consistency-lint`** → `lint-report.md`
3. **`consult-red-team`** → `red-team-report.md`
4. If critical findings or red-team BLOCK: increment `revision_loop` (max 2) → back to DESIGN or BUILD.
5. **Checkpoint:** Ship pack? yes/no

### 6 — PACKAGE

1. Optional **`timeln-quickly`** for appendix quotes.
2. **`consult-package`** → `{Client}-Engagement-Proposal-Pack.md`
3. **Checkpoint:** Final ship approval → `checkpoints.ship_approved`

### 7 — PURSUE

**Standard** (pack exists):

1. **`timeln-shipped`**, **`timeln-quickly`**
2. **`consult-pursue`** → `pursue/email.md`, `pursue/call-script.md`
3. **Checkpoint:** Send to client?

**Cold-start** (user gives client + topic only — no pack, no Input brief):

1. Infer slug; create `prospects/{slug}/` if missing.
2. Web research → `prospects/{slug}/00-research-public.md`.
3. Synthesize pack at `prospects/{slug}/{Client}-Engagement-Proposal-Pack.md` from `../consult-pursue/cold-start/` — label `(synthesized)`.
4. Passport: `stage: PURSUE`, `option_selected: POC`, `source_mode: cold_start`.
5. **`timeln-shipped`**, **`timeln-quickly`** → **`consult-pursue`**.
6. **Checkpoint:** Send to client? Upgrade to full pipeline when brief arrives (`/cos-research`).

See **`/cos-pursue`** and **`../consult-pursue/cold-start/EXAMPLES.md`**.  
Showcases: **`../consult-pursue/examples/ho-brothers/`** · **`../consult-pursue/examples/vodafone-portugal/`** (single-folder cold-start).

### 8 — DELIVER

Live engagement — not automated. User invokes **`timeln-quickly`** / **`timeln-decided`** ad hoc during delivery. Track gate sign-offs against `03-gates.md` / `04-acceptance.md`.

### 9 — CLOSE

1. **`timeln-find`** — synthesize learnings.
2. Write `09-close.md`; suggest Timeln ingest (transcript, decision, retro).
3. Update passport `stage: CLOSE`.

### 10 — SUMMARY

Write `10-process-summary.md`: stages completed, revision loops, Timeln pulls used, time estimate, open items.

Optional **`timeln-plan`** to reprioritize next pursuits.

**Post-win expansion (not a pipeline stage):** once a deal is won, run **`/cos-market`** (`consult-market`) to find the next 5 lookalike accounts in the same industry + size for the same use case. Standalone, manual-seed — does not read the passport.

## Output — process summary shape

```
## Pipeline summary -- {client} -- {YYYY-MM-DD}

**Stage reached:** ...
**Revision loops:** n/2
**Option selected:** ...

**Timeln skills invoked**
| Stage | Skill | Outcome |
|---|---|---|
| 1 | timeln-find | ... |
| ... | ... | ... |

**Artifacts**
- ...

**Open items**
- ...

**Next command:** /cos-resume | /cos-pursue | timeln-plan
```

## Rules

- Never duplicate Timeln MCP calls inline — always invoke the timeln-* skill workflow.
- If a Timeln skill returns `no record`, pass that through; do not invent memory.
- Do not skip integrity 3.5 before ARCHITECT or 5.5 before PACKAGE.
- One primary decision thread from frame through pack — lint enforces.
- Max 2 revision loops; then escalate to user with explicit tradeoff list.

## Commands

`/cos-plan` starts at 0; `/cos-resume` reads passport. (Slash commands in `.claude-plugin/commands/`.)

## Pairing

| Skill | Pipeline role |
|---|---|
| timeln-plan | Weekly prioritization + optional post-close |
| timeln-find | Research, build, close synthesis |
| timeln-decided | Research, gates, commercial, architect, deliver |
| timeln-shipped | Arc, commercial, integrity, build, pursue |
| timeln-warned | Arc, acceptance, architect, review |
| timeln-quickly | Frame, integrity, package, pursue, deliver |
| consult-market | Post-win: top-5 lookalike target list (standalone) |
