#!/usr/bin/env bash
# Combined pre-push hook
# Runs all pre-push checks

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HOOKS_DIR="$SCRIPT_DIR/pre-push"

# Source common utilities
source "$SCRIPT_DIR/helpers/common.sh"

echo ""
print_header "🚀 Pre-Push Checks"

# Run force push prevention
if [[ -x "$HOOKS_DIR/prevent-force-push.sh" ]]; then
    "$HOOKS_DIR/prevent-force-push.sh" "$@"
else
    print_warning "Force push prevention not found or not executable"
fi

print_header "✅ All Pre-Push Checks Passed!"
exit 0
