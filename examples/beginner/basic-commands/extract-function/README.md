# Extract Function - Slash Command

A simple slash command that helps you extract code into a well-named function with proper documentation.

## What It Does

This command helps refactor code by:
1. Taking a block of code you want to extract
2. Analyzing what parameters and return values are needed
3. Suggesting a meaningful function name
4. Creating the new function with documentation
5. Replacing the original code with a function call

## Installation

Copy the `command.md` file to your project's `.claude/commands/` directory:

```bash
cp command.md /path/to/your/project/.claude/commands/extract-function.md
```

## Usage

### Basic Usage

```bash
/extract-function
```

Then Claude will ask you for:
- The code to extract (or it will use current selection/context)
- The desired function name (or it will suggest one)
- The programming language

### With Arguments

You can also provide the function name directly:

```bash
/extract-function validateEmail
```

## Examples

### Example 1: JavaScript Email Validation

**Before:**
```javascript
function processUser(userData) {
  // Inline email validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(userData.email)) {
    throw new Error('Invalid email');
  }

  // Rest of processing...
}
```

**After running `/extract-function validateEmail`:**
```javascript
/**
 * Validates email format
 * @param {string} email - The email address to validate
 * @returns {boolean} True if email is valid
 */
function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function processUser(userData) {
  if (!validateEmail(userData.email)) {
    throw new Error('Invalid email');
  }

  // Rest of processing...
}
```

### Example 2: Python Data Processing

**Before:**
```python
def analyze_data(records):
    # Filter and transform
    filtered = [r for r in records if r['active'] and r['age'] >= 18]
    result = [{'name': r['name'], 'score': r['score'] * 1.1} for r in filtered]
    return result
```

**After running `/extract-function filter_adult_records`:**
```python
def filter_adult_records(records):
    """
    Filters records for active adults

    Args:
        records (list): List of record dictionaries

    Returns:
        list: Filtered records with adults only
    """
    return [r for r in records if r['active'] and r['age'] >= 18]

def analyze_data(records):
    filtered = filter_adult_records(records)
    result = [{'name': r['name'], 'score': r['score'] * 1.1} for r in filtered]
    return result
```

## What Gets Extracted

Claude will analyze and handle:
- **Parameters**: Variables used from outside the code block
- **Return values**: Variables that need to be returned
- **Side effects**: Warnings if the code modifies external state
- **Dependencies**: Any functions or imports needed
- **Documentation**: Proper comments/docstrings for the new function

## Supported Languages

- JavaScript/TypeScript (JSDoc format)
- Python (Google-style docstrings)
- Java (Javadoc format)
- Go (Go doc comments)
- Ruby (YARD format)
- C/C++ (Doxygen format)
- And more!

## When To Use

Use this command when you:
- Have repeated code that should be a function
- Want to make code more modular
- Need to improve code readability
- Are following the DRY (Don't Repeat Yourself) principle
- Want to make a code block testable

## Tips

1. **Choose descriptive names**: The function name should clearly describe what it does
2. **Keep functions focused**: Extract code that does one specific thing
3. **Consider scope**: Think about where the function should live (same file, utility file, etc.)
4. **Review the extraction**: Always review the suggested refactoring before accepting
5. **Test after extraction**: Make sure the behavior hasn't changed

## Best Practices

✅ **Do:**
- Extract code that is used multiple times
- Create functions with clear, single purposes
- Add meaningful documentation
- Keep function signatures simple

❌ **Don't:**
- Extract code that's only used once (unless it improves readability)
- Create functions with too many parameters (>4 is a code smell)
- Extract code with complex side effects
- Forget to update tests after extracting

## Troubleshooting

### "Too many parameters needed"

If the extraction would require many parameters, consider:
- Extracting a smaller piece of code
- Passing an object/struct instead of individual params
- Refactoring the surrounding code first

### "Side effects detected"

If the code modifies external state:
- Review if it should be extracted
- Consider making it pure by passing state as parameters
- Document the side effects clearly

### "Can't determine return type"

For languages requiring type annotations:
- Specify the return type manually
- Ensure the code has a clear return path
- Consider if multiple values should be returned as an object

## Related Commands

- `/refactor` - More comprehensive refactoring
- `/clean` - Clean up code without major changes
- `/review` - Review code quality before refactoring

## Learning More

For more advanced refactoring techniques:
- Check out Martin Fowler's "Refactoring" book
- Learn about the Extract Method pattern
- Study SOLID principles
- Practice with small examples first

## Customization

You can customize this command by editing `command.md`:
- Add your preferred documentation style
- Include team-specific naming conventions
- Add language-specific patterns
- Integrate with your code review process

## Examples in Different Languages

### TypeScript
```typescript
// Before
const data = items.filter(i => i.active).map(i => i.id);

// After
function getActiveItemIds(items: Item[]): string[] {
  return items.filter(i => i.active).map(i => i.id);
}

const data = getActiveItemIds(items);
```

### Java
```java
// Before
List<String> activeIds = items.stream()
  .filter(i -> i.isActive())
  .map(Item::getId)
  .collect(Collectors.toList());

// After
public List<String> getActiveItemIds(List<Item> items) {
  return items.stream()
    .filter(Item::isActive)
    .map(Item::getId)
    .collect(Collectors.toList());
}

List<String> activeIds = getActiveItemIds(items);
```

## Version History

- **v1.0**: Initial version with basic extraction
- Support for JavaScript, Python, Java
- Automatic parameter detection
- Basic documentation generation

---

**Note**: This is a beginner-friendly example. For production use, consider using dedicated refactoring tools in your IDE alongside this command.
