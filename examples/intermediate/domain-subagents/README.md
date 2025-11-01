# Domain Subagents - Intermediate Examples

Specialized AI experts for complex domain-specific tasks.

## What Are Domain Subagents?

Domain subagents are pre-configured AI personalities with deep expertise in specific domains. They have their own context windows and can be restricted to specific tools for safety.

## Available Examples

### API Designer
- **File**: `api-designer/subagent.md`
- **Expertise**: RESTful API design, GraphQL, API architecture
- **Use When**: Designing APIs, creating specifications
- **Tools**: Read, Write, Grep
- **Key Features**:
  - RESTful conventions
  - OpenAPI/Swagger specs
  - Proper status codes
  - Authentication patterns

### Database Architect
- **File**: `database-architect/subagent.md`
- **Expertise**: Schema design, query optimization, data modeling
- **Use When**: Designing databases, optimizing queries
- **Tools**: Read, Write, Grep
- **Key Features**:
  - Normalization
  - Index strategy
  - Relationship design
  - Performance optimization

## How to Use

### 1. Copy to Your Project
```bash
cp examples/intermediate/domain-subagents/api-designer/subagent.md \
   .claude/agents/api-designer.md
```

### 2. Call the Subagent
```
"use the api-designer subagent to design user management API"
"get the database-architect to optimize this query"
```

### 3. Claude Automatically Uses the Expert

## When to Use Subagents vs Skills

### Use Subagents When:
- ✅ Task requires deep domain expertise
- ✅ You want isolated context
- ✅ Tool restrictions needed (e.g., read-only)
- ✅ Complex analysis required
- ✅ Want to keep main conversation clean

### Use Skills When:
- ✅ Task is straightforward code generation
- ✅ No need for isolation
- ✅ Quick, automated assistance
- ✅ Part of larger workflow

## Creating Your Own Domain Subagent

```markdown
---
name: my-domain-expert
description: Expert in [domain] specializing in [specific tasks]
allowed-tools: [Read, Grep, Glob]  # Restrict tools if needed
---

# [Domain] Expert Subagent

You are an expert in [domain] with deep knowledge of [specifics].

## Your Expertise
- [Area 1]
- [Area 2]
- [Area 3]

## When to Call This Subagent
- [Use case 1]
- [Use case 2]

## Your Responsibilities

### 1. [Responsibility 1]
[Detailed instructions]

### 2. [Responsibility 2]
[Detailed instructions]

## Best Practices You Follow
- [Practice 1]
- [Practice 2]

## Output Format
[How to present findings]

## Remember
- [Key principles]
```

## Subagent Best Practices

### Design Principles
- Single, focused domain
- Clear expertise boundaries
- Specific use cases
- Comprehensive instructions
- Consistent output format

### Tool Restrictions
```markdown
---
allowed-tools: [Read, Grep, Glob]  # Read-only expert
---
```
Or:
```markdown
---
allowed-tools: [Read, Write, Bash, Grep]  # Can make changes
---
```

### When to Restrict Tools
- **Read-only**: Code reviewers, auditors, analyzers
- **Write enabled**: Generators, implementers, builders
- **Bash enabled**: Deployment, testing, automation experts

## Common Domain Patterns

### Review & Analysis Experts
- Code reviewers
- Security auditors
- Performance analyzers
- Architecture reviewers

### Design & Planning Experts
- API designers
- Database architects
- System architects
- UX designers

### Implementation Experts
- DevOps engineers
- Test engineers
- Documentation writers

## Advanced Patterns

### Chaining Subagents
```
"use the api-designer to design the API, then use the security-auditor to review it"
```

### Subagent Handoff
```
"use the database-architect to design the schema, then use the performance-optimizer to optimize it"
```

## Debugging Subagents

### Check Subagent Exists
```bash
ls .claude/agents/
```

### Verify YAML Frontmatter
```markdown
---
name: my-expert  # Must match
description: Clear description
allowed-tools: [Read, Write]  # Optional
---
```

### Call Explicitly
```
"use the my-expert subagent to analyze this code"
```

## See Also

- [Intermediate Kit](../../../intermediate-kit/) - Complete setup
- [Templates](../../../templates/) - Subagent templates
- [Best Practices](../../../resources/guides/best-practices.md)
