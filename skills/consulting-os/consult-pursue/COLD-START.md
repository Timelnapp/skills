# Cold-start pursue — how to use

Turn a **company + topic** into a pitch folder you can send — no transcript, no RFP required.

---

## One command

```text
/cos-pursue {client} for {topic}
```

**Examples**

```text
/cos-pursue https://hobrothers.com/home
/cos-pursue Ho Brothers for CustomHub agentic workflow
/cos-pursue vodafone portugal for agentic customer support
```

Paste a **website URL** or **company name**. Add `for {topic}` if the topic isn’t obvious from the site.

---

## What you need

| You provide | Notes |
|-------------|--------|
| Client | URL, company name, or existing folder under `prospects/` |
| Topic (optional) | What you’re pitching — e.g. “agentic workflow on their portal” |

You do **not** need a call transcript, brief, or existing proposal.

---

## What you get

Everything lands in **one folder**: `prospects/{slug}/`

```
prospects/ho-brothers/
├── engagement-passport.yaml          ← pipeline state (stage: PURSUE)
├── 00-research-public.md             ← public facts + sources
├── Ho-Brothers-Engagement-Proposal-Pack.md   ← exec summary + Option B POC
└── pursue/
    ├── email.md                      ← copy/paste outreach (≤250 words)
    └── call-script.md                ← 30-min call + objection stubs
```

Pack is labeled **(synthesized)** — built from public research, not client-validated facts.

---

## What to do next

1. **Open** `pursue/email.md` — review subject, body, proof lines.
2. **Attach** the proposal pack (+ research file if useful).
3. **Send** — update `engagement-passport.yaml` → `checkpoints.sent_to_client` when sent.
4. **Before the call** — skim `pursue/call-script.md` (opening, ask, Q&A stubs).

If proof lines say *assumption* or *public source*, treat them as research — not things the client told you.

---

## When a real brief arrives

Run **`/cos-research`** with transcript/RFP in `Input/`. That upgrades assumptions to client facts. Cold-start files can stay in the same folder.

Full proposal from scratch (no pursue shortcut): **`/cos-plan`** → drop brief in `Input/` → run stages through `/cos-ship`.

---

## Examples on disk

| Folder | Client |
|--------|--------|
| [`examples/ho-brothers/`](examples/ho-brothers/) | Custom jewelry manufacturer — CustomHub agentic workflow |
| [`examples/vodafone-portugal/`](examples/vodafone-portugal/) | Telco — agentic customer support POC |

Folder layout details: [`cold-start/EXAMPLES.md`](cold-start/EXAMPLES.md).

---

## Resume later

```text
/cos-resume prospects/ho-brothers
```

Reads `engagement-passport.yaml` and continues from the last stage.
