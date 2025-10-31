# GitHub Workflows MCP Integration

Example MCP server configuration for GitHub Actions integration.

## What This Provides

Access to GitHub workflows and actions through MCP:
- List workflows
- Trigger workflow runs
- Check workflow status
- View run logs
- Download artifacts

## Setup

### 1. Install MCP Server

```bash
# Using the github-actions MCP server
npm install -g @modelcontextprotocol/server-github
```

### 2. Configure in Claude

Add to your `.claude/mcp.json`:

```json
{
  "mcpServers": {
    "github-actions": {
      "command": "mcp-server-github",
      "args": [],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}",
        "GITHUB_REPO": "owner/repo"
      }
    }
  }
}
```

### 3. Set Environment Variable

```bash
export GITHUB_TOKEN="ghp_your_token_here"
```

## Usage Examples

### List Workflows

```
You: "Show me all GitHub workflows"

Claude: [Uses MCP to list workflows]

Workflows in owner/repo:
1. CI/CD Pipeline (.github/workflows/ci.yml)
   - Status: Active
   - Last run: 2 hours ago (success)

2. Deploy to Production (.github/workflows/deploy.yml)
   - Status: Active
   - Last run: 1 day ago (success)

3. Run Tests (.github/workflows/test.yml)
   - Status: Active
   - Last run: 30 minutes ago (in progress)
```

### Trigger Workflow

```
You: "Run the deployment workflow"

Claude: [Uses MCP to trigger workflow]

Triggering deployment workflow...

✅ Workflow run started:
   Run ID: 1234567890
   Status: queued
   URL: https://github.com/owner/repo/actions/runs/1234567890

You can check status with: "What's the status of run 1234567890?"
```

### Check Status

```
You: "What's the status of the latest CI run?"

Claude: [Uses MCP to check status]

Latest CI/CD Pipeline run:
   Run: #456
   Status: ✅ Success
   Duration: 3m 42s
   Commit: feat: add user auth (abc123)
   Started: 2 hours ago

   Jobs:
   ✅ Lint (45s)
   ✅ Test (2m 15s)
   ✅ Build (1m 30s)
```

## Integration with Commands

Create command that uses GitHub MCP:

`.claude/commands/deploy-staging.md`:
```markdown
Deploy current branch to staging environment.

## Instructions

1. Check current branch
2. Use GitHub MCP to:
   - Trigger staging deployment workflow
   - Pass branch name as input
3. Monitor workflow progress
4. Report when complete

Use these MCP tools:
- gh-workflows-list
- gh-workflow-trigger
- gh-run-status
```

## MCP Tools Available

Based on the GitHub MCP server:

```typescript
// List workflows
gh-workflows-list(): Workflow[]

// Get workflow details
gh-workflow-get(workflow_id): WorkflowDetails

// Trigger workflow
gh-workflow-trigger(
  workflow_id,
  ref,      // branch or tag
  inputs?   // workflow inputs
): RunId

// Get run status
gh-run-status(run_id): RunStatus

// Get run logs
gh-run-logs(run_id): string

// List artifacts
gh-run-artifacts(run_id): Artifact[]

// Download artifact
gh-artifact-download(artifact_id): Buffer
```

## Example Workflow

Complete deployment workflow:

```
You: "Deploy feature-x to staging"

Claude:
1. Checking current state...
   Branch: feature-x
   Last commit: feat: add new feature (def456)

2. Triggering staging deployment...
   [Uses gh-workflow-trigger]
   ✅ Workflow started (Run #789)

3. Monitoring progress...
   [Uses gh-run-status]
   ⏳ Build: in progress
   ⏳ Test: queued
   ⏳ Deploy: queued

   ... 2 minutes later ...

   ✅ Build: success (1m 30s)
   ✅ Test: success (45s)
   ⏳ Deploy: in progress

   ... 1 minute later ...

   ✅ Deploy: success (50s)

4. Deployment complete!
   Environment: staging
   URL: https://staging.example.com
   Version: feature-x@def456

   Next steps:
   - Test on staging: https://staging.example.com
   - Create PR: /pr-creator
   - Deploy to prod: "deploy to production"
```

## Security Notes

- Store GITHUB_TOKEN securely
- Use tokens with minimum required permissions
- Consider using GitHub Apps for better security
- Don't commit tokens to repository
- Rotate tokens regularly

## See Also

- MCP Server Documentation
- GitHub Actions API
- Authentication best practices
