#!/usr/bin/env bash
# Git Hooks Installation Script
# Installs executable git hooks into your repository

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'
BOLD='\033[1m'

print_header() {
    echo -e "\n${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BOLD}$1${NC}"
    echo -e "${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"
}

print_success() {
    echo -e "${GREEN}${BOLD}✓${NC} $1"
}

print_error() {
    echo -e "${RED}${BOLD}⛔ ERROR:${NC} $1" >&2
}

print_warning() {
    echo -e "${YELLOW}${BOLD}⚠️  WARNING:${NC} $1"
}

print_info() {
    echo -e "${BLUE}${BOLD}ℹ${NC} $1"
}

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    print_error "Not a git repository. Please run this script from the root of a git repository."
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GIT_HOOKS_DIR="$(git rev-parse --git-dir)/hooks"

print_header "🔧 Git Hooks Installation"

echo "This script will install executable git hooks into your repository."
echo ""
echo "Hooks to be installed:"
echo "  • pre-commit     - Secret scanning, env protection, linting"
echo "  • pre-push       - Force push prevention"
echo "  • commit-msg     - Conventional commits enforcement"
echo ""
echo "Installation directory: $GIT_HOOKS_DIR"
echo ""

# Ask for confirmation
read -p "Continue with installation? (y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_info "Installation cancelled"
    exit 0
fi

echo ""

# Create hooks directory if it doesn't exist
if [[ ! -d "$GIT_HOOKS_DIR" ]]; then
    mkdir -p "$GIT_HOOKS_DIR"
    print_success "Created hooks directory"
fi

# Function to install a hook
install_hook() {
    local hook_name="$1"
    local source_file="$SCRIPT_DIR/${hook_name}.sh"
    local target_file="$GIT_HOOKS_DIR/$hook_name"

    if [[ ! -f "$source_file" ]]; then
        print_warning "Source file not found: $source_file"
        return 1
    fi

    # Backup existing hook
    if [[ -f "$target_file" ]]; then
        local backup_file="${target_file}.backup.$(date +%s)"
        cp "$target_file" "$backup_file"
        print_info "Backed up existing $hook_name to $backup_file"
    fi

    # Copy hook
    cp "$source_file" "$target_file"
    chmod +x "$target_file"

    print_success "Installed $hook_name hook"
}

# Copy helper scripts
if [[ -d "$SCRIPT_DIR/helpers" ]]; then
    cp -r "$SCRIPT_DIR/helpers" "$GIT_HOOKS_DIR/"
    chmod +x "$GIT_HOOKS_DIR/helpers/"*.sh
    print_success "Installed helper scripts"
fi

# Copy individual hook scripts
for hook_dir in pre-commit pre-push commit-msg; do
    if [[ -d "$SCRIPT_DIR/$hook_dir" ]]; then
        cp -r "$SCRIPT_DIR/$hook_dir" "$GIT_HOOKS_DIR/"
        chmod +x "$GIT_HOOKS_DIR/$hook_dir/"*.sh
        print_success "Installed $hook_dir scripts"
    fi
done

# Install main hook files
echo ""
print_info "Installing main hook files..."

install_hook "pre-commit"
install_hook "pre-push"
install_hook "commit-msg"

echo ""
print_header "✅ Installation Complete!"

cat << 'EOF'

🎉 Git hooks have been successfully installed!

📝 WHAT'S INSTALLED:

Pre-Commit Hook:
  • Secret scanner - Prevents committing API keys and secrets
  • Env protection  - Blocks .env and credential files
  • Linting         - Enforces code quality standards
  • Dependency scan - Checks for vulnerabilities (optional)

Pre-Push Hook:
  • Force push prevention - Protects main/master/develop branches

Commit-Msg Hook:
  • Conventional commits - Enforces commit message format

🔧 CONFIGURATION:

You can configure hooks using environment variables:

# In your ~/.bashrc or ~/.zshrc
export RUN_SECRET_SCANNER=true
export RUN_ENV_PROTECTION=true
export RUN_LINTING=true
export RUN_DEPENDENCY_SCAN=false  # Disabled by default (can be slow)
export RUN_CONVENTIONAL_COMMITS=true

Or set them per-command:
RUN_LINTING=false git commit -m "feat: quick fix"

🚀 TESTING:

Try making a commit to test the hooks:
  echo "test" > test.txt
  git add test.txt
  git commit -m "test: trying out the hooks"

⚙️  BYPASS HOOKS (when needed):

If you need to bypass hooks temporarily:
  git commit --no-verify
  git push --no-verify

⚠️  NOT RECOMMENDED for normal use!

🗑️  UNINSTALL:

To remove the hooks:
  rm .git/hooks/pre-commit
  rm .git/hooks/pre-push
  rm .git/hooks/commit-msg
  rm -rf .git/hooks/helpers
  rm -rf .git/hooks/pre-commit
  rm -rf .git/hooks/pre-push
  rm -rf .git/hooks/commit-msg

Or restore backups:
  mv .git/hooks/pre-commit.backup.* .git/hooks/pre-commit

📚 MORE INFORMATION:

See README.md in this directory for detailed documentation.

EOF

print_success "Ready to use! Try making a commit to see the hooks in action."
