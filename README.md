# 🛡️ Delta TDL Squad (GBrain + Hermes Agent)

> **The Operational Blueprint for Technical Deployment Leads (TDLs) executing the 12-Week Agentic Transformation Lifecycle on Google Cloud.**

This project bridges frontier AI model capabilities into enterprise workflows using a 3-layer local multi-agent architecture powered by **Hermes Agent**, an **Expanded 8-Role Squad**, and **GBrain Shared Persistent Memory**.

---

## 📐 Ecosystem Architecture

```
                                ┌──────────────────────────────────────────────┐
                                │ 1. MONICA (Hermes Chief of Staff)            │
                                │    Orchestration, Synthesis & State Machine  │
                                └──────────────────────┬───────────────────────┘
                                                       │
   ┌───────────┬───────────┬───────────┬───────────────┼───────────────┬───────────┬───────────┐
   ▼           ▼           ▼           ▼               ▼               ▼           ▼           ▼
┌───────┐   ┌───────┐   ┌───────┐   ┌───────┐       ┌───────┐       ┌───────┐   ┌───────┐   ┌───────┐
│ LOGAN │   │  AVA  │   │  EVA  │   │ TYLER │       │  SAM  │       │ FRANK │   │ PETER │   │ ALEX  │
│  10X  │   │ AIAL  │   │ Value │   │  TDL  │       │SecOps │       │  FDE  │   │PlatEng│   │  ATL  │
└───────┘   └───────┘   └───────┘   └───────┘       └───────┘       └───────┘   └───────┘   └───────┘
```

---

## 👥 The Named 8-Role Squad Roster

1. **Monica (Chief of Staff & Hermes Orchestrator)**: Single front door for user queries, squad orchestration, state machine management (`STATE.md`), and answer synthesis.
2. **Logan (10X Lead)**: Qualifies high-leverage business opportunities moving client EBITDA.
3. **Ava (AI Activation Lead - AIAL)**: Owns program governance, executive sign-offs, velocity protection, and risk management.
4. **Eva (Value Lead & Tokenomics Analyst)**: Owns 50-sample retrospective audit baselines (`baseline_kpis.json`), EBITDA impact sizing (`ai-value-sizing`), LLM tokenomics, and API cost optimization.
5. **Tyler (Technical Deployment Lead - TDL)**: Immerses into client domain, redesigns legacy workflows into agentic pipelines, writes PRDs, builds low-fi prototypes, and designs evaluation criteria.
6. **Sam (Security & InfoSec Specialist)**: STRIDE-A threat matrix modeling (`threat-model-analyst`), InfoSec board clearance, sandbox synthetic data scrubbing (`dummy-dataset`), and AST security checks (`ast-resilient-remediation`).
7. **Frank (Forward-Deployed Engineer - FDE)**: Anchors prototypes in client environment, hardens enterprise integrations (SSO, ETL, IAM), drives TDD, and builds automated evaluation pipelines inside client VPCs.
8. **Peter (Platform Engineer)**: Builds "Golden Paths," reusable agent components, and CI/CD observability patterns.
9. **Alex (Agentic Transformation Lead - ATL)**: Drives organizational change management (OCM) and user adoption across client business units.

---

## 📅 The 12-Week Agentic Transformation Lifecycle

```
Phase 1: Discover & Define ──► Phase 2: Prototype & Validate ──► Phase 3: Production Build ──► Phase 4: Harden & Launch
   (Weeks 0-2 | Logan/Ava/Eva)        (Weeks 3-6 | Tyler & Sam)        (Weeks 6-10 | Frank & Peter)     (Weeks 11-12 | Full Squad)
```

### Dynamic Capability Resolution Matrix

| Phase | Capability Slot | Resolved Tool / Skill | Squad Owner | Output Artifact |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1: Discover** | `#CAPABILITY: Customer-Intake`<br>`#CAPABILITY: Scope-Mapping`<br>`#CAPABILITY: PRD-Creation`<br>`#CAPABILITY: ROI-Sizing` | `workshop-intake`<br>`opportunity-solution-tree`<br>`create-prd`<br>`ai-value-sizing` | **Logan, Ava, Eva & Tyler** | `baseline_kpis.json`<br>Frozen PRD |
| **Phase 2: Architect** | `#CAPABILITY: Arch-Grilling`<br>`#CAPABILITY: API-Design`<br>`#CAPABILITY: InfoSec-Threat` | `grill-with-docs`<br>`api-and-interface-design`<br>`threat-model-analyst` | **Tyler, Sam & Frank** | Architecture ADRs<br>`CONTEXT.md`<br>STRIDE-A Threat Matrix |
| **Phase 3: Build & QA** | `#CAPABILITY: Task-Breakdown`<br>`#CAPABILITY: TDD`<br>`#CAPABILITY: Code-Review`<br>`#CAPABILITY: Intent-Audit` | `planning-and-task-breakdown`<br>`test-driven-development`<br>`code-review-and-quality`<br>`intended-vs-implemented` | **Frank, Sam & Peter** | Jira Sprints<br>5-Axis Review<br>*(Rollback if intent fails)* |
| **Phase 4: Launch** | `#CAPABILITY: Agent-Evaluation`<br>`#CAPABILITY: Release-Deploy`<br>`#CAPABILITY: ROI-Sizing`<br>`#CAPABILITY: Handoff-Artifacts` | `google-agents-cli-eval`<br>`shipping-and-launch`<br>`ai-value-sizing`<br>`shipping-artifacts` | **Full Squad** *(Monica, Eva, Sam, Frank, Alex)* | Eval-on-Commit Suite<br>EBITDA Shift Report<br>Client Handoff Packet |

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
│   │   ├── tdl-squad-matrix.md    # Expanded 8-Role squad matrix roster
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
