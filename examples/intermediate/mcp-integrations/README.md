# MCP Integrations - Intermediate Examples

Connect Claude Code to your entire development ecosystem.

## What Are MCP Integrations?

Model Context Protocol (MCP) servers allow Claude Code to interact with external services like GitHub, databases, Slack, and cloud providers.

## Available Examples

### GitHub Workflows
- **File**: `github-workflows/README.md`
- **Purpose**: Integrate GitHub Actions for CI/CD
- **Features**:
  - List workflows
  - Trigger runs
  - Check status
  - Download artifacts

### Database Connections
- **File**: `database-connections/README.md`
- **Purpose**: Connect to databases for queries
- **Features**:
  - Run SQL queries
  - Analyze schema
  - Optimize queries
  - Export data

## How to Setup MCP

### 1. Copy Template
```bash
cp intermediate-kit/.mcp.json.template .mcp.json
```

### 2. Configure Servers

Edit `.mcp.json`:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      },
      "disabled": false
    }
  }
}
```

### 3. Add to .gitignore
```bash
echo ".mcp.json" >> .gitignore
```

### 4. Use in Claude Code
```
"list GitHub workflows"
"check status of latest deployment"
"query database for recent users"
```

## Available MCP Servers

### Source Control
- **GitHub**: Issues, PRs, repos, workflows
- **GitLab**: Projects, merge requests, pipelines

### Databases
- **PostgreSQL**: SQL queries, schema analysis
- **MongoDB**: Document queries, aggregations
- **MySQL**: Relational data access

### Communication
- **Slack**: Post messages, read channels
- **Discord**: Server management, messaging

### Cloud Platforms
- **AWS**: Resource management, deployment
- **GCP**: Cloud resources
- **Azure**: Azure resources

### Monitoring
- **Sentry**: Error tracking
- **Datadog**: Metrics and monitoring
- **New Relic**: Performance monitoring

### DevOps
- **Docker**: Container management
- **Kubernetes**: Cluster operations
- **Terraform**: Infrastructure changes

## Security Best Practices

### 1. Use Environment Variables
```json
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

Then set in your shell:
```bash
export GITHUB_TOKEN="ghp_..."
```

### 2. Use Read-Only Tokens
When possible, create tokens with minimum required permissions.

### 3. Rotate Credentials
Regularly rotate API tokens and access keys.

### 4. Never Commit Secrets
```bash
# Always in .gitignore
echo ".mcp.json" >> .gitignore
```

### 5. Audit MCP Servers
Review MCP server code before using, especially from third parties.

## Creating MCP Integrations

### Basic Configuration
```json
{
  "mcpServers": {
    "my-service": {
      "command": "npx",
      "args": ["-y", "mcp-server-myservice"],
      "env": {
        "API_KEY": "${MY_SERVICE_API_KEY}"
      },
      "disabled": false,
      "description": "Integration with My Service"
    }
  }
}
```

### Custom MCP Server
```javascript
// server.js
const { MCPServer } = require('@modelcontextprotocol/sdk');

const server = new MCPServer({
  name: 'my-service',
  version: '1.0.0',
});

// Register tools
server.tool('get-data', async (params) => {
  // Fetch data from your service
  return { data: ... };
});

server.start();
```

## Common Integration Patterns

### CI/CD Integration
```json
{
  "mcpServers": {
    "github": { ... },
    "jenkins": { ... },
    "vercel": { ... }
  }
}
```

Usage:
```
"trigger GitHub workflow for deployment"
"check Jenkins build status"
"deploy to Vercel production"
```

### Data Access
```json
{
  "mcpServers": {
    "postgresql": { ... },
    "redis": { ... },
    "elasticsearch": { ... }
  }
}
```

Usage:
```
"query users from last 7 days"
"check Redis cache hit rate"
"search logs in Elasticsearch"
```

### Monitoring & Alerts
```json
{
  "mcpServers": {
    "sentry": { ... },
    "datadog": { ... },
    "pagerduty": { ... }
  }
}
```

Usage:
```
"check recent errors in Sentry"
"query Datadog metrics"
"create PagerDuty incident"
```

## Troubleshooting

### MCP Server Not Working

1. **Check Configuration**:
   ```bash
   cat .mcp.json | jq
   ```

2. **Verify Credentials**:
   ```bash
   echo $GITHUB_TOKEN
   ```

3. **Test Server**:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

4. **Enable Debug Mode**:
   ```bash
   claude --debug
   ```

### Common Issues

| Issue | Solution |
|-------|----------|
| Server not found | Check `disabled: false` |
| Auth failed | Verify credentials |
| Permission denied | Check token permissions |
| Timeout | Increase timeout in config |
| Package not found | Install MCP server package |

## Advanced Usage

### Multiple Environments
```json
{
  "mcpServers": {
    "github-prod": {
      "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN_PROD}" }
    },
    "github-staging": {
      "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN_STAGING}" }
    }
  }
}
```

### Conditional Enablement
```bash
# Enable only in production
if [ "$ENV" = "production" ]; then
  jq '.mcpServers.aws.disabled = false' .mcp.json > tmp.json
  mv tmp.json .mcp.json
fi
```

## See Also

- [MCP Documentation](https://modelcontextprotocol.io/)
- [Intermediate Kit](../../../intermediate-kit/)
- [Security Guide](../../../resources/guides/security.md)
- [MCP Server Registry](https://github.com/modelcontextprotocol/servers)
