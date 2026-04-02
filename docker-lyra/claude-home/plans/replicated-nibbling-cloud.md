# Plan: Store Both Buyer and Seller Signatures in Contract Storage

## Context

Currently, the buyer's EIP-712 signature is verified during `buy()` but never written to contract storage — it only exists in event logs and transaction calldata. The seller's signature is stored in the `Listing` struct but becomes stale after the sale completes. The user wants both signatures permanently readable from contract storage, so anyone can query the contract directly (not just event logs) to retrieve the cryptographic proof of both parties' agreement.

## Changes

### 1. Add `SaleRecord` struct — `NFTmarketNFT.sol` after line 81

```solidity
struct SaleRecord {
    address seller;
    address buyer;
    bytes sellerSignature;
    bytes buyerSignature;
    bytes32 licenseHash;
    LicenseType licenseType;
    uint256 price;
    uint256 timestamp;
}
```

### 2. Add `saleRecords` mapping — `NFTmarketNFT.sol` after line 120

```solidity
mapping(uint256 => SaleRecord) public saleRecords;
```

### 3. Shrink `__gap` — `NFTmarketNFT.sol` line 1132

`uint256[50]` → `uint256[49]` (one new mapping = one slot consumed)

### 4. Write sale record in `buy()` — `NFTmarketNFT.sol` lines 732-754

- Add `uint256 recordTokenId = tokenId;` after line 732
- In the Display/Commercial path (line 748-754), set `recordTokenId = newTokenId` after minting
- After all three paths (after line 754, before the refund block), write:

```solidity
saleRecords[recordTokenId] = SaleRecord({
    seller: seller,
    buyer: msg.sender,
    sellerSignature: sellerSig,
    buyerSignature: signature,
    licenseHash: licenseHash,
    licenseType: licenseType,
    price: price,
    timestamp: block.timestamp
});
```

**Which token gets the record:**
- Transfer sale / license resale → `tokenId` (the token that changed hands)
- Display/Commercial sale → `newTokenId` (the newly minted license token)

### 5. Add `getSaleRecord()` view function — `NFTmarketNFT.sol` after line 1009

Returns all fields including both `bytes` signatures. Needed because the auto-generated public getter doesn't return dynamic `bytes` fields properly.

### 6. Add tests — `NFTmarketNFT.test.js` after the marketplace buying section (~line 807)

New `describe("Sale Records")` block with 7 tests:
- Transfer sale stores both signatures
- Display license sale stores record on **new** license token (not original)
- Commercial license sale stores record on new license token
- License token resale stores record correctly
- Resale overwrites previous record (most recent wins)
- Unminted/unsold token returns empty record
- Stored signatures match the ones submitted

## Files Modified

| File | Change |
|------|--------|
| `contracts/contracts/NFTmarketNFT.sol` | Add struct, mapping, storage write in `buy()`, view function, shrink `__gap` |
| `contracts/test/NFTmarketNFT.test.js` | Add 7 tests for sale records |

## Verification

```bash
cd /Users/robin/git/NFTmarket/contracts
npx hardhat test test/NFTmarketNFT.test.js
```

All existing tests must still pass. New "Sale Records" tests must pass for all three `buy()` code paths.
