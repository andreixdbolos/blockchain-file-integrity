import argparse
import hashlib
import json
import os
from web3 import Web3
import ipfshttpclient
from dotenv import load_dotenv

load_dotenv()

INFURA_URL = os.getenv('INFURA_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')
CONTRACT_ABI = json.loads(os.getenv('CONTRACT_ABI', '[]'))

w3 = Web3(Web3.HTTPProvider(INFURA_URL))
account = w3.eth.account.from_key(PRIVATE_KEY)
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

client = ipfshttpclient.connect()

def hash_file(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def upload_to_ipfs(path):
    res = client.add(path)
    print(f"Uploaded to IPFS: {res['Hash']}")
    return res['Hash']

def store_hash(file_name, file_hash):
    nonce = w3.eth.get_transaction_count(account.address)
    txn = contract.functions.storeHash(file_name, Web3.to_bytes(hexstr=file_hash)).build_transaction({
        'from': account.address,
        'nonce': nonce,
        'gas': 200000,
        'gasPrice': w3.to_wei('10', 'gwei')
    })
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
    print(f"Transaction sent: {tx_hash.hex()}")
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Transaction mined: {receipt.transactionHash.hex()}")

def verify_hash(file_name, file_hash):
    result = contract.functions.verifyHash(file_name, Web3.to_bytes(hexstr=file_hash)).call()
    print(f"File integrity intact? {result}")
    return result

def main():
    parser = argparse.ArgumentParser(description='Blockchain-based File Integrity Checker')
    subparsers = parser.add_subparsers(dest='command')

    upload_parser = subparsers.add_parser('upload')
    upload_parser.add_argument('file', help='File to upload and store hash')

    verify_parser = subparsers.add_parser('verify')
    verify_parser.add_argument('file', help='File to verify integrity')

    args = parser.parse_args()

    if args.command == 'upload':
        file_hash = hash_file(args.file)
        print(f"SHA-256: {file_hash}")
        ipfs_hash = upload_to_ipfs(args.file)
        store_hash(args.file, file_hash)
    elif args.command == 'verify':
        file_hash = hash_file(args.file)
        verify_hash(args.file, file_hash)
    else:
        parser.print_help()

if __name__ == '__main__':
    main() 