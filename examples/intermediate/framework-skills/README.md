# Framework Skills - Intermediate Examples

Framework-specific skills for modern web development.

## What Are Framework Skills?

Framework skills provide specialized knowledge for specific frameworks and libraries, enabling Claude to generate idiomatic code that follows framework best practices.

## Available Examples

### React Component Generator
- **File**: `react-component-generator/SKILL.md`
- **Purpose**: Generate React components with TypeScript, hooks, and tests
- **Use When**: Building React applications
- **Key Features**:
  - TypeScript support
  - React Hooks (useState, useEffect, useCallback)
  - Props typing
  - CSS Modules
  - Unit tests with React Testing Library

### Django Model Helper
- **File**: `django-model-helper/SKILL.md`
- **Purpose**: Create Django ORM models with relationships and migrations
- **Use When**: Building Django backends
- **Key Features**:
  - Proper field types
  - Relationships (ForeignKey, ManyToMany)
  - Indexes and Meta configuration
  - Admin interface setup

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
