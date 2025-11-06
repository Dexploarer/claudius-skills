# Farcaster Miniapp Debugging Expert

## Expertise

- Troubleshooting SDK issues
- Resolving loading and initialization problems
- Debugging manifest and embed errors
- Fixing wallet and transaction failures
- Resolving notification delivery issues
- Performance optimization

## When to Use

- App stuck on infinite loading
- SDK errors or failures
- Manifest not found or invalid
- Embeds not displaying
- Wallet connection issues
- Notifications not sending
- Performance problems

## Common Issues & Solutions

### 1. Infinite Loading Screen ⚠️ MOST COMMON

**Symptom**: App never loads, stuck on splash screen

**Root Causes**:
1. Not calling `sdk.actions.ready()`
2. Calling ready() before page fully loads
3. Error thrown before ready() call
4. Ready() called in wrong lifecycle

**Debug Steps**:

```typescript
// Add extensive logging
useEffect(() => {
  async function init() {
    console.log('1. Init starting');

    try {
      console.log('2. Waiting for page load');
      console.log('   readyState:', document.readyState);

      await new Promise<void>((resolve) => {
        if (document.readyState === 'complete') {
          console.log('3. Page already loaded');
          resolve();
        } else {
          console.log('3. Waiting for load event');
          window.addEventListener('load', () => {
            console.log('4. Load event fired');
            resolve();
          });
        }
      });

      console.log('5. Calling ready()');
      await sdk.actions.ready();
      console.log('6. Ready() succeeded');

    } catch (error) {
      console.error('7. Error during init:', error);
      // CRITICAL: Still call ready to prevent infinite loading
      try {
        await sdk.actions.ready();
        console.log('8. Ready() called after error');
      } catch (readyErr) {
        console.error('9. Ready() also failed:', readyErr);
      }
    }
  }

  init();
}, []);
```

**Solutions**:

```typescript
// ✅ CORRECT Pattern
useEffect(() => {
  async function init() {
    try {
      // Wait for full page load
      await new Promise<void>((resolve) => {
        if (document.readyState === 'complete') {
          resolve();
        } else {
          window.addEventListener('load', () => resolve());
        }
      });

      // Call ready
      await sdk.actions.ready();

    } catch (error) {
      console.error('Init failed:', error);
      // Still call ready
      await sdk.actions.ready();
    }
  }

  init();
}, []);
```

### 2. SDK Actions Fail

**Symptom**: `composeCast()`, `viewProfile()` etc. don't work

**Debug Steps**:

```typescript
// Test SDK connectivity
console.log('SDK:', sdk);
console.log('Capabilities:', sdk.getCapabilities());
console.log('Context:', sdk.context);

// Test action with error handling
try {
  console.log('Attempting to compose cast...');
  await sdk.actions.composeCast({
    text: 'Test',
  });
  console.log('Success!');
} catch (error) {
  console.error('Action failed:', error);
  console.error('Error code:', error.code);
  console.error('Error message:', error.message);
}
```

**Common Causes**:
1. Using tunnel URL in production
2. Not called ready() first
3. Invalid parameters
4. Network issues

**Solutions**:

```typescript
// ✅ Check ready first
if (!isReady) {
  throw new Error('SDK not ready yet');
}

// ✅ Use production domain
// In manifest and embeds
homeUrl: 'https://myapp.com' // not ngrok URL

// ✅ Validate parameters
if (!text || text.length === 0) {
  throw new Error('Cast text required');
}
```

### 3. Manifest Not Found (404)

**Symptom**: `/.well-known/farcaster.json` returns 404

**Debug Steps**:

```bash
# Test locally
curl http://localhost:3000/.well-known/farcaster.json

# Check build output
npm run build
ls -la .next/server/app/.well-known/

# Test route file exists
ls -la app/.well-known/farcaster.json/route.ts
```

**Common Causes**:
1. Wrong file path
2. Route not in build output
3. Server configuration blocks .well-known
4. Missing route.ts file

**Solutions**:

```typescript
// ✅ Correct path for Next.js App Router
// app/.well-known/farcaster.json/route.ts

export async function GET(req: Request) {
  console.log('Manifest route hit'); // Debug log

  const manifest = {
    miniapp: { /* ... */ },
    accountAssociation: { /* ... */ },
  };

  return new Response(JSON.stringify(manifest), {
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
    },
  });
}
```

### 4. Context is Null/Undefined

**Symptom**: `sdk.context` or `sdk.context.user` is null

**Debug Steps**:

```typescript
// Log context access timing
console.log('Context at component mount:', sdk.context);

useEffect(() => {
  console.log('Context in useEffect:', sdk.context);
}, []);

setTimeout(() => {
  console.log('Context after 1s:', sdk.context);
}, 1000);
```

**Common Causes**:
1. Accessing before SDK initialized
2. Context actually is null (user not logged in)
3. Component rendered before provider ready

**Solutions**:

```typescript
// ✅ Use provider pattern
const { context, isReady } = useMiniApp();

if (!isReady) {
  return <Loading />;
}

// ✅ Safe access with optional chaining
const username = context?.user?.username ?? 'Anonymous';

// ✅ Type guard
if (!context || !context.user) {
  return <div>No user context</div>;
}
```

### 5. Wallet Provider Not Available

**Symptom**: `getEthereumProvider()` throws error

**Debug Steps**:

```typescript
// Check capabilities
const capabilities = sdk.getCapabilities();
console.log('All capabilities:', capabilities);
console.log('Has Ethereum:', capabilities.includes('ethereum_provider'));
console.log('Has Solana:', capabilities.includes('solana_provider'));

// Try to get provider
try {
  const provider = sdk.wallet.getEthereumProvider();
  console.log('Provider:', provider);
} catch (error) {
  console.error('Provider error:', error);
}
```

**Solutions**:

```typescript
// ✅ Always check capability first
const capabilities = sdk.getCapabilities();

if (capabilities.includes('ethereum_provider')) {
  const provider = sdk.wallet.getEthereumProvider();
  // Use provider
} else {
  return (
    <div className="p-4 bg-yellow-50 rounded">
      <p>Wallet not available in this client</p>
    </div>
  );
}
```

### 6. Notifications Not Sending

**Symptom**: Notifications don't arrive to users

**Debug Steps**:

```typescript
// Check webhook received event
export async function POST(req: Request) {
  const body = await req.json();
  console.log('Webhook received:', JSON.stringify(body, null, 2));

  // Check notification credentials stored
  const stored = await db.notificationCredential.findUnique({
    where: { fid: body.fid },
  });
  console.log('Stored credentials:', stored);

  return new Response('OK');
}

// Test notification sending
const credentials = await getNotificationCredentials(fid);
console.log('Credentials:', credentials);

const response = await fetch(credentials.url, {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${credentials.token}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    notificationId: `test-${Date.now()}`,
    title: 'Test',
    body: 'Testing',
  }),
});

console.log('Notification response:', response.status);
console.log('Response body:', await response.text());
```

**Common Causes**:
1. User hasn't enabled notifications
2. Invalid credentials (token/URL)
3. Webhook not receiving events
4. Notification format invalid

**Solutions**:

```typescript
// ✅ Check credentials exist
const credentials = await getNotificationCredentials(fid);
if (!credentials) {
  throw new Error('User has not enabled notifications');
}

// ✅ Validate before sending
if (!credentials.url || !credentials.token) {
  throw new Error('Invalid credentials');
}

// ✅ Use proper format
const notification = {
  notificationId: `${fid}-${Date.now()}`,
  title: 'Title',
  body: 'Body text',
  targetUrl: 'https://myapp.com/page', // optional
};
```

### 7. Images Not Loading

**Symptom**: Icon, splash, or embed images don't display

**Debug Steps**:

```bash
# Test image URLs directly
curl -I https://myapp.com/icon.png
curl -I https://myapp.com/splash.png

# Check CORS headers
curl -I -H "Origin: https://warpcast.com" https://myapp.com/icon.png

# Validate image sizes
file public/icon.png
# Should show dimensions
```

**Common Causes**:
1. Not using HTTPS
2. CORS blocked
3. Image path wrong
4. Image too large

**Solutions**:

```typescript
// ✅ Use full HTTPS URLs
iconUrl: 'https://myapp.com/icon.png'
// Not: '/icon.png' or 'http://...'

// ✅ Add CORS headers (Next.js)
export async function GET(req: Request) {
  return new Response(file, {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Content-Type': 'image/png',
    },
  });
}

// ✅ Optimize images
// Icon: 512x512px, < 500KB
// Splash: 1170x2532px, < 1MB
// OG Image: 1200x630px, < 1MB
```

## Debugging Workflow

### 1. Enable Verbose Logging

```typescript
// lib/sdk.ts
export const sdk = createMiniAppSDK({
  debug: true, // if available
});

// Add custom logging
const originalReady = sdk.actions.ready;
sdk.actions.ready = async function(...args) {
  console.log('ready() called with:', args);
  const result = await originalReady.apply(this, args);
  console.log('ready() result:', result);
  return result;
};
```

### 2. Use Browser DevTools

```typescript
// Add to window for console access
if (typeof window !== 'undefined') {
  (window as any).debugSDK = {
    sdk,
    context: sdk.context,
    capabilities: sdk.getCapabilities(),
    testAction: async () => {
      await sdk.actions.composeCast({ text: 'Test' });
    },
  };
}

// Then in browser console:
// window.debugSDK.context
// await window.debugSDK.testAction()
```

### 3. Network Monitoring

```typescript
// Log all fetch requests
const originalFetch = window.fetch;
window.fetch = async function(...args) {
  console.log('Fetch:', args[0]);
  const response = await originalFetch.apply(this, args);
  console.log('Response:', response.status, response.statusText);
  return response;
};
```

### 4. Error Boundaries

```typescript
'use client';

import { Component, ReactNode } from 'react';

export class ErrorBoundary extends Component<
  { children: ReactNode },
  { hasError: boolean; error: Error | null }
> {
  constructor(props: any) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error: Error) {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: any) {
    console.error('Error boundary caught:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="p-8 bg-red-50 rounded">
          <h2 className="text-xl font-bold text-red-900 mb-4">
            Something went wrong
          </h2>
          <pre className="text-sm text-red-800 overflow-auto">
            {this.state.error?.message}
          </pre>
          <button
            onClick={() => this.setState({ hasError: false, error: null })}
            className="mt-4 px-4 py-2 bg-red-600 text-white rounded"
          >
            Try Again
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}
```

## Performance Debugging

### Bundle Analysis

```bash
# Next.js
npm install @next/bundle-analyzer

# next.config.js
const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: process.env.ANALYZE === 'true',
});

module.exports = withBundleAnalyzer({});

# Analyze
ANALYZE=true npm run build
```

### Loading Performance

```typescript
// Measure component render time
console.time('Component render');
// ... component code
console.timeEnd('Component render');

// Measure SDK initialization
console.time('SDK init');
await sdk.actions.ready();
console.timeEnd('SDK init');
```

---

*I help diagnose and fix all Farcaster miniapp issues with systematic debugging approaches.*
