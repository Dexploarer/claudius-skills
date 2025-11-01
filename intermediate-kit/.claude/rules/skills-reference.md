# Intermediate Kit - Skills Reference

> **Comprehensive guide to all 10 framework-specific skills**
> Auto-invoked capabilities for production-ready development

---

## 📋 Skills Overview

The Intermediate Kit includes **10 framework-specific skills** across:
- **Frontend:** React, Vue, Next.js
- **Backend:** Express.js, FastAPI, Django
- **API:** GraphQL, OpenAPI
- **Database:** Migration helpers
- **Testing:** Framework setup

All skills are located in: `intermediate-kit/.claude/skills/`

---

## 🎨 Frontend Framework Skills

### 1. react-component-generator

**File:** `intermediate-kit/.claude/skills/react-component-generator.md`

**Auto-invoked when:**
- "create React component"
- "add React component"
- "generate React component"
- "build React UI"

**Capabilities:**
- Modern React with TypeScript
- Functional components with hooks
- Props interface definitions
- State management (useState, useEffect, useContext)
- Event handler typing
- Styled-components or CSS modules
- Component documentation
- Prop validation

**Output Includes:**
- TypeScript interface for props
- Functional component with hooks
- Proper typing for all handlers
- Export statement
- Usage example in comments

**Example Trigger:**
```
You: "Create a React component for a user profile card"
Claude: [react-component-generator activates]
→ Generates TypeScript component with props interface
→ Includes useState for interactive state
→ Adds proper event handlers
→ Includes styled-components
```

**Technologies:**
- React 18+
- TypeScript
- React Hooks (useState, useEffect, useCallback, useMemo)
- Styled-components / CSS Modules
- PropTypes (if JavaScript)

---

### 2. vue-component-generator

**File:** `intermediate-kit/.claude/skills/vue-component-generator.md`

**Auto-invoked when:**
- "create Vue component"
- "add Vue component"
- "generate Vue 3 component"
- "build Vue UI"

**Capabilities:**
- Vue 3 Composition API
- `<script setup>` syntax
- TypeScript with defineProps
- Reactive state (ref, reactive, computed)
- Event emitters (defineEmits)
- Lifecycle hooks (onMounted, onUnmounted)
- Template refs
- Component documentation

**Output Includes:**
- `<template>` section
- `<script setup lang="ts">` with Composition API
- Props definition with TypeScript
- Reactive state variables
- Computed properties
- Event emitters
- `<style scoped>` section

**Example Trigger:**
```
You: "Create a Vue component for a product card with image and price"
Claude: [vue-component-generator activates]
→ Generates Vue 3 SFC with script setup
→ Includes defineProps with TypeScript
→ Adds reactive state with ref/reactive
→ Includes scoped styles
```

**Technologies:**
- Vue 3
- Composition API
- TypeScript
- `<script setup>`
- Scoped CSS / CSS Modules

---

### 3. nextjs-page-generator

**File:** `intermediate-kit/.claude/skills/nextjs-page-generator.md`

**Auto-invoked when:**
- "create Next.js page"
- "add Next page"
- "generate Next.js route"
- "create app router page"

**Capabilities:**
- Next.js App Router (app directory)
- Server Components (RSC)
- Client Components ('use client')
- Server Actions
- Metadata API
- Dynamic routes
- Loading and error states
- Layouts

**Output Includes:**
- Page component (Server or Client)
- Metadata export (title, description)
- Props with proper typing
- Data fetching (async Server Component or client hooks)
- Error boundaries
- Loading states

**Example Trigger:**
```
You: "Create a Next.js page for displaying blog posts"
Claude: [nextjs-page-generator activates]
→ Generates app router page.tsx
→ Includes async Server Component
→ Adds metadata export
→ Implements data fetching
```

**Technologies:**
- Next.js 13+ (App Router)
- React Server Components
- Server Actions
- TypeScript
- Metadata API

---

## 🔧 Backend Framework Skills

### 4. express-api-generator

**File:** `intermediate-kit/.claude/skills/express-api-generator.md`

**Auto-invoked when:**
- "create Express API"
- "add Express endpoint"
- "generate Express route"
- "build Express REST API"

**Capabilities:**
- Express.js Router
- RESTful endpoint design
- Middleware integration
- Request validation
- Error handling
- Response formatting
- Authentication middleware
- Database integration patterns

**Output Includes:**
- Router definition
- HTTP method handlers (GET, POST, PUT, DELETE)
- Request validation middleware
- Error handling
- Response status codes
- JSDoc documentation

**Example Trigger:**
```
You: "Create Express API endpoints for user management"
Claude: [express-api-generator activates]
→ Generates Express router
→ Includes CRUD operations
→ Adds validation middleware
→ Implements error handling
```

**Technologies:**
- Express.js 4+
- Express Router
- Middleware (body-parser, cors, helmet)
- Validation (express-validator, Joi)
- Error handling patterns

---

### 5. fastapi-generator

**File:** `intermediate-kit/.claude/skills/fastapi-generator.md`

**Auto-invoked when:**
- "create FastAPI endpoint"
- "add FastAPI route"
- "generate Python API"
- "build FastAPI REST API"

**Capabilities:**
- FastAPI router and endpoints
- Pydantic models for validation
- Async/await patterns
- Dependency injection
- OpenAPI automatic documentation
- Type hints
- Request/response models
- Error handling

**Output Includes:**
- FastAPI router
- Pydantic models (BaseModel)
- Async endpoint functions
- Type hints for all parameters
- Response models
- Dependency injection
- Status codes
- Automatic OpenAPI docs

**Example Trigger:**
```
You: "Create FastAPI endpoints for product catalog"
Claude: [fastapi-generator activates]
→ Generates FastAPI router
→ Creates Pydantic models
→ Implements async CRUD operations
→ Adds OpenAPI documentation
```

**Technologies:**
- FastAPI
- Pydantic (BaseModel, Field, validator)
- Python 3.7+ with async/await
- Type hints
- Dependency injection
- OpenAPI/Swagger

---

### 6. django-model-helper

**File:** `intermediate-kit/.claude/skills/django-model-helper.md`

**Auto-invoked when:**
- "create Django model"
- "add Django fields"
- "generate Django model"
- "build Django database model"

**Capabilities:**
- Django Model classes
- Field types and options
- Model relationships (ForeignKey, ManyToMany)
- Custom managers
- Model methods
- Meta options
- Signals
- Admin configuration

**Output Includes:**
- Model class definition
- Field definitions with validators
- Relationship fields
- String representation (__str__)
- Custom methods
- Meta class (ordering, indexes)
- Manager class (if needed)
- Admin class registration

**Example Trigger:**
```
You: "Create Django models for a blog with posts and comments"
Claude: [django-model-helper activates]
→ Generates Post and Comment models
→ Includes ForeignKey relationship
→ Adds fields with validators
→ Creates admin configuration
```

**Technologies:**
- Django 3.2+
- Django ORM
- Model fields
- Relationships
- Managers and QuerySets
- Django Admin

---

## 🔌 API & Documentation Skills

### 7. graphql-schema-generator

**File:** `intermediate-kit/.claude/skills/graphql-schema-generator.md`

**Auto-invoked when:**
- "create GraphQL schema"
- "add GraphQL type"
- "generate GraphQL API"
- "build GraphQL schema"

**Capabilities:**
- Type definitions
- Query definitions
- Mutation definitions
- Subscription definitions (optional)
- Resolver functions
- Input types
- Interface and Union types
- Custom scalars

**Output Includes:**
- Type definitions (SDL or code-first)
- Query resolvers
- Mutation resolvers
- Input types for mutations
- Resolver implementation patterns
- Error handling
- Field arguments with types

**Example Trigger:**
```
You: "Create GraphQL schema for a task management system"
Claude: [graphql-schema-generator activates]
→ Generates Task type definition
→ Creates queries (tasks, task)
→ Adds mutations (createTask, updateTask)
→ Includes resolver templates
```

**Technologies:**
- GraphQL
- Apollo Server / GraphQL Yoga
- Schema Definition Language (SDL)
- Resolvers
- Input types
- TypeGraphQL (TypeScript)

---

### 8. api-documentation-generator

**File:** `intermediate-kit/.claude/skills/api-documentation-generator.md`

**Auto-invoked when:**
- "document API"
- "create API docs"
- "generate OpenAPI spec"
- "add Swagger documentation"

**Capabilities:**
- OpenAPI 3.0 specification
- Endpoint documentation
- Request/response schemas
- Example payloads
- Authentication documentation
- Error response documentation
- Interactive Swagger UI setup

**Output Includes:**
- OpenAPI YAML/JSON spec
- Endpoint paths with operations
- Request body schemas
- Response schemas (success and error)
- Example requests/responses
- Security schemes
- Tags and grouping

**Example Trigger:**
```
You: "Document the user authentication API"
Claude: [api-documentation-generator activates]
→ Generates OpenAPI 3.0 spec
→ Documents POST /auth/login
→ Includes request/response examples
→ Adds security schemas
```

**Technologies:**
- OpenAPI 3.0
- Swagger/OpenAPI
- JSON Schema
- Swagger UI / ReDoc
- API documentation tools

---

## 💾 Database & Testing Skills

### 9. database-migration-helper

**File:** `intermediate-kit/.claude/skills/database-migration-helper.md`

**Auto-invoked when:**
- "create migration"
- "add database migration"
- "generate migration file"
- "create schema migration"

**Capabilities:**
- SQL migration files
- ORM migration files (Django, SQLAlchemy, Prisma)
- Up and down migrations
- Index creation
- Foreign key constraints
- Data transformations
- Rollback strategies

**Output Includes:**
- Migration file (SQL or ORM)
- Up migration (apply changes)
- Down migration (rollback)
- Timestamp naming
- Migration comments
- Index definitions
- Foreign key constraints

**Example Trigger:**
```
You: "Create a migration to add email verification to users table"
Claude: [database-migration-helper activates]
→ Generates timestamped migration file
→ Adds email_verified column
→ Creates index on email_verified
→ Includes rollback migration
```

**Technologies:**
- SQL (PostgreSQL, MySQL, SQLite)
- Django Migrations
- Alembic (SQLAlchemy)
- Prisma Migrate
- Knex.js migrations
- Sequelize migrations

---

### 10. testing-framework-helper

**File:** `intermediate-kit/.claude/skills/testing-framework-helper.md`

**Auto-invoked when:**
- "setup tests"
- "configure testing"
- "setup Jest/pytest/vitest"
- "initialize test framework"

**Capabilities:**
- Test framework configuration
- Test file structure
- Mock setup
- Test utilities
- Coverage configuration
- CI integration
- Test environment setup

**Output Includes:**
- Configuration file (jest.config.js, pytest.ini, vitest.config.ts)
- Test directory structure
- Example test files
- Mock/fixture setup
- Coverage thresholds
- Test scripts in package.json
- CI/CD test commands

**Example Trigger:**
```
You: "Setup Jest for testing React components"
Claude: [testing-framework-helper activates]
→ Creates jest.config.js
→ Configures @testing-library/react
→ Adds setupTests.ts
→ Creates example component test
```

**Technologies:**
- **JavaScript:** Jest, Vitest, Mocha, Jasmine
- **Python:** pytest, unittest
- **Test Libraries:** React Testing Library, Vue Test Utils
- **Mocking:** jest.mock(), pytest fixtures
- **Coverage:** Istanbul, coverage.py

---

## 🎯 Skill Invocation Patterns

### Natural Language Triggers

**For Framework Components:**
```
✅ "Create a React component for..."
✅ "Generate a Vue component that..."
✅ "Add a Next.js page for..."
```

**For API Development:**
```
✅ "Create Express API endpoints for..."
✅ "Generate FastAPI routes for..."
✅ "Add Django models for..."
```

**For API Documentation:**
```
✅ "Document the user API"
✅ "Create GraphQL schema for..."
✅ "Generate OpenAPI spec for..."
```

**For Database & Testing:**
```
✅ "Create a migration to..."
✅ "Setup Jest for..."
✅ "Configure pytest in..."
```

### Skill Combinations

Skills often work together:

```
Example 1: Full-Stack Feature
You: "Create a user registration feature"
→ react-component-generator: Creates registration form
→ express-api-generator: Creates POST /api/register
→ database-migration-helper: Adds users table
→ testing-framework-helper: Sets up integration tests
→ api-documentation-generator: Documents the API
```

```
Example 2: Django Application
You: "Build a blog feature in Django"
→ django-model-helper: Creates Post and Comment models
→ database-migration-helper: Generates migrations
→ api-documentation-generator: Documents Django REST API
→ testing-framework-helper: Configures pytest
```

---

## 💡 Best Practices

### When Using Skills:

1. **Be Specific About Framework**
   ```
   ❌ "Create a component"
   ✅ "Create a React component"
   ✅ "Create a Vue 3 component with Composition API"
   ```

2. **Mention TypeScript If Preferred**
   ```
   ✅ "Create a TypeScript React component"
   ✅ "Add TypeScript Express API endpoint"
   ```

3. **Specify Key Requirements**
   ```
   ✅ "Create React component with form validation"
   ✅ "Add Express API with JWT authentication"
   ✅ "Generate Django model with custom manager"
   ```

4. **Request Tests Alongside**
   ```
   ✅ "Create React component and write tests for it"
   ✅ "Add FastAPI endpoint with pytest tests"
   ```

### Skill Selection:

- **Frontend work** → Use React/Vue/Next.js skills
- **Backend APIs** → Use Express/FastAPI/Django skills
- **GraphQL** → Use graphql-schema-generator
- **Documentation** → Use api-documentation-generator
- **Database changes** → Use database-migration-helper
- **Test setup** → Use testing-framework-helper

### Getting Maximum Value:

1. Let skills auto-activate (use natural language)
2. Provide context about your tech stack
3. Ask for complete implementations (component + tests + docs)
4. Request error handling and validation
5. Ask for TypeScript when applicable

---

## 🔗 Related References

**Command References:**
- `/api-docs-generate` - Generates comprehensive API docs
- `/bundle-analyze` - Analyzes JavaScript bundle
- `/docker-build` - Builds Docker images
- `/migration-create` - Creates database migrations
- See: `@intermediate-kit/.claude/rules/commands-reference.md`

**Subagent References:**
- `api-designer` - For complex API design
- `database-architect` - For schema design
- `performance-optimizer` - For optimization
- See: `@intermediate-kit/.claude/rules/agents-reference.md`

**Framework-Specific Rules:**
- React: `@intermediate-kit/.claude/rules/frameworks/react.md`
- Vue: `@intermediate-kit/.claude/rules/frameworks/vue.md`
- Express: `@intermediate-kit/.claude/rules/frameworks/express.md`
- Django: `@intermediate-kit/.claude/rules/frameworks/django.md`
- Next.js: `@intermediate-kit/.claude/rules/frameworks/nextjs.md`

---

## 📚 Skill File Locations

All skill files are located in: `intermediate-kit/.claude/skills/`

```
intermediate-kit/.claude/skills/
├── react-component-generator.md
├── vue-component-generator.md
├── nextjs-page-generator.md
├── express-api-generator.md
├── fastapi-generator.md
├── django-model-helper.md
├── graphql-schema-generator.md
├── api-documentation-generator.md
├── database-migration-helper.md
└── testing-framework-helper.md
```

---

**Last Updated:** 2025-11-01
**Total Skills:** 10
**Level:** Intermediate (Production-Ready)
