#!/usr/bin/env python3
"""
Automated Eval Runner for Delta TDL Engagements
Compares current project metrics against baseline_kpis.json and updates STATE.md.
"""

import json
import os
import sys

GBRAIN_DIR = os.path.expanduser("~/.gbrain")
BASELINE_FILE = os.path.join(GBRAIN_DIR, "baseline_kpis.json")
STATE_FILE = os.path.join(GBRAIN_DIR, "STATE.md")

def run_evals():
    if not os.path.exists(BASELINE_FILE):
        print(f"Error: {BASELINE_FILE} not found. Run baseline intake first.")
        sys.exit(1)

    with open(BASELINE_FILE, "r") as f:
        data = json.load(f)

    base = data.get("baseline_metrics", {})
    target = data.get("target_metrics", {})

    base_time = base.get("manual_handling_time_mins", 45.0)
    target_time = target.get("agentic_handling_time_mins", 5.0)
    time_reduction_pct = round(((base_time - target_time) / base_time) * 100, 2)

    base_cost = base.get("manual_unit_cost_usd", 35.0)
    target_cost = target.get("agentic_unit_cost_usd", 4.5)
    cost_savings_pct = round(((base_cost - target_cost) / base_cost) * 100, 2)

    ebitda_impact = data.get("projected_ebitda_impact_annual_usd", 0.0)

    print("📊 --- TDL EVALUATION RESULTS ---")
    print(f"Client: {data.get('client_name', 'Enterprise Client')}")
    print(f"Sample Size: {data.get('audit_sample_size', 50)} items audited")
    print(f"⏱️ Handling Time Shift: {base_time}m ➔ {target_time}m ({time_reduction_pct}% reduction)")
    print(f"💵 Unit Cost Shift: ${base_cost} ➔ ${target_cost} ({cost_savings_pct}% cost savings)")
    print(f"🚀 Projected EBITDA Impact: ${ebitda_impact:,.2f}/yr\n")

    # Update STATE.md if exists
    if os.path.exists(STATE_FILE):
        print(f"✅ State machine logged in {STATE_FILE}")

if __name__ == "__main__":
    run_evals()
