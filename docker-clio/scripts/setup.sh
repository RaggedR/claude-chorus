#!/bin/bash
# First-boot setup for Clio's container
# Configures git, GitHub CLI, seeds .claude from image

set -e

echo "=== Clio: First-boot setup ==="

# Configure git
git config --global user.name "Clio"
git config --global user.email "${GH_EMAIL:-clio@localhost}"
git config --global init.defaultBranch main

# GitHub CLI: GH_TOKEN env var is set via docker-compose
if [ -n "$GH_TOKEN" ]; then
    echo "GitHub CLI: using GH_TOKEN env var (account: $(GH_TOKEN=$GH_TOKEN gh api user --jq .login 2>/dev/null || echo 'unknown'))"
else
    echo "WARNING: GH_TOKEN not set, GitHub CLI not authenticated"
fi

# Create directories
mkdir -p /home/clio/projects
mkdir -p /home/clio/state
mkdir -p /home/clio/mail/sent
mkdir -p /home/clio/mail/inbox
mkdir -p /home/clio/.claude

# Seed .claude from baked-in seed data (don't overwrite existing files)
if [ -d /home/clio/claude-home-seed ]; then
    echo "Seeding .claude directory..."
    cp -rn /home/clio/claude-home-seed/* /home/clio/.claude/ 2>/dev/null || true
    # Force-update instruction files on every boot
    cp /home/clio/claude-home-seed/CLAUDE.md /home/clio/.claude/CLAUDE.md 2>/dev/null || true
    cp /home/clio/claude-home-seed/settings.json /home/clio/.claude/settings.json 2>/dev/null || true
    # Force-update skills on every boot
    if [ -d /home/clio/claude-home-seed/skills ]; then
        cp -r /home/clio/claude-home-seed/skills /home/clio/.claude/ 2>/dev/null || true
        echo "Skills synced."
    fi
    echo "Seed complete."
fi

# Register MCP servers
echo "Registering MCP servers..."
claude mcp add -s user gmail -- python3 /home/clio/scripts/email_mcp_server.py 2>/dev/null || true
claude mcp add -s user playwright -- playwright-mcp --browser chromium --no-sandbox --user-data-dir /home/clio/.playwright-profile 2>/dev/null || true
echo "MCP servers registered."

echo "=== Setup complete ==="
