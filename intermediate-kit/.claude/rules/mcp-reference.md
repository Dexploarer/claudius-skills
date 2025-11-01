# Intermediate Kit - MCP Server Reference

> **Model Context Protocol (MCP) Integration Guide**
> External service integrations for production applications

---

## 📋 MCP Overview

**Model Context Protocol (MCP)** enables Claude Code to interact with external services and tools:
- **Version Control:** GitHub, GitLab
- **Databases:** PostgreSQL, MongoDB, MySQL, SQLite
- **Communication:** Slack, Discord
- **Cloud Services:** AWS, GCP, Azure
- **Monitoring:** Sentry, Datadog, New Relic
- **DevOps:** Docker, Kubernetes, Terraform

MCP servers extend Claude Code's capabilities beyond local file operations.

---

## 🚀 Getting Started with MCP

### Installation

MCP servers are configured in `.claude/settings.json`:

```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-name"],
      "env": {
        "API_KEY": "your-api-key"
      }
    }
  }
}
```

### Verification

After adding an MCP server:
```bash
# Restart Claude Code session
# MCP servers auto-load on session start
```

---

## 🔧 Source Control MCP Servers

### GitHub MCP Server

**Purpose:** Interact with GitHub repositories, issues, PRs

**Installation:**
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

**Capabilities:**
- Create/update issues
- Create/merge pull requests
- Review PRs
- Manage labels
- Search repositories
- Trigger workflows

**Example Usage:**
```
You: "Create a GitHub issue for the authentication bug"
Claude: [Uses GitHub MCP]
→ Creates issue with title, description, labels
→ Returns issue URL
```

**Setup Steps:**
1. Get GitHub Personal Access Token: https://github.com/settings/tokens
2. Add token to environment or settings.json
3. Grant permissions: repo, issues, pull_requests

---

### GitLab MCP Server

**Purpose:** Interact with GitLab repositories

**Installation:**
```json
{
  "mcpServers": {
    "gitlab": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gitlab"],
      "env": {
        "GITLAB_TOKEN": "glpat-your_token_here",
        "GITLAB_URL": "https://gitlab.com"
      }
    }
  }
}
```

**Capabilities:**
- Manage merge requests
- Create/update issues
- Trigger pipelines
- Manage labels
- Search projects

---

## 💾 Database MCP Servers

### PostgreSQL MCP Server

**Purpose:** Query and manage PostgreSQL databases

**Installation:**
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:password@localhost:5432/dbname"
      }
    }
  }
}
```

**Capabilities:**
- Execute SELECT queries
- Inspect schema
- View table definitions
- Analyze query performance
- Generate reports

**Example Usage:**
```
You: "Show me all users created in the last 7 days"
Claude: [Uses PostgreSQL MCP]
→ Generates SQL query
→ Executes query
→ Returns results
```

**Security:**
- Use read-only credentials when possible
- Limit access to production databases
- Use connection pooling
- Consider using SSH tunnels

---

### MongoDB MCP Server

**Purpose:** Query and manage MongoDB databases

**Installation:**
```json
{
  "mcpServers": {
    "mongodb": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-mongodb"],
      "env": {
        "MONGODB_URI": "mongodb://localhost:27017/mydb"
      }
    }
  }
}
```

**Capabilities:**
- Execute queries
- Inspect collections
- Analyze indexes
- Aggregate data

---

### MySQL MCP Server

**Purpose:** Query MySQL/MariaDB databases

**Installation:**
```json
{
  "mcpServers": {
    "mysql": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-mysql"],
      "env": {
        "MYSQL_HOST": "localhost",
        "MYSQL_USER": "user",
        "MYSQL_PASSWORD": "password",
        "MYSQL_DATABASE": "dbname"
      }
    }
  }
}
```

---

### SQLite MCP Server

**Purpose:** Query SQLite databases

**Installation:**
```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sqlite", "/path/to/database.db"]
    }
  }
}
```

**Use Cases:**
- Local development databases
- Testing
- Small production apps
- Embedded databases

---

## 💬 Communication MCP Servers

### Slack MCP Server

**Purpose:** Send messages, create channels, interact with Slack

**Installation:**
```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-your-token",
        "SLACK_TEAM_ID": "T1234567890"
      }
    }
  }
}
```

**Capabilities:**
- Send messages to channels
- Create channels
- Invite users
- Upload files
- Send notifications

**Example Usage:**
```
You: "Send a message to #engineering about the deployment"
Claude: [Uses Slack MCP]
→ Sends message to #engineering channel
→ Confirms delivery
```

**Setup:**
1. Create Slack App: https://api.slack.com/apps
2. Add Bot Token Scopes: chat:write, channels:read
3. Install to workspace
4. Copy Bot Token

---

### Discord MCP Server

**Purpose:** Interact with Discord servers

**Installation:**
```json
{
  "mcpServers": {
    "discord": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-discord"],
      "env": {
        "DISCORD_BOT_TOKEN": "your-bot-token"
      }
    }
  }
}
```

**Capabilities:**
- Send messages
- Create channels
- Manage roles
- Read messages

---

## ☁️ Cloud Platform MCP Servers

### AWS MCP Server

**Purpose:** Interact with AWS services

**Installation:**
```json
{
  "mcpServers": {
    "aws": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-aws"],
      "env": {
        "AWS_ACCESS_KEY_ID": "your-access-key",
        "AWS_SECRET_ACCESS_KEY": "your-secret-key",
        "AWS_REGION": "us-east-1"
      }
    }
  }
}
```

**Capabilities:**
- S3 operations
- EC2 management
- Lambda functions
- DynamoDB queries
- CloudWatch logs

**Example Usage:**
```
You: "List all S3 buckets"
Claude: [Uses AWS MCP]
→ Calls S3 ListBuckets API
→ Returns bucket names and creation dates
```

---

### Google Cloud MCP Server

**Purpose:** Interact with GCP services

**Installation:**
```json
{
  "mcpServers": {
    "gcp": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gcp"],
      "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "/path/to/credentials.json"
      }
    }
  }
}
```

---

### Azure MCP Server

**Purpose:** Interact with Azure services

**Installation:**
```json
{
  "mcpServers": {
    "azure": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-azure"],
      "env": {
        "AZURE_SUBSCRIPTION_ID": "your-subscription-id",
        "AZURE_TENANT_ID": "your-tenant-id",
        "AZURE_CLIENT_ID": "your-client-id",
        "AZURE_CLIENT_SECRET": "your-client-secret"
      }
    }
  }
}
```

---

## 📊 Monitoring MCP Servers

### Sentry MCP Server

**Purpose:** Access error tracking and performance monitoring

**Installation:**
```json
{
  "mcpServers": {
    "sentry": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sentry"],
      "env": {
        "SENTRY_AUTH_TOKEN": "your-auth-token",
        "SENTRY_ORG": "your-org",
        "SENTRY_PROJECT": "your-project"
      }
    }
  }
}
```

**Capabilities:**
- View recent errors
- Search issues
- Update issue status
- View error trends

**Example Usage:**
```
You: "Show me critical errors from the last hour"
Claude: [Uses Sentry MCP]
→ Queries Sentry API
→ Filters by severity and time
→ Returns error summaries with stack traces
```

---

### Datadog MCP Server

**Purpose:** Access metrics and logs

**Installation:**
```json
{
  "mcpServers": {
    "datadog": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-datadog"],
      "env": {
        "DD_API_KEY": "your-api-key",
        "DD_APP_KEY": "your-app-key"
      }
    }
  }
}
```

**Capabilities:**
- Query metrics
- View logs
- Create dashboards
- Set up monitors

---

### New Relic MCP Server

**Purpose:** Application performance monitoring

**Installation:**
```json
{
  "mcpServers": {
    "newrelic": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-newrelic"],
      "env": {
        "NEW_RELIC_API_KEY": "your-api-key",
        "NEW_RELIC_ACCOUNT_ID": "your-account-id"
      }
    }
  }
}
```

---

## 🔧 DevOps MCP Servers

### Docker MCP Server

**Purpose:** Manage Docker containers and images

**Installation:**
```json
{
  "mcpServers": {
    "docker": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-docker"]
    }
  }
}
```

**Capabilities:**
- List containers/images
- Start/stop containers
- Build images
- View logs
- Inspect resources

**Example Usage:**
```
You: "Show me all running containers"
Claude: [Uses Docker MCP]
→ Lists running containers with status
→ Shows resource usage
```

---

### Kubernetes MCP Server

**Purpose:** Manage Kubernetes clusters

**Installation:**
```json
{
  "mcpServers": {
    "kubernetes": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-kubernetes"],
      "env": {
        "KUBECONFIG": "/path/to/kubeconfig"
      }
    }
  }
}
```

**Capabilities:**
- List pods/deployments/services
- View logs
- Scale deployments
- Get resource status
- Apply configurations

---

### Terraform MCP Server

**Purpose:** Manage infrastructure as code

**Installation:**
```json
{
  "mcpServers": {
    "terraform": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-terraform"]
    }
  }
}
```

**Capabilities:**
- Plan infrastructure changes
- View state
- List resources
- Validate configurations

---

## 🎯 MCP Best Practices

### Security

1. **Use Environment Variables**
   ```json
   {
     "env": {
       "API_KEY": "${GITHUB_TOKEN}"  // Reference .env
     }
   }
   ```

2. **Limit Permissions**
   - Use read-only tokens when possible
   - Grant minimum required scopes
   - Rotate tokens regularly

3. **Protect Credentials**
   - Never commit tokens to git
   - Use secret management (Vault, AWS Secrets Manager)
   - Add .env to .gitignore

### Performance

1. **Cache Results**
   - MCP servers cache responses
   - Reduce API calls
   - Faster responses

2. **Limit Scope**
   - Only enable needed MCP servers
   - Reduces startup time
   - Lower resource usage

### Reliability

1. **Error Handling**
   - MCP servers handle failures gracefully
   - Provide fallback options
   - Log errors for debugging

2. **Monitoring**
   - Track MCP server status
   - Monitor API rate limits
   - Set up alerts

---

## 🔗 Recommended MCP Combinations

### Full-Stack Web Development
```json
{
  "mcpServers": {
    "github": {...},      // Version control
    "postgres": {...},    // Database
    "sentry": {...},      // Error tracking
    "slack": {...}        // Team communication
  }
}
```

### DevOps/Infrastructure
```json
{
  "mcpServers": {
    "aws": {...},         // Cloud platform
    "docker": {...},      // Containers
    "kubernetes": {...},  // Orchestration
    "datadog": {...}      // Monitoring
  }
}
```

### Data Analysis
```json
{
  "mcpServers": {
    "postgres": {...},    // SQL database
    "mongodb": {...},     // NoSQL database
    "aws": {...}          // S3 for data storage
  }
}
```

---

## 📚 MCP Resources

### Official Documentation
- MCP Specification: https://modelcontextprotocol.io/
- Server Registry: https://github.com/modelcontextprotocol/servers

### Creating Custom MCP Servers
- SDK: `@modelcontextprotocol/sdk`
- Template: https://github.com/modelcontextprotocol/server-template
- Documentation: https://modelcontextprotocol.io/docs

### Community Servers
- GitHub: Search "mcp-server-*"
- npm: Search "@modelcontextprotocol/"

---

## 🔗 Related References

**Settings File:**
- Configuration: `@intermediate-kit/.claude/settings.json`

**Other References:**
- Skills: `@intermediate-kit/.claude/rules/skills-reference.md`
- Commands: `@intermediate-kit/.claude/rules/commands-reference.md`
- Agents: `@intermediate-kit/.claude/rules/agents-reference.md`
- Hooks: `@intermediate-kit/.claude/rules/hooks-reference.md`

**Workflow Rules:**
- Deployment: `@intermediate-kit/.claude/rules/workflows/deployment.md`
- Security: `@intermediate-kit/.claude/rules/workflows/security.md`
- API Development: `@intermediate-kit/.claude/rules/workflows/api-development.md`

---

**Last Updated:** 2025-11-01
**Available MCP Servers:** 20+
**Level:** Intermediate (Production-Ready)
