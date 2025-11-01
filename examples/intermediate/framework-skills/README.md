# Framework Skills - Intermediate Examples

Framework-specific skills for modern web development.

## What Are Framework Skills?

Framework skills provide specialized knowledge for specific frameworks and libraries, enabling Claude to generate idiomatic code that follows framework best practices.

## Available Examples

### React Component Generator
- **File**: `react-component-generator/SKILL.md`
- **Purpose**: Generate React components with TypeScript, hooks, and tests
- **Use When**: Building React applications
- **Key Features**: TypeScript, React Hooks, Props typing, CSS Modules, Tests

### Vue Component Generator
- **File**: `vue-component-generator/SKILL.md`
- **Purpose**: Create Vue 3 components with Composition API
- **Use When**: Building Vue applications
- **Key Features**: Composition API, TypeScript, Reactive state, Scoped styles

### Express API Generator
- **File**: `express-api-generator/SKILL.md`
- **Purpose**: Generate Express.js REST APIs
- **Use When**: Building Node.js backend APIs
- **Key Features**: MVC architecture, Validation, Error handling, Auth patterns

### FastAPI Generator
- **File**: `fastapi-generator/SKILL.md`
- **Purpose**: Create FastAPI endpoints with Pydantic
- **Use When**: Building Python APIs
- **Key Features**: Pydantic validation, Async/await, OpenAPI docs, Type hints

### Next.js Page Generator
- **File**: `nextjs-page-generator/SKILL.md`
- **Purpose**: Generate Next.js 13+ pages
- **Use When**: Building Next.js applications
- **Key Features**: Server/Client Components, SSR/SSG, Metadata API

### GraphQL Schema Generator
- **File**: `graphql-schema-generator/SKILL.md`
- **Purpose**: Design GraphQL schemas
- **Use When**: Building GraphQL APIs
- **Key Features**: Types, Queries/Mutations, Resolvers, DataLoader

### Django Model Helper
- **File**: `django-model-helper/SKILL.md`
- **Purpose**: Create Django ORM models
- **Use When**: Building Django backends
- **Key Features**: Field types, Relationships, Indexes, Admin interface

### API Documentation Generator
- **File**: `api-documentation-generator/SKILL.md`
- **Purpose**: Generate OpenAPI/Swagger docs
- **Use When**: Documenting REST APIs
- **Key Features**: OpenAPI 3.0, Schemas, Auth docs, Examples

### Database Migration Helper
- **File**: `database-migration-helper/SKILL.md`
- **Purpose**: Create database migrations
- **Use When**: Changing database schema
- **Key Features**: Up/down migrations, Indexes, Data transforms, Rollback

### Testing Framework Helper
- **File**: `testing-framework-helper/SKILL.md`
- **Purpose**: Generate comprehensive test suites
- **Use When**: Writing tests for any framework
- **Key Features**: Multiple frameworks, Unit/Integration/E2E, Mocking, Coverage

## How to Use

1. **Copy to your project**:
   ```bash
   cp examples/intermediate/framework-skills/react-component-generator/SKILL.md \
      .claude/skills/react-component-generator.md
   ```

2. **Use naturally**:
   ```
   "create a Button component with loading state"
   "generate UserProfile component with data fetching"
   ```

3. **Claude automatically uses the skill when appropriate**

## Creating Your Own Framework Skill

```markdown
---
name: my-framework-helper
description: Generates components for MyFramework. Use when creating MyFramework components or UI.
allowed-tools: [Write, Read, Glob]
---

# MyFramework Component Generator

Expert at creating MyFramework components following best practices.

## When to Activate
- "create MyFramework component"
- "generate MyFramework UI"

## Component Structure
[Your framework-specific template]

## Best Practices
- [Framework best practices]
- [Common patterns]
```

## Best Practices

- Keep skills framework-specific
- Include TypeScript/type support
- Generate tests alongside code
- Follow framework conventions
- Include file organization
- Add documentation comments
- Implement proper error handling

## See Also

- [Intermediate Kit](../../../intermediate-kit/) - Complete setup
- [Templates](../../../templates/) - Skill templates
- [Claude Code Docs](https://docs.claude.com/claude-code/)
