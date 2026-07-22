# FDE Environment & Data Privacy Matrix

| Environment | Permitted Workload | Data Rule |
| :--- | :--- | :--- |
| **GTM FDE Projects** | Rapid PoCs / Internal EAP | **NO CUSTOMER DEMOS** |
| **Argolis / GCP** | Customer Demo Solutions | **Scrubbed / Synthetic Mocks Only** |
| **go/demos** | Sales & Internal Initiatives | Standardized Demos |
| **Client VPC** | Phase 3 Build & Production | **Real Customer Data Permitted** |

## 🛡️ Data Safeguards
1. **No PII/PHI in Sandbox/Argolis**: Never upload live client datasets into non-production Argolis or GTM test projects.
2. **Synthetic Data Scrubber**: Use `dummy-dataset` to generate synthetic CSV/JSON/SQL test data.
3. **AST Static Checks**: Run `ast-resilient-remediation` to scan code for hardcoded secrets, connection strings, or unscrubbed fields before committing.
