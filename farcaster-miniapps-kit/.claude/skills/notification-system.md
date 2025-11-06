---
name: notification-system
description: Implement push notifications for Farcaster miniapps with webhooks and notification management
version: 1.0.0
category: farcaster
tags: [farcaster, miniapps, notifications, webhooks, push]
author: Claudius Skills
---

# Farcaster Miniapp Notification System

## Purpose

This skill helps you implement push notifications for your Farcaster miniapp, allowing you to send notifications to users who have added your app and enabled notifications. Notifications appear in users' Farcaster clients (Warpcast, etc.) and can drive re-engagement.

## Activation Phrases

- "implement farcaster notifications"
- "setup miniapp notifications"
- "add push notifications"
- "create notification system"
- "setup notification webhooks"
- "send miniapp notifications"

## Understanding Notifications

**How It Works**:
1. User adds your miniapp to their app list
2. User enables notifications for your app
3. Your app receives a webhook with notification credentials
4. You can send notifications to that user via the provided URL

**Notification Flow**:
```
User Adds App → Webhook Triggered → Store Credentials → Send Notifications
```

## Prerequisites

1. **Manifest with webhook URL**:
   ```typescript
   export const manifest = {
     // ...other fields
     webhookUrl: 'https://api.myapp.com/webhook',
   };
   ```

2. **Node.js SDK (optional but recommended)**:
   ```bash
   npm install @farcaster/miniapp-node
   ```

## Instructions

### Step 1: Create Webhook Handler

**Using @farcaster/miniapp-node** (Recommended):

```typescript
// app/api/webhook/route.ts (Next.js App Router)
import { NextRequest, NextResponse } from 'next/server';
import { handleWebhook } from '@farcaster/miniapp-node';
import { storeNotificationCredentials } from '@/lib/notifications';

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();

    // Use SDK to handle webhook
    const event = handleWebhook(body);

    switch (event.type) {
      case 'notification_enabled':
        // User enabled notifications
        await storeNotificationCredentials({
          fid: event.fid,
          token: event.notificationDetails.token,
          url: event.notificationDetails.url,
          enabledAt: new Date(),
        });

        console.log(`Notifications enabled for FID ${event.fid}`);
        break;

      case 'notification_disabled':
        // User disabled notifications
        await deleteNotificationCredentials(event.fid);
        console.log(`Notifications disabled for FID ${event.fid}`);
        break;

      case 'app_removed':
        // User removed the app
        await deleteNotificationCredentials(event.fid);
        console.log(`App removed by FID ${event.fid}`);
        break;

      default:
        console.log('Unknown webhook event:', event.type);
    }

    return NextResponse.json({ success: true });

  } catch (error) {
    console.error('Webhook error:', error);
    return NextResponse.json(
      { error: 'Webhook processing failed' },
      { status: 500 }
    );
  }
}
```

**Manual Implementation** (without SDK):

```typescript
// app/api/webhook/route.ts
import { NextRequest, NextResponse } from 'next/server';

interface WebhookEvent {
  type: 'notification_enabled' | 'notification_disabled' | 'app_removed';
  fid: number;
  notificationDetails?: {
    token: string;
    url: string;
  };
  timestamp: string;
}

export async function POST(req: NextRequest) {
  try {
    const event: WebhookEvent = await req.json();

    // Validate webhook (add signature verification in production)
    if (!event.type || !event.fid) {
      return NextResponse.json(
        { error: 'Invalid webhook payload' },
        { status: 400 }
      );
    }

    switch (event.type) {
      case 'notification_enabled':
        if (!event.notificationDetails) {
          throw new Error('Missing notification details');
        }

        // Store credentials
        await db.notificationCredentials.create({
          data: {
            fid: event.fid,
            token: event.notificationDetails.token,
            url: event.notificationDetails.url,
            enabledAt: new Date(),
          },
        });
        break;

      case 'notification_disabled':
      case 'app_removed':
        // Remove credentials
        await db.notificationCredentials.delete({
          where: { fid: event.fid },
        });
        break;
    }

    return NextResponse.json({ success: true });

  } catch (error) {
    console.error('Webhook error:', error);
    return NextResponse.json(
      { error: 'Processing failed' },
      { status: 500 }
    );
  }
}
```

### Step 2: Database Schema

**Prisma Schema**:

```prisma
// schema.prisma
model NotificationCredential {
  id         String   @id @default(cuid())
  fid        Int      @unique
  token      String
  url        String
  enabledAt  DateTime @default(now())
  updatedAt  DateTime @updatedAt

  @@index([fid])
}

model NotificationLog {
  id            String   @id @default(cuid())
  fid           Int
  notificationId String  @unique
  title         String
  body          String
  targetUrl     String?
  sentAt        DateTime @default(now())
  deliveredAt   DateTime?
  errorMessage  String?

  @@index([fid])
  @@index([notificationId])
}
```

**SQL Schema** (if not using Prisma):

```sql
CREATE TABLE notification_credentials (
  id SERIAL PRIMARY KEY,
  fid INTEGER UNIQUE NOT NULL,
  token TEXT NOT NULL,
  url TEXT NOT NULL,
  enabled_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_fid ON notification_credentials(fid);

CREATE TABLE notification_logs (
  id SERIAL PRIMARY KEY,
  fid INTEGER NOT NULL,
  notification_id TEXT UNIQUE NOT NULL,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  target_url TEXT,
  sent_at TIMESTAMP DEFAULT NOW(),
  delivered_at TIMESTAMP,
  error_message TEXT
);

CREATE INDEX idx_notification_fid ON notification_logs(fid);
CREATE INDEX idx_notification_id ON notification_logs(notification_id);
```

### Step 3: Notification Service

Create notification sending service (`lib/notifications.ts`):

```typescript
import crypto from 'crypto';

export interface NotificationPayload {
  title: string;
  body: string;
  targetUrl?: string;
  icon?: string;
}

export interface NotificationCredentials {
  fid: number;
  token: string;
  url: string;
}

export class NotificationService {
  /**
   * Send a notification to a specific user
   */
  async sendNotification(
    credentials: NotificationCredentials,
    payload: NotificationPayload
  ): Promise<{ success: boolean; notificationId?: string; error?: string }> {
    try {
      // Generate unique notification ID (for idempotency)
      const notificationId = this.generateNotificationId(credentials.fid);

      const response = await fetch(credentials.url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${credentials.token}`,
        },
        body: JSON.stringify({
          notificationId,
          title: payload.title,
          body: payload.body,
          targetUrl: payload.targetUrl,
          icon: payload.icon,
        }),
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Notification failed: ${errorText}`);
      }

      // Log successful notification
      await this.logNotification({
        fid: credentials.fid,
        notificationId,
        ...payload,
        deliveredAt: new Date(),
      });

      return { success: true, notificationId };

    } catch (error) {
      console.error('Failed to send notification:', error);

      // Log failed notification
      await this.logNotification({
        fid: credentials.fid,
        notificationId: this.generateNotificationId(credentials.fid),
        ...payload,
        errorMessage: error instanceof Error ? error.message : 'Unknown error',
      });

      return {
        success: false,
        error: error instanceof Error ? error.message : 'Unknown error',
      };
    }
  }

  /**
   * Send notifications to multiple users
   */
  async sendBulkNotifications(
    recipients: NotificationCredentials[],
    payload: NotificationPayload
  ): Promise<{ sent: number; failed: number }> {
    const results = await Promise.allSettled(
      recipients.map(creds => this.sendNotification(creds, payload))
    );

    const sent = results.filter(r => r.status === 'fulfilled' && r.value.success).length;
    const failed = results.length - sent;

    return { sent, failed };
  }

  /**
   * Generate unique notification ID for idempotency
   * Format: FID-TIMESTAMP-RANDOM
   */
  private generateNotificationId(fid: number): string {
    const timestamp = Date.now();
    const random = crypto.randomBytes(8).toString('hex');
    return `${fid}-${timestamp}-${random}`;
  }

  /**
   * Log notification attempt
   */
  private async logNotification(data: {
    fid: number;
    notificationId: string;
    title: string;
    body: string;
    targetUrl?: string;
    deliveredAt?: Date;
    errorMessage?: string;
  }): Promise<void> {
    try {
      await db.notificationLog.create({ data });
    } catch (error) {
      console.error('Failed to log notification:', error);
    }
  }
}

export const notificationService = new NotificationService();
```

### Step 4: Send Notifications

**Example: Welcome Notification**:

```typescript
// app/api/notifications/welcome/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { notificationService } from '@/lib/notifications';
import { getNotificationCredentials } from '@/lib/db';

export async function POST(req: NextRequest) {
  try {
    const { fid } = await req.json();

    // Get user's notification credentials
    const credentials = await getNotificationCredentials(fid);

    if (!credentials) {
      return NextResponse.json(
        { error: 'Notifications not enabled for this user' },
        { status: 404 }
      );
    }

    // Send welcome notification
    const result = await notificationService.sendNotification(
      credentials,
      {
        title: 'Welcome to My Miniapp! 🎉',
        body: 'Thanks for enabling notifications. Stay tuned for updates!',
        targetUrl: `${process.env.NEXT_PUBLIC_APP_URL}/welcome`,
        icon: `${process.env.NEXT_PUBLIC_APP_URL}/icon.png`,
      }
    );

    return NextResponse.json(result);

  } catch (error) {
    console.error('Welcome notification error:', error);
    return NextResponse.json(
      { error: 'Failed to send notification' },
      { status: 500 }
    );
  }
}
```

**Example: Event Reminders**:

```typescript
// lib/cron/event-reminders.ts
import { notificationService } from '@/lib/notifications';
import { getUpcomingEvents, getEventAttendees } from '@/lib/events';

export async function sendEventReminders() {
  // Get events starting in 1 hour
  const events = await getUpcomingEvents({ startingIn: '1 hour' });

  for (const event of events) {
    const attendees = await getEventAttendees(event.id);

    // Send to all attendees
    await notificationService.sendBulkNotifications(
      attendees,
      {
        title: `${event.name} starts soon!`,
        body: `Your event "${event.name}" starts in 1 hour`,
        targetUrl: `${process.env.NEXT_PUBLIC_APP_URL}/events/${event.id}`,
      }
    );
  }
}
```

**Example: User Mentions**:

```typescript
// When user is mentioned in a post
async function notifyMention(mentionedFid: number, post: Post) {
  const credentials = await getNotificationCredentials(mentionedFid);

  if (credentials) {
    await notificationService.sendNotification(
      credentials,
      {
        title: `${post.author.username} mentioned you`,
        body: post.text.slice(0, 100),
        targetUrl: `${process.env.NEXT_PUBLIC_APP_URL}/posts/${post.id}`,
      }
    );
  }
}
```

### Step 5: Idempotency

**IMPORTANT**: Hosts deduplicate notifications using `(FID, notificationId)` for 24 hours.

This allows safe retries:

```typescript
async function sendWithRetry(
  credentials: NotificationCredentials,
  payload: NotificationPayload,
  maxRetries: number = 3
): Promise<boolean> {
  // Use same notificationId for all retries
  const notificationId = `manual-${credentials.fid}-${Date.now()}`;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const response = await fetch(credentials.url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${credentials.token}`,
        },
        body: JSON.stringify({
          notificationId, // Same ID = idempotent
          ...payload,
        }),
      });

      if (response.ok) {
        return true;
      }

      // Wait before retry (exponential backoff)
      await new Promise(resolve => setTimeout(resolve, 1000 * attempt));

    } catch (error) {
      console.error(`Attempt ${attempt} failed:`, error);
      if (attempt === maxRetries) {
        throw error;
      }
    }
  }

  return false;
}
```

### Step 6: Rate Limiting

Implement rate limiting to avoid spam:

```typescript
// lib/rate-limiter.ts
import { Redis } from '@upstash/redis';

const redis = new Redis({
  url: process.env.UPSTASH_REDIS_URL!,
  token: process.env.UPSTASH_REDIS_TOKEN!,
});

export async function checkNotificationRateLimit(
  fid: number,
  limit: number = 10, // max notifications per hour
  window: number = 3600 // 1 hour in seconds
): Promise<{ allowed: boolean; remaining: number }> {
  const key = `notification:ratelimit:${fid}`;

  const current = await redis.incr(key);

  if (current === 1) {
    // First request, set expiry
    await redis.expire(key, window);
  }

  const remaining = Math.max(0, limit - current);

  return {
    allowed: current <= limit,
    remaining,
  };
}

// Usage
const rateLimit = await checkNotificationRateLimit(fid);

if (!rateLimit.allowed) {
  throw new Error('Rate limit exceeded');
}

await notificationService.sendNotification(credentials, payload);
```

### Step 7: User Preferences

Allow users to customize notification preferences:

```typescript
// lib/notification-preferences.ts
export interface NotificationPreferences {
  fid: number;
  enableMentions: boolean;
  enableEvents: boolean;
  enableUpdates: boolean;
  quietHoursStart?: string; // "22:00"
  quietHoursEnd?: string;   // "08:00"
  timezone: string;
}

export async function shouldSendNotification(
  fid: number,
  type: 'mention' | 'event' | 'update'
): Promise<boolean> {
  const prefs = await getNotificationPreferences(fid);

  if (!prefs) {
    return true; // Default: allow all
  }

  // Check notification type preference
  const typeEnabled = {
    mention: prefs.enableMentions,
    event: prefs.enableEvents,
    update: prefs.enableUpdates,
  }[type];

  if (!typeEnabled) {
    return false;
  }

  // Check quiet hours
  if (prefs.quietHoursStart && prefs.quietHoursEnd) {
    const now = new Date().toLocaleTimeString('en-US', {
      hour12: false,
      timeZone: prefs.timezone,
    });

    const isQuietHour = isTimeInRange(
      now,
      prefs.quietHoursStart,
      prefs.quietHoursEnd
    );

    if (isQuietHour) {
      return false;
    }
  }

  return true;
}
```

### Step 8: Analytics

Track notification performance:

```typescript
// lib/notification-analytics.ts
export async function getNotificationStats(fid?: number) {
  const stats = await db.notificationLog.aggregate({
    where: fid ? { fid } : undefined,
    _count: {
      id: true,
    },
    _sum: {
      delivered: true,
    },
  });

  const deliveryRate = stats._count.id > 0
    ? (stats._sum.delivered || 0) / stats._count.id
    : 0;

  return {
    totalSent: stats._count.id,
    totalDelivered: stats._sum.delivered || 0,
    deliveryRate: (deliveryRate * 100).toFixed(2) + '%',
  };
}

export async function getEngagementRate(days: number = 7) {
  // Users who clicked notifications vs total notifications sent
  const clickedNotifications = await db.notificationLog.count({
    where: {
      sentAt: {
        gte: new Date(Date.now() - days * 24 * 60 * 60 * 1000),
      },
      clickedAt: {
        not: null,
      },
    },
  });

  const totalNotifications = await db.notificationLog.count({
    where: {
      sentAt: {
        gte: new Date(Date.now() - days * 24 * 60 * 60 * 1000),
      },
    },
  });

  const rate = totalNotifications > 0
    ? clickedNotifications / totalNotifications
    : 0;

  return {
    clickedNotifications,
    totalNotifications,
    engagementRate: (rate * 100).toFixed(2) + '%',
  };
}
```

## Complete Example: Newsletter Notifications

```typescript
// app/api/admin/send-newsletter/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { notificationService } from '@/lib/notifications';
import { getAllNotificationCredentials } from '@/lib/db';
import { checkNotificationRateLimit } from '@/lib/rate-limiter';

export async function POST(req: NextRequest) {
  try {
    const { title, body, targetUrl } = await req.json();

    // Get all users with notifications enabled
    const allCredentials = await getAllNotificationCredentials();

    console.log(`Sending newsletter to ${allCredentials.length} users`);

    let sent = 0;
    let failed = 0;
    let rateimited = 0;

    // Send in batches to avoid overwhelming
    const batchSize = 10;

    for (let i = 0; i < allCredentials.length; i += batchSize) {
      const batch = allCredentials.slice(i, i + batchSize);

      const results = await Promise.allSettled(
        batch.map(async (creds) => {
          // Check rate limit
          const rateLimit = await checkNotificationRateLimit(creds.fid);

          if (!rateLimit.allowed) {
            ratelimited++;
            return { success: false, error: 'Rate limited' };
          }

          // Send notification
          return notificationService.sendNotification(creds, {
            title,
            body,
            targetUrl,
          });
        })
      );

      results.forEach(result => {
        if (result.status === 'fulfilled' && result.value.success) {
          sent++;
        } else {
          failed++;
        }
      });

      // Wait between batches
      await new Promise(resolve => setTimeout(resolve, 1000));
    }

    return NextResponse.json({
      success: true,
      sent,
      failed,
      ratelimited,
      total: allCredentials.length,
    });

  } catch (error) {
    console.error('Newsletter error:', error);
    return NextResponse.json(
      { error: 'Failed to send newsletter' },
      { status: 500 }
    );
  }
}
```

## Best Practices

1. **Use Idempotent IDs**: Same ID = same notification (24hr deduplication)
2. **Implement Rate Limiting**: Prevent spam (10/hour recommended)
3. **Respect User Preferences**: Allow opt-out per notification type
4. **Handle Quiet Hours**: Don't disturb users at night
5. **Batch Sending**: Send in batches, not all at once
6. **Log Everything**: Track sent, delivered, clicked
7. **Retry Failed**: Use same notification ID for retries
8. **Clear CTAs**: Make targetUrl meaningful

## Troubleshooting

### Webhook Not Receiving Events

**Solutions**:
- Verify `webhookUrl` in manifest
- Ensure endpoint is publicly accessible (HTTPS)
- Check webhook endpoint returns 200 OK
- Review server logs for errors

### Notifications Not Delivering

**Solutions**:
- Verify user has notifications enabled
- Check credentials are up-to-date
- Ensure rate limits not exceeded
- Validate token and URL

### Duplicate Notifications

**Solutions**:
- Use unique `notificationId`
- Don't reuse IDs within 24 hours
- Implement idempotency on your side too

## Checklist

- [ ] Manifest includes `webhookUrl`
- [ ] Webhook endpoint created
- [ ] Database schema for credentials
- [ ] Notification service implemented
- [ ] Idempotency implemented
- [ ] Rate limiting added
- [ ] User preferences system
- [ ] Error handling and logging
- [ ] Analytics tracking
- [ ] Tested with real users

## Resources

- Notification Guide: https://miniapps.farcaster.xyz/docs/guides/notifications
- Webhook Specification: https://miniapps.farcaster.xyz/docs/specification
- Neynar Managed Notifications: https://docs.neynar.com/docs/send-notifications-to-mini-app-users

---

*This skill enables re-engagement through timely, relevant push notifications to your miniapp users.*
