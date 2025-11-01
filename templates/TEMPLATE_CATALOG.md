# Template Catalog - Complete Reference

**Last Updated:** 2025-01-01
**Total Templates:** 17

## 📚 Quick Navigation

- [Skills (3)](#skills)
- [Commands (2)](#commands)
- [Subagents (4)](#subagents)
- [Hooks (3)](#hooks)
- [MCP Configurations (3)](#mcp-configurations)
- [Complete Setups (3)](#complete-setups)

---

## Skills

Production-ready skill templates for automatic task execution.

### 1. Beginner Skill Template
**File:** `skills/beginner-skill-template.md`
**Size:** ~4,600 lines
**Level:** Beginner
**Use For:** Simple, focused tasks (formatters, generators)

**Features:**
- Single-purpose design
- Basic tool usage (Read, Edit)
- Clear step-by-step instructions
- Language-specific examples
- Error handling patterns
- Customization guidance

**Best For:**
- Code formatters (JSON, XML, etc.)
- Comment generators
- File organizers
- Simple validators

**Copy Command:**
```bash
cp templates/skills/beginner-skill-template.md \
   .claude/skills/my-skill.md
```

---

### 2. Intermediate Skill Template
**File:** `skills/intermediate-skill-template.md`
**Size:** ~12,000 lines
**Level:** Intermediate
**Use For:** Framework-specific code generation

**Features:**
- Multi-file generation
- TypeScript integration
- Testing with React Testing Library
- CSS Modules / styled-components
- Custom hooks patterns
- State management examples
- Comprehensive test suites

**Best For:**
- React/Vue/Angular component generators
- Django model creators
- API endpoint scaffolding
- Test suite generation

**Copy Command:**
```bash
cp templates/skills/intermediate-skill-template.md \
   .claude/skills/component-generator.md
```

---

### 3. Advanced Skill Template
**File:** `skills/advanced-skill-template.md`
**Size:** ~24,000 lines
**Level:** Advanced
**Use For:** Full-stack feature implementation

**Features:**
- Complete architecture design
- Database schema creation
- Backend API (controllers, services, routes)
- Frontend components with state
- Comprehensive testing (unit, integration, E2E)
- Documentation generation
- Deployment guidance
- Event-driven patterns
- CQRS implementation
- Microservices integration

**Best For:**
- Complete feature development
- Full-stack implementations
- Enterprise applications
- Complex workflows

**Copy Command:**
```bash
cp templates/skills/advanced-skill-template.md \
   .claude/skills/feature-builder.md
```

---

## Commands

Manual slash command templates for workflows.

### 1. Basic Command Template
**File:** `commands/basic-command-template.md`
**Size:** ~8,700 lines
**Type:** Simple Command
**Use For:** Quick, focused operations

**Features:**
- Argument parsing and validation
- --dry-run support
- --verbose mode
- --help documentation
- Error handling with helpful messages
- Safety confirmations
- Undo information
- Icon-based formatting
- Testing checklist

**Best For:**
- Git operations
- File processing
- Quick utilities
- Data transformations

**Example Commands:**
- `/format-json`
- `/create-component`
- `/run-migration`
- `/deploy-staging`

**Copy Command:**
```bash
cp templates/commands/basic-command-template.md \
   .claude/commands/my-command.md
```

---

### 2. Workflow Command Template
**File:** `commands/workflow-command-template.md`
**Size:** ~22,000 lines
**Type:** Complex Workflow
**Use For:** Multi-step processes

**Features:**
- 5-phase workflow (Pre-flight → Preparation → Execution → Verification → Cleanup)
- Checkpoint/rollback system
- Real-time progress tracking
- Health checks and validation
- Parallel execution support
- Conditional steps
- Interactive decision points
- Detailed logging
- Error recovery strategies
- Manual approval gates

**Best For:**
- Deployment pipelines
- Database migrations
- Release processes
- Complex automations

**Example Workflows:**
- `/deploy-production`
- `/migrate-database`
- `/create-release`
- `/run-e2e-tests`

**Copy Command:**
```bash
cp templates/commands/workflow-command-template.md \
   .claude/commands/deploy.md
```

---

## Subagents

Specialized AI experts for focused tasks.

### 1. Analyzer Subagent Template
**File:** `subagents/analyzer-subagent-template.md`
**Size:** ~15,000 lines
**Role:** Read-only Expert
**Tools:** Read, Grep, Glob

**Expertise:**
- Code quality analysis
- Security vulnerability detection
- Performance optimization
- Best practices review
- SOLID principles
- Accessibility (WCAG 2.1)

**Output:**
- Comprehensive analysis report
- Prioritized findings (Critical → Low)
- Code examples with fixes
- Metrics and scoring
- Actionable recommendations

**Best For:**
- Code reviews
- Security audits
- Performance analysis
- Architecture reviews

**Copy Command:**
```bash
cp templates/subagents/analyzer-subagent-template.md \
   .claude/agents/code-analyzer.md
```

---

### 2. Generator Subagent Template
**File:** `subagents/generator-subagent-template.md`
**Size:** ~18,000 lines
**Role:** Creative Builder
**Tools:** Read, Write, Edit, Grep, Glob

**Capabilities:**
- Generate production-ready code
- Create comprehensive tests
- Write detailed documentation
- Follow project conventions
- Include error handling
- Add accessibility features

**Generated Artifacts:**
- Complete implementations
- Type definitions
- Test suites
- Documentation files
- Configuration files

**Best For:**
- Component generation
- API endpoint creation
- Test suite creation
- Boilerplate generation

**Copy Command:**
```bash
cp templates/subagents/generator-subagent-template.md \
   .claude/agents/code-generator.md
```

---

### 3. Reviewer Subagent Template
**File:** `subagents/reviewer-subagent-template.md`
**Size:** ~5,000 lines
**Role:** PR Reviewer
**Tools:** Read, Grep, Glob, Bash

**Review Focus:**
- Code quality and readability
- Functionality correctness
- Test coverage and quality
- Security vulnerabilities
- Best practices adherence

**Output:**
- Structured PR review
- Severity-based prioritization
- Constructive feedback
- Code examples
- Approval status

**Best For:**
- Pull request reviews
- Code quality checks
- Mentoring through reviews
- Team standards enforcement

**Copy Command:**
```bash
cp templates/subagents/reviewer-subagent-template.md \
   .claude/agents/pr-reviewer.md
```

---

### 4. Domain Expert Template
**File:** `subagents/domain-expert-template.md`
**Size:** ~3,000 lines
**Role:** Specialized Expert
**Tools:** Configurable

**Example Domains:**
- Database Architecture
- Security Auditing
- API Design
- Performance Optimization
- DevOps/Infrastructure

**Provides:**
- Expert analysis
- Recommendations with rationale
- Trade-offs comparison
- Implementation guidance
- Common pitfalls

**Best For:**
- Specialized consulting
- Architecture decisions
- Deep technical questions
- Domain-specific guidance

**Copy Command:**
```bash
cp templates/subagents/domain-expert-template.md \
   .claude/agents/database-expert.md
```

---

## Hooks

Event-driven automation and safety guards.

### 1. Safety Hook Template
**File:** `hooks/safety-hook-template.json`
**Type:** Safety Guard
**Events:** PreToolUse

**Prevents:**
- Accidental pushes to main/master
- Committing secrets (.env, .pem, .key)
- Force pushes without confirmation
- Large deletions without confirmation

**Exit Codes:**
- 0: Allow operation
- 2: Block operation
- Other: Warning

**Best For:**
- Protecting critical branches
- Preventing credential leaks
- Avoiding accidental deletions
- Enforcing safe practices

**Copy Command:**
```bash
# Add to .claude/settings.json or create hooks file
```

---

### 2. Workflow Hook Template
**File:** `hooks/workflow-hook-template.json`
**Type:** Automation
**Events:** PostToolUse, SessionStart, SessionEnd

**Automates:**
- Code formatting after file save
- Running tests after code changes
- Welcome messages
- Cleanup on exit

**Best For:**
- Auto-formatting code
- Running tests automatically
- Session management
- Cleanup tasks

---

### 3. Quality Enforcement Template
**File:** `hooks/quality-enforcement-template.json`
**Type:** Quality Guard
**Events:** PreToolUse

**Enforces:**
- Linting before commits
- TypeScript type checking
- Test coverage thresholds
- Security scanning

**Thresholds:**
- Lint: Must pass
- Type check: Warning only
- Coverage: 80% minimum
- Security: High vulnerabilities block

---

## MCP Configurations

Model Context Protocol server configurations.

### 1. Basic MCP Template
**File:** `mcp/basic-mcp-template.json`
**Complexity:** Simple
**Servers:** 1

**Includes:**
- Single server example
- Environment variable usage
- Basic security notes
- Setup instructions

**Best For:**
- Learning MCP
- Single service integration
- Testing setup

**Copy Command:**
```bash
cp templates/mcp/basic-mcp-template.json .mcp.json
```

---

### 2. Multi-Service Template
**File:** `mcp/multi-service-template.json`
**Complexity:** Intermediate
**Servers:** 4 (GitHub, Filesystem, Memory, PostgreSQL)

**Includes:**
- Multiple server configuration
- Security best practices
- Environment variable documentation
- Selective enabling/disabling

**Best For:**
- Development environments
- Team setups
- Multi-tool workflows

**Copy Command:**
```bash
cp templates/mcp/multi-service-template.json .mcp.json
```

---

### 3. Production Template
**File:** `mcp/production-template.json`
**Complexity:** Advanced
**Servers:** 4 (GitHub, PostgreSQL, Sentry, Slack)

**Includes:**
- Production-ready configuration
- Health checks
- Monitoring setup
- Security checklist
- Audit logging
- Read-only credentials
- Token rotation plan

**Best For:**
- Production environments
- Enterprise deployments
- High-security requirements

**Copy Command:**
```bash
cp templates/mcp/production-template.json .mcp.json
```

---

## Complete Setups

Full project configurations ready to use.

### 1. Frontend Setup
**Directory:** `complete-setups/frontend/`
**Stack:** React/TypeScript
**Status:** Coming Soon

**Will Include:**
- Component generation skills
- Testing setup
- Build optimization
- Deployment commands
- Linting hooks

---

### 2. Backend Setup
**Directory:** `complete-setups/backend/`
**Stack:** Node.js/Express
**Status:** Coming Soon

**Will Include:**
- API scaffolding
- Database migrations
- Testing suite
- Docker configuration
- CI/CD pipeline

---

### 3. Fullstack Setup
**Directory:** `complete-setups/fullstack/`
**Stack:** MERN/MEAN/PERN
**Status:** Coming Soon

**Will Include:**
- Frontend + Backend combined
- Monorepo configuration
- Shared types
- E2E testing
- Complete deployment

---

## Usage Patterns

### For Beginners
```bash
# Start with simple templates
1. Copy beginner-skill-template.md
2. Copy basic-command-template.md
3. Add safety hooks
4. Set up basic MCP (memory, filesystem)
```

### For Intermediate
```bash
# Use framework-specific templates
1. Copy intermediate-skill-template.md
2. Copy workflow-command-template.md
3. Use reviewer-subagent-template.md
4. Add workflow hooks
5. Set up multi-service MCP
```

### For Advanced
```bash
# Use complete system templates
1. Copy advanced-skill-template.md
2. Use all subagent templates
3. Implement quality hooks
4. Set up production MCP
5. Use complete setup package
```

---

## Template Statistics

| Category | Templates | Total Lines | Avg Lines |
|----------|-----------|-------------|-----------|
| Skills | 3 | ~40,600 | ~13,533 |
| Commands | 2 | ~30,700 | ~15,350 |
| Subagents | 4 | ~41,000 | ~10,250 |
| Hooks | 3 | ~500 | ~167 |
| MCP | 3 | ~400 | ~133 |
| Setups | 3 | TBD | TBD |
| **Total** | **18** | **~113,200** | **~6,289** |

---

## Quick Reference Commands

```bash
# List all templates
ls -R templates/

# Copy entire template category
cp -r templates/skills .claude/

# Create from template with custom name
cp templates/skills/beginner-skill-template.md \
   .claude/skills/json-formatter.md

# Search for specific content
grep -r "pattern" templates/

# View template
cat templates/skills/beginner-skill-template.md

# Check template size
wc -l templates/**/*.md
```

---

## Next Steps

1. Browse templates by category
2. Copy relevant template
3. Customize for your needs
4. Test thoroughly
5. Commit to your repo
6. Share with team

For detailed usage instructions, see [TEMPLATES_GUIDE.md](./TEMPLATES_GUIDE.md)

---

**Questions?** See the [main README](../README.md) or individual template documentation.
