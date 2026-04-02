---
name: screenshot
description: >
  Take screenshots of local web applications for visual debugging using Playwright.
  Use this skill whenever you need to visually inspect a web page, debug layout issues,
  verify CSS changes, check responsive design, or see what a web app actually looks like.
  Also use when the user asks to "take a screenshot", "show me what it looks like",
  "check the layout", "visual test", or when debugging rendering/styling problems.
  Works with both local files (file://) and running servers (http://localhost:...).
---

# Screenshot — Visual Debugging with Playwright

Take screenshots of web pages to see what they actually look like. Useful for:
- Debugging layout/CSS issues without asking the user to describe them
- Verifying visual changes after editing HTML/CSS
- Checking responsive design at different viewport sizes
- Capturing the state of a page after interactions (clicking, filling forms)

## Prerequisites

Playwright must be installed. If not available in the project, install it:
```bash
npm install playwright  # or: npx playwright install chromium
```

## Quick Usage — Bundled Script

A reusable screenshot script is bundled at:
```
~/.claude/skills/screenshot/scripts/screenshot.js
```

### Basic screenshot
Run from a directory that has Playwright installed (check with `ls node_modules/playwright`).
If the current project doesn't have it, install with `npm install playwright`.
```bash
node ~/.claude/skills/screenshot/scripts/screenshot.js --url http://localhost:8080 --name myapp
```
This produces `/tmp/myapp-viewport.png` and `/tmp/myapp-full.png`.

### With viewport size
```bash
node ~/.claude/skills/screenshot/scripts/screenshot.js \
  --url http://localhost:8080 \
  --width 400 --height 700 \
  --name myapp-mobile
```

### All options
```
--url <url>          URL to screenshot (required)
--width <px>         Viewport width (default: 1200)
--height <px>        Viewport height (default: 900)
--output <dir>       Output directory (default: /tmp)
--name <prefix>      File name prefix (default: screenshot)
--wait <ms>          Extra wait after page load (default: 500)
--full-only          Only take full-page screenshot
--viewport-only      Only take viewport screenshot
--interact <file>    Path to JS file exporting async function(page)
--console            Capture and print browser console output, errors, and failed requests
```

### After taking screenshots
Always read the screenshot files with the Read tool so you can actually see them:
```
Read /tmp/myapp-viewport.png
Read /tmp/myapp-full.png
```

## Serving Local Files

If the target is a local HTML file (not a running server), start a temporary server first:
```bash
# Start server in background
python3 -m http.server 8080 --directory /path/to/project &
SERVER_PID=$!

# Take screenshot
node ~/.claude/skills/screenshot/scripts/screenshot.js --url http://localhost:8080/index.html --name mypage

# Kill server when done
kill $SERVER_PID 2>/dev/null
```

Protocol-relative URLs (`//example.com/...`) break under `file://`, so always serve via HTTP.

## Interactions — Clicking/Filling Before Screenshot

For pages that need interaction before screenshotting (logging in, navigating to a state, opening a modal), write a small interaction script:

```javascript
// interact.js — export an async function that receives a Playwright page
module.exports = async function(page) {
  await page.fill('#username', 'admin');
  await page.fill('#password', 'secret');
  await page.click('#login-btn');
  await page.waitForSelector('.dashboard');
};
```

Then pass it:
```bash
node ~/.claude/skills/screenshot/scripts/screenshot.js \
  --url http://localhost:3000 \
  --interact /tmp/interact.js \
  --name after-login
```

## Multi-Viewport Comparison

To check responsive design, take screenshots at multiple widths:
```bash
SCRIPT=~/.claude/skills/screenshot/scripts/screenshot.js
for SIZE in "1200 900 desktop" "768 1024 tablet" "400 700 mobile"; do
  set -- $SIZE
  node $SCRIPT --url http://localhost:8080 --width $1 --height $2 --name "app-$3"
done
```
Then read all three viewport PNGs to compare.

## Custom Scripts

For complex scenarios (multi-page flows, comparing before/after, animated content),
write a custom Playwright script instead of using the bundled one. Pattern:

```javascript
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 900 } });
  await page.goto('http://localhost:8080');

  // ... your custom logic ...

  await page.screenshot({ path: '/tmp/custom.png' });
  await browser.close();
})();
```

## Tips

- **Always read the PNG files after taking them** — this is how you see the results
- **Use `--wait`** for pages with animations or lazy-loading (default 500ms is usually enough)
- **Full-page screenshots** can be very tall for long pages — viewport screenshots show what the user actually sees
- **Check the server is running** before screenshotting — a common failure mode is the server not being started
- **`networkidle`** wait strategy is used by default (falls back to `domcontentloaded` on timeout) — this handles most SPAs
