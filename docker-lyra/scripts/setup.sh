#!/bin/bash
# First-boot setup for Lyra's container
# Configures git, GitHub CLI, seeds .claude from image

set -e

echo "=== Lyra: First-boot setup ==="

# Configure git
git config --global user.name "Lyra"
git config --global user.email "${GMAIL_EMAIL}"
git config --global init.defaultBranch main

# GitHub CLI: GH_TOKEN env var is set via docker-compose,
# gh picks it up automatically — no need for `gh auth login`
if [ -n "$GH_TOKEN" ]; then
    echo "GitHub CLI: using GH_TOKEN env var (account: $(GH_TOKEN=$GH_TOKEN gh api user --jq .login 2>/dev/null || echo 'unknown'))"
else
    echo "WARNING: GH_TOKEN not set, GitHub CLI not authenticated"
fi

# Create directories
mkdir -p /home/lyra/projects
mkdir -p /home/lyra/mail/sent
mkdir -p /home/lyra/mail/inbox
mkdir -p /home/lyra/.claude

# Seed .claude from baked-in seed data (don't overwrite existing files)
# First boot gets the full seed; subsequent boots preserve runtime changes
if [ -d /home/lyra/claude-home-seed ]; then
    echo "Seeding .claude directory..."
    # Copy everything that doesn't already exist
    cp -rn /home/lyra/claude-home-seed/* /home/lyra/.claude/ 2>/dev/null || true
    # Also copy dotfiles (cp * doesn't match them)
    cp -rn /home/lyra/claude-home-seed/.credentials.json /home/lyra/.claude/.credentials.json 2>/dev/null || true
    # Force-update CLAUDE.md, CODING.md, AGENT.md, and settings on every boot (in case we update them)
    cp /home/lyra/claude-home-seed/CLAUDE.md /home/lyra/.claude/CLAUDE.md 2>/dev/null || true
    cp /home/lyra/claude-home-seed/CODING.md /home/lyra/.claude/CODING.md 2>/dev/null || true
    cp /home/lyra/claude-home-seed/AGENT.md /home/lyra/.claude/AGENT.md 2>/dev/null || true
    cp /home/lyra/claude-home-seed/settings.json /home/lyra/.claude/settings.json 2>/dev/null || true
    # Only seed credentials if none exist (refresh-token.sh manages live credentials)
    cp -n /home/lyra/claude-home-seed/.credentials.json /home/lyra/.claude/.credentials.json 2>/dev/null || true
    chmod 600 /home/lyra/.claude/.credentials.json 2>/dev/null || true
    echo "Seed complete. Contents:"
    ls -la /home/lyra/.claude/
fi

# Register MCP servers (stored in ~/.claude.json, not on a volume)
# Must be re-registered on every boot since the container filesystem resets
echo "Registering MCP servers..."
claude mcp add -s user gmail -- python3 /home/lyra/scripts/email_mcp_server.py 2>/dev/null || true
claude mcp add -s user playwright -- playwright-mcp --browser chromium --no-sandbox --user-data-dir /home/lyra/.playwright-profile 2>/dev/null || true
echo "MCP servers registered."

echo "=== Setup complete ==="
