# Basic Commands - Beginner Examples

Simple, practical slash commands for common development tasks.

## Available Examples

### Git Commands

#### 1. Git Status
**Location:** `git-status/`
**Purpose:** Show a clean, formatted git status with helpful next steps
**Use:** `/git-status`

#### 2. Git Commit Quick
**Location:** `git-commit-quick/`
**Purpose:** Quick commit with auto-generated meaningful message
**Use:** `/git-commit-quick`

#### 3. Git Undo
**Location:** `git-undo/`
**Purpose:** Safely undo last commit while keeping changes
**Use:** `/git-undo`

#### 4. Git Sync
**Location:** `git-sync/`
**Purpose:** Pull latest changes and push your commits
**Use:** `/git-sync`

### Refactoring Commands

#### 5. Extract Function
**Location:** `extract-function/`
**Purpose:** Extract code into a well-named function
**Use:** `/extract-function`

#### 6. Rename Variable
**Location:** `rename-variable/`
**Purpose:** Rename variables/functions consistently across files
**Use:** `/rename-variable oldName newName`

## How to Use These Examples

### Step 1: Choose Commands to Install

Pick the commands that match your workflow.

### Step 2: Install

```bash
# Create commands directory if it doesn't exist
mkdir -p .claude/commands

# Copy command files (each command.md becomes a slash command)
cp git-commit-quick/command.md .claude/commands/git-commit-quick.md
cp git-status/command.md .claude/commands/git-status.md
# ... etc
```

### Step 3: Use in Claude

```bash
cd your-project
claude

# Then use any installed command:
/git-status
/git-commit-quick
/git-sync
/extract-function
/rename-variable oldName newName
```

## What Makes a Good Beginner Command?

### 1. Solves One Problem
❌ Command that does many unrelated things
✅ Command with single, clear purpose

### 2. Clear Name
❌ `/do-stuff`
✅ `/git-commit-quick`

### 3. Simple Instructions
- Step-by-step process
- Clear inputs and outputs
- Easy to understand logic

### 4. Safety First
- Ask before destructive operations
- Show what will happen
- Provide undo/rollback info

### 5. Good Output
- Clear success/error messages
- Next step suggestions
- Helpful context

## Command Structure

### Basic Template:
```markdown
Brief description of what command does.

## Instructions

1. Step 1
2. Step 2
3. Step 3

## Example Output

\`\`\`
What the user sees
\`\`\`

## Arguments

$1: First argument
$2: Second argument

## Notes

Important information
```

## Learning Path

### Week 1: Use Commands
- Install 2-3 commands
- Use them in your daily workflow
- Observe how they work

### Week 2: Modify Commands
- Open command.md files
- Adjust output format
- Customize for your style

### Week 3: Create Commands
- Copy an existing command
- Modify for your specific need
- Test thoroughly

## Common Patterns

### Git Workflow Commands
```markdown
Pattern: Check status → Show plan → Ask confirmation → Execute

Examples:
- /git-commit-quick
- /git-sync
- /git-undo
```

### Code Refactoring Commands
```markdown
Pattern: Analyze code → Suggest change → Show preview → Apply

Examples:
- /extract-function
- /rename-variable
```

### Information Commands
```markdown
Pattern: Gather data → Format nicely → Present with context

Examples:
- /git-status
```

## Tips for Success

### Creating Commands

**Start Simple:**
- One clear purpose
- 3-5 steps max
- No complex logic

**Be Specific:**
```markdown
❌ "Handle git stuff"
✅ "Pull from remote and push local commits"
```

**Show, Don't Tell:**
```markdown
✅ Show example output in command.md
✅ Include error handling examples
✅ Demonstrate success and failure cases
```

### Using Commands

**Read the Documentation:**
Each command's README explains:
- What it does
- When to use it
- How to customize it

**Test in Safe Environment:**
- Try on test repository first
- Understand what happens
- Know how to undo

**Combine Commands:**
```bash
/git-status          # Check what changed
/git-commit-quick    # Commit changes
/git-sync            # Sync with remote
```

## Customization Ideas

### Personal Workflow
```markdown
Create commands for your routine:
- /morning-sync (pull all branches)
- /end-of-day (commit and push all projects)
- /deploy-staging (your deployment steps)
```

### Team Standards
```markdown
Encode team practices:
- Commit message format
- Branch naming conventions
- Code review checklist
```

### Project-Specific
```markdown
Each project can have its own:
- /test (run project's specific tests)
- /build (project's build command)
- /deploy (project's deployment)
```

## Combining Commands with Other Features

### With Skills
```yaml
Skill activates → Does work → Suggests command

Example:
comment-generator adds docs → suggests /git-commit-quick
```

### With Hooks
```yaml
Command runs → Hook validates → Proceed or block

Example:
/git-commit-quick → hook checks tests pass → allow/deny
```

### With Subagents
```yaml
Command → Delegate to subagent → Return result

Example:
/extract-function → code-reviewer checks result → report
```

## Real-World Workflows

### Morning Routine
```bash
/git-sync           # Get latest changes
/git-status         # See what's pending
# Work on code...
/git-commit-quick   # Commit your work
```

### Feature Development
```bash
# Create feature branch
git checkout -b feature/new-thing

# Work on code...
/extract-function   # Refactor as you go
/rename-variable    # Clean up naming

# Commit frequently
/git-commit-quick   # Quick commits
/git-status         # Check progress
```

### End of Day
```bash
/git-status         # Review all changes
/git-commit-quick   # Commit everything
/git-sync           # Push to remote
```

## Next Steps

After mastering basic commands:
1. Create project-specific commands
2. Explore intermediate workflow commands
3. Combine commands into workflows
4. Create commands for your specific tools

## Need Help?

- Read the command's README
- Check the command.md file
- Look at similar commands
- Test in isolated environment

## Files in Each Command

- `command.md` - The actual command (copy to `.claude/commands/`)
- `README.md` - Documentation and examples

## Related Examples

- **simple-skills** - For always-on capabilities
- **safety-hooks** - For preventing mistakes
- See intermediate examples for advanced commands
