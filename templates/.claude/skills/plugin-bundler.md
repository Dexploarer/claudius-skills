---
name: plugin-bundler
description: Bundle multiple skills, commands, and agents from different sources into a cohesive plugin package
---

# Plugin Bundler Skill

## Purpose
Combine multiple skills, commands, agents, and hooks from different locations into a single, cohesive plugin package with proper manifest and documentation.

## Activation
Activate when the user requests to:
- "bundle these skills into a plugin"
- "combine multiple components into a plugin"
- "create plugin from multiple sources"
- "package these together as a plugin"
- "merge components into one plugin"

## Instructions

### Step 1: Identify Components to Bundle
Ask user to specify components:
1. Skills (from any .claude/skills/ directory)
2. Commands (from any .claude/commands/ directory)
3. Agents (from any .claude/agents/ directory)
4. Hooks (from any .claude/hooks/ directory)
5. Rules (custom configuration)

Accept:
- File paths (relative or absolute)
- Directory paths (bundle all from directory)
- Glob patterns (e.g., "skills/api-*.md")
- Plugin names (from existing plugins)

### Step 2: Gather Plugin Information
Request from user:
1. **Plugin name** (suggest based on component themes)
2. **Display name**
3. **Description** (auto-generate from components or ask)
4. **Category**
5. **Version** (default: 1.0.0)
6. **Theme/Purpose** (to ensure cohesion)

### Step 3: Analyze Component Compatibility
Check for:
1. Conflicting component names
2. Dependencies between components
3. Shared configuration requirements
4. Compatible frameworks/tools
5. Licensing compatibility

Warn user of potential conflicts.

### Step 4: Create Bundled Plugin Structure
```
[bundle-name]/
├── .claude/
│   ├── skills/           # All bundled skills
│   ├── commands/         # All bundled commands
│   ├── agents/           # All bundled agents
│   ├── hooks/            # All bundled hooks
│   └── rules/
│       └── CLAUDE.md     # Combined rules
├── .claude-plugin-manifest.json
└── README.md
```

### Step 5: Copy and Organize Components
For each component:
1. Copy to appropriate directory
2. Resolve naming conflicts (ask user for rename if needed)
3. Update internal references
4. Preserve original metadata
5. Track source attribution

### Step 6: Generate Combined Manifest
Create comprehensive manifest:
```json
{
  "name": "bundle-name",
  "displayName": "Bundle Display Name",
  "description": "Combined functionality description",
  "version": "1.0.0",
  "author": {
    "name": "Bundle Creator",
    "email": "creator@example.com"
  },
  "contributors": [
    "Original skill author 1",
    "Original skill author 2"
  ],
  "license": "MIT",
  "tags": ["bundled", "multi-source", "..."],
  "category": "category-name",
  "components": {
    "skills": [
      {
        "name": "skill-1",
        "file": ".claude/skills/skill-1.md",
        "description": "...",
        "source": "plugin-a"
      },
      {
        "name": "skill-2",
        "file": ".claude/skills/skill-2.md",
        "description": "...",
        "source": "plugin-b"
      }
    ],
    "commands": [...],
    "agents": [...],
    "hooks": [...]
  },
  "stats": {
    "skills": 5,
    "commands": 8,
    "agents": 3,
    "hooks": 2
  },
  "bundleInfo": {
    "sources": ["plugin-a", "plugin-b", "custom-skills"],
    "bundledAt": "2025-11-05",
    "purpose": "Specialized workflow bundle"
  }
}
```

### Step 7: Merge Configuration Rules
If multiple sources have rules:
1. Combine into single CLAUDE.md
2. Resolve conflicts (ask user for priority)
3. Organize by section
4. Add source attribution
5. Create coherent narrative

### Step 8: Generate Unified Documentation
Create README.md:
```markdown
# [Bundle Display Name]

> [Description of bundled functionality]

## Bundled Components
This plugin combines components from multiple sources:
- X skills (from plugin-a, plugin-b)
- Y commands (from plugin-c)
- Z agents (from custom)

## Features
[Combined feature list]

## Installation
\`\`\`bash
/plugin install [bundle-name]
\`\`\`

## Usage
### Skills
[Document each skill]

### Commands
[Document each command]

### Agents
[Document each agent]

## Attribution
This bundle includes components from:
- Plugin A (MIT License)
- Plugin B (MIT License)
- Custom Skills by User

## License
MIT (compatible with all source licenses)
```

### Step 9: Validate Bundle
Check:
1. No file name conflicts
2. All references resolve correctly
3. Compatible dependencies
4. License compatibility
5. JSON manifest is valid
6. Stats match actual counts
7. All files copied successfully

### Step 10: Optimize and Clean
1. Remove duplicate dependencies
2. Consolidate similar components if user approves
3. Optimize file structure
4. Remove unused files
5. Update cross-references

### Step 11: Test Bundle
Recommend user to:
1. Test installation in clean project
2. Verify all skills activate
3. Check command availability
4. Test agent functionality
5. Verify hooks trigger correctly

## Output Format
Present to user:
1. Bundle structure tree
2. Component sources map
3. Conflict resolutions (if any)
4. Total statistics
5. Installation instructions
6. Attribution summary

## Example Interaction
```
User: "Bundle my api-generator skill with the testing-helper from intermediate-kit and the api-designer agent"

Claude: I'll create a bundle from these components:

Sources identified:
1. api-generator.md (from ./skills/)
2. testing-helper.md (from intermediate-kit/.claude/skills/)
3. api-designer.md (from ./agents/)

What should we name this bundle?

User: "api-dev-suite"

Claude: Creating API Dev Suite bundle...

Copying components:
✓ api-generator skill
✓ testing-helper skill
✓ api-designer agent

Creating manifest...
Generating documentation...

✅ Bundle created: api-dev-suite
   - 2 skills
   - 1 agent
   - Cohesive API development workflow

Install with:
/plugin install api-dev-suite
```

## Best Practices
- Verify license compatibility before bundling
- Preserve original author attribution
- Check for component conflicts
- Test bundle before finalizing
- Document component sources clearly
- Use semantic versioning
- Maintain update path for source components
- Ask user to resolve conflicts rather than assuming
- Create cohesive documentation
- Tag as "bundled" for transparency

## Conflict Resolution Strategies
1. **Name conflicts**: Rename with prefix (e.g., "api-skill" vs "db-skill")
2. **Configuration conflicts**: Ask user for priority
3. **Dependency conflicts**: Use most recent compatible version
4. **License conflicts**: Warn user, suggest compatible alternatives
5. **Version conflicts**: Bundle latest stable versions

## Notes
- Always attribute original authors
- Check license compatibility
- Test thoroughly before publishing
- Document bundle composition clearly
- Version as 1.0.0 for first bundle
- Add "bundled-from" metadata
- Keep bundle focused and coherent
- Update strategy for source changes
