# Module 15: Blockchain & Web3 Game Development

## 🎯 Learning Objectives

- Build blockchain-integrated games
- Implement NFT systems for game assets
- Create play-to-earn mechanics
- Integrate crypto wallets
- Design tokenomics for games
- Understand smart contracts for gaming

**Duration:** 6-7 weeks | **Difficulty:** Advanced
**Prerequisites:** Module 8, JavaScript, Basic blockchain knowledge

---

## 🗓️ Core Topics

### Week 1-2: Web3 Fundamentals

```javascript
import { ethers } from 'ethers';
import Web3Modal from 'web3modal';

class Web3GameClient {
  constructor() {
    this.provider = null;
    this.signer = null;
    this.account = null;
    this.chainId = null;
  }

  async connect() {
    const web3Modal = new Web3Modal({
      cacheProvider: true,
      providerOptions: {
        // WalletConnect, Coinbase, etc.
      }
    });

    const instance = await web3Modal.connect();
    this.provider = new ethers.providers.Web3Provider(instance);
    this.signer = this.provider.getSigner();
    this.account = await this.signer.getAddress();

    const network = await this.provider.getNetwork();
    this.chainId = network.chainId;

    // Listen for account changes
    instance.on('accountsChanged', (accounts) => {
      this.account = accounts[0];
      this.onAccountChanged(accounts[0]);
    });

    // Listen for chain changes
    instance.on('chainChanged', (chainId) => {
      window.location.reload();
    });

    return {
      account: this.account,
      chainId: this.chainId
    };
  }

  async disconnect() {
    if (this.provider?.close) {
      await this.provider.close();
    }

    this.provider = null;
    this.signer = null;
    this.account = null;
  }

  async getBalance() {
    if (!this.account) return '0';

    const balance = await this.provider.getBalance(this.account);
    return ethers.utils.formatEther(balance);
  }

  async signMessage(message) {
    if (!this.signer) throw new Error('Not connected');

    return await this.signer.signMessage(message);
  }

  onAccountChanged(account) {
    // Handle account change in game
    console.log('Account changed to:', account);
  }
}
```

### Week 3: NFT Integration

```javascript
// ERC-721 NFT Contract Interaction
class GameNFTManager {
  constructor(web3Client, contractAddress, abi) {
    this.web3 = web3Client;
    this.contract = new ethers.Contract(
      contractAddress,
      abi,
      web3Client.signer
    );
  }

  async mintCharacter(characterData) {
    const metadata = {
      name: characterData.name,
      description: characterData.description,
      image: characterData.imageUrl,
      attributes: [
        { trait_type: 'Level', value: characterData.level },
        { trait_type: 'Strength', value: characterData.strength },
        { trait_type: 'Agility', value: characterData.agility },
        { trait_type: 'Intelligence', value: characterData.intelligence }
      ]
    };

    // Upload metadata to IPFS
    const metadataUri = await this.uploadToIPFS(metadata);

    // Mint NFT
    const tx = await this.contract.mint(metadataUri);
    await tx.wait();

    return tx.hash;
  }

  async getPlayerNFTs(address) {
    const balance = await this.contract.balanceOf(address);
    const nfts = [];

    for (let i = 0; i < balance; i++) {
      const tokenId = await this.contract.tokenOfOwnerByIndex(address, i);
      const tokenUri = await this.contract.tokenURI(tokenId);
      const metadata = await this.fetchMetadata(tokenUri);

      nfts.push({
        tokenId: tokenId.toString(),
        metadata
      });
    }

    return nfts;
  }

  async transferNFT(to, tokenId) {
    const from = this.web3.account;
    const tx = await this.contract.transferFrom(from, to, tokenId);
    await tx.wait();

    return tx.hash;
  }

  async upgradeNFT(tokenId, newStats) {
    // Update character stats (requires custom contract function)
    const tx = await this.contract.upgradeCharacter(
      tokenId,
      newStats.level,
      newStats.strength,
      newStats.agility,
      newStats.intelligence
    );

    await tx.wait();
    return tx.hash;
  }

  async uploadToIPFS(data) {
    // Using Pinata or similar IPFS service
    const formData = new FormData();
    formData.append('file', JSON.stringify(data));

    const response = await fetch('https://api.pinata.cloud/pinning/pinJSONToIPFS', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.PINATA_JWT}`
      },
      body: formData
    });

    const result = await response.json();
    return `ipfs://${result.IpfsHash}`;
  }

  async fetchMetadata(uri) {
    if (uri.startsWith('ipfs://')) {
      const hash = uri.replace('ipfs://', '');
      uri = `https://ipfs.io/ipfs/${hash}`;
    }

    const response = await fetch(uri);
    return await response.json();
  }
}
```

### Week 4: Play-to-Earn Mechanics

```javascript
// ERC-20 Token Integration
class GameTokenEconomy {
  constructor(web3Client, tokenAddress, abi) {
    this.web3 = web3Client;
    this.token = new ethers.Contract(
      tokenAddress,
      abi,
      web3Client.signer
    );
  }

  async getTokenBalance(address = null) {
    const account = address || this.web3.account;
    const balance = await this.token.balanceOf(account);
    return ethers.utils.formatEther(balance);
  }

  async rewardPlayer(amount, reason) {
    // Backend signs reward claim
    const signature = await this.getRewardSignature(
      this.web3.account,
      amount,
      reason
    );

    // Player claims reward on-chain
    const tx = await this.token.claimReward(
      ethers.utils.parseEther(amount),
      reason,
      signature
    );

    await tx.wait();
    return tx.hash;
  }

  async stakeTokens(amount, duration) {
    const amountWei = ethers.utils.parseEther(amount);

    // Approve staking contract
    const approveTx = await this.token.approve(
      this.stakingContractAddress,
      amountWei
    );
    await approveTx.wait();

    // Stake tokens
    const stakeTx = await this.stakingContract.stake(amountWei, duration);
    await stakeTx.wait();

    return stakeTx.hash;
  }

  async getStakingRewards() {
    const rewards = await this.stakingContract.pendingRewards(this.web3.account);
    return ethers.utils.formatEther(rewards);
  }

  async claimStakingRewards() {
    const tx = await this.stakingContract.claimRewards();
    await tx.wait();
    return tx.hash;
  }

  // Off-chain balance for gas-less transactions
  async getOffChainBalance() {
    const response = await fetch(
      `https://api.game.com/balance/${this.web3.account}`
    );
    return await response.json();
  }

  async withdrawToChain(amount) {
    // Request withdrawal from off-chain to on-chain
    const response = await fetch('https://api.game.com/withdraw', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        address: this.web3.account,
        amount
      })
    });

    return await response.json();
  }
}
```

### Week 5: Smart Contract Integration

```solidity
// GameAsset.sol - Example NFT Contract
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GameAsset is ERC721URIStorage, Ownable {
    uint256 private _tokenIdCounter;

    struct CharacterStats {
        uint8 level;
        uint16 strength;
        uint16 agility;
        uint16 intelligence;
        uint256 experience;
    }

    mapping(uint256 => CharacterStats) public characterStats;

    event CharacterMinted(uint256 tokenId, address owner);
    event CharacterUpgraded(uint256 tokenId, uint8 newLevel);

    constructor() ERC721("GameCharacter", "GCHAR") {}

    function mint(string memory uri) public returns (uint256) {
        uint256 tokenId = _tokenIdCounter++;
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, uri);

        // Initialize stats
        characterStats[tokenId] = CharacterStats({
            level: 1,
            strength: 10,
            agility: 10,
            intelligence: 10,
            experience: 0
        });

        emit CharacterMinted(tokenId, msg.sender);
        return tokenId;
    }

    function upgradeCharacter(
        uint256 tokenId,
        uint8 level,
        uint16 strength,
        uint16 agility,
        uint16 intelligence
    ) public {
        require(ownerOf(tokenId) == msg.sender, "Not owner");

        CharacterStats storage stats = characterStats[tokenId];
        require(level > stats.level, "Level must increase");

        stats.level = level;
        stats.strength = strength;
        stats.agility = agility;
        stats.intelligence = intelligence;

        emit CharacterUpgraded(tokenId, level);
    }

    function addExperience(uint256 tokenId, uint256 exp) public onlyOwner {
        characterStats[tokenId].experience += exp;
    }

    function getCharacterStats(uint256 tokenId)
        public
        view
        returns (CharacterStats memory)
    {
        return characterStats[tokenId];
    }
}
```

```solidity
// GameToken.sol - ERC-20 Game Token
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GameToken is ERC20, Ownable {
    mapping(address => bool) public gameServers;
    mapping(bytes32 => bool) public claimedRewards;

    event RewardClaimed(address player, uint256 amount, string reason);

    constructor() ERC20("GameToken", "GTK") {
        _mint(msg.sender, 1000000 * 10**decimals());
    }

    function addGameServer(address server) public onlyOwner {
        gameServers[server] = true;
    }

    function claimReward(
        uint256 amount,
        string memory reason,
        bytes memory signature
    ) public {
        bytes32 messageHash = keccak256(
            abi.encodePacked(msg.sender, amount, reason)
        );

        require(!claimedRewards[messageHash], "Already claimed");
        require(verifySignature(messageHash, signature), "Invalid signature");

        claimedRewards[messageHash] = true;
        _mint(msg.sender, amount);

        emit RewardClaimed(msg.sender, amount, reason);
    }

    function verifySignature(bytes32 messageHash, bytes memory signature)
        internal
        view
        returns (bool)
    {
        bytes32 ethSignedMessageHash = getEthSignedMessageHash(messageHash);
        address signer = recoverSigner(ethSignedMessageHash, signature);

        return gameServers[signer];
    }

    function getEthSignedMessageHash(bytes32 messageHash)
        internal
        pure
        returns (bytes32)
    {
        return keccak256(
            abi.encodePacked("\x19Ethereum Signed Message:\n32", messageHash)
        );
    }

    function recoverSigner(bytes32 ethSignedMessageHash, bytes memory signature)
        internal
        pure
        returns (address)
    {
        (bytes32 r, bytes32 s, uint8 v) = splitSignature(signature);
        return ecrecover(ethSignedMessageHash, v, r, s);
    }

    function splitSignature(bytes memory sig)
        internal
        pure
        returns (bytes32 r, bytes32 s, uint8 v)
    {
        require(sig.length == 65, "Invalid signature length");

        assembly {
            r := mload(add(sig, 32))
            s := mload(add(sig, 64))
            v := byte(0, mload(add(sig, 96)))
        }
    }
}
```

### Week 6: Marketplace & Trading

```javascript
class NFTMarketplace {
  constructor(web3Client, marketplaceAddress, abi) {
    this.web3 = web3Client;
    this.marketplace = new ethers.Contract(
      marketplaceAddress,
      abi,
      web3Client.signer
    );
  }

  async listNFT(nftContract, tokenId, price) {
    // Approve marketplace
    const nft = new ethers.Contract(
      nftContract,
      ['function approve(address,uint256)'],
      this.web3.signer
    );

    const approveTx = await nft.approve(this.marketplace.address, tokenId);
    await approveTx.wait();

    // List on marketplace
    const priceWei = ethers.utils.parseEther(price);
    const listTx = await this.marketplace.listItem(
      nftContract,
      tokenId,
      priceWei
    );

    await listTx.wait();
    return listTx.hash;
  }

  async buyNFT(listingId, price) {
    const priceWei = ethers.utils.parseEther(price);

    const tx = await this.marketplace.buyItem(listingId, {
      value: priceWei
    });

    await tx.wait();
    return tx.hash;
  }

  async getActiveListings() {
    const listings = await this.marketplace.getActiveListings();

    return Promise.all(
      listings.map(async (listing) => ({
        listingId: listing.id.toString(),
        seller: listing.seller,
        nftContract: listing.nftContract,
        tokenId: listing.tokenId.toString(),
        price: ethers.utils.formatEther(listing.price),
        metadata: await this.fetchNFTMetadata(
          listing.nftContract,
          listing.tokenId
        )
      }))
    );
  }

  async cancelListing(listingId) {
    const tx = await this.marketplace.cancelListing(listingId);
    await tx.wait();
    return tx.hash;
  }
}
```

### Week 7: Tokenomics Design

```javascript
class GameEconomy {
  constructor() {
    this.tokenMetrics = {
      totalSupply: 1000000000,
      circulatingSupply: 0,
      burnedTokens: 0,
      stakingPool: 0,
      rewardPool: 0
    };

    this.distribution = {
      team: 0.15,           // 15%
      ecosystem: 0.30,      // 30%
      playToEarn: 0.40,     // 40%
      liquidity: 0.10,      // 10%
      marketing: 0.05       // 5%
    };

    this.vestingSchedule = this.createVestingSchedule();
  }

  createVestingSchedule() {
    return {
      team: {
        cliff: 365,         // 1 year cliff
        duration: 1095,     // 3 years total
        portions: 36        // Monthly unlocks
      },
      ecosystem: {
        cliff: 0,
        duration: 1825,     // 5 years
        portions: 60        // Monthly unlocks
      }
    };
  }

  calculateReward(action, performance) {
    const baseRewards = {
      win_match: 10,
      complete_quest: 5,
      daily_login: 1,
      tournament_top10: 100
    };

    let reward = baseRewards[action] || 0;

    // Performance multiplier
    if (performance > 0.8) {
      reward *= 1.5;
    } else if (performance > 0.6) {
      reward *= 1.2;
    }

    // Apply inflation control
    reward *= this.getInflationMultiplier();

    return reward;
  }

  getInflationMultiplier() {
    const circulationRate = this.tokenMetrics.circulatingSupply /
                           this.tokenMetrics.totalSupply;

    if (circulationRate > 0.8) {
      return 0.5;  // Reduce rewards
    } else if (circulationRate > 0.6) {
      return 0.75;
    }

    return 1.0;
  }

  calculateBurnRate(transactionVolume) {
    // Dynamic burn based on transaction volume
    return Math.min(0.05, transactionVolume * 0.001);
  }
}
```

---

## 🎓 Projects

1. **NFT Character System** - Mint, upgrade, and trade characters
2. **Play-to-Earn Game** - Complete token economy
3. **NFT Marketplace** - Buy/sell game assets
4. **DAO Governance** - Community-governed game

---

## 📖 Resources

- Ethereum documentation
- OpenZeppelin contracts
- "Mastering Ethereum" by Antonopoulos
- Moralis Web3 documentation

---

## ✅ Assessment

**Passing Grade:** 75%
- Smart contract implementation (35%)
- NFT integration (25%)
- Tokenomics design (20%)
- Final project (20%)

**Career Paths:** Blockchain Developer, Web3 Game Developer, Smart Contract Engineer

**Salary Range:** $90,000 - $180,000

---

**Module Created:** 2025-11-02
