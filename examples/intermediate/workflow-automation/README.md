# Workflow Automation Examples

Learn how to combine Claude Code's Five Pillars to create powerful automated workflows.

## What Are Workflow Automations?

Workflow automations combine skills, commands, hooks, subagents, and MCP integrations to create seamless, end-to-end development processes.

## Available Examples

### Release Workflow
**Combines:** Commands + Hooks + MCP
- Version bumping
- Changelog generation
- Git tagging
- GitHub release creation
- Slack notification

**Use Case:** Automate entire release process with one command

### Code Review Workflow
**Combines:** Subagents + Hooks + MCP
- Auto-review on PR creation
- Security scanning
- Test enforcement
- GitHub PR comments
- Team notifications

**Use Case:** Automated code quality checks

### Deployment Pipeline
**Combines:** Commands + Hooks + Skills
- Pre-deployment checks
- Build and test
- Environment validation
- Deployment execution
- Health monitoring

**Use Case:** Safe, automated deployments

### Documentation Sync
**Combines:** Skills + MCP + Hooks
- Auto-generate API docs
- Update README
- Sync to wiki/docs site
- Notify team of changes

**Use Case:** Keep docs always up-to-date

## How Workflows Work

### Example: Release Workflow

**1. Slash Command** (`/release`)
```markdown
Perform a production release.

Steps:
1. Run tests (must pass)
2. Call version-bump-agent to determine version
3. Update version in files
4. Generate changelog
5. Create git tag
6. Push to remote
7. Create GitHub release (via MCP)
8. Notify team on Slack (via MCP)
```

**2. Pre-Commit Hook** (in settings.json)
```json
{
  "pattern": "Bash.*git push.*--tags",
  "command": "echo 'Creating release...' && npm test",
  "description": "Ensure tests pass before pushing release tags"
}
```

**3. MCP Integration** (GitHub + Slack)
```json
{
  "github": { "disabled": false },
  "slack": { "disabled": false }
}
```

**4. Subagent** (version-bump-agent.md)
```markdown
---
name: version-bump-agent
description: Analyzes commits to determine semantic version bump
---
Review commits since last tag and suggest version bump (major/minor/patch)
```

## Creating Your Own Workflows

### Step 1: Identify the Process
Map out your manual process:
- What steps do you take?
- What can be automated?
- What needs human approval?

### Step 2: Choose Your Tools
- **Commands**: Manual triggers
- **Skills**: Automatic detection
- **Hooks**: Safety checks and enforcement
- **Subagents**: Complex analysis
- **MCP**: External integrations

### Step 3: Build Incrementally
1. Start with a single command
2. Add hooks for safety
3. Integrate MCP if needed
4. Add subagents for complex logic
5. Test thoroughly

### Step 4: Document and Share
- Write clear documentation
- Include examples
- Share with team
- Gather feedback

## Best Practices

✅ **Do:**
- Start simple and iterate
- Add safety checks (hooks)
- Document each step
- Test error scenarios
- Provide clear feedback

❌ **Don't:**
- Automate without safeguards
- Skip testing
- Make workflows too complex
- Forget error handling

## Example Workflow: Feature Branch

Here's a complete example workflow for feature development:

**`/feature-start [name]`** - Start new feature
```markdown
1. Create feature branch
2. Setup tracking
3. Create initial commit
4. Open draft PR (via GitHub MCP)
5. Notify team on Slack
```

**`/feature-test`** - Test feature
```markdown
1. Run unit tests
2. Run integration tests
3. Check coverage
4. Lint code
5. Report results
```

**`/feature-finish`** - Complete feature
```markdown
1. Run /feature-test
2. Call code-reviewer subagent
3. Update PR description
4. Mark PR ready for review
5. Request reviews (via GitHub MCP)
```

**Hook: Pre-Push**
```json
{
  "pattern": "Bash.*git push",
  "command": "npm test",
  "description": "Tests must pass before pushing"
}
```

## See Also

- [Intermediate Commands](../workflow-commands/) - Pre-built commands
- [Domain Subagents](../domain-subagents/) - Specialized agents
- [MCP Integrations](../mcp-integrations/) - External services
- [Advanced Hooks](../advanced-hooks/) - Complex automation
