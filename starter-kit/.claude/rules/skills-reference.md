# Starter Kit - Skills Reference

> **Complete reference for all 5 beginner-level skills**

---

## Overview

Skills are **automatic, context-aware capabilities** that activate based on natural language requests. You don't need to explicitly invoke them - Claude Code detects when to use them based on your conversation.

**Location:** `starter-kit/.claude/skills/`

---

## 1. readme-generator

**File:** `starter-kit/.claude/skills/readme-generator.md`

### Description
Creates professional README files with proper structure, badges, and documentation sections.

### Auto-Activation Triggers
- "create readme"
- "generate readme"
- "make a readme file"
- "add project documentation"
- "write readme"

### What It Does
1. Analyzes project structure
2. Identifies technologies used
3. Generates comprehensive sections:
   - Title and description
   - Installation instructions
   - Usage examples
   - API documentation (if applicable)
   - Contributing guidelines
   - License information
4. Adds appropriate badges
5. Includes code examples

### Usage Example
```
You: "Can you create a README for this Express.js API project?"

Claude: [readme-generator skill activates]
        Creates comprehensive README.md with:
        - Project overview
        - API endpoints documentation
        - Installation steps
        - Environment variables
        - Usage examples
```

### Best Practices
- Provide context about your project
- Mention specific sections you want
- Include API endpoints if building an API
- Specify target audience (developers, end-users, etc.)

---

## 2. code-explainer

**File:** `starter-kit/.claude/skills/code-explainer.md`

### Description
Explains code in beginner-friendly terms with step-by-step breakdowns and examples.

### Auto-Activation Triggers
- "explain this code"
- "what does this do"
- "how does this work"
- "break down this function"
- "help me understand"

### What It Does
1. Analyzes code structure
2. Identifies key concepts
3. Provides line-by-line explanations
4. Uses beginner-friendly language
5. Includes analogies when helpful
6. Highlights important patterns

### Usage Example
```
You: "Can you explain what this React component does?"

Claude: [code-explainer skill activates]
        Provides:
        - Component purpose
        - Props explanation
        - State management breakdown
        - Lifecycle explanation
        - Rendering logic
        - Best practices notes
```

### Best Practices
- Specify your experience level
- Ask about specific parts if needed
- Request comparisons to other approaches
- Ask for visual diagrams when helpful

---

## 3. bug-finder

**File:** `starter-kit/.claude/skills/bug-finder.md`

### Description
Identifies common bugs, potential issues, edge cases, and code smells.

### Auto-Activation Triggers
- "find bugs"
- "check for errors"
- "are there any issues"
- "debug this code"
- "something's wrong with"

### What It Does
1. Static analysis of code
2. Identifies common bug patterns:
   - Null/undefined references
   - Type mismatches
   - Logic errors
   - Off-by-one errors
   - Race conditions
   - Memory leaks
3. Highlights edge cases
4. Suggests fixes
5. Explains why it's a bug

### Usage Example
```
You: "Can you find any bugs in this async function?"

Claude: [bug-finder skill activates]
        Identifies:
        - Missing error handling
        - Potential race conditions
        - Unhandled promise rejections
        - Missing null checks
        + Provides fixes for each
```

### Best Practices
- Provide full function/module context
- Mention observed symptoms if any
- Include error messages
- Specify runtime environment

### Common Bugs Detected
- **Null/Undefined:** Missing checks, undefined variables
- **Async Issues:** Unhandled promises, race conditions
- **Type Errors:** Mismatched types, wrong conversions
- **Logic Errors:** Wrong conditions, incorrect loops
- **Security:** SQL injection, XSS vulnerabilities
- **Performance:** Inefficient loops, memory leaks

---

## 4. test-helper

**File:** `starter-kit/.claude/skills/test-helper.md`

### Description
Helps write comprehensive tests with proper structure, edge cases, and assertions.

### Auto-Activation Triggers
- "write tests"
- "add test coverage"
- "create unit tests"
- "test this function"
- "generate tests for"

### What It Does
1. Analyzes code structure
2. Identifies test cases:
   - Happy path
   - Edge cases
   - Error conditions
   - Boundary values
3. Generates test code
4. Uses appropriate testing framework:
   - Jest (JavaScript/TypeScript)
   - pytest (Python)
   - JUnit (Java)
   - RSpec (Ruby)
5. Includes setup and teardown
6. Adds descriptive test names

### Usage Example
```
You: "Can you write tests for this user authentication function?"

Claude: [test-helper skill activates]
        Creates tests for:
        - Valid credentials (happy path)
        - Invalid username
        - Invalid password
        - Missing credentials
        - SQL injection attempts
        - Rate limiting
        - Session management
```

### Best Practices
- Specify testing framework
- Mention coverage requirements
- Include integration vs unit test preference
- Specify mock requirements

### Test Categories Generated
- **Unit Tests:** Individual function testing
- **Edge Cases:** Boundary values, empty inputs
- **Error Handling:** Exceptions, failures
- **Integration:** Component interactions
- **Security:** Injection, auth bypass

---

## 5. git-helper

**File:** `starter-kit/.claude/skills/git-helper.md`

### Description
Assists with git operations, commit messages, branching strategies, and workflows.

### Auto-Activation Triggers
- "help with git"
- "create commit"
- "write commit message"
- "git workflow"
- "branch strategy"

### What It Does
1. **Commit Assistance:**
   - Analyzes staged changes
   - Writes conventional commit messages
   - Follows commit best practices

2. **Workflow Guidance:**
   - Branch naming conventions
   - Merge vs rebase advice
   - Conflict resolution help

3. **History Management:**
   - Interactive rebase guidance
   - Cherry-pick assistance
   - Stash management

4. **Best Practices:**
   - Atomic commits
   - Descriptive messages
   - Branch organization

### Usage Example
```
You: "Help me create a good commit message for these API changes"

Claude: [git-helper skill activates]
        Generates:
        feat(api): add user authentication endpoints

        - Add POST /api/auth/login endpoint
        - Add POST /api/auth/register endpoint
        - Add JWT token generation
        - Add password hashing with bcrypt

        BREAKING CHANGE: Requires new AUTH_SECRET env var
```

### Best Practices
- Use conventional commit format
- Keep commits atomic
- Write descriptive messages
- Reference issue numbers

### Commit Message Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:** feat, fix, docs, style, refactor, test, chore

---

## Skills Comparison Matrix

| Feature | readme-generator | code-explainer | bug-finder | test-helper | git-helper |
|---------|-----------------|----------------|------------|-------------|------------|
| **Purpose** | Documentation | Understanding | Debugging | Testing | Version Control |
| **Auto-Invoked** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Creates Files** | ✅ README.md | ❌ | ❌ | ✅ Test files | ❌ |
| **Analyzes Code** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Beginner Friendly** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Framework Support** | All | All | All | Jest/pytest/JUnit | Git only |

---

## Combining Skills

Skills work together naturally:

### Example 1: New Feature Workflow
```
1. Write code
2. "Find any bugs in this" → bug-finder
3. "Write tests for this" → test-helper
4. "Help me commit these changes" → git-helper
5. "Update the README" → readme-generator
```

### Example 2: Code Review Workflow
```
1. "Explain what this module does" → code-explainer
2. "Find potential issues" → bug-finder
3. "Are there tests for this?" → test-helper
4. "Check git history" → git-helper
```

---

## Advanced Usage

### Skill Chaining
Skills automatically chain when appropriate:

```
You: "Review this code and add tests"

Claude:
1. Uses code-explainer to understand code
2. Uses bug-finder to identify issues
3. Fixes issues
4. Uses test-helper to generate tests
5. Uses git-helper for commit message
```

### Context Awareness
Skills understand project context:

```
If you have package.json → Assumes JavaScript/TypeScript
If you have requirements.txt → Assumes Python
If you have pom.xml → Assumes Java
```

---

## Troubleshooting

### Skill Not Activating?
- Use more explicit language
- Mention the skill name directly
- Check skill file exists in `.claude/skills/`

### Wrong Skill Activating?
- Be more specific in request
- Explicitly mention desired skill
- Provide more context

### Skill Errors?
- Check skill YAML frontmatter
- Validate file location
- Review skill description

---

## Next Steps

**When you're comfortable with starter skills:**
- Graduate to Intermediate Kit
- Location: `intermediate-kit/.claude/skills/`
- Additional capabilities: Framework-specific skills
- Reference: `@intermediate-kit/.claude/rules/skills-reference.md`

---

**Total Skills:** 5
**Difficulty:** Beginner
**Auto-Invoked:** ✅ All
**Last Updated:** 2025-11-01

