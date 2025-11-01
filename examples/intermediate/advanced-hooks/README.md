# Advanced Hooks - Intermediate Examples

Production-grade hooks for quality enforcement and automation.

## What Are Advanced Hooks?

Advanced hooks are event-driven automation that enforce code quality, security, and team standards automatically during development.

## Available Examples

### Pre-Commit Lint
- **File**: `pre-commit-lint/hook.json`
- **Event**: `user-prompt-submit`
- **Purpose**: Run linting before allowing commits
- **Features**:
  - Detects commit attempts
  - Runs appropriate linter
  - Blocks commit on errors
  - Shows warnings

### Test Enforcement
- **File**: `test-enforcement/hook.json`
- **Event**: `user-prompt-submit`
- **Purpose**: Ensure tests exist and pass
- **Features**:
  - Checks for test files
  - Runs test suite
  - Enforces coverage thresholds
  - Blocks deployment without tests

## How to Use

1. **Add to settings.json**:
   ```json
   {
     "hooks": {
       "PreToolUse": [
         {
           "pattern": "Bash.*git commit",
           "command": "npm run lint",
           "description": "Run linting before commit"
         }
       ]
     }
   }
   ```

2. **Hooks run automatically** when events occur

## Hook Types by Event

### SessionStart
- Welcome messages
- Environment setup
- Status checks

### PreToolUse
- Validation before actions
- Security checks
- Confirmations for dangerous operations

### PostToolUse
- Logging and tracking
- Notifications
- Cleanup operations

### SessionEnd
- Summary reports
- Cleanup
- Final checks

## Creating Your Own Advanced Hook

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "pattern": "Bash.*npm publish",
        "command": "npm run build && npm test && git diff-index --quiet HEAD --",
        "timeout": 120000,
        "description": "Validate before publishing package"
      }
    ]
  }
}
```

## Hook Exit Codes

- **0**: Success, continue
- **2**: Block operation
- **Other**: Warning, but allow

## Advanced Patterns

### Conditional Execution
```bash
if [ "$ENVIRONMENT" = "production" ]; then
  # Extra validation for production
  run_extra_checks
fi
```

### Async Operations
```bash
# Run in background
log_to_monitoring &

# Continue with main operation
exit 0
```

### Multi-Step Validation
```bash
# Chain multiple checks
check_1 && check_2 && check_3 || exit 2
```

## Best Practices

- Keep hooks fast (< 5 seconds)
- Provide clear error messages
- Use appropriate exit codes
- Set reasonable timeouts
- Test hooks thoroughly
- Document hook behavior
- Handle edge cases
- Avoid blocking development flow

## Common Use Cases

### Code Quality
- Linting before commits
- Format checking
- Complexity validation
- Documentation requirements

### Security
- Secret detection
- Dependency auditing
- Security scanning
- Access control

### Process Enforcement
- Required code review
- Test coverage minimums
- Changelog updates
- Version constraints

## Debugging Hooks

```bash
# Enable debug mode
claude --debug

# Check hook execution
# Hooks print to stderr

# Test hook command manually
bash -c "your-hook-command"
```

## See Also

- [Intermediate Kit](../../../intermediate-kit/) - Complete setup
- [Security Guide](../../../resources/guides/security.md)
- [Best Practices](../../../resources/guides/best-practices.md)
