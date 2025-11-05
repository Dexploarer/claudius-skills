# Claudius Skills Marketplace

This directory contains the marketplace configuration for the Claudius Skills repository, making all skills, commands, agents, and hooks available as installable plugins via Claude Code.

## 📦 Marketplace Structure

The `marketplace.json` file defines **26 plugins** organized into several categories:

### Core & Kits (10 plugins)
- **claudius-core** - Core safety systems and rules
- **starter-kit** - Beginner-friendly (5 skills, 12 commands, 4 agents)
- **intermediate-kit** - Production-ready (10 skills, 15 commands, 6 agents)
- **advanced-kit** - Enterprise-grade (15 skills, 20 commands, 10 agents)
- **railway-deployment-kit** - Railway.app deployment (5 skills, 6 commands, 4 agents)
- **eliza-os-kit** - elizaOS development (6 skills, 8 commands, 6 agents)
- **competitive-ai-frameworks** - Multi-agent simulations (3 skills, 12 agents)
- **productivity-starter** - Workflow automation (5 skills)
- **productivity-intermediate** - Advanced workflows (1 skill)
- **external-repo-bootstrap** - Quick external setup (3 components)

### Hooks Collections (6 plugins)
- **development-safety** - Prevent common mistakes (5 hooks)
- **production-deployment** - Deployment safety (5 hooks)
- **code-quality** - Quality enforcement (5 hooks)
- **security-enforcement** - Security checks (5 hooks)
- **knowledge-cutoff** - Version verification (5 hooks)
- **strict-typing** - TypeScript strict mode (6 hooks)

### Framework Rules (5 plugins)
- **react** - React patterns
- **vue** - Vue 3 patterns
- **nextjs** - Next.js 13+ patterns
- **django** - Django patterns
- **fastapi** - FastAPI patterns

### Learning Examples (3 plugins)
- **example-skills-beginner** - 7 beginner examples
- **example-skills-intermediate** - 19 intermediate examples
- **example-skills-advanced** - 14 advanced examples

### Additional Resources (2 plugins)
- **modern-commands** - 10 modern workflow commands
- **specialized-agents** - 4 expert consultant agents

## 🚀 Using the Marketplace

### Installing Plugins

```bash
# Install a complete kit
claude plugin add claudius-skills-marketplace/starter-kit

# Install specific hook collections
claude plugin add claudius-skills-marketplace/hooks-collection-development-safety

# Install framework rules
claude plugin add claudius-skills-marketplace/framework-rules-react

# Install examples for learning
claude plugin add claudius-skills-marketplace/example-skills-beginner
```

### Recommended Installation Paths

**For Beginners:**
1. Start with `starter-kit`
2. Add `example-skills-beginner`
3. Add `hooks-collection-development-safety`

**For Intermediate Developers:**
1. Install `intermediate-kit`
2. Add relevant `framework-rules-*`
3. Add `hooks-collection-code-quality`
4. Add `example-skills-intermediate`

**For Advanced/Enterprise:**
1. Install `advanced-kit`
2. Add `hooks-collection-security-enforcement`
3. Add `hooks-collection-production-deployment`
4. Add specialized kits as needed

**For Specific Platforms:**
- Railway.app developers: `railway-deployment-kit`
- AI agent builders: `eliza-os-kit`
- Security researchers: `competitive-ai-frameworks`

## 📊 Repository Statistics

- **Total Skills**: 87 unique skills
- **Total Commands**: 80+ slash commands
- **Total Agents**: 46 specialized agents
- **Total Hooks**: 36 automated hooks
- **Framework Support**: 17 frameworks
- **Learning Examples**: 40+ documented examples

## 🎯 Plugin Categories

### Learning (3 plugins)
Beginner to advanced examples and the starter kit for learning Claude Code extensibility.

### Productivity (3 plugins)
Workflow automation and efficiency-focused configurations.

### Development (14 plugins)
Framework-specific rules, advanced kits, and specialized tools.

### Security (2 plugins)
Security-focused hooks for safety and vulnerability prevention.

### Utility (1 plugin)
Bootstrap tools for external repository access.

## 🔗 Plugin Dependencies

Some plugins work best together:

- **starter-kit** → pairs well with **example-skills-beginner**
- **intermediate-kit** → pairs well with **framework-rules-*** matching your stack
- **advanced-kit** → requires understanding of **intermediate-kit**
- **eliza-os-kit** → standalone but benefits from **hooks-collection-development-safety**
- **railway-deployment-kit** → standalone deployment toolkit

## 📝 Marketplace Schema

The marketplace follows the official Claude Code marketplace schema:

```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "claudius-skills-marketplace",
  "version": "1.0.0",
  "description": "...",
  "owner": { ... },
  "plugins": [ ... ]
}
```

Each plugin includes:
- **name** - Unique identifier
- **version** - Semantic version
- **description** - What it does
- **author** - Contact information
- **source** - Directory path in repository
- **category** - Plugin classification
- **keywords** - Searchable tags
- **readme** - Detailed description

## 🔄 Updates and Versioning

The marketplace follows semantic versioning:
- **Major** (1.x.x) - Breaking changes to plugin structure
- **Minor** (x.1.x) - New plugins or significant features
- **Patch** (x.x.1) - Bug fixes and minor improvements

Current version: **1.0.0** (Initial release)

## 🤝 Contributing

To add new plugins to the marketplace:

1. Create plugin directory structure
2. Add plugin entry to `marketplace.json`
3. Update this README
4. Test plugin installation
5. Submit pull request

## 📚 Resources

- [Main Repository](https://github.com/Dexploarer/claudius-skills)
- [Documentation](../docs/)
- [Claude Code Docs](https://docs.claude.com/en/docs/claude-code/)
- [Plugin Development Guide](https://docs.claude.com/en/docs/claude-code/plugin-marketplaces)

## 📄 License

MIT License - See [LICENSE](../LICENSE) file for details

---

**Built with ❤️ by the Claudius Skills Team**
