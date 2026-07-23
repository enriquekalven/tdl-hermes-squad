# 🛡️ Delta TDL Squad (GBrain + Hermes Agent)

> **The Operational Blueprint for Technical Deployment Leads (TDLs) executing the 12-Week Agentic Transformation Lifecycle on Google Cloud.**

This project bridges frontier AI model capabilities into enterprise workflows using a pragmatic 3-scope functional execution matrix powered by **Hermes Agent**, **Google ADK CLI Skills Suite**, and **GBrain Shared Persistent Memory**.

---

## ⚡ Zero-Install Quick Start (10 Seconds)

### 1. Install Master Meta-Skills & Memory Engine
Give your AI coding agent (Antigravity, Cursor, Claude Code, or Hermes CLI) the master TDL operational meta-skill (`tdl-field-guide`) and persistent memory (`gbrain`) in one command:

```bash
npx skills add enriquekalven/tdl-hermes-squad
```

> **What gets installed**:
> - 🛠️ **`tdl-field-guide` (Master Meta-Skill)**: Governs the 12-week state machine (`STATE.md`) and resolves dynamic capability slots (`#CAPABILITY: PRD-Creation`, `#CAPABILITY: InfoSec-Threat`, `#CAPABILITY: ADK-Code`).
> - 🧠 **`gbrain` (Persistent State Skill)**: Enables agents to read/write persistent memory across turns.

---

### 📁 Google Shared Drive Setup (Recommended for Delta Team Engagements)

1. **Create Shared Drive**: The TDL creates a Google Shared Drive for the client engagement (e.g. `Delta_Project_X_GBrain`).
2. **Configure Environment Variable**: Copy `.env.example` to `.env` and set `GBRAIN_DRIVE_DIR`:
   ```bash
   cp .env.example .env
   ```
   Edit `.env`:
   ```env
   GBRAIN_DRIVE_DIR="/Volumes/GoogleDrive/Shared drives/Delta_Project_X_GBrain"
   ```
3. **Run Setup**:
   ```bash
   ./scripts/setup.sh acme_corp
   ```

---

## 💬 How to Trigger & Interact with Monica

Monica is your **Chief of Staff & Hermes Orchestrator**. She acts as the single front door for user queries, managing the 12-week state machine (`STATE.md`), dispatching work across **3 Functional Execution Scopes (Architect, Builder, Reviewer)**, and synthesizing outputs.

### 1. 🤖 In Antigravity / Jetski / Agent IDE (GUI Mode)
* **Start an Engagement Playbook**:
  > *"Monica, let me run tdl-field-guide to lead this Delta engagement."*
* **Check Status & Active Phase**:
  > *"Monica, check GBrain STATE.md and give me a progress report on Phase 1."*
* **Architecture Review**:
  > *"Monica, run the ARCHITECT scope with grill-with-docs on our proposed API gateway and generate ADRs."*
* **Code & Intent Audit**:
  > *"Monica, run the REVIEWER scope with intended-vs-implemented to check if our Phase 3 build matches PRD non-goals."*

---

### 2. 💻 In Terminal via Hermes CLI (CLI Mode)
Launch Hermes CLI in your terminal:
```bash
hermes
```

#### Utility Command Helpers & Interactive Console:
```bash
# 🛡️ Launch Hermes TDL Interactive Console (Zero-Friction CLI)
python3 scripts/tdl_console.py

# 🔍 Search GBrain Memory (Tenant Scope)
python3 scripts/search_brain.py "payment architecture" --tenant acme_corp

# 📊 Run Multi-Objective EBITDA & Quality Evals
python3 scripts/run_evals.py acme_corp

# 🎯 Resolve a TDL Capability Slot
python3 scripts/resolve_capability.py "#CAPABILITY: InfoSec-Threat"

# ⚠️ Trigger Automated State Checkpoint Rollback
./scripts/rollback.sh PHASE_2
```

---

## 📐 Ecosystem Architecture: Lean 3-Scope Execution Matrix

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

| Functional Scope | Core Responsibilities | Dynamic Capability Slot & Tool Mappings |
| :--- | :--- | :--- |
| **Orchestrator** (Monica) | Front door, state machine manager (`STATE.md`), context synthesis | `google-agents-cli-workflow`, `gbrain` |
| 🏛️ **ARCHITECT** | Discovery intake, PRD goal/non-goal freezing, ADRs, API boundaries | `#CAPABILITY: PRD-Creation` ➔ `create-prd`<br>`#CAPABILITY: Scope-Mapping` ➔ `opportunity-solution-tree`<br>`#CAPABILITY: Arch-Grilling` ➔ `grill-with-docs`<br>`#CAPABILITY: API-Design` ➔ `api-and-interface-design` |
| 💻 **BUILDER** | ADK project scaffolding, Python ADK microservices, TDD, Cloud deployment | `#CAPABILITY: Scaffolding` ➔ `google-agents-cli-scaffold`<br>`#CAPABILITY: ADK-Code` ➔ `google-agents-cli-adk-code`<br>`#CAPABILITY: TDD` ➔ `test-driven-development`<br>`#CAPABILITY: Release-Deploy` ➔ `google-agents-cli-deploy`<br>`#CAPABILITY: Registry-Publish` ➔ `google-agents-cli-publish` |
| 🔍 **REVIEWER** | Security threat matrix, 5-axis code quality reviews, intent audits, evals | `#CAPABILITY: InfoSec-Threat` ➔ `threat-model-analyst`<br>`#CAPABILITY: Code-Review` ➔ `code-review-and-quality`<br>`#CAPABILITY: Intent-Audit` ➔ `intended-vs-implemented`<br>`#CAPABILITY: Agent-Evaluation` ➔ `google-agents-cli-eval`<br>`#CAPABILITY: Agent-Observability` ➔ `google-agents-cli-observability` |

---

## 📅 The 12-Week Agentic Transformation Lifecycle

```
Phase 1: Discover & Define ──► Phase 2: Prototype & Validate ──► Phase 3: Production Build ──► Phase 4: Harden & Launch
   (Weeks 0-2 | ARCHITECT)           (Weeks 3-6 | ARCHITECT/REVIEWER)     (Weeks 6-10 | BUILDER/REVIEWER)       (Weeks 11-12 | BUILDER/REVIEWER)
```

---

## 🛡️ Governance & Data Privacy Policies

1. **Strict 1-In, 1-Out Scope Governance**: Mid-flight client feature requests require ejecting an equal-effort backlog item to protect sprint timelines.
2. **Zero-PII Local Data Policy**: GBrain (`.gbrain/` or Google Shared Drive) only stores anonymized architecture notes and SOPs. Real customer data stays strictly inside Client VPCs.
3. **FDE Quality Gate**: BUILDER scope uses `google-agents-cli-adk-code` paired with TDD unit tests and Intent Audits (`intended-vs-implemented`) before PR merge.

---

## 📄 License
Released under the [MIT License](LICENSE).
