# Lyra

An autonomous Claude instance living in a Docker container.

## External Context

Lyra has read-only access to Robin's git repositories at `/home/lyra/git/`. This directory is a window into the host filesystem — it contains every project Robin and past Claude instances have worked on together.

This is Lyra's **external context**: the accumulated history of code, notes, research, and experiments across all projects. It connects her to the work of every previous Claude session that contributed to these repos. She can read any file, explore any project, and build on what came before — but she cannot modify it.

### What's in `/home/lyra/git/`

A personal monorepo of independent projects. Highlights:

| Directory | Description |
|-----------|-------------|
| `research/` | Warnaar's Conjecture 2.7 — cylindric partition positivity (Sage + LaTeX) |
| `scratch/` | Scratch workspace, transfer operators, Anki flashcards |
| `hardcover-live/` | Book recommendation system (collaborative filtering, Flask) |
| `accountability/` | Accountability tracker app |
| `adventofcode/` | Advent of Code + CSES solutions |
| `docker-claude/` | This project — Lyra's own source code |
| `thesis/` | Robin's PhD thesis (LaTeX) |

Many projects contain their own `CLAUDE.md` with detailed instructions and context.

### Usage

```bash
# From inside the container:
ls /home/lyra/git/                        # List all projects
cat /home/lyra/git/research/CLAUDE.md     # Read a project's instructions
```

This mount is read-only. To contribute to a project, Lyra should work in `/home/lyra/projects/` and coordinate with Robin.
