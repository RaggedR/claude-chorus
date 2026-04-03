# Plan: Add Sentry Error Monitoring (Frontend + Backend)

## Context

Errors currently go to `console.error` (captured by Cloud Logging but nobody gets alerted). If OpenAI goes down, yt-dlp breaks, or the usage persistence we just added silently fails, you won't know until a user complains. This is Critical #2 from the production readiness audit.

**Sentry** is an error monitoring SaaS (free tier: 5K errors/mo). It captures errors with full context (stack trace, request data, user) and sends alerts (email, Slack, etc).

## Prerequisites (manual, before or during implementation)

1. Sign up at [sentry.io](https://sentry.io) (free)
2. Create a Sentry project (platform: Node.js / Express)
3. Copy the DSN from Project Settings > Client Keys
4. Create an auth token at Settings > Auth Tokens (scope: `project:releases`, `org:read`) — needed for source map uploads

## Files to Create/Modify

| File | Change |
|------|--------|
| `server/instrument.mjs` | **NEW** — Sentry Node SDK init (runs before all other code via `--import`) |
| `server/index.js` | Import Sentry, add `setupExpressErrorHandler(app)`, add `captureException` in 5 critical catch blocks |
| `server/usage.js` | Import Sentry, add `captureException` in 2 silent-failure catch blocks |
| `server/package.json` | Add `@sentry/node`, update `start`/`dev` scripts for `--import` |
| `server/Dockerfile` | Update CMD: `node --import ./instrument.mjs index.js` |
| `src/sentry.ts` | **NEW** — Frontend Sentry init |
| `src/main.tsx` | Import sentry.ts (first), wrap `<App>` in `Sentry.ErrorBoundary` |
| `src/services/api.ts` | Add `captureException` for 500+ API errors |
| `package.json` | Add `@sentry/react`, `@sentry/vite-plugin` |
| `vite.config.ts` | Enable source maps, add conditional `sentryVitePlugin` |
| `.github/workflows/ci.yml` | Add Sentry secrets to deploy env, update `--set-secrets` |
| `CLAUDE.md` | Document Sentry setup |

**No changes**: tests, `firestore.rules`, `deploy.sh` (CI handles deploys)

## Implementation Steps

### 1. Install dependencies

```bash
cd server && npm install @sentry/node
cd .. && npm install @sentry/react && npm install -D @sentry/vite-plugin
```

### 2. Create `server/instrument.mjs`

This file runs before ANY other code via Node's `--import` flag. It initializes Sentry's monkey-patching of `http`, `fetch`, etc.

```js
import * as Sentry from '@sentry/node';

Sentry.init({
  dsn: process.env.SENTRY_DSN || '',
  enabled: !!process.env.SENTRY_DSN,
  environment: process.env.GCS_BUCKET ? 'production' : 'development',
  tracesSampleRate: 0.2,
  beforeSend(event) {
    if (process.env.VITEST) return null;  // Never send during tests
    return event;
  },
});
```

### 3. Update `server/Dockerfile`

```dockerfile
CMD ["node", "--import", "./instrument.mjs", "index.js"]
```

### 4. Update `server/package.json` scripts

```json
"start": "node --import ./instrument.mjs index.js",
"dev": "node --watch --import ./instrument.mjs index.js"
```

### 5. Add Sentry error handler to `server/index.js`

**Top of file** (after existing imports):
```js
import * as Sentry from '@sentry/node';
```

**After all routes, before static file serving** (~line 1920):
```js
Sentry.setupExpressErrorHandler(app);
```

**Add `Sentry.captureException()` in these 5 catch blocks** (high-severity silent failures):

| Location | What it catches |
|----------|----------------|
| `/api/analyze` background task catch (~line 1169) | Analysis failures — most critical |
| `/api/download-chunk` video mode catch (~line 1784) | Video download failures |
| `/api/download-chunk` text mode catch (~line 1685) | TTS generation failures |
| `/api/load-more-chunks` catch (~line 1303) | Batch loading failures |
| `prefetchNextChunk` catch (~line 1916) | Silent prefetch failures (invisible to user) |

Pattern: add one line after the existing `console.error`:
```js
Sentry.captureException(error, { tags: { operation: 'analyze', sessionId } });
```

### 6. Add Sentry capture to `server/usage.js`

**Top of file** (after existing import):
```js
import * as Sentry from '@sentry/node';
```

**In `persistUsage` catch block** (~line 78): Add `Sentry.captureException(err, { tags: { operation: 'usage_persist', uid }, level: 'warning' });`

**In `initUsageStore` catch block** (~line 113): Add `Sentry.captureException(err, { tags: { operation: 'usage_init' }, level: 'error' });`

### 7. Create `src/sentry.ts`

```ts
import * as Sentry from '@sentry/react';

Sentry.init({
  dsn: import.meta.env.VITE_SENTRY_DSN || '',
  enabled: !!import.meta.env.VITE_SENTRY_DSN,
  environment: import.meta.env.MODE,
  tracesSampleRate: 0.2,
  beforeSend(event) {
    if (import.meta.env.VITE_E2E_TEST) return null;
    return event;
  },
});
```

### 8. Update `src/main.tsx`

```tsx
import './sentry';  // Must be first import
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import * as Sentry from '@sentry/react';
import './index.css';
import App from './App.tsx';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Sentry.ErrorBoundary fallback={<p>Something went wrong. Please refresh the page.</p>}>
      <App />
    </Sentry.ErrorBoundary>
  </StrictMode>,
);
```

### 9. Update `src/services/api.ts`

In the `!response.ok` error path, capture 500+ errors to Sentry:
```ts
import * as Sentry from '@sentry/react';

// After throwing, or before throwing:
if (response.status >= 500) {
  Sentry.captureException(error, { tags: { endpoint } });
}
```

### 10. Update `vite.config.ts`

```ts
import { sentryVitePlugin } from '@sentry/vite-plugin';

export default defineConfig({
  build: {
    sourcemap: 'hidden',  // Generate for Sentry upload, don't expose in prod
  },
  plugins: [
    react(),
    tailwindcss(),
    // Only upload source maps when auth token is available (CI only)
    ...(process.env.SENTRY_AUTH_TOKEN
      ? [sentryVitePlugin({
          org: process.env.SENTRY_ORG,
          project: process.env.SENTRY_PROJECT,
          authToken: process.env.SENTRY_AUTH_TOKEN,
        })]
      : []),
  ],
  server: { /* ...existing proxy config unchanged... */ },
});
```

### 11. Update `.github/workflows/ci.yml`

**Deploy job env** — add:
```yaml
SENTRY_AUTH_TOKEN: ${{ secrets.SENTRY_AUTH_TOKEN }}
SENTRY_ORG: ${{ secrets.SENTRY_ORG }}
SENTRY_PROJECT: ${{ secrets.SENTRY_PROJECT }}
```

**"Build frontend" step** — append to `.env.production`:
```yaml
echo "VITE_SENTRY_DSN=${{ secrets.VITE_SENTRY_DSN }}" >> .env.production
```

**"Deploy to Cloud Run" step** — add secret:
```yaml
--set-secrets="...,SENTRY_DSN=sentry-dsn:latest"
```

### 12. Update `CLAUDE.md`

Add section under Architecture documenting Sentry setup.

## Test Safety

- **No test changes needed.** All Sentry calls are no-ops when `enabled: false` (no DSN in test env).
- `instrument.mjs` is NOT loaded during tests (Vitest doesn't use `--import`).
- `@sentry/node` import in `index.js`/`usage.js` succeeds (package installed) but all methods are no-ops without `init()`.
- Frontend `beforeSend` returns `null` during E2E tests (`VITE_E2E_TEST` flag).
- **Verification**: `npm test` — all 501 tests still pass.

## GCP Secrets Setup (one-time, manual)

```bash
echo -n "https://xxx@yyy.ingest.sentry.io/zzz" | \
  gcloud secrets create sentry-dsn --data-file=- --project=russian-transcription

# Grant access to Cloud Run service account
gcloud secrets add-iam-policy-binding sentry-dsn \
  --member="serviceAccount:YOUR-SA@russian-transcription.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor" \
  --project=russian-transcription
```

## GitHub Secrets to Add

| Secret | Value | Purpose |
|--------|-------|---------|
| `VITE_SENTRY_DSN` | Sentry DSN | Embedded in frontend build |
| `SENTRY_AUTH_TOKEN` | Sentry auth token | Source map upload in CI |
| `SENTRY_ORG` | Sentry org slug | Source map upload |
| `SENTRY_PROJECT` | Sentry project slug | Source map upload |

## Confidence: 90%

The 10%: `--import` with `--watch` in Node 20 is documented as supported but I haven't verified this specific combo with `@sentry/node` v8. Fallback: use `NODE_OPTIONS="--import ./instrument.mjs" node --watch index.js`.
