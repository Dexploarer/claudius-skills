Rename a variable, function, or class throughout the codebase consistently.

## Instructions

1. Ask the user:
   - Current name to rename
   - New name
   - Scope: current file, directory, or entire project

2. Search for all occurrences:
   - Use Grep to find all matches
   - Consider case sensitivity
   - Identify contexts (declarations, usages, comments)

3. Show the user all occurrences found:
   - File paths and line numbers
   - Context around each occurrence
   - Total count

4. Ask for confirmation

5. Perform the rename:
   - Update all occurrences
   - Handle edge cases (partial matches, string literals)
   - Preserve formatting

6. Report results:
   - Number of files changed
   - Number of occurrences renamed
   - Any issues encountered

## Example Output

```
🏷️  Rename Variable

Searching for: "userData"
New name: "userProfile"
Scope: Current directory

Found 12 occurrences in 4 files:

📁 src/services/user.js (4 occurrences)
   Line 23: const userData = await fetchUser();
   Line 25: return userData.name;
   Line 30: if (userData.email) {
   Line 35: cache.set(id, userData);

📁 src/components/Profile.js (5 occurrences)
   Line 12: function Profile({ userData }) {
   Line 15: <h1>{userData.name}</h1>
   Line 18: <p>{userData.email}</p>
   Line 22: if (!userData) {
   Line 28: updateUser(userData);

📁 tests/user.test.js (2 occurrences)
   Line 45: const userData = mockUser();
   Line 48: expect(userData.name).toBe('John');

📁 docs/api.md (1 occurrence)
   Line 67: Returns userData object with user details

This will rename all 12 occurrences to "userProfile".

⚠️  Note: This includes a reference in documentation.
Update docs too? (recommended)

Proceed with rename? (yes/no)
```

## After Renaming

```
✅ Rename Complete!

Renamed "userData" → "userProfile"

Changes:
  • 4 files modified
  • 12 occurrences updated
  • src/services/user.js (4 changes)
  • src/components/Profile.js (5 changes)
  • tests/user.test.js (2 changes)
  • docs/api.md (1 change)

All occurrences have been renamed consistently.

Next steps:
  1. Run tests to verify: npm test
  2. Review changes: git diff
  3. Commit: /git-commit-quick
```

## Scope Options

### Current File
```
Search only in the currently open/specified file
```

### Current Directory
```
Search in all files in the current directory and subdirectories
```

### Entire Project
```
Search from project root
```

### Smart Scope
```
Detect based on variable type:
- Local variable: current function/file
- Class member: current class
- Global/exported: entire project
```

## Safety Checks

Before renaming:
- ⚠️ Check if new name already exists (potential conflict)
- ⚠️ Warn if renaming in many files (>10)
- ⚠️ Detect string literals that might need updating
- ⚠️ Find comments that reference the old name

## Arguments

Parse from $ARGUMENTS:
- $1: Old name (required)
- $2: New name (required)
- $3: Scope (optional: file/dir/project, default: dir)

Example:
```
/rename-variable userData userProfile project
```

## Edge Cases

### Partial Matches
```
Renaming "user" might match:
- user ✓
- userData ❓ (ask user)
- username ❓ (ask user)
- "user" in strings ❓ (ask user)

Default: Only exact matches (whole word)
```

### Case Sensitivity
```
Renaming "UserData":
- UserData ✓
- userData ❓ (different case)
- USERDATA ❓ (different case)

Ask user if should rename case variations.
```

### In Comments
```
Found in comments:
  // userData holds the user information

Should comments be updated too? (yes/no)
```

## Notes

- Use word boundaries to avoid partial matches
- Show context for each occurrence
- Allow user to exclude specific files
- Provide undo information
- Consider language-specific naming conventions
