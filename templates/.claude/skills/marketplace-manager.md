---
name: marketplace-manager
description: Manage Claude Code plugin marketplace entries including adding, updating, and organizing plugins in marketplace.json
---

# Marketplace Manager Skill

## Purpose
Manage plugin marketplace entries in the `.claude-plugin/marketplace.json` file including adding new plugins, updating existing entries, organizing categories, and maintaining marketplace metadata.

## Activation
Activate when the user requests to:
- "add plugin to marketplace"
- "update marketplace entry"
- "manage marketplace"
- "add to plugin marketplace"
- "update plugin in marketplace"
- "organize marketplace categories"

## Instructions

### Step 1: Locate Marketplace File
Find `.claude-plugin/marketplace.json` in the repository root. If it doesn't exist, offer to create one.

### Step 2: Parse Current Marketplace
Read and parse the marketplace.json:
1. Extract existing plugins
2. Identify categories
3. Check metadata completeness
4. Validate JSON structure

### Step 3: Determine Operation
Ask user what they want to do:
1. **Add new plugin** - Add entry for a new plugin
2. **Update existing** - Modify existing plugin entry
3. **Remove plugin** - Remove plugin from marketplace
4. **Reorganize categories** - Update category structure
5. **Update metadata** - Update marketplace-level metadata

### Step 4: Add New Plugin Entry
If adding a new plugin:
1. Request plugin information:
   - Name (kebab-case)
   - Display name
   - Description
   - Version
   - Source (directory path)
   - Category
   - Tags
2. Check for plugin manifest at source location
3. Auto-extract stats from manifest if available
4. Generate marketplace entry:
```json
{
  "name": "plugin-name",
  "displayName": "Display Name",
  "description": "Plugin description",
  "version": "1.0.0",
  "source": "./path/to/plugin",
  "category": "category-name",
  "tags": ["tag1", "tag2"],
  "stats": {
    "skills": 0,
    "commands": 0,
    "agents": 0
  },
  "bestFor": "Use case description",
  "includes": [
    "Feature 1",
    "Feature 2"
  ]
}
```
5. Add to plugins array in correct category order

### Step 5: Update Existing Plugin
If updating:
1. Find plugin by name
2. Show current entry
3. Ask what to update (version, description, stats, etc.)
4. Validate changes
5. Update entry while preserving other fields

### Step 6: Validate Marketplace Structure
Check:
1. JSON is valid
2. All plugins have required fields (name, source, description)
3. Source paths exist
4. Categories are defined
5. Stats are numeric
6. No duplicate plugin names
7. Tags are consistent

### Step 7: Update Marketplace Metadata
Update metadata section:
```json
"metadata": {
  "totalPlugins": 10,
  "totalSkills": 87,
  "totalCommands": 86,
  "totalAgents": 50,
  "totalHooks": 36,
  "lastUpdated": "2025-11-05"
}
```
Auto-calculate totals from plugin entries.

### Step 8: Organize Categories
Ensure categories object is complete:
```json
"categories": {
  "beginner": {
    "name": "Beginner",
    "description": "For learning Claude Code",
    "order": 1
  },
  ...
}
```

### Step 9: Write Updated Marketplace
1. Format JSON with 2-space indentation
2. Validate before writing
3. Create backup of original
4. Write updated marketplace.json
5. Verify file was written correctly

### Step 10: Provide Summary
Show user:
1. What was changed
2. Total plugins count
3. Marketplace statistics
4. Installation command for new plugins

## Example Interaction
```
User: "Add the docker-manager plugin to the marketplace"

Claude: I'll add docker-manager to the marketplace. Let me check for its manifest...

Found manifest at: ./docker-manager/.claude-plugin-manifest.json
Extracted information:
- Name: docker-manager
- Display Name: Docker Manager
- Category: specialized
- Skills: 3
- Commands: 5
- Agents: 2

Adding to marketplace...

✅ Plugin added to marketplace!

Total plugins: 11
Installation command:
/plugin marketplace add your-org/repo-name
/plugin install docker-manager
```

## Best Practices
- Always validate JSON before writing
- Create backups before modifications
- Auto-calculate statistics when possible
- Maintain consistent formatting (2-space indent)
- Verify source paths exist
- Keep categories organized by order
- Update lastUpdated timestamp
- Check for duplicate plugin names
- Validate semantic versioning
- Preserve existing entries when adding new ones

## Validation Rules
1. **Required Fields**:
   - name (unique, kebab-case)
   - displayName
   - description
   - version (semver)
   - source (valid path)
   - category (must exist in categories)

2. **Optional But Recommended**:
   - tags (array)
   - stats (object with counts)
   - bestFor (string or array)
   - includes (array)

3. **Metadata**:
   - Must match actual plugin counts
   - Date format: YYYY-MM-DD
   - Totals should be numeric

## Notes
- Backup marketplace.json before modifications
- Validate source paths before adding
- Check plugin manifest exists at source
- Auto-extract data from manifests when possible
- Maintain alphabetical order within categories
- Update metadata totals automatically
- Suggest tags based on plugin content
