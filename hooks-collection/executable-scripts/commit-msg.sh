#!/usr/bin/env bash
# Combined commit-msg hook
# Validates commit message format

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HOOKS_DIR="$SCRIPT_DIR/commit-msg"

# Configuration
RUN_CONVENTIONAL_COMMITS=${RUN_CONVENTIONAL_COMMITS:-true}

# Run conventional commits checker
if [[ "$RUN_CONVENTIONAL_COMMITS" == "true" ]]; then
    if [[ -x "$HOOKS_DIR/conventional-commits.sh" ]]; then
        "$HOOKS_DIR/conventional-commits.sh" "$1"
    else
        # Source common utilities for error message
        source "$SCRIPT_DIR/helpers/common.sh"
        print_warning "Conventional commits checker not found or not executable"
    fi
fi

exit 0
