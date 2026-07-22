---
name: tdl-field-guide
description: Master operational state machine meta-skill for Google Cloud Technical Deployment Leads (TDLs). Governs the 12-week Delta engagement lifecycle, Tier 1 Core & Tier 2 Extended squad matrices, Google ADK CLI skills (workflow, scaffold, adk-code, eval, deploy, publish, observability), 1-in-1-out scope control, dynamic capability slots, and regression loops.
---

# TDL Field Guide: 12-Week Delta Squad Operational Meta-Skill

Triggers on: *"tdl field guide"*, *"tdl playbook"*, *"run tdl engagement"*, *"lead delta engagement"*

## 🎯 Role Definition & Squad Matrix
The Technical Deployment Lead (TDL) orchestrates Tier 1 Core and Tier 2 Extended specialist agents:

### 🔹 Tier 1 Core Squad
- **Monica (Chief of Staff)**: Front door & state machine manager (`google-agents-cli-workflow`)
- **Logan (10X Lead)**: Originate EBITDA opportunities
- **Ava (AIAL)**: Governance & Sign-Offs
- **Eva (Value Lead)**: Baseline KPI audits & EBITDA shift sizing (`google-agents-cli-eval`)
- **Tyler (TDL)**: Discover, Redesign & Prototype (Lead Meta-Skill User)
- **Sam (Security Specialist)**: STRIDE-A threat matrix & data privacy gates
- **Frank (FDE)**: Production Build & ADK Microservices (`google-agents-cli-adk-code`, TDD)
- **Peter (Platform Engineer)**: Golden Paths & Observability (`google-agents-cli-observability`)
- **Alex (ATL)**: Change Management & User Enablement

### 🔸 Tier 2 Extended Specialists
- **Dara (Data & Analytics)**: BigQuery SQL validation & Cloud Trace observability (`google-agents-cli-observability`)
- **Devin (DevOps & Release)**: Cloud Run deployment (`google-agents-cli-deploy`), ADK scaffolding (`google-agents-cli-scaffold`), Gemini Enterprise publishing (`google-agents-cli-publish`)
- **Clara (Cloud WAF & Governance)**: GCP Well-Architected Framework & access arrays
- **Rory (Agile Story & Research)**: Stakeholder interrogation & INVEST stories

---

## 🔄 12-Week State Machine & Dynamic Capability Slots

### Phase 1: Discover & Define (Weeks 0-2 | Logan, Ava, Eva, Rory & Tyler)
- `#CAPABILITY: ADK-Workflow` ➔ Resolves to `google-agents-cli-workflow`
- `#CAPABILITY: Customer-Intake` ➔ Resolves to `workshop-intake` / `interview-me`
- `#CAPABILITY: Scope-Mapping` ➔ Resolves to `opportunity-solution-tree` / `user-stories`
- `#CAPABILITY: PRD-Creation` ➔ Resolves to `create-prd`
- `#CAPABILITY: ROI-Sizing` ➔ Resolves to `ai-value-sizing`
- **Output**: `baseline_kpis.json` & frozen PRD with Goals/Non-Goals.

### Phase 2: Prototype & Validate (Weeks 3-6 | Tyler, Sam, Clara, Devin & Frank)
- `#CAPABILITY: Scaffolding` ➔ Resolves to `google-agents-cli-scaffold`
- `#CAPABILITY: Arch-Grilling` ➔ Resolves to `grill-with-docs` / `google-cloud-waf-security`
- `#CAPABILITY: API-Design` ➔ Resolves to `api-and-interface-design`
- `#CAPABILITY: InfoSec-Threat` ➔ Resolves to `threat-model-analyst` / `agent-governance`
- **Output**: Architecture Decision Records (ADRs), `CONTEXT.md`, InfoSec threat matrix.

### Phase 3: Production Build (Weeks 6-10 | Frank, Sam, Dara & Peter)
- `#CAPABILITY: ADK-Code` ➔ Resolves to `google-agents-cli-adk-code`
- `#CAPABILITY: Task-Breakdown` ➔ Resolves to `planning-and-task-breakdown` & `to-tickets`
- `#CAPABILITY: TDD` ➔ Resolves to `test-driven-development` (Paired with `agents-cli`)
- `#CAPABILITY: Code-Review` ➔ Resolves to `code-review-and-quality` / `sql-queries`
- `#CAPABILITY: Intent-Audit` ➔ Resolves to `intended-vs-implemented`
- **Governance**:
  - **Frank's Combined Build Loop**: Frank uses `agents-cli scaffold` for ADK project scaffolding and `google-agents-cli-adk-code` for ADK patterns, paired with **TDD (Red-Green-Refactor)** for deterministic unit testing.
  - Enforce **Strict 1-In, 1-Out Scope Control**.
  - Enforce **Sam & Clara's Data Privacy Gate** (`dummy-dataset` & `ast-resilient-remediation`).
  - **Regression Loop**: If intent audit detects breaking architectural drift, set `ACTION: ROLLBACK_TO_PHASE_2` in `STATE.md`.

### Phase 4: Harden & Launch (Weeks 11-12 | Full Squad - Devin, Dara, Alex, Monica)
- `#CAPABILITY: Agent-Evaluation` ➔ Resolves to `google-agents-cli-eval`
- `#CAPABILITY: Agent-Observability` ➔ Resolves to `google-agents-cli-observability`
- `#CAPABILITY: Release-Deploy` ➔ Resolves to `shipping-and-launch` / `google-agents-cli-deploy`
- `#CAPABILITY: Registry-Publish` ➔ Resolves to `google-agents-cli-publish`
- `#CAPABILITY: ROI-Sizing` ➔ Resolves to `ai-value-sizing` / `ab-test-analysis`
- `#CAPABILITY: Handoff-Artifacts` ➔ Resolves to `shipping-artifacts`
- **Output**: Pre/post EBITDA shift comparison (by Eva & Dara), launch manifest (by Devin), Gemini Enterprise agent registry registration, client handoff packet.
