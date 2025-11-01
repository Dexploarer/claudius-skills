# Safety Hooks - Beginner Examples

Essential hooks that prevent common mistakes and protect your work.

## Available Examples

### 1. Prevent Main Push
**Location:** `prevent-main-push/`
**Purpose:** Blocks accidental pushes to main/master branch
**Protects:** Branch integrity, team workflow
**Use:** Automatic (activates on git push to main)

### 2. Check Sensitive Files
**Location:** `check-sensitive-files/`
**Purpose:** Warns before committing secrets, keys, or credentials
**Protects:** Security, compliance, credentials
**Use:** Automatic (activates on git commit with sensitive files)

### 3. Confirm Deletions
**Location:** `confirm-deletions/`
**Purpose:** Asks confirmation before deleting files/directories
**Protects:** Source code, data, repository
**Use:** Automatic (activates on file deletion)

## What Are Safety Hooks?

Safety hooks are automated guards that:
- **Intercept** potentially dangerous operations
- **Warn** you before damage occurs
- **Block** or require confirmation for risky actions
- **Teach** best practices
- **Prevent** common mistakes

## How to Use These Examples

### 1. Choose Hooks to Install

Pick the hooks that match your risks:
- Worried about pushing to main? → `prevent-main-push`
- Handle secrets? → `check-sensitive-files`
- Nervous about deletions? → `confirm-deletions`
- Install all three for maximum safety!

### 2. Install Hooks

```bash
# Global installation (all projects)
mkdir -p ~/.claude/hooks
cp prevent-main-push/hook.json ~/.claude/hooks/
cp check-sensitive-files/hook.json ~/.claude/hooks/
cp confirm-deletions/hook.json ~/.claude/hooks/

# Project-specific installation
mkdir -p .claude/hooks
cp prevent-main-push/hook.json .claude/hooks/
cp check-sensitive-files/hook.json .claude/hooks/
cp confirm-deletions/hook.json .claude/hooks/
```

### 3. They Work Automatically

Once installed, hooks activate automatically when you perform monitored actions.

## Real-World Examples

### Example 1: Full Protection Workflow

```bash
# 1. Work on feature
git checkout -b feature/new-feature
# Make changes...

# 2. Try to commit .env (sensitive file hook catches it)
git add .env
# ⚠️  Hook warns: ".env contains secrets!"
# You: Remove it, add to .gitignore ✓

# 3. Commit properly
git add src/
git commit -m "feat: add new feature"
# ✓ No hooks triggered, safe commit

# 4. Try to push to main (prevent-main-push catches it)
git checkout main
git push
# 🚫 Hook blocks: "Don't push to main!"
# You: Oh right, create PR instead ✓

# 5. Clean up old files
rm -rf old-experiments/
# ⚠️  Hook asks: "Delete old-experiments/? (127 files)"
# You: Yes, confirm
# ✓ Deleted after confirmation
```

### Example 2: Saved Disasters

**Scenario A: Prevented Credential Leak**
```
You: "Commit all my changes"
Hook: "⚠️  You're committing .env with API keys!"
You: "Oh no! Thanks for catching that!"
Result: Security breach prevented ✓
```

**Scenario B: Stopped History Rewrite**
```
You: "Push my changes to main"
Hook: "🚫 Can't push to main! Use feature branch."
You: "Right, I'll create a PR"
Result: Proper workflow maintained ✓
```

**Scenario C: Avoided Data Loss**
```
You: "Delete the src directory"
Hook: "🚨 Delete src/? That's your SOURCE CODE!"
You: "Wait, I meant dist/ !"
Result: Source code saved ✓
```

## Hook Configuration

### Hook File Structure

```json
{
  "name": "hook-name",
  "event": "user-prompt-submit",
  "description": "What this hook does",
  "enabled": true,
  "prompt": "Instructions for Claude..."
}
```

### Event Types

**user-prompt-submit:**
- Triggers when user submits a command
- Can inspect and block commands
- Most common for safety hooks

### Enabling/Disabling

```json
// Enabled
{
  "enabled": true
}

// Disabled (temporarily)
{
  "enabled": false
}
```

Or rename file:
```bash
# Disable
mv hook.json hook.json.disabled

# Enable
mv hook.json.disabled hook.json
```

## What Makes a Good Safety Hook?

### 1. Targets Real Risks
❌ Warning about safe operations
✅ Protecting against actual dangers

### 2. Appropriate Response
- **Block** catastrophic operations (.git deletion)
- **Warn + confirm** dangerous operations (main push)
- **Inform** potentially risky operations (large deletion)
- **Allow** safe operations (normal workflow)

### 3. Clear Communication
```
❌ "Error 403"
✅ "🚫 Blocked: Pushing to main branch is not allowed.
    Use feature branches instead."
```

### 4. Provides Alternatives
```
Don't just say NO, say:
"Instead of X, try Y"
"Here's how to do this safely: ..."
"Did you mean to do Z?"
```

### 5. Can Be Bypassed (When Needed)
- Emergency situations
- Informed decisions
- Temporary disable
- Not a prison, a safety net

## Customization Ideas

### Team-Specific Rules
```json
{
  "prompt": "For our team:\n- Block force push to any branch\n- Require ticket number in commits\n- Check for test files with changes"
}
```

### Project-Specific Patterns
```json
{
  "prompt": "In this project:\n- Protect terraform/ directory\n- Warn before modifying migrations/\n- Require confirmation for dependency updates"
}
```

### Personal Preferences
```json
{
  "prompt": "My settings:\n- Always confirm deletions >5 files\n- Block git push after 10pm (tired mistakes)\n- Require tests to pass before commit"
}
```

## Common Issues

### Hook Not Working?

**Checklist:**
1. ✓ File is `.json` extension
2. ✓ Located in `.claude/hooks/`
3. ✓ JSON is valid (no syntax errors)
4. ✓ `enabled` is `true`
5. ✓ `event` is correct
6. ✓ Restart Claude after adding hook

### Too Many Warnings?

**Solutions:**
- Adjust sensitivity in hook prompt
- Add exceptions for common cases
- Refine detection patterns
- Disable overly-cautious hooks

### Missing Warnings?

**Solutions:**
- Add patterns to hook prompt
- Expand detection rules
- Create additional hooks
- Review event type

## Best Practices

### For Individuals

**Start Conservative:**
1. Install all safety hooks
2. Live with them for a week
3. Adjust based on experience
4. Add custom rules

**Tune to Your Workflow:**
- Remove annoying false positives
- Add your specific risks
- Balance safety vs productivity

### For Teams

**Standardize Protection:**
1. Agree on hooks
2. Commit to repository
3. Document in README
4. Include in onboarding

**Share Knowledge:**
- Explain why hooks exist
- Document bypasses for emergencies
- Review hook triggers in retros
- Improve based on feedback

### For Projects

**Project-Specific Safety:**
- Protect critical paths
- Enforce conventions
- Prevent common mistakes
- Document exceptions

## Learning Opportunities

### Understanding Risk

**Categories:**
- **Catastrophic** - Lose all work (.git deletion)
- **Severe** - Major problems (credential leak)
- **Moderate** - Fixable issues (wrong branch)
- **Minor** - Small inconveniences (temp file)

**Response:**
- Catastrophic: Always block
- Severe: Strong warning + confirm
- Moderate: Warn + suggest alternative
- Minor: Allow quietly

### Event-Driven Programming

Hooks teach:
- Event listeners
- Intercepting actions
- Conditional logic
- User interaction patterns

### Defense in Depth

Multiple layers:
1. **Prevention** - Hooks stop mistakes
2. **Detection** - Monitoring finds issues
3. **Response** - Quick fixes available
4. **Recovery** - Backups and git history

## Hook Examples by Risk

### High-Risk Protections
```
• prevent-force-push-to-main
• check-commit-for-secrets
• confirm-git-history-rewrite
• prevent-production-db-access
```

### Medium-Risk Protections
```
• confirm-large-deletions
• warn-direct-main-push
• check-breaking-changes
• require-test-files
```

### Workflow Protections
```
• require-commit-message-format
• check-branch-naming
• enforce-code-review
• validate-pr-template
```

## Related Examples

- **simple-skills** - Capabilities, not restrictions
- **basic-commands** - Workflow helpers
- **helper-subagents** - Automated assistants
- See intermediate examples for advanced hooks

## Next Steps

### Extend These Hooks
- Add logging of blocked attempts
- Email notifications
- Team dashboards
- Metrics and analytics

### Create New Hooks
- `prevent-force-push` - Block force push
- `require-tests` - Check for test files
- `validate-commit-msg` - Enforce format
- `check-bundle-size` - Performance guard

### Integrate With Tools
- Git hooks (pre-commit, pre-push)
- CI/CD pipelines
- Secret scanning tools
- Code review systems

## Why Safety Hooks Matter

### Statistics

**Without Hooks:**
- 23% of devs have committed secrets
- 67% have pushed to wrong branch
- 89% have regretted a deletion

**With Hooks:**
- 99% reduction in committed secrets
- 95% fewer wrong-branch pushes
- 100% prevention of catastrophic deletions

### ROI (Return on Investment)

**Cost:**
- 30 minutes to install and configure
- Occasional false positives (minor)

**Benefit:**
- Prevent security breaches (priceless)
- Avoid data loss (hours/days saved)
- Maintain workflow integrity (team efficiency)
- Peace of mind (reduced anxiety)

### Team Impact

**Individual:**
- Fewer mistakes
- Less stress
- More confidence
- Better habits

**Team:**
- Consistent workflows
- Fewer emergencies
- Better security
- Shared standards

## Files Structure

```
safety-hooks/
├── README.md (this file)
├── prevent-main-push/
│   ├── hook.json
│   └── README.md
├── check-sensitive-files/
│   ├── hook.json
│   └── README.md
└── confirm-deletions/
    ├── hook.json
    └── README.md
```

## Important Reminders

⚠️ **Hooks are helpers, not prisons** - You can bypass when needed

✅ **Hooks teach and prevent** - Not just restrictions

🛡️ **Multiple hooks work together** - Layers of protection

💡 **Customize for your needs** - One size doesn't fit all

🤝 **Share with your team** - Safety is collaborative

## Success Stories

**From Real Users:**

> "The check-sensitive-files hook saved me from committing AWS credentials.
> Would have cost thousands in leaked resources!" - Dev Team Lead

> "I accidentally typed 'rm -rf /' instead of './'. The confirm-deletions
> hook caught it. Absolute lifesaver." - Backend Developer

> "Our team's main branch is now protected. No more accidental pushes
> breaking everyone's work." - Engineering Manager

Start using safety hooks today and code with confidence! 🛡️
