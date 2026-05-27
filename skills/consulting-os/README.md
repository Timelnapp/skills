# Consulting OS

Solo-founder consulting pursuit pipeline: **research → frame → design → architect → build → review → ship → pursue**. Human-in-the-loop at every gate. Timeln memory skills run at every stage — no duplicate memory layer.

## Skills

- **[consult-pipeline](./consult-pipeline/SKILL.md)** — Orchestrates the full pursuit workflow (CAPTURE → SUMMARY) with mandatory checkpoints. Owns `prospect-template/` and `engagement-passport.schema.json`.
- **[consult-frame](./consult-frame/SKILL.md)** — Turn a brief or transcript into a structured engagement frame: decision, definition of good, scope, stakeholders.
- **[consult-arc](./consult-arc/SKILL.md)** — Solution arc (3-option spread) for the engagement. Owns the `FRAMEWORK-VARIANTS.md` rubric used by build + red-team.
- **[consult-gates](./consult-gates/SKILL.md)** — Phasing and stage gates with exit criteria.
- **[consult-acceptance](./consult-acceptance/SKILL.md)** — Acceptance matrix with fallback rows fed by `timeln-warned`.
- **[consult-commercial](./consult-commercial/SKILL.md)** — Commercial section (duration, team shape, fees, access assumptions).
- **[consult-package](./consult-package/SKILL.md)** — Assemble the client-ready proposal pack.
- **[consult-integrity](./consult-integrity/SKILL.md)** — Gate 3.5 / 5.5 integrity check: citations, proof, scope lock, option drift, fabrication.
- **[consult-consistency-lint](./consult-consistency-lint/SKILL.md)** — Cross-artifact lint (frame ↔ arc ↔ acceptance ↔ commercial).
- **[consult-red-team](./consult-red-team/SKILL.md)** — Multi-perspective stress test (exec, procurement, technical skeptic, devil's advocate).
- **[consult-pursue](./consult-pursue/SKILL.md)** — Post-pack pursuit: cover email + call script. Cold-start mode synthesises a pack from client + topic alone. Owns `cold-start/` templates and `examples/`.

## Quick start

**Full pipeline** (transcript / brief on hand):

```text
/cos-plan                                # creates prospects/{slug}/
# drop transcript in Input/
/cos-research → /cos-frame → … → /cos-ship → /cos-pursue
```

**Cold-start pursue** (client + topic only — no brief):

```text
/cos-pursue {Client} for {topic}
```

How-to: [consult-pursue/COLD-START.md](./consult-pursue/COLD-START.md) · Examples: [ho-brothers](./consult-pursue/examples/ho-brothers/) · [vodafone-portugal](./consult-pursue/examples/vodafone-portugal/)

Resume any time: `/cos-resume prospects/{slug}`.

## Skill map (MECE)

Each type of work has exactly one owner skill. Pipeline orchestrates; it does not replace.

| Cluster | Work | Owner |
|---------|------|-------|
| Pipeline | End-to-end pursuit workflow | `consult-pipeline` |
| | Engagement state / resume | `engagement-passport.yaml` + `/cos-resume` |
| Build | Engagement frame | `consult-frame` |
| | Solution arc | `consult-arc` |
| | Stage gates | `consult-gates` |
| | Acceptance matrix | `consult-acceptance` |
| | Commercial section | `consult-commercial` |
| | Client-ready pack | `consult-package` |
| Quality | Cross-artifact consistency | `consult-consistency-lint` |
| | Integrity gate (quotes, proof, scope) | `consult-integrity` |
| | Multi-perspective stress test | `consult-red-team` |
| Pursuit | Pitch email + call script | `consult-pursue` |
| | Cold-start pursue (client + topic, no pack) | `consult-pursue` cold-start + `/cos-pursue` |
| | Architecture diagrams | `arch-diagrams` (external) |

### Timeln memory — invoked at every pipeline stage

| Work | Skill | Stages |
|------|-------|--------|
| Open synthesis, domain research | `timeln-find` | 1, 2, 5, 9 |
| Settled past decisions | `timeln-decided` | 1, 3, 4, 8 |
| Shipped work / proof | `timeln-shipped` | 3, 3.5, 5, 7 |
| Past failures / scars | `timeln-warned` | 3, 4, 5.5 |
| Mid-call one-breath recall | `timeln-quickly` | 2, 3.5, 6, 7, 8 |
| Weekly prioritization | `timeln-plan` | 0, 10, weekly |

**Rule:** Never add a `prospect-research` or duplicate Timeln skill — pipeline invokes the six timeln-* skills above.

## Overlap resolution

| User asks for… | Route to |
|----------------|----------|
| One artifact only ("just frame this") | Single `consult-*` skill |
| Full proposal from transcript | `consult-pipeline` or `/cos-plan` |
| Quick quote mid-call | `timeln-quickly` only |
| What pursuits this week | `timeln-plan` only |

## Docs

| Doc | What it covers |
|-----|----------------|
| [SETUP](./docs/SETUP.md) | Skills, Timeln MCP, prospect folders, weekly ops |
| [ARCHITECTURE](./docs/ARCHITECTURE.md) | Pipeline stages, skill clusters, integrity gates, layout |
| [POSITIONING](./docs/POSITIONING.md) | What Consulting OS is (and isn't), principles, license |

## Commands

Slash commands live at `.claude-plugin/commands/cos-*.md` (repo root): `/cos-plan`, `/cos-research`, `/cos-frame`, `/cos-design`, `/cos-integrity`, `/cos-architect`, `/cos-variants`, `/cos-lint`, `/cos-ship`, `/cos-pursue`, `/cos-resume`.

## Weekly

Run `timeln-plan` on Monday to rank which pursuits get pipeline time.
