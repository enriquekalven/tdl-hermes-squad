# Executive Guide & Architectural Analysis: Delta TDL Squad Framework

> **A Practical Guide for Engineering Directors, Principal Engineers, and Technical Deployment Leads (TDLs) executing GenAI Transformation on Google Cloud.**

---

## 🏛️ Executive Summary & Architectural Refactoring

This framework sits at the intersection of **methodological rigor** and **agentic automation**. Following feedback from Principal Engineering reviews, the architecture was intentionally refactored to eliminate persona fluff while preserving high-value delivery primitives.

### What Was Retained (The Real Engineering Value):
1. **Standardized 12-Week State Machine**: Rigid delivery phases (Discover ➔ Prototype ➔ Build ➔ Launch) with frozen entry/exit criteria and automated rollback (`scripts/rollback.sh`).
2. **Dynamic Capability Slots (`#CAPABILITY:`)**: Decouples operational phases from specific tools. If a specialized tool is missing, `scripts/resolve_capability.py` seamlessly falls back to local markdown SOPs.
3. **GBrain Persistent Memory Schema (`.gbrain/` / Google Shared Drive)**: Solves LLM statelessness by persisting architecture decisions, baseline KPIs, and sprint state across turns.

### What Was Streamlined (Persona Consolidation):
- Consolidated named personas into **3 Functional Execution Scopes**:
  - 🏛️ **ARCHITECT**: Intake, discovery, PRD freezing, ADRs, and API interface design.
  - 💻 **BUILDER**: ADK project scaffolding, Python microservices, TDD unit testing, Cloud Run deployment.
  - 🔍 **REVIEWER**: STRIDE-A threat matrix modeling, 5-axis code quality reviews, intent audits, eval quality flywheels.

---

## 📐 Functional Execution Matrix

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

## 📂 Multi-Tenant & Google Shared Drive Workspace Setup

```bash
# Option 1: Shared Drive setup via .env
cp .env.example .env
# Set GBRAIN_DRIVE_DIR="/Volumes/GoogleDrive/Shared drives/Delta_Project_X_GBrain"

# Option 2: Run setup script
./scripts/setup.sh acme_corp
```

---

## 🎯 Verification & Quality Checklist for TDLs

- [x] **Phase 1**: Baseline KPIs logged to `baseline_kpis.json`, PRD non-goals frozen by ARCHITECT scope.
- [x] **Phase 2**: ADRs written to `concepts/`, InfoSec threat matrix reviewed by REVIEWER scope.
- [x] **Phase 3**: ADK scaffolding built by BUILDER scope using `agents-cli scaffold`, verified with TDD unit tests and `intended-vs-implemented` intent audits.
- [x] **Phase 4**: Agent evals benchmarked by REVIEWER scope via `google-agents-cli-eval`, agent published to Gemini Enterprise Registry (`google-agents-cli-publish`).
