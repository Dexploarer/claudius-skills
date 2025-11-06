# Add Manifest Configuration

Add or update the Farcaster miniapp manifest file at `/.well-known/farcaster.json`.

## Steps

1. Enable Warpcast Developer Mode:
   - Visit https://warpcast.com/~/settings/developer-tools
   - Enable "Developer Mode"

2. Generate account association:
   - Click "Create Manifest"
   - Enter your production domain
   - Copy the generated signature values

3. Add environment variables to `.env.local`:
```env
FARCASTER_SIGNATURE_HEADER=<header>
FARCASTER_SIGNATURE_PAYLOAD=<payload>
FARCASTER_SIGNATURE=<signature>
NEXT_PUBLIC_APP_URL=https://your-domain.com
```

4. Create `minikit.config.ts`:
```typescript
export const manifest = {
  version: '1',
  name: 'Your App Name',
  iconUrl: 'https://your-domain.com/icon.png',
  splashImageUrl: 'https://your-domain.com/splash.png',
  splashBackgroundColor: '#6366f1',
  homeUrl: 'https://your-domain.com',
  description: 'Brief app description',
  webhookUrl: 'https://your-domain.com/api/webhook',
};
```

5. Create manifest route (Next.js App Router):
```bash
mkdir -p app/.well-known/farcaster.json
```

6. Test manifest endpoint:
```bash
curl http://localhost:3000/.well-known/farcaster.json
```

7. Validate with Warpcast Audit tool

## Required Images

- Icon: 512x512px PNG
- Splash: 1170x2532px PNG
- Use HTTPS URLs only
