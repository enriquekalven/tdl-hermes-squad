#!/usr/bin/env python3
"""
GBrain Knowledge Search Tool
Scans and queries ~/.gbrain/ entity markdown files for fast context retrieval.
"""

import sys
import os
import glob

GBRAIN_DIR = os.path.expanduser("~/.gbrain")

def search_brain(query):
    query = query.lower()
    results = []

    if not os.path.exists(GBRAIN_DIR):
        print(f"Error: {GBRAIN_DIR} directory does not exist.")
        return

    md_files = glob.glob(os.path.join(GBRAIN_DIR, "**/*.md"), recursive=True)

    for filepath in md_files:
        rel_path = os.path.relpath(filepath, GBRAIN_DIR)
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        
        matching_lines = []
        for idx, line in enumerate(lines, 1):
            if query in line.lower():
                matching_lines.append((idx, line.strip()))
        
        if matching_lines:
            results.append((rel_path, matching_lines))

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
    if len(sys.argv) < 2:
        print("Usage: python3 search_brain.py <search_query>")
        sys.exit(1)
    
    search_query = " ".join(sys.argv[1:])
    search_brain(search_query)
