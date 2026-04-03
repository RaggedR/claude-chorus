# Wallet Microservice Implementation Plan

## Overview

Create a separate wallet microservice that handles all private key management and signing. This removes wallet logic from both Flutter frontend and keeps concerns properly separated.

## Architecture

```
Flutter App          Wallet Service (NEW)        Backend              Contract
    |                      |                        |                    |
    |-- select account -->|                        |                    |
    |<-- sessionId -------|                        |                    |
    |                      |                        |                    |
    |-- get auth token -->|                        |                    |
    |<-- SIWE token ------|                        |                    |
    |                      |                        |                    |
    |-------- prepare listing ------------------->|                    |
    |<------- typedData, contractCall ------------|                    |
    |                      |                        |                    |
    |-- sign typed data ->|                        |                    |
    |<-- signature -------|                        |                    |
    |                      |                        |                    |
    |-- send transaction ->|                        |                    |
    |                      |-------- list() --------------------------->|
    |<-- txHash ----------|                        |                    |
```

## Wallet Service API

### Account Management
```
GET  /api/accounts           - List available test accounts
GET  /api/accounts/current   - Get current session's account
POST /api/accounts/select    - Select account, returns sessionId
```

### Signing
```
POST /api/sign/message       - Sign arbitrary message
POST /api/sign/typed-data    - Sign EIP-712 typed data
POST /api/auth/token         - Generate SIWE auth token for backend
```

### Transactions
```
POST /api/transaction/send   - Sign and submit transaction to blockchain
```

All endpoints except `/accounts` require `X-Session-Id` header.

## File Structure

```
wallet-service/
  package.json
  .env.example
  src/
    index.js                    # Express app entry (port 3001)
    config/
      hardhat-accounts.js       # Test account addresses + private keys
    middleware/
      session.js                # Session validation
    services/
      accounts.js               # Session storage, account management
      signer.js                 # EIP-712 signing with ethers
      blockchain.js             # Transaction submission
    routes/
      accounts.js               # Account endpoints
      sign.js                   # Signing endpoints
      auth.js                   # SIWE token generation
      transaction.js            # Transaction sending
```

## Implementation Steps

### Phase 1: Create wallet-service (new files)

1. **`wallet-service/package.json`**
   - Dependencies: express, cors, ethers, siwe, uuid, dotenv

2. **`wallet-service/src/config/hardhat-accounts.js`**
   - Move test accounts from Flutter (addresses + private keys)
   - Export as array of { address, privateKey, name }

3. **`wallet-service/src/services/accounts.js`**
   - In-memory session Map: sessionId -> { address, privateKey }
   - `createSession(address)` - returns sessionId
   - `getSession(sessionId)` - returns account info
   - `getAccountByAddress(address)` - lookup from config

4. **`wallet-service/src/services/signer.js`**
   - `signMessage(privateKey, message)` - personal_sign
   - `signTypedData(privateKey, domain, types, value)` - EIP-712
   - Uses ethers.Wallet for signing

5. **`wallet-service/src/services/blockchain.js`**
   - `sendTransaction(privateKey, to, data, value)` - submit tx
   - Connect to RPC from env (localhost:8545)

6. **`wallet-service/src/routes/*.js`**
   - accounts.js: GET /accounts, GET /accounts/current, POST /accounts/select
   - sign.js: POST /sign/message, POST /sign/typed-data
   - auth.js: POST /auth/token (builds SIWE message, signs, returns base64 token)
   - transaction.js: POST /transaction/send

7. **`wallet-service/src/index.js`**
   - Express app on port 3001
   - CORS enabled for localhost:*
   - Mount routes

### Phase 2: Update Flutter

1. **New `lib/services/wallet_service.dart`**
   ```dart
   class WalletService {
     static const baseUrl = 'http://localhost:3001';
     String? _sessionId;

     Future<List<Account>> getAccounts();
     Future<String> selectAccount(String address);  // returns sessionId
     Future<String> getAuthToken();
     Future<Uint8List> signTypedData(Map<String, dynamic> typedData);
     Future<String> sendTransaction({to, data, value});
   }
   ```

2. **Update `lib/providers/wallet_provider.dart`**
   - Remove TestAccount.privateKey field
   - Remove `_signHash()`, `signListingTypedData()`, `signPurchaseTypedData()`
   - Add `WalletService _walletService`
   - Update `connectTestAccount()` to call wallet service
   - Update `_createAuthToken()` to call `_walletService.getAuthToken()`
   - Add `Future<Uint8List> signTypedData(Map)` that delegates to wallet service
   - Add `Future<String> sendTransaction({to, data, value})` that delegates

3. **Update `lib/pages/token_detail_page.dart`**
   - `_list()`: Use wallet.sendTransaction() instead of contractService.listToken()
   - `_buy()`: Use wallet.sendTransaction() instead of contractService.buyToken()
   - `_delist()`: Use wallet.sendTransaction() instead of contractService.delistToken()

4. **Update `lib/services/contract_service.dart`**
   - Remove transaction-sending methods (listToken, buyToken, delistToken)
   - Keep read-only methods (getListing, getNonce, etc.)
   - Keep EIP-712 hash building (for reference/verification)

### Phase 3: Startup Scripts

1. **`wallet-service/start.sh`**
   ```bash
   RPC_URL=http://localhost:8545 node src/index.js
   ```

2. **Update `backend/start-local-blockchain.sh`**
   - Add instruction to start wallet-service first

3. **Create `start-all.sh`** in project root
   ```bash
   # Start hardhat
   cd contracts && npx hardhat node &
   sleep 2
   # Deploy
   npx hardhat run scripts/deploy.js --network localhost
   # Start wallet service
   cd ../wallet-service && npm run dev &
   # Start backend
   cd ../backend && ./start-local-blockchain.sh &
   # Start flutter
   cd ../flutter && flutter run -d chrome
   ```

## Key Files Modified

| File | Changes |
|------|---------|
| `wallet-service/*` | NEW - entire service |
| `flutter/lib/services/wallet_service.dart` | NEW - wallet service client |
| `flutter/lib/providers/wallet_provider.dart` | Remove private keys, add wallet service calls |
| `flutter/lib/pages/token_detail_page.dart` | Use wallet service for transactions |
| `flutter/lib/services/contract_service.dart` | Remove transaction methods |

## Verification

1. Start Hardhat node
2. Deploy contract
3. Start wallet-service on port 3001
4. Start backend on port 3000
5. Start Flutter
6. Test flow:
   - Select account in Flutter -> calls wallet service
   - Mint token -> uses backend API
   - List token -> calls backend (prepare) -> wallet service (sign) -> wallet service (send tx)
   - Switch account -> wallet service
   - Buy token -> backend (prepare) -> wallet service (sign + send)
   - Verify signatures recorded on-chain
