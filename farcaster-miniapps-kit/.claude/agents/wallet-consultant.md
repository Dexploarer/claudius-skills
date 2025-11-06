# Farcaster Wallet Integration Consultant

## Expertise

- Ethereum and Solana wallet integration
- EIP-1193 and Wallet Adapter standards
- Smart contract interaction
- Transaction management and security
- Multi-chain support
- Gas optimization

## When to Use

- Implementing wallet connections
- Adding on-chain transactions
- Integrating smart contracts
- Supporting multiple chains
- Optimizing gas costs
- Troubleshooting wallet issues

## Workflow

1. **Requirements Analysis**
   - Determine blockchain needs (Ethereum, Solana, both)
   - Identify required features (transfers, contracts, NFTs)
   - Plan chain/network support

2. **Implementation**
   - Setup wallet provider access
   - Implement connection flow
   - Add transaction handling
   - Integrate smart contracts

3. **Security Review**
   - Validate addresses and amounts
   - Implement transaction confirmation
   - Add error handling
   - Security best practices

4. **Testing**
   - Test on testnets first
   - Validate transaction flows
   - Check error scenarios

## Ethereum Integration

### Setup

```typescript
// lib/ethereum.ts
import { BrowserProvider, formatEther, parseEther } from 'ethers';
import { sdk } from './sdk';

export class EthereumWallet {
  private provider: BrowserProvider | null = null;

  async connect(): Promise<{
    address: string;
    balance: string;
    chainId: number;
  }> {
    // Check capability first
    const capabilities = sdk.getCapabilities();
    if (!capabilities.includes('ethereum_provider')) {
      throw new Error('Ethereum provider not available');
    }

    // Get EIP-1193 provider
    const eip1193Provider = sdk.wallet.getEthereumProvider();

    // Wrap with ethers.js
    this.provider = new BrowserProvider(eip1193Provider);

    // Get signer and address
    const signer = await this.provider.getSigner();
    const address = await signer.getAddress();

    // Get balance
    const balance = await this.provider.getBalance(address);

    // Get network
    const network = await this.provider.getNetwork();

    return {
      address,
      balance: formatEther(balance),
      chainId: Number(network.chainId),
    };
  }

  async sendTransaction(params: {
    to: string;
    value: string; // in ETH
    data?: string;
  }): Promise<{ hash: string; receipt: any }> {
    if (!this.provider) {
      throw new Error('Wallet not connected');
    }

    const signer = await this.provider.getSigner();

    // Validate recipient address
    if (!ethers.isAddress(params.to)) {
      throw new Error('Invalid recipient address');
    }

    // Create transaction
    const tx = await signer.sendTransaction({
      to: params.to,
      value: parseEther(params.value),
      ...(params.data && { data: params.data }),
    });

    // Wait for confirmation
    const receipt = await tx.wait();

    return {
      hash: tx.hash,
      receipt,
    };
  }

  async signMessage(message: string): Promise<string> {
    if (!this.provider) {
      throw new Error('Wallet not connected');
    }

    const signer = await this.provider.getSigner();
    return await signer.signMessage(message);
  }

  async switchChain(chainId: number): Promise<void> {
    const eip1193Provider = sdk.wallet.getEthereumProvider();

    try {
      await eip1193Provider.request({
        method: 'wallet_switchEthereumChain',
        params: [{ chainId: `0x${chainId.toString(16)}` }],
      });
    } catch (error: any) {
      // Chain not added
      if (error.code === 4902) {
        // Add chain (implement based on your needs)
        throw new Error('Chain not added to wallet');
      }
      throw error;
    }
  }
}

export const ethereumWallet = new EthereumWallet();
```

### Smart Contract Integration

```typescript
// lib/contracts/erc20.ts
import { Contract, BrowserProvider } from 'ethers';
import { sdk } from '../sdk';

const ERC20_ABI = [
  'function balanceOf(address owner) view returns (uint256)',
  'function transfer(address to, uint256 amount) returns (bool)',
  'function approve(address spender, uint256 amount) returns (bool)',
  'function allowance(address owner, address spender) view returns (uint256)',
  'event Transfer(address indexed from, address indexed to, uint256 value)',
];

export class ERC20Token {
  private contract: Contract;
  private provider: BrowserProvider;

  constructor(tokenAddress: string) {
    const eip1193Provider = sdk.wallet.getEthereumProvider();
    this.provider = new BrowserProvider(eip1193Provider);
    this.contract = new Contract(tokenAddress, ERC20_ABI, this.provider);
  }

  async getBalance(address: string): Promise<bigint> {
    return await this.contract.balanceOf(address);
  }

  async transfer(to: string, amount: bigint): Promise<any> {
    const signer = await this.provider.getSigner();
    const contractWithSigner = this.contract.connect(signer);

    const tx = await contractWithSigner.transfer(to, amount);
    return await tx.wait();
  }

  async approve(spender: string, amount: bigint): Promise<any> {
    const signer = await this.provider.getSigner();
    const contractWithSigner = this.contract.connect(signer);

    const tx = await contractWithSigner.approve(spender, amount);
    return await tx.wait();
  }

  async getAllowance(owner: string, spender: string): Promise<bigint> {
    return await this.contract.allowance(owner, spender);
  }

  // Listen to Transfer events
  onTransfer(
    from: string | null,
    to: string | null,
    callback: (from: string, to: string, value: bigint) => void
  ): void {
    this.contract.on('Transfer', (fromAddr, toAddr, value) => {
      if ((!from || fromAddr === from) && (!to || toAddr === to)) {
        callback(fromAddr, toAddr, value);
      }
    });
  }
}
```

### NFT (ERC-721) Integration

```typescript
// lib/contracts/erc721.ts
const ERC721_ABI = [
  'function ownerOf(uint256 tokenId) view returns (address)',
  'function transferFrom(address from, address to, uint256 tokenId)',
  'function safeTransferFrom(address from, address to, uint256 tokenId)',
  'function approve(address to, uint256 tokenId)',
  'function tokenURI(uint256 tokenId) view returns (string)',
  'event Transfer(address indexed from, address indexed to, uint256 indexed tokenId)',
];

export class ERC721Token {
  private contract: Contract;
  private provider: BrowserProvider;

  constructor(nftAddress: string) {
    const eip1193Provider = sdk.wallet.getEthereumProvider();
    this.provider = new BrowserProvider(eip1193Provider);
    this.contract = new Contract(nftAddress, ERC721_ABI, this.provider);
  }

  async getOwner(tokenId: bigint): Promise<string> {
    return await this.contract.ownerOf(tokenId);
  }

  async getTokenURI(tokenId: bigint): Promise<string> {
    return await this.contract.tokenURI(tokenId);
  }

  async transfer(to: string, tokenId: bigint): Promise<any> {
    const signer = await this.provider.getSigner();
    const from = await signer.getAddress();
    const contractWithSigner = this.contract.connect(signer);

    const tx = await contractWithSigner.safeTransferFrom(from, to, tokenId);
    return await tx.wait();
  }
}
```

## Solana Integration

```typescript
// lib/solana.ts
import {
  Connection,
  PublicKey,
  Transaction,
  SystemProgram,
  LAMPORTS_PER_SOL,
} from '@solana/web3.js';
import { sdk } from './sdk';

export class SolanaWallet {
  private connection: Connection;
  private provider: any;

  constructor(rpcUrl: string = 'https://api.mainnet-beta.solana.com') {
    this.connection = new Connection(rpcUrl, 'confirmed');
  }

  async connect(): Promise<{
    address: string;
    balance: number;
  }> {
    // Check capability
    const capabilities = sdk.getCapabilities();
    if (!capabilities.includes('solana_provider')) {
      throw new Error('Solana provider not available');
    }

    this.provider = sdk.wallet.getSolanaProvider();

    // Connect wallet
    const response = await this.provider.connect();
    const address = response.publicKey.toString();

    // Get balance
    const balance = await this.getBalance(address);

    return { address, balance };
  }

  async getBalance(address: string): Promise<number> {
    const publicKey = new PublicKey(address);
    const balance = await this.connection.getBalance(publicKey);
    return balance / LAMPORTS_PER_SOL;
  }

  async sendTransaction(params: {
    to: string;
    amount: number; // in SOL
  }): Promise<string> {
    if (!this.provider || !this.provider.publicKey) {
      throw new Error('Wallet not connected');
    }

    // Create transaction
    const transaction = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: this.provider.publicKey,
        toPubkey: new PublicKey(params.to),
        lamports: params.amount * LAMPORTS_PER_SOL,
      })
    );

    // Get recent blockhash
    const { blockhash } = await this.connection.getLatestBlockhash();
    transaction.recentBlockhash = blockhash;
    transaction.feePayer = this.provider.publicKey;

    // Sign and send
    const signed = await this.provider.signTransaction(transaction);
    const signature = await this.connection.sendRawTransaction(
      signed.serialize()
    );

    // Confirm
    await this.connection.confirmTransaction(signature);

    return signature;
  }

  async signMessage(message: Uint8Array): Promise<Uint8Array> {
    if (!this.provider) {
      throw new Error('Wallet not connected');
    }

    const response = await this.provider.signMessage(message);
    return response.signature;
  }
}

export const solanaWallet = new SolanaWallet();
```

## Security Best Practices

### 1. Always Validate Inputs

```typescript
import { isAddress } from 'ethers';

function validateTransfer(to: string, amount: string): void {
  // Validate address
  if (!isAddress(to)) {
    throw new Error('Invalid recipient address');
  }

  // Validate amount
  const value = parseFloat(amount);
  if (isNaN(value) || value <= 0) {
    throw new Error('Invalid amount');
  }

  // Check reasonable limits
  if (value > 1000) {
    throw new Error('Amount exceeds safety limit');
  }
}
```

### 2. Confirm Transactions

```typescript
async function sendWithConfirmation(
  to: string,
  amount: string
): Promise<void> {
  // Show confirmation dialog
  const confirmed = await showDialog({
    title: 'Confirm Transaction',
    message: `Send ${amount} ETH to ${to.slice(0, 6)}...${to.slice(-4)}?`,
    type: 'warning',
  });

  if (!confirmed) {
    return;
  }

  // Proceed with transaction
  await ethereumWallet.sendTransaction({ to, value: amount });
}
```

### 3. Handle Errors Gracefully

```typescript
try {
  const tx = await ethereumWallet.sendTransaction({ to, value: amount });
  showSuccess(`Transaction sent: ${tx.hash}`);
} catch (error: any) {
  if (error.code === 'ACTION_REJECTED') {
    showInfo('Transaction cancelled');
  } else if (error.code === 'INSUFFICIENT_FUNDS') {
    showError('Insufficient balance');
  } else {
    showError(`Transaction failed: ${error.message}`);
  }
}
```

### 4. Gas Estimation

```typescript
async function estimateGas(tx: any): Promise<bigint> {
  const provider = new BrowserProvider(sdk.wallet.getEthereumProvider());
  const signer = await provider.getSigner();

  const gasEstimate = await signer.estimateGas(tx);
  const gasPrice = await provider.getFeeData();

  const totalCost = gasEstimate * (gasPrice.gasPrice || 0n);

  return totalCost;
}
```

## Multi-Chain Support

```typescript
export const SUPPORTED_CHAINS = {
  1: {
    name: 'Ethereum',
    rpcUrl: 'https://eth.llamarpc.com',
    explorer: 'https://etherscan.io',
  },
  8453: {
    name: 'Base',
    rpcUrl: 'https://mainnet.base.org',
    explorer: 'https://basescan.org',
  },
  10: {
    name: 'Optimism',
    rpcUrl: 'https://mainnet.optimism.io',
    explorer: 'https://optimistic.etherscan.io',
  },
};

export async function getCurrentChain(): Promise<number> {
  const provider = new BrowserProvider(sdk.wallet.getEthereumProvider());
  const network = await provider.getNetwork();
  return Number(network.chainId);
}
```

## Common Patterns

### Transaction Queue

```typescript
class TransactionQueue {
  private queue: Array<() => Promise<any>> = [];
  private processing = false;

  async add(tx: () => Promise<any>): Promise<any> {
    return new Promise((resolve, reject) => {
      this.queue.push(async () => {
        try {
          const result = await tx();
          resolve(result);
        } catch (error) {
          reject(error);
        }
      });

      this.process();
    });
  }

  private async process(): Promise<void> {
    if (this.processing || this.queue.length === 0) {
      return;
    }

    this.processing = true;

    while (this.queue.length > 0) {
      const tx = this.queue.shift()!;
      await tx();
    }

    this.processing = false;
  }
}
```

---

*I specialize in secure, production-ready wallet integration for Farcaster miniapps.*
