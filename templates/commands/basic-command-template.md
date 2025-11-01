<!-- Basic Command Template -->
<!-- File: .claude/commands/{command-name}.md -->

Execute a simple, focused task with clear steps and helpful output.

## What This Command Does

Brief one-sentence description of the command's purpose.

## Usage

```bash
# Basic usage
/{command-name}

# With arguments
/{command-name} [arg1] [arg2]

# With options
/{command-name} --option value
```

## Arguments

Handle arguments if provided:
- `$ARGUMENTS` - All arguments as a single string
- `$1` - First argument
- `$2` - Second argument
- `$3` - Third argument

## Instructions

### Step 1: Validate Inputs

Check that required inputs are present:

```bash
# If $1 is empty
If no arguments provided:
  - Ask: "Please provide [required input]"
  - Show usage examples
  - Exit

# If $1 is invalid
If argument is invalid:
  - Show error: "Invalid value for [argument]"
  - Show valid options
  - Exit
```

### Step 2: Show Current State

Display relevant information before making changes:

```
📍 Current State:
  - [Key metric 1]: [value]
  - [Key metric 2]: [value]
  - [Key metric 3]: [value]
```

### Step 3: Execute Main Task

Perform the core functionality:

```bash
# Example: Run a git command
git [command] [options]

# Example: Process files
Find files matching [pattern]
For each file:
  - Process file
  - Show progress
```

### Step 4: Verify Success

Check that the operation completed successfully:

```bash
# Verify the result
Check that [expected outcome] occurred

If successful:
  - Show success message
  - Display summary

If failed:
  - Show error message
  - Suggest next steps
  - Offer to retry
```

### Step 5: Show Summary

Display what was done and suggest next steps:

```
✅ Success!

📊 Summary:
  - [Action 1]: Complete
  - [Action 2]: Complete
  - [Files affected]: X files

💡 Next Steps:
  - [Suggested action 1]
  - [Suggested action 2]
  - [Related command to run]
```

## Examples

### Example 1: No Arguments

```bash
/{command-name}
```

Expected behavior:
- Detect context automatically
- Execute default behavior
- Show results

### Example 2: With Specific Input

```bash
/{command-name} specific-value
```

Expected behavior:
- Use provided value
- Execute specific behavior
- Show customized results

### Example 3: With Options

```bash
/{command-name} value --dry-run
```

Expected behavior:
- Parse options
- Show what would happen (no changes)
- Ask for confirmation to proceed

## Error Handling

Handle common errors gracefully:

### Error: Missing Requirements

```
❌ Error: [Requirement] not found

This command requires:
  - [Requirement 1]
  - [Requirement 2]

Please install: [installation command]
```

### Error: Invalid Input

```
❌ Error: Invalid [input type]

Expected: [format]
Got: [actual value]

Examples:
  - Valid: [example 1]
  - Valid: [example 2]
```

### Error: Operation Failed

```
❌ Error: Failed to [action]

Reason: [error message]

Troubleshooting:
  - Check [thing 1]
  - Verify [thing 2]
  - Try [alternative approach]

Need help? Run: /help {command-name}
```

## Options and Flags

Support common options:

### --dry-run

Show what would happen without making changes:

```
🔍 Dry Run Mode

Would execute:
  1. [Action 1]
  2. [Action 2]
  3. [Action 3]

Files that would be affected:
  - [file 1]
  - [file 2]

Run without --dry-run to apply changes.
```

### --verbose

Show detailed information:

```
📝 Verbose Output

Checking [thing 1]... ✓
Validating [thing 2]... ✓
Processing [thing 3]...
  - Sub-step 1... ✓
  - Sub-step 2... ✓
  - Sub-step 3... ✓
Finalizing... ✓
```

### --help

Show detailed usage information:

```
📚 {Command Name} - Help

Description:
  [Detailed description of what this command does]

Usage:
  /{command-name} [arguments] [options]

Arguments:
  arg1    [Description of arg1]
  arg2    [Description of arg2] (optional)

Options:
  --dry-run    Show what would happen
  --verbose    Show detailed output
  --force      Skip confirmations
  --help       Show this help

Examples:
  /{command-name} example1
  /{command-name} example2 --dry-run
  /{command-name} example3 --verbose

See also:
  /{related-command-1}
  /{related-command-2}
```

## Output Format

Use consistent, readable formatting:

### Icons

Use these icons for clarity:
- ✅ Success / Completed
- ❌ Error / Failed
- ⚠️  Warning / Attention needed
- 📍 Current state / Location
- 💡 Suggestion / Tip
- 📊 Summary / Statistics
- 🔍 Inspection / Dry run
- 📝 Details / Verbose
- 🚀 Action / Next steps

### Colors (via emphasis)

```
**Important Information** (bold)
*Emphasis on key points* (italic)
`Code or commands` (backticks)
```

### Sections

Break output into clear sections:

```
## Section Title

Content here...

---

## Next Section

More content...
```

## Safety and Confirmation

For potentially destructive operations:

### Ask Before Proceeding

```
⚠️  Warning: This will [describe impact]

Affected resources:
  - [resource 1]
  - [resource 2]

Type 'yes' to continue, or 'no' to cancel:

If user types 'yes':
  - Proceed with operation
  - Show progress
  - Show completion message

If user types 'no' or anything else:
  - Show: "Operation cancelled. No changes made."
  - Exit
```

### Provide Undo Information

```
✅ Operation completed

To undo this change:
  /{undo-command}

Or manually:
  [manual undo steps]
```

## Integration with Other Tools

### Call Subagents

If complex analysis is needed:

```
# Delegate to a specialized subagent
"Call the {specialized-agent} subagent to analyze this"

Wait for analysis...

Use analysis results in next steps...
```

### Trigger Skills

If additional processing is needed:

```
# This might trigger related skills automatically
"Add documentation to the generated files"
```

### Chain Commands

Suggest related commands:

```
✅ Task complete!

Related commands you might want to run:
  /{next-command} - [what it does]
  /{alternative-command} - [what it does]
```

## Testing Your Command

Before using in production:

### Test 1: No Arguments

```bash
/{command-name}
```

Expected: Should work with sensible defaults OR ask for required input

### Test 2: Happy Path

```bash
/{command-name} valid-input
```

Expected: Should complete successfully with clear output

### Test 3: Invalid Input

```bash
/{command-name} invalid-input
```

Expected: Should show helpful error message

### Test 4: Edge Cases

```bash
/{command-name} ""
/{command-name} very-long-input-that-might-cause-issues
/{command-name} special-char$
```

Expected: Should handle gracefully

### Test 5: --dry-run

```bash
/{command-name} input --dry-run
```

Expected: Should show preview without making changes

## Best Practices

✅ **Do:**
- Keep commands focused on one task
- Provide clear, actionable output
- Handle errors gracefully
- Suggest next steps
- Make dangerous operations safe (confirmation)
- Show progress for long operations
- Provide --dry-run for testing

❌ **Don't:**
- Make silent changes
- Show cryptic error messages
- Assume inputs are valid
- Skip validation
- Make irreversible changes without warning
- Leave user wondering what happened

## Customization Tips

### For Your Project

Add project-specific logic:

```markdown
## Project-Specific Behavior

If in project type A:
  - Do [specific thing A]

If in project type B:
  - Do [specific thing B]

Detect project type by:
  - Checking for package.json vs requirements.txt vs pom.xml
```

### For Your Team

Add team conventions:

```markdown
## Team Conventions

Our team requires:
  - [Convention 1]
  - [Convention 2]

Check for compliance:
  - [Check 1]
  - [Check 2]

If not compliant:
  - Show warning
  - Offer to fix
```

## Performance Considerations

For slow operations:

```
🔄 Processing... This may take a moment.

Progress:
  [=====>                    ] 25% (5/20 items)

Estimated time remaining: 15 seconds
```

## Logging and Debug

Include debug information when needed:

```markdown
## Debug Mode

If user passes --debug:
  - Show detailed execution steps
  - Log all commands being run
  - Display timing information
  - Save log file to .claude/logs/{command-name}.log
```

## Related Commands

List related commands for discoverability:

```
## Related Commands

- /{related-cmd-1} - [Brief description]
- /{related-cmd-2} - [Brief description]
- /{related-cmd-3} - [Brief description]
```

## Notes

- This command is non-destructive (OR: This command modifies files)
- Requires: [any prerequisites]
- Works with: [compatible tools/frameworks]
- See also: [related documentation]

## Version History

Track important changes:

```markdown
## Changelog

### v1.2.0
- Added --dry-run support
- Improved error messages
- Added progress indicator

### v1.1.0
- Added validation for inputs
- Added --verbose option

### v1.0.0
- Initial version
```
