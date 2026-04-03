# Reddit Cross-Subreddit Opinion Tracker

## Overview
A Python CLI tool that tracks how topics are discussed differently across Reddit communities, using parallel sub-agents per subreddit and Claude API for sentiment analysis.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      CLI / Orchestrator                      │
│                      (main.py)                               │
├─────────────────────────────────────────────────────────────┤
│                     Task Coordinator                         │
│              (distributes work, merges results)              │
├──────────┬──────────┬──────────┬──────────┬────────────────┤
│ Agent 1  │ Agent 2  │ Agent 3  │ Agent N  │   (parallel)   │
│ r/tech   │ r/news   │ r/pol    │ r/...    │                │
├──────────┴──────────┴──────────┴──────────┴────────────────┤
│                    Shared Services                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ Reddit API  │  │ Claude API  │  │ Storage (JSON/SQLite)│ │
│  │   (PRAW)    │  │ (analysis)  │  │                     │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Directory Structure

```
reddit/
├── src/
│   ├── __init__.py
│   ├── cli.py              # CLI entry point (argparse)
│   ├── orchestrator.py     # Coordinates agents, merges results
│   ├── agent.py            # SubredditAgent class
│   ├── reddit_client.py    # PRAW wrapper, rate limiting
│   ├── analyzer.py         # Claude API sentiment/opinion extraction
│   ├── storage.py          # JSON file output, optional SQLite
│   └── models.py           # Pydantic models for data structures
├── config/
│   └── default.yaml        # Default subreddit lists, API settings
├── output/                 # Generated analysis results
├── requirements.txt
├── .env.example
└── README.md
```

## Core Components

### 1. CLI (`cli.py`)
```
python -m src.cli track "AI regulation" --subreddits technology,news,politics --mode historical --days 7
python -m src.cli track "AI regulation" --subreddits technology,news,politics --mode realtime
python -m src.cli compare output/analysis_123.json  # View cross-subreddit comparison
```

### 2. Orchestrator (`orchestrator.py`)
- Spawns one `SubredditAgent` per subreddit using `asyncio.gather()`
- Implements rate limiting pool shared across agents
- Merges results into unified analysis
- Handles graceful shutdown on Ctrl+C

### 3. SubredditAgent (`agent.py`)
Each agent independently:
1. Fetches posts matching topic query from its subreddit
2. Retrieves top comments per post
3. Batches content for Claude analysis
4. Returns structured opinion summary

```python
class SubredditAgent:
    async def analyze_topic(self, topic: str, mode: str, timeframe: int) -> SubredditAnalysis:
        posts = await self.fetch_posts(topic, timeframe)
        comments = await self.fetch_comments(posts)
        analysis = await self.analyzer.extract_opinions(posts, comments)
        return SubredditAnalysis(subreddit=self.name, ...)
```

### 4. Analyzer (`analyzer.py`)
Claude API integration for:
- Sentiment classification (positive/negative/neutral/mixed)
- Stance detection (supports/opposes/discusses topic)
- Key arguments extraction
- Notable quotes selection

Batches multiple posts into single API call where possible.

### 5. Models (`models.py`)
```python
class Post(BaseModel):
    id: str
    title: str
    body: str
    score: int
    created_utc: datetime
    num_comments: int

class Opinion(BaseModel):
    sentiment: Literal["positive", "negative", "neutral", "mixed"]
    stance: str
    key_arguments: list[str]
    notable_quotes: list[str]
    confidence: float

class SubredditAnalysis(BaseModel):
    subreddit: str
    topic: str
    post_count: int
    comment_count: int
    overall_sentiment: Opinion
    top_posts: list[Post]
    analyzed_at: datetime

class CrossSubredditReport(BaseModel):
    topic: str
    subreddits: list[SubredditAnalysis]
    consensus_points: list[str]
    divergence_points: list[str]
    summary: str
```

## Data Flow

### Historical Mode
1. User specifies topic + subreddits + timeframe
2. Orchestrator spawns N agents in parallel
3. Each agent searches Reddit for matching posts (PRAW search)
4. Each agent fetches top K comments per post
5. Each agent sends batched content to Claude for analysis
6. Orchestrator collects all SubredditAnalysis results
7. Orchestrator calls Claude to generate cross-subreddit comparison
8. Results saved to JSON file

### Real-time Mode
1. User specifies topic + subreddits
2. Orchestrator spawns N agents
3. Each agent uses PRAW stream to monitor new posts
4. On new matching post, agent queues for analysis
5. Periodic (every 5 min) analysis batches
6. Incremental updates to output file
7. Runs until Ctrl+C

## Key Design Decisions

### Why asyncio for parallelism?
- Reddit API is I/O bound (network requests)
- asyncio handles many concurrent requests efficiently
- Simpler than multiprocessing for this use case
- async-praw (asyncpraw) provides native async Reddit client

### Rate Limiting Strategy
- Reddit API: 60 requests/minute (shared pool across agents)
- Claude API: Configurable, default 10 requests/minute
- Use `asyncio.Semaphore` for both

### Batching for Claude API
- Combine 3-5 posts with their comments into single prompt
- Reduces API calls, maintains context
- ~4000 tokens input per batch typical

## Files to Create

| File | Purpose |
|------|---------|
| `src/__init__.py` | Package init |
| `src/cli.py` | Argument parsing, entry point |
| `src/orchestrator.py` | Agent coordination, result merging |
| `src/agent.py` | SubredditAgent class |
| `src/reddit_client.py` | PRAW wrapper with rate limiting |
| `src/analyzer.py` | Claude API integration |
| `src/storage.py` | JSON output handling |
| `src/models.py` | Pydantic data models |
| `config/default.yaml` | Default configuration |
| `requirements.txt` | Dependencies |
| `.env.example` | Environment variable template |

## Dependencies

```
asyncpraw>=7.7.0      # Async Reddit API
anthropic>=0.18.0     # Claude API
pydantic>=2.0         # Data validation
pyyaml>=6.0           # Config files
python-dotenv>=1.0    # Environment variables
rich>=13.0            # CLI formatting
```

## Verification Plan

1. **Unit tests**: Test each component in isolation with mocked APIs
2. **Integration test**: Run with 2 small subreddits, verify JSON output structure
3. **Manual verification**:
   ```bash
   # Set up credentials
   cp .env.example .env
   # Edit .env with Reddit and Claude API keys

   # Run historical analysis
   python -m src.cli track "python programming" --subreddits learnpython,python --days 1

   # Check output
   cat output/analysis_*.json | python -m json.tool
   ```

## Implementation Order

1. `models.py` - Data structures first
2. `reddit_client.py` - Reddit API wrapper
3. `analyzer.py` - Claude integration
4. `agent.py` - Single subreddit agent
5. `orchestrator.py` - Parallel coordination
6. `storage.py` - Output handling
7. `cli.py` - User interface
8. Config files and documentation
