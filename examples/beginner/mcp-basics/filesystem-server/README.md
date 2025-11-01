# Filesystem Server - MCP Example

Let Claude access files and directories outside your current project.

## What It Does

The Filesystem server lets Claude:
- **Read files** from anywhere on your system
- **Write files** to specified directories
- **List directories** outside the project
- **Search files** across multiple locations
- **Manage files** in designated folders

## Why Use This?

Perfect when you need to:
- Access documentation in another folder
- Read configuration files from home directory
- Work with files across multiple projects
- Organize downloads or temporary files
- Access shared team resources

## Installation

### Step 1: Create `.mcp.json`

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

**Important:** Replace `/path/to/allowed/directory` with actual paths you want to allow.

### Step 2: Configure Allowed Paths

You can allow multiple directories:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/yourname/Documents",
        "/Users/yourname/Downloads",
        "/tmp"
      ]
    }
  }
}
```

### Step 3: Restart Claude Code

```bash
exit
claude
```

### Step 4: Test It!

```bash
"List files in my Documents folder"
"Read the file at ~/Documents/notes.txt"
```

## Security Best Practices

### ⚠️ **IMPORTANT SECURITY NOTES**

The filesystem server gives Claude access to your files. Be careful:

1. **Only allow necessary directories**
   ```json
   // ❌ DON'T DO THIS (too broad)
   "args": ["-y", "@modelcontextprotocol/server-filesystem", "/"]

   // ✅ DO THIS (specific)
   "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/you/projects"]
   ```

2. **Never allow sensitive directories**
   - ❌ `~/.ssh` (SSH keys)
   - ❌ `~/.aws` (AWS credentials)
   - ❌ `~/` (entire home directory)
   - ❌ `/etc` (system files)

3. **Use read-only when possible**
   Check if server supports read-only mode in documentation.

4. **Review what Claude accesses**
   Always know what files Claude is reading or writing.

## Example Configurations

### Configuration 1: Documentation Access
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/yourname/Documents/project-docs"
      ]
    }
  }
}
```

**Use case:** Access project documentation outside the current repo.

### Configuration 2: Multi-Project Access
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/yourname/projects/frontend",
        "/Users/yourname/projects/backend",
        "/Users/yourname/projects/mobile"
      ]
    }
  }
}
```

**Use case:** Work across multiple related projects.

### Configuration 3: Temp and Downloads
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/tmp",
        "/Users/yourname/Downloads"
      ]
    }
  }
}
```

**Use case:** Process downloaded files or work with temp files.

## How to Use

### Reading Files

```bash
"Read the file at /Users/me/Documents/notes.txt"
"Show me the contents of ~/Documents/api-spec.yaml"
"What's in the README.md file in ~/projects/myapp/"
```

### Writing Files

```bash
"Write this content to ~/Documents/summary.md: [content]"
"Create a file at ~/Downloads/report.txt with the analysis"
"Save this code snippet to ~/temp/example.js"
```

### Listing Directories

```bash
"List all files in ~/Documents/"
"Show me markdown files in ~/projects/"
"What's in my Downloads folder?"
```

### Searching Files

```bash
"Find all .js files in ~/projects/"
"Search for 'TODO' in files in ~/Documents/"
"List all Python files in ~/code/"
```

## Example Use Cases

### Use Case 1: Cross-Project Reference

**Scenario:** You're working on a frontend app but need to reference the backend API.

```bash
# Setup: Allow both directories in .mcp.json
{
  "args": [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    "/Users/me/projects/frontend",
    "/Users/me/projects/backend"
  ]
}

# Usage
You: "Read the API routes from ~/projects/backend/routes.js"
Claude: "Here are the API routes: ..."

You: "Now update my frontend API client to match"
Claude: "I'll update the frontend API client..."
```

### Use Case 2: Documentation Workflow

**Scenario:** Keep project documentation separate from code.

```bash
# Setup
{
  "args": [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    "/Users/me/projects/myapp",
    "/Users/me/Documents/myapp-docs"
  ]
}

# Usage
You: "Read the architecture docs from ~/Documents/myapp-docs/"
Claude: "I'll read the architecture documentation..."

You: "Based on those docs, implement the auth module"
Claude: "Following the architecture, here's the auth implementation..."
```

### Use Case 3: File Organization

**Scenario:** Organize downloaded files.

```bash
# Setup
{
  "args": [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    "/Users/me/Downloads",
    "/Users/me/Documents/sorted"
  ]
}

# Usage
You: "List all PDF files in my Downloads"
Claude: "Found these PDFs: [list]"

You: "Move all PDFs to ~/Documents/sorted/pdfs/"
Claude: "I've moved the PDFs..."
```

### Use Case 4: Template Library

**Scenario:** Maintain a library of code templates.

```bash
# Setup
{
  "args": [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    "/Users/me/projects/current",
    "/Users/me/templates"
  ]
}

# Usage
You: "Show me the React component template from ~/templates/"
Claude: "Here's the template: ..."

You: "Create a new UserProfile component based on that template"
Claude: "I've created UserProfile.jsx..."
```

## Tips for Effective Use

### 1. Organize Your Allowed Paths

```
~/allowed-claude/
├── projects/
│   ├── frontend/
│   ├── backend/
│   └── shared/
├── docs/
│   ├── specs/
│   └── guides/
├── templates/
│   ├── components/
│   └── configs/
└── temp/
    └── working/
```

Then allow just `~/allowed-claude/` in config.

### 2. Use Absolute Paths

```bash
# ✅ Good
"Read /Users/alice/Documents/file.txt"

# ❌ Confusing
"Read file.txt"  # Which file.txt?
```

### 3. Be Explicit

```bash
# ✅ Clear
"Create /Users/me/temp/output.json with this data"

# ❌ Ambiguous
"Save this somewhere"
```

### 4. Regular Cleanup

```bash
# Periodically clean temp folders
"Delete all files in ~/temp/working/ older than 7 days"
```

## Best Practices

✅ **Do:**
- Allow specific directories only
- Use absolute paths
- Regularly review allowed paths
- Keep sensitive files elsewhere
- Document why paths are allowed
- Test with non-critical files first

❌ **Don't:**
- Allow your entire home directory
- Give access to system folders
- Allow `.ssh`, `.aws`, etc.
- Store passwords in allowed folders
- Allow more than you need
- Forget what you've allowed

## Common Patterns

### Pattern 1: Sandbox Directory

Create a dedicated directory for Claude:

```bash
mkdir ~/claude-workspace
```

```json
{
  "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/me/claude-workspace"]
}
```

Benefits:
- ✅ Clear boundary
- ✅ Easy to review
- ✅ Simple cleanup
- ✅ No sensitive data

### Pattern 2: Project Groups

Group related projects:

```bash
~/work/
├── project-a/
├── project-b/
└── shared/
```

```json
{
  "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/me/work"]
}
```

### Pattern 3: Read-Only Resources

Keep templates and references separate:

```bash
~/claude-readonly/  # Documentation, templates
~/claude-writable/  # Work files, outputs
```

## Troubleshooting

### Issue: "Permission denied"

**Cause:** Server not allowed to access that path.

**Solution:**
1. Check path is in allowed list in `.mcp.json`
2. Check file permissions: `ls -la /path/to/file`
3. Ensure no typos in path

### Issue: "File not found"

**Cause:** Incorrect path or file doesn't exist.

**Solution:**
```bash
# Verify path
ls -la /full/path/to/file

# Check spelling
# Use tab completion when writing paths
```

### Issue: "Server not starting"

**Cause:** Invalid arguments or path doesn't exist.

**Solution:**
```bash
# Test paths exist
ls /Users/me/Documents

# Check .mcp.json syntax
cat .mcp.json | jq .

# Test server directly
npx -y @modelcontextprotocol/server-filesystem /tmp
```

### Issue: "Can't write files"

**Cause:** Directory not writable or not allowed.

**Solution:**
1. Check directory permissions
2. Ensure directory exists
3. Verify path in allowed list
4. Check disk space

## Advanced Usage

### Multiple Filesystem Servers

You can run multiple instances for different purposes:

```json
{
  "mcpServers": {
    "filesystem-docs": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/me/docs"]
    },
    "filesystem-projects": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/me/projects"]
    },
    "filesystem-temp": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]
    }
  }
}
```

Benefits:
- Clear separation of concerns
- Easier to enable/disable
- Better organization

### Environment Variables for Paths

Use environment variables for flexibility:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "${HOME}/projects",
        "${HOME}/Documents"
      ]
    }
  }
}
```

### Combining with Other Servers

Filesystem works great with other MCP servers:

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
    }
  }
}
```

Use together:
```bash
"Read the spec from ~/docs/api-spec.yaml and remember the key points"
```

## Real-World Examples

### Example 1: Blog Writer

```json
{
  "filesystem": {
    "args": [
      "-y",
      "@modelcontextprotocol/server-filesystem",
      "/Users/me/blog/content",
      "/Users/me/blog/images"
    ]
  }
}
```

Usage:
```bash
"Create a new blog post at ~/blog/content/2024-11-01-topic.md"
"List all blog posts from October"
"Copy image from Downloads to ~/blog/images/"
```

### Example 2: Polyglot Developer

```json
{
  "filesystem": {
    "args": [
      "-y",
      "@modelcontextprotocol/server-filesystem",
      "/Users/me/projects/backend-go",
      "/Users/me/projects/frontend-react",
      "/Users/me/projects/mobile-flutter"
    ]
  }
}
```

Usage:
```bash
"Read the API types from the Go backend"
"Generate TypeScript interfaces for the React frontend"
"Create Flutter models for the mobile app"
```

### Example 3: Configuration Manager

```json
{
  "filesystem": {
    "args": [
      "-y",
      "@modelcontextprotocol/server-filesystem",
      "/Users/me/dotfiles",
      "/Users/me/projects/current"
    ]
  }
}
```

Usage:
```bash
"Copy my standard .eslintrc from ~/dotfiles/"
"Update .gitignore based on my template"
"Sync editor config across projects"
```

## FAQ

**Q: Can I use wildcards in paths?**
A: No, you must specify exact directory paths.

**Q: Can Claude access subdirectories?**
A: Yes, allowing a directory allows all subdirectories too.

**Q: Is there a file size limit?**
A: Check MCP server documentation, but generally handle files up to several MB.

**Q: Can I allow network drives?**
A: Yes, if mounted locally and accessible via path.

**Q: Does this work on Windows?**
A: Yes! Use Windows paths: `C:\\Users\\YourName\\Documents`

**Q: Can I revoke access without restarting?**
A: Remove from `.mcp.json` and restart Claude Code.

## Security Checklist

Before allowing a directory, ask:

- [ ] Does this directory contain sensitive data?
- [ ] Are there credentials or keys here?
- [ ] Could Claude accidentally delete important files?
- [ ] Is this the minimum access needed?
- [ ] Have I documented why this path is allowed?
- [ ] Would I be okay if this was publicly readable?

If any answer is concerning, reconsider.

## Next Steps

1. ✅ **Test with safe directory** - Try /tmp first
2. ✅ **Add useful paths** - Documents, projects, etc.
3. ✅ **Try cross-project work** - Reference between projects
4. ✅ **Move to next example** - Try github-server next

## Related Examples

- **memory-server** - Remember information
- **github-server** - Access GitHub repositories
- **sqlite-server** - Access databases

---

**Remember:** With great filesystem access comes great responsibility. Be careful what directories you allow! 🔒
