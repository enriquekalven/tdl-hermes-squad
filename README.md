# 🛡️ Delta TDL Squad (GBrain + Hermes Agent)

> **The Operational Blueprint for Technical Deployment Leads (TDLs) executing the 12-Week Agentic Transformation Lifecycle on Google Cloud.**

This project bridges frontier AI model capabilities into enterprise workflows using a 3-layer local multi-agent architecture powered by **Hermes Agent**, a **Tier 1 & Tier 2 Squad Matrix**, and **GBrain Shared Persistent Memory**.

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

## 👥 The Named Squad Roster (Tier 1 Core & Tier 2 Extended)

### 🔹 Tier 1 Core Squad
1. **Monica (Chief of Staff & Hermes Orchestrator)**: Single front door, state machine management (`STATE.md`), synthesis.
2. **Logan (10X Lead)**: Qualifies high-leverage business opportunities moving client EBITDA.
3. **Ava (AI Activation Lead - AIAL)**: Program governance, executive sign-offs, velocity protection, risk mitigation.
4. **Eva (Value Lead & Tokenomics Analyst)**: Baseline KPI audits (`baseline_kpis.json`), EBITDA impact sizing (`ai-value-sizing`), tokenomics.
5. **Tyler (Technical Deployment Lead - TDL)**: Domain immersion, PRD scope freezing (`create-prd`), low-fi prototyping, eval design.
6. **Sam (Security & InfoSec Specialist)**: STRIDE-A threat matrix modeling (`threat-model-analyst`), InfoSec board clearance, data privacy (`dummy-dataset`, `ast-resilient-remediation`).
7. **Frank (Forward-Deployed Engineer - FDE)**: Production code build, client VPC integration, TDD, 5-axis PSO code reviews (`code-review-and-quality`).
8. **Peter (Platform Engineer)**: Reusable agent "Golden Paths," CI/CD telemetry.
9. **Alex (Agentic Transformation Lead - ATL)**: Organizational change management (OCM), staff enablement, user adoption.

### 🔸 Tier 2 Extended Specialists
10. **Dara (Data & Analytics Specialist)**: BigQuery SQL validation (`sql-queries`), Cloud Trace observability (`google-agents-cli-observability`), cohort analytics (`ab-test-analysis`).
11. **Devin (DevOps & Release Specialist)**: Cloud Run / GKE deployment (`google-agents-cli-deploy`), Gemini Enterprise registry publishing (`google-agents-cli-publish`), release notes (`release-notes`).
12. **Clara (Cloud WAF & Governance Specialist)**: GCP Well-Architected Framework reviews (`google-cloud-waf-security`), policy access control arrays (`agent-governance`).
13. **Rory (Agile Story & Research Lead)**: Stakeholder alignment interrogation (`interview-me`), INVEST user/job stories (`user-stories`), retrospectives (`retro`).

---

## 📅 The 12-Week Agentic Transformation Lifecycle

```
Phase 1: Discover & Define ──► Phase 2: Prototype & Validate ──► Phase 3: Production Build ──► Phase 4: Harden & Launch
 (Weeks 0-2 | Logan/Ava/Eva/Rory)    (Weeks 3-6 | Tyler/Sam/Clara)    (Weeks 6-10 | Frank/Sam/Dara)    (Weeks 11-12 | Full Squad)
```

### Dynamic Capability Resolution Matrix

| Phase | Capability Slot | Resolved Tool / Skill | Squad Owner | Output Artifact |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1: Discover** | `#CAPABILITY: Customer-Intake`<br>`#CAPABILITY: Scope-Mapping`<br>`#CAPABILITY: PRD-Creation`<br>`#CAPABILITY: ROI-Sizing` | `workshop-intake` / `interview-me`<br>`opportunity-solution-tree` / `user-stories`<br>`create-prd`<br>`ai-value-sizing` | **Logan, Ava, Eva, Rory & Tyler** | `baseline_kpis.json`<br>Frozen PRD |
| **Phase 2: Architect** | `#CAPABILITY: Arch-Grilling`<br>`#CAPABILITY: API-Design`<br>`#CAPABILITY: InfoSec-Threat` | `grill-with-docs` / `google-cloud-waf-security`<br>`api-and-interface-design`<br>`threat-model-analyst` / `agent-governance` | **Tyler, Sam, Clara & Frank** | Architecture ADRs<br>`CONTEXT.md`<br>STRIDE-A Threat Matrix |
| **Phase 3: Build & QA** | `#CAPABILITY: Task-Breakdown`<br>`#CAPABILITY: TDD`<br>`#CAPABILITY: Code-Review`<br>`#CAPABILITY: Intent-Audit` | `planning-and-task-breakdown`<br>`test-driven-development`<br>`code-review-and-quality` / `sql-queries`<br>`intended-vs-implemented` | **Frank, Sam, Dara & Peter** | Jira Sprints<br>5-Axis Review<br>*(Rollback if intent fails)* |
| **Phase 4: Launch** | `#CAPABILITY: Agent-Evaluation`<br>`#CAPABILITY: Release-Deploy`<br>`#CAPABILITY: ROI-Sizing`<br>`#CAPABILITY: Handoff-Artifacts` | `google-agents-cli-eval` / `google-agents-cli-observability`<br>`shipping-and-launch` / `google-agents-cli-deploy`<br>`ai-value-sizing` / `ab-test-analysis`<br>`shipping-artifacts` / `google-agents-cli-publish` | **Full Squad** *(Monica, Devin, Dara, Alex)* | Eval-on-Commit Suite<br>EBITDA Shift Report<br>Client Handoff Packet |

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
│   │   ├── tdl-squad-matrix.md    # Tier 1 & Tier 2 squad matrix roster
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
