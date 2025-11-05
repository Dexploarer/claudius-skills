---
name: plugin-generator
description: Generate complete Claude Code plugins from scratch with skills, commands, agents, and marketplace-ready structure
---

# Plugin Generator Skill

## Purpose
Generate complete, production-ready Claude Code plugins with all necessary components including skills, commands, agents, plugin manifest, and marketplace entry.

## Activation
Activate when the user requests to:
- "create a new plugin"
- "generate a Claude Code plugin"
- "build a plugin for [specific purpose]"
- "make a plugin that [functionality]"
- "scaffold a new plugin"

## Instructions

### Step 1: Gather Plugin Requirements
Ask the user to provide:
1. **Plugin name** (kebab-case, e.g., "my-awesome-plugin")
2. **Display name** (human-readable, e.g., "My Awesome Plugin")
3. **Description** (one-line summary)
4. **Category** (beginner, intermediate, advanced, specialized, productivity, enhancement)
5. **Purpose** (what problem does it solve?)
6. **Components needed**:
   - Skills (how many and what they do)
   - Commands (slash commands needed)
   - Agents (specialized AI assistants)
   - Hooks (event-driven automation)

### Step 2: Create Plugin Directory Structure
```
[plugin-name]/
├── .claude/
│   ├── skills/
│   ├── commands/
│   ├── agents/
│   ├── hooks/
│   └── rules/
│       └── CLAUDE.md
├── .claude-plugin-manifest.json
└── README.md
```

### Step 3: Generate Plugin Manifest
Create `.claude-plugin-manifest.json` with:
```json
{
  "name": "plugin-name",
  "displayName": "Display Name",
  "description": "Plugin description",
  "version": "1.0.0",
  "author": {
    "name": "Author Name",
    "email": "author@example.com"
  },
  "license": "MIT",
  "tags": ["tag1", "tag2"],
  "category": "category-name",
  "components": {
    "skills": [],
    "commands": [],
    "agents": [],
    "hooks": []
  },
  "stats": {
    "skills": 0,
    "commands": 0,
    "agents": 0,
    "hooks": 0
  },
  "requirements": {
    "claudeCode": ">=2.0.0"
  },
  "bestFor": [
    "Use case 1",
    "Use case 2"
  ],
  "installation": {
    "auto": true,
    "steps": [
      "Installation steps"
    ]
  }
}
```

### Step 4: Generate Skills
For each skill the user requested:
1. Create markdown file in `.claude/skills/`
2. Use skill template format:
```markdown
---
name: skill-name
description: Brief description
---

# Skill Name

## Purpose
What this skill does

## Activation
When to activate (phrases, patterns, contexts)

## Instructions
Detailed step-by-step instructions for Claude Code

## Examples
Usage examples and expected outcomes
```

### Step 5: Generate Commands
For each command:
1. Create markdown file in `.claude/commands/`
2. Use command template format:
```markdown
# Command Name

## Description
What this command does

## Usage
/command-name [arguments]

## Parameters
- param1: Description
- param2: Description

## Implementation
How to execute this command

## Examples
- Example 1
- Example 2
```

### Step 6: Generate Agents
For each agent:
1. Create markdown file in `.claude/agents/`
2. Use agent template format:
```markdown
# Agent Name

## Expertise
Domain of expertise and specialization

## When to Use
Situations where this agent should be activated

## Capabilities
- Capability 1
- Capability 2
- Capability 3

## Workflow
How this agent operates:
1. Step 1
2. Step 2
3. Step 3

## Examples
Usage examples and expected outcomes
```

### Step 7: Generate Hooks (if needed)
For each hook:
1. Create JSON or shell script in `.claude/hooks/`
2. Include proper configuration and triggering conditions

### Step 8: Create Documentation
Generate comprehensive `README.md`:
```markdown
# [Plugin Display Name]

> [Description]

## Features
- Feature 1
- Feature 2
- Feature 3

## Installation

### Via Claudius Skills Marketplace
\`\`\`bash
/plugin marketplace add Dexploarer/claudius-skills
/plugin install [plugin-name]
\`\`\`

### Manual Installation
\`\`\`bash
cp -r [plugin-name]/.claude /your/project/
\`\`\`

## Usage
[Usage instructions]

## Components
- X skills
- Y commands
- Z agents

## License
MIT
```

### Step 9: Add to Marketplace (Optional)
If this is for the Claudius Skills marketplace:
1. Add entry to `.claude-plugin/marketplace.json`
2. Include all metadata (name, description, category, tags, stats)

### Step 10: Verify and Test
1. Check all files are created
2. Verify manifest is valid JSON
3. Ensure all components are referenced correctly
4. Test installation in a sample project

## Output Format
Present to the user:
1. Summary of what was created
2. File tree showing structure
3. Installation instructions
4. Next steps for customization

## Best Practices
- Use kebab-case for all file names
- Include comprehensive descriptions
- Add multiple activation phrases for skills
- Document all parameters for commands
- Include examples in every component
- Keep manifests up-to-date with actual components
- Follow semantic versioning (1.0.0)
- Include license information
- Add appropriate tags for discoverability

## Example Interaction
```
User: "Create a plugin for managing Docker containers"

Claude: I'll create a Docker management plugin for you. Let me gather some details:

1. Plugin name: docker-manager
2. Display name: Docker Manager
3. Description: Comprehensive Docker container management with deployment automation
4. Category: specialized
5. Components needed:
   - 3 skills (dockerfile-generator, compose-orchestrator, container-debugger)
   - 5 commands (/docker-build, /docker-deploy, /docker-logs, /docker-clean, /docker-optimize)
   - 2 agents (docker-architect, deployment-specialist)

Creating plugin structure...
[Creates all files]

✅ Plugin created successfully!
```

## Notes
- Always validate JSON syntax in manifest files
- Include version number in manifest (start with 1.0.0)
- Add comprehensive tags for marketplace discoverability
- Test installation before finalizing
- Document dependencies if any
- Include upgrade/migration path if applicable
