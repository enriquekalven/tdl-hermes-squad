# GBrain: Shared Knowledge Substrate Template

`GBrain` is a durable, structured knowledge store for Hermes Agent and specialist subagents. It organizes context into entity-based collections so knowledge compounds over time across research, engineering, content, and strategic planning.

## 📂 Directory Taxonomy

- `people/`: Profiles, key contacts, domain experts, team members, background notes.
- `companies/`: Company breakdowns, tech stacks, market research, competitor profiles.
- `concepts/`: Technical terms, architectural patterns, frameworks, research concepts.
- `ideas/`: Content ideas, product concepts, experiment hypotheses, feature angles.
- `projects/`: Project specs, repository notes, architecture decisions, release plans.
- `operations/`: Workflow SOPs, daily execution checklists, agent routines.
- `newsletter/`: Newsletter issues, performance metrics, audience feedback, top signals.

## 🔄 Read-First / Write-Back Rule

1. **Read-First**: Before executing a research or content task, agents query `~/.gbrain/` to retrieve existing facts.
2. **Write-Back**: When new high-signal information is discovered, agents capture it in the appropriate `~/.gbrain/<collection>/<filename>.md` document.
