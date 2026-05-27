## Call script — Ho Brothers — 2026-05-22

**Attendees:** Ho Brothers — CustomHub product/ops lead (TBD), head of manufacturing or CAD ops (TBD), account management lead (TBD) · Neurons Lab — Rahul Kumar  
**Goal:** Confirm Option B (8-week CustomHub Agentic POC), workflow priority, and path to access workshop + SOW.

---

### Opening (2 min)

Thanks for the time. We’ve been following Ho Brothers’ **CustomHub** story — 400+ retailers, standardized QC, 24–48 hour CAD turnaround — and we’re here to discuss the **next phase: agentic workflows on your existing portal**, not another greenfield CAD tool. Retailers are seeing AI-native design platforms; your moat is production + systems — this POC makes CustomHub feel agentic without ripping out what works.

---

### Decision recap (5 min)

**Primary decision:** Extend CustomHub from tracking and communication to **agentic job orchestration** on 2 high-volume paths, with measurable reduction in account-manager touches and faster structured intake.

**Where you are (public):**
- **CustomHub™** — job comms, real-time tracking, 3D renders, BI, white-label option ([hobrothers.com](https://hobrothers.com/home))
- **400+ retailers**, **100K+ CAD designs**, rush **7-day** / standard **15-day** production SLAs
- Global expansion — **Mumbai office operational** (Jan 2026)

**Where the gap is:** Portal tracks jobs well; **agentic** layer turns messy retailer email/sketch requests into structured briefs, automates revision ping-pong, and surfaces exceptions before account managers get pulled in.

**Our ask today:** Validate workflows, CustomHub sandbox access, and who signs eval + security gates.

---

### Recommendation (10 min)

**Option B — 8-week CustomHub Agentic Workflow POC** (recommended)

| Week | Focus |
|---|---|
| 1–2 | Workflow selection, golden intake samples, CustomHub API/event map |
| 3–5 | Orchestrator + 2 workflow agents; RAG on SOPs/pricing rules |
| 6–7 | Eval harness (human + LLM-as-judge); human-in-loop on quotes/approvals |
| 8 | Readout: structured-intake rate, AM touch reduction, white-label roadmap |

**Journey candidates:**
1. **Retailer intake → structured job brief** — email/sketch/notes → CustomHub-ready spec + CAD brief for designer queue  
2. **Status & exception handling** — “where is my job?”, rush risk, approval bottlenecks, stone/material flags  

**Architecture posture:** Sidecar orchestration via CustomHub APIs/events; no CustomHub replacement; design IP stays in Ho Brothers environment; audit trail for every agent action; human approval on all pricing.

**Proof we’ve done this:**
- Ukreximbank — delivered multi-agent support on knowledge graph  
- Solar Manager — production support assistant on AWS  
- AEON CCI — 750K+ monthly omni-channel interactions (workflow + handoff patterns)

---

### Risks & assumptions (5 min)

| Risk | Mitigation |
|---|---|
| CustomHub API access slow | Stub webhooks + recorded job transcripts weeks 1–4; swap live staging week 5 |
| Pricing automation too sensitive | Agent **drafts only**; AM approval gate on all quotes |
| Scope creep into AI CAD generation | Out of scope — Matrix/Rhino pipeline unchanged; POC is workflow only |
| Retailer white-label expectations | Option C adds white-label pilot after Option B proves evals |

**Assumptions to confirm:** English primary; AMs remain escalation path; security review in parallel; CustomHub stays primary retailer UI.

---

### Close (5 min)

**Ask:**  
1. Name **gate owner** for POC sign-off (ops + CustomHub product).  
2. Confirm **workflow #1** (intake vs status/exceptions).  
3. Schedule **½-day CustomHub access workshop** within 10 business days.  
4. NDA if not already in place — SOW draft within 2 weeks of workshop.

---

### Q&A stubs

| Question | Response | Source |
|---|---|---|
| “We already have CustomHub — why do we need you?” | CustomHub excels at **tracking and visibility**; agentic POC adds **structured intake, revision automation, and exception surfacing** — complementary layer, not replacement. | Pack §Frame; [hobrothers.com](https://hobrothers.com/home) |
| “Shouldn’t we just buy Diatech / BLNG / Tashvi?” | Those tools target **design generation**; Ho Brothers’ edge is **production + SEC systems**. POC automates **job lifecycle on CustomHub**, not sketch-to-CAD greenfield. | Pack §Out of scope; public AI jewelry market |
| “What metrics should we expect?” | Target **≥60% auto-structured intake** in sandbox and **≥50% fewer AM touches** on status queries; production targets set after golden-set baseline week 2. | Pack §Definition of good |
| “Our retailers trust account managers — will AI erode that?” | AMs stay on **quotes, approvals, and exceptions**; agent handles repetitive status and intake structuring; white-label co-pilot is optional Option C. | Pack §Assumptions |
| “IP / design confidentiality?” | Sidecar in Ho Brothers environment; no training on retailer CAD IP; audit log per action; aligns with your public stance that customer designs are their IP. | Pack §Assumptions; [Capabilities](https://hobrothers.com/capabilities) |

---

### Objection stubs (internal prep)

| Objection | Response | Proof |
|---|---|---|
| “Build vs buy — we can add AI to CustomHub ourselves.” | You know the domain; we bring **agent eval discipline, orchestration patterns, and faster time-to-sandbox** — POC proves ROI before permanent headcount. | Pack §Options |
| “8 weeks is too fast.” | Option A (3-week discovery) available; Option B is fixed 2 workflows only. | Pack §Options |
| “Prove you’ve shipped, not just proposed.” | Ukreximbank delivered; Solar Manager production case study. | timeln-shipped |
| “We’re scaling Mumbai — wrong time.” | Agentic intake/exceptions **reduce AM load per retailer** — supports scale without linear headcount. | Public Mumbai expansion; Pack §Why now |
| “AI will quote wrong metal/stone prices.” | Human approval gate on all pricing in POC; agent drafts from approved rules only. | Pack §Risks fallback |
