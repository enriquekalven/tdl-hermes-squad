---
name: tdl-field-guide
description: Master operational state machine meta-skill for Google Cloud Technical Deployment Leads (TDLs). Governs the 12-week Delta engagement lifecycle, 6-role squad matrix, 1-in-1-out scope control, dynamic capability slots, and regression loops.
---

# TDL Field Guide: 12-Week Delta Squad Operational Meta-Skill

Triggers on: *"tdl field guide"*, *"tdl playbook"*, *"run tdl engagement"*, *"lead delta engagement"*

## 🎯 Role Definition & Squad Matrix
The Technical Deployment Lead (TDL) orchestrates the 6-role squad matrix:
1. **10X Lead**: Originate & Shape
2. **AIAL**: Program Governance & Client Sign-Offs
3. **TDL**: Discover, Redesign & Prototype (Lead Meta-Skill User)
4. **FDE**: Production Build & Client VPC Integration
5. **Platform Engineer**: Reusable Golden Paths & Observability
6. **ATL**: Org Change Management & User Enablement

---

## 🔄 12-Week State Machine & Dynamic Capability Slots

### Phase 1: Discover & Define (Weeks 0-2)
- `#CAPABILITY: Customer-Intake` ➔ Resolves to `workshop-intake`
- `#CAPABILITY: Scope-Mapping` ➔ Resolves to `opportunity-solution-tree`
- `#CAPABILITY: PRD-Creation` ➔ Resolves to `create-prd`
- **Output**: `baseline_kpis.json` & frozen PRD with Goals/Non-Goals.

### Phase 2: Prototype & Validate (Weeks 3-6)
- `#CAPABILITY: Arch-Grilling` ➔ Resolves to `grill-with-docs`
- `#CAPABILITY: API-Design` ➔ Resolves to `api-and-interface-design`
- `#CAPABILITY: InfoSec-Threat` ➔ Resolves to `threat-model-analyst`
- **Output**: Architecture Decision Records (ADRs), `CONTEXT.md`, InfoSec threat matrix.

### Phase 3: Production Build (Weeks 6-10)
- `#CAPABILITY: Task-Breakdown` ➔ Resolves to `planning-and-task-breakdown` & `to-tickets`
- `#CAPABILITY: TDD` ➔ Resolves to `test-driven-development`
- `#CAPABILITY: Code-Review` ➔ Resolves to `code-review-and-quality`
- `#CAPABILITY: Intent-Audit` ➔ Resolves to `intended-vs-implemented`
- **Governance**:
  - Enforce **Strict 1-In, 1-Out Scope Control**.
  - Enforce **Data Privacy Gate** (`dummy-dataset` & `ast-resilient-remediation`).
  - **Regression Loop**: If intent audit detects breaking architectural drift, set `ACTION: ROLLBACK_TO_PHASE_2` in `STATE.md`.

### Phase 4: Harden & Launch (Weeks 11-12)
- `#CAPABILITY: Agent-Evaluation` ➔ Resolves to `google-agents-cli-eval`
- `#CAPABILITY: Release-Deploy` ➔ Resolves to `shipping-and-launch`
- `#CAPABILITY: ROI-Sizing` ➔ Resolves to `ai-value-sizing`
- `#CAPABILITY: Handoff-Artifacts` ➔ Resolves to `shipping-artifacts`
- **Output**: Pre/post EBITDA shift comparison, launch manifest, client handoff packet.
