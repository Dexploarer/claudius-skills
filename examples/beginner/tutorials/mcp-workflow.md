# Tutorial: Building Your First MCP Workflow

Learn how to connect external services to Claude Code using the Model Context Protocol (MCP).

## What You'll Build

A complete workflow using **GitHub + Memory MCP servers** that:
1. Fetches GitHub issues
2. Analyzes and prioritizes them
3. Stores analysis in persistent memory
4. Retrieves stored insights across sessions

**Why this workflow?**
- Demonstrates real MCP integration
- Uses two different MCP servers
- Solves practical problems
- Shows persistent memory
- Teaches MCP configuration

## Prerequisites

- Claude Code installed
- Completed previous tutorials
- GitHub account
- GitHub Personal Access Token
- Node.js installed (for MCP servers)
- 30-40 minutes of time

## Step 1: Understand MCP

**Model Context Protocol (MCP)** allows Claude Code to connect to external services and tools.

**What MCP Enables:**
- 📂 Access files outside your project (filesystem MCP)
- 🐙 Read GitHub issues, PRs, repos (GitHub MCP)
- 🧠 Remember information across sessions (memory MCP)
- 🗄️ Query databases (SQLite, PostgreSQL MCP)
- 🌐 Fetch web content (fetch MCP)
- 📊 And much more!

**How MCP Works:**
```
Claude Code  ←→  MCP Server  ←→  External Service
             (Protocol)          (GitHub, DB, etc.)
```

**MCP Servers are:**
- Separate processes that run alongside Claude
- Provide tools and resources to Claude
- Configured in `.mcp.json`
- Can be written in any language
- Often available as npm packages

## Step 2: Understanding MCP Configuration

MCP servers are configured in `.mcp.json` at your project root:

```json
{
  "mcpServers": {
    "server-name": {
      "command": "node",
      "args": ["/path/to/server/index.js"],
      "env": {
        "API_KEY": "your-api-key"
      }
    }
  }
}
```

**Key parts:**
- `server-name`: Friendly name for the server
- `command`: Program to run (node, python, npx, etc.)
- `args`: Arguments to pass
- `env`: Environment variables (API keys, config)

## Step 3: Set Up GitHub Personal Access Token

You'll need a GitHub token for the GitHub MCP server.

### Create Token

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a name: "Claude Code MCP"
4. Select scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `read:org` (Read org and team membership)
   - ✅ `read:user` (Read user profile data)
5. Click "Generate token"
6. **Copy the token** (you won't see it again!)

### Store Token Securely

**Option 1: Environment Variable (Recommended)**
```bash
# Add to ~/.bashrc or ~/.zshrc
export GITHUB_TOKEN="ghp_your_token_here"

# Reload
source ~/.bashrc
```

**Option 2: .env File (for this project only)**
```bash
# Create .env in your project
echo "GITHUB_TOKEN=ghp_your_token_here" > .env

# Add to .gitignore
echo ".env" >> .gitignore
```

⚠️ **NEVER** commit tokens to git!

## Step 4: Create MCP Configuration

Create `.mcp.json` in your project root:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "memory": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-memory"
      ]
    }
  }
}
```

**What this does:**
- `github`: Connects to GitHub API
  - Uses `npx` to run the server
  - `-y` auto-confirms installation
  - Token from environment variable
- `memory`: Provides persistent memory
  - No configuration needed
  - Stores data in local files

## Step 5: Test MCP Servers

Start Claude Code to initialize MCP servers:

```bash
cd your-project
claude
```

**On first start:**
- MCP servers will be downloaded
- May take a moment to initialize
- You'll see connection messages

**Test GitHub MCP:**
```
"List the issues in the repository facebook/react"
```

Expected: Claude uses GitHub MCP to fetch issues.

**Test Memory MCP:**
```
"Remember that my favorite programming language is TypeScript"
```

Then quit and restart Claude:
```bash
# Exit Claude
exit

# Restart
claude
```

Ask:
```
"What's my favorite programming language?"
```

Expected: Claude remembers from previous session!

## Step 6: Build the Workflow

Now let's create a practical workflow combining both MCP servers.

### Create a Slash Command

Create `.claude/commands/analyze-issues.md`:

```markdown
# Analyze GitHub Issues

Fetch, analyze, and remember GitHub issues for a repository.

## Arguments

$ARGUMENTS should be: owner/repo (e.g., "facebook/react")

## Instructions

### Step 1: Fetch Issues

Use GitHub MCP to fetch open issues from the repository.

\```bash
# Internally, Claude uses the GitHub MCP tools
# You can ask: "List open issues in REPO"
\```

### Step 2: Analyze Issues

For each issue, identify:
1. **Type**: Bug, feature request, question, etc.
2. **Priority**: Based on labels, reactions, comments
3. **Complexity**: Simple, medium, complex
4. **Category**: What part of the project it affects

### Step 3: Categorize

Group issues by:
- Priority (High/Medium/Low)
- Type (Bug/Feature/Docs/Question)
- Status (Needs triage/In progress/Blocked)

### Step 4: Store in Memory

Use Memory MCP to store:
\```
Repository: {repo}
Last analyzed: {date}
Total issues: {count}

High Priority:
- Issue #{number}: {title}
- Issue #{number}: {title}

Top Bugs:
- Issue #{number}: {title}

Recommendations:
- Focus on issues #{list}
- Consider closing stale issues
\```

### Step 5: Present Summary

Show:
\```
📊 Issue Analysis for {repo}
━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 Statistics:
   Total Issues: {count}
   Bugs: {count}
   Features: {count}
   Questions: {count}

🔥 High Priority ({count}):
   #{num} - {title}
   #{num} - {title}

💡 Recommendations:
   - {recommendation}
   - {recommendation}

✅ Analysis saved to memory
   Run /recall-analysis to see it again
\```

## Example Output

When you run:
\```
/analyze-issues facebook/react
\```

Expected output:
\```
📊 Issue Analysis for facebook/react
━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 Statistics:
   Total Issues: 847
   Bugs: 234
   Features: 156
   Questions: 98
   Other: 359

🔥 High Priority (5):
   #26925 - [Bug] Hydration mismatch in SSR
   #26894 - [Feature] Add useEvent hook
   #26883 - [Bug] Memory leak in useEffect

🐛 Top Bugs (3):
   #26925 - Hydration mismatch (42 reactions)
   #26883 - Memory leak (38 reactions)
   #26801 - Crash on navigation (29 reactions)

✨ Top Features (3):
   #26894 - Add useEvent hook (156 reactions)
   #26754 - Better TypeScript support (98 reactions)
   #26723 - Suspense improvements (87 reactions)

💡 Recommendations:
   - Focus on hydration issues (blocking SSR users)
   - Consider useEvent RFC (high demand)
   - Review memory leak reports (multiple similar issues)

✅ Analysis saved to memory
   Run /recall-analysis to retrieve
\```
```

### Create Recall Command

Create `.claude/commands/recall-analysis.md`:

```markdown
# Recall Issue Analysis

Retrieve previously saved issue analysis from memory.

## Instructions

1. Use Memory MCP to recall issue analysis
2. Search for: "Repository: " entries
3. Display the most recent analysis
4. If multiple repositories, show all

## Format

\```
📚 Saved Analyses
━━━━━━━━━━━━━━━

🗂️  {repo}
   Last analyzed: {date}
   Total issues: {count}
   High priority: {count}

   Quick actions:
   - /analyze-issues {repo}  # Re-analyze
   - "Show me issue #123 from {repo}"  # View specific issue
\```
```

## Step 7: Use the Workflow

### Analyze a Repository

```bash
claude

# Run analysis
/analyze-issues facebook/react
```

Claude will:
1. ✅ Fetch issues using GitHub MCP
2. ✅ Analyze and categorize them
3. ✅ Store summary in Memory MCP
4. ✅ Display results

### Retrieve Analysis Later

```bash
# Later, in a new session
claude

# Recall what you analyzed
/recall-analysis
```

### Ask Questions

```
"What were the high priority issues in the React repo?"
"Show me the bug with the most reactions"
"What did I learn about the React repository?"
```

Claude uses Memory MCP to recall!

## Step 8: Enhance the Workflow

### Add More MCP Servers

**SQLite MCP** (for local database):
```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sqlite",
        "--db-path",
        "./issues.db"
      ]
    }
  }
}
```

Use case: Store issue analysis in a queryable database.

**Filesystem MCP** (access files anywhere):
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/allowed/directory"
      ]
    }
  }
}
```

Use case: Read notes or docs from outside project.

### Create Issue Templates

Store common responses in memory:

```
"Remember this bug report template:
---
**Bug Description:**
[Clear, concise description]

**Steps to Reproduce:**
1. [First step]
2. [Second step]

**Expected Behavior:**
[What should happen]

**Actual Behavior:**
[What actually happens]

**Environment:**
- OS: [e.g., macOS 13.0]
- Browser: [e.g., Chrome 110]
- Version: [e.g., 1.2.3]
---
Tag this as: bug-template"
```

Retrieve:
```
"Show me the bug report template"
```

### Track Your Work

```
"Remember that today I:
- Reviewed React issues
- Found 5 critical bugs
- Proposed fix for #26925
Tag this as: work-log-2024-01-15"
```

Next day:
```
"What did I work on yesterday?"
```

## Step 9: Advanced MCP Patterns

### Pattern 1: Cross-Reference

```
"Find React issues similar to the bug I reported in my-project"
```

Uses:
1. GitHub MCP (fetch React issues)
2. Memory MCP (recall what you reported)
3. Analysis to find similarities

### Pattern 2: Persistent Context

```
"Remember my current project uses:
- React 18
- TypeScript 5
- Vite 4
Tag as: current-project-stack"
```

Later sessions:
```
"What version of React am I using?"
```

### Pattern 3: Knowledge Base

```
"Remember: To fix hydration mismatches:
1. Ensure server and client render identically
2. Check useEffect dependencies
3. Avoid Date.now() or Math.random() in render
Tag as: react-knowledge"
```

Build a personal knowledge base!

## Common Issues & Solutions

### Issue 1: MCP Server Won't Start

**Problem:** MCP server fails to connect

**Solutions:**
1. Check `.mcp.json` syntax (must be valid JSON)
2. Verify `command` exists: `which npx`
3. Check token is set: `echo $GITHUB_TOKEN`
4. Look at Claude Code logs for errors
5. Try manually: `npx @modelcontextprotocol/server-github`

### Issue 2: GitHub Token Invalid

**Problem:** GitHub MCP can't authenticate

**Solutions:**
1. Verify token hasn't expired
2. Check token has correct scopes
3. Ensure token is in environment: `env | grep GITHUB`
4. Regenerate token if needed

### Issue 3: Memory Not Persisting

**Problem:** Memory MCP forgets across sessions

**Solutions:**
1. Check if memory server is configured in `.mcp.json`
2. Verify memory files aren't being deleted
3. Look for `.mcp-memory/` directory
4. Don't add memory directory to `.gitignore`

### Issue 4: Slow MCP Responses

**Problem:** MCP operations take too long

**Solutions:**
1. Limit scope of queries (don't fetch all issues)
2. Use pagination
3. Cache results in memory
4. Check internet connection

## Best Practices

### ✅ Do:
- Use environment variables for secrets
- Add `.env` to `.gitignore`
- Test MCP servers independently
- Start with official MCP servers
- Document which MCP servers you use
- Version control `.mcp.json` (not secrets!)

### ❌ Don't:
- Commit API tokens to git
- Give MCP servers more access than needed
- Rely on MCP for critical paths (can fail)
- Store sensitive data in Memory MCP unencrypted
- Forget to test after configuration changes

## Available MCP Servers

### Official Servers

- **@modelcontextprotocol/server-github** - GitHub integration
- **@modelcontextprotocol/server-memory** - Persistent memory
- **@modelcontextprotocol/server-filesystem** - File access
- **@modelcontextprotocol/server-sqlite** - SQLite databases
- **@modelcontextprotocol/server-postgres** - PostgreSQL
- **@modelcontextprotocol/server-fetch** - Web fetching
- **@modelcontextprotocol/server-slack** - Slack integration

### Community Servers

- **mcp-server-jira** - Jira integration
- **mcp-server-notion** - Notion database
- **mcp-server-google-calendar** - Calendar access
- **mcp-server-aws** - AWS services

Find more: https://github.com/modelcontextprotocol/servers

## Real-World Use Cases

### 1. Project Management
```
MCP: GitHub + Jira + Memory
Workflow: Sync issues, track progress, remember context
```

### 2. Documentation
```
MCP: Filesystem + Memory + Fetch
Workflow: Read docs, remember key info, fetch examples
```

### 3. Development
```
MCP: GitHub + SQLite + Memory
Workflow: Track bugs, analyze patterns, store solutions
```

### 4. Research
```
MCP: Fetch + Memory + Filesystem
Workflow: Research topics, save insights, organize notes
```

## Security Considerations

### Protecting API Keys

```json
// ❌ Bad: Hardcoded
{
  "env": {
    "GITHUB_TOKEN": "ghp_actual_token_here"
  }
}

// ✅ Good: Environment variable
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

### Limiting MCP Access

```json
// Filesystem: Only allow specific directory
{
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    "./allowed-directory"  // Not "/" !
  ]
}
```

### Sensitive Data in Memory

```
// Don't store:
"Remember my password is: ..." ❌

// Do store:
"Remember I use PostgreSQL for this project" ✅
```

## Next Steps

### Level 1: Explore
- Try different MCP servers
- Build simple workflows
- Store useful information in memory

### Level 2: Integrate
- Combine 3+ MCP servers
- Create automated workflows
- Build a personal knowledge base

### Level 3: Custom
- Write your own MCP server
- Create domain-specific integrations
- Share with community

## Congratulations!

You've built your first MCP workflow! 🎉

**What you learned:**
- ✅ What MCP is and why it's useful
- ✅ How to configure MCP servers
- ✅ Managing API tokens securely
- ✅ Using GitHub MCP
- ✅ Using Memory MCP for persistence
- ✅ Building workflows with multiple MCP servers
- ✅ Best practices and security

**Next challenges:**
1. Add SQLite MCP to store structured data
2. Use Filesystem MCP to access project templates
3. Build a workflow for your specific needs
4. Create a personal knowledge management system

---

**Ready for the final tutorial? Continue with [complete-workflow.md](./complete-workflow.md)!**
