# /deploy-edge - Edge Function Deployment

Deploy functions to edge locations (Cloudflare, Vercel, Fastly, etc.).

---

## Usage

```
/deploy-edge [function] [platform]
/deploy-edge --list
/deploy-edge --rollback [version]
```

Examples:
- `/deploy-edge api-handler cloudflare`
- `/deploy-edge auth-middleware vercel`
- `/deploy-edge --list`
- `/deploy-edge --rollback v1.2.3`

---

## What This Command Does

1. **Pre-Deployment Checks**
   - Validate function size (<1MB)
   - Check cold start time
   - Verify environment variables
   - Test locally

2. **Build & Optimize**
   - Bundle code
   - Tree-shake dependencies
   - Minify output
   - Optimize for platform

3. **Deploy**
   - Upload to edge network
   - Configure routes
   - Set up regions
   - Apply rate limits

4. **Verify**
   - Test deployed function
   - Check response times
   - Validate from multiple regions
   - Monitor error rates

5. **Report**
   - Deployment summary
   - Edge locations
   - Performance metrics
   - Rollback instructions

---

## Supported Platforms

- **Cloudflare Workers**
- **Vercel Edge Functions**
- **Fastly Compute@Edge**
- **AWS Lambda@Edge**
- **Netlify Edge Functions**
- **Deno Deploy**

---

## Configuration

```json
{
  "platform": "cloudflare",
  "account_id": "your-account",
  "routes": [
    { "pattern": "api.example.com/*", "zone": "example.com" }
  ],
  "limits": {
    "cpu_ms": 50,
    "memory_mb": 128
  }
}
```

---

**Related Commands:**
- `/edge-logs` - View edge function logs
- `/edge-metrics` - View edge performance metrics
- `/edge-test` - Test edge function locally
