#!/usr/bin/env bash
# Quick Installer for Delta TDL Squad (GBrain + Hermes Agent)
# Google Shared Drive & Environment Variable Edition

set -e

# Load .env file if present in working directory
if [ -f ".env" ]; then
  export $(grep -v '^#' .env | xargs)
fi

TENANT_ID=${1:-${GBRAIN_TENANT:-"default"}}
CUSTOM_PATH=$2

# Detect Storage Location:
# 1. Custom CLI path ($2)
# 2. Environment Variable ($GBRAIN_DRIVE_DIR)
# 3. Git Repo (.gbrain)
# 4. Home directory (~/.gbrain)
if [ -n "$CUSTOM_PATH" ]; then
  GBRAIN_BASE="$CUSTOM_PATH"
  echo "📁 Using Custom CLI Path: $GBRAIN_BASE"
elif [ -n "$GBRAIN_DRIVE_DIR" ]; then
  GBRAIN_BASE="$GBRAIN_DRIVE_DIR"
  echo "📁 Using Google Shared Drive (GBRAIN_DRIVE_DIR): $GBRAIN_BASE"
elif git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  REPO_ROOT=$(git rev-parse --show-toplevel)
  GBRAIN_BASE="$REPO_ROOT/.gbrain"
  echo "📂 Git Repository Detected: Using In-Repo Shared GBrain at $GBRAIN_BASE"
else
  GBRAIN_BASE="$HOME/.gbrain"
  echo "🏠 Using Local Home GBrain at $GBRAIN_BASE"
fi

GBRAIN_TENANT_DIR="$GBRAIN_BASE/tenants/$TENANT_ID"

echo "🚀 Setting up Delta TDL Squad (GBrain + Hermes Agent)..."
echo "🏢 Tenant Namespace: $TENANT_ID ($GBRAIN_TENANT_DIR)"

# 1. Create GBrain directory structure
mkdir -p "$GBRAIN_TENANT_DIR"/{people,companies,concepts,ideas,projects,operations,newsletter}
mkdir -p "$GBRAIN_BASE"

# Set active tenant pointer
echo "$TENANT_ID" > "$GBRAIN_BASE/active_tenant"
echo "✅ Active tenant set to '$TENANT_ID'."

# 2. Copy template state, baseline, and SOP files if not exist
if [ ! -f "$GBRAIN_TENANT_DIR/STATE.md" ]; then
  cp brain_template/STATE.md "$GBRAIN_TENANT_DIR/"
fi

if [ ! -f "$GBRAIN_TENANT_DIR/baseline_kpis.json" ]; then
  cp brain_template/baseline_kpis.json "$GBRAIN_TENANT_DIR/"
fi

if [ ! -f "$GBRAIN_TENANT_DIR/README.md" ]; then
  cp brain_template/README.md "$GBRAIN_TENANT_DIR/"
fi

cp brain_template/operations/*.md "$GBRAIN_TENANT_DIR/operations/"
echo "✅ Initialized TDL squad matrix, 12-week lifecycle, and environment SOPs in tenant scope."

# 3. Create Hermes and Agent skills directories
mkdir -p ~/.hermes/skills ~/.agents/skills

# 4. Install TDL skills
cp -R skills/gbrain ~/.hermes/skills/
cp -R skills/gbrain ~/.agents/skills/

mkdir -p skills/tdl-field-guide
cp -R skills/tdl-field-guide ~/.hermes/skills/
cp -R skills/tdl-field-guide ~/.agents/skills/

echo "✅ Installed gbrain and tdl-field-guide skills in ~/.hermes/skills/ and ~/.agents/skills/."
echo "🎉 TDL Squad (GBrain + Hermes Agent) setup complete!"
echo "Check $GBRAIN_TENANT_DIR/STATE.md to track your 12-week engagement."
