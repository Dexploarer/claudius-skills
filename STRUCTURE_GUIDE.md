# Claudius Skills - Structure Guide

> Understanding the organizational patterns and file formats in this repository

**Last Updated:** 2025-11-02

---

## 📖 Overview

This guide explains how the Claudius Skills repository is organized, why different formats exist, and how to navigate between them effectively. If you're confused about where to find things or why there are multiple organizational patterns, this is your reference.

---

## 🗺️ Repository Organization Hierarchy

```
claudius-skills/
│
├── 📦 PRODUCTION KITS (Ready to use)
│   ├── Core Kits (3)
│   │   ├── starter-kit/
│   │   ├── intermediate-kit/
│   │   └── advanced-kit/
│   │
│   └── Specialized Kits (3)
│       ├── productivity-skills/
│       ├── competitive-ai-frameworks/
│       └── eliza-os-kit/
│
├── 📚 EXAMPLES (Learning resources)
│   ├── beginner/
│   ├── intermediate/
│   ├── advanced/
│   └── master/
│
├── 🔧 UTILITIES & RESOURCES
│   ├── framework-rules/
│   ├── hooks-collection/
│   ├── modern-commands/
│   ├── specialized-agents/
│   ├── templates/
│   └── resources/
│
└── 🎓 EDUCATIONAL CONTENT
    ├── skool/
    └── skool-courses/
```

---

## 🎯 Three Main Categories

### 1. Production Kits
**Purpose:** Complete, ready-to-use configurations you can copy directly to your project
**Structure:** Standard `.claude/` directory format
**Use When:** You want a full working setup for your project

### 2. Examples
**Purpose:** Learning resources and reference implementations
**Structure:** Mix of `.claude/` format and standalone `SKILL.md` files
**Use When:** Learning patterns or finding specific implementation examples

### 3. Utilities & Resources
**Purpose:** Reusable components, templates, and reference materials
**Structure:** Varies by utility type
**Use When:** Customizing your setup or building your own configurations

---

## 📁 Directory Format Patterns

### Pattern 1: Standard .claude Directory (Production Kits)

**Used In:** All production kits (starter, intermediate, advanced, productivity, competitive-ai, eliza-os)

```
kit-name/
└── .claude/
    ├── skills/
    │   ├── skill-1.md
    │   ├── skill-2.md
    │   └── skill-n.md
    ├── commands/
    │   ├── command-1.md
    │   ├── command-2.md
    │   └── command-n.md
    ├── agents/ (or subagents/)
    │   ├── agent-1.md
    │   ├── agent-2.md
    │   └── agent-n.md
    ├── hooks/
    │   ├── hook-1.json
    │   └── hook-n.json
    └── rules/
        ├── CLAUDE.md
        └── *.md
```

**How to Use:**
```bash
# Copy entire kit to your project
cp -r kit-name/.claude /path/to/your/project/

# Or copy specific components
cp kit-name/.claude/skills/skill-1.md /path/to/your/project/.claude/skills/
```

**Characteristics:**
- ✅ Production-ready
- ✅ Complete configurations
- ✅ Works out of the box
- ✅ Includes rules and documentation

---

### Pattern 2: Example with SKILL.md Format

**Used In:** `examples/beginner/` and `examples/intermediate/`

```
examples/intermediate/
└── category-skills/
    ├── skill-name-1/
    │   └── SKILL.md
    ├── skill-name-2/
    │   └── SKILL.md
    └── skill-name-n/
        └── SKILL.md
```

**How to Use:**
```bash
# Create .claude/skills directory if it doesn't exist
mkdir -p /path/to/your/project/.claude/skills/

# Copy and rename SKILL.md to skill-name.md
cp examples/intermediate/performance-skills/bundle-analyzer/SKILL.md \
   /path/to/your/project/.claude/skills/bundle-analyzer.md
```

**Characteristics:**
- 📚 Learning-focused
- 📝 Includes detailed documentation
- 🔍 Easy to browse individual examples
- ⚠️ Requires manual setup

---

### Pattern 3: Example with .claude Directory

**Used In:** `examples/advanced/emerging-tech-skills/`

```
examples/advanced/emerging-tech-skills/
└── skill-name/
    └── .claude/
        └── skills/
            └── skill-name.md
```

**How to Use:**
```bash
# Copy individual skill
cp examples/advanced/emerging-tech-skills/ai-ml-ops/.claude/skills/ai-ml-ops.md \
   /path/to/your/project/.claude/skills/

# Or copy entire .claude directory
cp -r examples/advanced/emerging-tech-skills/ai-ml-ops/.claude/* \
   /path/to/your/project/.claude/
```

**Characteristics:**
- 🚀 Production-ready format
- 📚 Still educational
- ✅ Drop-in compatible
- 🎯 Advanced use cases

---

### Pattern 4: Standalone Collections

**Used In:** `hooks-collection/`, `modern-commands/`, `specialized-agents/`, `framework-rules/`

```
collection-name/
├── category-1/
│   ├── item-1.json (or .md)
│   └── item-n.json (or .md)
├── category-2/
│   └── ...
└── README.md
```

**How to Use:**
```bash
# Copy entire category
cp collection-name/category-1/* /path/to/your/project/.claude/hooks/

# Or copy individual items
cp collection-name/category-1/item-1.json /path/to/your/project/.claude/hooks/
```

**Characteristics:**
- 🧩 Modular components
- 🔧 Mix and match
- 📖 Documented collections
- 🎨 Customization-friendly

---

## 🎓 Learning Path by Directory

### Level 1: Beginner → Start Here
```
starter-kit/                       # Copy this first
└── .claude/                       # Complete beginner setup

examples/beginner/                 # Browse these to learn
└── simple-skills/                 # Individual skill examples
    └── */SKILL.md
```

### Level 2: Intermediate → Production Projects
```
intermediate-kit/                  # Copy for production apps
└── .claude/                       # Framework-specific skills

examples/intermediate/             # Reference implementations
└── framework-skills/              # Framework examples
    └── */SKILL.md
```

### Level 3: Advanced → Complex Systems
```
advanced-kit/                      # Enterprise configurations
└── .claude/                       # Microservices, compliance

examples/advanced/                 # Advanced patterns
└── emerging-tech-skills/          # Cutting-edge tech
    └── */.claude/skills/
```

### Level 4: Master → Custom Frameworks
```
examples/master/                   # Master-level patterns
└── .claude/rules/                 # Advanced rules

templates/                         # Build your own
└── *-template.md                  # Templates for everything
```

---

## 🔍 Finding What You Need

### "I want a complete working setup"
→ Use **Production Kits** (Pattern 1)
- `starter-kit/.claude/`
- `intermediate-kit/.claude/`
- `advanced-kit/.claude/`
- `productivity-skills/starter-kit/.claude/`
- `competitive-ai-frameworks/.claude/`
- `eliza-os-kit/.claude/`

### "I want to learn how a specific skill works"
→ Browse **Examples** (Pattern 2 or 3)
- `examples/beginner/simple-skills/*/SKILL.md`
- `examples/intermediate/*/SKILL.md`
- `examples/advanced/emerging-tech-skills/*/.claude/skills/`

### "I want specific hooks/commands/agents"
→ Use **Standalone Collections** (Pattern 4)
- `hooks-collection/*/`
- `modern-commands/*/`
- `specialized-agents/`
- `framework-rules/`

### "I want to build my own configuration"
→ Use **Templates**
- `templates/skill-template.md`
- `templates/command-template.md`
- `templates/subagent-template.md`
- `templates/hooks/`

---

## 🎯 Kit Selection Guide

### Choose Starter Kit If:
- ✅ New to Claude Code
- ✅ Learning AI-assisted development
- ✅ Building simple projects
- ✅ Want basic automation

### Choose Intermediate Kit If:
- ✅ Building production applications
- ✅ Using frameworks (React, Vue, Django, etc.)
- ✅ Need advanced automation
- ✅ Implementing CI/CD

### Choose Advanced Kit If:
- ✅ Building enterprise systems
- ✅ Need compliance (SOC2, HIPAA, etc.)
- ✅ Implementing microservices
- ✅ Require full observability

### Choose Productivity Skills If:
- ✅ Managing meetings and docs
- ✅ Writing professional content
- ✅ Planning projects
- ✅ Improving personal workflows

### Choose Competitive AI Frameworks If:
- ✅ Coding competitions
- ✅ Bug hunting challenges
- ✅ Team-based development
- ✅ Competitive testing

### Choose Eliza OS Kit If:
- ✅ Building ElizaOS agents
- ✅ Creating AI characters
- ✅ Developing ElizaOS plugins
- ✅ Managing agent memory

---

## 📝 File Naming Conventions

### Skills
- **In Kits:** `skill-name.md` (e.g., `react-component-generator.md`)
- **In Examples:** `SKILL.md` (uppercase, in subdirectory named after skill)

### Commands
- **In Kits:** `command-name.md` (e.g., `deploy.md`)
- **Modern Commands:** `command-name.md` in domain subdirectory

### Agents
- **In Kits:** `agent-name.md` (e.g., `code-reviewer.md`)
- **Specialized:** `agent-name.md` at root level

### Hooks
- **All Locations:** `hook-name.json` (e.g., `prevent-force-push.json`)

### Framework Rules
- **All Locations:** `framework-name.md` (e.g., `react.md`)

---

## 🔄 Migration Patterns

### From SKILL.md to .claude/skills/

```bash
# If you have SKILL.md format
cp examples/intermediate/category/skill-name/SKILL.md \
   your-project/.claude/skills/skill-name.md
```

### Combining Multiple Kits

```bash
# Copy base kit
cp -r starter-kit/.claude your-project/

# Add specific skills from other kits
cp intermediate-kit/.claude/skills/react-component-generator.md \
   your-project/.claude/skills/

# Add hooks
cp hooks-collection/development-safety/* your-project/.claude/hooks/
```

### Custom Kit Assembly

```bash
# Start with structure
mkdir -p your-kit/.claude/{skills,commands,agents,hooks,rules}

# Cherry-pick from different sources
cp starter-kit/.claude/skills/readme-generator.md your-kit/.claude/skills/
cp intermediate-kit/.claude/commands/deploy.md your-kit/.claude/commands/
cp advanced-kit/.claude/agents/sre-consultant.md your-kit/.claude/agents/
cp hooks-collection/security-enforcement/*.json your-kit/.claude/hooks/
```

---

## 🏗️ Directory Purposes Explained

### Core Kits (starter, intermediate, advanced)
**Purpose:** Progressive learning path from beginner to enterprise
**Structure:** Complete `.claude/` directories
**Documentation:** Each has `/.claude/rules/CLAUDE.md`

### Specialized Kits (productivity, competitive-ai, eliza-os)
**Purpose:** Domain-specific complete solutions
**Structure:** Complete `.claude/` directories
**Documentation:** Full rules and guides included

### examples/
**Purpose:** Learning resources and reference implementations
**Structure:** Mixed formats for educational clarity
**Documentation:** Individual READMEs and comments

### framework-rules/
**Purpose:** Framework-specific guidance for modern web frameworks
**Structure:** Individual `.md` rule files
**Documentation:** Each rule file is self-documenting

### hooks-collection/
**Purpose:** Production-ready event-driven automation
**Structure:** JSON files organized by category
**Documentation:** Comprehensive README with usage examples

### modern-commands/
**Purpose:** Modern workflow commands for cutting-edge practices
**Structure:** Markdown files in domain directories
**Documentation:** Per-domain organization

### specialized-agents/
**Purpose:** Expert consultants for advanced topics
**Structure:** Individual `.md` agent files
**Documentation:** Self-contained in each file

### templates/
**Purpose:** Starting points for creating your own configurations
**Structure:** Template files with placeholders
**Documentation:** Instructions within each template

### resources/
**Purpose:** Guides, tutorials, and best practices
**Structure:** Markdown documentation
**Documentation:** Comprehensive guides

### skool/ & skool-courses/
**Purpose:** Educational content and structured curriculum
**Structure:** Course-based organization
**Documentation:** Lesson plans and learning materials

---

## 🎨 Customization Strategies

### Strategy 1: Start with a Kit
```bash
# Copy base kit
cp -r starter-kit/.claude my-project/

# Customize by adding/removing
# Edit .claude/skills/*.md to modify behaviors
```

### Strategy 2: Build from Examples
```bash
# Create structure
mkdir -p my-project/.claude/{skills,commands,agents}

# Copy cherry-picked examples
cp examples/intermediate/*/SKILL.md my-project/.claude/skills/
# Rename SKILL.md files to match skill names
```

### Strategy 3: Use Templates
```bash
# Copy template
cp templates/skill-template.md my-project/.claude/skills/my-skill.md

# Edit template placeholders
# Customize to your needs
```

### Strategy 4: Hybrid Approach
```bash
# Start with kit
cp -r intermediate-kit/.claude my-project/

# Add specific examples
cp examples/advanced/emerging-tech-skills/ai-ml-ops/.claude/skills/* \
   my-project/.claude/skills/

# Add hooks
cp hooks-collection/security-enforcement/* my-project/.claude/hooks/

# Add framework rules
cp framework-rules/astro.md my-project/.claude/rules/frameworks/
```

---

## 🔗 Cross-References

### Documentation Files
- **Main Guide:** [README.md](README.md) - Quick start and overview
- **Project Rules:** [CLAUDE.md](CLAUDE.md) - Architecture and design decisions
- **Complete Index:** [INVENTORY.md](INVENTORY.md) - Every configuration item
- **Implementation:** [IMPLEMENTATION_PROGRESS.md](IMPLEMENTATION_PROGRESS.md) - Development tracking

### Kit Documentation
- **Starter Kit:** `starter-kit/.claude/rules/CLAUDE.md`
- **Intermediate Kit:** `intermediate-kit/.claude/rules/CLAUDE.md`
- **Advanced Kit:** `advanced-kit/.claude/rules/CLAUDE.md`
- **Productivity Skills:** `productivity-skills/starter-kit/README.md`
- **Competitive AI:** `competitive-ai-frameworks/.claude/rules/CLAUDE.md`
- **Eliza OS Kit:** `eliza-os-kit/.claude/rules/CLAUDE.md`

### Collection Documentation
- **Hooks Guide:** [hooks-collection/README.md](hooks-collection/README.md)
- **Modern Commands:** `modern-commands/EXPANSION_README.md`

---

## 🚀 Quick Start Flowchart

```
START
  ↓
Are you new to Claude Code?
  ↓                    ↓
YES                   NO
  ↓                    ↓
Use starter-kit    What are you building?
  ↓                    ↓
            ┌──────────┼──────────┬──────────┐
            ↓          ↓          ↓          ↓
         Web App   Enterprise  ElizaOS   Something
            ↓          ↓        Agent     Else
    intermediate   advanced   eliza-os    ↓
         -kit        -kit        -kit   Browse
            ↓          ↓          ↓     examples/
            └──────────┴──────────┴──────┘
                       ↓
              Customize with:
            - examples/
            - hooks-collection/
            - modern-commands/
            - framework-rules/
                       ↓
                     DONE
```

---

## 💡 Pro Tips

### Tip 1: Version Control Your .claude Directory
```bash
# Add .claude to git
git add .claude/
git commit -m "Add Claude Code configurations"

# Team shares the same setup
```

### Tip 2: Combine Kits Strategically
```bash
# Use starter as base
cp -r starter-kit/.claude project/.claude/

# Add intermediate skills selectively
cp intermediate-kit/.claude/skills/react-component-generator.md \
   project/.claude/skills/
```

### Tip 3: Customize Gradually
Start with a kit → Use for a while → Add what you need → Remove what you don't

### Tip 4: Use Hooks Sparingly
Start with 2-3 critical hooks, add more as needed. Don't overwhelm yourself.

### Tip 5: Framework Rules Are Optional
Only add framework rules if you're primarily working in that framework.

### Tip 6: Check INVENTORY.md for Discovery
Use [INVENTORY.md](INVENTORY.md) to search for specific capabilities across all kits.

---

## 🆘 Troubleshooting

### "I can't find X skill/command/agent"
→ Check [INVENTORY.md](INVENTORY.md) for complete listing with file paths

### "Should I use SKILL.md or .claude/skills/ format?"
→ Always rename `SKILL.md` to `skill-name.md` when copying to your `.claude/skills/` directory

### "Which kit should I start with?"
→ Use the "Kit Selection Guide" section above or the flowchart

### "Can I mix kits?"
→ Yes! See "Combining Multiple Kits" section

### "Where do I put custom skills?"
→ In your project's `.claude/skills/` directory, follow naming conventions

### "Do I need all the hooks?"
→ No, start with 2-3 critical ones (see hooks-collection/README.md)

---

## 📚 Additional Resources

- **Official Claude Code Docs:** https://docs.claude.com/en/docs/claude-code/
- **Skills Documentation:** https://docs.claude.com/en/docs/claude-code/skills
- **Hooks Documentation:** https://docs.claude.com/en/docs/claude-code/hooks
- **MCP Documentation:** https://modelcontextprotocol.io/

---

## 🎯 Summary

**Key Takeaways:**
1. **Production Kits** = Copy and go
2. **Examples** = Learn and customize
3. **Utilities** = Mix and match
4. **Always use** `.claude/` directory structure in your project
5. **Rename** `SKILL.md` → `skill-name.md` when copying examples
6. **Start small**, customize gradually
7. **Check INVENTORY.md** to find anything

---

**Questions?** Open an issue or check the main [README.md](README.md)

---

**Last Updated:** 2025-11-02
**Maintainer:** Claudius Skills Project Team
