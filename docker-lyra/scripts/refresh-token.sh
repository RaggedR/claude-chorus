#!/bin/bash
# Refresh Lyra's OAuth token from the Mac keychain into the Docker container.
# Run this periodically (every 30 min) to keep Lyra authenticated.

set -euo pipefail

CONTAINER="lyra"
CRED_FILE="/tmp/lyra-credentials.json"

# Check container is running
if ! docker inspect "$CONTAINER" --format '{{.State.Running}}' 2>/dev/null | grep -q true; then
    exit 0  # Container not running, nothing to do
fi

# Extract fresh token from macOS keychain
security find-generic-password -s "Claude Code-credentials" -w > "$CRED_FILE" 2>/dev/null
if [ $? -ne 0 ] || [ ! -s "$CRED_FILE" ]; then
    echo "$(date): Failed to extract credentials from keychain" >> /tmp/lyra-token-refresh.log
    rm -f "$CRED_FILE"
    exit 1
fi

# Push into container
docker cp "$CRED_FILE" "$CONTAINER":/home/lyra/.claude/.credentials.json
docker exec "$CONTAINER" chown lyra:lyra /home/lyra/.claude/.credentials.json
docker exec "$CONTAINER" chmod 600 /home/lyra/.claude/.credentials.json

# Cleanup
rm -f "$CRED_FILE"
echo "$(date): Token refreshed successfully" >> /tmp/lyra-token-refresh.log
