#!/bin/bash
# Sync Lyra's in-container memory to the host for easy access.
# Run hourly via cron to keep ~/lyra-memory/ current.

set -euo pipefail

# Absolute path — cron's PATH doesn't include /usr/local/bin
DOCKER="/usr/local/bin/docker"

CONTAINER="lyra"
HOST_DIR="$HOME/lyra-memory"
LOG="$HOST_DIR/.sync.log"
HEARTBEAT="$HOST_DIR/.last-seen-running"
ALERT_HOURS=24

# Check container is running
if ! "$DOCKER" inspect "$CONTAINER" --format '{{.State.Running}}' 2>/dev/null | grep -q true; then
    # Container not running — check how long it's been down
    if [ -f "$HEARTBEAT" ]; then
        last_seen=$(cat "$HEARTBEAT")
        now=$(date +%s)
        elapsed_hours=$(( (now - last_seen) / 3600 ))
        if [ "$elapsed_hours" -ge "$ALERT_HOURS" ]; then
            /usr/bin/osascript -e "display notification \"Lyra's container has been down for ${elapsed_hours}h\" with title \"Lyra is offline\" sound name \"Funk\"" 2>/dev/null
            echo "$(date): ALERT — container down for ${elapsed_hours}h" >> "$LOG"
        fi
    fi
    exit 0
fi

# Container is running — update heartbeat
date +%s > "$HEARTBEAT"

# Sync memory from container to host
"$DOCKER" cp "$CONTAINER":/home/lyra/projects/memory/. "$HOST_DIR"/

# Keep log trimmed to last 50 lines
if [ -f "$LOG" ] && [ "$(wc -l < "$LOG")" -gt 50 ]; then
    tail -30 "$LOG" > "$LOG.tmp" && mv "$LOG.tmp" "$LOG"
fi
echo "$(date): Memory synced successfully" >> "$LOG"
