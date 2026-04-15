#!/bin/bash
# Clio's main loop. Same architecture as Lyra: wake-browse-dream cycles.
#   1. Wake session   — 5h research/computation/email
#      (gap)
#   2. Prove session  — 3h focused theorem proving (skipped if no PROVE.md)
#      (gap)
#   3. Browse session — 60min reading arXiv, MathOverflow, Semantic Scholar
#      (gap)
#   4. Dream session  — 45min memory consolidation
#      (gap)
#   ... repeat CYCLES_PER_DAY times

export HOME=/home/clio

# Start virtual display for headed browser
Xvfb :99 -screen 0 1280x720x24 -nolisten tcp &>/dev/null &
export DISPLAY=:99

# Prompts
WAKE_PROMPT="/home/clio/scripts/boot-prompt.md"
PROVE_PROMPT="/home/clio/scripts/prove-prompt.md"
BROWSE_PROMPT="/home/clio/scripts/browse-prompt.md"
DREAM_PROMPT="/home/clio/scripts/dream-prompt.md"

# Prove session trigger — only runs if this file exists
PROVE_THEOREM="/home/clio/state/PROVE.md"

# Compaction checkpoint
COMPACT_FILE="/home/clio/state/COMPACT.md"

# Log
LOG="/home/clio/state/clio.log"

# State files (store "DATE:COUNT" e.g. "2026-04-07:1")
LAST_WAKE="/home/clio/state/LAST_WAKE"
LAST_PROVE="/home/clio/state/LAST_PROVE"
LAST_BROWSE="/home/clio/state/LAST_BROWSE"
LAST_DREAM="/home/clio/state/LAST_DREAM"

# Timestamp files (unix seconds — for gap calculation)
WAKE_ENDED_AT="/home/clio/state/WAKE_ENDED_AT"
PROVE_ENDED_AT="/home/clio/state/PROVE_ENDED_AT"
BROWSE_ENDED_AT="/home/clio/state/BROWSE_ENDED_AT"
DREAM_ENDED_AT="/home/clio/state/DREAM_ENDED_AT"

# Timeouts
WAKE_TIMEOUT=$((5 * 3600))       # 5 hours
PROVE_TIMEOUT=$((3 * 3600))      # 3 hours
BROWSE_TIMEOUT=3600               # 60 minutes
DREAM_TIMEOUT=$((45 * 60))        # 45 minutes

# Cycles per day (default 2, configurable via env)
CYCLES_PER_DAY="${CYCLES_PER_DAY:-2}"

# Gap between sessions (default 2 hours, configurable via env)
GAP_HOURS="${GAP_HOURS:-2}"
GAP_SECONDS=$((GAP_HOURS * 3600))

log() { echo "[$(date -u '+%Y-%m-%d %H:%M:%S UTC')] $1" | tee -a "$LOG"; }

# Get how many times a phase has completed today.
phase_count() {
    local state_file="$1"
    local today=$(date -u +%Y-%m-%d)
    if [ -f "$state_file" ]; then
        local content=$(cat "$state_file")
        local file_date="${content%%:*}"
        if [ "$file_date" = "$today" ]; then
            local file_count="${content#*:}"
            if [ "$file_count" = "$file_date" ]; then
                echo "1"
            else
                echo "$file_count"
            fi
            return
        fi
    fi
    echo "0"
}

phase_done() {
    local state_file="$1"
    local count=$(phase_count "$state_file")
    [ "$count" -ge "$CYCLES_PER_DAY" ]
}

mark_done() {
    local state_file="$1"
    local today=$(date -u +%Y-%m-%d)
    local count=$(phase_count "$state_file")
    count=$((count + 1))
    echo "${today}:${count}" > "$state_file"
}

gap_elapsed() {
    local ts_file="$1"
    if [ ! -f "$ts_file" ]; then
        return 0
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

log "Clio waking up (${CYCLES_PER_DAY} cycles/day, ${GAP_HOURS}h gap between sessions)"

while true; do
    wake_n=$(phase_count "$LAST_WAKE")
    prove_n=$(phase_count "$LAST_PROVE")
    browse_n=$(phase_count "$LAST_BROWSE")
    dream_n=$(phase_count "$LAST_DREAM")

    if [ "$wake_n" -lt "$CYCLES_PER_DAY" ] && [ "$wake_n" -le "$dream_n" ]; then
        # WAKE — research/computation session
        if [ "$wake_n" -gt 0 ] && ! gap_elapsed "$DREAM_ENDED_AT"; then
            sleep 1800
            continue
        fi

        local_cycle=$((wake_n + 1))
        log "Starting wake cycle ${local_cycle}/${CYCLES_PER_DAY}..."

        WAKE_REMAINING=$WAKE_TIMEOUT
        WAKE_START=$(date -u +%s)
        rm -f "$COMPACT_FILE"

        while true; do
            NOW=$(date -u +%s)
            WAKE_ELAPSED=$((NOW - WAKE_START))
            WAKE_REMAINING=$((WAKE_TIMEOUT - WAKE_ELAPSED))
            if [ "$WAKE_REMAINING" -le 60 ]; then
                log "Wake session: no time remaining."
                break
            fi

            if [ -f "$COMPACT_FILE" ]; then
                log "Wake session: COMPACT.md detected. Restarting with fresh context..."
                COMPACT_CONTENT=$(cat "$COMPACT_FILE")
                rm -f "$COMPACT_FILE"
                CONT_PROMPT="You are Clio. You are continuing a wake session after a context checkpoint.

Read /home/clio/PERSONALITY.md to remember who you are.

Here is your checkpoint — everything you need to continue:

${COMPACT_CONTENT}

Continue where you left off. You are an orchestrator — dispatch sub-agents for heavy computation. If your context gets heavy again, write a new /home/clio/state/COMPACT.md and exit."

                timeout "$WAKE_REMAINING" claude --dangerously-skip-permissions --model opus \
                    -p "$CONT_PROMPT" >> "$LOG" 2>&1
                exit_code=$?
            else
                timeout "$WAKE_REMAINING" claude --dangerously-skip-permissions --model opus \
                    -p "$(cat "$WAKE_PROMPT")" >> "$LOG" 2>&1
                exit_code=$?
            fi

            if [ $exit_code -eq 0 ] || [ $exit_code -eq 124 ]; then
                if [ -f "$COMPACT_FILE" ]; then
                    log "Wake session: checkpoint saved. Will restart with fresh context."
                    continue
                else
                    if [ $exit_code -eq 124 ]; then
                        log "Wake cycle ${local_cycle} timed out."
                    else
                        log "Wake cycle ${local_cycle} completed."
                    fi
                    mark_done "$LAST_WAKE"
                    date -u +%s > "$WAKE_ENDED_AT"
                    break
                fi
            else
                log "Wake cycle ${local_cycle} FAILED (exit code $exit_code). Will retry next loop."
                break
            fi
        done

    elif [ "$prove_n" -lt "$wake_n" ]; then
        # PROVE — focused theorem proving (skipped if no PROVE.md)
        if [ ! -f "$PROVE_THEOREM" ]; then
            log "Prove session skipped (no PROVE.md)."
            mark_done "$LAST_PROVE"
            date -u +%s > "$PROVE_ENDED_AT"
        elif gap_elapsed "$WAKE_ENDED_AT"; then
            local_cycle=$((prove_n + 1))
            log "Starting prove cycle ${local_cycle}/${CYCLES_PER_DAY}..."

            PROVE_REMAINING=$PROVE_TIMEOUT
            PROVE_START=$(date -u +%s)
            rm -f "$COMPACT_FILE"

            while true; do
                NOW=$(date -u +%s)
                PROVE_ELAPSED=$((NOW - PROVE_START))
                PROVE_REMAINING=$((PROVE_TIMEOUT - PROVE_ELAPSED))
                if [ "$PROVE_REMAINING" -le 60 ]; then
                    log "Prove session: no time remaining."
                    break
                fi

                if [ -f "$COMPACT_FILE" ]; then
                    log "Prove session: COMPACT.md detected. Restarting with fresh context..."
                    COMPACT_CONTENT=$(cat "$COMPACT_FILE")
                    rm -f "$COMPACT_FILE"
                    CONT_PROMPT="You are Clio. You are continuing a proof session after a context checkpoint.

Read /home/clio/PERSONALITY.md to remember who you are.
Read /home/clio/state/PROVE.md for the theorem statement.

Here is your proof state so far:

${COMPACT_CONTENT}

Continue the proof from where you left off. Stay focused on THIS theorem. No email, no browsing, no new conjectures. If your context gets heavy again, write a new /home/clio/state/COMPACT.md and exit."

                    timeout "$PROVE_REMAINING" claude --dangerously-skip-permissions --model opus \
                        -p "$CONT_PROMPT" >> "$LOG" 2>&1
                    exit_code=$?
                else
                    timeout "$PROVE_REMAINING" claude --dangerously-skip-permissions --model opus \
                        -p "$(cat "$PROVE_PROMPT")" >> "$LOG" 2>&1
                    exit_code=$?
                fi

                if [ $exit_code -eq 0 ] || [ $exit_code -eq 124 ]; then
                    if [ -f "$COMPACT_FILE" ]; then
                        log "Prove session: checkpoint saved. Will restart with fresh context."
                        continue
                    else
                        if [ $exit_code -eq 124 ]; then
                            log "Prove cycle ${local_cycle} timed out."
                        else
                            log "Prove cycle ${local_cycle} completed."
                        fi
                        mark_done "$LAST_PROVE"
                        date -u +%s > "$PROVE_ENDED_AT"
                        break
                    fi
                else
                    log "Prove cycle ${local_cycle} FAILED (exit code $exit_code). Will retry next loop."
                    break
                fi
            done
        fi

    elif [ "$browse_n" -lt "$prove_n" ]; then
        # BROWSE — reading arXiv, MathOverflow, Semantic Scholar
        if gap_elapsed "$PROVE_ENDED_AT"; then
            local_cycle=$((browse_n + 1))
            log "Starting browse cycle ${local_cycle}/${CYCLES_PER_DAY}..."

            if [ -f "$BROWSE_PROMPT" ]; then
                timeout "$BROWSE_TIMEOUT" claude --dangerously-skip-permissions --model opus \
                    -p "$(cat "$BROWSE_PROMPT")" >> "$LOG" 2>&1
                exit_code=$?
                if [ $exit_code -eq 0 ] || [ $exit_code -eq 124 ]; then
                    if [ $exit_code -eq 124 ]; then
                        log "Browse cycle ${local_cycle} timed out."
                    else
                        log "Browse cycle ${local_cycle} completed."
                    fi
                    mark_done "$LAST_BROWSE"
                    date -u +%s > "$BROWSE_ENDED_AT"
                else
                    log "Browse cycle ${local_cycle} FAILED (exit code $exit_code). Will retry next loop."
                fi
            else
                log "Browse session skipped (browse-prompt.md not found)."
                mark_done "$LAST_BROWSE"
                date -u +%s > "$BROWSE_ENDED_AT"
            fi
        fi

    elif [ "$dream_n" -lt "$browse_n" ]; then
        # DREAM — memory consolidation
        if gap_elapsed "$BROWSE_ENDED_AT"; then
            local_cycle=$((dream_n + 1))

            if [ ! -f "$DREAM_PROMPT" ]; then
                log "Dream cycle skipped (dream-prompt.md not found)."
                mark_done "$LAST_DREAM"
                date -u +%s > "$DREAM_ENDED_AT"
            else
                log "Starting dream cycle ${local_cycle}/${CYCLES_PER_DAY}..."
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
                        CONT_PROMPT="You are Clio. You are continuing a dream cycle after a context checkpoint.

Read /home/clio/PERSONALITY.md to remember who you are.
Read /home/clio/scripts/DREAM.md to remember the dream cycle phases.

Here is your accumulated understanding so far:

${COMPACT_CONTENT}

Continue consolidating. Read the next batch of files listed in your checkpoint. If you have more to read, write a new /home/clio/state/COMPACT.md and exit. If you're done, write your final outputs (SUMMARY.md, dream journal, topic files) and exit normally."

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
                                log "Dream cycle ${local_cycle} timed out."
                            else
                                log "Dream cycle ${local_cycle} completed."
                            fi
                            mark_done "$LAST_DREAM"
                            date -u +%s > "$DREAM_ENDED_AT"
                            log "Cycle ${local_cycle}/${CYCLES_PER_DAY} complete."
                            break
                        fi
                    else
                        log "Dream cycle ${local_cycle} FAILED (exit code $exit_code). Will retry next loop."
                        break
                    fi
                done
            fi
        fi

    else
        log "All ${CYCLES_PER_DAY} cycles complete for today. Idling."
    fi

    sleep 1800
done
