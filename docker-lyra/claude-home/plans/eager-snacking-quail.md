# Plan: Re-implement Helmet.js Security Headers

## Context

Helmet was disabled (PR #23) because COOP, CORP, and CSP headers broke Firebase `signInWithPopup`. Now that login works via a same-origin reverse proxy (`/__/*` → `firebaseapp.com`), we can safely re-enable Helmet with a carefully configured setup.

**Strategy**: Deploy in **report-only** mode first (logs CSP violations without blocking). After verifying no violations in production, switch to enforcing mode in a follow-up.

## Files to Modify

1. **`server/index.js`** — Add helmet config, strip CSP from `/__` proxy responses
2. **`server/integration.test.js`** — Un-skip security header test, add proxy exclusion test
3. **`e2e/tests/security-headers.spec.ts`** — New E2E test for CSP violation monitoring

## Step 1: Add Helmet to `server/index.js`

Replace the commented-out helmet block (lines 103-105) with:

```js
app.use(helmet({
  contentSecurityPolicy: {
    reportOnly: true,  // Phase 1: log violations, don't block
    directives: {
      'default-src': ["'self'"],
      'script-src': ["'self'", "https://www.youtube.com"],
      'style-src': ["'self'", "https://fonts.googleapis.com", "'unsafe-inline'"],
      'font-src': ["'self'", "https://fonts.gstatic.com"],
      'img-src': ["'self'", "https://lh3.googleusercontent.com"],
      'connect-src': [
        "'self'",
        "https://firestore.googleapis.com",
        "https://securetoken.googleapis.com",
        "https://identitytoolkit.googleapis.com",
        "https://*.ingest.sentry.io",
      ],
      'media-src': [
        "'self'",
        "https://storage.googleapis.com",
        "https://*.mycdn.me",
        "https://*.userapi.com",
        "https://*.okcdn.ru",
        "https://ok.ru",
        "blob:",
      ],
      'frame-src': ["'self'", "https://www.youtube.com", "https://accounts.google.com"],
      'object-src': ["'none'"],
      'base-uri': ["'self'"],
      'form-action': ["'self'", "https://accounts.google.com"],
    },
  },
  crossOriginOpenerPolicy: { policy: 'same-origin-allow-popups' },
  crossOriginResourcePolicy: { policy: 'cross-origin' },
  crossOriginEmbedderPolicy: false,
  frameguard: { action: 'deny' },
  strictTransportSecurity: { maxAge: 63072000, includeSubDomains: true, preload: true },
  referrerPolicy: { policy: 'strict-origin-when-cross-origin' },
}));
```

Key decisions:
- **COOP `same-origin-allow-popups`**: Popup navigates to `accounts.google.com` then back — opener must keep its reference
- **CORP `cross-origin`**: Google Fonts, Firebase SDK load cross-origin
- **COEP disabled**: `require-corp` would block resources that don't send CORP headers
- **`'unsafe-inline'` in style-src only**: 4 components use React inline `style={{}}` — low risk for styles
- **YouTube in script-src**: `VideoPlayer.tsx:83` dynamically injects `https://www.youtube.com/iframe_api`

## Step 2: Strip CSP from `/__` Proxy Responses

In the `/__` proxy handler, add header removal before sending response. Firebase auth pages are third-party content — our CSP would break their JS.

```js
// At the top of the /__  handler, before res.send():
res.removeHeader('content-security-policy');
res.removeHeader('content-security-policy-report-only');
```

## Step 3: Un-skip and Expand Integration Test

In `server/integration.test.js`, replace the skipped test (lines 362-368):

```js
it('GET /api/health includes security headers from helmet', async () => {
  const res = await fetch(`${baseUrl}/api/health`);
  expect(res.headers.get('x-content-type-options')).toBe('nosniff');
  expect(res.headers.get('x-frame-options')).toBe('DENY');
  expect(res.headers.get('strict-transport-security')).toBeTruthy();
  expect(res.headers.get('content-security-policy-report-only')).toBeTruthy();
  expect(res.headers.get('cross-origin-opener-policy')).toBe('same-origin-allow-popups');
});
```

Add a new test verifying the proxy strips CSP:

```js
it('GET /__/firebase/init.json does NOT include CSP headers', async () => {
  const res = await fetch(`${baseUrl}/__/firebase/init.json`);
  expect(res.headers.get('content-security-policy')).toBeNull();
  expect(res.headers.get('content-security-policy-report-only')).toBeNull();
});
```

## Step 4: E2E Test for CSP Violations

New file `e2e/tests/security-headers.spec.ts` — loads the app, monitors for CSP violations in browser console, asserts security headers are present.

## Verification

1. `npm test` — all unit/integration tests pass including un-skipped helmet test
2. `npm run test:e2e` — E2E tests pass with no CSP violations
3. `quick-deploy.sh` — deploy and verify:
   - `curl -sI https://russian-transcription-fl6fjkunbq-uc.a.run.app/` shows helmet headers
   - Login with Google still works
   - Demo video/text playback still works
   - Check browser console for any CSP report-only violations
