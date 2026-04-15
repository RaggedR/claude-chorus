#!/bin/bash
# Clio's container entrypoint
# Setup as root, then run Claude in a loop as clio.
set -e

export HOME=/home/clio

# Root setup: fix ownership
chown -R clio:clio /home/clio/.claude /home/clio/projects /home/clio/mail /home/clio/state 2>/dev/null || true
chown -R clio:clio /home/clio/claude-home-seed /home/clio/scripts /home/clio/config 2>/dev/null || true

# Run first-boot setup
sudo -E -u clio /home/clio/scripts/setup.sh

# Hand everything to clio
exec sudo -E -u clio /home/clio/scripts/clio-loop.sh
