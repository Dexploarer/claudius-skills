# Getting Started with Claude Code

A complete beginner's guide to using Claude Code and its Five Pillars of Extensibility.

## What is Claude Code?

Claude Code is an AI-powered coding assistant that runs in your terminal. It can:
- Read and write code
- Run commands
- Analyze your codebase
- Help debug issues
- Write tests
- Create documentation
- And much more!

What makes it special is its **extensibility** - you can customize it with Skills, Commands, Hooks, Subagents, and MCP servers.

---

## Installation

### Prerequisites

- macOS, Linux, or Windows with WSL
- A Claude.ai or Claude Console account
- Terminal access

### Install Claude Code

**macOS (Homebrew):**
```bash
brew install claude
```

**Linux/macOS (curl):**
```bash
curl -fsSL https://claude.ai/install.sh | sh
```

**Windows (PowerShell):**
```powershell
irm https://claude.ai/install.ps1 | iex
```

### Verify Installation

```bash
claude --version
```

---

## First Steps

### 1. Start Claude Code

```bash
# Navigate to any project directory
cd ~/my-project

# Start Claude Code
claude
```

You'll see a welcome screen with session information.

### 2. Try Your First Command

```bash
# Ask Claude to explain a file
"Explain what this package.json file does"

# Ask for help with code
"How do I read a JSON file in Node.js?"

# Get code written
"Write a function to calculate factorial"
```

### 3. See Available Commands

```bash
/help
```

This shows all built-in slash commands.

---

## Understanding the Five Pillars

Claude Code has five ways to extend and customize it:

### 1. 🎯 Skills (Automatic)

**What:** Specialized knowledge that activates automatically
**When to use:** For capabilities you use frequently
**How it works:** You describe when to use it, Claude decides when to activate

**Example:**
```yaml
---
name: readme-generator
description: Generate README files when user asks for project documentation
---
[Instructions on how to create READMEs]
```

When you say "I need a README", this skill automatically activates!

### 2. ⚡ Slash Commands (Manual)

**What:** Quick shortcuts you trigger explicitly
**When to use:** For tasks you do repeatedly
**How it works:** Type `/command` to run

**Example:**
```markdown
# File: .claude/commands/test.md
Run all tests and summarize the results
```

Usage: `/test`

### 3. 🔗 Hooks (Event-Driven)

**What:** Automatic actions that run on specific events
**When to use:** For enforcing rules and automating workflows
**How it works:** Triggers on events like file edits, commits, etc.

**Example:**
```json
{
  "hooks": {
    "PreToolUse": [{
      "pattern": "Bash.*git commit",
      "command": "echo 'Checking for secrets...'",
      "description": "Security check before commit"
    }]
  }
}
```

### 4. 👥 Subagents (Specialists)

**What:** Pre-configured AI experts with separate context
**When to use:** For specialized analysis that keeps main chat clean
**How it works:** Call them in or Claude chooses them automatically

**Example:**
```yaml
---
name: code-reviewer
description: Expert code reviewer
allowed-tools: [Read, Grep, Glob]
---
You are a senior engineer who reviews code...
```

Usage: "Use the code-reviewer subagent to check my code"

### 5. 🌐 MCP Servers (External)

**What:** Connections to external services
**When to use:** For integrating with tools like GitHub, databases, Slack
**How it works:** Install and configure MCP servers

**Example:**
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your-token"
      }
    }
  }
}
```

---

## Your First Customization: Installing the Starter Kit

The easiest way to get started is with our starter kit!

### Step 1: Clone This Repository

```bash
git clone <repo-url>
cd claudius-skills
```

### Step 2: Copy the Starter Kit

```bash
# Copy to your project
cp -r starter-kit/.claude ~/my-project/

# Or try it directly in the starter-kit
cd starter-kit
claude
```

### Step 3: Try It Out!

```bash
# Try a slash command
/explain console.log("Hello")

# Ask for code review
/review

# Let skills activate automatically
"I need a README for this project"
```

---

## File Structure

When you use Claude Code customizations, your project looks like this:

```
your-project/
├── .claude/
│   ├── skills/           # Skills (automatic)
│   │   └── skill-name.md
│   ├── commands/         # Slash commands (manual)
│   │   └── command.md
│   ├── agents/           # Subagents (specialists)
│   │   └── agent-name.md
│   └── settings.json     # Hooks configuration
│
├── .mcp.json            # MCP server configuration (gitignored)
└── [your code files]
```

---

## Daily Workflow

Here's a typical workflow with Claude Code:

### Morning: Start Work

```bash
cd my-project
claude

# Claude (hook): "Good morning! Session started."
```

### During Development

```bash
# Write code with Claude's help
"Create a User model with name, email, and password fields"

# Skill automatically activates to follow your framework patterns
```

### Before Committing

```bash
# Review your changes
/review

# Subagent: code-reviewer automatically checks for issues
# Hook: Checks for secrets before commit

# Create commit
/commit

# Claude writes professional commit message
```

### Debugging

```bash
# When you hit an error
/debug login function throwing 401 error

# Subagent: debug-helper systematically helps you find the issue
```

### End of Day

```bash
# Exit Claude Code
exit

# Hook: "Session ended at 5:30 PM"
```

---

## Common Tasks

### Task: Explain Code

**Without customization:**
```bash
"Explain what this function does: [paste code]"
```

**With starter kit:**
```bash
/explain [paste code]
# code-explainer skill activates automatically
```

### Task: Write Tests

**Without customization:**
```bash
"Write tests for my calculateTotal function"
```

**With starter kit:**
```bash
"Use the test-writer subagent to write comprehensive tests for calculateTotal"
# Gets detailed, well-structured tests
```

### Task: Create Documentation

**Without customization:**
```bash
"Generate JSDoc comments for this function"
```

**With starter kit:**
```bash
/docs calculateTotal
# Or just: "I need documentation"
# readme-generator or doc-writer activates
```

---

## Configuration Files Explained

### Skills (.claude/skills/*.md)

```yaml
---
name: my-skill              # Unique identifier
description: What it does   # IMPORTANT: When to activate
allowed-tools: [Read]       # Optional: Restrict tools
---

# Instructions for Claude
[Detailed steps on what to do]
```

### Commands (.claude/commands/*.md)

```markdown
Instructions for what to do with: $ARGUMENTS

1. Step one
2. Step two
```

### Subagents (.claude/agents/*.md)

```yaml
---
name: my-agent
description: What this agent specializes in
allowed-tools: [Read, Grep]  # Often read-only for safety
---

You are an expert in [domain].
When you work on tasks, you...
```

### Hooks (.claude/settings.json)

```json
{
  "hooks": {
    "EventName": [{
      "pattern": "optional-pattern",
      "command": "bash command to run",
      "timeout": 5000,
      "description": "What this hook does"
    }]
  }
}
```

### MCP (.mcp.json)

```json
{
  "mcpServers": {
    "server-name": {
      "command": "how-to-start-server",
      "args": ["arguments"],
      "env": {
        "API_KEY": "credentials-here"
      }
    }
  }
}
```

**Important:** Never commit `.mcp.json` with real credentials!

---

## Tips for Beginners

### Start Simple

1. ✅ Use the starter kit as-is first
2. ✅ Learn what each component does
3. ✅ Then customize for your needs

### Don't Over-Customize

1. ❌ Don't create 50 skills on day one
2. ✅ Start with 2-3 most useful ones
3. ✅ Add more as you need them

### Understand Before Extending

1. ✅ Read the existing skills/commands
2. ✅ See how they're structured
3. ✅ Copy patterns that work

### Test Everything

1. ✅ Test skills with different phrasings
2. ✅ Verify commands work as expected
3. ✅ Check hooks don't break your workflow

---

## Troubleshooting

### Problem: Claude Code won't start

**Solution:**
```bash
# Check installation
claude --version

# Try updating
brew upgrade claude  # macOS
# Or reinstall with install script
```

### Problem: Skill isn't activating

**Solution:**
1. Check the `description` field - is it specific enough?
2. Try asking in different ways
3. Verify file is in `.claude/skills/`
4. Check for YAML syntax errors

### Problem: Command not found

**Solution:**
1. Ensure file is in `.claude/commands/`
2. File should be named `commandname.md`
3. Use as `/commandname`
4. Restart Claude Code

### Problem: Hook not running

**Solution:**
1. Check `.claude/settings.json` for syntax errors
2. Verify the event name is correct
3. Test the bash command separately
4. Check the pattern matches your use case

---

## Next Steps

### Level 1: Complete Beginner

1. ✅ Install Claude Code
2. ✅ Use it for basic tasks
3. ✅ Install the starter kit
4. ✅ Try the slash commands
5. ✅ Watch skills activate

**Time:** 1-2 days

### Level 2: Beginner

1. ✅ Understand all five pillars
2. ✅ Modify an existing skill
3. ✅ Create a simple command
4. ✅ Understand hooks
5. ✅ Call a subagent explicitly

**Time:** 1 week

### Level 3: Intermediate

1. ✅ Create your own skill from scratch
2. ✅ Build workflow commands
3. ✅ Add hooks for your needs
4. ✅ Create a specialized subagent
5. ✅ Set up an MCP server

**Time:** 2-4 weeks

### Level 4: Advanced

1. ✅ Build complex multi-file skills
2. ✅ Create sophisticated hook systems
3. ✅ Design subagent architectures
4. ✅ Integrate multiple MCP servers
5. ✅ Share configs with your team

**Time:** 1-3 months

---

## Learning Resources

### In This Repository

- **Starter Kit** - Complete working example
- **Templates** - Copy and customize
- **Examples** - See different patterns
- **Tutorials** - Step-by-step guides

### Official Documentation

- [Claude Code Docs](https://docs.claude.com/en/docs/claude-code/)
- [MCP Documentation](https://modelcontextprotocol.io/)

### Community

- GitHub Issues - Ask questions
- GitHub Discussions - Share ideas
- Pull Requests - Contribute

---

## Best Practices from Day One

### For Skills

- ✅ Write very specific descriptions
- ✅ Include examples in the skill file
- ✅ Keep them focused on one thing
- ✅ Test with different phrasings

### For Commands

- ✅ Use clear, memorable names
- ✅ Keep them simple and focused
- ✅ Document what arguments do
- ✅ Think about what you do every day

### For Hooks

- ✅ Start with non-blocking hooks (exit code 0)
- ✅ Test commands separately first
- ✅ Add descriptions for team members
- ✅ Be careful with automatic actions

### For Subagents

- ✅ Give them clear expertise boundaries
- ✅ Use read-only tools when possible
- ✅ Provide structured output formats
- ✅ Test them before sharing

### For Security

- ✅ Never commit `.mcp.json` with credentials
- ✅ Review hooks before running them
- ✅ Use read-only MCP when possible
- ✅ Keep `.claude/settings.local.json` gitignored

---

## Quick Command Reference

### Built-in Commands

```bash
/help          # Show help
/clear         # Clear conversation
/model         # Change AI model
/cost          # Show token usage
/agents        # Manage subagents
```

### Starter Kit Commands

```bash
/explain       # Explain code simply
/test          # Run all tests
/commit        # Create commit
/review        # Review changes
/clean         # Clean up code
/todo          # Find TODO comments
/setup         # Setup new project
/debug         # Debug issues
/refactor      # Refactor code
/docs          # Generate docs
/deps          # Check dependencies
/quickfix      # Quick fixes
```

---

## Keyboard Shortcuts

- `Ctrl+C` - Stop current operation
- `Ctrl+D` - Exit Claude Code
- `Up/Down` - Navigate command history

---

## Getting Help

### When You're Stuck

1. **Read the docs** - Check starter-kit/README.md
2. **Check examples** - See how others do it
3. **Ask Claude** - "How do I create a skill?"
4. **Search issues** - Someone may have asked before
5. **Ask the community** - Create a GitHub issue

### When You Find a Bug

1. Check if it's already reported
2. Create a GitHub issue with:
   - What you were trying to do
   - What happened instead
   - Steps to reproduce
   - Your Claude Code version

### When You Want to Contribute

1. Read CONTRIBUTING.md
2. Look for "good first issue" labels
3. Ask if help is needed
4. Submit PRs with clear descriptions

---

## Summary

**Claude Code is powerful because it's customizable.**

The Five Pillars let you:
- **Skills** - Teach Claude your workflows
- **Commands** - Create shortcuts for common tasks
- **Hooks** - Automate and enforce rules
- **Subagents** - Get specialized help
- **MCP** - Connect to external tools

**Start with the starter kit, learn by doing, and customize as you go!**

---

**Welcome to Claude Code! Happy coding! 🚀**
