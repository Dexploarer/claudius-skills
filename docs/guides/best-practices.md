# Best Practices - Claudius Skills

> Advanced techniques for maximum productivity with Claude Code

---

## 🎯 Skill Best Practices

### 1. Use Specific Activation Phrases

❌ **Vague:**
```
"Help with this code"
```

✅ **Specific:**
```
"Use the image-optimizer skill to optimize these images"
"Generate a React component with TypeScript"
"Set up MLflow for experiment tracking"
```

### 2. Combine Skills with Commands

```
# First, use a skill to generate code
"Create a FastAPI endpoint for user authentication"

# Then, use a command to test it
"/test"

# Finally, commit with automated review
"/commit"
```

### 3. Layer Multiple Skills

```
"Use the api-documentation-generator to create OpenAPI spec,
then use the security-header-generator to add security,
and finally generate tests with the test-helper skill"
```

---

## 🪝 Hook Best Practices

### 1. Start with Critical Hooks Only

**Week 1:** Safety essentials
```bash
cp hooks-collection/security-enforcement/secret-scanning.json .claude/hooks/
cp hooks-collection/development-safety/env-file-protection.json .claude/hooks/
cp hooks-collection/development-safety/prevent-force-push.json .claude/hooks/
```

**Week 2:** Add quality hooks
```bash
cp hooks-collection/code-quality/*.json .claude/hooks/
```

**Week 3:** Complete deployment hooks
```bash
cp hooks-collection/production-deployment/*.json .claude/hooks/
```

### 2. Customize Thresholds for Your Team

```json
// test-coverage-enforcement.json
{
  "name": "test-coverage-enforcement",
  // Adjust based on your project maturity
  "Statements: >= 60%"  // Start lower, increase gradually
}
```

### 3. Document Hook Exceptions

Create `.claude/hooks/EXCEPTIONS.md`:
```markdown
# Hook Exceptions

## env-file-protection
- `config/public-keys.env` - Contains only public keys, safe to commit

## large-file-warning
- `docs/architecture-diagram.pdf` - Important documentation, approved
```

---

## ⌨️ Command Best Practices

### 1. Create Aliases for Common Workflows

```markdown
<!-- .claude/commands/ship.md -->
# /ship - Complete deployment workflow

Runs:
1. /test - Run all tests
2. /security-audit - Security scan
3. /build - Build production
4. /deploy - Deploy to production
5. /health-check - Verify deployment
```

### 2. Chain Commands for Workflows

```
# Development workflow
/test && /lint && /commit

# Pre-deployment
/security-audit && /performance-profile && /deploy

# Post-deployment
/health-check && /setup-dashboards
```

### 3. Use Command Flags

```
/trace-request --analyze trace-id-123
/deploy-edge --platform cloudflare
/evaluate-model --compare model-v1 model-v2
```

---

## 👥 Agent Best Practices

### 1. Choose the Right Agent for the Task

**General Development:**
- `code-reviewer` - Code quality
- `test-writer` - Test generation
- `doc-writer` - Documentation

**Specialized Tasks:**
- `ml-ops-engineer` - ML infrastructure
- `edge-computing-specialist` - Edge deployment
- `platform-architect` - Internal platforms
- `webassembly-expert` - Performance optimization

### 2. Provide Context to Agents

❌ **Vague:**
```
"Review this code"
```

✅ **Contextual:**
```
"Review this authentication middleware for:
- Security vulnerabilities
- Performance bottlenecks
- Best practices for Express.js
- OWASP Top 10 compliance"
```

### 3. Use Agents for Complex Decisions

```
"I need to choose between SvelteKit, Next.js, and Remix for a new project.
Use the system-architect agent to analyze:
- Team expertise: React developers
- Requirements: SSR, excellent SEO, fast page loads
- Scale: 100k monthly active users
- Budget: Limited DevOps resources"
```

---

## 🔄 Workflow Best Practices

### Development Workflow

```
1. Start: "Scaffold a new REST API service"
2. Code: (AI assists with skills)
3. Test: /test
4. Review: "Review my code for security issues"
5. Commit: /commit
6. Deploy: /deploy (with hooks enforcing checklist)
```

### Team Standardization Workflow

```
1. Create golden path: /create-golden-path microservice
2. Add to templates: Save in team repository
3. Document: Update team wiki
4. Share hooks: Distribute .claude/hooks/
5. Monitor adoption: Track usage metrics
```

### Emergency Response Workflow

```
1. Incident detected: Alerts fire
2. Diagnose: /trace-request --analyze error-trace
3. Fix: Apply hotfix
4. Verify: /health-check
5. Rollback if needed: /rollback-emergency
6. Post-mortem: /postmortem-generate
```

---

## 📊 Team Collaboration

### 1. Share Configuration via Git

```bash
# Commit .claude/ directory
git add .claude/
git commit -m "Add Claude Code configuration"
git push

# Team members get:
- Same skills
- Same hooks
- Same commands
- Consistent experience
```

### 2. Create Team-Specific Skills

```markdown
<!-- .claude/skills/company-api-generator.md -->
# Company API Generator

Generates APIs following OUR company standards:
- Authentication: OAuth2 with company SSO
- Logging: Winston with company format
- Monitoring: Company Datadog dashboards
- Database: PostgreSQL with company schema conventions
```

### 3. Standardize with Hooks

```bash
# Enforce company standards
cp company-standards/hooks/*.json .claude/hooks/

# Hooks enforce:
- Commit message format
- Code style
- Test coverage (minimum 80%)
- Security requirements
- Documentation standards
```

---

## 🎓 Learning & Improvement

### 1. Start with Examples

```bash
# Try example before building
cd examples/intermediate/performance-skills/bundle-analyzer/
# See how it works
# Adapt to your needs
# Copy to your project
```

### 2. Incremental Adoption

**Month 1:** Core skills + safety hooks
**Month 2:** Framework-specific skills
**Month 3:** Quality enforcement hooks
**Month 4:** Advanced skills + specialized agents
**Month 5:** Team-wide standardization
**Month 6:** Custom skills for your domain

### 3. Measure Impact

Track:
- **Time saved:** Hours per week
- **Errors prevented:** Hook interventions
- **Quality improved:** Test coverage, security issues found
- **Onboarding speed:** New developer productivity

---

## ⚡ Performance Tips

### 1. Minimize Active Hooks

Only enable hooks you actually need:
```bash
# Too many hooks = slower workflow
# Keep it to ~10-15 most critical hooks
```

### 2. Use Specific Skills

```
# ❌ Slow - Claude searches all skills
"Help me with this"

# ✅ Fast - Direct skill invocation
"Use the react-component-generator skill"
```

### 3. Cache Common Patterns

Create skills for repeated tasks:
```markdown
<!-- .claude/skills/company-service.md -->
# Generates our standard microservice structure
# Reuses template, very fast
```

---

## 🔒 Security Best Practices

### 1. Always Enable Secret Scanning

```bash
# Non-negotiable
cp hooks-collection/security-enforcement/secret-scanning.json .claude/hooks/
```

### 2. Layer Security Hooks

```bash
# Multiple lines of defense
cp hooks-collection/security-enforcement/*.json .claude/hooks/
cp hooks-collection/development-safety/env-file-protection.json .claude/hooks/
```

### 3. Regular Security Audits

```bash
# Monthly or before major releases
/audit-security --focus all --report pdf
```

---

## 📈 Scaling Best Practices

### For Small Teams (2-10 developers)

- Starter or Intermediate kit
- 5-10 critical hooks
- Shared via git
- Weekly skill additions

### For Medium Teams (10-50 developers)

- Intermediate kit + selected advanced
- 15-20 hooks
- Golden path templates
- Platform team maintains configs
- Monthly reviews and updates

### For Large Organizations (50+ developers)

- Full advanced kit
- 25-30 hooks
- Internal developer platform
- Dedicated platform engineering team
- Custom skills for company domain
- Centralized hook management
- Compliance automation

---

## 🎯 Optimization Strategies

### 1. Profile Your Workflow

```
# What takes the most time?
- Writing boilerplate? → Create skills
- Fixing same mistakes? → Add hooks
- Onboarding new devs? → Create golden paths
- Deploying safely? → Add deployment hooks
```

### 2. Automate Repetitive Tasks

```
# If you do it > 3 times, create a skill or command
# Examples:
- Database migrations
- API endpoint generation
- Test boilerplate
- Documentation updates
```

### 3. Continuous Improvement

```
# Monthly review:
1. Which skills/commands are most used?
2. Which hooks prevented issues?
3. What new patterns emerged?
4. What can be automated next?
```

---

## 🏆 Advanced Techniques

### 1. Skill Composition

```
"First use database-architect to design the schema,
then use django-model-helper to generate models,
then use test-helper to create model tests,
and finally use api-documentation-generator for the API docs"
```

### 2. Context-Aware Customization

```markdown
<!-- .claude/skills/project-specific.md -->
# Project: E-commerce Platform
#
# When generating components:
# - Always include analytics tracking
# - Always add error boundaries
# - Always implement loading states
# - Always support theming
```

### 3. Meta-Automation

Create skills that generate skills:
```
"Create a new skill for generating GraphQL subscriptions
following our company patterns"
```

---

## 📝 Documentation Best Practices

### 1. Document Your Setup

```markdown
# PROJECT_CLAUDE.md

## Our Claude Code Setup

### Skills We Use
- react-component-generator: For UI components
- api-documentation-generator: Auto-generate OpenAPI specs
- Custom: company-auth-middleware (see .claude/skills/)

### Critical Hooks
- secret-scanning: Prevents API key commits
- test-coverage-enforcement: Minimum 80%
- pre-deploy-checklist: Enforces deployment safety

### Commands
- /ship: Complete deployment workflow
- /newfeature: Scaffold feature with all boilerplate
```

### 2. Onboarding Guide

```markdown
# NEW_DEVELOPER_GUIDE.md

## Day 1: Setup
1. Clone repo
2. Claude Code is already configured!
3. Try `/help` to see available commands
4. Say "create a README for this project" to test skills

## Day 2: Learn the Basics
- Try `/explain` on complex files
- Use `/test` to generate tests
- Commit with `/commit` (auto code review)

## Week 1: Productivity
- Learn our golden paths
- Use skills for common tasks
- Hooks prevent common mistakes
```

---

## 🚀 ROI Maximization

### Measure These Metrics

1. **Developer Productivity**
   - Time to first commit (new devs)
   - Daily commits per developer
   - PR cycle time

2. **Quality Improvements**
   - Bug reduction rate
   - Test coverage increase
   - Security incidents prevented

3. **Cost Savings**
   - CI/CD time reduced
   - Onboarding time saved
   - Incident reduction

### Calculate ROI

```
Monthly Value =
  (Hours saved per dev × Devs × Hourly rate) +
  (Incidents prevented × Incident cost) +
  (Onboarding time saved × New hire rate)

Example:
  (10 hours × 20 devs × $100/hr) +     # $20,000
  (3 incidents × $5,000) +              # $15,000
  (20 hours × 2 new hires × $100/hr)    # $4,000
  = $39,000/month value
```

---

## 🎉 Success Stories

### "We Cut Onboarding Time by 60%"
```
Before: 2 weeks to productivity
After: 3 days with golden paths + skills
Savings: 11 days × $800/day = $8,800 per new hire
```

### "Hooks Prevented 15 Production Incidents"
```
Secret scanning: 8 API keys caught
Force push prevention: 4 disasters avoided
Pre-deploy checklist: 3 incomplete deployments stopped
Value: 15 × $5,000 = $75,000 saved
```

### "80% Faster Code Reviews"
```
Before: Manual review, 2-4 hours
After: Automated pre-review with hooks + agent
Now: 30 minutes for final human review
Savings: 3 hours × 50 PRs/month × $100/hr = $15,000/month
```

---

**Ready for 100% Completion?** See `MASTER_INDEX.md` for everything available!

**Last Updated:** 2025-11-02
