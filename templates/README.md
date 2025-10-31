# Templates

Ready-to-use templates for creating your own Claude Code configurations.

## Available Templates

### 1. Skill Template
**File:** `skill-template.md`

Use this to create new skills. Includes:
- YAML frontmatter structure
- Instructions section
- Examples section
- Best practices
- Documentation guidelines

**Usage:**
```bash
cp templates/skill-template.md .claude/skills/my-skill.md
# Edit the file and customize for your needs
```

### 2. Slash Command Template
**File:** `command-template.md`

Use this to create new slash commands. Includes:
- Argument handling
- Step-by-step instructions
- Usage examples
- Output formatting

**Usage:**
```bash
cp templates/command-template.md .claude/commands/mycommand.md
# Edit the file and customize for your needs
```

### 3. Subagent Template
**File:** `subagent-template.md`

Use this to create new subagents. Includes:
- YAML frontmatter with tool restrictions
- Role definition
- Process guidelines
- Output format
- Examples

**Usage:**
```bash
cp templates/subagent-template.md .claude/agents/my-agent.md
# Edit the file and customize for your needs
```

### 4. Hooks Configuration
**File:** `hooks-template.json`

Use this to configure hooks. Includes:
- All event types
- Pattern matching examples
- Exit code handling
- Security considerations

**Usage:**
```bash
# Copy to your project's .claude directory
cp templates/hooks-template.json .claude/settings.json
# Edit and add your hooks
```

### 5. MCP Configuration
**File:** `mcp-template.json`

Use this to configure MCP servers. Includes:
- Common MCP server examples
- Security notes
- Environment variable setup
- Multiple server configuration

**Usage:**
```bash
# Copy to your project root
cp templates/mcp-template.json .mcp.json
# Add your credentials
# NEVER commit .mcp.json with real credentials!
```

## Quick Start

### Creating a New Skill

1. Copy the template:
   ```bash
   cp templates/skill-template.md .claude/skills/awesome-skill.md
   ```

2. Edit the YAML frontmatter:
   ```yaml
   ---
   name: awesome-skill
   description: Does awesome things when you ask for awesomeness
   ---
   ```

3. Fill in the instructions:
   - What the skill does
   - When to use it
   - Step-by-step process
   - Examples

4. Test it:
   ```bash
   claude
   # Ask something that matches the description
   ```

### Creating a New Command

1. Copy the template:
   ```bash
   cp templates/command-template.md .claude/commands/awesome.md
   ```

2. Write the instructions:
   ```markdown
   Do something awesome with: $ARGUMENTS

   1. First step...
   2. Second step...
   ```

3. Use it:
   ```bash
   /awesome some input here
   ```

### Creating a New Subagent

1. Copy the template:
   ```bash
   cp templates/subagent-template.md .claude/agents/awesome-expert.md
   ```

2. Define the role:
   ```yaml
   ---
   name: awesome-expert
   description: Expert in all things awesome
   allowed-tools: [Read, Grep, Glob]
   ---

   You are an expert in awesomeness...
   ```

3. Call it:
   ```bash
   # In Claude Code:
   "Use the awesome-expert subagent to review this code"
   ```

## Tips for Creating Great Configurations

### Skills
- ✅ Make the description very specific
- ✅ Include clear examples
- ✅ Test with different phrasings
- ✅ Keep it focused on one thing

### Commands
- ✅ Keep them simple and focused
- ✅ Use descriptive names
- ✅ Document what arguments do
- ✅ Test with various inputs

### Subagents
- ✅ Give them clear expertise boundaries
- ✅ Restrict tools appropriately
- ✅ Provide structured output formats
- ✅ Include decision-making guidelines

### Hooks
- ✅ Test commands separately first
- ✅ Use appropriate exit codes
- ✅ Add timeouts for long operations
- ✅ Document what each hook does

### MCP Servers
- ✅ Use environment variables for secrets
- ✅ Never commit credentials
- ✅ Test connections before use
- ✅ Use read-only access when possible

## Best Practices

1. **Start Simple**: Begin with basic functionality, add complexity later
2. **Document Everything**: Future you will thank you
3. **Test Thoroughly**: Try edge cases and error conditions
4. **Be Consistent**: Follow naming conventions
5. **Share Knowledge**: Contribute useful configurations back

## Common Patterns

### Skill with Multiple Capabilities
```yaml
---
name: multi-skill
description: Handles X, Y, and Z tasks when working with [domain]
---

# Choose the right approach based on the task:

## For X tasks:
[Instructions for X]

## For Y tasks:
[Instructions for Y]

## For Z tasks:
[Instructions for Z]
```

### Command with Options
```markdown
Handle different actions based on first argument:

If $1 is "create":
  - Do creation steps

If $1 is "update":
  - Do update steps

If $1 is "delete":
  - Do deletion steps
  - Ask for confirmation first!
```

### Subagent with Structured Output
```markdown
Always output in this format:

## Analysis

[Your analysis]

## Findings

- Finding 1
- Finding 2

## Recommendations

1. Recommendation 1
2. Recommendation 2
```

## Examples

See the `starter-kit/` directory for complete, working examples of all configuration types.

## Need Help?

- Check the starter kit for working examples
- Read the main README.md
- Look at examples in the examples/ directory
- Ask in GitHub Discussions
