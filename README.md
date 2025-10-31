# Claudius Skills - Claude Code Enhancement Collection

> A curated collection of Claude Code configurations, skills, commands, hooks, subagents, and MCP integrations for all skill levels - from beginner to master.

## 🎯 What is This Repository?

This is a comprehensive learning and reference repository for **Claude Code's Five Pillars of Extensibility**:

1. **Skills** - Automatic, context-aware capabilities
2. **Slash Commands** - Manual shortcuts for common tasks
3. **Hooks** - Event-driven automation
4. **Subagents** - Specialized AI consultants
5. **MCP Servers** - External service integrations

Whether you're just getting started with Claude Code or you're a power user looking for advanced configurations, you'll find useful examples here.

---

## 📚 Repository Structure

```
claudius-skills/
├── starter-kit/           # Complete beginner-friendly setup (START HERE!)
│   ├── .claude/
│   │   ├── skills/       # 5 essential skills
│   │   ├── commands/     # 12 useful slash commands
│   │   ├── agents/       # 4 specialist subagents
│   │   └── settings.json # Hooks configuration
│   ├── README.md         # Comprehensive guide
│   └── QUICK_REFERENCE.md
│
├── examples/
│   ├── beginner/         # Simple, single-purpose examples
│   ├── intermediate/     # More complex, real-world examples
│   ├── advanced/         # Advanced techniques and patterns
│   └── master/           # Complex integrations and workflows
│
├── templates/            # Reusable templates for creating your own
│
└── resources/            # Additional documentation and guides
```

---

## 🚀 Quick Start

### For Complete Beginners

**Start with the Starter Kit:**

```bash
# Clone this repository
git clone <repo-url>
cd claudius-skills

# Copy the starter kit to your project
cp -r starter-kit/.claude /path/to/your/project/

# Or use it directly in the starter-kit directory
cd starter-kit
claude
```

**Read the guide:**
- 📖 [Starter Kit README](./starter-kit/README.md) - Complete beginner's guide
- 📋 [Quick Reference](./starter-kit/QUICK_REFERENCE.md) - Command lookup

### For Intermediate Users

Browse the `examples/` directory to find specific use cases and patterns.

### For Advanced Users

Check out the `advanced/` and `master/` examples for complex integrations and custom workflows.

---

## 🎓 Learning Path

### Level 1: Beginner (Start Here)
1. **Read** the [Starter Kit README](./starter-kit/README.md)
2. **Install** the starter kit in a test project
3. **Try** the slash commands (`/explain`, `/test`, `/commit`)
4. **Observe** how skills activate automatically
5. **Experiment** with calling subagents

### Level 2: Intermediate
1. **Customize** the starter kit for your needs
2. **Create** your own simple slash commands
3. **Modify** existing skills
4. **Add** basic hooks for your workflow
5. **Browse** examples in `examples/intermediate/`

### Level 3: Advanced
1. **Build** complex skills with multiple files
2. **Create** specialized subagents for your domain
3. **Design** hook-based workflows
4. **Integrate** MCP servers
5. **Combine** multiple pillars for powerful automation

### Level 4: Master
1. **Architect** complete development environments
2. **Create** plugin-quality configurations
3. **Share** your work with the community
4. **Contribute** back to this repository

---

## 📦 What's Included

### Starter Kit (Beginner-Friendly)

A complete, ready-to-use setup with:
- **5 Skills**: README generation, code explanation, bug finding, testing help, git assistance
- **12 Slash Commands**: Common tasks like `/explain`, `/test`, `/commit`, `/review`, etc.
- **4 Subagents**: Code reviewer, test writer, doc writer, debug helper
- **Hooks**: Safety checks, logging, session management
- **MCP Template**: Ready to connect external services

### Examples (Coming Soon)

**Beginner Examples:**
- Single-purpose skills
- Simple slash commands
- Basic hooks
- Starter subagents

**Intermediate Examples:**
- Framework-specific skills (React, Python, etc.)
- Project workflow commands
- Advanced hooks patterns
- Specialized subagents

**Advanced Examples:**
- Multi-file complex skills
- Plugin-style configurations
- Advanced MCP integrations
- Custom agent architectures

**Master Examples:**
- Complete development environments
- Team workflow systems
- Advanced automation pipelines
- Complex MCP orchestrations

### Templates

Blank templates for creating your own:
- Skill template
- Slash command template
- Subagent template
- Hooks configuration template
- MCP server configuration template

### Resources

- Guides and tutorials
- Best practices
- Troubleshooting tips
- Community contributions

---

## 🛠️ The Five Pillars Explained

### 1. Skills (Automatic)
Skills are like teaching Claude specialized knowledge that activates automatically when needed.

**Example:** A skill for generating README files activates when you say "I need a README"

**Best for:** Reusable capabilities you use frequently

### 2. Slash Commands (Manual)
Quick shortcuts you trigger explicitly by typing `/command`.

**Example:** `/test` runs all tests in your project

**Best for:** Tasks you do repeatedly

### 3. Hooks (Event-Driven)
Automatic scripts that run when specific events occur.

**Example:** A hook that checks for secrets before every git commit

**Best for:** Enforcing rules and automating workflows

### 4. Subagents (Specialists)
Pre-configured AI personalities with specific expertise and separate context.

**Example:** A code-reviewer subagent that only has read access

**Best for:** Specialized analysis and keeping main conversation clean

### 5. MCP Servers (External)
Connections to external services like GitHub, databases, Slack, etc.

**Example:** An MCP server that lets Claude access your GitHub issues

**Best for:** Integrating with tools and services outside Claude Code

---

## 🎯 Use Cases

### For Individual Developers
- Set up your personal development environment
- Automate repetitive tasks
- Learn best practices through examples
- Customize workflows to your preferences

### For Teams
- Share standardized configurations via git
- Enforce code quality with hooks
- Create team-specific skills and commands
- Build collaborative workflows

### For Educators
- Teach programming concepts with skills
- Provide students with helpful subagents
- Create assignment-specific commands
- Build learning-focused environments

### For Open Source Projects
- Provide contributors with project-specific tools
- Automate contribution workflows
- Create project documentation helpers
- Standardize code review processes

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Add Your Examples
Have a useful skill, command, or configuration? Share it!

1. Fork this repository
2. Add your example to the appropriate directory
3. Include clear documentation
4. Submit a pull request

### Improve Documentation
- Fix typos or unclear explanations
- Add more examples
- Create tutorials
- Translate to other languages

### Share Your Experience
- Report what works well
- Suggest improvements
- Share use cases
- Help other users

### Contribution Guidelines
- **Document everything** - Clear explanations help everyone
- **Test your code** - Make sure it actually works
- **Follow the structure** - Keep things organized
- **Be beginner-friendly** - Remember, many users are learning

---

## 📖 Additional Resources

### Official Documentation
- [Claude Code Docs](https://docs.claude.com/en/docs/claude-code/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

### Learning Resources
- [Starter Kit Guide](./starter-kit/README.md) - Start here!
- [Quick Reference](./starter-kit/QUICK_REFERENCE.md) - Command lookup
- Templates directory - Create your own

### Community
- GitHub Issues - Ask questions, report bugs
- Discussions - Share ideas and examples
- Pull Requests - Contribute your work

---

## 🗺️ Roadmap

### Current (v1.0)
- ✅ Complete starter kit with all five pillars
- ✅ Comprehensive documentation
- ✅ Beginner-friendly setup

### Upcoming (v1.1)
- [ ] Add beginner examples
- [ ] Add intermediate examples
- [ ] Create templates directory
- [ ] Add framework-specific skills

### Future (v2.0)
- [ ] Advanced examples
- [ ] Master-level examples
- [ ] Video tutorials
- [ ] Interactive examples
- [ ] Plugin marketplace integration

---

## 📝 License

This repository is provided as-is for educational and practical use. Feel free to use, modify, and share.

---

## 🙏 Acknowledgments

- The Claude Code team for building an amazing extensible AI assistant
- The MCP community for creating useful integrations
- Contributors who share their configurations and examples

---

## 🚀 Get Started Now!

1. **Clone this repository**
   ```bash
   git clone <repo-url>
   cd claudius-skills
   ```

2. **Check out the starter kit**
   ```bash
   cd starter-kit
   cat README.md
   ```

3. **Copy to your project**
   ```bash
   cp -r .claude /path/to/your/project/
   ```

4. **Start Claude Code**
   ```bash
   cd /path/to/your/project
   claude
   ```

5. **Try a command**
   ```bash
   /explain console.log("Hello, world!")
   ```

**Welcome to the world of enhanced Claude Code! 🎉**

---

## ❓ FAQ

**Q: Do I need to use all five pillars?**
A: No! Start with what makes sense for you. Skills and slash commands are the easiest to begin with.

**Q: Can I use these in existing projects?**
A: Yes! Just copy the `.claude/` directory to your project.

**Q: Will this work with my team?**
A: Yes! Everything in `.claude/` is designed to be shared via git.

**Q: Is this safe to use?**
A: The included configurations are safe, but always review hooks and MCP servers before using them, as they run code and access external services.

**Q: How do I create my own skills/commands?**
A: Check the templates directory and look at existing examples. Start simple and build from there!

**Q: Where can I find more examples?**
A: Check the `examples/` directory. More examples are being added regularly.

**Q: Can I contribute?**
A: Absolutely! We welcome contributions. See the Contributing section above.

---

**Built with ❤️ for the Claude Code community**
