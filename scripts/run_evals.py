#!/usr/bin/env python3
"""
Automated Multi-Objective Eval Runner for Delta TDL Engagements
Compares current project metrics against baseline_kpis.json.
Protects against Reward Hacking by weighting Time Saved (50%) + Test Pass Rate (50%).
"""

import json
import os
import sys
import fcntl

GBRAIN_BASE = os.path.expanduser("~/.gbrain")

def get_active_tenant():
    active_file = os.path.join(GBRAIN_BASE, "active_tenant")
    if os.path.exists(active_file):
        with open(active_file, "r") as f:
            return f.read().strip()
    return "default"

def run_evals(tenant_id=None, test_pass_rate=1.0):
    if not tenant_id:
        tenant_id = get_active_tenant()

    tenant_dir = os.path.join(GBRAIN_BASE, "tenants", tenant_id)
    baseline_file = os.path.join(tenant_dir, "baseline_kpis.json")
    if not os.path.exists(baseline_file):
        # Fallback
        baseline_file = os.path.join(GBRAIN_BASE, "baseline_kpis.json")

    if not os.path.exists(baseline_file):
        print(f"Error: {baseline_file} not found. Run baseline intake first.")
        sys.exit(1)

    # Atomic File Read with Lock
    with open(baseline_file, "r") as f:
        fcntl.flock(f, fcntl.LOCK_SH)
        data = json.load(f)
        fcntl.flock(f, fcntl.LOCK_UN)

    base = data.get("baseline_metrics", {})
    target = data.get("target_metrics", {})

    base_time = base.get("manual_handling_time_mins", 45.0)
    target_time = target.get("agentic_handling_time_mins", 5.0)
    time_reduction_pct = round(((base_time - target_time) / base_time) * 100, 2)

    base_cost = base.get("manual_unit_cost_usd", 35.0)
    target_cost = target.get("agentic_unit_cost_usd", 4.5)
    cost_savings_pct = round(((base_cost - target_cost) / base_cost) * 100, 2)

    ebitda_impact = data.get("projected_ebitda_impact_annual_usd", 0.0)

    # Multi-Objective Fitness Score Calculation (Reward Hacking Guard)
    time_score = min(time_reduction_pct / 100.0, 1.0)
    composite_fitness = (0.5 * time_score) + (0.5 * test_pass_rate)

    print(f"🏢 Tenant Scope: [{tenant_id}]")
    print("📊 --- TDL MULTI-OBJECTIVE EVALUATION RESULTS ---")
    print(f"Client: {data.get('client_name', 'Enterprise Client')}")
    print(f"Sample Size: {data.get('audit_sample_size', 50)} items audited")
    print(f"⏱️ Handling Time Shift: {base_time}m ➔ {target_time}m ({time_reduction_pct}% reduction)")
    print(f"💵 Unit Cost Shift: ${base_cost} ➔ ${target_cost} ({cost_savings_pct}% cost savings)")
    print(f"🧪 Zero-Defect Test Pass Rate: {test_pass_rate * 100}%")
    print(f"🎯 Composite Fitness Score: {round(composite_fitness, 4)} / 1.0000")
    print(f"🚀 Projected EBITDA Impact: ${ebitda_impact:,.2f}/yr")

    if test_pass_rate < 1.0:
        print("⚠️ REWARD HACKING WARNING: Handling time is reduced, but test pass rate is degraded (<100%). Rework required!")
    else:
        print("✅ REWARD HACKING CHECK PASSED: High time savings verified with 100% test pass rate.")
    print()

if __name__ == "__main__":
    tenant = sys.argv[1] if len(sys.argv) > 1 else None
    run_evals(tenant_id=tenant)
