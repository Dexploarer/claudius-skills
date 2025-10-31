# Prevent Main Push Hook - Beginner Example

A safety hook that prevents accidental direct pushes to main/master branch.

## What This Example Teaches

- How hooks intercept actions
- Event-driven safety checks
- User-prompt-submit hook usage
- Blocking dangerous operations
- Providing helpful alternatives

## What It Does

Monitors user commands and blocks attempts to push directly to main or master branch, encouraging proper workflow through feature branches and pull requests.

## How to Use

### 1. Install the Hook

```bash
# Copy to your Claude config
mkdir -p ~/.claude/hooks
cp hook.json ~/.claude/hooks/prevent-main-push.json

# Or for project-specific
mkdir -p .claude/hooks
cp hook.json .claude/hooks/prevent-main-push.json
```

### 2. It Activates Automatically

The hook monitors every command you submit.

### 3. When It Blocks

**You type:**
```
Push my changes to main
```

**Hook blocks and shows:**
```
🚫 Push to Main Branch Blocked

You're attempting to push to the main/master branch.
This is usually not recommended.

Why this is blocked:
• main/master should be protected
• Changes should go through pull requests
• Direct pushes bypass code review

Recommended workflow:
1. Create a feature branch:
   git checkout -b feature/your-feature

2. Push to feature branch:
   git push origin feature/your-feature

3. Create pull request for review

If you really need to push to main:
• Disable this hook temporarily
• Or consult with your team lead
```

## Example Scenarios

### Scenario 1: Accidental Main Push

**You type:**
```
git push origin main
```

**Result:**
```
🚫 Blocked: Push to main branch

This hook prevents direct pushes to main.

Instead, try:
1. Create feature branch: git checkout -b feature/my-work
2. Push there: git push origin feature/my-work
3. Open pull request

To bypass (not recommended):
Temporarily disable this hook in ~/.claude/hooks/prevent-main-push.json
```

### Scenario 2: Safe Push to Feature Branch

**You type:**
```
git push origin feature/user-auth
```

**Result:**
```
✅ Command allowed - pushing to feature branch

Executing: git push origin feature/user-auth
[... normal git push output ...]
```

### Scenario 3: Viewing Main Branch

**You type:**
```
git checkout main
git pull origin main
```

**Result:**
```
✅ Commands allowed - not pushing to main

These operations are safe:
• Switching to main branch
• Pulling from main
• Viewing main

Hook only blocks pushes to main.
```

## What Makes This Useful?

### Prevents Mistakes
- Catches accidental main pushes
- Enforces team workflow
- Protects branch integrity

### Educational
- Teaches proper git workflow
- Explains why it's blocked
- Shows correct alternatives

### Customizable
- Enable/disable easily
- Adjust for your team's workflow
- Add exceptions if needed

## Customization Ideas

### Allow Hotfixes
```json
{
  "prompt": "...\n\nExceptions:\n- If commit message contains '[HOTFIX]', allow the push\n- If user confirms 3 times, allow (emergency)"
}
```

### Team-Specific Branches
```json
{
  "prompt": "Block pushes to:\n- main\n- master\n- production\n- staging\n\nAllow:\n- feature/*\n- bugfix/*\n- hotfix/* (with warning)"
}
```

### Add Logging
```json
{
  "prompt": "...\n\nAlso log blocked attempts to:\n~/.claude/hooks-log.txt\n\nFormat: [timestamp] Blocked: git push origin main by [user]"
}
```

## Common Issues

### Hook doesn't activate?

**Check:**
1. File is in correct location: `.claude/hooks/prevent-main-push.json`
2. JSON is valid (no syntax errors)
3. `enabled` is set to `true`
4. Hook event is `user-prompt-submit`

### Blocks too much?

**Adjust** the detection logic:
```json
{
  "prompt": "Only block explicit pushes:\n- git push origin main\n- git push origin master\n\nDon't block:\n- 'push my changes' (ambiguous)\n- Mentions of 'main' in other contexts"
}
```

### Need to bypass temporarily?

**Option 1:** Disable in JSON
```json
{
  "enabled": false
}
```

**Option 2:** Rename file temporarily
```bash
mv prevent-main-push.json prevent-main-push.json.disabled
```

## Hook Configuration

### Event Type
```json
"event": "user-prompt-submit"
```
This hook runs when user submits a prompt, before Claude processes it.

### Enable/Disable
```json
"enabled": true  // Active
"enabled": false // Disabled
```

### Hook Prompt
The `prompt` field contains instructions for Claude on what to check and how to respond.

## Best Practices

### For Teams

**Standard Setup:**
1. Add to project `.claude/hooks/`
2. Commit to repository
3. Team members get it automatically
4. Consistent workflow enforcement

**Documentation:**
- Include in project README
- Explain in onboarding docs
- List in team conventions

### For Personal Use

**Adjust to Your Workflow:**
- Add your branch patterns
- Customize messages
- Set your own rules

**Learn and Adapt:**
- Start with strict rules
- Relax as you learn
- Add exceptions as needed

## Learning Opportunities

### Understanding Hooks

**Event Lifecycle:**
```
User types command
    ↓
Hook intercepts (user-prompt-submit)
    ↓
Hook checks command
    ↓
✅ Allow or ❌ Block
    ↓
Command executes (if allowed)
```

### Hook Events

- `user-prompt-submit`: Before processing user input
- Other events available for different use cases

### Safety Patterns

- **Prevent**: Block dangerous operations
- **Warn**: Alert but allow
- **Log**: Record for review
- **Guide**: Suggest alternatives

## Related Hooks

- `check-sensitive-files` - Prevent committing secrets
- `confirm-deletions` - Confirm before deleting files
- See intermediate examples for advanced hooks

## Next Steps

### Extend This Hook
- Add branch name pattern matching
- Include commit message requirements
- Log all blocked attempts
- Send team notifications

### Create Related Hooks
- `prevent-force-push` - Block force pushes
- `require-pull-request` - Enforce PR workflow
- `check-branch-naming` - Validate branch names

### Combine With Other Features
- Use with `/git-commit-quick` command
- Pair with code review workflows
- Integrate with CI/CD

## Files

- `hook.json` - The hook configuration (copy to `.claude/hooks/`)
- `README.md` - This documentation

## Why This Pattern Works

### Proactive Prevention
- Catches mistakes before they happen
- No damage to undo
- Reduces anxiety

### Teaching Tool
- Explains proper workflow
- Shows alternatives
- Builds good habits

### Team Standard
- Enforces consistency
- Reduces accidents
- Improves code quality

## Important Notes

⚠️ **Hooks are not foolproof** - Determined users can bypass them

✅ **Hooks are educational** - They guide and remind

🎯 **Hooks work best** - When team agrees on their purpose

💡 **Hooks should explain** - Not just block, but teach why
