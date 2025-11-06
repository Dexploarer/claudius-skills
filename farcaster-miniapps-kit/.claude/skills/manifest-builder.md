---
name: manifest-builder
description: Build and configure Farcaster miniapp manifest files (/.well-known/farcaster.json)
version: 1.0.0
category: farcaster
tags: [farcaster, miniapps, manifest, configuration]
author: Claudius Skills
---

# Farcaster Miniapp Manifest Builder

## Purpose

This skill helps you create, configure, and validate the Farcaster miniapp manifest file that lives at `/.well-known/farcaster.json`. The manifest is your app's identity document and is required for your app to:
- Be added to users' app lists
- Send notifications
- Appear in app discovery
- Be recognized as an official Farcaster miniapp

## Activation Phrases

- "create farcaster manifest"
- "build miniapp manifest"
- "configure farcaster.json"
- "setup miniapp manifest"
- "generate manifest file"
- "create .well-known/farcaster.json"

## Understanding Manifest vs Embed

**Manifest** = App-level registration (one per domain)
- Location: `/.well-known/farcaster.json`
- Purpose: Identifies your entire miniapp
- Required for: App list, notifications, discovery

**Embed** = Page-level metadata (per shareable URL)
- Location: `fc:miniapp` meta tags in `<head>`
- Purpose: Makes individual pages shareable as rich cards
- Required for: Social sharing in feeds

**Best Practice**: Set up manifest first, then add embeds to shareable pages.

## Instructions

### Step 1: Create Manifest Configuration

Create `minikit.config.ts` in your project root:

```typescript
import type { MiniAppManifest } from '@farcaster/miniapp-sdk';

export const manifest: MiniAppManifest = {
  // REQUIRED FIELDS
  version: '1', // Always '1' for current spec
  name: 'Your Miniapp Name', // Display name (keep under 30 chars)
  iconUrl: 'https://yourdomain.com/icon.png', // App icon
  homeUrl: 'https://yourdomain.com', // Landing page URL

  // OPTIONAL BUT RECOMMENDED
  description: 'Brief description of your miniapp', // Under 100 chars
  splashImageUrl: 'https://yourdomain.com/splash.png', // Loading screen
  splashBackgroundColor: '#6366f1', // Hex color for splash

  // OPTIONAL - For notifications
  webhookUrl: 'https://yourdomain.com/api/webhook', // Notification webhook

  // OPTIONAL - Additional metadata
  imageUrl: 'https://yourdomain.com/og-image.png', // Social share image
};
```

### Step 2: Create Manifest API Route

**For Next.js App Router**:

Create `app/.well-known/farcaster.json/route.ts`:

```typescript
import { NextRequest, NextResponse } from 'next/server';
import { manifest } from '@/minikit.config';

export async function GET(req: NextRequest) {
  // Account association for domain ownership verification
  const accountAssociation = {
    header: process.env.FARCASTER_SIGNATURE_HEADER || '',
    payload: process.env.FARCASTER_SIGNATURE_PAYLOAD || '',
    signature: process.env.FARCASTER_SIGNATURE || '',
  };

  const manifestResponse = {
    miniapp: manifest,
    accountAssociation,
  };

  return NextResponse.json(manifestResponse, {
    status: 200,
    headers: {
      'Content-Type': 'application/json',
      'Cache-Control': 'public, max-age=3600, s-maxage=3600',
      'Access-Control-Allow-Origin': '*',
    },
  });
}

// Optional: Support OPTIONS for CORS
export async function OPTIONS() {
  return new NextResponse(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    },
  });
}
```

**For Next.js Pages Router**:

Create `pages/api/.well-known/farcaster.json.ts`:

```typescript
import type { NextApiRequest, NextApiResponse } from 'next';
import { manifest } from '@/minikit.config';

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const accountAssociation = {
    header: process.env.FARCASTER_SIGNATURE_HEADER || '',
    payload: process.env.FARCASTER_SIGNATURE_PAYLOAD || '',
    signature: process.env.FARCASTER_SIGNATURE || '',
  };

  const manifestResponse = {
    miniapp: manifest,
    accountAssociation,
  };

  res.setHeader('Content-Type', 'application/json');
  res.setHeader('Cache-Control', 'public, max-age=3600, s-maxage=3600');
  res.setHeader('Access-Control-Allow-Origin', '*');

  res.status(200).json(manifestResponse);
}
```

**For Express.js**:

```typescript
import express from 'express';
import { manifest } from './minikit.config';

const app = express();

app.get('/.well-known/farcaster.json', (req, res) => {
  const accountAssociation = {
    header: process.env.FARCASTER_SIGNATURE_HEADER || '',
    payload: process.env.FARCASTER_SIGNATURE_PAYLOAD || '',
    signature: process.env.FARCASTER_SIGNATURE || '',
  };

  const manifestResponse = {
    miniapp: manifest,
    accountAssociation,
  };

  res.setHeader('Content-Type', 'application/json');
  res.setHeader('Cache-Control', 'public, max-age=3600, s-maxage=3600');
  res.setHeader('Access-Control-Allow-Origin', '*');

  res.status(200).json(manifestResponse);
});
```

### Step 3: Generate Account Association Signature

The account association proves you own the domain and Farcaster account.

**Method 1: Using Warpcast Developer Tools (Recommended)**

1. Enable developer mode:
   - Visit https://warpcast.com/~/settings/developer-tools
   - Enable "Developer Mode"

2. Create manifest:
   - Click "Create Manifest"
   - Enter your domain (e.g., `myapp.com`)
   - Enter your app details
   - Generate signature

3. Copy the generated values:
   - `FARCASTER_SIGNATURE_HEADER`
   - `FARCASTER_SIGNATURE_PAYLOAD`
   - `FARCASTER_SIGNATURE`

**Method 2: Using API (Advanced)**

```typescript
// This requires your Farcaster private key - use with caution!
import { createAccountAssociation } from '@farcaster/miniapp-node';

const association = await createAccountAssociation({
  fid: YOUR_FID, // Your Farcaster ID
  domain: 'yourdomain.com',
  privateKey: process.env.FARCASTER_PRIVATE_KEY,
});

console.log('Header:', association.header);
console.log('Payload:', association.payload);
console.log('Signature:', association.signature);
```

### Step 4: Configure Environment Variables

Add to `.env.local`:

```env
# Farcaster Manifest Signature
FARCASTER_SIGNATURE_HEADER=eyJmaWQiOjEyMzQ1LCJ0eXBlIjoiY3VzdG9keSIsImtleSI6IjB4...
FARCASTER_SIGNATURE_PAYLOAD=eyJkb21haW4iOiJteWFwcC5jb20ifQ==
FARCASTER_SIGNATURE=MHg5ODc2NTQzMjEwOTg3NjU0MzIxMDk4NzY1NDMyMTA5ODc2NTQzMjEw...

# App URL
NEXT_PUBLIC_APP_URL=https://yourdomain.com
```

**Security Best Practices**:
- Never commit `.env.local` to git
- Add `.env.local` to `.gitignore`
- Store secrets in your hosting platform's environment variables
- Rotate signatures if compromised

### Step 5: Image Assets

Create optimized image assets:

**Icon Image** (`iconUrl`):
- Format: PNG or WebP
- Size: 512x512px recommended
- Max file size: 500KB
- Purpose: App list, discovery, profile

**Splash Image** (`splashImageUrl`):
- Format: PNG or WebP
- Size: Match common mobile screen sizes (1170x2532px for iPhone 14 Pro)
- Max file size: 1MB
- Purpose: Loading screen while app initializes
- Design: Should look good with `splashBackgroundColor`

**OG Image** (`imageUrl`):
- Format: PNG or JPEG
- Size: 1200x630px (OpenGraph standard)
- Max file size: 1MB
- Purpose: Social sharing, embeds

**Example asset setup**:

```
public/
├── icon.png              # 512x512px app icon
├── splash.png            # 1170x2532px splash screen
└── og-image.png          # 1200x630px social share
```

### Step 6: Validate Manifest

**Test Locally**:

```bash
# Start your development server
npm run dev

# Test manifest endpoint (should return JSON)
curl http://localhost:3000/.well-known/farcaster.json
```

**Test with Tunnel**:

```bash
# Start tunnel
cloudflared tunnel --url localhost:3000

# Copy the HTTPS URL (e.g., https://abc-123.trycloudflare.com)
# Test manifest
curl https://abc-123.trycloudflare.com/.well-known/farcaster.json
```

**Validate Structure**:

```typescript
// Create validation script: scripts/validate-manifest.ts
import { manifest } from '../minikit.config';

function validateManifest() {
  const errors: string[] = [];

  // Required fields
  if (!manifest.version || manifest.version !== '1') {
    errors.push('version must be "1"');
  }
  if (!manifest.name || manifest.name.length > 30) {
    errors.push('name is required and should be under 30 characters');
  }
  if (!manifest.iconUrl || !manifest.iconUrl.startsWith('https://')) {
    errors.push('iconUrl must be a valid HTTPS URL');
  }
  if (!manifest.homeUrl || !manifest.homeUrl.startsWith('https://')) {
    errors.push('homeUrl must be a valid HTTPS URL');
  }

  // Recommended fields
  if (!manifest.description) {
    console.warn('⚠️  description is recommended');
  }
  if (!manifest.splashImageUrl) {
    console.warn('⚠️  splashImageUrl is recommended');
  }
  if (!manifest.splashBackgroundColor) {
    console.warn('⚠️  splashBackgroundColor is recommended');
  }

  // Notifications
  if (!manifest.webhookUrl) {
    console.warn('⚠️  webhookUrl required for notifications');
  }

  if (errors.length > 0) {
    console.error('❌ Manifest validation failed:');
    errors.forEach(err => console.error(`   - ${err}`));
    process.exit(1);
  } else {
    console.log('✅ Manifest validation passed');
  }
}

validateManifest();
```

Run validation:

```bash
npx tsx scripts/validate-manifest.ts
```

### Step 7: Test in Warpcast

Once deployed to production:

1. **Audit Your Manifest**:
   - Visit https://warpcast.com/~/settings/developer-tools
   - Click "Audit Manifest"
   - Enter your domain
   - Review any errors or warnings

2. **Preview Your Miniapp**:
   - Click "Preview Miniapp"
   - Enter your app URL
   - Test functionality
   - Verify splash screen and loading

3. **Monitor Analytics**:
   - View miniapp analytics in developer tools
   - Track installations, opens, and retention

## Complete Example

**minikit.config.ts**:

```typescript
import type { MiniAppManifest } from '@farcaster/miniapp-sdk';

export const manifest: MiniAppManifest = {
  version: '1',
  name: 'EchoBoard',
  description: 'Real-time collaborative bulletin board for Farcaster communities',
  iconUrl: 'https://echoboard.app/icon.png',
  splashImageUrl: 'https://echoboard.app/splash.png',
  splashBackgroundColor: '#6366f1',
  homeUrl: 'https://echoboard.app',
  imageUrl: 'https://echoboard.app/og-image.png',
  webhookUrl: 'https://api.echoboard.app/webhook',
};
```

## Advanced Configuration

### Multiple Environments

```typescript
// minikit.config.ts
const isDevelopment = process.env.NODE_ENV === 'development';
const baseUrl = process.env.NEXT_PUBLIC_APP_URL || 'http://localhost:3000';

export const manifest: MiniAppManifest = {
  version: '1',
  name: isDevelopment ? '[DEV] My Miniapp' : 'My Miniapp',
  description: 'My awesome miniapp',
  iconUrl: `${baseUrl}/icon.png`,
  splashImageUrl: `${baseUrl}/splash.png`,
  splashBackgroundColor: '#6366f1',
  homeUrl: baseUrl,
  webhookUrl: isDevelopment
    ? `${baseUrl}/api/webhook`
    : 'https://api.myapp.com/webhook',
};
```

### TypeScript Type Safety

```typescript
// lib/manifest-types.ts
export interface MiniAppManifest {
  version: '1';
  name: string;
  iconUrl: string;
  homeUrl: string;
  description?: string;
  splashImageUrl?: string;
  splashBackgroundColor?: string;
  webhookUrl?: string;
  imageUrl?: string;
}

// Ensure all URLs are HTTPS
export type HttpsUrl = `https://${string}`;

export interface ValidatedManifest extends MiniAppManifest {
  iconUrl: HttpsUrl;
  homeUrl: HttpsUrl;
  splashImageUrl?: HttpsUrl;
  webhookUrl?: HttpsUrl;
  imageUrl?: HttpsUrl;
}
```

### Dynamic Manifest (Advanced)

For apps that need different manifests per subdomain or path:

```typescript
// app/.well-known/farcaster.json/route.ts
import { NextRequest, NextResponse } from 'next/server';

export async function GET(req: NextRequest) {
  const host = req.headers.get('host') || '';

  // Different manifests per subdomain
  const manifests: Record<string, any> = {
    'app1.example.com': {
      version: '1',
      name: 'App 1',
      iconUrl: 'https://app1.example.com/icon.png',
      homeUrl: 'https://app1.example.com',
    },
    'app2.example.com': {
      version: '1',
      name: 'App 2',
      iconUrl: 'https://app2.example.com/icon.png',
      homeUrl: 'https://app2.example.com',
    },
  };

  const manifest = manifests[host] || manifests['app1.example.com'];

  const accountAssociation = {
    header: process.env[`SIGNATURE_HEADER_${host.toUpperCase().replace(/\./g, '_')}`],
    payload: process.env[`SIGNATURE_PAYLOAD_${host.toUpperCase().replace(/\./g, '_')}`],
    signature: process.env[`SIGNATURE_${host.toUpperCase().replace(/\./g, '_')}`],
  };

  return NextResponse.json({
    miniapp: manifest,
    accountAssociation,
  });
}
```

## Troubleshooting

### Manifest Not Found (404)

**Problem**: `/.well-known/farcaster.json` returns 404

**Solutions**:
1. Check route file path is correct
2. Verify framework routing configuration
3. For Next.js App Router, ensure file is at `app/.well-known/farcaster.json/route.ts`
4. For Pages Router, check `pages/api/.well-known/farcaster.json.ts`
5. Check build output includes the route

### Invalid Signature

**Problem**: Account association signature fails validation

**Solutions**:
1. Regenerate signature using Warpcast developer tools
2. Ensure environment variables are set correctly
3. Verify no extra whitespace in .env values
4. Check signature matches the domain exactly
5. Ensure FID in signature matches your account

### Images Not Loading

**Problem**: Icon or splash images don't display

**Solutions**:
1. Verify URLs are HTTPS (not HTTP)
2. Check images are publicly accessible
3. Verify correct CORS headers
4. Optimize image sizes (< 500KB for icons)
5. Use CDN for better performance

### Manifest Cache Issues

**Problem**: Changes not reflected immediately

**Solutions**:
1. Check cache headers (max-age)
2. Clear browser cache
3. Use cache busting: `icon.png?v=2`
4. Wait for CDN/cache to expire
5. Test in incognito mode

## Checklist

- [ ] `minikit.config.ts` created with all required fields
- [ ] Manifest route created at `/.well-known/farcaster.json`
- [ ] Account association signature generated
- [ ] Environment variables configured
- [ ] Icon image created (512x512px)
- [ ] Splash image created (recommended)
- [ ] All URLs use HTTPS
- [ ] Manifest accessible via curl/browser
- [ ] Validated using Warpcast developer tools
- [ ] No CORS errors
- [ ] Proper cache headers set

## Resources

- Manifest Specification: https://miniapps.farcaster.xyz/docs/specification
- Manifest vs Embed Guide: https://miniapps.farcaster.xyz/docs/guides/manifest-vs-embed
- Warpcast Developer Tools: https://warpcast.com/~/settings/developer-tools
- Publishing Guide: https://miniapps.farcaster.xyz/docs/guides/publishing

## Next Steps

After setting up your manifest:

1. **Create Embeds**: Use the `embed-creator` skill
2. **Test Locally**: Use developer tools preview
3. **Deploy**: Push to production domain
4. **Audit**: Use Warpcast audit tool
5. **Share**: Create embed links for social sharing

---

*This skill ensures your miniapp has a valid, well-configured manifest for proper discovery and functionality.*
