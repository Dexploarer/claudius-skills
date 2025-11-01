# Starter Kit - Commands Reference

> **Complete reference for all 12 beginner-level slash commands**

---

## Overview

Slash commands are **manual, explicit workflows** that you invoke with `/` prefix. Unlike skills (which auto-activate), commands require direct invocation and are perfect for repeated workflows.

**Location:** `starter-kit/.claude/commands/`
**Total Commands:** 12

---

## Development Commands (6)

### `/commit`
**File:** `starter-kit/.claude/commands/commit.md`

**Purpose:** Git commit helper with conventional commits

**Usage:**
```
/commit
```

**What It Does:**
1. Runs `git status` to see changes
2. Runs `git diff` to review modifications
3. Analyzes changes semantically
4. Generates conventional commit message
5. Stages relevant files
6. Creates commit with generated message
7. Verifies commit success

**Generated Commit Format:**
```
<type>(<scope>): <description>

<body with detailed changes>

<footer with breaking changes/issues>
```

**Example Output:**
```bash
feat(auth): add JWT authentication

- Implement JWT token generation
- Add login endpoint with password validation
- Add middleware for protected routes
- Update user model with password hashing

Closes #123
```

**Best Practices:**
- Review staged changes before running
- Let command analyze semantic changes
- Don't override generated message unless needed
- Follow conventional commit types

**Related:**
- Skill: `git-helper` (auto-invoked)
- Hook: Secret detection (PreToolUse)
- Hook: Force push prevention

---

### `/debug`
**File:** `starter-kit/.claude/commands/debug.md`

**Purpose:** Analyze and fix code issues

**Usage:**
```
/debug
```

**What It Does:**
1. Analyzes current file or selection
2. Identifies potential bugs
3. Checks for common issues:
   - Null/undefined references
   - Type errors
   - Logic mistakes
   - Performance issues
4. Suggests fixes with explanations
5. Can apply fixes automatically

**Example Workflow:**
```
You: /debug

Claude:
Found 3 potential issues:

1. Line 42: Possible null reference
   → userdata.name without null check
   Fix: Add optional chaining userdata?.name

2. Line 58: Unhandled promise rejection
   → Missing .catch() on API call
   Fix: Add error handling

3. Line 73: Memory leak potential
   → Event listener never removed
   Fix: Add cleanup in useEffect
```

**Best Practices:**
- Run on specific files or functions
- Review suggestions before applying
- Understand why something is a bug
- Test after fixes applied

**Related:**
- Skill: `bug-finder` (auto-invoked)
- Command: `/test` (verify fixes)

---

### `/explain`
**File:** `starter-kit/.claude/commands/explain.md`

**Purpose:** Detailed code explanation

**Usage:**
```
/explain
```

**What It Does:**
1. Analyzes selected code or current file
2. Provides comprehensive breakdown:
   - Purpose and functionality
   - Line-by-line explanation
   - Key concepts
   - Design patterns used
   - Dependencies
3. Uses beginner-friendly language
4. Includes visual examples

**Example Output:**
```markdown
## Overview
This is a React authentication component using hooks and context.

## Key Concepts
1. **useState** - Manages local loading state
2. **useContext** - Accesses global auth state
3. **useEffect** - Handles side effects

## Line-by-Line Breakdown
[Detailed explanations...]

## Design Patterns
- Context API for state management
- Custom hooks for logic reuse
- Controlled components
```

**Best Practices:**
- Specify complexity level
- Ask about specific parts
- Request diagrams when helpful
- Compare to alternative approaches

**Related:**
- Skill: `code-explainer` (auto-invoked)
- Command: `/review` (includes explanations)

---

### `/quickfix`
**File:** `starter-kit/.claude/commands/quickfix.md`

**Purpose:** Fast fixes for common issues

**Usage:**
```
/quickfix
```

**What It Does:**
1. Scans code for quick-fix opportunities:
   - Missing imports
   - Unused variables
   - Simple type errors
   - Formatting issues
   - ESLint/Prettier fixes
2. Applies fixes automatically
3. Reports changes made

**Example:**
```
You: /quickfix

Claude:
Applied 7 quick fixes:
✓ Added missing import for useState
✓ Removed unused variable 'data'
✓ Fixed indentation (3 files)
✓ Added missing semicolons
✓ Converted var to const
✓ Fixed quote consistency
✓ Removed console.log statements
```

**Best Practices:**
- Review changes after applying
- Run before commits
- Configure linter rules first
- Test after bulk changes

**Related:**
- Command: `/refactor` (deeper changes)
- Command: `/clean` (project-wide)

---

### `/refactor`
**File:** `starter-kit/.claude/commands/refactor.md`

**Purpose:** Improve code structure and quality

**Usage:**
```
/refactor
```

**What It Does:**
1. Analyzes code structure
2. Identifies refactoring opportunities:
   - Extract functions
   - Reduce complexity
   - Improve naming
   - Remove duplication
   - Apply design patterns
3. Suggests improvements
4. Can apply changes incrementally

**Refactoring Types:**
- **Extract Function:** Break down large functions
- **Rename:** Improve variable/function names
- **Simplify:** Reduce cyclomatic complexity
- **DRY:** Remove code duplication
- **Pattern:** Apply design patterns

**Example:**
```
You: /refactor

Claude:
Refactoring suggestions:

1. Extract function: getUserData (lines 45-78)
   → 34 lines of logic can be extracted
   Benefit: Improves testability and reusability

2. Rename: handleClick → handleUserAuthentication
   Benefit: More descriptive

3. Reduce complexity: Cyclomatic complexity 12 → 6
   → Split conditional logic into guard clauses

Apply all? [y/n]
```

**Best Practices:**
- Refactor incrementally
- Test after each refactoring
- Keep commits atomic
- Document significant changes

**Related:**
- Command: `/review` (includes refactoring suggestions)
- Skill: `test-helper` (update tests after refactoring)

---

### `/review`
**File:** `starter-kit/.claude/commands/review.md`

**Purpose:** Comprehensive code review

**Usage:**
```
/review
```

**What It Does:**
1. Multi-perspective code analysis:
   - **Functionality:** Does it work correctly?
   - **Quality:** Is it well-written?
   - **Security:** Any vulnerabilities?
   - **Performance:** Efficiency issues?
   - **Testing:** Adequate coverage?
   - **Documentation:** Well-documented?
2. Provides structured feedback
3. Prioritizes issues
4. Suggests improvements

**Review Output:**
```markdown
# Code Review: user-auth.ts

## Summary
Overall quality: 7/10
Critical issues: 0
Warnings: 3
Suggestions: 5

## Critical Issues
None found ✓

## Warnings
⚠️ Missing input validation on line 23
⚠️ Hardcoded secret on line 45
⚠️ Missing error handling on line 67

## Suggestions
💡 Consider using TypeScript enums
💡 Extract validation logic
💡 Add JSDoc comments
💡 Reduce function complexity
💡 Add unit tests

## Security
✓ No SQL injection
✓ Passwords hashed
⚠️ Secret should be in .env

## Performance
✓ Efficient database queries
💡 Consider caching user lookups

## Recommendations
1. Move secret to environment variables (HIGH)
2. Add input validation (HIGH)
3. Add error handling (MEDIUM)
4. Improve documentation (LOW)
```

**Best Practices:**
- Run before merge requests
- Review feedback carefully
- Prioritize critical issues
- Apply suggestions incrementally

**Related:**
- Subagent: `code-reviewer` (expert-level reviews)
- Command: `/refactor` (apply suggestions)
- Command: `/test` (verify coverage)

---

## Documentation Commands (1)

### `/docs`
**File:** `starter-kit/.claude/commands/docs.md`

**Purpose:** Generate comprehensive documentation

**Usage:**
```
/docs
```

**What It Does:**
1. Analyzes code structure
2. Generates documentation:
   - API documentation
   - Function/class docs
   - Usage examples
   - Type definitions
3. Creates appropriate format:
   - JSDoc (JavaScript/TypeScript)
   - Docstrings (Python)
   - Javadoc (Java)
   - Markdown files
4. Includes examples and edge cases

**Example Output:**
```typescript
/**
 * Authenticates a user with email and password
 *
 * @param {string} email - User's email address
 * @param {string} password - User's password (plain text)
 * @returns {Promise<AuthResult>} Authentication result with token
 * @throws {AuthError} If credentials are invalid
 *
 * @example
 * const result = await authenticateUser('user@example.com', 'password123');
 * console.log(result.token);
 *
 * @example
 * // Handle authentication failure
 * try {
 *   await authenticateUser('invalid@example.com', 'wrong');
 * } catch (error) {
 *   console.error('Auth failed:', error.message);
 * }
 */
```

**Best Practices:**
- Document public APIs
- Include usage examples
- Document edge cases
- Keep docs up-to-date

**Related:**
- Skill: `readme-generator` (project documentation)
- Command: `/review` (check documentation)

---

## Testing Commands (1)

### `/test`
**File:** `starter-kit/.claude/commands/test.md`

**Purpose:** Run and manage tests

**Usage:**
```
/test
```

**What It Does:**
1. Detects testing framework (Jest, pytest, etc.)
2. Runs appropriate test command
3. Analyzes test results
4. Reports:
   - Pass/fail status
   - Coverage statistics
   - Failed test details
5. Suggests fixes for failures

**Example Output:**
```
Running tests with Jest...

Test Suites: 8 passed, 8 total
Tests:       42 passed, 42 total
Snapshots:   0 total
Time:        3.421 s
Coverage:    87.3%

Coverage by file:
  auth.ts        95.2% ✓
  users.ts       82.1% ⚠️
  database.ts    71.4% ⚠️

Files needing coverage:
  database.ts: Lines 45-67 not covered
  users.ts: Error handling not tested
```

**Best Practices:**
- Run tests before commits
- Aim for >80% coverage
- Test edge cases
- Keep tests maintainable

**Related:**
- Skill: `test-helper` (generate tests)
- Hook: Test failure alerts (PostToolUse)
- Command: `/review` (check test quality)

---

## Project Management Commands (4)

### `/setup`
**File:** `starter-kit/.claude/commands/setup.md`

**Purpose:** Initialize project structure

**Usage:**
```
/setup
```

**What It Does:**
1. Analyzes project type
2. Creates recommended structure:
   - Directory layout
   - Config files (.gitignore, .env.example)
   - Initial files (README.md, package.json)
   - Development tools (ESLint, Prettier)
3. Installs dependencies
4. Initializes git repository

**Example:**
```
You: /setup

Claude:
Setting up Node.js + Express project...

Created:
  ✓ src/
  ✓ src/routes/
  ✓ src/controllers/
  ✓ src/models/
  ✓ tests/
  ✓ .gitignore
  ✓ .env.example
  ✓ package.json
  ✓ README.md
  ✓ .eslintrc.json
  ✓ .prettierrc

Installing dependencies...
  ✓ express
  ✓ jest
  ✓ eslint
  ✓ prettier

Initialized git repository ✓

Next steps:
1. cp .env.example .env
2. Update .env with your settings
3. npm run dev
```

**Best Practices:**
- Run at project start
- Review generated structure
- Customize for your needs
- Keep .env.example updated

**Related:**
- Skill: `readme-generator` (documentation)
- Command: `/deps` (manage dependencies)

---

### `/todo`
**File:** `starter-kit/.claude/commands/todo.md`

**Purpose:** Find and manage TODO comments

**Usage:**
```
/todo
```

**What It Does:**
1. Scans codebase for TODO markers:
   - `// TODO:`
   - `# TODO:`
   - `/* TODO */`
   - `@TODO`
2. Categorizes by priority:
   - HIGH, MEDIUM, LOW
   - FIXME (critical)
   - HACK (technical debt)
3. Groups by file/module
4. Can create GitHub issues

**Example Output:**
```markdown
## TODO Summary (12 items)

### CRITICAL (2)
- [ ] FIXME: Security vulnerability in auth.ts:45
- [ ] TODO(HIGH): Database connection leak in db.ts:123

### MEDIUM (6)
- [ ] TODO: Add input validation (api.ts:67)
- [ ] TODO: Improve error messages (errors.ts:23)
- [ ] TODO: Add pagination (users.ts:89)
- [ ] TODO: Refactor complex function (utils.ts:145)
- [ ] TODO: Add caching (database.ts:234)
- [ ] HACK: Temporary workaround (legacy.ts:78)

### LOW (4)
- [ ] TODO: Add more tests (auth.test.ts:12)
- [ ] TODO: Improve documentation (README.md:45)
- [ ] TODO: Optimize query (reports.ts:156)
- [ ] TODO: Extract constants (config.ts:89)
```

**Best Practices:**
- Review regularly
- Prioritize TODOs
- Convert to issues for tracking
- Clean up before releases

**Related:**
- Command: `/review` (includes TODO checks)
- Command: `/refactor` (address technical debt)

---

### `/clean`
**File:** `starter-kit/.claude/commands/clean.md`

**Purpose:** Remove build artifacts and temporary files

**Usage:**
```
/clean
```

**What It Does:**
1. Removes build directories:
   - `node_modules/` (after backup)
   - `dist/`, `build/`
   - `*.pyc`, `__pycache__/`
   - `.next/`, `.nuxt/`
2. Clears caches
3. Removes logs
4. Preserves:
   - Source code
   - Configuration
   - .env files

**Example:**
```
You: /clean

Claude:
Cleaning project...

Removed:
  ✓ node_modules/ (234 MB)
  ✓ dist/ (12 MB)
  ✓ .next/ (45 MB)
  ✓ *.log files (8 files)
  ✓ .cache/ (5 MB)

Preserved:
  ✓ .env files
  ✓ Source code
  ✓ Configuration files

Space freed: 304 MB

Run 'npm install' to reinstall dependencies.
```

**Best Practices:**
- Run when switching branches
- Before fresh builds
- To free disk space
- After dependency updates

**Related:**
- Command: `/deps` (reinstall after clean)
- Hook: Docker cleanup confirmation

---

### `/deps`
**File:** `starter-kit/.claude/commands/deps.md`

**Purpose:** Manage project dependencies

**Usage:**
```
/deps
```

**What It Does:**
1. **Analyzes Dependencies:**
   - Lists all dependencies
   - Checks for updates
   - Identifies security vulnerabilities
   - Finds unused dependencies

2. **Updates Management:**
   - Shows available updates
   - Categorizes (major, minor, patch)
   - Highlights breaking changes
   - Can update automatically

3. **Security Audit:**
   - Runs npm audit / pip-audit
   - Reports vulnerabilities
   - Suggests fixes

**Example Output:**
```markdown
## Dependency Analysis

### Current Dependencies (23)
- react: 18.2.0
- express: 4.18.2
- mongoose: 7.0.3

### Updates Available (8)

MAJOR (Breaking changes):
  ⚠️ react: 18.2.0 → 19.0.0
  ⚠️ webpack: 5.75.0 → 6.0.0

MINOR (New features):
  📦 express: 4.18.2 → 4.19.0
  📦 mongoose: 7.0.3 → 7.2.0

PATCH (Bug fixes):
  🔧 lodash: 4.17.20 → 4.17.21
  🔧 axios: 1.3.4 → 1.3.6

### Security Vulnerabilities (2)

HIGH: lodash Prototype Pollution
  Fix: Update to 4.17.21

MODERATE: axios SSRF
  Fix: Update to 1.3.6

### Unused Dependencies (3)
  ❌ moment (use date-fns instead)
  ❌ request (deprecated)
  ❌ colors (not imported)
```

**Best Practices:**
- Check weekly
- Update patch versions freely
- Test after major updates
- Review breaking changes
- Remove unused dependencies

**Related:**
- Command: `/security-audit` (intermediate kit)
- Hook: Package installation reminders
- Command: `/clean` (before reinstall)

---

## Command Comparison Matrix

| Command | Purpose | Creates Files | Runs Tests | Git Operation | Frequency |
|---------|---------|---------------|------------|---------------|-----------|
| `/commit` | Git commits | ❌ | ❌ | ✅ | Per feature |
| `/debug` | Find bugs | ❌ | Suggests | ❌ | As needed |
| `/explain` | Documentation | ❌ | ❌ | ❌ | Learning |
| `/quickfix` | Fast fixes | ❌ | ❌ | ❌ | Before commit |
| `/refactor` | Improve code | ❌ | Suggests | ❌ | Sprint |
| `/review` | Code review | ❌ | Checks | ❌ | Before merge |
| `/docs` | Generate docs | ✅ | ❌ | ❌ | Per feature |
| `/test` | Run tests | ❌ | ✅ | ❌ | Often |
| `/setup` | Project init | ✅ | ❌ | ✅ | Once |
| `/todo` | Find TODOs | ❌ | ❌ | ❌ | Weekly |
| `/clean` | Cleanup | ❌ | ❌ | ❌ | Monthly |
| `/deps` | Dependencies | ❌ | ❌ | ❌ | Weekly |

---

## Workflow Examples

### Daily Development Workflow
```bash
1. /quickfix           # Clean up code
2. /test               # Run tests
3. /commit             # Create commit
```

### Code Review Workflow
```bash
1. /review             # Comprehensive review
2. /refactor           # Apply improvements
3. /test               # Verify changes
4. /commit             # Commit improvements
```

### New Feature Workflow
```bash
1. Write code
2. /debug              # Find issues
3. /test               # Add tests
4. /docs               # Document
5. /review             # Final review
6. /commit             # Commit
```

### Project Maintenance
```bash
Weekly:
  /deps                # Check dependencies
  /todo                # Review TODOs

Monthly:
  /clean               # Clear artifacts
  /deps                # Update dependencies
```

---

## Advanced Usage

### Command Arguments
Some commands accept arguments:
```bash
/explain utils.ts      # Explain specific file
/test auth.test.ts     # Run specific test
/review src/api/       # Review directory
```

### Combining Commands
Chain commands for workflows:
```bash
/refactor && /test && /commit
```

---

## Troubleshooting

### Command Not Found
- Check file exists in `.claude/commands/`
- Use exact command name with `/`
- Type `/` to see available commands

### Command Errors
- Check command file syntax
- Verify arguments are correct
- Review error message details

---

## Next Level Commands

**Ready for more?**
- Intermediate Kit: 15 additional commands
- Framework-specific workflows
- CI/CD automation
- Advanced deployment

**Reference:** `@intermediate-kit/.claude/rules/commands-reference.md`

---

**Total Commands:** 12
**Difficulty:** Beginner
**Manual Invocation:** ✅ Required
**Last Updated:** 2025-11-01

