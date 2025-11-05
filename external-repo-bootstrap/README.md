# Claudius Skills Bootstrap - External Repository Access

> **🚀 Quick Start: Get Claudius Skills in ANY project**

This bootstrap enables users working in external repositories to automatically set up their entire `.claude` configuration using the Claudius Skills repository.

---

## 🎯 What This Is

The **Claudius Skills Bootstrap** is a minimal `.claude` setup that you can copy to any project. Once installed, it provides:

1. **Automated Repository Access** - Connects to the Claudius Skills repository
2. **Intelligent Project Analysis** - Detects your frameworks and project type
3. **Smart Recommendations** - Suggests the right skills, commands, agents, and hooks
4. **One-Command Installation** - Install complete configurations with `/claudius-setup`
5. **Update Management** - Keep your configurations up-to-date

---

## 📦 Installation Methods

### Method 1: Quick Bootstrap (Recommended)

Copy the bootstrap to your project:

```bash
# From within the claudius-skills repository
cp -r external-repo-bootstrap/.claude /path/to/your/project/

# Or download directly from GitHub
curl -L https://github.com/Dexploarer/claudius-skills/archive/main.zip -o claudius.zip
unzip claudius.zip
cp -r claudius-skills-main/external-repo-bootstrap/.claude /path/to/your/project/
rm -rf claudius.zip claudius-skills-main
```

Then in your project:

```bash
cd /path/to/your/project
claude
```

Say: **"setup claudius for my project"** or run `/claudius-setup`

### Method 2: Manual Setup

If you prefer to set up manually:

```bash
# 1. Create .claude directory structure
mkdir -p .claude/{skills,commands,subagents,rules}

# 2. Copy bootstrap components
cp external-repo-bootstrap/.claude/skills/claudius-installer.md .claude/skills/
cp external-repo-bootstrap/.claude/subagents/claudius-setup-agent.md .claude/subagents/
cp external-repo-bootstrap/.claude/commands/claudius-*.md .claude/commands/

# 3. Start Claude Code and run setup
claude
```

Say: **"/claudius-setup"**

### Method 3: One-Line Install Script

We provide a one-line installer script:

```bash
curl -fsSL https://raw.githubusercontent.com/Dexploarer/claudius-skills/main/external-repo-bootstrap/install.sh | bash
```

This script:
- Creates `.claude` directory
- Copies bootstrap files
- Clones claudius-skills repository to `~/.claudius-skills`
- Runs initial setup wizard

---

## 🎮 How It Works

### Step 1: Bootstrap Installation

You copy the minimal bootstrap `.claude` to your project:

```
your-project/
├── .claude/
│   ├── skills/
│   │   └── claudius-installer.md      # Installation skill
│   ├── commands/
│   │   ├── claudius-setup.md          # Setup wizard
│   │   ├── claudius-update.md         # Update manager
│   │   └── claudius-info.md           # Installation info
│   └── subagents/
│       └── claudius-setup-agent.md    # Setup orchestrator
└── ... (your project files)
```

### Step 2: Repository Cloning

When you run `/claudius-setup`, it clones the full Claudius Skills repository:

```bash
~/.claudius-skills/
├── starter-kit/
├── intermediate-kit/
├── advanced-kit/
├── productivity-skills/
├── competitive-ai-frameworks/
├── eliza-os-kit/
├── railway-deployment-kit/
├── examples/
├── hooks-collection/
└── ... (complete repository)
```

### Step 3: Project Analysis

The setup agent analyzes your project:

```typescript
{
  type: 'frontend',              // Detected from package.json
  frameworks: ['React', 'Vite'],  // Identified dependencies
  complexity: 'intermediate',     // Based on project size
  languages: ['TypeScript'],      // From file extensions
  hasTests: true,                 // Found test files
  recommendations: {
    kits: ['intermediate-kit'],
    skills: ['react-component-generator', 'test-helper'],
    commands: ['/test', '/review', '/commit'],
    agents: ['code-reviewer', 'test-writer'],
    hooks: ['secret-scanning', 'test-coverage-enforcement']
  }
}
```

### Step 4: Installation

Based on analysis, components are copied to your project:

```bash
# Skills copied
cp ~/.claudius-skills/intermediate-kit/.claude/skills/* .claude/skills/

# Commands copied
cp ~/.claudius-skills/intermediate-kit/.claude/commands/* .claude/commands/

# Agents copied
cp ~/.claudius-skills/intermediate-kit/.claude/subagents/* .claude/subagents/

# Hooks copied
cp ~/.claudius-skills/intermediate-kit/.claude/hooks/* .claude/hooks/

# Rules copied
cp ~/.claudius-skills/intermediate-kit/.claude/rules/* .claude/rules/
```

### Step 5: Tracking

A manifest file tracks your installation:

```json
{
  "version": "1.0.0",
  "installedAt": "2025-11-05T00:00:00Z",
  "repositoryCommit": "f28b746...",
  "components": {
    "kits": ["intermediate-kit"],
    "skills": ["react-component-generator", "test-helper"],
    "commands": ["/test", "/review"],
    "agents": ["code-reviewer"],
    "hooks": ["secret-scanning"]
  }
}
```

---

## 💡 Usage Examples

### Example 1: React Frontend Project

```bash
# Copy bootstrap
cp -r external-repo-bootstrap/.claude ~/my-react-app/

# Navigate to project
cd ~/my-react-app

# Start Claude Code
claude
```

**Interaction:**

```
User: "setup claudius for my project"

Claude (via claudius-installer + setup agent):
Analyzing your project...

✓ Detected: React 18.2 with TypeScript
✓ Build Tool: Vite
✓ Testing: Vitest

Recommended: Intermediate Kit
- react-component-generator skill
- test-helper skill
- /test, /review, /commit commands
- code-reviewer, test-writer agents
- Security hooks enabled

Install? [yes/no/customize]

User: "yes"

Claude:
✅ Installation complete!

Try: "create a Button component with TypeScript"
```

### Example 2: Django Backend Project

```bash
cp -r external-repo-bootstrap/.claude ~/my-django-api/
cd ~/my-django-api
claude
```

```
User: "/claudius-setup"

Claude:
Analyzing your project...

✓ Detected: Django 4.2 with PostgreSQL
✓ Testing: pytest

Recommended: Intermediate Kit
- django-model-helper skill
- api-documentation-generator skill
- database-architect agent
- Security hooks for Django

Install? [yes]
```

### Example 3: ElizaOS Agent Project

```bash
cp -r external-repo-bootstrap/.claude ~/my-eliza-agent/
cd ~/my-eliza-agent
claude
```

```
User: "setup claudius"

Claude:
Analyzing your project...

✓ Detected: ElizaOS (@ai16z/eliza)
✓ Characters directory found

Recommended: Eliza OS Kit
- character-generator skill
- plugin-builder skill
- /dev-agent, /test-character commands
- character-designer agent

Install? [yes]
```

### Example 4: Enterprise Microservices

```bash
cp -r external-repo-bootstrap/.claude ~/enterprise-platform/
cd ~/enterprise-platform
claude
```

```
User: "/claudius-setup"

Claude:
Analyzing your project...

✓ Detected: Multiple services (8)
✓ Kubernetes configuration
✓ CI/CD pipeline

Recommended: Advanced Kit (Enterprise)
- 15 enterprise skills
- 20 advanced commands
- 10 specialist consultants
- Full compliance suite

Install? [yes]
```

---

## 🔧 Commands Available

### `/claudius-setup`
Interactive setup wizard

```bash
/claudius-setup              # Interactive mode
/claudius-setup auto         # Auto-install recommended
/claudius-setup custom       # Custom component selection
/claudius-setup dry-run      # Show recommendations only
```

### `/claudius-update`
Check for and install updates

```bash
/claudius-update             # Check for updates
/claudius-update all         # Update everything
/claudius-update skills      # Update only skills
/claudius-update --force     # Skip confirmations
```

### `/claudius-info`
Show installation information

```bash
/claudius-info               # Full installation info
/claudius-info version       # Version info only
/claudius-info components    # List components
```

---

## 🎯 What Gets Installed

Depending on your project, you'll get:

### Skills (Context-Aware Capabilities)
- Framework-specific generators (React, Vue, Django, Express, etc.)
- Testing helpers (Jest, Vitest, pytest, etc.)
- API documentation generators
- Version checkers and validators
- Security analyzers

### Commands (Manual Workflows)
- `/commit` - Smart git commits
- `/test` - Run tests with coverage
- `/review` - Code review
- `/deploy` - Deployment automation
- `/security-audit` - Security scanning

### Agents (AI Consultants)
- `code-reviewer` - Code review expert
- `test-writer` - Test generation specialist
- `database-architect` - Database design consultant
- `security-auditor` - Security analysis expert
- `performance-optimizer` - Performance tuning

### Hooks (Event-Driven Automation)
- Secret scanning before commits
- Force push prevention
- Test coverage enforcement
- Build size monitoring
- Dependency vulnerability scanning

### Rules (Framework & Project Guidelines)
- Framework-specific best practices
- Testing strategies
- Security guidelines
- Performance optimization rules

---

## 🔄 Update Workflow

Keep your installation up-to-date:

```bash
# Monthly: Check for updates
/claudius-update

# Review changelog
# Apply updates

# Or automatic updates
"enable auto-update for claudius"
```

Updates are tracked and backed up:

```
.claude/.backup/
├── 2025-11-05/    # Backup before latest update
├── 2025-10-15/    # Backup before previous update
└── ...
```

Rollback if needed:

```bash
"rollback claudius to 2025-10-15"
```

---

## 🛡️ Security Considerations

### Repository Verification

The bootstrap only connects to the official repository:

```
https://github.com/Dexploarer/claudius-skills.git
```

Before installation, verify:
```bash
cd ~/.claudius-skills
git remote -v
# Should show official repository
```

### Component Review

Always review what's being installed:
- Use `/claudius-setup dry-run` to see recommendations
- Review components before confirming installation
- Check hooks for unintended side effects

### Safe Defaults

Bootstrap includes security by default:
- Secret scanning enabled
- Force push prevention
- Environment file protection
- Dependency vulnerability scanning

---

## 🔧 Configuration

### Custom Repository Location

By default, claudius-skills is cloned to `~/.claudius-skills`. Change this:

```bash
"set claudius repository to /custom/path"
```

Or edit the configuration:

```json
{
  "claudius": {
    "repositoryPath": "/custom/path/to/claudius-skills",
    "repositoryUrl": "https://github.com/Dexploarer/claudius-skills.git",
    "autoUpdate": false,
    "updateCheckInterval": "7d"
  }
}
```

### Custom Repository (Forks)

Use your own fork:

```bash
"set claudius repository to https://github.com/my-org/custom-skills.git"
/claudius-setup
```

---

## 🐛 Troubleshooting

### Issue: Repository Clone Fails

**Error:**
```
Failed to clone repository
```

**Solutions:**
1. Check internet connection
2. Verify git is installed: `git --version`
3. Try manual clone:
   ```bash
   git clone https://github.com/Dexploarer/claudius-skills.git ~/.claudius-skills
   ```
4. Check firewall/proxy settings

### Issue: Permission Denied

**Error:**
```
Permission denied writing to .claude/
```

**Solutions:**
1. Check ownership: `ls -la .`
2. Fix permissions: `chmod -R u+w .claude/`
3. Ensure you own the directory

### Issue: Components Not Loading

**Error:**
```
Component not found or not loading
```

**Solutions:**
1. Verify file structure: `ls -R .claude/`
2. Check manifest: `cat .claude/.claudius-manifest.json`
3. Restart Claude Code
4. Reinstall: `/claudius-setup --force`

### Issue: Conflicts with Existing Config

**Warning:**
```
Existing .claude configuration found
```

**Solutions:**
1. Backup existing: `cp -r .claude .claude.backup`
2. Merge configurations (recommended)
3. Replace (if starting fresh)
4. Cherry-pick components

---

## 📚 Documentation

### In This Repository

- **README.md** (this file) - Bootstrap overview
- **INSTALLATION.md** - Detailed installation guide
- **ARCHITECTURE.md** - How the system works
- **EXAMPLES.md** - Real-world usage examples

### In Claudius Skills Repository

After cloning (`~/.claudius-skills/`):

- **README.md** - Main repository documentation
- **CLAUDE.md** - Project rules and architecture
- **IMPLEMENTATION_PROGRESS.md** - Complete skill listing
- **Kit-specific READMEs** - Detailed kit documentation

### Online

- Repository: https://github.com/Dexploarer/claudius-skills
- Documentation: https://github.com/Dexploarer/claudius-skills/wiki
- Issues: https://github.com/Dexploarer/claudius-skills/issues

---

## 🚀 Advanced Usage

### Multi-Project Setup

Install across all projects:

```bash
# Setup script for all projects
for dir in ~/projects/*/; do
  echo "Setting up $dir"
  cp -r external-repo-bootstrap/.claude "$dir"
  cd "$dir"
  claude --run "/claudius-setup auto"
done
```

### Team Sharing

Share your configuration:

```bash
# Export your setup
"export my claudius setup for team"
# Creates: claudius-team-config.tar.gz

# Team members install
tar -xzf claudius-team-config.tar.gz
cp -r .claude /path/to/project/
```

### Custom Kits

Create custom combinations:

```bash
"create custom kit with React, testing, and Railway deployment"
# Agent will cherry-pick components and create custom kit
```

### CI/CD Integration

Automate setup in CI:

```yaml
# .github/workflows/setup-claude.yml
name: Setup Claude Configuration
on: [push]
jobs:
  setup:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install Claudius Bootstrap
        run: |
          curl -fsSL https://raw.githubusercontent.com/Dexploarer/claudius-skills/main/external-repo-bootstrap/install.sh | bash
```

---

## 🎓 Learning Path

### 1. Start Simple
- Copy bootstrap to your project
- Run `/claudius-setup auto`
- Try recommended skills and commands

### 2. Explore
- Run `/claudius-info` to see what you have
- Try different skills: "create a component"
- Use commands: `/test`, `/review`

### 3. Customize
- Add specific components you need
- Remove unused components
- Adjust hook configurations

### 4. Stay Updated
- Monthly: `/claudius-update`
- Review new features
- Try new kits as they're released

### 5. Contribute
- Share useful customizations
- Report issues
- Suggest improvements

---

## 🤝 Contributing

Found a better way to do external repo access? Have ideas for improvements?

1. Fork the repository
2. Create your feature branch
3. Submit a pull request

Or open an issue:
https://github.com/Dexploarer/claudius-skills/issues

---

## 📄 License

Claudius Skills Bootstrap is part of the Claudius Skills project.

See LICENSE in the main repository.

---

## 🙏 Credits

Created by the Claudius Skills Project Team

Special thanks to:
- Claude Code team at Anthropic
- Community contributors
- Early adopters and testers

---

## 📞 Support

- **Issues**: https://github.com/Dexploarer/claudius-skills/issues
- **Discussions**: https://github.com/Dexploarer/claudius-skills/discussions
- **Wiki**: https://github.com/Dexploarer/claudius-skills/wiki

---

**Version:** 1.0.0
**Last Updated:** 2025-11-05
**Repository:** https://github.com/Dexploarer/claudius-skills

---

## Quick Start Summary

```bash
# 1. Copy bootstrap
cp -r external-repo-bootstrap/.claude /path/to/your/project/

# 2. Navigate to project
cd /path/to/your/project

# 3. Start Claude Code
claude

# 4. Run setup
# Say: "setup claudius for my project"
# Or: /claudius-setup

# 5. Start using
# Say: "create a Button component"
# Or: /test
```

That's it! 🎉
