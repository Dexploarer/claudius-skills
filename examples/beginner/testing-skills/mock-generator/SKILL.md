---
name: mock-generator
description: Generates test mocks, stubs, and fixtures for testing (Jest, Vitest, pytest, etc.). Use when user asks to "create mock", "generate stub", "mock function", "test fixtures", or "mock API response".
allowed-tools: [Read, Write, Edit, Glob, Grep]
---

# Mock Generator

Automatically generates test mocks, stubs, and fixtures for various testing frameworks.

## When to Use

- "Create a mock for this function"
- "Generate test fixtures"
- "Mock this API response"
- "Create stubs for testing"
- "Generate mock data"
- "Mock this class/module"

## Instructions

### 1. Identify What to Mock

Ask the user or analyze code to determine:
- What needs to be mocked (function, class, API, database, etc.)
- Which testing framework is used
- What the mock behavior should be
- What data the mock should return

Scan for testing framework:

```bash
# Check package.json for testing framework
grep -E "(jest|vitest|mocha|jasmine|pytest|unittest|minitest)" package.json

# Check for test files
find . -name "*.test.*" -o -name "*.spec.*" -o -name "test_*.py"
```

### 2. Determine Mock Type

**Function Mocks:**
- Simple return value
- Multiple return values
- Implementations
- Spy on function calls

**API Mocks:**
- HTTP request/response
- WebSocket messages
- GraphQL queries
- REST endpoints

**Class Mocks:**
- Instance methods
- Static methods
- Properties
- Constructors

**Module Mocks:**
- Entire module
- Partial module
- Default exports
- Named exports

### 3. Generate Mocks by Framework

## JavaScript/TypeScript Mocks

### Jest Mocks

**Simple Function Mock:**
```javascript
// Mock a simple function
const mockFn = jest.fn()
mockFn.mockReturnValue(42)

// Use in test
test('uses mocked function', () => {
  expect(mockFn()).toBe(42)
  expect(mockFn).toHaveBeenCalled()
})
```

**Function with Different Return Values:**
```javascript
const mockFn = jest.fn()
  .mockReturnValueOnce('first')
  .mockReturnValueOnce('second')
  .mockReturnValue('default')

expect(mockFn()).toBe('first')
expect(mockFn()).toBe('second')
expect(mockFn()).toBe('default')
```

**Mock Implementation:**
```javascript
const mockFn = jest.fn((x, y) => x + y)

expect(mockFn(1, 2)).toBe(3)
expect(mockFn).toHaveBeenCalledWith(1, 2)
```

**Module Mock:**
```javascript
// __mocks__/axios.js
export default {
  get: jest.fn(() => Promise.resolve({ data: {} })),
  post: jest.fn(() => Promise.resolve({ data: {} })),
}

// In test file
jest.mock('axios')
import axios from 'axios'

test('fetches data', async () => {
  axios.get.mockResolvedValue({ data: { name: 'John' } })

  const result = await fetchUser(1)

  expect(result.name).toBe('John')
  expect(axios.get).toHaveBeenCalledWith('/users/1')
})
```

**Class Mock:**
```javascript
// Mock a class
jest.mock('./Database')
import Database from './Database'

Database.mockImplementation(() => ({
  query: jest.fn().mockResolvedValue([{ id: 1, name: 'John' }]),
  connect: jest.fn().mockResolvedValue(true),
  disconnect: jest.fn().mockResolvedValue(true),
}))

test('uses database', async () => {
  const db = new Database()
  const users = await db.query('SELECT * FROM users')

  expect(users).toHaveLength(1)
  expect(db.query).toHaveBeenCalled()
})
```

**Partial Mock:**
```javascript
// Mock only specific methods
import * as utils from './utils'

jest.spyOn(utils, 'fetchData').mockResolvedValue({ data: 'mocked' })

test('uses mocked method', async () => {
  const result = await utils.fetchData()
  expect(result.data).toBe('mocked')
})
```

### Vitest Mocks

**Function Mock:**
```javascript
import { vi, expect, test } from 'vitest'

const mockFn = vi.fn()
mockFn.mockReturnValue(42)

test('uses mock', () => {
  expect(mockFn()).toBe(42)
})
```

**Module Mock:**
```javascript
// __mocks__/api.ts
import { vi } from 'vitest'

export const fetchUser = vi.fn()
export const createUser = vi.fn()

// In test
vi.mock('./api')
import { fetchUser } from './api'

test('fetches user', async () => {
  fetchUser.mockResolvedValue({ id: 1, name: 'John' })

  const user = await fetchUser(1)

  expect(user.name).toBe('John')
})
```

**Spy on Method:**
```javascript
import { vi } from 'vitest'

const obj = {
  method: () => 'original'
}

vi.spyOn(obj, 'method').mockReturnValue('mocked')

expect(obj.method()).toBe('mocked')
```

### TypeScript Mocks

**Type-Safe Mock:**
```typescript
import { vi } from 'vitest'

interface User {
  id: number
  name: string
  email: string
}

// Create type-safe mock
const mockUser: User = {
  id: 1,
  name: 'John Doe',
  email: 'john@example.com'
}

// Mock function with types
const mockFetchUser = vi.fn<[id: number], Promise<User>>()
mockFetchUser.mockResolvedValue(mockUser)
```

**Mock Factory:**
```typescript
// Create a factory for generating mocks
function createMockUser(overrides?: Partial<User>): User {
  return {
    id: 1,
    name: 'Test User',
    email: 'test@example.com',
    ...overrides
  }
}

// Use in tests
const user1 = createMockUser({ name: 'Alice' })
const user2 = createMockUser({ id: 2, email: 'bob@example.com' })
```

## Python Mocks

### unittest.mock

**Function Mock:**
```python
from unittest.mock import Mock

# Simple mock
mock_func = Mock(return_value=42)
assert mock_func() == 42
assert mock_func.called

# Mock with side effects
mock_func = Mock(side_effect=[1, 2, 3])
assert mock_func() == 1
assert mock_func() == 2
assert mock_func() == 3
```

**Patch Decorator:**
```python
from unittest.mock import patch, Mock

@patch('requests.get')
def test_fetch_data(mock_get):
    # Setup mock
    mock_response = Mock()
    mock_response.json.return_value = {'name': 'John'}
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    # Test
    result = fetch_user_data(1)

    assert result['name'] == 'John'
    mock_get.assert_called_once_with('https://api.example.com/users/1')
```

**Class Mock:**
```python
from unittest.mock import Mock, patch

@patch('database.Database')
def test_database_query(mock_database_class):
    # Setup mock instance
    mock_db = Mock()
    mock_db.query.return_value = [{'id': 1, 'name': 'John'}]
    mock_database_class.return_value = mock_db

    # Test
    db = Database()
    users = db.query('SELECT * FROM users')

    assert len(users) == 1
    assert users[0]['name'] == 'John'
    mock_db.query.assert_called_once()
```

**Context Manager Mock:**
```python
from unittest.mock import patch, mock_open

# Mock file operations
mock_data = "file contents"
with patch('builtins.open', mock_open(read_data=mock_data)):
    with open('file.txt') as f:
        content = f.read()
    assert content == mock_data
```

### pytest Fixtures

**Simple Fixture:**
```python
import pytest

@pytest.fixture
def mock_user():
    return {
        'id': 1,
        'name': 'John Doe',
        'email': 'john@example.com'
    }

def test_user_data(mock_user):
    assert mock_user['name'] == 'John Doe'
```

**Fixture with Cleanup:**
```python
@pytest.fixture
def mock_database():
    # Setup
    db = MockDatabase()
    db.connect()

    yield db  # Provide to test

    # Teardown
    db.disconnect()

def test_database_query(mock_database):
    result = mock_database.query('SELECT * FROM users')
    assert len(result) > 0
```

**Parametrized Fixture:**
```python
@pytest.fixture(params=[
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35}
])
def mock_user(request):
    return request.param

def test_user_age(mock_user):
    assert mock_user['age'] > 0
```

### pytest-mock

```python
def test_api_call(mocker):
    # Mock a function
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.json.return_value = {'status': 'ok'}

    result = fetch_data()

    assert result['status'] == 'ok'
    mock_get.assert_called_once()
```

## API Response Mocks

### REST API Mock

```javascript
// Mock fetch API
global.fetch = jest.fn(() =>
  Promise.resolve({
    ok: true,
    status: 200,
    json: async () => ({
      id: 1,
      name: 'John Doe',
      email: 'john@example.com'
    }),
    headers: new Headers({
      'Content-Type': 'application/json'
    })
  })
)

test('fetches user', async () => {
  const user = await fetchUser(1)

  expect(user.name).toBe('John Doe')
  expect(fetch).toHaveBeenCalledWith('/api/users/1')
})
```

### Mock Service Worker (MSW)

```javascript
// mocks/handlers.js
import { rest } from 'msw'

export const handlers = [
  rest.get('/api/users/:id', (req, res, ctx) => {
    const { id } = req.params

    return res(
      ctx.status(200),
      ctx.json({
        id: Number(id),
        name: 'John Doe',
        email: 'john@example.com'
      })
    )
  }),

  rest.post('/api/users', (req, res, ctx) => {
    return res(
      ctx.status(201),
      ctx.json({
        id: 123,
        ...req.body
      })
    )
  }),

  rest.get('/api/users', (req, res, ctx) => {
    return res(
      ctx.status(200),
      ctx.json([
        { id: 1, name: 'Alice' },
        { id: 2, name: 'Bob' }
      ])
    )
  })
]

// mocks/server.js
import { setupServer } from 'msw/node'
import { handlers } from './handlers'

export const server = setupServer(...handlers)

// setupTests.js
import { server } from './mocks/server'

beforeAll(() => server.listen())
afterEach(() => server.resetHandlers())
afterAll(() => server.close())
```

### GraphQL Mock

```javascript
import { graphql } from 'msw'

export const handlers = [
  graphql.query('GetUser', (req, res, ctx) => {
    const { id } = req.variables

    return res(
      ctx.data({
        user: {
          id,
          name: 'John Doe',
          email: 'john@example.com'
        }
      })
    )
  }),

  graphql.mutation('CreateUser', (req, res, ctx) => {
    const { input } = req.variables

    return res(
      ctx.data({
        createUser: {
          id: '123',
          ...input
        }
      })
    )
  })
]
```

## Database Mocks

### Prisma Mock

```typescript
import { PrismaClient } from '@prisma/client'
import { mockDeep, mockReset, DeepMockProxy } from 'jest-mock-extended'

export const prismaMock = mockDeep<PrismaClient>()

beforeEach(() => {
  mockReset(prismaMock)
})

// In test
test('creates user', async () => {
  const mockUser = { id: 1, name: 'John', email: 'john@example.com' }

  prismaMock.user.create.mockResolvedValue(mockUser)

  const user = await createUser({ name: 'John', email: 'john@example.com' })

  expect(user).toEqual(mockUser)
  expect(prismaMock.user.create).toHaveBeenCalledWith({
    data: { name: 'John', email: 'john@example.com' }
  })
})
```

### MongoDB Mock

```javascript
import { MongoMemoryServer } from 'mongodb-memory-server'
import { MongoClient } from 'mongodb'

let mongod
let client
let db

beforeAll(async () => {
  mongod = await MongoMemoryServer.create()
  const uri = mongod.getUri()
  client = new MongoClient(uri)
  await client.connect()
  db = client.db()
})

afterAll(async () => {
  await client.close()
  await mongod.stop()
})

test('inserts user', async () => {
  const users = db.collection('users')
  const user = { name: 'John', email: 'john@example.com' }

  await users.insertOne(user)

  const found = await users.findOne({ name: 'John' })
  expect(found.email).toBe('john@example.com')
})
```

## React Component Mocks

### React Testing Library

```jsx
import { render, screen } from '@testing-library/react'
import '@testing-library/jest-dom'

// Mock child component
jest.mock('./UserAvatar', () => ({
  UserAvatar: ({ name }) => <div data-testid="avatar">{name}</div>
}))

test('renders user profile', () => {
  render(<UserProfile name="John" />)

  expect(screen.getByTestId('avatar')).toHaveTextContent('John')
})
```

### Mock React Hooks

```javascript
import { renderHook } from '@testing-library/react'

// Mock useState
const mockSetState = jest.fn()
jest.spyOn(React, 'useState').mockImplementation(initial => [initial, mockSetState])

// Mock custom hook
jest.mock('./useUser')
import { useUser } from './useUser'

test('uses user hook', () => {
  useUser.mockReturnValue({
    user: { id: 1, name: 'John' },
    loading: false,
    error: null
  })

  const { result } = renderHook(() => useUser(1))

  expect(result.current.user.name).toBe('John')
})
```

## Test Fixtures and Factories

### Fixture Files

```javascript
// fixtures/users.js
export const mockUsers = [
  { id: 1, name: 'Alice', email: 'alice@example.com', role: 'admin' },
  { id: 2, name: 'Bob', email: 'bob@example.com', role: 'user' },
  { id: 3, name: 'Charlie', email: 'charlie@example.com', role: 'user' }
]

export const mockUser = mockUsers[0]

// In tests
import { mockUser, mockUsers } from './fixtures/users'

test('processes user', () => {
  const result = processUser(mockUser)
  expect(result.name).toBe('Alice')
})
```

### Factory Pattern

```javascript
// factories/userFactory.js
let userId = 1

export function createUser(overrides = {}) {
  return {
    id: userId++,
    name: 'Test User',
    email: `user${userId}@example.com`,
    role: 'user',
    createdAt: new Date(),
    ...overrides
  }
}

export function createAdmin(overrides = {}) {
  return createUser({
    role: 'admin',
    ...overrides
  })
}

// In tests
import { createUser, createAdmin } from './factories/userFactory'

test('creates user', () => {
  const user = createUser({ name: 'Alice' })
  expect(user.name).toBe('Alice')
  expect(user.role).toBe('user')
})

test('creates admin', () => {
  const admin = createAdmin({ name: 'Bob' })
  expect(admin.role).toBe('admin')
})
```

### Python Factory (factory_boy)

```python
import factory
from myapp.models import User

class UserFactory(factory.Factory):
    class Meta:
        model = User

    id = factory.Sequence(lambda n: n)
    name = factory.Faker('name')
    email = factory.Faker('email')
    role = 'user'

# In tests
def test_user_creation():
    user = UserFactory()
    assert user.name is not None
    assert '@' in user.email

def test_admin_creation():
    admin = UserFactory(role='admin')
    assert admin.role == 'admin'
```

## Best Practices

### 1. Keep Mocks Simple
```javascript
// ❌ BAD: Overly complex mock
const mock = jest.fn()
mock.mockImplementation((a, b, c) => {
  if (a > 10) {
    return b * c
  } else if (a < 5) {
    return b + c
  }
  return a + b + c
})

// ✅ GOOD: Simple, focused mock
const mock = jest.fn().mockReturnValue(42)
```

### 2. Use Factories for Complex Objects
```javascript
// ✅ GOOD: Reusable factory
function createMockUser(overrides) {
  return {
    id: 1,
    name: 'Test User',
    email: 'test@example.com',
    ...overrides
  }
}
```

### 3. Reset Mocks Between Tests
```javascript
afterEach(() => {
  jest.clearAllMocks() // Clear call history
  jest.resetAllMocks() // Clear call history + implementation
})
```

### 4. Type-Safe Mocks in TypeScript
```typescript
import { vi } from 'vitest'

const mockFn = vi.fn<[id: number], Promise<User>>()
// TypeScript ensures correct usage
mockFn(123) // ✅ OK
mockFn('abc') // ❌ TypeScript error
```

### 5. Document Mock Behavior
```javascript
// Document why mock behaves this way
test('handles rate limiting', async () => {
  // Mock returns 429 to simulate rate limiting
  fetch.mockRejectedValueOnce(new Error('Rate limited'))

  await expect(fetchData()).rejects.toThrow('Rate limited')
})
```

## Advanced Patterns

### Spy on Console
```javascript
const consoleErrorSpy = jest.spyOn(console, 'error').mockImplementation()

test('logs error', () => {
  functionThatLogs()
  expect(consoleErrorSpy).toHaveBeenCalledWith('Error occurred')
})

consoleErrorSpy.mockRestore()
```

### Mock Timers
```javascript
jest.useFakeTimers()

test('delays execution', () => {
  const callback = jest.fn()

  setTimeout(callback, 1000)

  jest.advanceTimersByTime(500)
  expect(callback).not.toHaveBeenCalled()

  jest.advanceTimersByTime(500)
  expect(callback).toHaveBeenCalled()
})

jest.useRealTimers()
```

### Mock Date
```javascript
const mockDate = new Date('2024-01-01')
jest.spyOn(global, 'Date').mockImplementation(() => mockDate)

test('uses fixed date', () => {
  const result = getCurrentDate()
  expect(result.getFullYear()).toBe(2024)
})
```
