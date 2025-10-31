# Comment Generator Skill - Beginner Example

A simple skill that automatically generates code comments and docstrings.

## What This Example Teaches

- How to create a focused skill (one purpose)
- Writing clear skill descriptions
- Providing language-specific examples
- Tool restrictions (Read, Edit only)

## How to Use

### 1. Install the Skill

```bash
# Copy to your project
cp SKILL.md ~/.claude/skills/comment-generator.md

# Or for project-specific
cp SKILL.md your-project/.claude/skills/comment-generator.md
```

### 2. Try It Out

```bash
cd your-project
claude

# Then ask:
"Add comments to this function"
"Document my Python class"
"Add JSDoc to my JavaScript code"
```

### 3. Watch It Activate

The skill automatically activates when you mention:
- "add comments"
- "document code"
- "add docstrings"
- "explain with comments"

## Example Usage

**You:**
```
Add comments to this function:

function fibonacci(n) {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}
```

**Claude (using comment-generator skill):**
```javascript
/**
 * Calculates the nth Fibonacci number using recursion
 * @param {number} n - The position in the Fibonacci sequence (0-indexed)
 * @returns {number} The Fibonacci number at position n
 * @example
 * fibonacci(5) // Returns 5 (sequence: 0, 1, 1, 2, 3, 5)
 */
function fibonacci(n) {
  // Base case: first two numbers are 0 and 1
  if (n <= 1) return n;

  // Recursive case: sum of previous two numbers
  return fibonacci(n - 1) + fibonacci(n - 2);
}
```

## What Makes This a Good Beginner Example?

### 1. Single, Clear Purpose
- Does ONE thing: generates comments
- Easy to understand and test

### 2. Specific Description
```yaml
description: Generate code comments and docstrings. Use when user asks to "add comments", "document this code", "explain with comments", or "add docstrings".
```
- Lists exact trigger phrases
- Clear when to activate

### 3. Language Support
- Handles multiple languages
- Shows proper comment styles
- Adapts to context

### 4. Safe Tool Restrictions
```yaml
allowed-tools: [Read, Edit]
```
- Only reads files and edits them
- Can't run commands or access network
- Minimal permissions needed

## Customization Ideas

### Make it framework-specific:
```yaml
description: Generate React component JSDoc. Use when documenting React components.
```

### Add your team's style:
```markdown
## Our Comment Style

Always include:
1. Author name
2. Date created
3. Ticket number
```

### Support more languages:
```markdown
## Additional Languages

**Ruby:**
```ruby
# Description here
def method
end
```

**Go:**
```go
// Description here
func method() {}
```
```

## Common Issues

### Skill doesn't activate?

**Check:** Is your description specific enough?
```yaml
# ❌ Too vague
description: For comments

# ✅ Specific
description: Generate code comments. Use when user asks to "add comments" or "document code"
```

### Comments don't match your style?

**Fix:** Add style guidelines in the skill:
```markdown
## Our Style Guide

- Use imperative mood ("Calculate" not "Calculates")
- Always include examples for public APIs
- Maximum 80 characters per line
```

## Next Steps

### Learn More
- See how description affects activation
- Try modifying for your code style
- Add support for your favorite language

### Build On This
- Create `function-namer` skill
- Create `code-formatter` skill
- Combine into a `code-quality` skill

## Files

- `SKILL.md` - The skill file (copy this to `.claude/skills/`)
- `README.md` - This documentation
