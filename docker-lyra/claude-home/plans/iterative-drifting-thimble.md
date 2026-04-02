# Pre-Payment Features: Legal, Account Deletion, Usage UI, Deck Export, GCP Alerts

## Context
The production hardening PR (#18) is merged. Before adding Stripe payments, the app needs: legal docs (required by law), account deletion (GDPR), usage visibility (so users understand their limits), deck export (data portability), and uptime monitoring (so we know when things break).

---

## Implementation Order
1. **Deck Export** — zero dependencies, pure frontend, fast
2. **ToS + Privacy Policy** — pure frontend, gets legal requirement done
3. **Usage UI** — new backend endpoint + frontend bars
4. **Account Deletion** — most complex, full-stack + Firestore rules
5. **GCP Alerts** — infrastructure only, no code dependencies

---

## 1. Deck Export (JSON)
**Files:** `src/components/SettingsPanel.tsx`, `src/App.tsx`

Pure frontend. Add "Export Deck" button to SettingsPanel that creates a JSON Blob and triggers download.

- Pass `cards: SRSCard[]` as new prop to SettingsPanel
- Button disabled when `cards.length === 0`, shows count: "Export 47 cards"
- Download filename: `russian-deck-YYYY-MM-DD.json`
- Implementation: `Blob` → `URL.createObjectURL` → hidden `<a>` click → `revokeObjectURL`

**Tests:** E2E — verify button visible in settings, verify download triggers with correct content (Playwright download interception)

---

## 2. Terms of Service + Privacy Policy
**Files:** `src/legal.ts` (new), `src/components/SettingsPanel.tsx`, `src/components/LoginScreen.tsx`

- New `src/legal.ts` exporting `TERMS_OF_SERVICE` and `PRIVACY_POLICY` string constants
- SettingsPanel: two collapsible sections after "About" — click header to expand, `max-h-64 overflow-y-auto` for scrollable text
- LoginScreen: add "By signing in, you agree to our Terms of Service and Privacy Policy" below sign-in button, with `<details>` elements for inline viewing (no prop threading needed since LoginScreen renders before SettingsPanel)

**Tests:** E2E — open settings, verify legal headers appear, click to expand/collapse. On login screen, verify agreement text visible.

---

## 3. Usage UI
**Files:** `server/usage.js`, `server/index.js`, `src/services/api.ts`, `src/components/SettingsPanel.tsx`

### Backend
- **`server/usage.js`** — Add translate getter functions (currently missing):
  - `getTranslateDailyCost(uid)`, `getTranslateWeeklyCost(uid)`, `getTranslateMonthlyCost(uid)`
  - Export all limit constants: `DAILY_LIMIT`, `WEEKLY_LIMIT`, `MONTHLY_LIMIT`, `TRANSLATE_DAILY_LIMIT`, `TRANSLATE_WEEKLY_LIMIT`, `TRANSLATE_MONTHLY_LIMIT`
- **`server/index.js`** — New `GET /api/usage` endpoint (requires `requireAuth`):
  ```json
  {
    "openai": { "daily": { "used": 0.45, "limit": 1.00 }, "weekly": {...}, "monthly": {...} },
    "translate": { "daily": {...}, "weekly": {...}, "monthly": {...} }
  }
  ```

### Frontend
- **`src/services/api.ts`** — New `getUsage()` function with `UsageData` type
- **`src/components/SettingsPanel.tsx`** — Add `userId: string | null` prop. When panel opens and userId is set, fetch usage data. Display progress bars with color coding: green <50%, yellow 50-80%, red >80%. Format: `$0.45 / $1.00`

**Tests:**
- Server unit tests in `server/usage.test.js`: translate getter functions work correctly
- Integration test: `GET /api/usage` returns correct shape
- E2E: mock `/api/usage`, open settings, verify bars render with values

---

## 4. Account Deletion
**Files:** `server/index.js`, `server/auth.js`, `server/usage.js`, `src/components/SettingsPanel.tsx`, `src/App.tsx`, `src/services/api.ts`, `firestore.rules`

### Backend
- **`server/auth.js`** — Export `adminAuth` for `deleteUser(uid)` call
- **`server/usage.js`** — Export `getDb()` for Firestore Admin access
- **`server/index.js`** — New `DELETE /api/account` endpoint:
  1. Delete Firestore `decks/{uid}` and `usage/{uid}` via Admin SDK
  2. Find and delete GCS sessions where `session.uid === uid` (iterate session files)
  3. Clean up in-memory sessions (`analysisSessions`, `localSessions`)
  4. Delete Firebase Auth user via `adminAuth.deleteUser(uid)`
  5. Return `{ success: true }`

### Frontend
- **`src/services/api.ts`** — New `deleteAccount()` function
- **`src/components/SettingsPanel.tsx`** — "Delete Account" section at bottom with red button. Clicking shows confirmation: user must type "DELETE" to proceed. Pass `onDeleteAccount` callback prop.
- **`src/App.tsx`** — `handleDeleteAccount` calls API, then `signOut()`. Pass as prop to SettingsPanel.

### Security
- **`firestore.rules`** — Add rules for `usage/{userId}`:
  ```
  match /usage/{userId} {
    allow read: if request.auth != null && request.auth.uid == userId;
    allow delete: if request.auth != null && request.auth.uid == userId;
  }
  ```

**Tests:**
- Integration: DELETE /api/account cleans up sessions, doesn't touch other users' sessions, returns 200
- E2E: open settings, click Delete Account, type "DELETE", mock the API, verify redirect to login

---

## 5. GCP Uptime Alerts
**Files:** `scripts/setup-monitoring.sh` (new)

New idempotent shell script:
- Enable `monitoring.googleapis.com` API
- Create email notification channel (skip if exists)
- Create uptime check: HTTPS on Cloud Run URL `/api/health` every 5 min (skip if exists)
- Create alert policy for uptime check failure

Usage: `./scripts/setup-monitoring.sh your@email.com`

**Tests:** None (manual verification via GCP console). Validate syntax with `bash -n`.

---

## Updated SettingsPanel Props

```ts
interface SettingsPanelProps {
  config: TranslatorConfig;
  onConfigChange: (config: TranslatorConfig) => void;
  isOpen: boolean;
  onClose: () => void;
  cards: SRSCard[];              // Feature 1: deck export
  userId: string | null;          // Feature 3: usage fetch
  onDeleteAccount: () => Promise<void>;  // Feature 4: account deletion
}
```

---

## E2E Mock Routes to Add
In `e2e/fixtures/mock-routes.ts`:
- `GET /api/usage` — return mock usage data
- `DELETE /api/account` — return `{ success: true }`

---

## Verification
1. `npm test` — all frontend + server tests pass
2. `npm run test:e2e` — all E2E tests pass
3. `firebase deploy --only firestore:rules` — deploy updated rules
4. `bash -n scripts/setup-monitoring.sh` — script syntax valid
5. Run monitoring script manually after deploy

## Estimated New Tests: ~18-22
## Confidence: 90% overall (account deletion GCS scan is the riskiest piece)
