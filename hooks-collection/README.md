# Comprehensive Hooks Collection

> Production-ready hooks for Claude Code automation across development, deployment, quality, and security

---

## 📚 Overview

This collection contains **30 production-ready hooks** organized into 6 categories:

1. **Development Safety** (5 hooks) - Prevent common mistakes
2. **Production Deployment** (5 hooks) - Ensure safe deployments
3. **Code Quality** (5 hooks) - Maintain high code standards
4. **Security Enforcement** (5 hooks) - Enforce security best practices
5. **Performance Monitoring** (5 hooks) - Monitor and optimize performance
6. **Knowledge Cutoff Awareness** (5 hooks) 🆕 - Verify assumptions before implementation

---

## 🚀 Quick Start

### Install All Hooks

```bash
# Copy entire hooks collection to your project
cp -r hooks-collection/.claude/hooks /path/to/your/project/.claude/

# Or copy specific category
cp hooks-collection/development-safety/*.json /path/to/your/project/.claude/hooks/
```

### Install Individual Hook

```bash
# Copy single hook
cp hooks-collection/development-safety/prevent-force-push.json \
   /path/to/your/project/.claude/hooks/
```

### Enable/Disable Hooks

Edit the hook JSON file and change:
```json
{
  "enabled": true  // Set to false to disable
}
```

---

## 📁 Hooks by Category

### 🛡️ Development Safety Hooks

Prevent common development mistakes and accidents.

| Hook | Purpose | Event | Critical |
|------|---------|-------|----------|
| `prevent-force-push` | Blocks force pushes to protected branches | pre-submit | ⚠️ Yes |
| `env-file-protection` | Prevents committing .env and credential files | pre-submit | ⚠️ Yes |
| `large-file-warning` | Warns about large files (suggests Git LFS) | pre-submit | No |
| `destructive-operation-confirm` | Confirms before rm -rf, DROP TABLE, etc. | pre-submit | ⚠️ Yes |
| `package-install-check` | Validates package installations (typos, deprecation) | pre-submit | No |

**Install Development Safety:**
```bash
cp hooks-collection/development-safety/*.json /path/to/project/.claude/hooks/
```

---

### 🚀 Production Deployment Hooks

Ensure safe and reliable production deployments.

| Hook | Purpose | Event | Critical |
|------|---------|-------|----------|
| `pre-deploy-checklist` | Enforces deployment checklist | pre-submit | ⚠️ Yes |
| `database-migration-safety` | Ensures safe DB migrations with backups | pre-submit | ⚠️ Yes |
| `deployment-notification` | Notifies team after deployments | post-submit | No |
| `blue-green-validation` | Validates traffic switching | pre-submit | ⚠️ Yes |
| `feature-flag-deployment` | Encourages feature flag usage | pre-submit | No |

**Install Deployment Hooks:**
```bash
cp hooks-collection/production-deployment/*.json /path/to/project/.claude/hooks/
```

---

### ✅ Code Quality Hooks

Maintain high code quality standards.

| Hook | Purpose | Event | Critical |
|------|---------|-------|----------|
| `test-coverage-enforcement` | Enforces minimum test coverage | pre-submit | No |
| `linting-enforcement` | Blocks commits with lint errors | pre-submit | No |
| `commit-message-standards` | Enforces conventional commits | pre-submit | No |
| `documentation-check` | Ensures code has documentation | pre-submit | No |
| `code-complexity-warning` | Warns about high cyclomatic complexity | pre-submit | No |

**Install Quality Hooks:**
```bash
cp hooks-collection/code-quality/*.json /path/to/project/.claude/hooks/
```

---

### 🔒 Security Enforcement Hooks

Enforce security best practices automatically.

| Hook | Purpose | Event | Critical |
|------|---------|-------|----------|
| `secret-scanning` | Scans for API keys and secrets | pre-submit | ⚠️ Yes |
| `dependency-vulnerability-scan` | Checks for vulnerable dependencies | pre-submit | ⚠️ Yes |
| `security-headers-check` | Validates security headers config | pre-submit | ⚠️ Yes |
| `license-compliance-check` | Checks for incompatible licenses | pre-submit | No |
| `cors-configuration-check` | Validates CORS settings | pre-submit | ⚠️ Yes |

**Install Security Hooks:**
```bash
cp hooks-collection/security-enforcement/*.json /path/to/project/.claude/hooks/
```

---

### ⚡ Performance Monitoring Hooks

Monitor and optimize application performance.

| Hook | Purpose | Event | Critical |
|------|---------|-------|----------|
| `build-size-alert` | Monitors bundle size increases | pre-submit | No |
| `ci-time-tracking` | Tracks CI/CD pipeline duration | post-submit | No |
| `memory-leak-warning` | Detects potential memory leaks | pre-submit | No |
| `n-plus-one-query-detection` | Identifies N+1 query patterns | pre-submit | ⚠️ Yes |
| `slow-test-detection` | Flags slow test execution | post-submit | No |

**Install Performance Hooks:**
```bash
cp hooks-collection/performance-monitoring/*.json /path/to/project/.claude/hooks/
```

---

### 🧠 Knowledge Cutoff Awareness Hooks 🆕

**NEW!** Prevent outdated assumptions by verifying package versions, APIs, and frameworks before implementation.

AI models have knowledge cutoffs. These hooks ensure Claude Code always verifies its assumptions about:
- Package versions and APIs
- Framework features and patterns
- Type definitions
- Third-party service endpoints

| Hook | Purpose | Event | Critical |
|------|---------|-------|----------|
| `package-installation-verification` | Verifies package versions before installation | pre-submit | ⚠️ Yes |
| `import-usage-verification` | Checks import/export structure before writing code | pre-submit | ⚠️ Yes |
| `api-endpoint-verification` | Validates API endpoints before use | pre-submit | ⚠️ Yes |
| `framework-feature-verification` | Confirms framework features before implementation | pre-submit | ⚠️ Yes |
| `type-definition-verification` | Verifies TypeScript types before use | pre-submit | ⚠️ Yes |

**Why these hooks matter:**
- ✅ Prevent "module not found" errors from outdated imports
- ✅ Avoid security issues from old authentication patterns
- ✅ Ensure compatibility with current package versions
- ✅ Save hours of debugging from outdated assumptions

**High-risk scenarios these hooks protect against:**
- 💳 Payment APIs (Stripe, PayPal) - Outdated code = lost revenue
- 🔐 Authentication (Auth0, OAuth) - Outdated code = security risks
- ☁️ Cloud SDKs (AWS, GCP, Azure) - Outdated code = deployment failures
- ⚛️ Frameworks (React, Next.js, Vue) - Rapid evolution, frequent breaking changes

**Install Knowledge Cutoff Hooks:**
```bash
cp hooks-collection/knowledge-cutoff/*.json /path/to/project/.claude/hooks/
```

**See full documentation:**
```bash
cat hooks-collection/knowledge-cutoff/README.md
```

**Related resources:**
- Rule file: `.claude/rules/knowledge-cutoff-awareness.md`
- Skill: `.claude/skills/version-checker.md`

---

## 🎯 Hook Configuration

### Hook Structure

```json
{
  "name": "hook-name",
  "event": "user-prompt-submit",
  "description": "What this hook does",
  "enabled": true,
  "prompt": "Instructions for Claude..."
}
```

### Available Events

- `user-prompt-submit` - Before executing user commands
- `post-tool-use` - After tool execution completes

### Customization

You can customize any hook by editing its JSON file:

1. **Change thresholds**:
```json
// In test-coverage-enforcement.json
"Statements: >= 80%"  // Change to your threshold
```

2. **Adjust severity**:
```json
// In large-file-warning.json
"Warning: Files > 10MB"  // Adjust size limits
```

3. **Modify patterns**:
```json
// In secret-scanning.json
Add your organization's secret patterns
```

---

## 💡 Usage Examples

### Example 1: Prevent Force Push

```bash
# This will be blocked
git push --force origin main

# Hook shows:
🚫 FORCE PUSH BLOCKED
You're attempting to force push to main branch.
[Detailed explanation and alternatives]

# Recommended instead
git push origin feature/my-branch
```

### Example 2: Secret Detection

```bash
# If you try to commit with secrets
git add config.js

# Hook detects:
🔐 SECRET DETECTED!
File: config.js
Type: AWS_ACCESS_KEY
[Instructions to fix]
```

### Example 3: Deployment Checklist

```bash
# Before production deployment
kubectl apply -f prod-deployment.yaml

# Hook enforces checklist:
🚀 PRODUCTION DEPLOYMENT
📋 PRE-DEPLOYMENT CHECKLIST
[Comprehensive checklist to verify]
```

---

## 🔧 Advanced Configuration

### Combining Hooks

You can use multiple hooks together for comprehensive protection:

```bash
# Essential security stack
cp hooks-collection/development-safety/prevent-force-push.json .claude/hooks/
cp hooks-collection/development-safety/env-file-protection.json .claude/hooks/
cp hooks-collection/security-enforcement/secret-scanning.json .claude/hooks/
cp hooks-collection/security-enforcement/dependency-vulnerability-scan.json .claude/hooks/
```

### Environment-Specific Hooks

Create different hook sets for different environments:

```bash
# Development environment
.claude/hooks/
  ├── linting-enforcement.json
  ├── test-coverage-enforcement.json
  └── documentation-check.json

# Production environment
.claude/hooks/
  ├── pre-deploy-checklist.json
  ├── database-migration-safety.json
  ├── secret-scanning.json
  └── security-headers-check.json
```

### Team Configuration

Share hooks with your team:

```bash
# Add hooks to version control
git add .claude/hooks/
git commit -m "Add Claude Code hooks for team"
git push

# Team members pull and use
git pull
# Hooks are now active for everyone
```

---

## 🎓 Best Practices

### 1. Start with Critical Hooks

Begin with hooks that prevent critical issues:

```bash
# Priority 1: Security
cp hooks-collection/security-enforcement/secret-scanning.json .claude/hooks/
cp hooks-collection/development-safety/env-file-protection.json .claude/hooks/

# Priority 2: Safety
cp hooks-collection/development-safety/prevent-force-push.json .claude/hooks/
cp hooks-collection/production-deployment/pre-deploy-checklist.json .claude/hooks/
```

### 2. Gradually Add More

Don't overwhelm your team. Add hooks incrementally:

- Week 1: Critical security hooks
- Week 2: Development safety
- Week 3: Code quality
- Week 4: Full deployment suite

### 3. Customize for Your Workflow

Modify hooks to match your team's processes:

- Adjust coverage thresholds
- Modify commit message formats
- Update deployment checklists
- Add organization-specific patterns

### 4. Document Exceptions

When hooks are bypassed, document why:

```bash
# In project README or docs
## Hook Exceptions
- `env-file-protection` disabled for config/public-keys.env (contains public keys only)
- `test-coverage-enforcement` threshold lowered to 70% during migration phase
```

### 5. Monitor Hook Effectiveness

Track how hooks help your team:

- How many secrets prevented from commit?
- How many force pushes blocked?
- How many vulnerable dependencies caught?
- Time saved in code review?

---

## 🐛 Troubleshooting

### Hook Not Triggering

1. Check hook is enabled:
```json
{ "enabled": true }
```

2. Verify hook location:
```bash
ls .claude/hooks/
```

3. Check event type matches command

### Hook Too Strict

1. Adjust thresholds in hook JSON
2. Or temporarily disable:
```json
{ "enabled": false }
```

### False Positives

1. Add exceptions to hook prompt
2. Or use more specific patterns

---

## 📊 Hook Statistics

### Coverage

- **Total Hooks**: 25
- **Categories**: 5
- **Critical Hooks**: 12
- **Events Covered**: 2 (pre-submit, post-submit)

### By Category

| Category | Count | Critical |
|----------|-------|----------|
| Development Safety | 5 | 3 |
| Production Deployment | 5 | 3 |
| Code Quality | 5 | 0 |
| Security Enforcement | 5 | 5 |
| Performance Monitoring | 5 | 1 |

---

## 🔗 Related Resources

### Documentation
- [Claude Code Hooks Guide](https://docs.claude.com/en/docs/claude-code/hooks)
- [Event Types Reference](https://docs.claude.com/en/docs/claude-code/hooks#events)

### Templates
- `/templates/hooks/safety-hook-template.json`
- `/templates/hooks/workflow-hook-template.json`

### Examples
- `/examples/beginner/safety-hooks/`
- `/examples/intermediate/advanced-hooks/`

---

## 📝 Creating Custom Hooks

Use the provided templates to create your own hooks:

```bash
# Copy template
cp templates/hooks/safety-hook-template.json .claude/hooks/my-custom-hook.json

# Edit to your needs
# - Change name and description
# - Customize detection patterns
# - Modify messages and actions
```

### Custom Hook Example

```json
{
  "name": "api-breaking-change-check",
  "event": "user-prompt-submit",
  "description": "Detects breaking API changes",
  "enabled": true,
  "prompt": "Check if API changes are backward compatible..."
}
```

---

## 🤝 Contributing

Have ideas for new hooks? See patterns we should add?

1. Create new hook following template
2. Test thoroughly
3. Document usage
4. Submit to the collection

---

## 📄 License

MIT License - Use freely in your projects

---

## 🎯 Quick Reference

### By Use Case

**New Project Setup:**
```bash
cp hooks-collection/development-safety/* .claude/hooks/
cp hooks-collection/code-quality/* .claude/hooks/
```

**Production Application:**
```bash
cp hooks-collection/production-deployment/* .claude/hooks/
cp hooks-collection/security-enforcement/* .claude/hooks/
cp hooks-collection/performance-monitoring/* .claude/hooks/
```

**Open Source Project:**
```bash
cp hooks-collection/code-quality/* .claude/hooks/
cp hooks-collection/security-enforcement/license-compliance-check.json .claude/hooks/
```

**Enterprise Application:**
```bash
# All hooks
cp -r hooks-collection/* .claude/hooks/
```

---

**Last Updated:** 2025-11-02
**Version:** 1.0.0
**Maintainer:** Claudius Skills Project

---

## 🎉 What's Next?

After setting up hooks:

1. **Combine with Skills** - Use automatic skills for development
2. **Add Slash Commands** - Manual workflows for common tasks
3. **Configure Agents** - Specialized consultants for complex work
4. **Set up MCP** - Connect to external services

See the main project README for complete Claude Code setup!
