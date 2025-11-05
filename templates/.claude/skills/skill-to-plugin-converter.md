---
name: skill-to-plugin-converter
description: Convert existing Claude Code skills, commands, or agents into installable plugins with proper manifest and marketplace structure
---

# Skill to Plugin Converter

## Purpose
Convert standalone skills, commands, or agents into proper Claude Code plugins with manifests, documentation, and marketplace-ready structure.

## Activation
Activate when the user requests to:
- "convert this skill to a plugin"
- "make a plugin from [skill/command/agent]"
- "package this as a plugin"
- "turn my skill into a plugin"
- "create plugin from existing components"

## Instructions

### Step 1: Identify Source Components
Scan for existing components:
1. Skills in `.claude/skills/`
2. Commands in `.claude/commands/`
3. Agents in `.claude/agents/`
4. Hooks in `.claude/hooks/`
5. Rules in `.claude/rules/`

Ask user which components to include in the plugin.

### Step 2: Gather Plugin Metadata
Request from user:
1. **Plugin name** (suggest based on main skill name)
2. **Display name** (human-readable title)
3. **Description** (summarize functionality)
4. **Category** (beginner/intermediate/advanced/specialized/productivity/enhancement)
5. **Tags** (suggest based on functionality)
6. **Author information**

### Step 3: Create Plugin Directory Structure
```
[plugin-name]/
├── .claude/
│   ├── skills/          # Copy selected skills
│   ├── commands/        # Copy selected commands
│   ├── agents/          # Copy selected agents
│   ├── hooks/           # Copy selected hooks
│   └── rules/           # Copy or create CLAUDE.md
├── .claude-plugin-manifest.json
└── README.md
```

### Step 4: Copy Components
For each selected component:
1. Copy file to new plugin directory
2. Preserve original structure
3. Update any internal references if needed
4. Add to manifest components list

### Step 5: Generate Plugin Manifest
Create `.claude-plugin-manifest.json`:
```json
{
  "name": "plugin-name",
  "displayName": "Display Name",
  "description": "Description from components",
  "version": "1.0.0",
  "author": {
    "name": "Author Name",
    "email": "author@example.com"
  },
  "license": "MIT",
  "tags": ["auto-generated", "from-components"],
  "category": "category-name",
  "components": {
    "skills": [
      {
        "name": "skill-name",
        "file": ".claude/skills/skill-name.md",
        "description": "Extracted from skill frontmatter"
      }
    ],
    "commands": [...],
    "agents": [...],
    "hooks": [...]
  },
  "stats": {
    "skills": 1,
    "commands": 0,
    "agents": 0,
    "hooks": 0
  }
}
```

### Step 6: Auto-Extract Metadata
From each component file:
- **Skills**: Extract name and description from frontmatter
- **Commands**: Extract command name from markdown header
- **Agents**: Extract agent name and expertise
- **Hooks**: Extract hook type and trigger conditions

### Step 7: Generate README
Create comprehensive README.md:
```markdown
# [Plugin Display Name]

> [Auto-generated description from components]

## Components
- X skills
- Y commands
- Z agents

## Features
[List extracted from component descriptions]

## Installation
\`\`\`bash
/plugin install [plugin-name]
\`\`\`

## Usage
[Auto-generated from component documentation]

## License
MIT
```

### Step 8: Verify Plugin Structure
Check:
1. All referenced files exist
2. Manifest JSON is valid
3. Stats match actual component count
4. No broken internal references

### Step 9: Offer Marketplace Integration
Ask if user wants to:
1. Add to Claudius Skills marketplace
2. Create own marketplace
3. Keep as standalone plugin

## Output Format
Show user:
1. Plugin structure tree
2. Components included
3. Manifest summary
4. Installation command
5. Next steps

## Example Interaction
```
User: "Convert my api-generator skill to a plugin"

Claude: I found the following in your .claude/ directory:
- skills/api-generator.md
- commands/generate-api.md
- agents/api-designer.md

Would you like to include all of these in the plugin? (yes/no/select)

User: "yes"

Claude: Creating plugin from components...

✅ Plugin created: api-generator
   - 1 skill (api-generator)
   - 1 command (/generate-api)
   - 1 agent (api-designer)

Install with:
/plugin install api-generator
```

## Best Practices
- Preserve original component structure
- Extract metadata automatically when possible
- Validate all JSON before writing
- Create comprehensive documentation
- Suggest meaningful plugin names
- Auto-detect dependencies between components
- Version as 1.0.0 for first conversion
- Include original author attribution
- Add "converted-from-components" tag

## Notes
- Ask before overwriting existing files
- Validate component references
- Check for external dependencies
- Preserve custom configurations
- Maintain backward compatibility
