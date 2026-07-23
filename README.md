# 🛡️ Delta TDL Squad (GBrain + Hermes Agent)

> **The Operational Blueprint for Technical Deployment Leads (TDLs) executing the 12-Week Agentic Transformation Lifecycle on Google Cloud.**

This project bridges frontier AI model capabilities into enterprise workflows using a 3-layer local multi-agent architecture powered by **Hermes Agent**, an **Expanded Tier 1 & Tier 2 Squad Matrix**, the **Google ADK CLI Skills Suite**, and **GBrain Shared Persistent Memory**.

---

## ⚡ Zero-Install Quick Start (10 Seconds)

Give your AI coding agent (Antigravity, Cursor, Claude Code, or Hermes CLI) the master TDL operational meta-skill in one command:

```bash
npx skills add enriquekalven/tdl-hermes-squad
```

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

Monica is your **Chief of Staff & Hermes Orchestrator**. She acts as the single front door for user queries, managing the 12-week state machine (`STATE.md`), delegating tasks to named specialist agents (Logan, Ava, Eva, Tyler, Sam, Frank, Peter, Alex, Dara, Devin, Clara, Rory), and synthesizing answers.

You can trigger and communicate with Monica across two interfaces:

### 1. 🤖 In Antigravity / Jetski / Agent IDE (GUI Mode)
Simply type natural-language instructions into your agent prompt box:

* **Start an Engagement Playbook**:
  > *"Monica, let's run tdl-field-guide to lead this Delta engagement."*
* **Check Status & Active Phase**:
  > *"Monica, check GBrain STATE.md and give me a progress report on Phase 1."*
* **Architecture Review**:
  > *"Monica, have Tyler run grill-with-docs on our proposed API gateway and generate ADRs."*
* **Code & Intent Audit**:
  > *"Monica, have Frank run intended-vs-implemented to check if our Phase 3 build matches PRD non-goals."*

---

### 2. 💻 In Terminal via Hermes CLI (CLI Mode)
Launch Hermes CLI in your terminal:
```bash
hermes
```

Then prompt Monica directly:
* *"Monica, check ~/.gbrain/tenants/acme_corp/baseline_kpis.json and calculate our EBITDA shift."*
* *"Monica, inspect active PRs in GitHub and log sprint status to GBrain."*

#### Utility Command Helpers & Interactive Console:
```bash
# 🛡️ Launch Hermes TDL Interactive Console (Zero-Friction CLI)
python3 scripts/tdl_console.py

# 🔍 Search GBrain Memory (Tenant Scope)
python3 scripts/search_brain.py "payment architecture" --tenant acme_corp

# 📊 Run EBITDA & Handling Time Evaluation (Multi-Objective)
python3 scripts/run_evals.py acme_corp

# 🎯 Resolve a TDL Capability Slot
python3 scripts/resolve_capability.py "#CAPABILITY: InfoSec-Threat"

# ⚠️ Trigger Automated State Checkpoint Rollback
./scripts/rollback.sh PHASE_2
```

---

## 📐 Ecosystem Architecture

```
                               ┌─────────────────────────────────────────┐
                               │ 1. MONICA (Hermes Chief of Staff)       │
                               │    Orchestration, Synthesis & State    │
                               └────────────────────┬────────────────────┘
                                                    │
        ┌───────────────────────────────────────────┴───────────────────────────────────────────┐
        │ TIER 1 CORE PRIMITIVES (8 Roles)                                                      │ TIER 2 EXTENDED SPECIALISTS (4 Roles)
        ▼                                                                                       ▼
┌────────────────────────────────────────────────────────┐             ┌────────────────────────────────────────────────────────┐
│ Logan (10X Lead: Originate EBITDA)                     │             │ Dara  (Data & Analytics: SQL, Telemetry, Evals)        │
│ Ava   (AIAL: Governance & Sign-Offs)                   │             │ Devin (DevOps Lead: Cloud Run, Deploy, Registry)       │
│ Eva   (Value Lead: Tokenomics & Sizing)               │             │ Clara (Cloud WAF & Governance: IAM, Access Arrays)     │
│ Tyler (TDL: Discover & Architecture)                   │             │ Rory  (Agile Story & Research: INVEST, Retros)         │
│ Sam   (Security: STRIDE-A Threat & Privacy)            │             └────────────────────────────────────────────────────────┘
│ Frank (FDE: Build & VPC Integration)                   │
│ Peter (Platform: Golden Paths & CI/CD)                 │
│ Alex  (ATL: Org Enablement & OCM)                      │
└────────────────────────────────────────────────────────┘
```

---

## 👥 The Named Squad Roster & Google ADK CLI Tool Integration

| Squad Role | Persona Name | Primary Focus & ADK Tool Mapping |
| :--- | :--- | :--- |
| **Chief of Staff** | **Monica** | Single front door & state machine manager (`google-agents-cli-workflow`) |
| **10X Lead** | **Logan** | Originate & shape high-EBITDA enterprise opportunities |
| **AIAL Lead** | **Ava** | Program governance, executive sign-offs, velocity protection |
| **Value Lead** | **Eva** | Baseline KPI audits (`baseline_kpis.json`), tokenomics & evals (`google-agents-cli-eval`) |
| **TDL Architect** | **Tyler** | Domain immersion, workflow redesign, PRD freezing, low-fi prototyping |
| **Security Specialist** | **Sam** | STRIDE-A threat matrix modeling & sandbox synthetic data privacy |
| **FDE Lead** | **Frank** | Production ADK microservice build (`google-agents-cli-adk-code`, TDD) |
| **Platform Eng** | **Peter** | Reusable Golden Paths, CI/CD telemetry (`google-agents-cli-observability`) |
| **ATL Lead** | **Alex** | Organizational change management (OCM) & IT staff enablement |
| **Data & Analytics** | **Dara** | BigQuery SQL, Cloud Trace observability (`google-agents-cli-observability`) |
| **DevOps Specialist** | **Devin** | ADK scaffold (`google-agents-cli-scaffold`), Cloud Run deploy (`google-agents-cli-deploy`), Gemini Enterprise publishing (`google-agents-cli-publish`) |
| **Cloud WAF & Gov** | **Clara** | GCP Well-Architected Framework reviews (`google-cloud-waf-security`) |
| **Agile Story Lead** | **Rory** | Stakeholder alignment interrogation (`interview-me`), INVEST user stories (`user-stories`) |

---

## 📅 The 12-Week Agentic Transformation Lifecycle

```
Phase 1: Discover & Define ──► Phase 2: Prototype & Validate ──► Phase 3: Production Build ──► Phase 4: Harden & Launch
 (Weeks 0-2 | Logan/Ava/Eva/Rory)    (Weeks 3-6 | Tyler/Sam/Clara)    (Weeks 6-10 | Frank/Sam/Dara)    (Weeks 11-12 | Full Squad)
```

### Dynamic Capability Resolution Matrix (With Google ADK CLI Suite)

| Phase | Capability Slot | Resolved Tool / Skill | Squad Owner | Output Artifact |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1: Discover** | `#CAPABILITY: ADK-Workflow`<br>`#CAPABILITY: Customer-Intake`<br>`#CAPABILITY: Scope-Mapping`<br>`#CAPABILITY: PRD-Creation`<br>`#CAPABILITY: ROI-Sizing` | `google-agents-cli-workflow`<br>`workshop-intake` / `interview-me`<br>`opportunity-solution-tree` / `user-stories`<br>`create-prd`<br>`ai-value-sizing` | **Logan, Ava, Eva, Rory & Tyler** | `baseline_kpis.json`<br>Frozen PRD |
| **Phase 2: Architect** | `#CAPABILITY: Scaffolding`<br>`#CAPABILITY: Arch-Grilling`<br>`#CAPABILITY: API-Design`<br>`#CAPABILITY: InfoSec-Threat` | `google-agents-cli-scaffold`<br>`grill-with-docs` / `google-cloud-waf-security`<br>`api-and-interface-design`<br>`threat-model-analyst` / `agent-governance` | **Tyler, Sam, Clara, Devin & Frank** | Architecture ADRs<br>`CONTEXT.md`<br>STRIDE-A Threat Matrix |
| **Phase 3: Build & QA** | `#CAPABILITY: ADK-Code`<br>`#CAPABILITY: Task-Breakdown`<br>`#CAPABILITY: TDD`<br>`#CAPABILITY: Code-Review`<br>`#CAPABILITY: Intent-Audit` | `google-agents-cli-adk-code`<br>`planning-and-task-breakdown`<br>`test-driven-development`<br>`code-review-and-quality`<br>`intended-vs-implemented` | **Frank, Sam, Dara & Peter** | ADK Agent Codebase<br>Jira Sprints<br>5-Axis PSO Review<br>*(Rollback if intent fails)* |
| **Phase 4: Launch** | `#CAPABILITY: Agent-Evaluation`<br>`#CAPABILITY: Agent-Observability`<br>`#CAPABILITY: Release-Deploy`<br>`#CAPABILITY: Registry-Publish`<br>`#CAPABILITY: ROI-Sizing`<br>`#CAPABILITY: Handoff-Artifacts` | `google-agents-cli-eval`<br>`google-agents-cli-observability`<br>`shipping-and-launch` / `google-agents-cli-deploy`<br>`google-agents-cli-publish`<br>`ai-value-sizing` / `ab-test-analysis`<br>`shipping-artifacts` | **Full Squad** *(Monica, Devin, Dara, Alex)* | Quality Flywheel Evals<br>Gemini Registry Pub<br>EBITDA Shift Report<br>Client Handoff Packet |

---

## 🛡️ Governance & Data Privacy Policies

1. **Strict 1-In, 1-Out Scope Governance**: Mid-flight client feature requests require ejecting an equal-effort RICE item back to the backlog or Post-Week 12 Expansion.
2. **Zero-PII Local Data Policy**: `~/.gbrain/` only stores anonymized architecture notes/SOPs scrubbed via `dummy-dataset`. Real customer data stays strictly inside Client VPCs.
3. **FDE Quality Gate**: Frank (FDE) uses `google-agents-cli-adk-code` paired with TDD unit tests and Intent Audits (`intended-vs-implemented`) before PR merge.

---

## 📂 Repository Structure

```
tdl-hermes-squad/
├── README.md                      # TDL Operational Blueprint & Ecosystem Architecture
├── LICENSE                        # Open-source MIT License
├── .gitignore                     # Git ignore rules
├── brain_template/                # Starter GBrain persistent memory template
│   ├── README.md                  # GBrain schema documentation
│   ├── STATE.md                   # 12-Week operational state machine tracking
│   ├── baseline_kpis.json         # Synthetic baseline metrics (50-sample audit)
│   ├── operations/
│   │   ├── tdl-squad-matrix.md    # Tier 1 & Tier 2 squad matrix roster
│   │   ├── 12-week-lifecycle.md   # Lifecycle phases & regression loops
│   │   └── environment-matrix.md  # FDE Data privacy & environment matrix
│   ├── people/, companies/, concepts/, ideas/, projects/, newsletter/
├── docs/
│   ├── EXECUTIVE_GUIDE.md         # Comprehensive setup & leadership evaluation guide
│   ├── PRESENTATION_DECK.md       # 10-slide executive presentation deck
│   └── WAYS_OF_WORKING_PRESENTATION.md # 9-slide TDL maturity framework deck
├── skills/
│   ├── gbrain/
│   │   └── SKILL.md               # GBrain persistent state skill (TDL Edition)
│   └── tdl-field-guide/
│       └── SKILL.md               # 12-Week TDL Master Operational Meta-Skill
└── scripts/
    ├── setup.sh                   # Installer script for local environment
    ├── tdl_console.py             # Interactive TDL CLI Console
    ├── search_brain.py            # Multi-Tenant GBrain search tool
    ├── run_evals.py               # Multi-Objective EBITDA eval tool
    └── resolve_capability.py      # Dynamic capability slot resolver
```

---

## 📄 License
Released under the [MIT License](LICENSE).
