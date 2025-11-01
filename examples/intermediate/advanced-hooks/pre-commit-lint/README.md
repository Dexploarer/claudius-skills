# Pre-Commit Lint Hook - Intermediate Example

An advanced hook that runs linting tools before allowing commits, ensuring code quality standards.

## What This Teaches

- Complex hook implementation
- Tool integration (ESLint, Prettier, etc.)
- Exit code handling
- Output formatting
- Performance optimization

## Installation

```bash
# Copy hook configuration
cp hook.json /path/to/your-project/.claude/hooks/pre-commit-lint.json

# Update .claude/settings.json to reference it
```

## How It Works

This hook:
1. Detects which files are staged
2. Runs appropriate linters based on file type
3. Reports errors in readable format
4. Blocks commit if linting fails
5. Provides fix suggestions

## Configuration

`.claude/settings.json`:

```json
{
  "hooks": {
    "tool-call": {
      "Bash": {
        "git commit": {
          "command": "bash .claude/hooks/pre-commit-lint.sh",
          "description": "Run linting on staged files",
          "blocking": true
        }
      }
    }
  }
}
```

## Hook Script

`.claude/hooks/pre-commit-lint.sh`:

```bash
#!/bin/bash

set -e

echo "🔍 Running pre-commit linting..."

# Get staged files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM)

if [ -z "$STAGED_FILES" ]; then
    echo "✅ No files to lint"
    exit 0
fi

ERRORS_FOUND=false

# JavaScript/TypeScript files
JS_FILES=$(echo "$STAGED_FILES" | grep -E '\.(js|jsx|ts|tsx)$' || true)
if [ -n "$JS_FILES" ]; then
    echo "Linting JavaScript/TypeScript files..."

    # ESLint
    if command -v eslint &> /dev/null; then
        if ! eslint $JS_FILES; then
            echo "❌ ESLint errors found"
            ERRORS_FOUND=true
        fi
    fi

    # Prettier
    if command -v prettier &> /dev/null; then
        if ! prettier --check $JS_FILES; then
            echo "❌ Prettier formatting issues found"
            echo "💡 Run: prettier --write $JS_FILES"
            ERRORS_FOUND=true
        fi
    fi
fi

# Python files
PY_FILES=$(echo "$STAGED_FILES" | grep -E '\.py$' || true)
if [ -n "$PY_FILES" ]; then
    echo "Linting Python files..."

    # flake8
    if command -v flake8 &> /dev/null; then
        if ! flake8 $PY_FILES; then
            echo "❌ flake8 errors found"
            ERRORS_FOUND=true
        fi
    fi

    # black
    if command -v black &> /dev/null; then
        if ! black --check $PY_FILES; then
            echo "❌ black formatting issues found"
            echo "💡 Run: black $PY_FILES"
            ERRORS_FOUND=true
        fi
    fi
fi

# CSS/SCSS files
CSS_FILES=$(echo "$STAGED_FILES" | grep -E '\.(css|scss)$' || true)
if [ -n "$CSS_FILES" ]; then
    echo "Linting CSS files..."

    if command -v stylelint &> /dev/null; then
        if ! stylelint $CSS_FILES; then
            echo "❌ stylelint errors found"
            ERRORS_FOUND=true
        fi
    fi
fi

# Final result
if [ "$ERRORS_FOUND" = true ]; then
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "❌ COMMIT BLOCKED: Linting Failed"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "Please fix the errors above and try again."
    echo ""
    echo "Options:"
    echo "  1. Fix the errors manually"
    echo "  2. Run auto-fix commands shown above"
    echo "  3. Use --no-verify to skip (not recommended)"
    exit 1
fi

echo "✅ All linting checks passed!"
exit 0
```

Make executable:
```bash
chmod +x .claude/hooks/pre-commit-lint.sh
```

## Features

### Multi-Language Support
- JavaScript/TypeScript (ESLint, Prettier)
- Python (flake8, black, pylint)
- CSS/SCSS (stylelint)
- Go (gofmt, golint)
- Rust (rustfmt, clippy)

### Smart Detection
- Only lints staged files
- Skips files that match .gitignore
- Detects available tools automatically

### Auto-Fix Suggestions
```
❌ Prettier formatting issues found
💡 Run: prettier --write src/**/*.js
```

### Performance Optimized
- Only processes changed files
- Parallel linting when possible
- Caches results

## Customization

### Add More Linters

```bash
# Go files
GO_FILES=$(echo "$STAGED_FILES" | grep -E '\.go$' || true)
if [ -n "$GO_FILES" ]; then
    echo "Linting Go files..."
    if ! gofmt -l $GO_FILES; then
        ERRORS_FOUND=true
    fi
fi
```

### Configure Severity Levels

```bash
# Warnings don't block, errors do
eslint --max-warnings 10 $JS_FILES
```

### Team-Specific Rules

```bash
# Check for banned patterns
if grep -r "console.log" $JS_FILES; then
    echo "⚠️  Found console.log (team policy violation)"
    ERRORS_FOUND=true
fi
```

## Troubleshooting

**Problem:** Hook too slow

**Solutions:**
- Lint only changed files
- Use `--cache` with linters
- Run expensive checks in CI only

**Problem:** Tool not found

**Solutions:**
```bash
# Check if tool exists before running
if command -v eslint &> /dev/null; then
    eslint $FILES
else
    echo "⚠️  ESLint not installed, skipping"
fi
```

## Best Practices

### ✅ Do:
- Provide clear error messages
- Suggest auto-fix commands
- Support --no-verify override
- Make it fast (< 3 seconds ideal)
- Only lint staged files

### ❌ Don't:
- Lint entire codebase
- Block without clear reason
- Modify files automatically
- Run slow operations

## Integration with CI/CD

Use same linting in CI:

```yaml
# .github/workflows/lint.yml
name: Lint
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: npm run lint
```

## Next Steps

1. Install hook in your project
2. Configure for your languages
3. Add your team's rules
4. Test with various file types
5. Share with team

---

**Pro Tip:** Combine with a test-enforcement hook for complete pre-commit quality checks!
