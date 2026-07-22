# 🛡️ Delta TDL Squad (GBrain + Hermes Agent)

> **The Operational Blueprint for Technical Deployment Leads (TDLs) executing the 12-Week Agentic Transformation Lifecycle on Google Cloud.**

This project bridges frontier AI model capabilities into enterprise workflows using a 3-layer local multi-agent architecture powered by **Hermes Agent**, **OpenClaw / Specialist Skills**, and **GBrain Shared Persistent Memory**.

---

## 📐 Ecosystem Architecture

```
                                  ┌───────────────────────────────────┐
                                  │      👤 TECHNICAL DEPLOYMENT LEAD │
                                  └─────────────────┬─────────────────┘
                                                    │
                                                    ▼
                                  ┌───────────────────────────────────┐
                                  │ 1. HERMES CHIEF OF STAFF          │
                                  │    ("Monica" Orchestrator)        │
                                  └─────────┬──────────────┬──────────┘
                                            │              │
        ┌───────────────────────────────────┘              └───────────────────────────────────┐
        │ Read/Write Persistent State                                                          │ Delegates Tasks
        ▼                                                                                      ▼
┌───────────────────────────────────┐                                      ┌───────────────────────────────────┐
│ 3. GBRAIN PERSISTENT MEMORY       │                                      │ 2. DELTA 6-ROLE SQUAD MATRIX      │
│    ~/.gbrain/                     │                                      ├───────────────────────────────────┤
│   ├── STATE.md (12-Week Machine)  │◄─────────────────────────────────────┤ 🎯 10X Lead (Originate)           │
│   ├── baseline_kpis.json          │      Enriches & Audits State         │ 🛡️ AIAL (Govern & Sign-Off)       │
│   ├── operations/                 │                                      │ 🛠️ TDL (Discover & Prototype)    │
│   └── companies/, projects/, etc. │                                      │ 💻 FDE (Build & Client VPC)       │
└───────────────────────────────────┘                                      │ ⚙️ Platform Eng (Golden Paths)    │
                                                                           │ 🚀 ATL (Org Enablement)           │
                                                                           └───────────────────────────────────┘
```

---

## 🎯 The 6-Role Squad Matrix

1. **10X Lead**: Qualifies high-leverage business opportunities moving client EBITDA.
2. **AI Activation Lead (AIAL)**: Owns program governance, executive sign-offs, and velocity protection.
3. **Technical Deployment Lead (TDL)**: Immerses into client domain, redesigns legacy workflows into agentic pipelines, writes PRDs, builds low-fi prototypes, and designs evaluation criteria.
4. **Forward-Deployed Engineer (FDE)**: Anchors prototypes in client environment, hardens enterprise integrations (SSO, ETL, IAM), and builds automated evaluation pipelines.
5. **Platform Engineer**: Builds "Golden Paths," reusable agent components, and CI/CD observability patterns.
6. **Agentic Transformation Lead (ATL)**: Drives organizational change management (OCM) and user adoption across client business units.

---

## 📅 The 12-Week Agentic Transformation Lifecycle

```
Phase 1: Discover & Define ──► Phase 2: Prototype & Validate ──► Phase 3: Production Build ──► Phase 4: Harden & Launch
   (Weeks 0-2 | TDL-Led)            (Weeks 3-6 | TDL+FDE)            (Weeks 6-10 | FDE-Led)          (Weeks 11-12 | Full Squad)
```

### Dynamic Capability Resolution Matrix

| Phase | Capability Slot | Resolved Tool / Skill | Output Artifact |
| :--- | :--- | :--- | :--- |
| **Phase 1: Discover** | `#CAPABILITY: Customer-Intake`<br>`#CAPABILITY: Scope-Mapping`<br>`#CAPABILITY: PRD-Creation` | `workshop-intake`<br>`opportunity-solution-tree`<br>`create-prd` | `baseline_kpis.json`<br>Frozen PRD |
| **Phase 2: Architect** | `#CAPABILITY: Arch-Grilling`<br>`#CAPABILITY: API-Design`<br>`#CAPABILITY: InfoSec-Threat` | `grill-with-docs`<br>`api-and-interface-design`<br>`threat-model-analyst` | Architecture ADRs<br>`CONTEXT.md`<br>STRIDE-A Threat Matrix |
| **Phase 3: Build & QA** | `#CAPABILITY: Task-Breakdown`<br>`#CAPABILITY: TDD`<br>`#CAPABILITY: Code-Review`<br>`#CAPABILITY: Intent-Audit` | `planning-and-task-breakdown`<br>`test-driven-development`<br>`code-review-and-quality`<br>`intended-vs-implemented` | Jira Sprints<br>5-Axis Review<br>*(Rollback to Phase 2 if intent audit fails)* |
| **Phase 4: Launch** | `#CAPABILITY: Agent-Evaluation`<br>`#CAPABILITY: Release-Deploy`<br>`#CAPABILITY: ROI-Sizing`<br>`#CAPABILITY: Handoff-Artifacts` | `google-agents-cli-eval`<br>`shipping-and-launch`<br>`ai-value-sizing`<br>`shipping-artifacts` | Eval-on-Commit Suite<br>EBITDA Shift Report<br>Client Handoff Packet |

---

## 🛡️ Governance & Data Privacy Rules

1. **Strict 1-In, 1-Out Scope Control**: Mid-flight client feature requests require ejecting an equal-effort RICE item or deferring to Post-Week 12 Expansion.
2. **Environment Policy Gate**:
   - **GTM FDE / Sandbox**: Rapid PoCs only (No customer demos).
   - **Argolis**: Synthetic / scrubbed mock data only (`dummy-dataset`).
   - **Client VPC**: Production build & real data allowed.
3. **Data Scrubbing**: Code is verified via AST checks (`ast-resilient-remediation`) to prevent hardcoded secrets or PII/PHI leakage.

---

## 📂 Repository Structure

```
gbrain-hermes-squad/
├── README.md                      # TDL Operational Blueprint & Ecosystem Architecture
├── LICENSE                        # Open-source MIT License
├── .gitignore                     # Git ignore rules
├── brain_template/                # Starter GBrain persistent memory template
│   ├── README.md                  # GBrain schema documentation
│   ├── STATE.md                   # 12-Week operational state machine tracking
│   ├── baseline_kpis.json         # Synthetic baseline metrics (50-sample audit)
│   ├── operations/
│   │   ├── tdl-squad-matrix.md    # 6-Role squad matrix guide
│   │   ├── 12-week-lifecycle.md   # Lifecycle phases & regression loops
│   │   └── environment-matrix.md  # FDE Data privacy & environment matrix
│   ├── people/, companies/, concepts/, ideas/, projects/, newsletter/
├── skills/
│   ├── gbrain/
│   │   └── SKILL.md               # GBrain persistent state skill (TDL Edition)
│   └── tdl-field-guide/
│       └── SKILL.md               # 12-Week TDL Master Operational Meta-Skill
└── scripts/
    └── setup.sh                   # Installer script for local environment
```

---

## 🚀 Installation & Quick Start

```bash
git clone https://github.com/enriquekalven/tdl-hermes-squad.git
cd gbrain-hermes-squad

# Run the TDL Squad installer
./scripts/setup.sh
```

To trigger the master TDL operational meta-skill inside Hermes Agent:
> *"Let's run tdl-field-guide to lead this Delta engagement."*

---

## 📄 License
Released under the [MIT License](LICENSE).
