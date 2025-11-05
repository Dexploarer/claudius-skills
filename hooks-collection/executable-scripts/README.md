# Executable Git Hooks

> Production-ready executable shell scripts for git hooks - actual scripts that run, not just JSON configurations

---

## 📚 Overview

This directory contains **executable shell scripts** that implement the git hooks defined in the parent `hooks-collection/` directory. While the parent directory contains JSON configurations for Claude Code's hook system, these are **actual bash scripts** that can be installed as traditional git hooks.

### What's Included

- **Pre-Commit Hooks** (4 scripts)
  - Secret Scanner - Detects API keys, tokens, and credentials
  - Env Protection - Prevents committing .env files
  - Linting Enforcement - Runs linters (ESLint, Prettier, Black, etc.)
  - Dependency Scanner - Scans for vulnerable dependencies

- **Pre-Push Hooks** (1 script)
  - Force Push Prevention - Blocks dangerous force pushes to protected branches

- **Commit-Msg Hooks** (1 script)
  - Conventional Commits - Enforces conventional commit message format

- **Helper Utilities**
  - Common functions for colored output, user prompts, git operations

---

## 🚀 Quick Start

### Installation

```bash
# Navigate to your git repository
cd /path/to/your/repo

# Run the installation script
/path/to/claudius-skills/hooks-collection/executable-scripts/install.sh
```

The installer will:
1. ✅ Check you're in a git repository
2. ✅ Show what will be installed
3. ✅ Ask for confirmation
4. ✅ Backup existing hooks
5. ✅ Install all hook scripts
6. ✅ Make scripts executable

### Manual Installation

```bash
# Copy hooks to your repository
cp -r hooks-collection/executable-scripts/.git/hooks/* /path/to/your/repo/.git/hooks/

# Or install specific hooks
cp hooks-collection/executable-scripts/pre-commit.sh /path/to/your/repo/.git/hooks/pre-commit
cp hooks-collection/executable-scripts/pre-push.sh /path/to/your/repo/.git/hooks/pre-push
cp hooks-collection/executable-scripts/commit-msg.sh /path/to/your/repo/.git/hooks/commit-msg

# Copy helper scripts
cp -r hooks-collection/executable-scripts/helpers /path/to/your/repo/.git/hooks/
cp -r hooks-collection/executable-scripts/pre-commit /path/to/your/repo/.git/hooks/
cp -r hooks-collection/executable-scripts/pre-push /path/to/your/repo/.git/hooks/
cp -r hooks-collection/executable-scripts/commit-msg /path/to/your/repo/.git/hooks/

# Make executable
chmod +x /path/to/your/repo/.git/hooks/*
```

---

## 📁 Directory Structure

```
executable-scripts/
├── README.md                    # This file
├── install.sh                   # Installation script
├── pre-commit.sh                # Main pre-commit hook
├── pre-push.sh                  # Main pre-push hook
├── commit-msg.sh                # Main commit-msg hook
│
├── helpers/
│   └── common.sh               # Shared utility functions
│
├── pre-commit/
│   ├── secret-scanner.sh       # Scans for secrets
│   ├── env-protection.sh       # Protects .env files
│   ├── linting-enforcement.sh  # Runs linters
│   └── dependency-scanner.sh   # Scans dependencies
│
├── pre-push/
│   └── prevent-force-push.sh   # Prevents force pushes
│
└── commit-msg/
    └── conventional-commits.sh # Enforces commit format
```

---

## 🔍 Hook Details

### Pre-Commit: Secret Scanner

**Purpose:** Prevents accidentally committing secrets, API keys, and credentials

**Detects:**
- AWS Access Keys (`AKIA...`)
- GitHub Personal Access Tokens
- API keys and secrets
- Private keys (PEM, SSH)
- JWT tokens
- Stripe keys
- Google API keys
- Slack tokens and webhooks
- Database connection strings
- And more...

**Usage:**
```bash
# Automatically runs on git commit
git commit -m "feat: add feature"

# If secrets detected:
⛔ SECRETS DETECTED!
File: config.js
Line 12: Type: AWS_ACCESS_KEY
  const key = "AKIA..."

# To skip (NOT recommended):
git commit --no-verify
```

**Configuration:**
```bash
# Disable secret scanner
export RUN_SECRET_SCANNER=false
```

---

### Pre-Commit: Env Protection

**Purpose:** Prevents committing .env files and credential files

**Blocks:**
- `.env` and variants (`.env.local`, `.env.production`, etc.)
- `credentials.json`
- `secrets.json`
- Service account keys
- Private keys
- And more...

**Allows:**
- `.env.example`
- `.env.template`
- `.env.sample`

**Usage:**
```bash
# Will be blocked
git add .env
git commit -m "feat: update config"

⛔ PROTECTED FILES DETECTED
  ✗ .env

# To fix:
git restore --staged .env
echo ".env" >> .gitignore
```

**Configuration:**
```bash
# Disable env protection (NOT recommended)
export RUN_ENV_PROTECTION=false
```

---

### Pre-Commit: Linting Enforcement

**Purpose:** Ensures code quality by running linters before commit

**Supports:**

**JavaScript/TypeScript:**
- ESLint
- Prettier

**Python:**
- flake8
- black
- mypy

**Go:**
- gofmt
- go vet
- golangci-lint

**Rust:**
- rustfmt
- clippy

**Usage:**
```bash
# Automatically runs on staged files
git commit -m "feat: add feature"

# If linting errors found:
⛔ ESLint found issues
To fix: eslint --fix src/file.js

# Auto-fix before committing:
eslint --fix .
prettier --write .
black .
gofmt -w .
rustfmt .
```

**Configuration:**
```bash
# Disable linting
export RUN_LINTING=false

# Or skip for one commit
RUN_LINTING=false git commit -m "wip: work in progress"
```

---

### Pre-Commit: Dependency Scanner

**Purpose:** Scans for vulnerable dependencies when package files change

**Supports:**
- npm/yarn (Node.js)
- pip/pipenv (Python)
- cargo (Rust)
- go mod (Go)
- composer (PHP)
- bundler (Ruby)

**Usage:**
```bash
# Only runs when package files change
git add package.json package-lock.json
git commit -m "feat: update dependencies"

# If vulnerabilities found:
⚠️ VULNERABILITIES DETECTED
npm audit found 3 vulnerabilities

To fix: npm audit fix

# Disabled by default (can be slow)
# Enable with:
export RUN_DEPENDENCY_SCAN=true
```

**Configuration:**
```bash
# Enable dependency scanning
export RUN_DEPENDENCY_SCAN=true

# Or enable for one commit
RUN_DEPENDENCY_SCAN=true git commit -m "chore: update deps"
```

---

### Pre-Push: Force Push Prevention

**Purpose:** Prevents dangerous force pushes to protected branches

**Protected Branches:**
- `main`
- `master`
- `develop`
- `production`
- `staging`

**Usage:**
```bash
# Will be blocked
git push --force origin main

⛔ FORCE PUSH BLOCKED
Branch: main
Risk Level: HIGH

Safer alternatives:
1. Merge instead of rebase
2. Create new branch
3. Coordinate with team

# Allowed on feature branches (with warning)
git push --force origin feature/my-branch

⚠️ Force Push Warning
Proceed? (y/n)
```

**Bypass:**
```bash
# Temporary bypass (NOT recommended for protected branches)
git push --no-verify --force
```

---

### Commit-Msg: Conventional Commits

**Purpose:** Enforces conventional commit message format

**Format:**
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Valid Types:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation
- `style` - Code style
- `refactor` - Refactoring
- `perf` - Performance
- `test` - Testing
- `build` - Build system
- `ci` - CI/CD
- `chore` - Maintenance
- `revert` - Revert

**Examples:**
```bash
# ✅ Good
git commit -m "feat(auth): add JWT authentication"
git commit -m "fix(api): resolve timeout issue"
git commit -m "docs: update README"

# ❌ Bad
git commit -m "fixed stuff"
git commit -m "WIP"
git commit -m "Updated the thing"
```

**Configuration:**
```bash
# Disable conventional commits
export RUN_CONVENTIONAL_COMMITS=false
```

---

## ⚙️ Configuration

### Environment Variables

All hooks can be configured using environment variables:

```bash
# Add to ~/.bashrc or ~/.zshrc
export RUN_SECRET_SCANNER=true
export RUN_ENV_PROTECTION=true
export RUN_LINTING=true
export RUN_DEPENDENCY_SCAN=false    # Disabled by default
export RUN_CONVENTIONAL_COMMITS=true
```

### Per-Command Configuration

```bash
# Skip linting for one commit
RUN_LINTING=false git commit -m "wip: work in progress"

# Enable dependency scan for one commit
RUN_DEPENDENCY_SCAN=true git commit -m "chore: update deps"

# Skip all pre-commit hooks
git commit --no-verify
```

### Project-Specific Configuration

Create a `.git/hooks/config.sh` file:

```bash
#!/usr/bin/env bash
# Project-specific hook configuration

export RUN_SECRET_SCANNER=true
export RUN_ENV_PROTECTION=true
export RUN_LINTING=true
export RUN_DEPENDENCY_SCAN=true  # Enable for this project
```

Then source it in your shell:
```bash
source .git/hooks/config.sh
```

---

## 🧪 Testing

### Test Secret Scanner

```bash
# Create test file with fake secret
echo 'const key = "AKIAIOSFODNN7EXAMPLE"' > test.js
git add test.js
git commit -m "test: secret scanner"

# Should be blocked
```

### Test Env Protection

```bash
# Create .env file
echo "API_KEY=secret" > .env
git add .env
git commit -m "test: env protection"

# Should be blocked
```

### Test Linting

```bash
# Create file with linting errors
echo "const x=1" > test.js  # Missing semicolon
git add test.js
git commit -m "test: linting"

# Should be blocked (if ESLint configured)
```

### Test Force Push Prevention

```bash
# Try force push to main
git checkout main
git push --force origin main

# Should be blocked
```

### Test Conventional Commits

```bash
# Try bad commit message
git commit -m "fixed stuff"

# Should be blocked
```

---

## 🔧 Troubleshooting

### Hook Not Running

**Check hook is executable:**
```bash
ls -l .git/hooks/pre-commit
# Should show -rwxr-xr-x

# Make executable if needed:
chmod +x .git/hooks/pre-commit
```

**Check hook exists:**
```bash
ls .git/hooks/
```

**Check for syntax errors:**
```bash
bash -n .git/hooks/pre-commit
```

### Hook Failing Unexpectedly

**Run hook manually:**
```bash
.git/hooks/pre-commit
```

**Check dependencies:**
```bash
# For linting
which eslint prettier flake8 black

# For dependency scanning
which npm pip cargo go
```

**View debug output:**
```bash
set -x  # Add to hook script for debug mode
```

### Bypass Hooks Temporarily

```bash
# Skip pre-commit
git commit --no-verify

# Skip pre-push
git push --no-verify
```

**⚠️ Use sparingly - hooks exist for good reasons!**

---

## 🗑️ Uninstallation

### Remove All Hooks

```bash
rm .git/hooks/pre-commit
rm .git/hooks/pre-push
rm .git/hooks/commit-msg
rm -rf .git/hooks/helpers
rm -rf .git/hooks/pre-commit
rm -rf .git/hooks/pre-push
rm -rf .git/hooks/commit-msg
```

### Restore Backups

```bash
# Backups created during installation
mv .git/hooks/pre-commit.backup.* .git/hooks/pre-commit
```

---

## 📊 Comparison with Claude Code Hooks

| Feature | Executable Scripts | Claude Code JSON Hooks |
|---------|-------------------|------------------------|
| **Installation** | Manual install to `.git/hooks/` | Automatic via `.claude/hooks/` |
| **Language** | Bash shell scripts | JSON configuration |
| **Execution** | Git triggers automatically | Claude Code interprets |
| **Portability** | Works in any git repo | Requires Claude Code |
| **Customization** | Edit bash scripts | Edit JSON prompts |
| **Performance** | Fast (native execution) | Depends on Claude Code |
| **Dependencies** | Standard Unix tools | Claude Code |
| **Best For** | Any git project | Projects using Claude Code |

**Use Executable Scripts when:**
- Working without Claude Code
- Need guaranteed enforcement
- Want standard git hook behavior
- Sharing with team not using Claude Code

**Use Claude Code JSON Hooks when:**
- Already using Claude Code
- Want AI-assisted enforcement
- Need flexible, prompt-based rules
- Prefer configuration over code

---

## 💡 Best Practices

### 1. Start Small

Don't enable all hooks at once:

```bash
# Week 1: Critical security
export RUN_SECRET_SCANNER=true
export RUN_ENV_PROTECTION=true

# Week 2: Add linting
export RUN_LINTING=true

# Week 3: Add dependency scanning
export RUN_DEPENDENCY_SCAN=true
```

### 2. Team Adoption

Share hooks with your team:

```bash
# Add installation script to README
echo "Run ./scripts/install-hooks.sh to install git hooks" >> README.md

# Or add to package.json
{
  "scripts": {
    "prepare": "bash ./scripts/install-hooks.sh"
  }
}
```

### 3. CI/CD Integration

Run same checks in CI:

```yaml
# .github/workflows/checks.yml
name: Code Checks
on: [push, pull_request]

jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Secret Scanner
        run: .git/hooks/pre-commit/secret-scanner.sh
      - name: Linting
        run: .git/hooks/pre-commit/linting-enforcement.sh
```

### 4. Document Exceptions

```markdown
## Hook Exceptions

- `RUN_DEPENDENCY_SCAN=false` - Too slow for rapid development
- Force push allowed on `feature/*` branches
- Conventional commits required for main/develop only
```

---

## 🤝 Contributing

### Adding New Hooks

1. Create script in appropriate directory
2. Follow naming convention: `descriptive-name.sh`
3. Make executable: `chmod +x script.sh`
4. Source common utilities: `source ../helpers/common.sh`
5. Add to main hook file (pre-commit.sh, etc.)
6. Update documentation
7. Test thoroughly

### Example Hook Template

```bash
#!/usr/bin/env bash
# Hook: My New Check
# Description: What this hook does

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../helpers/common.sh"

print_header "My New Check"

# Your logic here

if [[ $errors -gt 0 ]]; then
    print_error "Check failed"
    exit 1
else
    print_success "Check passed"
    exit 0
fi
```

---

## 📚 Resources

### Git Hooks Documentation
- [Git Hooks Official Docs](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
- [Conventional Commits](https://www.conventionalcommits.org/)

### Security Tools
- [gitleaks](https://github.com/zricethezav/gitleaks) - Secret scanner
- [git-secrets](https://github.com/awslabs/git-secrets) - AWS secret prevention
- [detect-secrets](https://github.com/Yelp/detect-secrets) - Yelp's secret scanner

### Linting Tools
- [ESLint](https://eslint.org/)
- [Prettier](https://prettier.io/)
- [Black](https://black.readthedocs.io/)
- [golangci-lint](https://golangci-lint.run/)

### Dependency Scanners
- [npm audit](https://docs.npmjs.com/cli/v8/commands/npm-audit)
- [pip-audit](https://github.com/pypa/pip-audit)
- [cargo-audit](https://github.com/RustSec/rustsec/tree/main/cargo-audit)

---

## 📄 License

MIT License - Use freely in your projects

---

## 🎯 Quick Reference

### Installation
```bash
./install.sh
```

### Configuration
```bash
export RUN_SECRET_SCANNER=true
export RUN_ENV_PROTECTION=true
export RUN_LINTING=true
export RUN_DEPENDENCY_SCAN=false
export RUN_CONVENTIONAL_COMMITS=true
```

### Bypass (use sparingly)
```bash
git commit --no-verify
git push --no-verify
```

### Uninstall
```bash
rm .git/hooks/{pre-commit,pre-push,commit-msg}
rm -rf .git/hooks/{helpers,pre-commit,pre-push,commit-msg}
```

---

**Last Updated:** 2025-11-05
**Version:** 1.0.0
**Maintainer:** Claudius Skills Project
