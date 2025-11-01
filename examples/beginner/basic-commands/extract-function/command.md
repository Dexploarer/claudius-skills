Extract selected code into a new function with a meaningful name.

## Instructions

1. Ask the user to provide:
   - The code to extract (or current file/selection context)
   - Desired function name (or suggest one based on what the code does)
   - Programming language (or detect from file extension)

2. Analyze the code to extract:
   - Identify variables used (parameters)
   - Identify variables modified (return values)
   - Determine appropriate return type
   - Check for dependencies

3. Show the user the refactoring plan:
   - New function signature
   - Parameters needed
   - Return value
   - Where it will be placed

4. Create the extracted function:
   - Add appropriate function definition
   - Include parameters
   - Add return statement if needed
   - Add basic documentation comment

5. Replace original code with function call

6. Show before/after comparison

## Example Output

```
📦 Extract Function

Analyzing code block...

Code to extract:
  Lines 45-52 in src/utils.js
  Purpose: Validates email format

Detected:
  • Uses: email (parameter)
  • Returns: boolean
  • No side effects

Proposed function:
  function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

This will:
  1. Create new function above current location
  2. Replace lines 45-52 with: isValidEmail(email)
  3. Add JSDoc comment

Proceed with extraction? (yes/no)
```

## Language-Specific Formats

### JavaScript/TypeScript:
```javascript
/**
 * Brief description
 * @param {type} paramName - description
 * @returns {type} description
 */
function functionName(paramName) {
  // extracted code
  return result;
}
```

### Python:
```python
def function_name(param_name):
    """
    Brief description

    Args:
        param_name (type): description

    Returns:
        type: description
    """
    # extracted code
    return result
```

### Java:
```java
/**
 * Brief description
 * @param paramName description
 * @return description
 */
public ReturnType functionName(ParamType paramName) {
    // extracted code
    return result;
}
```

## Arguments

If using $ARGUMENTS:
- $1: Function name (optional - will suggest if not provided)
- $2: File path (optional - will use current file)

## Best Practices

- **Choose good names**: Function name should describe what it does
- **Keep it focused**: Extracted function should do one thing
- **Document it**: Add comment explaining purpose
- **Consider scope**: Place function in appropriate location
- **Maintain behavior**: Don't change what the code does

## Notes

- Always show before/after comparison
- Detect and include all necessary parameters
- Handle edge cases (closures, this binding, etc.)
- Suggest improvements if code can be simplified
