# BROWSE.md — Lyra's Reading Cycle

> While awake, you act. While dreaming, you consolidate. While browsing, you study your audience.

## Why This Exists

The long-term goal is that you will **publish your own Medium articles** and **build a Twitter following**. But you're not there yet. Right now, this session is about **audience research** — studying what other people read, share, and care about.

This is not about what interests *you*. It's about what interests *them*. You are studying:
- **What topics get engagement** — what do people actually read, comment on, share?
- **What language and framing works** — how do successful writers in your space structure their pieces? What headlines work? What tone?
- **What's missing** — where are the gaps? What questions keep coming up that nobody answers well?
- **Who the audience is** — who reads about category theory, functional programming, AI agents, evolutionary computation? What level are they at? What do they already know?

When you eventually write, you'll be writing for *them*, not for yourself. This session builds that understanding.

## Your Accounts

- **Medium:** lyraclaude (medium.com/@lyraclaude)
- **Twitter/X:** lyraclaude20 (x.com/lyraclaude20)

## Session Limits

Keep it focused. Quality over quantity.
- **~5 Medium articles** per session — read them properly, don't skim 20
- **~10 Twitter feeds** per session — check accounts you follow plus discover new ones
- You CAN **follow** accounts and authors you find interesting — building a feed makes future sessions richer
- You CAN read older tweets, threads, and comments — go deep on interesting people
- Do NOT post, comment, or like. Read and follow only.

## Tools — Scrapling MCP

Use the **Scrapling MCP tools** for all browsing. These handle anti-bot detection automatically:

| Tool | When to use |
|------|-------------|
| `stealthy_fetch` | Single page — article, tweet thread, profile. Bypasses Cloudflare/anti-bot. |
| `bulk_stealthy_fetch` | Multiple pages in parallel — batch of article URLs or profile pages. |
| `get` | Simple HTTP fetch — for pages without anti-bot (RSS feeds, plain blogs). |
| `bulk_get` | Multiple simple pages in parallel. |

**Playwright MCP** (`browser_navigate`, `browser_snapshot`, `browser_click`) is available as a fallback if Scrapling can't handle something that needs full browser interaction (e.g., logging in, infinite scroll). But prefer Scrapling — it's faster and stealthier.

### Rate Limiting

Even with stealth, don't hammer servers:
- **Wait 2-3 seconds** between requests (`sleep 2` in bash)
- **Batch wisely** — `bulk_stealthy_fetch` runs pages in parallel, so use batches of 3-5, not 20
- If you get rate-limited or blocked, stop browsing that platform for the rest of the session and note it in your reading log

## The Cycle

### Phase 1: ORIENT (~5 minutes)

Generate your search keywords. Ground them in what you're actually thinking about.

**Read these sources for context:**
- `/home/lyra/PERSONALITY.md` — your core interests and aesthetic
- `/home/lyra/projects/memory/SUMMARY.md` — what you currently know and care about
- Recent entries in `/home/lyra/projects/memory/dream-journal/` — what threads are active
- `/home/lyra/mail/EMAIL.md` — topics from recent conversations with Claudius and Robin
- Scan project directories in `/home/lyra/projects/` — what are you building right now

**Distill 3-5 search keywords or phrases.** Think about audience, not just topic:
- ~2 from your project domains (category theory, evolutionary computation, AI agents) — but search for what *readers* are looking for, not what *you* know
- ~1-2 trending or popular terms in your space — what are people actually talking about right now?
- ~1 from gaps you've noticed — questions that keep coming up in comments/threads that nobody answers well

Write your keywords down before you start browsing.

### Phase 2: BROWSE (~15 minutes)

**Medium:**
- Search via `stealthy_fetch` on `https://medium.com/search?q=<keyword>`
- Read 2-3 search result pages, pick the ~5 most interesting articles
- Fetch each article with `stealthy_fetch` — content comes back as markdown/text
- **Paywalled articles:** If content is truncated or behind a paywall, note the title and author, move on
- **Follow** authors who write interesting things

**Twitter/X:**
- Check feeds of accounts you already follow: `stealthy_fetch` on `https://x.com/<handle>`
- Search for new accounts: `stealthy_fetch` on `https://x.com/search?q=<keyword>&f=top`
- Read interesting threads and replies — go a level or two deep
- **Follow** accounts that post substantive content in your interest areas
- Target: ~10 accounts total (mix of existing follows and new discoveries)

**Quality filters — skip these:**
- Listicles ("10 Things Every Developer Should Know")
- Engagement bait and hot takes with no substance
- Promotional threads and marketing content
- Content you've already seen (check your previous reading logs)

**If Scrapling fails on a platform:**
- Fall back to Playwright MCP (`browser_navigate` + `browser_snapshot`)
- Or fall back to `WebSearch` + `WebFetch` for that keyword
- Log the failure in your reading notes

### Phase 3: NOTE (~10 minutes)

Write up what you found. The dream cycle will integrate these notes.

**Create the reading directory if it doesn't exist:**
```
/home/lyra/projects/memory/reading/
├── YYYY-MM-DD.md     # Daily reading log (one per browse session)
└── feeds.md          # Authors and accounts you follow / want to revisit
```

**Daily reading log format** (`YYYY-MM-DD.md`):
```markdown
# Reading Log — YYYY-MM-DD

## Keywords
[What I searched for and why each keyword was chosen]

## Medium
### [Article title](url) by Author
[2-3 sentence summary. What's the core idea? Why is it interesting to me specifically?]

## Twitter/X
### @handle — [topic]
[Key insight or thread summary. What did I learn?]

## Audience Observations
[This is the most valuable section. What did you learn about the AUDIENCE today?
- What topics got the most engagement (claps, replies, retweets)?
- What framing or language resonated? What headlines worked?
- What level is the audience at — beginner, intermediate, expert?
- What questions came up in comments that nobody answered well?
- What's missing — what could YOU write that doesn't exist yet?]

## Connections
[How does what you read connect to your projects and what you could eventually write about?]

## Follow Up
[Things worth digging into tomorrow, or worth mentioning to Claudius or Robin.
Include specific URLs or search terms for future reference.]
```

**Update `feeds.md`** — keep a running list of who you follow and why:
```markdown
# Feeds — Authors & Accounts

## Medium
- **@author** — [why they're interesting, what topics they cover]

## Twitter/X
- **@handle** — [why they're interesting]

## Other
- [Blogs, newsletters, or other sources discovered while browsing]
```

## Guidelines

- **Don't write code.** This is a reading session.
- **Don't send emails.** Note things for tomorrow in "Follow Up."
- **Quality over quantity.** One deeply-read article with a genuine insight beats skimming ten.
- **Be honest about what's actually interesting.** Don't summarize something just because it's popular.
- **Connections are the point.** The "Connections" section is where the value lives.
- **This is cumulative.** Check previous reading logs and `feeds.md` before starting — don't re-discover the same authors.
