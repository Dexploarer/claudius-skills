---
name: sdk-integration
description: Integrate @farcaster/miniapp-sdk for authentication, context, actions, and Farcaster features
version: 1.0.0
category: farcaster
tags: [farcaster, miniapps, sdk, authentication, context]
author: Claudius Skills
---

# Farcaster Miniapp SDK Integration

## Purpose

This skill helps you integrate the `@farcaster/miniapp-sdk` to access native Farcaster features including:
- User context and session information
- Quick authentication with Sign-in with Farcaster
- Farcaster actions (compose cast, view profile, etc.)
- Capability detection
- App-to-app navigation

## Activation Phrases

- "integrate farcaster sdk"
- "setup miniapp sdk"
- "add farcaster sdk"
- "implement farcaster authentication"
- "use miniapp sdk"
- "setup farcaster context"

## Prerequisites

1. **Node.js 22.11.0+**: Verify version
   ```bash
   node --version
   ```

2. **Miniapp SDK Package**:
   ```bash
   npm install @farcaster/miniapp-sdk
   # or
   pnpm add @farcaster/miniapp-sdk
   ```

## Instructions

### Step 1: SDK Initialization

Create SDK singleton (`lib/sdk.ts`):

```typescript
import { createMiniAppSDK } from '@farcaster/miniapp-sdk';

// Create SDK instance
export const sdk = createMiniAppSDK();

// Export commonly used APIs
export const { context, actions, wallet, quickAuth } = sdk;

// Export types
export type { MiniAppContext, MiniAppCapability } from '@farcaster/miniapp-sdk';
```

### Step 2: Provider Component

Create a provider to manage SDK lifecycle (`components/MiniAppProvider.tsx`):

```typescript
'use client';

import { createContext, useContext, useEffect, useState, ReactNode } from 'react';
import { sdk, type MiniAppContext } from '@/lib/sdk';

interface MiniAppContextValue {
  context: MiniAppContext | null;
  isReady: boolean;
  capabilities: string[];
  error: Error | null;
}

const MiniAppContext = createContext<MiniAppContextValue>({
  context: null,
  isReady: false,
  capabilities: [],
  error: null,
});

export function useMiniApp() {
  const ctx = useContext(MiniAppContext);
  if (!ctx) {
    throw new Error('useMiniApp must be used within MiniAppProvider');
  }
  return ctx;
}

interface MiniAppProviderProps {
  children: ReactNode;
  fallback?: ReactNode;
}

export function MiniAppProvider({ children, fallback }: MiniAppProviderProps) {
  const [isReady, setIsReady] = useState(false);
  const [context, setContext] = useState<MiniAppContext | null>(null);
  const [capabilities, setCapabilities] = useState<string[]>([]);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    async function initializeMiniApp() {
      try {
        // Wait for page to be fully loaded
        await new Promise<void>((resolve) => {
          if (document.readyState === 'complete') {
            resolve();
          } else {
            window.addEventListener('load', () => resolve());
          }
        });

        // Get context before calling ready
        const ctx = sdk.context;
        setContext(ctx);

        // Get capabilities
        const caps = sdk.getCapabilities();
        setCapabilities(caps);

        // CRITICAL: Call ready() to hide splash screen
        await sdk.actions.ready();

        setIsReady(true);
      } catch (err) {
        console.error('Failed to initialize miniapp:', err);
        setError(err instanceof Error ? err : new Error('Unknown error'));
        // Still call ready to avoid infinite loading
        try {
          await sdk.actions.ready();
        } catch (readyErr) {
          console.error('Failed to call ready():', readyErr);
        }
      }
    }

    initializeMiniApp();
  }, []);

  if (error && !isReady) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-red-50">
        <div className="text-center p-8">
          <h1 className="text-2xl font-bold text-red-600 mb-4">
            Initialization Error
          </h1>
          <p className="text-red-800">{error.message}</p>
        </div>
      </div>
    );
  }

  if (!isReady) {
    return fallback || (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600 mx-auto mb-4" />
          <p className="text-gray-600">Loading miniapp...</p>
        </div>
      </div>
    );
  }

  return (
    <MiniAppContext.Provider value={{ context, isReady, capabilities, error }}>
      {children}
    </MiniAppContext.Provider>
  );
}
```

### Step 3: Access User Context

Context provides information about the user and environment:

```typescript
'use client';

import { useMiniApp } from '@/components/MiniAppProvider';

export function UserInfo() {
  const { context } = useMiniApp();

  if (!context) {
    return <div>Loading user info...</div>;
  }

  return (
    <div className="p-4 bg-white rounded-lg shadow">
      <h2 className="text-xl font-bold mb-4">User Context</h2>

      {/* User Information */}
      {context.user && (
        <div className="mb-4">
          <h3 className="font-semibold mb-2">User</h3>
          <p>FID: {context.user.fid}</p>
          <p>Username: @{context.user.username}</p>
          <p>Display Name: {context.user.displayName}</p>
          {context.user.pfpUrl && (
            <img
              src={context.user.pfpUrl}
              alt={context.user.displayName}
              className="w-16 h-16 rounded-full mt-2"
            />
          )}
        </div>
      )}

      {/* Client Information */}
      <div className="mb-4">
        <h3 className="font-semibold mb-2">Client</h3>
        <p>Name: {context.client.name}</p>
        <p>Version: {context.client.version}</p>
      </div>

      {/* Location Information */}
      <div>
        <h3 className="font-semibold mb-2">Location</h3>
        <p>Type: {context.location.type}</p>
        {context.location.cast && (
          <p>Cast Hash: {context.location.cast.hash}</p>
        )}
      </div>
    </div>
  );
}
```

**Context Structure**:

```typescript
interface MiniAppContext {
  // User who opened the miniapp (can be null/untrusted)
  user: {
    fid: number;
    username: string;
    displayName: string;
    pfpUrl?: string;
  } | null;

  // Client information
  client: {
    name: string;      // e.g., "Warpcast"
    version: string;   // e.g., "1.2.3"
  };

  // Where the miniapp was opened from
  location: {
    type: 'cast' | 'composer' | 'notification' | 'other';
    cast?: {
      hash: string;
      fid: number;
    };
  };
}
```

**IMPORTANT**: Context data is NOT authenticated and can be spoofed. Use for display purposes only, not for authorization.

### Step 4: Quick Authentication

Use Quick Auth for secure user authentication:

```typescript
'use client';

import { useState } from 'react';
import { quickAuth } from '@/lib/sdk';

export function AuthButton() {
  const [token, setToken] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleAuth() {
    try {
      setLoading(true);
      setError(null);

      // Get authentication token
      const authToken = await quickAuth.getToken();
      setToken(authToken);

      // Send token to your backend for verification
      const response = await fetch('/api/auth/verify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ token: authToken }),
      });

      if (!response.ok) {
        throw new Error('Authentication failed');
      }

      const data = await response.json();
      console.log('Authenticated user:', data);

    } catch (err) {
      console.error('Auth error:', err);
      setError(err instanceof Error ? err.message : 'Authentication failed');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-4">
      <button
        onClick={handleAuth}
        disabled={loading}
        className="px-4 py-2 bg-indigo-600 text-white rounded-lg disabled:opacity-50"
      >
        {loading ? 'Authenticating...' : 'Sign in with Farcaster'}
      </button>

      {error && (
        <p className="text-red-600">{error}</p>
      )}

      {token && (
        <div className="p-4 bg-green-50 rounded">
          <p className="text-green-800 font-semibold">✓ Authenticated</p>
          <p className="text-xs text-green-600 mt-2 break-all">
            Token: {token.slice(0, 50)}...
          </p>
        </div>
      )}
    </div>
  );
}
```

**Backend Verification** (`app/api/auth/verify/route.ts`):

```typescript
import { NextRequest, NextResponse } from 'next/server';
import { verifySignInMessage } from '@farcaster/auth-kit';

export async function POST(req: NextRequest) {
  try {
    const { token } = await req.json();

    // Verify the JWT token
    const verification = await verifySignInMessage(token);

    if (!verification.success) {
      return NextResponse.json(
        { error: 'Invalid token' },
        { status: 401 }
      );
    }

    // Token is valid - create session
    const user = {
      fid: verification.fid,
      username: verification.username,
      displayName: verification.displayName,
      pfpUrl: verification.pfpUrl,
    };

    // Store in session/database
    // ... your session logic here

    return NextResponse.json({ user });

  } catch (error) {
    console.error('Verification error:', error);
    return NextResponse.json(
      { error: 'Verification failed' },
      { status: 500 }
    );
  }
}
```

**Token Management**:

```typescript
// Quick Auth automatically manages token lifecycle
// It stores the token in memory and returns cached token if not expired

// ✅ Correct - call whenever you need a token
const token = await quickAuth.getToken();

// ❌ Wrong - don't manually manage token expiration
// Quick Auth handles this for you
```

### Step 5: Farcaster Actions

Trigger native Farcaster actions:

```typescript
'use client';

import { actions } from '@/lib/sdk';

export function FarcasterActions() {
  async function composeCast(text: string, embeds?: string[]) {
    try {
      await actions.composeCast({
        text,
        embeds,
      });
    } catch (error) {
      console.error('Failed to compose cast:', error);
    }
  }

  async function viewProfile(fid: number) {
    try {
      await actions.viewProfile({ fid });
    } catch (error) {
      console.error('Failed to view profile:', error);
    }
  }

  async function viewChannel(channelId: string) {
    try {
      await actions.viewChannel({ channelId });
    } catch (error) {
      console.error('Failed to view channel:', error);
    }
  }

  async function viewCast(hash: string) {
    try {
      await actions.viewCast({ hash });
    } catch (error) {
      console.error('Failed to view cast:', error);
    }
  }

  async function openUrl(url: string) {
    try {
      await actions.openUrl({ url });
    } catch (error) {
      console.error('Failed to open URL:', error);
    }
  }

  return (
    <div className="space-y-4 p-4">
      <h2 className="text-xl font-bold">Farcaster Actions</h2>

      <div className="grid grid-cols-2 gap-4">
        <button
          onClick={() => composeCast('Hello from my miniapp! 👋')}
          className="px-4 py-2 bg-purple-600 text-white rounded-lg"
        >
          Compose Cast
        </button>

        <button
          onClick={() => viewProfile(3)}
          className="px-4 py-2 bg-blue-600 text-white rounded-lg"
        >
          View Profile
        </button>

        <button
          onClick={() => viewChannel('farcaster')}
          className="px-4 py-2 bg-green-600 text-white rounded-lg"
        >
          View Channel
        </button>

        <button
          onClick={() => openUrl('https://farcaster.xyz')}
          className="px-4 py-2 bg-indigo-600 text-white rounded-lg"
        >
          Open URL
        </button>
      </div>
    </div>
  );
}
```

**Available Actions**:

```typescript
// Compose a new cast
await actions.composeCast({
  text: 'Check out this miniapp!',
  embeds: ['https://myapp.com/cool-feature'],
});

// View a user profile
await actions.viewProfile({ fid: 3 });

// View a channel
await actions.viewChannel({ channelId: 'farcaster' });

// View a specific cast
await actions.viewCast({ hash: '0x...' });

// Open external URL
await actions.openUrl({ url: 'https://example.com' });

// Close miniapp
await actions.close();
```

### Step 6: Capability Detection

Check what features are available:

```typescript
'use client';

import { useState, useEffect } from 'react';
import { sdk } from '@/lib/sdk';
import { useMiniApp } from '@/components/MiniAppProvider';

export function CapabilitiesDisplay() {
  const { capabilities } = useMiniApp();

  return (
    <div className="p-4 bg-gray-50 rounded-lg">
      <h3 className="font-semibold mb-2">Available Capabilities</h3>
      <ul className="space-y-1">
        {capabilities.map(cap => (
          <li key={cap} className="text-sm">
            ✓ {cap}
          </li>
        ))}
      </ul>
    </div>
  );
}

// Use capabilities to conditionally enable features
export function ConditionalFeatures() {
  const { capabilities } = useMiniApp();

  const hasEthProvider = capabilities.includes('ethereum_provider');
  const hasSolProvider = capabilities.includes('solana_provider');

  return (
    <div className="space-y-4">
      {hasEthProvider && (
        <button className="px-4 py-2 bg-blue-600 text-white rounded">
          Connect Ethereum Wallet
        </button>
      )}

      {hasSolProvider && (
        <button className="px-4 py-2 bg-purple-600 text-white rounded">
          Connect Solana Wallet
        </button>
      )}

      {!hasEthProvider && !hasSolProvider && (
        <p className="text-gray-600">
          Wallet features not available in this client
        </p>
      )}
    </div>
  );
}
```

### Step 7: Complete Integration Example

**Main App Layout** (`app/layout.tsx`):

```typescript
import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import { MiniAppProvider } from '@/components/MiniAppProvider';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'My Farcaster Miniapp',
  description: 'A cool miniapp for Farcaster',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <MiniAppProvider
          fallback={
            <div className="min-h-screen flex items-center justify-center">
              <div className="animate-pulse text-lg">Loading...</div>
            </div>
          }
        >
          {children}
        </MiniAppProvider>
      </body>
    </html>
  );
}
```

**Main Page** (`app/page.tsx`):

```typescript
'use client';

import { useMiniApp } from '@/components/MiniAppProvider';
import { UserInfo } from '@/components/UserInfo';
import { AuthButton } from '@/components/AuthButton';
import { FarcasterActions } from '@/components/FarcasterActions';

export default function Home() {
  const { context, isReady } = useMiniApp();

  return (
    <main className="min-h-screen p-8 bg-gray-100">
      <div className="max-w-4xl mx-auto space-y-8">
        <header className="text-center">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            My Farcaster Miniapp
          </h1>
          <p className="text-gray-600">
            {isReady ? '✓ Ready' : 'Initializing...'}
          </p>
        </header>

        {context?.user && (
          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-2xl font-bold mb-4">
              Welcome, @{context.user.username}!
            </h2>
            <p className="text-gray-600">FID: {context.user.fid}</p>
          </div>
        )}

        <UserInfo />
        <AuthButton />
        <FarcasterActions />
      </div>
    </main>
  );
}
```

## Best Practices

### 1. Always Call ready()

**CRITICAL**: This is the #1 cause of issues.

```typescript
// ✅ Correct
useEffect(() => {
  async function init() {
    // Wait for full load
    await new Promise<void>(resolve => {
      if (document.readyState === 'complete') resolve();
      else window.addEventListener('load', () => resolve());
    });

    await sdk.actions.ready(); // Hide splash screen
  }
  init();
}, []);

// ❌ Wrong - infinite loading screen
// Forgetting to call ready()
```

### 2. Context Security

```typescript
// ✅ Correct - display only
const greeting = `Hello, @${context.user?.username || 'friend'}!`;

// ❌ Wrong - using for authorization
if (context.user?.fid === ADMIN_FID) {
  // This can be spoofed! Don't rely on this
}

// ✅ Correct - use authenticated token
const token = await quickAuth.getToken();
// Verify token on backend
```

### 3. Error Handling

```typescript
// Wrap all SDK calls in try-catch
try {
  await actions.composeCast({ text: 'Hello!' });
} catch (error) {
  console.error('Action failed:', error);
  // Show user-friendly error message
}
```

### 4. Capability Checks

```typescript
// Check before using optional features
const capabilities = sdk.getCapabilities();

if (capabilities.includes('ethereum_provider')) {
  const provider = sdk.wallet.getEthereumProvider();
  // Use Ethereum features
}
```

### 5. Token Management

```typescript
// ✅ Correct - use Quick Auth
const token = await quickAuth.getToken();

// ❌ Wrong - manual token management
// Quick Auth handles caching and expiration
```

## Troubleshooting

### Infinite Loading Screen

**Problem**: App never loads, stuck on splash

**Solution**: Call `sdk.actions.ready()` after page loads

### Context is Null

**Problem**: `sdk.context` returns null

**Solution**: SDK may not be initialized yet. Use provider pattern.

### Actions Don't Work

**Problem**: SDK actions fail silently

**Solutions**:
1. Check you called `ready()` first
2. Verify not using tunnel URL in production
3. Check capability support
4. Add error handling

### TypeScript Errors

**Problem**: Type errors with SDK

**Solutions**:
```typescript
// Import types explicitly
import type { MiniAppContext } from '@farcaster/miniapp-sdk';

// Handle nullable types
const username = context?.user?.username ?? 'Anonymous';
```

## Checklist

- [ ] SDK installed (`@farcaster/miniapp-sdk`)
- [ ] SDK initialized in `lib/sdk.ts`
- [ ] MiniAppProvider component created
- [ ] `sdk.actions.ready()` called after page load
- [ ] Context accessed safely (nullable checks)
- [ ] Quick Auth implemented for authentication
- [ ] Backend verification for auth tokens
- [ ] Capability detection implemented
- [ ] Error handling added
- [ ] TypeScript types configured

## Resources

- SDK Documentation: https://miniapps.farcaster.xyz/docs/sdk
- Context API: https://miniapps.farcaster.xyz/docs/sdk/context
- Quick Auth: https://miniapps.farcaster.xyz/docs/guides/auth
- Capabilities: https://miniapps.farcaster.xyz/docs/sdk/detecting-capabilities

---

*This skill provides complete SDK integration with authentication, context access, and Farcaster actions.*
