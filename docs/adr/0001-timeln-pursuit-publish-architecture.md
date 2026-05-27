---
status: accepted
---

# Timeln Pursuit publish architecture

Consult skills ship as **Timeln Pursuit** inside `timelnapp/skills`, not as a clone-this-workspace template. The publishable unit is a **self-contained skill pack**: users install skills into any Cursor workspace via `npx skills add timelnapp/skills`. `consulting-os` remains a private dev workspace (real prospects, experiments); skills sync to `timelnapp/skills` by PR.

**Layout:** Consult skills live under `skills/consulting-os/consult-*/`; Timeln memory skills under `skills/thinking-os/timeln-*/`. Category folders follow the [mattpocock/skills](https://github.com/mattpocock/skills) shape: each skill is self-contained (SKILL.md + its own templates / references / scripts), each category has a README index.

**Orchestration:** `consult-pipeline` is the **fat skill** — embeds passport schema, folder conventions, cold-start templates, optional framework-variant rubric, and invoke cheat sheet. Other consult skills stay thin. Optional `docs/commands/` in the published repo documents slash-command parity; not a runtime dependency.

**Mandatory MCPs:** Timeln MCP and AWS Diagram MCP (`user-awslabs.aws-diagram-mcp-server`) are both required; skills fail fast if either is missing (no degraded "continue without MCP" mode in published skills).

**Diagrams:** New `consult-architect` replaces external `arch-diagrams`. Outputs: Mermaid sequence/logical flow (inline) + AWS reference PNG via Diagram MCP. PNG always uses AWS icons as logical stand-ins, captioned *"Reference topology — map to client cloud"* — even for GCP/Azure clients.

**Scope:** All 12 consult skills ship in v1. BUILD / framework variants is an optional pipeline stage (off unless requested). One sanitized cold-start example ships in `examples/consult-pursuit/`. No real client folders or `prospects/` content publishes.

**Considered options rejected:** Workspace template as product (b); self-contained without fat pipeline absorbing templates (ii→a hybrid); flat consult paths (namespace b won); Timeln-enhanced optional MCP (mandatory chosen); consult-architect folded into arc or pipeline only (d/b rejected); draw.io triple format (c rejected for b Mermaid+PNG); GCP-branching architect (c rejected for always reference PNG).

**Consequences:** Existing skill files must drop MCP-fallback language, external `shared/`/`commands/` references must move into `consult-pipeline` references, `consult-architect` must be authored, and AWS Diagram MCP must be documented in setup (currently errored/deprecated upstream — monitor migration to deploy-on-aws plugin).
