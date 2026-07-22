#!/usr/bin/env python3
"""
GBrain Knowledge Search Tool (Multi-Tenant & Hierarchical Indexing Edition)
Scans and queries ~/.gbrain/tenants/<tenant_id>/ entity markdown files for fast context retrieval.
"""

import sys
import os
import glob
import argparse

GBRAIN_BASE = os.path.expanduser("~/.gbrain")

def get_active_tenant():
    active_file = os.path.join(GBRAIN_BASE, "active_tenant")
    if os.path.exists(active_file):
        with open(active_file, "r") as f:
            return f.read().strip()
    return "default"

def search_brain(query, tenant_id=None):
    if not tenant_id:
        tenant_id = get_active_tenant()

    tenant_dir = os.path.join(GBRAIN_BASE, "tenants", tenant_id)
    if not os.path.exists(tenant_dir):
        # Fallback to legacy root ~/.gbrain if tenant dir doesn't exist
        tenant_dir = GBRAIN_BASE

    query = query.lower()
    results = []

    md_files = glob.glob(os.path.join(tenant_dir, "**/*.md"), recursive=True)

    for filepath in md_files:
        rel_path = os.path.relpath(filepath, tenant_dir)
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        
        matching_lines = []
        for idx, line in enumerate(lines, 1):
            if query in line.lower():
                matching_lines.append((idx, line.strip()))
        
        if matching_lines:
            results.append((rel_path, matching_lines))

    print(f"🏢 Tenant Scope: [{tenant_id}] ({tenant_dir})")
    if not results:
        print(f"🔍 No matches found in GBrain for: '{query}'")
        return

    print(f"🔍 Found {len(results)} file(s) matching '{query}' in GBrain:\n")
    for rel_path, matches in results:
        print(f"📄 {rel_path}:")
        for line_num, content in matches[:3]:
            print(f"   L{line_num}: {content[:100]}")
        print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GBrain Multi-Tenant Knowledge Search Tool")
    parser.add_argument("query", type=str, help="Search query string")
    parser.add_argument("--tenant", type=str, help="Tenant ID namespace (default: active tenant)")
    args = parser.parse_args()

    search_brain(args.query, tenant_id=args.tenant)
