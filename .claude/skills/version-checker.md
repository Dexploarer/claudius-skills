# version-checker

**Skill Name:** Version Checker & API Verifier

**Description:** Automatically verifies current package versions, API compatibility, and breaking changes to ensure knowledge cutoff assumptions are accurate before implementation.

**Category:** Development Tools / Knowledge Verification

**Complexity:** Intermediate

**Use Cases:**
- Verify package versions before installation
- Check for breaking changes since knowledge cutoff
- Validate API endpoint compatibility
- Confirm TypeScript type definitions are current
- Review framework feature compatibility

---

## 🎯 Activation Triggers

This skill activates when the user mentions:
- "check version of [package]"
- "verify [package] is up to date"
- "what's the latest version of [package]"
- "check if [API] has changed"
- "verify [framework] compatibility"
- "is this package syntax still valid"
- "check for breaking changes in [package]"

---

## 🔍 Verification Protocol

### 1. Package Version Checking

**For Node.js packages:**
```bash
# Check current published version
npm view <package> version

# Check all available versions
npm view <package> versions --json

# Check dist-tags (latest, next, beta, etc.)
npm view <package> dist-tags

# View package README and changelog
npm view <package> readme

# Check package metadata
npm view <package> --json
```

**For Python packages:**
```bash
# Check latest version
pip index versions <package>

# Show installed version
pip show <package>

# Check on PyPI (via WebFetch)
# https://pypi.org/pypi/<package>/json
```

**For other package managers:**
```bash
# Bundler (Ruby)
gem list <package> --remote

# Composer (PHP)
composer show <package> --all

# Cargo (Rust)
cargo search <package>
```

### 2. API Compatibility Verification

**Steps:**
1. **Identify the package/API being used**
2. **Check the current version**
3. **Review recent changelog/release notes**
4. **Look for BREAKING CHANGES sections**
5. **Verify the specific API methods/exports still exist**

**Using WebFetch to verify:**
```bash
# Fetch official documentation
WebFetch(url="https://package-docs.com/api-reference",
         prompt="What are the current API methods and have there been breaking changes?")

# Check GitHub releases
WebFetch(url="https://github.com/owner/repo/releases",
         prompt="What are the latest releases and breaking changes?")
```

### 3. Framework Feature Verification

**Ask the user for their version:**
```
"What version of [framework] are you using? This helps me ensure
compatibility with your setup."
```

**Then check for breaking changes:**
```bash
# For React
npm view react version
npm view react-dom version

# For Next.js
npm view next version

# Check their package.json
cat package.json | grep -E "(react|next|vue|angular)"
```

### 4. Type Definition Verification

**Check if types are built-in or need @types:**
```bash
# Check if package includes types
npm view <package> types

# If it returns a path, types are built-in
# If it returns nothing, check for @types

# Check @types package
npm view @types/<package> version
```

### 5. Breaking Changes Review

**Key areas to check:**
- **Major version bumps** (v1.x → v2.x → v3.x)
- **Deprecation warnings**
- **API method changes** (renamed, removed, signature changes)
- **Import/export structure changes**
- **Type definition updates**
- **Configuration changes**

---

## 📋 Verification Checklist

Before implementing code with external dependencies:

- [ ] **Package version confirmed** - Not assuming from training data
- [ ] **Changelog reviewed** - Checked for breaking changes since cutoff
- [ ] **API structure verified** - Confirmed exports/methods still exist
- [ ] **Type definitions checked** - Verified @types or built-in types
- [ ] **Framework version compatible** - Matches user's setup
- [ ] **Security advisories reviewed** - No known vulnerabilities
- [ ] **Documentation consulted** - Official docs referenced
- [ ] **User's version confirmed** - Asked if needed for accuracy

---

## 🎯 Skill Execution Steps

### Step 1: Acknowledge Knowledge Cutoff
```
"I'll help you with [task]. My knowledge cutoff is January 2025,
so I'll verify the current state of [package/API] before proceeding."
```

### Step 2: Check Current Versions
```bash
# Run appropriate version check commands
npm view <package> version
npm view <package> dist-tags
```

### Step 3: Review Documentation
```bash
# Fetch current documentation
WebFetch(url="https://official-docs.com",
         prompt="What are the current API methods and best practices?")
```

### Step 4: Check User's Setup (if needed)
```
"Could you share your package.json or let me know which version
of [framework] you're using? This ensures I provide compatible code."
```

### Step 5: Identify Breaking Changes
```bash
# Check changelog
npm view <package> readme

# Or fetch GitHub releases
WebFetch(url="https://github.com/owner/repo/releases",
         prompt="List breaking changes in recent versions")
```

### Step 6: Report Findings
```
"I've verified the current state:
- Latest version: X.Y.Z (up from A.B.C at my cutoff)
- Breaking changes: [list if any]
- API compatibility: [status]
- Recommended approach: [based on current version]"
```

### Step 7: Implement with Current Best Practices
```
"Based on the current version, here's the updated implementation..."
```

---

## 💡 Example Workflows

### Example 1: Verifying React Hook Usage

**User:** "Create a component using React hooks"

**Skill Response:**
```
"I'll create a React component with hooks. Let me first verify your React version
and current best practices, since my knowledge cutoff is January 2025."

[Checks package.json or asks user]
[Verifies React version]

"I see you're using React 19.x. Let me check for any new hooks or deprecations..."

[Uses WebFetch to check React docs if needed]

"Based on React 19.x, here's the component using current best practices..."
```

### Example 2: Verifying API Package

**User:** "Add Stripe payment integration"

**Skill Response:**
```
"I'll help set up Stripe integration. Since payment APIs frequently update,
let me verify the current Stripe SDK version and API structure."

[Runs: npm view stripe version]
[Checks: npm view stripe readme]

"The current Stripe SDK is v14.x (up from v12.x at my cutoff).
Let me check the documentation for any breaking changes..."

[Uses WebFetch to check Stripe docs]

"I found that the API structure changed in v13. Here's the current
recommended implementation for your version..."
```

### Example 3: Verifying TypeScript Types

**User:** "Add type definitions for this API"

**Skill Response:**
```
"I'll add TypeScript types. Let me first verify:
1. Your TypeScript version
2. Whether the package has built-in types
3. Current @types package version if needed"

[Checks: cat package.json | grep typescript]
[Checks: npm view <package> types]

"The package now includes built-in types (as of v3.0), so you don't
need @types/<package> anymore. Here are the current type definitions..."
```

---

## 🚨 Critical Use Cases

**ALWAYS use this skill for:**

1. **Security/Authentication Packages**
   - Auth0, NextAuth, Passport, OAuth libraries
   - Changes can introduce security vulnerabilities

2. **Payment Processing**
   - Stripe, PayPal, Square, payment gateways
   - Errors can cause financial losses

3. **Cloud SDKs**
   - AWS SDK, Google Cloud, Azure SDKs
   - Breaking changes common, deployment failures costly

4. **Framework Core Features**
   - React hooks, Vue composition, Angular signals
   - Rapid evolution, frequent breaking changes

5. **Database ORMs**
   - Prisma, TypeORM, Sequelize, Django ORM
   - Schema/query syntax changes can break applications

6. **Build Tools**
   - Vite, Webpack, Rollup, esbuild
   - Configuration changes common

7. **Testing Frameworks**
   - Jest, Vitest, Playwright, Cypress
   - API updates frequent

---

## ⚙️ Configuration Options

**Verification Depth Levels:**

**Quick Check (default):**
- Check current version
- Review dist-tags
- Quick changelog scan

**Standard Check:**
- All quick check items
- Review breaking changes
- Verify specific APIs being used
- Check security advisories

**Deep Check:**
- All standard check items
- Full changelog review
- Documentation verification
- Alternative package comparison
- Migration guide review

**User can specify:**
```
"Do a deep verification of the Stripe API before implementing"
```

---

## 📚 Knowledge Cutoff Dates Reference

**Model Knowledge Cutoffs:**
- Claude Sonnet 4.5: January 2025
- Future models: Up to July 2025 or later

**High-Change Areas (verify more frequently):**
- React ecosystem (hooks, patterns, tools)
- Next.js (app router, server components)
- TypeScript (new syntax features)
- Payment APIs (compliance, security updates)
- Cloud provider SDKs (service updates)
- Authentication systems (security patches)

---

## 🎓 Educational Component

**Teach users about knowledge cutoffs:**
```
"Note: AI models have training data cutoffs. My cutoff is [date], which means
information about packages, APIs, and frameworks from after that date is unknown
to me without verification. That's why I'm checking the current state before
implementing - to ensure you get accurate, up-to-date code."
```

**Encourage version specification:**
```
"Tip: Including your package.json or requirements.txt helps me provide code
that's compatible with your specific versions rather than assuming versions
from my training data."
```

---

## 🔄 Integration with Other Skills

**Works well with:**
- `api-documentation-generator` - After verifying API structure
- `test-helper` - Ensures tests use current API patterns
- `security-header-generator` - Verifies security best practices
- `dependency-scanner` - Checks for vulnerabilities

**Triggers from:**
- Before any package installation suggestions
- Before implementing external API integrations
- Before using framework-specific features
- Before writing import statements

---

## 📊 Success Metrics

**This skill is successful when:**
- ✅ No "module not found" errors from outdated imports
- ✅ No "method does not exist" errors from changed APIs
- ✅ No type errors from outdated @types packages
- ✅ No security vulnerabilities from old package versions
- ✅ User doesn't need to correct Claude's assumptions
- ✅ Code works on first try with current package versions

---

## 🎯 Key Reminders

**Before EVERY implementation:**
1. Acknowledge your knowledge cutoff date
2. Verify you're not assuming outdated information
3. Check current versions and APIs
4. Consult official documentation when uncertain
5. Ask the user about their specific versions if needed

**Red flags requiring verification:**
- Major version number in your training data (v1, v2, v3, etc.)
- Beta/alpha packages (high change rate)
- Recently released features (may have evolved)
- Security-critical packages (frequent updates)
- Cloud/payment services (compliance-driven changes)

---

## 💪 The Golden Rule

**"Verify first, implement second."**

Better to spend 30 seconds verifying than cause hours of debugging
from outdated assumptions.

Your users trust you to be accurate. Honor that trust by checking
when your knowledge might be stale.

---

**Last Updated:** 2025-11-03
**Priority:** CRITICAL - Use before implementing ANY external dependencies
**See Also:** `.claude/rules/knowledge-cutoff-awareness.md`
