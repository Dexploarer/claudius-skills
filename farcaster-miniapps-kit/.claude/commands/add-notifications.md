# Add Notification System

Implement push notifications to re-engage users who have enabled notifications for your miniapp.

## Steps

1. Add webhook URL to manifest in `minikit.config.ts`:
```typescript
export const manifest = {
  // ... other fields
  webhookUrl: 'https://your-domain.com/api/webhook',
};
```

2. Create webhook handler:
```bash
mkdir -p app/api/webhook
```

3. Install SDK (optional):
```bash
npm install @farcaster/miniapp-node
```

4. Implement webhook handler:
```typescript
export async function POST(req: Request) {
  const event = await req.json();

  switch (event.type) {
    case 'notification_enabled':
      // Store event.notificationDetails.token and .url
      await storeCredentials(event.fid, event.notificationDetails);
      break;

    case 'notification_disabled':
    case 'app_removed':
      await removeCredentials(event.fid);
      break;
  }

  return new Response('OK');
}
```

5. Create notification service in `lib/notifications.ts`

6. Send test notification:
```typescript
await fetch(credentials.url, {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${credentials.token}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    notificationId: 'unique-id',
    title: 'Welcome!',
    body: 'Thanks for enabling notifications',
    targetUrl: 'https://your-domain.com/welcome',
  }),
});
```

## Best Practices

- Use unique `notificationId` for idempotency
- Rate limit (max 10/hour per user)
- Respect quiet hours
- Allow user preferences
- Log all notifications
