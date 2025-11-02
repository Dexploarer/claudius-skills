# Edge Computing Deployment Automator

**Category:** Edge Computing & IoT
**Level:** Advanced
**Auto-trigger:** When user mentions edge deployment, CDN, edge functions, or distributed edge infrastructure

---

## Description

Automates deployment of applications and services to edge locations, including edge functions, CDN configuration, edge compute optimization, and edge-native architectures for low-latency, globally distributed applications.

---

## Activation Phrases

This skill automatically activates when you say things like:

- "Deploy to edge locations"
- "Set up edge functions"
- "Configure edge CDN"
- "Create edge compute infrastructure"
- "Deploy serverless edge"
- "Set up CloudFlare Workers"
- "Configure Fastly Compute@Edge"
- "Deploy AWS Lambda@Edge"
- "Set up Vercel Edge Functions"
- "Create edge-native application"

---

## What This Skill Does

When activated, I will:

1. **Assess Edge Requirements**
   - Identify latency requirements
   - Determine geographic distribution needs
   - Evaluate compute vs CDN needs
   - Check compliance and data residency requirements

2. **Configure Edge Platform**
   - Set up edge locations
   - Configure routing and failover
   - Implement geo-replication
   - Set up edge caching strategies

3. **Deploy Edge Functions**
   - Create serverless edge functions
   - Configure triggers and routes
   - Implement edge middleware
   - Set up edge authentication

4. **Optimize for Edge**
   - Minimize bundle sizes
   - Implement edge caching
   - Configure edge streaming
   - Set up regional failover

5. **Monitor Edge Performance**
   - Track latency by region
   - Monitor cache hit rates
   - Alert on edge failures
   - Analyze edge metrics

---

## Supported Edge Platforms

### Edge Function Platforms
- **Cloudflare Workers** - Global edge compute
- **Fastly Compute@Edge** - WebAssembly edge compute
- **AWS Lambda@Edge** - CloudFront edge functions
- **Vercel Edge Functions** - Next.js edge runtime
- **Deno Deploy** - Global JavaScript runtime
- **Netlify Edge Functions** - Deno-based edge functions

### CDN Platforms
- **Cloudflare CDN** - Global CDN with edge compute
- **AWS CloudFront** - Amazon's CDN
- **Fastly** - Real-time CDN
- **Akamai** - Enterprise CDN
- **Vercel** - Optimized for Next.js
- **Netlify** - Jamstack CDN

### Edge Storage
- **Cloudflare KV** - Key-value edge storage
- **Cloudflare Durable Objects** - Stateful edge objects
- **Upstash** - Serverless Redis at edge
- **Vercel Edge Config** - Global read-only data

---

## Code Examples

### Example 1: Cloudflare Worker with Edge KV

```typescript
// edge-worker.ts
/**
 * Cloudflare Worker with edge caching and KV storage
 * Demonstrates edge compute with global state
 */

interface Env {
  EDGE_KV: KVNamespace;
  ANALYTICS: AnalyticsEngineDataset;
}

interface CacheConfig {
  ttl: number;
  cacheEverything: boolean;
  cacheKey?: string;
}

export default {
  async fetch(
    request: Request,
    env: Env,
    ctx: ExecutionContext
  ): Promise<Response> {

    const url = new URL(request.url);
    const path = url.pathname;

    // Route handling
    if (path === '/api/data') {
      return handleDataRequest(request, env, ctx);
    }

    if (path.startsWith('/api/geo')) {
      return handleGeoRequest(request, env);
    }

    // Default: proxy to origin with edge caching
    return handleOriginRequest(request, env, ctx);
  }
};

/**
 * Handle data requests with KV storage
 */
async function handleDataRequest(
  request: Request,
  env: Env,
  ctx: ExecutionContext
): Promise<Response> {

  const url = new URL(request.url);
  const key = url.searchParams.get('key');

  if (!key) {
    return new Response('Missing key parameter', { status: 400 });
  }

  // Try to get from edge KV first
  const cached = await env.EDGE_KV.get(key, { type: 'json' });

  if (cached) {
    // Track cache hit
    ctx.waitUntil(
      env.ANALYTICS.writeDataPoint({
        blobs: ['cache_hit', key],
        doubles: [1],
        indexes: [key]
      })
    );

    return new Response(JSON.stringify(cached), {
      headers: {
        'Content-Type': 'application/json',
        'X-Cache-Status': 'HIT',
        'Cache-Control': 'public, max-age=3600'
      }
    });
  }

  // Fetch from origin
  const origin = await fetch(`https://api.example.com/data/${key}`);
  const data = await origin.json();

  // Store in KV for next time (background task)
  ctx.waitUntil(
    env.EDGE_KV.put(key, JSON.stringify(data), {
      expirationTtl: 3600 // 1 hour
    })
  );

  // Track cache miss
  ctx.waitUntil(
    env.ANALYTICS.writeDataPoint({
      blobs: ['cache_miss', key],
      doubles: [1],
      indexes: [key]
    })
  );

  return new Response(JSON.stringify(data), {
    headers: {
      'Content-Type': 'application/json',
      'X-Cache-Status': 'MISS'
    }
  });
}

/**
 * Handle geo-aware requests
 */
async function handleGeoRequest(
  request: Request,
  env: Env
): Promise<Response> {

  // Cloudflare provides geo information
  const country = request.headers.get('CF-IPCountry') || 'Unknown';
  const colo = request.headers.get('CF-Ray')?.split('-')[1] || 'Unknown';
  const city = request.cf?.city || 'Unknown';
  const region = request.cf?.region || 'Unknown';
  const timezone = request.cf?.timezone || 'Unknown';

  // Return geo-specific content
  const response = {
    message: `Hello from ${city}, ${country}!`,
    location: {
      city,
      region,
      country,
      timezone,
      edgeLocation: colo
    },
    timestamp: new Date().toISOString()
  };

  return new Response(JSON.stringify(response, null, 2), {
    headers: {
      'Content-Type': 'application/json',
      'X-Edge-Location': colo
    }
  });
}

/**
 * Proxy to origin with intelligent caching
 */
async function handleOriginRequest(
  request: Request,
  env: Env,
  ctx: ExecutionContext
): Promise<Response> {

  const url = new URL(request.url);
  const cacheKey = new Request(url.toString(), request);

  // Check edge cache
  const cache = caches.default;
  let response = await cache.match(cacheKey);

  if (response) {
    return new Response(response.body, {
      ...response,
      headers: {
        ...Object.fromEntries(response.headers),
        'X-Cache-Status': 'HIT'
      }
    });
  }

  // Fetch from origin
  response = await fetch(request);

  // Clone response for caching
  const responseToCache = response.clone();

  // Cache based on content type
  const contentType = response.headers.get('Content-Type') || '';

  if (shouldCache(contentType, url.pathname)) {
    const cacheConfig = getCacheConfig(contentType, url.pathname);

    // Create cached response with custom headers
    const cachedResponse = new Response(responseToCache.body, {
      ...responseToCache,
      headers: {
        ...Object.fromEntries(responseToCache.headers),
        'Cache-Control': `public, max-age=${cacheConfig.ttl}`,
        'X-Cache-Status': 'MISS'
      }
    });

    // Store in cache (background task)
    ctx.waitUntil(cache.put(cacheKey, cachedResponse));
  }

  return response;
}

/**
 * Determine if content should be cached
 */
function shouldCache(contentType: string, pathname: string): boolean {
  // Cache static assets
  if (
    contentType.includes('image/') ||
    contentType.includes('font/') ||
    contentType.includes('application/javascript') ||
    contentType.includes('text/css')
  ) {
    return true;
  }

  // Cache API responses
  if (pathname.startsWith('/api/')) {
    return true;
  }

  return false;
}

/**
 * Get cache configuration based on content
 */
function getCacheConfig(contentType: string, pathname: string): CacheConfig {
  // Long-term cache for static assets
  if (contentType.includes('image/') || contentType.includes('font/')) {
    return { ttl: 86400 * 365, cacheEverything: true }; // 1 year
  }

  // Medium cache for JS/CSS
  if (contentType.includes('javascript') || contentType.includes('css')) {
    return { ttl: 86400 * 7, cacheEverything: true }; // 1 week
  }

  // Short cache for API
  if (pathname.startsWith('/api/')) {
    return { ttl: 300, cacheEverything: false }; // 5 minutes
  }

  // Default
  return { ttl: 3600, cacheEverything: false }; // 1 hour
}
```

### Example 2: Vercel Edge Functions with Middleware

```typescript
// middleware.ts
/**
 * Vercel Edge Middleware
 * Runs on every request at the edge
 */

import { NextRequest, NextResponse } from 'next/server';
import { geolocation, ipAddress } from '@vercel/edge';

export const config = {
  matcher: [
    /*
     * Match all request paths except static files and images
     */
    '/((?!_next/static|_next/image|favicon.ico).*)',
  ],
};

export function middleware(request: NextRequest) {

  const url = request.nextUrl;
  const hostname = request.headers.get('host') || '';

  // Get geolocation data
  const geo = geolocation(request);
  const ip = ipAddress(request) || 'unknown';

  // A/B Testing at edge
  if (url.pathname === '/') {
    const bucket = getABTestBucket(ip);

    if (bucket === 'B') {
      url.pathname = '/variant-b';
      return NextResponse.rewrite(url);
    }
  }

  // Geo-based redirects
  if (geo.country === 'CN' && !url.pathname.startsWith('/cn')) {
    url.pathname = `/cn${url.pathname}`;
    return NextResponse.redirect(url);
  }

  // Feature flags at edge
  const features = getFeatureFlags(ip, geo.country);

  const response = NextResponse.next();

  // Add custom headers
  response.headers.set('X-Edge-Location', geo.city || 'unknown');
  response.headers.set('X-Country-Code', geo.country || 'unknown');
  response.headers.set('X-Features', JSON.stringify(features));

  // Add security headers
  response.headers.set('X-Frame-Options', 'DENY');
  response.headers.set('X-Content-Type-Options', 'nosniff');
  response.headers.set('Referrer-Policy', 'strict-origin-when-cross-origin');
  response.headers.set(
    'Content-Security-Policy',
    "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline';"
  );

  return response;
}

/**
 * Simple A/B test bucketing
 */
function getABTestBucket(ip: string): 'A' | 'B' {
  // Hash IP to determine bucket
  const hash = hashCode(ip);
  return hash % 2 === 0 ? 'A' : 'B';
}

/**
 * Get feature flags based on location
 */
function getFeatureFlags(ip: string, country: string): Record<string, boolean> {
  const flags: Record<string, boolean> = {
    newUI: false,
    betaFeatures: false,
    premiumContent: false
  };

  // Enable new UI for specific countries
  if (['US', 'UK', 'CA'].includes(country)) {
    flags.newUI = true;
  }

  // Beta features for internal IPs
  if (ip.startsWith('10.') || ip.startsWith('192.168.')) {
    flags.betaFeatures = true;
  }

  return flags;
}

/**
 * Simple string hash function
 */
function hashCode(str: string): number {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    const char = str.charCodeAt(i);
    hash = ((hash << 5) - hash) + char;
    hash = hash & hash; // Convert to 32-bit integer
  }
  return Math.abs(hash);
}
```

### Example 3: Deployment Configuration (wrangler.toml)

```toml
# wrangler.toml - Cloudflare Workers deployment config

name = "edge-api"
main = "src/index.ts"
compatibility_date = "2024-01-01"

# Account and deployment settings
account_id = "your-account-id"
workers_dev = true

# Routes for production
routes = [
  { pattern = "api.example.com/*", zone_name = "example.com" },
  { pattern = "*.example.com/api/*", zone_name = "example.com" }
]

# KV Namespaces
kv_namespaces = [
  { binding = "EDGE_KV", id = "your-kv-namespace-id", preview_id = "preview-kv-id" }
]

# Durable Objects
durable_objects.bindings = [
  { name = "COUNTER", class_name = "Counter", script_name = "edge-api" }
]

# Analytics Engine
analytics_engine_datasets = [
  { binding = "ANALYTICS" }
]

# Environment variables
[env.production]
vars = { ENVIRONMENT = "production", API_URL = "https://api.example.com" }

[env.staging]
vars = { ENVIRONMENT = "staging", API_URL = "https://staging-api.example.com" }

# Build configuration
[build]
command = "npm run build"
watch_dir = "src"

# Deployment configuration
[deploy]
workers_dev = false
routes = [
  "example.com/api/*"
]

# Limits and configuration
limits = { cpu_ms = 50 }

# Compatibility flags
compatibility_flags = [ "nodejs_compat" ]
```

---

## Best Practices

### 1. **Minimize Edge Function Size**
- Keep bundles small (<1MB for most platforms)
- Tree-shake unused code
- Use dynamic imports for large dependencies
- Optimize for cold start time

### 2. **Use Edge Caching Effectively**
- Cache static content aggressively
- Use stale-while-revalidate patterns
- Implement cache keys strategically
- Monitor cache hit rates

### 3. **Handle Geographic Distribution**
- Use geo-routing for content delivery
- Implement regional failover
- Consider data residency requirements
- Test from multiple regions

### 4. **Optimize for Cold Starts**
- Minimize initialization code
- Use lightweight dependencies
- Implement lazy loading
- Keep state minimal

### 5. **Monitor Edge Performance**
- Track latency by region
- Monitor error rates per location
- Alert on edge outages
- Analyze cache effectiveness

---

## Common Pitfalls

❌ **Large Bundle Sizes**
```typescript
// Importing entire lodash
import _ from 'lodash';
// → Huge bundle, slow cold starts
```

✅ **Import Only What You Need**
```typescript
// Import specific functions
import { debounce } from 'lodash/debounce';
```

---

❌ **No Error Handling**
```typescript
const data = await fetch(origin);
return new Response(data);
```

✅ **Robust Error Handling**
```typescript
try {
  const data = await fetch(origin);
  return new Response(data);
} catch (error) {
  return new Response('Service unavailable', { status: 503 });
}
```

---

## Production Checklist

- [ ] Edge locations configured
- [ ] Caching strategy defined
- [ ] Geographic routing set up
- [ ] Failover mechanism implemented
- [ ] Bundle size optimized (<1MB)
- [ ] Cold start time measured
- [ ] Regional monitoring enabled
- [ ] Cache hit rates tracked
- [ ] Security headers configured
- [ ] Rate limiting implemented
- [ ] Load testing completed
- [ ] Multi-region testing done

---

**Last Updated:** 2025-11-02
**Version:** 1.0.0
