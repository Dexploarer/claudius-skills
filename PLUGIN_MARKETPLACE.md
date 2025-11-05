# Claudius Skills Plugin Marketplace

> Install any Claudius Skills kit as a Claude Code plugin with one command

## Quick Start

### Install the Marketplace

```bash
/plugin marketplace add Dexploarer/claudius-skills
```

### Browse Available Plugins

```bash
/plugin
```

### Install a Plugin

```bash
/plugin install starter-kit
/plugin install intermediate-kit
/plugin install advanced-kit
```

## Available Plugins

### 🟢 Beginner Kits

#### Starter Kit
**Best for:** Learning Claude Code, simple projects

```bash
/plugin install starter-kit
```

**Includes:**
- 5 essential skills (README generation, code explanation, bug finding, testing, git helper)
- 12 core commands (`/explain`, `/test`, `/commit`, `/review`, `/refactor`)
- 4 generalist agents (code reviewer, test writer, doc writer, debugger)

---

### 🟡 Intermediate Kits

#### Intermediate Kit
**Best for:** Production applications, modern frameworks

```bash
/plugin install intermediate-kit
```

**Includes:**
- 10 framework skills (React, Vue, Next.js, Django, FastAPI, Express, GraphQL)
- 15 production commands (`/deploy`, `/docker-build`, `/api-docs-generate`)
- 6 specialist agents (API designer, database architect, DevOps engineer)

---

### 🔴 Advanced Kits

#### Advanced Kit
**Best for:** Enterprise systems, compliance, observability

```bash
/plugin install advanced-kit
```

**Includes:**
- 15 enterprise skills (microservices, compliance automation, distributed tracing)
- 20 advanced commands (`/canary-deploy`, `/compliance-scan`, `/incident-declare`)
- 10 enterprise consultants (architects, SRE, compliance officer, security architect)

---

### 💼 Productivity Kits

#### Productivity Starter Kit
**Best for:** Personal and team productivity

```bash
/plugin install productivity-starter
```

**Includes:**
- 5 productivity skills (brainstorming, email, meeting notes, reports)
- 13 commands (`/agenda`, `/email`, `/minutes`, `/summarize`)
- 4 productivity agents

#### Productivity Intermediate Kit
**Best for:** Professional presentations

```bash
/plugin install productivity-intermediate
```

**Includes:**
- 1 advanced presentation generation skill

---

### 🎯 Specialized Kits

#### Competitive AI Frameworks
**Best for:** AI competitions and code challenges

```bash
/plugin install competitive-ai
```

**Includes:**
- 3 competition skills (bug hunting, quality analysis, flow testing)
- 3 commands (`/run-bug-hunt`, `/run-flow-test`, `/run-quality-check`)
- 12 team agents (3 teams with specialized roles)

#### Eliza OS Development Kit
**Best for:** Building AI agents with ElizaOS

```bash
/plugin install eliza-os-kit
```

**Includes:**
- 6 ElizaOS skills (character generation, deployment, knowledge base, memory, plugins)
- 8 commands (`/dev-agent`, `/build-plugin`, `/deploy-agent`)
- 6 specialist agents

#### Railway Deployment Kit
**Best for:** Railway.app deployment automation

```bash
/plugin install railway-deployment
```

**Includes:**
- 5 Railway deployment skills
- Configuration and environment management
- Database setup and monitoring

---

### 🔧 Enhancement Kits

#### Production Hooks Collection
**Best for:** Event-driven automation and safety

```bash
/plugin install hooks-collection
```

**Includes:**
- 36 production hooks across 7 categories
- Development safety, deployment, code quality
- Security enforcement, performance monitoring

#### Framework Integration Rules
**Best for:** Framework-specific best practices

```bash
/plugin install framework-rules
```

**Includes:**
- 17 framework configurations (React, Vue, Next.js, Django, etc.)
- Framework-specific patterns and conventions

---

## Using the Marketplace

### Installation Methods

#### Method 1: Via Marketplace (Recommended)
```bash
# Add marketplace
/plugin marketplace add Dexploarer/claudius-skills

# Browse plugins
/plugin

# Install specific plugin
/plugin install starter-kit
```

#### Method 2: Direct Installation
```bash
# Install from GitHub directly
/plugin install Dexploarer/claudius-skills/starter-kit
```

#### Method 3: Manual Copy
```bash
# Clone repository
git clone https://github.com/Dexploarer/claudius-skills.git

# Copy desired kit
cp -r claudius-skills/starter-kit/.claude /your/project/
```

### Managing Plugins

#### List Installed Plugins
```bash
/plugin list
```

#### Update a Plugin
```bash
/plugin update starter-kit
```

#### Remove a Plugin
```bash
/plugin remove starter-kit
```

#### Update Marketplace
```bash
/plugin marketplace update Dexploarer/claudius-skills
```

---

## Creating Your Own Plugins

Claudius Skills includes 4 generator skills to help you create custom plugins:

### 1. Plugin Generator
Generate complete plugins from scratch:
```
Say: "create a new plugin for [purpose]"
```

### 2. Skill-to-Plugin Converter
Convert existing skills to plugins:
```
Say: "convert my [skill-name] to a plugin"
```

### 3. Marketplace Manager
Add plugins to marketplace:
```
Say: "add [plugin-name] to the marketplace"
```

### 4. Plugin Bundler
Bundle multiple components into one plugin:
```
Say: "bundle these skills into a plugin"
```

---

## Plugin Categories

| Category | Description | Plugin Count |
|----------|-------------|--------------|
| **Beginner** | Learning and simple projects | 1 |
| **Intermediate** | Production applications | 1 |
| **Advanced** | Enterprise systems | 1 |
| **Specialized** | Domain-specific tools | 3 |
| **Productivity** | Personal and team workflows | 2 |
| **Enhancement** | Hooks, rules, configurations | 2 |

---

## Features by Plugin

### Skills Comparison

| Plugin | Skills | Focus |
|--------|--------|-------|
| Starter Kit | 5 | Essential workflows |
| Intermediate Kit | 10 | Framework integration |
| Advanced Kit | 15 | Enterprise patterns |
| Productivity Starter | 5 | Team productivity |
| Competitive AI | 3 | Code competitions |
| Eliza OS Kit | 6 | AI agent development |
| Railway Deployment | 5 | Deployment automation |

### Commands Comparison

| Plugin | Commands | Focus |
|--------|----------|-------|
| Starter Kit | 12 | Core workflows |
| Intermediate Kit | 15 | Framework operations |
| Advanced Kit | 20 | Enterprise operations |
| Productivity Starter | 13 | Content creation |
| Competitive AI | 3 | Competition workflows |
| Eliza OS Kit | 8 | Agent management |

### Agents Comparison

| Plugin | Agents | Focus |
|--------|--------|-------|
| Starter Kit | 4 | General assistance |
| Intermediate Kit | 6 | Framework specialists |
| Advanced Kit | 10 | Enterprise consultants |
| Productivity Starter | 4 | Content creators |
| Competitive AI | 12 | Team coordination |
| Eliza OS Kit | 6 | Agent specialists |

---

## Frequently Asked Questions

### Can I install multiple plugins?
Yes! Plugins are designed to work together. Install as many as you need.

### Will plugins conflict with each other?
No. Each plugin's components are namespaced and don't interfere with others.

### Can I customize installed plugins?
Yes. After installation, you can edit any component in your `.claude/` directory.

### How do I update plugins?
Use `/plugin update [plugin-name]` or update the entire marketplace with `/plugin marketplace update`.

### Can I create my own marketplace?
Yes! Use the marketplace-manager skill or create a `.claude-plugin/marketplace.json` file in your repository.

### Are plugins versioned?
Yes. Each plugin has semantic versioning (e.g., 1.0.0) for compatibility tracking.

---

## Technical Details

### Marketplace Structure

```
.claude-plugin/
└── marketplace.json          # Marketplace catalog
```

### Plugin Structure

```
[plugin-name]/
├── .claude/
│   ├── skills/              # Skill definitions
│   ├── commands/            # Slash commands
│   ├── agents/              # Specialized agents
│   ├── hooks/               # Event automation
│   └── rules/               # Configuration
├── .claude-plugin-manifest.json  # Plugin metadata
└── README.md                # Documentation
```

### Manifest Format

See individual plugin manifests for detailed structure. Key fields:
- `name`: Unique identifier (kebab-case)
- `version`: Semantic version (1.0.0)
- `category`: Plugin category
- `components`: Skills, commands, agents, hooks
- `stats`: Component counts

---

## Support

- **Issues**: [GitHub Issues](https://github.com/Dexploarer/claudius-skills/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Dexploarer/claudius-skills/discussions)
- **Documentation**: [Complete Docs](docs/)

---

## License

All plugins in the Claudius Skills marketplace are MIT licensed and free to use commercially.

---

**Last Updated:** November 5, 2025
**Marketplace Version:** 1.0.0
**Total Plugins:** 10
