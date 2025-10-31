# Quick Reference Guide

## Slash Commands (Type these in Claude Code)

| Command | Usage |
|---------|-------|
| `/explain` | `/explain [code]` - Explains code simply |
| `/test` | `/test` - Runs all tests |
| `/commit` | `/commit` - Creates professional commit |
| `/review` | `/review` - Reviews uncommitted changes |
| `/clean` | `/clean` - Cleans up current file |
| `/todo` | `/todo` - Finds TODO/FIXME comments |
| `/setup` | `/setup` - Sets up new project |
| `/debug` | `/debug [issue]` - Helps debug issue |
| `/refactor` | `/refactor [code]` - Refactors code |
| `/docs` | `/docs [item]` - Generates documentation |
| `/deps` | `/deps` - Analyzes dependencies |
| `/quickfix` | `/quickfix` - Fixes common issues |

## Skills (Activate Automatically)

| Skill | Triggers When You... |
|-------|---------------------|
| **readme-generator** | Ask for a README or project documentation |
| **code-explainer** | Ask "what does this do" or "explain this code" |
| **bug-finder** | Ask to find bugs or debug code |
| **test-helper** | Ask for help writing tests |
| **git-helper** | Ask about git operations or workflows |

## Subagents (Call Explicitly or Auto-Used)

| Subagent | What They Do |
|----------|-------------|
| **code-reviewer** | Thorough code reviews (read-only) |
| **test-writer** | Writes comprehensive test suites |
| **doc-writer** | Creates professional documentation |
| **debug-helper** | Systematic debugging assistance |

### How to Use Subagents:

```bash
# Automatic:
"Review my code for security issues"

# Explicit:
"Use the test-writer subagent to write tests for UserController"

# Manage:
/agents
```

## Hooks (Run Automatically)

| Hook | When It Runs | What It Does |
|------|-------------|--------------|
| Session Start | Claude Code starts | Shows welcome message |
| Secret Detection | Before git commit | Checks for passwords/API keys |
| Force Push Warning | Before git push -f | Requires confirmation |
| File Modification | After file edit | Logs the change |
| Session End | Claude Code exits | Shows goodbye message |

## Common Workflows

### Code Review Before Commit
```bash
/review                 # Review changes
/commit                # Create commit with good message
                       # Hooks automatically check for secrets
```

### Debugging a Problem
```bash
/debug login not working
# Or:
"Use the debug-helper subagent to help with this error"
```

### Writing Tests
```bash
"Use the test-writer subagent to write tests for my Calculator class"
/test                  # Run the tests
```

### Understanding Code
```bash
/explain [paste code]
# Or just:
"Explain how this function works"
```

### Setting Up New Project
```bash
/setup
# Follow the prompts
```

### Finding Issues
```bash
/todo                  # Find all TODO comments
/review                # Review code quality
/deps                  # Check dependencies
```

## Customization

### Add Your Own Slash Command
```bash
# Create file:
.claude/commands/mycommand.md

# Content:
Do [task] with: $ARGUMENTS
```

### Add Your Own Skill
```bash
# Create file:
.claude/skills/my-skill.md

# Content:
---
name: my-skill
description: When to use this skill
---
Instructions here...
```

### Add Your Own Subagent
```bash
# Create file:
.claude/agents/my-expert.md

# Content:
---
name: my-expert
description: What this expert does
allowed-tools: [Read, Grep, Glob]
---
You are an expert in...
```

### Add Your Own Hook
Edit `.claude/settings.json`:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "pattern": "Edit",
        "command": "echo 'About to edit file'",
        "description": "Log before editing"
      }
    ]
  }
}
```

## MCP Servers

### Enable MCP Server
```bash
# Copy template
cp .mcp.json.template .mcp.json

# Edit .mcp.json:
# 1. Set "disabled": false
# 2. Add your credentials
# 3. Save (DO NOT commit to git!)
```

### Use MCP Server
```bash
# Example with GitHub MCP:
"Check for issues in my repository"
"Create a GitHub issue for this bug"
```

## Tips

- Skills activate automatically - just work naturally
- Use `/` to trigger slash commands
- Subagents keep separate context (cleaner conversations)
- Hooks enforce rules automatically
- MCP connects to external services

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Skill not activating | Check description is specific and matches your request |
| Command not found | Ensure file is in `.claude/commands/` |
| Hook not running | Check syntax in `.claude/settings.json` |
| Subagent unavailable | Verify file in `.claude/agents/` with correct YAML |
| MCP not working | Check `.mcp.json` exists with `disabled: false` |

## Need Help?

- Read `README.md` for full documentation
- Check individual files in `.claude/` for examples
- Experiment and learn by doing!
