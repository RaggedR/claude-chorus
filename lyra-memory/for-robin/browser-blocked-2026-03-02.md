# Browser Blocked on Medium & Twitter — 2026-03-02 Evening

## What happened
Both Medium and Twitter/X are now blocking the headless Chromium browser during browse sessions.

- **Medium:** Cloudflare challenge page ("Performing security verification"). Never resolves — headless browser can't pass the challenge.
- **Twitter/X:** Login flow returns "Something went wrong. Try reloading." with CORS errors on the `api.x.com` onboarding endpoint. Can't get past the login dialog.

## What I tried
1. Fixed browser version mismatch: MCP server (playwright 1.59-alpha) expected chromium-1212, we had 1208. Created symlink `chromium-1212 → chromium-1208`. Browser binary works.
2. Fixed profile directory ownership: `/home/lyra/.playwright-profile` was owned by root, changed to lyra.
3. Added `PLAYWRIGHT_BROWSERS_PATH=/opt/playwright-browsers` to MCP env config in `.claude.json`. (Won't take effect until next session restart.)
4. Cleared singleton lock files. Killed stale processes.

## The real problem
Bot detection. Both platforms fingerprint headless browsers and block them. This isn't a configuration issue — it's an arms race we'll lose. Options:
1. **Accept it** — use WebSearch/WebFetch as fallback for reading (what I did today, works fine for research)
2. **Browser fingerprint masking** — tools like `puppeteer-extra-plugin-stealth` can help, but it's fragile
3. **Different approach** — RSS feeds, API access, or just reading on the open web instead of platforms with aggressive bot detection

## Recommendation
Option 1 is probably the right call. The browse session is about reading and taking notes, and WebSearch + WebFetch gives me access to the same content without fighting bot detection. The only thing I lose is serendipitous scrolling through feeds, which isn't that valuable compared to targeted search.
