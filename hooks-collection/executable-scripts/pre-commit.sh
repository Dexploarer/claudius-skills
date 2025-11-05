#!/usr/bin/env bash
# Combined pre-commit hook
# Runs all pre-commit checks in sequence

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HOOKS_DIR="$SCRIPT_DIR/pre-commit"

# Source common utilities
source "$SCRIPT_DIR/helpers/common.sh"

echo ""
print_header "🔍 Pre-Commit Checks"

# Configuration - can be overridden by environment variables
RUN_SECRET_SCANNER=${RUN_SECRET_SCANNER:-true}
RUN_ENV_PROTECTION=${RUN_ENV_PROTECTION:-true}
RUN_LINTING=${RUN_LINTING:-true}
RUN_DEPENDENCY_SCAN=${RUN_DEPENDENCY_SCAN:-false}  # Disabled by default (can be slow)

# Track overall status
OVERALL_STATUS=0

# Run secret scanner
if [[ "$RUN_SECRET_SCANNER" == "true" ]]; then
    if [[ -x "$HOOKS_DIR/secret-scanner.sh" ]]; then
        "$HOOKS_DIR/secret-scanner.sh" || OVERALL_STATUS=1
    else
        print_warning "Secret scanner not found or not executable"
    fi
fi

# Run env file protection
if [[ "$RUN_ENV_PROTECTION" == "true" ]]; then
    if [[ -x "$HOOKS_DIR/env-protection.sh" ]]; then
        "$HOOKS_DIR/env-protection.sh" || OVERALL_STATUS=1
    else
        print_warning "Env protection not found or not executable"
    fi
fi

# Run linting
if [[ "$RUN_LINTING" == "true" ]]; then
    if [[ -x "$HOOKS_DIR/linting-enforcement.sh" ]]; then
        "$HOOKS_DIR/linting-enforcement.sh" || OVERALL_STATUS=1
    else
        print_warning "Linting enforcement not found or not executable"
    fi
fi

# Run dependency scanner (optional, can be slow)
if [[ "$RUN_DEPENDENCY_SCAN" == "true" ]]; then
    if [[ -x "$HOOKS_DIR/dependency-scanner.sh" ]]; then
        "$HOOKS_DIR/dependency-scanner.sh" || OVERALL_STATUS=1
    else
        print_warning "Dependency scanner not found or not executable"
    fi
fi

echo ""

if [[ $OVERALL_STATUS -eq 0 ]]; then
    print_header "✅ All Pre-Commit Checks Passed!"
    exit 0
else
    print_header "⛔ Some Pre-Commit Checks Failed"
    echo ""
    print_info "To skip these hooks, use: git commit --no-verify"
    print_warning "(Not recommended - you may be introducing issues)"
    echo ""
    exit 1
fi
