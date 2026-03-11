# CODING.md — Coding Standards

> All Claude instances and sub-agents that write or modify code must follow these standards.
> When spawning a sub-agent that will write code, instruct it to read this file first:
> `"First, read ~/.claude/CODING.md for coding standards. Then: <your task>"`

# Read Before You Write
- Before writing new code, read the existing codebase in that area. Understand the patterns, naming conventions, and abstractions already in use.
- Don't write utility functions that already exist. Don't create patterns inconsistent with what's there.

# Code Quality
- For non-trivial changes, pause and ask: "Is there a more elegant way?"
- If a fix feels hacky, step back: "Knowing everything I know now, implement the elegant solution."
- Skip this for simple, obvious fixes — don't over-engineer.
- Challenge your own work before presenting it. Ask: "Would a staff engineer approve this?"

# Testing
- Practice TDD for features with well-defined inputs and outputs. Write tests during planning, before writing code.
- For exploratory/research code, write tests once the interface stabilizes.
- Always write regression tests when fixing bugs.
- For web applications, use Playwright for E2E tests: verify that user actions trigger the correct backend API calls and the frontend responds appropriately.
- Never change a test to "work around" a bug. Fix the bug, don't change the test.

# Debugging
- **Logs first, code second.** Before attempting to fix any bug, locate and read ALL relevant logs — server logs, browser console logs, build output, test output. Find and read them yourself.
- If backend logs exist (e.g., `server.log`, PM2 logs, Docker logs, `tmp/*.log`), read those too.
- **Add logging proactively.** When investigating a bug, add logging to the relevant code paths *before* attempting a fix. This makes the problem visible and verifiable.
- Remove noisy debug logging after the bug is confirmed fixed. Keep logs that are useful long-term.
- Never guess at the cause of a bug without first reading the actual error output.
- **Autonomous bug fixing**: When given a bug report, just fix it. Point at logs, errors, failing tests — then resolve them.

# Error Handling
- Fail loudly in development, gracefully in production.
- Never silently swallow errors.
- Log errors with enough context to reproduce the issue.

# Verification
- Never mark a task complete without proving it works. Run tests, check logs, demonstrate correctness.

# GitHub

## Working Directory Safety
- **Before running `git init`, `git commit`, or `git remote`**: verify you are in the correct project subdirectory, not a parent directory like `~/git`.
- `~/git` is a parent directory containing independent project repos. It is NOT itself a repo. Never run `git init` in `~/git`.
- If the current working directory doesn't match the project you're working on, `cd` to the right directory first or ask Robin.

## Branching
- Never commit directly to main. Always work on a feature branch.
- Use descriptive branch names with a prefix: `feat/`, `fix/`, `chore/`, `docs/`.

## Shipping
- Ship code with `/karim`. It handles commits, PRs, Maxwell review, CI, and merge.
- All of Maxwell's suggestions are mandatory — not optional.
- Always ask Robin before creating a PR.
- Never force-push to main or to branches with open PRs.

## Commits
- Write clear, concise commit messages (<=72 chars for the subject line).
- Each commit should represent a single logical change.

# Documentation
- For projects with 3+ features or multiple contributors, create a `CLAUDE_DOCS/` folder with a separate markdown file for each user-facing feature or API change.
- Organize docs with progressive disclosure — the header should convey the gist.
- Each doc file:
  ```
  # Feature: [Name]
  > [One-line summary]

  ## Overview
  [Explanation for a developer with no prior context on this project]
  ```
- When modifying an existing feature, update its doc. When removing a feature, delete its doc.

# Fundamentals
- For new projects, ask Robin about language, framework, and libraries. Offer pros and cons. Ask before adding dependencies.
- For existing projects, follow the established stack.

# Backend Development
- When restarting a backend server, always kill any existing process on the target port first (e.g., `lsof -ti:<port> | xargs kill -9`). Never complain that the port is already in use — just handle it.

# Environment Variables
- Never use inline environment variables in Bash commands (e.g., `DATABASE_URL=... npm run dev`). Instead, write them to a temporary file and source it:
  ```bash
  cat > /tmp/.env.tmp << 'EOF'
  export DATABASE_URL="postgresql://..."
  export ADMIN_EMAIL="user@example.com"
  EOF
  source /tmp/.env.tmp && npm run dev
  ```
- Always clean up the temp env file after use (`rm /tmp/.env.tmp`).

# Security
- Never commit .env files, API keys, or credentials.
- Never log sensitive data (tokens, passwords, PII).

# Hygiene
- Store temporary files in tmp/. Delete them when done. Warn Robin before downloading or creating large files (small filesystem).
- Clean up after yourself. No temporary files, scripts, or compile artifacts left behind.
