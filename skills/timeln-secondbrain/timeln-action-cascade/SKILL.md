---
name: timeln-action-cascade
description: "Take a window of recently-saved Timeln documents and run them through a 6-framework cascade (PARA → MECE → RICE → Eisenhower → GTD → 4DX) to produce a prioritized action plan. Output is a single HTML file styled as a vertical pipeline — each framework shows what came in, the decision rule, what passed forward, and what was dropped, with connector pills between stages showing volume of handoff. Use this skill whenever Rahul says 'cascade my last X days', 'prioritize my recent Timeln saves', 'what should I do with my last week/month of saves', 'turn my saves into actions', 'run the framework cascade on my saves', 'eisenhower my saves', or any variation involving filtering recent Timeln captures into a single ranked plan with a WIG and next actions. Always queries Timeln MCP for the source data, applies LLM judgment for RICE scoring and MECE clustering, and produces a downloadable file in /mnt/user-data/outputs/."
---

# Timeln action cascade

Take N days of Timeln saves. Filter out the noise. Produce one ranked action plan.

## Context — what this skill produces

The output is a **vertical pipeline visualization** with 6 stages stacked top-to-bottom. **This specific format is the deliverable** — it is the result of multiple iterations and is the format Rahul wants:

- Each stage is a card with a left-border accent — teal for organise (PARA, MECE), amber for prioritise (RICE, Eisenhower), purple for execute (GTD, 4DX)
- Each card has 4 sections: header (framework + count in), Input (chips with what came in), Decision rule (the actual rule in prose), Pass through (what survived — chips, table, or rows depending on stage)
- Between stages: a connector pill showing volume + nature of handoff (e.g. "151 saves → 136 meaningful items pass forward")
- Items dropped at each stage are explicitly shown as struck-through chips — the filtering must be visible

**Do NOT produce alternative formats** — no kanban boards, no flowcharts, no clickable widgets. The pipeline file is the artifact. If Rahul wants a different visualization later, that's a separate request. The reason this matters: previous iterations included a kanban board and a simple cascade flowchart, but the pipeline-with-data-flow format won.

## Outcome

A single file (HTML by default, MD if requested) saved to `/mnt/user-data/outputs/cascade-{YYYYMMDD}-{days_back}d.html`. The file walks through:

1. **PARA** — sort 100% of saves into Projects / Areas / Resources / Archive
2. **MECE** — collapse topic tags into 4 non-overlapping clusters
3. **RICE** — crystallise one bet per cluster, score on Reach × Impact × Confidence ÷ Effort
4. **Eisenhower** — drop ranked bets + commitments into Q1 / Q2 / Q3 / Q4
5. **GTD** — convert every Q1 + Q2 item into a `verb + object + where` next action
6. **4DX** — define one WIG, two lead measures, one weekly cadence

## Required systems

- **Timeln MCP** must be connected in the host environment (Cursor, Claude Desktop, Claude Code). It exposes tools to query Rahul's saved documents.
- Tool names may evolve — discover them at runtime via `tool_search`. Do NOT hardcode tool names.

## When the user invokes this

Inputs to extract from the request:

| Parameter | Default | Notes |
|-----------|---------|-------|
| `days_back` | 30 | E.g. "last 7 days" → 7, "last month" → 30, "last quarter" → 90 |
| `account_email` | none | If user mentions a specific email, filter; otherwise pull what the MCP returns |
| `output_format` | `html` | Use `md` only if the user explicitly says markdown |

If the user is ambiguous on the window, ask once: "How many days back should I pull?" — don't assume.

## Workflow

### 1) Discover Timeln MCP tools

Call `tool_search` with multiple queries — Timeln MCP tool names aren't fixed:
- `timeln search documents`
- `timeln recent saves`
- `timeln list documents`
- `memory knowledge graph search`
- `second brain saves`

Look for tools whose names or descriptions match these capabilities:
- **Search / query** — natural language query into the saved corpus
- **List recent** — time-windowed listing of saves
- **Get topics** — topic/tag aggregation
- **Get document** — fetch a specific save

**Read the schema** of any tool you find before calling. Do NOT guess parameter names. The MCP may expose `query`, `q`, `search_text`, `text` — they're not interchangeable.

If multiple candidate tools exist, prefer the one that:
- Returns at least `id`, `title`, `summary`, `topics`, `created_at` per document
- Supports a date range filter or returns the date so you can filter client-side
- Returns ≥ 100 results per call (or supports pagination)

If no Timeln MCP tools are discoverable, stop and tell the user: *"I can't find Timeln MCP tools in this session. Make sure Timeln MCP is connected — Settings → API tokens → paste into MCP config → restart your agent."*

### 2) Pull the corpus

Call the discovered tool. Construct the query to get all saves within the window:

- If the tool supports date range: pass `from = today - days_back`, `to = today`
- If the tool only supports natural-language search: call with empty query or `*`, then filter by `created_at` client-side
- If the tool requires pagination: loop until you've got everything in the window
- If `account_email` is specified, filter

Required fields per save:
- `title`
- `summary` (or first ~200 chars of content)
- `topics` (array of tag strings)
- `created_at`
- `para_category` (if Timeln stores it; otherwise infer in stage 3)

If the corpus is empty or thin (< 5 items), stop and tell the user: *"Only N saves found in the last X days. Try a wider window?"*

### 3) Stage 1 — PARA · sort signal

If `para_category` is present in the data, count by it. If not, infer per save:

| Bucket | Inference logic |
|--------|----------------|
| Projects | Title implies a deliverable, ship date, or customer-facing output |
| Areas | Title implies an ongoing theme (e.g. "GTM strategy", "founder routine") |
| Resources | Reference material — papers, prompts, tools, documentation |
| Archive | Explicitly low-signal or off-mission |

**Decision rule to flag mislabelling:** If `Projects` is more than ~60% of the corpus AND many project-tagged titles look like passive reading (papers, articles, threads), surface this as a flag in the output: *"~30 passive reads mislabelled as Projects."* This is signal that the PARA tagging is being used loosely.

**Output of stage 1:** Counts by bucket, optional flag note, count of dropped (Archive) items.

### 4) Stage 2 — MECE · remove overlap

Extract topic tags from all saves. Aggregate frequencies. Group the top ~20 tags into **exactly 4** non-overlapping clusters using semantic similarity, not exact matching.

Standard cluster names for Rahul's domain (adapt if frequencies suggest different ones):

- **Builder Stack** — `claude code`, `ai agents`, `software development`, `developer tools`, `agentic systems`, `MCP`
- **Cognition & KM** — `knowledge management`, `second brain`, `obsidian`, `memory`, `note-taking`
- **Distribution** — `content marketing`, `LinkedIn`, `social media`, `digital marketing`, `content strategy`
- **Automation & Ops** — `automation`, `workflow optimization`, `marketing automation`, `ai automation`, `pipelines`

Saves spanning two clusters go to the dominant tag. Cross-cluster saves are signal that there's a bridge to build (e.g. distribution + builder = "ship a builder-themed post").

**Drop list at this stage:** topics that don't fit a cluster — usually noise (off-mission product saves, generic finance tweets, lyrics, skincare). Show explicitly as struck-through chips.

**Output of stage 2:** 4 cluster names with their tags and counts. A drop list with concrete examples.

### 5) Stage 3 — RICE · score & rank

For each of the 4 clusters, **crystallise one concrete bet** — a single action shippable in a sprint, not a vague theme.

If the corpus suggests a 5th high-leverage bet (e.g. content repurposing showing up across clusters), include it. Cap at 5.

Score each bet using **RICE = (R × I × C) ÷ E**:

- **Reach** (1–10): how many people / users / dollars are touched
- **Impact** (1–10): how much it moves Rahul's actual goal (Timeln pipeline, narrative, revenue)
- **Confidence** (0.3–1.0): probability this works as imagined
- **Effort** (1–10): size of the lift, higher = more work

**Show the working** — the output must display R, I, C, E numbers explicitly, not just the final score. Format: `8 × 8 × 0.8 ÷ 3 = 17.1`.

Rank descending by score.

**Output of stage 3:** Ranked table of 4–5 bets with all four input numbers visible + final score.

### 6) Stage 4 — Eisenhower · map urgency

Place ranked bets + any committed/calendar-locked items into 4 quadrants:

- **Q1 (urgent + important)** — deadline this week, customer demo, or top-RICE items that are also time-bound. Cap at 4.
- **Q2 (important, not urgent)** — rest of ranked bets + Q2 floats from PARA Areas. This is where most of the deep work lives. Cap at 8.
- **Q3 (urgent, not important)** — token cost sweeps, dashboard hygiene, duplicate productivity threads. Batch.
- **Q4 (neither)** — explicit archive items, off-mission saves, low-signal captures. Drop.

Numbered RICE rank stays visible on Q1/Q2 items.

**Output of stage 4:** 4 quadrants with item lists. Q3 + Q4 exit the system here — they don't pass to stage 5.

### 7) Stage 5 — GTD · next action

For each Q1 + Q2 item, write **exactly one** next physical action in `verb + object + where` format. If you can't write it that way, the item is still a project — break it down further until you can.

**Good examples:**
- "Open Timeln repo + MCP config, run smoketest, record pass/fail + screenshot in one doc"
- "Create `docs/mcp-tool-gating.md`, write: problem → user story → 3 acceptance criteria, stop at 1 page"
- "Clone Obscura repo, run hello-world fetch, write 5 bullets: fits Timeln agent use case? yes/no/why"

**Bad examples (reject and rewrite):**
- "Think about content strategy"
- "Improve LinkedIn presence"
- "Look into Obscura"

**Output of stage 5:** A numbered list of 8–11 next actions, each tagged Q1 or Q2.

### 8) Stage 6 — 4DX · stay accountable

Construct one WIG (Wildly Important Goal) that addresses the system bottleneck inferred from stages 2–4. Common bottleneck patterns:

- Heavy **Distribution** cluster but no measured loop → bottleneck is *distribution execution*
- Heavy **Builder Stack** cluster but no shipped proof → bottleneck is *product proof / demo*
- Heavy **Cognition & KM** with Timeln saves → bottleneck is *narrative or positioning*

Write the WIG as `From X to Y by [date]` — concrete metric + deadline. The deadline is end of the next calendar month relative to today.

Then 2 lead measures — predictive, daily/weekly, within Rahul's direct control. Examples:
- "3 ship touches per week (demo, post, or outbound)"
- "2 hours blocked before noon for WIG work — no new saves"

Then a cadence: "15 min weekly scoreboard — lag + both leads."

**Output of stage 6:** WIG + 2 lead measures + cadence.

## Generating the output file

### HTML (default)

Read `references/html-template.html`. Substitute these placeholders with computed data from stages 1–6:

- `{{WINDOW}}` — e.g. "Last 30 days · 2026-04-03 → 2026-05-03"
- `{{TOTAL_SAVES}}` — total document count
- `{{GENERATED_AT}}` — ISO timestamp
- `{{ACCOUNT}}` — account email or "all accounts"
- `{{PARA_TABLE_ROWS}}` — `<tr>` rows for stage 1 (bucket / count / treatment)
- `{{PARA_FLAGS}}` — optional callout if mislabelling detected (else empty string)
- `{{PARA_PASS_COUNT}}` — count of items passing to MECE
- `{{MECE_INPUT_CHIPS}}` — chips showing PARA buckets entering MECE
- `{{MECE_CLUSTERS}}` — 4 cluster blocks for stage 2 (use `<div class="cluster">` rows)
- `{{MECE_DROPPED}}` — chip list of dropped items (struck-through, `class="chip cdrop"`)
- `{{RICE_BET_COUNT}}` — number of bets scored (4–5)
- `{{RICE_INPUT_CHIPS}}` — chips for the 4–5 crystallised bets entering RICE
- `{{RICE_ROWS}}` — bet rows for stage 3 (use `<div class="rice-row">`)
- `{{EISEN_TOTAL}}` — total items entering Eisenhower
- `{{Q1_ITEMS}}`, `{{Q2_ITEMS}}`, `{{Q3_ITEMS}}`, `{{Q4_ITEMS}}` — chip HTML per quadrant
- `{{Q1_COUNT}}`, `{{Q2_COUNT}}`, `{{Q3_COUNT}}`, `{{Q4_COUNT}}` — counts
- `{{GTD_COUNT}}` — number of GTD next actions (8–11)
- `{{GTD_INPUT_CHIPS}}` — chips showing items entering GTD
- `{{GTD_ACTIONS}}` — `<div class="gtd-line">` blocks for each action
- `{{BOTTLENECK}}` — name of inferred bottleneck (e.g. "distribution execution")
- `{{TARGET_WINDOW}}` — e.g. "May 2026 window"
- `{{WIG_TEXT}}` — WIG one-liner
- `{{LEAD_1}}`, `{{LEAD_2}}` — lead measure lines
- `{{CADENCE}}` — cadence line

The template includes embedded CSS that adapts to light/dark mode via `@media (prefers-color-scheme)`. Do NOT modify the styling — only fill placeholders.

Save to `/mnt/user-data/outputs/cascade-{YYYYMMDD}-{days_back}d.html`.

### Markdown (alternative)

If user requests `md`, use `references/md-template.md` instead. Same placeholders, simpler structure.

Save to `/mnt/user-data/outputs/cascade-{YYYYMMDD}-{days_back}d.md`.

## After saving

Use `present_files` to surface the file. In the response, give a 3–5 line summary:
- Total saves processed
- Top RICE bet (winner with score)
- WIG one-liner
- "Open the file for the full cascade"

**Do NOT duplicate the entire file content in the chat response.** The file is the artifact. Keep the chat response under ~80 words.

## Data and safety rules

- Never fabricate counts, topic names, or save titles. Everything in the output must trace back to Timeln MCP results.
- If a stage has thin data (< 10 saves), still produce the output but flag the small sample explicitly: "Small sample — recalibrate next month."
- If RICE scoring feels arbitrary because the corpus is too narrow, write that note in the output near the RICE table.
- Do NOT invent commitments or deadlines. Q1 items are only "urgent" if the corpus or user input gives a real reason.
- If Timeln MCP returns multiple `email` accounts in the corpus, ask which one to focus on, or run all and segment.
- Do NOT build a kanban board, flowchart, or interactive widget. The cascade pipeline file is the only deliverable.

## QA checklist before presenting the file

- [ ] All 6 stages present, each with input / decision rule / pass-through / dropped sections
- [ ] PARA counts sum to the total saves
- [ ] MECE clusters cover all major topics (no top-frequency tag missing)
- [ ] RICE table shows R, I, C, E numbers explicitly (not just final scores)
- [ ] Eisenhower Q1 has ≤ 4 items, Q2 has ≤ 8 items
- [ ] GTD actions all in `verb + object + where` format — no vague "think about" or "improve"
- [ ] WIG has a concrete metric and a date
- [ ] Lead measures are weekly/daily and controllable, not outcome metrics
- [ ] Connector pills between stages show real volume numbers (e.g. "151 → 136")
- [ ] Dropped items are visible at every stage (struck-through chips)
- [ ] File saved to `/mnt/user-data/outputs/`
- [ ] `present_files` called

## Optional enhancements (only if user asks)

- Add a Theory of Constraints diagnosis paragraph between stages 4 and 5
- Add a "previous month comparison" if user provides last month's cascade file path
- Generate just the WIG section as a separate one-liner card for posting to LinkedIn
