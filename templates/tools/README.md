# Template Generator Tools

Interactive tools to help you generate Claude Code configurations quickly and easily.

## Available Tools

### 1. Bash Script Generator (`template-generator.sh`)

An interactive command-line tool for generating Claude Code templates.

#### Features

- ✅ Interactive menu-driven interface
- ✅ Colorized output for better readability
- ✅ Automatic file generation with placeholders replaced
- ✅ Support for all template types
- ✅ Input validation and error handling

#### Usage

```bash
# Make the script executable
chmod +x templates/tools/template-generator.sh

# Run the generator
./templates/tools/template-generator.sh

# Or set a custom target directory
TARGET_DIR=".claude" ./templates/tools/template-generator.sh
```

#### What It Can Generate

1. **Skills** - Beginner, Intermediate, or Advanced
2. **Commands** - Basic or Workflow
3. **Subagents** - Analyzer, Generator, or Domain Expert
4. **Hooks** - Links to template files
5. **MCP Configuration** - Links to template files
6. **Complete Setups** - Links to setup directories
7. **Language Services** - Go, Rust, PHP (via Claude Code)
8. **GitHub Workflows** - CI/CD, deployment, security (via Claude Code)

#### Example Session

```
╔══════════════════════════════════════════════════════════╗
║   Claude Code Interactive Template Generator            ║
╚══════════════════════════════════════════════════════════╝

What would you like to create?

  1) Skill
  2) Command
  3) Subagent
  4) Hook
  5) MCP Configuration
  6) Complete Setup
  7) Language-Specific Service
  8) GitHub Workflow
  9) Exit

? Select option: 1

═══ Creating New Skill ═══

Select skill level:
  1) Beginner (simple, focused)
  2) Intermediate (framework-specific)
  3) Advanced (full-stack)
  4) Cancel

? Skill level: 1
? Skill name (kebab-case): json-formatter
? Description (when should this activate?): Format JSON files when user says "format JSON" or "prettify JSON"
? Allowed tools (Read, Edit): Read, Edit

✓ Created skill: .claude/skills/json-formatter.md

📝 Next steps:
  1. Edit .claude/skills/json-formatter.md to customize the skill
  2. Add your specific instructions and examples
  3. Test with: claude
```

### 2. Interactive Template Skill (`interactive-template-skill.md`)

A Claude Code skill that provides guided template generation within Claude Code itself.

#### Installation

```bash
# Copy to your .claude/skills directory
cp templates/tools/interactive-template-skill.md .claude/skills/
```

#### Usage

Start Claude Code and use any of these phrases:

```
"generate a template"
"create a new skill"
"create a new command"
"create a new subagent"
"help me set up a Claude Code configuration"
"what template should I use?"
```

Claude will then guide you through an interactive process to:
1. Identify what you need
2. Gather requirements
3. Generate the configuration
4. Provide next steps and customization help

#### Features

- ✅ Conversational interface
- ✅ Context-aware questions based on template type
- ✅ Automatic file generation
- ✅ Customization assistance
- ✅ Usage examples and tips

#### Example Conversation

```
You: "I want to create a skill for formatting JSON files"

Claude: Great! I'll help you create a JSON formatting skill.

What complexity level would you like?
- **Beginner**: Simple, focused task (recommended for formatters)
- **Intermediate**: Framework-specific with multiple files
- **Advanced**: Full-stack with complex logic

You: "Beginner"

Claude: Perfect! A few more questions:

1. What should the skill be called? (use kebab-case, e.g., json-formatter)
2. When should it activate? (e.g., "when user asks to format JSON")
3. Which tools does it need? (For formatting, you'll likely need Read and Edit)

[Continue conversation...]
```

## Comparison: Bash Script vs. Skill

| Feature | Bash Script | Skill |
|---------|-------------|-------|
| **Interface** | Terminal menu | Conversational |
| **Availability** | Run outside Claude | Inside Claude Code |
| **Customization** | Basic replacement | Guided assistance |
| **File Preview** | No | Yes (can read generated files) |
| **Follow-up Help** | Limited | Full assistance |
| **Best For** | Quick generation | Learning + customization |

## Quick Start Guide

### Generate Your First Skill

**Method 1: Using Bash Script**

```bash
./templates/tools/template-generator.sh
# Select: 1 (Skill)
# Select: 1 (Beginner)
# Enter: my-first-skill
# Enter: Description
# Enter: Read, Edit
```

**Method 2: Using Skill in Claude Code**

```bash
# Copy the skill
cp templates/tools/interactive-template-skill.md .claude/skills/

# Start Claude Code
claude

# Say:
"create a new skill"

# Follow Claude's guidance
```

### Generate Your First Command

**Method 1: Using Bash Script**

```bash
./templates/tools/template-generator.sh
# Select: 2 (Command)
# Select: 1 (Basic)
# Enter: my-command
# Enter: Description
```

**Method 2: Using Skill in Claude Code**

```
"create a new command for deploying to staging"
```

### Generate a Language Service

**Method 1: Using Bash Script**

```bash
./templates/tools/template-generator.sh
# Select: 7 (Language-Specific Service)
# Select: 1 (Go) / 2 (Rust) / 3 (PHP)
# Enter: service-name
# Enter: resource (e.g., users)
# Follow displayed instructions
```

**Method 2: Using Skill in Claude Code**

```
"Generate a Go service for managing products"
"Generate a Rust service for user authentication"
"Generate a PHP Laravel service for orders"
```

## Advanced Usage

### Custom Target Directory

By default, files are generated in `.claude/`. To use a different directory:

```bash
TARGET_DIR="custom-claude-dir" ./templates/tools/template-generator.sh
```

### Batch Generation

Create a script to generate multiple templates:

```bash
#!/bin/bash

# Generate multiple skills
for skill in "json-formatter" "yaml-validator" "code-minifier"; do
    # Use expect or similar for automated input
    echo "Generating $skill..."
done
```

### Template Customization After Generation

All generated files are markdown with YAML frontmatter. You can:

1. **Manually edit** the generated file
2. **Ask Claude** for customization help (if using the skill)
3. **Use the templates as examples** for your own variations

## Templates Directory Structure

```
templates/
├── skills/
│   ├── beginner-skill-template.md
│   ├── intermediate-skill-template.md
│   └── advanced-skill-template.md
├── commands/
│   ├── basic-command-template.md
│   └── workflow-command-template.md
├── subagents/
│   ├── analyzer-subagent-template.md
│   ├── generator-subagent-template.md
│   └── domain-expert-template.md
├── hooks/
│   ├── safety-hook-template.json
│   ├── workflow-hook-template.json
│   └── quality-enforcement-template.json
├── mcp/
│   ├── basic-mcp-template.json
│   ├── multi-service-template.json
│   └── production-template.json
├── languages/
│   ├── go/
│   │   └── go-service-generator.md
│   ├── rust/
│   │   └── rust-service-generator.md
│   └── php/
│       └── php-service-generator.md
├── github/
│   └── github-workflow-generator.md
└── tools/
    ├── template-generator.sh          # This tool
    ├── interactive-template-skill.md   # This skill
    └── README.md                       # This file
```

## Best Practices

### When to Use Which Tool

**Use Bash Script When:**
- You want quick template generation
- You know exactly what you need
- You're comfortable with terminal interfaces
- You want to generate multiple templates quickly

**Use Interactive Skill When:**
- You're learning Claude Code
- You want guidance on which template to use
- You need help customizing after generation
- You want to see examples before committing

### Template Selection Guide

**Skill Levels:**
- **Beginner**: < 100 lines, single file operations, simple logic
- **Intermediate**: 100-500 lines, multiple files, framework integration
- **Advanced**: 500+ lines, full architecture, complex workflows

**Command Types:**
- **Basic**: < 5 steps, no rollback needed, < 5 min execution
- **Workflow**: 5+ steps, needs rollback, complex validation

**Subagent Roles:**
- **Analyzer**: Read-only operations, reporting, analysis
- **Generator**: Create files, generate code
- **Domain Expert**: Specialized knowledge application

## Troubleshooting

### Script Won't Run

```bash
# Make sure it's executable
chmod +x templates/tools/template-generator.sh

# Check shebang line
head -1 templates/tools/template-generator.sh
# Should output: #!/bin/bash
```

### Generated File Has Wrong Permissions

```bash
# Fix permissions on generated files
chmod 644 .claude/skills/*.md
chmod 644 .claude/commands/*.md
```

### Template Not Activating

1. **Check file location**: Must be in `.claude/skills/`, `.claude/commands/`, or `.claude/agents/`
2. **Check frontmatter**: Must have valid YAML with name and description
3. **Restart Claude**: Some changes require restart
4. **Check description**: Must match user's phrasing

### Skill Tool Not Found

```bash
# Ensure skill is in the right place
ls -la .claude/skills/interactive-template-skill.md

# Restart Claude Code
claude
```

## Examples

### Example 1: Generate JSON Formatter Skill

```bash
./templates/tools/template-generator.sh

# Select: 1 (Skill)
# Select: 1 (Beginner)
# Name: json-formatter
# Description: Format and prettify JSON files when user asks
# Tools: Read, Edit

# Result: .claude/skills/json-formatter.md created
```

### Example 2: Generate Deployment Command

```bash
./templates/tools/template-generator.sh

# Select: 2 (Command)
# Select: 2 (Workflow)
# Name: deploy
# Description: Deploy application to production with validation

# Result: .claude/commands/deploy.md created
# Usage: /deploy --env production
```

### Example 3: Generate Code Reviewer Subagent

```bash
./templates/tools/template-generator.sh

# Select: 3 (Subagent)
# Select: 1 (Analyzer)
# Name: code-reviewer
# Description: Review code for quality and security

# Result: .claude/agents/code-reviewer.md created
# Usage: "use the code-reviewer subagent to review my PR"
```

## Contributing

Found a useful template pattern? Share it!

1. Create your template in the appropriate directory
2. Add documentation in the template
3. Update this README with usage examples
4. Submit a PR

## Resources

- [Claude Code Documentation](https://docs.claude.com/claude-code/)
- [Templates Guide](../TEMPLATES_GUIDE.md)
- [Template Catalog](../TEMPLATE_CATALOG.md)
- [Complete Setups](../complete-setups/README.md)

---

**Happy template generating!** 🎉

If you have questions or need help, ask Claude:
```
"How do I use the template generator?"
"What template should I use for [use case]?"
"Help me customize my generated template"
```
