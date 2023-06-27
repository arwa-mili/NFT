// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract Collection is ERC721URIStorage {

    uint256 public counter;

    constructor() public ERC721("My First Collection", "Educative")
    {
        counter = 0;
    }

    function mintToken(string memory tokenURI) public {
        uint256 tokenId = counter;
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
        counter++;
    }
}