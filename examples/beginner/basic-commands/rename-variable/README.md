# Rename Variable - Slash Command

A slash command that helps you safely rename variables, functions, or other identifiers consistently across your codebase.

## What It Does

This command helps you rename identifiers by:
1. Finding all occurrences of the old name
2. Analyzing the scope (file, module, or global)
3. Checking for naming conflicts
4. Renaming consistently across all locations
5. Updating any related comments or documentation
6. Preserving code functionality

## Installation

Copy the `command.md` file to your project's `.claude/commands/` directory:

```bash
cp command.md /path/to/your/project/.claude/commands/rename-variable.md
```

## Usage

### Basic Usage

```bash
/rename-variable
```

Claude will ask for:
- The old name (current identifier)
- The new name (desired identifier)
- The scope (file, directory, or entire project)

### With Arguments

You can provide names directly:

```bash
/rename-variable getData fetchUserData
```

This renames `getData` to `fetchUserData` in the current file.

## Examples

### Example 1: Renaming a Function (JavaScript)

**Before:**
```javascript
// user.js
function getData(id) {
  return fetch(`/api/users/${id}`);
}

// app.js
import { getData } from './user.js';

const user = await getData(123);
```

**After running `/rename-variable getData fetchUserData`:**
```javascript
// user.js
function fetchUserData(id) {
  return fetch(`/api/users/${id}`);
}

// app.js
import { fetchUserData } from './user.js';

const user = await fetchUserData(123);
```

### Example 2: Renaming a Variable (Python)

**Before:**
```python
def process_data():
    x = load_file()  # Unclear name
    filtered_x = [item for item in x if item.active]
    return sum(filtered_x)
```

**After running `/rename-variable x records`:**
```python
def process_data():
    records = load_file()  # Clear name
    filtered_records = [item for item in records if item.active]
    return sum(filtered_records)
```

### Example 3: Renaming a Class (Java)

**Before:**
```java
public class Mgr {  // Unclear abbreviation
    private String name;

    public Mgr(String name) {
        this.name = name;
    }
}

// Usage
Mgr manager = new Mgr("Alice");
```

**After running `/rename-variable Mgr UserManager`:**
```java
public class UserManager {  // Clear, descriptive name
    private String name;

    public UserManager(String name) {
        this.name = name;
    }
}

// Usage
UserManager manager = new UserManager("Alice");
```

## What Gets Renamed

Claude will find and rename:
- **Variable declarations**: `let oldName = ...`
- **Function definitions**: `function oldName() { }`
- **Function calls**: `oldName(args)`
- **Class names**: `class OldName { }`
- **Method names**: `obj.oldName()`
- **Imports/exports**: `import { oldName }`
- **Type references**: `oldName: Type`
- **Comments**: References in comments
- **Documentation**: JSDoc, docstrings, etc.

## Scope Options

### File Scope (Default)
Renames only in the current file.

**Use when:**
- Variable is local to one file
- Function is private/internal
- Testing the rename first

### Directory Scope
Renames in current directory and subdirectories.

**Use when:**
- Module-level refactoring
- Related files in same folder
- Feature-specific changes

### Project Scope
Renames across entire project.

**Use when:**
- Public API changes
- Global function/class names
- Project-wide refactoring

## Smart Renaming Features

### Scope Awareness
```javascript
function test() {
  let count = 0;  // Local scope
}

function other() {
  let count = 10;  // Different scope - won't be renamed
}
```

### Case Sensitivity
```javascript
const userName = "Alice";     // Will rename
const USERNAME = "DEFAULT";   // Won't rename (different case)
```

### Partial Match Prevention
```javascript
const count = 5;          // Will rename 'count'
const counter = 10;       // Won't rename 'counter'
const recount = () => {}; // Won't rename 'recount'
```

### String Literals (Optional)
```javascript
const name = "oldName";  // Can optionally rename in strings
```

## Naming Conventions

The command suggests names following conventions:

| Language | Variables | Functions | Classes | Constants |
|----------|-----------|-----------|---------|-----------|
| JavaScript | camelCase | camelCase | PascalCase | UPPER_CASE |
| Python | snake_case | snake_case | PascalCase | UPPER_CASE |
| Java | camelCase | camelCase | PascalCase | UPPER_CASE |
| Go | camelCase | camelCase | PascalCase | camelCase |
| Ruby | snake_case | snake_case | PascalCase | UPPER_CASE |

## Safety Checks

Before renaming, Claude checks for:

### 1. Name Conflicts
```javascript
function calculateTotal() { }
function total() { }  // Conflict if renaming to 'total'
```

### 2. Reserved Keywords
```javascript
let class = 5;  // Can't use 'class' in JavaScript
```

### 3. Scope Issues
```javascript
let user = "global";

function test() {
  let user = "local";  // Different scope
}
```

### 4. Breaking Changes
```javascript
// Public API
export function getData() { }  // Renaming breaks external users!
```

## Preview Before Applying

Claude will show you:
- Number of occurrences found
- Files that will be modified
- Example changes
- Potential conflicts
- Breaking changes warning

**Example Preview:**
```
🔍 Found 15 occurrences of 'getData' in 5 files:

Files to modify:
  ✓ src/api/users.js (3 occurrences)
  ✓ src/api/posts.js (2 occurrences)
  ✓ src/components/UserList.js (5 occurrences)
  ✓ src/components/Dashboard.js (4 occurrences)
  ✓ tests/api.test.js (1 occurrence)

Example changes:
  - function getData() { ... }
  + function fetchUserData() { ... }

  - const data = await getData(id);
  + const data = await fetchUserData(id);

⚠️  WARNING: This function is exported
    Renaming will affect external imports

Proceed with rename? (yes/no)
```

## When To Use

Use this command when:
- Variable name is unclear (e.g., `x`, `data`, `temp`)
- Function name doesn't match what it does
- Following naming conventions
- Making code more readable
- Refactoring for clarity
- Fixing naming inconsistencies

## Tips

1. **Choose descriptive names**: Name should explain purpose
2. **Follow conventions**: Use language-appropriate style
3. **Preview first**: Always review changes before applying
4. **Start small**: Test on one file before project-wide
5. **Run tests after**: Ensure nothing broke
6. **Update docs**: Check if documentation needs updating

## Best Practices

✅ **Good Naming Examples:**
```javascript
// ❌ Bad → ✅ Good
const d = new Date();           → const currentDate = new Date();
function proc(x) { }            → function processOrder(order) { }
let temp = calcVal();           → let totalPrice = calculatePrice();
const arr = getStuff();         → const userList = getUsers();
```

✅ **Do:**
- Use clear, descriptive names
- Follow language conventions
- Keep names concise but meaningful
- Update related comments
- Test after renaming

❌ **Don't:**
- Use single-letter names (except loop counters)
- Use abbreviations unless standard (URL, API)
- Make names too long (>30 chars)
- Rename without reviewing scope
- Forget to run tests after

## Common Use Cases

### 1. Clarifying Purpose
```javascript
// Before: What does 'process' do?
function process(items) { }

// After: Clear what it does
function filterActiveUsers(items) { }
```

### 2. Fixing Typos
```javascript
// Before: Typo in name
function caluclateTotal() { }

// After: Fixed
function calculateTotal() { }
```

### 3. Following Standards
```python
# Before: Not following Python conventions
def GetData(): pass

# After: Following conventions
def get_data(): pass
```

### 4. Making Code Self-Documenting
```javascript
// Before: Need comment to understand
let x = parseFloat(input);  // User's score

// After: Name explains itself
let userScore = parseFloat(input);
```

## Troubleshooting

### "Too many occurrences found"

If there are hundreds of matches:
- Start with file scope first
- Check if name is too generic
- Consider if you have the right identifier

### "Name conflict detected"

If new name already exists:
- Choose a different name
- Review the conflicting identifier
- Consider renaming the conflict too

### "Unable to determine scope"

If scope is unclear:
- Specify scope explicitly
- Review the code structure
- Consider splitting into multiple renames

### "Changed but tests failing"

If tests break after rename:
- Check test files were updated
- Look for string literals with old name
- Review mocked/stubbed code
- Check configuration files

## Related Commands

- `/refactor` - Broader refactoring operations
- `/extract-function` - Extract code into a function
- `/clean` - Clean up code formatting
- `/review` - Review code quality

## Language-Specific Examples

### TypeScript
```typescript
// Rename with type updates
interface User { }
const users: User[] = [];

// After renaming User → UserProfile
interface UserProfile { }
const users: UserProfile[] = [];
```

### Python
```python
# Rename with docstring updates
def get_data():
    """Gets data from the API."""
    pass

# After renaming
def fetch_user_records():
    """Fetches user records from the API."""
    pass
```

### Java
```java
// Rename with Javadoc updates
/**
 * Gets data
 */
public Data getData() { }

// After renaming
/**
 * Fetches user profile data
 */
public Data fetchUserProfile() { }
```

## Customization

Edit `command.md` to customize:
- Default scope (file vs project)
- Naming convention rules
- String literal handling
- Comment update behavior
- Preview format

## IDE Integration

This command complements your IDE's rename refactoring:
- Use IDE for quick, local renames
- Use this command for cross-file analysis
- Use this command for learning what will change
- Use IDE for instant feedback

## Learning More

Resources for better naming:
- "Clean Code" by Robert C. Martin (Chapter 2: Meaningful Names)
- "Code Complete" by Steve McConnell (Chapter 11: Variable Names)
- Your language's style guide
- Your team's naming conventions

## FAQ

**Q: Will this break my code?**
A: The command is careful about scope and conflicts, but always review changes and run tests after.

**Q: Can it rename across languages?**
A: It focuses on one language at a time. For polyglot projects, run per-language.

**Q: Does it update tests?**
A: Yes! It searches test files too.

**Q: What about dynamically accessed properties?**
A: It will warn about `obj["name"]` style access that might be affected.

**Q: Can I undo a rename?**
A: Yes! Use `/git-undo` or `git reset --hard` if you committed.

## Advanced: Bulk Renaming

For renaming multiple identifiers:

```bash
# Create a rename list
/rename-variable x userData
/rename-variable y userList
/rename-variable fn processUsers
```

Or use the refactor command for comprehensive changes:
```bash
/refactor
# Then describe all the changes you want
```

---

**Remember**: Good names are one of the most important aspects of readable code. Take time to choose meaningful, clear names!
