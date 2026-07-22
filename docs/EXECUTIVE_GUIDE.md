# 📘 Google Cloud Delta: Hermes TDL Chief of Staff ("Monica") & GBrain User Guide

**Author**: Enrique Chan (Technical Deployment Lead, Google Cloud Delta /Forward)  
**Target Audience**: Delta TDLs, FDEs, Product Managers, Security Engineers, and Engineering Leadership  
**Status**: Active Operational Standard  

---

## 📌 Executive Summary

The **Hermes TDL Chief of Staff ("Monica") + GBrain Architecture** is a 3-layer agentic operating system designed to execute Google Cloud Delta's 12-week enterprise AI transformations. 

By combining **Hermes Agent** (Monica as Orchestrator), an **Expanded Squad Matrix** (Tier 1 Core + Tier 2 Extended Specialists), and **GBrain** (durable shared memory substrate), this architecture eliminates context loss, enforces 1-in-1-out scope governance, and provides metric-backed EBITDA value realization for C-suite sponsors.

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

## 👥 The Named Squad Roster (Tier 1 & Tier 2)

### 🔹 Tier 1 Core Squad
1. **Monica (Chief of Staff & Hermes Orchestrator)**: Single front door for user queries, state machine management (`STATE.md`), and answer synthesis.
2. **Logan (10X Lead: Originate · Innovate · Shape)**: Qualifies high-leverage business opportunities moving client EBITDA.
3. **Ava (AI Activation Lead - AIAL: Govern · De-risk · Expand)**: Owns program governance, executive sign-offs, velocity protection, and risk management.
4. **Eva (Value Lead & Tokenomics Analyst: Size · Model · Quantify)**: Owns 50-sample retrospective audit baselines (`baseline_kpis.json`), EBITDA impact sizing (`ai-value-sizing`), LLM tokenomics, and API cost optimization.
5. **Tyler (Technical Deployment Lead - TDL: Discover · Redesign · Prototype)**: Immerses into client domain, redesigns legacy workflows into agentic pipelines, writes PRDs, builds low-fi prototypes, and designs evaluation criteria.
6. **Sam (Security & InfoSec Specialist: Audit · Harden · Protect)**: STRIDE-A threat matrix modeling (`threat-model-analyst`), InfoSec board clearance, sandbox synthetic data scrubbing (`dummy-dataset`), and AST security checks (`ast-resilient-remediation`).
7. **Frank (Forward-Deployed Engineer - FDE: Build · Integrate · Operate)**: Anchors prototypes in client environment, hardens enterprise integrations (SSO, ETL, IAM), drives TDD, and builds automated evaluation pipelines inside client VPCs.
8. **Peter (Platform Engineer: Productize · Accelerate · Scale)**: Builds "Golden Paths," reusable agent components, and CI/CD observability patterns.
9. **Alex (Agentic Transformation Lead - ATL: Transform · Scale · Enable)**: Drives organizational change management (OCM), staff enablement, and user adoption across client business units.

### 🔸 Tier 2 Extended Specialists
10. **Dara (Data & Analytics Specialist)**: BigQuery SQL validation (`sql-queries`), Cloud Trace observability (`google-agents-cli-observability`), cohort analytics (`ab-test-analysis`).
11. **Devin (DevOps & Release Operations Specialist)**: Cloud Run / GKE deployment (`google-agents-cli-deploy`), Gemini Enterprise registry publishing (`google-agents-cli-publish`), release notes (`release-notes`).
12. **Clara (Cloud WAF & Governance Specialist)**: GCP Well-Architected Framework reviews (`google-cloud-waf-security`), policy access control arrays (`agent-governance`).
13. **Rory (Agile Story & User Research Lead)**: Stakeholder alignment interrogation (`interview-me`), INVEST user/job stories (`user-stories`), retrospectives (`retro`).

---

## 🛠️ Step-by-Step Setup & Operational Guide

### ⚡ 1. Zero-Install Quick Start (10 Seconds)
Install the `tdl-field-guide` master meta-skill into your agent environment (Antigravity, Cursor, Claude Code, or Hermes CLI):
```bash
npx skills add enriquekalven/tdl-hermes-squad
```

### 🏢 2. Multi-Tenant Workspace Setup
Clone the repository and initialize a tenant-isolated workspace (e.g. `ford` or `intel`):
```bash
git clone https://github.com/enriquekalven/tdl-hermes-squad.git
cd tdl-hermes-squad

# Initialize tenant workspace scope
./scripts/setup.sh ford
```
This initializes `~/.gbrain/tenants/ford/` (with entity subdirectories `people/`, `companies/`, `concepts/`, `ideas/`, `projects/`, `operations/`, `STATE.md`, and `baseline_kpis.json`).

---

## 🔬 AlphaEvolve Resilience & Hardening Engine

1. **Multi-Tenant Namespace Isolation**: Prevents context bleeding between different customer accounts via `~/.gbrain/tenants/<tenant_id>/`.
2. **Reward Hacking Prevention**: Multi-objective fitness scoring in `scripts/run_evals.py` pairs handling time reduction (50%) with zero-defect TDD test pass rates (50%).
3. **Atomic State Concurrency**: File-locking (`fcntl.flock`) on `STATE.md` prevents race conditions during parallel subagent execution.
4. **Graceful Capability Fallback Engine**: `scripts/resolve_capability.py` falls back gracefully to local native templates if upstream skills fail.

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
- **Strengths**: **Sam (Security Lead)** & **Clara (Cloud WAF)** execute STRIDE-A threat matrix analysis (`threat-model-analyst`) during Phase 2. Enforces non-production data scrubbing (`dummy-dataset`) and AST static analysis (`ast-resilient-remediation`) to prevent PII/PHI or credential leakage.
- **Impact**: De-risks InfoSec review boards, ensures compliance, and protects customer privacy.
