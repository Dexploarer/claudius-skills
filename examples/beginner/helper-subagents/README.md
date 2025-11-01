# Helper Subagents - Beginner Examples

Specialized AI assistants that handle specific tasks autonomously.

## Available Examples

### 1. Code Formatter
**Location:** `code-formatter/`
**Purpose:** Formats code according to language best practices
**Use:** Delegate formatting tasks to maintain consistency
**Tools:** Read, Edit, Glob

### 2. Quick Reviewer
**Location:** `quick-reviewer/`
**Purpose:** Fast code review for common issues and bugs
**Use:** Get quick feedback before formal review
**Tools:** Read, Grep, Glob

## What Are Subagents?

Subagents are specialized AI assistants that:
- **Focus** on specific tasks
- **Work autonomously** once delegated to
- **Have limited tools** (for safety and focus)
- **Report back** with results
- **Free you up** to handle other things

Think of them as junior developers you can delegate to!

## How to Use These Examples

### 1. Install Subagents

```bash
# Copy to your Claude config
mkdir -p ~/.claude/subagents
cp code-formatter/subagent.md ~/.claude/subagents/
cp quick-reviewer/subagent.md ~/.claude/subagents/

# Or project-specific
mkdir -p .claude/subagents
cp code-formatter/subagent.md .claude/subagents/
cp quick-reviewer/subagent.md .claude/subagents/
```

### 2. Delegate Tasks to Them

```bash
cd your-project
claude

# Delegate formatting
"Format all the JavaScript files in src/"
# Claude: "I'll delegate this to the code-formatter subagent"
# Subagent: [Formats files and reports back]

# Delegate review
"Review the user authentication code"
# Claude: "Let me have the quick-reviewer check this"
# Subagent: [Reviews and provides feedback]
```

### 3. They Work and Report Back

Subagents work independently and return with results.

## Example Workflows

### Workflow 1: Pre-Commit Cleanup

```
You: "I want to commit my changes, but clean everything up first"

Claude: "I'll coordinate this:
  1. Code formatter will fix formatting
  2. Quick reviewer will check for issues
  3. Then we'll commit

  Delegating to code-formatter..."

Code Formatter: "Formatted 5 files, fixed 47 issues"

Claude: "Great! Now delegating to quick-reviewer..."

Quick Reviewer: "Found 2 important issues:
  - Missing error handling in login.js:45
  - Potential null reference in profile.js:89

  Fix these before committing?"

You: "Yes, let me fix those"

[After fixes]

You: "Now commit"

Claude: "All clean! Committing..."
```

### Workflow 2: Feature Development

```
You: "I just built a new user dashboard feature"

Claude: "Excellent! Let me have the quick-reviewer check it"

Quick Reviewer: "Reviewing dashboard code...

✅ Good:
  - Well-structured components
  - Good error handling
  - Clear naming

💡 Suggestions:
  - Consider extracting data fetching logic
  - Add loading states
  - Cache API responses

Overall: Solid implementation!"

Claude: "Looks good! Want me to format it consistently?"

You: "Yes please"

Claude: "Delegating to code-formatter..."

Code Formatter: "Formatted 3 files to match project style"

Claude: "All set! Ready to push."
```

## What Makes a Good Subagent?

### 1. Focused Purpose
❌ "Handles all code tasks"
✅ "Formats code to follow style guides"

### 2. Clear Scope
```markdown
---
name: code-formatter
description: Formats code according to language best practices
allowed-tools: [Read, Edit, Glob]
---
```

### 3. Autonomous
- Can work independently
- Doesn't need constant guidance
- Makes reasonable decisions
- Reports back with results

### 4. Well-Documented
- Clear instructions
- Examples of what it does
- Edge cases handled
- Success criteria defined

### 5. Safe Tool Access
```yaml
# ✅ Good: Limited to what's needed
allowed-tools: [Read, Edit]

# ❌ Bad: Overly broad
allowed-tools: [*]
```

## Customization Ideas

### Project-Specific Formatter
```markdown
---
name: our-code-formatter
description: Formats code following OUR company style guide
---

## Our Style Rules

- 4 spaces (not 2)
- Semicolons required
- Single quotes always
- Max line length: 100
- Always use const/let (never var)
```

### Domain-Specific Reviewer
```markdown
---
name: api-reviewer
description: Reviews API endpoints for best practices
---

## API-Specific Checks

- RESTful naming
- Proper HTTP methods
- Status codes correct
- Error responses consistent
- Authentication present
- Rate limiting considered
```

### Language-Specific Agents
```markdown
---
name: python-linter
description: Checks Python code for PEP 8 compliance
---

---
name: typescript-checker
description: Ensures TypeScript types are properly used
---
```

## Common Issues

### Subagent Doesn't Activate?

**Check:**
1. File is in `.claude/subagents/`
2. File extension is `.md`
3. Has proper frontmatter (---  block)
4. Has `name`, `type`, `description`
5. Instructions are clear

### Wrong Subagent Activates?

**Fix:**
- Make descriptions more specific
- Use clear trigger words
- Avoid overlap between subagents

### Subagent Does Too Much?

**Solution:**
- Narrow the scope
- Limit tool access
- Split into multiple subagents
- Add clearer boundaries

## Best Practices

### For Creating Subagents

**Start Small:**
- One clear purpose
- Limited scope
- Minimal tools needed
- Well-tested

**Document Thoroughly:**
- What it does
- When to use it
- What tools it needs
- Example outputs

**Set Boundaries:**
```markdown
## What This Subagent Does

✅ Formats code
✅ Fixes indentation
✅ Normalizes spacing

❌ Does NOT refactor logic
❌ Does NOT rename variables
❌ Does NOT modify behavior
```

### For Using Subagents

**Know When to Delegate:**
- Repetitive tasks
- Well-defined scope
- Can work independently
- Results are verifiable

**Don't Delegate:**
- Critical decisions
- Ambiguous requirements
- Tasks needing context
- Creative problem-solving

**Review Results:**
- Check subagent's work
- Verify changes
- Test if needed
- Learn from approach

## Real-World Workflows

### Code Quality Workflow
```
1. Write new feature
2. Delegate to code-formatter
3. Delegate to quick-reviewer
4. Fix any issues found
5. Commit and push
```

### Refactoring Workflow
```
1. Identify code to refactor
2. Quick-reviewer analyzes issues
3. You refactor based on feedback
4. Code-formatter cleans it up
5. Quick-reviewer verifies improvements
```

### Pre-PR Workflow
```
1. Finish feature
2. Code-formatter ensures consistency
3. Quick-reviewer catches issues
4. Fix critical/important issues
5. Create pull request
```

## Learning Opportunities

### Understanding Delegation
- When to delegate
- How to give clear instructions
- Verifying results
- Iterative improvement

### Task Decomposition
- Breaking down complex tasks
- Identifying subtasks
- Parallel vs sequential work
- Coordination between agents

### Specialization Benefits
- Focused tools
- Domain expertise
- Consistent results
- Scalability

## Related Examples

- **simple-skills** - Always-on capabilities
- **basic-commands** - User-triggered actions
- **safety-hooks** - Automated guards
- See intermediate examples for advanced subagents

## Next Steps

### Extend These Subagents
- Add more language support
- Custom style rules
- Integration with linters
- Automated fixes

### Create New Subagents
- `test-generator` - Creates test cases
- `doc-writer` - Generates documentation
- `dependency-updater` - Updates packages
- `performance-analyzer` - Finds bottlenecks

### Build Workflows
- Chain multiple subagents
- Create standard processes
- Automate common tasks
- Team collaboration

## Subagent vs Other Features

### When to Use Subagent
```
✅ Focused, repeatable task
✅ Can work autonomously
✅ Clear success criteria
✅ Benefits from specialization

Example: Code formatting, code review
```

### When to Use Skill
```
✅ Always-on capability
✅ Activates on keywords
✅ Augments Claude's abilities
✅ Contextual assistance

Example: Comment generator, calculator
```

### When to Use Command
```
✅ Explicit user invocation
✅ Specific workflow step
✅ Clear start and end
✅ Discrete action

Example: Git commit, deploy
```

### When to Use Hook
```
✅ Event-driven trigger
✅ Safety check
✅ Validation
✅ Policy enforcement

Example: Prevent main push, check secrets
```

## Files Structure

```
helper-subagents/
├── README.md (this file)
├── code-formatter/
│   └── subagent.md
└── quick-reviewer/
    └── subagent.md
```

## Important Concepts

### Delegation
```
You → Claude → Subagent → Results → Claude → You
```

Claude decides when to delegate based on:
- Task type
- Subagent capabilities
- Current context
- Efficiency

### Autonomy
```
Subagents work independently:
1. Receive task
2. Plan approach
3. Execute
4. Report results
```

### Specialization
```
General Claude: Knows everything, does everything
Subagent: Knows one thing deeply, does it expertly
```

## Success Metrics

Good subagent when:
✓ Completes tasks correctly
✓ Works without supervision
✓ Returns helpful results
✓ Saves you time
✓ Consistent quality
✓ Clear communication

## Why Use Subagents?

### Efficiency
- Parallel work
- Specialized focus
- Faster execution
- Consistent results

### Quality
- Expertise in domain
- Thorough checking
- Best practices
- Attention to detail

### Scalability
- Handle multiple tasks
- Reusable workflows
- Team collaboration
- Process automation

## From Real Users

> "The code-formatter subagent saved me hours of manual formatting.
> It just works consistently across all files." - Frontend Developer

> "Quick-reviewer catches things I miss when I'm tired.
> It's like having a fresh pair of eyes." - Backend Developer

> "Delegating to subagents lets me focus on architecture while
> they handle the details." - Tech Lead

Start using subagents and multiply your productivity! 🚀

## Tips for Success

### Start Simple
- Use provided examples
- Learn how they work
- Observe the delegation
- Build from there

### Customize Gradually
- Start with defaults
- Adjust one thing at a time
- Test thoroughly
- Document changes

### Build Library
- Create subagents for your common tasks
- Share with team
- Refine based on usage
- Grow your toolkit

Your AI development team awaits! 🤖
