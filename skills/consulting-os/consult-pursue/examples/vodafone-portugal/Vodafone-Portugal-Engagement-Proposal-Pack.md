# Vodafone Portugal — agentic customer support — proposal pack (synthesized)

**Pack date:** 2026-05-22  
**Source:** Public research only — no client transcript or RFP on file. Mark assumptions explicitly.

---

## Executive summary — primary decision

**Primary decision:** Whether to extend Vodafone Portugal’s **SuperTOBi / TOBi** stack from GenAI Q&A into **agentic end-to-end customer support** on 2–3 priority journeys — with tool use against BSS/OSS, measurable containment and FTR, voice-channel parity, and an eval harness aligned to **SuperAgent**.

**Recommendation:** **Option B — 8-week Agentic Support POC** on **billing inquiry/resolution** and **appointment / retention** journeys (Portugal already proved appointment booking gains; billing is next per Vodafone public roadmap).

**Why now:** Portugal already moved FTR from 15% to 60% on appointments with SuperTOBi; group is investing in agentic AI (Google Concierge, Microsoft SuperAgent). POC de-risks the jump from “better answers” to “completed actions” before multi-market reuse.

---

## Frame

| Field | Content |
|---|---|
| **Definition of good** | ≥70% contained resolution on 2 pilot journeys in sandbox; p95 agent response <5s for tool-backed steps; eval rubric signed by CX + platform; handoff context preserved for SuperAgent |
| **In scope** | Agent orchestration layer; 2 journeys; RAG over approved knowledge; MCP/API adapters to agreed systems; golden-set evals; agent-assist handoff payload |
| **Out of scope** | Replacing SuperTOBi or Microsoft/Azure contract; full IVR/voice production cutover; net-new CRM/BSS procurement |
| **Assumptions** | Read-only/sandbox BSS access for POC; Portuguese + English; existing SuperTOBi channel remains primary UI; security review parallel |

---

## Options

| Option | Duration | Outcome |
|---|---|---|
| **A — Discovery only** | 3 weeks | Journey map, architecture, business case |
| **B — Agentic POC** ✓ | 8 weeks | 2 journeys live in sandbox + eval report + scale roadmap |
| **C — POC + voice pilot** | 12 weeks | Option B + limited voice intent slice |

**Selected:** **B — Agentic POC**

---

## Commercial (indicative)

- **POC:** 8 weeks, fixed fee TBD after access scoping workshop  
- **Team:** delivery lead, applied scientist, ML engineer, cloud engineer  
- **Path to kickoff:** NDA → ½-day access workshop → SOW within 2 weeks  

---

## Risks & assumptions

1. BSS/API access latency may slip POC — **fallback:** synthetic API + recorded journeys.  
2. Microsoft stack constraints on third-party agents — **fallback:** sidecar orchestration, no TOBi replacement.  
3. No named gate owner yet — **assumption:** Head of Digital CX or TOBi product owner (TBD).  

---

## Proof pointers (consult-pursue)

- Pack §Executive summary — primary decision  
- Pack §Options — Option B selected  
- Public: Vodafone SuperTOBi Portugal metrics (Jul 2024 release)  
