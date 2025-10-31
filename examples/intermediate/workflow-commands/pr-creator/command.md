Create a GitHub pull request with auto-generated description from commits.

## Instructions

1. Check current branch and commits
2. Get commit history since branching from main
3. Analyze changes to generate PR description
4. Create PR using gh CLI

## Steps

### 1. Verify State
```bash
# Current branch
git branch --show-current

# Commits ahead of main
git log main..HEAD --oneline

# Check if gh CLI available
gh --version
```

### 2. Generate PR Description

Analyze commits and changes to create:

```markdown
## Summary
- Brief overview of changes
- Key features added
- Bugs fixed

## Changes
- List major changes
- Link related issues

## Testing
- [ ] Unit tests pass
- [ ] Manual testing done
- [ ] No breaking changes

## Screenshots
(if UI changes)
```

### 3. Create PR
```bash
gh pr create \
  --title "feat: descriptive title" \
  --body "$(cat <<'EOF'
[generated description]
EOF
)" \
  --base main
```

## Usage

```bash
/pr-creator

# Or with title
/pr-creator "Add user authentication"
```

## Arguments

- $1: PR title (optional, will generate if not provided)
- $2: Base branch (optional, defaults to main)
