# Tutorial: Creating Your First Slash Command

Learn how to create a simple, useful slash command from scratch.

## What You'll Build

A `/quickstart` command that creates a basic project structure with all the essential files.

**Why this command?**
- Simple enough for beginners
- Immediately useful for new projects
- Teaches core concepts
- Easy to test and customize

## Prerequisites

- Claude Code installed
- A test directory to work in
- 15 minutes of time

## Step 1: Understand Slash Commands

Slash commands are shortcuts you trigger by typing `/commandname`.

**Examples:**
```bash
/test           # Runs all tests
/commit         # Creates a git commit
/explain code   # Explains code
```

**How they work:**
1. You type `/commandname` with optional arguments
2. Claude reads the command file
3. Claude follows the instructions in the file
4. Command completes!

## Step 2: Create the Command File

```bash
# Navigate to your project
cd ~/test-project

# Create commands directory
mkdir -p .claude/commands

# Create your command file
touch .claude/commands/quickstart.md
```

**Important naming:**
- Filename: `quickstart.md`
- Command usage: `/quickstart`
- They must match!

## Step 3: Write the Command

Open `.claude/commands/quickstart.md` and add:

```markdown
Create a quickstart project structure with essential files.

## What to Create

### 1. README.md
Create a README with:
- Project title
- Description
- Installation steps
- Usage examples
- Contributing guidelines

### 2. .gitignore
Create appropriate .gitignore for project type:
- Ask user: "What type of project? (node, python, java, etc.)"
- Generate language-specific ignore patterns

### 3. LICENSE
Create MIT license (or ask user for preference)

### 4. package.json / requirements.txt / etc.
Create appropriate dependency file for project type

### 5. Basic Directory Structure
```
project/
├── src/
├── tests/
├── docs/
└── examples/
```

## Instructions

1. **Ask for project details:**
   - Project name
   - Project type (node, python, etc.)
   - Description
   - License preference

2. **Create files:**
   - Use Write tool to create each file
   - Use appropriate templates
   - Fill in project-specific details

3. **Show summary:**
   ```
   ✅ Created:
   - README.md
   - .gitignore (Node.js)
   - LICENSE (MIT)
   - package.json
   - Directory structure

   📂 Your project is ready!

   Next steps:
   - Review the files
   - Run: npm install (or equivalent)
   - Start coding!
   ```

## Arguments

If user provides $ARGUMENTS:
- Use as project name
- Example: /quickstart my-awesome-app

If no arguments:
- Ask for project details interactively
```

## Step 4: Test Your Command

Save the file and start Claude Code:

```bash
# Start Claude Code in your test directory
cd ~/test-project
claude
```

Now test it:

```bash
/quickstart my-test-app
```

**Expected result:**
1. Claude asks for project details
2. Claude creates all the files
3. You see a summary of what was created
4. Files actually exist in your directory

**Verify:**
```bash
ls -la
# Should see: README.md, .gitignore, LICENSE, etc.
```

## Step 5: Refine Your Command

### Make It More Helpful

Add more guidance:

```markdown
## Usage

/quickstart [project-name]

Examples:
- /quickstart              # Interactive mode
- /quickstart my-app       # Quick mode with name
- /quickstart my-api node  # With project type
```

### Add Error Handling

```markdown
## Error Handling

- If files already exist: Ask before overwriting
- If project type unknown: Offer list of supported types
- If cancelled: Show "Operation cancelled"
```

### Add Templates

```markdown
## README Template

```markdown
# {PROJECT_NAME}

> {DESCRIPTION}

## Installation

```bash
npm install
```

## Usage

```bash
npm start
```

## Contributing

Contributions welcome!

## License

{LICENSE}
```
```

## Step 6: Test Different Scenarios

Test with various inputs:

### Test 1: No Arguments
```bash
/quickstart
```
Should ask for all details.

### Test 2: With Project Name
```bash
/quickstart awesome-project
```
Should use name, ask for other details.

### Test 3: In Existing Directory
```bash
# Create a README first
echo "# Test" > README.md

# Then run command
/quickstart
```
Should ask before overwriting.

### Test 4: Different Project Types
```bash
/quickstart python-app python
/quickstart java-app java
/quickstart rust-app rust
```
Should create appropriate files for each type.

## Step 7: Add Documentation

Add helpful comments at the top of your command file:

```markdown
# Quickstart Command

Creates a new project with all essential files and structure.

## Usage
/quickstart [project-name] [project-type]

## What It Creates
- README.md with project template
- .gitignore for your language
- LICENSE file (MIT by default)
- Dependency file (package.json, requirements.txt, etc.)
- Basic directory structure (src/, tests/, docs/)

## Examples

**Interactive mode:**
```bash
/quickstart
```
Prompts for all details.

**Quick mode:**
```bash
/quickstart my-new-app node
```
Creates Node.js project immediately.

## Customization

To customize templates:
1. Edit this file
2. Modify the template sections
3. Save and test

## Tips
- Run in an empty directory
- Review generated files before committing
- Customize for your team's standards
```

## Complete Example

Here's what your final command should look like:

```markdown
<!-- .claude/commands/quickstart.md -->

# Quickstart Command

Create a new project with essential files and structure.

## Usage
/quickstart [project-name] [project-type]

---

Create project structure with: $ARGUMENTS

## Step 1: Gather Information

If $ARGUMENTS provided:
- Use first argument as project name
- Use second argument as project type (if provided)

Otherwise, ask:
- "What's your project name?"
- "What type of project? (node, python, java, rust, go, other)"
- "Brief description?"
- "License? (MIT, Apache-2.0, GPL-3.0, other)"

## Step 2: Create Files

### README.md
```markdown
# {project_name}

> {description}

## Installation

[Installation instructions for {project_type}]

## Usage

[Usage examples]

## Contributing

Contributions are welcome!

## License

{license}
```

### .gitignore
Based on {project_type}, create appropriate patterns:
- Node.js: node_modules/, dist/, .env
- Python: __pycache__/, venv/, *.pyc
- Java: target/, *.class
- Rust: target/, Cargo.lock
- Go: vendor/, *.exe

### LICENSE
Create {license} file with current year and placeholder name.

### Dependency File
- Node.js: package.json with basic structure
- Python: requirements.txt (empty, ready for dependencies)
- Java: pom.xml or build.gradle skeleton
- Rust: Cargo.toml
- Go: go.mod

### Directory Structure
Create:
- src/ (source code)
- tests/ (test files)
- docs/ (documentation)
- examples/ (usage examples)

## Step 3: Show Summary

Display:
```
🚀 Project Created: {project_name}

✅ Files created:
   - README.md
   - .gitignore ({project_type})
   - LICENSE ({license})
   - {dependency_file}
   - Directory structure

📂 Structure:
   {project_name}/
   ├── src/
   ├── tests/
   ├── docs/
   ├── examples/
   ├── README.md
   ├── .gitignore
   ├── LICENSE
   └── {dependency_file}

📋 Next steps:
   1. Review generated files
   2. Initialize git: git init
   3. Install dependencies
   4. Start coding!

Happy hacking! 🎉
```

## Error Handling

- If files exist: "File {filename} exists. Overwrite? (yes/no)"
- If unknown project type: "Unsupported type. Choose: node, python, java, rust, go"
- If cancelled: "Operation cancelled. No files were created."
```

## Common Issues & Solutions

### Issue 1: Command Not Found

**Problem:**
```bash
/quickstart
# Error: Command not found
```

**Solutions:**
1. Check filename: Must be `quickstart.md` in `.claude/commands/`
2. Restart Claude Code
3. Check for typos in filename
4. Verify file has content

### Issue 2: Command Doesn't Do Anything

**Problem:** Command runs but nothing happens

**Solutions:**
1. Check if instructions are clear
2. Make sure you're using Write tool
3. Add explicit steps
4. Test in small increments

### Issue 3: Arguments Not Working

**Problem:** Can't pass arguments to command

**Solutions:**
1. Use `$ARGUMENTS` in command file
2. Test with: `/quickstart test-name`
3. Add argument handling instructions

### Issue 4: Files Created in Wrong Location

**Problem:** Files go to wrong directory

**Solutions:**
1. Specify full paths or relative paths clearly
2. Show user where files will be created
3. Ask for confirmation before creating

## Enhancements

Once your command works, try adding:

### 1. Git Initialization

```markdown
After creating files:
1. Run: git init
2. Run: git add .
3. Run: git commit -m "Initial commit"
4. Show: "Git repository initialized!"
```

### 2. Project Templates

```markdown
Support template selection:
- minimal: Just README, .gitignore, LICENSE
- standard: Above + src/, tests/
- complete: Above + CI/CD, Docker, docs
```

### 3. Interactive Selection

```markdown
Show menu:
"What to include?"
[ ] README.md
[ ] .gitignore
[ ] LICENSE
[ ] Tests directory
[ ] Docker files
[ ] CI/CD config
```

### 4. Team Presets

```markdown
Load team presets:
- /quickstart --preset=backend
- /quickstart --preset=frontend
- /quickstart --preset=fullstack
```

## Next Steps

### Create Related Commands

1. **/scaffold** - Create boilerplate for components
2. **/init** - Initialize configuration files
3. **/template** - Apply templates to existing files

### Combine with Skills

Create a skill that automatically suggests running `/quickstart` when:
- You're in an empty directory
- You mention starting a new project
- You ask about project setup

### Share with Team

1. Commit to your project's repository
2. Team members get it automatically
3. Customize for your team's standards

## Congratulations!

You've created your first slash command! 🎉

**What you learned:**
- ✅ Where command files go
- ✅ How to name them
- ✅ How to use arguments
- ✅ How to structure instructions
- ✅ How to test commands
- ✅ How to handle errors
- ✅ How to document commands

**Next challenges:**
1. Create a command for your most common task
2. Build a command that uses Bash tool
3. Create a command that calls a subagent
4. Share your command with others

---

**Ready for more? Continue with [setting-up-hooks.md](./setting-up-hooks.md)!**
