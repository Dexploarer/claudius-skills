# Tutorial: Setting Up Your First Hook

Learn how to create hooks that run automatically when specific events occur.

## What You'll Build

A **pre-commit hook** that checks for console.log statements and debugging code before allowing commits.

**Why this hook?**
- Simple enough for beginners
- Immediately useful for clean code
- Teaches core hook concepts
- Easy to test and customize

## Prerequisites

- Claude Code installed
- Completed "your-first-command.md" tutorial
- Basic understanding of git
- 20 minutes of time

## Step 1: Understand Hooks

Hooks are automatic scripts that run when specific events occur in Claude Code.

**Examples of events:**
- `user-prompt-submit` - Before Claude processes your request
- `tool-call` - Before/after Claude uses a tool
- `session-start` - When Claude Code starts
- `session-end` - When Claude Code exits

**How hooks work:**
1. An event occurs (like attempting a git commit)
2. Claude checks if you have a hook for that event
3. Claude runs your hook script
4. Based on the result, the event continues or is blocked

**Hook script examples:**
```bash
# Block if condition is met
if [ dangerous_condition ]; then
  echo "BLOCK: Reason for blocking"
  exit 1
fi

# Allow if all checks pass
echo "ALLOW: All checks passed"
exit 0
```

## Step 2: Understand Hook Configuration

Hooks are configured in `.claude/settings.json`:

```json
{
  "hooks": {
    "user-prompt-submit": {
      "command": "bash /path/to/script.sh",
      "description": "Runs before processing user prompts"
    }
  }
}
```

**Key parts:**
- `event-name`: When the hook runs
- `command`: What script to execute
- `description`: What the hook does (optional but recommended)

## Step 3: Create Your Project Structure

```bash
# Navigate to your test project
cd ~/test-project

# Create .claude directory if it doesn't exist
mkdir -p .claude/hooks

# Create settings.json if it doesn't exist
touch .claude/settings.json
```

**Directory structure:**
```
test-project/
├── .claude/
│   ├── settings.json     # Hook configuration
│   └── hooks/            # Hook scripts directory
│       └── check-debug-code.sh  # Our hook script
```

## Step 4: Create the Hook Script

Create `.claude/hooks/check-debug-code.sh`:

```bash
#!/bin/bash

# Hook: Check for debugging code before commits
# Prevents commits with console.log, debugger, etc.

# Get list of staged files (files about to be committed)
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM)

# If no files staged, allow commit
if [ -z "$STAGED_FILES" ]; then
  echo "ALLOW: No files staged"
  exit 0
fi

# Patterns to check for
PATTERNS=(
  "console\.log"
  "debugger;"
  "TODO:"
  "FIXME:"
  "console\.warn"
  "console\.error"
)

# Check each staged file
ISSUES_FOUND=false
for FILE in $STAGED_FILES; do
  # Only check JavaScript/TypeScript files
  if [[ $FILE == *.js || $FILE == *.ts || $FILE == *.jsx || $FILE == *.tsx ]]; then

    for PATTERN in "${PATTERNS[@]}"; do
      # Search for pattern in file
      if git diff --cached $FILE | grep -E "^\+.*$PATTERN" > /dev/null; then
        echo "⚠️  Found '$PATTERN' in $FILE"
        ISSUES_FOUND=true
      fi
    done
  fi
done

# Block commit if issues found
if [ "$ISSUES_FOUND" = true ]; then
  echo ""
  echo "❌ BLOCK: Debugging code found in staged files"
  echo ""
  echo "Please remove console.log, debugger statements, or TODO comments"
  echo "before committing, or use --no-verify to skip this check."
  exit 1
fi

# Allow commit if no issues
echo "✅ ALLOW: No debugging code found"
exit 0
```

Make the script executable:
```bash
chmod +x .claude/hooks/check-debug-code.sh
```

## Step 5: Configure the Hook

Edit `.claude/settings.json`:

```json
{
  "hooks": {
    "tool-call": {
      "Bash": {
        "git commit": {
          "command": "bash .claude/hooks/check-debug-code.sh",
          "description": "Checks for debugging code before commits",
          "blocking": true
        }
      }
    }
  }
}
```

**What this means:**
- `tool-call`: Hook runs when Claude uses a tool
- `Bash`: Specifically when using the Bash tool
- `git commit`: When the bash command contains "git commit"
- `blocking: true`: The commit will be blocked if hook exits with error

## Step 6: Test Your Hook

### Test 1: Clean Code (Should Allow)

Create a clean JavaScript file:

```javascript
// test.js
function add(a, b) {
  return a + b;
}
```

Try to commit:
```bash
claude

# In Claude Code:
"Add test.js and commit it"
```

**Expected result:**
```
✅ ALLOW: No debugging code found
[Commit proceeds normally]
```

### Test 2: With Debug Code (Should Block)

Add debugging code:

```javascript
// test.js
function add(a, b) {
  console.log('Adding:', a, b);  // Debug code!
  return a + b;
}
```

Stage and try to commit:
```bash
git add test.js

# In Claude Code:
"Commit the changes"
```

**Expected result:**
```
⚠️  Found 'console.log' in test.js

❌ BLOCK: Debugging code found in staged files

Please remove console.log, debugger statements, or TODO comments
before committing, or use --no-verify to skip this check.
```

The commit should be blocked! ✋

### Test 3: Override When Intentional

If you REALLY want to commit with debug code:

```bash
# In Claude Code:
"Run git commit --no-verify -m 'Debug code for testing'"
```

The `--no-verify` flag bypasses git hooks.

## Step 7: Understand the Hook Flow

```
You ask Claude to commit
        ↓
Claude prepares git commit command
        ↓
Hook fires: check-debug-code.sh runs
        ↓
  Script checks staged files
        ↓
    Found issues?
      ↙        ↘
    YES        NO
     ↓          ↓
  BLOCK      ALLOW
  (exit 1)   (exit 0)
     ↓          ↓
  Commit     Commit
  cancelled  proceeds
```

## Step 8: Enhance Your Hook

### Add More Patterns

```bash
PATTERNS=(
  "console\.log"
  "console\.warn"
  "console\.error"
  "debugger;"
  "TODO:"
  "FIXME:"
  "HACK:"
  "XXX:"
  "\.only\("       # describe.only or it.only in tests
  "\.skip\("       # describe.skip or it.skip
  "process\.exit"  # Hardcoded exits
)
```

### Check More File Types

```bash
# Check Python files too
if [[ $FILE == *.py ]]; then
  for PATTERN in "print(" "import pdb" "breakpoint()"; do
    if git diff --cached $FILE | grep -E "^\+.*$PATTERN" > /dev/null; then
      echo "⚠️  Found '$PATTERN' in $FILE"
      ISSUES_FOUND=true
    fi
  done
fi
```

### Add Whitelist Comments

Allow exceptions with special comments:

```bash
# Allow if line has "debug-ok" comment
if git diff --cached $FILE | grep -E "^\+.*$PATTERN.*debug-ok" > /dev/null; then
  continue  # Skip this one
fi
```

Usage:
```javascript
console.log('Important log');  // debug-ok
```

### Better Output

```bash
if [ "$ISSUES_FOUND" = true ]; then
  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "❌ PRE-COMMIT CHECK FAILED"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo ""
  echo "Debugging code detected in staged files."
  echo ""
  echo "Options:"
  echo "  1. Remove the debugging code"
  echo "  2. Add '// debug-ok' to allow specific lines"
  echo "  3. Use 'git commit --no-verify' to skip checks"
  echo ""
  exit 1
fi
```

## Step 9: Test Different Scenarios

### Scenario 1: Mixed Files

```bash
# Add both clean and dirty files
echo "console.log('test')" > dirty.js
echo "function clean() {}" > clean.js

git add dirty.js clean.js

# Try to commit - should block because of dirty.js
```

### Scenario 2: Only Non-JS Files

```bash
# Add non-JavaScript files
echo "# README" > README.md

git add README.md

# Try to commit - should allow (doesn't check .md files)
```

### Scenario 3: Unstaged Changes

```bash
# Modify file but don't stage
echo "console.log('test')" > test.js

# Try to commit other files - should allow
# (hook only checks staged files)
```

## Step 10: Create Related Hooks

Now that you understand hooks, create more!

### Hook 2: Prevent Pushing to Main

`.claude/hooks/prevent-main-push.sh`:
```bash
#!/bin/bash

BRANCH=$(git rev-parse --abbrev-ref HEAD)

if [[ "$BRANCH" == "main" || "$BRANCH" == "master" ]]; then
  echo "❌ BLOCK: Cannot push directly to $BRANCH"
  echo "Create a feature branch instead!"
  exit 1
fi

echo "✅ ALLOW: Pushing to $BRANCH"
exit 0
```

Configure in settings.json:
```json
{
  "hooks": {
    "tool-call": {
      "Bash": {
        "git push": {
          "command": "bash .claude/hooks/prevent-main-push.sh",
          "description": "Prevents pushing to main/master",
          "blocking": true
        }
      }
    }
  }
}
```

### Hook 3: Session Logger

`.claude/hooks/session-logger.sh`:
```bash
#!/bin/bash

LOG_FILE=".claude/session.log"
echo "[$(date)] Claude Code session started" >> $LOG_FILE
exit 0
```

Configure:
```json
{
  "hooks": {
    "session-start": {
      "command": "bash .claude/hooks/session-logger.sh",
      "description": "Logs session starts",
      "blocking": false
    }
  }
}
```

## Complete settings.json Example

```json
{
  "hooks": {
    "tool-call": {
      "Bash": {
        "git commit": {
          "command": "bash .claude/hooks/check-debug-code.sh",
          "description": "Checks for debugging code before commits",
          "blocking": true
        },
        "git push": {
          "command": "bash .claude/hooks/prevent-main-push.sh",
          "description": "Prevents pushing to main/master",
          "blocking": true
        }
      }
    },
    "session-start": {
      "command": "bash .claude/hooks/session-logger.sh",
      "description": "Logs session activity",
      "blocking": false
    }
  }
}
```

## Common Issues & Solutions

### Issue 1: Hook Doesn't Run

**Problem:** Created hook but it never executes

**Solutions:**
1. Check settings.json syntax (must be valid JSON)
2. Verify event name is correct
3. Make script executable: `chmod +x script.sh`
4. Test script manually: `bash .claude/hooks/script.sh`
5. Restart Claude Code

### Issue 2: Hook Blocks Everything

**Problem:** Hook blocks all commits even when clean

**Solutions:**
1. Test script manually to see output
2. Check exit codes (0 = allow, 1 = block)
3. Add debug output: `set -x` at top of script
4. Verify logic is correct

### Issue 3: Hook Script Errors

**Problem:** Hook has syntax errors

**Solutions:**
1. Test script independently: `bash -n script.sh` (syntax check)
2. Run with debugging: `bash -x script.sh`
3. Check for common issues:
   - Missing `#!/bin/bash` at top
   - Incorrect if/then/fi syntax
   - Missing quotes around variables

### Issue 4: Can't Find Git Commands

**Problem:** Script can't run git commands

**Solutions:**
1. Verify you're in a git repository
2. Check git is installed: `which git`
3. Use full paths: `/usr/bin/git` instead of `git`

## Best Practices

### ✅ Do:
- Keep hooks focused and fast
- Provide clear error messages
- Allow override with --no-verify
- Test thoroughly before deploying
- Document what each hook does
- Use exit 0 for allow, exit 1 for block

### ❌ Don't:
- Make hooks too slow (< 1 second ideal)
- Block without clear explanation
- Modify files in blocking hooks
- Forget to make scripts executable
- Use hooks for tasks better suited to commands

## Hook Ideas to Try Next

1. **File Size Checker**: Block commits with files > 10MB
2. **Test Runner**: Ensure tests pass before commit
3. **Linter**: Run eslint/prettier before commit
4. **Secret Scanner**: Check for API keys or passwords
5. **Branch Naming**: Enforce branch naming conventions
6. **Commit Message**: Validate commit message format
7. **Dependencies**: Check for updated package versions

## Understanding Hook Events

### user-prompt-submit
- Runs when you send a message to Claude
- Use for: Validation, logging, context injection
- Blocking: Can prevent Claude from processing

### tool-call (specific tools)
- Runs when Claude uses a specific tool
- Use for: Safety checks, logging, validation
- Blocking: Can prevent tool execution

### session-start
- Runs when Claude Code starts
- Use for: Initialization, logging, setup
- Usually non-blocking

### session-end
- Runs when Claude Code exits
- Use for: Cleanup, logging, backups
- Usually non-blocking

## Next Steps

### Level 1: Practice
- Create 2-3 more hooks
- Customize existing hooks
- Test edge cases

### Level 2: Advanced Hooks
- Combine multiple checks
- Create hook chains
- Add configuration files

### Level 3: Team Hooks
- Share hooks via git
- Create team standards
- Document for teammates

## Congratulations!

You've created your first hook! 🎉

**What you learned:**
- ✅ How hooks work
- ✅ Hook configuration format
- ✅ Writing bash scripts for hooks
- ✅ Testing and debugging hooks
- ✅ Exit codes (0 vs 1)
- ✅ Blocking vs non-blocking hooks
- ✅ Common hook patterns

**Next challenges:**
1. Create a hook that runs tests before commit
2. Build a hook that validates commit messages
3. Create a session-start hook that checks for updates
4. Combine multiple hooks into a workflow

---

**Ready for more? Continue with [creating-a-subagent.md](./creating-a-subagent.md)!**
