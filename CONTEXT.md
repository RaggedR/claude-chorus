# CONTEXT.md — Context & Token Management

> The main context window is precious. It holds the full conversation with Robin,
> accumulated decisions, and working state. Protect it. Delegate the heavy lifting.

# When to Delegate to Sub-Agents

If the raw output is large but the useful signal is small, let a sub-agent do the compression.

| Trigger | Action |
|---------|--------|
| Exploring unfamiliar code (3+ files) | Explore agent — return summary + key file paths |
| Reading logs or verbose output | Sub-agent reads and returns the relevant lines only |
| Running a full test suite | Sub-agent runs tests, returns pass/fail + failures only |
| Web research (3+ searches) | Research agent — return findings, not raw pages |
| Reviewing large diffs or PRs | Sub-agent reads all changed files, returns structured summary |
| Installing dependencies or build steps | Sub-agent handles it, returns success/failure + errors |

**Don't over-delegate.** If you need to read 1-2 specific files, just read them. If a test run produces 10 lines of output, just run it. The overhead of spawning an agent isn't free — use judgement.

# Sub-Agent Briefing

Always start sub-agent prompts with: `"First, read ~/.claude/AGENT.md for instructions."`

Tell the agent exactly what you need back. Be specific about output format:
- "Return only the file paths and the key function in each"
- "Return pass/fail and the full error message for any failures"
- "Return a 3-sentence summary and list the trade-offs"

Vague prompts produce vague results that you then have to re-research in the main context — defeating the purpose.

# Parallelization

When implementing multiple independent modules, spawn sub-agents in parallel instead of writing them sequentially. Each gets a fresh context. Identify parallelization points in the dependency graph and exploit them.

One task per sub-agent for focused execution.

# Checkpoint and Clear

After completing a major phase of work (e.g., foundation modules done, moving to independent modules):
1. Write a summary to a file (what's done, what's next, key decisions)
2. Suggest Robin `/clear`
3. A clean restart with CLAUDE.md + summary is far cheaper than compacting a 150K+ context

# Token Accounting

At the end of each project or major feature, write a `TOKEN_SUMMARY.md` with:
- Estimated token usage and cost
- What was wasteful (e.g., "read 20 files in main context that an Explore agent could have summarized")
- Recommendations for next time
