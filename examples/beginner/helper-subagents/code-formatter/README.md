# Code Formatter - Subagent

A specialized subagent that formats code to follow language best practices and style guides.

## What It Does

The Code Formatter subagent:
- Analyzes your code for formatting issues
- Applies language-specific formatting rules
- Fixes indentation, spacing, and line breaks
- Ensures consistent code style
- Follows established style guides (Prettier, PEP 8, etc.)
- Provides before/after comparisons

## Installation

Copy the `subagent.md` file to your project's `.claude/agents/` directory:

```bash
cp subagent.md /path/to/your/project/.claude/agents/code-formatter.md
```

## Usage

### Explicit Invocation

Tell Claude to use this subagent:

```bash
"Use the code-formatter subagent to format my code"
"Format this file using the code-formatter subagent"
```

### Automatic Activation

Claude may automatically use this subagent when you:
- Ask to "format this code"
- Say "fix the formatting"
- Request "make this code prettier"
- Mention "clean up indentation"

## Examples

### Example 1: JavaScript Formatting

**Before:**
```javascript
function calculateTotal(items){
const prices=items.map(item=>item.price)
const sum=prices.reduce((a,b)=>a+b,0)
const tax=sum*0.1
return sum+tax}
```

**After:**
```javascript
function calculateTotal(items) {
  const prices = items.map(item => item.price);
  const sum = prices.reduce((a, b) => a + b, 0);
  const tax = sum * 0.1;
  return sum + tax;
}
```

**Changes Applied:**
- ✓ Added proper indentation (2 spaces)
- ✓ Added spacing around operators
- ✓ Fixed line breaks
- ✓ Added semicolons
- ✓ Proper brace spacing

### Example 2: Python Formatting

**Before:**
```python
def process_data(items):
  filtered=[x for x in items if x>0]
  result=sum(filtered)
  return result
```

**After:**
```python
def process_data(items):
    filtered = [x for x in items if x > 0]
    result = sum(filtered)
    return result
```

**Changes Applied:**
- ✓ Fixed indentation (4 spaces for Python)
- ✓ Added spacing around operators
- ✓ Consistent spacing in list comprehension

### Example 3: CSS Formatting

**Before:**
```css
.button{background-color:#007bff;color:white;padding:10px 20px;border:none;}
.button:hover{background-color:#0056b3;}
```

**After:**
```css
.button {
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border: none;
}

.button:hover {
  background-color: #0056b3;
}
```

**Changes Applied:**
- ✓ Multi-line format
- ✓ Proper indentation
- ✓ Blank line between rules
- ✓ Consistent spacing

## Supported Languages

The subagent supports formatting for:

| Language | Style Guide | Indentation |
|----------|-------------|-------------|
| JavaScript/TypeScript | Prettier-style | 2 spaces |
| Python | PEP 8 | 4 spaces |
| Java | Google Java Style | 2 spaces |
| C/C++ | Google C++ Style | 2 spaces |
| Go | gofmt standard | Tabs |
| Ruby | RuboCop standard | 2 spaces |
| CSS/SCSS | Standard | 2 spaces |
| HTML | Standard | 2 spaces |
| JSON | Standard | 2 spaces |
| Markdown | Standard | N/A |

## What Gets Fixed

### Indentation Issues
```javascript
// ❌ Before
function test() {
if (true) {
console.log('test');
}
}

// ✅ After
function test() {
  if (true) {
    console.log('test');
  }
}
```

### Spacing Issues
```javascript
// ❌ Before
const sum=a+b;
const arr=[1,2,3];
if(x>5){doSomething();}

// ✅ After
const sum = a + b;
const arr = [1, 2, 3];
if (x > 5) {
  doSomething();
}
```

### Line Length Issues
```javascript
// ❌ Before
function veryLongFunctionName(parameterOne, parameterTwo, parameterThree, parameterFour) { return parameterOne + parameterTwo + parameterThree + parameterFour; }

// ✅ After
function veryLongFunctionName(
  parameterOne,
  parameterTwo,
  parameterThree,
  parameterFour
) {
  return parameterOne +
    parameterTwo +
    parameterThree +
    parameterFour;
}
```

### Trailing Whitespace
```javascript
// ❌ Before (spaces at end of lines)
const name = 'Alice';
const age = 30;

// ✅ After (no trailing spaces)
const name = 'Alice';
const age = 30;
```

## When To Use

Use this subagent when:
- Code looks messy or inconsistent
- You've copied code from different sources
- Setting up a new project
- Before code review
- Onboarding new team members
- After major refactoring
- Standardizing legacy code

## Why Use a Subagent?

**Benefits of using a subagent for formatting:**

1. **Separate Context**: Doesn't clutter your main conversation
2. **Focused Expertise**: Specialized only in formatting
3. **Safe Operations**: Read-only tools mean it can't accidentally break logic
4. **Consistent Results**: Follows strict formatting rules
5. **Detailed Reports**: Shows exactly what was changed

## Allowed Tools

This subagent only has access to:
- **Read**: Read files to format
- **Edit**: Apply formatting changes
- **Glob**: Find files to format

**No access to**: Bash, Web, or other potentially risky tools.

## Output Format

After formatting, you'll see:

```
📐 Code Formatting Complete

Files formatted: 3

Changes applied:
✓ Fixed indentation (42 lines)
✓ Added consistent spacing (28 locations)
✓ Broke long lines (5 lines)
✓ Removed trailing whitespace (15 lines)
✓ Standardized blank lines (8 locations)

Files:
✓ src/app.js - 45 formatting fixes
✓ src/utils.js - 23 formatting fixes
✓ src/config.js - 10 formatting fixes

All code now follows JavaScript Standard Style.
```

## Configuration Options

You can customize the subagent by editing `subagent.md`:

### Choose Style Guide
```markdown
Use ESLint style instead of Prettier:
- 4 spaces instead of 2
- No semicolons
- Single quotes
```

### Set Line Length
```markdown
Maximum line length: 80 characters (instead of 120)
```

### Specific Rules
```markdown
Additional rules:
- Always use trailing commas
- Sort imports alphabetically
- Group related code with blank lines
```

## Tips

1. **Run before commits**: Keep your codebase consistently formatted
2. **Format entire directories**: `"Format all files in src/ directory"`
3. **Check before submitting**: Format before code review
4. **Use with linters**: Run after this formats to check rules
5. **Team consistency**: Share this subagent config with your team

## Best Practices

✅ **Do:**
- Format before code review
- Use consistent style across project
- Run on new files immediately
- Format copied/pasted code
- Document your style choices

❌ **Don't:**
- Format without testing after
- Mix multiple style guides
- Format generated code without checking
- Change logic while formatting
- Format without team agreement

## Integration with Tools

### With Git
```bash
# Format before committing
"Use code-formatter to format staged files"
git add .
git commit -m "Format code"
```

### With Linters
```bash
# Format first, then lint
"Format all files"
npm run lint
```

### With CI/CD
```bash
# Check formatting in pipeline
npm run format:check
```

## Common Issues

### Issue 1: "Code doesn't run after formatting"
**Solution**: The formatter changed logic by accident. Review changes carefully. Use version control to revert.

### Issue 2: "Mixed tabs and spaces"
**Solution**: Tell the subagent your preference: `"Format using spaces only, no tabs"`

### Issue 3: "Comments got messed up"
**Solution**: Report to the subagent: `"Fix comment formatting in file.js"`

### Issue 4: "Too many changes"
**Solution**: Format one file at a time: `"Format only the UserController file"`

## Comparison with IDE Formatters

| Feature | IDE Formatter | This Subagent |
|---------|---------------|---------------|
| Speed | Instant | A few seconds |
| Explanation | None | Shows what changed |
| Customization | Config files | Natural language |
| Learning | No explanation | Explains changes |
| Multiple files | Varies | Easy with glob |

**Best practice**: Use both! IDE for quick fixes, subagent for understanding and batch operations.

## Examples for Different Scenarios

### Scenario 1: Single File
```bash
"Use the code-formatter subagent to format app.js"
```

### Scenario 2: Entire Directory
```bash
"Use the code-formatter subagent to format all JavaScript files in src/"
```

### Scenario 3: Multiple File Types
```bash
"Format all .js, .jsx, and .ts files in the components directory"
```

### Scenario 4: With Specific Rules
```bash
"Format this file using 4 spaces and no semicolons"
```

## Learning from the Subagent

Watch the changes it makes to learn:
- Proper indentation for your language
- Where to add spacing
- How to break long lines
- Comment formatting
- Blank line placement

## Advanced Usage

### Pre-commit Hook Integration
```bash
# Add to .claude/settings.json hooks
"PreToolUse": [
  {
    "pattern": "Bash.*git commit",
    "command": "echo 'Format staged files first!'",
    "description": "Remind to format before commit"
  }
]
```

### Batch Formatting Script
```bash
# Format everything at once
"Use code-formatter to format:
- All JS files in src/
- All Python files in scripts/
- All CSS files in styles/"
```

### Custom Style Guide
```bash
# Create project-specific formatting
"Format using our team style:
- 2 spaces
- Single quotes
- No semicolons
- Trailing commas"
```

## Related Tools

- **Prettier**: JavaScript/TypeScript/CSS formatter
- **Black**: Python code formatter
- **gofmt**: Go code formatter
- **rustfmt**: Rust code formatter
- **ESLint**: JavaScript linter (can auto-fix)
- **Pylint**: Python linter

## FAQ

**Q: Will this change my code's behavior?**
A: No! It only changes formatting (whitespace, indentation), not logic.

**Q: Can it format multiple languages at once?**
A: Yes, it handles each language with its appropriate rules.

**Q: Should I format before or after refactoring?**
A: Usually after. Refactor first, then format for cleanliness.

**Q: How is this different from Prettier/Black?**
A: Those are faster. This provides explanations and is more flexible.

**Q: Can I save my formatting preferences?**
A: Yes! Edit the subagent.md file to set your defaults.

**Q: Does it work with minified code?**
A: It can beautify minified code, but you should keep the minified version separate.

## Troubleshooting

### "Formatting created syntax error"
This shouldn't happen, but if it does:
1. Use `git diff` to see what changed
2. Undo with `git checkout -- <file>`
3. Report the issue
4. Format manually or use IDE

### "Some files weren't formatted"
Check:
- File permissions
- File is in specified scope
- Language is supported
- No syntax errors in original

### "Formatting style doesn't match team standards"
Customize the subagent:
1. Edit `subagent.md`
2. Add your team's style rules
3. Share updated config with team

## Version History

- **v1.0**: Initial formatter
  - JavaScript, Python, Java support
  - Basic indentation and spacing
  - Line length handling

---

**Remember**: Consistent formatting makes code easier to read, review, and maintain. Use this subagent to keep your codebase clean!
