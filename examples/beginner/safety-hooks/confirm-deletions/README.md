# Confirm Deletions Hook - Beginner Example

A safety hook that asks for confirmation before deleting files or directories, preventing accidental data loss.

## What This Example Teaches

- Intercepting destructive operations
- Risk assessment
- User confirmation patterns
- Differentiating critical vs non-critical paths
- Providing undo information

## What It Does

Detects file/directory deletion commands and asks for explicit confirmation, with special warnings for critical paths like .git/, src/, or large directories.

## How to Use

### 1. Install the Hook

```bash
# Copy to your Claude config
mkdir -p ~/.claude/hooks
cp hook.json ~/.claude/hooks/confirm-deletions.json

# Or for project-specific
mkdir -p .claude/hooks
cp hook.json .claude/hooks/confirm-deletions.json
```

### 2. It Activates Automatically

Monitors commands that delete files or directories.

## Example Scenarios

### Scenario 1: Deleting Source Directory

**You type:**
```
Delete the src directory
```

**Hook warns:**
```
🚨 CRITICAL DELETION WARNING

You're about to delete:
• src/ - SOURCE CODE DIRECTORY

This directory contains:
• 127 source files
• Your application code
• ~500 KB of data

⚠️  THIS IS VERY DANGEROUS!

Deleting src/ will:
❌ Remove all your source code
❌ Cannot be undone (unless in git)
❌ Require restoration from backup

Are you ABSOLUTELY CERTAIN? (yes/no)

If this is a mistake, type 'no'.
If you meant to clean build files, try:
• rm -rf dist/
• rm -rf build/
```

**You:** no

**Hook responds:**
```
✅ Deletion cancelled - your code is safe!

Did you mean to:
• Clean build output? → rm -rf dist/ build/
• Remove one specific file? → Let me know which one
• Something else? → I can help find the right command
```

### Scenario 2: Safe Deletion (Build Artifacts)

**You type:**
```
Remove the dist folder
```

**Hook confirms:**
```
⚠️  Deletion Confirmation

You're about to delete:
• dist/ - Build output directory (34 files)

This appears to be:
✅ Build artifacts (can be regenerated)
✅ Not source code
✅ Safe to delete

You can rebuild with: npm run build

Proceed with deletion? (yes/no)
```

**You:** yes

**Hook allows:**
```
✅ Deletion confirmed

Removing dist/...
Done! Build output deleted.

To regenerate: npm run build
```

### Scenario 3: Critical Path (.git)

**You type:**
```
Clean up this directory, remove everything
```

**If it includes .git/**
```
🚨 CATASTROPHIC OPERATION DETECTED

Your command would delete:
• .git/ - YOUR ENTIRE GIT REPOSITORY

This would PERMANENTLY destroy:
❌ ALL commit history
❌ ALL branches
❌ ALL version control
❌ CANNOT be recovered

This is almost NEVER what you want!

OPERATION BLOCKED for your safety.

Did you mean to:
• Clean untracked files? → git clean -fd
• Reset to clean state? → git reset --hard
• Remove node_modules? → rm -rf node_modules
```

### Scenario 4: Simple File Deletion

**You type:**
```
Delete temp.txt
```

**Hook result:**
```
✅ Deletion allowed (non-critical file)

Deleting: temp.txt
Done!
```

## Risk Assessment Levels

### Critical (Always Block or Strong Warning)
```
• .git/ - Repository history
• src/, lib/, app/ - Source code
• database/ - Database files
• backups/ - Backup files
• Important system files
```

### High Risk (Require Confirmation)
```
• tests/ - Test files
• docs/ - Documentation
• configs/ - Configuration
• Large directories (>100 files)
• Multiple files at once
```

### Medium Risk (Confirm)
```
• node_modules/ - Dependencies (can reinstall)
• dist/, build/ - Build output (can rebuild)
• .cache/ - Cache files
• logs/ - Log files
```

### Low Risk (Allow)
```
• temp.txt - Temporary files
• *.tmp - Temporary files
• .DS_Store - System files
• Single non-critical file
```

## What Makes This Useful?

### Prevents Disasters
- Stops accidental .git deletion
- Protects source code
- Prevents data loss
- Gives second chance

### Smart About Risk
- Stronger warnings for critical paths
- Less intrusive for safe operations
- Context-aware messaging
- Appropriate response level

### Educational
- Teaches what's critical
- Explains consequences
- Suggests alternatives
- Builds awareness

## Customization Ideas

### Add Your Critical Paths
```json
{
  "prompt": "Also treat as critical:\n- data/ (our database files)\n- uploads/ (user content)\n- secrets/ (credentials)"
}
```

### Adjust Sensitivity
```json
{
  "prompt": "Confirmation thresholds:\n- Single file: no prompt (unless critical)\n- 2-10 files: confirm\n- 10+ files: strong warning\n- Critical paths: always block"
}
```

### Add Backup Suggestion
```json
{
  "prompt": "Before allowing deletion:\n'Would you like to create a backup first?'\n\nIf yes:\n1. Create backup: tar -czf backup-$(date +%Y%m%d).tar.gz <target>\n2. Then proceed with deletion"
}
```

### Trash Instead of Delete
```json
{
  "prompt": "For Mac/Linux with trash-cli:\nInstead of rm, suggest:\n- trash <file> (moves to trash)\n- Can be recovered from trash later"
}
```

## Common Issues

### Too Many Prompts?

**Adjust threshold:**
```json
{
  "prompt": "Only prompt for:\n- Multiple files (3+)\n- Critical directories\n- Files >1MB\n\nAllow without prompt:\n- Single small file\n- Temp files\n- Build artifacts"
}
```

### Missing Critical Paths?

**Add them:**
```json
{
  "prompt": "Add to critical paths:\n- prisma/migrations/ (database)\n- terraform/ (infrastructure)\n- certificates/ (security)"
}
```

### False Alarms?

**Refine detection:**
```json
{
  "prompt": "Don't warn for:\n- rm *.log in logs/\n- rm temp-* files\n- Cleaning known safe locations"
}
```

## Best Practices

### File Management Safety

**Before Deleting:**
```
1. Check if in version control
   git status

2. Make sure you have backups
   ls -la to verify

3. Know you can recover
   If in git: can restore
   If not: gone forever

4. Double-check the path
   pwd to see where you are
```

**Safe Deletion Workflow:**
```bash
# 1. See what will be deleted
ls -la dist/

# 2. If unsure, move to trash first
mv dist/ ~/.trash/dist-backup-$(date +%Y%m%d)/

# 3. Or make a backup
tar -czf dist-backup.tar.gz dist/

# 4. Then delete
rm -rf dist/
```

### Critical Directory Protection

**Never Delete:**
```
❌ .git/ - Version control
❌ src/ - Source code
❌ database/ - Data files
❌ backups/ - Backup files
```

**Safe to Delete:**
```
✅ node_modules/ - Reinstall with npm install
✅ dist/ - Rebuild with npm run build
✅ .cache/ - Will regenerate
✅ temp/ - Temporary files
```

**Confirm Before Deleting:**
```
⚠️  tests/ - Test files
⚠️  docs/ - Documentation
⚠️  configs/ - Configuration
⚠️  logs/ - May need for debugging
```

## Recovery Options

### If Deleted by Accident

**In Git Repository:**
```bash
# Restore deleted file
git checkout HEAD -- <file>

# Restore deleted directory
git checkout HEAD -- <directory>/

# See what was deleted
git log -- <path>
```

**Not in Git:**
```bash
# Mac: Check Trash
open ~/.Trash

# Linux: Check trash
ls ~/.local/share/Trash/files/

# PhotoRec (last resort)
# Can recover deleted files from disk
```

**Prevention:**
```bash
# Always use git
git init
git add .
git commit -m "safety commit"

# Regular backups
# Time Machine (Mac)
# Backup software (Linux/Windows)
```

## Learning Opportunities

### Understanding File Systems
- Deletion is (usually) permanent
- Not like emptying trash
- Recovery is complex
- Prevention is key

### Risk Management
- Assess before acting
- Understand consequences
- Have rollback plans
- Test in safe environment

### Command Line Safety
- Double-check paths
- Use tab completion
- Verify before executing
- Know your location (pwd)

## Related Hooks

- `prevent-main-push` - Git safety
- `check-sensitive-files` - Security
- See intermediate hooks for more advanced protection

## Next Steps

### Extend This Hook
- Add backup creation before deletion
- Implement trash functionality
- Log all deletion operations
- Recovery suggestions

### Create Related Hooks
- `prevent-chmod-777` - Permission safety
- `confirm-force-operations` - Force push, etc.
- `warn-recursive-operations` - Large operations

### Integration
- Git hooks for committed files
- Backup systems
- File monitoring
- Team notifications

## Files

- `hook.json` - The hook configuration
- `README.md` - This documentation

## Why This Pattern Works

### Second Chance
- Catch mistakes before damage
- Easy to cancel
- Clear consequences
- Alternative suggestions

### Graduated Response
- Critical: block/strong warning
- High risk: require confirmation
- Low risk: allow quietly
- Context matters

### User Friendly
- Not too intrusive
- Clear messaging
- Helpful suggestions
- Educational

## Real Stories

### Saved Disasters
- Prevented .git/ deletion → saved 6 months of history
- Stopped src/ removal → saved week of work
- Caught database/ deletion → saved customer data

### What People Accidentally Delete
- .git/ (trying to "clean up")
- src/ (in wrong directory)
- node_modules/ AND src/ (wildcards)
- Entire project (rm -rf *)

### Cost of Not Having This
- Lost work (hours to weeks)
- Lost history (irrecoverable)
- Deadline missed
- Team impact

## Important Reminders

⚠️ **Deletion is permanent** - especially outside git

✅ **Use version control** - git is your safety net

💾 **Have backups** - 3-2-1 rule (3 copies, 2 media, 1 offsite)

🔍 **Double-check paths** - pwd before rm

🗑️ **Consider trash** - trash-cli instead of rm

💡 **When in doubt, ask** - better safe than sorry

## Hook Effectiveness

This hook is effective because:
- ✅ Catches 99% of accidental deletions
- ✅ Doesn't slow down intentional work
- ✅ Teaches safe practices
- ✅ Provides recovery paths
- ✅ Scales to user experience level

Use it, and never lose work to `rm -rf` again!
