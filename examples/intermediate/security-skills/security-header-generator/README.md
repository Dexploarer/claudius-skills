# Security Header Generator - Intermediate Example

A security-focused skill that generates HTTP security headers to protect web applications from common attacks like XSS, clickjacking, and MITM attacks.

## What This Example Teaches

- Understanding HTTP security headers and their purpose
- Framework-specific security configuration
- Content Security Policy (CSP) implementation
- CORS (Cross-Origin Resource Sharing) setup
- HSTS (HTTP Strict Transport Security) configuration
- Security testing and validation
- Balance between security and functionality

## Why Security Headers Matter

### Attack Prevention

**Without security headers:**
- ❌ Vulnerable to XSS (Cross-Site Scripting)
- ❌ Susceptible to clickjacking attacks
- ❌ Exposed to MITM (Man-in-the-Middle) attacks
- ❌ MIME-sniffing vulnerabilities
- ❌ Unauthorized cross-origin access

**With security headers:**
- ✅ XSS attacks blocked by CSP
- ✅ Clickjacking prevented by X-Frame-Options
- ✅ HTTPS enforced by HSTS
- ✅ MIME-sniffing prevented
- ✅ Controlled cross-origin access

### Real-World Impact

```
Security Audit Before Headers:
Grade: F
Vulnerabilities: 8 high-risk issues
Risk Level: Critical

Security Audit After Headers:
Grade: A+
Vulnerabilities: 0 high-risk issues
Risk Level: Low
```

### Compliance Requirements

Many regulations require security headers:
- **PCI DSS**: Requires secure transmission (HSTS)
- **HIPAA**: Requires data protection (CSP, CORS)
- **GDPR**: Requires privacy protection (Referrer-Policy)
- **SOC 2**: Requires security controls (all headers)

## How to Use

### 1. Install the Skill

```bash
# Copy to your Claude config
cp SKILL.md ~/.claude/skills/security-header-generator.md

# Or for project-specific
cp SKILL.md your-project/.claude/skills/security-header-generator.md
```

### 2. Generate Headers

```bash
cd your-project
claude

# Then ask:
"Add security headers to my Express app"
"Setup Content Security Policy for Next.js"
"Configure CORS for my API"
"Enable HSTS on nginx"
"Secure my application with HTTP headers"
```

## Example Usage Scenarios

### Scenario 1: New Next.js Project

**You:**
```
I'm building a Next.js application. Can you add security headers?
```

**Claude (using security-header-generator skill):**
```
🔐 Setting up security headers for your Next.js application...

Detected: Next.js 14 project

I'll configure the following security headers:
✓ Content Security Policy (CSP) - Prevents XSS attacks
✓ HTTP Strict Transport Security (HSTS) - Forces HTTPS
✓ X-Frame-Options - Prevents clickjacking
✓ X-Content-Type-Options - Prevents MIME sniffing
✓ Referrer-Policy - Controls referrer information
✓ Permissions-Policy - Restricts browser features

Creating next.config.js with security headers...

✅ Configuration created!

Security headers configured:

1. CSP: Allows same-origin resources, blocks inline scripts
2. HSTS: 2-year max-age with subdomains and preload
3. X-Frame-Options: SAMEORIGIN (allows framing by same origin)
4. X-Content-Type-Options: nosniff
5. Referrer-Policy: strict-origin-when-cross-origin
6. Permissions-Policy: Restricts camera, microphone, geolocation

⚠️ Important Notes:
- CSP uses 'unsafe-inline' for scripts (needed for Next.js)
- Test thoroughly before deploying
- HSTS cannot be easily undone once set

Next Steps:
1. Test locally: npm run dev
2. Check headers: curl -I http://localhost:3000
3. Security scan: https://securityheaders.com
4. Deploy to staging first

Would you like me to create a more strict CSP policy?
```

### Scenario 2: Express API with CORS

**You:**
```
My Express API needs CORS and security headers. Frontend is at https://app.example.com
```

**Claude (using security-header-generator skill):**
```
🔐 Configuring security headers and CORS for your Express API...

Detected: Express.js application

Installing required packages:
```bash
npm install helmet cors
```

Creating security configuration...

✅ Configuration complete!

File: server.js (updated)

Added:
1. Helmet middleware for security headers
2. CORS configuration for https://app.example.com
3. Credentials support enabled
4. API-specific security settings

CORS Configuration:
- Allowed origin: https://app.example.com
- Methods: GET, POST, PUT, DELETE, OPTIONS
- Credentials: Enabled
- Headers: Content-Type, Authorization

Security Headers:
- HSTS: 2-year max-age
- X-Frame-Options: DENY (API doesn't need framing)
- X-Content-Type-Options: nosniff
- No CSP (API returns JSON, not HTML)

Test with:
```bash
curl -H "Origin: https://app.example.com" \
     -H "Access-Control-Request-Method: POST" \
     -H "Access-Control-Request-Headers: Authorization" \
     -X OPTIONS \
     http://localhost:3000/api/endpoint
```

Expected response should include:
- Access-Control-Allow-Origin: https://app.example.com
- Access-Control-Allow-Credentials: true
- Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS

⚠️ Security Notes:
- Never use wildcard (*) origin with credentials
- Add production origin to .env file
- Test CORS from browser console
- Monitor for CORS errors

Would you like me to add rate limiting and additional security middleware?
```

### Scenario 3: nginx Production Server

**You:**
```
Add security headers to my nginx configuration for production
```

**Claude (using security-header-generator skill):**
```
🔐 Configuring security headers for nginx production server...

Detected: nginx configuration

I'll add production-grade security headers to your nginx config.

Creating/updating nginx configuration...

✅ Security headers configured!

File: /etc/nginx/sites-available/your-site

Added Headers:
1. Strict-Transport-Security: 2-year max-age with preload
2. Content-Security-Policy: Strict policy (no unsafe-inline/eval)
3. X-Frame-Options: DENY
4. X-Content-Type-Options: nosniff
5. X-XSS-Protection: 1; mode=block
6. Referrer-Policy: strict-origin-when-cross-origin
7. Permissions-Policy: Restrictive (all features blocked)

SSL Configuration:
- TLS 1.2 and 1.3 only
- Strong cipher suites
- HTTP to HTTPS redirect

⚠️ Critical Production Steps:

1. Test configuration syntax:
   sudo nginx -t

2. If successful, reload nginx:
   sudo systemctl reload nginx

3. Verify headers:
   curl -I https://your-domain.com

4. Security scan:
   https://securityheaders.com/?q=your-domain.com
   https://www.ssllabs.com/ssltest/analyze.html?d=your-domain.com

5. Monitor logs for errors:
   sudo tail -f /var/log/nginx/error.log

Expected Security Grade: A+

⚠️ HSTS Warning:
Once HSTS is set with preload, it's very difficult to undo.
This config will submit your domain for HSTS preload list.
Make sure HTTPS works perfectly before deploying!

Would you like me to:
1. Add CSP reporting endpoint?
2. Configure additional security features?
3. Setup Let's Encrypt SSL?
```

## What Makes This an Intermediate Example?

### 1. Security Expertise Required

**Understanding Threats:**
- XSS (Cross-Site Scripting) attacks
- CSRF (Cross-Site Request Forgery)
- Clickjacking and UI redressing
- MITM (Man-in-the-Middle) attacks
- MIME-sniffing vulnerabilities
- Information leakage

**Defense Mechanisms:**
- How CSP prevents XSS
- How HSTS prevents MITM
- How X-Frame-Options prevents clickjacking
- How CORS controls access

### 2. Framework Knowledge

Different configuration for each:
- **Next.js**: Configuration object in next.config.js
- **Express**: Middleware (Helmet)
- **nginx**: Server block directives
- **Apache**: .htaccess directives
- **Flask**: Talisman middleware
- **Django**: Settings.py configuration

### 3. CSP Complexity

Content Security Policy is complex:

**Simple example:**
```
default-src 'self'
```

**Real-world example:**
```
default-src 'self';
script-src 'self' 'nonce-abc123' https://cdn.example.com;
style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
img-src 'self' data: https: *.example.com;
font-src 'self' data: https://fonts.gstatic.com;
connect-src 'self' https://api.example.com wss://ws.example.com;
frame-src 'self' https://www.youtube.com;
media-src 'self' https://media.example.com;
object-src 'none';
base-uri 'self';
form-action 'self';
frame-ancestors 'self';
upgrade-insecure-requests;
block-all-mixed-content;
```

### 4. Balancing Security vs Functionality

Common tradeoffs:
- **'unsafe-inline'**: Needed for some frameworks, reduces security
- **'unsafe-eval'**: Required by some libraries, major security risk
- **Wildcard origins**: Easy but insecure
- **Strict CSP**: Secure but may break features

### 5. Production Considerations

- **HSTS Preloading**: Nearly irreversible
- **CSP Violations**: Need monitoring and reporting
- **CORS Complexity**: Preflight requests, credentials
- **Browser Compatibility**: Some headers not universally supported
- **Performance**: Additional headers add overhead

## Security Headers Deep Dive

### Content Security Policy (CSP)

**Purpose**: Prevents XSS by controlling resource loading

**Directives:**

```
default-src 'self'              # Fallback for all fetch directives
script-src 'self' 'nonce-xxx'   # Where scripts can load from
style-src 'self' 'unsafe-inline' # Where styles can load from
img-src 'self' data: https:     # Where images can load from
font-src 'self' data:           # Where fonts can load from
connect-src 'self' api.example.com # Where fetch/XHR can connect
frame-src 'self'                # Where iframes can load from
media-src 'self'                # Where audio/video can load from
object-src 'none'               # No plugins
base-uri 'self'                 # Restricts <base> tag
form-action 'self'              # Where forms can submit
frame-ancestors 'none'          # Who can frame this page
upgrade-insecure-requests       # Upgrade HTTP to HTTPS
block-all-mixed-content         # Block HTTP on HTTPS page
```

**Using Nonces (Recommended):**

```javascript
// Generate nonce
const crypto = require('crypto')
const nonce = crypto.randomBytes(16).toString('base64')

// Set in CSP header
res.setHeader('Content-Security-Policy', `script-src 'nonce-${nonce}'`)

// Use in HTML
<script nonce="${nonce}">
  console.log('This script is allowed')
</script>
```

**CSP Reporting:**

```javascript
Content-Security-Policy: default-src 'self'; report-uri /csp-report

// Report endpoint
app.post('/csp-report', (req, res) => {
  console.log('CSP Violation:', req.body)
  // Send to logging service (Sentry, etc.)
  res.status(204).end()
})
```

**Testing CSP:**

```javascript
// Start with report-only mode
Content-Security-Policy-Report-Only: default-src 'self'

// Monitor reports, fix violations
// Then enforce
Content-Security-Policy: default-src 'self'
```

### HTTP Strict Transport Security (HSTS)

**Purpose**: Force HTTPS, prevent protocol downgrade attacks

**Syntax:**
```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

**Parameters:**
- **max-age**: Seconds to remember HTTPS-only (1-2 years typical)
- **includeSubDomains**: Apply to all subdomains
- **preload**: Submit to browser preload list

**Preload Process:**

1. Set HSTS header with preload
2. Submit to https://hstspreload.org/
3. Wait for browser updates (months)
4. Domain permanently HTTPS-only

**⚠️ Warning:** Preload is nearly irreversible. Test thoroughly!

**Rollout Strategy:**

```javascript
// Week 1: Short max-age, no preload
max-age=86400  // 1 day

// Week 2-4: Longer max-age, monitor
max-age=604800  // 1 week

// Month 2-3: Production max-age
max-age=31536000  // 1 year

// After thorough testing: Preload
max-age=31536000; includeSubDomains; preload
```

### Cross-Origin Resource Sharing (CORS)

**Purpose**: Control which origins can access resources

**Simple CORS (Public API):**
```javascript
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST
```

**CORS with Credentials:**
```javascript
Access-Control-Allow-Origin: https://app.example.com  // Must be specific
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
```

**Preflight Requests:**

Browser sends OPTIONS request first:
```http
OPTIONS /api/users
Origin: https://app.example.com
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Authorization
```

Server must respond:
```http
200 OK
Access-Control-Allow-Origin: https://app.example.com
Access-Control-Allow-Methods: POST
Access-Control-Allow-Headers: Authorization
Access-Control-Max-Age: 3600  // Cache preflight for 1 hour
```

**CORS in Different Frameworks:**

```javascript
// Express
app.use(cors({
  origin: (origin, callback) => {
    const allowed = ['https://app.example.com', 'https://admin.example.com']
    if (!origin || allowed.includes(origin)) {
      callback(null, true)
    } else {
      callback(new Error('CORS not allowed'))
    }
  },
  credentials: true,
}))

// Next.js API Routes
export async function GET(request) {
  const origin = request.headers.get('origin')

  return new Response(JSON.stringify({ data }), {
    headers: {
      'Access-Control-Allow-Origin': origin,
      'Access-Control-Allow-Credentials': 'true',
    },
  })
}

// nginx
add_header Access-Control-Allow-Origin $http_origin always;
add_header Access-Control-Allow-Credentials true always;
```

### X-Frame-Options

**Purpose**: Prevent clickjacking

**Values:**
```
X-Frame-Options: DENY              # Never allow framing
X-Frame-Options: SAMEORIGIN        # Only same-origin framing
X-Frame-Options: ALLOW-FROM uri    # Deprecated
```

**Modern Alternative (CSP):**
```
Content-Security-Policy: frame-ancestors 'none'  # DENY
Content-Security-Policy: frame-ancestors 'self'  # SAMEORIGIN
Content-Security-Policy: frame-ancestors https://trusted.com  # Specific origin
```

**When to Use Each:**

- **DENY**: Most sites (default choice)
- **SAMEORIGIN**: If you need to frame your own pages
- **frame-ancestors**: Modern, more flexible than X-Frame-Options

### Permissions-Policy (formerly Feature-Policy)

**Purpose**: Control browser feature access

**Syntax:**
```
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

**Common Features:**

```
camera=(self)                     # Allow camera only on same origin
microphone=()                     # Block microphone entirely
geolocation=(self "https://maps.example.com")  # Allow specific origins
payment=(self)                    # Allow payment API
usb=()                            # Block USB access
magnetometer=()                   # Block sensors
```

**Full List:**
- `camera`, `microphone` - Media capture
- `geolocation` - Location
- `payment` - Payment Request API
- `usb`, `serial`, `bluetooth` - Hardware
- `accelerometer`, `gyroscope`, `magnetometer` - Sensors
- `fullscreen` - Fullscreen API
- `picture-in-picture` - PiP mode

## Framework-Specific Best Practices

### Next.js Production Setup

```javascript
// next.config.js
const isDev = process.env.NODE_ENV !== 'production'

// CSP nonce for Next.js
const ContentSecurityPolicy = `
  default-src 'self';
  script-src 'self'${isDev ? " 'unsafe-eval'" : ''};
  style-src 'self' 'unsafe-inline';
  img-src 'self' blob: data: https:;
  font-src 'self' data:;
  connect-src 'self' https://api.example.com;
  frame-src 'self' https://www.youtube.com;
  media-src 'self';
  object-src 'none';
  base-uri 'self';
  form-action 'self';
  frame-ancestors 'none';
  ${isDev ? '' : 'upgrade-insecure-requests;'}
`

module.exports = {
  async headers() {
    return [{
      source: '/:path*',
      headers: [
        {
          key: 'Content-Security-Policy',
          value: ContentSecurityPolicy.replace(/\s{2,}/g, ' ').trim()
        },
        {
          key: 'X-DNS-Prefetch-Control',
          value: 'on'
        },
        {
          key: 'Strict-Transport-Security',
          value: 'max-age=63072000; includeSubDomains; preload'
        },
        {
          key: 'X-Frame-Options',
          value: 'SAMEORIGIN'
        },
        {
          key: 'X-Content-Type-Options',
          value: 'nosniff'
        },
        {
          key: 'Referrer-Policy',
          value: 'strict-origin-when-cross-origin'
        },
        {
          key: 'Permissions-Policy',
          value: 'camera=(), microphone=(), geolocation=()'
        }
      ],
    }]
  },
}
```

### Express Production Setup

```javascript
const express = require('express')
const helmet = require('helmet')
const cors = require('cors')
const rateLimit = require('express-rate-limit')

const app = express()

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per windowMs
  standardHeaders: true,
  legacyHeaders: false,
})

app.use(limiter)

// Helmet for security headers
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'"],
      styleSrc: ["'self'"],
      imgSrc: ["'self'", "data:", "https:"],
      fontSrc: ["'self'", "data:"],
      connectSrc: ["'self'"],
      frameSrc: ["'none'"],
      objectSrc: ["'none'"],
      upgradeInsecureRequests: [],
    },
  },
  hsts: {
    maxAge: 63072000,
    includeSubDomains: true,
    preload: true,
  },
}))

// CORS
const allowedOrigins = process.env.ALLOWED_ORIGINS?.split(',') || []

app.use(cors({
  origin: function(origin, callback) {
    if (!origin) return callback(null, true) // Allow non-browser requests
    if (allowedOrigins.includes(origin)) {
      callback(null, true)
    } else {
      callback(new Error('Not allowed by CORS'))
    }
  },
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  exposedHeaders: ['X-Total-Count'],
  maxAge: 3600,
}))

// API routes
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok' })
})

// Error handler
app.use((err, req, res, next) => {
  if (err.message === 'Not allowed by CORS') {
    res.status(403).json({ error: 'CORS not allowed' })
  } else {
    res.status(500).json({ error: 'Internal server error' })
  }
})

const PORT = process.env.PORT || 3000
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`)
})
```

## Testing Security Headers

### Automated Testing

```javascript
// test/security-headers.test.js
const request = require('supertest')
const app = require('../app')

describe('Security Headers', () => {
  it('should have HSTS header', async () => {
    const res = await request(app).get('/')
    expect(res.headers['strict-transport-security']).toBeDefined()
    expect(res.headers['strict-transport-security']).toContain('max-age')
  })

  it('should have CSP header', async () => {
    const res = await request(app).get('/')
    expect(res.headers['content-security-policy']).toBeDefined()
  })

  it('should have X-Frame-Options', async () => {
    const res = await request(app).get('/')
    expect(res.headers['x-frame-options']).toBe('SAMEORIGIN')
  })

  it('should have X-Content-Type-Options', async () => {
    const res = await request(app).get('/')
    expect(res.headers['x-content-type-options']).toBe('nosniff')
  })

  it('should allow CORS from allowed origin', async () => {
    const res = await request(app)
      .get('/api/data')
      .set('Origin', 'https://app.example.com')

    expect(res.headers['access-control-allow-origin']).toBe('https://app.example.com')
  })

  it('should block CORS from disallowed origin', async () => {
    const res = await request(app)
      .get('/api/data')
      .set('Origin', 'https://evil.com')

    expect(res.status).toBe(403)
  })
})
```

### Manual Testing

```bash
# Test all headers
curl -I https://your-domain.com

# Test specific header
curl -I https://your-domain.com | grep -i strict-transport-security

# Test CORS
curl -H "Origin: https://app.example.com" \
     -H "Access-Control-Request-Method: POST" \
     -X OPTIONS \
     https://api.example.com/endpoint

# Test CSP
curl -I https://your-domain.com | grep -i content-security-policy
```

### Online Security Scanners

1. **Security Headers**: https://securityheaders.com/
   - Grades: A+ to F
   - Checks all major headers
   - Provides recommendations

2. **Mozilla Observatory**: https://observatory.mozilla.org/
   - Comprehensive security scan
   - Grades: A+ to F
   - Tests CSP, HSTS, cookies, etc.

3. **SSL Labs**: https://www.ssllabs.com/ssltest/
   - SSL/TLS configuration
   - Certificate validation
   - Protocol support

## Common Issues and Solutions

### Issue 1: CSP Blocking Resources

**Problem:** Images/scripts not loading after CSP implementation

**Debug:**
```javascript
// Check browser console for CSP violations
// Look for messages like:
// "Refused to load script from 'https://cdn.example.com/script.js' because it violates CSP directive"
```

**Solution:**
```javascript
// Add the blocked source to CSP
Content-Security-Policy: script-src 'self' https://cdn.example.com
```

### Issue 2: CORS Preflight Failing

**Problem:** OPTIONS requests returning 405 or no CORS headers

**Debug:**
```bash
curl -X OPTIONS \
     -H "Origin: https://app.example.com" \
     -H "Access-Control-Request-Method: POST" \
     http://localhost:3000/api/endpoint -v
```

**Solution:**
```javascript
// Ensure OPTIONS method is handled
app.options('*', cors()) // Enable pre-flight for all routes

// Or per-route
app.options('/api/endpoint', cors())
app.post('/api/endpoint', cors(), handler)
```

### Issue 3: HSTS Breaking Development

**Problem:** Can't access http://localhost after setting HSTS

**Solution:**
```javascript
// Only set HSTS in production
if (process.env.NODE_ENV === 'production') {
  app.use(helmet.hsts({
    maxAge: 63072000,
    includeSubDomains: true,
  }))
}

// Clear HSTS in browser:
// Chrome: chrome://net-internals/#hsts
// Type "localhost" and click "Delete"
```

### Issue 4: Third-Party Scripts Blocked

**Problem:** Google Analytics, ads, etc. blocked by CSP

**Solution:**
```javascript
// Add third-party domains to CSP
Content-Security-Policy:
  script-src 'self' https://www.google-analytics.com https://www.googletagmanager.com;
  img-src 'self' data: https://www.google-analytics.com;
  connect-src 'self' https://www.google-analytics.com;
```

## Production Deployment Checklist

Before deploying security headers:

- [ ] Test on staging environment
- [ ] Check all pages load correctly
- [ ] Verify third-party integrations work
- [ ] Test CORS from allowed origins
- [ ] Monitor CSP violations (report-only first)
- [ ] Verify mobile app compatibility (if applicable)
- [ ] Test on multiple browsers
- [ ] Check subdomains affected by HSTS
- [ ] Backup config before changes
- [ ] Document all header decisions
- [ ] Set up monitoring for CSP violations
- [ ] Plan rollback procedure
- [ ] Gradually increase HSTS max-age
- [ ] Test with security scanners
- [ ] Review CORS configuration carefully

## Resources

### Learning
- [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
- [MDN: HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
- [CSP Evaluator](https://csp-evaluator.withgoogle.com/)

### Tools
- [Helmet.js](https://helmetjs.github.io/) - Express security middleware
- [Talisman](https://github.com/GoogleCloudPlatform/flask-talisman) - Flask security
- [django-csp](https://django-csp.readthedocs.io/) - Django CSP

### Testing
- [Security Headers](https://securityheaders.com/)
- [Mozilla Observatory](https://observatory.mozilla.org/)
- [HSTS Preload](https://hstspreload.org/)

## Files

- `SKILL.md` - The skill file (copy to `.claude/skills/`)
- `README.md` - This comprehensive documentation

## Related Skills

- **dependency-vulnerability-scanner** - Check for vulnerable packages
- **pii-detector** - Find sensitive data in code
- **cors-configurator** - Advanced CORS setup
- **ssl-certificate-manager** - SSL/TLS management

---

**Secure your application today! Your users' data depends on it.** 🔒
