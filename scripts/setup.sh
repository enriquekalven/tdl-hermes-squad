#!/usr/bin/env bash
# Quick Installer for Delta TDL Squad (GBrain + Hermes Agent)
# Supports Multi-Tenant Namespace Isolation

set -e

TENANT_ID=${1:-"default"}
GBRAIN_TENANT_DIR="$HOME/.gbrain/tenants/$TENANT_ID"

echo "🚀 Setting up Delta TDL Squad (GBrain + Hermes Agent)..."
echo "🏢 Tenant Namespace: $TENANT_ID ($GBRAIN_TENANT_DIR)"

# 1. Create Multi-Tenant GBrain directory structure
mkdir -p "$GBRAIN_TENANT_DIR"/{people,companies,concepts,ideas,projects,operations,newsletter}
mkdir -p "$HOME/.gbrain"

# Create symlink or active tenant file pointer
echo "$TENANT_ID" > "$HOME/.gbrain/active_tenant"
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

# 4. Install TDL skills (gbrain & tdl-field-guide, github, gdrive)
cp -R skills/gbrain ~/.hermes/skills/
cp -R skills/gbrain ~/.agents/skills/

mkdir -p skills/tdl-field-guide
cp -R skills/tdl-field-guide ~/.hermes/skills/
cp -R skills/tdl-field-guide ~/.agents/skills/

if [ -d skills/github-integration ]; then
  cp -R skills/github-integration ~/.hermes/skills/
  cp -R skills/github-integration ~/.agents/skills/
fi

if [ -d skills/gdrive-integration ]; then
  cp -R skills/gdrive-integration ~/.hermes/skills/
  cp -R skills/gdrive-integration ~/.agents/skills/
fi

echo "✅ Installed gbrain and tdl-field-guide skills in ~/.hermes/skills/ and ~/.agents/skills/."
echo "🎉 TDL Squad (GBrain + Hermes Agent) setup complete!"
echo "Check $GBRAIN_TENANT_DIR/STATE.md to track your 12-week engagement."
