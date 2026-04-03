# Project Memory

## PR Reviews
- User prefers PR reviews to be handled by Maxwell (MaxwellMergeSlam) remotely, NOT done locally by Claude Code. Don't run tests/analysis locally for reviews.
- **Strict review loop**: Address ALL issues AND suggestions (even if verdict is APPROVE). Re-request review from Maxwell. Repeat until zero issues/suggestions. Only then merge.

## CI/CD
- CI: lint + build + vitest (frontend + server) + Playwright E2E on every PR
- CD: Auto-deploy to Cloud Run on merge to main via Workload Identity Federation
- GCP project: `russian-transcription`, service: `russian-transcription`, region: `us-central1`
- Ship config at `.claude/ship-config.md`
