# elizaOS Development Kit for Claude Code

> **Master-Level AI Assistant Configuration for elizaOS Framework Development**

A comprehensive, production-ready Claude Code configuration providing complete support for building, testing, and deploying elizaOS agents, plugins, and integrations.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![elizaOS](https://img.shields.io/badge/elizaOS-Compatible-blue.svg)](https://elizaos.ai)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Optimized-green.svg)](https://docs.claude.com)

---

## 🌟 Features

### 🎭 Character Development
- **Intelligent Character Generator** - Create compelling AI agent personalities
- **Personality Design Patterns** - Helper, Expert, Companion, Analyst archetypes
- **Training Data Creation** - Generate diverse conversation examples
- **Multi-Platform Configuration** - Discord, Telegram, Twitter, Web

### 🔌 Plugin Engineering
- **Complete Plugin Scaffolding** - Full TypeScript project structure
- **Component Generators** - Actions, Providers, Evaluators, Services
- **Testing Infrastructure** - Unit, integration, and E2E test setup
- **Build & Package Tools** - Production-ready npm packages

### 🧠 Memory & Knowledge
- **Memory Management** - Pruning strategies and optimization
- **Knowledge Base Builder** - RAG system with semantic search
- **Context Optimization** - Efficient token usage and windowing
- **Embedding Generation** - Batch processing and caching

### 🧪 Testing & Quality
- **Automated Test Generation** - Comprehensive test suites
- **Validation Tools** - Character and plugin validation
- **Quality Metrics** - Coverage analysis and reporting
- **CI/CD Integration** - GitHub Actions and automated testing

### 🚀 Production Deployment
- **Docker Configuration** - Containerization and orchestration
- **Monitoring Setup** - Observability and alerting
- **Scaling Strategies** - Load balancing and multi-agent swarms
- **Security Hardening** - Best practices and secrets management

---

## 📦 What's Included

### Skills (6 Production-Ready)

| Skill | Description | Triggers |
|-------|-------------|----------|
| `character-generator` | Create complete character configurations | "create character", "generate agent" |
| `plugin-builder` | Scaffold production-ready plugins | "create plugin", "build extension" |
| `knowledge-base-builder` | Setup RAG and semantic search | "create knowledge base", "setup RAG" |
| `memory-manager` | Optimize agent memory systems | "manage memory", "optimize context" |
| `testing-helper` | Generate comprehensive tests | "create tests", "test plugin" |
| `deployment-helper` | Deploy to production | "deploy agent", "production setup" |

### Slash Commands (8 Workflows)

| Command | Purpose |
|---------|---------|
| `/validate-character` | Validate character configuration |
| `/test-character` | Run comprehensive tests |
| `/dev-agent` | Start development mode |
| `/build-plugin` | Build and package plugin |
| `/deploy-agent` | Deploy to production |
| `/optimize-memory` | Analyze and optimize memory |
| `/sync-knowledge` | Update knowledge base |
| `/analyze-conversations` | Conversation analytics |

### Specialist Agents (6 Experts)

| Agent | Expertise |
|-------|-----------|
| `character-designer` | Personality and conversation design |
| `plugin-architect` | Plugin development and architecture |
| `memory-architect` | Memory system optimization |
| `integration-specialist` | Platform integrations |
| `deployment-engineer` | Production operations |
| `testing-specialist` | Quality assurance |

### Hooks (17 Automations)

**Pre-Tool-Use (Safety & Prevention):**
- **Secret detection** in commits
- **Character validation** before start
- **Environment variable** checks
- **Plugin publish** confirmation
- **Test enforcement** before build

**Post-Tool-Use (Validation & Reminders):**
- **Knowledge sync** reminders
- **Validation prompts** after edits
- **Test reminders** after code changes
- **Plugin structure validation** (NPM naming, dependencies, init())
- **Service lifecycle validation** (extends Service, start(), stop())
- **Action pattern validation** (validate(), handler(), similes, examples)
- **Character completeness check** (name, bio, adjectives, examples)
- **Error handling verification** (try-catch for async functions)
- **Zod validation check** (input validation for actions)
- **Import path validation** (@elizaos/* imports)
- **TypeScript config validation** (strict mode, esModuleInterop)
- **Package dependencies check** (@elizaos/core presence)

### Official elizaOS Rules (Aligned with Core Framework)

**Based on official elizaOS v2 architecture:**
- `elizaos-core-runtime.md` - Runtime lifecycle and character configuration patterns
- `elizaos-plugin-patterns.md` - Plugin, service, action, provider implementation standards
- Comprehensive code examples showing ✅ correct vs ❌ incorrect patterns
- Validation checklist for production readiness

---

## 🚀 Quick Start

### Installation

1. **Copy the kit to your elizaOS project:**

```bash
# Clone or copy the eliza-os-kit
cp -r eliza-os-kit/.claude /path/to/your/elizaos/project/
```

2. **Or create a new elizaOS project with the kit:**

```bash
# Create new project directory
mkdir my-eliza-agent
cd my-eliza-agent

# Copy the .claude configuration
cp -r /path/to/eliza-os-kit/.claude .

# Initialize npm project
npm init -y
```

3. **Start Claude Code in your project directory:**

```bash
cd /path/to/your/elizaos/project
# Open Claude Code or your IDE with Claude Code extension
```

### First Steps

#### Create Your First Character

```typescript
// In Claude Code, simply ask:
"Create a technical support character for Discord that helps with React and TypeScript"

// The character-generator skill will:
// ✅ Design personality and traits
// ✅ Generate conversation examples
// ✅ Configure plugins
// ✅ Create knowledge structure
// ✅ Setup environment template
// ✅ Generate tests
// ✅ Write documentation
```

#### Build Your First Plugin

```typescript
// Ask Claude Code:
"Create a plugin that integrates with GitHub API for repository management"

// The plugin-builder skill will:
// ✅ Scaffold complete directory structure
// ✅ Generate TypeScript configuration
// ✅ Create actions, providers, services
// ✅ Setup comprehensive tests
// ✅ Configure build scripts
// ✅ Generate documentation
```

#### Setup Knowledge Base

```typescript
// Ask Claude Code:
"Create a knowledge base from my documentation in /docs folder"

// The knowledge-base-builder skill will:
// ✅ Scan and process documents
// ✅ Implement smart chunking
// ✅ Generate embeddings
// ✅ Configure semantic search
// ✅ Setup retrieval optimization
```

---

## 📚 Documentation

### Core Concepts

#### elizaOS Architecture

```
elizaOS Agent
├── Character (Configuration)
│   ├── Identity & Personality
│   ├── Knowledge & Training
│   ├── Plugins & Capabilities
│   └── Settings & Environment
├── Runtime (Execution)
│   ├── Memory System
│   ├── Action Handlers
│   ├── Provider Pipeline
│   ├── Evaluator Chain
│   └── Service Manager
└── Integrations (Platforms)
    ├── Discord, Telegram, Twitter
    ├── Custom APIs
    └── External Services
```

#### Plugin System

- **Actions**: User-triggered operations (CRUD, API calls, calculations)
- **Providers**: Context enrichment (recent messages, facts, capabilities)
- **Evaluators**: Response quality assessment (safety, relevance, accuracy)
- **Services**: Long-running processes (platform connections, background tasks)

#### Memory System

- **Short-term**: Current conversation context (working memory)
- **Long-term**: Important facts with decay (persistent memory)
- **Knowledge**: Static facts from configuration (knowledge base)

### Example Projects

#### 1. Discord Support Bot

```typescript
// Create character
"Create a Discord support bot for a React community that answers questions,
provides code examples, and troubleshoots common issues"

// Validate
/validate-character

// Test locally
/dev-agent

// Deploy
/deploy-agent
```

#### 2. Twitter Content Creator

```typescript
// Create character
"Create a Twitter bot that shares daily programming tips, engages with
developers, and curates tech news"

// Build knowledge base
"Create a knowledge base from my programming tips markdown files"

// Sync knowledge
/sync-knowledge

// Deploy
/deploy-agent
```

#### 3. Custom GitHub Integration Plugin

```typescript
// Build plugin
"Create a plugin that lets agents create GitHub issues, pull requests,
and manage repositories"

// Build and test
/build-plugin
npm test

// Publish
npm publish
```

---

## 🎯 Use Cases

### Technical Support
- Multi-platform support (Discord, Telegram, Web)
- Knowledge base from documentation
- Code example generation
- Issue troubleshooting and escalation

### Content Creation
- Social media management (Twitter, LinkedIn)
- Style-specific writing
- Research and fact-checking
- Multi-platform posting and analytics

### Community Management
- Welcome messages and onboarding
- FAQ responses and moderation
- Event announcements
- User engagement tracking

### Data Analysis
- Database query generation
- Report generation
- Metric monitoring
- Visualization creation

### Internal Tools
- Workflow automation
- Slack integrations
- Custom API access
- Knowledge management

---

## 📖 Learning Path

### Beginner (Week 1-2)

**Goals**: Understand basics, create first character

- [ ] Read [elizaOS documentation](https://docs.elizaos.ai)
- [ ] Create a simple character with character-generator
- [ ] Test character locally with /dev-agent
- [ ] Configure basic plugins (Discord or Telegram)
- [ ] Deploy simple agent

**Example Project**: Create a Discord welcome bot

### Intermediate (Week 3-6)

**Goals**: Build custom plugins, optimize memory

- [ ] Build custom action with plugin-builder
- [ ] Create knowledge base with RAG
- [ ] Implement memory pruning
- [ ] Multi-platform deployment
- [ ] Production monitoring

**Example Project**: Create technical support agent with knowledge base

### Advanced (Month 2-3)

**Goals**: Complex architectures, production scale

- [ ] Build complete plugin with services
- [ ] Advanced memory strategies
- [ ] Multi-agent coordination
- [ ] Performance optimization
- [ ] Enterprise deployment

**Example Project**: Build multi-agent swarm with specialized roles

---

## 🔧 Configuration

### Project Structure

```
your-elizaos-project/
├── .claude/                 # This kit
│   ├── skills/
│   ├── commands/
│   ├── agents/
│   ├── hooks.json
│   └── rules/
├── characters/              # Your characters
│   └── my-agent.ts
├── plugins/                 # Custom plugins
│   └── my-plugin/
├── knowledge/              # Knowledge base
│   └── docs/
├── __tests__/              # Tests
├── .env                    # Environment variables
├── .env.example            # Template
├── package.json
└── tsconfig.json
```

### Environment Variables

```bash
# .env

# LLM Providers (at least one required)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...

# Database (required)
DATABASE_URL=postgresql://user:pass@localhost:5432/eliza
# Or use PGLite for local dev
# DATABASE_URL=pglite://./data/db

# Platform Integrations (optional)
DISCORD_API_TOKEN=
DISCORD_APPLICATION_ID=
TELEGRAM_BOT_TOKEN=
TWITTER_API_KEY=
TWITTER_API_SECRET=

# Optional Services
REDIS_URL=redis://localhost:6379
PINECONE_API_KEY=
```

### Package Configuration

```json
{
  "name": "my-eliza-agent",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "elizaos dev",
    "start": "elizaos start",
    "test": "vitest",
    "build": "tsc",
    "validate": "node scripts/validate-character.js"
  },
  "dependencies": {
    "@elizaos/core": "latest",
    "@elizaos/plugin-bootstrap": "latest",
    "@elizaos/plugin-sql": "latest"
  }
}
```

---

## 🛠️ Development Workflow

### 1. Character Development

```bash
# Ask Claude Code to create character
"Create a [type] character for [platform] that [purpose]"

# Validate
/validate-character

# Test locally
/dev-agent

# Review and iterate
# Make changes to character file
# Revalidate and test
```

### 2. Plugin Development

```bash
# Scaffold plugin
"Create a plugin that [functionality]"

# Implement components
# - Edit actions in src/actions/
# - Edit providers in src/providers/
# - Edit services in src/services/

# Test
npm test

# Build
/build-plugin

# Publish (when ready)
npm publish
```

### 3. Knowledge Management

```bash
# Create knowledge base
"Create a knowledge base from [source]"

# Add documents
# - Create markdown files in knowledge/
# - Reference in character.knowledge

# Sync
/sync-knowledge

# Test retrieval
/test-character

# Optimize
/optimize-memory
```

### 4. Production Deployment

```bash
# Validate everything
/validate-character
npm test

# Build production assets
/build-plugin

# Deploy
/deploy-agent

# Monitor
# Check health endpoints
# Review logs
# Monitor metrics
```

---

## 🧪 Testing

### Run Tests

```bash
# All tests
npm test

# With coverage
npm run test:coverage

# Specific test file
npm test __tests__/character.test.ts

# Watch mode
npm test --watch
```

### Validation

```bash
# Validate character
/validate-character

# Test character responses
/test-character

# Analyze conversation quality
/analyze-conversations
```

---

## 🚀 Deployment

### Local Development

```bash
# Start in development mode
/dev-agent

# Or manually
npm run dev
```

### Docker Deployment

```bash
# Build image
docker build -t my-eliza-agent .

# Run container
docker run -p 3000:3000 \
  --env-file .env \
  my-eliza-agent

# Or use docker-compose
docker-compose up -d
```

### Production Deployment

```bash
# Deploy with kit's helper
/deploy-agent

# Or follow manual steps:
# 1. Configure environment
# 2. Run migrations
# 3. Build assets
# 4. Deploy to platform (Heroku, Railway, AWS, etc.)
# 5. Configure monitoring
# 6. Verify deployment
```

---

## 📊 Monitoring

### Health Checks

```typescript
// Health endpoint (auto-generated)
GET /health

Response:
{
  "status": "healthy",
  "agent": "AgentName",
  "uptime": 3600,
  "version": "1.0.0"
}
```

### Metrics

```typescript
// Metrics endpoint (Prometheus compatible)
GET /metrics

# agent_messages_total{agent="AgentName",status="success"} 1234
# agent_response_duration_seconds{quantile="0.5"} 0.234
# agent_memory_size{agent="AgentName"} 5678
```

### Logging

```bash
# View logs
docker logs my-eliza-agent -f

# Or if running locally
npm run dev # Shows detailed logs
```

---

## 🔒 Security

### Best Practices

- ✅ Never commit `.env` files
- ✅ Use environment variables for secrets
- ✅ Validate all user input
- ✅ Implement rate limiting
- ✅ Use HTTPS in production
- ✅ Regular security audits
- ✅ Keep dependencies updated
- ✅ Implement proper authentication
- ✅ Log security events
- ✅ Follow principle of least privilege

### Secret Management

```bash
# Use environment variables
export OPENAI_API_KEY=sk-...

# Or use secret management services
# - AWS Secrets Manager
# - HashiCorp Vault
# - Docker secrets
```

---

## 🤝 Contributing

Contributions are welcome! This kit is designed to grow with the elizaOS community.

### How to Contribute

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Update documentation
6. Submit a pull request

### Areas for Contribution

- New skills for common tasks
- Additional specialist agents
- More slash commands
- Enhanced hooks
- Documentation improvements
- Example projects
- Bug fixes

---

## 📝 Changelog

### v1.0.0 (2025-11-01)

**Initial Release - Master Level Kit**

- ✨ 6 production-ready skills
- ⚡ 8 workflow slash commands
- 👥 6 specialist agents
- 🪝 8 automated hooks
- 📚 Comprehensive documentation
- 🎯 Best practices and patterns
- 🚀 Deployment configurations
- 🧪 Testing infrastructure

---

## 📚 Additional Resources

### Official Documentation
- [elizaOS Website](https://elizaos.ai)
- [elizaOS Documentation](https://docs.elizaos.ai)
- [Plugin Development Guide](https://docs.elizaos.ai/plugins)
- [API Reference](https://docs.elizaos.ai/api)

### Community
- [Discord Community](https://discord.gg/elizaos)
- [GitHub Repository](https://github.com/elizaos/eliza)
- [Examples Repository](https://github.com/elizaos/examples)
- [Twitter](https://twitter.com/elizaos)

### Tools
- [Character Validator](https://elizaos.ai/tools/validator)
- [Plugin Generator](https://elizaos.ai/tools/generator)
- [Knowledge Builder](https://elizaos.ai/tools/knowledge)

---

## ❓ FAQ

**Q: Do I need the entire elizaOS framework installed?**
A: Yes, this is a Claude Code configuration kit for elizaOS development. Install elizaOS first: `npm install @elizaos/core`

**Q: Can I use this with existing elizaOS projects?**
A: Absolutely! Just copy the `.claude` directory to your project root.

**Q: Does this work with all Claude Code features?**
A: Yes, this kit leverages all five pillars: Skills, Commands, Agents, Hooks, and MCP integrations.

**Q: Can I customize the skills and commands?**
A: Yes! All configurations are markdown-based and easily customizable.

**Q: Is this suitable for production use?**
A: Yes, all components are designed for production with security, testing, and monitoring built-in.

**Q: What LLM providers are supported?**
A: OpenAI, Anthropic, and any elizaOS-compatible provider.

**Q: Can I contribute new skills?**
A: Yes! Contributions are welcome. See the Contributing section.

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🙏 Acknowledgments

- **elizaOS Team** - For the amazing AI agent framework
- **Anthropic** - For Claude Code and Claude AI
- **Community Contributors** - For feedback and improvements

---

## 💬 Support

### Need Help?

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review [elizaOS Documentation](https://docs.elizaos.ai)
3. Ask in [Discord Community](https://discord.gg/elizaos)
4. Open an issue on GitHub

### Professional Support

For enterprise support, custom development, or consulting:
- Enterprise deployment assistance
- Custom plugin development
- Training and workshops
- Architecture consulting

---

## 🎯 Next Steps

Ready to build amazing AI agents? Here's what to do next:

1. ✅ Install the kit in your project
2. ✅ Create your first character
3. ✅ Test locally with /dev-agent
4. ✅ Build a custom plugin
5. ✅ Deploy to production
6. ✅ Join the community
7. ✅ Share your creations!

**Happy Building! 🚀**

---

<p align="center">
  <i>Built with ❤️ by the Claudius Skills Team</i>
  <br>
  <i>Powered by elizaOS and Claude Code</i>
</p>
