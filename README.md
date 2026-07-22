# 🛡️ Delta TDL Squad (GBrain + Hermes Agent)

> **The Operational Blueprint for Technical Deployment Leads (TDLs) executing the 12-Week Agentic Transformation Lifecycle on Google Cloud.**

This project bridges frontier AI model capabilities into enterprise workflows using a 3-layer local multi-agent architecture powered by **Hermes Agent**, an **Expanded Tier 1 & Tier 2 Squad Matrix**, and **GBrain Shared Persistent Memory**.

---

## ⚡ Zero-Install Quick Start (10 Seconds)

Give your AI coding agent (Antigravity, Cursor, Claude Code, or Hermes CLI) the master TDL operational meta-skill in one command:

```bash
npx skills add enriquekalven/tdl-hermes-squad
```

Or clone and initialize locally:
```bash
git clone https://github.com/enriquekalven/tdl-hermes-squad.git
cd tdl-hermes-squad
./scripts/setup.sh
```

---

## 💬 How to Trigger & Interact with Monica

Monica is your **Chief of Staff & Hermes Orchestrator**. She acts as the single front door for user queries, managing the 12-week state machine (`STATE.md`), delegating tasks to named specialist agents (Logan, Ava, Eva, Tyler, Sam, Frank, Peter, Alex), and synthesizing answers.

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
* *"Monica, check ~/.gbrain/tenants/ford/baseline_kpis.json and calculate our EBITDA shift."*
* *"Monica, inspect active PRs in GitHub and log sprint status to GBrain."*

#### Utility Command Helpers:
```bash
# 🔍 Search GBrain Memory (Tenant Scope)
python3 scripts/search_brain.py "payment architecture" --tenant ford

# 📊 Run EBITDA & Handling Time Evaluation (Multi-Objective)
python3 scripts/run_evals.py ford

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

## 🛡️ Governance & Data Privacy Policies

1. **Strict 1-In, 1-Out Scope Governance**: Mid-flight client feature requests require ejecting an equal-effort RICE item back to the backlog or Post-Week 12 Expansion.
2. **Zero-PII Local Data Policy**: `~/.gbrain/` only stores anonymized architecture notes/SOPs scrubbed via `dummy-dataset`. Real customer data stays strictly inside Client VPCs.
3. **FDE Quality Gate**: Frank (FDE) must pass 5-axis PSO Code Review, TDD unit tests, and Intent Audits (`intended-vs-implemented`) before PR merge.

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
    └── setup.sh                   # Installer script for local environment
```

---

## 📄 License
Released under the [MIT License](LICENSE).
