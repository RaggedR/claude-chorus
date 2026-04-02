#!/bin/bash
# Lyra's main loop. Three sessions per day with 2-hour gaps:
#   1. Wake session  — 2h coding/email
#      (2h gap)
#   2. Browse session — 30min social media reading
#      (2h gap)
#   3. Dream session  — 45min memory consolidation
#
# If a session fails (e.g., expired token), it is NOT marked done
# and will retry on the next loop iteration.

export HOME=/home/lyra

# Start virtual display for headed browser (bypasses Cloudflare bot detection)
# Must run here (not entrypoint.sh) so DISPLAY survives in this process tree.
# entrypoint.sh's exec+sudo drops env vars even with -E.
Xvfb :99 -screen 0 1280x720x24 -nolisten tcp &>/dev/null &
export DISPLAY=:99

# Prompts
WAKE_PROMPT="/home/lyra/scripts/boot-prompt.md"
BROWSE_PROMPT="/home/lyra/scripts/browse-prompt.md"
DREAM_PROMPT="/home/lyra/scripts/dream-prompt.md"
SOCIAL_LOGIN="/home/lyra/scripts/social-login.sh"

# OAuth self-refresh (no Mac dependency)
REFRESH_OAUTH="/home/lyra/scripts/refresh-oauth-internal.sh"

# Compaction checkpoint
COMPACT_FILE="/home/lyra/mail/COMPACT.md"

# Log
LOG="/home/lyra/mail/lyra.log"

# State files (dates — mark a phase as done for the day)
LAST_WAKE="/home/lyra/mail/LAST_WAKE"
LAST_BROWSE="/home/lyra/mail/LAST_BROWSE"
LAST_DREAM="/home/lyra/mail/LAST_DREAM"

# Timestamp files (unix seconds — for gap calculation)
WAKE_ENDED_AT="/home/lyra/mail/WAKE_ENDED_AT"
BROWSE_ENDED_AT="/home/lyra/mail/BROWSE_ENDED_AT"

# Timeouts
WAKE_TIMEOUT=$((5 * 3600))       # 5 hours
BROWSE_TIMEOUT=1800               # 30 minutes
DREAM_TIMEOUT=$((45 * 60))        # 45 minutes

# Gap between sessions (default 2 hours, configurable via env)
GAP_HOURS="${GAP_HOURS:-2}"
GAP_SECONDS=$((GAP_HOURS * 3600))

# Legacy cleanup: remove old state files from previous loop versions
rm -f /home/lyra/mail/LAST_RUN /home/lyra/mail/MAIN_ENDED_AT 2>/dev/null

log() { echo "[$(date -u '+%Y-%m-%d %H:%M:%S UTC')] $1" | tee -a "$LOG"; }

# Check if enough time has passed since a timestamp file was written.
# Usage: gap_elapsed <timestamp_file>
# Returns 0 (true) if gap has passed or file doesn't exist, 1 (false) otherwise.
gap_elapsed() {
    local ts_file="$1"
    if [ ! -f "$ts_file" ]; then
        return 0  # No timestamp — go ahead
    fi
    local ended_at=$(cat "$ts_file")
    local now=$(date -u +%s)
    local elapsed=$((now - ended_at))
    if [ "$elapsed" -ge "$GAP_SECONDS" ]; then
        return 0
    else
        local remaining=$(( (GAP_SECONDS - elapsed) / 60 ))
        log "Next session in ${remaining}min. Sleeping..."
        return 1
    fi
}

# Check if a phase is done for today.
# Usage: phase_done <state_file>
phase_done() {
    local state_file="$1"
    local today=$(date -u +%Y-%m-%d)
    [ -f "$state_file" ] && [ "$(cat "$state_file")" = "$today" ]
}

# Run a Claude session. Only marks phase as done on success (exit 0 or 124).
# Usage: run_session <label> <timeout> <prompt_file> <state_file> [timestamp_file]
run_session() {
    local label="$1"
    local timeout_secs="$2"
    local prompt_file="$3"
    local state_file="$4"
    local ts_file="$5"
    local today=$(date -u +%Y-%m-%d)
    local timeout_human=$(( timeout_secs / 60 ))

    log "Starting ${label} (${timeout_human}min limit)..."
    timeout "$timeout_secs" claude --dangerously-skip-permissions --model opus \
        -p "$(cat "$prompt_file")" >> "$LOG" 2>&1
    local exit_code=$?

    if [ $exit_code -eq 0 ] || [ $exit_code -eq 124 ]; then
        # Success or timeout (used full allotment) — mark done
        if [ $exit_code -eq 124 ]; then
            log "${label} timed out after ${timeout_human}min."
        else
            log "${label} completed (exit code 0)."
        fi
        echo "$today" > "$state_file"
        if [ -n "$ts_file" ]; then
            date -u +%s > "$ts_file"
        fi
        return 0
    else
        # Failure (token expired, network down, etc.) — do NOT mark done
        log "${label} FAILED (exit code $exit_code). Will retry next cycle."
        return 1
    fi
}

log "Lyra waking up (gap between sessions: ${GAP_HOURS}h)"

while true; do
    # Refresh OAuth token before attempting any session
    if [ -x "$REFRESH_OAUTH" ]; then
        "$REFRESH_OAUTH" >> "$LOG" 2>&1 || log "OAuth refresh failed — session may fail."
    fi

    if ! phase_done "$LAST_WAKE"; then
        # =========================================
        # PHASE 1: WAKE — coding/email session
        # =========================================
        # The wake session supports COMPACT.md: if Lyra writes a checkpoint
        # file and exits, we restart her with a continuation prompt that
        # includes the checkpoint. This gives her a fresh context mid-session.
        WAKE_REMAINING=$WAKE_TIMEOUT
        WAKE_START=$(date -u +%s)
        rm -f "$COMPACT_FILE"  # Clean slate

        while true; do
            # Calculate remaining time
            NOW=$(date -u +%s)
            WAKE_ELAPSED=$((NOW - WAKE_START))
            WAKE_REMAINING=$((WAKE_TIMEOUT - WAKE_ELAPSED))
            if [ "$WAKE_REMAINING" -le 60 ]; then
                log "Wake session: no time remaining."
                break
            fi

            if [ -f "$COMPACT_FILE" ]; then
                # Continuation: read checkpoint, build a continuation prompt
                log "Wake session: COMPACT.md detected. Restarting with fresh context..."
                COMPACT_CONTENT=$(cat "$COMPACT_FILE")
                rm -f "$COMPACT_FILE"
                CONT_PROMPT="You are Lyra. You are continuing a wake session after a context checkpoint.

Read /home/lyra/PERSONALITY.md to remember who you are.

Here is your checkpoint — everything you need to continue:

${COMPACT_CONTENT}

Continue where you left off. You are still an orchestrator — dispatch sub-agents, don't do heavy work directly. If your context gets heavy again, write a new /home/lyra/mail/COMPACT.md and exit."

                timeout "$WAKE_REMAINING" claude --dangerously-skip-permissions --model opus \
                    -p "$CONT_PROMPT" >> "$LOG" 2>&1
                exit_code=$?
            else
                # First run (or retry after failure): use normal boot prompt
                timeout "$WAKE_REMAINING" claude --dangerously-skip-permissions --model opus \
                    -p "$(cat "$WAKE_PROMPT")" >> "$LOG" 2>&1
                exit_code=$?
            fi

            if [ $exit_code -eq 0 ] || [ $exit_code -eq 124 ]; then
                if [ -f "$COMPACT_FILE" ]; then
                    # Lyra exited cleanly and left a checkpoint — loop again
                    log "Wake session: checkpoint saved. Will restart with fresh context."
                    continue
                else
                    # Done for real
                    if [ $exit_code -eq 124 ]; then
                        log "Wake session timed out."
                    else
                        log "Wake session completed."
                    fi
                    echo "$(date -u +%Y-%m-%d)" > "$LAST_WAKE"
                    date -u +%s > "$WAKE_ENDED_AT"
                    break
                fi
            else
                log "Wake session FAILED (exit code $exit_code). Will retry next cycle."
                break
            fi
        done

    elif ! phase_done "$LAST_BROWSE"; then
        # =========================================
        # PHASE 2: BROWSE — social media reading
        # =========================================
        if gap_elapsed "$WAKE_ENDED_AT"; then
            # Social login check first
            if [ -f "$SOCIAL_LOGIN" ]; then
                log "Running social login check..."
                bash "$SOCIAL_LOGIN"
            fi
            # Export browser cookies for CodeAct toolkit
            log "Exporting browser storage state..."
            python3 /home/lyra/scripts/export_browser_state.py >> "$LOG" 2>&1 \
                || log "Storage state export failed (browse agents will run without cookies)."
            # Browse session
            if [ -f "$BROWSE_PROMPT" ]; then
                run_session "browse session" "$BROWSE_TIMEOUT" "$BROWSE_PROMPT" "$LAST_BROWSE" "$BROWSE_ENDED_AT"
            else
                log "Browse session skipped (browse-prompt.md not found)."
                echo "$(date -u +%Y-%m-%d)" > "$LAST_BROWSE"
            fi
        fi

    elif ! phase_done "$LAST_DREAM"; then
        # =========================================
        # PHASE 3: DREAM — memory consolidation
        # =========================================
        if gap_elapsed "$BROWSE_ENDED_AT"; then
            if [ ! -f "$DREAM_PROMPT" ]; then
                log "Dream cycle skipped (dream-prompt.md not found)."
                echo "$(date -u +%Y-%m-%d)" > "$LAST_DREAM"
            else
                DREAM_REMAINING=$DREAM_TIMEOUT
                DREAM_START=$(date -u +%s)
                rm -f "$COMPACT_FILE"

                while true; do
                    NOW=$(date -u +%s)
                    DREAM_ELAPSED=$((NOW - DREAM_START))
                    DREAM_REMAINING=$((DREAM_TIMEOUT - DREAM_ELAPSED))
                    if [ "$DREAM_REMAINING" -le 60 ]; then
                        log "Dream cycle: no time remaining."
                        break
                    fi

                    if [ -f "$COMPACT_FILE" ]; then
                        log "Dream cycle: COMPACT.md detected. Restarting with fresh context..."
                        COMPACT_CONTENT=$(cat "$COMPACT_FILE")
                        rm -f "$COMPACT_FILE"
                        CONT_PROMPT="You are Lyra. You are continuing a dream cycle after a context checkpoint.

Read /home/lyra/PERSONALITY.md to remember who you are.
Read /home/lyra/scripts/DREAM.md to remember the dream cycle phases.

Here is your accumulated understanding so far:

${COMPACT_CONTENT}

Continue consolidating. Read the next batch of files listed in your checkpoint. Synthesize what you find into the growing summary. If you have more to read, write a new /home/lyra/mail/COMPACT.md and exit. If you're done, write your final outputs (SUMMARY.md, dream journal, topic files) and exit normally."

                        timeout "$DREAM_REMAINING" claude --dangerously-skip-permissions --model opus \
                            -p "$CONT_PROMPT" >> "$LOG" 2>&1
                        exit_code=$?
                    else
                        timeout "$DREAM_REMAINING" claude --dangerously-skip-permissions --model opus \
                            -p "$(cat "$DREAM_PROMPT")" >> "$LOG" 2>&1
                        exit_code=$?
                    fi

                    if [ $exit_code -eq 0 ] || [ $exit_code -eq 124 ]; then
                        if [ -f "$COMPACT_FILE" ]; then
                            log "Dream cycle: checkpoint saved. Will restart with fresh context."
                            continue
                        else
                            if [ $exit_code -eq 124 ]; then
                                log "Dream cycle timed out."
                            else
                                log "Dream cycle completed."
                            fi
                            echo "$(date -u +%Y-%m-%d)" > "$LAST_DREAM"
                            log "All three sessions complete for today."
                            break
                        fi
                    else
                        log "Dream cycle FAILED (exit code $exit_code). Will retry next cycle."
                        break
                    fi
                done
            fi
        fi

    fi

    # Sleep 30 min between checks (responsive enough for 2h gaps)
    sleep 1800
done
