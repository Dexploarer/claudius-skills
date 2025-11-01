# Tutorial: Building a Complete Development Workflow

Learn how to combine all five pillars of Claude Code into a cohesive, powerful development environment.

## What You'll Build

A **complete feature development workflow** that combines:
1. **Skills**: Auto-activate for common tasks
2. **Commands**: Quick shortcuts for complex operations
3. **Hooks**: Automatic safety and quality checks
4. **Subagents**: Specialized reviewers and generators
5. **MCP**: Integration with GitHub and persistent memory

**The Workflow:**
- Create a new feature branch
- Implement the feature with auto-activating skills
- Generate tests automatically
- Review code with specialized subagent
- Run quality checks via hooks
- Create commit with perfect message
- Generate PR with full description
- Track progress in memory

**Time:** 45-60 minutes
**Prerequisites:** Completed all previous tutorials

## Step 1: The Scenario

You're building a **user authentication system** for a web app.

**Requirements:**
- Login endpoint
- Password validation
- Session management
- Error handling
- Tests
- Documentation

**Our workflow will handle:**
- ✅ Branch creation and management
- ✅ Code generation with best practices
- ✅ Automatic test generation
- ✅ Code quality review
- ✅ Pre-commit safety checks
- ✅ Perfect commit messages
- ✅ PR generation
- ✅ Progress tracking

## Step 2: Set Up the Environment

### Project Structure

```bash
# Create test project
mkdir auth-feature-demo
cd auth-feature-demo

# Initialize git
git init
git checkout -b main

# Initial commit
echo "# Auth Feature Demo" > README.md
git add README.md
git commit -m "Initial commit"

# Create directories
mkdir -p src tests .claude/{skills,commands,agents,hooks}
```

### Install MCP Servers

Create `.mcp.json`:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

## Step 3: Create the Skills

### Skill 1: Feature Developer

`.claude/skills/feature-developer.md`:

```markdown
---
name: feature-developer
description: Develops new features following best practices. Activates when creating new functionality or implementing features.
allowed-tools: [Read, Write, Edit, Grep, Glob]
---

# Feature Developer

Expert at implementing features with clean, tested, documented code.

## When to Activate
- "implement [feature]"
- "create [functionality]"
- "build [component]"

## Process

### 1. Understand Requirements
Ask clarifying questions:
- What's the input/output?
- What are edge cases?
- Performance requirements?
- Security concerns?

### 2. Plan Implementation
- File structure
- Functions needed
- Data flow
- Dependencies

### 3. Write Code
- Clear naming
- Type safety (if applicable)
- Error handling
- Input validation

### 4. Add Tests
- Unit tests for each function
- Edge cases
- Error scenarios
- Integration tests

### 5. Document
- Function docstrings
- Usage examples
- API documentation

## Best Practices
- Keep functions small and focused
- Handle errors gracefully
- Validate all inputs
- Write self-documenting code
- Test before marking complete
```

### Skill 2: Test Generator

`.claude/skills/test-generator.md`:

```markdown
---
name: test-generator
description: Generates comprehensive unit tests for code. Activates when asked to write tests or test coverage.
allowed-tools: [Read, Write, Grep]
---

# Test Generator

Specialized in creating thorough, meaningful tests.

## Test Structure

### For Each Function:
1. **Happy path** - Normal usage
2. **Edge cases** - Boundaries
3. **Error cases** - Invalid inputs
4. **Integration** - Works with other code

### Test Template

\`\`\`javascript
describe('functionName', () => {
  it('should handle normal case', () => {
    // Arrange
    const input = validInput;

    // Act
    const result = functionName(input);

    // Assert
    expect(result).toBe(expected);
  });

  it('should handle edge case', () => {
    // Test boundaries
  });

  it('should throw on invalid input', () => {
    expect(() => functionName(null)).toThrow();
  });
});
\`\`\`

## Coverage Goals
- 100% of public functions
- All error paths
- Edge cases
- Integration points
```

## Step 4: Create the Commands

### Command 1: Start Feature

`.claude/commands/start-feature.md`:

```markdown
# Start Feature

Creates a feature branch and initializes feature development.

## Usage
/start-feature [feature-name]

## Instructions

### 1. Get Feature Name
From $ARGUMENTS or ask: "What feature are you building?"

### 2. Check Git Status
\`\`\`bash
git status
\`\`\`
Ensure working tree is clean.

### 3. Update Main
\`\`\`bash
git checkout main
git pull origin main
\`\`\`

### 4. Create Feature Branch
\`\`\`bash
git checkout -b feature/[feature-name]
\`\`\`

### 5. Store in Memory
Use Memory MCP:
\`\`\`
Current feature: [feature-name]
Started: [date]
Branch: feature/[feature-name]
Status: in-progress
\`\`\`

### 6. Show Summary
\`\`\`
✅ Feature branch created!

📍 Branch: feature/[feature-name]
📅 Started: [date]

Next steps:
- Implement your feature
- Run /test when ready
- Run /review for code review
- Run /finish-feature when done
\`\`\`
```

### Command 2: Finish Feature

`.claude/commands/finish-feature.md`:

```markdown
# Finish Feature

Completes feature development with review, tests, and PR creation.

## Usage
/finish-feature

## Instructions

### 1. Recall Current Feature
Query Memory MCP for current feature info.

### 2. Run Tests
\`\`\`bash
npm test
# or python -m pytest
# or appropriate test command
\`\`\`

If tests fail, STOP and report issues.

### 3. Call Code Review Subagent
"Call code-reviewer subagent to review all changes"

Wait for review. If issues found, ask user to fix.

### 4. Call Commit Message Generator
"Call commit-message-generator subagent"

### 5. Create Commit
Use generated message:
\`\`\`bash
git add -A
git commit -m "[generated message]"
\`\`\`

### 6. Push Branch
\`\`\`bash
git push -u origin [branch-name]
\`\`\`

### 7. Generate PR Description
Analyze commits since branching from main:
\`\`\`bash
git log main..HEAD
git diff main...HEAD --stat
\`\`\`

Create PR description:
\`\`\`markdown
## Summary
[What this feature does]

## Changes
- [Key change 1]
- [Key change 2]

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Screenshots
[If UI changes]

## Breaking Changes
[If any]

## Related Issues
Closes #[issue-number]
\`\`\`

### 8. Create PR
If GitHub MCP available:
\`\`\`bash
gh pr create --title "[feature-name]" --body "[description]"
\`\`\`

### 9. Update Memory
\`\`\`
Feature: [feature-name]
Status: completed
PR: [pr-url]
Completed: [date]
\`\`\`

### 10. Show Summary
\`\`\`
🎉 Feature Complete!

✅ Tests passed
✅ Code reviewed
✅ Committed
✅ Pushed
✅ PR created: [url]

Great work! 🚀
\`\`\`
```

## Step 5: Create the Hooks

### Hook 1: Pre-Commit Quality Check

`.claude/hooks/pre-commit-quality.sh`:

```bash
#!/bin/bash

echo "🔍 Running pre-commit quality checks..."

# Check for debugging code
if git diff --cached | grep -E "^\+.*(console\.log|debugger|pdb\.set_trace)" > /dev/null; then
  echo "❌ BLOCK: Debugging code found"
  echo "   Remove console.log, debugger, etc."
  exit 1
fi

# Check for TODO/FIXME
if git diff --cached | grep -E "^\+.*(TODO|FIXME|HACK)" > /dev/null; then
  echo "⚠️  WARNING: Found TODO/FIXME comments"
  echo "   Consider addressing before committing"
  # Don't block, just warn
fi

# Run linter (if available)
if command -v eslint &> /dev/null; then
  echo "Running eslint..."
  if ! eslint $(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(js|ts|jsx|tsx)$'); then
    echo "❌ BLOCK: Linting errors found"
    exit 1
  fi
fi

# Run tests (if available and fast)
if [ -f "package.json" ] && grep -q '"test"' package.json; then
  echo "Running tests..."
  if ! npm test -- --passWithNoTests 2>&1 | grep -q "PASS\|0 failed"; then
    echo "❌ BLOCK: Tests failed"
    exit 1
  fi
fi

echo "✅ ALLOW: All quality checks passed"
exit 0
```

Make executable:
```bash
chmod +x .claude/hooks/pre-commit-quality.sh
```

### Hook 2: Feature Tracker

`.claude/hooks/track-feature.sh`:

```bash
#!/bin/bash

# Track feature progress in memory
BRANCH=$(git rev-parse --abbrev-ref HEAD)

if [[ $BRANCH == feature/* ]]; then
  FEATURE_NAME=${BRANCH#feature/}

  # Log the commit
  echo "📝 Logging commit for feature: $FEATURE_NAME"

  # Update could be done via Claude's memory MCP
  # This is a simple file-based alternative
  echo "[$(date)] Commit on $FEATURE_NAME" >> .claude/feature-log.txt
fi

exit 0
```

### Hook Configuration

`.claude/settings.json`:

```json
{
  "hooks": {
    "tool-call": {
      "Bash": {
        "git commit": {
          "command": "bash .claude/hooks/pre-commit-quality.sh",
          "description": "Quality checks before commit",
          "blocking": true
        }
      }
    },
    "session-start": {
      "command": "bash .claude/hooks/track-feature.sh",
      "description": "Track feature progress",
      "blocking": false
    }
  }
}
```

## Step 6: Create the Subagents

### Subagent 1: Code Reviewer

`.claude/agents/code-reviewer.md`:

```markdown
---
name: code-reviewer
description: Reviews code for quality, bugs, and best practices
allowed-tools: [Read, Grep, Bash]
---

# Code Reviewer

Specialized code review subagent focusing on quality and correctness.

## Review Checklist

### Code Quality
- [ ] Clear, descriptive names
- [ ] Functions are focused (single responsibility)
- [ ] No duplication
- [ ] Consistent style

### Correctness
- [ ] Logic is sound
- [ ] Edge cases handled
- [ ] Error handling present
- [ ] No obvious bugs

### Security
- [ ] Input validation
- [ ] No hardcoded secrets
- [ ] SQL injection prevention
- [ ] XSS prevention (if web)

### Performance
- [ ] No obvious inefficiencies
- [ ] Appropriate data structures
- [ ] No unnecessary loops

### Testing
- [ ] Tests exist
- [ ] Edge cases tested
- [ ] Error cases tested

## Review Process

1. Read all changed files
2. Check each item in checklist
3. Note issues found
4. Suggest improvements
5. Rate severity (Critical/Major/Minor)

## Output Format

\`\`\`
📋 CODE REVIEW REPORT
━━━━━━━━━━━━━━━━━━━

✅ Passed (X items)
⚠️  Warnings (Y items)
❌ Issues (Z items)

## Critical Issues
[None found / List issues]

## Major Issues
[None found / List issues]

## Minor Issues / Suggestions
- Consider extracting [X] to a separate function
- Could simplify [Y] logic

## Overall Assessment
[APPROVE / APPROVE WITH COMMENTS / REQUEST CHANGES]

## Summary
[Brief summary of changes and quality]
\`\`\`
```

### Subagent 2: Documentation Writer

`.claude/agents/doc-writer.md`:

```markdown
---
name: doc-writer
description: Writes clear documentation for code and APIs
allowed-tools: [Read, Write, Grep]
---

# Documentation Writer

Specialized in creating clear, helpful documentation.

## Documentation Types

### Function Documentation
\`\`\`javascript
/**
 * Brief description of what function does
 *
 * @param {Type} paramName - Description
 * @returns {Type} Description of return value
 * @throws {ErrorType} When this error occurs
 *
 * @example
 * functionName(exampleInput)
 * // => exampleOutput
 */
\`\`\`

### API Documentation
\`\`\`markdown
## POST /api/endpoint

Description of endpoint.

### Request
\`\`\`json
{
  "field": "value"
}
\`\`\`

### Response
\`\`\`json
{
  "result": "value"
}
\`\`\`

### Errors
- 400: Invalid input
- 401: Unauthorized
- 500: Server error
\`\`\`

## README Documentation
- Clear project description
- Installation steps
- Usage examples
- API reference
- Contributing guide
```

## Step 7: Put It All Together

Now let's use the complete workflow!

### Start a Feature

```bash
claude

# Start new feature
/start-feature user-authentication
```

Expected:
```
✅ Feature branch created!

📍 Branch: feature/user-authentication
📅 Started: 2024-01-15

Next steps:
- Implement your feature
- Run /test when ready
- Run /review for code review
- Run /finish-feature when done
```

### Implement the Feature

```
"Implement a user authentication system with:
- login(username, password) function
- validatePassword function
- createSession function
- All with proper error handling"
```

The **feature-developer skill** automatically activates and:
1. Creates `src/auth.js` with implementation
2. Adds error handling
3. Validates inputs
4. Includes documentation

### Generate Tests

```
"Generate comprehensive tests for the auth module"
```

The **test-generator skill** activates and creates:
- `tests/auth.test.js` with full coverage
- Happy path tests
- Edge case tests
- Error scenario tests

### Review the Code

```
"Call the code-reviewer subagent to review my changes"
```

Subagent analyzes code and provides detailed review.

### Finish the Feature

```
/finish-feature
```

This automatically:
1. ✅ Runs tests (via hook)
2. ✅ Checks code quality (via hook)
3. ✅ Reviews code (via subagent)
4. ✅ Generates commit message (via subagent)
5. ✅ Creates commit
6. ✅ Pushes branch
7. ✅ Generates PR description
8. ✅ Creates PR (if GitHub MCP configured)
9. ✅ Updates memory with completion status

## Step 8: Advanced Workflow Enhancements

### Add Metrics Tracking

Create `.claude/skills/metrics-tracker.md`:

```markdown
---
name: metrics-tracker
description: Tracks development metrics and progress
allowed-tools: [Read, Grep, Bash]
---

# Metrics Tracker

Track lines of code, test coverage, and commit frequency.

Use Memory MCP to store:
- Lines of code added/removed
- Number of tests
- Features completed
- Time estimates vs actuals
```

### Add Automated Documentation

```markdown
---
name: auto-doc-updater
description: Automatically updates documentation when code changes
allowed-tools: [Read, Write, Edit]
---

# Auto Documentation Updater

When code changes:
1. Update API docs
2. Update README if needed
3. Update CHANGELOG
4. Generate migration guides for breaking changes
```

### Create Deployment Command

`.claude/commands/deploy.md`:

```markdown
# Deploy Feature

Deploys feature to specified environment with safety checks.

## Usage
/deploy [staging|production]

## Instructions

1. Confirm current branch is merged to main
2. Run full test suite
3. Build production bundle
4. Run smoke tests
5. Deploy to environment
6. Run health checks
7. Update Memory MCP with deployment info
8. Notify team (if Slack MCP configured)
```

## Step 9: Real-World Example

Let's see the complete workflow in action:

```bash
# Day 1: Start feature
/start-feature user-authentication

# Implement
"Build user authentication with JWT tokens"
# feature-developer skill activates

"Add tests for auth module"
# test-generator skill activates

"Document the auth API"
# doc-writer subagent called

# Review
"Review my changes"
# code-reviewer subagent provides feedback

# Fix issues
"Fix the issues from the review"

# Commit (hook runs automatically)
git add -A
git commit
# pre-commit-quality.sh runs
# ✅ All checks pass

# Day 2: Continue work
"Remember what feature I'm working on?"
# Memory MCP recalls: user-authentication

"Add password reset functionality"
# Continue development...

# Day 3: Finish
/finish-feature
# Full automated pipeline runs
# PR created automatically!
```

## Step 10: Customization Ideas

### For Your Team

1. **Add team-specific hooks**
   - Enforce ticket numbers in commits
   - Check branch naming conventions
   - Require approval before merging

2. **Custom skills for your stack**
   - React component generator
   - Django model creator
   - API endpoint scaffolder

3. **Specialized subagents**
   - Security auditor
   - Performance optimizer
   - Accessibility checker

4. **MCP integrations**
   - Jira (track issues)
   - Slack (notifications)
   - AWS (deployments)

### For Solo Developers

1. **Personal productivity**
   - Time tracking in memory
   - Daily goals and progress
   - Learning notes and insights

2. **Project management**
   - Feature planning
   - Bug tracking
   - Release notes generation

3. **Learning assistant**
   - Store TIL (Today I Learned)
   - Track technology decisions
   - Remember code patterns

## Best Practices

### ✅ Do:
- Start simple, add complexity gradually
- Test each pillar independently first
- Document your workflow for teammates
- Review and refine regularly
- Keep hooks fast (< 1 second)
- Use subagents for focused tasks
- Store important context in Memory MCP

### ❌ Don't:
- Try to automate everything at once
- Make hooks too strict (frustrating)
- Give subagents too many tools
- Store secrets in Memory MCP
- Over-complicate simple tasks
- Forget to commit your .claude/ directory

## Troubleshooting

### Workflow Too Slow

**Problem:** Too many checks slowing you down

**Solutions:**
- Make hooks non-blocking for warnings
- Run expensive checks only on /finish-feature
- Cache results where possible
- Parallelize independent checks

### Skills Conflict

**Problem:** Multiple skills activating for same task

**Solutions:**
- Make skill descriptions more specific
- Use different trigger phrases
- Disable unused skills temporarily
- Create a "dispatcher" skill

### Memory Not Helpful

**Problem:** Memory MCP not providing useful context

**Solutions:**
- Be more explicit about what to remember
- Use tags for organization
- Review and clean memory periodically
- Create memory templates

## Workflow Checklist

Use this to verify your complete workflow:

```markdown
## Setup
- [ ] .mcp.json configured
- [ ] Skills created
- [ ] Commands created
- [ ] Hooks configured and tested
- [ ] Subagents created
- [ ] Environment variables set

## Skills
- [ ] Feature developer
- [ ] Test generator
- [ ] Documentation writer
- [ ] [Your custom skills]

## Commands
- [ ] /start-feature
- [ ] /finish-feature
- [ ] /review
- [ ] [Your custom commands]

## Hooks
- [ ] Pre-commit quality checks
- [ ] Feature tracking
- [ ] [Your custom hooks]

## Subagents
- [ ] Code reviewer
- [ ] Commit message generator
- [ ] Doc writer
- [ ] [Your custom subagents]

## MCP
- [ ] GitHub integration
- [ ] Memory persistence
- [ ] [Your custom MCP servers]

## Testing
- [ ] Each skill activates correctly
- [ ] Commands run successfully
- [ ] Hooks block/allow appropriately
- [ ] Subagents provide good analysis
- [ ] MCP servers connect
- [ ] Full workflow end-to-end
```

## Congratulations!

You've built a complete, production-ready Claude Code workflow! 🎉

**What you've mastered:**
- ✅ All five pillars of Claude Code
- ✅ How to combine pillars effectively
- ✅ Building cohesive workflows
- ✅ Automation best practices
- ✅ Real-world development patterns
- ✅ Customization techniques
- ✅ Troubleshooting and optimization

**You're now a Claude Code power user!**

## What's Next?

### Share Your Workflow
- Commit `.claude/` to your repository
- Share with your team
- Contribute examples back to community

### Keep Learning
- Explore advanced MCP servers
- Build custom integrations
- Create domain-specific skills
- Write your own MCP server

### Join the Community
- Share your workflows
- Help other developers
- Contribute to documentation
- Build awesome things!

---

**You've completed all beginner tutorials!**

**Next:** Check out [intermediate examples](../../intermediate/) for framework-specific and advanced patterns!

---

*Built with ❤️ for the Claude Code community*
