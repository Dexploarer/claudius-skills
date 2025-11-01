# Memory Server - MCP Example

The simplest MCP server to get started! Gives Claude a persistent memory that survives between sessions.

## What It Does

The Memory server lets Claude:
- **Remember things** between sessions
- **Store notes** that persist
- **Save decisions** you've made
- **Keep TODO lists**
- **Store code snippets** for later

Think of it as giving Claude a notebook that it keeps forever.

## Why Start Here?

Perfect for beginners because:
- ✅ **No external accounts** needed
- ✅ **No API keys** required
- ✅ **Works instantly**
- ✅ **No network** required
- ✅ **Simple to understand**
- ✅ **Great for learning** MCP basics

## Installation

### Step 1: Create `.mcp.json`

In your project root, create `.mcp.json`:

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

### Step 2: Restart Claude Code

```bash
# Exit Claude Code if running
exit

# Start it again
claude
```

### Step 3: Test It!

```bash
# In Claude Code:
"Remember: The main API endpoint is at /api/v2"
"What did I tell you to remember?"
```

That's it! You're using MCP! 🎉

## How to Use

### Storing Information

```bash
"Remember: We decided to use PostgreSQL for the database"
"Store this note: Need to refactor the auth module"
"Save this: API rate limit is 1000 requests/hour"
```

### Retrieving Information

```bash
"What database did we decide to use?"
"What notes do I have?"
"List everything you remember"
```

### Updating Information

```bash
"Update the note about the auth module: Refactoring is complete"
```

### Deleting Information

```bash
"Forget about the API rate limit"
"Delete all notes about the auth module"
```

## Example Use Cases

### Use Case 1: Project Decisions

```bash
# Day 1
You: "Remember: We're using React instead of Vue for this project"
Claude: "I've stored that decision."

# Week later
You: "What framework are we using?"
Claude: "You're using React instead of Vue for this project."
```

### Use Case 2: TODO Tracking

```bash
You: "Add to my TODO list: Fix the login bug, Add tests, Update docs"
Claude: "I've added those to your TODO list."

# Later
You: "What's on my TODO list?"
Claude: "Your TODOs:
1. Fix the login bug
2. Add tests
3. Update docs"

# After completing one
You: "Mark 'Fix the login bug' as done"
Claude: "Removed from TODO list. Remaining: Add tests, Update docs"
```

### Use Case 3: Code Snippets

```bash
You: "Remember this SQL query for later: SELECT * FROM users WHERE active = true"
Claude: "I've saved that query."

# Later when you need it
You: "What was that SQL query I asked you to remember?"
Claude: "Here's the query: SELECT * FROM users WHERE active = true"
```

### Use Case 4: Team Conventions

```bash
You: "Remember our naming convention: Components in PascalCase, utilities in camelCase"
Claude: "I'll remember that naming convention."

# During development
You: "What's our naming convention?"
Claude: "Components use PascalCase, utilities use camelCase."
```

### Use Case 5: Bug Tracking

```bash
You: "Add bug: Login form doesn't validate empty emails"
You: "Add bug: Profile page crashes on mobile"
You: "Add bug: Search is too slow with large datasets"

# Later
You: "List all bugs"
Claude: "Known bugs:
1. Login form doesn't validate empty emails
2. Profile page crashes on mobile
3. Search is too slow with large datasets"
```

## Where Is Data Stored?

The memory server stores data in your home directory:

```
~/.mcp/memory/
  └── memory.db
```

This is a simple JSON file containing all stored memories.

## Available Commands

The memory server provides these capabilities:

### 1. Store Memory
```bash
"Remember [something]"
"Store this note: [something]"
"Save this: [something]"
```

### 2. Retrieve Memory
```bash
"What did I tell you about [topic]?"
"List all memories"
"Show me what you remember"
"Do you remember anything about [topic]?"
```

### 3. Update Memory
```bash
"Update the memory about [topic]: [new info]"
"Change the note about [topic] to [new info]"
```

### 4. Delete Memory
```bash
"Forget about [topic]"
"Delete the memory about [topic]"
"Clear all memories"
```

### 5. Search Memory
```bash
"Search your memory for [keyword]"
"Find all memories about [topic]"
```

## Tips for Effective Use

### 1. Be Specific

✅ **Good:**
```bash
"Remember: Main branch name is 'develop', not 'main'"
```

❌ **Too vague:**
```bash
"Remember the branch thing"
```

### 2. Use Categories

```bash
"Remember [DECISION]: Using REST API not GraphQL"
"Remember [TODO]: Refactor auth module"
"Remember [BUG]: Login validation issue"
"Remember [SNIPPET]: SQL query for active users"
```

### 3. Review Periodically

```bash
# Weekly review
"List all TODOs"
"Show me all decisions"
"What bugs are still open?"
```

### 4. Clean Up Old Items

```bash
"Delete completed TODOs"
"Forget about the old API endpoint"
```

## Best Practices

✅ **Do:**
- Store important decisions
- Keep track of TODOs
- Save useful code snippets
- Remember team conventions
- Track known issues
- Document why choices were made

❌ **Don't:**
- Store sensitive data (passwords, keys)
- Keep outdated information
- Store what's already in code
- Use as a backup system
- Store large amounts of data
- Forget to clean up old memories

## Limitations

### What Memory Server CAN'T Do:
- ❌ Store large files
- ❌ Store binary data
- ❌ Share between team members
- ❌ Version control
- ❌ Complex queries
- ❌ Encrypt sensitive data

### What It CAN Do:
- ✅ Store text notes
- ✅ Persist between sessions
- ✅ Simple search
- ✅ Update/delete entries
- ✅ Lightweight and fast
- ✅ No configuration needed

## Troubleshooting

### Issue: "Memory server not found"

**Solution:**
```bash
# Make sure npx is installed
which npx

# Test the server directly
npx -y @modelcontextprotocol/server-memory --help

# Check .mcp.json syntax
cat .mcp.json | jq .
```

### Issue: "Memory not persisting"

**Solution:**
```bash
# Check if data file exists
ls -la ~/.mcp/memory/

# Check permissions
chmod 755 ~/.mcp/memory/

# Try recreating .mcp.json
```

### Issue: "Can't retrieve memories"

**Solution:**
```bash
# Be specific in queries
# Instead of: "What did I save?"
# Try: "List all memories about the API"

# Check data file
cat ~/.mcp/memory/memory.db
```

## Advanced Usage

### Structured Storage

Organize memories with prefixes:

```bash
"Remember [PROJECT:MyApp] Using PostgreSQL"
"Remember [PROJECT:MyApp] API at /api/v2"
"Remember [PROJECT:OtherApp] Using MongoDB"

# Later, retrieve by project
"Show me all memories for PROJECT:MyApp"
```

### Timestamped Notes

```bash
"Remember [2024-11-01] Decided on architecture"
"Remember [2024-11-02] Started implementation"
```

### Priority Levels

```bash
"Remember [HIGH] Security issue in auth module"
"Remember [MEDIUM] Refactor needed in utils"
"Remember [LOW] Consider dark mode feature"
```

## Integration with Other Tools

### With Git Workflow

```bash
# Store commit reminders
"Remember: Need to squash commits before merging"

# Store branch strategies
"Remember: Feature branches use 'feature/' prefix"
```

### With Code Reviews

```bash
# Store common feedback
"Remember: Always check for null before accessing properties"
"Remember: Prefer async/await over .then()"
```

### With Documentation

```bash
# Store docs locations
"Remember: Architecture docs in /docs/architecture.md"
"Remember: API docs auto-generated from OpenAPI spec"
```

## Example Session

```bash
# Start of week
You: "Remember: This week's focus is refactoring the auth module"
Claude: "I'll remember that this week's focus is refactoring the auth module."

# During work
You: "What am I focusing on this week?"
Claude: "You're focusing on refactoring the auth module."

# Adding details
You: "Remember: Auth refactor steps - 1) Extract logic 2) Add tests 3) Update docs"
Claude: "I've saved those auth refactor steps."

# End of week
You: "Show me everything about the auth refactor"
Claude: "Here's what I remember about the auth refactor:
- This week's focus is refactoring the auth module
- Steps: 1) Extract logic 2) Add tests 3) Update docs"

# Cleanup
You: "Delete memories about auth refactor"
Claude: "I've deleted the auth refactor memories."
```

## Combining with Other MCP Servers

Memory server works great with others:

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
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
"Create a GitHub issue for the bug I told you to remember"
"Remember: Created issue #123 for the login bug"
```

## Security Notes

### Safe to Store:
- ✅ Project decisions
- ✅ TODO items
- ✅ Code snippets (non-sensitive)
- ✅ Team conventions
- ✅ Public information

### NOT Safe to Store:
- ❌ Passwords
- ❌ API keys
- ❌ Access tokens
- ❌ Private keys
- ❌ Personal data
- ❌ Customer information

**Remember:** Memory is stored in plain text in `~/.mcp/memory/memory.db`

## FAQ

**Q: Can team members share the same memory?**
A: No, memory is local to your machine. For team sharing, use GitHub issues or project documentation.

**Q: What happens if I delete ~/.mcp/memory/?**
A: All memories are lost. The server will create a new empty database on next use.

**Q: Is there a size limit?**
A: Technically no, but keep it to short text notes for best performance.

**Q: Can I backup memories?**
A: Yes! Just copy `~/.mcp/memory/memory.db` to a backup location.

**Q: Can I edit memories directly?**
A: Yes, the file is JSON and can be edited, but use Claude's commands for safety.

**Q: Does this work across different Claude Code projects?**
A: Yes! Memories are global, available in any project with memory server configured.

## Next Steps

Now that you understand the memory server:

1. ✅ **Try it out** - Store some information and retrieve it
2. ✅ **Use it daily** - Track TODOs and decisions
3. ✅ **Move to next example** - Try filesystem-server next
4. ✅ **Combine servers** - Use multiple MCP servers together

## Related Examples

- **filesystem-server** - Access files outside project
- **github-server** - Integrate with GitHub
- **sqlite-server** - Store structured data

---

**Congratulations!** You've learned your first MCP server. This is the foundation for using all other MCP servers! 🎉
