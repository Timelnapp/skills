# Timeln Skills

Agent skills that ground your AI in your real memory — not its training data.

When the agent needs something specific from your history (a past decision, a quote from a call, what you've actually shipped), it reaches into your Timeln second brain through a hosted MCP server. Every answer cites a source. If memory has nothing, the skill says so plainly — never invents.

## Quickstart

```bash
npx skills@latest add timelnapp/skills
```

Then connect the hosted MCP — once per agent:

1. **[timeln.app/signup](https://timeln.app/signup)** — free, Google SSO.
2. **Settings → API Tokens → Create**. Copy the `tln_...` token.
3. Add to your agent's MCP config (`~/.claude.json`, `~/.cursor/mcp.json`, etc.):

   ```json
   {
     "mcpServers": {
       "timeln": {
         "url": "https://timeln-mcp-production.up.railway.app/mcp",
         "headers": { "Authorization": "Bearer tln_YOUR_TOKEN_HERE" }
       }
     }
   }
   ```

4. Restart your agent. `/mcp` should list `timeln`.

No Python, no local daemon — the MCP is hosted.

## Why these skills exist

Two problems, two skill packs.

### Memory — the agent fabricates instead of recalling

Agents asked to "recall" usually pattern-match training data, then dress it up as your history. The fix is a real lookup against your second brain, with hard rules against fabrication: every claim cites a Timeln doc, and "no record" is treated as the correct answer when memory is empty.

That's **[thinking-os](./skills/thinking-os/)**: six recall skills that each own a specific moment (mid-call, mid-pitch, Monday planning) and one output shape. Plus a local TTS engine to narrate what you find.

### Consulting work — the agent skips the gates

Pursuing engagements is a multi-stage process with mandatory human checkpoints. Off-the-shelf agents skip the gates: they jump from a transcript straight to a "proposal" without a frame, without integrity checks, without a red-team pass.

That's **[consulting-os](./skills/consulting-os/)**: a solo-founder pursuit pipeline (capture → frame → design → architect → build → review → ship → pursue) with checkpoints at every stage. Memory skills from thinking-os run at every stage — no duplicate memory layer.

## Reference

### thinking-os

Memory & recall, grounded in Timeln MCP.

- **[timeln-find](./skills/thinking-os/timeln-find/SKILL.md)** — Open-ended search and synthesis over your memory. MECE gap analysis, PARA framework, optional D3 knowledge graph.
- **[timeln-plan](./skills/thinking-os/timeln-plan/SKILL.md)** — Convert recent saves into a ranked action plan via a 6-framework cascade (PARA → MECE → RICE → Eisenhower → GTD → 4DX). HTML pipeline output.
- **[timeln-quickly](./skills/thinking-os/timeln-quickly/SKILL.md)** — One-breath mid-call recall. One sentence or one verbatim quote, one citation, under a second.
- **[timeln-shipped](./skills/thinking-os/timeln-shipped/SKILL.md)** — Proof of actually-shipped work with artifact pointers ready to paste mid-pitch.
- **[timeln-decided](./skills/thinking-os/timeln-decided/SKILL.md)** — Past decisions with stated rationale and rejected alternatives. Stops agents from relitigating settled calls.
- **[timeln-warned](./skills/thinking-os/timeln-warned/SKILL.md)** — Past failures, retros, post-mortems. Your actual scars, not "common pitfalls."
- **[timeln-podcast](./skills/thinking-os/timeln-podcast/SKILL.md)** — Generate podcast-quality narration from any text using local Kokoro TTS. Runs entirely offline.

### consulting-os

Solo-founder consulting pursuit pipeline, with human-in-the-loop gates.

- **[consult-pipeline](./skills/consulting-os/consult-pipeline/SKILL.md)** — Orchestrates the full workflow (CAPTURE → SUMMARY) with mandatory checkpoints. Owns the prospect template and engagement passport schema.
- **[consult-frame](./skills/consulting-os/consult-frame/SKILL.md)** — Brief or transcript → structured engagement frame: decision, definition of good, scope, stakeholders.
- **[consult-arc](./skills/consulting-os/consult-arc/SKILL.md)** — Solution arc (3-option spread). Owns the framework-variants rubric used by build + red-team.
- **[consult-gates](./skills/consulting-os/consult-gates/SKILL.md)** — Phasing and stage gates with exit criteria.
- **[consult-acceptance](./skills/consulting-os/consult-acceptance/SKILL.md)** — Acceptance matrix with fallback rows fed by `timeln-warned`.
- **[consult-commercial](./skills/consulting-os/consult-commercial/SKILL.md)** — Commercial section: duration, team shape, fees, access assumptions.
- **[consult-package](./skills/consulting-os/consult-package/SKILL.md)** — Assemble the client-ready proposal pack.
- **[consult-integrity](./skills/consulting-os/consult-integrity/SKILL.md)** — Gate 3.5 / 5.5 integrity check: citations, proof, scope lock, option drift, fabrication.
- **[consult-consistency-lint](./skills/consulting-os/consult-consistency-lint/SKILL.md)** — Cross-artifact lint (frame ↔ arc ↔ acceptance ↔ commercial).
- **[consult-red-team](./skills/consulting-os/consult-red-team/SKILL.md)** — Multi-perspective stress test (exec, procurement, technical skeptic, devil's advocate).
- **[consult-pursue](./skills/consulting-os/consult-pursue/SKILL.md)** — Post-pack pursuit: cover email + call script. Cold-start mode synthesises a pack from client + topic alone.

Slash commands: `/cos-plan`, `/cos-research`, `/cos-frame`, `/cos-design`, `/cos-integrity`, `/cos-architect`, `/cos-variants`, `/cos-lint`, `/cos-ship`, `/cos-pursue`, `/cos-resume` — defined in [`.claude-plugin/commands/`](.claude-plugin/commands/).

## Installation per agent

`npx skills@latest add timelnapp/skills` works for Claude Code, Cursor, Codex CLI, OpenCode, and GitHub Copilot CLI. Skills are auto-discovered from each agent's skills directory.

- **Claude Code**: `/plugin install timeln-skills@timeln-skills`
- **Cursor**: `/add-plugin timeln-skills` in agent chat
- **Gemini CLI**: `gemini extensions install https://github.com/Timelnapp/skills`
- **Codex App**: Plugins sidebar → Productivity → Timeln Skills → +
- **OpenCode**: see [.opencode/INSTALL.md](.opencode/INSTALL.md)

If you use more than one agent, install separately for each.

## License

MIT — see [LICENSE](LICENSE).
