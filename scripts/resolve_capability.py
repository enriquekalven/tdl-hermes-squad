#!/usr/bin/env python3
"""
Dynamic Capability Slot Resolver for TDL Meta-Skills (Google ADK CLI Suite Edition)
Maps abstract capability slots (#CAPABILITY: Slot) to installed tool skills.
Includes Graceful Fallback Engine if upstream skills are missing.
"""

import sys
import os

CAPABILITY_LOOKUP = {
    "#CAPABILITY: ADK-Workflow": ("google-agents-cli-workflow", "tdl-field-guide"),
    "#CAPABILITY: Customer-Intake": ("workshop-intake", "interview-me"),
    "#CAPABILITY: Scope-Mapping": ("opportunity-solution-tree", "user-stories"),
    "#CAPABILITY: PRD-Creation": ("create-prd", "spec-driven-development"),
    "#CAPABILITY: Scaffolding": ("google-agents-cli-scaffold", "prototype"),
    "#CAPABILITY: Arch-Grilling": ("grill-with-docs", "google-cloud-waf-security"),
    "#CAPABILITY: API-Design": ("api-and-interface-design", "codebase-design"),
    "#CAPABILITY: InfoSec-Threat": ("threat-model-analyst", "agent-governance"),
    "#CAPABILITY: ADK-Code": ("google-agents-cli-adk-code", "test-driven-development"),
    "#CAPABILITY: Task-Breakdown": ("planning-and-task-breakdown", "to-tickets"),
    "#CAPABILITY: TDD": ("test-driven-development", "tdd"),
    "#CAPABILITY: Code-Review": ("code-review-and-quality", "pso-code-quality-reviewer"),
    "#CAPABILITY: Intent-Audit": ("intended-vs-implemented", "code-review"),
    "#CAPABILITY: Agent-Evaluation": ("google-agents-cli-eval", "eval-quality-gate"),
    "#CAPABILITY: Agent-Observability": ("google-agents-cli-observability", "metrics-dashboard"),
    "#CAPABILITY: Release-Deploy": ("shipping-and-launch", "google-agents-cli-deploy"),
    "#CAPABILITY: Registry-Publish": ("google-agents-cli-publish", "shipping-artifacts"),
    "#CAPABILITY: ROI-Sizing": ("ai-value-sizing", "metrics-dashboard"),
    "#CAPABILITY: Handoff-Artifacts": ("shipping-artifacts", "google-agents-cli-publish")
}

HERMES_SKILLS = os.path.expanduser("~/.hermes/skills")
AGENTS_SKILLS = os.path.expanduser("~/.agents/skills")

def check_skill_exists(skill_name):
    path_h = os.path.join(HERMES_SKILLS, skill_name)
    path_a = os.path.join(AGENTS_SKILLS, skill_name)
    return os.path.exists(path_h) or os.path.exists(path_a)

def resolve_slot(slot_name):
    skills = CAPABILITY_LOOKUP.get(slot_name, ("unknown-skill", "default-fallback"))
    primary, fallback = skills[0], skills[1]

    if check_skill_exists(primary):
        resolved = primary
        status = "✅ Primary Skill Installed"
    elif check_skill_exists(fallback):
        resolved = fallback
        status = "⚠️ Fallback Skill Installed"
    else:
        resolved = primary
        status = "ℹ️ Skill Resolution (Native Template Fallback)"

    print(f"🎯 Slot: {slot_name:<30} ➔ Resolved: {resolved:<30} [{status}]")
    return resolved

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Installed Capability Resolution Matrix:\n")
        for slot in CAPABILITY_LOOKUP:
            resolve_slot(slot)
        sys.exit(0)

    slot_query = sys.argv[1]
    resolve_slot(slot_query)
