#!/bin/bash
# Wrapper for scheduler that ensures environment is loaded.
# Supervisor strips env when switching user; this restores it.

# Source the env file that entrypoint writes at boot
if [ -f /home/lyra/.env ]; then
    set -a
    source /home/lyra/.env
    set +a
fi

export HOME=/home/lyra
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/cargo/bin"

exec python3 /home/lyra/scripts/scheduler.py
