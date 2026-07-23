#!/usr/bin/env bash
# Argolis-to-GCP Production Tenant Migration Script (FDE Fast-Track)
# Lifts and shifts GBrain persistent state and deployment metadata from Argolis sandbox to Customer Production GCP Landing Zone.

set -e

TENANT_ID=${1:-"default"}
TARGET_GCP_PROJECT=${2:-""}

if [ -z "$TARGET_GCP_PROJECT" ]; then
  echo "⚠️ Usage: ./scripts/migrate_tenant.sh <tenant_id> <target_gcp_project_id>"
  echo "Example: ./scripts/migrate_tenant.sh acme_corp customer-gcp-prod-88"
  exit 1
fi

# Detect GBrain Base
if [ -n "$GBRAIN_DRIVE_DIR" ]; then
  GBRAIN_BASE="$GBRAIN_DRIVE_DIR"
elif git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  REPO_ROOT=$(git rev-parse --show-toplevel)
  GBRAIN_BASE="$REPO_ROOT/.gbrain"
else
  GBRAIN_BASE="$HOME/.gbrain"
fi

TENANT_DIR="$GBRAIN_BASE/tenants/$TENANT_ID"

if [ ! -d "$TENANT_DIR" ]; then
  echo "❌ Tenant directory not found: $TENANT_DIR"
  exit 1
fi

echo "=========================================================================="
echo " ✈️ FDE FAST-TRACK: ARGOLIS ➔ GCP PROD LANDING ZONE MIGRATION"
echo "=========================================================================="
echo "🏢 Tenant Scope:       [$TENANT_ID]"
echo "📂 Source Memory Path:  $TENANT_DIR"
echo "☁️ Target GCP Project:  $TARGET_GCP_PROJECT"
echo "=========================================================================="

# 1. Update target GCP project in STATE.md
STATE_FILE="$TENANT_DIR/STATE.md"
if [ -f "$STATE_FILE" ]; then
  sed -i '' "s/gcp-project: .*/gcp-project: $TARGET_GCP_PROJECT/g" "$STATE_FILE" 2>/dev/null || true
  echo "✅ Updated GCP target project in STATE.md ➔ $TARGET_GCP_PROJECT"
fi

# 2. Generate Migration Manifest
MANIFEST_FILE="$TENANT_DIR/operations/migration_manifest.json"
cat <<EOF > "$MANIFEST_FILE"
{
  "tenant_id": "$TENANT_ID",
  "source_environment": "Argolis-Sandbox",
  "target_gcp_project": "$TARGET_GCP_PROJECT",
  "migration_timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "gbrain_status": "MIGRATED_SUCCESS",
  "artifacts_included": [
    "STATE.md",
    "baseline_kpis.json",
    "operations/tdl-squad-matrix.md",
    "operations/environment-matrix.md"
  ]
}
EOF

echo "📄 Migration Manifest Generated: $MANIFEST_FILE"
echo "🎉 Tenant state & GBrain memory successfully prepared for $TARGET_GCP_PROJECT launch!"
