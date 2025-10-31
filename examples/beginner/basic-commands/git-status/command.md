Show a clean, formatted git status with:

1. Current branch name
2. Commits ahead/behind remote
3. Staged changes (green)
4. Unstaged changes (red)
5. Untracked files
6. Helpful next steps

## Format the output nicely:

```
📍 Branch: main
🔗 Remote: origin/main (up to date)

✅ Staged Changes (3 files):
  - modified: src/app.js
  - new file: src/utils.js
  - deleted: old-file.js

⚠️  Unstaged Changes (2 files):
  - modified: README.md
  - modified: package.json

📝 Untracked Files:
  - temp.log
  - draft.md

💡 Next Steps:
  - Review unstaged changes: git diff
  - Stage all changes: git add -A
  - Commit changes: /commit
  - Discard changes: git restore <file>
```

## Instructions:

1. Run `git status --porcelain -b` to get machine-readable status
2. Run `git status` for human-readable version
3. Format the output with emojis and colors
4. Group by status (staged/unstaged/untracked)
5. Provide helpful next step suggestions based on current state

## Edge Cases:

- If no changes: "✨ Working tree clean!"
- If detached HEAD: Warn and explain
- If merge conflict: Highlight and suggest resolution
- If no remote: Note "No remote configured"
