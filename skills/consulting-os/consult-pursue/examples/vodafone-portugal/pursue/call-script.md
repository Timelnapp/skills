## Call script — Vodafone Portugal — 2026-05-22

**Attendees:** Vodafone PT — Head of Customer Experience / Digital (TBD), TOBi or SuperTOBi product owner (TBD), IT/BSS platform rep (TBD) · Neurons Lab — Rahul Kumar  
**Goal:** Confirm Option B (8-week Agentic POC), journey priority, and path to access workshop + SOW.

---

### Opening (2 min)

Thanks for the time. We’ve been tracking Vodafone Portugal’s SuperTOBi rollout — strong appointment results — and we’re here to discuss the **next step: agentic resolution**, not another chatbot from scratch. We propose a bounded POC that sits alongside your Microsoft stack and feeds SuperAgent on handoff.

---

### Decision recap (5 min)

**Primary decision:** Extend SuperTOBi from better answers to **completed actions** on 2 journeys, with measurable containment and FTR.

**Where you are (public):**
- SuperTOBi live in PT; appointments FTR **15% → 60%**, NPS **64**
- Billing journeys rolling out
- SuperAgent for agent assist; group moving toward agentic AI (Google Concierge in other markets)

**Where the gap is:** GenAI assistants answer well; **agentic** support executes multi-step flows (check bill → explain → apply credit/adjustment → confirm) with governance and evals.

**Our ask today:** Validate journeys, sandbox access, and who signs eval + security gates.

---

### Recommendation (10 min)

**Option B — 8-week Agentic Support POC** (recommended)

| Week | Focus |
|---|---|
| 1–2 | Journey selection, golden questions, sandbox API map |
| 3–5 | Orchestrator + 2 journey agents, RAG on approved KB |
| 6–7 | Eval harness (human + LLM-as-judge), handoff payload for SuperAgent |
| 8 | Readout: containment, FTR, scale roadmap to voice |

**Journey candidates:**
1. **Billing** — aligns with Vodafone’s stated next rollout after appointments  
2. **Appointment / retention** — build on proven PT win; extend to plan-save flows  

**Architecture posture:** Sidecar orchestration (Agno/MCP-style); no TOBi replacement; EU data residency; audit trail for every tool call.

**Proof we’ve done this:**
- Solar Manager — production support assistant on AWS  
- AEON CCI — 750K+ monthly omni-channel interactions  
- CardX-scale voice-first design (50% automation target, copilot handoff) — adjacent telco-scale volume patterns  

---

### Risks & assumptions (5 min)

| Risk | Mitigation |
|---|---|
| BSS sandbox access slow | Start with synthetic API + recorded journeys; swap in live read-only week 4 |
| Microsoft stack constraints | Orchestration sidecar; integrate via approved APIs only |
| Journey scope creep | Fixed 2 journeys; change control after week 2 |

**Assumptions to confirm:** PT + EN; CX owner for eval rubric; security review in parallel; SuperTOBi remains primary customer UI.

---

### Close (5 min)

**Ask:**  
1. Name **gate owner** for POC sign-off (CX + platform).  
2. Confirm **journey #1** (billing vs retention).  
3. Schedule **½-day access workshop** within 10 business days.  
4. NDA if not already in place — we’ll send SOW draft within 2 weeks of workshop.

---

### Q&A stubs

| Question | Response | Source |
|---|---|---|
| “We already have SuperTOBi — why do we need you?” | SuperTOBi improved understanding and FTR on chat; agentic POC adds **tool execution, eval discipline, and journey completion** on BSS — complementary, not replacement. | Pack §Frame; Vodafone Jul 2024 release |
| “How is this different from Microsoft SuperAgent?” | SuperAgent **assists humans**; this POC **automates customer-side resolution** and passes structured context on escalation — designed to feed SuperAgent summaries. | Pack §Frame; Vodafone SuperAgent public description |
| “What containment should we expect?” | Target **≥70% sandbox containment** on 2 bounded journeys; production targets set after golden-set baseline in week 2. | Pack §Definition of good |
| “Voice is our biggest channel — chat POC feels narrow.” | Chat-first de-risks integrations; roadmap includes **Option C voice pilot** (+4 weeks) once BSS adapters proven. | Pack §Options |
| “Who else has done this at telecom scale?” | AEON CCI (750K+ monthly interactions, voice/chat/WhatsApp); CardX voice-first at hundreds of thousands of calls/month; Globe Telecom cited in our telecom portfolio. | timeln-shipped / use cases portfolio |

---

### Objection stubs (internal prep)

| Objection | Response | Proof |
|---|---|---|
| “Build vs buy — Microsoft/Google will ship this.” | Group partners give models and copilots; **journey orchestration, BSS adapters, and evals** are market-specific — POC proves PT-specific ROI before group template. | Pack §Risks |
| “Security / GDPR.” | EU residency, no training on customer data, tool-call audit log, human-in-loop on money-moving actions in POC. | Pack §Assumptions |
| “We don’t have API access.” | Week 1–2 uses synthetic + recorded paths; live read-only is stretch goal, not blocker. | Pack §Risks fallback |
| “8 weeks is too fast.” | Option A (3-week discovery) available; Option B is fixed scope, 2 journeys only. | Pack §Options |
| “Prove you’ve shipped, not just proposed.” | Solar Manager production case study; AEON CCI delivered omni-channel stack. | timeln-shipped URLs above |
