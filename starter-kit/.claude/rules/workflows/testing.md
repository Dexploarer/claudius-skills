# Testing Workflow - Starter Kit

> **Best practices and workflows for testing in beginner projects**

---

## Overview

This guide covers testing workflows using the Starter Kit's testing capabilities:
- **Skill:** `test-helper` (auto-generates tests)
- **Command:** `/test` (runs tests)
- **Subagent:** `test-writer` (expert test generation)
- **Hooks:** Test failure alerts

---

## Testing Philosophy

### Why Test?
- ✅ Catch bugs early
- ✅ Enable refactoring
- ✅ Document behavior
- ✅ Improve code quality
- ✅ Build confidence

### Testing Pyramid (Beginner)
```
        /\
       /  \  E2E (Few)
      /----\
     /      \ Integration (Some)
    /--------\
   /          \ Unit Tests (Many)
  /____________\
```

**Focus:** Start with unit tests, add integration tests as needed.

---

## Available Testing Tools

### 1. test-helper Skill (Auto-Invoked)
**Best For:** Quick test generation
**Triggers:** "write tests", "add tests", "test this function"

**Example:**
```
You: "Can you write tests for this authentication function?"

Claude: [test-helper skill activates]
        Creates unit tests with:
        - Happy path
        - Edge cases
        - Error scenarios
```

### 2. /test Command (Manual)
**Best For:** Running existing tests
**Usage:** `/test` or `/test specific-file.test.js`

**Example:**
```
You: /test

Claude: Running tests...
        Test Suites: 8 passed
        Tests: 42 passed
        Coverage: 87.3%
```

### 3. test-writer Subagent (Expert)
**Best For:** Comprehensive test suite creation
**Usage:** "Use test-writer subagent to create tests for X"

**Example:**
```
You: "Use test-writer subagent to generate comprehensive tests for the user service"

Claude: [test-writer creates]:
        - Complete test suite
        - All edge cases
        - Integration tests
        - Mocking setup
        - Documentation
```

---

## Testing Workflows

### Workflow 1: New Function → Tests
**When:** After writing a new function

```
1. Write function
2. "Write tests for this function" → test-helper activates
3. Review generated tests
4. /test → Run tests
5. Adjust tests if needed
6. /commit → Commit code + tests together
```

**Example:**
```javascript
// 1. Write function
function calculateTotal(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}

// 2. Request tests
You: "Write tests for calculateTotal"

// 3. test-helper generates
describe('calculateTotal', () => {
  it('should sum item prices', () => {
    const items = [
      { price: 10 },
      { price: 20 },
      { price: 30 }
    ];
    expect(calculateTotal(items)).toBe(60);
  });

  it('should return 0 for empty array', () => {
    expect(calculateTotal([])).toBe(0);
  });

  it('should handle single item', () => {
    expect(calculateTotal([{ price: 42 }])).toBe(42);
  });

  it('should handle negative prices', () => {
    const items = [{ price: -10 }, { price: 20 }];
    expect(calculateTotal(items)).toBe(10);
  });
});

// 4. Run tests
You: /test

// 5. All pass! Commit
You: /commit
```

---

### Workflow 2: Fix Bug → Add Test
**When:** Fixing a bug

```
1. Bug reported
2. Reproduce bug
3. Write failing test (TDD)
4. Fix the bug
5. Test passes
6. /commit with bug fix + test
```

**Example:**
```javascript
// 1. Bug: calculateTotal fails with null prices

// 2. Reproduce
const items = [{ price: 10 }, { price: null }];
calculateTotal(items); // Returns NaN (bug!)

// 3. Write failing test
it('should handle null prices', () => {
  const items = [{ price: 10 }, { price: null }];
  expect(calculateTotal(items)).toBe(10);
});

// Test fails ✗

// 4. Fix bug
function calculateTotal(items) {
  return items.reduce((sum, item) =>
    sum + (item.price || 0), 0
  );
}

// 5. Test passes ✓

// 6. Commit
You: /commit
```

---

### Workflow 3: Refactor → Ensure Tests Pass
**When:** Improving code structure

```
1. /test → Run tests (baseline)
2. Refactor code
3. /test → Ensure still passing
4. If tests fail: fix code or tests
5. /commit → Commit refactored code
```

**Example:**
```javascript
// 1. Initial tests all pass ✓

// 2. Refactor: Extract validation
function calculateTotal(items) {
  validateItems(items);
  return items.reduce((sum, item) =>
    sum + (item.price || 0), 0
  );
}

function validateItems(items) {
  if (!Array.isArray(items)) {
    throw new Error('Items must be an array');
  }
}

// 3. Run tests
You: /test

// Some tests fail! (missing validation tests)

// 4. Add validation tests
it('should throw if items not an array', () => {
  expect(() => calculateTotal(null))
    .toThrow('Items must be an array');
});

// 5. All tests pass ✓
You: /commit
```

---

### Workflow 4: Code Review → Check Coverage
**When:** Before merging/deploying

```
1. /review → Code review
2. /test → Check coverage
3. Add tests for uncovered code
4. /review → Final check
5. /commit → Ready to merge
```

---

## Test-Driven Development (TDD)

### TDD Cycle: Red → Green → Refactor

**Red:** Write failing test
```javascript
describe('User.create', () => {
  it('should create user with valid data', async () => {
    const user = await User.create({
      email: 'test@example.com',
      password: 'Pass123!'
    });

    expect(user.id).toBeDefined();
    expect(user.email).toBe('test@example.com');
  });
});
// Test fails ✗ (User.create doesn't exist)
```

**Green:** Write minimum code to pass
```javascript
class User {
  static async create(data) {
    return {
      id: 1,
      email: data.email
    };
  }
}
// Test passes ✓
```

**Refactor:** Improve implementation
```javascript
class User {
  static async create(data) {
    // Add validation
    if (!this.isValidEmail(data.email)) {
      throw new Error('Invalid email');
    }

    // Hash password
    const hashedPassword = await bcrypt.hash(data.password, 10);

    // Save to database
    return await db.users.insert({
      email: data.email,
      password: hashedPassword
    });
  }
}
// Tests still pass ✓
```

---

## Testing Patterns

### Pattern 1: Arrange-Act-Assert (AAA)

```javascript
it('should authenticate user with valid credentials', async () => {
  // Arrange: Set up test data
  const user = await createTestUser({
    email: 'test@example.com',
    password: 'Pass123!'
  });

  // Act: Perform the action
  const result = await auth.login({
    email: 'test@example.com',
    password: 'Pass123!'
  });

  // Assert: Verify the result
  expect(result.token).toBeDefined();
  expect(result.user.id).toBe(user.id);
});
```

### Pattern 2: Setup/Teardown

```javascript
describe('UserService', () => {
  let db;
  let userService;

  // Run before each test
  beforeEach(async () => {
    db = await createTestDatabase();
    userService = new UserService(db);
  });

  // Run after each test
  afterEach(async () => {
    await db.close();
  });

  it('test 1', async () => {
    // Fresh db for each test
  });

  it('test 2', async () => {
    // Fresh db for each test
  });
});
```

### Pattern 3: Mocking Dependencies

```javascript
// Mock external API
jest.mock('../services/email-service');

it('should send welcome email on signup', async () => {
  const emailService = require('../services/email-service');
  emailService.send.mockResolvedValue({ success: true });

  await user.signup({ email: 'test@example.com' });

  expect(emailService.send).toHaveBeenCalledWith({
    to: 'test@example.com',
    subject: 'Welcome!',
    template: 'welcome'
  });
});
```

---

## Test Organization

### File Structure
```
src/
  services/
    user-service.js

tests/
  services/
    user-service.test.js

# Or co-located:
src/
  services/
    user-service.js
    user-service.test.js
```

### Test Naming
```javascript
// ✅ Good: Descriptive test names
it('should return null when user not found')
it('should throw ValidationError for invalid email')
it('should hash password before saving')

// ❌ Bad: Vague test names
it('works')
it('test user')
it('should return value')
```

### Test Grouping
```javascript
describe('UserService', () => {
  describe('create', () => {
    describe('with valid data', () => {
      it('should create user')
      it('should hash password')
      it('should return user object')
    });

    describe('with invalid data', () => {
      it('should reject invalid email')
      it('should reject weak password')
    });
  });

  describe('findById', () => {
    // ...
  });
});
```

---

## Coverage Goals

### What to Aim For (Beginner Level)

| Coverage Type | Beginner Goal | Good | Excellent |
|--------------|---------------|------|-----------|
| **Lines** | 60%+ | 80%+ | 90%+ |
| **Functions** | 70%+ | 85%+ | 95%+ |
| **Branches** | 50%+ | 75%+ | 85%+ |

### What to Test First

**Priority 1 (Must Test):**
- Authentication/authorization
- Payment processing
- Data validation
- Security-critical functions

**Priority 2 (Should Test):**
- Business logic
- API endpoints
- Database operations
- Error handling

**Priority 3 (Nice to Test):**
- UI components
- Utility functions
- Simple getters/setters

---

## Using Test Tools Together

### Example: Comprehensive Testing Workflow

```
1. Feature request: User registration

2. "Use test-writer subagent to create comprehensive tests for user registration"
   → Generates complete test suite

3. Review tests, implement feature following TDD

4. /test
   → Run test suite

5. Hook triggers: "📝 File modified: Write"
   → Confirms test file created

6. /test
   → Coverage: 65% (needs more!)

7. "Write tests for the password validation edge cases"
   → test-helper adds more tests

8. /test
   → Coverage: 85% ✓

9. /review
   → Checks test quality

10. /commit
    → Hook: "⚠️ Potential secret detected"
    → Fix: Remove hardcoded test password

11. /commit
    → Success! Feature complete with tests
```

---

## Common Testing Mistakes (Beginner)

### ❌ Mistake 1: Testing Implementation Details
```javascript
// Bad: Testing internal state
it('should set isLoading to true', () => {
  expect(component.state.isLoading).toBe(true);
});

// Good: Testing behavior
it('should show loading spinner during fetch', () => {
  expect(screen.getByRole('status')).toBeInTheDocument();
});
```

### ❌ Mistake 2: No Assertions
```javascript
// Bad: No verification
it('should create user', async () => {
  await User.create({ email: 'test@example.com' });
  // Test passes but doesn't verify anything!
});

// Good: Assert the result
it('should create user', async () => {
  const user = await User.create({ email: 'test@example.com' });
  expect(user.id).toBeDefined();
  expect(user.email).toBe('test@example.com');
});
```

### ❌ Mistake 3: Tests Depend on Each Other
```javascript
// Bad: Tests share state
let userId;

it('should create user', async () => {
  const user = await User.create({...});
  userId = user.id; // Global state!
});

it('should find user', async () => {
  const user = await User.findById(userId); // Depends on previous test!
});

// Good: Independent tests
it('should find user', async () => {
  const user = await createTestUser(); // Fresh user each time
  const found = await User.findById(user.id);
  expect(found).toBeDefined();
});
```

---

## Testing Frameworks

### JavaScript/TypeScript
**Jest (Recommended for beginners)**
```bash
npm install --save-dev jest

# package.json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage"
  }
}
```

**Vitest (Modern alternative)**
```bash
npm install --save-dev vitest

# Faster, better for Vite projects
```

### Python
**pytest (Recommended)**
```bash
pip install pytest

# Run tests
pytest
pytest --cov
```

---

## Quick Reference

### Generate Tests
```
"Write tests for this function"           → test-helper skill
"Use test-writer subagent for X"         → Comprehensive tests
```

### Run Tests
```
/test                    → Run all tests
/test path/to/test.js    → Run specific test
```

### Check Coverage
```
npm test -- --coverage
pytest --cov
```

### Testing Commands
```
/test              → Run tests
/review            → Check test quality
/commit            → Commit with tests
```

---

## Next Steps

**When You've Mastered Starter Kit Testing:**
- Integration testing patterns
- E2E testing with Playwright/Cypress
- Performance testing
- Load testing
- Snapshot testing

**Advanced Testing:**
- Intermediate Kit testing workflows
- Framework-specific testing (React Testing Library, etc.)
- CI/CD integration
- Test automation

**Reference:** `@intermediate-kit/.claude/rules/workflows/testing.md`

---

**Difficulty:** Beginner
**Tools Used:** test-helper, /test, test-writer
**Coverage Goal:** 80%+
**Last Updated:** 2025-11-01

