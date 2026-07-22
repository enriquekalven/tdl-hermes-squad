# 📄 Product Requirements Document (PRD)
## Material Exception Resolution Agent MVP

**Author**: Tyler (Technical Deployment Lead, Google Cloud Delta /Forward)  
**Stakeholders**: Joint Project Steering Committee (Ford MP&L, Sourcing, Crisis Teams & Google Cloud PSO)  
**Version**: 1.0 (Frozen Scope)  
**Engagement Target**: 10-Week MVP Engineering Cycle  

---

## 1. Executive Summary & Problem Statement
Currently, Ford manages material supply chain exceptions—where supplier committed part supply falls short of Ford's 13-week rolling demand forecast—via a highly manual, reactive process across disparate spreadsheets. Calculating part run-out dates and assessing assembly line build schedules takes **4 to 6 weeks**, exposing Ford to high-stakes risks of assembly line shutdowns, elevated premium freight expenses, and lost vehicle revenue.

The **Material Exception Resolution Agent MVP** deploys an ADK-powered multi-agent system operating on a schema-validated synthetic data layer to compress the disruption-to-decision timeline from **4–6 weeks down to <5 minutes**.

---

## 2. Objectives & Key Results (OKRs)

### 🎯 Objective: Compress Disruption-to-Mitigation Decision Latency
* **KR 1 (Turnaround Speed)**: Compress disruption assessment turnaround from 4–6 weeks to **<5 minutes**.
* **KR 2 (Touch-Hour Reduction)**: Reduce analyst manual touch-hours per exception case from 45.0 hrs to **<0.5 hrs** (**88.89% reduction**).
* **KR 3 (ROI / Financial Protection)**: Enable optimal margin allocation prioritizing high-margin vehicle lines (F-150 over Maverick) to protect annual EBITDA.

---

## 3. Core System Scope (The 4-Stage Agentic Flow)

```
┌────────────────────────────────┐       ┌────────────────────────────────┐
│ STAGE 1: AUTOMATED IMPACT      │ ────► │ STAGE 2: PARALLEL ROOT CAUSE   │
│ Trace commit gaps to build plan│       │ Ingest alerts & generate RCA   │
└───────────────┬────────────────┘       └───────────────┬────────────────┘
                │                                        │
                ▼                                        ▼
┌────────────────────────────────┐       ┌────────────────────────────────┐
│ STAGE 3: CONCURRENT MITIGATION │ ────► │ STAGE 4: MARGIN ALLOCATION     │
│ Freight modes & supplier search│       │ Prioritize F-150 & shape demand│
└────────────────────────────────┘       └────────────────────────────────┘
```

1. **Stage 1: Automated Impact Assessment**: Automatically monitor Tier-1 commit gaps, trace shortages from deep-tier components up to active vehicle build plans, compile point-of-view (POV) risk reports, and generate outbound supplier surveys.
2. **Stage 2: Parallel Root Cause Analysis**: Ingest disruption alerts (fires, weather, transport disruptions) across unstructured streams and generate high-confidence evidence-based RCA reports.
3. **Stage 3: Concurrent Mitigation & Scenario Evaluation**: Simultaneously evaluate response options in parallel (Expedited Air Freight vs. Ground Truck, 4,000+ supplier search, engineering-cleared substitution parts).
4. **Stage 4: Margin-Optimized Recommendation & Demand Shaping**: Prioritize allocating constrained parts to keep high-margin vehicle lines running (F-150 over Maverick). Execute demand shaping for optional features (heated seat switch swaps). Log analyst decisions into hybrid precedence store (Cloud SQL + Vector Search).

---

## 4. In-Scope Features vs. Explicit Non-Goals

### ✅ In-Scope (Phase 1 Commitments):
- **4-Stage ADK Agentic Microservice Architecture**: Built on Google Agent Development Kit (ADK).
- **Gemini Enterprise App Integration**: Push notifications and email HITL approvals.
- **PEGA Connection Mockup**: Schema-aligned JSON payload adapter for auto-case logging (`PegaMockAdapter`).
- **Hybrid Precedence Database**: Log decision variables (Cloud SQL) and natural language rationales (Vertex AI Vector Search) for HITL learning flywheel.
- **Manual Freeform Disruption Simulator**: Analyst inputs simulated disruption prompts to trigger downstream reasoning logic.

### ❌ Explicit Non-Goals (Scope Protection Boundary):
- ❌ **NO Live System/Database Integrations**: Bypasses IT network delays; operates on schema-validated synthetic datasets inside a Ford-owned GCP instance.
- ❌ **NO Custom React Desktop UI Build**: Scoped to wireframes/mocks only.
- ❌ **NO Mobile RBAC Layouts**: All user groups log into a single unified workstation interface.
- ❌ **NO Automated Web/News Scraping**: Disruption triggers are initiated via manual prompt inputs.

---

## 5. Data Architecture (14 Supply Chain Assets)

| Sr No | Source | Data Asset & Description | Strategy |
| :--- | :--- | :--- | :--- |
| 1 | IDP | CMMS - Part Master, Inventory, ASN, Transactions | Synthetic Schema Mock |
| 2 | IDP | E2Open Supply Chain Collaboration Platform | Synthetic Schema Mock |
| 3 | IDP | Global Supplier Database (4,000+ suppliers) | Synthetic Schema Mock |
| 4 | IDP | Value Stream Mapping & Multi-Tier Risk | Synthetic Schema Mock |
| 5 | IDP | Supplier E2Open Commit / Promise Data | Synthetic Schema Mock |
| 6 | IDP | CMMS Release Forecasts (SA/NA/EU/AP) | Synthetic Schema Mock |
| 7 | IDP | Supplier Performance Data | Synthetic Schema Mock |
| 8 | EDP | Resilinc Supply Chain Event Data | Synthetic Schema Mock |
| 9 | EDP | Indirect NA Outbound Freight Spend | Synthetic Schema Mock |
| 10 | EDP | Ascent Collab Data | Synthetic Schema Mock |
| 11 | MECM | PEGA Commit Gap Triage & Incident Case Data | PEGA JSON Mockup Adapter |
| 12 | LSL | Logistics Service Layer (Frequency, ETA, Freight) | Synthetic Schema Mock |
| 13 | PD-DCA | Product Development (BOM, Engineering Changes) | Static Rules Engine |
| 14 | MFG | Customer Supplier MFG Capacity Data | Static Rules Engine |

---

## 6. Acceptance & Sign-off Criteria (3-2-1 Protocol)
- **Technical Sign-off**: ADK codebase passes 5-axis PSO Code Review, TDD tests, and Intent Audit (`intended-vs-implemented`).
- **Enablement Sign-off**: Completion of 1x 3-hour CodeLabs technical transfer session for 3 junior Ford IT resources.
- **Value Sign-off**: Verified 50-sample retrospective eval suite showing <5 min turnaround and 100% decision explainability.
