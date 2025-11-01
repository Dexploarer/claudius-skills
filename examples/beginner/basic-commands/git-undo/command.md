Safely undo the last git commit while preserving your changes.

## Instructions

1. Check the current git status
2. Show the user the last commit that will be undone:
   - Commit message
   - Files changed
   - When it was made
3. Explain what will happen: commit removed, changes kept as uncommitted
4. Ask for confirmation
5. If confirmed, run: `git reset --soft HEAD~1`
6. Show the result with `git status`

## What This Does

- **Removes** the last commit from history
- **Keeps** all your changes as uncommitted (staged)
- **Preserves** your work completely
- Does NOT touch the working directory

## Safety Notes

⚠️ **Warning if:**
- The commit has been pushed to remote (dangerous to undo)
- Multiple commits exist on this branch (suggest being more specific)
- Working directory has uncommitted changes (might be confusing)

## Example Output

```
🔄 Undo Last Commit

Last commit:
  7a3c9e2 - "feat: add disabled state to Button component"
  Author: John Doe
  Date: 2 hours ago
  Files: 3 changed

This will:
  ✅ Remove this commit from history
  ✅ Keep your changes as uncommitted (staged)
  ❌ NOT delete any of your work

⚠️  Note: This commit has NOT been pushed to remote.
   Safe to undo locally.

Proceed with undo? (yes/no)
```

## Usage

```bash
# Undo last commit
/git-undo

# For more commits, be explicit
git reset --soft HEAD~3  # undo last 3
```

## Options

If user wants to:
- **Keep changes staged**: `git reset --soft HEAD~1` (default)
- **Keep changes unstaged**: `git reset HEAD~1` (mixed)
- **Discard changes completely**: `git reset --hard HEAD~1` (⚠️ dangerous!)

Always default to `--soft` (safest option).

## Notes

- Always check if commit has been pushed before undoing
- Explain the difference between local and remote commits
- Provide alternative if commit is already pushed (use `git revert` instead)
