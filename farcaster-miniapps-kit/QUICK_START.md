# Farcaster Miniapps Kit - Quick Start Guide

## 🚀 5-Minute Setup

### 1. Copy Kit to Your Project

```bash
cp -r farcaster-miniapps-kit/.claude /your/project/
cd /your/project
```

### 2. Create New Miniapp

In Claude Code, type:
```
/new-miniapp
```

Or naturally:
```
Create a new Farcaster miniapp for [your idea]
```

### 3. Configure Manifest

```
/add-manifest
```

Then follow prompts to:
- Generate signature at https://warpcast.com/~/settings/developer-tools
- Add environment variables
- Configure images

### 4. Add Features

```
/setup-auth          # Add Quick Auth authentication
/add-embed          # Make pages shareable
/add-wallet         # Add Ethereum/Solana (optional)
/add-notifications  # Enable push notifications (optional)
```

### 5. Deploy

```
/deploy-miniapp
```

## 📦 What You Get

### 6 Skills

1. **miniapp-generator** - Create new projects
2. **manifest-builder** - Configure manifests
3. **embed-creator** - Shareable embeds
4. **sdk-integration** - SDK setup
5. **notification-system** - Push notifications
6. **wallet-integration** - Web3 wallets

### 8 Commands

- `/new-miniapp` - Start project
- `/add-manifest` - Add manifest
- `/add-embed` - Create embed
- `/setup-auth` - Setup auth
- `/add-notifications` - Add notifications
- `/add-wallet` - Add wallet
- `/deploy-miniapp` - Deploy
- `/debug-miniapp` - Debug

### 4 Agents

- **miniapp-architect** - Architecture consultant
- **authentication-specialist** - Auth expert
- **wallet-consultant** - Wallet expert
- **debugging-expert** - Troubleshooting

### 4 Hooks

- Manifest validation
- SDK ready() check
- HTTPS enforcement
- Node version check

## ⚠️ Critical Requirements

### 1. Node.js 22.11.0+

```bash
node --version  # Must be v22.11.0 or higher
```

### 2. Call sdk.actions.ready()

**MOST COMMON ISSUE** - Forgetting this causes infinite loading:

```typescript
useEffect(() => {
  async function init() {
    await new Promise<void>(resolve => {
      if (document.readyState === 'complete') resolve();
      else window.addEventListener('load', () => resolve());
    });
    await sdk.actions.ready(); // CRITICAL!
  }
  init();
}, []);
```

### 3. HTTPS URLs Only

```typescript
// ✅ Production
homeUrl: 'https://myapp.com'

// ❌ Development only
homeUrl: 'https://xyz.ngrok.io'
```

### 4. Never Trust Context

```typescript
// ❌ WRONG
if (context.user?.fid === adminFid) { /* Insecure */ }

// ✅ CORRECT
const token = await quickAuth.getToken();
// Verify on backend
```

## 🎯 Common Workflows

### Create Game Miniapp

```
You: Create a Farcaster miniapp for a multiplayer game
Claude: [Creates project with game structure]

You: Add Ethereum wallet integration
Claude: [Adds wallet support]

You: Setup notifications for game events
Claude: [Configures notification system]
```

### Create Social App

```
You: Build a Farcaster miniapp for community polls
Claude: [Creates project]

You: Add authentication
Claude: [Implements Quick Auth]

You: Make poll results shareable
Claude: [Creates embeds]
```

### Create DeFi App

```
You: Create a token swap miniapp
Claude: [Creates project]

You: Integrate Ethereum wallet
Claude: [Adds wallet with contract interaction]

You: Support multiple chains
Claude: [Adds multi-chain support]
```

## 🐛 Troubleshooting

### Infinite Loading

```
Problem: App stuck on splash screen
Solution: Check sdk.actions.ready() is called

Debug:
/debug-miniapp
```

### Manifest 404

```
Problem: /.well-known/farcaster.json not found
Solution: Check route path

Next.js App Router:
app/.well-known/farcaster.json/route.ts
```

### SDK Actions Fail

```
Problem: composeCast() etc. don't work
Solution: Use production HTTPS domain

Check:
- Not using ngrok/cloudflared URLs
- Called ready() first
```

## 📚 Learn More

### Documentation

- **Full README**: [README.md](./README.md)
- **Farcaster Docs**: https://miniapps.farcaster.xyz
- **SDK Reference**: https://miniapps.farcaster.xyz/docs/sdk

### Developer Tools

- **Warpcast Dev Tools**: https://warpcast.com/~/settings/developer-tools
- **Create CLI**: `npm create @farcaster/mini-app`
- **Tunnel**: cloudflared, ngrok

### Community

- **Warpcast**: /farcaster-dev channel
- **GitHub**: https://github.com/farcasterxyz/miniapps

## 🎓 Example Projects

### Minimal Example

```typescript
// app/page.tsx
'use client';
import { useEffect } from 'react';
import { sdk } from '@/lib/sdk';

export default function Home() {
  useEffect(() => {
    async function init() {
      await new Promise<void>(resolve => {
        if (document.readyState === 'complete') resolve();
        else window.addEventListener('load', () => resolve());
      });
      await sdk.actions.ready();
    }
    init();
  }, []);

  const context = sdk.context;

  return (
    <main className="p-8">
      <h1>Welcome, @{context?.user?.username || 'friend'}!</h1>
      <button onClick={() => sdk.actions.composeCast({ text: 'Hello!' })}>
        Create Cast
      </button>
    </main>
  );
}
```

### With Authentication

```typescript
const token = await quickAuth.getToken();

await fetch('/api/protected', {
  headers: { 'Authorization': `Bearer ${token}` },
});
```

### With Wallet

```typescript
const provider = sdk.wallet.getEthereumProvider();
const ethersProvider = new BrowserProvider(provider);
const signer = await ethersProvider.getSigner();
const address = await signer.getAddress();
```

## ✅ Deployment Checklist

- [ ] Node.js 22.11.0+
- [ ] sdk.actions.ready() called
- [ ] Manifest at /.well-known/farcaster.json
- [ ] All URLs use HTTPS
- [ ] Images optimized
- [ ] Tested in Warpcast preview
- [ ] Environment variables set
- [ ] Error handling implemented

## 🎯 Next Steps

1. **Explore Skills**: Browse `.claude/skills/` for detailed guides
2. **Try Commands**: Use slash commands for quick tasks
3. **Ask Agents**: Consult specialists for expert advice
4. **Build**: Start creating your miniapp!

---

**Need Help?**

- Ask Claude Code naturally: "How do I...?"
- Use `/debug-miniapp` for troubleshooting
- Consult agents for specialized advice
- Check official docs at miniapps.farcaster.xyz

**Ready? Start with `/new-miniapp`!** 🚀
