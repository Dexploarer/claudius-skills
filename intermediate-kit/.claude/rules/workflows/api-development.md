# API Development Workflow - Intermediate Kit

> **RESTful and GraphQL API development best practices**

---

## 🎯 Overview

This workflow covers end-to-end API development using the Intermediate Kit capabilities.

**Related Skills:**
- `express-api-generator` - Express.js REST APIs
- `fastapi-generator` - Python FastAPI
- `django-model-helper` - Django REST Framework
- `graphql-schema-generator` - GraphQL APIs
- `api-documentation-generator` - OpenAPI/Swagger

**Related Commands:**
- `/api-docs-generate` - Generate API documentation
- `/security-audit` - Security validation
- `/migration-create` - Database migrations

**Related Agents:**
- `api-designer` - API architecture design
- `security-auditor` - API security review
- `database-architect` - Data model design

---

## 📋 API Development Process

### Phase 1: Planning & Design

**Step 1: Use api-designer for Architecture**
```
"Use api-designer to design a RESTful API for user management"
```

**Outputs:**
- Resource endpoints
- HTTP methods
- Request/response schemas
- Authentication strategy
- Versioning approach

**Step 2: Use database-architect for Data Model**
```
"Use database-architect to design the database schema for users, posts, and comments"
```

**Outputs:**
- Normalized schema
- Relationships
- Indexes
- Constraints

---

### Phase 2: Implementation

**Step 3: Generate API Endpoints**

**For Express.js:**
```
"Create Express API endpoints for user management with CRUD operations"
```

**For FastAPI:**
```
"Create FastAPI endpoints for user management with Pydantic validation"
```

**For Django:**
```
"Create Django models and ViewSets for user management"
```

**Step 4: Create Database Migrations**
```
/migration-create add_users_table
```

---

### Phase 3: Documentation

**Step 5: Generate API Documentation**
```
/api-docs-generate
```

**Outputs:**
- OpenAPI 3.0 specification
- Interactive Swagger UI
- Request/response examples
- Authentication documentation

---

### Phase 4: Testing

**Step 6: Write Tests**
```
"Write integration tests for the user API endpoints"
```

**Step 7: Run Tests**
```
npm test  # or pytest, etc.
```

---

### Phase 5: Security & Deployment

**Step 8: Security Audit**
```
/security-audit
```

**Checks:**
- Input validation
- Authentication/authorization
- SQL injection prevention
- Rate limiting
- CORS configuration

**Step 9: Deploy**
```
/deploy staging
```

---

## 🛠️ RESTful API Best Practices

### 1. Resource Naming

**Good:**
```
GET    /api/v1/users
GET    /api/v1/users/:id
POST   /api/v1/users
PUT    /api/v1/users/:id
DELETE /api/v1/users/:id
```

**Bad:**
```
GET    /api/v1/getAllUsers
POST   /api/v1/createUser
```

### 2. HTTP Status Codes

```
200 OK - Successful GET, PUT, PATCH
201 Created - Successful POST
204 No Content - Successful DELETE
400 Bad Request - Validation error
401 Unauthorized - Missing/invalid auth
403 Forbidden - Insufficient permissions
404 Not Found - Resource doesn't exist
422 Unprocessable Entity - Validation error
500 Internal Server Error - Server error
```

### 3. Request/Response Format

**Request:**
```json
POST /api/v1/users
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": "123",
  "name": "John Doe",
  "email": "john@example.com",
  "createdAt": "2025-11-01T14:30:00Z"
}
```

### 4. Error Responses

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "field": "email",
    "timestamp": "2025-11-01T14:30:00Z"
  }
}
```

---

## 🔐 Authentication Patterns

### 1. JWT Authentication

```typescript
// Express.js
app.post('/api/v1/auth/login', async (req, res) => {
  const { email, password } = req.body;
  const user = await User.findOne({ email });

  if (!user || !await bcrypt.compare(password, user.passwordHash)) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }

  const token = jwt.sign({ userId: user.id }, process.env.JWT_SECRET, {
    expiresIn: '24h'
  });

  res.json({ token, user: { id: user.id, email: user.email } });
});

// Middleware
const authMiddleware = (req, res, next) => {
  const token = req.headers.authorization?.replace('Bearer ', '');

  try {
    const payload = jwt.verify(token, process.env.JWT_SECRET);
    req.userId = payload.userId;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
  }
};
```

### 2. API Key Authentication

```typescript
const apiKeyMiddleware = (req, res, next) => {
  const apiKey = req.headers['x-api-key'];

  if (!apiKey || !isValidApiKey(apiKey)) {
    return res.status(401).json({ error: 'Invalid API key' });
  }

  next();
};
```

---

## 📊 Pagination & Filtering

### Pagination

```
GET /api/v1/users?page=1&limit=20
```

**Response:**
```json
{
  "data": [...],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "pages": 8
  }
}
```

### Filtering

```
GET /api/v1/users?role=admin&status=active
```

### Sorting

```
GET /api/v1/users?sort=-createdAt  # Descending
GET /api/v1/users?sort=name        # Ascending
```

---

## 🚀 GraphQL API Patterns

### Schema Definition

```graphql
type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post!]!
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
}

type Query {
  user(id: ID!): User
  users(limit: Int, offset: Int): [User!]!
}

type Mutation {
  createUser(name: String!, email: String!, password: String!): User!
  updateUser(id: ID!, name: String, email: String): User!
  deleteUser(id: ID!): Boolean!
}
```

### Resolvers

```typescript
const resolvers = {
  Query: {
    user: async (_, { id }) => await User.findById(id),
    users: async (_, { limit = 10, offset = 0 }) => {
      return await User.find().limit(limit).skip(offset);
    }
  },
  Mutation: {
    createUser: async (_, { name, email, password }) => {
      const user = new User({ name, email, password });
      await user.save();
      return user;
    }
  },
  User: {
    posts: async (user) => await Post.find({ authorId: user.id })
  }
};
```

---

## 🔗 Related References

- **Skills:** `@intermediate-kit/.claude/rules/skills-reference.md`
- **Commands:** `@intermediate-kit/.claude/rules/commands-reference.md`
- **Agents:** `@intermediate-kit/.claude/rules/agents-reference.md`
- **Frameworks:** `@intermediate-kit/.claude/rules/frameworks/`

---

**Last Updated:** 2025-11-01
