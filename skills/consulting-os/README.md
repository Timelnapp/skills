# Consulting OS

A human-in-the-loop copilot for solo-founder consulting pursuits. You decide at every gate; Timeln is the memory layer under every step. One win feeds the next five pursuits.

## Setup (3 steps)

1. **Install** — this repo loads as a skills source. Type `/cos` to confirm the commands appear.
2. **Connect Timeln** — add the Timeln MCP and authenticate, then ask *"call whoami on Timeln MCP."* (No Timeln? Skills still run on docs + web and mark memory `skipped`.)
3. **Optional** — connect Apollo/Clay for verified contacts in `/cos-market`.

Full details: **[docs/SETUP.md](./docs/SETUP.md)**.

---

## The consulting loop

One full cycle, command by command. The six Timeln skills (`find · decided · shipped · warned · quickly · plan`) run at every stage — there is no separate research step.

```
                      ╔═══════════════════════════════════════════════╗
                      ║              TIMELN — memory layer             ║
                      ║   find · decided · shipped · warned · quickly  ║
                      ╚═══════════════════════╤═══════════════════════╝
                                              │  feeds every stage below
        /cos-plan                            │
            │                                ▼
            ▼
   ┌─────────┐   ┌──────────┐   ┌────────┐   ┌────────┐   ┌───────────┐
   │ CAPTURE │──▶│ RESEARCH │──▶│ FRAME  │──▶│ DESIGN │──▶│ INTEGRITY │
   └─────────┘   └──────────┘   └────────┘   └────────┘   └─────┬─────┘
                                     ▲                     gate 3.5 │ (block if FAIL)
                                     │                              ▼
                                     │                        ┌───────────┐
                            revision loop (max 2)             │ ARCHITECT │
                                     │                        └─────┬─────┘
                                     │                              ▼
                   ┌────────┐   ┌────────┐                   ┌──────────┐
                   │ REVIEW │◀──│ BUILD  │◀──────────────────│ variants │
                   └───┬────┘   └────────┘                   └──────────┘
              gate 5.5 │
                       ▼
                  ┌─────────┐      ┌────────┐
                  │ PACKAGE │─────▶│ PURSUE │────▶ send to client
                  └─────────┘      └───┬────┘
                                       │
                                   WIN ▼
                  ┌────────┐      ┌─────────┐
                  │  CLOSE │◀─────│ DELIVER │
                  └───┬────┘      └─────────┘
                      │
              /cos-market  (post-win expansion)
                      ▼
            ┌───────────────────────────┐
            │  Top-5 lookalike targets   │
            │  same industry · size ·    │
            │  use case + contacts       │
            └─────────────┬──────────────┘
                          │  hand each target to /cos-pursue
                          └──────────────────────────────┐
                                                          │
            ◀── the loop closes: a win becomes 5 new pursuits ──┘
```

### Stage → command

| Stage | Command | Produces |
|---|---|---|
| Plan / capture | `/cos-plan` | Prospect folder + engagement passport |
| Research | `/cos-research` | `00-research.md` |
| Frame | `/cos-frame` | Engagement frame card |
| Design | `/cos-design` | Arc · gates · acceptance · commercial |
| Integrity 3.5 | `/cos-integrity` | Quote + proof gate (blocks if FAIL) |
| Architect | `/cos-architect` | Diagrams matched to scope |
| Build | `/cos-variants` | Framework variants |
| Review 5.5 | `/cos-lint` | Consistency lint + red team |
| Package | `/cos-ship` | Proposal pack |
| Pursue | `/cos-pursue` | Cover email + call script |
| **Expand (post-win)** | **`/cos-market`** | **Top-5 lookalike target list** |
| Resume anytime | `/cos-resume` | Picks up from the passport |

Cold-start (client + topic, no brief): `/cos-pursue {Client} for {topic}`.

## More

[SETUP](./docs/SETUP.md) · [ARCHITECTURE](./docs/ARCHITECTURE.md) · [POSITIONING](./docs/POSITIONING.md) · examples: [ho-brothers](./consult-pursue/examples/ho-brothers/) · [vodafone-portugal](./consult-pursue/examples/vodafone-portugal/)
