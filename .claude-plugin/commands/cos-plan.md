# /cos-plan — Start new pursuit (stage 0 CAPTURE)

Run **`consult-pipeline`** from stage **0 CAPTURE**.

## Do

1. Ask for client name + slug (or infer slug: lowercase-hyphenated).
2. Copy `skills/consulting-os/consult-pipeline/prospect-template/` → `prospects/{slug}/` (or legacy `prospect {name}/`).
3. Initialize `engagement-passport.yaml` — set `client`, `slug`, `stage: CAPTURE`.
4. Prompt user to drop transcript/brief in `Input/`.
5. Optional: if user asks what to work on this week, run **`timeln-plan`** first.
6. **Checkpoint:** "Is this a real pursuit?" → on yes, advance to RESEARCH and run stage 1.

**Shortcut:** If user has no brief yet but wants outreach now → **`/cos-pursue {client} for {topic}`** (cold-start; skips stages 1–6).

## Say

*"New pursuit folder at `prospects/{slug}/`. Add your transcript to `Input/`, then `/cos-research` or continue pipeline."*
