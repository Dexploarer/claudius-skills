# Simple Skills - Beginner Examples

Easy-to-understand, single-purpose skills perfect for learning.

## Available Examples

### 1. Comment Generator
**Location:** `comment-generator/`
**Purpose:** Automatically adds comments and docstrings to code
**Teaches:** Skill basics, language detection, tool restrictions
**Use when:** "Add comments to this code"

### 2. TODO Finder (Coming Soon)
**Purpose:** Finds TODO, FIXME, HACK comments in codebase
**Teaches:** Using Grep, organizing output, read-only skills
**Use when:** "Find all TODOs"

### 3. File Organizer (Coming Soon)
**Purpose:** Organizes files by type into folders
**Teaches:** File operations, user confirmation, safety
**Use when:** "Organize these files"

## How to Use These Examples

### Step 1: Choose an Example
Pick a skill that interests you or solves a problem you have.

### Step 2: Read the README
Each example has a README explaining:
- What it does
- How to install it
- How to use it
- How it works
- How to customize it

### Step 3: Install and Test
```bash
# Copy to your project
cp comment-generator/SKILL.md your-project/.claude/skills/

# Or use directly
cd comment-generator
claude
```

### Step 4: Customize
- Modify the description
- Add your style guidelines
- Adapt to your workflow

## What Makes a Good Beginner Skill?

### 1. Single Purpose
❌ "Handles all file operations"
✅ "Generates code comments"

### 2. Specific Description
❌ "For code"
✅ "Generate code comments when user asks to 'add comments' or 'document code'"

### 3. Limited Tools
```yaml
allowed-tools: [Read, Grep]  # Start with minimal permissions
```

### 4. Clear Examples
Include examples of:
- When it activates
- What it produces
- How to use it

### 5. Good Documentation
- Installation steps
- Usage examples
- Customization ideas
- Troubleshooting

## Learning Path

### Week 1: Use As-Is
- Install a skill
- Use it in your workflow
- Observe when it activates

### Week 2: Modify
- Change the description
- Add your style preferences
- Test the changes

### Week 3: Create Your Own
- Copy a similar example
- Adapt for your needs
- Test thoroughly

## Common Patterns

### Read-Only Analysis
```yaml
allowed-tools: [Read, Grep, Glob]
description: Analyzes code for [specific thing]
```

### Code Generation
```yaml
allowed-tools: [Read, Write]
description: Generates [specific code type]
```

### Code Modification
```yaml
allowed-tools: [Read, Edit]
description: Modifies code to [specific change]
```

## Tips for Success

### Start Simple
Your first skill should:
- Do ONE thing
- Use 2-3 tools max
- Have clear activation phrase

### Test Thoroughly
- Try different phrasings
- Test with edge cases
- Verify it activates correctly

### Document Well
- Explain what it does
- Show examples
- Note limitations

## Next Steps

After mastering simple skills:
1. Check out **basic-commands** examples
2. Try **intermediate** framework-specific skills
3. Create your own skill from scratch

## Need Help?

- Read the skill file comments
- Check the README
- Look at other examples
- Ask in GitHub Discussions
