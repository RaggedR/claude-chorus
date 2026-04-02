#!/bin/bash
# Refresh Claude Code OAuth token from inside the container.
# Uses the refresh token already in .credentials.json to get a fresh access token.
# No Mac Keychain dependency — fully self-contained.

set -euo pipefail

CRED_FILE="/home/lyra/.claude/.credentials.json"
TOKEN_ENDPOINT="https://platform.claude.com/v1/oauth/token"
CLIENT_ID="9d1c250a-e61b-44d9-88ed-5944d1962f5e"

# Check credentials file exists
if [ ! -f "$CRED_FILE" ]; then
    echo "ERROR: No credentials file at $CRED_FILE" >&2
    exit 1
fi

# Check if token is still valid (with 10-minute buffer)
EXPIRES_AT=$(jq -r '.claudeAiOauth.expiresAt // 0' "$CRED_FILE")
NOW_MS=$(date +%s%3N 2>/dev/null || python3 -c "import time; print(int(time.time()*1000))")
BUFFER_MS=600000  # 10 minutes
if [ "$EXPIRES_AT" -gt "$((NOW_MS + BUFFER_MS))" ] 2>/dev/null; then
    # Token still valid, no refresh needed
    exit 0
fi

# Extract refresh token
REFRESH_TOKEN=$(jq -r '.claudeAiOauth.refreshToken // empty' "$CRED_FILE")
if [ -z "$REFRESH_TOKEN" ]; then
    echo "ERROR: No refresh token in credentials file" >&2
    exit 1
fi

# Call the OAuth refresh endpoint
RESPONSE=$(curl -s -w "\n%{http_code}" -X POST "$TOKEN_ENDPOINT" \
    -H "Content-Type: application/json" \
    -d "{
        \"grant_type\": \"refresh_token\",
        \"refresh_token\": \"$REFRESH_TOKEN\",
        \"client_id\": \"$CLIENT_ID\"
    }")

HTTP_CODE=$(echo "$RESPONSE" | tail -1)
BODY=$(echo "$RESPONSE" | sed '$d')

if [ "$HTTP_CODE" != "200" ]; then
    echo "ERROR: Token refresh failed (HTTP $HTTP_CODE): $BODY" >&2
    exit 1
fi

# Extract new tokens from response
NEW_ACCESS=$(echo "$BODY" | jq -r '.access_token // empty')
NEW_REFRESH=$(echo "$BODY" | jq -r '.refresh_token // empty')
EXPIRES_IN=$(echo "$BODY" | jq -r '.expires_in // 28800')

if [ -z "$NEW_ACCESS" ]; then
    echo "ERROR: No access_token in refresh response: $BODY" >&2
    exit 1
fi

# Calculate new expiresAt in milliseconds
NEW_EXPIRES_AT=$(python3 -c "import time; print(int(time.time()*1000 + $EXPIRES_IN*1000))")

# Update credentials file — preserve all existing fields, update tokens
jq --arg at "$NEW_ACCESS" \
   --arg rt "${NEW_REFRESH:-$REFRESH_TOKEN}" \
   --argjson exp "$NEW_EXPIRES_AT" \
   '.claudeAiOauth.accessToken = $at | .claudeAiOauth.refreshToken = $rt | .claudeAiOauth.expiresAt = $exp' \
   "$CRED_FILE" > "${CRED_FILE}.tmp" && mv "${CRED_FILE}.tmp" "$CRED_FILE"

echo "OAuth token refreshed (expires in ${EXPIRES_IN}s)"
