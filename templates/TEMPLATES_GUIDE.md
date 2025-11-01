# Complete Templates Guide

Production-ready templates for all Claude Code components.

## 📚 Table of Contents

- [Overview](#overview)
- [Available Templates](#available-templates)
- [Quick Start](#quick-start)
- [Template Categories](#template-categories)
- [Usage Examples](#usage-examples)
- [Best Practices](#best-practices)
- [Customization Guide](#customization-guide)

## Overview

This templates directory contains comprehensive, production-ready templates for creating Claude Code configurations. Each template includes:

- ✅ Complete documentation
- ✅ Best practices built-in
- ✅ Error handling patterns
- ✅ Real-world examples
- ✅ Customization guidance
- ✅ Testing strategies

## Available Templates

### 🎯 Skills (`.claude/skills/`)

| Template | Level | Use Case | Features |
|----------|-------|----------|----------|
| `skills/beginner-skill-template.md` | Beginner | Simple, focused tasks | Single purpose, basic tools, clear examples |
| `skills/intermediate-skill-template.md` | Intermediate | Framework-specific | TypeScript, testing, multi-file generation |
| `skills/advanced-skill-template.md` | Advanced | Full-stack features | Architecture design, complete implementation |

###  Commands (`.claude/commands/`)

| Template | Type | Use Case | Features |
|----------|------|----------|----------|
| `commands/basic-command-template.md` | Basic | Simple operations | Validation, error handling, options |
| `commands/workflow-command-template.md` | Workflow | Complex processes | Multi-step, rollback, progress tracking |

### 🤖 Subagents (`.claude/agents/`)

| Template | Role | Expertise | Tools |
|----------|------|-----------|-------|
| `subagents/analyzer-template.md` | Analyzer | Code review, analysis | Read, Grep, Glob |
| `subagents/generator-template.md` | Generator | Code generation | Read, Write, Edit |
| `subagents/expert-template.md` | Domain Expert | Specialized knowledge | Configurable |

### 🔒 Hooks (`.claude/hooks/` or `settings.json`)

| Template | Category | Purpose | Exit Codes |
|----------|----------|---------|------------|
| `hooks/safety-hook-template.json` | Safety | Prevent mistakes | 0 = allow, 2 = block |
| `hooks/workflow-hook-template.json` | Workflow | Automation | Event-based triggers |
| `hooks/quality-hook-template.json` | Quality | Enforce standards | Validation checks |

### 🔌 MCP Configurations (`.mcp.json`)

| Template | Services | Use Case | Security |
|----------|----------|----------|----------|
| `mcp/basic-mcp-template.json` | Single server | Simple integration | Basic auth |
| `mcp/multi-service-template.json` | Multiple servers | Complex setups | Env variables |
| `mcp/production-template.json` | Full stack | Production ready | Best practices |

### 📦 Complete Setups

| Template | Stack | Includes | Ready For |
|----------|-------|----------|-----------|
| `complete-setups/frontend-setup/` | React/TS | Components, hooks, skills | Web apps |
| `complete-setups/backend-setup/` | Node/Express | API, DB, testing | Services |
| `complete-setups/fullstack-setup/` | MERN | Everything | Full projects |

## Quick Start

### 1. Choose Your Template

```bash
# List all templates
ls -R templates/

# View a specific template
cat templates/skills/beginner-skill-template.md
```

### 2. Copy and Customize

```bash
# Copy template to your project
cp templates/skills/beginner-skill-template.md \
   .claude/skills/my-awesome-skill.md

# Edit the template
# - Change the name in frontmatter
# - Update the description
# - Customize the instructions
# - Add your examples
```

### 3. Test Your Configuration

```bash
# Start Claude Code
claude

# Test your skill/command
"Test your new configuration"
```

## Template Categories

### Skills: When to Use Which Template

**Beginner Template** - Use when:
- Creating simple, focused functionality
- Learning skill basics
- Building code formatters, comment generators
- Task needs only Read/Edit tools
- No complex decision making required

**Intermediate Template** - Use when:
- Working with specific frameworks (React, Django, etc.)
- Generating multiple related files
- Need TypeScript/testing integration
- Moderate complexity (3-5 steps)
- Building component generators, scaffolders

**Advanced Template** - Use when:
- Implementing complete features
- Need architecture design
- Working across full stack
- Database + API + Frontend
- Production-grade requirements
- Team collaboration needed

### Commands: Basic vs Workflow

**Basic Commands** - Use for:
- Single git operations
- File manipulations
- Simple queries
- Quick utilities
- < 5 minute execution
- No rollback needed

**Workflow Commands** - Use for:
- Multi-step processes
- Deployment pipelines
- Data migrations
- Critical operations
- Need checkpoints/rollback
- Require validation phases
- 5+ minute execution

### Subagents: Choosing the Right Type

**Analyzer** - Read-only expert:
```yaml
Tools: [Read, Grep, Glob]
Purpose: Review, audit, analyze
Output: Reports, findings, recommendations
```

**Generator** - Creative builder:
```yaml
Tools: [Read, Write, Edit, Glob]
Purpose: Create files, generate code
Output: New files, boilerplate, scaffolding
```

**Expert** - Domain specialist:
```yaml
Tools: Configurable based on domain
Purpose: Specialized knowledge application
Output: Context-specific solutions
```

## Usage Examples

### Example 1: Creating a Simple Skill

```bash
# 1. Copy template
cp templates/skills/beginner-skill-template.md \
   .claude/skills/json-formatter.md

# 2. Edit frontmatter
---
name: json-formatter
description: Format JSON files when user asks to "format JSON" or "prettify JSON"
allowed-tools: [Read, Edit]
---

# 3. Customize instructions
(Edit the template to add JSON-specific formatting logic)

# 4. Test
claude
> "Format this JSON file"
```

### Example 2: Creating a Deployment Command

```bash
# 1. Copy workflow template
cp templates/commands/workflow-command-template.md \
   .claude/commands/deploy.md

# 2. Customize for your deployment
- Update pre-flight checks (your specific requirements)
- Add your build commands
- Configure your deployment steps
- Set up health checks

# 3. Test with dry-run
/deploy --dry-run

# 4. Run actual deployment
/deploy --env production
```

### Example 3: Setting Up Code Review Subagent

```bash
# 1. Copy analyzer template
cp templates/subagents/analyzer-template.md \
   .claude/agents/code-reviewer.md

# 2. Configure for your standards
---
name: code-reviewer
description: Review code for quality, security, and best practices
allowed-tools: [Read, Grep, Glob]
---

# 3. Add your team's coding standards
(Edit to include your specific rules)

# 4. Use it
"use the code-reviewer subagent to review my PR"
```

### Example 4: MCP Configuration

```bash
# 1. Copy MCP template
cp templates/mcp/multi-service-template.json .mcp.json

# 2. Add your credentials
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}

# 3. Set environment variable
export GITHUB_TOKEN="your-token"

# 4. Test connection
claude
> "list my GitHub repositories"
```

## Best Practices

### For All Templates

✅ **Do:**
- Read the entire template before customizing
- Keep the structure (it's battle-tested)
- Add your specific requirements
- Test thoroughly before production use
- Document your customizations
- Share useful modifications with team

❌ **Don't:**
- Skip the validation sections
- Remove error handling
- Hardcode sensitive data
- Ignore the examples
- Over-complicate simple tasks
- Forget to test edge cases

### Template-Specific Best Practices

**Skills:**
- Make descriptions very specific (they control activation)
- Start with minimal tools, add more if needed
- Include real examples from your codebase
- Test with different phrasings

**Commands:**
- Always include --dry-run option
- Show what will happen before doing it
- Provide clear error messages
- Include undo/rollback information

**Subagents:**
- Restrict tools to minimum needed
- Define clear expertise boundaries
- Include structured output format
- Test in isolation first

**Hooks:**
- Test hook commands separately first
- Use appropriate exit codes (0=allow, 2=block)
- Add timeouts for slow operations
- Provide clear feedback messages

**MCP:**
- Never commit real credentials
- Use environment variables
- Test connections before relying on them
- Use read-only tokens when possible

## Customization Guide

### Making Templates Your Own

Each template is designed to be customized. Here's how:

#### 1. Project-Specific Patterns

```markdown
## Our Project Standards

Add sections like:
- File naming conventions
- Code style requirements
- Testing standards
- Documentation format
```

#### 2. Team Conventions

```markdown
## Team Guidelines

Include:
- PR review checklist
- Commit message format
- Branch naming rules
- Deploy approval process
```

#### 3. Framework Integration

```markdown
## Framework-Specific

Customize for:
- React: Component patterns, hooks rules
- Django: Model conventions, admin setup
- Express: Middleware patterns, error handling
```

#### 4. Tool Restrictions

```yaml
---
# Start restrictive
allowed-tools: [Read, Grep]

# Add tools as needed
allowed-tools: [Read, Write, Edit, Grep]

# Full access (use carefully)
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, Task]
---
```

### Version Control for Templates

```bash
# Track your customizations
git add .claude/
git commit -m "Add custom skill for API generation"

# Share with team
git push origin main

# Team members get your configs
git pull origin main
```

### Creating Template Libraries

```bash
# Organize templates by project type
company-templates/
├── web-app/
│   ├── react-component-skill.md
│   ├── api-endpoint-command.md
│   └── deploy-to-vercel.md
├── backend-service/
│   ├── crud-generator-skill.md
│   ├── migration-command.md
│   └── deploy-to-aws.md
└── mobile-app/
    ├── screen-generator-skill.md
    ├── navigation-command.md
    └── deploy-to-app-store.md
```

## Advanced Topics

### Composing Multiple Templates

Combine templates for powerful workflows:

```markdown
## Example: Complete Feature Workflow

1. Skill: Generate full-stack feature
   (Uses advanced-skill-template.md)

2. Command: Run tests and checks
   (Uses workflow-command-template.md)

3. Subagent: Review generated code
   (Uses analyzer-template.md)

4. Command: Deploy if approved
   (Uses workflow-command-template.md)

All work together for end-to-end feature delivery!
```

### Template Inheritance

Create base templates and extend them:

```markdown
# base-skill-template.md
---
name: base-skill
---

Common instructions that all your skills share...

# specific-skill.md
Extends: base-skill-template.md

Additional specific instructions...
```

### Dynamic Templates

Use placeholders for generation:

```bash
# generate-from-template.sh
#!/bin/bash

TEMPLATE=$1
NAME=$2

cp "templates/$TEMPLATE" ".claude/skills/$NAME.md"

# Replace placeholders
sed -i "s/{{NAME}}/$NAME/g" ".claude/skills/$NAME.md"
sed -i "s/{{DATE}}/$(date)/g" ".claude/skills/$NAME.md"
```

## Troubleshooting Templates

### Common Issues

**Template doesn't activate:**
- Check description specificity
- Verify file location (.claude/skills/, etc.)
- Ensure YAML frontmatter is valid
- Restart Claude Code

**Template gives errors:**
- Validate JSON/YAML syntax
- Check tool permissions
- Verify file paths
- Review error messages carefully

**Template works differently than expected:**
- Re-read template documentation
- Check examples in template
- Test with simpler inputs first
- Enable verbose/debug mode

### Getting Help

1. **Read the template comments** - They contain important guidance
2. **Check examples in template** - See how it's meant to be used
3. **Review beginner examples** - See simpler working versions
4. **Test incrementally** - Start simple, add complexity gradually

## Template Maintenance

### Keeping Templates Updated

```bash
# Update templates from repository
git pull origin main

# Compare with your customizations
git diff templates/

# Merge updates carefully
git merge --no-commit origin/main
```

### Contributing Back

Found a useful pattern? Share it:

```bash
# Create your template
cp templates/skills/intermediate-skill-template.md \
   templates/skills/my-pattern-skill-template.md

# Document it
# Add to TEMPLATES_GUIDE.md

# Submit PR
git add templates/
git commit -m "Add template for [use case]"
git push origin my-template-branch
```

## Examples from the Wild

### Real-World Template Customizations

**1. E-commerce Checkout Skill**
- Base: intermediate-skill-template.md
- Adds: Payment processing, inventory checks
- Tools: [Read, Write, Bash] (for payment API calls)

**2. Database Migration Command**
- Base: workflow-command-template.md
- Adds: Backup, migrate, verify cycle
- Features: Automatic rollback on failure

**3. Security Audit Subagent**
- Base: analyzer-template.md
- Adds: CVE checking, dependency scanning
- Output: Security report with severity ratings

## Next Steps

1. **Explore Templates** - Browse all available templates
2. **Start Simple** - Begin with beginner templates
3. **Customize Gradually** - Add complexity as needed
4. **Test Thoroughly** - Validate before production
5. **Share Knowledge** - Contribute improvements back

## Resources

- [Claude Code Documentation](https://docs.claude.com/claude-code/)
- [Examples Directory](../examples/)
- [Starter Kits](../starter-kit/)
- [Best Practices Guide](../resources/guides/best-practices.md)

---

**Ready to build? Pick a template and start creating!** 🚀
