# 📊 Presentation Deck: Hermes TDL Squad & GBrain Architecture

> **Compounding Agentic Intelligence for Google Cloud Delta & Enterprise AI Deployments**  
> **Presenter**: Enrique Chan (Technical Deployment Lead, Google Cloud Delta)  

---

## 🎬 Slide 1: Title & Headline
# 🧠 Hermes TDL Squad: Compounding Agentic Intelligence
### Scaling 12-Week Google Cloud Enterprise Transformations with 5x Operating Leverage

- **Presenter**: Enrique Chan (TDL, Google Cloud Delta /Forward)
- **Architecture**: Hermes Agent (Orchestration) + 6-Role Squad (Execution) + GBrain (Shared Memory)
- **Repo**: `github.com/enriquekalven/tdl-hermes-squad`

---

## 💥 Slide 2: The Enterprise Deployment Challenge
# Why Most Enterprise AI Deployments Stall

1. **Context Fragmentation**: AI tools & engineers start from zero on every task, spending 30-50% of sprint time re-researching legacy facts.
2. **Uncontrolled Scope Drift**: Mid-flight feature requests cause 12-week SOWs to bloat into 24-week delays.
3. **No Metric-Backed ROI**: Difficulty quantifying pre- and post-deployment business value for C-suite sponsors.

> *"We don't need another isolated coding chatbot. We need a persistent, state-gated agent squad."*

---

## 📐 Slide 3: The 3-Layer Solution
# The 3-Layer Hermes Squad Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ 1. HERMES AGENT ("Monica")                                  │
│    Chief of Staff · Single Front Door · State Machine       │
└──────────────┬──────────────────────────────┬───────────────┘
               │                              │
               ▼                              ▼
┌──────────────────────────────┐┌──────────────────────────────┐
│ 2. SPECIALIST SQUAD MATRIX   ││ 3. GBRAIN PERSISTENT MEMORY  │
│    10X Lead · AIAL · TDL     ││    ~/.gbrain/                │
│    FDE · Platform · ATL      ││    STATE.md · baseline_kpis  │
└──────────────────────────────┘└──────────────────────────────┘
```

---

## 👥 Slide 4: The 6-Role Squad Matrix
# Synchronized Execution Across 6 Specialized Roles

- **🎯 10X Lead**: Originate & shape high-EBITDA enterprise opportunities.
- **🛡️ AI Activation Lead (AIAL)**: Program governance, sign-offs, and velocity protection.
- **🛠️ Technical Deployment Lead (TDL)**: Domain immersion, workflow redesign, PRD freezing, low-fi prototyping.
- **💻 Forward-Deployed Engineer (FDE)**: Production build, client VPC integration, automated evals.
- **⚙️ Platform Engineer**: Reusable Golden Paths, CI/CD, and telemetry patterns.
- **🚀 Agentic Transformation Lead (ATL)**: Organizational change management (OCM) and user enablement.

---

## 📅 Slide 5: The 12-Week Transformation Lifecycle
# Dynamic Capability Resolution Matrix

```
Phase 1: Discover & Define ──► Phase 2: Prototype & Validate ──► Phase 3: Production Build ──► Phase 4: Harden & Launch
   (Weeks 0-2 | TDL-Led)            (Weeks 3-6 | TDL+FDE)            (Weeks 6-10 | FDE-Led)          (Weeks 11-12 | Full Squad)
```

- **Phase 1**: `#CAPABILITY: Customer-Intake` ➔ `workshop-intake` | `baseline_kpis.json`
- **Phase 2**: `#CAPABILITY: Arch-Grilling` ➔ `grill-with-docs` | ADRs & `CONTEXT.md`
- **Phase 3**: `#CAPABILITY: Task-Breakdown` ➔ `planning-and-task-breakdown` | TDD & 5-Axis Code Review
- **Phase 4**: `#CAPABILITY: Agent-Evaluation` ➔ `google-agents-cli-eval` | EBITDA Shift Report

---

## 🧠 Slide 6: GBrain Shared Memory Architecture
# Structured Knowledge that Compounds Over Time

- **Read-First Rule**: Before starting research or code, agents query `~/.gbrain/` to build on stored facts.
- **Write-Back Rule**: High-signal discoveries automatically save to entity collections:
  - `companies/`, `concepts/`, `projects/`, `operations/`, `STATE.md`
- **Impact**: Zero context loss between team members or agent turns.

---

## 🛡️ Slide 7: Governance & Safety Nets
# Strict Scope Control & Automated Rollbacks

- **1-In, 1-Out Trade-off Rule**: RICE-driven feature swaps prevent sprint bloat.
- **Automated Intent Audits**: `intended-vs-implemented` checks code against PRD non-goals.
- **Automated Rollback Checkpoint**: Trigger `./scripts/rollback.sh PHASE_2` if breaking architectural drift occurs.

---

## 🔒 Slide 8: Enterprise Security & Data Privacy
# De-Risking InfoSec Review Boards

- **STRIDE-A Threat Matrix**: `threat-model-analyst` runs threat modeling before InfoSec review.
- **Argolis & GTM Privacy Rule**: Customer PII/PHI is never uploaded to non-prod sandbox environments.
- **Data Scrubbing**: `dummy-dataset` synthetic data + `ast-resilient-remediation` static code checks.

---

## 📊 Slide 9: Quantifiable EBITDA Business Value
# Metric-Backed ROI Realization

- **Sample Size**: 50-sample retrospective audit benchmark.
- **⏱️ Handling Time Reduction**: **88.89%** (45m ➔ 5m)
- **💵 Unit Cost Savings**: **87.14%** ($35.00 ➔ $4.50)
- **🚀 EBITDA Impact**: **$1,500,000 / year** projected savings.

---

## 🚀 Slide 10: Open Source Strategy & Call to Action
# Open-Sourcing the TDL Hermes Squad Framework

- **Open Source Repository**: `https://github.com/enriquekalven/tdl-hermes-squad`
- **Open Standards**: Built on `SKILL.md` (agentskills.io) compatible with Hermes, Antigravity, Cursor, and Claude Code.
- **Call to Action**: Clone the repo, run `./scripts/setup.sh`, and empower your deployment leads today!
