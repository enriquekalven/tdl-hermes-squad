#!/usr/bin/env python3
"""
🛡️ Hermes TDL Interactive Console (AlphaEvolved Edition)
Zero-friction interactive terminal environment for Technical Deployment Leads (TDLs).
Orchestrates Monica (Chief of Staff) and the 8-Role Squad Matrix across Phases 1 to 4.
"""

import sys
import os
import subprocess

GBRAIN_BASE = os.path.expanduser("~/.gbrain")

def get_active_tenant():
    active_file = os.path.join(GBRAIN_BASE, "active_tenant")
    if os.path.exists(active_file):
        with open(active_file, "r") as f:
            return f.read().strip()
    return "default"

def print_banner():
    tenant = get_active_tenant()
    print("==========================================================================")
    print(" 🛡️  HERMES TDL SQUAD INTERACTIVE OPERATING CONSOLE (AlphaEvolved v2.0)")
    print(f" 🏢 Active Tenant Scope: [{tenant}] ({os.path.join(GBRAIN_BASE, 'tenants', tenant)})")
    print(" 🧠 Orchestrator: Monica (Chief of Staff)")
    print("==========================================================================")

def show_menu():
    print("\nSelect an operational action:\n")
    print("  [1] 📋 View Active 12-Week State Machine (Monica)")
    print("  [2] 🔍 Search GBrain Memory Substrate (Multi-Tenant)")
    print("  [3] 📊 Run Multi-Objective EBITDA & Quality Evals (Eva)")
    print("  [4] 🎯 Resolve Dynamic Capability Slot (Tyler)")
    print("  [5] 🏢 Switch / Initialize Tenant Scope (setup.sh)")
    print("  [6] ⚠️ Trigger Automated State Checkpoint Rollback")
    print("  [0] 🚪 Exit Console\n")

def run_action(choice):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tenant = get_active_tenant()
    tenant_dir = os.path.join(GBRAIN_BASE, "tenants", tenant)

    if choice == "1":
        state_file = os.path.join(tenant_dir, "STATE.md")
        if os.path.exists(state_file):
            print(f"\n📄 Current State Machine ({state_file}):\n")
            with open(state_file, "r") as f:
                print(f.read()[:800])
        else:
            print(f"\n⚠️ State file not found for tenant [{tenant}]. Run [5] to initialize.")

    elif choice == "2":
        query = input("🔍 Enter search query for GBrain: ").strip()
        if query:
            cmd = [sys.executable, os.path.join(base_dir, "search_brain.py"), query, "--tenant", tenant]
            subprocess.run(cmd)

    elif choice == "3":
        cmd = [sys.executable, os.path.join(base_dir, "run_evals.py"), tenant]
        subprocess.run(cmd)

    elif choice == "4":
        slot = input("🎯 Enter capability slot (e.g. #CAPABILITY: InfoSec-Threat): ").strip()
        if slot:
            cmd = [sys.executable, os.path.join(base_dir, "resolve_capability.py"), slot]
            subprocess.run(cmd)

    elif choice == "5":
        new_tenant = input("🏢 Enter tenant ID (e.g. acme_corp): ").strip()
        if new_tenant:
            cmd = [os.path.join(base_dir, "setup.sh"), new_tenant]
            subprocess.run(cmd)

    elif choice == "6":
        phase = input("⚠️ Enter phase to rollback to (e.g. PHASE_1, PHASE_2): ").strip()
        if phase:
            cmd = [os.path.join(base_dir, "rollback.sh"), phase]
            subprocess.run(cmd)

    elif choice == "0":
        print("👋 Exiting Hermes TDL Console. Happy deploying!")
        sys.exit(0)

def main():
    while True:
        print_banner()
        show_menu()
        choice = input("Enter choice [0-6]: ").strip()
        run_action(choice)
        input("\nPress Enter to continue...")
        print("\n" * 2)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--non-interactive":
        print_banner()
        print("✅ Interactive Console initialized and ready for TDL use.")
    else:
        main()
