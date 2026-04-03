#!/usr/bin/env node
// Screenshot tool — takes viewport + full-page screenshots of a URL
// Usage: node screenshot.js [options]
//   --url <url>          URL to screenshot (required)
//   --width <px>         Viewport width (default: 1200)
//   --height <px>        Viewport height (default: 900)
//   --output <dir>       Output directory (default: /tmp)
//   --name <prefix>      File name prefix (default: screenshot)
//   --wait <ms>          Extra wait after load (default: 500)
//   --full-only          Only take full-page screenshot
//   --viewport-only      Only take viewport screenshot
//   --interact <file>    Path to JS module exporting async function(page)
//   --console            Capture and print browser console output

// Resolve playwright from the cwd's node_modules (not the script's location)
const { createRequire } = require('module');
const cwdRequire = createRequire(process.cwd() + '/package.json');
let chromium;
try {
  ({ chromium } = cwdRequire('playwright'));
} catch {
  try {
    ({ chromium } = cwdRequire('@playwright/test'));
  } catch {
    try {
      // Last resort: try from script's own resolution path
      ({ chromium } = require('playwright'));
    } catch {
      console.error('Playwright not found. Run from a project with playwright installed,');
      console.error('or install it: npm install playwright');
      process.exit(1);
    }
  }
}

function parseArgs(argv) {
  const args = { width: 1200, height: 900, output: '/tmp', name: 'screenshot', wait: 500 };
  for (let i = 2; i < argv.length; i++) {
    switch (argv[i]) {
      case '--url': args.url = argv[++i]; break;
      case '--width': args.width = parseInt(argv[++i]); break;
      case '--height': args.height = parseInt(argv[++i]); break;
      case '--output': args.output = argv[++i]; break;
      case '--name': args.name = argv[++i]; break;
      case '--wait': args.wait = parseInt(argv[++i]); break;
      case '--full-only': args.fullOnly = true; break;
      case '--viewport-only': args.viewportOnly = true; break;
      case '--interact': args.interact = argv[++i]; break;
      case '--console': args.console = true; break;
      default:
        if (!args.url && !argv[i].startsWith('--')) args.url = argv[i];
    }
  }
  if (!args.url) {
    console.error('Usage: node screenshot.js --url <url> [--width N] [--height N] [--name prefix] [--interact file.js]');
    process.exit(1);
  }
  return args;
}

(async () => {
  const args = parseArgs(process.argv);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: args.width, height: args.height } });

  // Console capture — attach listeners before navigation so nothing is missed
  const consoleLogs = [];
  if (args.console) {
    page.on('console', msg => {
      consoleLogs.push({ type: msg.type(), text: msg.text() });
    });
    page.on('pageerror', err => {
      consoleLogs.push({ type: 'error', text: err.message });
    });
    page.on('requestfailed', req => {
      consoleLogs.push({ type: 'network-error', text: `${req.failure().errorText}: ${req.url()}` });
    });
  }

  try {
    await page.goto(args.url, { waitUntil: 'networkidle', timeout: 30000 });
  } catch (e) {
    // Fall back to domcontentloaded if networkidle times out
    try {
      await page.goto(args.url, { waitUntil: 'domcontentloaded', timeout: 15000 });
    } catch (e2) {
      console.error('Failed to load:', args.url, e2.message);
      await browser.close();
      process.exit(1);
    }
  }

  // Run interaction script if provided
  if (args.interact) {
    const path = require('path');
    const interactFn = require(path.resolve(args.interact));
    await (typeof interactFn === 'function' ? interactFn : interactFn.default)(page);
  }

  // Extra wait for rendering
  if (args.wait > 0) await page.waitForTimeout(args.wait);

  const files = [];

  if (!args.fullOnly) {
    const vp = `${args.output}/${args.name}-viewport.png`;
    await page.screenshot({ path: vp });
    files.push(vp);
    console.log('Viewport:', vp);
  }

  if (!args.viewportOnly) {
    const fp = `${args.output}/${args.name}-full.png`;
    await page.screenshot({ path: fp, fullPage: true });
    files.push(fp);
    console.log('Full page:', fp);
  }

  // Print captured console output
  if (args.console) {
    console.log('\n=== CONSOLE OUTPUT ===');
    if (consoleLogs.length === 0) {
      console.log('(no console messages)');
    } else {
      for (const log of consoleLogs) {
        console.log(`[${log.type}] ${log.text}`);
      }
    }
    console.log('=== END ===');
  }

  await browser.close();
  console.log('Done.');
})();
