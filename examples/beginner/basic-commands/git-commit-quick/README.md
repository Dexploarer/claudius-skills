# Git Commit Quick Command - Beginner Example

A handy command that analyzes your changes and creates a commit with an auto-generated meaningful message.

## What This Example Teaches

- Creating workflow shortcuts
- Analyzing git changes
- Generating context-aware messages
- User confirmation patterns
- Combining multiple git commands

## How to Use

### 1. Install the Command

```bash
# Copy to your .claude/commands directory
mkdir -p .claude/commands
cp command.md .claude/commands/git-commit-quick.md
```

### 2. Use It

```bash
cd your-project
claude

# Then use:
/git-commit-quick
```

### 3. It Will:
1. Check what files changed
2. Analyze the changes
3. Generate a commit message
4. Ask for your approval
5. Commit if you confirm

## Example Usage

**You type:**
```
/git-commit-quick
```

**Claude responds:**
```
📝 Quick Commit Analysis

Changes detected:
  ✏️  Modified: src/components/Button.js
      - Added disabled state
      - Fixed hover effect

  ✏️  Modified: src/styles/button.css
      - Added disabled styles

  ✨ New: tests/Button.test.js
      - Added test for disabled state

Proposed commit message:
  "feat: add disabled state to Button component"

This follows conventional commit format (feat: = new feature).

Proceed with commit? (yes/no)
```

**You:** yes

**Claude:**
```
Committing changes...

✅ Commit successful!

[main 7a3c9e2] feat: add disabled state to Button component
 3 files changed, 45 insertions(+), 3 deletions(-)
 create mode 100644 tests/Button.test.js

Your changes have been committed.
```

## What Makes This Useful?

### Saves Time
- No need to type `git add`, `git commit -m`
- Automatic message generation
- One command does it all

### Better Commit Messages
- Analyzes actual changes
- Follows conventions
- More descriptive than "fix stuff"

### Safe
- Shows you what will be committed
- Asks for confirmation
- Doesn't commit unexpected changes

## Customization Ideas

### Add Emoji Support
```markdown
## Emoji Commit Style

- ✨ feat: new feature
- 🐛 fix: bug fix
- 📝 docs: documentation
- 💅 style: formatting
- ♻️ refactor: refactoring
- ✅ test: tests
```

### Team Conventions
```markdown
## Commit Format

Always include:
- Ticket number: [PROJ-123]
- Type: feat/fix/docs
- Brief description

Example: "[PROJ-123] feat: add user authentication"
```

### Auto-Push Option
```markdown
## After Committing

Ask user: "Push to remote? (yes/no)"
If yes: git push origin <current-branch>
```

### Branch Check
```markdown
## Safety Check

Before committing:
1. Check current branch
2. Warn if on main/master
3. Suggest creating feature branch if needed
```

## Common Issues

### No changes to commit?

**Result:**
```
ℹ️  No changes detected

Working tree is clean. Nothing to commit.
```

### Too many changes?

**Suggestion:**
```
⚠️  Large changeset detected (15 files)

Consider:
1. Committing related changes separately
2. Using git add <specific-files> for partial commits
3. Reviewing changes with /git-status first
```

### Merge conflicts?

**Warning:**
```
🚨 Merge conflict detected

Cannot commit while conflicts exist.
Resolve conflicts first, then try again.
```

## Tips for Use

### Before Committing
- Review changes: `/git-status`
- Check diff: `git diff`
- Make sure tests pass

### Good Commit Messages
- **Be specific**: "fix login validation" not "fix bug"
- **Use imperative**: "add feature" not "added feature"
- **Mention context**: "fix: resolve error when username is empty"

### When to Use
✅ Small, focused changes
✅ Clear, related modifications
✅ Ready to commit everything

❌ Large, unrelated changes
❌ Work in progress
❌ Experimental code

## Learning Opportunities

### Understanding Git Workflow
Learn the typical commit cycle:
1. Make changes
2. Review changes (`git status`, `git diff`)
3. Stage changes (`git add`)
4. Commit (`git commit`)
5. Push (optional)

### Commit Message Conventions
Practice writing good commit messages:
- Conventional Commits format
- Clear, descriptive messages
- Proper categorization (feat, fix, etc.)

### Combining Commands
See how multiple git commands work together:
- `git status` for overview
- `git diff` for details
- `git add` for staging
- `git commit` for saving

## Related Commands

- `/git-status` - See what's changed
- `/git-undo` - Undo last commit
- `/git-sync` - Pull latest and push changes

## Next Steps

### Extend This Command
- Add support for partial commits
- Include pre-commit hooks
- Add automatic testing before commit
- Generate more detailed messages

### Create Related Commands
- `/git-amend` - Amend last commit
- `/git-fixup` - Create fixup commit
- `/git-wip` - Quick "work in progress" commit

### Integrate With Workflow
- Use before switching branches
- Pair with code review process
- Combine with deployment scripts

## Files

- `command.md` - The command file (copy to `.claude/commands/`)
- `README.md` - This documentation

## Why This Pattern Works

### Reduces Friction
- Makes committing easier
- Encourages frequent commits
- Removes repetitive typing

### Improves Quality
- Better commit messages
- Consistent format
- More descriptive

### Maintains Safety
- Shows changes before committing
- Asks for confirmation
- No surprises
