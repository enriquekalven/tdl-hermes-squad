# Delta Delivery Model: Functional Execution Matrix

The Delta /Forward operating model relies on a lean 3-scope functional execution matrix orchestrated by **Monica (Hermes Chief of Staff)** operating on **GBrain Shared Persistent Memory**.

```
                                ┌──────────────────────────────────────────────┐
                                │ MONICA (Hermes Chief of Staff / Orchestrator)│
                                │ State Machine, Dispatch & Context Synthesis  │
                                └──────────────────────┬───────────────────────┘
                                                       │
                 ┌─────────────────────────────────────┼─────────────────────────────────────┐
                 ▼                                     ▼                                     ▼
   ┌───────────────────────────┐         ┌───────────────────────────┐         ┌───────────────────────────┐
   │ 1. ARCHITECT (Scope/Design)│         │ 2. BUILDER (Code/Deploy)  │         │ 3. REVIEWER (QA/Security) │
   │ Intake, PRD, Scope Freeze │         │ ADK Code, TDD, Scaffold   │         │ Evals, Threat Scan, Audits│
   └───────────────────────────┘         └───────────────────────────┘         └───────────────────────────┘
```

---

## 👥 Functional Execution Scopes & Capabilities

### 👑 Orchestrator: Monica (Chief of Staff)
- **Role**: Single front door for user queries, 12-week state machine tracking (`STATE.md`), dispatching functional scopes, and synthesizing outputs.
- **Master Skill**: `google-agents-cli-workflow`

---

### 🏛️ 1. ARCHITECT Scope (Discovery, Strategy & API Contracts)
- **Primary Focus**: Discovery workshops, PRD scope freezing, baseline KPI intake, architecture decision records (ADRs), and contract-first API boundaries.
- **Dynamic Capability Slot Mappings**:
  - `#CAPABILITY: Customer-Intake` ➔ `workshop-intake` / `interview-me`
  - `#CAPABILITY: Scope-Mapping` ➔ `opportunity-solution-tree` / `user-stories`
  - `#CAPABILITY: PRD-Creation` ➔ `create-prd` / `spec-driven-development`
  - `#CAPABILITY: Arch-Grilling` ➔ `grill-with-docs` / `google-cloud-waf-security`
  - `#CAPABILITY: API-Design` ➔ `api-and-interface-design` / `codebase-design`

---

### 💻 2. BUILDER Scope (Engineering, TDD & Cloud Deployment)
- **Primary Focus**: ADK project scaffolding, TDD unit testing, microservice development, Cloud Run / GKE container deployment, and registry publishing.
- **Dynamic Capability Slot Mappings**:
  - `#CAPABILITY: Scaffolding` ➔ `google-agents-cli-scaffold`
  - `#CAPABILITY: ADK-Code` ➔ `google-agents-cli-adk-code`
  - `#CAPABILITY: Task-Breakdown` ➔ `planning-and-task-breakdown` / `to-tickets`
  - `#CAPABILITY: TDD` ➔ `test-driven-development` (Paired with `agents-cli`)
  - `#CAPABILITY: Release-Deploy` ➔ `shipping-and-launch` / `google-agents-cli-deploy`
  - `#CAPABILITY: Registry-Publish` ➔ `google-agents-cli-publish`

---

### 🔍 3. REVIEWER Scope (Security, Evals & Quality Gates)
- **Primary Focus**: STRIDE-A threat matrix modeling, 5-axis PSO code reviews, intent audits (`intended-vs-implemented`), eval quality flywheels, and tokenomics metrics.
- **Dynamic Capability Slot Mappings**:
  - `#CAPABILITY: InfoSec-Threat` ➔ `threat-model-analyst` / `agent-governance`
  - `#CAPABILITY: Code-Review` ➔ `code-review-and-quality` / `sql-queries`
  - `#CAPABILITY: Intent-Audit` ➔ `intended-vs-implemented`
  - `#CAPABILITY: Agent-Evaluation` ➔ `google-agents-cli-eval`
  - `#CAPABILITY: Agent-Observability` ➔ `google-agents-cli-observability`
  - `#CAPABILITY: ROI-Sizing` ➔ `ai-value-sizing` / `ab-test-analysis`
