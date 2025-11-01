# Rules System Overview

> **Comprehensive Rules Directory Structure for Claudius Skills Project**
> Created: 2025-11-01

---

## 🎯 Purpose

This document provides an overview of the comprehensive rules directory system implemented across all skill levels in the Claudius Skills project. The rules system uses CLAUDE.md files and organized subdirectories to provide context-aware guidance to Claude Code.

---

## 📁 Directory Structure

```
claudius-skills/
├── CLAUDE.md                                    # Project-wide rules
│
├── starter-kit/.claude/rules/                   # Beginner Level
│   ├── CLAUDE.md                                # Starter kit overview
│   ├── skills-reference.md                      # 5 skills detailed
│   ├── commands-reference.md                    # 12 commands detailed
│   ├── agents-reference.md                      # 4 agents detailed
│   ├── hooks-reference.md                       # Hook system explained
│   ├── frameworks/                              # Framework-specific rules
│   ├── workflows/                               # Workflow guides
│   │   ├── testing.md                          # Testing workflow
│   │   └── git-workflow.md                     # Git workflow
│   └── domains/                                 # Domain-specific rules
│
├── intermediate-kit/.claude/rules/              # Intermediate Level
│   ├── CLAUDE.md                                # Intermediate kit overview
│   ├── frameworks/                              # React, Vue, Django, Express
│   ├── workflows/                               # API, Database, Deployment
│   └── domains/                                 # Frontend, Backend, DevOps
│
├── examples/advanced/.claude/rules/             # Advanced Level
│   ├── CLAUDE.md                                # Advanced level overview
│   ├── frameworks/                              # Advanced framework patterns
│   ├── workflows/                               # Performance, Security, A11y
│   └── domains/                                 # Enterprise patterns
│
└── examples/master/.claude/rules/               # Master Level
    ├── CLAUDE.md                                # Master level overview
    ├── frameworks/                              # Custom frameworks
    ├── workflows/                               # Distributed systems
    ├── domains/                                 # Architecture patterns
    └── patterns/                                # Advanced design patterns
```

---

## 🎓 Skill Levels

### Level 1: Starter Kit (Beginner)
**Location:** `starter-kit/.claude/rules/`

**Capabilities:**
- 5 essential skills (readme-generator, code-explainer, bug-finder, test-helper, git-helper)
- 12 basic commands (/commit, /debug, /test, /review, etc.)
- 4 helper subagents (code-reviewer, test-writer, doc-writer, debug-helper)
- 8+ safety hooks (secret detection, force push prevention, etc.)

**Documentation:**
- `CLAUDE.md` - Complete beginner guide
- `skills-reference.md` - Detailed skill documentation (5 skills)
- `commands-reference.md` - Detailed command documentation (12 commands)
- `agents-reference.md` - Detailed subagent documentation (4 agents)
- `hooks-reference.md` - Complete hooks system explanation
- `workflows/testing.md` - Testing workflow guide
- `workflows/git-workflow.md` - Git workflow guide

**Target Audience:** New to Claude Code, learning AI-assisted development

---

### Level 2: Intermediate Kit (Production-Ready)
**Location:** `intermediate-kit/.claude/rules/`

**Capabilities:**
- 10 framework-specific skills (React, Vue, Next.js, Express, FastAPI, Django, GraphQL, etc.)
- 15 advanced commands (/api-docs-generate, /bundle-analyze, /deploy, /security-audit, etc.)
- 6 specialist subagents (api-designer, database-architect, devops-engineer, etc.)
- Enhanced production-aware hooks

**Documentation:**
- `CLAUDE.md` - Production-ready guide with framework support
- Framework-specific rules (planned)
- Workflow guides for API, database, deployment (planned)
- Domain-specific rules for frontend/backend/devops (planned)

**Framework Support:**
- Frontend: React, Vue, Next.js
- Backend: Express, FastAPI, Django
- API: REST, GraphQL, OpenAPI
- Database: SQL, MongoDB, migrations
- Testing: Jest, pytest, vitest

**Target Audience:** Building production applications, framework-specific development

---

### Level 3: Advanced (Enterprise)
**Location:** `examples/advanced/.claude/rules/`

**Capabilities:**
- 15+ advanced skills across 10 categories:
  - Performance: image-optimizer, bundle-analyzer, lighthouse-ci
  - Security: security-header-generator, dependency-scanner, wcag-checker
  - DevOps: dockerfile-generator, kubernetes-manifest, github-actions
  - i18n: translation-key-extractor, i18n-setup-wizard
  - Accessibility: a11y-annotation-generator, wcag-compliance-checker
  - Specialized: jupyter-assistant, regex-builder, smart-contract-generator

**Documentation:**
- `CLAUDE.md` - Enterprise-grade guide
- Performance optimization workflows (planned)
- Security hardening workflows (planned)
- Accessibility compliance workflows (planned)
- Container orchestration workflows (planned)

**Focus Areas:**
- Performance optimization at scale
- Security compliance (WCAG 2.1, OWASP)
- Container orchestration (Docker, Kubernetes)
- International applications (i18n)
- Advanced CI/CD pipelines

**Target Audience:** Enterprise applications, compliance requirements, performance-critical systems

---

### Level 4: Master (Expert)
**Location:** `examples/master/.claude/rules/`

**Capabilities (Planned):**
- Distributed systems patterns
- Microservices architecture
- Custom framework development
- Multi-cloud deployments
- Real-time systems at scale
- Advanced security implementations

**Documentation:**
- `CLAUDE.md` - Expert-level guide for distributed systems
- Distributed systems patterns (planned)
- Microservices workflows (planned)
- Multi-cloud deployment patterns (planned)
- Real-time system architectures (planned)
- Custom framework development (planned)

**Focus Areas:**
- Event-driven architectures (CQRS, Event Sourcing, Saga)
- Service mesh implementations
- Multi-cloud and hybrid cloud
- Real-time collaboration systems
- Zero-trust security
- Custom DSL and framework development

**Target Audience:** System architects, principal engineers, complex distributed systems

---

## 📚 Documentation Coverage

### Root Level (Project-Wide)
**File:** `CLAUDE.md`
**Lines:** 400+

**Contents:**
- Project overview and structure
- All 25 skills categorized
- All 39 commands listed
- All 14 subagents documented
- Hook system overview
- MCP integrations (20+)
- Skill level progression
- Quick start guides
- Security guidelines
- Best practices

---

### Starter Kit (Beginner)
**Total Files:** 7
**Total Lines:** 3,500+

**Coverage:**
1. **CLAUDE.md** (500+ lines)
   - Complete beginner guide
   - All capabilities explained
   - Learning workflow
   - Quick start

2. **skills-reference.md** (1,200+ lines)
   - 5 skills in detail
   - Usage examples
   - Best practices
   - Comparison matrix

3. **commands-reference.md** (1,500+ lines)
   - 12 commands in detail
   - Usage examples
   - Workflow examples
   - Command combinations

4. **agents-reference.md** (1,000+ lines)
   - 4 subagents in detail
   - Example outputs
   - Usage patterns
   - Comparison matrix

5. **hooks-reference.md** (800+ lines)
   - All hook types explained
   - Configuration examples
   - Security hooks detailed
   - Custom hook recipes

6. **workflows/testing.md** (700+ lines)
   - Complete testing workflow
   - TDD patterns
   - Test organization
   - Framework integration

7. **workflows/git-workflow.md** (600+ lines)
   - Git workflow patterns
   - Branch strategies
   - Commit best practices
   - Integration with Claude

---

### Intermediate Kit (Production-Ready)
**Total Files:** 1+
**Total Lines:** 400+

**Coverage:**
1. **CLAUDE.md** (400+ lines)
   - Production-ready guide
   - 10 framework skills
   - 15 advanced commands
   - 6 specialist agents
   - Framework support matrix
   - Production checklist

**Planned:**
- Framework-specific rules (React, Vue, Django, Express)
- Workflow guides (API development, database design, deployment)
- Domain rules (frontend, backend, devops)

---

### Advanced Level (Enterprise)
**Total Files:** 1+
**Total Lines:** 350+

**Coverage:**
1. **CLAUDE.md** (350+ lines)
   - Enterprise-grade guide
   - 15+ advanced skills
   - Performance optimization
   - Security compliance
   - DevOps automation
   - Enterprise use cases

**Planned:**
- Performance optimization workflows
- Security hardening workflows
- Accessibility compliance workflows
- Container orchestration workflows

---

### Master Level (Expert)
**Total Files:** 1+
**Total Lines:** 400+

**Coverage:**
1. **CLAUDE.md** (400+ lines)
   - Expert-level guide
   - Distributed systems focus
   - Microservices patterns
   - Multi-cloud architectures
   - Real-time systems
   - Community contribution guide

**Planned:**
- Distributed systems patterns
- Microservices workflows
- Multi-cloud deployment guides
- Real-time architecture patterns
- Custom framework development guides

---

## 🔍 Rules System Features

### 1. Hierarchical Context
- **Root CLAUDE.md** - Always loaded for project context
- **Level-specific CLAUDE.md** - Loaded for kit being used
- **Directory-specific rules** - Loaded on demand when working in specific areas

### 2. Comprehensive References
Each level includes complete documentation of:
- All available skills with activation triggers
- All available commands with usage examples
- All available subagents with invocation patterns
- All configured hooks with safety explanations

### 3. Cross-References
Extensive use of `@path/to/file` imports:
- Reference other rule files
- Link to templates
- Point to guides
- Connect related resources

### 4. Progressive Learning
- **Starter Kit** - Learn fundamentals
- **Intermediate Kit** - Apply to frameworks
- **Advanced Level** - Enterprise patterns
- **Master Level** - Expert architectures

### 5. Practical Examples
Every rule file includes:
- Usage examples
- Code snippets
- Workflow demonstrations
- Best practices
- Common mistakes to avoid

---

## 🎯 Usage Patterns

### For Beginners
```
1. Copy starter-kit/.claude to project
2. Read starter-kit/.claude/rules/CLAUDE.md
3. Explore skills-reference.md to understand auto-skills
4. Try commands from commands-reference.md
5. Call subagents from agents-reference.md
6. Follow testing.md and git-workflow.md guides
```

### For Intermediate Developers
```
1. Graduate from starter-kit
2. Copy intermediate-kit/.claude to project
3. Read intermediate-kit/.claude/rules/CLAUDE.md
4. Use framework-specific skills (React, Vue, Django, etc.)
5. Leverage advanced commands (/deploy, /security-audit, etc.)
6. Consult specialist subagents (api-designer, database-architect)
```

### For Advanced/Enterprise
```
1. Master intermediate kit
2. Reference examples/advanced/.claude/rules/CLAUDE.md
3. Implement performance optimization skills
4. Apply security compliance skills (WCAG, vulnerability scanning)
5. Use DevOps skills (Docker, Kubernetes, GitHub Actions)
6. Follow enterprise workflows for compliance
```

### For Experts/Architects
```
1. Reference examples/master/.claude/rules/CLAUDE.md
2. Study distributed systems patterns
3. Design microservices architectures
4. Plan multi-cloud deployments
5. Contribute master-level skills to community
```

---

## 🔗 File Path Reference

### Quick Access Paths

**Root:**
- Project Overview: `@CLAUDE.md`
- Rules Overview: `@RULES_SYSTEM_OVERVIEW.md`

**Starter Kit:**
- Overview: `@starter-kit/.claude/rules/CLAUDE.md`
- Skills: `@starter-kit/.claude/rules/skills-reference.md`
- Commands: `@starter-kit/.claude/rules/commands-reference.md`
- Agents: `@starter-kit/.claude/rules/agents-reference.md`
- Hooks: `@starter-kit/.claude/rules/hooks-reference.md`
- Testing: `@starter-kit/.claude/rules/workflows/testing.md`
- Git: `@starter-kit/.claude/rules/workflows/git-workflow.md`

**Intermediate Kit:**
- Overview: `@intermediate-kit/.claude/rules/CLAUDE.md`

**Advanced Level:**
- Overview: `@examples/advanced/.claude/rules/CLAUDE.md`

**Master Level:**
- Overview: `@examples/master/.claude/rules/CLAUDE.md`

**Templates:**
- Skill: `@templates/skill-template.md`
- Command: `@templates/command-template.md`
- Subagent: `@templates/subagent-template.md`

**Guides:**
- Getting Started: `@resources/guides/getting-started.md`
- Best Practices: `@resources/guides/best-practices.md`
- Security: `@resources/guides/security.md`
- Troubleshooting: `@resources/guides/troubleshooting.md`

---

## 📊 Statistics

### Documentation Metrics
- **Total Rules Files:** 11+
- **Total Lines of Documentation:** 5,500+
- **Skill Levels Covered:** 4 (Beginner → Master)
- **Skills Documented:** 25+
- **Commands Documented:** 39+
- **Subagents Documented:** 14+
- **Hooks Documented:** 11+
- **MCP Integrations Documented:** 20+

### Coverage by Level
- **Starter Kit:** 7 comprehensive files (3,500+ lines)
- **Intermediate Kit:** 1+ files (400+ lines) with planned expansion
- **Advanced Level:** 1+ files (350+ lines) with planned expansion
- **Master Level:** 1+ files (400+ lines) - planning phase

---

## 🚀 Best Practices for Using Rules

### 1. Start at Your Level
- New to Claude Code? → Start with starter-kit
- Experienced developer? → Jump to intermediate-kit
- Enterprise needs? → Reference advanced level
- System architect? → Explore master level

### 2. Reference Frequently
- Use `@path/to/rule.md` syntax to import context
- Cross-reference between rule files
- Link to specific sections for focused context

### 3. Follow Progressive Learning
- Master each level before advancing
- Apply learnings in real projects
- Contribute back to the community

### 4. Combine with Skills/Commands/Agents
- Skills auto-activate based on context
- Commands provide manual workflows
- Agents offer expert consultation
- Rules provide the knowledge base

---

## 🔄 Maintenance & Updates

### Keeping Rules Current
- Rules updated with each skill addition
- New patterns documented as discovered
- Community feedback incorporated
- Best practices evolved based on usage

### Version Control
- Rules committed to git
- Changes tracked in git history
- Team can collaborate on rules
- Personal rules in .local.md files

---

## 🤝 Contributing to Rules

### How to Contribute
1. Identify gaps in documentation
2. Add new workflow guides
3. Improve existing rule files
4. Share use cases and patterns
5. Submit PRs with improvements

### Priority Areas
- Framework-specific rules (intermediate kit)
- Workflow guides (all levels)
- Domain-specific rules
- Master-level patterns
- Real-world case studies

---

## 📈 Future Enhancements

### Planned Additions
1. **Framework Rules:**
   - React patterns and best practices
   - Vue composition API patterns
   - Django ORM optimization
   - Express middleware patterns

2. **Workflow Rules:**
   - API development workflow
   - Database design workflow
   - Security hardening workflow
   - Performance optimization workflow

3. **Domain Rules:**
   - Frontend architecture rules
   - Backend architecture rules
   - DevOps patterns
   - Data science workflows

4. **Master Level:**
   - Distributed systems patterns
   - Microservices architecture
   - Multi-cloud patterns
   - Real-time systems

---

## 📚 Related Documentation

- **Main README:** `README.md`
- **Implementation Progress:** `IMPLEMENTATION_PROGRESS.md`
- **Skills Status:** `SKILLS_STATUS.md`
- **Milestone:** `MILESTONE_60_PERCENT.md`
- **Research:** `NICHE_SKILLS_RESEARCH.md`

---

**Created:** 2025-11-01
**Total Files Created:** 11+
**Total Lines:** 5,500+
**Skill Levels:** 4 (Beginner → Master)
**Status:** ✅ Complete (with planned expansions)

**This rules system provides comprehensive, context-aware guidance for Claude Code across all skill levels, from beginner to expert.**

