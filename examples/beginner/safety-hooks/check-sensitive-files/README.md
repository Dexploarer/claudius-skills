# Check Sensitive Files Hook - Beginner Example

A safety hook that warns before committing files that might contain secrets, credentials, or sensitive information.

## What This Example Teaches

- Detecting security risks
- Warning vs blocking approaches
- Pattern matching for filenames
- Security best practices
- Alternative solutions

## What It Does

Scans for files that commonly contain sensitive data (like .env, keys, credentials) before they're committed, warns the user, and provides safe alternatives.

## How to Use

### 1. Install the Hook

```bash
# Copy to your Claude config
mkdir -p ~/.claude/hooks
cp hook.json ~/.claude/hooks/check-sensitive-files.json

# Or for project-specific
mkdir -p .claude/hooks
cp hook.json .claude/hooks/check-sensitive-files.json
```

### 2. It Activates Automatically

Monitors git add and git commit commands.

## Example Scenarios

### Scenario 1: Attempting to Commit .env File

**You type:**
```
Commit my changes including the .env file
```

**Hook warns:**
```
⚠️  Sensitive File Warning

You're about to commit potentially sensitive files:
• .env - Environment variables file (likely contains secrets)

Risks if committed:
• API keys exposed publicly
• Database passwords visible
• Security vulnerability
• Potential compliance violation

Recommended actions:

1. Add to .gitignore:
   echo '.env' >> .gitignore
   git rm --cached .env

2. Create example file instead:
   cp .env .env.example
   # Remove actual values from .env.example
   git add .env.example

3. Use environment variables:
   • Keep .env local only
   • Document required vars in README
   • Use secrets management in production

What .env typically contains:
• DATABASE_URL=postgresql://user:password@host/db
• API_KEY=sk_live_xxxxxxxxxxxxx
• JWT_SECRET=your_secret_here

These should NEVER be in version control!

Do you still want to commit .env? (yes/no)
Type 'no' and I'll help you fix this properly.
```

**You:** no

**Hook helps:**
```
Good choice! Let's fix this properly.

Step 1: Remove .env from staging
Running: git reset HEAD .env

Step 2: Add .env to .gitignore
Adding '.env' to .gitignore file

Step 3: Create .env.example
Creating .env.example with placeholder values...

✅ Done! Your secrets are safe.

Next steps:
• Commit .env.example: git add .env.example
• Document required env vars in README
• Never commit .env again!
```

### Scenario 2: Safe Files

**You type:**
```
git add src/app.js README.md
```

**Hook result:**
```
✅ No sensitive files detected

Files to be added:
• src/app.js
• README.md

These appear safe to commit. Proceeding...
```

### Scenario 3: SSH Key Warning

**You type:**
```
Add my SSH key to the repo
```

**Hook warns:**
```
🚨 CRITICAL: SSH Private Key Detected

You're attempting to commit:
• id_rsa - SSH private key

This is EXTREMELY dangerous!

If committed:
❌ Anyone can access servers you can access
❌ Complete security breach
❌ Impossible to fully revoke (stays in history)

NEVER commit private keys!

Correct approach:
• Keep keys in ~/.ssh/ only
• Never add to git
• Use deploy keys for CI/CD
• Use SSH agent for authentication

This operation is BLOCKED for your safety.
```

## Sensitive File Patterns

### High Risk (Strong Warning)
```
• .env, .env.local, .env.production
• *.pem, *.key (private keys)
• id_rsa, id_dsa, id_ecdsa (SSH keys)
• *.p12, *.pfx (certificates)
• *credentials*, *secrets*
```

### Medium Risk (Warning)
```
• config/production.json, config/prod.js
• .aws/credentials
• *.log (might contain sensitive data)
• docker-compose.override.yml
```

### Low Risk (Inform)
```
• package-lock.json (large file)
• yarn.lock (large file)
• .DS_Store (Mac system file)
```

## What Makes This Useful?

### Prevents Security Breaches
- Catches secrets before they're committed
- Protects API keys, passwords, certificates
- Prevents compliance violations

### Educational
- Teaches security best practices
- Explains why files are risky
- Shows proper alternatives

### Flexible
- Warns but doesn't always block
- User can override if needed
- Provides guidance

## Customization Ideas

### Add More Patterns
```json
{
  "prompt": "Also check for:\n- database.yml (Rails)\n- application.properties (Spring)\n- appsettings.json (ASP.NET)\n- service-account.json (GCP)"
}
```

### Team-Specific Files
```json
{
  "prompt": "For our team, also flag:\n- internal-tools-config.json\n- customer-data-*.csv\n- backup-*.sql"
}
```

### Auto-Fix
```json
{
  "prompt": "When .env detected:\n1. Automatically add to .gitignore\n2. Create .env.example\n3. Remove from staging\n4. Ask for confirmation after fixes"
}
```

### Integration with .gitignore
```json
{
  "prompt": "Check .gitignore first:\n- If file is in .gitignore, allow (user knows)\n- If not in .gitignore, warn and suggest adding"
}
```

## Common Issues

### False Positives?

**Legitimate Files:**
Sometimes `.env.example` or `example.key` are safe to commit.

**Solution:**
```json
{
  "prompt": "Exclude patterns:\n- *.example.*\n- *sample*\n- *template*\n- *placeholder*"
}
```

### Missing Files?

**Add to Pattern List:**
```json
{
  "prompt": "Add your project-specific patterns:\n- secrets.yaml\n- private-config.js\n- auth-tokens.json"
}
```

## Security Best Practices

### For Environment Files
```
✅ DO:
• Keep .env in .gitignore
• Use .env.example with placeholders
• Document required variables
• Use secrets management in production

❌ DON'T:
• Commit .env files
• Hardcode secrets in code
• Share secrets in chat/email
• Reuse secrets across environments
```

### For Credentials
```
✅ DO:
• Use environment variables
• Use secret management services (AWS Secrets, Vault)
• Rotate secrets regularly
• Use principle of least privilege

❌ DON'T:
• Store in source code
• Put in configuration files
• Commit to version control
• Share unencrypted
```

### For Keys
```
✅ DO:
• Generate separate keys per environment
• Use key management services
• Rotate keys periodically
• Restrict key permissions

❌ DON'T:
• Commit private keys
• Share keys via insecure channels
• Reuse keys across projects
• Leave keys unencrypted
```

## What to Do If You Already Committed Secrets

### Immediate Actions
```bash
1. Rotate the compromised secrets immediately
   • Generate new API keys
   • Change passwords
   • Create new certificates

2. Remove from git history (complex):
   git filter-branch --tree-filter 'rm -f .env' HEAD
   # Or use BFG Repo Cleaner

3. Force push (if you must):
   git push --force

4. Notify your team

5. Review access logs for unauthorized use
```

### Prevention Going Forward
```
• Enable this hook for everyone
• Set up git-secrets or similar
• Use pre-commit hooks
• Regular security audits
• Team training
```

## Learning Opportunities

### Security Awareness
- Understand what's sensitive
- Learn secure storage methods
- Practice defense in depth

### Git Best Practices
- Use .gitignore effectively
- Clean git history
- Proper file organization

### Tools and Services
- Secret management (Vault, AWS Secrets)
- Environment variable management
- CI/CD secrets handling

## Related Hooks

- `prevent-main-push` - Workflow safety
- `confirm-deletions` - Prevent accidents
- See intermediate hooks for pre-commit scanning

## Next Steps

### Extend This Hook
- Add automatic .gitignore updates
- Integration with secret scanning tools
- Email alerts for blocked attempts
- Pattern learning from false positives

### Create Related Hooks
- `scan-for-hardcoded-secrets` - Check code for literals
- `validate-env-example` - Ensure .env.example exists
- `check-dependency-vulnerabilities` - Security scanning

### Use With Tools
- Integrate with git-secrets
- Use with Trufflehog
- Combine with Gitleaks
- Add to CI/CD pipeline

## Files

- `hook.json` - The hook configuration
- `README.md` - This documentation

## Why This Pattern Works

### Multiple Layers
- File pattern matching
- Content scanning (can be added)
- User confirmation
- Guidance and alternatives

### Balanced Approach
- Warns but doesn't always block
- Explains the risk
- Provides solutions
- Allows informed decisions

### Educational
- Teaches security
- Builds awareness
- Prevents future mistakes
- Creates good habits

## Real-World Impact

### Stories of Saved Breaches
- API keys not leaked to GitHub
- Database credentials kept private
- SSH keys never committed
- Customer data protected

### Cost of NOT Having This
- $1000s in cloud costs from leaked API keys
- Security breaches
- Compliance fines
- Customer trust lost

### Value of Prevention
- One caught secret can save your project
- Peace of mind
- Professional reputation
- Security culture

## Important Reminders

⚠️ **Hooks are helpful but not perfect** - Use multiple layers of security

✅ **Always rotate compromised secrets** - Even if caught by hook

🔒 **Make security a habit** - Not just a one-time check

💡 **Educate your team** - Security is everyone's responsibility
