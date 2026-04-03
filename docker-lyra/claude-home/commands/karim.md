---
argument-hint: [commit-message]
description: Commit, PR, strict Maxwell review loop, merge → auto-deploy
---

# Karim — Ship with strict review

Commit changes, create a PR, get Maxwell's review, fix EVERYTHING (issues AND suggestions), re-review until spotless, then merge. CD auto-deploys on merge to main (if configured).

## Your Task

Ship the current changes with optional commit message: $ARGUMENTS

## Step 0: Repo initialization (first time only)

Skip this step if `.claude/ship-initialized` exists.

```bash
if [ -f ".claude/ship-initialized" ]; then
  echo "Repo already initialized, skipping Step 0"
fi
```

**If not initialized**, ask the user to confirm the repo name and set everything up:

### 0a. Confirm the repo

```bash
REPO=$(gh repo view --json nameWithOwner -q '.nameWithOwner' 2>/dev/null || echo "")
```

If `REPO` is empty (no remote yet), ask the user: **"What should the GitHub repo be called?"** Then create it:

```bash
gh repo create <owner>/<name> --private --source=. --push
```

If `REPO` exists, confirm with the user: "Shipping to `<REPO>` — correct?"

### 0b. Add reviewers as collaborators

Source credentials and invite MaxwellMergeSlam (and KelvinBitBrawler if available):

```bash
source ~/.enspyr-claude-skills/.env 2>/dev/null || source .env 2>/dev/null
REPO=$(gh repo view --json nameWithOwner -q '.nameWithOwner')

# Check if already a collaborator
if ! gh api repos/$REPO/collaborators/MaxwellMergeSlam 2>/dev/null; then
  if [ -n "$ENSPYR_ADMIN_PAT" ]; then
    # Invite
    curl -s -X PUT \
      -H "Authorization: Bearer $ENSPYR_ADMIN_PAT" \
      -H "Accept: application/vnd.github+json" \
      "https://api.github.com/repos/$REPO/collaborators/MaxwellMergeSlam" \
      -d '{"permission":"push"}'

    # Accept invitation
    INVITE_ID=$(curl -s -H "Authorization: Bearer $MAXWELL_PAT" \
      "https://api.github.com/user/repository_invitations" | \
      jq -r ".[] | select(.repository.full_name==\"$REPO\") | .id")
    [ -n "$INVITE_ID" ] && curl -s -X PATCH \
      -H "Authorization: Bearer $MAXWELL_PAT" \
      "https://api.github.com/user/repository_invitations/$INVITE_ID"
  else
    echo "ENSPYR_ADMIN_PAT not set. Ask a repo admin to add MaxwellMergeSlam as collaborator."
  fi
fi
```

### 0c. Set up branch protection

```bash
BASE_BRANCH=$(gh repo view --json defaultBranchRef -q '.defaultBranchRef.name')

# Check if protection already exists
if ! gh api repos/$REPO/branches/$BASE_BRANCH/protection 2>/dev/null; then
  gh api repos/$REPO/branches/$BASE_BRANCH/protection -X PUT \
    -H "Accept: application/vnd.github+json" \
    -f "required_pull_request_reviews[required_approving_review_count]=1" \
    -f "required_pull_request_reviews[dismiss_stale_reviews]=true" \
    -f "enforce_admins=false" \
    -f "required_status_checks=null" \
    -f "restrictions=null"
fi
```

### 0d. Create CI workflow (if none exists)

If `.github/workflows/` has no CI files, auto-detect the stack and create a `ci.yml` with two jobs:

**Job 1: `test`** (auto-detected, runs on every PR and push to main):
- Has `package.json` → Node.js: `npm ci && npm run lint && npm run build && npm test`
- Has `pubspec.yaml` → Flutter: `flutter pub get && flutter analyze && flutter test`
- Has `Makefile` with `test` target → `make test`
- Has `pyproject.toml` / `requirements.txt` → Python: `pip install -r requirements.txt && pytest`

**Job 2: `deploy`** (generic wrapper, runs only on push to main):
```yaml
deploy:
  needs: test
  runs-on: ubuntu-latest
  if: github.event_name == 'push' && github.ref == 'refs/heads/main'
  steps:
    - uses: actions/checkout@v4
    - name: Deploy
      run: |
        if [ -f "./scripts/deploy.sh" ]; then
          chmod +x ./scripts/deploy.sh
          ./scripts/deploy.sh
        else
          echo "No deploy script found, skipping deploy"
        fi
```

The deploy job calls `scripts/deploy.sh` if it exists. This script is **project-specific** and NOT auto-generated — it's created in a separate conversation with the user where they decide the deploy target (Cloud Run, Vercel, Firebase Hosting, etc.). To change deploy strategy later, just edit `scripts/deploy.sh`.

Check `.claude/ship-config.md` for `ci: none` or `ci: skip` to opt out.

If CI was created, update branch protection to require the `test` status check.

### 0e. Mark as initialized

```bash
mkdir -p .claude
cat > .claude/ship-initialized << INIT_EOF
initialized=$(date -Iseconds)
reviewer=MaxwellMergeSlam
repo=$REPO
INIT_EOF
git add .claude/ship-initialized .github/workflows/ 2>/dev/null
git commit -m "chore: initialize shipping workflow

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
git push
```

---

## Step 1: Check for changes

```bash
git status
git diff --stat
```

If there are no changes, stop.

## Step 2: Run tests locally

Detect and run the project's test command:

1. Check `.claude/ship-config.md` for `test-command` setting
2. If not configured, auto-detect:
   - Has `package.json` with `test` script → `npm test`
   - Has `pubspec.yaml` → `flutter test`
   - Has `Makefile` with `test` target → `make test`
   - Has `pytest.ini` or `pyproject.toml` with pytest → `pytest`
   - `test-command: none` or nothing detected → skip
3. If tests fail, stop and fix them before proceeding.

## Step 3: Create branch and commit

If on main, create a feature branch from the changes:

```bash
# Generate branch name from changes (e.g., feat/add-auth, fix/lint-errors)
git checkout -b <branch-name>
```

Stage relevant files. NEVER stage:
- `.env`, credentials, secrets
- Large binaries, `.epub`, `.pdf` (unless they're project files)
- Personal/unrelated files

Commit message rules:
- Use conventional commits: `type(scope): description`
- If `$ARGUMENTS` is provided, use it as the commit message
- Otherwise, generate from the diff
- End with `Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>`

```bash
git add <specific-files>
git commit -m "$(cat <<'EOF'
type(scope): description

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

## Step 4: Push and create PR

```bash
git push -u origin <branch-name>

gh pr create --title "PR title" --body "$(cat <<'EOF'
## Summary
- Brief description of changes

## Test plan
- [ ] All unit tests pass
- [ ] All E2E tests pass
- [ ] Lint clean

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

**CI starts automatically here** — GitHub Actions triggers on `pull_request`. CI (lint, build, unit tests, E2E tests) runs in parallel with Maxwell's review.

## Step 5: Maxwell reviews (parallel with CI)

Source the environment and post the review:

```bash
source ~/.enspyr-claude-skills/.env 2>/dev/null || source .env 2>/dev/null
```

Then run `/pr-review <PR_NUMBER>` to get Maxwell's review.

While waiting for the review response, check if CI has finished:

```bash
gh pr checks <PR_NUMBER>
```

## Step 6: The strict review + CI loop

**Both gates must pass before merge. Do NOT skip either.**

### Gate 1: Maxwell's review must be spotless

After Maxwell's review:

1. Read ALL issues AND suggestions from the review (even if verdict is APPROVE)
2. If there are ANY issues or suggestions:
   a. Fix every single one — issues AND suggestions, no exceptions
   b. Run tests locally to verify fixes don't break anything
   c. Commit and push the fixes (this re-triggers CI automatically)
   d. Re-request review from Maxwell: run `/pr-review <PR_NUMBER>` again
   e. Go back to step 1
3. Only proceed when Maxwell's review has ZERO issues AND ZERO suggestions

**Rules:**
- "Suggestions" are NOT optional. Fix them all.
- Even if Maxwell says APPROVE, if there are suggestions listed, fix them and get another review
- The loop ends ONLY when the review body contains no actionable feedback

### Gate 2: CI must be green

Before merging, check CI status:

```bash
gh pr checks <PR_NUMBER>
```

- If CI is still running, wait and re-check (poll every 30s, max 10 min)
- If CI failed, read the failure logs, fix the issue, commit and push (re-triggers both CI and needs a new Maxwell review)
- Only proceed to merge when ALL checks show ✓ pass

**If a fix is pushed for CI, you must also get a fresh Maxwell review on the new code.**

## Step 7: Merge

Only after BOTH gates pass (clean review + green CI):

```bash
# Check for stacked PRs
PR_BRANCH=$(gh pr view --json headRefName -q '.headRefName')
DOWNSTREAM=$(gh pr list --base "$PR_BRANCH" --json number -q '.[].number' 2>/dev/null)

if [ -n "$DOWNSTREAM" ]; then
  gh pr merge --squash
  for pr in $DOWNSTREAM; do
    gh pr edit $pr --base main
  done
  git push origin --delete "$PR_BRANCH" 2>/dev/null || true
else
  gh pr merge --squash --delete-branch
fi
```

## Step 8: Verify deploy

After merge, CI runs again on the `push` to main trigger. If the project has a deploy job configured, it runs after tests pass.

```bash
# Find the CI run triggered by the merge to main
sleep 10
RUN_ID=$(gh run list --branch main --limit 1 --json databaseId -q '.[0].databaseId')
echo "CI run: $RUN_ID"
gh run view $RUN_ID --json jobs --jq '.jobs[] | {name: .name, status: .status, conclusion: .conclusion}'
```

If the run is still in progress, report the run ID so the user can check later. Do NOT block waiting for it — just tell the user:

> CI run #<RUN_ID> is in progress. Check with: `gh run view <RUN_ID>`

## Step 9: Report

```markdown
## Shipped 🚀

- **Branch:** <branch-name>
- **PR:** #<number> — <title>
- **Reviews:** <N> rounds until clean
- **CI:** ✅ All checks passed on PR
- **Merged:** squash merge to main
- **Deploy:** CI run #<RUN_ID> triggered — CD will auto-deploy if configured

Check deploy status: `gh run view <RUN_ID>`
```

## Safety

- NEVER force-push
- NEVER commit secrets or .env files
- NEVER merge with failing CI
- NEVER merge with unaddressed review feedback
- NEVER skip the review loop
- NEVER block waiting for long CI runs — report the run ID and move on
