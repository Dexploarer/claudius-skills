# GitHub Server - MCP Example

Connect Claude Code to GitHub to manage issues, pull requests, and repositories.

## What It Does

The GitHub server lets Claude:
- **List issues** in your repositories
- **Create issues** from bugs you find
- **Manage pull requests** - list, review, comment
- **Search repositories** and code
- **Read repository information**
- **List branches, commits, and more**

## Prerequisites

Before starting, you need:
- A GitHub account
- A Personal Access Token (PAT) from GitHub

## Getting Your GitHub Token

### Step 1: Go to GitHub Settings

1. Go to [github.com](https://github.com)
2. Click your profile picture (top right)
3. Click **Settings**
4. Scroll down to **Developer settings** (bottom left)
5. Click **Personal access tokens** → **Tokens (classic)**

### Step 2: Generate New Token

1. Click **Generate new token** → **Generate new token (classic)**
2. Give it a name: "Claude Code MCP"
3. Select scopes (permissions):
   - ✅ `repo` (Full control of private repositories)
   - ✅ `read:org` (Read org and team membership)
   - ✅ `user` (Read user profile data)
4. Set expiration (recommend 90 days for security)
5. Click **Generate token**

### Step 3: Copy Token

**⚠️ Important:** Copy the token immediately! You can't see it again.

Save it somewhere temporarily, you'll need it in a moment.

## Installation

### Step 1: Create `.mcp.json`

In your project root:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your-token-here"
      }
    }
  }
}
```

**Replace `your-token-here` with your actual token.**

### Step 2: Secure the File

**CRITICAL:** Don't commit your token to git!

```bash
# Add .mcp.json to .gitignore
echo ".mcp.json" >> .gitignore

# Verify it's ignored
git status  # Should not show .mcp.json
```

### Step 3: Create Template for Team

```bash
# Create template without real token
cp .mcp.json .mcp.json.template

# Edit .mcp.json.template
# Replace token with: "YOUR_GITHUB_TOKEN_HERE"

# Commit the template (safe)
git add .mcp.json.template
```

### Step 4: Restart Claude Code

```bash
exit
claude
```

### Step 5: Test It!

```bash
"List my GitHub repositories"
"Show me open issues in my repo"
```

## How to Use

### Listing Repositories

```bash
"List all my GitHub repositories"
"Show me my most recently updated repos"
"Which of my repos have open issues?"
```

### Managing Issues

#### List Issues
```bash
"List open issues in username/repo-name"
"Show me all my assigned issues"
"What issues have the 'bug' label?"
```

#### Create Issues
```bash
"Create an issue in username/repo-name"
"Add a GitHub issue: Title: Fix login bug, Body: Login fails with empty email"
```

#### Update Issues
```bash
"Close issue #123 in username/repo-name"
"Add label 'bug' to issue #123"
"Comment on issue #123: Working on this now"
```

### Managing Pull Requests

```bash
"List open pull requests in username/repo-name"
"Show me PRs waiting for my review"
"Get details of PR #45"
"Comment on PR #45: Looks good!"
```

### Searching

```bash
"Search for 'authentication' in username/repo-name"
"Find all files with 'TODO' in username/repo-name"
"Search GitHub for React components"
```

### Repository Info

```bash
"Get info about username/repo-name"
"Show me the branches in username/repo-name"
"List recent commits in username/repo-name"
```

## Example Use Cases

### Use Case 1: Bug Tracking

**Scenario:** You find bugs while coding and want to track them.

```bash
# While coding
You: "I found a bug - the login form doesn't validate empty emails"

Claude: "I can create a GitHub issue for that. What repository?"

You: "username/my-app"

Claude: "I'll create an issue..."

# Result: Issue #42 created with title and description
```

### Use Case 2: Code Review Workflow

**Scenario:** Review PRs without leaving your terminal.

```bash
You: "List open PRs in username/my-app"

Claude: "Found 3 open PRs:
#15: Add dark mode
#16: Fix navigation bug
#17: Update dependencies"

You: "Show me details of PR #15"

Claude: "PR #15: Add dark mode
- Changes: 8 files
- +245 -32 lines
- Author: teammate
- [details...]"

You: "Comment on PR #15: Great work! Just some minor style suggestions..."

Claude: "Comment added to PR #15"
```

### Use Case 3: Project Planning

**Scenario:** Plan work by reviewing existing issues.

```bash
You: "Show me all open issues with label 'enhancement' in username/my-app"

Claude: "Found 5 enhancement requests: [list]"

You: "Create a summary document of these enhancements"

Claude: "Here's a summary: [document]"

You: "Remember this list for sprint planning"  # Using memory server
```

### Use Case 4: Cross-Repository Work

**Scenario:** Working with multiple related repos.

```bash
You: "List my repositories"

Claude: "Your repositories:
- username/frontend
- username/backend
- username/mobile
- ..."

You: "Show open issues across all three"

Claude: "Open issues:
Frontend: 3 issues
Backend: 5 issues
Mobile: 2 issues
[details...]"
```

## Best Practices

### Security

✅ **Do:**
- Create token with minimum permissions needed
- Set token expiration (90 days recommended)
- Never commit `.mcp.json` with real token
- Revoke token when no longer needed
- Use different tokens for different purposes
- Check token permissions regularly

❌ **Don't:**
- Use token with full admin access
- Share token with anyone
- Commit token to git
- Use same token for everything
- Leave token active indefinitely
- Post token in issues or chats

### Token Management

```bash
# ✅ Good: Use environment variable
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}

# Then set in your shell
export GITHUB_TOKEN="your-token"
```

### Repository Names

```bash
# ✅ Always use full name
"username/repo-name"

# ❌ Don't use just
"repo-name"  # Ambiguous if multiple users have same repo name
```

## Common Commands

### Issue Management

```bash
# List issues
"List issues in username/repo"
"Show open issues"
"Show closed issues"
"Issues assigned to me"
"Issues with label 'bug'"

# Create issues
"Create issue: [title] - [description]"
"Add bug report: [details]"

# Update issues
"Close issue #X"
"Add comment to issue #X"
"Add label 'bug' to issue #X"
```

### Pull Request Management

```bash
# List PRs
"List pull requests"
"Show open PRs"
"PRs waiting for review"

# Review PRs
"Show PR #X"
"Get PR #X details"
"Comment on PR #X: [comment]"
```

### Repository Operations

```bash
# Info
"Show repo info"
"List branches"
"Recent commits"
"Contributors"

# Search
"Search for '[term]' in repo"
"Find files matching '[pattern]'"
```

## Troubleshooting

### Issue: "Authentication failed"

**Causes:**
- Token is incorrect
- Token expired
- Token doesn't have required permissions

**Solutions:**
```bash
# 1. Check token in .mcp.json
cat .mcp.json | grep GITHUB_TOKEN

# 2. Verify token on GitHub
# Go to Settings → Developer settings → Personal access tokens
# Check token exists and has correct permissions

# 3. Generate new token if needed
# Follow "Getting Your GitHub Token" steps above
```

### Issue: "Repository not found"

**Causes:**
- Wrong repository name
- Token doesn't have access to that repo
- Repository is private and token lacks permissions

**Solutions:**
```bash
# 1. Check repository name format
# Should be: "username/repo-name"
# Not just: "repo-name"

# 2. Verify you have access
# Go to github.com/username/repo-name in browser

# 3. Check token permissions
# Token needs 'repo' scope for private repos
```

### Issue: "Rate limit exceeded"

**Cause:** GitHub has rate limits on API usage.

**Solution:**
```bash
# Wait a bit before making more requests

# Check rate limit status
"Check my GitHub rate limit"

# For heavy use, consider:
# - Caching frequently accessed data
# - Reducing number of requests
# - Using GraphQL API (not in basic server)
```

### Issue: "Server not starting"

**Solutions:**
```bash
# 1. Check .mcp.json syntax
cat .mcp.json | jq .

# 2. Test server directly
npx -y @modelcontextprotocol/server-github --help

# 3. Check npx is installed
which npx

# 4. Try with debug mode
claude --debug
```

## Advanced Usage

### Multiple Tokens

Different tokens for different purposes:

```json
{
  "mcpServers": {
    "github-work": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "work-token-here"
      }
    },
    "github-personal": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "personal-token-here"
      }
    }
  }
}
```

### Environment Variables

More secure approach:

```bash
# In your ~/.bashrc or ~/.zshrc
export GITHUB_TOKEN_WORK="your-work-token"
export GITHUB_TOKEN_PERSONAL="your-personal-token"
```

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN_WORK}"
      }
    }
  }
}
```

### Combining with Other Servers

GitHub + Memory + Filesystem = powerful workflow:

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/me/docs"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your-token"
      }
    }
  }
}
```

Use together:
```bash
"List GitHub issues, remember the top 3 priorities, and create a plan in ~/docs/sprint-plan.md"
```

## Real-World Workflows

### Workflow 1: Daily Standup Prep

```bash
"Show me:
1. Issues assigned to me
2. PRs I need to review
3. Recent activity on my PRs"

# Use this info for standup meeting
```

### Workflow 2: Bug Report Flow

```bash
# 1. Find bug while coding
You: "The login form has a validation bug"

# 2. Create issue immediately
You: "Create a GitHub issue in username/app: Fix login validation"

# 3. Remember for later
You: "Remember: Created issue #47 for login validation"

# 4. Continue working
# ...

# 5. Later, when fixing
You: "What was that issue I created?"
You: "Show me issue #47"
You: "Close issue #47 after I fix it"
```

### Workflow 3: Code Review Assistant

```bash
# Morning routine
You: "List all open PRs in username/app"

# For each PR
You: "Show me details of PR #15"
You: "Read the changed files"  # Using filesystem or Git
You: "Review this code for issues"  # Using quick-reviewer subagent
You: "Comment on PR #15 with my feedback"
```

### Workflow 4: Sprint Planning

```bash
# Gather data
You: "Show all open issues with label 'sprint-next'"
You: "Group these by priority"
You: "Estimate effort for each"
You: "Create sprint plan document"  # Using filesystem

# Update GitHub
You: "Add label 'in-progress' to issues #1, #2, #3"
You: "Create milestone 'Sprint 5' with these issues"
```

## Tips

1. **Use specific repository names** - Always include username/repo
2. **Be descriptive in issues** - More detail = better tracking
3. **Use labels effectively** - Helps organize and filter
4. **Review before creating** - Claude can draft issues for your review
5. **Combine with other tools** - Use with memory, filesystem, etc.

## FAQ

**Q: Does this work with GitHub Enterprise?**
A: Yes, but you need to configure the API endpoint. Check server documentation.

**Q: Can I create pull requests?**
A: The basic server focuses on reading. For creating PRs, check advanced features or use `gh` CLI.

**Q: How many repositories can I access?**
A: All repositories your token has access to.

**Q: Can I access private repositories?**
A: Yes, if your token has the 'repo' scope.

**Q: What about GitHub Actions?**
A: Not supported in basic server. Use GitHub CLI or API directly.

**Q: Can team members share one token?**
A: No, each person should have their own token for security and attribution.

**Q: Does this affect my GitHub usage limits?**
A: Yes, API calls count toward your rate limit. Monitor usage with `"Check rate limit"`.

## Security Checklist

Before using GitHub server:

- [ ] Token has minimum necessary permissions
- [ ] Token has expiration date set
- [ ] `.mcp.json` is in `.gitignore`
- [ ] `.mcp.json.template` created for team (without token)
- [ ] Team knows not to commit real tokens
- [ ] You know how to revoke token if needed
- [ ] You're using different tokens for work/personal

## Next Steps

1. ✅ **Generate GitHub token** - Follow steps above
2. ✅ **Configure `.mcp.json`** - Add your token
3. ✅ **Test with your repos** - List issues, create one
4. ✅ **Build a workflow** - Integrate into daily routine
5. ✅ **Try combining** - Use with memory and filesystem servers

## Related Examples

- **memory-server** - Remember GitHub workflows
- **filesystem-server** - Save GitHub data locally
- **sqlite-server** - Store issue data in database

---

**Important:** Always keep your GitHub token secure. Never commit it to version control! 🔒
