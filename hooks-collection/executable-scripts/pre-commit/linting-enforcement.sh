#!/usr/bin/env bash
# Pre-commit hook: Linting Enforcement
# Runs linters on staged files and blocks commits with errors

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../helpers/common.sh"

print_header "✅ Linting Enforcement"

# Track errors
LINT_ERRORS=0

# Run ESLint for JavaScript/TypeScript files
run_eslint() {
    local files=()

    # Get staged JS/TS files
    while IFS= read -r file; do
        if [[ -n "$file" ]] && [[ -f "$file" ]]; then
            files+=("$file")
        fi
    done < <(get_staged_files | grep -E '\.(js|jsx|ts|tsx|mjs|cjs)$')

    if [[ ${#files[@]} -eq 0 ]]; then
        return 0
    fi

    if ! command_exists eslint; then
        print_warning "ESLint not found - skipping JavaScript/TypeScript linting"
        return 0
    fi

    print_info "Running ESLint on ${#files[@]} file(s)..."

    if eslint "${files[@]}" --max-warnings=0; then
        print_success "ESLint passed"
        return 0
    else
        print_error "ESLint found issues"
        echo ""
        echo "To fix automatically, run:"
        echo "  eslint --fix ${files[*]}"
        echo ""
        return 1
    fi
}

# Run Prettier for formatting
run_prettier() {
    local files=()

    # Get staged files that Prettier can handle
    while IFS= read -r file; do
        if [[ -n "$file" ]] && [[ -f "$file" ]]; then
            files+=("$file")
        fi
    done < <(get_staged_files | grep -E '\.(js|jsx|ts|tsx|css|scss|json|md|yaml|yml|html)$')

    if [[ ${#files[@]} -eq 0 ]]; then
        return 0
    fi

    if ! command_exists prettier; then
        print_warning "Prettier not found - skipping format checking"
        return 0
    fi

    print_info "Running Prettier on ${#files[@]} file(s)..."

    if prettier --check "${files[@]}"; then
        print_success "Prettier passed"
        return 0
    else
        print_error "Prettier found formatting issues"
        echo ""
        echo "To fix automatically, run:"
        echo "  prettier --write ${files[*]}"
        echo ""
        return 1
    fi
}

# Run Python linters (flake8, black, mypy)
run_python_linters() {
    local files=()

    # Get staged Python files
    while IFS= read -r file; do
        if [[ -n "$file" ]] && [[ -f "$file" ]]; then
            files+=("$file")
        fi
    done < <(get_staged_files | grep -E '\.py$')

    if [[ ${#files[@]} -eq 0 ]]; then
        return 0
    fi

    print_info "Running Python linters on ${#files[@]} file(s)..."

    local python_errors=0

    # Run flake8
    if command_exists flake8; then
        if flake8 "${files[@]}"; then
            print_success "flake8 passed"
        else
            print_error "flake8 found issues"
            python_errors=1
        fi
    fi

    # Run black
    if command_exists black; then
        if black --check "${files[@]}"; then
            print_success "black passed"
        else
            print_error "black found formatting issues"
            echo "  To fix: black ${files[*]}"
            python_errors=1
        fi
    fi

    # Run mypy
    if command_exists mypy; then
        if mypy "${files[@]}"; then
            print_success "mypy passed"
        else
            print_error "mypy found type errors"
            python_errors=1
        fi
    fi

    return $python_errors
}

# Run Go linters
run_go_linters() {
    local files=()

    # Get staged Go files
    while IFS= read -r file; do
        if [[ -n "$file" ]] && [[ -f "$file" ]]; then
            files+=("$file")
        fi
    done < <(get_staged_files | grep -E '\.go$')

    if [[ ${#files[@]} -eq 0 ]]; then
        return 0
    fi

    print_info "Running Go linters on ${#files[@]} file(s)..."

    local go_errors=0

    # Run gofmt
    if command_exists gofmt; then
        local unformatted=$(gofmt -l "${files[@]}")
        if [[ -z "$unformatted" ]]; then
            print_success "gofmt passed"
        else
            print_error "gofmt found unformatted files:"
            echo "$unformatted"
            echo "  To fix: gofmt -w ${files[*]}"
            go_errors=1
        fi
    fi

    # Run go vet
    if command_exists go; then
        if go vet "${files[@]}" 2>&1; then
            print_success "go vet passed"
        else
            print_error "go vet found issues"
            go_errors=1
        fi
    fi

    # Run golangci-lint if available
    if command_exists golangci-lint; then
        if golangci-lint run "${files[@]}"; then
            print_success "golangci-lint passed"
        else
            print_error "golangci-lint found issues"
            go_errors=1
        fi
    fi

    return $go_errors
}

# Run Rust linters
run_rust_linters() {
    local files=()

    # Get staged Rust files
    while IFS= read -r file; do
        if [[ -n "$file" ]] && [[ -f "$file" ]]; then
            files+=("$file")
        fi
    done < <(get_staged_files | grep -E '\.rs$')

    if [[ ${#files[@]} -eq 0 ]]; then
        return 0
    fi

    print_info "Running Rust linters on ${#files[@]} file(s)..."

    local rust_errors=0

    # Run rustfmt
    if command_exists rustfmt; then
        if rustfmt --check "${files[@]}" 2>/dev/null; then
            print_success "rustfmt passed"
        else
            print_error "rustfmt found formatting issues"
            echo "  To fix: rustfmt ${files[*]}"
            rust_errors=1
        fi
    fi

    # Run clippy
    if command_exists cargo; then
        if cargo clippy -- -D warnings; then
            print_success "clippy passed"
        else
            print_error "clippy found issues"
            rust_errors=1
        fi
    fi

    return $rust_errors
}

# Main linting logic
main() {
    print_info "Scanning staged files for linting..."

    # Run language-specific linters
    run_eslint || ((LINT_ERRORS++))
    run_prettier || ((LINT_ERRORS++))
    run_python_linters || ((LINT_ERRORS++))
    run_go_linters || ((LINT_ERRORS++))
    run_rust_linters || ((LINT_ERRORS++))

    echo ""

    if [[ $LINT_ERRORS -gt 0 ]]; then
        print_header "⛔ COMMIT BLOCKED - LINTING ERRORS"

        cat << 'EOF'

Please fix the linting errors before committing.

Common fixes:
• Run auto-fixers:
  - ESLint:   eslint --fix <files>
  - Prettier: prettier --write <files>
  - Black:    black <files>
  - gofmt:    gofmt -w <files>
  - rustfmt:  rustfmt <files>

• Install missing linters
• Configure linter rules in project config
• Add exceptions in linter config if needed

To bypass this check (NOT recommended):
  git commit --no-verify

EOF

        if ask_yes_no "Skip linting and commit anyway?"; then
            print_warning "Proceeding with commit despite linting errors..."
            return 0
        else
            print_error "Commit aborted. Please fix linting errors."
            exit 1
        fi
    else
        print_success "All linting checks passed!"
    fi
}

main "$@"
