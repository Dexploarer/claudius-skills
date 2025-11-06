# MCP Basics - Model Context Protocol Examples for Beginners

Welcome to MCP (Model Context Protocol) basics! This section teaches you how to connect Claude Code to external services like GitHub, databases, Slack, and more.

## What is MCP?

**MCP (Model Context Protocol)** is a way for Claude Code to talk to external services and tools. Think of it as a bridge that lets Claude:
- Access your GitHub repositories
- Query databases
- Read/write files on your system
- Send messages to Slack
- Interact with APIs
- And much more!

## Why Use MCP?

Without MCP, Claude can only work with files in your project. With MCP, Claude can:
- ✅ Check GitHub issues and create PRs
- ✅ Query your database for information
- ✅ Access files outside the project
- ✅ Integrate with your team's tools
- ✅ Remember things between sessions
- ✅ Connect to any API or service

## Available Examples

This directory contains beginner-friendly MCP examples:

### 1. **filesystem-server/** - Local File Access
Learn how to let Claude access files outside your project directory.

**Use cases:**
- Access documentation in another folder
- Read configuration files from home directory
- Work with files across multiple projects

### 2. **memory-server/** - Persistent Notes
Give Claude a memory that persists between sessions.

**Use cases:**
- Remember project decisions
- Store TODO lists
- Keep track of bugs to fix
- Save code snippets

### 3. **github-server/** - GitHub Integration
Connect Claude to GitHub to manage issues and PRs.

**Use cases:**
- Create GitHub issues from bugs you find
- List and review pull requests
- Check repository information
- Search code across repos

### 4. **sqlite-server/** - Database Access
Let Claude query SQLite databases.

**Use cases:**
- Analyze database contents
- Generate queries
- Create reports from data
- Debug database issues

## Quick Start

### Step 1: Understanding the Setup

MCP servers are configured in a file called `.mcp.json` in your project root:

```json
{
  "mcpServers": {
    "server-name": {
      "command": "command-to-run",
      "args": ["arguments"],
      "env": {
        "ENVIRONMENT_VARIABLES": "values"
      }
    }
  }
}
```

### Step 2: Choose Your First Server

Start with the **memory server** - it's the simplest:
1. No external accounts needed
2. No API keys required
3. Works immediately
4. Great for learning

### Step 3: Try It Out

See the individual example directories for detailed setup instructions!

## How MCP Works

```
┌─────────────────┐
│   Claude Code   │
│                 │
│  Your project   │
└────────┬────────┘
         │
         │ Uses MCP Protocol
         │
    ┌────▼─────┐
    │   MCP    │
    │  Server  │
    └────┬─────┘
         │
         │ Connects to
         │
┌────────▼────────┐
│ External Service│
│                 │
│ GitHub, DB, etc │
└─────────────────┘
```

## Installation Methods

### Method 1: NPX (Easiest)
Many MCP servers can run directly with npx:
```json
{
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-github"]
}
```

### Method 2: System Installation
Install globally and use:
```bash
npm install -g @modelcontextprotocol/server-github
```
```json
{
  "command": "mcp-server-github"
}
```

### Method 3: Local Project
Install in your project:
```bash
npm install @modelcontextprotocol/server-github
```
```json
{
  "command": "node_modules/.bin/mcp-server-github"
}
```

## Security Best Practices

### 🔒 Important Security Rules:

1. **NEVER commit `.mcp.json` with real credentials**
   ```bash
   # Add to .gitignore
   echo ".mcp.json" >> .gitignore
   ```

2. **Use environment variables when possible**
   ```json
   {
     "env": {
       "API_KEY": "${API_KEY}"  // Reads from your shell
     }
   }
   ```

3. **Use read-only credentials when possible**
   - Create tokens with minimal permissions
   - Only grant what's needed
   - Revoke tokens when done

4. **Review MCP servers before using**
   - Only use servers from trusted sources
   - Check what permissions they need
   - Understand what they can access

5. **Create a template file for sharing**
   ```bash
   cp .mcp.json .mcp.json.template
   # Replace real credentials with placeholders
   git add .mcp.json.template
   ```

## Common Setup Pattern

Every example follows this pattern:

### 1. Create `.mcp.json`
```json
{
  "mcpServers": {
    "my-server": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-name"],
      "env": {
        "API_KEY": "your-key-here"
      }
    }
  }
}
```

### 2. Get Credentials (if needed)
- Create API token
- Set up access
- Note permissions needed

### 3. Test It
```bash
claude
# In Claude Code:
"List available MCP tools"
```

### 4. Use It
```bash
"Use the github server to list my issues"
```

## Troubleshooting MCP

### Issue: "MCP server not found"

**Check:**
1. Is `.mcp.json` in project root?
2. Is JSON syntax correct?
3. Is command accessible?
4. Did you restart Claude Code?

**Fix:**
```bash
# Validate JSON
cat .mcp.json | jq .

# Test command
npx -y @modelcontextprotocol/server-github --help

# Restart Claude Code
exit
claude
```

### Issue: "Authentication failed"

**Check:**
1. Are credentials correct?
2. Does token have right permissions?
3. Is token expired?
4. Are environment variables set?

**Fix:**
- Regenerate token
- Check permissions
- Set environment variables
- Review server documentation

### Issue: "Command not found"

**Check:**
1. Is npx installed? (`which npx`)
2. Is path correct?
3. Is package name correct?

**Fix:**
```bash
# Install npx if needed (comes with Node.js)
node --version
npm --version

# Try full path
"command": "/usr/local/bin/npx"
```

### Issue: "Server crashes immediately"

**Check:**
1. Look at error message
2. Check server logs
3. Verify dependencies

**Fix:**
```bash
# Run with debug mode
claude --debug
```

## Tips for Success

### 1. Start Simple
- Begin with memory server (no auth needed)
- Then try filesystem (local only)
- Graduate to external services (GitHub, etc.)

### 2. Test Incrementally
- Add one server at a time
- Test it works before adding next
- Keep backup of working config

### 3. Read the Documentation
Each MCP server has its own:
- Required credentials
- Available commands
- Configuration options
- Usage examples

### 4. Use Templates
- Create `.mcp.json.template` for your team
- Document which credentials are needed
- Include setup instructions

### 5. Organize by Project
```
project-a/.mcp.json  → Uses GitHub + PostgreSQL
project-b/.mcp.json  → Uses Slack + Memory
home-config/.mcp.json → Your personal defaults
```

## Learning Path

### Week 1: Local Servers
Start with servers that don't need external services:
1. ✅ Memory server - Learn MCP basics
2. ✅ Filesystem server - Understand permissions
3. ✅ Practice using them naturally

### Week 2: External Services
Add servers that connect externally:
1. ✅ GitHub server - Learn API integration
2. ✅ Try with your repos
3. ✅ Create issues and PRs

### Week 3: Data Services
Work with data:
1. ✅ SQLite server - Database queries
2. ✅ Create test database
3. ✅ Practice querying

### Week 4: Advanced
Build your own:
1. ✅ Custom MCP server
2. ✅ Team-specific integrations
3. ✅ Workflow automation

## Real-World Use Cases

### Use Case 1: Project Management
```json
{
  "mcpServers": {
    "github": { /* GitHub config */ },
    "memory": { /* Memory config */ }
  }
}
```

Workflow:
1. Find bugs while coding
2. "Create a GitHub issue for this bug"
3. "Remember to refactor this module"
4. Later: "What did I want to refactor?"

### Use Case 2: Data Analysis
```json
{
  "mcpServers": {
    "sqlite": { /* SQLite config */ },
    "filesystem": { /* Filesystem config */ }
  }
}
```

Workflow:
1. "Show me the database schema"
2. "Query all users from last month"
3. "Export results to CSV in /reports/"
4. "Read and analyze the CSV"

### Use Case 3: Documentation
```json
{
  "mcpServers": {
    "filesystem": { /* Access docs folder */ },
    "memory": { /* Remember decisions */ }
  }
}
```

Workflow:
1. "Read the API docs from /docs/"
2. "Remember: We decided to use REST not GraphQL"
3. "What was our API decision?"
4. "Update the docs with this change"

## Available MCP Servers

### Official Servers
From `@modelcontextprotocol`:
- **filesystem** - File operations
- **github** - GitHub integration
- **gitlab** - GitLab integration
- **postgres** - PostgreSQL database
- **sqlite** - SQLite database
- **memory** - Persistent storage
- **fetch** - HTTP requests
- **slack** - Slack integration
- **google-drive** - Google Drive access
- **puppeteer** - Browser automation

### Community Servers
Many more from the community! Search npm for "mcp-server-*"

## Creating Your Own MCP Server

Want to create a custom MCP server? Check the advanced examples!

Basic structure:
```javascript
import { Server } from '@modelcontextprotocol/sdk/server/index.js';

const server = new Server({
  name: 'my-custom-server',
  version: '1.0.0'
});

// Add your tools and logic
server.setRequestHandler(/* ... */);

// Start server
server.connect(/* ... */);
```

## Best Practices Summary

✅ **Do:**
- Start with simple servers
- Test thoroughly
- Use read-only credentials when possible
- Document your setup
- Keep `.mcp.json` in `.gitignore`
- Create template files for team
- Review server code before using
- Use environment variables for secrets

❌ **Don't:**
- Commit real credentials to git
- Use overly permissive tokens
- Trust unknown MCP servers
- Share credentials in config files
- Forget to test after setup
- Use production credentials for testing

## Getting Help

### Official Resources
- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP GitHub](https://github.com/modelcontextprotocol)
- [MCP Servers List](https://github.com/modelcontextprotocol/servers)

### Community
- GitHub Discussions
- Discord servers
- Stack Overflow (tag: mcp)

### Debugging
```bash
# Run Claude with debug output
claude --debug

# Check MCP server logs
claude --mcp-debug

# Test server directly
npx @modelcontextprotocol/server-github --test
```

## Next Steps

1. **Choose an example** from this directory
2. **Follow the setup guide** in its README
3. **Try it out** with Claude Code
4. **Experiment** with different use cases
5. **Add more servers** as you need them

## FAQ

**Q: Do I need to install MCP separately?**
A: No! MCP support is built into Claude Code.

**Q: How many MCP servers can I use at once?**
A: As many as you want! Just add them to `.mcp.json`.

**Q: Are MCP servers free?**
A: Most are free and open source. Some services (like GitHub API) may have rate limits.

**Q: Can I create my own MCP server?**
A: Yes! Check the advanced examples and MCP SDK documentation.

**Q: Is MCP secure?**
A: MCP itself is secure, but be careful with:
- What servers you trust
- What permissions you grant
- What credentials you use

**Q: Do MCP servers work offline?**
A: Some do (filesystem, memory, sqlite), some need internet (github, slack).

**Q: Can I use MCP with teams?**
A: Yes! Share `.mcp.json.template` files (without real credentials).

---

## 🚀 Advanced: Code Execution Pattern (98.7% Token Savings!)

Once you're comfortable with basic MCP, consider upgrading to Anthropic's **filesystem-based code execution pattern** for massive performance gains.

**Traditional MCP (this guide):**
- ✅ Easy to learn
- ✅ Simple setup
- ✅ Great for beginners
- ❌ Higher token usage

**Code Execution Pattern (advanced):**
- ✅ 98.7% token savings
- ✅ Better performance
- ✅ Enhanced privacy
- ✅ Reusable skills
- ℹ️ Requires code execution environment

**Learn more:**
- **Example:** `examples/advanced/mcp-code-execution/README.md`
- **Skill:** `advanced-kit/.claude/skills/mcp-code-execution.md`
- **Templates:** `templates/mcp-code-execution/`
- **Blog Post:** https://www.anthropic.com/engineering/code-execution-with-mcp

**When to upgrade:**
- Processing large datasets (1,000+ rows)
- Multi-step workflows (5+ operations)
- Privacy-sensitive data (PII)
- High-frequency MCP usage

---

**Ready to get started? Pick an example and dive in!**

Recommended order:
1. 📝 memory-server (easiest)
2. 📁 filesystem-server (very useful)
3. 🐙 github-server (powerful)
4. 🗄️ sqlite-server (data access)

**Then level up:**
5. 🚀 Code execution pattern (98.7% token savings!)

Happy integrating! 🚀
