#!/usr/bin/env python3
"""
🛡️ Hermes TDL & FDE Interactive Console (Dual-Track Edition)
Zero-friction CLI environment for Technical Deployment Leads (TDLs) & Forward Deployed Engineers (FDEs).
Supports Enterprise 12-Week Track and FDE Fast-Track (2-4 Weeks) Argolis-to-GCP Production Migration.
"""

import sys
import os
import subprocess

GBRAIN_BASE = os.path.expanduser("~/.gbrain")

def detect_gbrain_base():
    drive_dir = os.environ.get("GBRAIN_DRIVE_DIR")
    if drive_dir and os.path.exists(drive_dir):
        return os.path.expanduser(drive_dir)
    try:
        res = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True)
        repo_root = res.stdout.strip()
        in_repo_gbrain = os.path.join(repo_root, ".gbrain")
        if os.path.exists(in_repo_gbrain):
            return in_repo_gbrain
    except Exception:
        pass
    return os.path.expanduser("~/.gbrain")

GBRAIN_BASE = detect_gbrain_base()

def get_active_tenant():
    active_file = os.path.join(GBRAIN_BASE, "active_tenant")
    if os.path.exists(active_file):
        with open(active_file, "r") as f:
            return f.read().strip()
    return "default"

def print_banner():
    tenant = get_active_tenant()
    print("==========================================================================")
    print(" 🛡️  HERMES TDL & FDE OPERATING CONSOLE (Dual-Track v2.1)")
    print(f" 🏢 Active Tenant Scope: [{tenant}] ({os.path.join(GBRAIN_BASE, 'tenants', tenant)})")
    print(" 🧠 Orchestrator: Monica (Chief of Staff)")
    print("==========================================================================")

def show_menu():
    print("\nSelect an operational action:\n")
    print("  [1] 📋 View Active State Machine & Lifecycle Mode")
    print("  [2] 🔍 Search GBrain Memory Substrate (Multi-Tenant)")
    print("  [3] 📊 Run Multi-Objective EBITDA & Quality Evals")
    print("  [4] 🎯 Resolve Dynamic Capability Slot")
    print("  [5] 🏢 Switch / Initialize Tenant Scope (setup.sh)")
    print("  [6] ⚠️ Trigger Automated State Checkpoint Rollback")
    print("  [7] ✈️ FDE FAST-TRACK: Migrate Argolis Sandbox ➔ GCP Prod Project")
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

    elif choice == "7":
        target_gcp = input("✈️ Enter Target Customer GCP Project ID (e.g. customer-gcp-prod-88): ").strip()
        if target_gcp:
            cmd = [os.path.join(base_dir, "migrate_tenant.sh"), tenant, target_gcp]
            subprocess.run(cmd)

    elif choice == "0":
        print("👋 Exiting Hermes Console. Happy deploying!")
        sys.exit(0)

def main():
    while True:
        print_banner()
        show_menu()
        choice = input("Enter choice [0-7]: ").strip()
        run_action(choice)
        input("\nPress Enter to continue...")
        print("\n" * 2)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--non-interactive":
        print_banner()
        print("✅ Interactive Console initialized and ready for TDL/FDE use.")
    else:
        main()
