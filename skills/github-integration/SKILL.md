---
name: github-integration
description: Query and track GitHub repositories, pull requests, issues, and commit activity for Monica and specialist agents. Syncs repo progress to ~/.gbrain/projects/.
---

# GitHub Integration Skill for Monica

This skill enables Monica (Hermes Chief of Staff) and specialist agents to interact with local and remote GitHub repositories.

## 🛠️ Commands & Capabilities

### 1. Track Pull Requests & Code Reviews
```bash
# List open PRs for a repository
gh pr list --repo <owner/repo>

# Inspect PR diffs and changes
gh pr diff <pr_number> --repo <owner/repo>

# View PR details and checks
gh pr view <pr_number> --repo <owner/repo>
```

### 2. Track Issues & Backlog Sprints
```bash
# List active sprint issues
gh issue list --repo <owner/repo> --state open

# View issue details
gh issue view <issue_number> --repo <owner/repo>
```

### 3. Track Commit Progress & Releases
```bash
# View recent release tags
gh release list --repo <owner/repo>

# View repository summary
gh repo view <owner/repo>
```

## 🔄 GBrain Sync Rule
When Monica inspects a repository's progress, she automatically updates `~/.gbrain/projects/<repo_name>.md` with current PR status, active sprint blockers, and recent release tags.
