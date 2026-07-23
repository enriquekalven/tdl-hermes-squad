# Operation: Hermes Functional Delivery SOP

## 🛠️ Execution Scopes & Responsibilities

1. **Monica (Chief of Staff / Orchestrator)**:
   - Front door for all user queries.
   - Manages 12-week state machine (`STATE.md`) and GBrain memory.
   - Dispatches tasks to 3 functional scopes (Architect, Builder, Reviewer).

2. **ARCHITECT Scope (Scoping & Design)**:
   - Discovery intake, PRD goal/non-goal freezing (`create-prd`), ADRs, API boundaries.

3. **BUILDER Scope (Engineering & Deployment)**:
   - ADK scaffolding (`google-agents-cli-scaffold`), ADK Python microservices (`google-agents-cli-adk-code`), TDD unit tests, Cloud Run deployment.

4. **REVIEWER Scope (Security, Evals & Quality Gates)**:
   - STRIDE-A threat matrix modeling (`threat-model-analyst`), 5-axis code quality reviews (`code-review-and-quality`), intent audits (`intended-vs-implemented`), eval quality flywheel (`google-agents-cli-eval`).
