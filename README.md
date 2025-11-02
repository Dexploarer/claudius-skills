# Claudius Skills

> My personal collection of Claude Code configurations - from beginner experiments to advanced setups

<div align="center">

[![Skills](https://img.shields.io/badge/Skills-55-orange)]()
[![Commands](https://img.shields.io/badge/Commands-80+-purple)]()
[![Hooks](https://img.shields.io/badge/Hooks-25-blue)]()
[![Agents](https://img.shields.io/badge/Agents-46-red)]()
[![Frameworks](https://img.shields.io/badge/Frameworks-17-yellow)]()
[![Status](https://img.shields.io/badge/Status-100%25%20Complete-brightgreen)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

[Quick Start](#-quick-start) • [What's Inside](#-whats-inside) • [Examples](#-examples)

</div>

---

## 📖 What This Is

This is my personal playground for **Claude Code extensibility**. I've built configurations across all five pillars:

| Pillar | What It Does |
|--------|-------------|
| **Skills** | Automatically activate based on what you're doing |
| **Slash Commands** | Manual shortcuts you invoke with `/command` |
| **Hooks** | React to events (before/after file edits, etc.) |
| **Agents** | Specialized AI assistants with focused expertise |
| **MCP Servers** | Connect to external tools and services |

Feel free to use what's here, but I built this for me. If it helps you too, cool.

---

## 🎯 What's Inside

### 📦 Core Development Kits

#### **Starter Kit**
Basic configs for learning.

- **5 Skills**: README generation, code explanation, bug finding, testing, git help
- **12 Commands**: `/explain`, `/test`, `/commit`, `/review`, `/refactor`, `/docs`, `/debug`, `/quickfix`, `/setup`, `/todo`, `/clean`, `/deps`
- **4 Agents**: Code reviewer, test writer, doc writer, debug helper

Copy the `.claude/` folder to your project and go.

#### **Intermediate Kit**
Framework-specific stuff.

- **10 Skills**: React, Vue, Next.js, Django, FastAPI, Express, GraphQL, OpenAPI, database migrations, testing frameworks
- **15 Commands**: `/api-docs-generate`, `/bundle-analyze`, `/changelog-update`, `/coverage-report`, `/db-backup`, `/deploy`, `/dependency-update`, `/docker-build`, `/env-setup`, `/health-check`, `/migration-create`, `/performance-profile`, `/pr-creator`, `/security-audit`, `/version-bump`
- **6 Agents**: API designer, database architect, DevOps engineer, performance optimizer, security auditor, system architect

For when you're actually building something.

#### **Advanced Kit**
Enterprise/distributed systems configurations.

- **15 Skills**: Microservices orchestration, compliance automation, observability, platform engineering, disaster recovery, etc.
- **20 Commands**: Release orchestration, canary/blue-green deploys, incident management, compliance scanning, cost analysis, runbook execution, and more
- **10 Agents**: Enterprise architect, distributed systems architect, data architect, platform engineer, SRE consultant, incident commander, chaos engineer, FinOps analyst, compliance officer, security architect

For complex systems and compliance requirements.

### 📦 Specialized Kits

#### **Productivity Skills Kit**
Personal and team productivity workflows.

- **6 Skills**: Brainstorming, email composition, meeting notes, reports, task breakdown, strategic planning
- **13 Commands**: `/agenda`, `/decision`, `/email`, `/journal`, `/minutes`, `/presentation`, `/prioritize`, `/schedule`, and more
- **4 Agents**: Content writer, creative consultant, productivity coach, project coordinator

#### **Competitive AI Frameworks Kit** 🆕
AI-powered code competitions and testing.

- **3 Skills**: Bug hunting simulator, code quality analyzer, user flow tester
- **3 Commands**: `/run-bug-hunt`, `/run-flow-test`, `/run-quality-check`
- **12 Team Agents**: Organized into 3 teams with specialized roles (coordinator, tester, reviewer, documenter)

For competitive programming and team-based challenges.

#### **Eliza OS Kit** 🆕
Complete ElizaOS agent and character development toolkit.

- **6 Skills**: Character generation, deployment, knowledge base management, memory optimization, plugin building, testing
- **8 Commands**: `/dev-agent`, `/build-plugin`, `/deploy-agent`, `/test-character`, `/analyze-conversations`, and more
- **6 Specialist Agents**: Character designer, deployment engineer, integration specialist, memory architect, plugin architect, testing specialist

For building AI agents with the ElizaOS framework.

---

## 🚀 Quick Start

```bash
# Clone this repo
git clone https://github.com/Dexploarer/claudius-skills.git
cd claudius-skills

# Pick a kit and copy to your project
cp -r starter-kit/.claude /path/to/your/project/                    # Start here
cp -r intermediate-kit/.claude /path/to/your/project/               # Production apps
cp -r advanced-kit/.claude /path/to/your/project/                   # Enterprise
cp -r productivity-skills/starter-kit/.claude /path/to/your/project/ # Productivity
cp -r competitive-ai-frameworks/.claude /path/to/your/project/      # Competitions
cp -r eliza-os-kit/.claude /path/to/your/project/                   # ElizaOS agents

# Go use Claude Code
cd /path/to/your/project
claude
```

That's it. Skills activate automatically. Commands are `/command-name`. Agents are available when you need them.

### Examples

Check `examples/` for specific use cases:
- `examples/beginner/` - Simple examples to learn from
- `examples/intermediate/` - Framework-specific configs (React, Django, etc.)
- `examples/advanced/` - Complex setups (microservices, compliance, observability)

---

## 📚 Repository Structure

```
claudius-skills/
├── starter-kit/                  # 5 skills, 12 commands, 4 agents
├── intermediate-kit/             # 10 skills, 15 commands, 6 agents
├── advanced-kit/                 # 15 skills, 20 commands, 10 agents
├── productivity-skills/          # 6 skills, 13 commands, 4 agents
├── competitive-ai-frameworks/    # 3 skills, 3 commands, 12 agents 🆕
├── eliza-os-kit/                # 6 skills, 8 commands, 6 agents 🆕
├── examples/                     # Lots of specific examples
│   ├── beginner/                # Learning-focused examples
│   ├── intermediate/            # Production patterns
│   ├── advanced/                # Emerging tech & complex setups
│   └── master/                  # Master-level patterns
├── framework-rules/             # 8 modern framework rules (Angular, Astro, etc.)
├── hooks-collection/            # 25 production hooks (5 categories)
├── modern-commands/             # 10 modern workflow commands
├── specialized-agents/          # 4 specialized consultant agents
├── skool/                       # Educational content & tutorials
├── skool-courses/               # Structured course curriculum
├── templates/                   # Templates for making your own
└── resources/                   # Guides and docs
```

---

## 💡 What's Actually Here

### The Kits
Each kit (starter/intermediate/advanced) has its own `.claude/` directory with:
- Skills that auto-activate
- Commands you can call with `/command-name`
- Agents for specialized help
- Rules and configurations

### Plus Examples
The `examples/` directory has 25+ specialized skills organized by category:
- Performance: image optimization, bundle analysis, Lighthouse CI, query optimization
- Security: header generation, dependency scanning, PII detection, WCAG compliance
- Testing: mock generation, property-based testing, visual regression
- DevOps: Dockerfiles, GitHub Actions, Kubernetes, Terraform
- i18n: translation extraction, i18n setup
- Mobile: app icons, React Native components
- Data Science: Jupyter assistance, data cleaning
- Web3: smart contract generation
- 3D Graphics: Three.js scenes
- And more...

### And Templates
The `templates/` directory has templates for creating your own skills, commands, agents, and hooks.

---

## 📚 Resources

**Official Docs:**
- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**In This Repo:**
- `resources/guides/getting-started.md` - Start here if you're new
- `resources/guides/best-practices.md` - Useful patterns
- `resources/guides/security.md` - Security considerations
- `templates/` - Templates for making your own stuff

---

## 📜 License

MIT License. Use it however you want. See [LICENSE](LICENSE) for details.

---

**Built with Claude Code** • [Report Issues](https://github.com/Dexploarer/claudius-skills/issues)
