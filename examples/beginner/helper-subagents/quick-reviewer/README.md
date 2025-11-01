# Quick Reviewer - Subagent

A fast code review subagent that checks for common issues, bugs, and improvements.

## What It Does

The Quick Reviewer subagent:
- Performs rapid code review
- Identifies common bugs and issues
- Checks code quality and readability
- Suggests improvements
- Looks for security concerns
- Validates best practices
- Provides actionable feedback

## Installation

Copy the `subagent.md` file to your project's `.claude/agents/` directory:

```bash
cp subagent.md /path/to/your/project/.claude/agents/quick-reviewer.md
```

## Usage

### Explicit Invocation

Tell Claude to use this subagent:

```bash
"Use the quick-reviewer subagent to review my changes"
"Quick review this file with the quick-reviewer"
```

### Automatic Activation

Claude may automatically use this subagent when you:
- Ask to "review this code"
- Say "check this for bugs"
- Request "look for issues in this code"
- Want a "quick code review"

## Example Reviews

### Example 1: JavaScript Bug Detection

**Code Submitted:**
```javascript
function calculateDiscount(price, discount) {
  const discountAmount = price * discount;
  const finalPrice = price - discountAmount;
  return finalPrice;
}

const total = calculateDiscount(100, 50);
```

**Review Output:**
```
🔍 Quick Code Review - calculateDiscount

Issues Found: 2

🐛 BUG (High Priority):
  Line 6: calculateDiscount(100, 50)

  Issue: Discount value should be a percentage (0-1), not 50
  This will result in a negative price: 100 - (100 * 50) = -4900

  Fix: Use 0.5 instead of 50
  const total = calculateDiscount(100, 0.5);

⚠️  IMPROVEMENT (Medium):
  Line 1-4: calculateDiscount function

  Issue: No input validation

  Suggestion: Add validation for edge cases:
  - Check if price is positive
  - Check if discount is between 0 and 1
  - Handle null/undefined inputs

  Example:
  function calculateDiscount(price, discount) {
    if (price < 0 || discount < 0 || discount > 1) {
      throw new Error('Invalid input');
    }
    // rest of code...
  }

✅ Good: Function name is clear and descriptive
✅ Good: Logic is straightforward and easy to follow
```

### Example 2: Python Code Quality

**Code Submitted:**
```python
def get_user_data(id):
    data = database.query(id)
    return data
```

**Review Output:**
```
🔍 Quick Code Review - get_user_data

Issues Found: 4

⚠️  STYLE (Low):
  Line 1: Parameter name 'id'

  Issue: 'id' shadows Python built-in function

  Fix: Use a different name like 'user_id':
  def get_user_data(user_id):

🐛 BUG (High):
  Line 2: database.query(id)

  Issue: No error handling
  What if database connection fails?
  What if user doesn't exist?

  Fix: Add try/except:
  try:
      data = database.query(user_id)
  except DatabaseError:
      return None

📝 MISSING (Medium):
  Line 1: No docstring

  Add documentation:
  def get_user_data(user_id):
      """
      Retrieves user data from database.

      Args:
          user_id (int): The user's ID

      Returns:
          dict: User data or None if not found
      """

🔒 SECURITY (Medium):
  Line 2: Direct database query

  Issue: Potential SQL injection if 'id' comes from user input

  Fix: Use parameterized queries:
  data = database.query("SELECT * FROM users WHERE id = ?", user_id)
```

### Example 3: React Component Review

**Code Submitted:**
```jsx
function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('/api/users')
      .then(res => res.json())
      .then(data => setUsers(data));
  });

  return (
    <div>
      {users.map(user => (
        <div>{user.name}</div>
      ))}
    </div>
  );
}
```

**Review Output:**
```
🔍 Quick Code Review - UserList Component

Issues Found: 4

🐛 BUG (High):
  Line 4-8: useEffect without dependency array

  Issue: This creates an infinite loop!
  Effect runs on every render → updates state → causes re-render → repeat

  Fix: Add empty dependency array:
  useEffect(() => {
    // ...
  }, []); // ← Add this!

⚠️  MISSING (High):
  Line 5-7: No error handling

  Issue: What if API request fails?
  User sees nothing, no error message

  Fix: Add .catch():
  fetch('/api/users')
    .then(res => res.json())
    .then(data => setUsers(data))
    .catch(err => console.error(err));

⚠️  MISSING (Medium):
  Line 13: map() without key prop

  Issue: React warning in console
  Poor performance on re-renders

  Fix: Add unique key:
  {users.map(user => (
    <div key={user.id}>{user.name}</div>
  ))}

💡 IMPROVEMENT (Low):
  Component lacks loading state

  Suggestion: Show loading indicator while fetching:
  const [loading, setLoading] = useState(true);

  if (loading) return <div>Loading...</div>;
```

## What Gets Reviewed

The subagent checks for:

### 🐛 Bugs
- Null/undefined errors
- Off-by-one errors
- Infinite loops
- Type mismatches
- Logic errors

### 🔒 Security
- SQL injection
- XSS vulnerabilities
- Hardcoded secrets
- Insecure dependencies
- Authorization issues

### ⚠️ Code Quality
- Naming conventions
- Code duplication
- Complex functions
- Missing error handling
- Poor readability

### 📝 Documentation
- Missing comments
- No function documentation
- Unclear variable names
- No README/docs

### 💡 Best Practices
- Language idioms
- Framework patterns
- Performance issues
- Maintainability
- Testing coverage

## Review Priorities

Issues are categorized by severity:

| Priority | Description | Examples |
|----------|-------------|----------|
| 🔴 **High** | Bugs that will break code | Null errors, infinite loops |
| 🟡 **Medium** | Issues that should be fixed | Missing validation, poor error handling |
| 🟢 **Low** | Nice-to-have improvements | Naming, comments, style |
| ℹ️ **Info** | Suggestions and tips | Alternative approaches, optimizations |

## When To Use

Use this subagent:
- **Before committing** - Catch issues early
- **After writing code** - Quick sanity check
- **Before code review** - Fix obvious issues first
- **Learning** - Understand common mistakes
- **Refactoring** - Ensure nothing broke
- **Onboarding** - Learn team standards

## Why Use a Subagent?

**Benefits:**

1. **Separate Context**: Review doesn't clutter main conversation
2. **Focused Analysis**: Dedicated to finding issues
3. **Read-Only**: Can't accidentally modify code
4. **Fast Feedback**: Quick turnaround
5. **Consistent**: Same standards every time
6. **Learning Tool**: Explains why issues matter

## Allowed Tools

This subagent only has access to:
- **Read**: Read files to review
- **Glob**: Find related files
- **Grep**: Search for patterns

**No access to**: Edit, Bash, Web, or modification tools.

This ensures the review is purely analytical and safe.

## Output Format

```
🔍 Quick Code Review - [File/Function Name]

Issues Found: [count]

[For each issue:]
[Emoji] [CATEGORY] ([Priority]):
  Line [X]: [Location]

  Issue: [What's wrong]
  [Why it matters]

  Fix: [How to fix it]
  [Code example if helpful]

✅ Good: [What's done well]
✅ Good: [Other positive aspects]

📊 Summary:
  - Bugs: [count]
  - Security: [count]
  - Quality: [count]
  - Documentation: [count]

Overall: [Rating]
```

## Configuration

You can customize the review by editing `subagent.md`:

### Set Review Depth
```markdown
Focus on:
- Critical bugs only (fast review)
- Bugs + Security (standard)
- Everything including style (thorough)
```

### Language-Specific Rules
```markdown
For Python:
- Enforce PEP 8
- Check for type hints
- Validate docstrings

For JavaScript:
- Check for === instead of ==
- Validate async/await usage
- Look for missing error handling
```

### Team Standards
```markdown
Team rules:
- Functions must have JSDoc
- No console.log in production
- All API calls need try/catch
```

## Tips

1. **Review early and often** - Catch issues while code is fresh
2. **Don't take it personally** - Reviews help improve code
3. **Learn from patterns** - Notice recurring issues
4. **Fix high priority first** - Focus on bugs before style
5. **Run tests after fixes** - Ensure fixes didn't break anything

## Best Practices

✅ **Do:**
- Review before committing
- Address high priority issues
- Learn from feedback
- Share review with team
- Use for learning

❌ **Don't:**
- Ignore security warnings
- Skip reviews to save time
- Only fix what reviewer sees
- Review without testing after
- Argue with every suggestion

## Comparison with Human Reviews

| Aspect | This Subagent | Human Reviewer |
|--------|---------------|----------------|
| Speed | Seconds | Hours/Days |
| Availability | Always | Limited |
| Consistency | Same standards | Varies |
| Depth | Common issues | Deep analysis |
| Context | Limited | Full understanding |
| Learning | Explains issues | May assume knowledge |

**Best approach**: Use both! Subagent for quick checks, humans for architecture and complex logic.

## Common Findings

### Finding 1: Missing Error Handling
```javascript
// ❌ Common issue
const data = await fetchData();

// ✅ Better
try {
  const data = await fetchData();
} catch (error) {
  console.error('Failed to fetch:', error);
}
```

### Finding 2: No Input Validation
```javascript
// ❌ Common issue
function divide(a, b) {
  return a / b;
}

// ✅ Better
function divide(a, b) {
  if (b === 0) throw new Error('Division by zero');
  return a / b;
}
```

### Finding 3: Hardcoded Values
```javascript
// ❌ Common issue
const API_KEY = 'abc123';

// ✅ Better
const API_KEY = process.env.API_KEY;
```

## Integration Examples

### With Git Workflow
```bash
# Review before commit
git add .
"Use quick-reviewer to review staged changes"
# Fix issues
git commit -m "Fix issues from review"
```

### With Pull Requests
```bash
# Review before creating PR
"Review all changes in this branch"
# Fix issues
# Then create PR
```

### With CI/CD
```bash
# Add review step to pipeline
- name: Code Review
  run: claude-review --quick
```

## Learning from Reviews

Track patterns in feedback:
- Do you often forget error handling?
- Are there common security issues?
- Do you need better naming?

Use this awareness to improve!

## Advanced Usage

### Review Specific Aspects
```bash
"Review for security issues only"
"Check for performance problems"
"Look for React best practices"
```

### Comparative Review
```bash
"Review my changes compared to main branch"
```

### Batch Review
```bash
"Review all modified files"
```

## Troubleshooting

### "Too many false positives"
Adjust sensitivity in subagent.md:
```markdown
Focus on:
- High severity only
- Confirmed bugs only
```

### "Missing real issues"
Run a thorough review:
```bash
"Use quick-reviewer for deep analysis"
```

### "Don't understand feedback"
Ask for clarification:
```bash
"Explain why [issue] is a problem"
```

## Related Tools

- **ESLint**: JavaScript linter
- **Pylint**: Python linter
- **SonarQube**: Code quality platform
- **CodeClimate**: Automated code review
- **GitHub CodeQL**: Security analysis

## FAQ

**Q: How long does a review take?**
A: Typically 10-30 seconds depending on file size.

**Q: Can it review multiple files at once?**
A: Yes! "Review all files in src/ directory"

**Q: Does it understand my project's context?**
A: It focuses on general best practices. For project-specific rules, create a custom subagent.

**Q: Will it catch all bugs?**
A: No tool catches everything. Use as one layer of quality checking.

**Q: Can I ignore certain warnings?**
A: Yes, you can customize what it checks for.

## Examples for Different Languages

### Python Review Focus
- Type hints
- Docstrings
- PEP 8 compliance
- Common Python pitfalls

### JavaScript/TypeScript Review Focus
- Async/await usage
- Promise handling
- Type safety (TS)
- React best practices

### Java Review Focus
- Exception handling
- Null safety
- Stream API usage
- OOP principles

---

**Remember**: Code review is about learning and improving. Use this subagent to catch issues early and become a better developer!
