# Best Practices for Claude Code

Proven patterns and techniques for getting the most out of Claude Code's Five Pillars.

## Table of Contents

1. [General Principles](#general-principles)
2. [Skills Best Practices](#skills-best-practices)
3. [Slash Commands Best Practices](#slash-commands-best-practices)
4. [Hooks Best Practices](#hooks-best-practices)
5. [Subagents Best Practices](#subagents-best-practices)
6. [MCP Servers Best Practices](#mcp-servers-best-practices)
7. [Team Collaboration](#team-collaboration)
8. [Security](#security)
9. [Performance](#performance)
10. [Maintenance](#maintenance)

---

## General Principles

### Start Small, Grow Gradually

❌ **Bad:**
```bash
# Day 1: Create 30 skills, 50 commands, 10 subagents
```

✅ **Good:**
```bash
# Week 1: Use starter kit as-is
# Week 2: Add 1-2 custom commands
# Week 3: Modify a skill for your needs
# Week 4: Create your first custom skill
```

### Keep It Simple

**The KISS Principle applies to Claude Code configurations.**

❌ **Bad:**
```yaml
---
name: super-mega-multi-purpose-helper
description: Does everything including cooking breakfast
---
[500 lines of complex instructions]
```

✅ **Good:**
```yaml
---
name: react-component-generator
description: Generate React components when user asks to create a component
---
[Focused, clear instructions for one thing]
```

### Document Everything

**Future you (and your team) will thank you.**

✅ **Always include:**
- Clear descriptions
- Usage examples
- Expected inputs/outputs
- Edge cases
- When to use (and when not to)

### Test Thoroughly

**Before sharing with your team or deploying:**

1. Test the happy path
2. Test edge cases
3. Test error conditions
4. Test with different phrasings (for skills)
5. Test with different arguments (for commands)

---

## Skills Best Practices

### 1. Write Specific Descriptions

The description determines when your skill activates. Be **very specific**.

❌ **Bad:**
```yaml
description: For files
```

✅ **Good:**
```yaml
description: Generate professional README files for projects. Use when the user wants to create or update a README, needs documentation for a new project, or asks for help with project documentation.
```

**Why:** Vague descriptions rarely activate. Specific ones work reliably.

### 2. Include Clear Examples

**Examples help Claude understand what to do.**

✅ **Good structure:**
```markdown
## Examples

### Example 1: Basic Usage

**Input:** User asks "Create a README for this Node.js project"

**Output:**
```markdown
# Project Name
...
```

**Explanation:** The skill detected...
```

### 3. Use Tool Restrictions Wisely

**Restrict tools for safety and clarity.**

```yaml
# Read-only skill
allowed-tools: [Read, Grep, Glob]

# Can modify files
allowed-tools: [Read, Write, Edit, Grep, Glob]

# Can run commands
allowed-tools: [Read, Bash, Grep, Glob]
```

**Principle:** Give minimum necessary permissions.

### 4. Keep Skills Focused

**One skill = One capability**

❌ **Bad:** "Full-stack development helper"
✅ **Good:** "React component generator"
✅ **Good:** "API endpoint creator"
✅ **Good:** "Database migration helper"

### 5. Test Activation Phrases

**Test how users might ask for this skill.**

```bash
# If skill is "readme-generator", test with:
"Create a README"
"I need documentation"
"Generate a readme file"
"Help me document this project"
```

**Tip:** Update the description if some phrasings don't work.

### 6. Handle Edge Cases

**Account for different scenarios:**

```markdown
## Edge Cases

- If no package.json exists, create generic README
- If project is in TypeScript, mention TS in install instructions
- If README already exists, ask before overwriting
```

### 7. Provide Fallbacks

**What happens when something goes wrong?**

```markdown
If unable to determine project type:
1. Ask the user what type of project this is
2. Use a generic template
3. List what information is needed
```

---

## Slash Commands Best Practices

### 1. Use Memorable Names

**Short, clear, memorable.**

✅ **Good:**
- `/test` - Run tests
- `/commit` - Create commit
- `/review` - Review code
- `/explain` - Explain code

❌ **Bad:**
- `/rtatsgc` - Run tests and then show git changes
- `/dothething` - What thing?

### 2. Handle Arguments Properly

**Make it clear how to use arguments.**

```markdown
<!-- At the top of the command file -->
# Usage: /debug [description of issue]

Help debug: $ARGUMENTS

1. Understand the issue: $ARGUMENTS
2. Search for related code
3. Identify potential causes
4. Suggest fixes
```

### 3. Provide Usage Examples

```markdown
## Examples

```bash
/debug login button doesn't respond to clicks
/debug API returns 500 error
/debug tests failing on CI but passing locally
```
```

### 4. Show What You're Doing

**Keep the user informed.**

```markdown
Creating commit message:

1. Reviewing changes with git diff
2. Analyzing modified files
3. Generating commit message
4. Showing you the message for approval

[Do the steps]
```

### 5. Ask for Confirmation on Dangerous Operations

```markdown
# For /clean command

⚠️  About to:
- Remove unused imports
- Delete console.log statements
- Fix formatting

This will modify your files. Continue? (yes/no)
```

### 6. Handle No Arguments Gracefully

```markdown
# Check if arguments provided
If no $ARGUMENTS provided:
  Show usage: "/debug [description of issue]"
  Ask: "What would you like me to debug?"

Otherwise:
  Proceed with debugging $ARGUMENTS
```

### 7. Group Related Commands

**Use consistent naming:**

```bash
/test              # Run all tests
/test-unit         # Run unit tests only
/test-e2e          # Run E2E tests only
/test-watch        # Run tests in watch mode
```

---

## Hooks Best Practices

### 1. Start with Non-Blocking Hooks

**Use exit code 0 for logging/info, not enforcement.**

✅ **Good for beginners:**
```json
{
  "hooks": {
    "PostToolUse": [{
      "pattern": "Edit",
      "command": "echo 'File edited at '$(date)",
      "description": "Log file edits"
    }]
  }
}
```

**Then progress to blocking hooks:**
```json
{
  "hooks": {
    "PreToolUse": [{
      "pattern": "Bash.*git commit",
      "command": "if git diff --cached | grep -i password; then exit 2; fi",
      "description": "Block commits with passwords"
    }]
  }
}
```

### 2. Test Commands Separately First

**Before putting in a hook, test the command:**

```bash
# Test this first
if git diff --cached | grep -i password; then echo "Found password!"; exit 2; fi

# Once it works, add to hooks
```

### 3. Use Appropriate Exit Codes

```bash
# Exit 0: Success, continue
echo "All good!" && exit 0

# Exit 2: Block the operation
echo "ERROR: Problem found!" >&2 && exit 2

# Other: Warning, but continue
echo "Warning: Something odd" >&2 && exit 1
```

### 4. Set Reasonable Timeouts

```json
{
  "hooks": {
    "PreToolUse": [{
      "command": "quick-check.sh",
      "timeout": 5000      // 5 seconds for quick checks
    }],
    "PostToolUse": [{
      "command": "npm test",
      "timeout": 60000     // 60 seconds for tests
    }]
  }
}
```

### 5. Document What Each Hook Does

```json
{
  "hooks": {
    "PreToolUse": [{
      "command": "complex-script.sh",
      "description": "Checks code style and runs linter before edits"
      // ^ Helps team understand what's happening
    }]
  }
}
```

### 6. Use Pattern Matching Effectively

```json
{
  "hooks": {
    // Only on git commit commands
    "PreToolUse": [{
      "pattern": "Bash.*git commit"
    }],

    // Only on file writes
    "PreToolUse": [{
      "pattern": "Write"
    }],

    // On any edit or write
    "PreToolUse": [{
      "pattern": "Edit|Write"
    }]
  }
}
```

### 7. Provide Helpful Error Messages

```bash
# Bad
exit 2

# Good
echo "ERROR: Code style check failed!" >&2
echo "Run 'npm run lint:fix' to auto-fix issues" >&2
exit 2
```

### 8. Don't Overuse Hooks

❌ **Bad:** Hook for everything
```json
{
  "hooks": {
    "PreToolUse": [/* 15 different hooks */],
    "PostToolUse": [/* 20 different hooks */]
  }
}
```

✅ **Good:** Hook for important things
```json
{
  "hooks": {
    "PreToolUse": [
      /* Secret detection */,
      /* Dangerous operation confirmation */
    ],
    "PostToolUse": [
      /* Run tests on changes */
    ]
  }
}
```

---

## Subagents Best Practices

### 1. Define Clear Expertise Boundaries

**Each subagent should have a specific domain.**

✅ **Good:**
```yaml
---
name: security-auditor
description: Security expert who identifies vulnerabilities in code
---

You specialize in:
- SQL injection
- XSS vulnerabilities
- Authentication issues
- Data exposure

You do NOT:
- Review code style
- Optimize performance
- Write tests
```

### 2. Use Tool Restrictions

**Restrict tools based on the subagent's purpose.**

```yaml
# Code reviewer - read only
allowed-tools: [Read, Grep, Glob]

# Test writer - can read and write
allowed-tools: [Read, Write, Bash, Grep, Glob]

# Documentation writer - can read and write
allowed-tools: [Read, Write, Edit, Grep, Glob]
```

### 3. Provide Structured Output

**Make output predictable and useful.**

```markdown
Always output in this format:

## Summary
[One paragraph summary]

## Findings
1. [Finding 1]
2. [Finding 2]

## Recommendations
1. [Action 1]
2. [Action 2]

## Priority
[High/Medium/Low]
```

### 4. Include Decision-Making Guidelines

**Help the subagent make good choices.**

```markdown
## When to Flag an Issue

Critical (🚨):
- Security vulnerabilities
- Data loss risks
- Production-breaking bugs

Warning (⚠️):
- Performance issues
- Code smells
- Missing tests

Info (ℹ️):
- Style suggestions
- Refactoring opportunities
```

### 5. Give Examples of Good Work

```markdown
## Example Output

When reviewing this code:
```javascript
function login(password) {
  return db.query("SELECT * FROM users WHERE password = '" + password + "'");
}
```

Output:
```markdown
## Summary
Critical SQL injection vulnerability found in login function.

## Findings
🚨 CRITICAL: SQL Injection vulnerability
- Line 2: User input directly concatenated into SQL query
- Attacker can bypass authentication with: ' OR '1'='1

## Recommendations
1. Use parameterized queries or prepared statements
2. Example fix: [code example]
3. Add input validation
```
```

### 6. Test Subagents Independently

```bash
# Test by explicitly calling them
"Use the security-auditor subagent to review the login.js file"

# Verify they:
# - Stay in their expertise area
# - Provide useful output
# - Follow the format
# - Give actionable advice
```

### 7. Name Subagents Clearly

✅ **Good names:**
- `code-reviewer`
- `test-writer`
- `security-auditor`
- `performance-optimizer`
- `api-designer`

❌ **Bad names:**
- `helper`
- `agent1`
- `thing`
- `bob`

---

## MCP Servers Best Practices

### 1. Use Environment Variables for Secrets

❌ **Bad:**
```json
{
  "env": {
    "GITHUB_TOKEN": "ghp_actual_secret_token_here"
  }
}
```

✅ **Good:**
```json
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

Then set in your shell:
```bash
export GITHUB_TOKEN="your-token"
```

### 2. Never Commit .mcp.json

**Always in .gitignore:**
```gitignore
.mcp.json
**/.mcp.json
```

**Use templates:**
```json
# .mcp.json.template (committed)
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your-token-here"
      },
      "disabled": true
    }
  }
}
```

### 3. Use Read-Only Access When Possible

```bash
# GitHub - use personal access token with minimal scopes
# Only grant: repo:read, issues:read

# Database - use read-only credentials
# PostgreSQL: GRANT SELECT ON ALL TABLES

# File system - use read-only paths
```

### 4. Test Connections Before Full Use

```bash
# Start small
"List my GitHub repositories"

# Then expand
"Create an issue in my repo"

# Not: "Reorganize all my repos and create 50 issues"
```

### 5. Document Required Permissions

```markdown
## GitHub MCP Server Setup

Requires GitHub Personal Access Token with:
- `repo` - Access repositories
- `read:org` - Read organization data

Create token at: https://github.com/settings/tokens

Add to .mcp.json:
...
```

### 6. Handle Errors Gracefully

**Configure timeouts:**
```json
{
  "mcpServers": {
    "api": {
      "command": "...",
      "timeout": 30000
    }
  }
}
```

### 7. Use Scoped Configurations

**Per-project MCP servers:**
```bash
# Project A uses GitHub
project-a/.mcp.json

# Project B uses PostgreSQL
project-b/.mcp.json

# Both use your user-level configs
~/.claude/.mcp.json
```

---

## Team Collaboration

### 1. Share via Git

**Commit to repository:**
```bash
.claude/skills/
.claude/commands/
.claude/agents/
.claude/settings.json
```

**Don't commit:**
```bash
.claude/settings.local.json
.mcp.json
```

### 2. Document Team Conventions

**Create a team README:**
```markdown
# Team Claude Code Setup

## Required Skills
- api-generator: Creates API endpoints following our conventions
- test-helper: Writes tests using our testing library

## Available Commands
- /test - Runs our test suite
- /lint - Runs ESLint with our config
- /deploy [env] - Deploys to staging/production

## Hooks
- Pre-commit: Runs linter and tests
- Post-edit: Formats code with Prettier

## How to Use
1. Clone this repo
2. Copy .claude/ to your project root
3. Run `claude` and try `/test`
```

### 3. Version Your Configurations

```yaml
---
name: api-generator
version: 2.1.0
description: ...
---

# Changelog
## v2.1.0 - 2024-01-15
- Added support for async endpoints
- Improved error handling

## v2.0.0 - 2024-01-01
- Breaking: Changed to REST conventions
```

### 4. Code Review Configurations

**Treat configs like code:**
- Review PRs that add/modify skills
- Test before merging
- Document breaking changes

### 5. Provide Migration Guides

```markdown
# Migrating from v1 to v2

## Breaking Changes

### API Generator Skill

**Old usage:**
"Create POST endpoint"

**New usage:**
"Create REST endpoint for [resource]"

**Why:** More consistent with our API conventions
```

---

## Security

### 1. Review Hooks Before Running

**Hooks execute arbitrary bash commands!**

```bash
# Before adding this hook, understand what it does
cat .claude/settings.json

# Test the command separately
git diff --cached | grep -i password
```

### 2. Validate MCP Server Sources

**Only use trusted MCP servers:**

✅ **Trusted:**
- Official `@modelcontextprotocol/server-*` packages
- Well-known open source projects
- Your company's internal servers

❌ **Risky:**
- Random npm packages
- Unreviewed code
- Servers requesting excessive permissions

### 3. Use Principle of Least Privilege

**Give minimum necessary access:**

```yaml
# Read-only subagent
allowed-tools: [Read, Grep, Glob]

# Read-only MCP
GITHUB_TOKEN with read-only scope

# Database with SELECT-only user
```

### 4. Keep Secrets Out of Git

**Use:**
- Environment variables
- Secret management tools
- `.gitignore` for sensitive files

**Never:**
- Hardcode API keys
- Commit `.mcp.json` with tokens
- Share credentials in skills/commands

### 5. Audit Regularly

```bash
# Check what's in your configs
grep -r "password\|token\|secret\|key" .claude/

# Review hooks
cat .claude/settings.json

# Check MCP servers
cat .mcp.json
```

---

## Performance

### 1. Keep Skills Concise

**Long skills = slower activation**

✅ **Good:** 50-200 lines
⚠️ **OK:** 200-500 lines
❌ **Too long:** 1000+ lines

### 2. Limit Number of Skills

**Claude checks all skills for activation.**

✅ **Good:** 5-15 skills
⚠️ **OK:** 15-30 skills
❌ **Too many:** 50+ skills

**Better:** Combine related skills or use subagents.

### 3. Optimize Hook Commands

```bash
# Slow
find . -name "*.js" -exec eslint {} \;

# Faster
eslint .
```

### 4. Use Appropriate Timeouts

```json
{
  "hooks": {
    "PreToolUse": [{
      "command": "quick-check",
      "timeout": 2000      // 2 seconds - keep it fast
    }]
  }
}
```

### 5. Cache When Possible

**For expensive operations:**

```bash
# Cache linter output
if [ ! -f .lint-cache ] || [ $FILE -nt .lint-cache ]; then
  eslint $FILE > .lint-cache
fi
cat .lint-cache
```

---

## Maintenance

### 1. Review and Update Regularly

**Monthly checklist:**
- [ ] Remove unused skills/commands
- [ ] Update descriptions that aren't working
- [ ] Test critical hooks still work
- [ ] Update subagents with new patterns
- [ ] Check for deprecated MCP servers

### 2. Keep Documentation Updated

**When you change a skill:**
```yaml
---
name: api-generator
version: 1.2.0  # Update version
updated: 2024-01-15  # Add date
---

<!-- Update examples to match new behavior -->
```

### 3. Monitor Usage

**Track what's actually useful:**

```bash
# Which commands are you using?
# Which skills activate?
# Which subagents help most?

# Remove what you don't use
```

### 4. Sync with Team

**Regular team sync:**
- Share new useful configs
- Deprecate old patterns
- Discuss what works
- Improve together

### 5. Backup Important Configurations

```bash
# Backup your configs
tar -czf claude-configs-backup.tar.gz .claude/

# Or commit to git (recommended)
git add .claude/
git commit -m "Update Claude Code configs"
```

---

## Quick Reference Checklist

### Before Creating a Skill
- [ ] Is this a single, focused capability?
- [ ] Can I describe when it should activate clearly?
- [ ] Have I checked for existing similar skills?
- [ ] Do I have examples of what it should do?

### Before Creating a Command
- [ ] Is this something I do repeatedly?
- [ ] Is the name clear and memorable?
- [ ] Does it handle arguments properly?
- [ ] Is it documented with examples?

### Before Adding a Hook
- [ ] Have I tested the command separately?
- [ ] Is the timeout appropriate?
- [ ] Is the error handling clear?
- [ ] Have I documented what it does?
- [ ] Is it safe for my team?

### Before Creating a Subagent
- [ ] Is the expertise area clearly defined?
- [ ] Are tools appropriately restricted?
- [ ] Is the output format structured?
- [ ] Have I provided examples?
- [ ] Does it add value over a skill?

### Before Adding an MCP Server
- [ ] Is the source trusted?
- [ ] Are credentials in environment variables?
- [ ] Is .mcp.json in .gitignore?
- [ ] Do I need only minimum permissions?
- [ ] Have I tested the connection?

---

## Common Mistakes to Avoid

### ❌ Over-Engineering

Don't create complex systems you don't need.

### ❌ Vague Descriptions

"For code" won't activate. "Generate React components with TypeScript and tests when user asks to create a component" will.

### ❌ Ignoring Security

Review hooks, secure MCP servers, keep secrets out of git.

### ❌ No Documentation

Future you won't remember what that skill does.

### ❌ Not Testing

Test before sharing with your team.

### ❌ Creating Too Much

Start small, add as needed.

### ❌ Copying Without Understanding

Understand before copying configs.

---

## Summary

**Good practices make Claude Code powerful and reliable:**

1. **Start small** - Don't over-customize on day one
2. **Keep it simple** - One skill = one thing
3. **Document everything** - Help your future self
4. **Test thoroughly** - Before sharing with team
5. **Secure by default** - Least privilege, no secrets in git
6. **Maintain regularly** - Remove unused, update outdated
7. **Share with team** - Via git, with documentation
8. **Learn continuously** - Build on what works

**Follow these practices and you'll build a robust, secure, and maintainable Claude Code environment!**
