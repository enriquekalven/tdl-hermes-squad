# 📘 Google Cloud Delta: Hermes TDL Chief of Staff ("Monica") & GBrain User Guide

**Author**: Enrique Chan (Technical Deployment Lead, Google Cloud Delta /Forward)  
**Target Audience**: Delta TDLs, FDEs, Product Managers, Security Engineers, and Engineering Leadership  
**Status**: Active Operational Standard  

---

## 📌 Executive Summary

The **Hermes TDL Chief of Staff ("Monica") + GBrain Architecture** is a 3-layer agentic operating system designed to execute Google Cloud Delta's 12-week enterprise AI transformations. 

By combining **Hermes Agent** (Monica as Orchestrator), **Expanded Named Squad** (Logan, Ava, Eva, Tyler, Sam, Frank, Peter, Alex), and **GBrain** (durable shared memory substrate), this architecture eliminates context loss, enforces 1-in-1-out scope governance, and provides metric-backed EBITDA value realization for C-suite sponsors.

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

## 👥 The Expanded Named Squad Roster & Roles

1. **Monica (Chief of Staff & Hermes Orchestrator)**: Single front door for user queries, squad orchestration, state machine management (`STATE.md`), and answer synthesis.
2. **Logan (10X Lead: Originate · Innovate · Shape)**: Qualifies high-leverage business opportunities moving client EBITDA.
3. **Ava (AI Activation Lead - AIAL: Govern · De-risk · Expand)**: Owns program governance, executive sign-offs, velocity protection, and risk management.
4. **Eva (Value Lead & Tokenomics Analyst: Size · Model · Quantify)**: Owns 50-sample retrospective audit baselines (`baseline_kpis.json`), EBITDA impact sizing (`ai-value-sizing`), LLM tokenomics, and API cost optimization.
5. **Tyler (Technical Deployment Lead - TDL: Discover · Redesign · Prototype)**: Immerses into client domain, redesigns legacy workflows into agentic pipelines, writes PRDs, builds low-fi prototypes, and designs evaluation criteria.
6. **Sam (Security & InfoSec Specialist: Audit · Harden · Protect)**: STRIDE-A threat matrix modeling (`threat-model-analyst`), InfoSec board clearance, sandbox synthetic data scrubbing (`dummy-dataset`), and AST security checks (`ast-resilient-remediation`).
7. **Frank (Forward-Deployed Engineer - FDE: Build · Integrate · Operate)**: Anchors prototypes in client environment, hardens enterprise integrations (SSO, ETL, IAM), drives TDD, and builds automated evaluation pipelines inside client VPCs.
8. **Peter (Platform Engineer: Productize · Accelerate · Scale)**: Builds "Golden Paths," reusable agent components, and CI/CD observability patterns.
9. **Alex (Agentic Transformation Lead - ATL: Transform · Scale · Enable)**: Drives organizational change management (OCM), staff enablement, and user adoption across client business units.

---

## 🛠️ Step-by-Step Setup & Operational Guide

### 1. Prerequisites & Environment Setup
Ensure your Mac has the required developer tools installed:
```bash
# Node.js (v18+) & Python (3.10+)
node --version
python3 --version

# GitHub CLI & Google Cloud CLI
gh auth status
gcloud auth list
```

### 2. Local Repository & Memory Initialization
Clone the repository and run the automated installer:
```bash
git clone https://github.com/enriquekalven/tdl-hermes-squad.git
cd gbrain-hermes-squad

# Run the 1-step setup script
./scripts/setup.sh
```
This initializes `~/.gbrain/` (with entity subdirectories `people/`, `companies/`, `concepts/`, `ideas/`, `projects/`, `operations/`, `newsletter/`, `STATE.md`, and `baseline_kpis.json`) and installs the `tdl-field-guide`, `gbrain`, `github-integration`, and `gdrive-integration` skills into `~/.hermes/skills/` and `~/.agents/skills/`.

---

## 👔 Leadership Evaluation & Multi-Perspective Review

### 🎯 1. Principal Product Manager (PPM) Perspective
> *"This architecture enforces traditional product management rigor inside an autonomous agentic loop."*
- **Strengths**: Freezes explicit PRD Goals and Non-Goals in Phase 1 before code is written. RICE-driven 1-in-1-out trade-off governance protects sprint commitments.
- **Impact**: Eliminates vague requirements, reduces rework, and provides C-suite metric tracking via `baseline_kpis.json` driven by **Eva**.

### 🛠️ 2. TDL Leadership Perspective
> *"Provides a standardized, state-gated operational machine for managing complex 12-week enterprise transformations."*
- **Strengths**: Replaces unstructured prompts with a deterministic 4-phase state machine (`STATE.md`). Features dynamic capability resolution and automated regression rollbacks (`scripts/rollback.sh`).
- **Impact**: Provides operational leverage, allowing **Tyler (TDL)** to oversee multiple complex client engagements predictably.

### 💻 3. FDE Leadership Perspective
> *"Accelerates engineering velocity while enforcing strict module seam isolation and test-driven quality."*
- **Strengths**: Enforces contract-first API design (`api-and-interface-design`), TDD, and 5-axis PSO code reviews (`code-review-and-quality`). Compiles clean client handoff packets (`shipping-artifacts`).
- **Impact**: **Frank (FDE)** receives clear, non-ambiguous specs, reducing PR churn and ensuring high delivery reliability inside client VPCs.

### 🛡️ 4. Security & InfoSec Leadership Perspective
> *"Proactively clears enterprise security review boards with threat modeling and strict data privacy gates."*
- **Strengths**: **Sam (Security Lead)** executes STRIDE-A threat matrix analysis (`threat-model-analyst`) during Phase 2. Enforces non-production data scrubbing (`dummy-dataset`) and AST static analysis (`ast-resilient-remediation`) to prevent PII/PHI or credential leakage in Argolis/GTM test projects.
- **Impact**: De-risks InfoSec review boards, ensures compliance, and protects customer privacy.
