# Intermediate Kit - Production-Ready Rules

> **Level 2: Production-Ready Claude Code Configuration**
> Framework-specific tools and advanced automation for building real-world applications.

---

## 🎯 Purpose

The Intermediate Kit provides **production-ready capabilities** for professional development:
- 10 framework-specific skills (React, Vue, Django, Express, etc.)
- 15 advanced slash commands (deploy, security-audit, pr-creator, etc.)
- 6 specialist subagents (api-designer, database-architect, etc.)
- Enhanced safety hooks with production awareness

**Target Audience:** Building production applications, working with frameworks, need advanced automation

---

## 📚 Available Capabilities

### Framework-Specific Skills (10 Total)
All skills located in: `intermediate-kit/.claude/skills/`

**Frontend Frameworks:**
1. **react-component-generator** - Modern React with TypeScript & hooks
   - Auto-invoked: "create React component", "add React component"
   - Features: TypeScript, hooks, props validation, styled-components
   - Reference: `@intermediate-kit/.claude/skills/react-component-generator.md`

2. **vue-component-generator** - Vue 3 Composition API
   - Auto-invoked: "create Vue component", "add Vue component"
   - Features: Vue 3, Composition API, TypeScript, script setup
   - Reference: `@intermediate-kit/.claude/skills/vue-component-generator.md`

3. **nextjs-page-generator** - Next.js pages and layouts
   - Auto-invoked: "create Next.js page", "add Next route"
   - Features: App router, RSC, server actions, metadata
   - Reference: `@intermediate-kit/.claude/skills/nextjs-page-generator.md`

**Backend Frameworks:**
4. **express-api-generator** - Express.js REST APIs
   - Auto-invoked: "create Express API", "add Express endpoint"
   - Features: Router, middleware, error handling, validation
   - Reference: `@intermediate-kit/.claude/skills/express-api-generator.md`

5. **fastapi-generator** - FastAPI REST APIs
   - Auto-invoked: "create FastAPI endpoint", "add Python API"
   - Features: Pydantic models, async, OpenAPI, dependency injection
   - Reference: `@intermediate-kit/.claude/skills/fastapi-generator.md`

6. **django-model-helper** - Django models and relationships
   - Auto-invoked: "create Django model", "add Django fields"
   - Features: Models, migrations, managers, signals
   - Reference: `@intermediate-kit/.claude/skills/django-model-helper.md`

**API & Documentation:**
7. **graphql-schema-generator** - GraphQL schema definitions
   - Auto-invoked: "create GraphQL schema", "add GraphQL type"
   - Features: Types, queries, mutations, resolvers
   - Reference: `@intermediate-kit/.claude/skills/graphql-schema-generator.md`

8. **api-documentation-generator** - OpenAPI/Swagger documentation
   - Auto-invoked: "document API", "create OpenAPI spec"
   - Features: Swagger/OpenAPI, request/response examples
   - Reference: `@intermediate-kit/.claude/skills/api-documentation-generator.md`

**Database & Testing:**
9. **database-migration-helper** - Database migrations
   - Auto-invoked: "create migration", "add database column"
   - Features: SQL migrations, ORM migrations, rollback
   - Reference: `@intermediate-kit/.claude/skills/database-migration-helper.md`

10. **testing-framework-helper** - Testing framework setup
    - Auto-invoked: "setup tests", "configure Jest/pytest"
    - Features: Jest, pytest, vitest, mocking, coverage
    - Reference: `@intermediate-kit/.claude/skills/testing-framework-helper.md`

### Advanced Slash Commands (15 Total)
All commands located in: `intermediate-kit/.claude/commands/`

**Development & Build:**
- `/api-docs-generate` - Generate comprehensive API documentation
- `/bundle-analyze` - Analyze JavaScript bundle size
- `/performance-profile` - Profile application performance
- `/docker-build` - Build and optimize Docker images

**Database & Deployment:**
- `/db-backup` - Create database backups
- `/migration-create` - Create new database migration
- `/deploy` - Deploy application to production
- `/env-setup` - Set up environment configuration

**CI/CD & Quality:**
- `/pr-creator` - Create pull request with description
- `/changelog-update` - Update CHANGELOG.md
- `/coverage-report` - Generate detailed test coverage report
- `/security-audit` - Run comprehensive security audit
- `/dependency-update` - Update and audit dependencies
- `/version-bump` - Bump version number (semver)
- `/health-check` - Check application health

### Specialist Subagents (6 Total)
All agents located in: `intermediate-kit/.claude/agents/`

1. **api-designer** - REST/GraphQL API design expert
   - Invocation: "Use api-designer to design the user API"
   - Expertise: RESTful design, GraphQL schemas, API versioning
   - Tools: Read, Write, Grep
   - Reference: `@intermediate-kit/.claude/agents/api-designer.md`

2. **database-architect** - Database schema design specialist
   - Invocation: "Use database-architect to design the schema"
   - Expertise: Normalization, indexes, relationships, performance
   - Tools: Read, Write, Grep
   - Reference: `@intermediate-kit/.claude/agents/database-architect.md`

3. **devops-engineer** - DevOps and infrastructure expert
   - Invocation: "Use devops-engineer for deployment strategy"
   - Expertise: CI/CD, containers, orchestration, monitoring
   - Tools: Read, Write, Bash, Grep
   - Reference: `@intermediate-kit/.claude/agents/devops-engineer.md`

4. **performance-optimizer** - Performance tuning specialist
   - Invocation: "Use performance-optimizer to optimize the app"
   - Expertise: Profiling, caching, bundling, lazy loading
   - Tools: Read, Grep, Bash
   - Reference: `@intermediate-kit/.claude/agents/performance-optimizer.md`

5. **security-auditor** - Security analysis expert
   - Invocation: "Use security-auditor to audit security"
   - Expertise: Vulnerabilities, OWASP, authentication, authorization
   - Tools: Read, Grep, Bash
   - Reference: `@intermediate-kit/.claude/agents/security-auditor.md`

6. **system-architect** - System design and architecture expert
   - Invocation: "Use system-architect for architecture design"
   - Expertise: Design patterns, scalability, microservices
   - Tools: Read, Grep
   - Reference: `@intermediate-kit/.claude/agents/system-architect.md`

### Enhanced Safety Hooks
Configuration: `intermediate-kit/.claude/settings.json`

**PreToolUse Hooks (Production-Aware):**
- ✅ Comprehensive secret detection (API keys, tokens, credentials)
- ✅ Force push prevention (main/master specific)
- ✅ .env file gitignore validation
- ✅ Package manager reminders (npm, yarn, pnpm)
- ✅ Docker cleanup with mandatory confirmation
- ✅ Migration confirmation with branch awareness
- ✅ Version bump suggestions (semver)
- ✅ Recursive delete with confirmation required

**PostToolUse Hooks (Production Monitoring):**
- File modification counter
- Test failure detection with details
- Build size warnings (>1MB threshold)

---

## 🎓 Production Workflow

### Recommended Usage Pattern:

1. **Framework-Specific Development**
   ```
   You: "Create a React component for user profile"
   → react-component-generator creates TypeScript component with hooks
   ```

2. **API Development**
   ```
   You: "Create Express API endpoint for user authentication"
   → express-api-generator creates router with validation
   → api-documentation-generator adds OpenAPI spec
   ```

3. **Database Design**
   ```
   You: "Use database-architect to design the e-commerce schema"
   → Comprehensive schema with relationships and indexes
   ```

4. **Deployment**
   ```
   /docker-build → Build optimized container
   /security-audit → Check vulnerabilities
   /deploy → Deploy to production
   ```

---

## 📖 Framework Support

### Frontend Frameworks
- **React** - Components, hooks, TypeScript, testing
- **Vue 3** - Composition API, script setup, TypeScript
- **Next.js** - App router, RSC, server actions, metadata
- **Angular** - (via advanced patterns)

### Backend Frameworks
- **Express.js** - REST APIs, middleware, routing
- **FastAPI** - Python async APIs, Pydantic, OpenAPI
- **Django** - Models, ORM, admin, authentication
- **Flask** - (via Express patterns)

### API Technologies
- **REST** - RESTful design, versioning
- **GraphQL** - Schemas, resolvers, mutations
- **OpenAPI** - Documentation, specification

### Databases
- **SQL** - PostgreSQL, MySQL, migrations
- **MongoDB** - NoSQL, schemas, indexes
- **ORM** - Sequelize, SQLAlchemy, Prisma

### Testing
- **Jest** - JavaScript/TypeScript testing
- **Vitest** - Vite-powered testing
- **pytest** - Python testing
- **Testing Library** - Component testing

---

## 🚀 Quick Start

### Setup for React Project:
```bash
# Copy intermediate kit
cp -r intermediate-kit/.claude /path/to/react-project/

# Available immediately:
# - react-component-generator skill
# - nextjs-page-generator skill
# - testing-framework-helper skill
# - /bundle-analyze command
# - /api-docs-generate command
# - performance-optimizer subagent
```

### Setup for Full-Stack Project:
```bash
cp -r intermediate-kit/.claude /path/to/fullstack-project/

# Backend: express-api-generator, fastapi-generator, django-model-helper
# Frontend: react-component-generator, vue-component-generator
# Database: database-migration-helper, database-architect
# DevOps: /docker-build, /deploy, devops-engineer
```

---

## 🔐 Production Security

### Enhanced Secret Detection
```
Hook checks for:
- API_KEY, SECRET_KEY, ACCESS_TOKEN
- Private keys, certificates
- Database credentials
- OAuth secrets
- JWT secrets
```

### Migration Safety
```
Hook behavior:
- Confirms database migrations
- Checks current branch
- Reminds about backups
- Validates migration files
```

### Version Control Safety
```
- Prevents force push to main/master
- Validates .env in .gitignore
- Suggests version bumps on package.json changes
- Confirms destructive operations
```

---

## 💡 Best Practices

### For Framework-Specific Skills:
- Mention the framework explicitly in requests
- Use TypeScript for type safety
- Follow framework conventions
- Request tests alongside components

### For Commands:
- Run `/security-audit` before deployment
- Use `/bundle-analyze` to optimize size
- Create `/pr-creator` for team review
- Update `/changelog-update` for releases

### For Subagents:
- Call api-designer before implementation
- Use database-architect for schema changes
- Consult security-auditor for sensitive features
- Leverage system-architect for complex features

---

## 📊 Production Checklist

### Before Deployment:
- [ ] All tests pass (`/test`)
- [ ] Security audit clean (`/security-audit`)
- [ ] Bundle size acceptable (`/bundle-analyze`)
- [ ] Database migrations ready (`/migration-create`)
- [ ] Environment variables documented
- [ ] API documentation updated (`/api-docs-generate`)
- [ ] CHANGELOG.md updated (`/changelog-update`)
- [ ] Version bumped (`/version-bump`)
- [ ] PR created and reviewed (`/pr-creator`)
- [ ] Health check passes (`/health-check`)

---

## 🔗 Detailed Rule References

For comprehensive documentation:
- **Skills Reference:** `@intermediate-kit/.claude/rules/skills-reference.md`
- **Commands Reference:** `@intermediate-kit/.claude/rules/commands-reference.md`
- **Agents Reference:** `@intermediate-kit/.claude/rules/agents-reference.md`
- **Hooks Reference:** `@intermediate-kit/.claude/rules/hooks-reference.md`

### Framework-Specific Rules:
- React: `@intermediate-kit/.claude/rules/frameworks/react.md`
- Vue: `@intermediate-kit/.claude/rules/frameworks/vue.md`
- Express: `@intermediate-kit/.claude/rules/frameworks/express.md`
- Django: `@intermediate-kit/.claude/rules/frameworks/django.md`

### Workflow Rules:
- API Development: `@intermediate-kit/.claude/rules/workflows/api-development.md`
- Database Design: `@intermediate-kit/.claude/rules/workflows/database.md`
- Deployment: `@intermediate-kit/.claude/rules/workflows/deployment.md`
- Security: `@intermediate-kit/.claude/rules/workflows/security.md`

---

## 🎯 Use Cases

### E-Commerce Application
```
Skills: react-component-generator, express-api-generator, database-migration-helper
Agents: database-architect, api-designer, security-auditor
Commands: /docker-build, /deploy, /security-audit
```

### SaaS Platform
```
Skills: nextjs-page-generator, fastapi-generator, graphql-schema-generator
Agents: system-architect, performance-optimizer, devops-engineer
Commands: /pr-creator, /bundle-analyze, /health-check
```

### REST API Service
```
Skills: express-api-generator, api-documentation-generator, testing-framework-helper
Agents: api-designer, security-auditor
Commands: /api-docs-generate, /security-audit, /deploy
```

---

## 📈 Progression Path

**Current Level:** Intermediate (Production-Ready)

**What You've Learned:**
- Framework-specific development
- Production deployment workflows
- API design and documentation
- Database design patterns
- Security best practices
- CI/CD automation

**Next Steps:**
1. Master all framework skills
2. Use specialist subagents regularly
3. Implement full CI/CD pipelines
4. Optimize performance systematically

**When Ready for Next Level:**
- Building enterprise applications
- Need advanced performance optimization
- Implementing compliance requirements (WCAG, SOC2)
- Complex distributed systems
- Advanced security implementations

**Graduate To:** Advanced Examples
- Location: `examples/advanced/.claude/`
- Rules: `@examples/advanced/.claude/rules/CLAUDE.md`
- Capabilities: Performance optimization, security compliance, advanced DevOps

---

## 🔗 Related Resources

**Project Root:**
- Main Overview: `@CLAUDE.md`
- Project README: `@README.md`

**Previous Level:**
- Starter Kit: `@starter-kit/.claude/rules/CLAUDE.md`

**Next Level:**
- Advanced Examples: `@examples/advanced/.claude/rules/CLAUDE.md`

**Templates:**
- Skill Template: `@templates/skill-template.md`
- Command Template: `@templates/command-template.md`
- Subagent Template: `@templates/subagent-template.md`

**Guides:**
- Best Practices: `@resources/guides/best-practices.md`
- Security Guide: `@resources/guides/security.md`
- Troubleshooting: `@resources/guides/troubleshooting.md`

---

**Level:** Intermediate (Production-Ready)
**Last Updated:** 2025-11-01
**Capabilities:** 10 skills, 15 commands, 6 agents, 8+ hooks
**Framework Support:** React, Vue, Next.js, Express, FastAPI, Django, GraphQL

