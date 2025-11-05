#!/usr/bin/env bash
# Common utilities for git hooks

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color
BOLD='\033[1m'

# Print colored messages
print_error() {
    echo -e "${RED}${BOLD}⛔ ERROR:${NC} $1" >&2
}

print_warning() {
    echo -e "${YELLOW}${BOLD}⚠️  WARNING:${NC} $1"
}

print_success() {
    echo -e "${GREEN}${BOLD}✓${NC} $1"
}

print_info() {
    echo -e "${BLUE}${BOLD}ℹ${NC} $1"
}

print_header() {
    echo -e "\n${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BOLD}$1${NC}"
    echo -e "${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"
}

# Ask yes/no question
ask_yes_no() {
    local prompt="$1"
    local response

    while true; do
        echo -en "${YELLOW}${prompt} (y/n):${NC} "
        read -r response
        case "$response" in
            [Yy]* ) return 0;;
            [Nn]* ) return 1;;
            * ) echo "Please answer y or n.";;
        esac
    done
}

# Check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Get list of staged files
get_staged_files() {
    git diff --cached --name-only --diff-filter=ACM
}

# Get list of staged files with specific extension
get_staged_files_by_ext() {
    local extension="$1"
    get_staged_files | grep -E "\\.${extension}$"
}

# Check if we're in a git repository
check_git_repo() {
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        print_error "Not a git repository"
        exit 1
    fi
}

# Get current branch name
get_current_branch() {
    git symbolic-ref --short HEAD 2>/dev/null || git rev-parse --short HEAD 2>/dev/null
}

# Check if branch is protected
is_protected_branch() {
    local branch="$1"
    local protected_branches=("main" "master" "develop" "production" "staging")

    for protected in "${protected_branches[@]}"; do
        if [[ "$branch" == "$protected" ]]; then
            return 0
        fi
    done
    return 1
}

# Export functions
export -f print_error
export -f print_warning
export -f print_success
export -f print_info
export -f print_header
export -f ask_yes_no
export -f command_exists
export -f get_staged_files
export -f get_staged_files_by_ext
export -f check_git_repo
export -f get_current_branch
export -f is_protected_branch
