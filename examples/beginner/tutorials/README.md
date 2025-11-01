# Beginner Tutorials

Step-by-step tutorials to help you master Claude Code's Five Pillars.

## Available Tutorials

### 1. **your-first-command.md** - Create Your First Slash Command
Learn how to create a simple, useful slash command from scratch.

**What you'll build:** A `/format` command that formats code files

**Time:** 15 minutes

**Prerequisites:** Claude Code installed

### 2. **setting-up-hooks.md** - Your First Hook
Learn how to create hooks that run automatically on events.

**What you'll build:** A pre-commit hook that checks for console.log statements

**Time:** 20 minutes

**Prerequisites:** Understanding of bash commands

### 3. **creating-a-subagent.md** - Build a Specialized Subagent
Learn how to create a subagent for a specific task.

**What you'll build:** A subagent that generates commit messages

**Time:** 25 minutes

**Prerequisites:** Understanding of subagents

### 4. **mcp-workflow.md** - Connect Your First MCP Server
Learn how to set up and use MCP servers.

**What you'll build:** A complete workflow using GitHub + Memory servers

**Time:** 30 minutes

**Prerequisites:** GitHub account

### 5. **complete-workflow.md** - Build a Complete Development Workflow
Learn how to combine all five pillars into a cohesive workflow.

**What you'll build:** A full development environment setup

**Time:** 45 minutes

**Prerequisites:** Completion of tutorials 1-4

## Learning Path

### Week 1: Basics
- [x] Complete getting-started.md in resources/guides
- [x] Install the starter kit
- [x] Try all the commands and skills
- [ ] Complete tutorial 1: Your First Command

### Week 2: Automation
- [ ] Complete tutorial 2: Setting Up Hooks
- [ ] Create your own custom command
- [ ] Experiment with different hooks

### Week 3: Specialization
- [ ] Complete tutorial 3: Creating a Subagent
- [ ] Modify an existing skill
- [ ] Create a simple skill

### Week 4: Integration
- [ ] Complete tutorial 4: MCP Workflow
- [ ] Set up memory server
- [ ] Try filesystem or GitHub server

### Week 5: Mastery
- [ ] Complete tutorial 5: Complete Workflow
- [ ] Build your own complete setup
- [ ] Share with your team

## How to Use These Tutorials

### 1. Work Through in Order
Each tutorial builds on the previous one.

### 2. Hands-On Practice
Don't just read - actually create the examples.

### 3. Experiment
After each tutorial, try variations and customizations.

### 4. Take Notes
Document what works for you.

### 5. Build Your Own
Use tutorials as templates for your own creations.

## Tips for Success

### Start Simple
Don't try to build everything at once.

### Practice Regularly
Spend 30 minutes a day with Claude Code.

### Learn from Errors
When something doesn't work, understand why.

### Ask Questions
Use Claude Code itself to help you learn!

```bash
# Ask Claude:
"How do I make a skill activate on specific phrases?"
"What tools can a subagent use?"
"How do hooks work?"
```

### Share Your Progress
Document your learning journey - it helps solidify understanding.

## Additional Resources

### In This Repository
- **/examples/beginner/** - Simple, focused examples
- **/starter-kit/** - Complete working setup
- **/templates/** - Blank templates to copy
- **/resources/guides/** - Comprehensive guides

### Official Documentation
- [Claude Code Docs](https://docs.claude.com/en/docs/claude-code/)
- [MCP Documentation](https://modelcontextprotocol.io/)

## Getting Help

### When You're Stuck

1. **Check the example** - See how others solved it
2. **Read the guide** - Review the relevant best practices
3. **Ask Claude** - Use Claude Code to help you debug
4. **Search issues** - Someone may have had the same problem
5. **Ask the community** - Create a GitHub issue

### Common Problems

**"My skill doesn't activate"**
- Check the description field
- Make sure file is in `.claude/skills/`
- Try different phrasings
- Review tutorial 1 section on descriptions

**"My command doesn't work"**
- Verify file is in `.claude/commands/`
- Check filename matches command name
- Restart Claude Code
- Review tutorial 1

**"Hooks not running"**
- Test the bash command separately
- Check `.claude/settings.json` syntax
- Verify event name is correct
- Review tutorial 2

**"MCP server won't connect"**
- Check credentials are correct
- Verify `.mcp.json` syntax
- Ensure server package is accessible
- Review tutorial 4

## Next Steps After Tutorials

### Level 1: Apply What You Learned
- Create commands for your daily tasks
- Build skills for your framework
- Set up hooks for your workflow
- Connect MCP servers you need

### Level 2: Customize Further
- Build complex multi-step skills
- Create sophisticated hooks
- Design specialized subagents
- Integrate multiple MCP servers

### Level 3: Share with Team
- Document your setup
- Create team conventions
- Share best practices
- Build team-specific tools

### Level 4: Contribute Back
- Share useful examples
- Improve documentation
- Help other beginners
- Submit pull requests

## Completion Certificate

Once you complete all tutorials, you'll understand:
- ✅ How to create skills that activate automatically
- ✅ How to build slash commands for common tasks
- ✅ How to set up hooks for automation
- ✅ How to create specialized subagents
- ✅ How to integrate external services with MCP
- ✅ How to combine all five pillars into workflows

**Congratulations! You're now a Claude Code power user!** 🎉

---

**Ready to start? Begin with [your-first-command.md](./your-first-command.md)!**
