---
name: gbrain
description: Query and write durable, structured context to the GBrain shared knowledge store (~/.gbrain/). Always read before starting tasks and write back new insights, STATE.md state machine status, and baseline metrics.
---

# GBrain Knowledge Management Skill (TDL Squad Edition)

This skill allows Hermes Agent and specialist agents to interact with `GBrain`, a structured, persistent knowledge substrate located at `~/.gbrain/`.

## 📁 GBrain Directory Schema

- `~/.gbrain/STATE.md`: Active 12-week operational state machine & phase gate log.
- `~/.gbrain/baseline_kpis.json`: Synthetic baseline metrics (50-sample retrospective audit).
- `~/.gbrain/people/`: Information on people, contacts, background.
- `~/.gbrain/companies/`: Company profiles, tech stacks, market research.
- `~/.gbrain/concepts/`: Technical terms, architectural patterns, frameworks.
- `~/.gbrain/ideas/`: Content ideas, product concepts, experiment hypotheses.
- `~/.gbrain/projects/`: Project specs, repository notes, architecture decisions.
- `~/.gbrain/operations/`: SOPs, execution checklists, 6-role squad matrix, env matrix.
- `~/.gbrain/newsletter/`: Newsletter issues, performance metrics, top signals.

## 📖 Standard Operating Procedure

### 1. Read-First Phase (Before starting work)
Before researching a topic, creating content, or writing code:
- Check `~/.gbrain/STATE.md` to identify the current 12-week Phase (Phase 1 to 4).
- Search `~/.gbrain/` for existing entity files matching the target.
- If a relevant file exists, read it first to avoid re-researching stored facts.

### 2. Write-Back Phase (After discovering high-signal insights)
After completing research or analysis:
- Create or update the relevant markdown file under `~/.gbrain/<category>/<entity-slug>.md`.
- Update `~/.gbrain/STATE.md` phase checkboxes and metrics when milestones are completed.
- If an architectural intent audit fails, append `ACTION: ROLLBACK_TO_PHASE_2` in `~/.gbrain/STATE.md`.
