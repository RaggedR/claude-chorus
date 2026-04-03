---
name: read-logs
description: Read and analyze backend server logs and console output from Node.js applications. Use when debugging errors, investigating crashes, or reviewing application behavior.
---

# Read Logs

Automatically find and read backend and console logs for the current project.

## Step 1: Locate Logs

Search for log sources in this order:

1. **Running processes**: Check for running Node.js/npm dev servers
   - `lsof -i -P | grep node` to find running Node processes
   - `ps aux | grep -E 'node|npm|next|vite|express'` to find server processes

2. **Log files on disk**: Search the project for log files
   - `*.log` files in the project root and common subdirectories
   - `logs/` directory if it exists
   - `npm-debug.log`, `yarn-error.log`, `yarn-debug.log`
   - `.next/` logs for Next.js projects
   - `tmp/` or `var/` directories

3. **PM2 logs** (if pm2 is installed):
   - `pm2 logs --lines 100 --nostream`

4. **Package manager output**:
   - Check for recent build errors in `node_modules/.cache/`

## Step 2: Read and Parse

- For log files: read the last 200 lines (use `tail -200`) to focus on recent output
- For large logs: use Grep to filter for ERROR, WARN, Error, TypeError, ReferenceError, FATAL, UnhandledPromiseRejection, ECONNREFUSED, ENOENT
- Identify timestamps and group related entries
- Extract full stack traces (don't truncate them)

## Step 3: Summarize

Provide a structured summary:

### Errors Found
- List each distinct error with its timestamp, message, and file:line reference

### Warnings
- List warnings that may be relevant

### Recent Activity
- Brief overview of what the server has been doing

### Suggested Fixes
- For each error, suggest a concrete fix or debugging step

## Arguments

If the user provides arguments, treat them as:
- A file path to read directly: `$ARGUMENTS`
- Or a keyword to grep for in logs: `grep -i "$ARGUMENTS"` across log files
