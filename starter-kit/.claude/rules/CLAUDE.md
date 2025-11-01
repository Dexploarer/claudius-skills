# Starter Kit - Beginner Level Rules

> **Level 1: Beginner-Friendly Claude Code Configuration**
> Perfect for learning AI-assisted development and building simple projects.

---

## 🎯 Purpose

The Starter Kit provides a **beginner-friendly foundation** for Claude Code, including:
- 5 essential skills for common tasks
- 12 slash commands for quick workflows
- 4 helper subagents for specialized tasks
- Safety hooks for secure development

**Target Audience:** New to Claude Code, learning AI-assisted development

---

## 📚 Available Capabilities

### Skills (5 Total)
All skills located in: `starter-kit/.claude/skills/`

1. **readme-generator** - Creates professional README files
   - Auto-invoked when: "create readme", "generate documentation"
   - Reference: `@starter-kit/.claude/skills/readme-generator.md`

2. **code-explainer** - Explains code in beginner-friendly terms
   - Auto-invoked when: "explain this code", "what does this do"
   - Reference: `@starter-kit/.claude/skills/code-explainer.md`

3. **bug-finder** - Identifies common bugs and potential issues
   - Auto-invoked when: "find bugs", "check for errors"
   - Reference: `@starter-kit/.claude/skills/bug-finder.md`

4. **test-helper** - Helps write comprehensive tests
   - Auto-invoked when: "write tests", "add test coverage"
   - Reference: `@starter-kit/.claude/skills/test-helper.md`

5. **git-helper** - Assists with git operations and workflows
   - Auto-invoked when: "help with git", "create commit"
   - Reference: `@starter-kit/.claude/skills/git-helper.md`

### Slash Commands (12 Total)
All commands located in: `starter-kit/.claude/commands/`

**Development Commands:**
- `/commit` - Git commit helper
  - Usage: `/commit` → Stages changes and creates commit
  - Reference: `@starter-kit/.claude/commands/commit.md`

- `/debug` - Debug code issues
  - Usage: `/debug` → Analyzes and fixes bugs
  - Reference: `@starter-kit/.claude/commands/debug.md`

- `/explain` - Explain code
  - Usage: `/explain` → Provides detailed code explanations
  - Reference: `@starter-kit/.claude/commands/explain.md`

- `/quickfix` - Quick code fixes
  - Usage: `/quickfix` → Applies fast fixes to common issues
  - Reference: `@starter-kit/.claude/commands/quickfix.md`

- `/refactor` - Refactor code
  - Usage: `/refactor` → Improves code structure
  - Reference: `@starter-kit/.claude/commands/refactor.md`

- `/review` - Code review
  - Usage: `/review` → Comprehensive code review
  - Reference: `@starter-kit/.claude/commands/review.md`

**Documentation Commands:**
- `/docs` - Generate documentation
  - Usage: `/docs` → Creates comprehensive docs
  - Reference: `@starter-kit/.claude/commands/docs.md`

**Testing Commands:**
- `/test` - Run tests
  - Usage: `/test` → Executes test suite
  - Reference: `@starter-kit/.claude/commands/test.md`

**Project Management:**
- `/setup` - Project setup
  - Usage: `/setup` → Initializes project structure
  - Reference: `@starter-kit/.claude/commands/setup.md`

- `/todo` - Find TODO comments
  - Usage: `/todo` → Lists all TODO items
  - Reference: `@starter-kit/.claude/commands/todo.md`

- `/clean` - Clean project
  - Usage: `/clean` → Removes build artifacts
  - Reference: `@starter-kit/.claude/commands/clean.md`

- `/deps` - Manage dependencies
  - Usage: `/deps` → Analyzes and updates dependencies
  - Reference: `@starter-kit/.claude/commands/deps.md`

### Subagents (4 Total)
All agents located in: `starter-kit/.claude/agents/`

1. **code-reviewer** - Comprehensive code review specialist
   - Invocation: "Use code-reviewer subagent to review this"
   - Capabilities: Read, Grep, Glob
   - Reference: `@starter-kit/.claude/agents/code-reviewer.md`

2. **test-writer** - Test generation expert
   - Invocation: "Use test-writer subagent to create tests"
   - Capabilities: Read, Write, Grep
   - Reference: `@starter-kit/.claude/agents/test-writer.md`

3. **doc-writer** - Documentation specialist
   - Invocation: "Use doc-writer subagent to document this"
   - Capabilities: Read, Write, Grep
   - Reference: `@starter-kit/.claude/agents/doc-writer.md`

4. **debug-helper** - Debugging assistant
   - Invocation: "Use debug-helper subagent to find the issue"
   - Capabilities: Read, Grep, Bash
   - Reference: `@starter-kit/.claude/agents/debug-helper.md`

### Hooks (Event-Driven Safety)
Configuration: `starter-kit/.claude/settings.json`

**SessionStart Hooks:**
- Welcome message with timestamp
- Session initialization

**PreToolUse Hooks (Safety First):**
- ✅ Secret detection for git commits
- ✅ Force push prevention
- ✅ .env file security check
- ✅ Package installation reminders
- ✅ Docker cleanup confirmation
- ✅ Database migration confirmation
- ✅ Package.json version tracking
- ✅ Recursive delete protection

**PostToolUse Hooks (Monitoring):**
- File modification tracking
- Test failure alerts
- Build size monitoring

**SessionEnd Hooks:**
- Session summary with statistics

---

## 🎓 Learning Workflow

### Recommended Usage Pattern:

1. **Start with Skills** - Let Claude auto-detect when to help
   ```
   You: "Can you explain this code?"
   → code-explainer skill activates automatically
   ```

2. **Use Commands for Workflows** - Manual invocation for specific tasks
   ```
   You: "/commit"
   → Guided commit creation
   ```

3. **Call Subagents for Expertise** - Specialized deep-dive analysis
   ```
   You: "Use code-reviewer subagent to review my API endpoints"
   → Comprehensive expert review
   ```

4. **Trust the Hooks** - Automatic safety and validation
   ```
   You: "git commit this file"
   → Hook checks for secrets automatically
   ```

---

## 📖 Detailed Rule References

For detailed usage patterns and examples, see:
- **Skills Reference:** `@starter-kit/.claude/rules/skills-reference.md`
- **Commands Reference:** `@starter-kit/.claude/rules/commands-reference.md`
- **Agents Reference:** `@starter-kit/.claude/rules/agents-reference.md`
- **Hooks Reference:** `@starter-kit/.claude/rules/hooks-reference.md`
- **Workflows:** `@starter-kit/.claude/rules/workflows/`
- **Frameworks:** `@starter-kit/.claude/rules/frameworks/`

---

## 🚀 Quick Start

### First Time Setup:
```bash
# Copy starter kit to your project
cp -r starter-kit/.claude /path/to/your/project/

# Start using Claude Code
cd /path/to/your/project
claude
```

### Try Your First Skill:
```
You: "Can you create a README for this project?"
Claude: [readme-generator skill activates]
```

### Try Your First Command:
```
You: "/explain"
Claude: [Explains your code in detail]
```

### Try Your First Subagent:
```
You: "Use code-reviewer subagent to review my main.py file"
Claude: [Comprehensive expert review]
```

---

## 🔐 Security Features

### Built-in Protections:
- **Secret Detection:** Prevents committing API keys, passwords
- **Safe Git Operations:** Blocks destructive force pushes
- **File Safety:** Warns about .env files in commits
- **Confirmation Required:** For deletions, migrations, Docker ops

### What to Watch For:
- Always review hook warnings
- Never bypass security confirmations
- Keep .env files out of git
- Use environment variables for secrets

---

## 💡 Best Practices

### For Skills:
- Let Claude auto-invoke - don't force it
- Use natural language requests
- Skills activate based on context

### For Commands:
- Use `/` prefix for quick actions
- Commands are explicit workflows
- Check available commands with `/help`

### For Subagents:
- Call explicitly for deep analysis
- Specify which subagent to use
- Use for specialized tasks

### For Hooks:
- Never disable safety hooks
- Read hook messages carefully
- Configure in settings.json

---

## 📊 Progression Path

**Current Level:** Beginner (Starter Kit)

**Next Steps:**
1. Master all 5 skills
2. Try all 12 commands
3. Experiment with subagents
4. Understand hook behavior

**When Ready for Next Level:**
- Comfortable with basic workflows
- Building production applications
- Need framework-specific tools
- Want advanced automation

**Graduate To:** Intermediate Kit
- Location: `intermediate-kit/.claude/`
- Rules: `@intermediate-kit/.claude/rules/CLAUDE.md`
- Capabilities: 10 skills, 15 commands, 6 agents

---

## 🔗 Related Resources

**Templates:**
- Skill Template: `@templates/skill-template.md`
- Command Template: `@templates/command-template.md`
- Subagent Template: `@templates/subagent-template.md`

**Guides:**
- Getting Started: `@resources/guides/getting-started.md`
- Best Practices: `@resources/guides/best-practices.md`
- Security Guide: `@resources/guides/security.md`
- Troubleshooting: `@resources/guides/troubleshooting.md`

**Project Root:**
- Main Overview: `@CLAUDE.md`
- Project README: `@README.md`

---

**Level:** Beginner
**Last Updated:** 2025-11-01
**Capabilities:** 5 skills, 12 commands, 4 agents, 8+ hooks

