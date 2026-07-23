---
name: tdl-field-guide
description: Master operational state machine meta-skill for Google Cloud Technical Deployment Leads (TDLs). Governs the 12-week Delta engagement lifecycle across 3 functional execution scopes (Architect, Builder, Reviewer), Google ADK CLI skills, 1-in-1-out scope control, dynamic capability slots, and regression loops.
---

# TDL Field Guide: 12-Week Delta Squad Operational Meta-Skill

Triggers on: *"tdl field guide"*, *"tdl playbook"*, *"run tdl engagement"*, *"lead delta engagement"*

## 🎯 Role Definition & Functional Execution Scopes
The Technical Deployment Lead (TDL) orchestrates 3 functional execution scopes:
1. **Monica (Chief of Staff)**: Front door & state machine manager (`google-agents-cli-workflow`)
2. **ARCHITECT Scope**: Scoping, PRD freezing, ADRs & API design
3. **BUILDER Scope**: ADK scaffolding, Python ADK microservices, TDD & Cloud deployment
4. **REVIEWER Scope**: Security threat matrix, 5-axis code review, intent audits & eval benchmarks

---

## 🔄 12-Week State Machine & Dynamic Capability Slots

### Phase 1: Discover & Define (Weeks 0-2 | ARCHITECT Scope)
- `#CAPABILITY: ADK-Workflow` ➔ Resolves to `google-agents-cli-workflow`
- `#CAPABILITY: Customer-Intake` ➔ Resolves to `workshop-intake` / `interview-me`
- `#CAPABILITY: Scope-Mapping` ➔ Resolves to `opportunity-solution-tree` / `user-stories`
- `#CAPABILITY: PRD-Creation` ➔ Resolves to `create-prd`
- `#CAPABILITY: ROI-Sizing` ➔ Resolves to `ai-value-sizing`
- **Output**: `baseline_kpis.json` & frozen PRD with Goals/Non-Goals.

### Phase 2: Prototype & Validate (Weeks 3-6 | ARCHITECT & REVIEWER Scopes)
- `#CAPABILITY: Scaffolding` ➔ Resolves to `google-agents-cli-scaffold`
- `#CAPABILITY: Arch-Grilling` ➔ Resolves to `grill-with-docs` / `google-cloud-waf-security`
- `#CAPABILITY: API-Design` ➔ Resolves to `api-and-interface-design`
- `#CAPABILITY: InfoSec-Threat` ➔ Resolves to `threat-model-analyst` / `agent-governance`
- **Output**: Architecture Decision Records (ADRs), `CONTEXT.md`, InfoSec threat matrix.

### Phase 3: Production Build (Weeks 6-10 | BUILDER & REVIEWER Scopes)
- `#CAPABILITY: ADK-Code` ➔ Resolves to `google-agents-cli-adk-code`
- `#CAPABILITY: Task-Breakdown` ➔ Resolves to `planning-and-task-breakdown` & `to-tickets`
- `#CAPABILITY: TDD` ➔ Resolves to `test-driven-development` (Paired with `agents-cli`)
- `#CAPABILITY: Code-Review` ➔ Resolves to `code-review-and-quality` / `sql-queries`
- `#CAPABILITY: Intent-Audit` ➔ Resolves to `intended-vs-implemented`
- **Governance**:
  - **Combined Build Loop**: BUILDER scope uses `agents-cli scaffold` for ADK project scaffolding and `google-agents-cli-adk-code` for ADK patterns, paired with **TDD (Red-Green-Refactor)** for deterministic unit testing.
  - Enforce **Strict 1-In, 1-Out Scope Control**.
  - Enforce **Data Privacy Gate** (`dummy-dataset` & `ast-resilient-remediation`).
  - **Regression Loop**: If intent audit detects breaking architectural drift, set `ACTION: ROLLBACK_TO_PHASE_2` in `STATE.md`.

### Phase 4: Harden & Launch (Weeks 11-12 | BUILDER & REVIEWER Scopes)
- `#CAPABILITY: Agent-Evaluation` ➔ Resolves to `google-agents-cli-eval`
- `#CAPABILITY: Agent-Observability` ➔ Resolves to `google-agents-cli-observability`
- `#CAPABILITY: Release-Deploy` ➔ Resolves to `shipping-and-launch` / `google-agents-cli-deploy`
- `#CAPABILITY: Registry-Publish` ➔ Resolves to `google-agents-cli-publish`
- `#CAPABILITY: ROI-Sizing` ➔ Resolves to `ai-value-sizing` / `ab-test-analysis`
- `#CAPABILITY: Handoff-Artifacts` ➔ Resolves to `shipping-artifacts`
- **Output**: Pre/post EBITDA shift comparison, launch manifest, Gemini Enterprise agent registry registration, client handoff packet.
