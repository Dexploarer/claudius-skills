---
name: miniapp-generator
description: Generate new Farcaster miniapp projects with proper structure, SDK integration, and configuration
version: 1.0.0
category: farcaster
tags: [farcaster, miniapps, generator, web3, social]
author: Claudius Skills
---

# Farcaster Miniapp Generator

## Purpose

This skill helps you scaffold new Farcaster miniapp projects with the correct structure, SDK integration, manifest configuration, and all necessary files to get started quickly. It supports multiple frameworks (Next.js, React, Vue, etc.) and includes best practices for authentication, wallet integration, and notifications.

## Activation Phrases

- "create a farcaster miniapp"
- "generate a new farcaster miniapp"
- "scaffold farcaster miniapp"
- "build a new miniapp for farcaster"
- "create miniapp project"
- "new farcaster app"
- "initialize farcaster miniapp"

## Prerequisites

Before creating a Farcaster miniapp, verify:

1. **Node.js Version**: Node.js 22.11.0 or higher is required
   ```bash
   node --version
   ```

2. **Package Manager**: npm, pnpm, or yarn installed

3. **HTTPS Requirement**: Production miniapps require HTTPS (use tunneling tools like ngrok or cloudflared for local development)

## Instructions

### Step 1: Project Setup

**Option A: Using Official CLI (Recommended)**

Use the official `@farcaster/create-mini-app` CLI:

```bash
# Using npm
npm create @farcaster/mini-app

# Using pnpm
pnpm create @farcaster/mini-app

# Using yarn
yarn create @farcaster/mini-app
```

The CLI will prompt you to:
- Choose a project name
- Select a framework (Next.js, React, etc.)
- Configure manifest setup (can be done later)

**Option B: Manual Setup**

For manual setup or custom frameworks:

1. Create project directory:
```bash
mkdir my-miniapp
cd my-miniapp
npm init -y
```

2. Install the SDK:
```bash
npm install @farcaster/miniapp-sdk
# or
pnpm add @farcaster/miniapp-sdk
```

### Step 2: Project Structure

Create the following directory structure:

```
my-miniapp/
├── app/
│   ├── page.tsx                          # Main entry point
│   ├── .well-known/
│   │   └── farcaster.json/
│   │       └── route.ts                  # Manifest endpoint
│   └── layout.tsx
├── components/
│   ├── MiniappProvider.tsx              # SDK context provider
│   ├── Home/
│   │   ├── App.tsx                      # Main app screen
│   │   ├── User.tsx                     # User context display
│   │   ├── FarcasterActions.tsx         # Farcaster native actions
│   │   └── WalletActions.tsx            # Wallet/onchain actions
├── lib/
│   ├── sdk.ts                           # SDK initialization
│   └── utils.ts
├── public/
│   └── images/
│       ├── splash.png                   # Splash screen image
│       └── feed-image.png               # Feed/embed image
├── minikit.config.ts                    # Manifest configuration
├── package.json
├── tsconfig.json
└── next.config.js
```

### Step 3: SDK Integration

Create SDK initialization file (`lib/sdk.ts`):

```typescript
import { createMiniAppSDK } from '@farcaster/miniapp-sdk';

// Initialize SDK
export const sdk = createMiniAppSDK();

// Export commonly used methods
export const { context, actions, wallet, quickAuth } = sdk;
```

Create MiniApp Provider component (`components/MiniappProvider.tsx`):

```typescript
'use client';

import { useEffect, useState } from 'react';
import { sdk } from '@/lib/sdk';

export function MiniappProvider({ children }: { children: React.ReactNode }) {
  const [isReady, setIsReady] = useState(false);

  useEffect(() => {
    async function initializeApp() {
      try {
        // Wait for app to be fully loaded
        await new Promise(resolve => {
          if (document.readyState === 'complete') {
            resolve(true);
          } else {
            window.addEventListener('load', resolve);
          }
        });

        // CRITICAL: Call ready() to hide splash screen
        await sdk.actions.ready();
        setIsReady(true);
      } catch (error) {
        console.error('Failed to initialize miniapp:', error);
      }
    }

    initializeApp();
  }, []);

  if (!isReady) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-center">
          <p>Loading miniapp...</p>
        </div>
      </div>
    );
  }

  return <>{children}</>;
}
```

### Step 4: Main App Component

Create the main app screen (`app/page.tsx`):

```typescript
'use client';

import { useEffect, useState } from 'react';
import { sdk } from '@/lib/sdk';
import { MiniappProvider } from '@/components/MiniappProvider';

export default function Home() {
  const [context, setContext] = useState<any>(null);

  useEffect(() => {
    // Access context information
    const ctx = sdk.context;
    setContext(ctx);

    console.log('User:', ctx.user);
    console.log('Client:', ctx.client);
    console.log('Location:', ctx.location);
  }, []);

  return (
    <MiniappProvider>
      <main className="min-h-screen p-4">
        <h1 className="text-2xl font-bold mb-4">
          Welcome to My Miniapp
        </h1>

        {context?.user && (
          <div className="mb-4">
            <p>Hello, @{context.user.username}!</p>
            <p>FID: {context.user.fid}</p>
          </div>
        )}

        {/* Add your app content here */}
      </main>
    </MiniappProvider>
  );
}
```

### Step 5: Manifest Configuration

Create manifest configuration (`minikit.config.ts`):

```typescript
import type { MiniAppManifest } from '@farcaster/miniapp-sdk';

export const manifest: MiniAppManifest = {
  version: '1',
  name: 'My Miniapp',
  iconUrl: 'https://your-domain.com/icon.png',
  splashImageUrl: 'https://your-domain.com/splash.png',
  splashBackgroundColor: '#ffffff',
  homeUrl: 'https://your-domain.com',
  description: 'A brief description of your miniapp',
  webhookUrl: 'https://your-domain.com/api/webhook',
};
```

Create manifest route (`app/.well-known/farcaster.json/route.ts`):

```typescript
import { NextRequest, NextResponse } from 'next/server';
import { manifest } from '@/minikit.config';

export async function GET(req: NextRequest) {
  const accountAssociation = {
    header: process.env.FARCASTER_SIGNATURE_HEADER,
    payload: process.env.FARCASTER_SIGNATURE_PAYLOAD,
    signature: process.env.FARCASTER_SIGNATURE,
  };

  const manifestWithAuth = {
    miniapp: manifest,
    accountAssociation,
  };

  return NextResponse.json(manifestWithAuth, {
    headers: {
      'Content-Type': 'application/json',
      'Cache-Control': 'public, max-age=3600',
    },
  });
}
```

### Step 6: Environment Variables

Create `.env.local`:

```env
# Manifest Signing (generate via Warpcast developer tools)
FARCASTER_SIGNATURE_HEADER=
FARCASTER_SIGNATURE_PAYLOAD=
FARCASTER_SIGNATURE=

# App Configuration
NEXT_PUBLIC_APP_URL=https://your-domain.com
```

### Step 7: TypeScript Configuration

Update `tsconfig.json` for strict typing:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "jsx": "preserve",
    "paths": {
      "@/*": ["./*"]
    }
  }
}
```

### Step 8: Package.json Scripts

Add useful development scripts:

```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "tunnel": "cloudflared tunnel --url localhost:3000",
    "type-check": "tsc --noEmit"
  }
}
```

### Step 9: Development Setup

1. **Start Development Server**:
```bash
npm run dev
```

2. **Create HTTPS Tunnel** (for local testing):
```bash
# Install cloudflared
# macOS
brew install cloudflare/cloudflare/cloudflared

# Then start tunnel
npm run tunnel
# or
cloudflared tunnel --url localhost:3000
```

3. **Enable Developer Mode**:
   - Visit https://warpcast.com/~/settings/developer-tools
   - Enable developer mode
   - Access manifest creator and preview tools

## Best Practices

### 1. Always Call ready()

**CRITICAL**: The most common issue is forgetting to call `sdk.actions.ready()` after your app loads:

```typescript
// ✅ Correct
useEffect(() => {
  async function init() {
    // Wait for full page load
    await new Promise(resolve => {
      if (document.readyState === 'complete') {
        resolve(true);
      } else {
        window.addEventListener('load', resolve);
      }
    });

    await sdk.actions.ready(); // Hide splash screen
  }
  init();
}, []);

// ❌ Wrong - will cause infinite loading
// Not calling ready() at all
```

### 2. Context Data Security

Context data is NOT authenticated by default:

```typescript
// ✅ Correct - treat as untrusted for display only
const displayName = sdk.context.user?.displayName || 'Guest';

// ❌ Wrong - don't use for authorization
if (sdk.context.user?.fid === adminFid) {
  // This can be spoofed!
}

// ✅ Correct - use Quick Auth for real authentication
const token = await sdk.quickAuth.getToken();
// Verify this token on your backend
```

### 3. HTTPS Requirements

```typescript
// Production domains only
// ✅ Correct
homeUrl: 'https://myapp.com'

// ❌ Wrong - tunnel URLs fail in production
homeUrl: 'https://xyz.ngrok.io'

// Tunnel URLs are ONLY for local development
```

### 4. Error Handling

```typescript
try {
  await sdk.actions.ready();
} catch (error) {
  console.error('SDK initialization failed:', error);
  // Implement fallback UI
}

// Check capabilities before using features
const capabilities = sdk.getCapabilities();
if (capabilities.includes('ethereum_provider')) {
  const provider = sdk.wallet.getEthereumProvider();
}
```

### 5. Manifest Best Practices

```typescript
export const manifest: MiniAppManifest = {
  version: '1',
  name: 'Clear, Concise Name',  // Max ~30 chars
  iconUrl: 'https://cdn.example.com/icon-512.png', // 512x512px recommended
  splashImageUrl: 'https://cdn.example.com/splash.png', // Full screen
  splashBackgroundColor: '#6366f1', // Match brand
  homeUrl: 'https://app.example.com', // Production domain
  description: 'Compelling one-liner under 100 chars',
  webhookUrl: 'https://api.example.com/webhook', // For notifications
};
```

## Framework-Specific Guidance

### Next.js App Router (Recommended)

- Use Server Components where possible
- Client Components for SDK interaction (add 'use client')
- API Routes for webhooks and backend logic

### React (Create React App / Vite)

```typescript
// App.tsx
import { useEffect } from 'react';
import { sdk } from './lib/sdk';

function App() {
  useEffect(() => {
    window.addEventListener('load', async () => {
      await sdk.actions.ready();
    });
  }, []);

  return <div>My Miniapp</div>;
}
```

### Vue 3

```vue
<script setup lang="ts">
import { onMounted } from 'vue';
import { sdk } from './lib/sdk';

onMounted(async () => {
  await new Promise(resolve => {
    if (document.readyState === 'complete') {
      resolve(true);
    } else {
      window.addEventListener('load', resolve);
    }
  });
  await sdk.actions.ready();
});
</script>
```

## Checklist

After generating a miniapp, verify:

- [ ] Node.js version 22.11.0 or higher
- [ ] `@farcaster/miniapp-sdk` installed
- [ ] SDK initialization in lib/sdk.ts
- [ ] MiniappProvider component created
- [ ] `sdk.actions.ready()` called after full page load
- [ ] Manifest configuration in minikit.config.ts
- [ ] Manifest route at /.well-known/farcaster.json
- [ ] Environment variables configured
- [ ] Development tunnel setup (cloudflared or ngrok)
- [ ] Developer mode enabled in Warpcast
- [ ] TypeScript strict mode configured
- [ ] Error handling implemented

## Common Issues

1. **Infinite Loading Screen**: Forgot to call `sdk.actions.ready()`
2. **SDK Actions Fail**: Using tunnel URL in production (use proper domain)
3. **Context Data Missing**: Called before SDK initialized
4. **Manifest Not Found**: Wrong path or not deployed to /.well-known/farcaster.json
5. **Node Version Error**: Using Node.js < 22.11.0

## Resources

- Official Docs: https://miniapps.farcaster.xyz
- GitHub Repo: https://github.com/farcasterxyz/miniapps
- Warpcast Developer Tools: https://warpcast.com/~/settings/developer-tools
- Specification: https://miniapps.farcaster.xyz/docs/specification

## Next Steps

After generating the project:

1. **Add Authentication**: Use the `farcaster-auth` skill
2. **Configure Embeds**: Use the `embed-creator` skill
3. **Add Wallet Integration**: Use the `wallet-integration` skill
4. **Setup Notifications**: Use the `notification-system` skill
5. **Deploy**: Use the `/deploy-miniapp` command

---

*This skill generates production-ready Farcaster miniapps with best practices, proper SDK integration, and comprehensive error handling.*
