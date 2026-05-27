# Consulting OS — Language

## Product

**Skill pack** — the publishable unit is installable agent skills, not a clone-this-whole-workspace template. Users add skills to any Cursor workspace.

**Self-contained skill** — a skill carries everything it needs to run (output shapes, folder conventions it creates, inline templates). It must not require `shared/`, `commands/`, or pre-existing `prospects/` scaffolding in the host workspace.

_Avoid:_ calling the repo a "workspace template" or assuming users clone consulting-os as their working directory.

## Pipeline

**Consult pipeline** — the orchestrator skill (`consult-pipeline`) that runs CAPTURE → SUMMARY. It is the **fat skill**: embeds passport schema, folder layout, cold-start templates, variant rubric, and full stage workflow inline. Other consult skills stay thin (inputs/outputs only).

**Engagement passport** — YAML state file (`engagement-passport.yaml`) tracking stage, artifacts, checkpoints. Schema lives inside `consult-pipeline` (not a separate repo file).

**Framework variants (BUILD)** — **optional** pipeline stage. Default run skips V1–V5 generation; user must explicitly request ("framework variants", "run BUILD", etc.). Rubric embedded in `consult-pipeline` references when invoked.

_Avoid:_ shipping `commands/` or `shared/` as install prerequisites for the published pack.

**Invoke cheat sheet** — Optional `docs/commands/` in **timelnapp/skills** (thin markdown, not runtime deps). `consult-pipeline` also embeds a `## How to invoke` table. consulting-os keeps local `/cos-*` for dev; published repo documents parity phrases for Cursor users.

## Consult build skills

**Consult architect** — new skill (`consult-architect`) at `skills/consult/pipeline/` sibling path `skills/consult/architect/`. Owns stage 4 diagram generation. Replaces external `arch-diagrams` in the published pack.

**Diagram backend** — `consult-architect` uses the **AWS Diagram MCP** (`user-awslabs.aws-diagram-mcp-server`: `generate_diagram`, `list_icons`, `get_diagram_examples`). Pattern follows `aws-architecture-diagram-mcp` skill (layered PNG, numbered clusters, Well-Architected defaults).

**Consult architect outputs** — **two formats per engagement**: (1) `2-sequence-diagram.md` with Mermaid (inline, no MCP); (2) AWS deployment PNG via MCP `generate_diagram`. No draw.io in the published skill.

**Reference architecture** — AWS-icon PNG is **always** produced, even when the client's cloud is GCP/Azure/on-prem. Icons are **logical stand-ins** (e.g. SageMaker → ML training). Every PNG is captioned: *"Reference topology — map to client cloud."*

_Avoid:_ skipping AWS PNG for non-AWS clients; avoid implying the client runs AWS when the frame says GCP.

**Consult arc** — narrative only (as-is → target → sequence). Does **not** produce diagrams; pairs with `consult-architect`.

_Avoid:_ calling `consult-arc` the diagram skill; avoid `arch-diagrams` as a publish dependency.

## Memory layer

**Timeln MCP** — **mandatory** for consult skills. Consult skills do not run without Timeln MCP configured. Published alongside the six `timeln-*` memory skills in `timelnapp/skills`.

**AWS Diagram MCP** — **mandatory** for the consult stack (same tier as Timeln). Full pipeline and `consult-architect` fail fast if `user-awslabs.aws-diagram-mcp-server` is not configured.

_Avoid:_ "Timeln-enhanced" or "continue without MCP" language in published consult skills.

## Repositories

**Consulting-os** — private **development workspace** only. Holds skill drafts, real `prospects/`, experiments, and grill artifacts. Not the public install target.

**Timelnapp/skills** — **publish target**. Skills are organised by category folder: `skills/consulting-os/` (build skills) and `skills/thinking-os/` (memory skills). Released via `npx skills add timelnapp/skills`.

**Timeln skill paths** — live under `skills/thinking-os/timeln-*/`. Consult skills live under `skills/consulting-os/consult-*/`. Category folders match the [mattpocock/skills](https://github.com/mattpocock/skills) shape.

_Avoid:_ publishing `prospects/`, client packs, or legacy `prospect ABC/` content to timelnapp/skills.

**Public examples** — One **sanitized cold-start fixture** in timelnapp/skills (e.g. `examples/consult-pursuit/vodafone-portugal/`) with `(synthesized)` labels. Demonstrates folder layout, pack, email, call script — no real client transcripts.

**Publish manifest** — **All 12 consult skills** ship in v1: pipeline, frame, arc, gates, acceptance, commercial, package, consistency-lint, integrity, red-team, pursue, architect (new). Plus six flat `timeln-*` skills unchanged.

**Timeln Pursuit** — Public brand for the consult skill line inside `timelnapp/skills`. README groups: **Memory** (`timeln-*`) | **Pursuit** (`consult-*`). Tagline: memory + pursuit pipeline for solo consultants.

**Maintenance** — You solo-maintain Pursuit skills. consulting-os is source of truth; changes sync to timelnapp/skills via PR (script TBD).

_Avoid:_ treating consult skills as a separate unrelated product with no Timeln connection in the published README.

**Consult namespace** — consult skills live under `skills/consult/{name}/` (e.g. `skills/consult/pipeline/SKILL.md`, `skills/consult/frame/SKILL.md`), not flat `skills/consult-pipeline/`.

**Consult skill slug** — frontmatter `name` stays prefixed: `consult-pipeline`, `consult-frame`, etc. Folder path is organizational only; triggers and docs unchanged.

_Avoid:_ renaming slugs to `pipeline` / `frame` when moving into the namespace.
