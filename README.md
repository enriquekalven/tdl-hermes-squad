# 🛡️ Delta TDL & FDE Squad (GBrain + Hermes Agent)

> **The Operational Blueprint for Technical Deployment Leads (TDLs) & Forward Deployed Engineers (FDEs) executing Agentic Transformation on Google Cloud.**

This project bridges frontier AI model capabilities into enterprise workflows using a pragmatic 3-scope functional execution matrix powered by **Hermes Agent**, **Google ADK CLI Skills Suite**, **FDE Fast-Track Mode**, and **GBrain Shared Persistent Memory**.

---

## 🏎️ Dual Lifecycle Tracks: Choose Your Deployment Speed

```
┌────────────────────────────────────────────────────────────────────────┐
│ TRACK 1: FDE FAST-TRACK (2-4 WEEKS)                                    │
│ Rapid Client Prototyping & Argolis ➔ GCP Prod Landing Zone             │
│ Phase 1: Rapid Discover (W1) ➔ Phase 2: Fast-Build (W2-3) ➔ Phase 3: Handover (W4) │
├────────────────────────────────────────────────────────────────────────┤
│ TRACK 2: ENTERPRISE PSO TRACK (12 WEEKS)                              │
│ Full Organizational Transformation                                     │
│ Phase 1: Discover (W0-2) ➔ Phase 2: Prototype (W3-6) ➔ Phase 3: Build (W6-10) ➔ Phase 4: Launch (W11-12) │
└────────────────────────────────────────────────────────────────────────┘
```

---

## ⚡ Zero-Install Quick Start (10 Seconds)

### 1. Install Master Meta-Skills & Memory Engine
Give your AI coding agent (Antigravity, Cursor, Claude Code, or Hermes CLI) the master TDL/FDE operational meta-skill (`tdl-field-guide`) and persistent memory (`gbrain`) in one command:

```bash
npx skills add enriquekalven/tdl-hermes-squad
```

---

### 📁 Google Shared Drive Setup (Recommended for Delta Team Engagements)

1. **Configure Environment Variable**: Copy `.env.example` to `.env` and set `GBRAIN_DRIVE_DIR`:
   ```bash
   cp .env.example .env
   ```
2. **Run Setup**:
   ```bash
   ./scripts/setup.sh acme_corp
   ```

---

## ✈️ FDE Fast-Track: Argolis Sandbox ➔ GCP Production Migration

When an FDE finishes prototyping in an Argolis playground (`gcp-argolis-123`) and is ready to deploy to the customer's actual GCP Production Landing Zone (`customer-gcp-prod-88`), run the automated migration command:

```bash
./scripts/migrate_tenant.sh acme_corp customer-gcp-prod-88
```

> **What happens**:
> - 📄 Updates target GCP project IDs across `STATE.md` and environment SOPs.
> - 📦 Generates `migration_manifest.json` preserving architecture decision records, baseline KPIs, and test floor pass rates.
> - 🚀 Prepares ADK container deployment (`google-agents-cli-deploy`) to the customer's secure production project.

---

## 💬 How to Trigger & Interact with Monica

Monica is your **Chief of Staff & Hermes Orchestrator**. She acts as the single front door for user queries, managing the state machine (`STATE.md`), dispatching work across **3 Functional Execution Scopes (Architect, Builder, Reviewer)**, and synthesizing outputs.

### Utility Command Helpers & Interactive Console:
```bash
# 🛡️ Launch Hermes TDL & FDE Interactive Console (Dual-Track CLI)
python3 scripts/tdl_console.py

# ✈️ Run FDE Fast-Track Argolis ➔ GCP Prod Migration
./scripts/migrate_tenant.sh acme_corp customer-gcp-prod-88

# 🔍 Search GBrain Memory (Tenant Scope)
python3 scripts/search_brain.py "payment architecture" --tenant acme_corp

# 📊 Run Multi-Objective EBITDA & Quality Evals
python3 scripts/run_evals.py acme_corp

# 🎯 Resolve a Capability Slot
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

## 🛡️ Governance & Data Privacy Policies

1. **Strict 1-In, 1-Out Scope Governance**: Mid-flight client feature requests require ejecting an equal-effort backlog item to protect sprint timelines.
2. **Zero-PII Argolis Data Policy**: Argolis sandboxes strictly use synthetic datasets (`dummy-dataset`). Real customer database connections are established *only* after deploying to the Customer GCP Production Landing Zone.
3. **FDE Quality Gate**: BUILDER scope uses `google-agents-cli-adk-code` paired with TDD unit tests and Intent Audits (`intended-vs-implemented`) before PR merge.

---

## 📄 License
Released under the [MIT License](LICENSE).
