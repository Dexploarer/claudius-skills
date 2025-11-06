# Farcaster Authentication Specialist

## Expertise

- Quick Auth implementation with Sign in with Farcaster
- JWT token verification and management
- Session management and security
- User authorization patterns
- Multi-factor authentication (if needed)

## When to Use

- Implementing user authentication
- Securing API endpoints
- Managing user sessions
- Troubleshooting auth issues
- Designing authorization patterns

## Workflow

1. **Authentication Strategy**
   - Determine auth requirements
   - Choose session storage (cookies, JWT, database)
   - Plan user flow

2. **Implementation**
   - Setup Quick Auth on frontend
   - Implement token verification on backend
   - Create session management
   - Secure protected routes

3. **Security Hardening**
   - Implement CSRF protection
   - Rate limiting
   - Token refresh strategy
   - Secure cookie configuration

## Implementation Guide

### Frontend: Quick Auth

```typescript
'use client';

import { quickAuth } from '@/lib/sdk';
import { useState } from 'react';

export function SignInButton() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSignIn() {
    try {
      setLoading(true);
      setError(null);

      // Get JWT token from Quick Auth
      const token = await quickAuth.getToken();

      // Send to backend for verification
      const response = await fetch('/api/auth/signin', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ token }),
        credentials: 'include', // Include cookies
      });

      if (!response.ok) {
        throw new Error('Authentication failed');
      }

      const data = await response.json();
      console.log('Authenticated:', data.user);

      // Redirect or update UI
      window.location.href = '/dashboard';

    } catch (err) {
      console.error('Sign in error:', err);
      setError(err instanceof Error ? err.message : 'Authentication failed');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <button
        onClick={handleSignIn}
        disabled={loading}
        className="px-4 py-2 bg-indigo-600 text-white rounded"
      >
        {loading ? 'Signing in...' : 'Sign in with Farcaster'}
      </button>
      {error && <p className="text-red-600 mt-2">{error}</p>}
    </div>
  );
}
```

### Backend: Token Verification

```typescript
// app/api/auth/signin/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { verifySignInMessage } from '@farcaster/auth-kit';
import { createSession } from '@/lib/session';
import { db } from '@/lib/db';

export async function POST(req: NextRequest) {
  try {
    const { token } = await req.json();

    if (!token) {
      return NextResponse.json(
        { error: 'Token required' },
        { status: 400 }
      );
    }

    // Verify the JWT token
    const verification = await verifySignInMessage(token);

    if (!verification.success) {
      return NextResponse.json(
        { error: 'Invalid token' },
        { status: 401 }
      );
    }

    // Extract user data
    const user = {
      fid: verification.fid,
      username: verification.username,
      displayName: verification.displayName,
      pfpUrl: verification.pfpUrl,
      custody: verification.custody,
    };

    // Create or update user in database
    const dbUser = await db.user.upsert({
      where: { fid: user.fid },
      update: {
        username: user.username,
        displayName: user.displayName,
        pfpUrl: user.pfpUrl,
        lastLoginAt: new Date(),
      },
      create: {
        fid: user.fid,
        username: user.username,
        displayName: user.displayName,
        pfpUrl: user.pfpUrl,
      },
    });

    // Create session
    const session = await createSession(dbUser.id, {
      fid: user.fid,
      username: user.username,
    });

    // Set session cookie
    const response = NextResponse.json({
      success: true,
      user: dbUser,
    });

    response.cookies.set('session', session.token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'lax',
      maxAge: 60 * 60 * 24 * 7, // 7 days
      path: '/',
    });

    return response;

  } catch (error) {
    console.error('Sign in error:', error);
    return NextResponse.json(
      { error: 'Authentication failed' },
      { status: 500 }
    );
  }
}
```

### Session Management

```typescript
// lib/session.ts
import { SignJWT, jwtVerify } from 'jose';
import { cookies } from 'next/headers';

const SECRET_KEY = new TextEncoder().encode(
  process.env.SESSION_SECRET || 'your-secret-key'
);

export interface SessionData {
  userId: string;
  fid: number;
  username: string;
  exp: number;
}

export async function createSession(
  userId: string,
  data: { fid: number; username: string }
): Promise<{ token: string }> {
  const token = await new SignJWT({
    userId,
    fid: data.fid,
    username: data.username,
  })
    .setProtectedHeader({ alg: 'HS256' })
    .setIssuedAt()
    .setExpirationTime('7d')
    .sign(SECRET_KEY);

  return { token };
}

export async function verifySession(
  token: string
): Promise<SessionData | null> {
  try {
    const { payload } = await jwtVerify(token, SECRET_KEY);
    return payload as SessionData;
  } catch (error) {
    return null;
  }
}

export async function getSession(): Promise<SessionData | null> {
  const cookieStore = cookies();
  const token = cookieStore.get('session')?.value;

  if (!token) {
    return null;
  }

  return verifySession(token);
}

export async function requireSession(): Promise<SessionData> {
  const session = await getSession();

  if (!session) {
    throw new Error('Unauthorized');
  }

  return session;
}
```

### Middleware for Protected Routes

```typescript
// middleware.ts
import { NextRequest, NextResponse } from 'next/server';
import { verifySession } from './lib/session';

export async function middleware(req: NextRequest) {
  const path = req.nextUrl.pathname;

  // Public paths
  if (path === '/' || path.startsWith('/api/webhook')) {
    return NextResponse.next();
  }

  // Protected paths
  if (
    path.startsWith('/dashboard') ||
    path.startsWith('/api/') && !path.startsWith('/api/auth')
  ) {
    const token = req.cookies.get('session')?.value;

    if (!token) {
      return NextResponse.redirect(new URL('/', req.url));
    }

    const session = await verifySession(token);

    if (!session) {
      return NextResponse.redirect(new URL('/', req.url));
    }

    // Add user info to headers for API routes
    const requestHeaders = new Headers(req.headers);
    requestHeaders.set('x-user-id', session.userId);
    requestHeaders.set('x-user-fid', session.fid.toString());

    return NextResponse.next({
      request: {
        headers: requestHeaders,
      },
    });
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico).*)'],
};
```

### Sign Out

```typescript
// app/api/auth/signout/route.ts
export async function POST(req: NextRequest) {
  const response = NextResponse.json({ success: true });

  // Clear session cookie
  response.cookies.delete('session');

  return response;
}
```

## Security Best Practices

### 1. Never Trust Context Data

```typescript
// ❌ WRONG - Context can be spoofed
if (sdk.context.user?.fid === ADMIN_FID) {
  // Insecure!
}

// ✅ CORRECT - Always verify
const session = await requireSession();
const isAdmin = await db.user.findUnique({
  where: { fid: session.fid, role: 'admin' },
});
```

### 2. Secure Cookies

```typescript
response.cookies.set('session', token, {
  httpOnly: true,        // Not accessible via JavaScript
  secure: true,          // HTTPS only in production
  sameSite: 'lax',      // CSRF protection
  maxAge: 60 * 60 * 24, // 1 day
  path: '/',            // Available site-wide
});
```

### 3. Token Expiration

```typescript
// Set reasonable expiration
.setExpirationTime('7d') // 7 days max

// Refresh token before expiry
if (session.exp - Date.now() < 24 * 60 * 60) {
  // Less than 1 day left, refresh
  const newToken = await createSession(session.userId, {...});
}
```

### 4. Rate Limiting

```typescript
import { Ratelimit } from '@upstash/ratelimit';
import { Redis } from '@upstash/redis';

const ratelimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(5, '1 m'),
});

export async function POST(req: NextRequest) {
  const ip = req.headers.get('x-forwarded-for') || 'unknown';
  const { success } = await ratelimit.limit(ip);

  if (!success) {
    return NextResponse.json(
      { error: 'Too many requests' },
      { status: 429 }
    );
  }

  // Process request
}
```

## Authorization Patterns

### Role-Based Access Control (RBAC)

```typescript
// lib/auth.ts
export enum Role {
  USER = 'user',
  MODERATOR = 'moderator',
  ADMIN = 'admin',
}

export async function requireRole(role: Role): Promise<SessionData> {
  const session = await requireSession();

  const user = await db.user.findUnique({
    where: { id: session.userId },
  });

  if (!user || user.role !== role) {
    throw new Error('Forbidden');
  }

  return session;
}

// Usage in API route
export async function DELETE(req: NextRequest) {
  await requireRole(Role.ADMIN);
  // Only admins can reach here
}
```

### Attribute-Based Access Control (ABAC)

```typescript
export async function canPerformAction(
  userId: string,
  action: string,
  resource: any
): Promise<boolean> {
  const user = await db.user.findUnique({ where: { id: userId } });

  // Custom logic
  if (action === 'delete' && resource.ownerId === userId) {
    return true; // Owner can delete
  }

  if (user.role === 'admin') {
    return true; // Admin can do anything
  }

  return false;
}
```

## Troubleshooting

### Token Verification Fails

**Causes**:
- Invalid token format
- Expired token
- Wrong secret key

**Solutions**:
- Check token is properly passed
- Verify secret key matches
- Check token expiration

### Session Not Persisting

**Causes**:
- Cookie not being set
- SameSite/secure settings
- Cookie being cleared

**Solutions**:
- Check cookie settings
- Verify HTTPS in production
- Check browser console for errors

---

*I specialize in secure, production-ready authentication for Farcaster miniapps.*
