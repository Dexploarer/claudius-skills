# Starter Kit - Hooks Reference

> **Complete reference for event-driven automation hooks**

---

## Overview

Hooks are **event-driven automation** that execute shell commands in response to Claude Code events. They provide automatic validation, safety checks, and workflow automation.

**Configuration:** `starter-kit/.claude/settings.json`
**Total Hook Types:** 4 event types
**Total Configured Hooks:** 8+

---

## What Are Hooks?

**Hooks = Automatic Event-Driven Commands**

### Key Characteristics:
- **Event-Triggered:** Run automatically on events
- **Shell Commands:** Execute bash scripts
- **Exit Codes:** 0 = proceed, non-zero = block
- **Safety-First:** Prevent destructive operations
- **Context-Aware:** Access tool names, arguments

### Hook Types Available:

1. **SessionStart** - When Claude Code session begins
2. **PreToolUse** - Before a tool executes (can block)
3. **PostToolUse** - After a tool executes (monitoring)
4. **SessionEnd** - When session ends

---

## Hook Configuration Structure

```json
{
  "hooks": {
    "SessionStart": [/* hooks */],
    "PreToolUse": [/* hooks */],
    "PostToolUse": [/* hooks */],
    "SessionEnd": [/* hooks */]
  }
}
```

### Individual Hook Structure:
```json
{
  "event": "PreToolUse",
  "pattern": "Bash",           // Tool name regex
  "command": "echo 'Check'",   // Shell command
  "timeout": 5000,             // Max execution time (ms)
  "blocking": true             // Block on failure?
}
```

---

## SessionStart Hooks

### Purpose
Initialize session, display welcome messages, verify environment.

### Configured Hooks (1)

#### 1. Welcome Message
```json
{
  "event": "SessionStart",
  "command": "echo \"🚀 Claude Code session started at $(date)\"",
  "timeout": 1000
}
```

**What It Does:**
- Displays welcome message
- Shows current timestamp
- Confirms session initialization

**Example Output:**
```
🚀 Claude Code session started at Fri Nov  1 10:30:45 PDT 2025
```

### Custom SessionStart Ideas

**Environment Verification:**
```json
{
  "event": "SessionStart",
  "command": "node --version && npm --version",
  "timeout": 2000
}
```

**Git Status Check:**
```json
{
  "event": "SessionStart",
  "command": "git status --short",
  "timeout": 2000
}
```

**Load Project Context:**
```json
{
  "event": "SessionStart",
  "command": "cat .claude/project-context.md",
  "timeout": 1000
}
```

---

## PreToolUse Hooks (Safety Critical)

### Purpose
**Validate, prevent, and confirm before tools execute.**
These hooks can **BLOCK operations** by returning non-zero exit codes.

### Configured Hooks (6+)

#### 1. Secret Detection (Git Commits)
```json
{
  "event": "PreToolUse",
  "pattern": "Bash.*git.*commit",
  "command": "git diff --cached | grep -qiE '(api[_-]?key|secret|password|token)' && echo '⚠️ Potential secret detected in commit!' && exit 1 || exit 0",
  "blocking": true,
  "timeout": 5000
}
```

**Protects Against:**
- API keys in commits
- Passwords in code
- Secret tokens
- Authentication credentials

**Triggers When:**
- `git commit` command executed
- Changes are staged

**Exit Behavior:**
- **Exit 0:** No secrets found → Allow commit
- **Exit 1:** Secrets detected → BLOCK commit

**Example Blocked:**
```
You: "git commit -m 'add auth'"

Hook Output:
⚠️ Potential secret detected in commit!

Claude: The commit was blocked because potential secrets were detected.
Please review your changes and remove any sensitive data.
```

---

#### 2. Force Push Prevention
```json
{
  "event": "PreToolUse",
  "pattern": "Bash.*git.*push.*(-f|--force)",
  "command": "echo '⛔ Force push prevented! Use --force-with-lease if necessary.' && exit 1",
  "blocking": true,
  "timeout": 2000
}
```

**Protects Against:**
- Overwriting remote history
- Destroying teammates' commits
- Irreversible git operations

**Triggers When:**
- `git push -f` or `git push --force`

**Example Blocked:**
```
You: "git push -f origin main"

Hook Output:
⛔ Force push prevented! Use --force-with-lease if necessary.

Claude: Force push has been blocked for safety.
If you must force push, use: git push --force-with-lease
```

---

#### 3. .env File Security Check
```json
{
  "event": "PreToolUse",
  "pattern": "Bash.*git.*(add|commit).*\\.env",
  "command": "echo '⚠️ Attempting to commit .env file! This may contain secrets.' && exit 1",
  "blocking": true,
  "timeout": 2000
}
```

**Protects Against:**
- Committing environment variables
- Exposing configuration secrets
- Sharing credentials

**Triggers When:**
- `.env` file in git add/commit

**Example Blocked:**
```
You: "git add .env"

Hook Output:
⚠️ Attempting to commit .env file! This may contain secrets.

Claude: Blocked .env file from being committed.
Ensure .env is in .gitignore
Use .env.example for templates instead.
```

---

#### 4. Package Installation Reminder
```json
{
  "event": "PreToolUse",
  "pattern": "Bash.*(npm|yarn|pnpm) install",
  "command": "echo '📦 Installing packages... This may take a while.'",
  "timeout": 1000
}
```

**Purpose:**
- Inform about long-running operation
- Set expectations
- Confirm intentional installation

**Triggers When:**
- `npm install`, `yarn install`, or `pnpm install`

**Example:**
```
You: "npm install lodash"

Hook Output:
📦 Installing packages... This may take a while.

Claude: Installing lodash...
[Installation proceeds]
```

---

#### 5. Docker Cleanup Confirmation
```json
{
  "event": "PreToolUse",
  "pattern": "Bash.*docker.*(prune|rm|rmi).*-a",
  "command": "echo '🐳 This will remove all unused Docker resources. Continue? [y/N]' && read -r response && [[ \"$response\" =~ ^[Yy]$ ]] || exit 1",
  "blocking": true,
  "timeout": 30000
}
```

**Protects Against:**
- Accidental deletion of Docker images
- Removing active containers
- Loss of cached layers

**Triggers When:**
- `docker prune`, `docker rm`, `docker rmi` with `-a` flag

**Example:**
```
You: "docker system prune -a"

Hook Output:
🐳 This will remove all unused Docker resources. Continue? [y/N]

[Waits for user input]
```

---

#### 6. Database Migration Confirmation
```json
{
  "event": "PreToolUse",
  "pattern": "Bash.*(migrate|db:migrate)",
  "command": "echo '🗄️ Running database migration. Ensure you have a backup!' && sleep 2",
  "timeout": 5000
}
```

**Protects Against:**
- Unintentional schema changes
- Production database modifications
- Data loss

**Triggers When:**
- Migration commands executed

**Example:**
```
You: "npm run db:migrate"

Hook Output:
🗄️ Running database migration. Ensure you have a backup!

[2 second pause]
Claude: Proceeding with migration...
```

---

#### 7. Package.json Version Tracking
```json
{
  "event": "PreToolUse",
  "pattern": "Write.*package\\.json",
  "command": "echo '📝 package.json modified. Remember to update version if needed.'",
  "timeout": 1000
}
```

**Purpose:**
- Remind about semantic versioning
- Track dependency changes
- Prompt changelog updates

---

#### 8. Recursive Delete Protection
```json
{
  "event": "PreToolUse",
  "pattern": "Bash.*rm.*-r.*",
  "command": "echo '⚠️ Recursive delete detected! Verify the path.' && exit 1",
  "blocking": true,
  "timeout": 2000
}
```

**Protects Against:**
- Accidental directory deletion
- Recursive removal of important files
- Data loss

**Example Blocked:**
```
You: "rm -rf build/"

Hook Output:
⚠️ Recursive delete detected! Verify the path.

Claude: Recursive deletion blocked for safety.
Please confirm the path is correct.
```

---

## PostToolUse Hooks (Monitoring)

### Purpose
**Monitor, log, and alert after tools execute.**
Cannot block operations (already completed).

### Configured Hooks (3)

#### 1. File Modification Tracking
```json
{
  "event": "PostToolUse",
  "pattern": "(Write|Edit)",
  "command": "echo \"📝 File modified: $TOOL_NAME\"",
  "timeout": 1000
}
```

**What It Does:**
- Logs file writes/edits
- Tracks modifications
- Provides audit trail

**Example:**
```
[After file edit]

Hook Output:
📝 File modified: Edit
```

---

#### 2. Test Failure Alerts
```json
{
  "event": "PostToolUse",
  "pattern": "Bash.*test",
  "command": "if [ $TOOL_EXIT_CODE -ne 0 ]; then echo '❌ Tests failed! Exit code: '$TOOL_EXIT_CODE; fi",
  "timeout": 1000
}
```

**What It Does:**
- Detects test failures
- Shows exit code
- Highlights issues

**Example:**
```
[After test run with failures]

Hook Output:
❌ Tests failed! Exit code: 1
```

---

#### 3. Build Size Monitoring
```json
{
  "event": "PostToolUse",
  "pattern": "Bash.*(build|bundle)",
  "command": "if [ -d dist ]; then size=$(du -sh dist | cut -f1); echo \"📦 Build size: $size\"; fi",
  "timeout": 2000
}
```

**What It Does:**
- Measures build output
- Alerts to size increases
- Monitors bundle size

**Example:**
```
[After build completes]

Hook Output:
📦 Build size: 2.3M
```

---

## SessionEnd Hooks

### Purpose
**Cleanup, summarize, and save state when session ends.**

### Configured Hooks (1)

#### 1. Session Summary
```json
{
  "event": "SessionEnd",
  "command": "echo \"👋 Claude Code session ended at $(date)\"",
  "timeout": 1000
}
```

**What It Does:**
- Displays goodbye message
- Shows session end time
- Confirms cleanup

**Example:**
```
👋 Claude Code session ended at Fri Nov  1 15:45:30 PDT 2025
```

### Custom SessionEnd Ideas

**Save Session Statistics:**
```json
{
  "event": "SessionEnd",
  "command": "echo \"Session stats: $(git diff --stat)\" >> .claude/session-log.txt",
  "timeout": 2000
}
```

**Cleanup Temporary Files:**
```json
{
  "event": "SessionEnd",
  "command": "rm -f .claude/temp-*",
  "timeout": 2000
}
```

---

## Hook Best Practices

### Security Hooks (PreToolUse)
✅ **DO:**
- Block dangerous operations
- Validate inputs
- Check for secrets
- Require confirmations

❌ **DON'T:**
- Make hooks too slow (< 5s)
- Block routine operations
- Ignore exit codes
- Create false positives

### Monitoring Hooks (PostToolUse)
✅ **DO:**
- Log important operations
- Track metrics
- Alert on failures
- Keep lightweight

❌ **DON'T:**
- Block operations (can't anyway)
- Produce too much output
- Run expensive operations
- Ignore errors

### Performance
- **Timeout:** Set appropriate timeouts (1-5s typical)
- **Blocking:** Only use for safety-critical hooks
- **Commands:** Keep simple and fast
- **Patterns:** Use specific regex patterns

---

## Hook Pattern Matching

### Tool Name Patterns
```
"Bash"              → Matches Bash tool
"Bash.*git"         → Bash with git command
"Write.*\\.env"     → Write to .env files
"(Write|Edit)"      → Write OR Edit tools
```

### Command Patterns
```
"Bash.*commit"             → git commit
"Bash.*push.*-f"           → force push
"Bash.*rm.*-r"             → recursive delete
"Bash.*(npm|yarn) install" → package install
```

---

## Environment Variables in Hooks

### Available Variables:
- `$TOOL_NAME` - Name of tool executed
- `$TOOL_EXIT_CODE` - Exit code (PostToolUse only)
- `$TOOL_ARGS` - Tool arguments (if available)

### Example Usage:
```json
{
  "event": "PostToolUse",
  "pattern": "Bash",
  "command": "echo \"Executed: $TOOL_NAME with exit code: $TOOL_EXIT_CODE\"",
  "timeout": 1000
}
```

---

## Adding Custom Hooks

### 1. Edit settings.json
```bash
code starter-kit/.claude/settings.json
```

### 2. Add Hook Entry
```json
{
  "hooks": {
    "PreToolUse": [
      /* existing hooks */,
      {
        "event": "PreToolUse",
        "pattern": "YourPattern",
        "command": "your-command",
        "blocking": true,
        "timeout": 5000
      }
    ]
  }
}
```

### 3. Test Hook
```bash
# Trigger the hook
# Verify behavior
# Check exit codes
```

---

## Debugging Hooks

### Hook Not Triggering?
1. Check pattern regex
2. Verify event type
3. Test command separately
4. Check timeout setting

### Hook Blocking Incorrectly?
1. Check exit code (0 = success)
2. Test command in terminal
3. Verify blocking: true
4. Check timeout isn't expiring

### Hook Command Failing?
1. Run command directly in terminal
2. Check environment variables
3. Verify file paths
4. Increase timeout if needed

---

## Security Considerations

### What Hooks CAN'T Protect Against:
- Direct file system access outside Claude Code
- Manual git commands outside Claude
- External scripts and tools
- Malicious hook commands themselves

### Layered Security:
1. **Hooks:** First line of defense
2. **.gitignore:** Prevent tracking sensitive files
3. **Pre-commit:** Additional git hooks
4. **Code Review:** Human verification
5. **CI/CD:** Automated scanning

---

## Common Hook Recipes

### Prevent Commits to Main
```json
{
  "event": "PreToolUse",
  "pattern": "Bash.*git.*commit",
  "command": "branch=$(git branch --show-current); if [ \"$branch\" = \"main\" ]; then echo '⛔ Direct commits to main blocked!'; exit 1; fi",
  "blocking": true,
  "timeout": 2000
}
```

### Require Commit Message Format
```json
{
  "event": "PreToolUse",
  "pattern": "Bash.*git.*commit.*-m",
  "command": "git log -1 --pretty=%B | grep -qE '^(feat|fix|docs|style|refactor|test|chore):' || (echo '❌ Use conventional commit format!'; exit 1)",
  "blocking": true,
  "timeout": 2000
}
```

### Auto-format Before Commit
```json
{
  "event": "PreToolUse",
  "pattern": "Bash.*git.*commit",
  "command": "npm run format",
  "timeout": 10000
}
```

### Backup Before Destructive Ops
```json
{
  "event": "PreToolUse",
  "pattern": "Bash.*rm.*-rf",
  "command": "echo '💾 Creating backup...' && tar -czf backup-$(date +%s).tar.gz .",
  "timeout": 30000
}
```

---

## Hook Reference Summary

| Hook Type | Count | Can Block | Purpose | Example |
|-----------|-------|-----------|---------|---------|
| SessionStart | 1 | ❌ | Initialize | Welcome message |
| PreToolUse | 6+ | ✅ | Validate/Prevent | Secret detection |
| PostToolUse | 3 | ❌ | Monitor/Log | Track changes |
| SessionEnd | 1 | ❌ | Cleanup | Session summary |

---

## Next Level Hooks

**Ready for advanced hooks?**
- Intermediate Kit: Enhanced hook configurations
- Advanced patterns and workflows
- Integration with CI/CD
- Custom validation logic

**Reference:** `@intermediate-kit/.claude/rules/hooks-reference.md`

---

**Configuration:** `starter-kit/.claude/settings.json`
**Total Hooks:** 11 configured
**Safety Level:** Beginner-friendly with essential protections
**Last Updated:** 2025-11-01

