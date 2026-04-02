# AI Art Generation + USDC Payments Implementation Plan

## Overview

Add Stability AI image generation and USDC stablecoin payments to NFTmarket. Users pay USDC on-chain to generate AI art and mint NFTs.

## User Flow

```
Connect Wallet → Enter Prompt → Approve USDC → Pay for Generation →
View Generated Images → Select Image → Pay for Mint → NFT Minted
```

## Pricing Model

| Action | USDC | Notes |
|--------|------|-------|
| Generate 1 image | $0.50 | Covers Stability AI (~$0.04) + margin |
| Generate 4 images | $1.50 | Bulk discount |
| Mint NFT | $1.00 | Any license type |

---

## Phase 1: Smart Contract

### New File: `contracts/contracts/NFTmarketPayments.sol`

Payment handler contract accepting USDC via approve+transferFrom:

```solidity
// State
IERC20 public usdc;  // 0x3c499c542cef5e3811e1192ce70d8cc03d5c3359 (Polygon)
mapping(bytes32 => bool) public paymentProcessed;
uint256 public generationFeeUSDC = 500000;  // $0.50 (6 decimals)
uint256 public mintFeeUSDC = 1000000;       // $1.00

// Events
event GenerationPaid(address indexed user, bytes32 indexed paymentId, uint256 amount);
event MintPaid(address indexed user, bytes32 indexed paymentId, uint256 amount);

// Functions
function payForGeneration(bytes32 paymentId) external;
function payForMint(bytes32 paymentId) external;
function verifyPayment(bytes32 paymentId) view returns (bool);
function setFees(uint256 generation, uint256 mint) onlyOwner;
```

### New File: `contracts/test/NFTmarketPayments.test.js`

Test coverage for payment flows, fee updates, replay prevention.

---

## Phase 2: Backend Services

### New File: `backend/src/services/ai-generation.js`

Stability AI integration:

```javascript
async function generateImage(prompt, style, count = 1)
// POST https://api.stability.ai/v2beta/stable-image/generate/ultra
// Returns: [{ buffer: Buffer, seed: number }]

// Mock mode: USE_MOCK_AI=true returns placeholder images
```

### New File: `backend/src/services/payment.js`

On-chain payment verification:

```javascript
async function createPaymentId(wallet, type, nonce)
// Returns: bytes32 hash

async function verifyPayment(paymentId)
// Calls contract.verifyPayment() or checks events

// Mock mode: USE_MOCK_PAYMENTS=true uses in-memory Map
```

### New File: `backend/src/routes/generate.js`

```
POST /api/generate/prices     → { generation1: "0.50", generation4: "1.50", mint: "1.00" }
POST /api/generate/create     → { paymentId, feeUSDC, contractAddress }
POST /api/generate            → { generationId, images: [base64...] }
GET  /api/generate/:id        → { prompt, images, createdAt }
```

### Modify: `backend/src/routes/mint.js`

- Accept `generationId` + `imageIndex` to mint from AI generation
- Require `paymentId` and verify mint payment before proceeding
- Return 402 if payment not verified

### Modify: `backend/src/index.js`

Register `/api/generate` routes.

### New Env Variables

```
STABILITY_API_KEY=sk-...
PAYMENT_CONTRACT_ADDRESS=0x...
USE_MOCK_AI=true
USE_MOCK_PAYMENTS=true
```

---

## Phase 3: Flutter App

### New File: `flutter/lib/services/payment_service.dart`

Build and send USDC transactions:

```dart
const usdcAddress = '0x3c499c542cef5e3811e1192ce70d8cc03d5c3359';

Future<String> approveUSDC(String spender, BigInt amount);
Future<String> payForGeneration(String contractAddress, String paymentId);
Future<String> payForMint(String contractAddress, String paymentId);
Future<BigInt> getUSDCBalance(String address);
```

### New File: `flutter/lib/providers/generation_provider.dart`

State machine for generation flow:

```dart
enum GenerationState { idle, awaitingPayment, paying, generating, selectingImage, error }

class GenerationProvider extends ChangeNotifier {
  String prompt;
  String? paymentId;
  List<Uint8List>? images;

  Future<void> createPaymentRequest(prompt, style, count);
  Future<void> waitForPaymentAndGenerate();
  void selectImageForMint(int index);
}
```

### New File: `flutter/lib/pages/generate_page.dart`

UI sections:
1. Prompt input + style selector
2. Image count selector (1 or 4)
3. Price display + "Generate" button
4. Payment modal (Approve → Pay → Waiting)
5. Generated images grid
6. "Mint This" button per image

### Modify: `flutter/lib/providers/wallet_provider.dart`

Add `sendTransaction(to, data, value)` for contract interactions.

### Modify: `flutter/lib/services/api_service.dart`

Add generation API methods.

### Modify: `flutter/lib/router.dart`

Add `/generate` route with wallet guard.

### Modify: `flutter/lib/providers/mint_provider.dart`

Add `setFromGeneration(generationId, imageIndex, imageBytes)` to populate mint form from AI generation.

---

## Phase 4: Testing

### Contract Tests
- Payment acceptance and event emission
- Duplicate paymentId rejection
- Fee updates by owner

### Backend Tests (Mock Mode)
- `npm test -- --testPathPattern=payment`
- `npm test -- --testPathPattern=ai-generation`
- `npm test -- --testPathPattern=generate`

### Integration Test
```bash
# Terminal 1: Local blockchain
cd contracts && npx hardhat node

# Terminal 2: Deploy contracts
npx hardhat run scripts/deploy-payments.js --network localhost

# Terminal 3: Backend with mocks
cd backend && ./start-dev.sh

# Terminal 4: Flutter
cd flutter && flutter run -d chrome
```

---

## Files Summary

| Action | File |
|--------|------|
| Create | `contracts/contracts/NFTmarketPayments.sol` |
| Create | `contracts/test/NFTmarketPayments.test.js` |
| Create | `contracts/scripts/deploy-payments.js` |
| Create | `backend/src/services/ai-generation.js` |
| Create | `backend/src/services/payment.js` |
| Create | `backend/src/routes/generate.js` |
| Create | `backend/test/services/ai-generation.test.js` |
| Create | `backend/test/services/payment.test.js` |
| Create | `backend/test/routes/generate.test.js` |
| Create | `flutter/lib/services/payment_service.dart` |
| Create | `flutter/lib/providers/generation_provider.dart` |
| Create | `flutter/lib/pages/generate_page.dart` |
| Modify | `backend/src/index.js` |
| Modify | `backend/src/routes/mint.js` |
| Modify | `backend/start-dev.sh` |
| Modify | `flutter/lib/router.dart` |
| Modify | `flutter/lib/providers/wallet_provider.dart` |
| Modify | `flutter/lib/providers/mint_provider.dart` |
| Modify | `flutter/lib/services/api_service.dart` |

---

## Verification

1. **Contract**: Deploy to local Hardhat, run `npx hardhat test test/NFTmarketPayments.test.js`
2. **Backend**: Run `npm test` with mock mode enabled
3. **E2E**:
   - Connect wallet in Flutter
   - Navigate to /generate
   - Enter prompt, complete USDC payment flow
   - Verify images appear
   - Select image, complete mint payment
   - Verify NFT minted with correct metadata
