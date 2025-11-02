# ElizaOS Plugin Architecture Patterns

**Version:** 1.0.0
**Based on:** Official elizaOS v2 Plugin System
**Purpose:** Standards for building production-ready elizaOS plugins

---

## Core Understanding

**Plugins are self-contained modules** that extend agent capabilities through registration with `AgentRuntime`, which acts as the central control system.

A plugin can provide:
- **Services**: Long-running stateful components (databases, APIs, caches)
- **Actions**: Operations agents can perform (send email, transfer funds)
- **Providers**: Context injection into agent state (time, balance, facts)
- **Evaluators**: Post-interaction processing (quality checks, logging)
- **Models**: Custom AI model implementations

---

## Plugin Interface Structure

###✅ CORRECT Pattern

```typescript
import type { Plugin, Action, Provider, Service, Evaluator } from '@elizaos/core';

export const myPlugin: Plugin = {
  // === IDENTITY ===
  name: '@my-org/plugin-name',  // NPM-style naming
  description: 'Clear description of plugin purpose',

  // === DEPENDENCIES ===
  dependencies: [
    '@elizaos/plugin-bootstrap',  // Core dependency
    '@elizaos/plugin-sql'         // Database access
  ],
  priority: 100,  // Lower = higher priority

  // === LIFECYCLE ===
  async init(config: any, runtime: IAgentRuntime): Promise<void> {
    // CRITICAL: This is the ONLY guaranteed point where
    // dependency services are available

    // 1. Validate configuration
    if (!config.apiKey) {
      throw new Error('API key is required');
    }

    // 2. Verify dependencies
    const dbService = runtime.getService('DATABASE');
    if (!dbService) {
      throw new Error('Database service is required');
    }

    // 3. Initialize plugin-specific resources
    await this.setupResources(runtime);

    console.log(`✅ ${this.name} initialized`);
  },

  // === CAPABILITIES ===
  services: [MyService],
  actions: [myAction],
  providers: [myProvider],
  evaluators: [myEvaluator]
};

export default myPlugin;
```

### ❌ INCORRECT Anti-Pattern

```typescript
// DON'T: Missing critical fields and validation
export const badPlugin = {
  name: 'plugin',  // ❌ Not NPM-style
  // ❌ Missing description
  // ❌ Missing dependencies declaration
  actions: [someAction],
  // ❌ No init() function - missing validation
};
```

---

## Plugin Lifecycle

### Load Order (Managed by Runtime)

```
1. Dependency Resolution
   └─> Runtime recursively scans plugin.dependencies[]

2. Topological Sorting
   └─> Creates linear load order (dependencies first)

3. Registration
   └─> Iterates through sorted list calling registerPlugin()

4. Initialization
   └─> Calls plugin.init() - dependency services available

5. Component Registration
   └─> Services, Actions, Providers, Evaluators registered

6. Ready
   └─> Plugin fully loaded and operational
```

**Critical**: Always declare dependencies explicitly. Runtime uses this for correct ordering.

---

## Service Pattern

### ✅ CORRECT Pattern

```typescript
import { Service, ServiceTypeName, type IAgentRuntime } from '@elizaos/core';

export class CacheService extends Service {
  // Unique service identifier
  static serviceType: ServiceTypeName = 'CACHE' as ServiceTypeName;

  // Service description for capabilities
  capabilityDescription = 'In-memory caching with TTL support';

  private cache: Map<string, CacheEntry> = new Map();
  private cleanupInterval: NodeJS.Timeout | null = null;

  constructor(runtime: IAgentRuntime) {
    super(runtime);
  }

  // Factory method - REQUIRED
  static async start(runtime: IAgentRuntime): Promise<Service> {
    const service = new CacheService(runtime);
    await service.initialize();
    return service;
  }

  private async initialize(): Promise<void> {
    try {
      // Setup cleanup interval
      this.cleanupInterval = setInterval(() => {
        this.cleanup();
      }, 60000); // Every minute

      console.log('✅ Cache service initialized');
    } catch (error) {
      console.error('❌ Cache initialization failed:', error);
      throw error;
    }
  }

  // Cleanup - REQUIRED
  async stop(): Promise<void> {
    if (this.cleanupInterval) {
      clearInterval(this.cleanupInterval);
    }
    this.cache.clear();
    console.log('✅ Cache service stopped');
  }

  // Service methods
  async get<T>(key: string): Promise<T | null> {
    const entry = this.cache.get(key);
    if (!entry) return null;

    if (Date.now() > entry.expires) {
      this.cache.delete(key);
      return null;
    }

    return entry.value as T;
  }

  async set(key: string, value: any, ttl: number = 300000): Promise<void> {
    this.cache.set(key, {
      value,
      expires: Date.now() + ttl
    });
  }

  private cleanup(): void {
    const now = Date.now();
    for (const [key, entry] of this.cache.entries()) {
      if (now > entry.expires) {
        this.cache.delete(key);
      }
    }
  }
}

interface CacheEntry {
  value: any;
  expires: number;
}
```

### ❌ INCORRECT Anti-Pattern

```typescript
// DON'T: Missing lifecycle management
export class BadCacheService extends Service {
  static serviceType = 'CACHE';

  // ❌ No static start() method
  // ❌ No initialization
  // ❌ No cleanup in stop()

  async stop(): Promise<void> {
    // ❌ Empty - no resource cleanup
  }
}
```

---

## Action Pattern

### ✅ CORRECT Pattern

```typescript
import { type Action, type IAgentRuntime, type Memory, type State } from '@elizaos/core';
import { z } from 'zod';

// Input validation schema
const sendEmailSchema = z.object({
  to: z.string().email(),
  subject: z.string().min(1),
  body: z.string().min(1)
});

export const sendEmailAction: Action = {
  // Unique action identifier
  name: 'SEND_EMAIL',

  // Similar names for LLM matching
  similes: [
    'EMAIL',
    'SEND_MESSAGE',
    'MAIL',
    'SEND_EMAIL_TO'
  ],

  // Clear description for LLM
  description: 'Send an email to a recipient with subject and body',

  // Training examples for LLM
  examples: [
    [
      {
        name: "{{user}}",
        content: { text: "Send an email to john@example.com about the meeting" }
      },
      {
        name: "{{agentName}}",
        content: {
          text: "I'll send that email for you",
          action: "SEND_EMAIL"
        }
      }
    ]
  ],

  // Validation - determines if action is available
  validate: async (
    runtime: IAgentRuntime,
    message: Memory,
    state?: State
  ): Promise<boolean> {
    try {
      // 1. Check if email service is available
      const emailService = runtime.getService('EMAIL');
      if (!emailService) {
        console.log('Email service not available');
        return false;
      }

      // 2. Extract parameters
      const params = extractEmailParams(message);

      // 3. Validate with Zod
      sendEmailSchema.parse(params);

      // 4. Check permissions (if needed)
      if (!hasEmailPermission(runtime, message)) {
        return false;
      }

      return true;
    } catch (error) {
      console.error('Email action validation failed:', error);
      return false;
    }
  },

  // Handler - executes the action
  handler: async (
    runtime: IAgentRuntime,
    message: Memory,
    state?: State,
    options?: any,
    callback?: (response: any) => void
  ): Promise<string | null> {
    try {
      // 1. Extract and validate parameters
      const params = extractEmailParams(message);
      const validated = sendEmailSchema.parse(params);

      // 2. Send progress update
      if (callback) {
        callback({
          text: 'Sending email...',
          action: 'SEND_EMAIL'
        });
      }

      // 3. Get email service
      const emailService = runtime.getService<EmailService>('EMAIL');
      if (!emailService) {
        throw new Error('Email service not available');
      }

      // 4. Execute action
      const result = await emailService.send({
        to: validated.to,
        subject: validated.subject,
        body: validated.body
      });

      // 5. Store result in memory
      await runtime.createMemory({
        entityId: runtime.agentId,
        roomId: message.roomId,
        content: {
          text: `Email sent to ${validated.to}`,
          metadata: {
            action: 'SEND_EMAIL',
            messageId: result.messageId
          }
        }
      });

      // 6. Return success message
      return `✅ Email sent successfully to ${validated.to}`;

    } catch (error) {
      console.error('Email action failed:', error);

      // Return user-friendly error
      if (error instanceof z.ZodError) {
        return `❌ Invalid email parameters: ${error.message}`;
      }

      return `❌ Failed to send email: ${error.message}`;
    }
  }
};

// Helper functions
function extractEmailParams(message: Memory): any {
  // Extract from message content
  return {
    to: message.content.to,
    subject: message.content.subject,
    body: message.content.body
  };
}

function hasEmailPermission(runtime: IAgentRuntime, message: Memory): boolean {
  // Check user permissions
  return true;
}
```

### ❌ INCORRECT Anti-Pattern

```typescript
// DON'T: Missing validation and error handling
export const badAction: Action = {
  name: 'EMAIL',
  description: 'sends email',  // ❌ Vague description
  // ❌ Missing similes
  // ❌ Missing examples
  // ❌ No validate function

  handler: async (runtime, message) => {
    // ❌ No error handling
    // ❌ No parameter validation
    // ❌ No service availability check
    await sendEmail(message.content.to, message.content.body);
    return 'sent';  // ❌ Not user-friendly
  }
};
```

---

## Provider Pattern

### ✅ CORRECT Pattern

```typescript
import { type Provider, type IAgentRuntime, type Memory, type State } from '@elizaos/core';

export const accountBalanceProvider: Provider = {
  // Unique provider identifier
  name: 'ACCOUNT_BALANCE',

  // Description for capabilities
  description: 'Provides current account balance information',

  // Optional: only execute when explicitly requested
  dynamic: false,

  // Optional: hide from public context
  private: false,

  // Execution order (lower = earlier)
  position: 100,

  // Gather and format context
  get: async (
    runtime: IAgentRuntime,
    message: Memory,
    state?: State
  ): Promise<{
    values: Record<string, any>;
    data: Record<string, any>;
    text: string;
  }> {
    try {
      // 1. Get required service
      const walletService = runtime.getService<WalletService>('WALLET');
      if (!walletService) {
        return {
          values: {},
          data: {},
          text: ''
        };
      }

      // 2. Fetch data
      const balance = await walletService.getBalance(message.entityId);
      const formatted = formatCurrency(balance);

      // 3. Return structured result
      return {
        // For template variables: {{balance}}
        values: {
          balance: formatted,
          balanceRaw: balance
        },

        // For programmatic access
        data: {
          balance,
          currency: 'USD',
          timestamp: Date.now()
        },

        // For LLM context
        text: `Current Account Balance: ${formatted}`
      };

    } catch (error) {
      console.error('Balance provider failed:', error);

      // Return empty on error - don't break state composition
      return {
        values: {},
        data: {},
        text: ''
      };
    }
  }
};

function formatCurrency(amount: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD'
  }).format(amount);
}
```

### ❌ INCORRECT Anti-Pattern

```typescript
// DON'T: Throw errors or return inconsistent structures
export const badProvider: Provider = {
  name: 'BALANCE',

  get: async (runtime, message) => {
    const balance = await getBalance();  // ❌ No error handling
    return { balance };  // ❌ Wrong structure
  }
};
```

---

## Best Practices Summary

### Plugin Organization ✅
- One plugin = one core functionality
- Declare all dependencies explicitly
- Use NPM-style naming (@org/plugin-name)
- Include comprehensive description
- Set appropriate priority for load order

### Initialization ✅
- Validate all required configuration in init()
- Check for required services
- Throw descriptive errors on failure
- Log successful initialization
- Setup resources that need cleanup

### State Management ✅
- Encapsulate state within Service classes
- Don't use global variables
- Use runtime.getService() to access services
- Implement proper cleanup in stop()
- Handle service unavailability gracefully

### Error Handling ✅
- Validate inputs with Zod or similar
- Return user-friendly error messages
- Log errors for debugging
- Don't break runtime on errors
- Implement fallback behavior where possible

### Testing ✅
- Test plugin loading and initialization
- Test each action's validate and handler
- Test provider with missing services
- Test service lifecycle (start → stop)
- Test error scenarios

---

## Anti-Patterns to Avoid ❌

### Plugin-Level
- ❌ Not declaring dependencies
- ❌ Using generic names (plugin, myPlugin)
- ❌ Skipping init() validation
- ❌ Circular dependencies

### Service-Level
- ❌ No static start() factory method
- ❌ Empty stop() implementation
- ❌ Using global state
- ❌ Not handling initialization errors

### Action-Level
- ❌ No validate() function
- ❌ Missing similes for LLM matching
- ❌ No error handling in handler
- ❌ Not using Zod for validation
- ❌ Vague descriptions

### Provider-Level
- ❌ Throwing errors instead of returning empty
- ❌ Wrong return structure
- ❌ Not checking service availability
- ❌ Expensive operations without caching

---

## Validation Checklist

Before publishing a plugin:

- [ ] NPM-style name (@org/plugin-name)
- [ ] Clear, comprehensive description
- [ ] All dependencies declared
- [ ] init() validates configuration
- [ ] All services have static start() method
- [ ] All services implement stop() properly
- [ ] All actions have validate() function
- [ ] All actions use Zod validation
- [ ] All providers handle errors gracefully
- [ ] Comprehensive error messages
- [ ] Tests cover all components
- [ ] Tests cover error scenarios
- [ ] Documentation includes examples
- [ ] README has installation instructions

---

**Remember:** Plugins extend agent capabilities, but they must be reliable, well-tested, and follow the lifecycle patterns established by the runtime. Proper initialization, validation, and cleanup are essential.

---

**Related Rules:**
- `elizaos-core-runtime.md` - Runtime lifecycle patterns
- `elizaos-service-patterns.md` - Service implementation details
- `elizaos-testing-standards.md` - Testing requirements
