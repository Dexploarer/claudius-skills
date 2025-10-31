# File Organizer Skill - Beginner Example

A practical skill that organizes files into categorized folders by file type, making messy directories clean and navigable.

## What This Example Teaches

- Using Bash for file operations
- Implementing safety confirmations
- Handling file system operations carefully
- Creating user-friendly interactive workflows
- Dealing with edge cases (conflicts, hidden files, etc.)

## How to Use

### 1. Install the Skill

```bash
# Copy to your Claude config
cp SKILL.md ~/.claude/skills/file-organizer.md

# Or for project-specific
cp SKILL.md your-project/.claude/skills/file-organizer.md
```

### 2. Try It Out

```bash
cd your-messy-directory
claude

# Then ask:
"Organize the files in this folder"
"Sort these files by type"
"Clean up this directory"
"Categorize these files"
```

### 3. Review and Confirm

The skill will:
1. Analyze the files
2. Show you the organization plan
3. Wait for your confirmation
4. Execute only after you approve

## Example Usage

**You:**
```
Organize the files in my Downloads folder
```

**Claude (using file-organizer skill):**
```
Analyzing Downloads folder...

Found 32 files to organize:

📁 Images/ (10 files)
   - vacation-photo.jpg
   - screenshot-01.png
   - logo.svg
   [... 7 more]

📁 Documents/ (15 files)
   - invoice-march.pdf
   - notes.txt
   - project-spec.md
   [... 12 more]

📁 Archives/ (4 files)
   - backup.zip
   - photos.tar.gz
   [... 2 more]

📁 Videos/ (3 files)
   - tutorial.mp4
   - demo.mov
   - recording.webm

This will create 4 new folders and move all files.
Proceed with organization? (yes/no)
```

**You:** yes

**Claude:**
```
✅ Organization complete!

Created folders:
- Images/ (10 files moved)
- Documents/ (15 files moved)
- Archives/ (4 files moved)
- Videos/ (3 files moved)

Your Downloads folder is now organized!
```

## What Makes This a Good Beginner Example?

### 1. Solves Real Problem
- Everyone has messy folders
- Immediate practical value
- Saves time on manual organization

### 2. Teaches Safety First
```yaml
Key safety features:
- Always asks for confirmation
- Shows exactly what will happen
- Handles file conflicts carefully
- Provides undo instructions
```

### 3. Uses Multiple Tools
```yaml
allowed-tools: [Read, Bash, Glob]
```
- Glob to find files
- Read for context
- Bash for file operations

### 4. Interactive Workflow
- Analyzes first
- Presents plan
- Gets confirmation
- Executes carefully
- Reports results

## Customization Ideas

### Custom Categories
```markdown
## My Organization Scheme

Work:
- Invoices/
- Contracts/
- Reports/

Personal:
- Photos/
- Documents/
- Receipts/

Projects:
- Code/
- Design/
- Documentation/
```

### Date-Based Organization
```markdown
## Organize by Date

Instead of by type, organize by:
- Today/
- This Week/
- This Month/
- Older/
  - 2024-01/
  - 2024-02/
  - ...
```

### Project-Based Organization
```markdown
## Project Structure

For development projects:
- src/ (all source code)
- tests/ (test files)
- docs/ (documentation)
- config/ (configuration files)
- assets/ (images, videos, etc.)
```

### Smart Naming
```markdown
## Naming Conventions

When organizing:
- Use lowercase folder names
- Add date prefixes: 2024-03-15_report.pdf
- Include categories: work_invoice.pdf, personal_photo.jpg
```

## Common Issues

### Files Not Moving?

**Check:** Permissions on the directory
```bash
# Make sure you have write permissions
ls -la
```

### Conflicts with Existing Files?

**Solution:** The skill should rename automatically
```
photo.jpg → photo-2.jpg (if photo.jpg exists)
```

If not, update the skill to handle conflicts better:
```bash
# Check before moving
if [ -f "dest/file.ext" ]; then
  mv "file.ext" "dest/file-2.ext"
fi
```

### Too Many Files?

**Approach:** Organize in stages
1. First by type
2. Then by date within each type
3. Or organize one category at a time

## Tips for Use

### Before Organizing
- **Back up important files** (just in case)
- **Review the plan carefully** before confirming
- **Test on a small folder first** to see how it works

### During Organization
- **Read the plan completely** before saying yes
- **Stop if something looks wrong** (just say no)
- **Ask for modifications** if needed

### After Organization
- **Verify files are where expected**
- **Check that nothing is missing**
- **Note the undo instructions** if provided

## Safety Best Practices

### Always Confirm
```
❌ BAD: Automatically move files
✅ GOOD: Show plan, wait for confirmation
```

### Handle Conflicts
```
❌ BAD: Overwrite existing files
✅ GOOD: Rename to avoid conflicts
```

### Preserve Files
```
❌ BAD: Modify file contents
✅ GOOD: Only move files, keep contents identical
```

### Provide Undo Path
```
✅ GOOD: Tell user how to undo
✅ GOOD: Consider creating an undo command
```

## Learning Opportunities

### File System Operations
Learn about:
- Moving files with `mv`
- Creating directories with `mkdir -p`
- Checking file existence
- Handling permissions

### User Interaction
Practice:
- Presenting information clearly
- Getting user confirmation
- Explaining what will happen
- Reporting results

### Safety Patterns
Understand:
- Why confirmation is important
- How to handle conflicts
- Preserving data integrity
- Providing rollback options

## Real-World Workflows

### Downloads Cleanup
```bash
# Weekly routine
1. Navigate to Downloads/
2. Ask Claude to organize files
3. Review plan
4. Confirm and execute
5. Delete empty folders if any
```

### Project Setup
```bash
# Starting new project
1. Create project directory
2. Add initial files
3. Ask Claude to organize by function
4. Get proper structure automatically
```

### Media Organization
```bash
# Organizing photo collection
1. Organize by type first (photos vs videos)
2. Then organize by date within each type
3. Create albums/collections
```

### Code Repository Cleanup
```bash
# Cleaning up messy repo
1. Organize source files into src/
2. Move tests into tests/
3. Documentation into docs/
4. Configs into config/
```

## Next Steps

### Extend This Skill
- Add date-based organization
- Include file size consideration
- Support custom categories via arguments
- Add undo functionality
- Create organization presets

### Create Related Skills
- `duplicate-finder` - Find and remove duplicates
- `large-file-finder` - Find files over certain size
- `old-file-archiver` - Archive files older than X days

### Combine With Other Skills
- Use with `todo-finder` to organize code projects
- Pair with backup systems for safety
- Integrate with cleanup workflows

## Advanced Usage

### Custom Organization Schemes
```
"Organize files but put all work documents in Work/ and personal in Personal/"
"Sort files by date, not type"
"Create subfolders by month within each category"
```

### Selective Organization
```
"Only organize image files"
"Organize everything except config files"
"Move only files older than 30 days"
```

### Batch Processing
```
"Organize all subdirectories one level deep"
"Clean up all project folders in this workspace"
```

## Files

- `SKILL.md` - The skill file (copy this to `.claude/skills/`)
- `README.md` - This documentation

## Related Examples

- **comment-generator** - Another safe, focused skill
- **todo-finder** - Read-only analysis skill
- See intermediate examples for more complex file operations

## Why This Pattern Works

### User Control
- Never surprises the user
- Clear about what will happen
- Easy to cancel or modify

### Safe by Design
- Confirmation before action
- Conflict handling
- No data loss
- Reversible operation

### Practical Value
- Solves real problems
- Saves time
- Improves organization
- Reduces clutter

### Educational
- Teaches file operations
- Shows safety patterns
- Demonstrates user interaction
- Explains best practices

## Important Reminders

⚠️ **Always back up important files before organizing**

⚠️ **Review the organization plan carefully**

⚠️ **Start with a test folder to learn how it works**

⚠️ **Don't organize system directories or critical folders**

✅ **Use for Downloads, Documents, projects, media collections**

✅ **Confirm you understand the plan before approving**

✅ **Keep the skill's safety features in place**
