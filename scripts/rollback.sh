#!/usr/bin/env bash
# Automated State & Code Rollback Script for TDL Engagements

set -e

TARGET_PHASE=${1:-"PHASE_2"}
STATE_FILE="$HOME/.gbrain/STATE.md"

echo "⚠️ Initiating automated TDL State Rollback to $TARGET_PHASE..."

# 1. Create a rollback tag in git if inside a repo
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  TAG_NAME="rollback-$(date +%Y%m%d-%H%M%S)"
  git tag "$TAG_NAME"
  echo "🏷️ Created git rollback checkpoint tag: $TAG_NAME"
fi

# 2. Append regression trigger to STATE.md
if [ -f "$STATE_FILE" ]; then
  echo "" >> "$STATE_FILE"
  echo "### 🔄 REGRESSION TRIGGER AT $(date)" >> "$STATE_FILE"
  echo "ACTION: ROLLBACK_TO_${TARGET_PHASE} - Intent audit exposed architectural drift." >> "$STATE_FILE"
  echo "✅ Updated $STATE_FILE with regression trigger."
fi

echo "🎉 Rollback checkpoint recorded. Current state set to $TARGET_PHASE."
