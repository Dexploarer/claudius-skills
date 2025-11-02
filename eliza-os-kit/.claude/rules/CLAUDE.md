# elizaOS Development Kit - Claude Code Configuration

> **Comprehensive AI assistant configuration for elizaOS framework development**
> Master-level toolkit for building, testing, and deploying elizaOS agents, plugins, and integrations.

---

## 🎯 Overview

The **elizaOS Development Kit** is a production-ready Claude Code configuration providing complete support for:

- 🎭 **Character Development** - Create compelling AI agent personalities
- 🔌 **Plugin Engineering** - Build extensible plugin architectures
- 🧠 **Memory Management** - Optimize agent memory and context
- 📚 **Knowledge Systems** - Implement RAG and semantic search
- 🧪 **Testing & QA** - Comprehensive testing strategies
- 🚀 **Production Deployment** - Deploy and scale elizaOS agents

**Current Status:** Master-level comprehensive kit for professional elizaOS development

---

## 📁 Kit Structure

```
eliza-os-kit/.claude/
├── skills/                      # Automatic capabilities
│   ├── character-generator.md  # Character creation
│   ├── plugin-builder.md       # Plugin scaffolding
│   ├── knowledge-base-builder.md # Knowledge systems
│   ├── memory-manager.md       # Memory optimization
│   ├── testing-helper.md       # Test generation
│   └── deployment-helper.md    # Production deployment
├── commands/                    # Manual workflows
│   ├── validate-character.md   # Character validation
│   ├── test-character.md       # Testing workflows
│   ├── dev-agent.md           # Development mode
│   ├── build-plugin.md        # Plugin building
│   ├── deploy-agent.md        # Deployment
│   ├── optimize-memory.md     # Memory optimization
│   ├── sync-knowledge.md      # Knowledge sync
│   └── analyze-conversations.md # Analytics
├── agents/                      # Specialist consultants
│   ├── character-designer.md   # Personality expert
│   ├── plugin-architect.md     # Plugin specialist
│   ├── memory-architect.md     # Memory expert
│   ├── integration-specialist.md # Platform integrations
│   ├── deployment-engineer.md  # DevOps expert
│   └── testing-specialist.md   # QA specialist
├── hooks.json                   # Event automation
└── rules/                       # Documentation
    ├── CLAUDE.md               # This file
    ├── frameworks/             # Framework guides
    ├── workflows/              # Workflow patterns
    └── domains/                # Domain expertise
```

---

## 🎓 elizaOS Framework Knowledge

### Core Architecture

```
elizaOS Agent System
├── Character (Configuration)
│   ├── Identity (name, bio, personality)
│   ├── Knowledge (facts, documents, training)
│   ├── Plugins (extensions, capabilities)
│   └── Settings (model, environment)
├── Runtime (Execution)
│   ├── Memory System
│   ├── Action Handlers
│   ├── Provider Pipeline
│   ├── Evaluator Chain
│   └── Service Manager
└── Platform Integrations
    ├── Discord
    ├── Telegram
    ├── Twitter
    └── Custom APIs
```

### Key Concepts

#### Characters vs Agents
- **Character**: Static configuration blueprint (JSON/TypeScript)
- **Agent**: Live runtime instance with state and lifecycle

#### Plugin System
- **Actions**: Executable user-triggered operations
- **Providers**: Context enrichment for state composition
- **Evaluators**: Response quality assessment
- **Services**: Long-running platform integrations
- **Models**: Custom LLM handlers

#### Memory System
- **Short-term**: Current conversation (working memory)
- **Long-term**: Important facts (persistent, with decay)
- **Knowledge**: Static facts (configuration + learned)

#### State Composition
Aggregation of:
- Conversation history
- Provider-contributed context
- Memory retrievals
- Agent capabilities
- Metadata (room, entity, timestamp)

---

## 🛠️ Available Capabilities

### Skills (6 Production-Ready)

#### Character Generator
**Trigger**: "create character", "generate agent config"
- Creates complete character configurations
- Designs personality and conversation patterns
- Sets up knowledge bases
- Configures plugin ecosystems
- Generates training examples
- Production-ready validation

#### Plugin Builder
**Trigger**: "create plugin", "build elizaOS extension"
- Scaffolds complete plugin structure
- Generates actions, providers, services
- TypeScript configuration
- Comprehensive testing setup
- Documentation generation
- Build and packaging

#### Knowledge Base Builder
**Trigger**: "create knowledge base", "setup RAG"
- Document ingestion and processing
- Smart chunking strategies
- Embedding generation
- Semantic search optimization
- Knowledge versioning
- Quality metrics

#### Memory Manager
**Trigger**: "manage memory", "optimize context"
- Memory pruning strategies
- Context window optimization
- Conversation archiving
- Importance scoring
- Decay implementation
- Performance monitoring

#### Testing Helper
**Trigger**: "create tests", "test plugin"
- Unit test generation
- Integration testing
- E2E test scenarios
- Coverage analysis
- Test utilities
- Quality validation

#### Deployment Helper
**Trigger**: "deploy agent", "production setup"
- Docker configuration
- Environment setup
- Database migrations
- Monitoring configuration
- Scaling strategies
- Health checks

### Slash Commands (8 Workflows)

- `/validate-character` - Validate character configuration
- `/test-character` - Run comprehensive tests
- `/dev-agent` - Start development mode
- `/build-plugin` - Build and package plugin
- `/deploy-agent` - Deploy to production
- `/optimize-memory` - Analyze and optimize memory
- `/sync-knowledge` - Update knowledge base
- `/analyze-conversations` - Conversation analytics

### Specialist Agents (6 Experts)

- **Character Designer** - Personality and conversation expert
- **Plugin Architect** - Plugin development specialist
- **Memory Architect** - Memory system expert
- **Integration Specialist** - Platform integration expert
- **Deployment Engineer** - Production operations expert
- **Testing Specialist** - Quality assurance expert

### Hooks (8 Automations)

#### Pre-Tool-Use Hooks
- Secret detection in commits
- Character validation before start
- Environment variable checks
- Plugin publish confirmation
- Test enforcement before build

#### Post-Tool-Use Hooks
- Knowledge sync reminders
- Character validation prompts
- Test reminders after code changes

---

## 🚀 Quick Start

### For Character Development

```typescript
// 1. Use the character-generator skill
"Create a technical support character for Discord that specializes in React and TypeScript"

// 2. Validate the generated character
/validate-character

// 3. Test locally
/dev-agent

// 4. Deploy
/deploy-agent
```

### For Plugin Development

```typescript
// 1. Use the plugin-builder skill
"Create a plugin that integrates with GitHub API for repository management"

// 2. Build the plugin
/build-plugin

// 3. Test thoroughly
npm test

// 4. Publish
npm publish
```

### For Knowledge Management

```typescript
// 1. Use knowledge-base-builder
"Create a knowledge base from my React documentation folder"

// 2. Sync knowledge
/sync-knowledge

// 3. Test retrieval
/test-character

// 4. Optimize
/optimize-memory
```

---

## 📚 elizaOS Development Patterns

### Character Configuration Pattern

```typescript
import { Character } from '@elizaos/core';

export const character: Character = {
  // === IDENTITY ===
  name: 'AgentName',
  username: 'agent_handle',
  bio: [
    "Primary role and expertise",
    "Secondary capabilities",
    "Personality traits",
    "Communication style"
  ],

  // === PERSONALITY ===
  adjectives: ["trait1", "trait2", "trait3"],
  topics: ["domain1", "domain2", "domain3"],

  // === STYLE ===
  style: {
    all: ["Universal rule"],
    chat: ["Conversational rule"],
    post: ["Social media rule"]
  },

  // === TRAINING ===
  messageExamples: [/* 2D array of conversations */],
  postExamples: [/* social posts */],

  // === KNOWLEDGE ===
  knowledge: [
    "Simple fact",
    { path: "./knowledge/domain", shared: true }
  ],

  // === PLUGINS ===
  plugins: [
    '@elizaos/plugin-bootstrap',
    '@elizaos/plugin-sql',
    ...(process.env.OPENAI_API_KEY ? ['@elizaos/plugin-openai'] : []),
  ],

  // === SETTINGS ===
  settings: {
    model: 'gpt-4',
    temperature: 0.7,
    maxTokens: 2000,
    conversationLength: 32
  }
};
```

### Plugin Development Pattern

```typescript
import type { Plugin, Action, Provider, Service } from '@elizaos/core';

// Action Implementation
export const myAction: Action = {
  name: 'ACTION_NAME',
  similes: ['similar1', 'similar2'],
  description: 'What this does',
  validate: async (runtime, message, state) => boolean,
  handler: async (runtime, message, state, options, callback) => {
    // Implementation
    return result;
  }
};

// Provider Implementation
export const myProvider: Provider = {
  name: 'PROVIDER_NAME',
  description: 'Context provided',
  position: 100,
  get: async (runtime, message, state) => ({
    values: {},  // Template variables
    data: {},    // Structured data
    text: ''     // LLM context
  })
};

// Service Implementation
export class MyService extends Service {
  static serviceType: ServiceTypeName = 'MY_SERVICE';
  capabilityDescription = 'What this provides';

  static async start(runtime: IAgentRuntime): Promise<Service> {
    const service = new MyService(runtime);
    await service.initialize();
    return service;
  }

  async stop(): Promise<void> {
    // Cleanup
  }
}

// Plugin Export
export const myPlugin: Plugin = {
  name: '@elizaos/plugin-name',
  description: 'Plugin purpose',
  actions: [myAction],
  providers: [myProvider],
  services: [MyService]
};
```

### Memory Management Pattern

```typescript
// Create Memory
await runtime.createMemory({
  entityId: userId,
  roomId: conversationId,
  content: {
    text: 'Important information',
    metadata: { importance: 'high' }
  },
  embedding: await generateEmbedding(text)
});

// Retrieve Memories
const memories = await runtime.getMemories({
  roomId: conversationId,
  limit: 10,
  unique: true
});

// Search Semantically
const results = await runtime.searchMemories(
  'query text',
  { limit: 5, minScore: 0.7 }
);

// Prune Old Memories
async function pruneOldMemories(daysToKeep: number = 30) {
  const cutoffDate = Date.now() - (daysToKeep * 24 * 60 * 60 * 1000);
  const oldMemories = await runtime.getMemories({
    createdBefore: cutoffDate,
    importance: 'low'
  });
  for (const memory of oldMemories) {
    await runtime.deleteMemory(memory.id);
  }
}
```

### Testing Pattern

```typescript
import { describe, it, expect, beforeEach } from 'vitest';
import { createMockRuntime, createMockMessage } from '@elizaos/core/test';

describe('MyAction', () => {
  let runtime: any;
  let message: any;

  beforeEach(() => {
    runtime = createMockRuntime();
    message = createMockMessage({ content: { text: 'test' } });
  });

  it('validates correct input', async () => {
    const valid = await myAction.validate(runtime, message);
    expect(valid).toBe(true);
  });

  it('executes successfully', async () => {
    const result = await myAction.handler(runtime, message);
    expect(result).toBeDefined();
  });
});
```

### Deployment Pattern

```typescript
// src/index.ts
import { AgentRuntime } from '@elizaos/core';
import { PGAdapter } from '@elizaos/adapter-postgresql';
import character from './character';

const runtime = new AgentRuntime({
  databaseAdapter: new PGAdapter(process.env.DATABASE_URL),
  character,
  env: process.env
});

await runtime.initialize();

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'healthy', agent: character.name });
});

// Graceful shutdown
process.on('SIGTERM', async () => {
  await runtime.stop();
  process.exit(0);
});
```

---

## 🎯 Best Practices

### Character Design
1. ✅ Keep personality simple and consistent
2. ✅ Provide 3-5 diverse conversation examples minimum
3. ✅ Align bio, adjectives, and style rules
4. ✅ Use conditional plugin loading
5. ✅ Document all custom settings
6. ✅ Test character responses thoroughly
7. ✅ Version character configurations
8. ✅ Never hardcode secrets
9. ✅ Validate before deployment
10. ✅ Monitor performance metrics

### Plugin Development
1. ✅ Single responsibility per plugin
2. ✅ Type safety with strict TypeScript
3. ✅ Comprehensive error handling
4. ✅ Input validation with Zod
5. ✅ >80% test coverage
6. ✅ Clear API documentation
7. ✅ Semantic versioning
8. ✅ Minimal dependencies
9. ✅ Performance optimization
10. ✅ Security-first design

### Memory Management
1. ✅ Set appropriate memory limits
2. ✅ Implement importance scoring
3. ✅ Use time-based decay
4. ✅ Archive important conversations
5. ✅ Optimize embedding search
6. ✅ Monitor growth patterns
7. ✅ Regular pruning schedules
8. ✅ Cache frequent queries
9. ✅ Batch memory operations
10. ✅ Index properly for performance

### Knowledge Systems
1. ✅ Structure documents clearly
2. ✅ Balance chunk size (500-1500 chars)
3. ✅ Include 10-20% overlap
4. ✅ Version knowledge files
5. ✅ Regular quality review
6. ✅ Pre-compute embeddings
7. ✅ Never include sensitive data
8. ✅ Organize in directories
9. ✅ Validate retrieval quality
10. ✅ Monitor usage patterns

### Testing
1. ✅ Unit tests for all components
2. ✅ Integration tests for plugins
3. ✅ E2E tests for critical flows
4. ✅ Test error scenarios
5. ✅ Cover edge cases
6. ✅ Mock external dependencies
7. ✅ Measure coverage (>80%)
8. ✅ Performance testing
9. ✅ Load testing for scale
10. ✅ Continuous integration

### Deployment
1. ✅ Validate configuration
2. ✅ Run migrations
3. ✅ Test production build
4. ✅ Implement health checks
5. ✅ Configure monitoring
6. ✅ Setup error tracking
7. ✅ Enable logging
8. ✅ Secure HTTPS
9. ✅ Plan for scaling
10. ✅ Document rollback

---

## 🔧 Configuration

### Environment Variables

```bash
# LLM Providers
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/eliza

# Platform Integrations
DISCORD_API_TOKEN=
TELEGRAM_BOT_TOKEN=
TWITTER_API_KEY=

# Optional Services
REDIS_URL=redis://localhost:6379
PINECONE_API_KEY=
```

### TypeScript Configuration

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ES2022",
    "moduleResolution": "node",
    "strict": true,
    "esModuleInterop": true,
    "declaration": true,
    "outDir": "./dist",
    "rootDir": "./src"
  }
}
```

### Package Scripts

```json
{
  "scripts": {
    "dev": "elizaos dev",
    "start": "elizaos start",
    "test": "vitest",
    "build": "tsc",
    "validate": "node scripts/validate-character.js",
    "lint": "eslint src/**/*.ts",
    "format": "prettier --write \"src/**/*.ts\""
  }
}
```

---

## 📖 Learning Path

### 1. Beginner → Intermediate (1-2 weeks)
- Understand elizaOS architecture
- Create first character
- Configure basic plugins
- Test locally
- Deploy simple agent

### 2. Intermediate → Advanced (2-4 weeks)
- Build custom plugins
- Implement actions and providers
- Optimize memory management
- Setup knowledge bases
- Multi-platform deployment

### 3. Advanced → Expert (1-3 months)
- Complex plugin architectures
- Advanced memory strategies
- Custom model integrations
- Production scaling
- Performance optimization

---

## 🎭 Use Cases

### Technical Support Agent
- Discord/Telegram integration
- Knowledge base from documentation
- Code example generation
- Issue troubleshooting
- Escalation workflows

### Content Creation Agent
- Twitter/social media integration
- Style-specific writing
- Research and fact-checking
- Multi-platform posting
- Analytics tracking

### Data Analysis Agent
- Database integration
- Query generation
- Visualization creation
- Report generation
- Metric monitoring

### Community Management Agent
- Multi-platform moderation
- Welcome messages
- FAQ responses
- Event announcements
- User engagement tracking

---

## 🔍 Troubleshooting

### Common Issues

**Character not responding**
- Check API keys in .env
- Verify plugins loaded correctly
- Review logs for errors
- Test with /validate-character

**Memory issues**
- Reduce conversationLength
- Implement pruning
- Use /optimize-memory
- Check database size

**Plugin errors**
- Verify dependencies installed
- Check TypeScript compilation
- Run tests: npm test
- Review plugin initialization

**Deployment failures**
- Validate environment variables
- Test production build locally
- Check database connectivity
- Review deployment logs

---

## 🚀 Advanced Topics

### Multi-Agent Swarms
- Shared database architecture
- Agent coordination
- Load balancing
- Inter-agent communication

### Custom Model Integration
- Model handler implementation
- Token counting
- Streaming support
- Fallback mechanisms

### Advanced Memory
- Hierarchical memory
- Memory consolidation
- Cross-agent memory sharing
- Temporal relevance modeling

### Performance Optimization
- Caching strategies
- Batch operations
- Database optimization
- Query performance

---

## 📚 Resources

### Official Documentation
- [elizaOS Docs](https://docs.elizaos.ai)
- [Plugin Development Guide](https://docs.elizaos.ai/plugins)
- [API Reference](https://docs.elizaos.ai/api)

### Community
- [Discord Community](https://discord.gg/elizaos)
- [GitHub Repository](https://github.com/elizaos/eliza)
- [Examples Repository](https://github.com/elizaos/examples)

### Tools
- [Character Validator](https://elizaos.ai/tools/validator)
- [Plugin Generator](https://elizaos.ai/tools/generator)
- [Knowledge Builder](https://elizaos.ai/tools/knowledge)

---

## 🎯 Project Philosophy

**Production-Ready**: Every component is battle-tested and ready for production
**Education-First**: Learn elizaOS through comprehensive examples and guidance
**Security-Minded**: Built-in protections and best practices
**Performance-Optimized**: Efficient patterns for scale
**Community-Driven**: Contributions and improvements welcome

---

**Last Updated:** 2025-11-01
**Kit Version:** 1.0.0 - Master Level elizaOS Development
**Maintainer:** Claudius Skills elizaOS Team

---

## 💡 Getting Help

When working with this kit:
1. Check the relevant skill documentation
2. Use specialist agents for expert guidance
3. Run validation commands before deployment
4. Leverage hooks for automated checks
5. Test thoroughly at each stage

For issues or contributions:
- Review troubleshooting guide
- Check official elizaOS documentation
- Engage with community on Discord
- Submit issues or PRs to repository

**Happy Building! 🚀**
