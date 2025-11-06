# Farcaster Miniapps Kit - Claude Code Guidance

## Overview

This kit provides comprehensive tooling for building Farcaster miniapps with best practices, security, and production-ready patterns.

## Kit Contents

### Skills (6)
1. **miniapp-generator** - Scaffold new Farcaster miniapps
2. **manifest-builder** - Create and configure manifests
3. **embed-creator** - Build shareable embeds
4. **sdk-integration** - Integrate SDK for auth and actions
5. **notification-system** - Implement push notifications
6. **wallet-integration** - Add Ethereum/Solana wallets

### Commands (8)
- `/new-miniapp` - Create new miniapp project
- `/add-manifest` - Add manifest configuration
- `/add-embed` - Create embed for page
- `/setup-auth` - Setup authentication
- `/add-notifications` - Add notification system
- `/add-wallet` - Integrate wallet
- `/deploy-miniapp` - Deploy to production
- `/debug-miniapp` - Debug common issues

### Agents (4)
- **miniapp-architect** - Architecture and design consultant
- **authentication-specialist** - Auth implementation expert
- **wallet-consultant** - Web3 wallet integration expert
- **debugging-expert** - Troubleshooting specialist

### Hooks (4)
- Manifest validation
- SDK ready() check
- HTTPS URL enforcement
- Node version verification

## Critical Requirements

### 1. Node.js Version
**MINIMUM**: Node.js 22.11.0 or higher
- Earlier versions are NOT supported by @farcaster/miniapp-sdk
- Always verify version before installation

### 2. sdk.actions.ready()
**CRITICAL**: Must be called after full page load
- Failure to call ready() causes infinite loading screen
- This is the #1 most common issue
- Must wait for document.readyState === 'complete'

### 3. HTTPS Requirement
**PRODUCTION**: All URLs must use HTTPS
- Tunnel URLs (ngrok, cloudflared) only for development
- SDK actions will fail with tunnel URLs in production
- Manifest URLs must be production HTTPS domains

### 4. Context Security
**UNTRUSTED**: Context data can be spoofed
- Use for display purposes only
- Never use for authorization
- Always authenticate with quickAuth.getToken()

## Framework-Specific Patterns

### Next.js App Router (Recommended)

```typescript
// app/layout.tsx
import { MiniAppProvider } from '@/components/MiniAppProvider';

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <MiniAppProvider>
          {children}
        </MiniAppProvider>
      </body>
    </html>
  );
}

// app/page.tsx
'use client'; // Required for SDK usage

import { useMiniApp } from '@/components/MiniAppProvider';

export default function Home() {
  const { context, isReady } = useMiniApp();
  // ...
}
```

### React (Vite/CRA)

```typescript
// main.tsx
import { sdk } from './lib/sdk';

function App() {
  useEffect(() => {
    window.addEventListener('load', async () => {
      await sdk.actions.ready();
    });
  }, []);

  return <div>App</div>;
}
```

### Vue 3

```vue
<script setup>
import { onMounted } from 'vue';
import { sdk } from './lib/sdk';

onMounted(async () => {
  await new Promise(resolve => {
    if (document.readyState === 'complete') {
      resolve();
    } else {
      window.addEventListener('load', resolve);
    }
  });
  await sdk.actions.ready();
});
</script>
```

## Best Practices

### 1. Provider Pattern
Always wrap app in MiniAppProvider for centralized SDK management

### 2. Error Handling
Wrap all SDK calls in try-catch blocks

### 3. Capability Detection
Check capabilities before using optional features

### 4. TypeScript
Use strict mode with proper types from SDK

### 5. Rate Limiting
Implement rate limiting for notifications (10/hour recommended)

## Common Pitfalls

### ❌ Forgetting ready()
```typescript
// Wrong - infinite loading
useEffect(() => {
  // Not calling sdk.actions.ready()
}, []);
```

### ✅ Correct
```typescript
// Correct
useEffect(() => {
  async function init() {
    await new Promise(resolve => {
      if (document.readyState === 'complete') resolve();
      else window.addEventListener('load', resolve);
    });
    await sdk.actions.ready();
  }
  init();
}, []);
```

### ❌ Using Context for Auth
```typescript
// Wrong - can be spoofed
if (context.user?.fid === adminFid) {
  // Insecure!
}
```

### ✅ Correct
```typescript
// Correct - use Quick Auth
const token = await quickAuth.getToken();
// Verify on backend
```

### ❌ Tunnel URLs in Production
```typescript
// Wrong
homeUrl: 'https://abc-123.ngrok.io'
```

### ✅ Correct
```typescript
// Correct
homeUrl: 'https://myapp.com'
```

## Resources

- Official Docs: https://miniapps.farcaster.xyz
- GitHub: https://github.com/farcasterxyz/miniapps
- Warpcast Dev Tools: https://warpcast.com/~/settings/developer-tools

---

*Follow these guidelines for successful Farcaster miniapp development.*
