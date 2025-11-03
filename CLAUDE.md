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

**Current Status:** 🎉 100% COMPLETE (57 skills + 36 hooks + 80+ commands + 46 agents + 17 frameworks) ✨

---

## 📁 Project Structure

```
claudius-skills/
├── starter-kit/                  # Beginner-friendly (5 skills, 12 commands, 4 agents)
├── intermediate-kit/             # Production-ready (10 skills, 15 commands, 6 agents)
├── advanced-kit/                 # Enterprise-grade (15 skills, 20 commands, 10 agents) ✨
├── productivity-skills/          # Productivity workflows (6 skills, 13 commands, 4 agents)
│   ├── starter-kit/             # Basic productivity skills
│   └── intermediate-kit/        # Advanced productivity skills
├── competitive-ai-frameworks/    # AI competition tools (3 skills, 3 commands, 12 agents) 🆕
├── eliza-os-kit/                # ElizaOS integration (6 skills, 8 commands, 6 agents) 🆕
├── examples/                     # Multi-level examples (Beginner → Master)
│   ├── beginner/                # Learning-focused examples (10+ categories)
│   ├── intermediate/            # Production patterns (17+ categories)
│   ├── advanced/                # Complex integrations (emerging tech, devops)
│   └── master/                  # Master-level patterns
├── framework-rules/             # Modern web framework rules (8 frameworks)
├── hooks-collection/            # Production hooks (25 hooks across 5 categories)
├── modern-commands/             # Modern workflow commands (10 commands)
├── specialized-agents/          # Specialized consultant agents (4 agents)
├── skool/                       # Educational content & tutorials
├── skool-courses/               # Structured course curriculum (3 levels)
├── templates/                   # Reusable templates
└── resources/                   # Guides and tutorials
```

---

## 🛠️ Available Capabilities

### Skills (55 Total Across All Kits)

**Core Skills (2 essential skills - use across all kits):**
- `version-checker` - Verifies package versions, API compatibility, and breaking changes to ensure knowledge cutoff assumptions are accurate
- `class-builder` - Generates strictly-typed TypeScript classes with encapsulation, validation, and type safety

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

**Productivity Skills Kit (6 skills):**
- `brainstorm-facilitator` - Creative brainstorming and ideation
- `email-composer` - Professional email drafting
- `meeting-notes-formatter` - Structured meeting notes
- `report-generator` - Report creation and formatting
- `task-breakdown` - Project task decomposition
- `strategic-planner` - Strategic planning and roadmaps

**Competitive AI Frameworks Kit (3 skills) 🆕:**
- `bug-hunting-simulator` - Simulated bug hunting competitions
- `code-quality-analyzer` - Competitive code quality analysis
- `user-flow-tester` - User flow testing automation

**Eliza OS Kit (6 skills) 🆕:**
- `character-generator` - ElizaOS character creation
- `deployment-helper` - ElizaOS deployment automation
- `knowledge-base-builder` - Knowledge base management
- `memory-manager` - Memory system optimization
- `plugin-builder` - Plugin scaffolding and development
- `testing-helper` - ElizaOS testing utilities

### Slash Commands (80+ Total Across All Kits)

**Starter Kit Commands:**
`/commit`, `/debug`, `/docs`, `/explain`, `/quickfix`, `/refactor`, `/review`, `/setup`, `/test`, `/todo`, `/clean`, `/deps`

**Intermediate Kit Commands:**
`/api-docs-generate`, `/bundle-analyze`, `/changelog-update`, `/coverage-report`, `/db-backup`, `/deploy`, `/dependency-update`, `/docker-build`, `/env-setup`, `/health-check`, `/migration-create`, `/performance-profile`, `/pr-creator`, `/security-audit`, `/version-bump`

**Advanced Kit Commands (20 advanced):**
`/release-orchestrator`, `/canary-deploy`, `/blue-green-deploy`, `/rollback-emergency`, `/feature-flag-toggle`, `/compliance-scan`, `/adr-create`, `/sla-report`, `/security-posture`, `/cost-analysis`, `/incident-declare`, `/runbook-execute`, `/postmortem-generate`, `/oncall-schedule`, `/environment-clone`, `/data-migration`, `/traffic-replay`, `/load-test-suite`, `/dependency-graph`, `/tech-debt-audit`

**Productivity Skills Commands (13):**
`/agenda`, `/decision`, `/email`, `/goal-setting`, `/journal`, `/minutes`, `/outline`, `/presentation`, `/prioritize`, `/schedule`, `/summarize`, `/weekly-review`

**Competitive AI Frameworks Commands (3) 🆕:**
`/run-bug-hunt`, `/run-flow-test`, `/run-quality-check`

**Eliza OS Kit Commands (8) 🆕:**
`/analyze-conversations`, `/build-plugin`, `/deploy-agent`, `/dev-agent`, `/optimize-memory`, `/sync-knowledge`, `/test-character`, `/validate-character`

**Modern Commands (10):**
`/train-model`, `/evaluate-model`, `/optimize-pipeline`, `/setup-data-pipeline`, `/deploy-edge`, `/setup-dashboards`, `/trace-request`, `/create-golden-path`, `/scaffold-service`, `/audit-security`

### Subagents (46 Total Across All Kits)

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

**Productivity Skills Agents (4):**
- `content-writer` - Content creation and writing
- `creative-consultant` - Creative ideation and brainstorming
- `productivity-coach` - Workflow optimization
- `project-coordinator` - Project management assistance

**Competitive AI Frameworks Agents (12) 🆕:**
- **Team 1:** `team-1-coordinator`, `team-1-tester`, `team-1-reviewer`, `team-1-documenter`
- **Team 2:** `team-2-coordinator`, `team-2-tester`, `team-2-reviewer`, `team-2-documenter`
- **Team 3:** `team-3-coordinator`, `team-3-tester`, `team-3-reviewer`, `team-3-documenter`

**Eliza OS Kit Agents (6) 🆕:**
- `character-designer` - Character design and personality
- `deployment-engineer` - Deployment and infrastructure
- `integration-specialist` - Third-party integrations
- `memory-architect` - Memory system design
- `plugin-architect` - Plugin architecture and design
- `testing-specialist` - Testing strategies and automation

**Specialized Agents (4):**
- `edge-computing-specialist` - Edge deployment and optimization
- `ml-ops-engineer` - MLOps and model deployment
- `platform-architect` - Platform engineering
- `webassembly-expert` - WebAssembly optimization

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

*Performance Monitoring (5):*
- `build-size-alert` - Monitors bundle size increases
- `ci-time-tracking` - Tracks CI/CD pipeline duration
- `memory-leak-warning` - Detects potential memory leaks
- `n-plus-one-query-detection` - Identifies N+1 query patterns
- `slow-test-detection` - Flags slow test execution

**Knowledge Cutoff Awareness (5 NEW!) 🆕:**
- `package-installation-verification` - Verifies package versions before installation
- `import-usage-verification` - Checks import/export structure before writing code
- `api-endpoint-verification` - Validates API endpoints before use
- `framework-feature-verification` - Confirms framework features before implementation
- `type-definition-verification` - Verifies TypeScript types before use

**Strict Typing & Class Patterns (6 NEW!) 🆕:**
- `no-any-type` - Prevents use of `any` type (ERROR)
- `prefer-classes-over-interfaces` - Enforces classes for data structures
- `explicit-return-types` - Requires return types on all functions
- `no-non-null-assertions` - Prevents non-null assertions (!)
- `explicit-variable-types` - Requires type annotations on all variables
- `class-property-initialization` - Ensures all properties are initialized

**Location:** `hooks-collection/` with comprehensive README
**Total:** 36 hooks across 7 categories

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
**Focus:** Master-level patterns and plugin ecosystems
**Rules:** `examples/master/.claude/rules/`

Use when:
- Building distributed systems
- Custom framework development
- Advanced security implementations
- Complex architectural patterns
- Creating reusable plugin ecosystems

### Specialized Kits

#### Productivity Skills Kit
**Location:** `productivity-skills/.claude/`
**Focus:** Personal and team productivity
**Contents:** 6 skills, 13 commands, 4 agents

Use when:
- Managing meetings and documentation
- Writing professional communications
- Planning projects and strategies
- Breaking down complex tasks
- Improving personal productivity workflows

**Quick Start:**
```bash
cp -r productivity-skills/starter-kit/.claude /path/to/your/project/
# Use brainstorm-facilitator for ideation
/agenda "Team planning session"
```

#### Competitive AI Frameworks Kit 🆕
**Location:** `competitive-ai-frameworks/.claude/`
**Focus:** AI-powered code competitions
**Contents:** 3 skills, 3 commands, 12 team-based agents

Use when:
- Participating in coding competitions
- Running simulated bug hunts
- Competitive code quality analysis
- Team-based development challenges
- User flow testing competitions

**Quick Start:**
```bash
cp -r competitive-ai-frameworks/.claude /path/to/your/project/
/run-bug-hunt
# Team-based agents will coordinate the competition
```

#### Eliza OS Kit 🆕
**Location:** `eliza-os-kit/.claude/`
**Focus:** ElizaOS agent and character development
**Contents:** 6 skills, 8 commands, 6 specialist agents

Use when:
- Building ElizaOS characters and agents
- Developing ElizaOS plugins
- Managing character knowledge bases
- Optimizing memory systems
- Deploying ElizaOS agents

**Quick Start:**
```bash
cp -r eliza-os-kit/.claude /path/to/elizaos/project/
Use character-generator to create a new character
/dev-agent "Start ElizaOS development environment"
```

**Documentation:**
- `eliza-os-kit/.claude/rules/CLAUDE.md` - Complete ElizaOS integration guide
- `eliza-os-kit/.claude/rules/elizaos-core-runtime.md` - Runtime documentation
- `eliza-os-kit/.claude/rules/elizaos-plugin-patterns.md` - Plugin development patterns
- `eliza-os-kit/.claude/rules/plugin-registry.md` - Plugin registry reference

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

## ⚠️ Knowledge Cutoff Awareness

### CRITICAL: AI Model Knowledge Has Cutoff Dates

**Your knowledge cutoff:** January 2025 (Claude Sonnet 4.5) or July 2025 (future models)

**What this means:**
- Package versions, APIs, and types may have changed since your training
- Framework features may be deprecated or replaced
- Security vulnerabilities may exist in versions you suggest
- Breaking changes may have occurred in dependencies

### Verification Protocol - ALWAYS FOLLOW

**Before using ANY package, API, or framework feature:**

1. **Check current versions** - Don't assume your knowledge is current
   ```bash
   npm view <package> version
   pip index versions <package>
   ```

2. **Verify API compatibility** - Endpoints and methods change
   ```bash
   npm view <package> readme
   # Or use WebFetch to check official docs
   ```

3. **Review breaking changes** - Check changelogs since cutoff
   ```bash
   npm view <package> versions --json
   # Look for major version bumps
   ```

4. **Ask users about their versions** - When uncertain, confirm
   ```
   "What version of [framework] are you using? My knowledge
   cutoff is [date], so I want to ensure compatibility."
   ```

### Knowledge Cutoff Hooks

**Automatic reminders via hooks:**
- `package-installation-verification` - Before npm/pip/yarn commands
- `import-usage-verification` - Before writing import statements
- `api-endpoint-verification` - Before using third-party APIs
- `framework-feature-verification` - Before framework-specific code
- `type-definition-verification` - Before TypeScript type usage

**Location:** `hooks-collection/knowledge-cutoff/`

### Version Checker Skill

**Use the `version-checker` skill to:**
- Verify package versions before installation
- Check for breaking changes since cutoff
- Validate API endpoint compatibility
- Confirm TypeScript type definitions are current
- Review framework feature compatibility

**Activation:**
- "check version of [package]"
- "verify [API] is still valid"
- "check for breaking changes in [package]"

### High-Risk Areas - ALWAYS Verify

**Critical packages that change frequently:**
- 🔐 **Security/Auth:** Auth0, NextAuth, Passport, OAuth libraries
- 💳 **Payments:** Stripe, PayPal, Square (errors = financial loss)
- ☁️ **Cloud SDKs:** AWS, GCP, Azure (breaking changes common)
- ⚛️ **Frameworks:** React, Next.js, Vue, Angular (rapid evolution)
- 🗄️ **ORMs:** Prisma, TypeORM, Sequelize (query syntax changes)
- 🔨 **Build Tools:** Vite, Webpack, esbuild (config changes)
- 🧪 **Testing:** Jest, Vitest, Playwright (API updates)

### The Golden Rule

**"When in doubt, verify. Never assume your knowledge is current."**

Better to:
1. Acknowledge uncertainty
2. Verify current information
3. Implement with confidence

Than to:
1. Assume knowledge is current
2. Implement outdated patterns
3. Cause bugs and frustration

### Documentation

**See:** `.claude/rules/knowledge-cutoff-awareness.md` for complete verification protocol

---

## 🔧 Strict Type Checking & Class-Based Patterns

### CRITICAL: TypeScript Strict Mode Required

This project enforces **STRICT TYPE CHECKING** and **CLASS-BASED ARCHITECTURE**.

**Core principles:**
1. **Zero tolerance for `any`** - All types must be explicit
2. **Classes over interfaces** - Use classes for all data structures
3. **Explicit return types** - All functions must declare return types
4. **No non-null assertions** - Handle undefined/null explicitly
5. **Initialize all properties** - No undefined class fields
6. **Explicit variable types** - No reliance on type inference

### Strict Typing Hooks (6 NEW!) 🆕

**Automatic enforcement of strict patterns:**
- `no-any-type` - Prevents use of `any` type (ERROR)
- `prefer-classes-over-interfaces` - Enforces classes for data structures
- `explicit-return-types` - Requires return types on all functions
- `no-non-null-assertions` - Prevents non-null assertions (!)
- `explicit-variable-types` - Requires type annotations on all variables
- `class-property-initialization` - Ensures all properties are initialized

**Location:** `hooks-collection/strict-typing/`

### Class Builder Skill

**Use the `class-builder` skill to:**
- Generate strictly-typed domain entities
- Create value objects with validation
- Build service classes with dependency injection
- Generate repository classes
- Create proper DTOs for serialization

**Activation:**
- "create a class for [entity]"
- "generate [Model] class"
- "build TypeScript class for [domain object]"

### When to Use Classes vs Interfaces

**✅ ALWAYS use classes for:**
- Domain entities (User, Product, Order)
- Value objects (Email, Money, Address)
- Services (UserService, EmailService)
- Repositories (UserRepository)
- Any data structure with behavior

**✅ Interfaces ONLY for:**
- Service contracts (IEmailService, IUserRepository)
- Polymorphic behavior (IHandler, IProcessor)
- Third-party API contracts

**❌ NEVER use interfaces for:**
- Data structures
- Domain models
- DTOs (use `type` instead)

### Why Classes Over Interfaces?

**Benefits of classes:**
- ✅ Encapsulation with private fields
- ✅ Validation logic lives with data
- ✅ Constructor guarantees valid state
- ✅ Runtime type checking (`instanceof`)
- ✅ Methods and data together
- ✅ Single source of truth

**Problems with interfaces:**
- ❌ No encapsulation
- ❌ No validation
- ❌ No behavior/methods
- ❌ Compile-time only
- ❌ Easy to create invalid states

### Configuration Templates

**TypeScript:** `templates/tsconfig.strict.json`
- All strict compiler options enabled
- `strictNullChecks`, `noImplicitAny`, `strictPropertyInitialization`
- Additional checks: `noUncheckedIndexedAccess`, `noImplicitOverride`

**ESLint:** `templates/.eslintrc.strict.json`
- Enforces explicit types everywhere
- No `any` allowed
- Explicit return types required
- No non-null assertions
- Naming conventions (private fields with `_` prefix, interfaces with `I` prefix)

### Documentation

**See:** `.claude/rules/strict-typing-class-patterns.md` for complete guidelines

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

### Additional Resources

#### Modern Commands Collection
**Location:** `modern-commands/`
**Contents:** 10 modern workflow commands organized by domain
**Domains:** ai-ml-workflows, data, devops, edge-operations, observability, platform-engineering, security

Modern commands are organized as standalone markdown files outside the `.claude` structure for easy distribution and customization.

#### Specialized Agents
**Location:** `specialized-agents/`
**Contents:** 4 specialized consultant agents
- `edge-computing-specialist` - Edge deployment expertise
- `ml-ops-engineer` - MLOps and model lifecycle
- `platform-architect` - Platform engineering
- `webassembly-expert` - WebAssembly optimization

These agents can be integrated into any kit for specialized consulting on advanced topics.

#### Framework Rules
**Location:** `framework-rules/`
**Contents:** 8 modern web framework rules
**Frameworks:** Angular, Astro, Fresh, Nuxt3, Qwik, Remix, SolidJS, SvelteKit

Copy framework-specific rules to your `.claude/rules/frameworks/` directory for framework-optimized assistance.

#### Educational Content
**Skool Directory:** `skool/`
- Advanced tutorials
- Framework guides
- Game development genres
- Marketing strategies
- Project showcases
- Monetization strategies

**Skool Courses:** `skool-courses/`
- Structured curriculum with 3 levels (Beginner → Intermediate → Advanced)
- Downloadable templates
- Bonus resources
- Complete course materials

---

**Last Updated:** 2025-11-02
**Project Status:** 100% COMPLETE - All Documented (55 skills, 80+ commands, 25 hooks, 46 agents, 17 frameworks)
**Maintainer:** Claudius Skills Project Team

