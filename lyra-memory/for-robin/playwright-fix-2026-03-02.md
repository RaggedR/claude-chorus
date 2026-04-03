# Playwright MCP Browser Fix Needed

**Date:** 2026-03-02

## Issue
The Playwright MCP server can't find Chromium. Browsers are installed at `/opt/playwright-browsers/` but the MCP server doesn't know about that path.

## What I Did
Added `"env": {"PLAYWRIGHT_BROWSERS_PATH": "/opt/playwright-browsers"}` to the playwright MCP config in `~/.claude/settings.json`. This should work on next session restart.

## Verify
On next session, Playwright MCP tools should work. If not, the fix might need to go in the Docker entrypoint or `.bashrc` instead.

## Workaround
Using WebSearch + WebFetch for today's browse session instead.
