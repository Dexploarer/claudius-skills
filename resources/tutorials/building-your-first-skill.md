# Tutorial: Building Your First Claude Code Skill

A hands-on guide to creating your first skill from scratch.

## What You'll Build

A skill that generates `.gitignore` files for different project types.

**Why this skill?**
- Simple enough for beginners
- Immediately useful
- Teaches all key concepts
- Easy to test

## Prerequisites

- Claude Code installed
- Basic understanding of what skills are
- A test project to work in

## Step-by-Step Guide

### Step 1: Create the File

```bash
# Navigate to your project
cd your-project

# Create the skills directory if it doesn't exist
mkdir -p .claude/skills

# Create your skill file
touch .claude/skills/gitignore-generator.md
```

### Step 2: Add YAML Frontmatter

Open `.claude/skills/gitignore-generator.md` and add:

```yaml
---
name: gitignore-generator
description: Generate .gitignore files for different project types. Use when user asks to "create gitignore", "generate gitignore", or "add gitignore for [language/framework]".
allowed-tools: [Write]
---
```

**Let's break this down:**

- `name`: Unique identifier (lowercase, hyphens only)
- `description`: **CRITICAL** - when this skill activates
  - Be specific!
  - Include trigger phrases
  - Mention what it does
- `allowed-tools`: What tools this skill can use
  - `[Write]` = can create files
  - Start minimal, add as needed

### Step 3: Add Instructions

Below the frontmatter, add:

```markdown
# Gitignore Generator Skill

Generates appropriate .gitignore files based on project type.

## Instructions

### Step 1: Determine Project Type

Ask the user what type of project if not specified:
- Node.js / JavaScript / TypeScript
- Python
- Java
- Ruby
- Go
- Rust
- General

### Step 2: Generate Content

Based on project type, include appropriate ignore patterns:

**For Node.js:**
```
# Dependencies
node_modules/
package-lock.json (if using yarn)

# Environment
.env
.env.local

# Build output
dist/
build/
.next/

# Logs
*.log

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
```

**For Python:**
```
# Virtual environment
venv/
env/
.venv/

# Byte-compiled
__pycache__/
*.py[cod]
*$py.class

# Distribution
dist/
build/
*.egg-info/

# Environment
.env

# Jupyter
.ipynb_checkpoints/
```

[Add patterns for other languages...]

### Step 3: Write the File

1. Create `.gitignore` in project root
2. If file exists, ask before overwriting
3. Show the user what was created
4. Explain what each section does

### Step 4: Provide Next Steps

Suggest:
- Review the file
- Add custom patterns if needed
- Commit to git
```

### Step 4: Test Your Skill

Save the file and start Claude Code:

```bash
claude
```

Now test it:

```
You: "Create a .gitignore for my Node.js project"
```

**Expected behavior:**
1. Skill activates automatically
2. Claude creates a .gitignore file
3. File contains Node.js-specific patterns
4. You see a summary of what was added

### Step 5: Refine the Description

If the skill doesn't activate, make the description more specific:

```yaml
# ❌ Too vague
description: For gitignore files

# ✅ Better
description: Generate .gitignore files. Use when user asks to "create gitignore" or "add gitignore".

# ✅ Even better
description: Generate .gitignore files for Node.js, Python, Java, and other project types. Use when user asks to "create gitignore", "generate gitignore", "add gitignore", or "ignore files for [project type]".
```

**Test again with different phrasings:**
- "I need a gitignore"
- "Generate gitignore for Python"
- "Create .gitignore"
- "Add a gitignore file"

### Step 6: Add More Features

Now that it works, enhance it:

```markdown
## Advanced Features

### Multi-Language Support

If project has multiple languages:
1. Detect all languages in project
2. Combine patterns from all
3. Add section comments

Example:
```
# === JavaScript ===
node_modules/

# === Python ===
venv/
__pycache__/
```

### Custom Patterns

Allow user to add custom patterns:
"Generate gitignore for Node.js and also ignore *.backup files"

### Smart Detection

If .gitignore already exists:
1. Read current content
2. Identify what's missing
3. Suggest additions
4. Merge carefully
```

### Step 7: Document Your Skill

Add a comment block at the top:

```markdown
---
name: gitignore-generator
description: ...
---

# Gitignore Generator Skill

## What It Does

Automatically generates appropriate .gitignore files based on your project type.

## Activation Phrases

- "Create a .gitignore"
- "Generate gitignore for [language]"
- "Add gitignore"
- "I need a gitignore file"

## Supported Languages

- Node.js / JavaScript / TypeScript
- Python
- Java
- Ruby
- Go
- Rust

## Examples

**Input:** "Create a .gitignore for my Python project"

**Output:**
```
# Python project .gitignore

# Virtual environments
venv/
...
```

## Limitations

- Doesn't handle custom build tools
- May need manual tweaking for specific needs
- Always review before committing
```

## Complete Example

Here's what your final skill file should look like:

```yaml
---
name: gitignore-generator
description: Generate .gitignore files for Node.js, Python, Java, and other project types. Use when user asks to "create gitignore", "generate gitignore", "add gitignore", or "ignore files for [project type]".
allowed-tools: [Write]
---

# Gitignore Generator Skill

Automatically generates .gitignore files for different project types.

## Activation Phrases
- "Create gitignore"
- "Generate .gitignore"
- "Add gitignore for Python"

## Instructions

### Step 1: Determine Project Type
[Instructions as shown above...]

### Step 2: Generate Content
[Patterns for each language...]

### Step 3: Write File
[File creation steps...]

## Supported Languages

**Node.js/JavaScript:**
```
node_modules/
dist/
.env
```

**Python:**
```
venv/
__pycache__/
.env
```

[More languages...]
```

## Testing Checklist

- [ ] Skill file created in `.claude/skills/`
- [ ] YAML frontmatter is valid
- [ ] Description includes trigger phrases
- [ ] Instructions are clear
- [ ] Skill activates with test phrases
- [ ] Generated file is correct
- [ ] Edge cases handled
- [ ] Documented properly

## Common Issues

### Skill Doesn't Activate

**Problem:** You say "create gitignore" but nothing happens

**Solutions:**
1. Check description has "create gitignore" phrase
2. Restart Claude Code
3. Try exact phrase from description
4. Run `claude --debug` to see activation attempts

### Wrong Content Generated

**Problem:** Creates wrong ignore patterns

**Solution:** Improve project detection:
```markdown
## Project Detection

1. Check package.json -> Node.js
2. Check requirements.txt -> Python
3. Check pom.xml -> Java
4. Ask user if unclear
```

### File Already Exists

**Problem:** Overwrites existing .gitignore

**Solution:** Add safety check:
```markdown
Before writing:
1. Check if .gitignore exists
2. If yes, ask: "File exists. Overwrite, merge, or cancel?"
3. If merge, combine patterns
4. If cancel, abort
```

## Next Steps

### Enhance This Skill

1. Add more languages (C++, C#, PHP)
2. Support frameworks (Django, Rails, Spring)
3. Add templates from gitignore.io
4. Smart merge with existing files

### Create Related Skills

1. **license-generator**: Creates LICENSE files
2. **readme-generator**: Creates README files (in starter kit!)
3. **editorconfig-generator**: Creates .editorconfig

### Build a Suite

Combine into a **project-setup skill** that creates:
- .gitignore
- README.md
- LICENSE
- package.json
- All together!

## Congratulations!

You've just created your first Claude Code skill! 🎉

**What you learned:**
- How to structure a skill file
- Writing effective descriptions
- Using allowed-tools
- Testing and refining
- Handling edge cases
- Documentation

**Next challenges:**
1. Create a skill for your specific workflow
2. Build a more complex multi-file skill
3. Create a skill that uses multiple tools
4. Share your skill with your team

## Resources

- **Starter Kit**: Complete working examples
- **Templates**: Blank templates to copy
- **Examples**: More skill patterns
- **Guides**: Best practices and tips

---

**Happy skill building!** 🚀
