# How to Use Claudius Skills from External Repositories

**Quick Reference Guide for Developers**

---

## ⚡ Quick Start (30 seconds)

### One-Line Installation

Run this in your project directory:

```bash
curl -fsSL https://raw.githubusercontent.com/Dexploarer/claudius-skills/main/external-repo-bootstrap/install.sh | bash
```

Then start Claude Code:

```bash
claude
```

And say: **"setup claudius for my project"** or run `/claudius-setup`

**That's it!** The system will:
1. Analyze your project
2. Recommend appropriate skills and commands
3. Install everything automatically
4. Keep you updated with `/claudius-update`

---

## 🎯 What You Get

### Minimal Bootstrap (4 files copied to your project)

```
your-project/
├── .claude/
│   ├── skills/
│   │   └── claudius-installer.md       # ~657 lines - Installation management
│   ├── commands/
│   │   ├── claudius-setup.md           # ~376 lines - Setup wizard
│   │   ├── claudius-update.md          # ~389 lines - Update manager
│   │   └── claudius-info.md            # ~104 lines - Installation info
│   └── subagents/
│       └── claudius-setup-agent.md     # ~617 lines - Setup orchestrator
```

**Total:** ~2,143 lines (~100KB)

### Full Repository (cloned to `~/.claudius-skills/`)

- 87 skills across 8 kits
- 86 commands
- 50 agents
- 36 hooks
- 17 framework rules
- Complete documentation

---

## 🔧 How It Works

### Architecture

```
┌─────────────────────────────────────┐
│     Your Project (.claude/)         │
│  • Bootstrap files (4 files)        │
│  • Triggers installation            │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  ~/.claudius-skills/ (Local Cache)  │
│  • Full repository clone            │
│  • All 8 kits available             │
│  • Updated via git pull             │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   GitHub: Dexploarer/claudius-skills│
│  • Source of truth                  │
│  • Latest updates                   │
└─────────────────────────────────────┘
```

### Workflow

1. **Bootstrap Installation** - Copy minimal .claude setup to your project
2. **Activation** - Run `/claudius-setup` in Claude Code
3. **Repository Access** - System clones full repo to `~/.claudius-skills`
4. **Project Analysis** - Detects frameworks, languages, complexity
5. **Recommendations** - Suggests appropriate kits, skills, commands, agents
6. **Installation** - Copies selected components to your project
7. **Tracking** - Creates manifest to track what's installed
8. **Updates** - Run `/claudius-update` to keep everything current

---

## 📋 Installation Methods

### Method 1: One-Line Installer (Recommended)

```bash
# In your project directory
curl -fsSL https://raw.githubusercontent.com/Dexploarer/claudius-skills/main/external-repo-bootstrap/install.sh | bash
```

**What it does:**
- ✅ Clones full repo to `~/.claudius-skills` (if needed)
- ✅ Creates `.claude/` structure in current directory
- ✅ Copies 4 bootstrap files
- ✅ Verifies installation
- ✅ Shows next steps

---

### Method 2: Manual Copy

```bash
# 1. Clone repository (one-time)
git clone https://github.com/Dexploarer/claudius-skills.git ~/.claudius-skills

# 2. Copy bootstrap to your project
cd /path/to/your/project
cp -r ~/.claudius-skills/external-repo-bootstrap/.claude .

# 3. Start Claude Code
claude
```

Then: **"setup claudius"** or `/claudius-setup`

---

### Method 3: Git Submodule (For Teams)

```bash
# Add as submodule
git submodule add https://github.com/Dexploarer/claudius-skills.git .claudius-skills

# Copy bootstrap
cp -r .claudius-skills/external-repo-bootstrap/.claude .

# Commit
git add .gitmodules .claudius-skills .claude
git commit -m "Add Claudius Skills bootstrap"
```

**Benefits:**
- ✅ Version controlled
- ✅ Team syncs exact versions
- ✅ Easy updates: `git submodule update --remote`

---

## 🚀 Usage Examples

### Example 1: React Developer

```bash
cd ~/my-react-app
curl -fsSL https://raw.githubusercontent.com/Dexploarer/claudius-skills/main/external-repo-bootstrap/install.sh | bash
claude
```

```
You: "setup claudius"

Claude:
Analyzing project...
✓ React 18.2 + TypeScript + Vite

Recommending: Intermediate Kit
- react-component-generator
- test-helper
- bundle-analyzer
- /test, /review, /commit commands
- code-reviewer, test-writer agents

Install? yes

✅ Complete!
Try: "create a Button component"
```

---

### Example 2: Django Backend

```bash
cd ~/my-django-api
cp -r ~/.claudius-skills/external-repo-bootstrap/.claude .
claude
```

```
You: "/claudius-setup"

Claude:
Analyzing...
✓ Django 4.2 + PostgreSQL

Recommended additions:
- django-model-helper
- api-documentation-generator
- database-architect agent
- Security hooks

Install? yes
```

---

### Example 3: Enterprise Microservices

```bash
cd ~/enterprise-platform
/claudius-setup
```

```
Claude:
Analyzing...
✓ 12 services
✓ Kubernetes + Terraform
✓ CI/CD pipelines

Recommended: Advanced Kit (Enterprise)
- 15 enterprise skills
- 20 advanced commands
- 10 specialist consultants
- Full compliance automation

Install? yes

✅ Enterprise toolkit ready!
Try: /compliance-scan soc2
```

---

## 🔄 Keeping Updated

### Check for Updates

```bash
/claudius-update
```

**Shows:**
- What's new in the repository
- Which components can be updated
- Breaking changes
- Changelog

### Auto-Update Specific Components

```bash
# Update all
"update all claudius components"

# Selective update
"update only claudius skills"

# Check without updating
"/claudius-update dry-run"
```

---

## 📦 What Gets Installed

### Project Detection

The system automatically detects:

- **Frameworks:** React, Vue, Angular, Django, Express, FastAPI, etc.
- **Languages:** TypeScript, JavaScript, Python, Go, Rust
- **Tools:** Vite, Webpack, Jest, Vitest, pytest
- **Complexity:** Starter, Intermediate, Advanced, Enterprise

### Smart Recommendations

Based on detection:

| Detected | Recommended Kit | Key Components |
|----------|----------------|----------------|
| React + TypeScript | Intermediate Kit | react-component-generator, test-helper, bundle-analyzer |
| Django + PostgreSQL | Intermediate Kit | django-model-helper, api-docs-generator, database-architect |
| Microservices | Advanced Kit | microservices-orchestrator, distributed-tracing, compliance-auditor |
| ElizaOS | Eliza OS Kit | character-generator, plugin-builder, deployment-helper |

---

## 🎓 Commands Reference

### Core Commands

| Command | Description |
|---------|-------------|
| `/claudius-setup` | Interactive setup wizard |
| `/claudius-setup auto` | Auto-install recommended config |
| `/claudius-update` | Check and install updates |
| `/claudius-info` | Show installation details |

### After Installation

Typical intermediate setup includes:

**Skills:**
- Framework-specific generators (React, Vue, Django, etc.)
- Testing helpers
- Version checker
- Documentation generators

**Commands:**
- `/commit` - Smart git commits
- `/test` - Run tests with coverage
- `/review` - Code review
- `/refactor` - Intelligent refactoring
- `/deploy` - Deployment automation

**Agents:**
- `code-reviewer` - Code review expert
- `test-writer` - Test generation specialist
- `database-architect` - Database design consultant
- `performance-optimizer` - Performance tuning expert

**Hooks:**
- Secret scanning
- Test coverage enforcement
- Build size monitoring
- Force push prevention

---

## 🔐 Security

### Repository Verification

Always verify you're using the official repository:

```bash
cd ~/.claudius-skills
git remote -v

# Should show:
# origin  https://github.com/Dexploarer/claudius-skills.git
```

### Built-in Security

Bootstrap includes:
- ✅ Secret scanning before commits
- ✅ Environment file protection
- ✅ Force push prevention
- ✅ Dependency vulnerability scanning

### Safe Installation

- ✅ Never overwrites without confirmation
- ✅ Backs up existing configurations
- ✅ Read-only bootstrap files
- ✅ Manifest tracking of all changes

---

## 🐛 Troubleshooting

### Install Script Fails

```bash
# Check git
git --version

# Check connectivity
ping github.com

# Manual clone
git clone https://github.com/Dexploarer/claudius-skills.git ~/.claudius-skills

# Copy bootstrap manually
cp -r ~/.claudius-skills/external-repo-bootstrap/.claude .
```

### Permission Errors

```bash
# Fix ownership
sudo chown -R $USER .claude/

# Fix permissions
chmod -R u+w .claude/
```

### Components Not Loading

```bash
# Verify installation
ls -R .claude/

# Check manifest
cat .claude/.claudius-manifest.json

# Reinstall
/claudius-setup --force
```

---

## 📚 Full Documentation

- **This guide:** Quick reference for external repo usage
- **Complete guide:** [EXTERNAL_REPO_ACCESS.md](EXTERNAL_REPO_ACCESS.md) - 1,000+ lines
- **Main README:** [README.md](README.md) - Project overview
- **Project rules:** [CLAUDE.md](CLAUDE.md) - Claude Code guidance
- **Bootstrap README:** [external-repo-bootstrap/README.md](external-repo-bootstrap/README.md)

---

## 💡 Tips & Best Practices

### 1. Start Clean

Best used on new projects or after backing up existing `.claude/` directory.

### 2. Trust Recommendations

The setup agent analyzes your actual project structure - its recommendations are based on what you're using.

### 3. Keep Updated

Run `/claudius-update` monthly to get new features, security fixes, and improvements.

### 4. Selective Installation

You don't need to install everything. Start with recommended kit, add more as needed.

### 5. Document Customizations

If you customize components, note changes in the manifest for future reference.

---

## 🌟 Key Benefits

### For Individual Developers

- ⚡ **Fast Setup:** 30 seconds to install
- 🎯 **Smart Recommendations:** Based on your actual project
- 🔄 **Stay Updated:** Easy updates via `/claudius-update`
- 📦 **Lightweight:** Only ~100KB bootstrap in your project

### For Teams

- 🤝 **Consistent:** Same configurations across team
- 📋 **Version Controlled:** Git submodule support
- 🔐 **Secure:** Built-in security hooks
- 📊 **Trackable:** Manifest tracks all components

### For Enterprises

- 🏢 **Scalable:** Supports microservices and distributed systems
- ✅ **Compliant:** SOC2, HIPAA, GDPR, PCI-DSS automation
- 🔍 **Observable:** Full observability stack
- 🚀 **Production-Ready:** Battle-tested configurations

---

## 🎯 Next Steps

1. **Install Bootstrap**
   ```bash
   curl -fsSL https://raw.githubusercontent.com/Dexploarer/claudius-skills/main/external-repo-bootstrap/install.sh | bash
   ```

2. **Run Setup**
   ```bash
   claude
   # Say: "setup claudius for my project"
   ```

3. **Start Using**
   - Generate components: "create a User component"
   - Run commands: `/test`, `/review`, `/commit`
   - Get help: "show me my claudius setup"

4. **Stay Updated**
   - Monthly: `/claudius-update`
   - Review changelog
   - Test in dev branch

---

## 📞 Support

- **Issues:** https://github.com/Dexploarer/claudius-skills/issues
- **Discussions:** https://github.com/Dexploarer/claudius-skills/discussions
- **Documentation:** https://github.com/Dexploarer/claudius-skills
- **Main Repo:** `~/.claudius-skills/README.md` (after installation)

---

**Version:** 1.0.0
**Last Updated:** November 5, 2025
**Repository:** https://github.com/Dexploarer/claudius-skills
**Maintainer:** Claudius Skills Project Team

---

## One Command to Remember

```bash
curl -fsSL https://raw.githubusercontent.com/Dexploarer/claudius-skills/main/external-repo-bootstrap/install.sh | bash && claude
```

🎉 **That's all you need to access the entire Claudius Skills collection from any repository!**
