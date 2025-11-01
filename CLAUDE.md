# Claudius Skills - Project Rules & Architecture

> **Project Memory for Claude Code AI Assistant**
> This file provides architectural context, design decisions, and available capabilities for the Claudius Skills project.

---

## 🎯 Project Overview

**Claudius Skills** is a comprehensive, production-ready collection of Claude Code extensibility configurations covering **Claude Code's Five Pillars of Extensibility**:

1. **Skills** - Automatic, context-aware capabilities
2. **Slash Commands** - Manual workflow shortcuts
3. **Hooks** - Event-driven automation
4. **Subagents** - Specialized AI consultants
5. **MCP Servers** - External service integrations

**Current Status:** 60% Complete (15/25 niche skills implemented)

---

## 📁 Project Structure

```
claudius-skills/
├── starter-kit/          # Beginner-friendly (5 skills, 12 commands, 4 agents)
├── intermediate-kit/     # Production-ready (10 skills, 15 commands, 6 agents)
├── examples/            # Multi-level examples (Beginner → Master)
│   ├── beginner/        # Learning-focused examples
│   ├── intermediate/    # Production patterns
│   ├── advanced/        # Complex integrations
│   └── master/          # Expert-level (planned)
├── templates/           # Reusable templates
├── resources/           # Guides and tutorials
└── .claude/rules/       # Project-wide rules (this directory structure)
```

---

## 🛠️ Available Capabilities

### Skills (25 Total)

**Starter Kit (5 skills):**
- `readme-generator` - Professional README creation
- `code-explainer` - Beginner-friendly code explanations
- `bug-finder` - Common bug identification
- `test-helper` - Comprehensive test writing
- `git-helper` - Git operation assistance

**Intermediate Kit (10 skills):**
- `react-component-generator` - Modern React with TypeScript
- `vue-component-generator` - Vue 3 Composition API
- `express-api-generator` - Express.js REST APIs
- `fastapi-generator` - FastAPI endpoints
- `django-model-helper` - Django models and relationships
- `nextjs-page-generator` - Next.js pages/layouts
- `graphql-schema-generator` - GraphQL schemas
- `api-documentation-generator` - OpenAPI/Swagger docs
- `database-migration-helper` - Database migrations
- `testing-framework-helper` - Test setup (Jest, pytest, vitest)

**Niche Skills (15 implemented):**
- Performance: `image-optimizer`, `bundle-analyzer`, `lighthouse-ci-integrator`
- Security: `security-header-generator`, `dependency-scanner`, `wcag-compliance-checker`
- Testing: `mock-generator`
- DevOps: `dockerfile-generator`, `github-actions-builder`, `kubernetes-manifest-generator`
- i18n: `translation-key-extractor`, `i18n-setup-wizard`
- Accessibility: `a11y-annotation-generator`
- Mobile: `app-icon-generator`
- Productivity: `regex-pattern-builder`
- Data Science: `jupyter-assistant`
- Web3: `smart-contract-generator`

### Slash Commands (39 Total)

**Starter Kit Commands:**
`/commit`, `/debug`, `/docs`, `/explain`, `/quickfix`, `/refactor`, `/review`, `/setup`, `/test`, `/todo`, `/clean`, `/deps`

**Intermediate Kit Commands:**
`/api-docs-generate`, `/bundle-analyze`, `/changelog-update`, `/coverage-report`, `/db-backup`, `/deploy`, `/dependency-update`, `/docker-build`, `/env-setup`, `/health-check`, `/migration-create`, `/performance-profile`, `/pr-creator`, `/security-audit`, `/version-bump`

### Subagents (14 Total)

**Generalist Agents:**
- `code-reviewer` - Comprehensive code review
- `test-writer` - Test generation expert
- `doc-writer` - Documentation specialist
- `debug-helper` - Debugging assistance

**Specialist Agents:**
- `api-designer` - REST/GraphQL API design
- `database-architect` - Database schema design
- `devops-engineer` - Infrastructure and deployment
- `performance-optimizer` - Performance tuning
- `security-auditor` - Security analysis
- `system-architect` - System design patterns

### MCP Integrations (20+ Available)

**Source Control:** GitHub, GitLab
**Databases:** PostgreSQL, MongoDB, MySQL, SQLite
**Communication:** Slack, Discord
**Cloud:** AWS, GCP, Azure
**Monitoring:** Sentry, Datadog, New Relic
**DevOps:** Docker, Kubernetes, Terraform

### Hooks (Event-Driven Automation)

**PreToolUse Hooks:**
- Secret detection (git commit)
- Force push prevention (main/master)
- .env file security checks
- Package installation reminders
- Docker cleanup confirmations
- Database migration confirmations
- Recursive delete protection

**PostToolUse Hooks:**
- File modification tracking
- Test failure alerts
- Build size monitoring

---

## 🎓 Skill Levels & Learning Path

### Level 1: Beginner (Starter Kit)
**Location:** `starter-kit/.claude/`
**Focus:** Learning fundamentals
**Rules:** `starter-kit/.claude/rules/`

Use when:
- New to Claude Code
- Learning AI-assisted development
- Building simple projects
- Need basic automation

### Level 2: Intermediate (Intermediate Kit)
**Location:** `intermediate-kit/.claude/`
**Focus:** Production-ready workflows
**Rules:** `intermediate-kit/.claude/rules/`

Use when:
- Building production applications
- Working with frameworks (React, Vue, Django, etc.)
- Need advanced automation
- Implementing CI/CD pipelines

### Level 3: Advanced (Examples)
**Location:** `examples/advanced/.claude/`
**Focus:** Complex integrations
**Rules:** `examples/advanced/.claude/rules/`

Use when:
- Building enterprise applications
- Implementing security compliance
- Performance optimization at scale
- Complex DevOps workflows

### Level 4: Master (Planned)
**Location:** `examples/master/.claude/`
**Focus:** Expert-level patterns
**Rules:** `examples/master/.claude/rules/`

Use when:
- Building distributed systems
- Custom framework development
- Advanced security implementations
- Complex architectural patterns

---

## 🔐 Security Guidelines

### Always Check Before:
- Committing `.env` files
- Force pushing to main/master
- Deleting files recursively
- Running database migrations
- Executing Docker operations

### Built-in Protections:
- Secret detection in commits
- Sensitive file warnings
- Destructive operation confirmations
- Package installation validation

---

## 🎯 Design Decisions

### Why This Structure?
1. **Progressive Learning** - Start simple, scale complexity
2. **Separation of Concerns** - Each kit serves specific needs
3. **Production-Ready** - All intermediate+ examples are battle-tested
4. **Security-First** - Built-in protections and validations
5. **Framework Agnostic** - Supports 25+ frameworks across 12+ languages

### Technology Choices
- **TypeScript First** - Modern React, Vue, Next.js examples
- **ORM Support** - Django, SQLAlchemy, Prisma patterns
- **Testing Focus** - Jest, pytest, vitest, Mocha coverage
- **Container Ready** - Docker, Kubernetes, multi-stage builds
- **CI/CD Native** - GitHub Actions, GitLab CI patterns

---

## 📚 Important Files to Reference

### Core Documentation
- `README.md` - Main project guide (377 lines)
- `IMPLEMENTATION_PROGRESS.md` - Detailed skill tracking (850+ lines)
- `SKILLS_STATUS.md` - Quick reference
- `MILESTONE_60_PERCENT.md` - Achievement summary

### Templates
- `templates/skill-template.md` - Create new skills
- `templates/command-template.md` - Create new commands
- `templates/subagent-template.md` - Create new agents

### Guides
- `resources/guides/getting-started.md` - Beginner guide
- `resources/guides/best-practices.md` - Best practices
- `resources/guides/security.md` - Security guidelines
- `resources/guides/troubleshooting.md` - Common issues

---

## 🚀 Quick Start References

### To Use Starter Kit:
```bash
cp -r starter-kit/.claude /path/to/your/project/
# Available: 5 skills, 12 commands, 4 agents
# See: starter-kit/.claude/rules/
```

### To Use Intermediate Kit:
```bash
cp -r intermediate-kit/.claude /path/to/your/project/
# Available: 10 skills, 15 commands, 6 agents
# See: intermediate-kit/.claude/rules/
```

### To Use Specific Skills:
```bash
cp examples/intermediate/performance-skills/bundle-analyzer/.claude/skills/bundle-analyzer.md \
   /path/to/your/project/.claude/skills/
```

---

## 🔍 Context Import Patterns

When working in specific areas, Claude Code will automatically import relevant context:

- **Root level** - This CLAUDE.md file
- **Kit level** - Kit-specific CLAUDE.md + rules
- **Subdirectory level** - Directory-specific rules on demand

---

## 📖 Rule Files Organization

Rules are organized hierarchically:

```
.claude/rules/
├── CLAUDE.md              # Level-specific overview
├── skills-reference.md    # All available skills
├── commands-reference.md  # All available commands
├── agents-reference.md    # All available subagents
├── hooks-reference.md     # Hook configurations
├── mcp-reference.md       # MCP server integrations
├── frameworks/            # Framework-specific rules
│   ├── react.md
│   ├── vue.md
│   ├── django.md
│   └── express.md
├── workflows/             # Workflow-specific rules
│   ├── testing.md
│   ├── deployment.md
│   ├── security.md
│   └── performance.md
└── domains/               # Domain-specific rules
    ├── frontend.md
    ├── backend.md
    ├── devops.md
    └── data-science.md
```

---

## 💡 Best Practices for This Project

### When Adding New Skills:
1. Choose appropriate level (beginner/intermediate/advanced)
2. Update IMPLEMENTATION_PROGRESS.md
3. Add to relevant rules directory
4. Test with multiple phrasings
5. Document in level-specific CLAUDE.md

### When Creating Examples:
1. Include comprehensive comments
2. Add README.md with usage
3. Reference in rules files
4. Test all code paths
5. Document security considerations

### When Modifying Configurations:
1. Test changes incrementally
2. Update relevant documentation
3. Check all references
4. Validate hook syntax
5. Verify MCP connections

---

## 🎭 Project Philosophy

**Education First** - Every configuration teaches a concept
**Production Ready** - All intermediate+ examples are tested
**Security Minded** - Built-in protections and validations
**Framework Agnostic** - Support diverse tech stacks
**Progressive Enhancement** - Start simple, scale up

---

## 🔗 External References

### Official Documentation
- Claude Code Docs: https://docs.claude.com/en/docs/claude-code/
- Skills Guide: https://docs.claude.com/en/docs/claude-code/skills
- Hooks Reference: https://docs.claude.com/en/docs/claude-code/hooks

### Community Resources
- GitHub Issues: https://github.com/anthropics/claude-code/issues
- Best Practices: (Community articles and guides)

---

**Last Updated:** 2025-11-01
**Project Status:** 60% Complete - 15/25 Niche Skills Implemented
**Maintainer:** Claudius Skills Project Team

