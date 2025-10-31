# Git Undo Command - Beginner Example

A safe way to undo your last commit while keeping all your changes intact.

## What This Example Teaches

- Git reset operations
- Safety checks before destructive operations
- Explaining git concepts clearly
- Providing alternatives for different scenarios
- Distinguishing local vs remote changes

## How to Use

### 1. Install the Command

```bash
# Copy to your .claude/commands directory
mkdir -p .claude/commands
cp command.md .claude/commands/git-undo.md
```

### 2. Use It

```bash
cd your-project
claude

# Then use:
/git-undo
```

## Example Usage

### Scenario: You just committed but want to make more changes

**You type:**
```
/git-undo
```

**Claude responds:**
```
🔄 Undo Last Commit

Last commit details:
  Commit: 7a3c9e2
  Message: "fix: resolve validation error"
  Author: You
  Time: 5 minutes ago
  Changes:
    - Modified: src/validator.js (12 lines)
    - Modified: tests/validator.test.js (5 lines)

What will happen:
  ✅ Commit 7a3c9e2 will be removed from history
  ✅ Your changes will remain as staged files
  ✅ You can edit and commit again with new message

This commit has NOT been pushed to remote - safe to undo.

Proceed? (yes/no)
```

**You:** yes

**Claude:**
```
Undoing commit...

✅ Commit undone successfully!

Current status:
  Changes staged for commit:
    - modified: src/validator.js
    - modified: tests/validator.test.js

Your changes are preserved. You can now:
  1. Make additional changes
  2. Commit with a new message: /git-commit-quick
  3. Or discard changes: git restore --staged .
```

### Scenario: Commit was already pushed

**You type:**
```
/git-undo
```

**Claude responds:**
```
⚠️  Warning: Pushed Commit Detected

Last commit:
  Commit: 3f8a2c1
  Message: "feat: add new dashboard"
  Status: PUSHED to origin/main

⚠️  This commit has been pushed to remote!

Undoing it locally would:
  ❌ Create history mismatch with remote
  ❌ Cause problems for other developers
  ❌ Require force push (dangerous)

Recommended alternatives:

1. **Revert the commit** (safe):
   git revert 3f8a2c1
   This creates a new commit that undoes the changes.

2. **Create a fix commit** (safest):
   Make your corrections and commit normally.

3. **Force push** (only if you're sure nobody pulled this):
   Use with extreme caution!

Would you like me to:
  a) Revert the commit (recommended)
  b) Explain these options in detail
  c) Cancel
```

## What Makes This Useful?

### Safe by Default
- Uses `--soft` reset (keeps changes)
- Checks if commit was pushed
- Explains what will happen
- Asks for confirmation

### Educational
- Explains git concepts
- Shows alternatives
- Teaches best practices
- Warns about dangers

### Practical
- Common use case
- Quick to use
- Clear output
- Reversible

## Customization Ideas

### Add More Undo Options
```markdown
## Undo Variants

/git-undo 1      # undo last commit (default)
/git-undo 3      # undo last 3 commits
/git-undo-hard   # undo and discard changes (⚠️ dangerous)
```

### Add Undo History
```markdown
## Show What Will Be Undone

Before undoing, show:
- Commit messages for all commits being undone
- Total lines changed
- Files affected
- Time period covered
```

### Add Redo Capability
```markdown
## Redo Support

After undoing, save the commit hash:
"To redo this undo: git reset --hard 7a3c9e2"

Or create /git-redo command
```

## Common Issues

### No commits to undo?

**Response:**
```
ℹ️  No Commits to Undo

This repository has no commits yet.
Or you're already at the initial commit.
```

### Uncommitted changes present?

**Warning:**
```
⚠️  Uncommitted Changes Detected

You have uncommitted changes in your working directory.
Undoing the last commit will add more uncommitted changes.

Current uncommitted:
  - modified: src/app.js

This might be confusing. Recommended:
  1. Commit or stash current changes first
  2. Then undo the previous commit

Proceed anyway? (yes/no)
```

### Merge commit?

**Special handling:**
```
⚠️  Merge Commit Detected

Last commit is a merge commit.
Undoing this is more complex.

Options:
  1. Undo the merge: git reset --soft HEAD~1
  2. Or specify which parent to keep

This requires extra care. Proceed? (yes/no)
```

## Git Reset Options Explained

### --soft (Default, Safest)
```
git reset --soft HEAD~1

✅ Removes commit
✅ Keeps changes staged
✅ Ready to commit again
```

### --mixed (Middle Ground)
```
git reset HEAD~1

✅ Removes commit
✅ Keeps changes unstaged
⚠️  Need to git add again
```

### --hard (Dangerous!)
```
git reset --hard HEAD~1

❌ Removes commit
❌ DELETES changes
⚠️  Cannot be undone!
```

## Tips for Use

### When to Use Git Undo
✅ Just committed but forgot something
✅ Want to change commit message substantially
✅ Need to split one commit into multiple
✅ Commit hasn't been pushed yet

### When NOT to Use
❌ Commit already pushed to shared branch
❌ Other people have pulled your changes
❌ Want to reverse effects (use `git revert`)
❌ On main/master branch with others working

### Best Practices
1. **Check push status first** - Never undo pushed commits on shared branches
2. **Use soft reset** - Always keep your changes unless certain
3. **Consider alternatives** - Sometimes a new commit is better
4. **Communicate** - If working with team, coordinate

## Learning Opportunities

### Understanding Git Reset
Learn the three modes:
- `--soft`: Move HEAD, keep staging and working directory
- `--mixed`: Move HEAD, reset staging, keep working directory
- `--hard`: Move HEAD, reset everything

### Local vs Remote
Understand the difference:
- Local commits: Safe to modify
- Pushed commits: Dangerous to change
- Shared branches: Coordinate with team

### Git History
Learn about:
- HEAD pointer
- Commit history
- Rewriting history
- When it's safe vs dangerous

## Related Commands

- `/git-commit-quick` - Quick commit after undoing
- `/git-status` - Check current state
- `/git-revert` - Safely undo pushed commits

## Next Steps

### Extend This Command
- Support undoing multiple commits
- Add interactive mode to choose what to undo
- Show diff of what will be undone
- Provide redo functionality

### Create Related Commands
- `/git-revert-last` - Revert pushed commits safely
- `/git-amend` - Modify last commit without undoing
- `/git-reset-to` - Reset to specific commit

### Learn More About Git
- Rewriting history
- Interactive rebase
- Cherry-picking commits
- Git reflog (safety net)

## Files

- `command.md` - The command file (copy to `.claude/commands/`)
- `README.md` - This documentation

## Why This Pattern Works

### Safety First
- Checks before acting
- Uses safest option by default
- Warns about dangers
- Provides alternatives

### Clear Communication
- Explains what will happen
- Shows exact changes
- Uses simple language
- No git jargon

### Practical Value
- Solves common problem
- Quick to use
- Reduces errors
- Teaches git concepts
