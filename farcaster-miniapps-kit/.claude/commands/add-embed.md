# Add Miniapp Embed

Create `fc:miniapp` embed metadata to make pages shareable as rich cards in Farcaster.

## Steps

1. Create embed utility in `lib/embed-utils.ts`

2. Add embed to page metadata (Next.js App Router):
```typescript
export async function generateMetadata({ params }) {
  const embedContent = JSON.stringify({
    version: '1',
    imageUrl: 'https://your-domain.com/og-image.png',
    button: {
      title: 'View Page',
      action: {
        type: 'launch',
        name: 'Your App',
        url: 'https://your-domain.com/page',
        splashImageUrl: 'https://your-domain.com/splash.png',
        splashBackgroundColor: '#6366f1',
      },
    },
  });

  return {
    title: 'Page Title',
    other: {
      'fc:miniapp': embedContent,
    },
  };
}
```

3. Create OG image (1200x630px)

4. Test embed:
   - Share URL in Warpcast
   - Use Warpcast Embed Tool
   - Verify preview displays correctly

## Button Title Tips

- Use clear call-to-action
- Keep under 20 characters
- Examples: "View Post", "Play Game", "Join Event"
