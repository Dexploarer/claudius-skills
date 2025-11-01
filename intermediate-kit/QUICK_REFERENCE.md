# Intermediate Kit - Quick Reference

Quick lookup for all intermediate-level skills, commands, and subagents.

---

## 🛠️ Framework Skills (10)

| Skill | Usage | Description |
|-------|-------|-------------|
| `react-component-generator` | "create Button component" | React components with TypeScript & hooks |
| `vue-component-generator` | "generate Vue navigation component" | Vue 3 Composition API components |
| `express-api-generator` | "create Express API for users" | Express.js REST APIs with TypeScript |
| `fastapi-generator` | "build FastAPI endpoints" | FastAPI async endpoints with Pydantic |
| `django-model-helper` | "create Django model for posts" | Django ORM models with relationships |
| `nextjs-page-generator` | "create Next.js dashboard page" | Next.js 13+ App Router pages |
| `graphql-schema-generator` | "design GraphQL schema" | GraphQL types, queries, mutations |
| `database-migration-helper` | "create migration for..." | Database migrations with rollback |
| `testing-framework-helper` | "write tests for UserService" | Comprehensive test suites |
| `api-documentation-generator` | "generate API docs" | OpenAPI/Swagger documentation |

---

## ⚡ Workflow Commands (15)

| Command | Arguments | Description |
|---------|-----------|-------------|
| `/deploy` | `[environment]` | Deploy with full safety checks |
| `/version-bump` | `[major\|minor\|patch]` | Bump semantic version |
| `/migration-create` | `"description"` | Create database migration |
| `/security-audit` | - | Comprehensive security scan |
| `/performance-profile` | `[url]` | Analyze performance |
| `/pr-creator` | `[base-branch]` | Create PR with description |
| `/env-setup` | - | Setup environment variables |
| `/coverage-report` | - | Generate test coverage |
| `/bundle-analyze` | - | Analyze bundle size |
| `/changelog-update` | `[version]` | Update CHANGELOG.md |
| `/db-backup` | - | Create encrypted backup |
| `/health-check` | `[url]` | Run health checks |
| `/dependency-update` | - | Safely update dependencies |
| `/docker-build` | `[image] [tag]` | Build Docker image |
| `/api-docs-generate` | - | Generate API documentation |

---

## 👥 Domain Subagents (6)

| Subagent | Specialty | When to Use |
|----------|-----------|-------------|
| `api-designer` | API architecture & design | Designing REST/GraphQL APIs |
| `performance-optimizer` | Performance analysis | Fixing slow code, optimization |
| `security-auditor` | Security & vulnerabilities | Security audits, vulnerability review |
| `devops-engineer` | CI/CD & infrastructure | Deployment, Docker, Kubernetes |
| `database-architect` | Database design | Schema design, query optimization |
| `system-architect` | System architecture | Microservices, scalability design |

### How to Call Subagents

```
"use the [subagent-name] subagent to [task]"

Examples:
"use the performance-optimizer subagent to analyze this code"
"use the api-designer subagent to design user management API"
"use the security-auditor subagent to review authentication"
```

---

## 🔧 Advanced Hooks

### Pre-Commit Hooks
- 🔒 **Secret Detection** - Blocks commits with passwords/keys
- 🚫 **Force Push Protection** - Prevents push to main/master
- ⚠️ **Migration Confirmation** - Confirms database migrations
- 📝 **.env Validation** - Warns if .env not in .gitignore

### Development Hooks
- 📦 **Dependency Tracking** - Reminds to commit package.json
- 🔢 **Version Detection** - Suggests using /version-bump
- ⚠️ **Dangerous Operations** - Confirms rm -rf, docker cleanup

### Post-Action Hooks
- 📊 **File Tracking** - Counts modified files
- ✅ **Test Alerts** - Alerts on test failures
- 📦 **Build Monitoring** - Reports build size

---

## 🌐 MCP Integrations (10)

| Server | Purpose | Environment Variables |
|--------|---------|----------------------|
| `github` | Issues, PRs, repos | `GITHUB_TOKEN` |
| `gitlab` | GitLab integration | `GITLAB_TOKEN`, `GITLAB_URL` |
| `postgresql` | Database queries | `DATABASE_URL` |
| `slack` | Notifications | `SLACK_BOT_TOKEN`, `SLACK_TEAM_ID` |
| `jira` | Issue tracking | `JIRA_URL`, `JIRA_EMAIL`, `JIRA_API_TOKEN` |
| `aws` | Cloud resources | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` |
| `docker` | Container management | - |
| `kubernetes` | Cluster management | `KUBECONFIG` |
| `sentry` | Error tracking | `SENTRY_AUTH_TOKEN`, `SENTRY_ORG` |
| `datadog` | Monitoring | `DATADOG_API_KEY`, `DATADOG_APP_KEY` |

### Setup MCP

```bash
# 1. Copy template
cp .mcp.json.template .mcp.json

# 2. Edit with your credentials
vim .mcp.json

# 3. Enable servers
# Set "disabled": false

# 4. Add to gitignore
echo ".mcp.json" >> .gitignore
```

---

## 📋 Common Workflows

### Deployment Workflow
```bash
# 1. Run tests
npm test

# 2. Security audit
/security-audit

# 3. Deploy to staging
/deploy staging

# 4. Health check
/health-check https://staging.example.com
```

### Release Workflow
```bash
# 1. Bump version
/version-bump minor

# 2. Update changelog
/changelog-update

# 3. Create PR
/pr-creator

# 4. After merge, tag release
git push --tags
```

### New Feature Workflow
```bash
# 1. Create feature branch
git checkout -b feature/user-auth

# 2. Generate code
"create Express API for authentication"

# 3. Write tests
"write tests for auth service"

# 4. Check coverage
/coverage-report

# 5. Create PR
/pr-creator
```

### Database Workflow
```bash
# 1. Create migration
/migration-create "add user roles table"

# 2. Review migration
cat migrations/...

# 3. Run migration
npm run migrate

# 4. Backup database
/db-backup
```

---

## 🔥 Quick Tips

### Performance Optimization
```bash
# Profile performance
/performance-profile

# Analyze bundle
/bundle-analyze

# Check database queries
"use the performance-optimizer subagent to optimize these queries"
```

### Security Best Practices
```bash
# Run security audit
/security-audit

# Review code for vulnerabilities
"use the security-auditor subagent to review this authentication code"

# Setup environment
/env-setup
```

### API Development
```bash
# Design API
"use the api-designer subagent to design REST API for e-commerce"

# Generate endpoints
"create Express API for products"

# Generate docs
/api-docs-generate
```

### Database Optimization
```bash
# Design schema
"use the database-architect subagent to design schema for blog system"

# Create migration
/migration-create "add indexes for performance"

# Optimize queries
"use the database-architect subagent to optimize this query"
```

---

## 🐛 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Skill not activating | Check description matches request |
| Command not found | Verify file in `.claude/commands/` |
| Hook not running | Check `.claude/settings.json` syntax |
| MCP not working | Verify credentials in `.mcp.json` |
| Subagent error | Check file in `.claude/agents/` |
| Tests failing | Run `/coverage-report` to see gaps |
| Build too large | Run `/bundle-analyze` |
| Security issues | Run `/security-audit` |

---

## 📱 Cheat Sheet

### Generate Code
```
"create [Framework] [Component] for [Feature]"
"generate [API Type] for [Resource]"
"write tests for [Component]"
```

### Run Commands
```bash
/deploy [environment]
/security-audit
/performance-profile
/version-bump [type]
```

### Call Experts
```
"use the [expert] subagent to [task]"
"get the [expert] to review [code]"
```

### Configure
```bash
# Copy config
cp -r .claude/ /project/

# Setup MCP
cp .mcp.json.template .mcp.json

# Edit settings
vim .claude/settings.json
```

---

## 🎯 Pro Tips

1. **Use Tab Completion**: Type `/` and tab for command list
2. **Chain Commands**: Run multiple commands in sequence
3. **Save Workflows**: Create custom commands for repeated tasks
4. **Use MCP**: Connect your tools for powerful automation
5. **Monitor Hooks**: Check hook output for valuable info
6. **Call Subagents**: Use domain experts for complex tasks
7. **Framework-Specific**: Use the right skill for your stack
8. **Security First**: Run `/security-audit` before deployment
9. **Performance Matters**: Profile before optimizing
10. **Test Coverage**: Aim for 80%+ with `/coverage-report`

---

## 📚 See Also

- [Full README](./README.md) - Complete documentation
- [Starter Kit](../starter-kit/) - Beginner guide
- [Examples](../examples/intermediate/) - More examples
- [Templates](../templates/) - Create your own

---

**Questions? Check the [full README](./README.md) or open an issue!**
