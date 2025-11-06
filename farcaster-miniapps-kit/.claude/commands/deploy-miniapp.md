# Deploy Miniapp to Production

Deploy your Farcaster miniapp to production with proper configuration.

## Pre-deployment Checklist

- [ ] Node.js 22.11.0+ verified
- [ ] `sdk.actions.ready()` called after page load
- [ ] Manifest at `/.well-known/farcaster.json`
- [ ] All URLs use HTTPS (no tunnel URLs)
- [ ] Environment variables set
- [ ] Images optimized and accessible
- [ ] Tested in Warpcast preview tool
- [ ] Error handling implemented

## Deployment Steps

### 1. Choose Hosting Platform

**Recommended**:
- Vercel (Next.js optimized)
- Railway
- Netlify
- Cloudflare Pages

### 2. Configure Environment Variables

Set in hosting platform:
```env
FARCASTER_SIGNATURE_HEADER=...
FARCASTER_SIGNATURE_PAYLOAD=...
FARCASTER_SIGNATURE=...
NEXT_PUBLIC_APP_URL=https://your-domain.com
```

### 3. Update Manifest URLs

In `minikit.config.ts`:
```typescript
export const manifest = {
  iconUrl: 'https://your-domain.com/icon.png',
  homeUrl: 'https://your-domain.com',
  webhookUrl: 'https://your-domain.com/api/webhook',
  // ... other fields
};
```

### 4. Build and Deploy

```bash
# Build
npm run build

# Deploy (platform-specific)
vercel deploy --prod
# or
railway up
# or
netlify deploy --prod
```

### 5. Verify Deployment

Test these URLs:
```bash
# Manifest
curl https://your-domain.com/.well-known/farcaster.json

# Main app
curl https://your-domain.com

# Webhook (should return 405 for GET)
curl https://your-domain.com/api/webhook
```

### 6. Audit with Warpcast

1. Visit https://warpcast.com/~/settings/developer-tools
2. Click "Audit Manifest"
3. Enter your domain
4. Fix any errors reported

### 7. Test in Production

1. Share app URL in Warpcast
2. Test all features
3. Verify embeds display correctly
4. Test notifications (if enabled)
5. Test wallet features (if enabled)

## Post-Deployment

- Monitor error logs
- Track analytics
- Set up uptime monitoring
- Configure CDN for images
- Enable CORS if needed

## Troubleshooting

- **Manifest 404**: Check build output includes route
- **SDK errors**: Verify no tunnel URLs in config
- **Images not loading**: Check CORS and HTTPS
- **Ready() timeout**: Ensure called after full load
