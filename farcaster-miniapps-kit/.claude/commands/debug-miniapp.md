# Debug Miniapp Issues

Diagnose and fix common Farcaster miniapp issues.

## Common Issues & Solutions

### 1. Infinite Loading Screen

**Symptom**: App never loads, stuck on splash

**Causes**:
- Not calling `sdk.actions.ready()`
- Calling ready() too early
- Error before ready() call

**Solutions**:
```typescript
// ✅ Correct
useEffect(() => {
  async function init() {
    try {
      await new Promise<void>(resolve => {
        if (document.readyState === 'complete') {
          resolve();
        } else {
          window.addEventListener('load', () => resolve());
        }
      });

      await sdk.actions.ready();
    } catch (error) {
      console.error('Init failed:', error);
      // Still call ready to avoid infinite loading
      await sdk.actions.ready();
    }
  }
  init();
}, []);
```

### 2. SDK Actions Fail

**Symptom**: `composeCast()`, `viewProfile()` etc. don't work

**Causes**:
- Using tunnel URL in production
- Not calling ready() first
- Network issues

**Solutions**:
- Use production HTTPS domain (not ngrok/cloudflared)
- Ensure ready() called before actions
- Check browser console for errors

### 3. Manifest Not Found (404)

**Symptom**: `/.well-known/farcaster.json` returns 404

**Causes**:
- Wrong file path
- Route not exported in build
- Server configuration issue

**Solutions**:
```bash
# Next.js App Router: create at
app/.well-known/farcaster.json/route.ts

# Verify in build output
npm run build
# Check .next/server/app for the route

# Test locally
curl http://localhost:3000/.well-known/farcaster.json
```

### 4. Context is Null/Undefined

**Symptom**: `sdk.context` returns null or properties missing

**Causes**:
- Accessing before SDK initialization
- Component rendered before provider ready

**Solutions**:
```typescript
// Use provider pattern
const { context, isReady } = useMiniApp();

if (!isReady || !context) {
  return <Loading />;
}

// Safe to use context
console.log(context.user?.fid);
```

### 5. Images Not Loading

**Symptom**: Icon, splash, or embed images don't display

**Causes**:
- Not using HTTPS
- CORS issues
- Wrong image path

**Solutions**:
- Use full HTTPS URLs
- Add CORS headers to image server
- Optimize image sizes (< 1MB)
- Test images directly in browser

### 6. Notifications Not Sending

**Symptom**: Notifications don't arrive

**Causes**:
- User hasn't enabled notifications
- Invalid credentials
- Rate limit exceeded
- Wrong webhook URL

**Debug**:
```typescript
// Check credentials exist
const creds = await getNotificationCredentials(fid);
console.log('Credentials:', creds);

// Test notification
const response = await fetch(creds.url, {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${creds.token}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    notificationId: `test-${Date.now()}`,
    title: 'Test',
    body: 'Testing notifications',
  }),
});

console.log('Response:', response.status, await response.text());
```

### 7. Wallet Provider Not Available

**Symptom**: `getEthereumProvider()` throws error

**Causes**:
- Capability not supported by client
- Not checking capabilities first

**Solutions**:
```typescript
const capabilities = sdk.getCapabilities();

if (capabilities.includes('ethereum_provider')) {
  const provider = sdk.wallet.getEthereumProvider();
  // Use provider
} else {
  // Show fallback UI
  return <div>Wallet not available</div>;
}
```

## Debugging Tools

### 1. Browser Console

Check for:
- SDK initialization errors
- Ready() call logs
- Network request failures

### 2. Warpcast Developer Tools

- Preview miniapp
- Audit manifest
- Test embeds
- View analytics

### 3. Network Tab

Monitor:
- Manifest fetch (/.well-known/farcaster.json)
- Webhook calls
- Image loading
- API requests

### 4. Add Debug Logging

```typescript
// lib/sdk.ts
export const sdk = createMiniAppSDK();

// Log context on init
console.log('SDK Context:', sdk.context);
console.log('Capabilities:', sdk.getCapabilities());

// Log ready call
sdk.actions.ready().then(() => {
  console.log('SDK ready() called successfully');
});
```

## Testing Checklist

- [ ] Manifest accessible at /.well-known/farcaster.json
- [ ] ready() called after full page load
- [ ] All images load (HTTPS URLs)
- [ ] Context accessible in components
- [ ] Actions work (composeCast, etc.)
- [ ] Wallet features work (if enabled)
- [ ] Notifications send (if enabled)
- [ ] Embeds display in Warpcast
- [ ] No console errors
- [ ] Tested in Warpcast preview

## Get Help

- Documentation: https://miniapps.farcaster.xyz
- GitHub Issues: https://github.com/farcasterxyz/miniapps/issues
- Warpcast: /farcaster-dev channel
