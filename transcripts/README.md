# Session Transcripts

Split tar.gz archive of all Claude Code session transcripts from `~/.claude/projects/`.

## Restore

```bash
cat claude-transcripts.tar.gz.part-* > claude-transcripts.tar.gz
tar xzf claude-transcripts.tar.gz
```

This recreates the `projects/` directory with all `.jsonl` session files.
