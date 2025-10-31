Synchronize your local branch with remote - pull latest changes and push your commits.

## Instructions

1. Check git status to see current state
2. Check if there are uncommitted changes (warn user if so)
3. Get current branch name
4. Show the user what will happen:
   - Pull from remote
   - Push local commits (if any)
5. Ask for confirmation
6. If confirmed:
   - Run `git pull origin <current-branch>`
   - If successful and there are commits to push, run `git push origin <current-branch>`
7. Show the results

## What This Does

- **Pulls** latest changes from remote
- **Pushes** your commits to remote
- **Syncs** your branch with the team

## Safety Checks

Before syncing:
- ⚠️ Warn if uncommitted changes exist (recommend committing first)
- ⚠️ Check if on main/master (different message)
- ⚠️ Check if remote exists
- ⚠️ Handle merge conflicts gracefully

## Example Output

```
🔄 Git Sync

Current branch: feature/user-auth
Remote: origin/feature/user-auth

Status:
  • Local commits: 2 ahead
  • Remote commits: 1 behind
  • Uncommitted changes: None ✓

This will:
  1. Pull 1 new commit from remote
  2. Push your 2 local commits to remote

Proceed with sync? (yes/no)
```

## After Sync

```
✅ Sync complete!

Pulled changes:
  - 1 commit from origin/feature/user-auth
  - Files updated: 3
  - No conflicts

Pushed changes:
  - 2 commits to origin/feature/user-auth

Your branch is now in sync with remote.
```

## Handle Conflicts

If merge conflicts occur:
```
⚠️  Merge Conflicts Detected

Conflicts in:
  - src/app.js
  - src/utils.js

Sync paused. To resolve:
  1. Open conflicted files
  2. Resolve conflicts (look for <<<<<<)
  3. Run: git add <resolved-files>
  4. Run: git commit
  5. Try sync again: /git-sync
```

## Usage

```bash
# Sync current branch
/git-sync

# Just pull (no push)
/git-sync pull

# Just push (no pull)
/git-sync push
```

## Arguments

- No args: Pull then push (full sync)
- `pull`: Only pull from remote
- `push`: Only push to remote

Parse from $ARGUMENTS if provided.

## Notes

- Always check for uncommitted changes first
- Explain what will happen before doing it
- Handle errors gracefully (no remote, conflicts, etc.)
- Provide helpful next steps if something fails
