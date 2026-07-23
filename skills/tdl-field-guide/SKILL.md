---
name: tdl-field-guide
description: Master operational state machine meta-skill for Google Cloud Technical Deployment Leads (TDLs) & Forward Deployed Engineers (FDEs). Supports Enterprise 12-Week Track and FDE Fast-Track (2-4 Weeks) with Argolis to GCP Prod migration automation.
---

# TDL Field Guide: Dual-Track Operational Meta-Skill

Triggers on: *"tdl field guide"*, *"tdl playbook"*, *"fde fast-track"*, *"run tdl engagement"*, *"lead delta engagement"*

---

## 🏎️ Dual Lifecycle Tracks: Choose Your Deployment Speed

### Track 1: FDE Fast-Track Mode (2-4 Weeks | Rapid Client Prototyping)
Designed for FDE sprints where speed to working demo is critical:
- **Phase 1: Rapid Discover & Scope Freeze (Week 1)**: Set `baseline_kpis.json`, freeze PRD non-goals, initialize Argolis sandbox.
- **Phase 2: Fast-Build & Prototype (Weeks 2-3)**: Build ADK microservices (`google-agents-cli-adk-code`), run TDD unit tests, iterate fast.
- **Phase 3: Argolis ➔ GCP Prod Handover (Week 4)**: Run `./scripts/migrate_tenant.sh`, deploy Cloud Run (`google-agents-cli-deploy`), register agent (`google-agents-cli-publish`).

### Track 2: Enterprise PSO Track (12 Weeks | Full Digital Transformation)
Standard 4-phase transformation lifecycle:
- **Phase 1: Discover & Define (Weeks 0-2)**
- **Phase 2: Prototype & Validate (Weeks 3-6)**
- **Phase 3: Production Build (Weeks 6-10)**
- **Phase 4: Harden & Launch (Weeks 11-12)**

---

## 🎯 Functional Execution Scopes (Zero Bureaucracy)

1. **Monica (Chief of Staff / CLI Dispatcher)**: Front door & CLI command dispatcher (`google-agents-cli-workflow`).
2. **ARCHITECT Scope**: Intake, PRD scope freezing, ADRs (`grill-with-docs`), API contracts.
3. **BUILDER Scope**: ADK scaffolding (`google-agents-cli-scaffold`), ADK Python microservices (`google-agents-cli-adk-code`), TDD unit tests, Cloud Run deployment.
4. **REVIEWER Scope**: Security threat matrix (`threat-model-analyst`), intent audits (`intended-vs-implemented`), eval benchmarks (`google-agents-cli-eval`).

---

## 🔄 Dynamic Capability Slots & Fallback Engine

- `#CAPABILITY: ADK-Workflow` ➔ `google-agents-cli-workflow`
- `#CAPABILITY: Customer-Intake` ➔ `workshop-intake` / `interview-me`
- `#CAPABILITY: Scope-Mapping` ➔ `opportunity-solution-tree` / `user-stories`
- `#CAPABILITY: PRD-Creation` ➔ `create-prd`
- `#CAPABILITY: Scaffolding` ➔ `google-agents-cli-scaffold`
- `#CAPABILITY: Arch-Grilling` ➔ `grill-with-docs` / `google-cloud-waf-security`
- `#CAPABILITY: API-Design` ➔ `api-and-interface-design`
- `#CAPABILITY: InfoSec-Threat` ➔ `threat-model-analyst` / `agent-governance`
- `#CAPABILITY: ADK-Code` ➔ `google-agents-cli-adk-code`
- `#CAPABILITY: TDD` ➔ `test-driven-development` (Paired with `agents-cli`)
- `#CAPABILITY: Code-Review` ➔ `code-review-and-quality`
- `#CAPABILITY: Intent-Audit` ➔ `intended-vs-implemented`
- `#CAPABILITY: Agent-Evaluation` ➔ `google-agents-cli-eval`
- `#CAPABILITY: Agent-Observability` ➔ `google-agents-cli-observability`
- `#CAPABILITY: Release-Deploy` ➔ `shipping-and-launch` / `google-agents-cli-deploy`
- `#CAPABILITY: Registry-Publish` ➔ `google-agents-cli-publish`
