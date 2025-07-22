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