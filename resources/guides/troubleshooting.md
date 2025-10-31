# Troubleshooting Guide

Solutions to common problems with Claude Code and its Five Pillars.

## Quick Diagnosis

**Problem Category:**
- [Installation & Setup](#installation--setup)
- [Skills Not Working](#skills-not-working)
- [Commands Not Found](#commands-not-found)
- [Hooks Not Running](#hooks-not-running)
- [Subagents Issues](#subagents-issues)
- [MCP Server Problems](#mcp-server-problems)
- [Performance Issues](#performance-issues)
- [Error Messages](#common-error-messages)

---

## Installation & Setup

### Claude Code won't start

**Symptom:**
```bash
claude
# command not found: claude
```

**Solutions:**

1. **Verify installation:**
```bash
which claude
# If empty, Claude Code isn't installed
```

2. **Reinstall:**
```bash
# macOS
brew install claude

# Linux/macOS
curl -fsSL https://claude.ai/install.sh | sh

# Add to PATH if needed
export PATH="$HOME/.claude/bin:$PATH"
```

3. **Check version:**
```bash
claude --version
```

### Authentication fails

**Symptom:**
```
Error: Authentication required
```

**Solutions:**

1. **Login again:**
```bash
claude login
```

2. **Check credentials:**
```bash
cat ~/.claude/config
# Verify API key is present
```

3. **Try different account:**
- Console account vs Claude.ai account
- Check which one you're using

---

## Skills Not Working

### Skill never activates

**Symptom:** You have a skill, but Claude never uses it.

**Diagnosis Checklist:**

1. **Check file location:**
```bash
ls .claude/skills/
# Skill file should be here
```

2. **Verify filename:**
```bash
# Should be: skill-name.md
# Not: skill-name.txt or skill-name
```

3. **Check YAML syntax:**
```yaml
---
name: my-skill  # ✅ Correct
description: What it does
---

# ❌ Wrong - missing closing ---
name: my-skill
description: What it does

# ❌ Wrong - incorrect format
name = my-skill
```

4. **Test description specificity:**

❌ **Too vague:**
```yaml
description: For code
```

✅ **Specific:**
```yaml
description: Generate React components with TypeScript when user asks to create a component or new React file
```

5. **Try different phrasings:**
```bash
# If description says "when user wants to create React components"
# Try:
"Create a React component"
"I need a new component"
"Generate a Button component"
"Make me a component for user login"
```

**Solution:**

Make description more specific with trigger phrases:
```yaml
description: Generate React components. Use when user says "create component", "new component", "make a component", or "generate component"
```

### Skill activates but fails

**Symptom:** Skill activates but doesn't work correctly.

**Diagnosis:**

1. **Check tool restrictions:**
```yaml
---
name: file-creator
description: Creates files
allowed-tools: [Read]  # ❌ Can't create files with only Read!
---

# Fix:
allowed-tools: [Read, Write]  # ✅
```

2. **Test instructions manually:**
```bash
# Read the skill instructions
cat .claude/skills/my-skill.md

# Try following them manually
# Do they work? Are they clear?
```

3. **Check for errors in logic:**
```markdown
## Instructions

1. Read the file
2. If file doesn't exist, throw error  # ❌ Should handle this gracefully
3. Process file
```

**Solution:**

Add error handling:
```markdown
## Instructions

1. Try to read the file
2. If file doesn't exist:
   - Create it with default content
   - Or ask user what to do
3. Process file
```

---

## Commands Not Found

### /command not recognized

**Symptom:**
```bash
/mycommand
# Unknown command: /mycommand
```

**Diagnosis:**

1. **Check file exists:**
```bash
ls .claude/commands/
# Should see: mycommand.md
```

2. **Verify filename matches:**
```bash
# File: mycommand.md
# Use: /mycommand
# NOT /my-command or /my_command
```

3. **Check file extension:**
```bash
# ✅ Correct: mycommand.md
# ❌ Wrong: mycommand.txt
# ❌ Wrong: mycommand
```

4. **Restart Claude Code:**
```bash
# Exit and restart
exit
claude
```

**Solution:**

Ensure correct structure:
```bash
.claude/
└── commands/
    └── mycommand.md  # File name = command name

# Use as: /mycommand
```

### Command runs but does nothing

**Symptom:** Command executes but produces no output.

**Diagnosis:**

1. **Check file has content:**
```bash
cat .claude/commands/mycommand.md
# Should have instructions, not be empty
```

2. **Verify instructions are clear:**
```markdown
# ❌ Too vague
Do the thing

# ✅ Specific
Run all tests using npm test and summarize the results.
Show:
1. Number of tests passed
2. Number of tests failed
3. List failed tests
4. Overall status
```

**Solution:**

Add detailed, step-by-step instructions.

---

## Hooks Not Running

### Hook never executes

**Symptom:** Hook is configured but never runs.

**Diagnosis:**

1. **Check settings.json syntax:**
```bash
# Validate JSON
cat .claude/settings.json | jq .
# If error, JSON is malformed
```

2. **Common JSON errors:**
```json
{
  "hooks": {
    "PreToolUse": [{
      "command": "echo 'test'",  // ❌ Missing comma
      "description": "test"
    }]  // ❌ Extra comma
  },
}
```

**Fixed:**
```json
{
  "hooks": {
    "PreToolUse": [{
      "command": "echo 'test'",
      "description": "test"
    }]
  }
}
```

3. **Verify event name:**
```json
{
  "hooks": {
    "preToolUse": [...]  // ❌ Wrong case
    "PreToolUse": [...]  // ✅ Correct
  }
}
```

**Valid events:**
- `SessionStart`
- `SessionEnd`
- `PreToolUse`
- `PostToolUse`
- `UserPromptSubmit`
- `Stop`
- `SubagentStop`

4. **Test pattern matching:**
```json
{
  "pattern": "Edit"  // Matches only Edit tool
  "pattern": "Edit|Write"  // Matches Edit OR Write
  "pattern": "Bash.*git"  // Matches Bash tools with 'git' in args
}
```

**Solution:**

Enable debug mode to see hook execution:
```bash
claude --debug
```

### Hook command fails

**Symptom:** Hook runs but returns error.

**Diagnosis:**

1. **Test command separately:**
```bash
# If hook command is:
git diff --cached | grep -i password

# Test it:
cd your-project
git add .
git diff --cached | grep -i password
echo $?  # Check exit code
```

2. **Check for missing dependencies:**
```bash
# If command uses 'jq'
which jq
# If empty, jq not installed
```

3. **Verify file paths:**
```json
{
  "command": "./scripts/check.sh"  // ❌ Relative path
  "command": "/full/path/to/check.sh"  // ✅ Absolute path
}
```

4. **Check permissions:**
```bash
ls -l scripts/check.sh
# Should be executable
chmod +x scripts/check.sh
```

**Solution:**

Use absolute paths and test commands first:
```bash
# Test command
/full/path/to/script.sh

# Add to hook only after it works
```

### Hook timeout

**Symptom:**
```
Hook timeout after 5000ms
```

**Solution:**

Increase timeout for slow operations:
```json
{
  "hooks": {
    "PostToolUse": [{
      "command": "npm test",
      "timeout": 60000  // 60 seconds
    }]
  }
}
```

---

## Subagents Issues

### Subagent not available

**Symptom:**
```
"Use the myagent subagent to review code"
# Subagent 'myagent' not found
```

**Diagnosis:**

1. **Check file location:**
```bash
ls .claude/agents/
# Should see: myagent.md
```

2. **Verify YAML frontmatter:**
```yaml
---
name: myagent  # ✅ Correct
description: What it does
---

# ❌ Wrong - missing dashes
name: myagent
description: What it does
```

3. **List available subagents:**
```bash
/agents
# See all available subagents
```

**Solution:**

Ensure proper file structure:
```bash
.claude/
└── agents/
    └── myagent.md

# YAML at top:
---
name: myagent
description: ...
---
```

### Subagent can't perform action

**Symptom:**
```
Subagent cannot write files (tool not allowed)
```

**Diagnosis:**

Check `allowed-tools`:
```yaml
---
name: test-writer
description: Writes tests
allowed-tools: [Read]  # ❌ Can't write with only Read!
---
```

**Solution:**

Add necessary tools:
```yaml
allowed-tools: [Read, Write, Bash, Grep, Glob]
```

---

## MCP Server Problems

### MCP server won't connect

**Symptom:**
```
Error: Failed to connect to MCP server 'github'
```

**Diagnosis:**

1. **Check .mcp.json exists:**
```bash
ls .mcp.json
# If not found, create it
```

2. **Verify server is enabled:**
```json
{
  "mcpServers": {
    "github": {
      "disabled": false  // ✅ Must be false
    }
  }
}
```

3. **Check credentials:**
```json
{
  "env": {
    "GITHUB_TOKEN": "ghp_..."  // Should be actual token
  }
}
```

4. **Test server package:**
```bash
# For npx-based servers
npx -y @modelcontextprotocol/server-github --version
```

5. **Check network:**
```bash
# Can you reach the internet?
ping github.com
```

**Solution:**

Debug with:
```bash
claude --debug
# Shows MCP connection attempts
```

### MCP authentication fails

**Symptom:**
```
Error: Authentication failed for MCP server
```

**Solutions:**

1. **Regenerate credentials:**
```bash
# For GitHub: Create new personal access token
# https://github.com/settings/tokens
```

2. **Check token permissions:**
```
# GitHub PAT needs:
- repo (for private repos)
- read:org (for organizations)
```

3. **Use environment variables:**
```bash
# In shell
export GITHUB_TOKEN="your-token"

# In .mcp.json
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

---

## Performance Issues

### Claude Code is slow

**Diagnosis:**

1. **Too many skills:**
```bash
ls .claude/skills/ | wc -l
# If > 30, might be slow
```

**Solution:** Combine or remove unused skills.

2. **Skills too large:**
```bash
wc -l .claude/skills/*
# If any > 500 lines, split or simplify
```

3. **Hooks taking too long:**
```json
{
  "hooks": {
    "PreToolUse": [{
      "command": "npm test",  // ❌ Too slow for pre-hook
      "timeout": 120000
    }]
  }
}
```

**Solution:** Move slow operations to post-hooks or remove.

### Memory issues

**Symptom:**
```
Error: Out of memory
```

**Solutions:**

1. **Reduce context:**
- Fewer skills
- Smaller skill files
- Use subagents (separate context)

2. **Clear conversation:**
```bash
/clear
```

---

## Common Error Messages

### "YAML parse error"

**Cause:** Malformed YAML frontmatter

**Fix:**
```yaml
# ❌ Wrong
---
name: my-skill
description: Does things
// ❌ Wrong comment style

# ✅ Correct
---
name: my-skill
description: Does things
---
# Correct comment after frontmatter
```

### "Tool not allowed"

**Cause:** Skill/subagent trying to use restricted tool

**Fix:**
```yaml
# Add tool to allowed list
allowed-tools: [Read, Write, Bash]
```

### "Hook command failed with exit code 2"

**Cause:** Hook intentionally blocking operation

**Check:**
```bash
# Hook output should explain why
# Check stderr for error message
```

### "MCP server not found"

**Cause:** Server not installed or configured

**Fix:**
```bash
# Install server
claude mcp add github

# Or manually configure in .mcp.json
```

---

## Debug Mode

### Enable debug output

```bash
claude --debug
```

**Shows:**
- Skill activation attempts
- Hook executions
- MCP server connections
- Tool usage
- Error details

### Debug specific issue

```bash
# Debug with verbose logging
CLAUDE_DEBUG=1 claude

# Debug MCP only
CLAUDE_DEBUG_MCP=1 claude

# Debug hooks only
CLAUDE_DEBUG_HOOKS=1 claude
```

---

## Getting Help

### Before Asking for Help

Gather this information:

1. **What you're trying to do:**
```
"I want my skill to activate when I ask about React"
```

2. **What's happening:**
```
"Skill never activates, Claude asks me to clarify instead"
```

3. **Configuration:**
```yaml
# Share your skill/command/hook config
```

4. **Steps to reproduce:**
```
1. Created skill in .claude/skills/react-helper.md
2. Started claude
3. Asked "create a React component"
4. Skill didn't activate
```

5. **Environment:**
```
- Claude Code version: 1.2.3
- OS: macOS 13.0
- Project type: Node.js/React
```

### Where to Ask

1. **GitHub Issues** - Bug reports
2. **GitHub Discussions** - How-to questions
3. **Discord/Community** - Quick help

---

## Quick Fixes

### Restart Claude Code
```bash
exit
claude
# Fixes: Command not found, stale config
```

### Clear conversation
```bash
/clear
# Fixes: Context overload, confusion
```

### Verify file syntax
```bash
# Check YAML
cat .claude/skills/skill.md | head -n 10

# Check JSON
cat .claude/settings.json | jq .
```

### Check file locations
```bash
tree .claude/
# Verify all files in correct locations
```

### Test components individually
```bash
# Test hook command
bash -c "command here"

# Test MCP server
npx @modelcontextprotocol/server-github

# Test skill instructions manually
```

---

## Preventive Measures

### Before adding configuration

- [ ] Test commands separately
- [ ] Validate JSON/YAML syntax
- [ ] Check file locations
- [ ] Test with simple examples
- [ ] Document what it does

### Regular maintenance

- [ ] Review unused skills/commands
- [ ] Update descriptions that don't work
- [ ] Test hooks still function
- [ ] Check MCP servers connect
- [ ] Clean up old configurations

---

## Summary

**Most common issues:**

1. **Skills don't activate** → Make description more specific
2. **Commands not found** → Check filename and location
3. **Hooks don't run** → Validate JSON syntax
4. **Subagents unavailable** → Verify YAML frontmatter
5. **MCP won't connect** → Check credentials and network

**Always:**
- Test individually before combining
- Use debug mode when stuck
- Check syntax with validators
- Read error messages carefully
- Ask for help with details

**When in doubt, restart Claude Code!**
