---
name: wallet-integration
description: Integrate Ethereum and Solana wallet providers for on-chain transactions in Farcaster miniapps
version: 1.0.0
category: farcaster
tags: [farcaster, miniapps, wallet, ethereum, solana, web3]
author: Claudius Skills
---

# Farcaster Miniapp Wallet Integration

## Purpose

This skill helps you integrate Ethereum and Solana wallet providers into your Farcaster miniapp, enabling users to:
- Connect their wallets
- Sign transactions
- Interact with smart contracts
- Send tokens and NFTs
- Execute batch transactions
- Switch networks/chains

## Activation Phrases

- "integrate wallet into miniapp"
- "add ethereum wallet"
- "setup solana wallet"
- "implement wallet connection"
- "add web3 wallet"
- "setup miniapp wallet integration"

## Understanding Wallet Providers

Farcaster miniapps expose **EIP-1193** (Ethereum) and **Solana Wallet Adapter** compatible providers through the SDK.

**Key Concepts**:
- **Provider**: Interface to interact with blockchain
- **Signer**: User's wallet that signs transactions
- **Chain**: Network (Ethereum mainnet, Base, etc.)
- **Account**: User's wallet address

## Prerequisites

1. **SDK Installed**:
   ```bash
   npm install @farcaster/miniapp-sdk
   ```

2. **Web3 Libraries**:
   ```bash
   # For Ethereum
   npm install ethers@6 viem@2

   # For Solana
   npm install @solana/web3.js @solana/wallet-adapter-base
   ```

3. **Check Capabilities**:
   ```typescript
   const capabilities = sdk.getCapabilities();
   const hasEthProvider = capabilities.includes('ethereum_provider');
   const hasSolProvider = capabilities.includes('solana_provider');
   ```

## Instructions

### Step 1: Ethereum Wallet Integration

**Get Ethereum Provider**:

```typescript
// lib/ethereum.ts
import { sdk } from './sdk';
import { BrowserProvider, formatEther, parseEther } from 'ethers';

export class EthereumWallet {
  private provider: BrowserProvider | null = null;

  async connect(): Promise<string> {
    try {
      // Get EIP-1193 provider from SDK
      const eip1193Provider = sdk.wallet.getEthereumProvider();

      // Wrap with ethers.js
      this.provider = new BrowserProvider(eip1193Provider);

      // Request account access
      const signer = await this.provider.getSigner();
      const address = await signer.getAddress();

      return address;
    } catch (error) {
      console.error('Failed to connect wallet:', error);
      throw error;
    }
  }

  async getBalance(address: string): Promise<string> {
    if (!this.provider) {
      throw new Error('Provider not connected');
    }

    const balance = await this.provider.getBalance(address);
    return formatEther(balance);
  }

  async getNetwork() {
    if (!this.provider) {
      throw new Error('Provider not connected');
    }

    return await this.provider.getNetwork();
  }

  async sendTransaction(to: string, amount: string) {
    if (!this.provider) {
      throw new Error('Provider not connected');
    }

    const signer = await this.provider.getSigner();

    const tx = await signer.sendTransaction({
      to,
      value: parseEther(amount),
    });

    return await tx.wait();
  }

  async signMessage(message: string): Promise<string> {
    if (!this.provider) {
      throw new Error('Provider not connected');
    }

    const signer = await this.provider.getSigner();
    return await signer.signMessage(message);
  }
}

export const ethereumWallet = new EthereumWallet();
```

**React Component**:

```typescript
'use client';

import { useState } from 'react';
import { ethereumWallet } from '@/lib/ethereum';
import { useMiniApp } from '@/components/MiniAppProvider';

export function EthereumWalletConnect() {
  const { capabilities } = useMiniApp();
  const [address, setAddress] = useState<string | null>(null);
  const [balance, setBalance] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const hasEthProvider = capabilities.includes('ethereum_provider');

  async function connect() {
    try {
      setLoading(true);

      const addr = await ethereumWallet.connect();
      setAddress(addr);

      const bal = await ethereumWallet.getBalance(addr);
      setBalance(bal);

    } catch (error) {
      console.error('Connection failed:', error);
    } finally {
      setLoading(false);
    }
  }

  if (!hasEthProvider) {
    return (
      <div className="p-4 bg-yellow-50 rounded-lg">
        <p className="text-yellow-800">
          Ethereum wallet not available in this client
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-4 p-4 bg-white rounded-lg shadow">
      <h2 className="text-xl font-bold">Ethereum Wallet</h2>

      {!address ? (
        <button
          onClick={connect}
          disabled={loading}
          className="px-4 py-2 bg-blue-600 text-white rounded-lg disabled:opacity-50"
        >
          {loading ? 'Connecting...' : 'Connect Wallet'}
        </button>
      ) : (
        <div className="space-y-2">
          <div>
            <p className="text-sm text-gray-600">Address</p>
            <p className="font-mono text-sm">{address}</p>
          </div>

          <div>
            <p className="text-sm text-gray-600">Balance</p>
            <p className="text-lg font-semibold">{balance} ETH</p>
          </div>
        </div>
      )}
    </div>
  );
}
```

### Step 2: Using Viem (Alternative to ethers.js)

```typescript
// lib/viem-wallet.ts
import { sdk } from './sdk';
import { createWalletClient, custom, publicActions } from 'viem';
import { mainnet, base } from 'viem/chains';

export function createViemWallet(chainId: number = 1) {
  const provider = sdk.wallet.getEthereumProvider();

  const chain = chainId === 8453 ? base : mainnet;

  const client = createWalletClient({
    chain,
    transport: custom(provider),
  }).extend(publicActions);

  return client;
}

// Usage
export async function sendEthWithViem(to: string, amount: string) {
  const client = createViemWallet();

  const [address] = await client.getAddresses();

  const hash = await client.sendTransaction({
    account: address,
    to,
    value: parseEther(amount),
  });

  const receipt = await client.waitForTransactionReceipt({ hash });
  return receipt;
}
```

### Step 3: Smart Contract Interaction

```typescript
// lib/contracts.ts
import { BrowserProvider, Contract, Interface } from 'ethers';
import { sdk } from './sdk';

// ERC-20 Token Interface
const ERC20_ABI = [
  'function balanceOf(address owner) view returns (uint256)',
  'function transfer(address to, uint256 amount) returns (bool)',
  'function approve(address spender, uint256 amount) returns (bool)',
  'function allowance(address owner, address spender) view returns (uint256)',
];

export class ERC20Contract {
  private contract: Contract;

  constructor(tokenAddress: string) {
    const provider = new BrowserProvider(sdk.wallet.getEthereumProvider());
    this.contract = new Contract(tokenAddress, ERC20_ABI, provider);
  }

  async getBalance(address: string): Promise<bigint> {
    return await this.contract.balanceOf(address);
  }

  async transfer(to: string, amount: bigint) {
    const signer = await this.contract.runner.provider.getSigner();
    const contractWithSigner = this.contract.connect(signer);

    const tx = await contractWithSigner.transfer(to, amount);
    return await tx.wait();
  }

  async approve(spender: string, amount: bigint) {
    const signer = await this.contract.runner.provider.getSigner();
    const contractWithSigner = this.contract.connect(signer);

    const tx = await contractWithSigner.approve(spender, amount);
    return await tx.wait();
  }
}

// NFT Contract (ERC-721)
const ERC721_ABI = [
  'function ownerOf(uint256 tokenId) view returns (address)',
  'function transferFrom(address from, address to, uint256 tokenId)',
  'function safeTransferFrom(address from, address to, uint256 tokenId)',
];

export class ERC721Contract {
  private contract: Contract;

  constructor(nftAddress: string) {
    const provider = new BrowserProvider(sdk.wallet.getEthereumProvider());
    this.contract = new Contract(nftAddress, ERC721_ABI, provider);
  }

  async ownerOf(tokenId: bigint): Promise<string> {
    return await this.contract.ownerOf(tokenId);
  }

  async transfer(to: string, tokenId: bigint) {
    const signer = await this.contract.runner.provider.getSigner();
    const from = await signer.getAddress();

    const contractWithSigner = this.contract.connect(signer);

    const tx = await contractWithSigner.transferFrom(from, to, tokenId);
    return await tx.wait();
  }
}
```

### Step 4: Solana Wallet Integration

```typescript
// lib/solana.ts
import { sdk } from './sdk';
import {
  Connection,
  PublicKey,
  Transaction,
  SystemProgram,
  LAMPORTS_PER_SOL,
} from '@solana/web3.js';

export class SolanaWallet {
  private connection: Connection;

  constructor(rpcUrl: string = 'https://api.mainnet-beta.solana.com') {
    this.connection = new Connection(rpcUrl, 'confirmed');
  }

  async connect(): Promise<string> {
    try {
      const provider = sdk.wallet.getSolanaProvider();

      // Request connection
      const response = await provider.connect();

      return response.publicKey.toString();
    } catch (error) {
      console.error('Failed to connect Solana wallet:', error);
      throw error;
    }
  }

  async getBalance(address: string): Promise<number> {
    const publicKey = new PublicKey(address);
    const balance = await this.connection.getBalance(publicKey);
    return balance / LAMPORTS_PER_SOL;
  }

  async sendTransaction(to: string, amount: number) {
    const provider = sdk.wallet.getSolanaProvider();

    if (!provider.publicKey) {
      throw new Error('Wallet not connected');
    }

    const transaction = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: provider.publicKey,
        toPubkey: new PublicKey(to),
        lamports: amount * LAMPORTS_PER_SOL,
      })
    );

    // Get recent blockhash
    const { blockhash } = await this.connection.getLatestBlockhash();
    transaction.recentBlockhash = blockhash;
    transaction.feePayer = provider.publicKey;

    // Sign and send
    const signed = await provider.signTransaction(transaction);
    const signature = await this.connection.sendRawTransaction(
      signed.serialize()
    );

    await this.connection.confirmTransaction(signature);

    return signature;
  }

  async signMessage(message: Uint8Array): Promise<Uint8Array> {
    const provider = sdk.wallet.getSolanaProvider();
    const response = await provider.signMessage(message);
    return response.signature;
  }
}

export const solanaWallet = new SolanaWallet();
```

**Solana React Component**:

```typescript
'use client';

import { useState } from 'react';
import { solanaWallet } from '@/lib/solana';
import { useMiniApp } from '@/components/MiniAppProvider';

export function SolanaWalletConnect() {
  const { capabilities } = useMiniApp();
  const [address, setAddress] = useState<string | null>(null);
  const [balance, setBalance] = useState<number | null>(null);
  const [loading, setLoading] = useState(false);

  const hasSolProvider = capabilities.includes('solana_provider');

  async function connect() {
    try {
      setLoading(true);

      const addr = await solanaWallet.connect();
      setAddress(addr);

      const bal = await solanaWallet.getBalance(addr);
      setBalance(bal);

    } catch (error) {
      console.error('Connection failed:', error);
    } finally {
      setLoading(false);
    }
  }

  if (!hasSolProvider) {
    return (
      <div className="p-4 bg-yellow-50 rounded-lg">
        <p className="text-yellow-800">
          Solana wallet not available in this client
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-4 p-4 bg-white rounded-lg shadow">
      <h2 className="text-xl font-bold">Solana Wallet</h2>

      {!address ? (
        <button
          onClick={connect}
          disabled={loading}
          className="px-4 py-2 bg-purple-600 text-white rounded-lg disabled:opacity-50"
        >
          {loading ? 'Connecting...' : 'Connect Wallet'}
        </button>
      ) : (
        <div className="space-y-2">
          <div>
            <p className="text-sm text-gray-600">Address</p>
            <p className="font-mono text-sm break-all">{address}</p>
          </div>

          <div>
            <p className="text-sm text-gray-600">Balance</p>
            <p className="text-lg font-semibold">{balance?.toFixed(4)} SOL</p>
          </div>
        </div>
      )}
    </div>
  );
}
```

### Step 5: Batch Transactions

Farcaster miniapps support batch transactions (sequential execution):

```typescript
// lib/batch-transactions.ts
import { BrowserProvider } from 'ethers';
import { sdk } from './sdk';

export async function executeBatchTransactions() {
  const provider = new BrowserProvider(sdk.wallet.getEthereumProvider());
  const signer = await provider.getSigner();

  // All transactions are validated and scanned individually
  // They execute sequentially with full security
  const transactions = [
    // 1. Approve token spending
    {
      to: TOKEN_ADDRESS,
      data: erc20.interface.encodeFunctionData('approve', [
        SPENDER_ADDRESS,
        amount,
      ]),
    },
    // 2. Transfer tokens
    {
      to: TOKEN_ADDRESS,
      data: erc20.interface.encodeFunctionData('transfer', [
        RECIPIENT_ADDRESS,
        amount,
      ]),
    },
  ];

  const results = [];

  for (const tx of transactions) {
    const result = await signer.sendTransaction(tx);
    const receipt = await result.wait();
    results.push(receipt);
  }

  return results;
}
```

### Step 6: Chain/Network Switching

```typescript
// lib/chain-utils.ts
export const SUPPORTED_CHAINS = {
  ethereum: {
    chainId: 1,
    name: 'Ethereum Mainnet',
    rpcUrl: 'https://eth.llamarpc.com',
    nativeCurrency: { name: 'Ether', symbol: 'ETH', decimals: 18 },
  },
  base: {
    chainId: 8453,
    name: 'Base',
    rpcUrl: 'https://mainnet.base.org',
    nativeCurrency: { name: 'Ether', symbol: 'ETH', decimals: 18 },
  },
  optimism: {
    chainId: 10,
    name: 'Optimism',
    rpcUrl: 'https://mainnet.optimism.io',
    nativeCurrency: { name: 'Ether', symbol: 'ETH', decimals: 18 },
  },
};

export async function switchChain(chainId: number) {
  const provider = sdk.wallet.getEthereumProvider();

  try {
    await provider.request({
      method: 'wallet_switchEthereumChain',
      params: [{ chainId: `0x${chainId.toString(16)}` }],
    });
  } catch (error: any) {
    // Chain not added to wallet
    if (error.code === 4902) {
      const chain = Object.values(SUPPORTED_CHAINS).find(
        c => c.chainId === chainId
      );

      if (chain) {
        await provider.request({
          method: 'wallet_addEthereumChain',
          params: [
            {
              chainId: `0x${chainId.toString(16)}`,
              chainName: chain.name,
              rpcUrls: [chain.rpcUrl],
              nativeCurrency: chain.nativeCurrency,
            },
          ],
        });
      }
    } else {
      throw error;
    }
  }
}
```

### Step 7: Complete Wallet Component

```typescript
'use client';

import { useState, useEffect } from 'react';
import { BrowserProvider, formatEther } from 'ethers';
import { sdk } from '@/lib/sdk';
import { useMiniApp } from '@/components/MiniAppProvider';

export function WalletDashboard() {
  const { capabilities } = useMiniApp();
  const [ethAddress, setEthAddress] = useState<string | null>(null);
  const [ethBalance, setEthBalance] = useState<string | null>(null);
  const [chainId, setChainId] = useState<number | null>(null);
  const [loading, setLoading] = useState(false);

  const hasEthProvider = capabilities.includes('ethereum_provider');

  async function connectEthereum() {
    try {
      setLoading(true);

      const provider = new BrowserProvider(sdk.wallet.getEthereumProvider());
      const signer = await provider.getSigner();
      const address = await signer.getAddress();

      setEthAddress(address);

      const balance = await provider.getBalance(address);
      setEthBalance(formatEther(balance));

      const network = await provider.getNetwork();
      setChainId(Number(network.chainId));

    } catch (error) {
      console.error('Failed to connect:', error);
    } finally {
      setLoading(false);
    }
  }

  async function sendEth() {
    if (!ethAddress) return;

    try {
      const provider = new BrowserProvider(sdk.wallet.getEthereumProvider());
      const signer = await provider.getSigner();

      const tx = await signer.sendTransaction({
        to: '0x...recipient',
        value: parseEther('0.001'),
      });

      await tx.wait();

      alert('Transaction sent!');
    } catch (error) {
      console.error('Transaction failed:', error);
    }
  }

  if (!hasEthProvider) {
    return (
      <div className="p-6 bg-yellow-50 rounded-lg">
        <p className="text-yellow-800">
          Wallet features not available in this client
        </p>
      </div>
    );
  }

  return (
    <div className="p-6 bg-white rounded-lg shadow-lg space-y-6">
      <h2 className="text-2xl font-bold">Wallet</h2>

      {!ethAddress ? (
        <button
          onClick={connectEthereum}
          disabled={loading}
          className="w-full px-6 py-3 bg-blue-600 text-white rounded-lg disabled:opacity-50"
        >
          {loading ? 'Connecting...' : 'Connect Wallet'}
        </button>
      ) : (
        <div className="space-y-4">
          <div className="p-4 bg-gray-50 rounded-lg">
            <p className="text-sm text-gray-600 mb-1">Address</p>
            <p className="font-mono text-sm break-all">{ethAddress}</p>
          </div>

          <div className="p-4 bg-gray-50 rounded-lg">
            <p className="text-sm text-gray-600 mb-1">Balance</p>
            <p className="text-2xl font-bold">{ethBalance} ETH</p>
          </div>

          <div className="p-4 bg-gray-50 rounded-lg">
            <p className="text-sm text-gray-600 mb-1">Network</p>
            <p className="font-semibold">
              {chainId === 1 && 'Ethereum Mainnet'}
              {chainId === 8453 && 'Base'}
              {chainId === 10 && 'Optimism'}
              {chainId && ![1, 8453, 10].includes(chainId) && `Chain ${chainId}`}
            </p>
          </div>

          <button
            onClick={sendEth}
            className="w-full px-6 py-3 bg-green-600 text-white rounded-lg"
          >
            Send Transaction
          </button>
        </div>
      )}
    </div>
  );
}
```

## Best Practices

### 1. Check Capabilities First

```typescript
// ✅ Correct
const capabilities = sdk.getCapabilities();
if (capabilities.includes('ethereum_provider')) {
  const provider = sdk.wallet.getEthereumProvider();
}

// ❌ Wrong - may throw error
const provider = sdk.wallet.getEthereumProvider();
```

### 2. Handle Errors Gracefully

```typescript
try {
  const tx = await signer.sendTransaction({...});
  await tx.wait();
} catch (error: any) {
  if (error.code === 'ACTION_REJECTED') {
    // User rejected transaction
    console.log('Transaction rejected');
  } else {
    // Other error
    console.error('Transaction failed:', error);
  }
}
```

### 3. Validate Addresses

```typescript
import { isAddress } from 'ethers';

function validateEthereumAddress(address: string): boolean {
  return isAddress(address);
}

// Solana
import { PublicKey } from '@solana/web3.js';

function validateSolanaAddress(address: string): boolean {
  try {
    new PublicKey(address);
    return true;
  } catch {
    return false;
  }
}
```

### 4. Use Proper Units

```typescript
// ✅ Correct - use parseEther/formatEther
import { parseEther, formatEther } from 'ethers';

const value = parseEther('1.5'); // 1.5 ETH in wei
const display = formatEther(value); // "1.5"

// ❌ Wrong - manual conversion prone to errors
const value = '1500000000000000000'; // Error-prone
```

### 5. Security Checks

```typescript
// Verify transaction parameters before sending
function validateTransaction(to: string, amount: string) {
  if (!isAddress(to)) {
    throw new Error('Invalid recipient address');
  }

  const value = parseEther(amount);
  if (value <= 0n) {
    throw new Error('Amount must be positive');
  }

  // Add more checks as needed
}
```

## Troubleshooting

### Provider Not Available

**Problem**: `getEthereumProvider()` throws error

**Solution**: Check capabilities first

### Transaction Fails

**Problem**: Transaction reverts or fails

**Solutions**:
- Check gas estimation
- Verify contract ABI
- Ensure sufficient balance
- Check network congestion

### Wrong Network

**Problem**: Connected to wrong chain

**Solution**: Implement chain switching or detect current chain

## Checklist

- [ ] Capability detection implemented
- [ ] Ethereum provider integrated
- [ ] Solana provider integrated (if needed)
- [ ] Error handling added
- [ ] Address validation implemented
- [ ] Transaction confirmation UI
- [ ] Chain/network detection
- [ ] Balance display
- [ ] Security checks in place
- [ ] User feedback for all actions

## Resources

- Wallet Guide: https://miniapps.farcaster.xyz/docs/guides/wallets
- EIP-1193: https://eips.ethereum.org/EIPS/eip-1193
- ethers.js: https://docs.ethers.org/v6/
- Viem: https://viem.sh/
- Solana Web3.js: https://solana-labs.github.io/solana-web3.js/

---

*This skill enables full blockchain wallet integration for your Farcaster miniapp.*
