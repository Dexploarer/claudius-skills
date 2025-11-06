# Farcaster Miniapps Framework Rules

## Overview

Farcaster miniapps are web apps that integrate with the Farcaster social protocol, providing native-like experiences within Farcaster clients.

## Core Requirements

### 1. SDK Integration

**Package**: `@farcaster/miniapp-sdk`

**Minimum Node Version**: 22.11.0

```typescript
import { createMiniAppSDK } from '@farcaster/miniapp-sdk';

const sdk = createMiniAppSDK();
```

### 2. Manifest File

**Required Location**: `/.well-known/farcaster.json`

**Structure**:
```typescript
{
  "miniapp": {
    "version": "1",
    "name": "App Name",
    "iconUrl": "https://...",
    "homeUrl": "https://...",
    "webhookUrl": "https://..." // optional
  },
  "accountAssociation": {
    "header": "...",
    "payload": "...",
    "signature": "..."
  }
}
```

### 3. Initialization Pattern

**Critical**: Must call `sdk.actions.ready()` after page loads

```typescript
useEffect(() => {
  async function init() {
    await new Promise<void>(resolve => {
      if (document.readyState === 'complete') {
        resolve();
      } else {
        window.addEventListener('load', () => resolve());
      }
    });

    // CRITICAL: Hide splash screen
    await sdk.actions.ready();
  }

  init();
}, []);
```

## Security Guidelines

### Context Data is Untrusted

```typescript
// ❌ WRONG - Can be spoofed
if (sdk.context.user?.fid === ADMIN_FID) {
  // This is insecure!
}

// ✅ CORRECT - Use authenticated token
const token = await sdk.quickAuth.getToken();
// Verify token on backend
```

### HTTPS Requirements

- **Development**: Use tunnel (ngrok/cloudflared)
- **Production**: Must use proper HTTPS domain
- **SDK Actions**: Fail with tunnel URLs in production

### Manifest Signing

- Generate via Warpcast Developer Tools
- Never commit signatures to public repos
- Store in environment variables

## API Patterns

### Context Access

```typescript
const context = sdk.context;

// User info (may be null)
const user = context.user;
console.log(user?.fid, user?.username);

// Client info
console.log(context.client.name); // "Warpcast"

// Location
console.log(context.location.type); // "cast" | "composer" | ...
```

### Quick Authentication

```typescript
// Get JWT token (auto-cached, auto-refreshed)
const token = await sdk.quickAuth.getToken();

// Send to backend for verification
await fetch('/api/auth', {
  method: 'POST',
  body: JSON.stringify({ token }),
});
```

### Farcaster Actions

```typescript
// Compose cast
await sdk.actions.composeCast({
  text: 'Hello!',
  embeds: ['https://example.com'],
});

// View profile
await sdk.actions.viewProfile({ fid: 3 });

// View channel
await sdk.actions.viewChannel({ channelId: 'farcaster' });

// Open URL
await sdk.actions.openUrl({ url: 'https://example.com' });

// Close miniapp
await sdk.actions.close();
```

### Wallet Integration

```typescript
// Check capability
const capabilities = sdk.getCapabilities();
if (capabilities.includes('ethereum_provider')) {
  // Get EIP-1193 provider
  const provider = sdk.wallet.getEthereumProvider();

  // Use with ethers.js
  const ethersProvider = new BrowserProvider(provider);
}

// Solana
if (capabilities.includes('solana_provider')) {
  const provider = sdk.wallet.getSolanaProvider();
}
```

## Notification System

### Webhook Handler

```typescript
// Receive when user enables/disables notifications
export async function POST(req: Request) {
  const event = await req.json();

  switch (event.type) {
    case 'notification_enabled':
      // Store event.notificationDetails.token and url
      break;

    case 'notification_disabled':
    case 'app_removed':
      // Remove credentials
      break;
  }

  return new Response('OK');
}
```

### Sending Notifications

```typescript
await fetch(notificationDetails.url, {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${notificationDetails.token}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    notificationId: 'unique-id', // For idempotency
    title: 'Notification Title',
    body: 'Notification body text',
    targetUrl: 'https://app.com/page', // optional
  }),
});
```

### Idempotency

- Same `(fid, notificationId)` deduplicated for 24 hours
- Use same ID for retries
- Format: `${fid}-${timestamp}-${random}`

## Embed System

### Meta Tag Format

```html
<meta name="fc:miniapp" content='{"version":"1","imageUrl":"https://...","button":{"title":"Open","action":{"type":"launch","name":"App","url":"https://...","splashImageUrl":"https://...","splashBackgroundColor":"#fff"}}}' />
```

### Programmatic Creation

```typescript
const embed = {
  version: '1',
  imageUrl: 'https://app.com/og-image.png',
  button: {
    title: 'View Post',
    action: {
      type: 'launch',
      name: 'My App',
      url: 'https://app.com/posts/123',
      splashImageUrl: 'https://app.com/splash.png',
      splashBackgroundColor: '#6366f1',
    },
  },
};

<meta name="fc:miniapp" content={JSON.stringify(embed)} />
```

## TypeScript Types

```typescript
import type {
  MiniAppContext,
  MiniAppManifest,
  MiniAppEmbed,
  MiniAppCapability,
} from '@farcaster/miniapp-sdk';

// Context structure
interface MiniAppContext {
  user: {
    fid: number;
    username: string;
    displayName: string;
    pfpUrl?: string;
  } | null;
  client: {
    name: string;
    version: string;
  };
  location: {
    type: 'cast' | 'composer' | 'notification' | 'other';
    cast?: {
      hash: string;
      fid: number;
    };
  };
}
```

## Testing & Debugging

### Local Development

```bash
# Start dev server
npm run dev

# Create HTTPS tunnel
cloudflared tunnel --url localhost:3000

# Test in Warpcast preview tool
```

### Developer Tools

1. Enable at https://warpcast.com/~/settings/developer-tools
2. Use "Create Manifest" tool
3. Use "Preview Miniapp" tool
4. Use "Audit Manifest" tool

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Infinite loading | No ready() call | Call sdk.actions.ready() |
| SDK actions fail | Tunnel URL in prod | Use production domain |
| Context is null | Too early | Access after SDK init |
| Manifest 404 | Wrong path | Must be /.well-known/farcaster.json |

## Performance

### Bundle Size
- SDK is lightweight (~50KB)
- Tree-shake unused features
- Lazy load heavy dependencies

### Loading Speed
- Call ready() as soon as possible
- Preload critical assets
- Optimize splash screen image

## Deployment Checklist

- [ ] Node.js 22.11.0+ verified
- [ ] sdk.actions.ready() called
- [ ] Manifest at /.well-known/farcaster.json
- [ ] All URLs use HTTPS
- [ ] Manifest signed with account association
- [ ] Images optimized and publicly accessible
- [ ] Webhook endpoint responding
- [ ] Error handling implemented
- [ ] Tested in Warpcast preview
- [ ] Audit passed

## Version Compatibility

- **SDK**: Use latest @farcaster/miniapp-sdk
- **Spec Version**: Currently "1"
- **Node.js**: 22.11.0 minimum
- **Browsers**: Modern browsers with ES2020+ support

## Related Resources

- Specification: https://miniapps.farcaster.xyz/docs/specification
- SDK Reference: https://miniapps.farcaster.xyz/docs/sdk
- Examples: https://github.com/farcasterxyz/miniapps/tree/main/examples

---

*Follow these framework rules for compliant, secure Farcaster miniapps.*
