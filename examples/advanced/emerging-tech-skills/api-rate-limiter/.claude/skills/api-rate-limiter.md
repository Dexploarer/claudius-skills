# API Rate Limiting & Throttling

**Category:** API Security & Performance
**Level:** Advanced
**Auto-trigger:** When user mentions rate limiting, API throttling, or request quotas

---

## Description

Implements sophisticated rate limiting for APIs including token bucket, sliding window, distributed rate limiting with Redis, and tiered quotas.

---

## Code Example

```typescript
// rate-limiter.ts
import Redis from 'ioredis';

class RateLimiter {
  constructor(private redis: Redis) {}

  async checkLimit(
    key: string,
    limit: number,
    windowSeconds: number
  ): Promise<{ allowed: boolean; remaining: number }> {

    const now = Date.now();
    const windowStart = now - (windowSeconds * 1000);

    // Sliding window with Redis sorted set
    const pipeline = this.redis.pipeline();

    // Remove old entries
    pipeline.zremrangebyscore(key, 0, windowStart);

    // Add current request
    pipeline.zadd(key, now, `${now}`);

    // Count requests in window
    pipeline.zcard(key);

    // Set expiry
    pipeline.expire(key, windowSeconds);

    const results = await pipeline.exec();
    const count = results![2][1] as number;

    return {
      allowed: count <= limit,
      remaining: Math.max(0, limit - count)
    };
  }
}

// Express middleware
export function rateLimitMiddleware(
  limiter: RateLimiter,
  options: { limit: number; window: number }
) {
  return async (req: Request, res: Response, next: NextFunction) => {
    const key = `rate_limit:${req.ip}`;

    const result = await limiter.checkLimit(
      key,
      options.limit,
      options.window
    );

    res.setHeader('X-RateLimit-Limit', options.limit);
    res.setHeader('X-RateLimit-Remaining', result.remaining);

    if (!result.allowed) {
      return res.status(429).json({
        error: 'Too many requests',
        retryAfter: options.window
      });
    }

    next();
  };
}
```

---

**Last Updated:** 2025-11-02
