#!/bin/bash
# Lyra's container entrypoint
# Setup as root, then run Claude in a loop as lyra.
# No supervisor, no scheduler. Claude IS the process.
set -e

export HOME=/home/lyra

# Root setup: fix ownership
chown -R lyra:lyra /home/lyra/.claude /home/lyra/projects /home/lyra/mail 2>/dev/null || true
chown -R lyra:lyra /home/lyra/claude-home-seed /home/lyra/scripts /home/lyra/config 2>/dev/null || true

# Run first-boot setup
sudo -E -u lyra /home/lyra/scripts/setup.sh

# Hand everything to lyra
exec sudo -E -u lyra /home/lyra/scripts/lyra-loop.sh
