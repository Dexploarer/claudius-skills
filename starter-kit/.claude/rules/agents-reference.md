# Starter Kit - Subagents Reference

> **Complete reference for all 4 beginner-level subagents**

---

## Overview

Subagents are **specialized AI consultants** with specific expertise and restricted tool access. Unlike skills (auto-invoked) and commands (workflows), subagents provide expert-level analysis in focused domains.

**Location:** `starter-kit/.claude/agents/`
**Total Agents:** 4

---

## What Are Subagents?

**Subagents = Specialized Experts with Limited Tools**

### Key Characteristics:
- **Focused Expertise:** Deep knowledge in specific domain
- **Tool Restrictions:** Only access tools needed for their role
- **Explicit Invocation:** You must call them explicitly
- **Independent Analysis:** Make autonomous decisions within scope

### When to Use Subagents:
✅ Need expert-level analysis
✅ Want focused, specialized review
✅ Require structured output
✅ Need independent assessment

### When NOT to Use Subagents:
❌ Simple questions (use skills)
❌ Quick workflows (use commands)
❌ General tasks (use main Claude)

---

## 1. code-reviewer

**File:** `starter-kit/.claude/agents/code-reviewer.md`

### Role
Comprehensive code review specialist with focus on quality, maintainability, and best practices.

### Expertise
- Code quality assessment
- Design pattern recognition
- Best practices validation
- Security analysis
- Performance review
- Maintainability evaluation

### Allowed Tools
```yaml
allowed-tools: [Read, Grep, Glob]
```
**Why these tools?**
- `Read`: Examine code files
- `Grep`: Search for patterns
- `Glob`: Find related files
**Cannot:** Modify code, run commands, write files

### Invocation
```
You: "Use code-reviewer subagent to review my authentication module"
You: "Call code-reviewer to analyze the API endpoints"
You: "code-reviewer: review src/services/"
```

### What It Does
1. **Code Quality Analysis:**
   - Complexity metrics
   - Code smells
   - Duplication detection
   - Naming conventions

2. **Architecture Review:**
   - Design patterns
   - SOLID principles
   - Separation of concerns
   - Module organization

3. **Security Assessment:**
   - Vulnerability detection
   - Security best practices
   - Input validation
   - Authentication/Authorization

4. **Performance Analysis:**
   - Inefficient algorithms
   - Memory management
   - Database query optimization
   - Caching opportunities

5. **Maintainability:**
   - Documentation quality
   - Test coverage
   - Error handling
   - Logging practices

### Example Output
```markdown
# Code Review: src/auth/authentication.ts

## Executive Summary
Quality Score: 7.5/10
Review Date: 2025-11-01
Lines Reviewed: 345
Issues Found: 12 (3 high, 5 medium, 4 low)

## Critical Issues (3)

### 1. Security: Hardcoded Secret (HIGH)
**Location:** Line 45
**Issue:** JWT secret hardcoded in source
**Impact:** Security vulnerability
**Recommendation:** Move to environment variable
```typescript
// Current (INSECURE)
const secret = 'my-secret-key';

// Recommended
const secret = process.env.JWT_SECRET;
if (!secret) throw new Error('JWT_SECRET not configured');
```

### 2. Error Handling: Unhandled Promise (HIGH)
**Location:** Line 123
**Issue:** Promise rejection not caught
**Impact:** Potential server crash
**Recommendation:** Add .catch() or try/catch

### 3. Validation: Missing Input Sanitization (HIGH)
**Location:** Line 67
**Issue:** User input not validated
**Impact:** SQL injection risk
**Recommendation:** Add input validation layer

## Medium Issues (5)
[Detailed list...]

## Low Issues (4)
[Detailed list...]

## Strengths
✓ Well-structured code organization
✓ Consistent naming conventions
✓ Good test coverage (82%)
✓ Proper use of TypeScript types

## Recommendations
1. Address security issues immediately (HIGH)
2. Add input validation layer (HIGH)
3. Improve error handling (MEDIUM)
4. Extract complex functions (LOW)
5. Add JSDoc comments (LOW)

## Code Metrics
- Cyclomatic Complexity: 8.2 (acceptable)
- Lines of Code: 345
- Test Coverage: 82%
- Documentation: 65%
```

### Best Practices
- Provide specific files/directories
- Mention review focus if any
- Review feedback carefully
- Address high-priority issues first

---

## 2. test-writer

**File:** `starter-kit/.claude/agents/test-writer.md`

### Role
Test generation expert specializing in comprehensive test coverage and testing best practices.

### Expertise
- Unit test generation
- Integration test design
- Edge case identification
- Test-driven development (TDD)
- Mocking strategies
- Coverage optimization

### Allowed Tools
```yaml
allowed-tools: [Read, Write, Grep]
```
**Why these tools?**
- `Read`: Analyze source code
- `Write`: Create test files
- `Grep`: Find existing tests
**Cannot:** Run commands, modify source code

### Invocation
```
You: "Use test-writer subagent to create tests for the user service"
You: "test-writer: generate comprehensive tests for auth.ts"
You: "Call test-writer to add edge case tests"
```

### What It Does
1. **Test Analysis:**
   - Identifies untested code
   - Analyzes code paths
   - Finds edge cases
   - Calculates coverage gaps

2. **Test Generation:**
   - Unit tests (individual functions)
   - Integration tests (component interaction)
   - Edge cases (boundary values)
   - Error scenarios
   - Happy path tests

3. **Test Organization:**
   - Proper describe/it structure
   - Logical grouping
   - Clear test names
   - Setup/teardown

4. **Mocking Strategy:**
   - Identifies dependencies
   - Creates appropriate mocks
   - Mock data generation
   - Stub creation

### Example Output
```typescript
// Generated tests for: src/services/user-service.ts

import { describe, it, expect, beforeEach, jest } from '@jest/globals';
import { UserService } from '../src/services/user-service';
import { Database } from '../src/database';

// Mock dependencies
jest.mock('../src/database');

describe('UserService', () => {
  let userService: UserService;
  let mockDb: jest.Mocked<Database>;

  beforeEach(() => {
    mockDb = new Database() as jest.Mocked<Database>;
    userService = new UserService(mockDb);
  });

  describe('createUser', () => {
    describe('happy path', () => {
      it('should create user with valid data', async () => {
        const userData = {
          email: 'test@example.com',
          password: 'StrongPass123!',
          name: 'Test User'
        };

        mockDb.insert.mockResolvedValue({ id: 1, ...userData });

        const result = await userService.createUser(userData);

        expect(result.id).toBe(1);
        expect(result.email).toBe(userData.email);
        expect(mockDb.insert).toHaveBeenCalledWith('users', expect.any(Object));
      });
    });

    describe('validation', () => {
      it('should reject invalid email format', async () => {
        const userData = {
          email: 'invalid-email',
          password: 'StrongPass123!',
          name: 'Test User'
        };

        await expect(userService.createUser(userData))
          .rejects
          .toThrow('Invalid email format');
      });

      it('should reject weak password', async () => {
        const userData = {
          email: 'test@example.com',
          password: '123',
          name: 'Test User'
        };

        await expect(userService.createUser(userData))
          .rejects
          .toThrow('Password too weak');
      });

      it('should reject missing required fields', async () => {
        const userData = {
          email: 'test@example.com'
          // missing password and name
        };

        await expect(userService.createUser(userData))
          .rejects
          .toThrow('Missing required fields');
      });
    });

    describe('edge cases', () => {
      it('should handle duplicate email', async () => {
        mockDb.insert.mockRejectedValue(new Error('UNIQUE constraint'));

        await expect(userService.createUser({
          email: 'existing@example.com',
          password: 'Pass123!',
          name: 'Test'
        })).rejects.toThrow('Email already exists');
      });

      it('should handle very long names', async () => {
        const longName = 'a'.repeat(256);

        await expect(userService.createUser({
          email: 'test@example.com',
          password: 'Pass123!',
          name: longName
        })).rejects.toThrow('Name too long');
      });

      it('should trim whitespace from inputs', async () => {
        const userData = {
          email: '  test@example.com  ',
          password: 'Pass123!',
          name: '  Test User  '
        };

        mockDb.insert.mockResolvedValue({ id: 1, ...userData });

        const result = await userService.createUser(userData);

        expect(result.email).toBe('test@example.com');
        expect(result.name).toBe('Test User');
      });
    });

    describe('database errors', () => {
      it('should handle database connection failure', async () => {
        mockDb.insert.mockRejectedValue(new Error('Connection failed'));

        await expect(userService.createUser({
          email: 'test@example.com',
          password: 'Pass123!',
          name: 'Test'
        })).rejects.toThrow('Database error');
      });

      it('should rollback on transaction failure', async () => {
        mockDb.beginTransaction = jest.fn();
        mockDb.rollback = jest.fn();
        mockDb.insert.mockRejectedValue(new Error('Insert failed'));

        await expect(userService.createUser({
          email: 'test@example.com',
          password: 'Pass123!',
          name: 'Test'
        })).rejects.toThrow();

        expect(mockDb.rollback).toHaveBeenCalled();
      });
    });
  });

  describe('getUserById', () => {
    // Similar comprehensive test structure...
  });

  describe('updateUser', () => {
    // Similar comprehensive test structure...
  });

  describe('deleteUser', () => {
    // Similar comprehensive test structure...
  });
});

// Test Coverage Summary:
// Lines: 95%
// Functions: 100%
// Branches: 92%
```

### Best Practices
- Specify testing framework (Jest, pytest, etc.)
- Mention coverage requirements
- Include integration test needs
- Request specific test types

---

## 3. doc-writer

**File:** `starter-kit/.claude/agents/doc-writer.md`

### Role
Documentation specialist focused on creating clear, comprehensive, and maintainable documentation.

### Expertise
- API documentation
- Code comments
- README files
- Architecture docs
- User guides
- Developer guides

### Allowed Tools
```yaml
allowed-tools: [Read, Write, Grep]
```
**Why these tools?**
- `Read`: Analyze code structure
- `Write`: Create documentation files
- `Grep`: Find undocumented code
**Cannot:** Modify source code, run commands

### Invocation
```
You: "Use doc-writer subagent to document the API"
You: "doc-writer: create comprehensive docs for this module"
You: "Call doc-writer to add JSDoc comments"
```

### What It Does
1. **API Documentation:**
   - Endpoint documentation
   - Request/response examples
   - Error codes
   - Authentication details

2. **Code Documentation:**
   - Function/class comments
   - Parameter descriptions
   - Return value docs
   - Usage examples

3. **User Documentation:**
   - Installation guides
   - Quick start tutorials
   - Configuration guides
   - Troubleshooting

4. **Architecture Documentation:**
   - System diagrams
   - Component descriptions
   - Data flow
   - Design decisions

### Example Output

**README.md:**
```markdown
# User Authentication Service

Complete authentication system with JWT tokens, password hashing, and session management.

## Features

- ✅ JWT-based authentication
- ✅ Bcrypt password hashing
- ✅ Session management
- ✅ Role-based access control (RBAC)
- ✅ Password reset functionality
- ✅ Email verification

## Installation

```bash
npm install @myapp/auth-service
```

## Quick Start

```typescript
import { AuthService } from '@myapp/auth-service';

const auth = new AuthService({
  jwtSecret: process.env.JWT_SECRET,
  tokenExpiry: '7d'
});

// Register user
const user = await auth.register({
  email: 'user@example.com',
  password: 'SecurePass123!',
  name: 'John Doe'
});

// Login
const session = await auth.login({
  email: 'user@example.com',
  password: 'SecurePass123!'
});

console.log(session.token); // JWT token
```

## API Reference

### `register(userData): Promise<User>`

Registers a new user account.

**Parameters:**
- `userData` (Object)
  - `email` (string, required): User's email address
  - `password` (string, required): Password (min 8 chars)
  - `name` (string, required): Full name

**Returns:** Promise<User>
- `id` (number): User ID
- `email` (string): Email address
- `name` (string): Full name
- `createdAt` (Date): Registration timestamp

**Throws:**
- `ValidationError`: Invalid input data
- `DuplicateError`: Email already exists

**Example:**
```typescript
try {
  const user = await auth.register({
    email: 'new@example.com',
    password: 'StrongPass123!',
    name: 'Jane Smith'
  });
  console.log(`User created: ${user.id}`);
} catch (error) {
  if (error instanceof DuplicateError) {
    console.error('Email already registered');
  }
}
```

[Additional endpoints documented similarly...]

## Configuration

```typescript
interface AuthConfig {
  jwtSecret: string;        // Secret for JWT signing
  tokenExpiry: string;      // Token expiration (e.g., '7d', '24h')
  bcryptRounds: number;     // Bcrypt hashing rounds (default: 10)
  sessionStore?: Store;     // Custom session store
}
```

## Environment Variables

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `JWT_SECRET` | Yes | Secret key for JWT | `your-secret-key-here` |
| `TOKEN_EXPIRY` | No | Token lifetime | `7d` (default) |
| `BCRYPT_ROUNDS` | No | Hashing strength | `10` (default) |

## Security Considerations

⚠️ **Important Security Notes:**
- Never commit JWT_SECRET to version control
- Use strong secrets (min 32 chars, random)
- Rotate secrets periodically
- Use HTTPS in production
- Implement rate limiting

## Testing

```bash
npm test                    # Run all tests
npm test -- --coverage      # With coverage
npm test auth.test.ts       # Specific test
```

## Troubleshooting

### "Invalid token" error
**Cause:** Expired or malformed JWT token
**Solution:** Request new token via login

### "Password too weak" error
**Cause:** Password doesn't meet requirements
**Requirements:**
- Minimum 8 characters
- At least one uppercase letter
- At least one number
- At least one special character

## License

MIT
```

**JSDoc Comments:**
```typescript
/**
 * Authenticates a user with email and password
 *
 * Validates credentials, generates JWT token, and creates session.
 * Implements rate limiting to prevent brute force attacks.
 *
 * @param {LoginCredentials} credentials - User login credentials
 * @param {string} credentials.email - User's email address
 * @param {string} credentials.password - User's password (plain text)
 *
 * @returns {Promise<AuthSession>} Authentication session with token
 * @returns {string} return.token - JWT access token
 * @returns {User} return.user - Authenticated user object
 * @returns {Date} return.expiresAt - Token expiration timestamp
 *
 * @throws {ValidationError} If email or password format is invalid
 * @throws {AuthenticationError} If credentials don't match
 * @throws {RateLimitError} If too many failed attempts
 *
 * @example
 * // Successful login
 * const session = await auth.login({
 *   email: 'user@example.com',
 *   password: 'MyPassword123!'
 * });
 * console.log(session.token);
 *
 * @example
 * // Handle authentication failure
 * try {
 *   await auth.login({
 *     email: 'wrong@example.com',
 *     password: 'wrongpass'
 *   });
 * } catch (error) {
 *   if (error instanceof AuthenticationError) {
 *     console.error('Invalid credentials');
 *   }
 * }
 *
 * @see {@link register} for creating new users
 * @see {@link logout} for ending sessions
 *
 * @since 1.0.0
 * @public
 */
async login(credentials: LoginCredentials): Promise<AuthSession> {
  // Implementation...
}
```

### Best Practices
- Specify documentation type needed
- Mention target audience
- Include examples in docs
- Keep docs updated with code

---

## 4. debug-helper

**File:** `starter-kit/.claude/agents/debug-helper.md`

### Role
Debugging specialist focused on identifying and resolving code issues systematically.

### Expertise
- Bug identification
- Root cause analysis
- Debugging strategies
- Error interpretation
- Performance debugging
- Memory leak detection

### Allowed Tools
```yaml
allowed-tools: [Read, Grep, Bash]
```
**Why these tools?**
- `Read`: Examine code
- `Grep`: Search for patterns
- `Bash`: Run diagnostic commands
**Cannot:** Modify code directly

### Invocation
```
You: "Use debug-helper subagent to find why tests are failing"
You: "debug-helper: investigate this memory leak"
You: "Call debug-helper to analyze the stack trace"
```

### What It Does
1. **Bug Analysis:**
   - Stack trace interpretation
   - Error message analysis
   - Log examination
   - State inspection

2. **Root Cause Investigation:**
   - Code flow tracing
   - Dependency analysis
   - Timing issues
   - State corruption

3. **Debugging Strategy:**
   - Systematic approach
   - Hypothesis formation
   - Test case isolation
   - Binary search debugging

4. **Solution Recommendations:**
   - Fix suggestions
   - Prevention strategies
   - Test improvements
   - Monitoring additions

### Example Output
```markdown
# Debug Analysis: Memory Leak in User Service

## Problem Summary
**Reported Issue:** Application memory grows continuously
**Impact:** Server crashes after ~6 hours
**Severity:** HIGH
**Status:** Root cause identified

## Investigation Process

### Step 1: Reproduce Issue
✓ Confirmed: Memory increases 50MB/hour under normal load
✓ Environment: Production and staging
✓ Trigger: Occurs during user authentication requests

### Step 2: Memory Profile Analysis
```bash
# Heap snapshot analysis
node --inspect server.js
# Chrome DevTools Memory Profiler shows:
# - EventEmitter listeners: 15,000+ (abnormal)
# - UserSession objects: 8,500+ (never cleaned)
```

### Step 3: Code Examination
**File:** `src/services/user-service.ts`
**Issue Found:** Event listeners not removed

```typescript
// PROBLEMATIC CODE (Line 45-52)
class UserService {
  async authenticateUser(credentials) {
    const session = new EventEmitter();

    // ❌ Event listener added but never removed!
    session.on('login', this.handleLogin);
    session.on('logout', this.handleLogout);

    return session;
  }
}
```

### Step 4: Root Cause
**Primary Cause:** Event listeners accumulate without cleanup
**Contributing Factors:**
1. No session cleanup on logout
2. Missing timeout for inactive sessions
3. Event emitters stored in memory indefinitely

## Solution

### Immediate Fix
```typescript
class UserService {
  async authenticateUser(credentials) {
    const session = new EventEmitter();

    // ✅ Use 'once' instead of 'on' for one-time events
    session.once('login', this.handleLogin);
    session.once('logout', this.handleLogout);

    // ✅ Add cleanup timeout
    setTimeout(() => {
      session.removeAllListeners();
    }, 1000 * 60 * 30); // 30 minute timeout

    return session;
  }

  // ✅ Add explicit cleanup method
  async cleanupSession(session) {
    session.removeAllListeners();
    session = null;
  }
}
```

### Long-term Improvements
1. **Session Management:**
   ```typescript
   // Implement session store with TTL
   const sessionStore = new Map();

   function setSession(id, data, ttl = 30 * 60 * 1000) {
     sessionStore.set(id, data);
     setTimeout(() => sessionStore.delete(id), ttl);
   }
   ```

2. **Monitoring:**
   ```typescript
   // Add memory monitoring
   setInterval(() => {
     const usage = process.memoryUsage();
     if (usage.heapUsed > THRESHOLD) {
       logger.warn('High memory usage', usage);
     }
   }, 60000);
   ```

3. **Testing:**
   ```typescript
   // Add memory leak test
   describe('Memory Leaks', () => {
     it('should not leak listeners', async () => {
       const before = process.memoryUsage().heapUsed;

       // Simulate 1000 authentications
       for (let i = 0; i < 1000; i++) {
         await userService.authenticateUser(testCreds);
       }

       const after = process.memoryUsage().heapUsed;
       const growth = after - before;

       expect(growth).toBeLessThan(10 * 1024 * 1024); // <10MB
     });
   });
   ```

## Verification Steps
1. ✅ Apply immediate fix
2. ⏳ Run memory profiler for 2 hours
3. ⏳ Monitor production metrics
4. ⏳ Run leak detection tests
5. ⏳ Deploy to staging
6. ⏳ Deploy to production

## Prevention
- Add ESLint rule: `no-unused-listeners`
- Implement session lifecycle hooks
- Add automated memory leak tests
- Monitor heap growth in production
- Set up alerts for memory thresholds

## Related Issues
- #234: Session timeout not working
- #189: Event emitter warnings in logs
```

### Best Practices
- Provide error messages/stack traces
- Include reproduction steps
- Mention environment details
- Share relevant logs

---

## Subagents Comparison Matrix

| Aspect | code-reviewer | test-writer | doc-writer | debug-helper |
|--------|--------------|-------------|------------|--------------|
| **Focus** | Quality | Testing | Documentation | Debugging |
| **Tools** | Read, Grep, Glob | Read, Write, Grep | Read, Write, Grep | Read, Grep, Bash |
| **Creates Files** | ❌ | ✅ Tests | ✅ Docs | ❌ |
| **Modifies Code** | ❌ | ❌ | ❌ | ❌ |
| **Runs Commands** | ❌ | ❌ | ❌ | ✅ Diagnostic |
| **Output Style** | Report | Code | Markdown/Code | Analysis |
| **Best For** | Pre-merge review | Coverage | Public APIs | Bug investigation |

---

## Combining Subagents

Subagents can work in sequence for comprehensive analysis:

### Example: New Feature Workflow
```
1. Write feature code
2. "Use test-writer to generate tests"
3. "Use code-reviewer to review implementation and tests"
4. "Use doc-writer to document the API"
5. Manual testing
6. "Use debug-helper if issues found"
7. Final review and merge
```

### Example: Bug Fix Workflow
```
1. Bug reported
2. "Use debug-helper to investigate root cause"
3. Apply fix
4. "Use test-writer to add regression tests"
5. "Use code-reviewer to review the fix"
6. "Use doc-writer to document the issue" (if needed)
```

---

## Advanced Usage

### Scoped Reviews
```
"Use code-reviewer to focus on security in auth.ts"
"test-writer: only integration tests for the API"
"doc-writer: just API reference, skip tutorials"
```

### Iterative Refinement
```
1. "code-reviewer: initial review"
2. Apply suggestions
3. "code-reviewer: re-review the changes"
```

---

## Troubleshooting

### Subagent Not Responding
- Check explicit invocation syntax
- Verify agent file exists
- Use clear agent name

### Wrong Output Format
- Specify desired format explicitly
- Check agent capabilities
- Review agent YAML configuration

### Limited Analysis
- Provide more context
- Specify focus areas
- Give access to related files

---

## Next Level Agents

**Ready for more advanced agents?**
- Intermediate Kit: 6 specialist agents
- Domain-specific expertise
- Advanced tool access
- Complex workflows

**Agents:** api-designer, database-architect, devops-engineer, performance-optimizer, security-auditor, system-architect

**Reference:** `@intermediate-kit/.claude/rules/agents-reference.md`

---

**Total Agents:** 4
**Difficulty:** Beginner
**Explicit Invocation:** ✅ Required
**Last Updated:** 2025-11-01

