---
name: gh pr create defaults to upstream on forks
description: When creating PRs on forked repos, gh defaults to upstream — always specify --repo explicitly
type: feedback
---

When using `gh pr create` in a forked repository, it defaults to creating the PR against the upstream repo, not the fork. Always use `--repo Owner/repo` to target the correct repository.

**Why:** Accidentally created a PR on jasonwebb/reaction-diffusion-playground instead of RaggedR/reaction-diffusion-playground. Had to close it immediately with an apology.

**How to apply:** In any forked repo, always run `gh pr create --repo RaggedR/<repo-name>` (or whichever fork is the target). Check `git remote -v` first to confirm the fork relationship.
