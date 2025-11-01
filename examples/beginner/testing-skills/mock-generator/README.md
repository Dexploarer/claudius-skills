# Mock Generator - Beginner Example

A testing-focused skill that generates mocks, stubs, and fixtures for various testing frameworks, making test writing faster and more consistent.

## What This Example Teaches

- Test doubles (mocks, stubs, spies, fakes)
- Testing framework patterns (Jest, Vitest, pytest)
- API mocking strategies
- Database mocking techniques
- Test fixture patterns
- Factory patterns for test data

## Why Mocking Matters

### Testing Challenges Without Mocks

**Without mocks:**
- ❌ Tests depend on external services
- ❌ Slow tests (real API/DB calls)
- ❌ Flaky tests (network issues)
- ❌ Can't test error scenarios
- ❌ Expensive (API costs, DB setup)

**With mocks:**
- ✅ Fast, isolated tests
- ✅ Reliable, repeatable results
- ✅ Easy error scenario testing
- ✅ No external dependencies
- ✅ Free to run unlimited times

### Real-World Impact

```
Test Suite Without Mocks:
- Duration: 8 minutes
- Flakiness: 15% failure rate
- API costs: $50/month
- Setup complexity: High

Test Suite With Mocks:
- Duration: 12 seconds (40x faster)
- Flakiness: 0% failure rate
- API costs: $0
- Setup complexity: Low
```

## How to Use

### 1. Install the Skill

```bash
# Copy to your Claude config
cp SKILL.md ~/.claude/skills/mock-generator.md

# Or for project-specific
cp SKILL.md your-project/.claude/skills/mock-generator.md
```

### 2. Generate Mocks

```bash
cd your-project
claude

# Then ask:
"Create a mock for the fetchUser function"
"Generate test fixtures for user data"
"Mock the database connection"
"Create API response mocks"
"Generate Jest mocks for this module"
```

## Example Usage Scenarios

### Scenario 1: Basic Function Mock

**You:**
```
I need to mock this function:

async function fetchUser(id) {
  const response = await fetch(`/api/users/${id}`)
  return response.json()
}

Using Jest.
```

**Claude (using mock-generator skill):**
```
Creating Jest mock for fetchUser function...

✅ Mock created!

```javascript
// __tests__/fetchUser.test.js
import { fetchUser } from './api'

// Mock the global fetch
global.fetch = jest.fn()

describe('fetchUser', () => {
  beforeEach(() => {
    // Reset mock before each test
    fetch.mockClear()
  })

  it('fetches user successfully', async () => {
    // Setup mock response
    const mockUser = {
      id: 1,
      name: 'John Doe',
      email: 'john@example.com'
    }

    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockUser
    })

    // Test
    const user = await fetchUser(1)

    // Assertions
    expect(user).toEqual(mockUser)
    expect(fetch).toHaveBeenCalledWith('/api/users/1')
    expect(fetch).toHaveBeenCalledTimes(1)
  })

  it('handles fetch errors', async () => {
    // Setup mock to reject
    fetch.mockRejectedValueOnce(new Error('Network error'))

    // Test
    await expect(fetchUser(1)).rejects.toThrow('Network error')
  })

  it('handles 404 responses', async () => {
    // Setup mock 404 response
    fetch.mockResolvedValueOnce({
      ok: false,
      status: 404,
      json: async () => ({ error: 'User not found' })
    })

    const user = await fetchUser(999)

    expect(user.error).toBe('User not found')
  })
})
```

This mock:
✓ Isolates the test (no real API calls)
✓ Tests success scenario
✓ Tests error handling
✓ Tests edge cases (404)
✓ Fast and reliable
```

### Scenario 2: Class/Module Mock

**You:**
```
Mock this database class for testing:

class Database {
  constructor(config) {
    this.config = config
  }

  async connect() {
    // Real connection logic
  }

  async query(sql) {
    // Real query logic
  }

  async disconnect() {
    // Real disconnect logic
  }
}
```

**Claude (using mock-generator skill):**
```
Creating Jest mock for Database class...

✅ Mock created!

```javascript
// __mocks__/Database.js
export default class Database {
  constructor(config) {
    this.config = config
    this.connect = jest.fn().mockResolvedValue(true)
    this.query = jest.fn()
    this.disconnect = jest.fn().mockResolvedValue(true)
  }
}

// __tests__/userService.test.js
jest.mock('../Database')
import Database from '../Database'
import UserService from '../userService'

describe('UserService', () => {
  let db
  let userService

  beforeEach(() => {
    // Create fresh mock for each test
    db = new Database({ host: 'localhost' })
    userService = new UserService(db)
  })

  it('fetches users from database', async () => {
    // Setup mock to return user data
    const mockUsers = [
      { id: 1, name: 'Alice' },
      { id: 2, name: 'Bob' }
    ]

    db.query.mockResolvedValueOnce(mockUsers)

    // Test
    const users = await userService.getAllUsers()

    // Assertions
    expect(users).toEqual(mockUsers)
    expect(db.query).toHaveBeenCalledWith('SELECT * FROM users')
    expect(db.query).toHaveBeenCalledTimes(1)
  })

  it('handles database errors', async () => {
    // Setup mock to throw error
    db.query.mockRejectedValueOnce(new Error('Connection lost'))

    // Test
    await expect(userService.getAllUsers()).rejects.toThrow('Connection lost')
  })

  it('connects to database on initialization', async () => {
    await userService.initialize()

    expect(db.connect).toHaveBeenCalled()
  })
})
```

This mock:
✓ No real database needed
✓ Tests all methods
✓ Verifies correct SQL queries
✓ Tests error scenarios
✓ Isolates unit under test
```

### Scenario 3: API Mock with MSW

**You:**
```
I'm building a React app that calls:
GET /api/users
POST /api/users
GET /api/users/:id

Can you set up comprehensive API mocking?
```

**Claude (using mock-generator skill):**
```
Setting up Mock Service Worker (MSW) for your API...

Installing MSW:
```bash
npm install --save-dev msw
```

✅ API mocks created!

```javascript
// src/mocks/handlers.js
import { rest } from 'msw'

const mockUsers = [
  { id: 1, name: 'Alice', email: 'alice@example.com' },
  { id: 2, name: 'Bob', email: 'bob@example.com' },
  { id: 3, name: 'Charlie', email: 'charlie@example.com' }
]

export const handlers = [
  // GET /api/users - List all users
  rest.get('/api/users', (req, res, ctx) => {
    // Query params
    const page = req.url.searchParams.get('page') || '1'
    const limit = req.url.searchParams.get('limit') || '10'

    return res(
      ctx.status(200),
      ctx.json({
        users: mockUsers,
        page: Number(page),
        total: mockUsers.length
      })
    )
  }),

  // POST /api/users - Create user
  rest.post('/api/users', async (req, res, ctx) => {
    const newUser = await req.json()

    // Validate
    if (!newUser.name || !newUser.email) {
      return res(
        ctx.status(400),
        ctx.json({ error: 'Name and email required' })
      )
    }

    // Success response
    return res(
      ctx.status(201),
      ctx.json({
        id: mockUsers.length + 1,
        ...newUser
      })
    )
  }),

  // GET /api/users/:id - Get single user
  rest.get('/api/users/:id', (req, res, ctx) => {
    const { id } = req.params
    const user = mockUsers.find(u => u.id === Number(id))

    if (!user) {
      return res(
        ctx.status(404),
        ctx.json({ error: 'User not found' })
      )
    }

    return res(
      ctx.status(200),
      ctx.json(user)
    )
  })
]

// src/mocks/server.js
import { setupServer } from 'msw/node'
import { handlers } from './handlers'

export const server = setupServer(...handlers)

// src/setupTests.js
import { server } from './mocks/server'

// Start server before all tests
beforeAll(() => server.listen())

// Reset handlers after each test
afterEach(() => server.resetHandlers())

// Clean up after all tests
afterAll(() => server.close())

// Example test
// src/__tests__/UserList.test.jsx
import { render, screen, waitFor } from '@testing-library/react'
import UserList from '../UserList'

test('displays users from API', async () => {
  render(<UserList />)

  // Wait for users to load
  await waitFor(() => {
    expect(screen.getByText('Alice')).toBeInTheDocument()
    expect(screen.getByText('Bob')).toBeInTheDocument()
    expect(screen.getByText('Charlie')).toBeInTheDocument()
  })
})

test('handles API errors', async () => {
  // Override handler for this test
  server.use(
    rest.get('/api/users', (req, res, ctx) => {
      return res(ctx.status(500))
    })
  )

  render(<UserList />)

  await waitFor(() => {
    expect(screen.getByText(/error/i)).toBeInTheDocument()
  })
})
```

MSW Benefits:
✓ Works with any HTTP library (fetch, axios, etc.)
✓ Network-level mocking (most realistic)
✓ Easy to override per-test
✓ Can be reused in development (src/mocks/browser.js)
✓ Great for integration tests
```

## What Makes This a Beginner Example?

### 1. Simple Concept

**Mocking is just providing fake data:**
```javascript
// Real function
const result = await fetchUser(1) // Makes real HTTP request

// Mocked function
mockFetchUser.mockReturnValue({ id: 1, name: 'Test' }) // Returns immediately
const result = mockFetchUser(1)
```

### 2. Immediate Benefits

See faster tests right away:
```javascript
// Without mocks: 5 seconds per test
// With mocks: 5 milliseconds per test
```

### 3. Clear Patterns

Most mocks follow same structure:
1. Setup mock
2. Run code
3. Assert behavior

### 4. Practical Examples

Every test needs mocks for:
- API calls
- Database queries
- File system operations
- External services
- Time-dependent code

## Common Mock Patterns

### Pattern 1: Return Value Mock

**Use when:** Function returns simple data

```javascript
const mockFn = jest.fn()
mockFn.mockReturnValue(42)

expect(mockFn()).toBe(42)
```

### Pattern 2: Resolved Promise Mock

**Use when:** Async function that succeeds

```javascript
const mockFn = jest.fn()
mockFn.mockResolvedValue({ id: 1, name: 'John' })

const result = await mockFn()
expect(result.name).toBe('John')
```

### Pattern 3: Rejected Promise Mock

**Use when:** Testing error handling

```javascript
const mockFn = jest.fn()
mockFn.mockRejectedValue(new Error('Failed'))

await expect(mockFn()).rejects.toThrow('Failed')
```

### Pattern 4: Sequential Returns

**Use when:** Function called multiple times

```javascript
const mockFn = jest.fn()
  .mockReturnValueOnce('first')
  .mockReturnValueOnce('second')
  .mockReturnValue('default')

expect(mockFn()).toBe('first')
expect(mockFn()).toBe('second')
expect(mockFn()).toBe('default')
expect(mockFn()).toBe('default')
```

### Pattern 5: Implementation Mock

**Use when:** Need custom logic

```javascript
const mockFn = jest.fn((a, b) => a + b)

expect(mockFn(2, 3)).toBe(5)
expect(mockFn).toHaveBeenCalledWith(2, 3)
```

### Pattern 6: Spy on Existing Function

**Use when:** Want to track calls but keep original behavior

```javascript
const obj = {
  method: () => 'original'
}

const spy = jest.spyOn(obj, 'method')

obj.method() // Still returns 'original'
expect(spy).toHaveBeenCalled()

// Can override after spying
spy.mockReturnValue('mocked')
```

## Testing Framework Comparison

### Jest
```javascript
// Most popular, built into Create React App
const mock = jest.fn()
mock.mockReturnValue(42)
expect(mock()).toBe(42)
```

### Vitest
```javascript
// Fast, modern, Vite-compatible
import { vi, expect } from 'vitest'

const mock = vi.fn()
mock.mockReturnValue(42)
expect(mock()).toBe(42)
```

### pytest (Python)
```python
# Built-in unittest.mock
from unittest.mock import Mock

mock = Mock(return_value=42)
assert mock() == 42
```

All follow similar patterns!

## Test Data Factories

### Simple Factory

```javascript
// factories/userFactory.js
export function createUser(overrides = {}) {
  return {
    id: Math.floor(Math.random() * 1000),
    name: 'Test User',
    email: 'test@example.com',
    role: 'user',
    createdAt: new Date(),
    ...overrides
  }
}

// In tests
const user1 = createUser({ name: 'Alice' })
const user2 = createUser({ name: 'Bob', role: 'admin' })
```

**Benefits:**
- Consistent test data
- Easy to customize
- Reduces boilerplate
- Self-documenting

### Advanced Factory with faker.js

```javascript
import { faker } from '@faker-js/faker'

export function createUser(overrides = {}) {
  return {
    id: faker.number.int({ min: 1, max: 1000 }),
    name: faker.person.fullName(),
    email: faker.internet.email(),
    avatar: faker.image.avatar(),
    address: {
      street: faker.location.streetAddress(),
      city: faker.location.city(),
      country: faker.location.country()
    },
    ...overrides
  }
}

// Generates realistic random data each time
const user = createUser()
console.log(user.name) // "Dr. Maryam Anderson"
console.log(user.email) // "maryam.anderson12@hotmail.com"
```

## Common Pitfalls and Solutions

### Pitfall 1: Not Resetting Mocks

```javascript
// ❌ BAD: Mocks persist between tests
test('test 1', () => {
  mockFn.mockReturnValue(1)
  expect(mockFn()).toBe(1)
})

test('test 2', () => {
  // Still returns 1 from test 1!
  expect(mockFn()).toBe(1)
})

// ✅ GOOD: Reset between tests
afterEach(() => {
  jest.clearAllMocks()
})
```

### Pitfall 2: Mocking Too Much

```javascript
// ❌ BAD: Mocking everything
jest.mock('./utils')
jest.mock('./helpers')
jest.mock('./api')
jest.mock('./database')
jest.mock('./cache')

// Not testing much real code!

// ✅ GOOD: Mock only external dependencies
jest.mock('./api') // External service

// Test real code
import { utils } from './utils'
import { helpers } from './helpers'
```

### Pitfall 3: Brittle Mocks

```javascript
// ❌ BAD: Overly specific assertions
expect(mockFn).toHaveBeenCalledWith({
  id: 1,
  name: 'John',
  email: 'john@example.com',
  createdAt: new Date('2024-01-01'),
  updatedAt: new Date('2024-01-01'),
  preferences: {
    theme: 'dark',
    notifications: true
  }
})

// ✅ GOOD: Test what matters
expect(mockFn).toHaveBeenCalledWith(
  expect.objectContaining({
    name: 'John',
    email: 'john@example.com'
  })
)
```

### Pitfall 4: Not Testing Mock Calls

```javascript
// ❌ BAD: Not verifying mock was called correctly
mockApi.fetchUser.mockResolvedValue({ name: 'John' })
await service.getUser(1)
// Didn't verify fetchUser was called with ID 1

// ✅ GOOD: Verify calls
mockApi.fetchUser.mockResolvedValue({ name: 'John' })
await service.getUser(1)
expect(mockApi.fetchUser).toHaveBeenCalledWith(1)
expect(mockApi.fetchUser).toHaveBeenCalledTimes(1)
```

## Real-World Example: E-commerce Checkout

```javascript
// checkout.test.js
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import { rest } from 'msw'
import { server } from './mocks/server'
import Checkout from './Checkout'

// Mock Stripe
jest.mock('@stripe/stripe-js', () => ({
  loadStripe: jest.fn(() => ({
    confirmCardPayment: jest.fn().mockResolvedValue({
      paymentIntent: { status: 'succeeded' }
    })
  }))
}))

describe('Checkout', () => {
  const mockCart = {
    items: [
      { id: 1, name: 'Widget', price: 19.99, quantity: 2 },
      { id: 2, name: 'Gadget', price: 29.99, quantity: 1 }
    ],
    total: 69.97
  }

  beforeEach(() => {
    // Mock cart API
    server.use(
      rest.get('/api/cart', (req, res, ctx) => {
        return res(ctx.json(mockCart))
      }),

      rest.post('/api/orders', async (req, res, ctx) => {
        const order = await req.json()
        return res(ctx.json({
          id: '12345',
          status: 'confirmed',
          ...order
        }))
      })
    )
  })

  it('completes checkout successfully', async () => {
    render(<Checkout />)

    // Wait for cart to load
    await waitFor(() => {
      expect(screen.getByText('Widget')).toBeInTheDocument()
      expect(screen.getByText('$69.97')).toBeInTheDocument()
    })

    // Fill in form
    fireEvent.change(screen.getByLabelText('Email'), {
      target: { value: 'customer@example.com' }
    })

    fireEvent.change(screen.getByLabelText('Card Number'), {
      target: { value: '4242424242424242' }
    })

    // Submit order
    fireEvent.click(screen.getByText('Place Order'))

    // Verify success
    await waitFor(() => {
      expect(screen.getByText(/order confirmed/i)).toBeInTheDocument()
      expect(screen.getByText('12345')).toBeInTheDocument()
    })
  })

  it('handles payment failure', async () => {
    // Override Stripe mock for this test
    const mockStripe = require('@stripe/stripe-js')
    mockStripe.loadStripe.mockImplementationOnce(() => ({
      confirmCardPayment: jest.fn().mockResolvedValue({
        error: { message: 'Payment declined' }
      })
    }))

    render(<Checkout />)

    await waitFor(() => screen.getByText('Widget'))

    fireEvent.change(screen.getByLabelText('Email'), {
      target: { value: 'customer@example.com' }
    })

    fireEvent.click(screen.getByText('Place Order'))

    await waitFor(() => {
      expect(screen.getByText(/payment declined/i)).toBeInTheDocument()
    })
  })

  it('handles out of stock items', async () => {
    // Mock API to return out of stock error
    server.use(
      rest.post('/api/orders', (req, res, ctx) => {
        return res(
          ctx.status(400),
          ctx.json({ error: 'Widget is out of stock' })
        )
      })
    )

    render(<Checkout />)

    await waitFor(() => screen.getByText('Widget'))

    fireEvent.click(screen.getByText('Place Order'))

    await waitFor(() => {
      expect(screen.getByText(/out of stock/i)).toBeInTheDocument()
    })
  })
})
```

## Best Practices Checklist

When creating mocks:

- [ ] Reset mocks between tests (afterEach)
- [ ] Mock only external dependencies
- [ ] Use factories for complex test data
- [ ] Verify mock calls and arguments
- [ ] Test both success and error cases
- [ ] Keep mocks simple and focused
- [ ] Document why you're mocking
- [ ] Use type-safe mocks (TypeScript)
- [ ] Test edge cases (404, timeout, etc.)
- [ ] Group related mocks in setup files

## Resources

### Libraries
- [Jest](https://jestjs.io/) - JavaScript testing framework
- [Vitest](https://vitest.dev/) - Fast unit test framework
- [MSW](https://mswjs.io/) - API mocking library
- [faker.js](https://fakerjs.dev/) - Generate fake data
- [jest-mock-extended](https://github.com/marchaos/jest-mock-extended) - TypeScript mocks

### Learning
- [Kent C. Dodds: Common Testing Mistakes](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library)
- [Testing Library](https://testing-library.com/) - Testing best practices
- [Python Mock Documentation](https://docs.python.org/3/library/unittest.mock.html)

## Files

- `SKILL.md` - The skill file (copy to `.claude/skills/`)
- `README.md` - This comprehensive documentation

## Related Skills

- **test-runner** - Run tests automatically
- **code-coverage** - Measure test coverage
- **factory-generator** - Advanced test data factories
- **api-mocker** - Specialized API mocking

---

**Start mocking! Your tests will be faster and more reliable.** ✅
