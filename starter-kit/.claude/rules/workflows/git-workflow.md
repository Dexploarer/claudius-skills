# Git Workflow - Starter Kit

> **Best practices for version control using Git with Claude Code**

---

## Overview

Git workflow using Starter Kit capabilities:
- **Skill:** `git-helper` (auto-assists with git)
- **Command:** `/commit` (automated commits)
- **Hooks:** Secret detection, force push prevention, .env protection

---

## Basic Git Workflow

### Standard Development Flow

```bash
1. Create/switch branch
2. Make changes
3. Stage changes
4. Commit → /commit or git-helper
5. Push to remote
```

---

## Available Git Tools

### 1. git-helper Skill (Auto-Invoked)
**Triggers:** "help with git", "create commit message", "git workflow"

**Example:**
```
You: "Help me create a good commit message for these authentication changes"

Claude: [git-helper activates]
        Analyzes changes and suggests:

        feat(auth): add JWT authentication

        - Implement JWT token generation
        - Add login endpoint with password validation
        - Add middleware for protected routes

        Closes #123
```

### 2. /commit Command
**Purpose:** Automated git commit workflow

**What it does:**
1. Runs `git status`
2. Runs `git diff`
3. Analyzes changes semantically
4. Generates conventional commit message
5. Stages files
6. Creates commit

**Example:**
```
You: /commit

Claude:
Running git status...
Running git diff...

Proposed commit:

feat(api): add user profile endpoints

- Add GET /api/users/:id endpoint
- Add PUT /api/users/:id endpoint
- Implement profile validation
- Add authentication middleware

Stage these files and commit? [y/n]
```

### 3. Safety Hooks
**Automatic Protection:**
- Secret detection in commits
- Force push prevention
- .env file warnings

---

## Commit Message Format

### Conventional Commits

**Structure:**
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

**Examples:**
```
feat(auth): add password reset functionality

fix(api): resolve null pointer in user lookup

docs(readme): add installation instructions

refactor(utils): simplify date formatting

test(auth): add edge cases for login
```

---

## Git Workflows

### Workflow 1: Feature Branch

```bash
# 1. Create feature branch
git checkout -b feat/user-authentication

# 2. Make changes
# Edit files...

# 3. Commit with Claude
You: /commit
Claude: [Creates conventional commit]

# 4. Push feature branch
git push -u origin feat/user-authentication

# 5. Create pull request
# (manually on GitHub, or use intermediate-kit /pr-creator)
```

**When to Use:**
- New features
- Non-urgent fixes
- Collaborative work

---

### Workflow 2: Quick Fix

```bash
# 1. Create fix branch
git checkout -b fix/login-validation

# 2. Fix the bug
# Edit file...

# 3. Test the fix
You: /test

# 4. Commit
You: /commit
Claude: fix(auth): validate email format in login

# 5. Push
git push -u origin fix/login-validation

# 6. Merge quickly
```

**When to Use:**
- Bug fixes
- Hotfixes
- Small corrections

---

### Workflow 3: Direct to Main (Simple Projects)

```bash
# Only for simple projects or solo development!

# 1. Make changes
# Edit files...

# 2. Commit
You: /commit

# Hook Warning if on main branch (can configure)

# 3. Push
git push origin main
```

**When to Use:**
- Personal projects
- Solo development
- Simple changes
- Documentation updates

---

## Branch Naming Conventions

### Feature Branches
```
feat/user-authentication
feat/payment-integration
feature/search-functionality
```

### Fix Branches
```
fix/login-validation
fix/memory-leak
bugfix/api-timeout
```

### Other Types
```
docs/api-documentation
refactor/user-service
test/integration-tests
chore/dependency-update
```

---

## Git Safety with Hooks

### Hook 1: Secret Detection

**Protects Against:**
- API keys in code
- Passwords
- Auth tokens
- Credentials

**Example Blocked Commit:**
```
You: /commit

Hook Output:
⚠️ Potential secret detected in commit!

Claude: Found potential secret in src/config.js:
const API_KEY = 'sk_live_abc123';

This appears to be an API key. Please:
1. Remove the hardcoded value
2. Add to .env file
3. Use process.env.API_KEY instead
```

**How to Fix:**
```javascript
// Before (BLOCKED)
const API_KEY = 'sk_live_abc123';

// After (SAFE)
const API_KEY = process.env.API_KEY;
```

```bash
# .env (not committed)
API_KEY=sk_live_abc123

# .env.example (committed)
API_KEY=your_api_key_here
```

---

### Hook 2: Force Push Prevention

**Protects Against:**
- Overwriting history
- Destroying teammates' work
- Irreversible changes

**Example Blocked:**
```
You: "git push -f origin main"

Hook Output:
⛔ Force push prevented! Use --force-with-lease if necessary.

Claude: Force push blocked for safety.

If you must force push:
1. Communicate with team
2. Ensure you have latest changes
3. Use: git push --force-with-lease
```

**When Force Push is OK:**
- Personal feature branches
- After interactive rebase
- Fixing commit messages
- With --force-with-lease

---

### Hook 3: .env File Protection

**Protects Against:**
- Committing secrets
- Exposing credentials
- Configuration leaks

**Example Blocked:**
```
You: "git add .env"

Hook Output:
⚠️ Attempting to commit .env file! This may contain secrets.

Claude: .env files should never be committed!

Fix:
1. Remove .env from staging: git reset .env
2. Add to .gitignore:
   echo ".env" >> .gitignore
3. Create .env.example instead:
   cp .env .env.example
   # Remove sensitive values
   git add .env.example
```

---

## Git Best Practices

### DO ✅

**Commit Often:**
```bash
# Make small, focused commits
git commit -m "feat(auth): add login validation"
git commit -m "test(auth): add login tests"
git commit -m "docs(auth): document login endpoint"
```

**Write Good Messages:**
```bash
# Good: Descriptive and specific
feat(api): add user profile endpoint with validation

# Bad: Vague
updated stuff
```

**Use Branches:**
```bash
# Keep main clean
git checkout -b feat/new-feature
# Work on branch
# Merge when ready
```

**Keep History Clean:**
```bash
# Squash before merging
git rebase -i main
# Combine related commits
```

### DON'T ❌

**Don't Commit Secrets:**
```bash
# ❌ NEVER
git add .env
git commit -m "add config"

# ✅ Instead
git add .env.example
```

**Don't Force Push to Main:**
```bash
# ❌ DANGEROUS
git push -f origin main

# ✅ Safe alternative
git push --force-with-lease origin feat/my-branch
```

**Don't Make Huge Commits:**
```bash
# ❌ Bad: Everything at once
git add .
git commit -m "many changes"

# ✅ Good: Focused commits
git add src/auth.js
git commit -m "feat(auth): add login"
git add tests/auth.test.js
git commit -m "test(auth): add login tests"
```

**Don't Skip Testing:**
```bash
# ❌ Bad
git commit -m "fix bug"
git push

# ✅ Good
/test
git commit -m "fix bug"
git push
```

---

## Common Git Scenarios

### Scenario 1: Merge Conflict

```bash
# During merge/pull
git pull origin main

# Conflict!
Auto-merging src/utils.js
CONFLICT (content): Merge conflict in src/utils.js

# Ask Claude for help
You: "Help me resolve this merge conflict in src/utils.js"

Claude: [Analyzes conflict]
        The conflict is between:
        - Your changes: Added new validation
        - Remote changes: Updated error handling

        Suggested resolution:
        [Shows combined version]

# After resolving
git add src/utils.js
git commit  # Uses default merge message
```

---

### Scenario 2: Undo Last Commit

```bash
# Committed too early
git commit -m "incomplete feature"

# Undo but keep changes
git reset HEAD~1

# Make more changes
# Then commit again
You: /commit
```

---

### Scenario 3: Change Last Commit Message

```bash
# Typo in commit message
git commit -m "feat(auth): add logn endpoint"  # Oops!

# Fix message
git commit --amend -m "feat(auth): add login endpoint"

# Or ask Claude
You: "Fix my last commit message - I meant login not logn"
```

---

### Scenario 4: Forgot to Add Files

```bash
# Committed without all files
git commit -m "feat(api): add endpoints"

# Realize you forgot tests
git add tests/api.test.js
git commit --amend --no-edit  # Add to previous commit
```

---

## Git Commands Reference

### Daily Commands

```bash
# Status
git status                 # Check current state
git diff                   # See unstaged changes
git diff --staged          # See staged changes

# Branching
git branch                 # List branches
git checkout -b feat/new   # Create and switch
git checkout main          # Switch to main
git branch -d feat/old     # Delete merged branch

# Staging
git add file.js            # Stage specific file
git add src/               # Stage directory
git add .                  # Stage all (use carefully!)
git reset file.js          # Unstage file

# Committing
/commit                    # Use Claude's /commit
git commit -m "message"    # Manual commit
git commit --amend         # Fix last commit

# Syncing
git pull origin main       # Get latest
git push origin feat/new   # Push branch
git push -u origin feat    # Push and track
```

### Occasionally Needed

```bash
# Stashing
git stash                  # Save work temporarily
git stash pop              # Restore stashed work
git stash list             # See stashed changes

# History
git log                    # Commit history
git log --oneline          # Compact history
git log --graph           # Visual history

# Undoing
git reset HEAD~1           # Undo last commit
git checkout -- file.js    # Discard file changes
git revert abc123          # Undo specific commit

# Remote
git remote -v              # List remotes
git remote add origin URL  # Add remote
git fetch origin           # Get remote updates
```

---

## Integrating with Claude Code

### Let Claude Help With Git

**For commit messages:**
```
You: "/commit"
You: "Help me write a commit message for these API changes"
You: "What's a good commit message for this bug fix?"
```

**For git advice:**
```
You: "Should I use merge or rebase here?"
You: "How do I undo my last 3 commits?"
You: "Help me resolve this merge conflict"
```

**For git operations:**
```
You: "Create a feature branch for user authentication"
You: "Clean up my git history before merging"
You: "Squash my last 5 commits"
```

---

## .gitignore Best Practices

### Essential .gitignore Entries

```gitignore
# Dependencies
node_modules/
vendor/

# Environment variables
.env
.env.local
.env.*.local

# Build outputs
dist/
build/
*.log

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Test coverage
coverage/
*.coverage

# Temporary
*.tmp
temp/
.cache/
```

### Check .gitignore

```bash
# What's being ignored?
git status --ignored

# Is this file ignored?
git check-ignore -v filename.txt
```

---

## Git Workflow Checklist

### Before Committing
- [ ] Code works
- [ ] Tests pass (`/test`)
- [ ] No secrets in code
- [ ] .env not staged
- [ ] Changes reviewed (`/review`)

### Committing
- [ ] Use `/commit` or conventional format
- [ ] Descriptive message
- [ ] Focused commit (one concern)
- [ ] Related files together

### Before Pushing
- [ ] Pull latest changes
- [ ] Resolve conflicts
- [ ] Tests still pass
- [ ] On correct branch

### Before Merging
- [ ] Branch up to date with main
- [ ] All tests pass
- [ ] Code reviewed
- [ ] CI/CD passes (if configured)

---

## Troubleshooting

### "Detached HEAD state"
```bash
# You checked out a commit, not a branch
git checkout main          # Go back to main
git checkout -b new-branch # Or create branch from here
```

### "Your branch has diverged"
```bash
# Local and remote have different histories
git pull --rebase origin main  # Rebase local on remote
# Or
git pull origin main           # Merge remote into local
```

### "Please commit or stash changes"
```bash
# Can't switch branches with changes
git stash              # Temporarily save changes
git checkout other-branch
git stash pop          # Restore changes
```

---

## Next Steps

**When Ready for Advanced Git:**
- Interactive rebase workflows
- Git hooks integration
- Automated PR creation
- Advanced branching strategies
- Git submodules

**Advanced Git Workflows:**
- Intermediate Kit: `/pr-creator` command
- GitHub Actions integration
- Automated testing on commits
- Release management

**Reference:** `@intermediate-kit/.claude/rules/workflows/git-workflow.md`

---

**Tools:** git-helper, /commit, safety hooks
**Philosophy:** Commit often, push safely, communicate clearly
**Last Updated:** 2025-11-01

