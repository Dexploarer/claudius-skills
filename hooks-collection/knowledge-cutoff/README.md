# Knowledge Cutoff Awareness Hooks

> **Prevent outdated assumptions. Verify before implementing.**

## 🎯 Purpose

These hooks ensure Claude Code always verifies its assumptions about packages, APIs, types, and frameworks before implementation. AI models have knowledge cutoffs, and information about:

- Package versions and APIs
- Framework features and patterns
- Type definitions and interfaces
- Third-party service endpoints
- Security best practices

...can change rapidly AFTER the model's training cutoff date.

**These hooks prevent bugs, security issues, and wasted debugging time by prompting verification BEFORE code is written.**

---

## 📦 Available Hooks

### 1. package-installation-verification
**File:** `package-installation-verification.json`
**Type:** `user-prompt-submit`
**Triggers on:** npm install, pip install, yarn add, etc.

**Purpose:** Verifies package versions and APIs before installation

**Checks:**
- Current package version
- Recent breaking changes
- API compatibility
- Security advisories

**Example trigger:**
```bash
npm install react
```

**Hook reminder:**
```
⚠️ KNOWLEDGE CUTOFF REMINDER:
Before installing packages, you MUST:
1. Check the current version: npm view react version
2. Review the changelog: npm view react readme
3. Verify the API hasn't changed since your cutoff
4. Check for breaking changes in recent versions
5. Look for security advisories
```

---

### 2. import-usage-verification
**File:** `import-usage-verification.json`
**Type:** `user-prompt-submit`
**Triggers on:** import statements, from/require, framework usage

**Purpose:** Reminds to verify import/export structure before writing code

**Checks:**
- Package export structure is current
- Imports still exist
- No renamed or deprecated exports
- TypeScript types are available

**Example trigger:**
```typescript
import { useState } from 'react';
```

**Hook reminder:**
```
⚠️ IMPORT/EXPORT VERIFICATION REQUIRED:
Before writing import statements:
1. Verify the package's current export structure
2. Check if the imports you're suggesting still exist
3. Look for renamed or deprecated exports
4. Verify TypeScript types if using @types packages
```

---

### 3. api-endpoint-verification
**File:** `api-endpoint-verification.json`
**Type:** `user-prompt-submit`
**Triggers on:** API calls, fetch, axios, third-party services

**Purpose:** Ensures API endpoints are verified before use

**High-priority services:**
- Payment APIs (Stripe, PayPal, Square)
- Authentication (Auth0, OAuth, Okta)
- Cloud SDKs (AWS, GCP, Azure)
- Communication (Twilio, SendGrid)

**Example trigger:**
```typescript
fetch('https://api.stripe.com/v1/charges', ...)
```

**Hook reminder:**
```
⚠️ API ENDPOINT VERIFICATION CRITICAL:
Third-party APIs change FREQUENTLY. Before using any API:
1. STOP and verify the current API documentation
2. Check if the endpoint structure has changed
3. Verify authentication methods are still valid
4. Look for API version updates
5. Check for deprecation notices

ESPECIALLY CRITICAL FOR:
- Payment APIs - errors = lost revenue
- Authentication - errors = security risks
- Cloud SDKs - errors = deployment failures
```

---

### 4. framework-feature-verification
**File:** `framework-feature-verification.json`
**Type:** `user-prompt-submit`
**Triggers on:** Framework-specific features and patterns

**Purpose:** Verifies framework features before implementation

**Frameworks tracked:**
- React (18.x → 19.x changes)
- Next.js (13.x → 14.x → 15.x changes)
- Vue (3.x updates)
- Angular (15.x → 16.x → 17.x changes)
- Django (4.x → 5.x changes)
- TypeScript (4.x → 5.x changes)

**Example trigger:**
```typescript
"use client"  // Next.js App Router
```

**Hook reminder:**
```
⚠️ FRAMEWORK FEATURE VERIFICATION:
Frameworks evolve RAPIDLY with breaking changes.
Before using framework features:

1. Ask the user for their framework version
2. Check for breaking changes since your cutoff
3. Verify current best practices
4. Look for deprecation warnings

Ask before implementing:
"I'm going to implement [feature] using [framework].
Since my knowledge cutoff is [date], should I verify
the current best practices for your version first?"
```

---

### 5. type-definition-verification
**File:** `type-definition-verification.json`
**Type:** `user-prompt-submit`
**Triggers on:** TypeScript types, @types packages, interfaces

**Purpose:** Verifies TypeScript type definitions before use

**Checks:**
- @types packages still needed (many packages now have built-in types)
- @types version matches main package
- TypeScript version compatibility
- New syntax features availability

**Example trigger:**
```typescript
import type { ReactNode } from 'react';
```

**Hook reminder:**
```
⚠️ TYPE DEFINITION VERIFICATION:
TypeScript and type definitions evolve rapidly.
Before using types:

1. Check if @types packages are still needed
2. Verify @types package versions match the main package
3. Check for TypeScript version compatibility
4. Look for type definition changes

Common issues:
- Using @types when package has built-in types
- Mismatched @types and package versions
- Using syntax from newer TS than project supports
```

---

## 🚀 Installation

### Option 1: Install All Knowledge Cutoff Hooks

```bash
# Copy the entire knowledge-cutoff directory to your project
cp -r hooks-collection/knowledge-cutoff /path/to/your/project/.claude/hooks/

# Or create symlinks
ln -s $(pwd)/hooks-collection/knowledge-cutoff /path/to/your/project/.claude/hooks/
```

### Option 2: Install Individual Hooks

```bash
# Copy specific hooks
cp hooks-collection/knowledge-cutoff/package-installation-verification.json \
   /path/to/your/project/.claude/hooks/

cp hooks-collection/knowledge-cutoff/api-endpoint-verification.json \
   /path/to/your/project/.claude/hooks/
```

### Option 3: Enable in Existing Project

If you already have a `.claude/hooks/` directory:

```bash
cd /path/to/your/project/.claude/hooks/
cp /path/to/claudius-skills/hooks-collection/knowledge-cutoff/*.json ./
```

---

## ⚙️ Configuration

### Enabling/Disabling Hooks

Each hook has an `enabled` field in its JSON configuration:

```json
{
  "enabled": true  // Set to false to disable
}
```

### Customizing Trigger Patterns

You can customize which patterns trigger each hook by editing the `trigger_patterns` array:

```json
{
  "config": {
    "trigger_patterns": [
      "npm install",
      "yarn add",
      "pnpm add"
      // Add more patterns as needed
    ]
  }
}
```

### Adjusting Prompt Injection

The `prompt_injection` field contains the reminder message. Customize it for your team's needs:

```json
{
  "config": {
    "prompt_injection": "\n\nYour custom reminder message here..."
  }
}
```

---

## 🎯 Use Cases

### For Solo Developers
- **Prevent wasted time** debugging outdated package APIs
- **Avoid security issues** from using old authentication patterns
- **Stay current** with framework best practices
- **Learn as you code** by seeing what has changed

### For Teams
- **Standardize verification** across all team members
- **Prevent junior developers** from using outdated patterns
- **Reduce code review overhead** by catching issues early
- **Document version requirements** automatically

### For Enterprise Projects
- **Security compliance** by verifying all dependencies
- **Audit trail** of version checks
- **Risk mitigation** for critical integrations
- **Knowledge sharing** about ecosystem changes

---

## 📊 Impact Metrics

**Without these hooks:**
- ❌ Time wasted debugging "module not found" errors
- ❌ Security vulnerabilities from outdated patterns
- ❌ Production bugs from API changes
- ❌ Type errors from mismatched @types packages

**With these hooks:**
- ✅ Verify before implementing → code works first try
- ✅ No surprises from API changes
- ✅ Security best practices enforced
- ✅ Team stays current with ecosystem

**Time savings:**
- **30 seconds** to verify → saves **hours** of debugging
- **Quick version check** → prevents production incidents
- **Ask user about versions** → ensures compatibility

---

## 🎓 Best Practices

### 1. Enable All Hooks for High-Risk Projects
If your project uses:
- Payment processing
- Authentication systems
- Cloud infrastructure
- Financial transactions
- Healthcare data

**→ Enable ALL knowledge cutoff hooks**

### 2. Customize for Your Tech Stack
Edit trigger patterns to match your specific:
- Package managers
- Frameworks
- APIs
- Build tools

### 3. Educate Your Team
Share the knowledge cutoff concept:
```
"AI models have training cutoffs. Always verify package
versions and APIs before implementing to ensure current
best practices."
```

### 4. Integrate with CI/CD
Use hooks as reminders to:
- Run security scans
- Update dependencies regularly
- Review breaking changes
- Test with latest versions

### 5. Document Version Decisions
When you verify and choose a version:
```typescript
// Verified 2025-11-03: Using Stripe SDK v14.x
// Breaking changes from v12.x documented in CHANGELOG.md
import Stripe from 'stripe';
```

---

## 🔍 Related Resources

### Documentation
- **Knowledge Cutoff Awareness Rules:** `.claude/rules/knowledge-cutoff-awareness.md`
- **Version Checker Skill:** `.claude/skills/version-checker.md`
- **Main Project Guide:** `CLAUDE.md`

### Skills
- **version-checker** - Automated package/API verification
- **dependency-scanner** - Security vulnerability scanning
- **api-documentation-generator** - Generate API docs from current schemas

### Commands
- `/deps` - Dependency management
- `/security-audit` - Security scanning
- `/version-bump` - Version management

---

## 🚨 Critical Reminders

### For Claude Code (AI Assistant)

**Before EVERY implementation involving external dependencies:**

1. ✅ **Acknowledge your knowledge cutoff**
   ```
   "My knowledge cutoff is [date]. Let me verify the current
   state of [package/API] before proceeding."
   ```

2. ✅ **Check current versions**
   ```bash
   npm view <package> version
   npm view <package> dist-tags
   ```

3. ✅ **Verify APIs haven't changed**
   ```bash
   npm view <package> readme
   # Or use WebFetch for official docs
   ```

4. ✅ **Ask user about their versions**
   ```
   "What version of [framework] are you using? This helps
   me ensure compatibility."
   ```

5. ✅ **Review breaking changes**
   ```bash
   npm view <package> versions --json
   # Look for major version bumps
   ```

### High-Risk Scenarios

**IMMEDIATELY verify for:**
- 🔐 Security/authentication packages
- 💳 Payment processing
- ☁️ Cloud SDKs
- ⚛️ Framework core features
- 🗄️ Database ORMs
- 🔨 Build tools
- 🧪 Testing frameworks

**These change FREQUENTLY. Outdated code can cause:**
- Security vulnerabilities
- Payment processing errors
- Deployment failures
- Type errors
- Production incidents

---

## 🎯 The Golden Rule

**"When in doubt, verify. Never assume your knowledge is current."**

**Better to:**
1. ✅ Acknowledge uncertainty
2. ✅ Verify current information
3. ✅ Implement with confidence

**Than to:**
1. ❌ Assume knowledge is current
2. ❌ Implement outdated patterns
3. ❌ Cause bugs and frustration

---

## 📈 Roadmap

**Future enhancements:**
- [ ] Auto-fetch package changelogs
- [ ] Compare versions automatically
- [ ] Suggest migration paths for breaking changes
- [ ] Integration with security advisory databases
- [ ] Team-wide version tracking
- [ ] Dependency update suggestions

---

## 🤝 Contributing

Found a package type or API pattern that should trigger verification?

**Add it to the appropriate hook:**

1. Edit the hook's JSON file
2. Add to `trigger_patterns` array
3. Update the `prompt_injection` if needed
4. Test with real-world usage
5. Submit a PR

**Example contribution:**
```json
{
  "trigger_patterns": [
    "existing patterns...",
    "your new pattern"
  ]
}
```

---

## 📝 License

Part of the Claudius Skills project. See main project LICENSE.

---

**Last Updated:** 2025-11-03
**Category:** Development Safety / Knowledge Verification
**Priority:** CRITICAL - Prevent outdated implementations
**Total Hooks:** 5 hooks covering all major verification scenarios

---

## 💡 Remember

**Users trust you to be accurate.**

Honor that trust by verifying when your knowledge might be stale.

A 30-second verification can save hours of debugging.

**Verify first. Implement second. Ship with confidence.** ✨
