# Environment SOP: Argolis Sandbox to GCP Production Landing Zone

This SOP governs environment management for Technical Deployment Leads (TDLs) and Forward Deployed Engineers (FDEs).

---

## 🚀 Environment Progression Architecture

```
┌─────────────────────────────────────────┐       ┌─────────────────────────────────────────┐
│ 1. ARGOLIS DEMO SANDBOX                 │ ────► │ 2. CUSTOMER GCP PRODUCTION LANDING ZONE │
│ Quick prototyping & EAP testing         │       │ Secured, IAM hardened, VPC SC protected │
│ Project ID: argolis-sandbox-xxx         │       │ Project ID: customer-gcp-prod-xxx       │
└─────────────────────────────────────────┘       └─────────────────────────────────────────┘
```

---

## 🛠️ Argolis-to-Production Migration Workflow

1. **Phase 1-2 (Argolis Sandbox Rapid Prototyping)**:
   - Build agent tools and prototypes in Google Argolis or developer sandbox.
   - Store architecture decisions and baseline metrics in GBrain (`.gbrain/tenants/<tenant_id>/`).

2. **Phase 3 Handover (Automated Shift)**:
   - Run the FDE migration script to transfer GBrain state and update GCP landing zone targets:
     ```bash
     ./scripts/migrate_tenant.sh acme_corp customer-gcp-prod-88
     ```
   - Deploy ADK agent container to Customer GCP Cloud Run via `google-agents-cli-deploy`.
   - Publish to Client Gemini Enterprise Agent Registry via `google-agents-cli-publish`.

---

## 🔒 Security & Data Privacy Rules

- **Zero PII in Argolis**: Only anonymized dummy data (`dummy-dataset`) may enter Argolis sandboxes.
- **Client VPC Isolation**: Real customer database connections are established *only* after deploying to the Customer GCP Production Landing Zone.
