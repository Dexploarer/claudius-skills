# Git Status - Slash Command

A prettier, more informative version of `git status` with helpful next steps.

## What It Does

This command shows you a clean, formatted view of your git repository status including:
- Current branch name and remote tracking
- Commits ahead/behind remote
- Staged changes (ready to commit)
- Unstaged changes (modified but not staged)
- Untracked files (not in git yet)
- Helpful suggestions for what to do next

## Installation

Copy the `command.md` file to your project's `.claude/commands/` directory:

```bash
cp command.md /path/to/your/project/.claude/commands/git-status.md
```

## Usage

```bash
/git-status
```

That's it! No arguments needed.

## Example Output

### Clean Working Tree
```
📍 Branch: main
🔗 Remote: origin/main (up to date)

✨ Working tree clean!

💡 Next Steps:
  - Pull latest changes: git pull
  - Create a new branch: git checkout -b feature-name
  - View commit history: git log
```

### With Changes
```
📍 Branch: feature-login
🔗 Remote: origin/feature-login (1 commit ahead)

✅ Staged Changes (3 files):
  - modified: src/auth/login.js
  - new file: src/auth/utils.js
  - deleted: src/old-auth.js

⚠️  Unstaged Changes (2 files):
  - modified: README.md
  - modified: package.json

📝 Untracked Files (2 files):
  - temp.log
  - notes.md

💡 Next Steps:
  - Review unstaged changes: git diff
  - Stage all changes: git add -A
  - Stage specific file: git add <file>
  - Commit staged changes: /commit or git commit
  - Push to remote: git push
```

### With Merge Conflicts
```
📍 Branch: main
🔗 Remote: origin/main (up to date)

⚠️  MERGE CONFLICT!

Conflicts in:
  - src/app.js
  - src/config.js

💡 Next Steps:
  1. Open conflicted files and resolve conflicts
  2. Look for <<<<<<< HEAD markers
  3. Edit files to keep desired changes
  4. Stage resolved files: git add <file>
  5. Complete merge: git commit
  6. Or abort merge: git merge --abort
```

### Detached HEAD
```
📍 Branch: HEAD detached at a3b5c7d
🔗 No remote branch

⚠️  You are in 'detached HEAD' state!

This means you're not on any branch. If you make commits here,
they might be lost when you switch branches.

💡 Next Steps:
  - Create a new branch here: git checkout -b new-branch-name
  - Return to a branch: git checkout main
  - Just looking around? No worries, just don't commit changes
```

## Why Use This Instead of Plain `git status`?

| Feature | Regular `git status` | This Command |
|---------|---------------------|--------------|
| Visual formatting | Plain text | Emojis and sections |
| Remote info | Sometimes unclear | Always clear |
| Grouping | Mixed together | Clearly separated |
| Next steps | None | Suggested actions |
| Beginner-friendly | Can be confusing | Easy to understand |
| Color/emphasis | Limited | Enhanced |

## When To Use

Use this command when you want to:
- Check what's changed before committing
- See if you're ahead/behind remote
- Get a quick overview of your git state
- Learn what to do next
- Have a cleaner view than `git status`

## Understanding the Output

### Branch Information
- **📍 Branch**: Which branch you're currently on
- **🔗 Remote**: Which remote branch it tracks (if any)
- **Ahead/Behind**: How many commits you're ahead or behind the remote

### Change Types

**✅ Staged Changes (Green)**
- These files are ready to be committed
- You've used `git add` on these
- They'll be included in your next commit

**⚠️ Unstaged Changes (Red)**
- These files are modified but not staged
- You need to `git add` them to include in commit
- Or use `git add -A` to stage all changes

**📝 Untracked Files**
- These files aren't tracked by git yet
- They're new files that haven't been added
- Use `git add <file>` to start tracking them

## Tips

1. **Run it often**: Check status before and after making changes
2. **Before committing**: Always check what you're about to commit
3. **After pulling**: See if pull brought in any changes
4. **Before switching branches**: Make sure working tree is clean
5. **When confused**: This command helps you understand where you are

## Common Scenarios

### Scenario 1: Ready to Commit
```
✅ Staged Changes (2 files)
⚠️  Unstaged Changes (0 files)
📝 Untracked Files (0 files)

→ You're ready! Use /commit or git commit -m "message"
```

### Scenario 2: Forgot to Stage Changes
```
✅ Staged Changes (0 files)
⚠️  Unstaged Changes (3 files)

→ Stage your changes first: git add -A
→ Then commit: /commit
```

### Scenario 3: Need to Push
```
Branch: feature-x (3 commits ahead)

→ Your commits are local only
→ Push them: git push or git push -u origin feature-x
```

### Scenario 4: Need to Pull
```
Branch: main (2 commits behind)

→ Remote has new commits
→ Pull them: git pull
→ Or fetch first: git fetch
```

## Customization

You can edit `command.md` to customize:
- The emoji symbols used
- What information is shown
- The format of suggestions
- Language and tone of next steps
- Additional git commands to suggest

## Keyboard Shortcuts

After using this command, Claude remembers your state and can help with:
- `/commit` - Commit staged changes
- `/review` - Review uncommitted changes
- `git add -A` - Stage all changes
- `git push` - Push to remote

## Learning Git

This command helps you learn git by:
- Showing you exactly what state you're in
- Explaining what each status means
- Suggesting appropriate next commands
- Using consistent, clear terminology

## Troubleshooting

### "Not a git repository"
```
❌ Error: Not a git repository

This directory is not tracked by git.

💡 To initialize git:
  git init
```

### "No remote configured"
```
📍 Branch: main
🔗 No remote configured

💡 To add a remote:
  git remote add origin <url>
```

### "Can't determine status"
```
❌ Error: Unable to read git status

Possible issues:
- Git is not installed
- Repository is corrupted
- Permissions issue

Try: git status (to see raw error)
```

## Related Commands

- `/commit` - Create a commit with good message
- `/git-undo` - Undo last commit
- `/git-sync` - Pull and push in one command
- `/review` - Review uncommitted changes

## Best Practices

✅ **Do:**
- Check status before committing
- Review staged changes before commit
- Keep working tree clean when switching branches
- Pull before starting new work

❌ **Don't:**
- Commit without checking what's staged
- Leave untracked files lying around (add to .gitignore if needed)
- Work with pending merge conflicts
- Push without reviewing local commits

## Advanced: Understanding Git States

```
Working Directory → Staging Area → Git Repository → Remote
     (edit)          (git add)      (git commit)   (git push)

Unstaged Changes → Staged Changes → Committed → Pushed
```

This command shows you exactly where your changes are in this flow!

## FAQ

**Q: How is this different from `git status`?**
A: It's the same information, just formatted better with helpful suggestions.

**Q: Does it modify anything?**
A: No! It's read-only. It just shows you information.

**Q: Can I use this in scripts?**
A: It's designed for interactive use. For scripts, use `git status --porcelain`.

**Q: Will this work with all git workflows?**
A: Yes! It works with standard git workflows, branches, remotes, etc.

**Q: Does it work with git submodules?**
A: Basic support yes, but submodules might need special attention.

## Examples for Different Situations

### Starting New Feature
```bash
/git-status  # Check you're on the right branch
# Shows: Clean working tree
# Suggested: Create feature branch
```

### Mid-Development
```bash
/git-status  # See what you've changed
# Shows: Several unstaged changes
# Suggested: Review with git diff, then stage
```

### Ready to Commit
```bash
/git-status  # Verify staged changes
# Shows: Files ready to commit
# Suggested: Use /commit
```

### Before Pull Request
```bash
/git-status  # Final check
# Shows: All committed, ahead of remote
# Suggested: Push to remote
```

---

**Pro Tip**: Use this command frequently! It's a great way to stay aware of your git state and learn git concepts through practice.
