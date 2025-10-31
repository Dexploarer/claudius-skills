# Git Sync Command - Beginner Example

A convenient command to keep your branch synchronized with the remote repository - pull the latest changes and push your commits.

## What This Example Teaches

- Combining git pull and push
- Checking branch status
- Handling merge conflicts
- Safety checks before operations
- Clear status reporting

## How to Use

### 1. Install the Command

```bash
# Copy to your .claude/commands directory
mkdir -p .claude/commands
cp command.md .claude/commands/git-sync.md
```

### 2. Use It

```bash
cd your-project
claude

# Then use:
/git-sync
```

## Example Usage

### Scenario: Normal sync with no conflicts

**You type:**
```
/git-sync
```

**Claude responds:**
```
🔄 Git Sync - feature/dashboard

Checking status...

Current state:
  • Branch: feature/dashboard
  • Remote: origin/feature/dashboard
  • Status: 3 commits ahead, 2 commits behind
  • Uncommitted changes: None ✓

This will:
  1. Pull 2 new commits from remote
  2. Merge them with your local branch
  3. Push your 3 local commits to remote

Proceed? (yes/no)
```

**You:** yes

**Claude:**
```
Syncing...

⬇️  Pulling from remote...
   Fetched 2 commits
   Updated files:
     - src/components/Chart.js
     - tests/chart.test.js

⬆️  Pushing to remote...
   Pushed 3 commits

✅ Sync complete!

Your branch is now up to date with origin/feature/dashboard.

Recent commits:
  • 7a3c9e2 (you) - feat: add dashboard widgets
  • 5f1b8a4 (you) - fix: chart rendering
  • 3e9d7c1 (you) - test: add chart tests
  • 8b2f4d6 (teammate) - refactor: improve chart performance
  • 1c5a9e3 (teammate) - docs: update API docs
```

### Scenario: Uncommitted changes warning

**You type:**
```
/git-sync
```

**Claude responds:**
```
⚠️  Uncommitted Changes Detected

You have uncommitted changes:
  • Modified: src/app.js
  • Modified: src/utils.js
  • New file: src/config.js

Syncing with uncommitted changes can cause:
  • Merge conflicts
  • Lost changes
  • Confusion

Recommended actions:
  1. Commit your changes: /git-commit-quick
  2. Or stash them: git stash
  3. Then sync: /git-sync

Proceed anyway? (not recommended) (yes/no)
```

### Scenario: Merge conflicts

**You type:**
```
/git-sync
```

**After pulling:**
```
⚠️  Merge Conflicts

Pulled changes conflict with your local changes.

Conflicted files:
  • src/app.js
  • src/components/Header.js

To resolve:

1. Open each file and look for conflict markers:
   <<<<<<< HEAD (your changes)
   ...
   =======
   ...
   >>>>>>> origin/feature (remote changes)

2. Edit to keep the correct version

3. Remove conflict markers

4. Stage resolved files:
   git add src/app.js src/components/Header.js

5. Complete the merge:
   git commit

6. Then sync again:
   /git-sync

Need help resolving conflicts? Just ask!
```

## What Makes This Useful?

### Convenient
- One command does pull + push
- No need to remember branch names
- Automatic status checking

### Safe
- Checks for uncommitted changes
- Warns before potentially destructive operations
- Handles errors gracefully

### Informative
- Shows what will happen before doing it
- Reports exactly what changed
- Provides clear next steps

## Customization Ideas

### Add Auto-Stash
```markdown
## Auto-Stash Option

If uncommitted changes:
1. Automatically stash them
2. Pull and push
3. Pop stash back
4. Report any conflicts
```

### Add Rebase Option
```markdown
## Sync with Rebase

Instead of merge, use rebase:
  git pull --rebase origin <branch>

Keeps history linear.
Use: /git-sync --rebase
```

### Add Force Push Protection
```markdown
## Never Force Push

Block force push attempts:
- Detect diverged history
- Explain the situation
- Suggest proper resolution
- Never use --force automatically
```

### Add Multiple Remotes
```markdown
## Sync to Multiple Remotes

If repository has multiple remotes:
1. List all remotes
2. Ask which to sync with
3. Or sync with all: /git-sync --all
```

## Common Issues

### No remote branch?

**Response:**
```
ℹ️  No Remote Branch

Your branch "feature/new-feature" doesn't exist on remote yet.

To push it:
  git push -u origin feature/new-feature

This will:
  • Create the branch on remote
  • Set up tracking
  • Push your commits

Proceed? (yes/no)
```

### Diverged history?

**Warning:**
```
⚠️  Diverged History

Your branch and origin/feature have diverged:
  • Your branch: 3 commits ahead
  • Remote branch: 2 commits ahead
  • Common ancestor: 5b3a7c9

This means you and someone else made different commits.

Options:
  1. Pull and merge (creates merge commit)
  2. Pull with rebase (linear history)
  3. Force push (⚠️ dangerous - will lose remote commits)

Recommended: Option 1 (merge)
Proceed with merge? (yes/no)
```

### Network error?

**Error handling:**
```
❌ Sync Failed

Could not connect to remote:
  fatal: unable to access 'https://github.com/...':
  Connection timeout

Possible causes:
  • No internet connection
  • GitHub is down
  • Repository deleted
  • Access revoked

Try:
  1. Check your internet connection
  2. Verify repository exists
  3. Check your access permissions
  4. Try again later
```

## Git Operations Explained

### Pull (Fetch + Merge)
```bash
git pull origin feature-branch

Does:
1. git fetch origin (download commits)
2. git merge origin/feature-branch (merge them)
```

### Push
```bash
git push origin feature-branch

Does:
• Upload your local commits to remote
• Update remote branch pointer
```

### Full Sync
```bash
git pull origin feature-branch
git push origin feature-branch

Ensures local and remote are identical
```

## Tips for Use

### Before Syncing
✅ Commit your changes first
✅ Make sure tests pass
✅ Review what you're pushing

### When to Sync
✅ Start of each work session (pull latest)
✅ End of each feature (push your work)
✅ Before creating pull request
✅ After resolving conflicts

### Best Practices
1. **Sync frequently** - Avoid large merges
2. **Commit before sync** - Keep changes separate
3. **Pull before push** - Stay up to date
4. **Communicate** - Let team know about big changes

## Learning Opportunities

### Understanding Git Remotes
Learn about:
- Remote repositories
- Tracking branches
- Fetch vs pull
- Push mechanics

### Merge vs Rebase
Understand:
- When to merge
- When to rebase
- Trade-offs
- History management

### Conflict Resolution
Practice:
- Reading conflict markers
- Choosing correct version
- Testing after resolution
- Preventing conflicts

## Related Commands

- `/git-commit-quick` - Commit before syncing
- `/git-status` - Check status before syncing
- `/git-undo` - Undo if sync goes wrong

## Next Steps

### Extend This Command
- Add interactive mode for conflicts
- Support multiple remotes
- Add rebase option
- Show detailed diff of changes

### Create Related Commands
- `/git-pull-all` - Pull all branches
- `/git-push-force` - Safe force push (with checks)
- `/git-sync-check` - Dry run to see what would sync

### Integrate With Workflow
- Auto-sync on branch switch
- Pre-push hooks
- Conflict prevention
- Team notifications

## Files

- `command.md` - The command file (copy to `.claude/commands/`)
- `README.md` - This documentation

## Why This Pattern Works

### Reduces Complexity
- One command instead of two
- Automatic branch detection
- Handles common cases

### Prevents Errors
- Checks state first
- Warns about problems
- Provides guidance

### Saves Time
- Quick synchronization
- No manual branch tracking
- Clear status reporting

### Teaches Best Practices
- Commit before sync
- Pull before push
- Handle conflicts properly
- Stay synchronized
