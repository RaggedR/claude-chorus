#!/bin/bash
# Backup all Claude ecosystem state to the claude-chorus repo.
# Run from anywhere: ~/git/claude-chorus/backup.sh
#
# Sources:
#   ~/.claude/          → instruction files, settings, notes, skills, project memories
#   ~/lyra-memory/      → dreams, reading, messages, topics, connections
#   ~/docker-lyra/      → Lyra's Docker container (personality, email, plans, scripts)
#
# Excludes:
#   ~/.claude/tasks/            (ephemeral runtime locks)
#   ~/.claude/mcp-needs-auth-cache.json
#   ~/.claude/stats-cache.json
#   docker-lyra/.env            (real credentials)

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_DIR"

echo "Backing up to $REPO_DIR"

# ── Instruction files + settings ──────────────────────────────
for f in CLAUDE.md TEAM.md CODING.md AGENT.md CONTEXT.md settings.json settings.local.json; do
  [ -f "$HOME/.claude/$f" ] && cp "$HOME/.claude/$f" "$REPO_DIR/$f"
done
echo "✓ instruction files + settings"

# ── Bulletin board ────────────────────────────────────────────
mkdir -p "$REPO_DIR/notes"
rsync -a --delete "$HOME/.claude/tmp/notes/" "$REPO_DIR/notes/"
echo "✓ bulletin board ($(ls "$REPO_DIR/notes/" | wc -l | tr -d ' ') notes)"

# ── Skills ────────────────────────────────────────────────────
mkdir -p "$REPO_DIR/skills"
rsync -a --delete --exclude='node_modules' "$HOME/.claude/skills/" "$REPO_DIR/skills/"
echo "✓ skills"

# ── Project memories ──────────────────────────────────────────
mkdir -p "$REPO_DIR/project-memory"
for dir in "$HOME"/.claude/projects/*/memory; do
  [ -d "$dir" ] || continue
  project="$(basename "$(dirname "$dir")")"
  mkdir -p "$REPO_DIR/project-memory/$project"
  rsync -a "$dir/" "$REPO_DIR/project-memory/$project/"
done
echo "✓ project memories ($(find "$REPO_DIR/project-memory" -type f | wc -l | tr -d ' ') files)"

# ── Lyra's memory ────────────────────────────────────────────
rsync -a --delete "$HOME/lyra-memory/" "$REPO_DIR/lyra-memory/"
echo "✓ lyra-memory ($(find "$REPO_DIR/lyra-memory" -type f | wc -l | tr -d ' ') files)"

# ── Docker-lyra (Lyra's container) ───────────────────────────
rsync -a --delete \
  --exclude='.env' \
  --exclude='__pycache__' \
  --exclude='.DS_Store' \
  --exclude='*.pyc' \
  "$HOME/docker-lyra/" "$REPO_DIR/docker-lyra/"
echo "✓ docker-lyra ($(find "$REPO_DIR/docker-lyra" -type f | wc -l | tr -d ' ') files)"

# ── Session transcripts (compressed + split for GitHub) ──────
mkdir -p "$REPO_DIR/transcripts"
echo "  compressing transcripts..."
tar czf /tmp/claude-transcripts.tar.gz -C "$HOME/.claude" projects/
split -b 95m /tmp/claude-transcripts.tar.gz "$REPO_DIR/transcripts/claude-transcripts.tar.gz.part-"
rm /tmp/claude-transcripts.tar.gz
echo "✓ transcripts ($(du -sh "$REPO_DIR/transcripts/" | cut -f1) compressed)"

# ── Summary ──────────────────────────────────────────────────
echo ""
echo "Done. Review changes with:"
echo "  cd $REPO_DIR && git status"
echo "  git add -A && git commit -m 'Backup $(date +%Y-%m-%d)'"
echo "  git push"
