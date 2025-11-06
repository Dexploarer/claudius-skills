---
name: embed-creator
description: Create fc:miniapp embeds for shareable Farcaster miniapp pages
version: 1.0.0
category: farcaster
tags: [farcaster, miniapps, embeds, sharing, social]
author: Claudius Skills
---

# Farcaster Miniapp Embed Creator

## Purpose

This skill helps you create fc:miniapp embeds that make individual pages in your miniapp shareable as rich cards in Farcaster feeds. Embeds use OpenGraph-inspired metadata to display beautiful previews when users share your app's pages.

## Activation Phrases

- "create farcaster embed"
- "add miniapp embed"
- "create fc:miniapp meta tag"
- "make page shareable"
- "setup miniapp embed"
- "create shareable miniapp card"

## Understanding Embeds

**Manifest vs Embed**:
- **Manifest** (`.well-known/farcaster.json`): App-level identity
- **Embed** (`fc:miniapp` meta tag): Page-level social sharing

**Embed Use Cases**:
- Share specific content/posts
- Deep link to app sections
- Promote events or features
- Drive engagement from social feeds

**Without embeds**: Pages shared as plain text links
**With embeds**: Pages shown as rich, interactive cards with images and CTA buttons

## Instructions

### Step 1: Understand Embed Structure

An embed is a JSON object in a meta tag:

```html
<meta name="fc:miniapp" content='{"version":"1","imageUrl":"https://...","button":{"title":"Open","action":{"type":"launch","name":"App","url":"https://...","splashImageUrl":"https://...","splashBackgroundColor":"#ffffff"}}}' />
```

**Embed Components**:

```typescript
interface MiniAppEmbed {
  version: '1';                  // Always '1' for current spec
  imageUrl: string;             // Preview image URL (1200x630px)
  button: {
    title: string;              // Button text (e.g., "View Post", "Play Game")
    action: {
      type: 'launch';           // Always 'launch'
      name: string;             // Internal name
      url: string;              // Deep link URL
      splashImageUrl: string;   // Splash screen image
      splashBackgroundColor: string; // Hex color
    };
  };
}
```

### Step 2: Create Embed Helper Functions

Create `lib/embed-utils.ts`:

```typescript
export interface MiniAppEmbedConfig {
  version: '1';
  imageUrl: string;
  buttonTitle: string;
  appName: string;
  url: string;
  splashImageUrl: string;
  splashBackgroundColor: string;
}

export function createMiniAppEmbed(config: MiniAppEmbedConfig): string {
  const embed = {
    version: config.version,
    imageUrl: config.imageUrl,
    button: {
      title: config.buttonTitle,
      action: {
        type: 'launch' as const,
        name: config.appName,
        url: config.url,
        splashImageUrl: config.splashImageUrl,
        splashBackgroundColor: config.splashBackgroundColor,
      },
    },
  };

  return JSON.stringify(embed);
}

export function validateEmbedUrl(url: string): boolean {
  try {
    const urlObj = new URL(url);
    return urlObj.protocol === 'https:';
  } catch {
    return false;
  }
}

export function validateHexColor(color: string): boolean {
  return /^#[0-9A-Fa-f]{6}$/.test(color);
}
```

### Step 3: Create Embed Component (React/Next.js)

Create `components/MiniAppEmbed.tsx`:

```typescript
import { createMiniAppEmbed, MiniAppEmbedConfig } from '@/lib/embed-utils';

interface MiniAppEmbedProps {
  imageUrl: string;
  buttonTitle: string;
  url: string;
  appName?: string;
  splashImageUrl?: string;
  splashBackgroundColor?: string;
}

export function MiniAppEmbed({
  imageUrl,
  buttonTitle,
  url,
  appName = 'My Miniapp',
  splashImageUrl = '/splash.png',
  splashBackgroundColor = '#6366f1',
}: MiniAppEmbedProps) {
  const embedContent = createMiniAppEmbed({
    version: '1',
    imageUrl,
    buttonTitle,
    appName,
    url,
    splashImageUrl: splashImageUrl.startsWith('http')
      ? splashImageUrl
      : `${process.env.NEXT_PUBLIC_APP_URL}${splashImageUrl}`,
    splashBackgroundColor,
  });

  return (
    <meta name="fc:miniapp" content={embedContent} />
  );
}
```

### Step 4: Add Embeds to Pages

**Next.js App Router** with Metadata:

```typescript
// app/posts/[id]/page.tsx
import { Metadata } from 'next';
import { createMiniAppEmbed } from '@/lib/embed-utils';

interface PageProps {
  params: { id: string };
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  // Fetch post data
  const post = await getPost(params.id);

  // Create embed
  const embedContent = createMiniAppEmbed({
    version: '1',
    imageUrl: post.imageUrl || 'https://myapp.com/default-og.png',
    buttonTitle: 'View Post',
    appName: 'My Blog',
    url: `https://myapp.com/posts/${params.id}`,
    splashImageUrl: 'https://myapp.com/splash.png',
    splashBackgroundColor: '#6366f1',
  });

  return {
    title: post.title,
    description: post.excerpt,
    openGraph: {
      title: post.title,
      description: post.excerpt,
      images: [post.imageUrl],
    },
    other: {
      'fc:miniapp': embedContent,
    },
  };
}

export default async function PostPage({ params }: PageProps) {
  const post = await getPost(params.id);
  return <article>{/* Post content */}</article>;
}
```

**Next.js Pages Router**:

```typescript
// pages/posts/[id].tsx
import Head from 'next/head';
import { GetServerSideProps } from 'next';
import { createMiniAppEmbed } from '@/lib/embed-utils';

interface PostPageProps {
  post: Post;
  embedContent: string;
}

export default function PostPage({ post, embedContent }: PostPageProps) {
  return (
    <>
      <Head>
        <title>{post.title}</title>
        <meta name="description" content={post.excerpt} />

        {/* OpenGraph */}
        <meta property="og:title" content={post.title} />
        <meta property="og:description" content={post.excerpt} />
        <meta property="og:image" content={post.imageUrl} />

        {/* Farcaster Miniapp Embed */}
        <meta name="fc:miniapp" content={embedContent} />
      </Head>

      <article>{/* Post content */}</article>
    </>
  );
}

export const getServerSideProps: GetServerSideProps = async ({ params }) => {
  const post = await getPost(params?.id as string);

  const embedContent = createMiniAppEmbed({
    version: '1',
    imageUrl: post.imageUrl,
    buttonTitle: 'View Post',
    appName: 'My Blog',
    url: `https://myapp.com/posts/${params?.id}`,
    splashImageUrl: 'https://myapp.com/splash.png',
    splashBackgroundColor: '#6366f1',
  });

  return {
    props: { post, embedContent },
  };
};
```

**React (Static)**:

```typescript
// src/pages/PostPage.tsx
import { Helmet } from 'react-helmet';
import { createMiniAppEmbed } from '../lib/embed-utils';

export function PostPage({ post }: { post: Post }) {
  const embedContent = createMiniAppEmbed({
    version: '1',
    imageUrl: post.imageUrl,
    buttonTitle: 'View Post',
    appName: 'My Blog',
    url: `https://myapp.com/posts/${post.id}`,
    splashImageUrl: 'https://myapp.com/splash.png',
    splashBackgroundColor: '#6366f1',
  });

  return (
    <>
      <Helmet>
        <title>{post.title}</title>
        <meta name="fc:miniapp" content={embedContent} />
      </Helmet>

      <article>{/* Post content */}</article>
    </>
  );
}
```

### Step 5: Dynamic Embed Configuration

For apps with many pages, create a configuration system:

```typescript
// lib/embed-config.ts
export interface PageEmbedConfig {
  path: string;
  getImageUrl: (params: any) => string;
  getButtonTitle: (params: any) => string;
  getUrl: (params: any) => string;
}

export const embedConfigs: Record<string, PageEmbedConfig> = {
  post: {
    path: '/posts/:id',
    getImageUrl: (post) => post.imageUrl || 'https://myapp.com/default.png',
    getButtonTitle: () => 'Read Post',
    getUrl: (post) => `https://myapp.com/posts/${post.id}`,
  },
  profile: {
    path: '/profile/:username',
    getImageUrl: (user) => user.avatarUrl,
    getButtonTitle: (user) => `View @${user.username}`,
    getUrl: (user) => `https://myapp.com/profile/${user.username}`,
  },
  event: {
    path: '/events/:id',
    getImageUrl: (event) => event.bannerUrl,
    getButtonTitle: () => 'Join Event',
    getUrl: (event) => `https://myapp.com/events/${event.id}`,
  },
};

export function generateEmbed(type: string, data: any): string {
  const config = embedConfigs[type];
  if (!config) {
    throw new Error(`Unknown embed type: ${type}`);
  }

  return createMiniAppEmbed({
    version: '1',
    imageUrl: config.getImageUrl(data),
    buttonTitle: config.getButtonTitle(data),
    appName: 'My App',
    url: config.getUrl(data),
    splashImageUrl: 'https://myapp.com/splash.png',
    splashBackgroundColor: '#6366f1',
  });
}
```

### Step 6: Embed Image Best Practices

**Image Specifications**:

```typescript
// lib/embed-images.ts
export const EMBED_IMAGE_SPECS = {
  width: 1200,
  height: 630,
  maxSizeBytes: 1024 * 1024, // 1MB
  formats: ['image/png', 'image/jpeg', 'image/webp'],
};

// Generate OG image URL with dynamic text
export function generateOGImageUrl(params: {
  title: string;
  description?: string;
  backgroundImage?: string;
}): string {
  const searchParams = new URLSearchParams({
    title: params.title,
    ...(params.description && { description: params.description }),
    ...(params.backgroundImage && { bg: params.backgroundImage }),
  });

  return `https://myapp.com/api/og?${searchParams.toString()}`;
}
```

**Dynamic OG Image API Route** (Next.js):

```typescript
// app/api/og/route.tsx
import { ImageResponse } from 'next/og';

export const runtime = 'edge';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const title = searchParams.get('title') || 'Default Title';
  const description = searchParams.get('description');

  return new ImageResponse(
    (
      <div
        style={{
          height: '100%',
          width: '100%',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          backgroundColor: '#6366f1',
          padding: '40px',
        }}
      >
        <h1 style={{ fontSize: '72px', color: 'white', textAlign: 'center' }}>
          {title}
        </h1>
        {description && (
          <p style={{ fontSize: '32px', color: '#e0e7ff', textAlign: 'center' }}>
            {description}
          </p>
        )}
      </div>
    ),
    {
      width: 1200,
      height: 630,
    }
  );
}
```

### Step 7: Test Embeds

**Local Testing**:

```bash
# Start dev server
npm run dev

# Start tunnel
cloudflared tunnel --url localhost:3000

# Copy HTTPS URL
# Share the URL in Warpcast to preview embed
```

**Use Warpcast Embed Tool**:

1. Enable developer mode in Warpcast
2. Navigate to developer tools
3. Click "Embed Tool"
4. Enter your page URL
5. Preview how the embed looks

**Manual Testing**:

```typescript
// scripts/test-embed.ts
import { createMiniAppEmbed } from '../lib/embed-utils';

const testEmbed = createMiniAppEmbed({
  version: '1',
  imageUrl: 'https://myapp.com/test.png',
  buttonTitle: 'Test Button',
  appName: 'Test App',
  url: 'https://myapp.com/test',
  splashImageUrl: 'https://myapp.com/splash.png',
  splashBackgroundColor: '#6366f1',
});

console.log('Embed JSON:');
console.log(testEmbed);

// Validate JSON structure
try {
  const parsed = JSON.parse(testEmbed);
  console.log('\n✅ Valid JSON');
  console.log('Version:', parsed.version);
  console.log('Image URL:', parsed.imageUrl);
  console.log('Button Title:', parsed.button.title);
  console.log('Target URL:', parsed.button.action.url);
} catch (error) {
  console.error('\n❌ Invalid JSON:', error);
}
```

### Step 8: Advanced Embed Patterns

**Conditional Embeds**:

```typescript
// Only show embed when shared on Farcaster
import { headers } from 'next/headers';

export async function generateMetadata({ params }: PageProps) {
  const headersList = headers();
  const userAgent = headersList.get('user-agent') || '';

  // Check if request is from Farcaster
  const isFarcaster = userAgent.includes('farcaster') ||
                      userAgent.includes('warpcast');

  if (!isFarcaster) {
    return { title: 'My Page' };
  }

  // Return embed metadata
  const embedContent = createMiniAppEmbed({...});

  return {
    title: 'My Page',
    other: {
      'fc:miniapp': embedContent,
    },
  };
}
```

**Multi-Action Embeds** (Future):

```typescript
// Prepare for future multi-button support
interface MultiActionEmbed {
  version: '1';
  imageUrl: string;
  buttons: Array<{
    title: string;
    action: LaunchAction;
  }>;
}

// Currently, only single button is supported
```

**Deep Linking with Query Parameters**:

```typescript
export function createDeepLinkEmbed(params: {
  baseUrl: string;
  path: string;
  queryParams?: Record<string, string>;
  imageUrl: string;
  buttonTitle: string;
}) {
  const url = new URL(params.path, params.baseUrl);

  if (params.queryParams) {
    Object.entries(params.queryParams).forEach(([key, value]) => {
      url.searchParams.append(key, value);
    });
  }

  return createMiniAppEmbed({
    version: '1',
    imageUrl: params.imageUrl,
    buttonTitle: params.buttonTitle,
    appName: 'My App',
    url: url.toString(),
    splashImageUrl: `${params.baseUrl}/splash.png`,
    splashBackgroundColor: '#6366f1',
  });
}

// Usage
const embed = createDeepLinkEmbed({
  baseUrl: 'https://myapp.com',
  path: '/game',
  queryParams: {
    level: '5',
    mode: 'challenge',
    ref: 'social',
  },
  imageUrl: 'https://myapp.com/game-level-5.png',
  buttonTitle: 'Play Level 5',
});
```

## Button Title Best Practices

**Good Button Titles** (Clear CTAs):
- ✅ "View Post"
- ✅ "Join Event"
- ✅ "Play Game"
- ✅ "Read Article"
- ✅ "Shop Now"
- ✅ "Watch Video"

**Poor Button Titles** (Vague):
- ❌ "Click Here"
- ❌ "Open"
- ❌ "Go"
- ❌ "Launch"

**Guidelines**:
- Use action verbs
- Be specific to content type
- Keep under 20 characters
- Avoid generic phrases
- Match user expectations

## Complete Example: Blog Post Embeds

```typescript
// app/posts/[slug]/page.tsx
import { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { createMiniAppEmbed, generateOGImageUrl } from '@/lib/embed-utils';
import { getPostBySlug } from '@/lib/api';

interface PageProps {
  params: { slug: string };
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const post = await getPostBySlug(params.slug);

  if (!post) {
    return { title: 'Post Not Found' };
  }

  const appUrl = process.env.NEXT_PUBLIC_APP_URL!;
  const postUrl = `${appUrl}/posts/${params.slug}`;

  // Generate dynamic OG image
  const imageUrl = post.coverImage ||
    generateOGImageUrl({
      title: post.title,
      description: post.excerpt,
    });

  // Create miniapp embed
  const embedContent = createMiniAppEmbed({
    version: '1',
    imageUrl,
    buttonTitle: `Read: ${post.title.slice(0, 15)}${post.title.length > 15 ? '...' : ''}`,
    appName: 'My Blog',
    url: postUrl,
    splashImageUrl: `${appUrl}/splash.png`,
    splashBackgroundColor: '#6366f1',
  });

  return {
    title: post.title,
    description: post.excerpt,
    openGraph: {
      title: post.title,
      description: post.excerpt,
      images: [imageUrl],
      url: postUrl,
      type: 'article',
      publishedTime: post.publishedAt,
      authors: [post.author.name],
    },
    twitter: {
      card: 'summary_large_image',
      title: post.title,
      description: post.excerpt,
      images: [imageUrl],
    },
    other: {
      'fc:miniapp': embedContent,
    },
  };
}

export default async function PostPage({ params }: PageProps) {
  const post = await getPostBySlug(params.slug);

  if (!post) {
    notFound();
  }

  return <article>{/* Post content */}</article>;
}
```

## Troubleshooting

### Embed Not Showing

**Solutions**:
1. Check `fc:miniapp` meta tag is in `<head>`
2. Verify JSON is valid (use JSON validator)
3. Ensure all URLs are HTTPS
4. Check image URLs are publicly accessible
5. Test with Warpcast embed tool

### Invalid JSON Error

**Solutions**:
1. Escape special characters in strings
2. Use `JSON.stringify()` for embed content
3. Validate with JSON parser
4. Check no trailing commas
5. Ensure proper quote escaping

### Image Not Loading in Embed

**Solutions**:
1. Verify image URL is HTTPS
2. Check CORS headers on image server
3. Optimize image size (< 1MB)
4. Use proper image dimensions (1200x630px)
5. Test image URL directly in browser

## Checklist

- [ ] Embed helper functions created
- [ ] Meta tags added to shareable pages
- [ ] Image assets created (1200x630px)
- [ ] Button titles are clear and actionable
- [ ] All URLs use HTTPS
- [ ] JSON structure validated
- [ ] Tested with Warpcast embed tool
- [ ] Tested sharing actual URLs
- [ ] Dynamic OG images working (if used)
- [ ] Deep linking tested

## Resources

- Embed Specification: https://miniapps.farcaster.xyz/docs/specification
- Manifest vs Embed: https://miniapps.farcaster.xyz/docs/guides/manifest-vs-embed
- Sharing Guide: https://miniapps.farcaster.xyz/docs/guides/sharing
- OG Image Guide: https://vercel.com/docs/functions/og-image-generation

---

*This skill enables rich social sharing for your miniapp pages with beautiful, interactive embeds.*
