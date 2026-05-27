# Consulting OS — Architecture

Solo-founder pursuit pipeline modeled on [Academic Research Skills](https://github.com/Imbad0202/academic-research-skills): human-in-the-loop stages, integrity gates, revision caps, engagement passport.

## Four clusters

| Cluster | Skills |
|---------|--------|
| **Pipeline** | `consult-pipeline` |
| **Consult build** | frame → arc → gates → acceptance → commercial → package |
| **Consult quality** | integrity, consistency-lint, red-team |
| **Pursuit** | pursue |
| **Memory (Timeln)** | find, decided, shipped, warned, quickly, plan — **invoked at every stage** |

No duplicate Timeln wrapper skills. See the **Skill map** in [`../README.md`](../README.md).

## Pipeline

```
CAPTURE → RESEARCH → FRAME → DESIGN → INTEGRITY_3.5 → ARCHITECT → BUILD
→ REVIEW → PACKAGE → PURSUE → DELIVER → CLOSE → SUMMARY
```

Max **2 revision loops** between REVIEW and DESIGN/BUILD.

## Timeln integration matrix

| Stage | timeln-find | timeln-decided | timeln-shipped | timeln-warned | timeln-quickly | timeln-plan |
|-------|:-----------:|:--------------:|:--------------:|:-------------:|:--------------:|:-----------:|
| 0 CAPTURE | | | | | | optional |
| 1 RESEARCH | ✓ | ✓ | | | | |
| 2 FRAME | ✓ | | | | ✓ | |
| 3 DESIGN | | ✓ | ✓ | ✓ | | |
| 3.5 INTEGRITY | | | ✓ | | ✓ | |
| 4 ARCHITECT | | ✓ | | ✓ | | |
| 5 BUILD | ✓ | | ✓ | | | |
| 5.5 REVIEW | | | | ✓ | | |
| 6 PACKAGE | | | | | optional | |
| 7 PURSUE | | | ✓ | | ✓ | |
| 8 DELIVER | | ✓ | | | ✓ | |
| 9 CLOSE | ✓ | | | | | |
| 10 SUMMARY | | | | | | optional |
| Weekly | | | | | | ✓ |

## Engagement passport

YAML state file per prospect: `engagement-passport.yaml`. Schema: [`../consult-pipeline/engagement-passport.schema.json`](../consult-pipeline/engagement-passport.schema.json).

Resume: `/cos-resume`. Reset: `COS_PASSPORT_RESET=1`.

## Repo layout

```
skills/consulting-os/             # the skills (category folder)
├── README.md                     # category index + skill map
├── CONTEXT.md
├── consult-pipeline/             # owns prospect-template/, engagement-passport schema, passport-status.sh
├── consult-pursue/               # owns cold-start templates, examples/, cos-pursue-scaffold.sh
├── consult-arc/                  # owns FRAMEWORK-VARIANTS.md rubric
└── consult-* (frame, gates, acceptance, commercial, package, integrity, consistency-lint, red-team)

.claude-plugin/commands/          # /cos-* slash commands (Claude Code plugin convention)
docs/adr/                         # repo-root ADRs
prospects/{slug}/                 # user-runtime work (created by /cos-plan or /cos-pursue, not in the skills repo)
```

## Integrity gates

| Gate | When | Blocks |
|------|------|--------|
| 3.5 | After DESIGN | ARCHITECT |
| 5.5 | After BUILD/REVIEW | PACKAGE |

Seven modes: citation, proof, scope lock, option drift, metric fabrication, stakeholder invention, diagram orphan.

## External dependencies

- **Timeln MCP** — all six timeln-* skills
- **arch-diagrams** — stage 4
