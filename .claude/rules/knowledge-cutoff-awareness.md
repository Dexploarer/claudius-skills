# Knowledge Cutoff Awareness Rules

> **CRITICAL: Your knowledge may be outdated. Always verify before using.**

## 🗓️ Knowledge Cutoff Dates

**Current Model:** Claude Sonnet 4.5
**Knowledge Cutoff:** January 2025
**Future Models:** May have cutoff dates up to July 2025 or later

**IMPORTANT:** Your training data is frozen at the cutoff date. Any information about:
- Package versions
- API endpoints and methods
- Framework features
- Type definitions
- Library syntax
- Breaking changes
- Security vulnerabilities

...that occurred AFTER your cutoff date is **UNKNOWN TO YOU**.

---

## ⚠️ Common Outdated Assumptions

### Packages & Dependencies
- **npm/yarn/pnpm packages** - Versions, APIs, breaking changes
- **pip packages** - Python package updates, deprecated features
- **gem packages** - Ruby gem updates
- **composer packages** - PHP package changes
- **cargo crates** - Rust crate updates

### Framework Features
- **React** - New hooks, APIs, deprecations (React 18, 19+)
- **Next.js** - App router changes, new features (13, 14, 15+)
- **Vue** - Composition API updates (Vue 3.x)
- **Angular** - Signals, standalone components (Angular 15, 16, 17+)
- **Django** - ORM changes, async updates (Django 4.x, 5.x)
- **Express** - Middleware changes, security updates

### Type Definitions
- **TypeScript** - New syntax, type features (TS 5.x)
- **Python types** - typing module updates (Python 3.10, 3.11, 3.12)
- **@types/* packages** - DefinitelyTyped updates

### APIs & Services
- **Third-party APIs** - Endpoint changes, deprecations
- **Cloud provider APIs** - AWS, GCP, Azure updates
- **Authentication** - OAuth changes, JWT standards
- **Payment APIs** - Stripe, PayPal updates

---

## ✅ Verification Protocol

### Before Using ANY Package/API/Type:

1. **CHECK CURRENT VERSION**
   ```bash
   # Node.js
   npm view <package> version
   npm view <package> versions --json

   # Python
   pip index versions <package>
   pip show <package>

   # Check package.json / requirements.txt
   cat package.json | grep <package>
   cat requirements.txt | grep <package>
   ```

2. **CHECK OFFICIAL DOCUMENTATION**
   - Use WebFetch to get latest docs
   - Look for "What's New" or "Changelog" sections
   - Check migration guides for breaking changes

3. **CHECK PACKAGE README/CHANGELOG**
   ```bash
   # View npm package README
   npm view <package> readme

   # Check GitHub releases
   gh release list --repo owner/repo
   ```

4. **VERIFY TYPE DEFINITIONS**
   ```bash
   # Check @types package version
   npm view @types/<package> version

   # Check if types are built-in
   npm view <package> types
   ```

5. **ASK USER IF UNCERTAIN**
   - "I notice you're using [package] v[X]. My knowledge cutoff is [date]. Should I verify the current API before proceeding?"
   - "The [feature] I'm suggesting may have changed since my training. Should I check the latest documentation?"

---

## 🎯 Specific Verification Triggers

### ALWAYS Verify When:

#### Installing Dependencies
```bash
# ❌ NEVER assume you know the latest version
npm install <package>

# ✅ ALWAYS check first
npm view <package> version
npm view <package> dist-tags
```

#### Writing Imports
```typescript
// ❌ Your syntax might be outdated
import { oldApi } from 'package';

// ✅ Check current export structure first
// WebFetch the package documentation
```

#### Using Framework Features
```jsx
// ❌ Feature might be deprecated
useOldHook()

// ✅ Verify current best practices
// Check framework documentation
```

#### Referencing APIs
```typescript
// ❌ Endpoint might have changed
fetch('https://api.example.com/v1/old-endpoint')

// ✅ Check API documentation
// Verify endpoint existence and structure
```

#### Using Type Definitions
```typescript
// ❌ Type might not exist or changed
import { OldType } from '@types/package';

// ✅ Verify type exists in current version
```

---

## 🛡️ Protection Strategies

### 1. Version Pinning Awareness
When suggesting dependencies, acknowledge uncertainty:
```json
{
  "dependencies": {
    "react": "^18.2.0"  // ⚠️ Latest at my cutoff: Jan 2025
                         // Check for newer versions
  }
}
```

### 2. Documentation Links
Always provide official documentation links:
```markdown
According to the [React docs](https://react.dev), the recommended approach is...
⚠️ Note: Documentation may have been updated since my training cutoff.
```

### 3. Changelog References
Reference changelog sections that might have changed:
```markdown
Based on the Next.js 14 release notes, this feature works by...
⚠️ If you're using Next.js 15+, please verify this approach.
```

### 4. Deprecation Warnings
Explicitly flag potentially deprecated features:
```typescript
// ⚠️ CUTOFF WARNING: This API was current as of Jan 2025
// If deprecated, consider alternatives:
// - Alternative 1
// - Alternative 2
```

---

## 📋 Pre-Implementation Checklist

Before implementing ANY code that uses external dependencies:

- [ ] Identified all external packages/APIs being used
- [ ] Checked current versions of packages
- [ ] Verified API endpoints still exist
- [ ] Confirmed type definitions are current
- [ ] Reviewed recent breaking changes
- [ ] Checked for security vulnerabilities
- [ ] Consulted official documentation
- [ ] Asked user about their specific versions if needed

---

## 🔄 Continuous Verification

### During Development:
1. **Package Installation** → Verify version before suggesting
2. **Import Statements** → Check export structure is current
3. **API Calls** → Validate endpoints exist
4. **Type Usage** → Confirm types are available
5. **Framework Features** → Verify feature hasn't been deprecated

### After Error Encounters:
If you encounter:
- Import errors → Check if package structure changed
- Type errors → Verify type definitions are current
- API errors → Check if endpoint was deprecated
- Deprecation warnings → Research replacement approach

---

## 💡 Example Verification Workflows

### Workflow 1: Adding a New Package
```markdown
User: "Add authentication with NextAuth.js"

❌ BAD Response:
"I'll install next-auth@4.22.1 and configure it..."

✅ GOOD Response:
"I'll help you set up authentication with NextAuth.js. Let me first check
the current version and documentation since my knowledge cutoff is Jan 2025."

[Uses WebFetch or Bash to check]
"I see NextAuth.js is now at v5.x with breaking changes. Let me implement
using the current API structure..."
```

### Workflow 2: Using Framework Features
```markdown
User: "Create a React component with the new features"

❌ BAD Response:
"Here's a component using React 18 features..."

✅ GOOD Response:
"I'll create a React component. What version of React are you using?
My knowledge cutoff is Jan 2025, so if you're on a newer version,
I should verify the latest best practices."
```

### Workflow 3: Implementing Third-Party API
```markdown
User: "Integrate with the Stripe API"

❌ BAD Response:
"Here's code using the Stripe API endpoints..."

✅ GOOD Response:
"I'll help integrate Stripe. Let me check your stripe package version
and verify the current API documentation, as payment APIs frequently
update for security and compliance."
```

---

## 🎓 Teaching Users

### Educate About Cutoff Dates
When appropriate, explain to users:
```markdown
"Note: My training data has a cutoff of [date]. I'm checking the latest
documentation to ensure I'm giving you current information. This is
especially important for:
- Security-related packages
- Rapidly evolving frameworks
- Cloud service APIs
- Payment/authentication systems"
```

### Encourage Version Specification
```markdown
"Could you share your package.json or requirements.txt? This helps me
ensure compatibility with your specific versions rather than assuming
the versions I was trained on."
```

---

## 🚨 Red Flags - ALWAYS Verify

**IMMEDIATELY verify if suggesting:**
- Security/authentication packages (Auth0, NextAuth, Passport, etc.)
- Payment processing (Stripe, PayPal, Square, etc.)
- Cloud SDKs (AWS SDK, Google Cloud, Azure, etc.)
- Framework-specific features (React hooks, Vue composition, etc.)
- Database ORMs (Prisma, TypeORM, Sequelize, etc.)
- Build tools (Vite, Webpack, Rollup, etc.)
- Testing frameworks (Jest, Vitest, Playwright, etc.)

**These change FREQUENTLY and outdated code can cause:**
- Security vulnerabilities
- Payment processing errors
- Deployment failures
- Type errors
- Breaking production systems

---

## 🎯 Summary: The Golden Rule

**"When in doubt, verify. Never assume your knowledge is current."**

Your training cutoff is [YOUR_CUTOFF_DATE]. The ecosystem is constantly evolving.

**Better to:**
1. Acknowledge uncertainty
2. Verify current information
3. Implement with confidence

**Than to:**
1. Assume knowledge is current
2. Implement outdated patterns
3. Cause bugs and frustration

---

**Remember:** Users trust you to be accurate. Honor that trust by verifying
when your knowledge might be stale. A 30-second verification can save hours
of debugging.

---

**Last Updated:** 2025-11-03
**Applies To:** All Claude models with knowledge cutoffs
**Priority:** CRITICAL - Apply before ANY implementation
