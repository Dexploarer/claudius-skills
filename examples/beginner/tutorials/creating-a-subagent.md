# Tutorial: Creating Your First Subagent

Learn how to create specialized subagents for specific tasks.

## What You'll Build

A **Commit Message Generator** subagent that analyzes your changes and creates well-formatted commit messages following conventional commit standards.

**Why this subagent?**
- Solves a real, common problem
- Demonstrates subagent isolation
- Shows how to restrict tool access
- Teaches best practices
- Immediately useful

## Prerequisites

- Claude Code installed
- Completed previous tutorials (commands and hooks)
- Basic understanding of git
- 25 minutes of time

## Step 1: Understand Subagents

Subagents are specialized AI personalities with:
- **Separate context**: Don't clutter your main conversation
- **Restricted tools**: Only access what they need
- **Specific expertise**: Focused on one domain
- **Isolated history**: Keep analysis separate from implementation

**When to use subagents:**
- ✅ Code review (read-only analysis)
- ✅ Security audits (restricted access)
- ✅ Documentation writing (specific purpose)
- ✅ Commit messages (focused task)
- ❌ General coding (use main Claude)
- ❌ Complex workflows (use commands)

**Main Claude vs Subagent:**

| Aspect | Main Claude | Subagent |
|--------|-------------|----------|
| Context | Full conversation | Fresh, focused context |
| Tools | All tools | Restricted subset |
| Purpose | General development | Specific task |
| History | Accumulates | Isolated |
| Best for | Implementation | Analysis/Review |

## Step 2: Plan Your Subagent

Our Commit Message Generator needs to:

1. **Analyze** staged changes
2. **Classify** the type of change (feat, fix, docs, etc.)
3. **Generate** a conventional commit message
4. **Explain** the reasoning

**Required tools:**
- `Bash`: To run git commands
- `Read`: To read modified files (optional)

**NOT needed:**
- `Write`: Subagent won't modify files
- `Edit`: Read-only analysis
- `Task`: Keeps it simple

## Step 3: Create the Subagent File

Create `.claude/agents/commit-message-generator.md`:

```bash
mkdir -p .claude/agents
touch .claude/agents/commit-message-generator.md
```

**Directory structure:**
```
your-project/
├── .claude/
│   └── agents/
│       └── commit-message-generator.md
```

## Step 4: Write the Subagent Configuration

Add this content to `commit-message-generator.md`:

```markdown
---
name: commit-message-generator
description: Generates conventional commit messages by analyzing staged git changes
allowed-tools: [Bash, Read, Grep]
---

# Commit Message Generator

Expert at analyzing code changes and generating conventional commit messages.

## Your Role

You are a git commit message specialist. Your job is to:
1. Analyze staged changes in a git repository
2. Determine the type and scope of changes
3. Generate a conventional commit message
4. Explain your reasoning

## Conventional Commit Format

All commit messages must follow this format:

\```
<type>(<scope>): <subject>

<body>

<footer>
\```

### Types
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation only
- **style**: Code style changes (formatting, semicolons, etc.)
- **refactor**: Code change that neither fixes a bug nor adds a feature
- **perf**: Performance improvement
- **test**: Adding or updating tests
- **chore**: Maintenance (deps, config, etc.)
- **ci**: CI/CD changes
- **build**: Build system changes

### Scope
The area affected: api, auth, ui, database, etc.

### Subject
- Use imperative mood ("add" not "added" or "adds")
- Don't capitalize first letter
- No period at the end
- Max 50 characters

### Body (optional)
- Explain WHAT and WHY (not HOW)
- Wrap at 72 characters
- Separate from subject with blank line

### Footer (optional)
- Breaking changes: `BREAKING CHANGE: description`
- Issue references: `Fixes #123` or `Closes #456`

## Process

### Step 1: Analyze Staged Changes
\```bash
# Check what's staged
git diff --cached --stat

# See the actual changes
git diff --cached

# Get list of changed files
git diff --cached --name-only
\```

### Step 2: Determine Type

Ask yourself:
- New functionality? → **feat**
- Fixing a bug? → **fix**
- Only docs? → **docs**
- Code formatting? → **style**
- Restructuring without changing behavior? → **refactor**
- Performance improvement? → **perf**
- Adding/updating tests? → **test**
- Dependencies, config? → **chore**

### Step 3: Identify Scope

Common scopes:
- File/module name: `auth`, `api`, `utils`
- Feature area: `login`, `payment`, `search`
- Layer: `frontend`, `backend`, `database`
- Component: `button`, `navbar`, `sidebar`

### Step 4: Write Subject

Good subjects:
- ✅ "add user authentication endpoint"
- ✅ "fix null pointer in payment processing"
- ✅ "update installation instructions"

Bad subjects:
- ❌ "Added new features" (not specific)
- ❌ "Fix bugs" (which bugs?)
- ❌ "Updates" (too vague)
- ❌ "Fixed the thing that was broken" (informal)

### Step 5: Add Body (if needed)

Include body when:
- Change is complex
- Need to explain WHY
- Multiple related changes
- Breaking changes

Skip body when:
- Change is obvious
- Subject says it all
- Simple fix

### Step 6: Add Footer (if needed)

Include footer for:
- Breaking changes
- Issue/ticket references
- Co-authors

## Examples

### Example 1: New Feature
\```
feat(auth): add JWT token refresh mechanism

Implement automatic token refresh to improve user experience.
Users will no longer be logged out after token expiration.

- Add refresh token endpoint
- Store refresh tokens securely
- Handle token refresh on 401 responses

Closes #234
\```

### Example 2: Bug Fix
\```
fix(payment): prevent duplicate charge on retry

Check for existing transaction before processing payment.
This prevents users from being charged twice when they
retry a failed payment.

Fixes #567
\```

### Example 3: Documentation
\```
docs(readme): update installation instructions

Add prerequisites section and troubleshooting guide
for common installation issues.
\```

### Example 4: Simple Refactor
\```
refactor(utils): extract validation logic to separate module
\```

### Example 5: Breaking Change
\```
feat(api): change user endpoint response format

BREAKING CHANGE: User endpoint now returns nested user object
instead of flat structure. Update clients to use response.user
instead of response directly.

Before: { id: 1, name: "John" }
After: { user: { id: 1, name: "John" } }
\```

## Output Format

When user asks you to generate a commit message, provide:

1. **The commit message** (formatted, ready to use)
2. **Analysis** (what changes you observed)
3. **Reasoning** (why you chose this type/scope)
4. **Alternatives** (other valid options, if any)

Example output:

\```
=== COMMIT MESSAGE ===

feat(auth): add password reset functionality

Implement password reset flow with email verification.
Users can now request password reset via email link.

- Add reset token generation
- Create email template
- Implement token verification endpoint

Closes #123

=== ANALYSIS ===

Staged changes include:
- New files: src/auth/reset.js, templates/reset-email.html
- Modified: src/routes/auth.js, package.json
- Tests: tests/auth/reset.test.js

This adds new functionality (password reset) to the auth module.

=== REASONING ===

Type: "feat" - This is a new feature, not a bug fix
Scope: "auth" - Changes are in authentication module
Subject: Imperative mood, describes what it does

Body included because:
- Feature is non-trivial
- Multiple components added
- Good to document what's included

=== ALTERNATIVES ===

Could also be scoped as "feat(user)" if password reset
is considered a user feature rather than auth feature.
\```

## Guidelines

### ✅ Do:
- Analyze actual code changes carefully
- Use appropriate commit type
- Keep subject line under 50 characters
- Use imperative mood ("add" not "added")
- Include body for non-trivial changes
- Reference issues when applicable
- Suggest improvements if commit is too large

### ❌ Don't:
- Guess at changes without checking git diff
- Use vague descriptions
- Mix multiple unrelated changes in one message
- Write novel-length commit messages
- Forget to check if it's a breaking change
- Include obvious information in body

## Special Cases

### Large Commits
If staged changes are too large or mixed:
\```
⚠️ WARNING: This commit includes multiple types of changes.

Recommend splitting into separate commits:
1. feat(auth): add login functionality
2. fix(api): correct validation errors
3. docs(readme): update setup instructions

Would you like me to suggest how to split these changes?
\```

### No Staged Changes
\```
❌ ERROR: No staged changes found.

Please stage your changes first:
  git add <files>

Or stage all changes:
  git add -A
\```

### Unclear Changes
If changes are ambiguous, ask questions:
\```
I see changes to multiple areas. To generate the best commit message:

1. Is this primarily a new feature or a bug fix?
2. What prompted these changes?
3. Are there any breaking changes?
\```

## Remember

You are a specialist. Your ONLY job is generating commit messages.
- Don't offer to make code changes
- Don't review code quality (unless it affects the commit message)
- Don't suggest new features
- Stay focused on the task

Keep your context clean and focused on commit message generation.
```

## Step 5: Test Your Subagent

### Test 1: Create Some Changes

```bash
# Create a new feature
mkdir -p src
cat > src/auth.js << 'EOF'
// User authentication module
function login(username, password) {
  // TODO: Implement login logic
  return { token: 'fake-token' };
}

module.exports = { login };
EOF

# Stage it
git add src/auth.js
```

### Test 2: Call the Subagent

Start Claude Code and ask:

```bash
claude

# In Claude:
"Call the commit-message-generator subagent to create a commit message for my staged changes"
```

### Test 3: Verify Output

The subagent should:
1. Run `git diff --cached` to see changes
2. Analyze that it's a new file with auth functionality
3. Generate a message like:
   ```
   feat(auth): add user authentication module

   Create initial login function with basic structure.
   Implementation details to be added.
   ```
4. Explain its reasoning
5. Return control to main Claude

### Test 4: Different Change Types

Try different scenarios:

**Bug Fix:**
```javascript
// Fix a bug
// In src/auth.js, change:
return { token: 'fake-token' };
// To:
return { token: 'fake-token', expiresIn: 3600 };

git add src/auth.js
# Ask subagent again
```

**Documentation:**
```bash
echo "# Auth Module" > README.md
git add README.md
# Ask subagent
```

## Step 6: Use in Your Workflow

### Method 1: Direct Request
```
"Generate a commit message for my changes"
```
Claude will automatically call the subagent (if description is clear).

### Method 2: Explicit Call
```
"Call the commit-message-generator subagent"
```

### Method 3: With a Command

Create `.claude/commands/commit-with-message.md`:
```markdown
Generate a conventional commit message and create the commit.

## Instructions

1. Call the commit-message-generator subagent
2. Wait for the generated message
3. Review the message with the user
4. If approved, create the commit with that message
5. Show git log to confirm
```

Usage:
```
/commit-with-message
```

## Step 7: Enhance Your Subagent

### Add Team Conventions

```markdown
## Our Team's Conventions

### Scopes We Use
- `api` - Backend API
- `web` - Frontend web app
- `mobile` - Mobile app
- `infra` - Infrastructure/DevOps
- `db` - Database changes

### Required Footer
All commits must include ticket number:
\```
Relates-To: PROJ-123
\```

### Subject Format
Start with ticket number when applicable:
\```
feat(api): [PROJ-123] add user endpoint
\```
```

### Add Emoji Support (Optional)

```markdown
## Emoji Prefixes (Optional)

Our team uses emoji prefixes:
- ✨ feat
- 🐛 fix
- 📝 docs
- 💄 style
- ♻️  refactor
- ⚡ perf
- ✅ test
- 🔧 chore

Example:
\```
✨ feat(auth): add password reset
\```
```

### Add Validation

```markdown
## Validation Rules

Before generating, check:
1. ❌ No changes > 500 lines (suggest splitting)
2. ❌ No mixed types (feat + fix in same commit)
3. ❌ No direct commits to main/master
4. ✅ All tests are in test files
5. ✅ Breaking changes are marked

If validation fails, explain and suggest corrections.
```

## Step 8: Create Related Subagents

Now that you understand subagents, create more!

### Code Reviewer
```markdown
---
name: code-reviewer
description: Reviews code changes for quality, bugs, and best practices
allowed-tools: [Read, Grep, Bash]
---

# Code Reviewer

Specialized in reviewing code changes for:
- Potential bugs
- Code quality issues
- Best practice violations
- Security concerns

[Add detailed review guidelines]
```

### Test Writer
```markdown
---
name: test-writer
description: Generates unit tests for new code
allowed-tools: [Read, Write, Grep]
---

# Test Writer

Expert at creating comprehensive unit tests.

[Add test writing guidelines]
```

### Documentation Writer
```markdown
---
name: doc-writer
description: Writes clear documentation for code and APIs
allowed-tools: [Read, Write, Grep]
---

# Documentation Writer

Specializes in creating clear, helpful documentation.

[Add documentation guidelines]
```

## Common Issues & Solutions

### Issue 1: Subagent Doesn't Activate

**Problem:** Subagent doesn't get called automatically

**Solutions:**
1. Description must match use case
2. Call explicitly: "Call the [name] subagent"
3. Check file is in `.claude/agents/`
4. Verify YAML frontmatter is valid
5. Restart Claude Code

### Issue 2: Subagent Has Wrong Tools

**Problem:** Subagent can't access needed tools

**Solutions:**
1. Check `allowed-tools` in frontmatter
2. Add required tools: `[Bash, Read, Write]`
3. Don't give too many tools (principle of least privilege)

### Issue 3: Subagent Context Is Lost

**Problem:** Subagent forgets previous analysis

**This is by design!** Subagents have isolated context.

If you need persistent context, either:
- Use main Claude instead
- Have subagent write findings to a file
- Pass information explicitly

### Issue 4: Subagent Output Too Verbose

**Problem:** Subagent provides too much detail

**Solution:** Add instructions:
```markdown
## Output Format

Keep responses concise:
- Maximum 200 words
- Bullet points preferred
- Only include essential information
```

## Best Practices

### ✅ Do:
- Keep subagents focused on one task
- Restrict tools to minimum needed
- Write clear, detailed guidelines
- Include examples in subagent definition
- Test thoroughly
- Document when to use vs. main Claude

### ❌ Don't:
- Give subagents all tools
- Make subagents too general
- Use subagents for implementation
- Expect subagents to remember context
- Over-complicate simple tasks

## Subagent Design Patterns

### Pattern 1: Read-Only Analyzer
```yaml
allowed-tools: [Read, Grep, Bash]
purpose: Analysis without modification
examples: Code reviewer, security auditor, metrics analyzer
```

### Pattern 2: Generator
```yaml
allowed-tools: [Read, Write, Grep]
purpose: Create new files based on analysis
examples: Test generator, documentation writer, scaffold builder
```

### Pattern 3: Validator
```yaml
allowed-tools: [Read, Bash]
purpose: Check compliance with rules
examples: Code quality checker, style validator, security scanner
```

## When to Use Subagents

| Task | Use Subagent? | Why |
|------|---------------|-----|
| Code review | ✅ Yes | Isolated analysis, read-only |
| Writing tests | ✅ Yes | Focused task, separate context |
| Bug fixing | ❌ No | Needs full context, iteration |
| New feature | ❌ No | Complex, needs main context |
| Security audit | ✅ Yes | Specialized analysis |
| Refactoring | ❌ No | Needs full understanding |
| Documentation | ✅ Yes | Specific output, clear task |
| Commit messages | ✅ Yes | Simple, focused task |

## Next Steps

### Level 1: Practice
- Create 2-3 more subagents
- Use them in real projects
- Refine based on experience

### Level 2: Specialize
- Add domain-specific knowledge
- Create framework-specific reviewers
- Build team-specific subagents

### Level 3: Advanced
- Chain subagents together
- Create subagent workflows
- Build subagent libraries

## Congratulations!

You've created your first subagent! 🎉

**What you learned:**
- ✅ What subagents are and when to use them
- ✅ How to configure allowed tools
- ✅ Writing clear subagent instructions
- ✅ Providing examples and guidelines
- ✅ Testing subagents
- ✅ Main Claude vs. subagent tradeoffs
- ✅ Best practices for specialization

**Next challenges:**
1. Create a code-reviewer subagent
2. Build a test-writer subagent
3. Make a security-auditor subagent
4. Create subagents for your specific framework/language

---

**Ready for more? Continue with [mcp-workflow.md](./mcp-workflow.md)!**
