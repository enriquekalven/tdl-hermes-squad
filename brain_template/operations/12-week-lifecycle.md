# The 12-Week Agentic Transformation Lifecycle

Delta engagements execute against a strict 12-week production gate with dynamic state regression loops.

```
Phase 1: Discover & Define ──► Phase 2: Prototype & Validate ──► Phase 3: Production Build ──► Phase 4: Harden & Launch
   (Weeks 0-2 | TDL-Led)            (Weeks 3-6 | TDL+FDE)            (Weeks 6-10 | FDE-Led)          (Weeks 11-12 | Full Squad)
```

## 📅 Lifecycle Phases

### Phase 1: Discover & Define (Weeks 0-2)
- **Focus**: Domain immersion, process mapping, data access validation, framing problem statements.
- **Key Deliverables**:
  - `baseline_kpis.json` (50-sample retrospective audit of manual time/cost/error baseline).
  - Frozen PRD with explicit Goals and Non-Goals (`create-prd`).

### Phase 2: Prototype & Validate (Weeks 3-6)
- **Focus**: Low-fidelity prototype, SME validation, architecture design, InfoSec board prep.
- **Key Deliverables**:
  - Architecture Grilling & ADR generation (`grill-with-docs`).
  - Contract-first API design (`api-and-interface-design`).
  - STRIDE-A Threat Matrix (`threat-model-analyst`).

### Phase 3: Production Build (Weeks 6-10)
- **Focus**: Production code, enterprise security hardening, automated evaluation pipelines.
- **Key Governance Rules**:
  - **Strict '1-In, 1-Out' Trade-off Rule**: Mid-flight feature requests require ejecting an equal-effort RICE item or shifting to Post-Week 12 Expansion.
  - **Intent Audit & Rollback Trigger**: Run `intended-vs-implemented`. If architectural flaws exist, write `ACTION: ROLLBACK_TO_PHASE_2` in `STATE.md`.
  - **Data Privacy Gate**: Customer PII/PHI scrubbing enforced via `dummy-dataset` and static AST checks (`ast-resilient-remediation`).

### Phase 4: Harden & Launch (Weeks 11-12)
- **Focus**: Load testing, user adoption training, handoff documentation, GTM expansion.
- **Key Deliverables**:
  - Eval-on-Commit regression test suites (`google-agents-cli-eval`).
  - Production launch manifests and rollback plans (`shipping-and-launch`).
  - Pre/Post EBITDA ROI sizing (`ai-value-sizing`).
  - Client handoff packet (`shipping-artifacts`).
