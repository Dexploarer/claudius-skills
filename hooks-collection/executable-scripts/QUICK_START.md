# Executable Git Hooks - Quick Start

> Get up and running with executable git hooks in 5 minutes

---

## 🚀 Installation (One Command)

```bash
cd /path/to/your/repo
/path/to/claudius-skills/hooks-collection/executable-scripts/install.sh
```

That's it! The hooks are now active.

---

## 📋 What You Get

✅ **Secret Scanner** - Blocks commits with API keys, tokens, passwords
✅ **Env Protection** - Prevents committing .env files
✅ **Linting** - Enforces code quality (ESLint, Prettier, Black, etc.)
✅ **Force Push Prevention** - Protects main/master/develop branches
✅ **Conventional Commits** - Enforces commit message format
✅ **Dependency Scanner** - Finds vulnerable packages (optional)

---

## 🧪 Test It

```bash
# Test secret scanner
echo 'const key = "AKIAIOSFODNN7EXAMPLE"' > test.js
git add test.js
git commit -m "test: check hooks"
# ⛔ Should be blocked

# Test env protection
echo "SECRET=key" > .env
git add .env
git commit -m "test: env file"
# ⛔ Should be blocked

# Test conventional commits
git commit -m "bad message format"
# ⛔ Should be blocked

# Test correct format
git commit -m "feat: add new feature"
# ✅ Should work
```

---

## ⚙️ Configuration

### Disable Specific Checks

```bash
# Disable linting for one commit
RUN_LINTING=false git commit -m "wip: work in progress"

# Disable all pre-commit checks
git commit --no-verify
```

### Permanent Configuration

Add to `~/.bashrc` or `~/.zshrc`:

```bash
export RUN_SECRET_SCANNER=true
export RUN_ENV_PROTECTION=true
export RUN_LINTING=true
export RUN_DEPENDENCY_SCAN=false    # Slow, disabled by default
export RUN_CONVENTIONAL_COMMITS=true
```

---

## 📊 Hook Checklist

| Hook | Enabled by Default | Can Disable |
|------|-------------------|-------------|
| Secret Scanner | ✅ Yes | `RUN_SECRET_SCANNER=false` |
| Env Protection | ✅ Yes | `RUN_ENV_PROTECTION=false` |
| Linting | ✅ Yes | `RUN_LINTING=false` |
| Dependency Scan | ❌ No | `RUN_DEPENDENCY_SCAN=true` |
| Force Push Prevention | ✅ Yes | `git push --no-verify` |
| Conventional Commits | ✅ Yes | `RUN_CONVENTIONAL_COMMITS=false` |

---

## 🔧 Common Issues

### Hook not running?

```bash
# Make sure it's executable
chmod +x .git/hooks/pre-commit

# Verify it exists
ls -l .git/hooks/
```

### Want to skip hooks temporarily?

```bash
git commit --no-verify   # Skip pre-commit
git push --no-verify     # Skip pre-push
```

### Linting errors?

```bash
# Auto-fix
eslint --fix .
prettier --write .
black .
```

---

## 📚 Full Documentation

See [README.md](./README.md) for complete documentation.

---

## 🗑️ Uninstall

```bash
rm .git/hooks/pre-commit
rm .git/hooks/pre-push
rm .git/hooks/commit-msg
rm -rf .git/hooks/{helpers,pre-commit,pre-push,commit-msg}
```

---

## 💡 Pro Tips

1. **Start with security hooks only:**
   ```bash
   export RUN_LINTING=false
   export RUN_CONVENTIONAL_COMMITS=false
   ```

2. **Enable dependency scanning for security-critical projects:**
   ```bash
   export RUN_DEPENDENCY_SCAN=true
   ```

3. **Share with your team:**
   - Add install script to `package.json`:
     ```json
     {
       "scripts": {
         "prepare": "bash ./scripts/install-hooks.sh"
       }
     }
     ```

4. **Run in CI/CD too:**
   ```yaml
   # GitHub Actions
   - name: Run Hooks
     run: |
       .git/hooks/pre-commit
   ```

---

## 🎯 Quick Reference Commands

```bash
# Install
./install.sh

# Skip hooks once
git commit --no-verify

# Disable linting
RUN_LINTING=false git commit -m "msg"

# Enable dependency scan
RUN_DEPENDENCY_SCAN=true git commit -m "msg"

# Uninstall
rm .git/hooks/{pre-commit,pre-push,commit-msg}
```

---

**Need help?** See [README.md](./README.md) for detailed documentation.

**Last Updated:** 2025-11-05
