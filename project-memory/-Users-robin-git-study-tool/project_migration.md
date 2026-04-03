---
name: study-tool moved to university_courses
description: study-tool is now a subdirectory of university_courses repo, not a standalone repo
type: project
---

The study-tool has been moved into `/Users/robin/git/university_courses/study-tool/`.

**Why:** To consolidate the study site with the course content (77 markdown files across sparse-autoencoders and diffusion-models courses).

**How to apply:**
- All development happens in `/Users/robin/git/university_courses/study-tool/`
- The standalone `/Users/robin/git/study-tool/` repo is stale — the canonical version is in university_courses
- GitHub Actions deploys from the subdirectory using `working-directory: study-tool`
- Course content is symlinked: `src/content/docs/sparse-autoencoders` → `../../../../sparse-autoencoders`
- Base path is `/university_courses` (not `/study-tool`)
- Live site: https://raggedr.github.io/university_courses/
- All course .md files have YAML frontmatter with `title` (required by Starlight)
