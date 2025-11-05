# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## 🎯 Repository Purpose

**Claudius Skills** is a production-ready collection of Claude Code extensibility configurations covering all five pillars of extensibility:
- **Skills** - Context-aware capabilities (87 skills)
- **Slash Commands** - Manual workflow shortcuts (80+ commands)
- **Hooks** - Event-driven automation (36 hooks)
- **Subagents** - Specialized AI consultants (46 agents)
- **MCP Servers** - External service integrations (20+)

This is a **documentation and configuration repository** - not a code repository. The "code" here consists of:
- Markdown skill definitions
- Markdown command definitions
- Markdown agent definitions
- Shell script hooks
- JSON configuration files
- Educational content and examples

---

## 🏗️ Repository Architecture

### Progressive Learning Structure

The repository is organized in **progressive levels** from beginner to master:

```
Level 1: Starter Kit       → 5 skills, 12 commands, 4 agents
Level 2: Intermediate Kit  → 10 skills, 15 commands, 6 agents
Level 3: Advanced Examples → 25 niche + 10 emerging tech skills
Level 4: Advanced Kit      → 15 enterprise skills, 20 commands, 10 agents
Level 5: Master Examples   → Complex patterns and architectures
```

### Directory Structure

```
claudius-skills/
├── .claude/                           # Root-level core skills
│   ├── skills/                       # 2 core skills (version-checker, class-builder)
│   └── rules/                        # 2 critical rules
│       ├── knowledge-cutoff-awareness.md
│       └── strict-typing-class-patterns.md
│
├── starter-kit/.claude/              # Level 1: Beginner (5 skills)
├── intermediate-kit/.claude/         # Level 2: Production (10 skills)
├── advanced-kit/.claude/             # Level 4: Enterprise (15 skills)
│
├── productivity-skills/              # Specialized: Productivity workflows
│   ├── starter-kit/.claude/         # 5 productivity skills
│   └── intermediate-kit/.claude/    # 1 advanced productivity skill
│
├── competitive-ai-frameworks/.claude/ # Specialized: AI competitions (3 skills, 12 agents)
├── eliza-os-kit/.claude/             # Specialized: ElizaOS integration (6 skills)
├── railway-deployment-kit/.claude/   # Specialized: Railway.app deployment (5 skills)
│
├── examples/                         # Learning examples by level
│   ├── beginner/                    # Level 1: 7 example skills
│   ├── intermediate/                # Level 2: 19 niche skills
│   ├── advanced/                    # Level 3: 14 emerging tech + complex skills
│   └── master/                      # Level 5: Master patterns
│
├── hooks-collection/                 # 36 production hooks (7 categories)
├── framework-rules/                  # 17 framework integrations
├── modern-commands/                  # 10 modern workflow commands
├── specialized-agents/               # 4 specialized consultants
├── templates/                        # Templates for creating new components
└── docs/                            # Consolidated documentation
```

### The `.claude/` Pattern

Each kit follows this structure:
```
[kit-name]/.claude/
├── skills/         # Skill definitions (.md files)
├── commands/       # Slash commands (.md files)
├── agents/         # Subagent definitions (.md files)
├── hooks/          # Event automation (optional)
└── rules/          # Configuration rules
    ├── CLAUDE.md   # Kit-specific overview
    └── frameworks/ # Framework-specific rules
```

---

## 🔧 Common Development Tasks

### Analyzing Skill Coverage

```bash
# Count all skill files
find . -name "*.md" -path "*/.claude/skills/*" | wc -l

# List skills by kit
ls -1 starter-kit/.claude/skills/
ls -1 intermediate-kit/.claude/skills/
ls -1 advanced-kit/.claude/skills/

# Find example skills (SKILL.md pattern)
find examples/ -name "SKILL.md"
```

### Validating Structure

```bash
# Check for required kit structure
for kit in starter-kit intermediate-kit advanced-kit; do
  echo "=== $kit ==="
  ls -la $kit/.claude/
done

# Verify hook categories
ls -1 hooks-collection/

# List framework rules
ls -1 framework-rules/
```

### Testing Configurations

To test a specific kit:
```bash
# Copy kit to a test project
cp -r starter-kit/.claude /path/to/test/project/

# Or test intermediate kit
cp -r intermediate-kit/.claude /path/to/test/project/

# Start Claude Code in test project
cd /path/to/test/project && claude
```

### Documentation Updates

When updating documentation:
```bash
# Main documentation files to update:
# - README.md (user-facing overview)
# - CLAUDE.md (this file - Claude Code guidance)
# - IMPLEMENTATION_PROGRESS.md (detailed skill tracking)
# - SKILLS_REFERENCE.md (complete skills directory)
# - CHANGELOG.md (version history)

# Kit-specific documentation:
# - [kit]/.claude/rules/CLAUDE.md
# - [kit]/.claude/rules/skills-reference.md
```

---

## 📐 Design Patterns

### Skill Definition Pattern

Skills use markdown with this structure:
```markdown
---
name: skill-name
description: Brief description
---

# Skill Name

## Purpose
What this skill does

## Activation
When to activate (phrases, patterns)

## Instructions
Step-by-step instructions for Claude Code

## Examples
Usage examples
```

### Command Pattern

Commands use markdown with kebab-case naming:
```markdown
# Command Name

## Description
What this command does

## Usage
/command-name [arguments]

## Implementation
How to execute this command
```

### Agent Pattern

Agents define specialized consultants:
```markdown
# Agent Name

## Expertise
Domain of expertise

## When to Use
Situations to activate this agent

## Workflow
How this agent operates
```

### Hook Pattern

Hooks use shell scripts with JSON configuration:
```json
{
  "type": "hook-type",
  "description": "What this hook does",
  "match": "pattern-to-match"
}
```

---

## 🎯 File Organization Principles

### 1. Kit-Based vs Example-Based

**Kit-Based** (`.claude/skills/*.md`):
- Comprehensive, production-ready implementations
- 200-300+ lines of detailed guidance
- Multiple activation phrases
- Framework-specific examples
- Used when copying entire kits

**Example-Based** (`examples/*/SKILL.md`):
- Learning-focused, concise implementations
- 100-150 lines
- Quick reference format
- Progressive complexity
- Used for understanding patterns

### 2. Duplicate Implementations

10 skills have both kit and example versions:
- api-documentation-generator
- database-migration-helper
- django-model-helper
- express-api-generator
- fastapi-generator
- graphql-schema-generator
- nextjs-page-generator
- react-component-generator
- testing-framework-helper
- vue-component-generator

**Why?** Kit versions for production use, example versions for learning.

### 3. Hook Organization

Hooks are organized by category:
```
hooks-collection/
├── development-safety/     # 5 hooks (prevent mistakes)
├── production-deployment/  # 5 hooks (deployment safety)
├── code-quality/          # 5 hooks (enforce standards)
├── security-enforcement/  # 5 hooks (security checks)
├── performance-monitoring/# 5 hooks (performance tracking)
├── knowledge-cutoff/      # 5 hooks (verify assumptions)
└── strict-typing/         # 6 hooks (TypeScript strict mode)
```

---

## ⚠️ Critical Safety Systems

### 1. Knowledge Cutoff Awareness

**Location:** `.claude/rules/knowledge-cutoff-awareness.md`

Claude Code MUST verify current information before using packages, APIs, or frameworks:

**Verification Protocol:**
1. Check current package versions
2. Verify API compatibility
3. Review breaking changes since knowledge cutoff
4. Ask users about their versions when uncertain

**Hooks:** 5 hooks in `hooks-collection/knowledge-cutoff/`
- `package-installation-verification.json`
- `import-usage-verification.json`
- `api-endpoint-verification.json`
- `framework-feature-verification.json`
- `type-definition-verification.json`

**Skill:** `version-checker` in `.claude/skills/`

### 2. Strict TypeScript Type Checking

**Location:** `.claude/rules/strict-typing-class-patterns.md`

This project enforces:
- Zero `any` types
- Explicit return types on all functions
- Classes over interfaces for data structures
- No non-null assertions
- Full property initialization

**Hooks:** 6 hooks in `hooks-collection/strict-typing/`
- `no-any-type.json`
- `prefer-classes-over-interfaces.json`
- `explicit-return-types.json`
- `no-non-null-assertions.json`
- `explicit-variable-types.json`
- `class-property-initialization.json`

**Skill:** `class-builder` in `.claude/skills/`

**Templates:**
- `templates/tsconfig.strict.json` - TypeScript strict config
- `templates/.eslintrc.strict.json` - ESLint strict rules

---

## 📊 Skill Distribution

Total: 87 unique skills

**By Level:**
- Core: 2 skills (2.3%)
- Beginner: 13 skills (15%)
- Intermediate: 35 skills (40%)
- Advanced: 25 skills (29%)
- Specialized: 15 skills (17%)

**By Domain:**
- Frontend Development: 15 skills
- Backend Development: 12 skills
- DevOps/Infrastructure: 14 skills
- Testing/Quality: 7 skills
- Security: 6 skills
- Data/AI: 5 skills
- Productivity: 7 skills
- Observability: 4 skills
- Platform Engineering: 10 skills
- Other: 7 skills

**By Kit:**
- Starter Kit: 5 skills
- Intermediate Kit: 10 skills
- Advanced Kit: 15 skills
- Productivity: 6 skills
- Competitive AI: 3 skills
- Eliza OS: 6 skills
- Railway Deployment: 5 skills
- Niche Skills (examples): 25 skills
- Emerging Tech (examples): 10 skills
- Beginner Simple (examples): 6 skills

---

## 🔍 Finding Components

### Finding Skills

```bash
# All skills in a kit
ls -1 [kit-name]/.claude/skills/

# Search for specific skill
find . -name "*query-optimizer*" -path "*/.claude/skills/*"

# Example skills (learning format)
find examples/ -name "SKILL.md" -exec grep -l "pattern" {} \;
```

### Finding Commands

```bash
# All commands in a kit
ls -1 [kit-name]/.claude/commands/

# Search for specific command
find . -name "*deploy*" -path "*/.claude/commands/*"
```

### Finding Agents

```bash
# All agents in a kit
ls -1 [kit-name]/.claude/agents/

# List all available agents
find . -name "*.md" -path "*/.claude/agents/*"
```

### Finding Hooks

```bash
# By category
ls -1 hooks-collection/[category]/

# All hooks
find hooks-collection/ -name "*.json" -o -name "*.sh"
```

---

## 📚 Important Reference Files

### Must-Read for Understanding

1. **README.md** - User-facing overview, quick start, project stats
2. **CLAUDE.md** (this file) - Claude Code operational guidance
3. **IMPLEMENTATION_PROGRESS.md** - Detailed skill tracking (87 skills documented)
4. **SKILLS_REFERENCE.md** - Complete skills directory with descriptions

### Contributing

1. **CONTRIBUTING.md** - How to contribute (150+ lines)
2. **templates/** - Templates for creating new components
   - `skill-template.md`
   - `commands/basic-command-template.md`
   - `commands/workflow-command-template.md`
   - `subagent-template.md`

### Documentation Structure

```
docs/
├── getting-started/     # Quick start guides
├── guides/             # Comprehensive guides
│   ├── best-practices.md
│   ├── implementation.md
│   └── troubleshooting.md
├── reference/          # Reference catalogs
│   ├── skills-catalog.md
│   └── master-index.md
└── architecture/       # Design decisions
    ├── project-structure.md
    └── milestones.md
```

---

## 🎓 Educational Content

### Skool Directory

**Location:** `skool/`

Contains:
- Advanced tutorials
- Framework guides
- Game development genres
- Marketing strategies
- Project showcases
- Monetization strategies

### Skool Courses

**Location:** `skool-courses/`

Structured curriculum with 3 levels:
- Beginner
- Intermediate
- Advanced

Includes downloadable templates and bonus resources.

---

## 🚀 Adding New Components

### Adding a New Skill

1. Choose appropriate kit level (starter/intermediate/advanced/specialized)
2. Copy template: `templates/skill-template.md`
3. Create: `[kit]/.claude/skills/skill-name.md`
4. Update: `IMPLEMENTATION_PROGRESS.md`
5. Update: `[kit]/.claude/rules/skills-reference.md`
6. Test activation phrases

### Adding a New Command

1. Choose appropriate kit
2. Copy template: `templates/commands/basic-command-template.md`
3. Create: `[kit]/.claude/commands/command-name.md`
4. Use kebab-case naming
5. Document parameters and usage

### Adding a New Agent

1. Choose appropriate kit
2. Copy template: `templates/subagent-template.md`
3. Create: `[kit]/.claude/agents/agent-name.md`
4. Define expertise area clearly
5. Document when to activate

### Adding a New Hook

1. Choose category in `hooks-collection/`
2. Create JSON configuration or shell script
3. Test thoroughly
4. Document triggering conditions
5. Update `hooks-collection/README.md`

---

## 🔗 External Integration

### MCP Servers

The project documents integration with 20+ MCP servers:
- Source Control: GitHub, GitLab
- Databases: PostgreSQL, MongoDB, MySQL, SQLite
- Communication: Slack, Discord
- Cloud: AWS, GCP, Azure
- Monitoring: Sentry, Datadog, New Relic
- DevOps: Docker, Kubernetes, Terraform

### Framework Support

17 frameworks with dedicated rules in `framework-rules/`:
- React, Vue, Next.js, Nuxt3
- Angular, Svelte, SvelteKit
- Astro, Fresh, Qwik, Remix, SolidJS
- Django, FastAPI, Express
- And more

---

## 💡 Best Practices for This Repository

### When Working on Documentation

1. **Maintain Consistency** - Follow established patterns
2. **Update Multiple Files** - Documentation is interconnected
3. **Verify Counts** - Skill/command/agent counts must be accurate
4. **Test Examples** - All code examples should work
5. **Use Templates** - Templates ensure consistency

### When Adding Skills

1. **Progressive Complexity** - Start simple, scale up
2. **Clear Activation** - Multiple activation phrases
3. **Framework Agnostic** - Support diverse tech stacks where possible
4. **Production Ready** - All intermediate+ should be tested
5. **Security Minded** - Include security considerations

### When Modifying Structure

1. **Preserve Hierarchy** - Maintain level-based organization
2. **Update References** - Check all files referencing changed paths
3. **Test Integration** - Verify kits still work when copied
4. **Document Changes** - Update CHANGELOG.md

---

## 🔐 Security Considerations

This repository contains:
- ✅ Configuration files (safe)
- ✅ Documentation (safe)
- ✅ Shell scripts for hooks (reviewed)
- ✅ No secrets or credentials
- ✅ No executable code beyond hooks

### Built-in Security Features

36 hooks provide automatic protection:
- Secret detection in commits
- .env file protection
- Force push prevention
- Destructive operation confirmation
- Dependency vulnerability scanning
- CORS configuration checks
- Security header validation
- License compliance checks

---

## 📊 Project Statistics

| Metric | Count |
|--------|-------|
| Total Skills | 87 |
| Total Commands | 80+ |
| Total Hooks | 36 |
| Total Agents | 46 |
| Framework Rules | 17 |
| Specialized Kits | 4 |
| Lines of Documentation | 100,000+ |
| Code Examples | 500+ |
| Technologies Covered | 25+ |

---

## 🎯 Project Philosophy

1. **Education First** - Every configuration teaches a concept
2. **Production Ready** - All intermediate+ examples are tested
3. **Security Minded** - Built-in protections and validations
4. **Framework Agnostic** - Support diverse tech stacks
5. **Progressive Enhancement** - Start simple, scale up

---

## 🔄 Git Workflow

### Current Branch

Branch: `claude/claude-skill-exploration-011CUftgTCDaCU11qRo3vUHK`

This is also the main branch for this repository.

### Recent Activity

Recent PRs have added:
- Railway Deployment Kit (PR #32)
- Documentation audit discovering 87 skills (PR #31)
- Repository reorganization (PR #30)
- Knowledge cutoff awareness system (PR #28)
- Strict TypeScript patterns (PR #28)

### Commit Message Format

Follow conventional commits:
```
<type>(<scope>): <subject>

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation changes
- refactor: Code refactoring
- test: Testing updates
- chore: Maintenance
```

---

## 🎓 Learning Path Recommendation

For Claude Code instances working in this repository:

1. **Understand Structure First** - Read this CLAUDE.md
2. **Review README.md** - User-facing overview
3. **Check IMPLEMENTATION_PROGRESS.md** - Detailed skill tracking
4. **Examine Templates** - Understand patterns
5. **Look at Examples** - See implementations
6. **Test Changes** - Copy to test project

---

## 🤝 Collaboration Guidelines

When working on this repository:

1. **Preserve Existing Work** - 100% complete, maintain quality
2. **Follow Templates** - Use provided templates
3. **Update Documentation** - Keep all docs in sync
4. **Test Thoroughly** - Copy and test configurations
5. **Maintain Counts** - Skill/command/agent numbers must be accurate

---

## 📞 Support Resources

- **Documentation:** `docs/` directory
- **Issues:** GitHub issue tracker
- **Discussions:** GitHub discussions
- **Contributing:** See CONTRIBUTING.md
- **Official Docs:** https://docs.claude.com/en/docs/claude-code/

---

**Project Status:** ✅ 100% COMPLETE - All 87 Skills Documented
**Last Updated:** November 5, 2025
**Maintainer:** Claudius Skills Project Team
