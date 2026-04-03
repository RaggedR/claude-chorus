# Flutter Regression Test Plan

## Problem
The Flutter frontend is flaky - "sometimes it works, sometimes it doesn't." Current tests (2,188 lines) have good UI coverage but weak API mocking, and many tests are skipped because they require wallet service running.

## Goal
Add regression tests that:
1. Run without external services (mock HTTP)
2. Test actual page widgets (not rebuilt snippets)
3. Cover the new license upgrade logic
4. Catch regressions before they reach production

---

## Implementation Plan

### Phase 1: HTTP Mocking Infrastructure

**Create `test/mocks/mock_http_client.dart`**
- Implement `MockClient` that intercepts HTTP requests
- Support URL pattern matching and canned responses
- Allow tests to verify requests were made correctly

**Create `test/fixtures/api_responses.dart`**
- Pre-built JSON responses for all API endpoints
- Tokens, listings, galleries, license status

**Create `test/utils/test_app.dart`**
- Standard wrapper with providers pre-configured
- Support connected/disconnected wallet states
- Inject mock HTTP client

### Phase 2: Critical Regression Tests (Priority 1)

**`test/regression/license_status_test.dart`** (~15 tests)
Focus on the new license upgrade logic:
```
- getLicenseStatus returns correct canBuy flags
- Display owner can upgrade to Commercial
- Display owner can upgrade to Transfer
- Commercial owner can upgrade to Transfer
- Commercial owner CANNOT buy Display (downgrade blocked)
- Transfer owner CANNOT buy any license (max level)
- UI shows "Upgrade to X" when upgrade available
- UI shows "Cannot downgrade" message when blocked
- UI shows existing license info box
- Buy button disabled when cannot buy
```

**`test/regression/marketplace_browse_test.dart`** (~12 tests)
Test marketplace page with mocked API:
```
- Loads listings on mount
- Shows loading indicator
- Displays listing cards with correct info
- License badge colors correct (blue/orange/purple)
- Empty state when no listings
- Error state with retry button
- Tap listing navigates to detail
```

**`test/regression/gallery_browse_test.dart`** (~12 tests)
Test gallery page with mocked API:
```
- Loads galleries on mount
- Shows "My Collection" for own address
- Token cards show FOR SALE badge
- Multi-license tokens show multiple badges
- Search by address works
- Search by nickname works (Alice, Bob)
- Tap token navigates to detail
```

**`test/regression/token_detail_test.dart`** (~20 tests)
Test token detail page - the most complex page:
```
- Shows token info (name, creator, owner)
- Owner sees "List for Sale" when not listed
- Owner sees "Remove Listing" when listed
- Non-owner sees "Buy" button when listed
- Non-owner sees "Connect Wallet" when disconnected
- Shows bilateral agreement notice
- List dialog has price input and license options
- License type selection works
```

### Phase 3: Wallet & State Tests (Priority 2)

**`test/regression/wallet_connection_test.dart`** (~10 tests)
```
- Connect shows account picker
- Selecting account sets connected state
- Disconnect clears state
- Switch account changes address
- Protected routes redirect when disconnected
```

**`test/unit/mint_provider_test.dart`** (~15 tests)
```
- State machine transitions (idle → imageSelected → minting → success)
- canMint validation (requires image + name + wallet)
- Progress updates during mint
- Error handling
```

### Phase 4: Enhanced Existing Tests (Priority 3)

**Enhance `test/unit/api_service_test.dart`**
Add HTTP mocking to test actual request/response handling:
- getListings, getGallery, getLicenseStatus
- Error responses (400, 500)
- Auth header included when token present

---

## File Structure

```
flutter/test/
├── mocks/
│   └── mock_http_client.dart      # NEW - HTTP interceptor
├── fixtures/
│   └── api_responses.dart         # NEW - Canned responses
├── utils/
│   └── test_app.dart              # NEW - Provider wrapper
├── regression/                     # NEW directory
│   ├── license_status_test.dart   # Priority 1
│   ├── marketplace_browse_test.dart
│   ├── gallery_browse_test.dart
│   └── token_detail_test.dart
└── unit/
    ├── api_service_test.dart      # ENHANCED
    └── mint_provider_test.dart    # NEW
```

## Estimated Scope

| Category | Tests | Lines |
|----------|-------|-------|
| Mocking infrastructure | - | ~200 |
| License status regression | 15 | ~400 |
| Marketplace regression | 12 | ~350 |
| Gallery regression | 12 | ~350 |
| Token detail regression | 20 | ~500 |
| Wallet connection | 10 | ~300 |
| MintProvider unit | 15 | ~350 |
| ApiService enhanced | 10 | ~250 |
| **Total** | **~94** | **~2,700** |

## Critical Files to Modify/Create

| File | Action |
|------|--------|
| `test/mocks/mock_http_client.dart` | Create |
| `test/fixtures/api_responses.dart` | Create |
| `test/utils/test_app.dart` | Create |
| `test/regression/license_status_test.dart` | Create |
| `test/regression/marketplace_browse_test.dart` | Create |
| `test/regression/gallery_browse_test.dart` | Create |
| `test/regression/token_detail_test.dart` | Create |
| `test/regression/wallet_connection_test.dart` | Create |
| `test/unit/mint_provider_test.dart` | Create |
| `test/unit/api_service_test.dart` | Enhance |

## Verification

1. Run `flutter test` - all tests should pass
2. Run `flutter test test/regression/` - regression suite passes
3. CI should run tests on PR (already configured)
4. Break something intentionally (e.g., change license level check) and verify test catches it

## Dependencies

No new packages needed - uses existing:
- `flutter_test` (SDK)
- `mockito` (already in pubspec.yaml)
- `http` (mock client pattern)
