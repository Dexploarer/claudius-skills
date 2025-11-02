# ElizaOS Core Runtime Rules

**Version:** 1.0.0
**Based on:** Official elizaOS v2 Architecture
**Purpose:** Guidance for implementing elizaOS AgentRuntime systems

---

## Core Principles

The `AgentRuntime` is the **central orchestration component** managing:
- Agent lifecycle (initialization → running → shutdown)
- Character configuration and personality
- Plugin registration and dependency resolution
- Service orchestration and health monitoring
- Memory system management
- State composition and context building

**Critical Understanding:** Runtime initialization is a structured, critical process requiring proper error handling, validation, and lifecycle management at every stage.

---

## Character Configuration

### ✅ CORRECT Pattern

```typescript
import { Character } from '@elizaos/core';

export const character: Character = {
  // === IDENTITY (Required) ===
  name: 'AgentName',
  bio: [
    "Primary role and expertise",
    "Key capabilities and knowledge domains",
    "Personality traits and communication style"
  ],

  // === PERSONALITY ===
  adjectives: [
    "helpful",
    "knowledgeable",
    "professional",
    "empathetic"
  ],

  topics: [
    "domain expertise 1",
    "domain expertise 2",
    "specialization area"
  ],

  // === STYLE GUIDE ===
  style: {
    all: [
      "Be clear and concise",
      "Use professional language",
      "Provide examples when helpful"
    ],
    chat: [
      "Be conversational and friendly",
      "Ask clarifying questions"
    ],
    post: [
      "Keep under 280 characters",
      "Use relevant hashtags"
    ]
  },

  // === TRAINING EXAMPLES ===
  messageExamples: [
    [
      {
        name: "{{user}}",
        content: { text: "User message example" }
      },
      {
        name: "AgentName",
        content: { text: "Agent response showing personality" }
      }
    ]
  ],

  postExamples: [
    "Example social media post showing voice",
    "Another post demonstrating style"
  ],

  // === KNOWLEDGE ===
  knowledge: [
    "Core fact about domain",
    {
      path: "./knowledge/domain-expertise",
      shared: true
    }
  ],

  // === PLUGINS ===
  plugins: [
    '@elizaos/plugin-bootstrap',
    '@elizaos/plugin-sql',
    ...(process.env.OPENAI_API_KEY ? ['@elizaos/plugin-openai'] : []),
  ],

  // === SETTINGS ===
  settings: {
    secrets: {},
    model: 'gpt-4',
    temperature: 0.7,
    maxTokens: 2000,
    conversationLength: 32
  }
};
```

### ❌ INCORRECT Anti-Pattern

```typescript
// DON'T: Minimal configuration without validation
export const character = {
  name: 'Bot',
  bio: 'A bot',
  plugins: ['@elizaos/plugin-openai']
  // Missing: personality, examples, knowledge, proper settings
};
```

---

## Runtime Lifecycle

### ✅ CORRECT Pattern

```typescript
import { AgentRuntime } from '@elizaos/core';
import { PostgresAdapter } from '@elizaos/adapter-postgres';
import character from './character';

async function initializeAgent(): Promise<AgentRuntime> {
  try {
    // 1. Validate environment
    if (!process.env.DATABASE_URL) {
      throw new Error('DATABASE_URL is required');
    }

    // 2. Create database adapter
    const databaseAdapter = new PostgresAdapter({
      connectionString: process.env.DATABASE_URL,
      max: 20,
      ssl: process.env.NODE_ENV === 'production'
    });

    // 3. Initialize runtime with full configuration
    const runtime = new AgentRuntime({
      databaseAdapter,
      character,
      env: process.env,
      // Optional: custom configuration
      serverUrl: process.env.SERVER_URL,
      token: process.env.AUTH_TOKEN
    });

    // 4. Initialize runtime (loads plugins, registers components)
    await runtime.initialize();

    // 5. Verify critical services are available
    const dbService = runtime.getService('DATABASE');
    if (!dbService) {
      throw new Error('Database service failed to initialize');
    }

    console.log('✅ Agent runtime initialized successfully');
    return runtime;

  } catch (error) {
    console.error('❌ Runtime initialization failed:', error);
    throw error;
  }
}

// Graceful shutdown
async function shutdownAgent(runtime: AgentRuntime): Promise<void> {
  try {
    console.log('Shutting down agent runtime...');
    await runtime.stop();
    console.log('✅ Agent shutdown complete');
  } catch (error) {
    console.error('❌ Shutdown error:', error);
    throw error;
  }
}

// Process signal handlers
process.on('SIGTERM', async () => {
  if (runtime) {
    await shutdownAgent(runtime);
  }
  process.exit(0);
});

process.on('SIGINT', async () => {
  if (runtime) {
    await shutdownAgent(runtime);
  }
  process.exit(0);
});
```

### ❌ INCORRECT Anti-Pattern

```typescript
// DON'T: Skip error handling and validation
const runtime = new AgentRuntime({
  databaseAdapter: new PostgresAdapter(process.env.DATABASE_URL),
  character
});
await runtime.initialize();
// Missing: error handling, validation, graceful shutdown
```

---

## Plugin Management

### ✅ CORRECT Pattern

```typescript
// Plugin registration through runtime (automatic dependency resolution)
const runtime = new AgentRuntime({
  databaseAdapter,
  character: {
    ...character,
    plugins: [
      '@elizaos/plugin-bootstrap',    // Core - always first
      '@elizaos/plugin-sql',           // Database access
      '@elizaos/plugin-openai',        // LLM provider
      '@elizaos/plugin-discord',       // Platform client
      './custom-plugins/my-plugin'     // Custom plugin
    ]
  },
  env: process.env
});

// Runtime handles:
// 1. Dependency resolution
// 2. Topological sorting
// 3. Init() execution
// 4. Component registration
await runtime.initialize();
```

### ❌ INCORRECT Anti-Pattern

```typescript
// DON'T: Manual service instantiation bypassing runtime
import { MyService } from './services/my-service';

const service = new MyService(runtime);  // ❌ Wrong!
await service.start();                    // ❌ Bypasses lifecycle

// Should use: runtime.getService<MyService>('MY_SERVICE')
```

---

## Service Lifecycle

### ✅ CORRECT Pattern

```typescript
import { Service, ServiceTypeName } from '@elizaos/core';

export class DatabaseService extends Service {
  static serviceType: ServiceTypeName = 'DATABASE' as ServiceTypeName;

  private pool: any;
  private healthCheckInterval: NodeJS.Timeout | null = null;

  capabilityDescription = 'Database connection and query execution';

  constructor(runtime: IAgentRuntime) {
    super(runtime);
  }

  // Factory method for service initialization
  static async start(runtime: IAgentRuntime): Promise<Service> {
    const service = new DatabaseService(runtime);
    await service.initialize();
    return service;
  }

  private async initialize(): Promise<void> {
    try {
      // 1. Initialize connection
      this.pool = await this.createPool();

      // 2. Verify connectivity
      await this.healthCheck();

      // 3. Setup monitoring
      this.setupHealthMonitoring();

      console.log('✅ Database service initialized');
    } catch (error) {
      console.error('❌ Database initialization failed:', error);
      throw error;
    }
  }

  private async healthCheck(): Promise<boolean> {
    try {
      await this.pool.query('SELECT 1');
      return true;
    } catch (error) {
      console.error('Database health check failed:', error);
      return false;
    }
  }

  private setupHealthMonitoring(): void {
    this.healthCheckInterval = setInterval(async () => {
      const healthy = await this.healthCheck();
      if (!healthy) {
        console.error('❌ Database connection lost');
        // Implement reconnection logic
      }
    }, 30000); // Check every 30s
  }

  async stop(): Promise<void> {
    try {
      // 1. Stop health monitoring
      if (this.healthCheckInterval) {
        clearInterval(this.healthCheckInterval);
      }

      // 2. Close connections
      if (this.pool) {
        await this.pool.end();
      }

      console.log('✅ Database service stopped');
    } catch (error) {
      console.error('❌ Database shutdown error:', error);
    }
  }

  // Service methods
  async query(sql: string, params?: any[]): Promise<any> {
    return this.pool.query(sql, params);
  }
}
```

### ❌ INCORRECT Anti-Pattern

```typescript
// DON'T: Skip health monitoring and proper lifecycle
export class BadDatabaseService extends Service {
  static async start(runtime: IAgentRuntime): Promise<Service> {
    return new BadDatabaseService(runtime);  // ❌ No initialization!
  }

  async stop(): Promise<void> {
    // ❌ Empty - no cleanup!
  }
}
```

---

## Error Handling

### ✅ CORRECT Pattern

```typescript
// Custom error classes for different failure types
export class RuntimeInitializationError extends Error {
  constructor(message: string, public cause?: Error) {
    super(message);
    this.name = 'RuntimeInitializationError';
  }
}

export class ServiceStartupError extends Error {
  constructor(serviceName: string, cause?: Error) {
    super(`Failed to start service: ${serviceName}`);
    this.name = 'ServiceStartupError';
    this.cause = cause;
  }
}

// Usage in runtime initialization
async function initializeWithErrorHandling(): Promise<AgentRuntime> {
  try {
    const runtime = new AgentRuntime(config);
    await runtime.initialize();
    return runtime;
  } catch (error) {
    if (error instanceof ServiceStartupError) {
      // Handle service-specific errors
      console.error('Service failed:', error.message);
      // Maybe retry or use fallback
    } else if (error instanceof RuntimeInitializationError) {
      // Handle initialization errors
      console.error('Runtime init failed:', error.message);
      // Fatal - cannot continue
    }
    throw error;
  }
}
```

### ❌ INCORRECT Anti-Pattern

```typescript
// DON'T: Ignore errors or use generic handling
try {
  await runtime.initialize();
} catch (e) {
  console.log('error');  // ❌ No proper handling
}
```

---

## State Composition

### ✅ CORRECT Pattern

```typescript
// Runtime automatically composes state from:
// 1. Conversation history
// 2. Provider contributions
// 3. Memory retrievals
// 4. Agent capabilities

const state = await runtime.composeState(message, {
  providers: ['FACTS', 'RECENT_MESSAGES', 'CAPABILITIES'],
  includeProviders: true
});

// State contains:
// - messages: Memory[]
// - facts: string[]
// - providers: Record<string, ProviderResult>
// - context: string (formatted for LLM)
```

### ❌ INCORRECT Anti-Pattern

```typescript
// DON'T: Manually build state bypassing providers
const state = {
  messages: await getMessages(),
  // ❌ Missing provider context, facts, capabilities
};
```

---

## Best Practices Summary

### DO ✅
- Centralize configuration in character definitions
- Implement comprehensive error handling with custom error classes
- Use factory patterns (Service.start()) for complex setup
- Establish health monitoring for all services
- Maintain proper logging throughout lifecycle
- Validate configuration before initialization
- Implement graceful shutdown with cleanup
- Use runtime.getService() to access services
- Allow runtime to handle dependency resolution

### DON'T ❌
- Skip validation steps during initialization
- Use minimal character configurations
- Manually instantiate services outside runtime
- Bypass runtime's dependency resolution
- Ignore error handling in critical paths
- Skip health checks for long-running services
- Forget to implement graceful shutdown
- Hardcode configuration values
- Use global state instead of service encapsulation

---

## Validation Checklist

Before deploying any agent runtime:

- [ ] Character has comprehensive bio and personality
- [ ] All required environment variables validated
- [ ] Database adapter properly configured
- [ ] Error handling implemented at each lifecycle stage
- [ ] Health checks configured for services
- [ ] Graceful shutdown handlers registered
- [ ] Plugins loaded in correct dependency order
- [ ] Memory limits configured appropriately
- [ ] Logging and monitoring enabled
- [ ] Tests cover initialization failure scenarios

---

**Remember:** The AgentRuntime is the heart of your elizaOS agent. Proper initialization, lifecycle management, and error handling are not optional—they are essential for production reliability.

---

**Related Rules:**
- `elizaos-plugin-patterns.md` - Plugin development standards
- `elizaos-service-patterns.md` - Service implementation patterns
- `elizaos-testing-standards.md` - Testing requirements
