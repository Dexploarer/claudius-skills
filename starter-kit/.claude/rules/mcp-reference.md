# Starter Kit - MCP Server Reference

> **Model Context Protocol (MCP) Introduction for Beginners**
> Extend Claude Code with external services

---

## 📋 What is MCP?

**Model Context Protocol (MCP)** allows Claude Code to connect to external services:
- **GitHub:** Create issues, manage PRs
- **Databases:** Query PostgreSQL, MySQL, SQLite
- **Communication:** Send Slack messages
- **Cloud Services:** Interact with AWS, GCP

Think of MCP servers as "plugins" that give Claude Code superpowers! 🚀

---

## 🎯 Beginner-Friendly MCP Servers

### 1. GitHub MCP Server

**What It Does:** Lets Claude Code interact with GitHub

**Use Cases:**
- Create issues automatically
- Manage pull requests
- Search repositories
- View issue status

**Setup:**
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your_token_here"
      }
    }
  }
}
```

**Getting a GitHub Token:**
1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Select scopes: `repo`, `issues`
4. Copy the token

**Example:**
```
You: "Create a GitHub issue for fixing the login bug"
Claude: [Uses GitHub MCP]
→ Creates issue with title "Fix login bug"
→ Returns issue URL
```

---

### 2. SQLite MCP Server

**What It Does:** Query local SQLite databases

**Use Cases:**
- View database tables
- Run simple queries
- Analyze data
- Generate reports

**Setup:**
```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sqlite", "./database.db"]
    }
  }
}
```

**Example:**
```
You: "Show me all users in the database"
Claude: [Uses SQLite MCP]
→ Runs: SELECT * FROM users
→ Returns results
```

**Why SQLite?**
- Perfect for beginners
- No server setup required
- File-based database
- Great for learning SQL

---

### 3. Slack MCP Server

**What It Does:** Send messages to Slack

**Use Cases:**
- Send deployment notifications
- Alert team about errors
- Share updates
- Automated reminders

**Setup:**
```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-your-token",
        "SLACK_TEAM_ID": "T1234567"
      }
    }
  }
}
```

**Getting a Slack Token:**
1. Go to https://api.slack.com/apps
2. Create new app
3. Add "Bot Token Scopes": `chat:write`
4. Install to workspace
5. Copy Bot Token

**Example:**
```
You: "Send a message to #general saying tests passed"
Claude: [Uses Slack MCP]
→ Sends message to #general channel
→ Confirms delivery
```

---

## 🚀 How to Add MCP Servers

### Step 1: Edit settings.json

Your settings file is at: `starter-kit/.claude/settings.json`

Add the `mcpServers` section:

```json
{
  "hooks": {
    // existing hooks...
  },
  "mcpServers": {
    // Add MCP servers here
  }
}
```

### Step 2: Add a Server

Example - Adding GitHub:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### Step 3: Restart Claude Code

Exit and restart your Claude Code session. The MCP server will load automatically.

### Step 4: Test It

```
You: "List my GitHub repositories"
Claude: [Uses GitHub MCP if configured]
→ Returns list of repositories
```

---

## 🛡️ Security Best Practices

### 1. Never Commit Tokens

**Bad:**
```json
{
  "env": {
    "GITHUB_TOKEN": "ghp_abc123xyz"  // ❌ Don't do this!
  }
}
```

**Good:**
```json
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"  // ✅ Reference environment variable
  }
}
```

Then create `.env` file:
```
GITHUB_TOKEN=ghp_abc123xyz
```

And add to `.gitignore`:
```
.env
.env.local
```

### 2. Use Read-Only Tokens

When possible, create tokens with minimal permissions:
- GitHub: Read-only scope for viewing issues
- Database: Read-only user for queries

### 3. Rotate Tokens Regularly

Change tokens every 3-6 months for security.

---

## 💡 Common Use Cases

### Use Case 1: Bug Tracking

**Scenario:** Automatically create GitHub issues

```
You: "I found a bug in the login page. Create a GitHub issue."
Claude:
→ Uses GitHub MCP
→ Creates issue with details
→ Adds "bug" label
→ Returns issue URL
```

### Use Case 2: Data Analysis

**Scenario:** Query local database

```
You: "How many users signed up this week?"
Claude:
→ Uses SQLite MCP
→ Runs query with date filter
→ Returns count and details
```

### Use Case 3: Team Notifications

**Scenario:** Alert team on Slack

```
You: "Notify #dev-team that deployment is complete"
Claude:
→ Uses Slack MCP
→ Sends message to #dev-team
→ Confirms delivery
```

---

## 🔍 Available MCP Servers

### Source Control
- **GitHub** - Issue tracking, PRs
- **GitLab** - Merge requests, pipelines

### Databases
- **SQLite** - Local file database (beginner-friendly)
- **PostgreSQL** - Production database
- **MySQL** - Popular database

### Communication
- **Slack** - Team messaging
- **Discord** - Community chat

### Cloud
- **AWS** - Amazon Web Services
- **GCP** - Google Cloud Platform

---

## 📚 Learning Path

### Week 1: Start with GitHub MCP
1. Set up GitHub token
2. Create an issue via Claude
3. View repository info
4. List issues

### Week 2: Try SQLite MCP
1. Create a simple database
2. Query data via Claude
3. Generate reports
4. Analyze data

### Week 3: Add Slack MCP
1. Set up Slack bot
2. Send test message
3. Create notification workflows
4. Automate team updates

---

## 🔧 Troubleshooting

### MCP Server Not Loading

**Check:**
1. ✅ Valid JSON in settings.json
2. ✅ Correct command and args
3. ✅ Environment variables set
4. ✅ Restarted Claude Code

### Authentication Errors

**Check:**
1. ✅ Token is valid
2. ✅ Token has correct permissions
3. ✅ Token not expired
4. ✅ Environment variable loaded

### Can't Find MCP Tools

**Check:**
1. ✅ Node.js installed (v18+)
2. ✅ npx available
3. ✅ Internet connection
4. ✅ Server package exists

---

## 🎓 Next Steps

### When You're Comfortable:
1. Try multiple MCP servers together
2. Create custom workflows
3. Automate repetitive tasks
4. Explore advanced MCP servers

### Graduate to Intermediate:
When you're ready for:
- Production databases (PostgreSQL, MongoDB)
- Cloud platforms (AWS, GCP, Azure)
- Monitoring (Sentry, Datadog)
- DevOps (Docker, Kubernetes)

See: `@intermediate-kit/.claude/rules/mcp-reference.md`

---

## 🔗 Related References

**Settings File:**
- Your config: `@starter-kit/.claude/settings.json`

**Other References:**
- Skills: `@starter-kit/.claude/rules/skills-reference.md`
- Commands: `@starter-kit/.claude/rules/commands-reference.md`
- Agents: `@starter-kit/.claude/rules/agents-reference.md`
- Hooks: `@starter-kit/.claude/rules/hooks-reference.md`

**Guides:**
- Getting Started: `@resources/guides/getting-started.md`
- Security Guide: `@resources/guides/security.md`

---

## 📖 Helpful Resources

### Official MCP Documentation
- Specification: https://modelcontextprotocol.io/
- Server List: https://github.com/modelcontextprotocol/servers

### Tutorials
- GitHub MCP Setup: (See official docs)
- Database Integration: (See official docs)
- Slack Bot Creation: https://api.slack.com/start

---

## 🎓 Next Level: Code Execution Pattern

Once you master basic MCP, learn about Anthropic's advanced **code execution pattern**:

**Benefits:**
- 🚀 98.7% token savings
- ⚡ 75% latency reduction
- 🔒 Better privacy (PII tokenization)
- 📦 Reusable skills

**When to Use:**
- Large datasets (1,000+ items)
- Multi-step workflows
- Privacy-sensitive data
- High-frequency MCP operations

**Resources:**
- **Example:** `@examples/advanced/mcp-code-execution/README.md`
- **Skill:** `@advanced-kit/.claude/skills/mcp-code-execution.md`
- **Templates:** `@templates/mcp-code-execution/`
- **Blog:** https://www.anthropic.com/engineering/code-execution-with-mcp

**Pattern Comparison:**

```typescript
// Traditional (this guide) - Simple, good for learning
const issues = await callTool('github_list_issues', { repo: 'react' });

// Code execution (advanced) - 98.7% token savings
import { listIssues } from './servers/github';
const issues = await listIssues({ repo: 'facebook/react' });
```

---

**Last Updated:** 2025-11-05
**Recommended for Beginners:** GitHub, SQLite, Slack
**Level:** Beginner (Starter Kit)
**Advanced Pattern:** Code execution (see resources above)
