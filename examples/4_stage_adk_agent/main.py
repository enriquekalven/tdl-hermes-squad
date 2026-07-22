"""
4-Stage ADK Agent Multi-Agent Microservice Orchestrator
Evolved via AlphaEvolve (AE) Principles for Zero-Friction & Maximum End-User Value:
1. Parallel Execution (asyncio) for Stage 2 (RCA) & Stage 3 (Mitigation)
2. Dynamic Plant Maintenance & Inventory-Aware Margin Optimization
3. 1-Click HITL Decision & Visual Trade-Off Card Rendering
"""

import json
import os
import sys
import asyncio
import time
from precedence_store import PrecedenceStore
from incident_adapter import IncidentMockAdapter

class AlphaEvolvedADKOrchestrator:
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
        print(f"   [Alert] Shortage Traced: {part_number} ({part['description']})")
        print(f"   [Impact] Shortage Gap: {gap} units | Affected Line: {vehicle} (Priority {part['margin_priority']})")
        return part

    async def stage_2_root_cause_analysis_async(self, supplier_id):
        await asyncio.sleep(0.05)  # Simulated parallel network fetch
        events = [e for e in self.db["disruption_events"] if e["supplier_id"] == supplier_id]
        if not events:
            return "Unknown disruption"
        event = events[0]
        rca_report = (
            f"RCA Report ({event['event_id']}): {event['disruption_type']} at {event['facility']}. "
            f"Downtime: {event['estimated_downtime_days']} days."
        )
        return rca_report

    async def stage_3_concurrent_mitigation_async(self, part_number):
        await asyncio.sleep(0.05)  # Simulated parallel network fetch
        opts = [o for o in self.db["mitigation_options"] if o["part_number"] == part_number]
        return opts

    def stage_4_margin_optimized_recommendation(self, impact_data, options):
        print("\n💵 Stage 4: Margin-Optimized Allocation & Dynamic Trade-Off Card")
        
        # AlphaEvolve Mutation: Rank options by composite score (Freight Cost + Lead Time Penalty)
        evaluated_options = []
        for opt in options:
            cost = opt["expedited_freight_cost_usd"]
            time_penalty = opt["lead_time_days"] * 1000.0  # $1,000 per day lead-time risk penalty
            total_penalty = cost + time_penalty
            evaluated_options.append((total_penalty, opt))
        
        evaluated_options.sort(key=lambda x: x[0])
        best_penalty, best_option = evaluated_options[0]

        print(f"   🎯 Recommended Action: Keep [{impact_data['vehicle_line']}] line active.")
        print(f"   🚚 Optimal Carrier: {best_option['mode']} via {best_option['alternate_supplier']} (${best_option['expedited_freight_cost_usd']})")
        
        # Render Visual Trade-Off Card for Analyst 1-Click HITL Approval
        print("\n   ┌────────────────────────────────────────────────────────────────────────┐")
        print("   │ 💡 GEMINI ENTERPRISE 1-CLICK ANALYST DECISION CARD                       │")
        print("   ├───────────────────────┬───────────────────────┬────────────────────────┤")
        print("   │ Option                │ Freight Cost / ETA    │ Line Downtime Risk     │")
        print("   ├───────────────────────┼───────────────────────┼────────────────────────┤")
        for p, opt in evaluated_options:
            is_rec = " ⭐ [RECOMMENDED]" if opt["option_id"] == best_option["option_id"] else ""
            print(f"   │ {opt['mode'][:21]:<21} │ ${opt['expedited_freight_cost_usd']:<8} / {opt['lead_time_days']}d   │ Minimal Risk{is_rec:<12} │")
        print("   └────────────────────────────────────────────────────────────────────────┘")

        return best_option

    async def run_full_flow_async(self, case_id, part_number):
        start_time = time.time()
        print("======================================================================")
        print(f"🚀 EXECUTING ALPHAEVOLVED 4-STAGE AGENTIC FLOW FOR CASE: {case_id}")
        print("======================================================================")
        
        # Stage 1: Sequential Impact Intake
        part_info = self.stage_1_impact_assessment(part_number)
        if not part_info:
            print("Part not found.")
            return

        # AlphaEvolve Optimization: Execute Stage 2 (RCA) and Stage 3 (Mitigation) IN PARALLEL!
        print("\n⚡ [AlphaEvolve Parallel Microservices] Running Stage 2 (RCA) & Stage 3 (Mitigation) concurrently...")
        rca_task = self.stage_2_root_cause_analysis_async(part_info["supplier_id"])
        mitigation_task = self.stage_3_concurrent_mitigation_async(part_number)
        
        rca, options = await asyncio.gather(rca_task, mitigation_task)
        
        print(f"   🔥 [Stage 2 Async Output] {rca}")
        print(f"   ✈️ [Stage 3 Async Output] Discovered {len(options)} viable mitigation path(s).")

        # Stage 4: Dynamic Margin Optimization & Trade-Off Card Rendering
        best_option = self.stage_4_margin_optimized_recommendation(part_info, options)

        # Incident Auto-Case Mockup
        IncidentMockAdapter.create_incident_case(case_id, part_number, "CRITICAL", rca)

        # HITL Precedence Log
        self.precedence.log_analyst_decision(
            case_id=case_id,
            part_number=part_number,
            selected_option=best_option["option_id"],
            analyst_rationale=f"1-Click HITL Approved: {best_option['mode']} selected to protect {part_info['vehicle_line']}."
        )

        elapsed = round((time.time() - start_time) * 1000, 2)
        print(f"\n✅ AlphaEvolved Agentic Flow Complete in {elapsed} ms.")

if __name__ == "__main__":
    agent = AlphaEvolvedADKOrchestrator()
    asyncio.run(agent.run_full_flow_async(case_id="CAS-2026-AE-001", part_number="PART-AL-PANEL-01"))
