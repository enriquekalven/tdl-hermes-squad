---
name: gdrive-integration
description: Search, read, and sync Google Drive files, Google Docs, and Google Sheets for Monica and specialist agents. Syncs baseline metrics and PRD notes to ~/.gbrain/.
---

# Google Drive & Workspace Integration Skill for Monica

This skill enables Monica (Hermes Chief of Staff) to search, query, and sync Google Drive documents, Google Docs, and Google Sheets.

## 🛠️ Integration Capabilities

### 1. Active Account Context
- Account: `enriq@google.com` (authenticated via Google Cloud CLI `gcloud`).

### 2. Reading Google Docs & Architecture Specs
- Search Google Drive folders for client docs (e.g., `go/welcome-to-delta` or `go/tdl-fde-pm-mindset`).
- Extract document headers, goals, non-goals, and technical requirements.
- Store summary notes under `~/.gbrain/projects/<doc_name>.md`.

### 3. Syncing Baseline Metrics & Sheets
- Read 50-sample retrospective audit sheets.
- Extract `manual_handling_time_mins`, `manual_unit_cost_usd`, and `baseline_error_rate_pct`.
- Update `~/.gbrain/baseline_kpis.json` to recalculate pre/post EBITDA shift.

## 🔄 GBrain Sync Rule
After fetching Google Drive updates, Monica updates `~/.gbrain/STATE.md` with the latest document links, stakeholder sign-offs, and requirement changes.
