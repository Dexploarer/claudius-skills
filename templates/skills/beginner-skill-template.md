---
name: my-simple-skill
description: Generate code comments when user asks to "add comments", "document code", or "explain with comments"
allowed-tools: [Read, Edit]
---

# My Simple Skill

A focused skill that does ONE thing really well.

## When to Use

This skill activates when the user asks to:
- "Add comments to this code"
- "Document this function"
- "Explain this code with comments"

## What This Skill Does

This skill:
1. Reads the code you want to comment
2. Analyzes what the code does
3. Adds clear, helpful comments
4. Updates the file with the commented version

## Instructions

### Step 1: Understand the Code

First, read and understand what the code does:
- What is the main purpose?
- What are the inputs and outputs?
- Are there any complex or tricky parts?

### Step 2: Identify Language

Detect the programming language to use the right comment style:
- **JavaScript/TypeScript**: `/* */` and `//`
- **Python**: `"""` or `#`
- **Java**: `/** */` and `//`
- **Other**: Adapt appropriately

### Step 3: Add Comments

Add comments that:
- ✅ Explain WHY, not just WHAT
- ✅ Are concise but clear
- ✅ Follow language conventions
- ✅ Add value (don't state obvious)

Example:
```javascript
/**
 * Calculates the factorial of a number
 * @param {number} n - The number to calculate factorial for
 * @returns {number} The factorial result
 */
function factorial(n) {
  // Base case: factorial of 0 or 1 is 1
  if (n <= 1) return 1;

  // Recursive case: n! = n * (n-1)!
  return n * factorial(n - 1);
}
```

### Step 4: Apply Changes

Use the Edit tool to update the file with the commented version.

## Best Practices

- Keep comments helpful, not redundant
- Update comments when code changes
- Use proper formatting for the language
- Don't over-comment simple code
- Focus on complex logic

## Examples

### Example 1: Simple Function

**Before:**
```python
def add(a, b):
    return a + b
```

**After:**
```python
def add(a, b):
    """
    Adds two numbers together.

    Args:
        a (int|float): First number
        b (int|float): Second number

    Returns:
        int|float: Sum of a and b
    """
    return a + b
```

### Example 2: Complex Logic

**Before:**
```javascript
function isPrime(num) {
  if (num <= 1) return false;
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) return false;
  }
  return true;
}
```

**After:**
```javascript
/**
 * Checks if a number is prime
 * Uses trial division up to square root for efficiency
 * @param {number} num - The number to check
 * @returns {boolean} True if prime, false otherwise
 */
function isPrime(num) {
  // Numbers <= 1 are not prime by definition
  if (num <= 1) return false;

  // Check divisibility up to square root (optimization)
  // If num has a divisor, it must be <= sqrt(num)
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) return false;
  }

  return true;
}
```

## Common Mistakes to Avoid

❌ **Don't state the obvious:**
```javascript
// Set x to 5
x = 5;
```

❌ **Don't copy code in comments:**
```javascript
// Return a + b
return a + b;
```

✅ **Do explain the "why":**
```javascript
// Use square root optimization to reduce checks from O(n) to O(√n)
for (let i = 2; i * i <= num; i++) {
```

## Tips

💡 **For Beginners:** Start by commenting function purposes and parameters

💡 **For Complex Code:** Add inline comments to explain tricky logic

💡 **For APIs:** Always add full documentation with examples

## When NOT to Use This Skill

This skill is NOT needed for:
- Already well-commented code
- Self-explanatory simple code
- Temporary test code

## Customization

To customize this skill for your style:

1. **Add your comment format:**
   ```markdown
   ### Our Team's Comment Style
   - Always include: Author, Date, Ticket #
   - Use present tense
   - Max 80 characters per line
   ```

2. **Add language-specific rules:**
   ```markdown
   ### For Python
   - Use Google-style docstrings
   - Include type hints in docstring
   ```

3. **Add domain-specific requirements:**
   ```markdown
   ### For API Endpoints
   - Document HTTP method
   - List all possible status codes
   - Include example request/response
   ```

## Success Criteria

A successful comment should:
- ✅ Be understandable by someone unfamiliar with the code
- ✅ Explain the "why" behind non-obvious decisions
- ✅ Follow language/team conventions
- ✅ Add real value (not just noise)

## Notes

- This skill only READS and EDITS files (no Bash or network access)
- Comments are added in-place (file is modified)
- Always review generated comments before accepting
- Adjust verbosity based on code complexity
