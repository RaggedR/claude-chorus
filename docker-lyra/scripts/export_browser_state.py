#!/usr/bin/env python3
"""Export browser cookies from Playwright MCP's persistent profile to a storage state JSON.

This bridges the gap between Playwright MCP (which uses a persistent browser profile
directory with OS-level file locks) and the CodeAct browse_toolkit (which needs cookies
as a JSON file to create independent BrowserContexts).

Runs once before each browse session, after social-login.sh has ensured cookies are fresh.

Usage:
    python3 /home/lyra/scripts/export_browser_state.py
"""

import json
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

PROFILE_DIR = "/home/lyra/.playwright-profile"
OUTPUT_PATH = os.path.join(PROFILE_DIR, "storage-state.json")


def export_storage_state():
    """Open the persistent profile, export cookies as storage state JSON."""

    profile = Path(PROFILE_DIR)

    # First-run case: no profile directory yet
    if not profile.is_dir():
        print(f"No profile directory at {PROFILE_DIR} — writing empty state file.")
        profile.mkdir(parents=True, exist_ok=True)
        Path(OUTPUT_PATH).write_text(json.dumps({"cookies": [], "origins": []}))
        return

    with sync_playwright() as p:
        # Open the persistent profile (same one Playwright MCP uses)
        # This briefly locks the profile — must not run while MCP is active
        context = p.chromium.launch_persistent_context(
            PROFILE_DIR,
            headless=True,
            args=["--no-sandbox"],
        )

        # Export cookies + localStorage as JSON
        context.storage_state(path=OUTPUT_PATH)

        cookie_count = len(context.cookies())
        context.close()

    print(f"Exported {cookie_count} cookies to {OUTPUT_PATH}")


if __name__ == "__main__":
    try:
        export_storage_state()
    except Exception as e:
        print(f"Storage state export failed: {e}", file=sys.stderr)
        # Write empty state so browse_toolkit doesn't crash looking for the file
        Path(PROFILE_DIR).mkdir(parents=True, exist_ok=True)
        Path(OUTPUT_PATH).write_text(json.dumps({"cookies": [], "origins": []}))
        print(f"Wrote empty state file to {OUTPUT_PATH}")
        sys.exit(1)
