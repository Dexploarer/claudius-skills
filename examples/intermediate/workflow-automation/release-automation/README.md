# Release Automation Workflow

Complete automation for production releases with version management, changelog generation, and team notifications.

## What It Does

This workflow automates:
- ✅ Pre-release validation (tests, linting, git status)
- ✅ Semantic version bumping
- ✅ Changelog generation
- ✅ Git tagging and pushing
- ✅ GitHub release creation
- ✅ Team notifications via Slack

## Installation

### 1. Copy the Release Command

```bash
cp examples/intermediate/workflow-automation/release-automation/release-command.md \
   .claude/commands/release.md
```

### 2. Setup MCP Integrations (Optional)

For GitHub releases and Slack notifications:

```bash
# Copy MCP template
cp templates/mcp-template.json .mcp.json

# Edit with your credentials
# Enable github and slack servers
```

### 3. Add Safety Hook (Recommended)

Add to `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "pattern": "Bash.*git push.*--tags",
        "command": "echo '🚀 Releasing...' && npm test",
        "timeout": 60000,
        "description": "Ensure tests pass before release"
      }
    ]
  }
}
```

## Usage

### Basic Release

```bash
/release
```

Claude will:
1. Analyze commits to suggest version
2. Run all validations
3. Complete the release process
4. Notify your team

### Specify Version Type

```bash
/release patch  # 1.2.3 → 1.2.4
/release minor  # 1.2.3 → 1.3.0
/release major  # 1.2.3 → 2.0.0
```

## Example Output

```
🔍 Pre-Release Validation
✅ Working directory clean
✅ On branch: main
✅ Up to date with origin
✅ Tests passed (42 tests, 0 failures)
✅ Linting passed

📊 Analyzing commits since v1.2.3...
Found:
- 5 feat commits (new features)
- 3 fix commits (bug fixes)
- 1 docs commit

💡 Recommended: minor version bump (1.2.3 → 1.3.0)

Proceed with v1.3.0? (y/n)
> y

📝 Updating version...
✅ Updated package.json
✅ Committed version bump

📄 Generating changelog...
✅ Updated CHANGELOG.md
✅ Committed changelog

🏷️  Creating git tag v1.3.0...
✅ Tag created

⬆️  Pushing to origin...
✅ Pushed main branch
✅ Pushed tags

🐙 Creating GitHub release...
✅ Release created: https://github.com/user/repo/releases/tag/v1.3.0

💬 Notifying team...
✅ Posted to #releases on Slack

🎉 Release v1.3.0 Complete!

Summary:
- Version: 1.3.0
- Commits: 9
- Features: 5
- Bug fixes: 3
- GitHub: https://github.com/user/repo/releases/tag/v1.3.0
```

## Components

### 1. Release Command
Main orchestrator that runs all steps in sequence.

### 2. Pre-Release Hooks
Safety checks that run before critical operations.

### 3. MCP Integrations
- **GitHub**: Creates releases
- **Slack**: Notifies team

### 4. Version Analysis
Analyzes commits using conventional commit format:
- `feat:` triggers minor bump
- `fix:` triggers patch bump
- `BREAKING CHANGE:` triggers major bump

## Customization

### For Python Projects

Update the command to use Python conventions:

```markdown
Update version in:
- pyproject.toml
- setup.py
- __version__.py

Run tests with:
- pytest
```

### For Different Branching Strategy

Modify branch checks:

```markdown
Ensure on correct branch:
- develop (for pre-release)
- main (for production)
```

### Custom Notifications

Add Discord, Teams, or email notifications by integrating additional MCP servers.

## Rollback Procedure

If something goes wrong:

```bash
# Delete the tag locally and remotely
git tag -d v1.3.0
git push origin :refs/tags/v1.3.0

# Delete GitHub release (via GitHub UI or MCP)

# Reset version files
git revert HEAD~2..HEAD
```

## Best Practices

1. **Always run tests first** - Never skip validation
2. **Use semantic versioning** - Follow conventional commits
3. **Keep changelog updated** - Helps track changes
4. **Test in staging first** - Before production release
5. **Monitor after release** - Watch for issues

## Troubleshooting

**"Working directory not clean"**
- Commit or stash your changes
- Or use `git status` to see what's uncommitted

**"Tests failed"**
- Fix failing tests before releasing
- Release is automatically aborted

**"GitHub MCP not working"**
- Check `.mcp.json` configuration
- Ensure GITHUB_TOKEN is valid
- Verify repo access

**"Slack notification failed"**
- Check Slack bot token
- Ensure bot is in #releases channel
- Verify workspace connection

## See Also

- [Version Bump Command](../../workflow-commands/version-bump/) - Standalone version bumping
- [Changelog Update Command](../../workflow-commands/changelog-update/) - Generate changelogs
- [MCP Integrations](../../mcp-integrations/) - Setup GitHub and Slack
- [Advanced Hooks](../../advanced-hooks/) - More hook examples
