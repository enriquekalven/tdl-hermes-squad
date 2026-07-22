#!/usr/bin/env bash
# Quick Installer for TDL Squad (GBrain + Hermes Agent)

set -e

echo "🚀 Setting up Delta TDL Squad (GBrain + Hermes Agent)..."

# 1. Create GBrain directory structure
mkdir -p ~/.gbrain/{people,companies,concepts,ideas,projects,operations,newsletter}
echo "✅ Initialized ~/.gbrain/ directory taxonomy."

# 2. Copy template state, baseline, and SOP files if not exist
if [ ! -f ~/.gbrain/STATE.md ]; then
  cp brain_template/STATE.md ~/.gbrain/
fi

if [ ! -f ~/.gbrain/baseline_kpis.json ]; then
  cp brain_template/baseline_kpis.json ~/.gbrain/
fi

if [ ! -f ~/.gbrain/README.md ]; then
  cp brain_template/README.md ~/.gbrain/
fi

cp brain_template/operations/*.md ~/.gbrain/operations/
echo "✅ Initialized TDL squad matrix, 12-week lifecycle, and environment SOPs."

# 3. Create Hermes and Agent skills directories
mkdir -p ~/.hermes/skills ~/.agents/skills

# 4. Install TDL skills (gbrain & tdl-field-guide)
cp -R skills/gbrain ~/.hermes/skills/
cp -R skills/gbrain ~/.agents/skills/

mkdir -p skills/tdl-field-guide
cp -R skills/tdl-field-guide ~/.hermes/skills/
cp -R skills/tdl-field-guide ~/.agents/skills/

echo "✅ Installed gbrain and tdl-field-guide skills in ~/.hermes/skills/ and ~/.agents/skills/."

echo "🎉 TDL Squad (GBrain + Hermes Agent) setup complete!"
echo "Check ~/.gbrain/STATE.md to track your 12-week engagement."
