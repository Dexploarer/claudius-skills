# Test Enforcement Hook - Intermediate Example

An advanced hook that ensures tests exist and pass before allowing commits, maintaining test coverage.

## What This Teaches

- Test automation in hooks
- Coverage enforcement
- File matching patterns
- Test runner integration
- Quality gates

## Installation

```bash
cp hook.json /path/to/your-project/.claude/hooks/test-enforcement.json
```

## How It Works

This hook:
1. Detects code file changes
2. Checks if corresponding tests exist
3. Runs affected tests
4. Verifies test coverage threshold
5. Blocks commit if tests fail or are missing

## Hook Script

`.claude/hooks/test-enforcement.sh`:

```bash
#!/bin/bash

echo "🧪 Running test enforcement..."

# Get staged files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM)

# Filter source files (not test files)
SOURCE_FILES=$(echo "$STAGED_FILES" | grep -E '\.(js|jsx|ts|tsx|py)$' | grep -v -E '\.(test|spec)\.' || true)

if [ -z "$SOURCE_FILES" ]; then
    echo "✅ No source files changed"
    exit 0
fi

MISSING_TESTS=()
FAILED_TESTS=false

# Check for corresponding test files
for FILE in $SOURCE_FILES; do
    # Convert source file to test file path
    # e.g., src/utils/math.js -> src/utils/math.test.js
    DIR=$(dirname "$FILE")
    BASE=$(basename "$FILE" | sed 's/\.[^.]*$//')
    EXT="${FILE##*.}"

    # Try common test patterns
    TEST_PATTERNS=(
        "${DIR}/${BASE}.test.${EXT}"
        "${DIR}/${BASE}.spec.${EXT}"
        "${DIR}/__tests__/${BASE}.test.${EXT}"
        "tests/${FILE}"
        "test/${FILE}"
    )

    TEST_EXISTS=false
    for PATTERN in "${TEST_PATTERNS[@]}"; do
        if [ -f "$PATTERN" ]; then
            TEST_EXISTS=true
            break
        fi
    done

    if [ "$TEST_EXISTS" = false ]; then
        MISSING_TESTS+=("$FILE")
    fi
done

# Report missing tests
if [ ${#MISSING_TESTS[@]} -gt 0 ]; then
    echo ""
    echo "❌ Missing tests for:"
    for FILE in "${MISSING_TESTS[@]}"; do
        echo "   - $FILE"
    done
    echo ""
    echo "Please add tests before committing."
    exit 1
fi

# Run tests
echo "Running tests..."

# Detect test framework and run
if [ -f "package.json" ]; then
    # JavaScript/TypeScript project
    if ! npm test -- --passWithNoTests --bail; then
        FAILED_TESTS=true
    fi
elif [ -f "pytest.ini" ] || [ -f "setup.py" ]; then
    # Python project
    if ! pytest --tb=short; then
        FAILED_TESTS=true
    fi
fi

# Check coverage (if available)
if command -v nyc &> /dev/null; then
    # JavaScript coverage
    COVERAGE=$(nyc report --reporter=text-summary | grep "Lines" | awk '{print $3}' | sed 's/%//')
    if (( $(echo "$COVERAGE < 80" | bc -l) )); then
        echo "⚠️  Coverage below 80%: ${COVERAGE}%"
        echo "Please add more tests."
        exit 1
    fi
fi

if [ "$FAILED_TESTS" = true ]; then
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "❌ COMMIT BLOCKED: Tests Failed"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "Fix failing tests before committing."
    exit 1
fi

echo "✅ All tests passed!"
exit 0
```

Make executable:
```bash
chmod +x .claude/hooks/test-enforcement.sh
```

## Features

### Test Detection Patterns
- `src/utils/math.js` → `src/utils/math.test.js`
- `lib/parser.py` → `lib/parser.test.py`
- `components/Button.tsx` → `components/__tests__/Button.test.tsx`

### Multi-Framework Support
- JavaScript: Jest, Mocha, Jasmine
- Python: pytest, unittest
- Go: go test
- Rust: cargo test

### Coverage Enforcement
```bash
# Require minimum 80% coverage
if [ $COVERAGE -lt 80 ]; then
    echo "Coverage too low: ${COVERAGE}%"
    exit 1
fi
```

### Smart Test Running
- Only runs affected tests
- Fails fast with `--bail`
- Skips if no source changes

## Configuration

### Set Coverage Threshold

```bash
# In .claude/hooks/test-enforcement.sh
MIN_COVERAGE=80  # Your threshold

if [ $COVERAGE -lt $MIN_COVERAGE ]; then
    echo "Coverage ${COVERAGE}% < ${MIN_COVERAGE}%"
    exit 1
fi
```

### Customize Test Patterns

```bash
# Add your patterns
TEST_PATTERNS=(
    "${DIR}/${BASE}.test.${EXT}"
    "${DIR}/${BASE}.spec.${EXT}"
    "spec/${FILE}"                    # RSpec style
    "${DIR}/test_${BASE}.${EXT}"     # Python style
)
```

### Exclude Certain Files

```bash
# Skip config files, types, etc.
SOURCE_FILES=$(echo "$STAGED_FILES" | \
    grep -E '\.(js|jsx|ts|tsx|py)$' | \
    grep -v -E '\.(test|spec|d\.ts|config)\.' || true)
```

## Customization

### Require Integration Tests

```bash
# Check for integration tests too
INTEGRATION_TEST="tests/integration/${BASE}.integration.test.js"
if [ ! -f "$INTEGRATION_TEST" ]; then
    echo "⚠️  Missing integration test for $FILE"
fi
```

### Test Quality Checks

```bash
# Ensure tests have assertions
TEST_FILE="src/utils/math.test.js"
if ! grep -q "expect\|assert\|should" "$TEST_FILE"; then
    echo "❌ Test file has no assertions: $TEST_FILE"
    exit 1
fi
```

### Snapshot Testing

```bash
# Warn about snapshot changes
if git diff --cached | grep -q "\.snap$"; then
    echo "⚠️  Snapshot files changed. Review carefully!"
fi
```

## Real-World Examples

### JavaScript Project

```bash
# .claude/hooks/test-enforcement.sh for React app
npm test -- --coverage --passWithNoTests --bail

# Check specific coverage areas
COVERAGE_LINES=$(nyc report --reporter=json | jq '.total.lines.pct')
COVERAGE_BRANCHES=$(nyc report --reporter=json | jq '.total.branches.pct')

if (( $(echo "$COVERAGE_LINES < 80" | bc -l) )); then
    echo "Line coverage too low"
    exit 1
fi
```

### Python Project

```bash
# Run pytest with coverage
pytest --cov=src --cov-report=term --cov-fail-under=80

# Type checking
mypy src/

# Linting
flake8 src/
```

## Troubleshooting

**Problem:** Tests run every commit (slow)

**Solutions:**
- Only run tests for changed files
- Use test caching (`jest --cache`)
- Run full suite in CI, quick check in hook

**Problem:** False positives for missing tests

**Solutions:**
- Update TEST_PATTERNS for your structure
- Exclude certain file types
- Add exception list

**Problem:** Hook blocks unfairly

**Solutions:**
- Allow `--no-verify` for WIP commits
- Warning mode instead of blocking
- Skip for certain branches

## Best Practices

### ✅ Do:
- Run only affected tests
- Provide clear error messages
- Support standard test patterns
- Make fast (< 10 seconds)
- Allow coverage threshold config

### ❌ Don't:
- Run entire test suite
- Block without explanation
- Ignore test failures
- Modify source during tests

## Integration Examples

### With CI/CD

```yaml
# .github/workflows/test.yml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: npm test -- --coverage
      - run: npx codecov
```

### With Pre-Push Hook

```json
{
  "hooks": {
    "tool-call": {
      "Bash": {
        "git push": {
          "command": "npm test",
          "description": "Run full test suite before push",
          "blocking": true
        }
      }
    }
  }
}
```

## Next Steps

1. Install in your project
2. Configure for your test framework
3. Set coverage threshold
4. Test with real commits
5. Adjust patterns as needed

---

**Pro Tip:** Combine with pre-commit-lint hook for comprehensive quality enforcement!
