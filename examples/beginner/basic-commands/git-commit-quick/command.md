Quick git commit with automatic message generation.

## Instructions

1. Run `git status` to see what files have changed
2. Run `git diff` to see the changes
3. Analyze the changes and generate a descriptive commit message
4. Show the user the proposed commit message
5. If user approves (or if changes are straightforward), proceed with:
   - `git add -A` to stage all changes
   - `git commit -m "your generated message"`
   - Show the result

## Commit Message Format

Follow conventional commit format:
- `feat: add new feature`
- `fix: resolve bug in X`
- `docs: update documentation`
- `style: format code`
- `refactor: restructure X`
- `test: add tests for Y`
- `chore: update dependencies`

## Example Output

```
📝 Quick Commit

Changes detected:
  Modified: src/app.js (added error handling)
  Modified: tests/app.test.js (added test cases)
  New file: docs/api.md (API documentation)

Proposed commit message:
  "feat: add error handling and API documentation"

Proceed with this commit? (yes/no)
```

## Usage

```bash
/git-commit-quick
```

Or with a custom message:
```bash
/git-commit-quick "custom commit message"
```

## Notes

- Always show the user what will be committed before committing
- Generate meaningful commit messages based on actual changes
- Don't commit if there are no changes
- Warn if there are uncommitted changes that look important
