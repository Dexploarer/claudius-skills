# Claude Code Starter Kit - The Complete Guide

Welcome! This repository contains a complete, beginner-to-moderate friendly setup for Claude Code's **Five Pillars of Extensibility**. Think of this as your starter pack for supercharging your AI coding assistant.

## What's Inside?

This starter kit includes:

- **5 Skills** - Automatic, context-aware capabilities
- **12 Slash Commands** - Quick shortcuts for common tasks
- **Hooks Configuration** - Automatic safety checks and logging
- **4 Subagents** - Expert specialists for different tasks
- **MCP Template** - Ready to connect external services

Everything is pre-configured, documented, and ready to use!

---

## Quick Start

### 1. Clone or Copy This Repository

```bash
# If you're starting a new project
git clone <this-repo-url>
cd claudius-skills

# OR just copy the .claude folder to your existing project
cp -r .claude /path/to/your/project/
```

### 2. Start Using It!

```bash
cd your-project
claude
```

That's it! Claude Code will automatically detect and load all the skills, commands, hooks, and subagents.

### 3. Try It Out

```bash
# Try a slash command
/explain console.log("Hello, world!")

# Claude will automatically use skills when appropriate
# Just work naturally and the skills activate when needed

# Try a subagent
"Use the code-reviewer subagent to review my recent changes"
```

---

## What Are The Five Pillars?

Think of the Five Pillars as different ways to customize and extend Claude Code:

| Pillar | What It Does | When To Use | How It Works |
|--------|--------------|-------------|--------------|
| **Skills** | Teach Claude specialized knowledge | For reusable capabilities you use often | Claude decides when to use them automatically |
| **Slash Commands** | Quick shortcuts for tasks | For tasks you do repeatedly | You type `/command` to trigger |
| **Hooks** | Automatic actions on events | For enforcing rules and logging | Runs automatically on events |
| **Subagents** | Expert consultants | For specialized analysis/work | Claude or you can call them in |
| **MCP Servers** | Connect to external tools | For accessing outside services | Bridge to external APIs/data |

---

## The Skills (Automatic Helpers)

Skills are like teaching Claude specialized knowledge that it uses automatically when appropriate.

### Included Skills:

1. **readme-generator** - Creates professional README files
2. **code-explainer** - Explains code in simple, beginner-friendly terms
3. **bug-finder** - Identifies common bugs and potential issues
4. **test-helper** - Helps write comprehensive tests
5. **git-helper** - Assists with git operations and workflows

### How Skills Work:

You don't call skills explicitly - Claude recognizes when they're needed:

```bash
# You say:
"I need a README for this project"

# Claude thinks:
"This matches the readme-generator skill's description"

# Claude automatically uses the skill to generate a great README
```

### Creating Your Own Skills:

```bash
# Create a new skill file
touch .claude/skills/my-skill.md
```

```markdown
---
name: my-skill
description: Clear description of what this does and when to use it
---

# Your skill instructions here

When doing X, follow these steps:
1. Step one
2. Step two
...
```

**Pro tip:** The `description` field is crucial - it tells Claude when to activate the skill!

---

## The Slash Commands (Quick Shortcuts)

Slash commands are manual shortcuts. You type `/command` and Claude runs that task.

### Included Commands:

| Command | What It Does |
|---------|--------------|
| `/explain [code]` | Explains code in simple terms |
| `/test` | Runs all tests and summarizes results |
| `/commit` | Creates a professional commit message |
| `/review` | Reviews your uncommitted changes |
| `/clean` | Cleans up current file (removes unused imports, fixes formatting) |
| `/todo` | Finds all TODO/FIXME comments in codebase |
| `/setup` | Sets up a new project with best practices |
| `/debug [issue]` | Helps debug a specific issue |
| `/refactor [code]` | Refactors code for better quality |
| `/docs [item]` | Generates documentation |
| `/deps` | Analyzes project dependencies |
| `/quickfix` | Quickly fixes common issues |

### How To Use:

```bash
# In Claude Code, just type the command:
/explain const user = { name: "Alice", age: 30 };

# Or with arguments:
/debug login button doesn't work
```

### Creating Your Own Commands:

```bash
# Create a new command file
touch .claude/commands/mycommand.md
```

```markdown
Do something specific with: $ARGUMENTS

Step 1: ...
Step 2: ...
```

Now you can use `/mycommand whatever` and Claude will run those instructions.

---

## The Hooks (Automatic Watchdogs)

Hooks are like security cameras - they watch for specific events and automatically do something.

### Included Hooks:

1. **Session Start** - Welcome message when you start Claude Code
2. **Secret Detection** - Warns before committing passwords/API keys
3. **Force Push Warning** - Confirms before force pushing to git
4. **File Modification Log** - Logs when files are modified
5. **Session End** - Goodbye message when you exit

### How Hooks Work:

```bash
# You run:
git commit -m "Add new feature"

# Hook automatically runs BEFORE commit:
# Checks for secrets in the code
# If found, blocks the commit with warning
# If safe, allows commit to proceed
```

### Hooks Configuration:

Hooks are configured in `.claude/settings.json`. Each hook has:
- **Event**: When to trigger (SessionStart, PreToolUse, etc.)
- **Pattern**: What to watch for (optional)
- **Command**: What bash command to run
- **Description**: What this hook does

### Example Hook:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "pattern": "Bash.*git commit",
        "command": "echo 'Checking for secrets...' && git diff --cached | grep -i 'password'",
        "description": "Check for passwords before committing"
      }
    ]
  }
}
```

**Safety Note:** Hooks run bash commands automatically. Only add hooks you understand and trust!

---

## The Subagents (Expert Consultants)

Subagents are specialized versions of Claude with specific expertise and their own context window.

### Included Subagents:

1. **code-reviewer** - Thorough code review expert (read-only)
2. **test-writer** - Testing specialist who writes comprehensive tests
3. **doc-writer** - Technical documentation expert
4. **debug-helper** - Debugging specialist

### Why Use Subagents?

**Separate Context:** Each subagent has its own "memory" that doesn't clutter your main conversation.

**Specialized Expertise:** Each subagent is pre-configured with specific instructions for their domain.

**Tool Restrictions:** Some subagents are read-only (like code-reviewer) for safety.

### How To Use Subagents:

```bash
# Automatic (Claude decides):
"Review my code for bugs and security issues"
# Claude may automatically use the code-reviewer subagent

# Explicit (you choose):
"Use the test-writer subagent to write tests for the UserController"

# Via interface:
/agents
# Opens interface to create/manage subagents
```

### Creating Your Own Subagents:

```bash
touch .claude/agents/my-expert.md
```

```markdown
---
name: my-expert
description: What this expert does
allowed-tools: [Read, Grep, Glob]  # Optional: restrict tools
---

You are an expert in [domain].

When working on [tasks]:
1. Do this
2. Then that
3. Always check for...
```

---

## MCP Servers (External Connections)

MCP servers connect Claude to external services like GitHub, databases, Slack, etc.

### Setting Up MCP:

1. **Copy the template:**
   ```bash
   cp .mcp.json.template .mcp.json
   ```

2. **Enable a server:**
   ```json
   {
     "mcpServers": {
       "github": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-github"],
         "env": {
           "GITHUB_TOKEN": "your-actual-token-here"
         },
         "disabled": false  // Change to false
       }
     }
   }
   ```

3. **Add your credentials:**
   - Replace `"your-actual-token-here"` with real credentials
   - **NEVER commit `.mcp.json` to git!** (it's in .gitignore)

4. **Use it:**
   ```bash
   # Claude can now access GitHub!
   "Check for high-priority issues in my repo"
   "Create a GitHub issue for the bug I just found"
   ```

### Popular MCP Servers:

- **GitHub** - Issues, PRs, repos
- **PostgreSQL/SQLite** - Database queries
- **Slack** - Messages, channels
- **Google Drive** - Files, folders
- **Filesystem** - Local file access
- **Memory** - Persistent notes

### Installing MCP Servers:

```bash
# Easy way:
claude mcp add github

# Or manually add to .mcp.json
```

**Security Warning:** MCP servers have access to your external services. Only use trusted servers and use read-only credentials when possible!

---

## Directory Structure

```
your-project/
├── .claude/
│   ├── skills/              # Skills (automatic)
│   │   ├── readme-generator.md
│   │   ├── code-explainer.md
│   │   ├── bug-finder.md
│   │   ├── test-helper.md
│   │   └── git-helper.md
│   │
│   ├── commands/            # Slash commands (manual)
│   │   ├── explain.md
│   │   ├── test.md
│   │   ├── commit.md
│   │   ├── review.md
│   │   ├── clean.md
│   │   ├── todo.md
│   │   ├── setup.md
│   │   ├── debug.md
│   │   ├── refactor.md
│   │   ├── docs.md
│   │   ├── deps.md
│   │   └── quickfix.md
│   │
│   ├── agents/              # Subagents (specialists)
│   │   ├── code-reviewer.md
│   │   ├── test-writer.md
│   │   ├── doc-writer.md
│   │   └── debug-helper.md
│   │
│   └── settings.json        # Hooks configuration
│
├── .mcp.json.template       # MCP server template
├── .mcp.json               # Your MCP config (gitignored)
├── .gitignore              # Protects sensitive files
└── README.md               # This file!
```

---

## Common Use Cases

### "I want to understand some code"

```bash
# Use the slash command:
/explain [paste code here]

# Or just ask naturally:
"Explain this function to me in simple terms"
# The code-explainer skill activates automatically
```

### "I want to write tests"

```bash
# Explicit subagent call:
"Use the test-writer subagent to write tests for my UserController class"

# Or just ask:
"Write tests for this function"
# The test-helper skill may activate
```

### "I want to review my code before committing"

```bash
# Use the slash command:
/review

# This will check for bugs, security issues, code quality, etc.
```

### "I want to commit my changes"

```bash
# Use the slash command:
/commit

# Claude will:
# 1. Review your changes
# 2. Write a professional commit message
# 3. Show it to you for approval
# 4. Commit (if you approve)

# Plus, hooks automatically check for secrets before committing!
```

### "I need to debug something"

```bash
# Use the slash command:
/debug login button doesn't work

# Or call the subagent explicitly:
"Use the debug-helper subagent to help me figure out this error"
```

### "I need a README for my project"

```bash
# Just ask:
"Create a README for this project"

# The readme-generator skill activates automatically
```

---

## Customization Guide

### For Beginners

Start by just using what's provided:
1. Use the slash commands
2. Work naturally and let skills activate
3. Observe what happens
4. Gradually learn how each piece works

### For Intermediate Users

Start customizing:
1. Modify existing skills/commands to fit your workflow
2. Add your own simple commands
3. Adjust hooks for your team's practices
4. Create a subagent for your specific domain

### For Advanced Users

Go all out:
1. Create comprehensive skills for your tech stack
2. Build complex hooks for automation
3. Set up multiple specialized subagents
4. Connect MCP servers for your tools
5. Share your setup with your team via git

---

## Team Usage

### Sharing With Your Team

This entire setup is designed to be shared via git:

```bash
# Everything in .claude/ is team-shared
git add .claude/
git commit -m "Add Claude Code configuration"
git push

# Teammates pull and get everything automatically!
git pull
# Their Claude Code now has all your skills, commands, and subagents
```

### Personal Customizations

For personal tweaks that shouldn't be shared:

```bash
# Put personal stuff in:
~/.claude/skills/         # Personal skills (all projects)
~/.claude/commands/       # Personal commands (all projects)
~/.claude/agents/         # Personal subagents (all projects)
~/.claude/settings.json   # Personal settings (all projects)

# Or use local settings in project:
.claude/settings.local.json  # Personal project settings (gitignored)
```

---

## Troubleshooting

### "Skills aren't activating"

1. Check the skill's `description` field - is it clear and specific?
2. Try asking in a way that matches the description
3. Check for syntax errors in the SKILL.md file

### "Slash command not found"

1. Make sure the file is in `.claude/commands/`
2. File name should be `commandname.md`
3. Use it as `/commandname`
4. Restart Claude Code if needed

### "Hooks not running"

1. Check `.claude/settings.json` for syntax errors
2. Make sure the hook pattern matches the tool use
3. Test the bash command separately to ensure it works
4. Check exit codes (0 = success, 2 = block, other = warning)

### "Subagent not available"

1. Check that the `.md` file is in `.claude/agents/`
2. Verify the YAML frontmatter is correct
3. Try calling it explicitly: "Use the [name] subagent to..."
4. Check `/agents` to see all available subagents

### "MCP server not working"

1. Make sure `.mcp.json` exists (copied from template)
2. Check that `"disabled": false`
3. Verify credentials are correct
4. Check that the server package is accessible
5. Look for errors with `claude --debug`

---

## Best Practices

### Do's ✅

- ✅ Start simple, add complexity as needed
- ✅ Write clear descriptions for skills
- ✅ Test commands before sharing with team
- ✅ Document any custom hooks
- ✅ Use meaningful names for everything
- ✅ Keep skills focused on one thing
- ✅ Share useful configurations with your team
- ✅ Review hooks for security before running them

### Don'ts ❌

- ❌ Don't commit `.mcp.json` with real credentials
- ❌ Don't create overly complex skills
- ❌ Don't use hooks for tasks that should be manual
- ❌ Don't trust hooks/MCP servers from unknown sources
- ❌ Don't make skills/commands too generic
- ❌ Don't skip testing your configurations

---

## Learning Resources

### Understanding Each Pillar

1. **Skills** - Read the included skills to see how they work
2. **Slash Commands** - Check `.claude/commands/` for examples
3. **Hooks** - Review `.claude/settings.json` to see hook patterns
4. **Subagents** - Look at `.claude/agents/` for specialist examples
5. **MCP** - Check `.mcp.json.template` for server examples

### Experimentation Ideas

- Create a skill for your favorite framework
- Make a slash command for your most repeated task
- Add a hook to enforce your team's code standards
- Build a subagent expert in your domain
- Connect an MCP server to your tools

---

## What's Next?

### Immediate Next Steps

1. ✅ Clone/copy this repo to your project
2. ✅ Try the slash commands
3. ✅ Watch skills activate automatically
4. ✅ Experiment with calling subagents
5. ✅ Optionally set up MCP servers

### Going Further

- Customize existing skills for your needs
- Create commands for your specific workflow
- Add hooks that make sense for your team
- Build subagents for your tech stack
- Connect to your external tools via MCP

### Share Your Experience

This is a learning tool! As you use it:
- Note what works well
- Identify what could be better
- Create your own configurations
- Share improvements with others

---

## FAQ

**Q: Do I need to use all five pillars?**
A: No! Use what makes sense for you. Start with slash commands (easiest) and skills (most useful), then explore the others.

**Q: Can I use this with existing projects?**
A: Yes! Just copy the `.claude/` folder to your project.

**Q: Will this work with my team?**
A: Yes! Everything in `.claude/` is designed to be shared via git.

**Q: Is this safe?**
A: The included configurations are safe, but be careful with:
- Custom hooks (they run bash commands)
- MCP servers (they access external services)
- Hooks/servers from unknown sources

**Q: What if something breaks?**
A: You can always remove/disable parts:
- Delete a skill: remove the file
- Disable a command: delete or rename the file
- Turn off hooks: edit settings.json
- Disable MCP: set `"disabled": true`

**Q: Can I see examples of each pillar in action?**
A: Yes! Just use Claude Code naturally. The skills will activate automatically, you can try the slash commands, and hooks will trigger on their events.

---

## Contributing

Found a bug? Have an improvement? Created a cool skill or command?

Feel free to:
- Open an issue
- Submit a pull request
- Share your configurations
- Help improve the documentation

---

## License

This starter kit is provided as-is for educational and practical use. Use, modify, and share as you see fit!

---

## Final Thoughts

The Five Pillars give you incredible power to customize Claude Code:

- **Skills** teach Claude domain knowledge
- **Slash Commands** give you instant shortcuts
- **Hooks** enforce rules automatically
- **Subagents** bring in specialists
- **MCP Servers** connect to the world

Start simple, experiment, and build your perfect development environment!

**Happy coding with Claude! 🚀**
