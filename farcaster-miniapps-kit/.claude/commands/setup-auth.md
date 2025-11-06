# Setup Authentication

Implement Quick Auth for secure user authentication in your miniapp.

## Steps

1. Create authentication button component:
```typescript
'use client';

import { quickAuth } from '@/lib/sdk';

export function AuthButton() {
  async function signIn() {
    const token = await quickAuth.getToken();

    await fetch('/api/auth/verify', {
      method: 'POST',
      body: JSON.stringify({ token }),
    });
  }

  return <button onClick={signIn}>Sign in with Farcaster</button>;
}
```

2. Create backend verification route:
```bash
mkdir -p app/api/auth/verify
```

3. Install auth verification library:
```bash
npm install @farcaster/auth-kit
```

4. Implement verification:
```typescript
import { verifySignInMessage } from '@farcaster/auth-kit';

export async function POST(req: Request) {
  const { token } = await req.json();

  const result = await verifySignInMessage(token);

  if (!result.success) {
    return new Response('Invalid', { status: 401 });
  }

  // Create session with result.fid, result.username, etc.
  return Response.json({ user: result });
}
```

5. Test authentication flow

## Security Notes

- Never trust `sdk.context.user` for authorization
- Always verify tokens on backend
- Use HTTPS in production
- Store tokens securely
