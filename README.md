# Blockchain-based File Integrity Checker

## Overview
This project allows you to upload files to IPFS, store their hashes on the Ethereum blockchain, and verify file integrity later.

## Features
- Upload files to IPFS
- Store file hashes on Ethereum (testnet)
- Verify file integrity at any time

## Tech Stack
- Python
- Ethereum (Sepolia testnet or Ganache)
- IPFS (Infura or local)
- Solidity

## Setup
1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your `.env` file with your Infura and wallet details (see below).
4. Deploy the smart contract in `contracts/IntegrityChecker.sol` using Remix, Hardhat, or Truffle. Save the contract address and ABI.
5. Run the Python script to upload and verify files.

## .env Example
```
INFURA_URL=https://sepolia.infura.io/v3/YOUR_INFURA_KEY
PRIVATE_KEY=your_wallet_private_key
CONTRACT_ADDRESS=your_deployed_contract_address
CONTRACT_ABI=your_contract_abi_json
```

## Usage
- To upload and store a file hash:
  ```bash
  python scripts/upload_and_verify.py upload myfile.txt
  ```
- To verify a file's integrity:
  ```bash
  python scripts/upload_and_verify.py verify myfile.txt
  ```

## Screenshots
- IPFS upload result
- Etherscan transaction hash

## Optional
- Add a simple UI (CLI or Streamlit)
- Add timestamping or versioning 