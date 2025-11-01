# Claude Code Intermediate Kit - Production-Ready Development

Welcome to the Intermediate Kit! This is a comprehensive, production-focused setup for experienced developers who have mastered Claude Code's Five Pillars and are ready to build sophisticated, framework-specific workflows.

## 🎯 Who Is This For?

This intermediate kit is for developers who:
- ✅ Have used the [Starter Kit](../starter-kit/) and understand the Five Pillars
- ✅ Work with specific frameworks (React, Vue, Django, FastAPI, Express, etc.)
- ✅ Need production-grade workflows (CI/CD, deployment, security audits)
- ✅ Build real applications with complex requirements
- ✅ Want framework-specific automation and domain expertise

## 📦 What's Included?

This kit contains:

- **10 Framework Skills** - React, Vue, Express, FastAPI, Django, Next.js, GraphQL, Database Migrations, Testing, API Docs
- **15 Workflow Commands** - Deploy, version-bump, security-audit, performance-profile, pr-creator, migration-create, and more
- **6 Domain Subagents** - API Designer, Performance Optimizer, Security Auditor, DevOps Engineer, Database Architect, System Architect
- **8+ Advanced Hooks** - Pre-commit lint, test enforcement, secret detection, migration confirmation, etc.
- **10 MCP Integrations** - GitHub, Slack, Jira, AWS, Docker, Kubernetes, PostgreSQL, and more

Everything is production-ready, battle-tested, and ready to enhance your development workflow!

---

## 🚀 Quick Start

### 1. Prerequisites

Make sure you've completed the [Starter Kit](../starter-kit/) first, or are familiar with Claude Code's Five Pillars.

### 2. Installation

```bash
# Copy the intermediate kit to your project
cp -r intermediate-kit/.claude /path/to/your/project/

# Copy MCP template (optional)
cp intermediate-kit/.mcp.json.template /path/to/your/project/.mcp.json

# Edit .mcp.json with your credentials
# IMPORTANT: Never commit .mcp.json with real credentials!
```

### 3. Start Using It

```bash
cd /path/to/your/project
claude
```

### 4. Try It Out

```bash
# Try a workflow command
/deploy staging

# Use a framework skill
"create a React component for UserProfile"

# Call a domain expert
"use the performance-optimizer subagent to analyze this code"

# Run security audit
/security-audit
```

---

## 🛠️ The 10 Framework Skills

Framework-specific skills that understand your tech stack:

### 1. **react-component-generator**
Creates modern React components with TypeScript, hooks, proper types, and tests.

**Usage:**
```
"create a Button component with loading state"
"generate UserProfile component with data fetching"
```

### 2. **vue-component-generator**
Generates Vue 3 components with Composition API, TypeScript, and best practices.

**Usage:**
```
"create a Vue component for the navigation menu"
"build a DataTable component in Vue"
```

### 3. **express-api-generator**
Scaffolds Express.js APIs with proper layering, validation, error handling, and TypeScript.

**Usage:**
```
"create Express API for user management"
"generate REST endpoints for products"
```

### 4. **fastapi-generator**
Creates FastAPI endpoints with Pydantic models, async/await, and OpenAPI docs.

**Usage:**
```
"build FastAPI endpoint for orders"
"create Python REST API with FastAPI"
```

### 5. **django-model-helper**
Generates Django models with proper fields, relationships, indexes, and migrations.

**Usage:**
```
"create Django model for blog posts"
"generate User model with relationships"
```

### 6. **nextjs-page-generator**
Creates Next.js 13+ pages with App Router, Server/Client Components, and data fetching.

**Usage:**
```
"create Next.js page for user dashboard"
"generate product listing page with SSR"
```

### 7. **graphql-schema-generator**
Designs GraphQL schemas with types, queries, mutations, resolvers, and DataLoaders.

**Usage:**
```
"create GraphQL schema for e-commerce"
"design API with GraphQL for blog"
```

### 8. **database-migration-helper**
Creates database migrations with proper up/down, indexes, and data transformations.

**Usage:**
```
"create migration to add user roles"
"generate schema changes for posts table"
```

### 9. **testing-framework-helper**
Generates comprehensive test suites with unit, integration, and E2E tests.

**Usage:**
```
"write tests for UserService"
"create test suite for authentication"
```

### 10. **api-documentation-generator**
Creates OpenAPI/Swagger specs and comprehensive API documentation.

**Usage:**
```
"generate API documentation for endpoints"
"create OpenAPI spec for REST API"
```

---

## ⚡ The 15 Workflow Commands

Production-grade commands for real development workflows:

| Command | Description |
|---------|-------------|
| `/deploy [env]` | Deploy with safety checks, tests, and health checks |
| `/version-bump [type]` | Bump semantic version (major/minor/patch) |
| `/migration-create [name]` | Create database migration with rollback |
| `/security-audit` | Comprehensive security scanning |
| `/performance-profile` | Analyze and optimize performance |
| `/pr-creator` | Create PR with auto-generated description |
| `/env-setup` | Setup environment variables safely |
| `/coverage-report` | Generate test coverage report |
| `/bundle-analyze` | Analyze bundle size |
| `/changelog-update` | Update CHANGELOG.md |
| `/db-backup` | Create encrypted database backup |
| `/health-check` | Run application health checks |
| `/dependency-update` | Safely update dependencies |
| `/docker-build` | Build optimized Docker image |
| `/api-docs-generate` | Generate API documentation |

---

## 👥 The 6 Domain Subagents

Expert consultants for specialized tasks:

### 1. **api-designer**
Expert at designing RESTful APIs, GraphQL schemas, and API architecture.

**When to use:**
- Designing new APIs
- Reviewing API structure
- Creating API documentation
- Implementing best practices

### 2. **performance-optimizer**
Specialist in identifying and fixing performance bottlenecks.

**When to use:**
- Application running slow
- High memory/CPU usage
- Slow database queries
- Large bundle sizes
- Performance audits

### 3. **security-auditor**
Security expert for vulnerability assessment and secure coding.

**When to use:**
- Security audits
- Code security review
- Identifying vulnerabilities
- Implementing security best practices

### 4. **devops-engineer**
Expert in CI/CD, Docker, Kubernetes, and infrastructure.

**When to use:**
- Setting up CI/CD pipelines
- Dockerizing applications
- Kubernetes deployment
- Infrastructure as Code
- Deployment automation

### 5. **database-architect**
Database design and optimization specialist.

**When to use:**
- Designing database schema
- Query optimization
- Index strategy
- Data modeling
- Migration planning

### 6. **system-architect**
Expert in system design and architecture patterns.

**When to use:**
- Designing system architecture
- Microservices planning
- Scalability design
- Architecture review
- Technology decisions

---

## 🔧 Advanced Hooks Configuration

The intermediate kit includes 8+ production-grade hooks:

### Pre-Commit Hooks
- **Secret Detection**: Blocks commits containing passwords, API keys, tokens
- **Force Push Protection**: Prevents accidental force pushes to main/master
- **Migration Confirmation**: Confirms before running database migrations

### Development Hooks
- **.env Validation**: Warns if .env isn't in .gitignore
- **Dependency Tracking**: Reminds to commit package.json changes
- **Version Change Detection**: Suggests using `/version-bump` command
- **Dangerous Operations**: Confirms before `rm -rf`, Docker cleanup, etc.

### Post-Action Hooks
- **File Modification Tracking**: Counts and logs file changes
- **Test Result Alerts**: Alerts on test failures
- **Build Size Monitoring**: Reports build size and warns if too large

---

## 🌐 MCP Integrations

Connect Claude Code to your entire development ecosystem:

### Team & Communication
- **Slack**: Send notifications, read channels, post updates
- **GitHub**: Manage issues, PRs, and repositories
- **GitLab**: Alternative Git hosting integration
- **Jira**: Issue tracking and project management

### Infrastructure & Deployment
- **AWS**: Manage cloud resources and deployments
- **Docker**: Container management and building
- **Kubernetes**: Cluster management and deployments

### Monitoring & Observability
- **Sentry**: Error tracking and monitoring
- **Datadog**: Metrics and performance monitoring

### Data & Databases
- **PostgreSQL**: Database queries and analysis

### Setup

1. Copy `.mcp.json.template` to `.mcp.json`
2. Replace `${VARIABLE}` placeholders with actual values
3. Set `disabled: false` for servers you want to use
4. **NEVER** commit `.mcp.json` with real credentials!

```bash
cp .mcp.json.template .mcp.json
# Edit .mcp.json with your credentials
echo ".mcp.json" >> .gitignore
```

---

## 📁 Directory Structure

```
your-project/
├── .claude/
│   ├── skills/                      # 10 Framework Skills
│   │   ├── react-component-generator.md
│   │   ├── vue-component-generator.md
│   │   ├── express-api-generator.md
│   │   ├── fastapi-generator.md
│   │   ├── django-model-helper.md
│   │   ├── nextjs-page-generator.md
│   │   ├── graphql-schema-generator.md
│   │   ├── database-migration-helper.md
│   │   ├── testing-framework-helper.md
│   │   └── api-documentation-generator.md
│   │
│   ├── commands/                    # 15 Workflow Commands
│   │   ├── deploy.md
│   │   ├── version-bump.md
│   │   ├── migration-create.md
│   │   ├── security-audit.md
│   │   ├── performance-profile.md
│   │   ├── pr-creator.md
│   │   ├── env-setup.md
│   │   ├── coverage-report.md
│   │   ├── bundle-analyze.md
│   │   ├── changelog-update.md
│   │   ├── db-backup.md
│   │   ├── health-check.md
│   │   ├── dependency-update.md
│   │   ├── docker-build.md
│   │   └── api-docs-generate.md
│   │
│   ├── agents/                      # 6 Domain Subagents
│   │   ├── api-designer.md
│   │   ├── performance-optimizer.md
│   │   ├── security-auditor.md
│   │   ├── devops-engineer.md
│   │   ├── database-architect.md
│   │   └── system-architect.md
│   │
│   └── settings.json                # Advanced Hooks
│
├── .mcp.json.template               # MCP server template
├── .mcp.json                        # Your MCP config (gitignored)
├── .gitignore                       # Protects sensitive files
└── README.md                        # This file!
```

---

## 💡 Common Use Cases

### "I need to deploy to staging"

```bash
/deploy staging

# Runs:
# 1. Pre-deployment validation
# 2. Tests and linting
# 3. Build
# 4. Deploy
# 5. Health checks
```

### "Create a new API endpoint"

```
"use the express-api-generator skill to create user authentication API"

# Or for Python:
"use the fastapi-generator skill to create product endpoints"
```

### "My app is slow"

```
"use the performance-optimizer subagent to analyze performance bottlenecks"

# Or run command:
/performance-profile
```

### "Security audit before release"

```bash
/security-audit

# Scans for:
# - Dependency vulnerabilities
# - Exposed secrets
# - Security misconfigurations
# - Common vulnerabilities
```

### "Create a new database migration"

```bash
/migration-create "add user roles and permissions"

# Creates migration with proper structure and rollback
```

### "Bump version for release"

```bash
/version-bump minor

# Updates:
# - package.json / pyproject.toml
# - CHANGELOG.md
# - Git tag
```

---

## 🎯 Learning Path from Beginner to Intermediate

### You've Mastered Beginner When:
- ✅ You understand all Five Pillars
- ✅ You've used the starter kit
- ✅ You can create basic skills and commands
- ✅ You understand how hooks work

### Intermediate Skills to Develop:
- 🎯 Framework-specific expertise
- 🎯 Production deployment workflows
- 🎯 Performance optimization
- 🎯 Security best practices
- 🎯 Database design and optimization
- 🎯 CI/CD pipeline setup
- 🎯 Infrastructure as Code
- 🎯 System architecture

### Next Steps to Advanced:
- Build custom frameworks around the Five Pillars
- Create company/team-specific skills
- Design sophisticated automation workflows
- Integrate multiple services via MCP
- Build plugin-quality configurations

---

## 🔒 Security Best Practices

This kit includes multiple security features:

### Automatic Security
- Secret detection in commits
- .env file protection
- Dependency vulnerability scanning
- Security headers checking
- HTTPS enforcement

### Security Commands
```bash
# Run comprehensive security audit
/security-audit

# Check for secrets before deploying
# (automatically done by /deploy command)
```

### MCP Security
- Use read-only tokens when possible
- Rotate credentials regularly
- Never commit .mcp.json
- Audit MCP packages before use
- Use environment variables

---

## 📊 Performance Features

### Automatic Performance Monitoring
- Build size tracking
- Bundle analysis
- Memory leak detection
- Query performance monitoring

### Performance Commands
```bash
# Analyze performance
/performance-profile

# Check bundle size
/bundle-analyze

# Generate coverage report
/coverage-report
```

---

## 🤝 Team Collaboration

### Sharing with Your Team

```bash
# Share Claude Code configuration via git
git add .claude/
git commit -m "Add intermediate Claude Code setup"
git push

# Teammates get everything automatically
git pull
```

### Personal vs. Team Configuration

**Team Configuration** (committed to git):
- `.claude/skills/` - Shared skills
- `.claude/commands/` - Team commands
- `.claude/agents/` - Shared subagents
- `.claude/settings.json` - Team hooks

**Personal Configuration** (not committed):
- `.mcp.json` - Your personal MCP servers
- `~/.claude/` - Your global personal config

---

## 🐛 Troubleshooting

### "Skills aren't activating"
- Check skill description matches your request
- Verify YAML frontmatter is correct
- Check for syntax errors

### "Commands not found"
- Ensure file is in `.claude/commands/`
- Check file name matches command
- Restart Claude Code

### "Hooks not running"
- Verify `.claude/settings.json` syntax
- Check hook pattern matches tool use
- Ensure commands are executable
- Check exit codes (0=success, 2=block)

### "MCP server not working"
- Verify `.mcp.json` exists
- Check `disabled: false`
- Validate credentials
- Try with `claude --debug`

### "Subagent errors"
- Check agent file exists in `.claude/agents/`
- Verify YAML frontmatter
- Check `allowed-tools` if restricted
- Try calling explicitly

---

## 🎓 Advanced Topics

### Custom Framework Skills

Create skills for your specific frameworks:

```markdown
---
name: my-framework-helper
description: Generates components for MyFramework
---

# Instructions for using MyFramework...
```

### Workflow Automation

Chain commands together:

```bash
# Create PR workflow
/version-bump patch
/changelog-update
/pr-creator
```

### Multi-Service MCP

Connect multiple services:

```javascript
// Use GitHub + Slack + Jira together
"Create GitHub issue, post to Slack, and link Jira ticket"
```

---

## 📚 Additional Resources

- [Starter Kit](../starter-kit/) - Beginner guide
- [Examples Directory](../examples/) - More examples
- [Templates](../templates/) - Reusable templates
- [Claude Code Docs](https://docs.claude.com/claude-code/)
- [MCP Documentation](https://modelcontextprotocol.io/)

---

## ✨ What's Next?

### Immediate Next Steps
1. ✅ Copy `.claude/` to your project
2. ✅ Try the workflow commands
3. ✅ Use framework-specific skills
4. ✅ Call domain subagents
5. ✅ Setup MCP integrations (optional)

### Going Further
- Customize skills for your tech stack
- Create project-specific commands
- Add team-specific hooks
- Connect your tools via MCP
- Build advanced automation workflows

### Contributing
Found a bug? Have an improvement? Created a useful skill?
- Open an issue
- Submit a pull request
- Share your configurations

---

## 🙏 Acknowledgments

- The Claude Code team for the Five Pillars
- The MCP community for integrations
- Contributors who share their expertise

---

**Ready to level up your development workflow? Let's build something amazing! 🚀**
