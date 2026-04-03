---
name: check-usage
description: Check API key status and remaining usage/rate limits for Anthropic, OpenAI, and Google AI providers. Reads keys from environment variables only.
---

# Check API Usage

Check the status and rate limits of AI API providers by reading keys from environment variables. **Never ask the user for API keys directly** — only read from env vars.

## Steps

### 1. Detect Available Keys

Check which API keys are set as environment variables:

- `ANTHROPIC_API_KEY` — Anthropic (Claude)
- `OPENAI_API_KEY` — OpenAI (GPT)
- `GOOGLE_API_KEY` or `GEMINI_API_KEY` — Google AI (Gemini)

For each key that is NOT set, report it as "not configured" and skip it.
For each key that IS set, proceed to validate it.

### 2. Validate Keys and Fetch Rate Limits

Run these checks using `curl`. Include `-s` for silent mode and `-w` to capture HTTP status codes. Use `-D -` or `-i` to capture response headers where rate limit info is available.

**Anthropic:**
```bash
curl -s -i https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model":"claude-sonnet-4-5-20250929","max_tokens":1,"messages":[{"role":"user","content":"hi"}]}'
```
Parse these response headers:
- `x-ratelimit-requests-limit` — max requests per minute
- `x-ratelimit-requests-remaining` — requests remaining
- `x-ratelimit-tokens-limit` — max tokens per minute
- `x-ratelimit-tokens-remaining` — tokens remaining
- `x-ratelimit-tokens-reset` — when tokens reset

**OpenAI:**
```bash
curl -s -i https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```
A 200 response means the key is valid. Parse rate limit headers:
- `x-ratelimit-limit-requests`
- `x-ratelimit-remaining-requests`
- `x-ratelimit-limit-tokens`
- `x-ratelimit-remaining-tokens`

**Google AI:**
```bash
curl -s -i "https://generativelanguage.googleapis.com/v1/models?key=$GOOGLE_API_KEY"
```
A 200 response means the key is valid. Google doesn't return rate limit headers here, so just confirm the key works and list available models.

### 3. Present Results

Format the output as a clear summary table:

```
Provider     | Status | Requests Left | Tokens Left    | Resets
-------------|--------|---------------|----------------|-------
Anthropic    | valid  | 45/50 per min | 38,000/40,000  | 42s
OpenAI       | valid  | 58/60 per min | 85,000/90,000  | 28s
Google AI    | valid  | -             | -              | -
```

If a key is invalid (401/403), show "INVALID KEY" in the status column.
If a key is not set, show "NOT SET" in the status column.

### 4. Arguments

If the user provides an argument, filter to that provider only:
- `/check-usage anthropic` — only check Anthropic
- `/check-usage openai` — only check OpenAI
- `/check-usage google` — only check Google AI
