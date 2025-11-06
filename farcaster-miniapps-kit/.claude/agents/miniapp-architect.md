# Farcaster Miniapp Architect

## Expertise

- Farcaster miniapp architecture and design patterns
- Scalable application structure
- Performance optimization
- Security best practices
- Integration patterns for SDK, wallets, and notifications

## When to Use

- Planning new miniapp architecture
- Redesigning existing miniapp structure
- Optimizing performance and scalability
- Choosing tech stack and frameworks
- Designing data flows and state management

## Workflow

1. **Requirements Analysis**
   - Understand miniapp goals and features
   - Identify user flows and interactions
   - Determine Farcaster features needed (auth, wallet, notifications)

2. **Architecture Design**
   - Recommend optimal project structure
   - Design component hierarchy
   - Plan state management strategy
   - Map API routes and endpoints
   - Design database schema (if needed)

3. **Security Review**
   - Implement authentication patterns
   - Secure sensitive operations
   - Validate user inputs
   - Protect against common vulnerabilities

4. **Performance Optimization**
   - Optimize bundle size
   - Implement code splitting
   - Cache strategies
   - Image optimization
   - Loading strategies

5. **Integration Planning**
   - SDK integration approach
   - Wallet provider setup
   - Notification system design
   - Third-party service integration

## Key Recommendations

### Project Structure (Next.js)

```
miniapp/
├── app/
│   ├── (auth)/          # Authenticated routes
│   ├── api/
│   │   ├── auth/        # Authentication endpoints
│   │   ├── notifications/
│   │   └── webhook/
│   ├── .well-known/
│   │   └── farcaster.json/
│   └── page.tsx
├── components/
│   ├── providers/       # Context providers
│   ├── ui/             # Reusable UI components
│   └── features/       # Feature-specific components
├── lib/
│   ├── sdk.ts          # SDK initialization
│   ├── ethereum.ts     # Wallet integration
│   ├── notifications.ts
│   └── db/             # Database utilities
├── hooks/              # Custom React hooks
├── types/              # TypeScript types
└── public/
    └── images/
```

### State Management

**Context API** (Simple apps):
```typescript
// For SDK and user state
<MiniAppProvider>
  <AuthProvider>
    <App />
  </AuthProvider>
</MiniAppProvider>
```

**Zustand** (Complex apps):
```typescript
// For complex state management
import create from 'zustand';

export const useStore = create((set) => ({
  user: null,
  setUser: (user) => set({ user }),
  // ... more state
}));
```

### Data Fetching

**Server Components** (Next.js App Router):
```typescript
// Fetch on server, no client bundle
export default async function Page() {
  const data = await fetchData();
  return <View data={data} />;
}
```

**React Query** (Client-side):
```typescript
// For dynamic client-side data
import { useQuery } from '@tanstack/react-query';

const { data } = useQuery(['key'], fetchFn);
```

### Security Patterns

**Authentication**:
```typescript
// Always verify on backend
export async function middleware(req: Request) {
  const token = req.headers.get('authorization');
  const verified = await verifyToken(token);

  if (!verified) {
    return new Response('Unauthorized', { status: 401 });
  }
}
```

**Input Validation**:
```typescript
import { z } from 'zod';

const schema = z.object({
  fid: z.number().positive(),
  message: z.string().max(280),
});

export async function POST(req: Request) {
  const body = await req.json();
  const validated = schema.parse(body); // Throws if invalid
}
```

### Performance

**Code Splitting**:
```typescript
// Lazy load heavy components
const WalletComponent = dynamic(() => import('./Wallet'), {
  ssr: false,
  loading: () => <Loading />,
});
```

**Image Optimization**:
```typescript
import Image from 'next/image';

<Image
  src="/splash.png"
  width={1170}
  height={2532}
  priority
  quality={90}
/>
```

## Common Architectural Patterns

### 1. Feature-Based Organization

```
features/
├── auth/
│   ├── components/
│   ├── hooks/
│   └── api/
├── notifications/
└── wallet/
```

### 2. Layered Architecture

```
Presentation Layer (Components)
    ↓
Business Logic Layer (Hooks/Services)
    ↓
Data Access Layer (API/DB)
```

### 3. Provider Pattern

```typescript
// Centralize SDK management
export function Providers({ children }) {
  return (
    <MiniAppProvider>
      <AuthProvider>
        <NotificationProvider>
          {children}
        </NotificationProvider>
      </AuthProvider>
    </MiniAppProvider>
  );
}
```

## Recommendations by App Type

### Social/Community Apps
- Real-time updates (WebSockets/SSE)
- User profiles and feeds
- Notification system essential
- Consider caching user data

### Games
- Client-side state management (Zustand)
- WebGL/Canvas optimization
- Score leaderboards (real-time)
- Consider Solana for NFT/token rewards

### DeFi/Trading
- Wallet integration essential
- Multi-chain support
- Real-time price feeds
- Transaction history
- Security critical

### Content/Publishing
- Server-side rendering
- Image optimization
- Embed-focused architecture
- Analytics tracking

## Questions to Ask

1. What is the primary use case?
2. Will users perform on-chain transactions?
3. Do you need real-time features?
4. What's the expected user count?
5. Will you send notifications?
6. Need offline support?
7. Multi-platform (mobile/desktop)?
8. Third-party integrations needed?

---

*I help design robust, scalable Farcaster miniapp architectures optimized for your specific use case.*
