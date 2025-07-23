# Blockchain-based File Integrity Checker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)

---

## Table of Contents
- [What is This Project? (Beginner Friendly)](#what-is-this-project-beginner-friendly)
- [Glossary: Key Concepts](#glossary-key-concepts)
- [How Does It Work? (Step by Step)](#how-does-it-work-step-by-step)
- [What Do I Need? (Prerequisites)](#what-do-i-need-prerequisites)
- [Step 1: Install Python and Pip](#step-1-install-python-and-pip)
- [Step 2: Install Project Dependencies](#step-2-install-project-dependencies)
- [Step 3: Set Up IPFS](#step-3-set-up-ipfs)
- [Step 4: Get an Ethereum Wallet and Testnet ETH](#step-4-get-an-ethereum-wallet-and-testnet-eth)
- [Step 5: Deploy the Smart Contract (with Remix)](#step-5-deploy-the-smart-contract-with-remix)
- [Step 6: Set Up the .env File](#step-6-set-up-the-env-file)
- [Step 7: Run the Scripts](#step-7-run-the-scripts)
- [Step 8: Verify Everything Works](#step-8-verify-everything-works)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Contact & Support](#contact--support)
- [License](#license)

---

## What is This Project? (Beginner Friendly)
This project helps you prove that a file (like a document or image) hasn’t been changed, by storing its fingerprint (hash) on a public blockchain. You upload your file to a decentralized storage system (IPFS), and the project saves a unique code (hash) representing your file on the Ethereum blockchain. Later, you (or anyone) can check if a file is still the same by comparing its hash to the one on the blockchain.

**Why is this useful?**
- Prove a file existed at a certain time
- Detect if a file has been tampered with
- Store evidence or important documents securely

## Glossary: Key Concepts
- **Blockchain:** A public, tamper-proof digital ledger (like a database) that anyone can read but no one can secretly change.
- **Ethereum:** A popular blockchain that supports smart contracts (programs that run on the blockchain).
- **IPFS:** InterPlanetary File System, a decentralized way to store and share files.
- **Hash:** A unique digital fingerprint of a file. If the file changes, the hash changes.
- **Smart Contract:** A program on Ethereum that stores and checks file hashes.
- **Testnet:** A free, fake version of Ethereum for testing (no real money involved).

## How Does It Work? (Step by Step)
1. You choose a file you want to protect.
2. The script calculates the file’s hash (fingerprint).
3. The file is uploaded to IPFS (so it’s stored in a decentralized way).
4. The hash is sent to a smart contract on Ethereum, which stores it forever.
5. Later, you (or anyone) can check if a file is unchanged by comparing its hash to the one on the blockchain.

## What Do I Need? (Prerequisites)
- A computer with Linux, macOS, or Windows
- Python 3.7 or newer
- pip (Python package manager)
- An Ethereum wallet (like MetaMask)
- Some testnet ETH (fake money)
- An Infura account (for Ethereum and/or IPFS)
- (Optional) A local IPFS node

---

## Step 1: Install Python and Pip
If you don’t have Python 3.7+ and pip:
- **Linux:**
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip
  ```
- **macOS:**
  Download from [python.org](https://www.python.org/downloads/)
- **Windows:**
  Download from [python.org](https://www.python.org/downloads/)

Check installation:
```bash
python3 --version
pip3 --version
```

## Step 2: Install Project Dependencies
Clone this repository and install dependencies:
```bash
git clone <repo-url>
cd blockchain-file-integrity
pip install -r requirements.txt
```

## Step 3: Set Up IPFS
- **Option 1: Use Infura (Recommended for Beginners)**
  1. Sign up at [Infura.io](https://infura.io/)
  2. Create a new IPFS project and get your API credentials
- **Option 2: Run a Local IPFS Node**
  1. Download and extract go-ipfs:
     ```bash
     tar -xvzf go-ipfs_v0.7.0_linux-amd64.tar.gz
     cd go-ipfs
     ./install.sh
     ipfs init
     ipfs daemon &
     ```
  2. Check it’s running:
     ```bash
     ipfs swarm peers
     ```

## Step 4: Get an Ethereum Wallet and Testnet ETH
1. **Install MetaMask** (browser extension): [metamask.io](https://metamask.io/)
2. **Create a wallet** (save your seed phrase!)
3. **Switch to Sepolia Testnet** in MetaMask
4. **Get testnet ETH:**
   - Use a faucet like [https://sepoliafaucet.com/](https://sepoliafaucet.com/)
5. **Get your wallet’s private key:**
   - In MetaMask: Account > Export Private Key (keep it secret!)

## Step 5: Deploy the Smart Contract (with Remix)
1. Go to [Remix IDE](https://remix.ethereum.org/)
2. Create a new file, paste in `contracts/IntegrityChecker.sol`:
   ```solidity
   // SPDX-License-Identifier: MIT
   pragma solidity ^0.8.0;
   contract IntegrityChecker {
       mapping(string => bytes32) public fileHashes;
       function storeHash(string memory fileName, bytes32 fileHash) public {
           fileHashes[fileName] = fileHash;
       }
       function verifyHash(string memory fileName, bytes32 fileHash) public view returns (bool) {
           return fileHashes[fileName] == fileHash;
       }
   }
   ```
3. Compile the contract (Solidity compiler tab)
4. In Remix, connect MetaMask (top right, select "Injected Provider - MetaMask")
5. Deploy the contract (Deploy & Run tab)
6. Copy the deployed contract address
7. Copy the contract ABI (from Remix, under "Compilation Details" or "ABI" button)

## Step 6: Set Up the .env File
Create a file named `.env` in your project root:
```
INFURA_URL=https://sepolia.infura.io/v3/YOUR_INFURA_KEY
PRIVATE_KEY=your_wallet_private_key
CONTRACT_ADDRESS=your_deployed_contract_address
CONTRACT_ABI=your_contract_abi_json
```
- Replace `YOUR_INFURA_KEY` with your Infura project key
- Replace `your_wallet_private_key` with your MetaMask private key
- Replace `your_deployed_contract_address` with the address from Remix
- Replace `your_contract_abi_json` with the ABI (as a single line JSON string)

**Never share your private key or .env file!**

## Step 7: Run the Scripts
- **To upload and store a file hash:**
  ```bash
  python scripts/upload_and_verify.py upload myfile.txt
  ```
  - You’ll see output like:
    ```
    SHA-256: 0xabc123...
    Uploaded to IPFS: Qm...
    Transaction sent: 0x...
    Transaction mined: 0x...
    ```
- **To verify a file’s integrity:**
  ```bash
  python scripts/upload_and_verify.py verify myfile.txt
  ```
  - Output:
    ```
    SHA-256: 0xabc123...
    File integrity intact? True
    ```

## Step 8: Verify Everything Works
- Check your file’s hash and IPFS hash in the output
- Check your transaction on [Etherscan Sepolia](https://sepolia.etherscan.io/) using the transaction hash
- Try changing the file and running the verify command again (it should say `False`)

## Troubleshooting
- **IPFS connection error:** Make sure your IPFS daemon is running or your Infura credentials are correct
- **Web3 connection error:** Check your Infura URL and internet connection
- **Contract errors:** Make sure the contract address and ABI in `.env` match your deployed contract
- **Out of gas:** Increase the gas limit in the script if needed
- **File not found:** Ensure the file path is correct and accessible

## FAQ
**Q: Do I need real money?**
A: No, you use testnet ETH which is free from a faucet.

**Q: Can I use this on Windows/Mac/Linux?**
A: Yes, it works on all major operating systems.

**Q: Is my file public?**
A: Files on public IPFS are accessible by anyone with the hash. For privacy, encrypt before uploading.

**Q: Can I use another blockchain?**
A: Yes, with some code changes.

**Q: What if I lose my private key?**
A: You lose access to your contract interactions. Keep it safe!

## License
MIT 