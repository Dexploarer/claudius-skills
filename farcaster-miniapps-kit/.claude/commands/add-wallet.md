# Add Wallet Integration

Integrate Ethereum or Solana wallet for on-chain transactions.

## Steps

1. Check wallet capabilities:
```typescript
const capabilities = sdk.getCapabilities();
const hasEthWallet = capabilities.includes('ethereum_provider');
const hasSolWallet = capabilities.includes('solana_provider');
```

2. Install web3 libraries:
```bash
# For Ethereum
npm install ethers@6

# For Solana
npm install @solana/web3.js
```

3. Create Ethereum wallet service in `lib/ethereum.ts`:
```typescript
import { BrowserProvider } from 'ethers';
import { sdk } from './sdk';

export async function connectEthereumWallet() {
  const provider = new BrowserProvider(
    sdk.wallet.getEthereumProvider()
  );

  const signer = await provider.getSigner();
  const address = await signer.getAddress();

  return { provider, signer, address };
}
```

4. Create wallet component:
```typescript
'use client';

export function WalletConnect() {
  const [address, setAddress] = useState<string | null>(null);

  async function connect() {
    const { address } = await connectEthereumWallet();
    setAddress(address);
  }

  return (
    <button onClick={connect}>
      {address ? `Connected: ${address.slice(0, 6)}...` : 'Connect Wallet'}
    </button>
  );
}
```

5. Implement transactions:
```typescript
async function sendTransaction(to: string, amount: string) {
  const { signer } = await connectEthereumWallet();

  const tx = await signer.sendTransaction({
    to,
    value: parseEther(amount),
  });

  return await tx.wait();
}
```

## Security Notes

- Always validate addresses
- Confirm transactions with user
- Handle errors gracefully
- Check network/chain ID
- Display gas estimates
