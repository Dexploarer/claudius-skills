# PR Creator Command - Intermediate Example

An intelligent pull request creation command that analyzes changes and generates comprehensive PR descriptions.

## What This Teaches

- Git analysis and diff parsing
- PR description generation
- GitHub CLI integration
- Markdown formatting
- Automated workflows

## Installation

```bash
cp command.md /path/to/your-project/.claude/commands/pr-creator.md
```

## Usage

```bash
/pr-creator [base-branch]

# Examples:
/pr-creator main
/pr-creator develop
/pr-creator
```

## What It Does

Automated PR creation:
1. **Analyze changes** - Review commits and diffs
2. **Generate title** - Descriptive, conventional format
3. **Create description** - Summary, changes, testing
4. **Add checklist** - Review, testing, documentation
5. **Link issues** - Auto-detect and reference
6. **Create PR** - Using GitHub CLI

## Example Output

**Generated PR:**

```markdown
Title: feat(auth): add JWT authentication with refresh tokens

## Summary

Implements JWT-based authentication system with refresh token support. Users can now log in using email/password and receive both access and refresh tokens. Access tokens expire after 15 minutes, while refresh tokens are valid for 7 days.

## Changes

### Added
- JWT token generation and validation
- Refresh token mechanism
- Token expiration handling
- Secure cookie storage for refresh tokens
- Authentication middleware

### Modified
- User model to include refresh token field
- Login endpoint to return tokens
- Protected routes to verify JWT

### Database
- Added `refresh_token` column to users table
- Added `token_expiry` column

## Testing

### Manual Testing
- [x] User can log in and receive tokens
- [x] Access token expires correctly
- [x] Refresh token flow works
- [x] Invalid tokens are rejected
- [x] Logout clears tokens

### Automated Tests
- [x] Unit tests for token generation
- [x] Unit tests for token validation
- [x] Integration tests for auth flow
- [x] Test coverage > 90%

## Screenshots/Demos

N/A - Backend changes only

## Breaking Changes

⚠️ **BREAKING**: Login endpoint response format changed

**Before:**
\```json
{ "token": "..." }
\```

**After:**
\```json
{
  "accessToken": "...",
  "refreshToken": "...",
  "expiresIn": 900
}
\```

Migration: Update all clients to use new response format

## Checklist

- [x] Code follows project style guidelines
- [x] Self-review completed
- [x] Comments added for complex logic
- [x] Documentation updated
- [x] Tests added/updated
- [x] All tests passing
- [x] No new warnings
- [x] Dependent changes merged
- [x] Reviewed security implications

## Related Issues

Closes #234
Relates to #156

## Additional Notes

- Tokens are stored as HTTP-only cookies for security
- Redis cache used for token blacklisting
- Consider adding rate limiting in future PR
```

## Command Implementation

`.claude/commands/pr-creator.md`:

```markdown
# PR Creator

Create a pull request with auto-generated description.

## Usage
/pr-creator [base-branch]

## Instructions

### Step 1: Get Base Branch

From $ARGUMENTS or ask: "PR to which branch? (main/develop)"

Default: main

### Step 2: Analyze Changes

\```bash
# Get current branch
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Get commits since branching
git log $BASE_BRANCH..$CURRENT_BRANCH --oneline

# Get file changes
git diff $BASE_BRANCH...$CURRENT_BRANCH --stat

# Get actual changes
git diff $BASE_BRANCH...$CURRENT_BRANCH
\```

### Step 3: Generate PR Title

Based on commits and changes:

**Format:** `type(scope): description`

**Type:**
- feat: New feature
- fix: Bug fix
- docs: Documentation
- refactor: Code refactoring
- test: Adding tests
- chore: Maintenance

**Examples:**
- "feat(auth): add JWT authentication"
- "fix(api): correct validation in user endpoint"
- "docs(readme): update installation instructions"

### Step 4: Generate Description

Analyze changes and create:

\```markdown
## Summary
[1-3 sentence overview]

## Changes
[Bullet points of key changes]

## Testing
[How it was tested]

## Breaking Changes
[If any]

## Related Issues
Closes #[issue-number]
\```

### Step 5: Create PR

\```bash
# Using GitHub CLI
gh pr create \
  --base $BASE_BRANCH \
  --title "$TITLE" \
  --body "$DESCRIPTION"
\```

Or show the command to run manually.

### Step 6: Show Summary

\```
✅ Pull Request Created!

📝 Title: $TITLE
🔗 URL: $PR_URL
🎯 Base: $BASE_BRANCH
📊 Changes: $NUM_FILES files, +$ADDITIONS/-$DELETIONS

Next steps:
- Review the PR description
- Request reviewers
- Link to project board
- Monitor CI/CD checks
\```
```

## Features

### Smart Analysis
- Detects change patterns
- Identifies breaking changes
- Auto-links issues
- Suggests labels

### Conventional Commits
- Follows conventional commit format
- Auto-detects type from commits
- Proper scope extraction

### Complete Descriptions
- Summary from commits
- Detailed change list
- Testing checklist
- Breaking change warnings

### GitHub Integration
- Uses GitHub CLI
- Sets labels automatically
- Requests reviewers
- Links to projects

## Customization

### Add Team Template

```markdown
## Our PR Template

\```markdown
## Ticket

JIRA-1234

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation

## Description

[Describe changes]

## Testing Instructions

1. Checkout branch
2. Run: npm install
3. Test: ...

## Screenshots

[If UI changes]

## Deployment Notes

[Any special deployment steps]
\```
```

### Add Auto-Reviewers

```bash
# Request reviewers based on files changed
if git diff --name-only | grep -q "frontend/"; then
    gh pr edit --add-reviewer @frontend-team
fi

if git diff --name-only | grep -q "backend/"; then
    gh pr edit --add-reviewer @backend-team
fi
```

### Add Labels

```bash
# Auto-label based on changes
if git diff | grep -q "package.json"; then
    gh pr edit --add-label "dependencies"
fi

if git diff | grep -q "BREAKING"; then
    gh pr edit --add-label "breaking-change"
fi
```

## Real-World Examples

### Feature PR
```
Title: feat(dashboard): add analytics widgets
Changes: New charts, data fetching, responsive layout
Tests: Jest tests, Storybook stories
Size: Large (+850, -120)
```

### Bug Fix PR
```
Title: fix(auth): prevent session expiry during active use
Changes: Update token refresh logic
Tests: Added test for edge case
Size: Small (+25, -10)
```

### Refactoring PR
```
Title: refactor(api): extract validation to middleware
Changes: New middleware, updated routes
Tests: Existing tests still pass
Size: Medium (+200, -180)
```

## Best Practices

### ✅ Do:
- Write clear, descriptive titles
- Include testing details
- Note breaking changes
- Link related issues
- Add helpful context
- Request appropriate reviewers

### ❌ Don't:
- Create PRs without description
- Skip testing section
- Ignore breaking changes
- Forget to link issues
- Create huge PRs (split them!)

## Troubleshooting

**Problem:** GitHub CLI not installed

**Solution:**
```bash
# Install gh CLI
brew install gh  # macOS
# or
sudo apt install gh  # Linux

# Authenticate
gh auth login
```

**Problem:** PR description not helpful

**Solution:** Be more specific in commits:
```bash
# Bad
git commit -m "fix stuff"

# Good
git commit -m "fix(auth): prevent null pointer in token validation"
```

## Integration

### With CI/CD

PR creation triggers:
- Automated tests
- Code coverage reports
- Security scanning
- Deployment previews

### With Project Management

```bash
# Auto-add to project board
gh pr edit --add-project "Sprint 23"

# Set milestone
gh pr edit --milestone "v2.0"
```

## Next Steps

1. Install PR creator command
2. Test with a feature branch
3. Customize description template
4. Set up auto-reviewers
5. Integrate with workflow

---

**Pro Tip:** Combine with a commit-message-generator subagent for perfect commit messages that generate perfect PR descriptions!
