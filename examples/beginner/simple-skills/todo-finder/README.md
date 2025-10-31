# TODO Finder Skill - Beginner Example

A simple skill that finds and organizes TODO, FIXME, HACK, and other action item comments in your codebase.

## What This Example Teaches

- Using the Grep tool effectively
- Organizing and presenting search results
- Creating read-only analysis skills
- Working with multiple file types
- Prioritizing and categorizing findings

## How to Use

### 1. Install the Skill

```bash
# Copy to your Claude config
cp SKILL.md ~/.claude/skills/todo-finder.md

# Or for project-specific
cp SKILL.md your-project/.claude/skills/todo-finder.md
```

### 2. Try It Out

```bash
cd your-project
claude

# Then ask:
"Find all TODOs"
"Show me FIXMEs in the codebase"
"What action items are in the code?"
"List all HACKs that need fixing"
```

### 3. Watch It Activate

The skill automatically activates when you mention:
- "find TODOs"
- "show FIXMEs"
- "list action items"
- "what needs to be done"
- "scan for TODOs"

## Example Usage

**You:**
```
Find all TODOs in this project
```

**Claude (using todo-finder skill):**
```
Searching for TODO comments across the codebase...

Found 12 TODO items:

📁 src/components/Header.js:23
   TODO: Add mobile responsive navigation

📁 src/services/api.js:67
   TODO: Implement request retry logic

📁 src/utils/validation.js:45
   TODO: Add email validation

📁 src/pages/Dashboard.js:89
   TODO: Add loading states

[... more items ...]

Total: 12 TODO items found
Consider prioritizing these in your next sprint.
```

**You:**
```
Show me all critical issues - FIXMEs and BUGs
```

**Claude (using todo-finder skill):**
```
Scanning for critical issues...

🔴 CRITICAL ITEMS (3):

📁 src/auth/login.js:156
   FIXME: Authentication bypass possible when token is expired

📁 src/api/payments.js:234
   BUG: Payment processing fails for amounts with decimals

📁 src/utils/security.js:89
   FIXME: XSS vulnerability in user input handling

Total: 3 critical issues that need immediate attention
```

## What Makes This a Good Beginner Example?

### 1. Practical and Useful
- Every codebase has TODOs
- Provides immediate value
- Helps with project management

### 2. Read-Only with Grep
```yaml
allowed-tools: [Grep, Read, Glob]
```
- Uses Grep for fast searching
- Read for context
- Glob for file patterns
- No modifications, completely safe

### 3. Clear Output Organization
- Groups by priority
- Shows file locations
- Makes results actionable
- Easy to navigate

### 4. Teaches Search Patterns
- Learn regex patterns
- Understand file filtering
- See how to organize results

## Customization Ideas

### Add Your Team's Markers
```markdown
## Custom Markers

Search for your team's specific tags:
- TECHDEBT: Technical debt items
- REVIEW: Needs code review
- DISCUSS: Needs team discussion
- QUESTION: Open questions
```

### Integrate with Issue Tracking
```markdown
## GitHub Integration

When finding TODOs, suggest:
1. Create GitHub issue for each critical item
2. Add issue numbers to TODO comments
3. Track completion in project board
```

### Add Ownership
```markdown
## Show TODO Ownership

For each TODO, show:
- Who added it (from git blame)
- When it was added
- Related commits or PRs
```

### Filter by Age
```markdown
## Highlight Old TODOs

Flag TODOs that are:
- Over 6 months old: ⚠️  Stale
- Over 1 year old: 🚨 Very old
- Over 2 years old: 💀 Ancient
```

## Common Issues

### Not finding all TODOs?

**Check:** Search pattern might be too strict
```yaml
# ❌ Too specific
grep "TODO:"

# ✅ More flexible
grep -i -E "(TODO|FIXME|HACK|BUG):"
```

### Finding too many false positives?

**Fix:** Add context to filter:
```markdown
## Filtering Strategy

Only include if:
- In a comment (// or /* */ or #)
- Followed by colon (:)
- Has actual text after it
```

### Results not organized well?

**Improve:** Add better categorization
```markdown
## Categories

By Priority:
- 🔴 Critical: FIXME, BUG, SECURITY
- 🟡 Important: TODO, HACK
- 🔵 Info: NOTE, OPTIMIZE

By Type:
- 🐛 Bugs
- ✨ Features
- ⚡ Performance
- 🔧 Refactoring
```

## Tips for Use

### For Project Overview
Ask: "Find all action items in the project"
- Gets complete picture
- Helps with sprint planning
- Identifies priorities

### For Specific Areas
Ask: "Find TODOs in the authentication code"
- Focus on one module
- Easier to act on
- Less overwhelming

### For Critical Issues
Ask: "Show me all FIXMEs and BUGs"
- Immediate action items
- Security concerns
- Quality issues

### For Code Quality
Ask: "Find all HACKs and technical debt"
- Identify shortcuts
- Plan refactoring
- Improve code quality

## Learning Opportunities

### Master Grep Tool
Learn how to:
- Search multiple file types
- Use regex patterns
- Filter results
- Find patterns across codebase

### Organize Information
Practice:
- Categorizing results
- Prioritizing findings
- Presenting data clearly
- Making information actionable

### Read-Only Analysis
Understand:
- Safe, non-destructive operations
- Analysis without modification
- Gathering information
- Reporting findings

## Real-World Workflows

### Sprint Planning
1. Find all TODOs
2. Categorize by feature area
3. Estimate effort
4. Add to sprint backlog

### Code Quality Review
1. Find all HACKs
2. Assess technical debt
3. Plan refactoring sprints
4. Track improvements

### Bug Triage
1. Find all FIXMEs and BUGs
2. Assess severity
3. Assign to team members
4. Track in issue tracker

### Documentation Audit
1. Find all DOC and NOTE comments
2. Identify missing docs
3. Update documentation
4. Remove outdated notes

## Next Steps

### Extend This Skill
- Add git blame integration to show authors
- Include time since TODO was added
- Link to related GitHub issues
- Generate reports

### Create Related Skills
- `issue-creator` - Create GitHub issues from TODOs
- `tech-debt-analyzer` - Analyze technical debt
- `code-quality-checker` - Check for code smells

### Combine With Other Skills
- Use with `comment-generator` to improve documentation
- Pair with code review workflows
- Integrate with project management tools

## Advanced Usage

### With Filters
"Find TODOs added in the last month"
"Show HACKs in components only"
"Find critical items in backend code"

### With Actions
"Find all TODOs and create issues for them"
"Show FIXMEs and estimate fix time"
"List technical debt and prioritize"

### With Reports
"Generate a TODO report for the team"
"Create a technical debt summary"
"Show action items by developer"

## Files

- `SKILL.md` - The skill file (copy this to `.claude/skills/`)
- `README.md` - This documentation

## Related Examples

- **comment-generator** - Adds documentation to code
- **calculator-helper** - Another read-only analysis skill
- See intermediate examples for integration with issue trackers

## Why This Pattern Works

### Single Responsibility
- Does one thing well
- Easy to understand
- Simple to maintain

### Immediate Value
- Helps with project management
- Identifies priorities
- No setup required

### Safe and Fast
- Read-only operations
- Quick to execute
- No side effects

### Educational
- Teaches Grep usage
- Shows result organization
- Demonstrates clear output formatting
