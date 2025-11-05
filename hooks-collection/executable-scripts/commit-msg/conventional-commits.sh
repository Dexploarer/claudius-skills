#!/usr/bin/env bash
# Commit-msg hook: Conventional Commits
# Enforces conventional commit message format

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../helpers/common.sh"

# Get commit message file
COMMIT_MSG_FILE="$1"

if [[ ! -f "$COMMIT_MSG_FILE" ]]; then
    print_error "Commit message file not found: $COMMIT_MSG_FILE"
    exit 1
fi

# Read commit message
COMMIT_MSG=$(cat "$COMMIT_MSG_FILE")

# Skip merge commits and reverts
if echo "$COMMIT_MSG" | grep -qE "^(Merge|Revert)"; then
    exit 0
fi

print_header "📝 Conventional Commit Checker"

# Conventional commit pattern
# Format: type(scope): subject
# Examples:
#   feat(auth): add login functionality
#   fix(api): resolve timeout issue
#   docs: update README

PATTERN='^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\(.+\))?: .{1,100}'

# Valid commit types
VALID_TYPES=(
    "feat     - A new feature"
    "fix      - A bug fix"
    "docs     - Documentation only changes"
    "style    - Code style changes (formatting, missing semi colons, etc)"
    "refactor - Code change that neither fixes a bug nor adds a feature"
    "perf     - Performance improvements"
    "test     - Adding missing tests or correcting existing tests"
    "build    - Changes that affect the build system or dependencies"
    "ci       - Changes to CI configuration files and scripts"
    "chore    - Other changes that don't modify src or test files"
    "revert   - Reverts a previous commit"
)

# Check if commit message matches pattern
if echo "$COMMIT_MSG" | grep -qE "$PATTERN"; then
    print_success "Commit message follows conventional commits format"
    exit 0
else
    print_header "⛔ INVALID COMMIT MESSAGE"

    cat << 'EOF'

Your commit message doesn't follow the Conventional Commits format.

📋 CONVENTIONAL COMMITS FORMAT:

<type>(<optional scope>): <subject>

<optional body>

<optional footer>

📝 VALID TYPES:

EOF

    for type_desc in "${VALID_TYPES[@]}"; do
        echo "  • $type_desc"
    done

    cat << 'EOF'

✅ GOOD EXAMPLES:

feat(auth): add JWT authentication
fix(api): resolve timeout in user endpoint
docs: update installation guide
style(ui): format button components
refactor(db): optimize query performance
perf(api): add caching to reduce latency
test(auth): add unit tests for login
build(deps): upgrade React to v18
ci(github): add automated testing workflow
chore(deps): update dependencies

With scope and body:
feat(auth): add OAuth2 support

Implement OAuth2 authentication flow with support
for Google and GitHub providers.

Closes #123

With breaking change:
feat(api)!: change authentication endpoint

BREAKING CHANGE: The /auth endpoint now requires
OAuth2 tokens instead of API keys.

❌ BAD EXAMPLES:

Updated stuff
Fixed bug
WIP
asdf
Updated README file
Added new feature for users
Fixed the thing that was broken

📏 RULES:

• Use lowercase for type
• Scope is optional but recommended
• Subject must be present
• Subject should be lowercase
• No period at the end of subject
• Subject max length: 100 characters
• Use imperative mood ("add" not "added" or "adds")
• Body and footer are optional
• Separate body with blank line
• Use footer for breaking changes and issue references

🔗 MORE INFO:

https://www.conventionalcommits.org/

EOF

    print_info "Your commit message was:"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "$COMMIT_MSG"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    if ask_yes_no "Edit commit message?"; then
        # Open editor for user to fix message
        ${EDITOR:-vi} "$COMMIT_MSG_FILE"

        # Re-check the edited message
        NEW_COMMIT_MSG=$(cat "$COMMIT_MSG_FILE")

        if echo "$NEW_COMMIT_MSG" | grep -qE "$PATTERN"; then
            print_success "Commit message updated successfully!"
            exit 0
        else
            print_error "Commit message still invalid"
            exit 1
        fi
    else
        print_error "Commit aborted due to invalid message"
        exit 1
    fi
fi
