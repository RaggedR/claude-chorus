# Stripe Subscription Payment System

## Context

The app currently has a free usage-based budget ($1/day, $5/week, $10/month) for all users. The goal is to add a paywall: new users get a **30-day free trial** (no card required), after which they must subscribe at **$10/month** to continue. Paid subscribers keep the same budget limits — payment is for access, not higher usage. Stripe Checkout (redirect mode) for payments, Stripe Customer Portal for management.

## Architecture Summary

```
User signs in → Backend lazily creates trial (30 days) → User uses app freely
Trial expires → Frontend shows PaywallScreen → User clicks Subscribe
→ Backend creates Stripe Checkout session → Redirect to Stripe
→ Stripe webhook fires → Firestore updated → User has access
```

**Key design choices:**
- Stripe Checkout redirect (no Stripe.js on frontend, no PCI scope)
- Subscription status in Firestore `subscriptions/{userId}`, synced via webhooks
- In-memory cache on backend (5-min TTL) to avoid Firestore reads on every request
- `requireSubscription` middleware between `requireAuth` and route handlers
- Lazy trial creation: first API request creates the Firestore doc

## Files to Create

| File | Purpose |
|------|---------|
| `server/stripe.js` | Stripe SDK init, subscription status, checkout/portal sessions, webhook handler, in-memory cache |
| `server/stripe.test.js` | Unit tests for all stripe.js exports |
| `src/hooks/useSubscription.ts` | Frontend hook (fetches status, provides subscribe/manage callbacks, E2E bypass) |
| `src/components/PaywallScreen.tsx` | Paywall UI shown when trial expired |
| `e2e/tests/subscription.spec.ts` | E2E tests for paywall flow and settings subscription UI |

## Files to Modify

| File | Changes |
|------|---------|
| `server/index.js` | Webhook route (before `express.json()`), 3 new endpoints, `requireSubscription` on budget routes, account deletion cleanup, startup init |
| `server/integration.test.js` | Mock stripe.js, test new endpoints, test subscription middleware blocking |
| `server/package.json` | Add `stripe` dependency |
| `src/App.tsx` | Subscription loading gate + paywall gate between login and main app |
| `src/components/SettingsPanel.tsx` | Subscription status display, manage/subscribe buttons |
| `src/services/api.ts` | `getSubscription()`, `createCheckoutSession()`, `createPortalSession()` API functions + types |
| `e2e/fixtures/mock-routes.ts` | Mock routes for `/api/subscription`, checkout, portal |
| `firestore.rules` | Add `subscriptions/{userId}` (read + delete by owner) |
| `scripts/deploy.sh` | Add Stripe secrets to `--set-secrets` |
| `quick-deploy.sh` | Add Stripe secrets to `--set-secrets` |
| `CLAUDE.md` | Document new endpoints, Firestore collection, env vars |

## Implementation Steps

### Step 1: Install stripe + create `server/stripe.js` with tests (TDD)

**`server/stripe.test.js`** — tests written first:

- `getSubscriptionStatus(uid)`: returns trialing for new user (lazy-creates Firestore doc), caches within 5-min TTL, returns active/canceled/past_due correctly, computes `needsPayment` flag
- `requireSubscription(req, res, next)`: calls next() for trialing/active/past_due, returns 403 for canceled/expired-trial, skips check in VITEST
- `createCheckoutSession(uid, email)`: calls Stripe SDK correctly, sets `client_reference_id: uid` and `subscription_data.metadata.firebaseUid: uid`, returns `{ url }`
- `createPortalSession(stripeCustomerId)`: calls Stripe SDK, returns `{ url }`
- `handleWebhook(event)`: handles `checkout.session.completed` (sets status=active, stores IDs), `customer.subscription.updated`, `customer.subscription.deleted` (status=canceled), `invoice.payment_failed` (status=past_due), invalidates cache on every update

**`server/stripe.js`** — exports:

```js
getSubscriptionStatus(uid)           // → Promise<SubscriptionInfo>
requireSubscription(req, res, next)  // Express middleware
createCheckoutSession(uid, email)    // → Promise<{ url }>
createPortalSession(customerId)      // → Promise<{ url }>
handleWebhook(event)                 // → Promise<void>
cancelSubscription(subscriptionId)   // → Promise<void> (for account deletion)
initSubscriptionStore()              // → Promise<void> (optional startup warm)
clearSubscriptionCacheForTesting()   // test-only
```

**Firestore doc schema** (`subscriptions/{userId}`):
```
{
  status: 'trialing' | 'active' | 'past_due' | 'canceled',
  trialStart: ISO string,
  trialEnd: ISO string (trialStart + 30 days),
  stripeCustomerId: string | null,
  stripeSubscriptionId: string | null,
  currentPeriodEnd: ISO string | null,
  updatedAt: ISO string
}
```

**SubscriptionInfo** returned by `getSubscriptionStatus()`:
```
{
  status, trialEnd, trialDaysRemaining, currentPeriodEnd,
  stripeCustomerId, stripeSubscriptionId, needsPayment
}
```

`needsPayment` logic:
- trialing + `trialEnd > now` → false
- trialing + `trialEnd <= now` → true (expired trial)
- active → false
- past_due → false (Stripe retrying)
- canceled → true

### Step 2: Wire into Express (`server/index.js`)

**Webhook route** — register BEFORE `express.json()` (line 148) so raw body is available for Stripe signature verification:
```js
// Line ~147 (before app.use(express.json()))
app.post('/api/webhook', express.raw({ type: 'application/json' }), handler);
```

**New endpoints** — after `requireAuth` (line 296) but don't need `requireSubscription`:
- `GET /api/subscription` — returns `getSubscriptionStatus(req.uid)`
- `POST /api/create-checkout-session` — returns `{ url }` for Stripe redirect
- `POST /api/create-portal-session` — returns `{ url }`, 400 if no `stripeCustomerId`

**`requireSubscription` middleware** — add to the 4 routes that use `requireBudget`:
- `POST /api/analyze` (line 973): add `requireSubscription` before `requireBudget`
- `POST /api/translate` (line 620): same
- `POST /api/extract-sentence` (line 692): same
- `POST /api/download-chunk` (line 1535): same

Routes that do NOT get `requireSubscription`:
- `/api/subscription`, `/api/create-checkout-session`, `/api/create-portal-session` (need to work for paywalled users)
- `/api/usage`, `/api/demo`, `/api/health` (informational or free)
- `/api/webhook` (no auth at all — Stripe-signed)

**Account deletion** (`DELETE /api/account`, line 539): Add after Firestore cleanup:
```js
// 5. Cancel Stripe subscription + delete subscriptions doc
const subStatus = await getSubscriptionStatus(uid);
if (subStatus.stripeSubscriptionId) await cancelSubscription(subStatus.stripeSubscriptionId);
db.collection('subscriptions').doc(uid).delete().catch(() => {});
```

**Startup** (line 1931): Add `initSubscriptionStore()` to the chain.

**Integration tests** (`server/integration.test.js`): Mock `stripe.js` module (same pattern as usage.js mock), test new endpoints return correct shapes, test webhook accessible without auth, test `requireSubscription` blocking when mocked to return needsPayment.

### Step 3: Firestore rules + CSP headers

**`firestore.rules`** — add after `usage/{userId}`:
```
match /subscriptions/{userId} {
  allow read: if request.auth != null && request.auth.uid == userId;
  allow delete: if request.auth != null && request.auth.uid == userId;
}
```

**CSP** (`server/index.js` helmet config): Add `https://checkout.stripe.com` and `https://billing.stripe.com` to `form-action` directive (line 131).

### Step 4: Frontend API + useSubscription hook

**`src/services/api.ts`** — add types and 3 functions:
- `SubscriptionData` interface (matches backend SubscriptionInfo)
- `getSubscription()`, `createCheckoutSession()`, `createPortalSession()`

**`src/hooks/useSubscription.ts`** — two implementations:
- `useSubscriptionReal(userId)`: fetches `GET /api/subscription`, returns `{ subscription, isLoading, needsPayment, handleSubscribe, handleManageSubscription, refetch }`
- `useSubscriptionE2E(userId)`: always returns `{ status: 'active', needsPayment: false }`, with `window.__E2E_SUBSCRIPTION` override for paywall tests
- Export: `import.meta.env.VITE_E2E_TEST ? useSubscriptionE2E : useSubscriptionReal`

### Step 5: PaywallScreen + App.tsx gate

**`src/components/PaywallScreen.tsx`**:
- Shows "Your free trial has ended" (or "Subscription canceled")
- Price: $10/month
- "Subscribe" button (`data-testid="subscribe-btn"`) → calls `handleSubscribe()` → redirects to Stripe
- "Sign out" link
- Tailwind-styled, matches LoginScreen aesthetic

**`src/App.tsx`** — add between login gate (line 713) and main app (line 730):
```tsx
// After login gate, before main app:
if (subLoading) return <Spinner />;
if (needsPayment) return <PaywallScreen ... />;
```

Also check for `?subscription=success` query param on return from Stripe Checkout → refetch subscription status.

### Step 6: SettingsPanel subscription section

**`src/components/SettingsPanel.tsx`** — new props: `subscription`, `onManageSubscription`, `onSubscribe`

New "Subscription" section:
- **Trialing**: "Free trial — X days remaining" (green badge), "Subscribe now" button
- **Active**: "Active subscription" (green badge), next billing date, "Manage subscription" button (`data-testid="manage-subscription-btn"`) → Stripe portal redirect
- **Past due**: "Payment issue — retrying" (yellow badge), "Update payment" button
- **Canceled**: "Canceled" (red badge)

### Step 7: E2E tests + mock routes

**`e2e/fixtures/mock-routes.ts`** — add 3 mock routes:
- `GET /api/subscription` → returns trialing with needsPayment: false (default)
- `POST /api/create-checkout-session` → returns mock URL
- `POST /api/create-portal-session` → returns mock URL

**`e2e/tests/subscription.spec.ts`**:
- Paywall appears when trial expired (override `window.__E2E_SUBSCRIPTION`)
- Subscribe button triggers redirect
- Sign out from paywall returns to login
- Paywall does NOT appear during active trial
- Settings shows trial countdown for trialing user
- Settings shows manage button for active subscriber

### Step 8: Deployment

**Env vars** (add to `.env` for local dev):
```
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
STRIPE_PRICE_ID=price_...
```

**GCP Secret Manager** (manual, one-time):
```bash
echo -n "sk_live_..." | gcloud secrets create stripe-secret-key --data-file=-
echo -n "whsec_..." | gcloud secrets create stripe-webhook-secret --data-file=-
echo -n "price_..." | gcloud secrets create stripe-price-id --data-file=-
```

**`scripts/deploy.sh`** (line 71) — add to `--set-secrets`:
```
STRIPE_SECRET_KEY=stripe-secret-key:latest,STRIPE_WEBHOOK_SECRET=stripe-webhook-secret:latest,STRIPE_PRICE_ID=stripe-price-id:latest
```

**`quick-deploy.sh`** (line 39) — same addition.

**Stripe Dashboard setup** (manual):
1. Create product "Russian Video & Text" at $10/month
2. Copy Price ID → `STRIPE_PRICE_ID`
3. Create webhook endpoint → `https://<cloud-run-url>/api/webhook`
4. Subscribe to: `checkout.session.completed`, `customer.subscription.updated`, `customer.subscription.deleted`, `invoice.payment_failed`
5. Copy webhook signing secret → `STRIPE_WEBHOOK_SECRET`
6. Enable Customer Portal (cancel, update payment, view invoices)

### Step 9: Update CLAUDE.md

Add new endpoints to API table, document `subscriptions/{userId}` collection, list new env vars, update deployment secrets list, add to completed roadmap.

## Verification

1. **Unit tests**: `cd server && npx vitest run stripe.test.js` — all pass
2. **Integration tests**: `cd server && npx vitest run integration.test.js` — new endpoint tests pass
3. **All existing tests**: `npm test` — no regressions
4. **E2E tests**: `npm run test:e2e` — subscription flow tests + all existing tests pass
5. **Manual smoke test** (local dev):
   - Sign in → see app (trial active, 30 days remaining)
   - Check Settings → trial countdown visible
   - Manually expire trial in Firestore → refresh → paywall appears
   - Click Subscribe → redirects to Stripe Checkout (test mode)
   - After Stripe test checkout → redirected back, paywall gone

## Confidence: 90%

The architecture follows established patterns in this codebase (in-memory cache + Firestore persistence, E2E bypass with build-time flag + window override, middleware chaining). Main risk is the webhook raw-body handling (must be registered before `express.json()`), which is a well-documented Stripe requirement.
