# Cold-start pursue — single-folder layout (examples)

**Rule:** All artifacts from `/cos-pursue` cold-start live in **one folder**: `prospects/{slug}/`.  
Do **not** nest under `Output/{Client}-Engagement/` until the engagement upgrades to the full pipeline.

---

## Correct — cold-start (use this)

### Example 1: Ho Brothers

```
prospects/ho-brothers/
├── README.md
├── engagement-passport.yaml
├── 00-research-public.md
├── Ho-Brothers-Engagement-Proposal-Pack.md
└── pursue/
    ├── email.md
    └── call-script.md
```

Showcase: [`../examples/ho-brothers/`](../examples/ho-brothers/)

Passport artifact paths (relative to slug root):

```yaml
artifacts:
  research: 00-research-public.md
  pack: Ho-Brothers-Engagement-Proposal-Pack.md
  pursue_email: pursue/email.md
  pursue_script: pursue/call-script.md
```

### Example 2: Vodafone Portugal

```
prospects/vodafone-portugal/
├── engagement-passport.yaml
├── Input/                                    # optional until brief arrives
├── 00-research-public.md
├── Vodafone-Portugal-Engagement-Proposal-Pack.md
└── pursue/
    ├── email.md
    └── call-script.md
```

Showcase: [`../examples/vodafone-portugal/`](../examples/vodafone-portugal/)

---

## Wrong — do not use for cold-start

```
prospects/ho-brothers/
├── engagement-passport.yaml
├── Input/README.md
└── Output/Ho-Brothers-Engagement/          ← extra nesting
    ├── 00-research-public.md
    ├── Ho-Brothers-Engagement-Proposal-Pack.md
    └── pursue/
        ├── email.md
        └── call-script.md
```

Why wrong: splits pursuit artifacts across `Input/`, slug root, and `Output/` — hard to zip, send, or resume.

---

## When to add `Output/`

Only after upgrading to the **full pipeline** (`/cos-plan`, `/cos-research`, stages 1–6). Then add:

```
prospects/{slug}/
├── … (existing cold-start files stay at slug root OR migrate once)
└── Output/{Client}-Engagement/
    ├── 01-frame.md
    ├── 02-arc.md
    └── …
```

Cold-start pursue files can stay at slug root alongside `Output/` — do not duplicate pack/research in both places.

---

## Passport paths by mode

| Mode | `research` | `pack` | `pursue_*` |
|------|------------|--------|------------|
| **Cold-start** | `00-research-public.md` | `{Client}-Engagement-Proposal-Pack.md` | `pursue/email.md` |
| **Full pipeline** | `Output/…/00-research.md` | `Output/…/{Client}-Engagement-Proposal-Pack.md` | `Output/…/pursue/email.md` |
