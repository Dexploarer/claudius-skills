# Intermediate Kit - Hooks Reference

> **Comprehensive guide to production-aware event-driven automation**
> Advanced safety hooks and monitoring for professional development

---

## 📋 Hooks Overview

The Intermediate Kit includes **enhanced hooks** across all event types:
- **SessionStart:** Environment initialization
- **PreToolUse:** Production-aware safety checks (8 hooks)
- **PostToolUse:** Monitoring and tracking (3 hooks)
- **SessionEnd:** Summary and reminders

All hooks are configured in: `intermediate-kit/.claude/settings.json`

---

## 🎯 Hook Types

### SessionStart Hooks

**Trigger:** When Claude Code session begins

**Purpose:** Welcome message and environment setup

**Hook Configuration:**
```json
{
  "command": "echo '\n🚀 Intermediate Dev Environment Loaded! 🚀\n📅 '$(date '+%Y-%m-%d %H:%M:%S')'\n📂 '$(pwd)'\n💡 Use /help to see available commands\n'",
  "description": "Welcome message for intermediate developers"
}
```

**What It Does:**
- Displays welcome banner
- Shows current date/time
- Shows working directory
- Reminds about /help command

**Example Output:**
```
🚀 Intermediate Dev Environment Loaded! 🚀
📅 2025-11-01 14:30:00
📂 /home/user/my-project
💡 Use /help to see available commands
```

---

## 🛡️ PreToolUse Hooks (Safety First)

### 1. Comprehensive Secret Detection

**Pattern:** `Bash.*git commit`

**Purpose:** Prevent committing secrets to version control

**Hook Configuration:**
```json
{
  "pattern": "Bash.*git commit",
  "command": "if git diff --cached | grep -qE '(password|api_key|secret|token|private_key)\\s*=\\s*[\"'\\''`]'; then echo '⚠️  WARNING: Potential secret detected in commit!' >&2; echo 'Files with secrets:' >&2; git diff --cached --name-only | xargs grep -l -E '(password|api_key|secret|token)' >&2; exit 2; fi",
  "timeout": 5000,
  "description": "Comprehensive secret detection before commits"
}
```

**What It Checks:**
- `password` assignments
- `api_key` assignments
- `secret` assignments
- `token` assignments
- `private_key` assignments

**Action:** Blocks commit and shows affected files

**Example:**
```
⚠️  WARNING: Potential secret detected in commit!
Files with secrets:
src/config/database.ts
.env.production

Commit blocked! Remove secrets before committing.
```

**How to Fix:**
1. Remove hardcoded secrets
2. Move to environment variables
3. Use .env files (excluded from git)
4. Consider using secret management (Vault, AWS Secrets Manager)

---

### 2. Force Push Protection

**Pattern:** `Bash.*git push.*-f`

**Purpose:** Prevent destructive force pushes, especially to main/master

**Hook Configuration:**
```json
{
  "pattern": "Bash.*git push.*-f",
  "command": "BRANCH=$(git branch --show-current); if [ \"$BRANCH\" = \"main\" ] || [ \"$BRANCH\" = \"master\" ]; then echo '❌ BLOCKED: Force push to main/master is not allowed!' >&2; exit 2; fi; echo '⚠️  Force push detected on branch: '$BRANCH >&2; read -p 'Type FORCE to confirm: ' confirm; if [ \"$confirm\" != \"FORCE\" ]; then echo 'Force push cancelled' >&2; exit 2; fi",
  "timeout": 30000,
  "description": "Prevent force push to main/master, confirm for other branches"
}
```

**Behavior:**
- **main/master:** Completely blocked
- **Other branches:** Requires confirmation

**Example (main/master):**
```
❌ BLOCKED: Force push to main/master is not allowed!
```

**Example (feature branch):**
```
⚠️  Force push detected on branch: feature/user-auth
Type FORCE to confirm: _
```

**When to Force Push:**
- Rebasing feature branches
- Cleaning up commit history
- After amending commits
- **NEVER** on main/master

---

### 3. .env File Protection

**Pattern:** `Write.*\\.env$`

**Purpose:** Warn if .env file is not in .gitignore

**Hook Configuration:**
```json
{
  "pattern": "Write.*\\.env$",
  "command": "if ! grep -q '^\\.env$' .gitignore 2>/dev/null; then echo '⚠️  WARNING: .env is not in .gitignore!' >&2; echo 'Add .env to .gitignore before committing' >&2; fi",
  "description": "Warn if .env is not in .gitignore"
}
```

**What It Checks:**
- Verifies .gitignore exists
- Checks if `.env` is in .gitignore

**Example:**
```
⚠️  WARNING: .env is not in .gitignore!
Add .env to .gitignore before committing
```

**Recommended .gitignore entries:**
```
.env
.env.local
.env.production
.env.*.local
*.env
```

---

### 4. Package Installation Reminder

**Pattern:** `Bash.*npm install [^-]|Bash.*yarn add [^-]`

**Purpose:** Remind to commit package.json and lock files

**Hook Configuration:**
```json
{
  "pattern": "Bash.*npm install [^-]|Bash.*yarn add [^-]",
  "command": "echo '📦 Installing package...' && echo 'Remember to commit package.json and lock file'",
  "description": "Reminder to commit dependency changes"
}
```

**Example:**
```
📦 Installing package...
Remember to commit package.json and lock file

After installation:
✅ git add package.json package-lock.json
✅ git commit -m "chore: add lodash dependency"
```

**Files to Commit:**
- `package.json`
- `package-lock.json` (npm)
- `yarn.lock` (yarn)
- `pnpm-lock.yaml` (pnpm)

---

### 5. Docker Cleanup Confirmation

**Pattern:** `Bash.*docker.*rm|Bash.*docker.*prune`

**Purpose:** Confirm before removing Docker resources

**Hook Configuration:**
```json
{
  "pattern": "Bash.*docker.*rm|Bash.*docker.*prune",
  "command": "echo '⚠️  WARNING: Docker cleanup operation detected' >&2; read -p 'This will remove Docker resources. Continue? (y/N): ' confirm; if [ \"$confirm\" != \"y\" ]; then exit 2; fi",
  "timeout": 30000,
  "description": "Confirm before Docker cleanup operations"
}
```

**What It Protects:**
- `docker rm` - Remove containers
- `docker prune` - Remove unused resources

**Example:**
```
⚠️  WARNING: Docker cleanup operation detected
This will remove Docker resources. Continue? (y/N): _
```

**Safe Docker Commands:**
- `docker ps` - List (no confirmation needed)
- `docker images` - List (no confirmation needed)
- `docker rm <specific-container>` - Requires confirmation
- `docker system prune` - Requires confirmation

---

### 6. Database Migration Confirmation

**Pattern:** `Bash.*(migrate|migration).*(?!status|show)`

**Purpose:** Confirm before running database migrations

**Hook Configuration:**
```json
{
  "pattern": "Bash.*(migrate|migration).*(?!status|show)",
  "command": "echo '⚠️  Database migration detected' >&2; echo 'Current branch: '$(git branch --show-current) >&2; read -p 'Run migration? (y/N): ' confirm; if [ \"$confirm\" != \"y\" ]; then exit 2; fi",
  "timeout": 30000,
  "description": "Confirm before running database migrations"
}
```

**What It Does:**
- Shows current git branch
- Requires confirmation
- Reminds about backup

**Example:**
```
⚠️  Database migration detected
Current branch: feature/add-user-roles
Run migration? (y/N): _
```

**Migration Best Practices:**
1. **Always backup** before migrations
2. **Test migrations** on development first
3. **Review SQL** before applying
4. **Have rollback plan** ready
5. **Run on correct branch** (check git branch)

**Commands that DON'T trigger:**
- `python manage.py migrate --status`
- `alembic history`
- `prisma migrate status`

---

### 7. Version Bump Suggestion

**Pattern:** `Edit.*package\\.json`

**Purpose:** Suggest using /version-bump for version changes

**Hook Configuration:**
```json
{
  "pattern": "Edit.*package\\.json",
  "command": "if git diff package.json | grep -q '\"version\":'; then echo '📦 Version change detected in package.json' && echo 'Consider running /version-bump instead for proper version management'; fi",
  "description": "Suggest using version-bump command"
}
```

**What It Does:**
- Detects version field changes
- Suggests using /version-bump command
- Ensures proper semantic versioning

**Example:**
```
📦 Version change detected in package.json
Consider running /version-bump instead for proper version management

Better approach:
/version-bump patch  # 1.0.0 → 1.0.1
/version-bump minor  # 1.0.0 → 1.1.0
/version-bump major  # 1.0.0 → 2.0.0
```

**Benefits of /version-bump:**
- Updates CHANGELOG.md
- Creates git tag
- Follows semantic versioning
- Commits with standard message

---

### 8. Recursive Delete Protection

**Pattern:** `Bash.*rm.*-rf`

**Purpose:** Prevent accidental recursive deletions

**Hook Configuration:**
```json
{
  "pattern": "Bash.*rm.*-rf",
  "command": "echo '⚠️  DANGER: Recursive delete operation!' >&2; echo 'Files/folders to be deleted:' >&2; echo \"$(echo \"$TOOL_USE\" | grep -o 'rm.*' | sed 's/rm -rf //')\" >&2; read -p 'Type DELETE to confirm: ' confirm; if [ \"$confirm\" != \"DELETE\" ]; then exit 2; fi",
  "timeout": 30000,
  "description": "Confirm dangerous recursive delete operations"
}
```

**What It Does:**
- Shows what will be deleted
- Requires typing "DELETE" to confirm
- Prevents accidental data loss

**Example:**
```
⚠️  DANGER: Recursive delete operation!
Files/folders to be deleted:
node_modules/
Type DELETE to confirm: _
```

**Safe Alternatives:**
- Use specific file paths
- Use .gitignore instead of deleting
- Use `/clean` command for build artifacts
- Consider `git clean -fd` for git-ignored files

---

## 📊 PostToolUse Hooks (Monitoring)

### 1. File Modification Tracking

**Pattern:** `Write|Edit`

**Purpose:** Track and count file modifications

**Hook Configuration:**
```json
{
  "pattern": "Write|Edit",
  "command": "FILES_MODIFIED=$((FILES_MODIFIED + 1)); echo '✅ File modified ['$FILES_MODIFIED'] at '$(date '+%H:%M:%S')",
  "description": "Track file modifications with counter"
}
```

**Example:**
```
✅ File modified [1] at 14:30:15
✅ File modified [2] at 14:30:42
✅ File modified [3] at 14:31:03
```

**Use Cases:**
- Track productivity
- Session summary
- Code review preparation

---

### 2. Test Failure Alerts

**Pattern:** `Bash.*npm test|Bash.*pytest|Bash.*go test`

**Purpose:** Alert on test failures

**Hook Configuration:**
```json
{
  "pattern": "Bash.*npm test|Bash.*pytest|Bash.*go test",
  "command": "if echo \"$TOOL_RESULT\" | grep -q 'FAIL\\|failed\\|Error'; then echo '❌ Tests failed - review before committing' >&2; else echo '✅ Tests passed'; fi",
  "description": "Alert on test failures"
}
```

**Example (Pass):**
```
✅ Tests passed
```

**Example (Fail):**
```
❌ Tests failed - review before committing
```

**Next Steps on Failure:**
1. Review test output
2. Fix failing tests
3. Re-run tests
4. **Never commit** with failing tests

---

### 3. Build Size Monitoring

**Pattern:** `Bash.*npm run build|Bash.*yarn build`

**Purpose:** Monitor build size and warn if too large

**Hook Configuration:**
```json
{
  "pattern": "Bash.*npm run build|Bash.*yarn build",
  "command": "if [ -d 'dist' ] || [ -d 'build' ]; then SIZE=$(du -sh dist build 2>/dev/null | head -1 | cut -f1); echo '📦 Build size: '$SIZE; if du -sb dist build 2>/dev/null | head -1 | awk '{if ($1 > 1048576) exit 1}'; then echo '⚠️  Build size exceeds 1MB - consider optimization'; fi; fi",
  "description": "Report build size and warn if too large"
}
```

**Example (Good):**
```
📦 Build size: 850K
```

**Example (Warning):**
```
📦 Build size: 2.3M
⚠️  Build size exceeds 1MB - consider optimization
```

**Optimization Steps:**
1. Run `/bundle-analyze`
2. Check for large dependencies
3. Implement code splitting
4. Use tree shaking
5. Compress assets

---

## 👋 SessionEnd Hook

**Trigger:** When Claude Code session ends

**Purpose:** Provide session summary

**Hook Configuration:**
```json
{
  "command": "echo '\n👋 Session Complete\n⏱️  '$(date '+%H:%M:%S')'\n📊 Files modified: '${FILES_MODIFIED:-0}'\n💾 Remember to commit your changes!\n'",
  "description": "Summary on session end"
}
```

**Example:**
```
👋 Session Complete
⏱️  16:45:30
📊 Files modified: 12
💾 Remember to commit your changes!
```

---

## 🎯 Hook Management

### Viewing Active Hooks

All hooks are in: `intermediate-kit/.claude/settings.json`

```bash
# View hooks
cat .claude/settings.json | grep -A5 "hooks"
```

### Customizing Hooks

**Add New Hook:**
```json
{
  "pattern": "Bash.*npm publish",
  "command": "echo 'Publishing to npm registry...' && read -p 'Confirm publish (y/N): ' confirm; if [ \"$confirm\" != \"y\" ]; then exit 2; fi",
  "timeout": 30000,
  "description": "Confirm npm publish"
}
```

**Modify Existing Hook:**
Edit the `command` field in `settings.json`

**Disable Hook:**
Comment out or remove the hook object

---

## 💡 Best Practices

### Hook Development

1. **Test hooks locally** before committing
2. **Use appropriate timeouts** (30s for confirmations)
3. **Provide clear error messages**
4. **Exit with code 2** to block operations
5. **Use >&2** for warnings/errors

### Hook Debugging

```bash
# Test hook command directly
if git diff --cached | grep -qE '(password|api_key)'; then
  echo "Secret detected!"
fi
```

### Hook Maintenance

1. **Review hooks monthly**
2. **Update patterns** as needed
3. **Add new hooks** for new workflows
4. **Document custom hooks**

---

## 🔗 Related References

**Settings File:**
- Configuration: `@intermediate-kit/.claude/settings.json`

**Other References:**
- Skills: `@intermediate-kit/.claude/rules/skills-reference.md`
- Commands: `@intermediate-kit/.claude/rules/commands-reference.md`
- Agents: `@intermediate-kit/.claude/rules/agents-reference.md`

**Workflow Rules:**
- Security: `@intermediate-kit/.claude/rules/workflows/security.md`
- Deployment: `@intermediate-kit/.claude/rules/workflows/deployment.md`
- Git Workflow: `@intermediate-kit/.claude/rules/workflows/git-workflow.md`

---

## 📚 Hook Summary Table

| Hook | Type | Pattern | Purpose | Blocking |
|------|------|---------|---------|----------|
| Secret Detection | PreToolUse | `git commit` | Prevent secret commits | Yes |
| Force Push | PreToolUse | `git push -f` | Prevent destructive pushes | Yes (main/master) |
| .env Warning | PreToolUse | `Write .env` | Warn about .gitignore | No |
| Package Install | PreToolUse | `npm install` | Remind to commit | No |
| Docker Cleanup | PreToolUse | `docker rm/prune` | Confirm cleanup | Yes |
| Migration | PreToolUse | `migrate` | Confirm migration | Yes |
| Version Bump | PreToolUse | `Edit package.json` | Suggest /version-bump | No |
| Delete | PreToolUse | `rm -rf` | Confirm deletion | Yes |
| File Modified | PostToolUse | `Write/Edit` | Track changes | No |
| Test Failure | PostToolUse | `npm test` | Alert on failure | No |
| Build Size | PostToolUse | `npm run build` | Monitor size | No |

---

**Last Updated:** 2025-11-01
**Total Hooks:** 12 (8 PreToolUse, 3 PostToolUse, 1 SessionStart, 1 SessionEnd)
**Level:** Intermediate (Production-Ready)
