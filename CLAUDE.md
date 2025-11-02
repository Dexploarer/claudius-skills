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

**Current Status:** 🎉 100% COMPLETE (50 skills + 35 hooks + 57 commands + 18 agents + 14 frameworks) ✨

---

## 📁 Project Structure

```
claudius-skills/
├── starter-kit/          # Beginner-friendly (5 skills, 12 commands, 4 agents)
├── intermediate-kit/     # Production-ready (10 skills, 15 commands, 6 agents)
├── advanced-kit/         # Enterprise-grade (15 skills, 20 commands, 10 agents) ✨
├── examples/             # Multi-level examples (Beginner → Master)
│   ├── beginner/        # Learning-focused examples
│   ├── intermediate/    # Production patterns
│   ├── advanced/        # Complex integrations
│   └── master/          # Advanced-level (planned)
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

**Niche Skills (25 implemented):**
- Performance: `image-optimizer`, `bundle-analyzer`, `lighthouse-ci-integrator`, `database-query-optimizer`
- Security: `security-header-generator`, `dependency-scanner`, `pii-detector`, `wcag-compliance-checker`
- Testing: `mock-generator`, `property-based-test-generator`, `visual-regression-setup`
- DevOps: `dockerfile-generator`, `github-actions-builder`, `kubernetes-manifest-generator`, `terraform-module-builder`
- i18n: `translation-key-extractor`, `i18n-setup-wizard`
- Accessibility: `a11y-annotation-generator`, `wcag-compliance-checker`
- Mobile: `app-icon-generator`, `react-native-component-generator`
- Productivity: `regex-pattern-builder`
- Data Science: `jupyter-assistant`, `data-cleaning-pipeline`
- Web3: `smart-contract-generator`
- Graphics: `threejs-scene-builder`

**Emerging Tech Skills (10 NEW!):**
- AI/ML: `ai-ml-ops` (MLflow, Kubeflow, feature stores)
- Edge: `edge-deployment` (Cloudflare, Vercel, Fastly)
- Performance: `webassembly-optimizer` (Rust/WASM, browser integration)
- API: `graphql-federation` (Apollo Federation, distributed schemas)
- DevOps: `feature-flags`, `serverless-patterns`, `event-streaming`
- Security: `api-rate-limiter` (Redis, token bucket, sliding window)
- SaaS: `multi-tenant-architect` (isolation strategies, data partitioning)
- Quantum: `quantum-setup` (Qiskit, Cirq, Q#)

**Advanced Kit (15 enterprise skills):**
- Architecture: `microservices-orchestrator`, `api-gateway-configurator`, `event-driven-architect`, `service-mesh-integrator`
- Compliance: `compliance-auditor`, `architecture-decision-recorder`, `sla-monitor-generator`, `disaster-recovery-planner`
- Observability: `distributed-tracing-setup`, `metrics-pipeline-builder`, `log-aggregation-configurator`, `chaos-engineering-setup`
- Platform: `internal-platform-builder`, `developer-portal-generator`, `golden-path-creator`

### Slash Commands (39 Total)

**Starter Kit Commands:**
`/commit`, `/debug`, `/docs`, `/explain`, `/quickfix`, `/refactor`, `/review`, `/setup`, `/test`, `/todo`, `/clean`, `/deps`

**Intermediate Kit Commands:**
`/api-docs-generate`, `/bundle-analyze`, `/changelog-update`, `/coverage-report`, `/db-backup`, `/deploy`, `/dependency-update`, `/docker-build`, `/env-setup`, `/health-check`, `/migration-create`, `/performance-profile`, `/pr-creator`, `/security-audit`, `/version-bump`

**Advanced Kit Commands (20 advanced):**
`/release-orchestrator`, `/canary-deploy`, `/blue-green-deploy`, `/rollback-emergency`, `/feature-flag-toggle`, `/compliance-scan`, `/adr-create`, `/sla-report`, `/security-posture`, `/cost-analysis`, `/incident-declare`, `/runbook-execute`, `/postmortem-generate`, `/oncall-schedule`, `/environment-clone`, `/data-migration`, `/traffic-replay`, `/load-test-suite`, `/dependency-graph`, `/tech-debt-audit`

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

**Advanced Kit Agents (10 consultants):**
- Architecture: `enterprise-architect`, `distributed-systems-architect`, `data-architect`, `platform-engineer`
- Operations: `sre-consultant`, `incident-commander`, `chaos-engineer`, `finops-analyst`
- Compliance: `compliance-officer`, `security-architect`

### MCP Integrations (20+ Available)

**Source Control:** GitHub, GitLab
**Databases:** PostgreSQL, MongoDB, MySQL, SQLite
**Communication:** Slack, Discord
**Cloud:** AWS, GCP, Azure
**Monitoring:** Sentry, Datadog, New Relic
**DevOps:** Docker, Kubernetes, Terraform

### Hooks (Event-Driven Automation)

**Example Hooks (10):**
- Secret detection (git commit)
- Force push prevention (main/master)
- .env file security checks
- Package installation reminders
- Docker cleanup confirmations
- Database migration confirmations
- Recursive delete protection
- File modification tracking
- Test failure alerts
- Build size monitoring

**Production Hooks Collection (20 NEW!):**

*Development Safety (5):*
- `prevent-force-push` - Blocks force pushes to protected branches
- `env-file-protection` - Prevents committing .env and credentials
- `large-file-warning` - Warns about files >10MB (Git LFS suggestion)
- `destructive-operation-confirm` - Confirms rm -rf, DROP TABLE, etc.
- `package-install-check` - Validates package installations

*Production Deployment (5):*
- `pre-deploy-checklist` - Enforces comprehensive deployment checklist
- `database-migration-safety` - Ensures backups before migrations
- `deployment-notification` - Notifies team after deployments
- `blue-green-validation` - Validates traffic switching
- `feature-flag-deployment` - Encourages feature flag usage

*Code Quality (5):*
- `test-coverage-enforcement` - Enforces minimum coverage (80%)
- `linting-enforcement` - Blocks commits with lint errors
- `commit-message-standards` - Enforces conventional commits
- `documentation-check` - Ensures code documentation
- `code-complexity-warning` - Warns about high cyclomatic complexity

*Security Enforcement (5):*
- `secret-scanning` - Detects API keys, tokens, passwords
- `dependency-vulnerability-scan` - Checks for CVEs
- `security-headers-check` - Validates CSP, CORS, security headers
- `license-compliance-check` - Checks for incompatible licenses (GPL, etc.)
- `cors-configuration-check` - Validates CORS settings

**Location:** `hooks-collection/` with comprehensive README

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

### Level 4: Advanced Pack (Enterprise) ✨
**Location:** `advanced-kit/.claude/`
**Focus:** Enterprise-grade systems
**Rules:** `advanced-kit/.claude/rules/CLAUDE.md`

Use when:
- Building enterprise distributed systems (microservices, event-driven)
- Requiring compliance frameworks (SOC2, HIPAA, GDPR, PCI-DSS)
- Implementing full observability stacks (tracing, metrics, logging)
- Building internal developer platforms
- Managing multi-cloud architectures
- Orchestrating complex deployments
- Leading technical teams and initiatives

**Capabilities:**
- 15 enterprise skills (architecture, compliance, observability, platform)
- 20 advanced commands (deployment, incident response, compliance)
- 10 specialist consultant agents (architects, SRE, compliance, security)
- Production-critical hooks (compliance enforcement, cost monitoring)
- Full compliance automation (SOC2, HIPAA, GDPR, PCI-DSS)

**Quick Start:**
```bash
cp -r advanced-kit/.claude /path/to/enterprise/project/
Use enterprise-architect to design the architecture
/compliance-scan soc2
```

### Level 5: Master (Examples)
**Location:** `examples/master/.claude/`
**Focus:** Advanced-level patterns and plugin ecosystems
**Rules:** `examples/master/.claude/rules/`

Use when:
- Building distributed systems
- Custom framework development
- Advanced security implementations
- Complex architectural patterns
- Creating reusable plugin ecosystems

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

