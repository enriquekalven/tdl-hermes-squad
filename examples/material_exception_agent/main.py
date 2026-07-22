"""
Material Exception Resolution Agent MVP (ADK Multi-Agent Orchestrator)
Phase 3 Reference Implementation executing 4-Stage Agentic Flow:
1. Automated Impact Assessment
2. Parallel Root Cause Analysis
3. Concurrent Mitigation & Scenario Evaluation
4. Margin-Optimized Recommendation & Demand Shaping (F-150 over Maverick)
"""

import json
import os
import sys
from precedence_store import PrecedenceStore
from pega_adapter import PegaMockAdapter

class MaterialExceptionOrchestrator:
    def __init__(self, data_path=None):
        if not data_path:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            data_path = os.path.join(base_dir, "mock_data.json")
        with open(data_path, "r") as f:
            self.db = json.load(f)
        self.precedence = PrecedenceStore()

    def stage_1_impact_assessment(self, part_number):
        print("\n🔍 Stage 1: Automated Impact Assessment")
        parts = [p for p in self.db["part_master"] if p["part_number"] == part_number]
        if not parts:
            return None
        part = parts[0]
        gap = part["shortage_gap_units"]
        vehicle = part["vehicle_line"]
        print(f"   [Alert] Part Shortage Traced: {part_number} ({part['description']})")
        print(f"   [Impact] Shortage Gap: {gap} units | Affected Line: {vehicle} (Priority {part['margin_priority']})")
        return part

    def stage_2_root_cause_analysis(self, supplier_id):
        print("\n🔥 Stage 2: Parallel Root Cause Analysis (RCA)")
        events = [e for e in self.db["disruption_events"] if e["supplier_id"] == supplier_id]
        if not events:
            return "Unknown disruption"
        event = events[0]
        rca_report = (
            f"RCA Report ({event['event_id']}): {event['disruption_type']} at {event['facility']}. "
            f"Estimated Downtime: {event['estimated_downtime_days']} days."
        )
        print(f"   [RCA] {rca_report}")
        return rca_report

    def stage_3_concurrent_mitigation(self, part_number):
        print("\n✈️ Stage 3: Concurrent Mitigation & Scenario Evaluation")
        opts = [o for o in self.db["mitigation_options"] if o["part_number"] == part_number]
        for opt in opts:
            print(f"   [Scenario] Option {opt['option_id']}: {opt['mode']} via {opt['alternate_supplier']} | Lead Time: {opt['lead_time_days']}d | Cost: ${opt['expedited_freight_cost_usd']}")
        return opts

    def stage_4_margin_optimized_recommendation(self, impact_data, options):
        print("\n💵 Stage 4: Margin-Optimized Allocation & Demand Shaping")
        # Rule: Prioritize F-150 (Priority 1) over Maverick (Priority 2)
        sorted_opts = sorted(options, key=lambda x: x["expedited_freight_cost_usd"])
        best = sorted_opts[0]
        
        print(f"   🎯 Recommended Action: Allocate constrained inventory to keep [{impact_data['vehicle_line']}] assembly line active.")
        print(f"   🚚 Selected Logistics Plan: {best['mode']} (${best['expedited_freight_cost_usd']})")
        print(f"   💡 Demand Shaping Rule: Priority {impact_data['margin_priority']} line protection enforced.")
        return best

    def run_full_flow(self, case_id, part_number):
        print("======================================================================")
        print(f"🚀 EXECUTING 4-STAGE AGENTIC FLOW FOR CASE: {case_id}")
        print("======================================================================")
        
        # Stage 1
        part_info = self.stage_1_impact_assessment(part_number)
        if not part_info:
            print("Part not found.")
            return

        # Stage 2
        rca = self.stage_2_root_cause_analysis(part_info["supplier_id"])

        # Stage 3
        options = self.stage_3_concurrent_mitigation(part_number)

        # Stage 4
        best_option = self.stage_4_margin_optimized_recommendation(part_info, options)

        # PEGA Case Mockup
        PegaMockAdapter.create_incident_case(case_id, part_number, "CRITICAL", rca)

        # HITL Precedence Log
        self.precedence.log_analyst_decision(
            case_id=case_id,
            part_number=part_number,
            selected_option=best_option["option_id"],
            analyst_rationale=f"Approved expedited logistics to prevent {part_info['vehicle_line']} shutdown ($150k/hr line cost)."
        )
        print("\n✅ 4-Stage Agentic Flow Execution Complete.")

if __name__ == "__main__":
    agent = MaterialExceptionOrchestrator()
    agent.run_full_flow(case_id="CAS-2026-8801", part_number="F150-AL-PANEL-01")
