# External Repository Access Guide

> **How users in external repositories can use Claudius Skills**

This comprehensive guide explains how developers working in their own repositories can access and use the entire Claudius Skills collection.

---

## 🎯 Overview

The **Claudius Skills External Repo Access System** allows any developer to:

1. **Copy a minimal bootstrap** to their project (3 files)
2. **Run a single command** (`/claudius-setup`)
3. **Get intelligent recommendations** based on their project
4. **Install complete configurations** automatically
5. **Keep everything up-to-date** with `/claudius-update`

---

## 📦 System Architecture

### Three-Tier Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User's Project                            │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  .claude/ (Bootstrap - 3 files)                      │  │
│  │  ├── skills/claudius-installer.md                    │  │
│  │  ├── commands/claudius-setup.md                      │  │
│  │  └── subagents/claudius-setup-agent.md              │  │
│  └──────────────────────────────────────────────────────┘  │
│                           │                                  │
│                           │ Activates                        │
│                           ▼                                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│              ~/.claudius-skills/ (Local Cache)               │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Full Repository Clone                               │  │
│  │  ├── starter-kit/                                    │  │
│  │  ├── intermediate-kit/                               │  │
│  │  ├── advanced-kit/                                   │  │
│  │  ├── productivity-skills/                            │  │
│  │  ├── competitive-ai-frameworks/                      │  │
│  │  ├── eliza-os-kit/                                   │  │
│  │  ├── railway-deployment-kit/                         │  │
│  │  ├── examples/                                       │  │
│  │  ├── hooks-collection/                               │  │
│  │  └── ...                                             │  │
│  └──────────────────────────────────────────────────────┘  │
│                           │                                  │
│                           │ Sources components               │
│                           ▼                                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│          GitHub: Dexploarer/claudius-skills                  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Source of Truth                                     │  │
│  │  • 87 skills across 8 kits                          │  │
│  │  • 86 commands                                       │  │
│  │  • 50 agents                                         │  │
│  │  • 36 hooks                                          │  │
│  │  • 17 frameworks                                     │  │
│  │  • Complete documentation                            │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Component Flow

```
1. User copies bootstrap → Project has minimal .claude/ setup
2. User runs /claudius-setup → Activates installer skill + setup agent
3. Agent clones repository → Full repo cached at ~/.claudius-skills
4. Agent analyzes project → Detects frameworks, complexity, needs
5. Agent recommends components → Shows appropriate kits/skills/commands
6. User confirms → Agent copies selected components to project
7. Manifest created → Tracks what's installed and when
8. User runs /claudius-update → Keeps components up-to-date
```

---

## 🚀 Installation Methods

### Method 1: One-Line Installer (Easiest)

```bash
curl -fsSL https://raw.githubusercontent.com/Dexploarer/claudius-skills/main/external-repo-bootstrap/install.sh | bash
```

This script:
- ✅ Clones repository to `~/.claudius-skills`
- ✅ Creates `.claude/` structure in current directory
- ✅ Copies bootstrap files (skill, agent, commands)
- ✅ Verifies installation
- ✅ Provides next steps

### Method 2: Manual Bootstrap Copy

```bash
# Clone the repository first (one-time)
git clone https://github.com/Dexploarer/claudius-skills.git ~/.claudius-skills

# Copy bootstrap to your project
cp -r ~/.claudius-skills/external-repo-bootstrap/.claude /path/to/your/project/

# Navigate to project and start Claude
cd /path/to/your/project
claude
```

Then say: **"setup claudius for my project"** or run `/claudius-setup`

### Method 3: Download Bootstrap Only

```bash
# Download just the bootstrap (no full clone)
curl -L https://github.com/Dexploarer/claudius-skills/archive/main.zip -o claudius.zip
unzip claudius.zip
cp -r claudius-skills-main/external-repo-bootstrap/.claude /path/to/your/project/
rm -rf claudius.zip claudius-skills-main

# Start Claude
cd /path/to/your/project
claude
```

Then say: **"/claudius-setup"** (will clone repo during setup)

### Method 4: Git Submodule (For Version Control)

```bash
# Add as git submodule
git submodule add https://github.com/Dexploarer/claudius-skills.git .claudius-skills

# Copy bootstrap
cp -r .claudius-skills/external-repo-bootstrap/.claude .

# Commit the submodule
git add .gitmodules .claudius-skills .claude
git commit -m "Add Claudius Skills bootstrap"
```

Benefits:
- Version controlled
- Easy to update: `git submodule update --remote`
- Team can sync exact versions

---

## 💡 How It Works

### Phase 1: Bootstrap Installation

You add a minimal `.claude` setup to your project:

```
your-project/
├── .claude/
│   ├── skills/
│   │   └── claudius-installer.md          # ~500 lines
│   ├── commands/
│   │   ├── claudius-setup.md              # Setup wizard
│   │   ├── claudius-update.md             # Update manager
│   │   └── claudius-info.md               # Installation info
│   └── subagents/
│       └── claudius-setup-agent.md        # Setup orchestrator
└── ... (your project files)
```

**Size:** ~4 files, ~2000 lines total (very lightweight)

### Phase 2: Activation

When you say **"setup claudius for my project"** or run `/claudius-setup`:

1. **claudius-installer skill** is triggered
2. **claudius-setup-agent** is spawned
3. Agent checks for repository at `~/.claudius-skills`
4. If not found, clones: `git clone https://github.com/Dexploarer/claudius-skills.git ~/.claudius-skills`
5. If found, updates: `cd ~/.claudius-skills && git pull`

### Phase 3: Project Analysis

The setup agent analyzes your project:

```typescript
interface ProjectAnalysis {
  // Project metadata
  rootPath: string;
  type: 'frontend' | 'backend' | 'fullstack' | 'mobile' | 'cli' | 'library';

  // Detected technologies
  frameworks: string[];        // ['React', 'Vite']
  languages: string[];          // ['TypeScript', 'JavaScript']
  packageManager: string;       // 'npm' | 'yarn' | 'pnpm'

  // Project characteristics
  hasTests: boolean;
  hasCI: boolean;
  hasDocker: boolean;
  complexity: 'starter' | 'intermediate' | 'advanced' | 'enterprise';

  // Existing configuration
  existingClaude: {
    hasConfig: boolean;
    skills: string[];
    commands: string[];
    agents: string[];
    hooks: string[];
  };

  // Recommendations
  recommendations: {
    kits: string[];             // ['intermediate-kit']
    skills: string[];            // ['react-component-generator', ...]
    commands: string[];          // ['/test', '/review', ...]
    agents: string[];            // ['code-reviewer', ...]
    hooks: string[];             // ['secret-scanning', ...]
  };
}
```

**Detection Logic:**

```typescript
// Frontend detection
if (packageJson.dependencies.react) {
  frameworks.push('React');
  recommendations.skills.push('react-component-generator');
}

// Backend detection
if (packageJson.dependencies.express) {
  frameworks.push('Express');
  recommendations.skills.push('express-api-generator');
}

// Testing detection
if (packageJson.devDependencies.vitest) {
  hasTests = true;
  recommendations.skills.push('test-helper');
}

// Complexity assessment
if (multipleServices || kubernetes || microservices) {
  complexity = 'enterprise';
  recommendations.kits.push('advanced-kit');
} else if (frameworks.length > 1 || production) {
  complexity = 'intermediate';
  recommendations.kits.push('intermediate-kit');
} else {
  complexity = 'starter';
  recommendations.kits.push('starter-kit');
}
```

### Phase 4: Recommendations

Agent presents recommendations:

```
📊 Project Analysis Complete

Detected:
- Type: Frontend SPA
- Framework: React 18.2 with TypeScript
- Build Tool: Vite 4.5
- Testing: Vitest + React Testing Library
- Complexity: Intermediate

📦 Recommended Kit: Intermediate Kit

This includes:
✓ 10 framework-specific skills
✓ 15 workflow commands
✓ 6 specialist agents
✓ Security & quality hooks

🎯 Specific Recommendations:

Skills:
  • react-component-generator - Modern React components
  • test-helper - Vitest test generation
  • version-checker - API compatibility verification
  • bundle-analyzer - Bundle size optimization

Commands:
  • /commit - Smart git commits
  • /test - Run tests with coverage
  • /review - Code review
  • /bundle-analyze - Bundle analysis

Agents:
  • code-reviewer - Expert code review
  • test-writer - Test generation specialist
  • performance-optimizer - Performance tuning

Hooks:
  • secret-scanning - Prevent secrets in commits
  • test-coverage-enforcement - 80% coverage minimum
  • build-size-alert - Monitor bundle size

Installation Options:
1. Install complete recommended kit ← Recommended
2. Custom selection (choose components)
3. Show detailed information
4. Cancel

What would you like to do? [1/2/3/4]
```

### Phase 5: Installation

User selects option 1 (complete kit):

```bash
# Agent copies components from ~/.claudius-skills to project

# Copy skills
cp ~/.claudius-skills/intermediate-kit/.claude/skills/react-component-generator.md \
   .claude/skills/

cp ~/.claudius-skills/intermediate-kit/.claude/skills/test-helper.md \
   .claude/skills/

# ... (all recommended skills)

# Copy commands
cp ~/.claudius-skills/intermediate-kit/.claude/commands/commit.md \
   .claude/commands/

# ... (all recommended commands)

# Copy agents
cp ~/.claudius-skills/intermediate-kit/.claude/subagents/code-reviewer.md \
   .claude/subagents/

# ... (all recommended agents)

# Copy hooks
cp ~/.claudius-skills/hooks-collection/security/secret-scanning/ \
   .claude/hooks/

# ... (all recommended hooks)

# Copy framework rules
cp ~/.claudius-skills/framework-rules/react.md \
   .claude/rules/frameworks/
```

### Phase 6: Manifest Creation

Agent creates `.claude/.claudius-manifest.json`:

```json
{
  "version": "1.0.0",
  "installedAt": "2025-11-05T10:30:00Z",
  "lastUpdated": "2025-11-05T10:30:00Z",
  "repositoryUrl": "https://github.com/Dexploarer/claudius-skills.git",
  "repositoryPath": "/home/user/.claudius-skills",
  "repositoryCommit": "f28b746abc123...",
  "components": {
    "kits": ["intermediate-kit"],
    "skills": [
      "react-component-generator",
      "test-helper",
      "version-checker",
      "bundle-analyzer",
      "api-documentation-generator"
    ],
    "commands": [
      "/commit",
      "/test",
      "/review",
      "/bundle-analyze",
      "/refactor"
    ],
    "agents": [
      "code-reviewer",
      "test-writer",
      "performance-optimizer"
    ],
    "hooks": [
      "secret-scanning",
      "test-coverage-enforcement",
      "build-size-alert",
      "prevent-force-push"
    ],
    "rules": [
      "frameworks/react.md",
      "workflows/testing.md"
    ]
  },
  "projectInfo": {
    "type": "frontend",
    "frameworks": ["React", "Vite"],
    "languages": ["TypeScript"],
    "complexity": "intermediate"
  },
  "customizations": []
}
```

### Phase 7: Verification & Completion

```
✅ Installation Complete! 🎉

Installed Components:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ 5 skills
✓ 5 commands
✓ 3 agents
✓ 4 hooks
✓ 2 rule files

Quick Start Guide:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Try these examples:

1. Generate a component:
   "create a Button component with TypeScript"

2. Write tests:
   "write tests for the Button component"

3. Run code review:
   /review

4. Check package version:
   "check version of react"

Security Enabled:
✓ Secret scanning active
✓ Test coverage enforced (80%)
✓ Build size monitoring
✓ Force push prevention

Documentation:
- Installation manifest: .claude/.claudius-manifest.json
- Local repository: ~/.claudius-skills/
- Online docs: https://github.com/Dexploarer/claudius-skills

Next Steps:
- Try the examples above
- Run /claudius-info to see full installation
- Run /claudius-update monthly for updates
```

---

## 🔄 Update Management

### Checking for Updates

```bash
/claudius-update
```

Process:
1. Fetches latest from GitHub
2. Compares with installed commit (from manifest)
3. Shows changelog
4. Offers update options

Example output:

```
🔄 Checking for Updates...

✓ Fetched latest from repository
✓ Read installation manifest

Current: f28b746 (2025-10-15)
Latest:  a1b2c3d (2025-11-05)

📋 Changelog:

2025-11-05 - Railway Deployment Kit
  + Added 5 Railway deployment skills
  + Added 6 deployment commands
  + Added 4 specialist agents

2025-11-02 - React 19 Support
  * Updated react-component-generator
  * Added Server Components support

2025-10-28 - Security Enhancements
  * 50+ new secret patterns
  * Improved detection accuracy

Updates Available:
✓ react-component-generator (no breaking changes)
✓ secret-scanning (recommended)
✓ version-checker (enhancement)

New Kits Available:
✓ Railway Deployment Kit

Update Options:
1. Update all components
2. Selective update
3. View detailed changes
4. Skip this update

What would you like to do? [1]
```

### Selective Updates

```bash
/claudius-update select
```

Interactive checklist:

```
Select components to update:

Skills:
[x] react-component-generator - React 19 support
[x] version-checker - Breaking change detection
[ ] bundle-analyzer - No changes

Commands:
[x] /test - Vitest browser mode
[ ] /commit - No changes
[ ] /review - No changes

Agents:
[x] code-reviewer - Enhanced security
[ ] test-writer - No changes

Hooks:
[x] secret-scanning - 50+ new patterns
[ ] test-coverage-enforcement - No changes

New Kits:
[ ] Railway Deployment Kit - Add to installation

Select all [a] | Update selected [u] | Cancel [c]: u

Updating 5 components...
✓ Complete
```

### Automatic Updates

Configure auto-update:

```json
{
  "claudius": {
    "autoUpdate": true,
    "updateCheckInterval": "7d",
    "autoUpdateTypes": ["hooks", "security"],
    "requireConfirmation": true
  }
}
```

---

## 🎯 Real-World Examples

### Example 1: React Frontend Developer

**Scenario:** Building a new React app with TypeScript

```bash
# Install bootstrap
curl -fsSL https://raw.githubusercontent.com/Dexploarer/claudius-skills/main/external-repo-bootstrap/install.sh | bash

# Start Claude
claude
```

**Interaction:**

```
User: "setup claudius"

Claude:
Analyzing your project...

✓ React 18.2 + TypeScript
✓ Vite build tool
✓ Vitest testing

Recommended: Intermediate Kit

Skills:
- react-component-generator
- test-helper
- bundle-analyzer
- version-checker

Commands:
- /test, /review, /commit
- /bundle-analyze

Agents:
- code-reviewer
- performance-optimizer

Install? [yes]

User: "yes"

Claude:
✅ Installation complete!

Try: "create a Button component"
```

**Result:**
- Complete React development setup
- Can generate components with proper TypeScript
- Testing integrated
- Performance monitoring
- Security hooks enabled

### Example 2: Django Backend Team

**Scenario:** Existing Django API, adding AI assistance

```bash
cd ~/my-django-api
cp -r ~/.claudius-skills/external-repo-bootstrap/.claude .
claude
```

```
User: "/claudius-setup"

Claude:
Analyzing...

✓ Django 4.2 + PostgreSQL
✓ pytest + coverage
✓ Existing .claude/ found (will merge)

Recommended additions:
- django-model-helper skill
- api-documentation-generator skill
- database-architect agent
- Security hooks

Install? [yes]
```

**Result:**
- Merged with existing config
- Django-specific capabilities added
- API documentation automation
- Database design consultation
- Security scanning

### Example 3: Enterprise Microservices

**Scenario:** Large-scale distributed system

```bash
cd ~/enterprise-platform
/claudius-setup
```

```
Claude:
Analyzing...

✓ Multiple services (12)
✓ Kubernetes + Terraform
✓ Full CI/CD pipeline
✓ Compliance requirements

Recommended: Advanced Kit (Enterprise)

Includes:
- 15 enterprise skills
- 20 advanced commands
- 10 specialist consultants
- Full compliance automation

This is a comprehensive installation.
Review details? [yes/no/install]

User: "install"

Claude:
Installing Advanced Kit...
✅ Complete

Enterprise features available:
- /compliance-scan soc2
- /canary-deploy
- /incident-declare
- Use enterprise-architect for design
```

**Result:**
- Complete enterprise toolkit
- Compliance automation
- Advanced deployment strategies
- Specialist consultants
- Full observability

### Example 4: ElizaOS Developer

**Scenario:** Building AI agents with ElizaOS

```bash
cd ~/my-eliza-agent
curl -fsSL https://raw.githubusercontent.com/Dexploarer/claudius-skills/main/external-repo-bootstrap/install.sh | bash
claude
```

```
User: "setup claudius for elizaos"

Claude:
Detected ElizaOS project!

✓ @ai16z/eliza dependency
✓ characters/ directory
✓ ElizaOS configuration

Recommended: Eliza OS Kit

Skills:
- character-generator
- plugin-builder
- knowledge-base-builder
- memory-manager

Commands:
- /dev-agent
- /test-character
- /deploy-agent
- /build-plugin

Agents:
- character-designer
- plugin-architect
- integration-specialist

Install? [yes]

User: "yes"

Claude:
✅ ElizaOS Kit installed!

Try: "create a trader character"
Or: /dev-agent "start development"
```

**Result:**
- Complete ElizaOS development environment
- Character generation and testing
- Plugin scaffolding
- Deployment automation
- Specialist consultants

---

## 🔧 Configuration Options

### Repository Location

Default: `~/.claudius-skills`

Change via:

```bash
"set claudius repository path to /custom/path"
```

Or create `.claudius-config.json`:

```json
{
  "repositoryPath": "/custom/path/to/claudius-skills",
  "repositoryUrl": "https://github.com/Dexploarer/claudius-skills.git"
}
```

### Using a Fork

```bash
"set claudius repository to https://github.com/my-org/custom-skills.git"
/claudius-setup
```

Benefits:
- Custom skills and modifications
- Private components
- Company-specific configurations
- Still get upstream updates

### Update Frequency

```json
{
  "claudius": {
    "updateCheckInterval": "7d",    // Check weekly
    "autoUpdate": false,             // Manual updates only
    "requireConfirmation": true      // Always ask
  }
}
```

---

## 🛡️ Security

### Repository Verification

Always verify you're using the official repository:

```bash
cd ~/.claudius-skills
git remote -v

# Should show:
# origin  https://github.com/Dexploarer/claudius-skills.git (fetch)
# origin  https://github.com/Dexploarer/claudius-skills.git (push)
```

### Component Review

Before installing:
- Use `/claudius-setup dry-run` to see recommendations
- Review skill/command descriptions
- Check hooks for side effects
- Inspect code if needed

### Automatic Security

Bootstrap includes security by default:
- ✅ Secret scanning before commits
- ✅ Force push prevention
- ✅ Environment file protection
- ✅ Dependency vulnerability scanning

### Permission Model

Bootstrap files are read-only after installation:

```bash
chmod 644 .claude/**/*
```

Claude can read configurations but won't modify them without explicit user requests.

---

## 🐛 Troubleshooting

### Issue: Clone Fails

**Error:** `Failed to clone repository`

**Solutions:**
```bash
# Check git
git --version

# Check connectivity
ping github.com

# Try SSH instead
git clone git@github.com:Dexploarer/claudius-skills.git ~/.claudius-skills

# Check firewall/proxy
```

### Issue: Permission Denied

**Error:** `Permission denied writing to .claude/`

**Solutions:**
```bash
# Fix ownership
sudo chown -R $USER .claude/

# Fix permissions
chmod -R u+w .claude/
```

### Issue: Components Not Loading

**Error:** `Skill not found`

**Solutions:**
```bash
# Verify installation
ls -R .claude/

# Check manifest
cat .claude/.claudius-manifest.json

# Reinstall
/claudius-setup --force
```

### Issue: Update Conflicts

**Error:** `Conflict during update`

**Solutions:**
```bash
# Backup first
cp -r .claude .claude.backup

# Try update again
/claudius-update

# Or rollback
"rollback claudius to previous version"
```

---

## 📚 Documentation

### Quick Reference

| Command | Description |
|---------|-------------|
| `/claudius-setup` | Interactive setup wizard |
| `/claudius-setup auto` | Auto-install recommended |
| `/claudius-update` | Check and install updates |
| `/claudius-info` | Show installation info |
| `"setup claudius"` | Activate installer skill |

### Full Documentation

After installation:
- **Bootstrap guide:** `external-repo-bootstrap/README.md`
- **Main repository:** `~/.claudius-skills/README.md`
- **Project rules:** `~/.claudius-skills/CLAUDE.md`
- **Implementation:** `~/.claudius-skills/IMPLEMENTATION_PROGRESS.md`

### Online Resources

- **Repository:** https://github.com/Dexploarer/claudius-skills
- **Issues:** https://github.com/Dexploarer/claudius-skills/issues
- **Discussions:** https://github.com/Dexploarer/claudius-skills/discussions
- **Wiki:** https://github.com/Dexploarer/claudius-skills/wiki

---

## 🤝 Contributing

### Share Your Experience

- Report issues: GitHub Issues
- Share use cases: GitHub Discussions
- Suggest improvements: Pull Requests
- Write guides: Documentation PRs

### Contribute Components

Fork the repository and add:
- New skills for frameworks
- Useful commands
- Specialist agents
- Hook patterns

Submit PR to benefit everyone!

---

## 📊 Statistics

### Bootstrap Size
- **Files:** 4 core files
- **Size:** ~2000 lines (~100KB)
- **Installation time:** < 5 seconds

### Full Repository
- **Skills:** 87 across 8 kits
- **Commands:** 86
- **Agents:** 50
- **Hooks:** 36
- **Frameworks:** 17
- **Size:** ~50MB (with git history)

### After Installation
- **Typical intermediate setup:** 20-30 files
- **Advanced enterprise:** 50-70 files
- **Disk usage:** 1-2MB of markdown

---

## 🎓 Best Practices

### 1. Start Clean
- Use bootstrap on new projects
- Or back up existing `.claude/` first

### 2. Follow Recommendations
- Agent knows the repo structure
- Trust the analysis
- Customize later if needed

### 3. Keep Updated
- Monthly: `/claudius-update`
- Review changelog
- Test in dev branch

### 4. Document Customizations
- Note changes in manifest
- Keep list of modifications
- Share useful patterns

### 5. Security First
- Always enable security hooks
- Review components before install
- Keep dependencies updated

---

## 🚀 Next Steps

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
   ```bash
   # Generate components
   "create a User component"

   # Run commands
   /test
   /review
   ```

4. **Stay Updated**
   ```bash
   # Monthly
   /claudius-update
   ```

---

**Version:** 1.0.0
**Last Updated:** 2025-11-05
**Repository:** https://github.com/Dexploarer/claudius-skills
**Author:** Claudius Skills Project Team

---

## Quick Start Command

```bash
# One command to rule them all
curl -fsSL https://raw.githubusercontent.com/Dexploarer/claudius-skills/main/external-repo-bootstrap/install.sh | bash && claude
```

🎉 **That's it! You now have full access to Claudius Skills from any repository!**
