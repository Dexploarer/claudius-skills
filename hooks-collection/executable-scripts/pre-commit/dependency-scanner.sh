#!/usr/bin/env bash
# Pre-commit hook: Dependency Vulnerability Scanner
# Scans for vulnerable dependencies when package files change

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../helpers/common.sh"

print_header "🔍 Dependency Vulnerability Scanner"

# Check if package files changed
check_package_files_changed() {
    local package_files=(
        "package.json"
        "package-lock.json"
        "yarn.lock"
        "pnpm-lock.yaml"
        "requirements.txt"
        "Pipfile"
        "Pipfile.lock"
        "Cargo.toml"
        "Cargo.lock"
        "go.mod"
        "go.sum"
        "composer.json"
        "composer.lock"
        "Gemfile"
        "Gemfile.lock"
    )

    local changed=0

    while IFS= read -r file; do
        for pkg_file in "${package_files[@]}"; do
            if [[ "$file" == *"$pkg_file" ]]; then
                changed=1
                break 2
            fi
        done
    done < <(get_staged_files)

    return $((1 - changed))
}

# Scan npm/yarn dependencies
scan_npm() {
    if [[ ! -f "package.json" ]]; then
        return 0
    fi

    print_info "Scanning npm dependencies..."

    if command_exists npm; then
        if npm audit --audit-level=moderate 2>&1; then
            print_success "No npm vulnerabilities found"
            return 0
        else
            print_error "npm audit found vulnerabilities"
            echo ""
            echo "To fix automatically, run:"
            echo "  npm audit fix"
            echo ""
            echo "For breaking changes:"
            echo "  npm audit fix --force"
            echo ""
            return 1
        fi
    elif command_exists yarn; then
        if yarn audit --level moderate 2>&1; then
            print_success "No yarn vulnerabilities found"
            return 0
        else
            print_error "yarn audit found vulnerabilities"
            echo ""
            echo "To fix, run:"
            echo "  yarn audit"
            echo ""
            return 1
        fi
    else
        print_warning "npm/yarn not found - skipping npm scan"
        return 0
    fi
}

# Scan Python dependencies
scan_python() {
    if [[ ! -f "requirements.txt" ]] && [[ ! -f "Pipfile" ]]; then
        return 0
    fi

    print_info "Scanning Python dependencies..."

    if command_exists pip-audit; then
        if pip-audit 2>&1; then
            print_success "No Python vulnerabilities found"
            return 0
        else
            print_error "pip-audit found vulnerabilities"
            echo ""
            echo "Install pip-audit with:"
            echo "  pip install pip-audit"
            echo ""
            return 1
        fi
    elif command_exists safety; then
        if safety check 2>&1; then
            print_success "No Python vulnerabilities found"
            return 0
        else
            print_error "safety found vulnerabilities"
            echo ""
            echo "Install safety with:"
            echo "  pip install safety"
            echo ""
            return 1
        fi
    else
        print_warning "pip-audit/safety not found - skipping Python scan"
        print_info "Install with: pip install pip-audit"
        return 0
    fi
}

# Scan Go dependencies
scan_go() {
    if [[ ! -f "go.mod" ]]; then
        return 0
    fi

    print_info "Scanning Go dependencies..."

    if command_exists nancy; then
        if go list -json -m all | nancy sleuth 2>&1; then
            print_success "No Go vulnerabilities found"
            return 0
        else
            print_error "nancy found vulnerabilities"
            echo ""
            echo "Install nancy with:"
            echo "  go install github.com/sonatype-nexus-community/nancy@latest"
            echo ""
            return 1
        fi
    elif command_exists govulncheck; then
        if govulncheck ./... 2>&1; then
            print_success "No Go vulnerabilities found"
            return 0
        else
            print_error "govulncheck found vulnerabilities"
            return 1
        fi
    else
        print_warning "nancy/govulncheck not found - skipping Go scan"
        print_info "Install with: go install golang.org/x/vuln/cmd/govulncheck@latest"
        return 0
    fi
}

# Scan Rust dependencies
scan_rust() {
    if [[ ! -f "Cargo.toml" ]]; then
        return 0
    fi

    print_info "Scanning Rust dependencies..."

    if command_exists cargo-audit; then
        if cargo audit 2>&1; then
            print_success "No Rust vulnerabilities found"
            return 0
        else
            print_error "cargo-audit found vulnerabilities"
            echo ""
            echo "Install cargo-audit with:"
            echo "  cargo install cargo-audit"
            echo ""
            return 1
        fi
    else
        print_warning "cargo-audit not found - skipping Rust scan"
        print_info "Install with: cargo install cargo-audit"
        return 0
    fi
}

# Scan PHP dependencies
scan_php() {
    if [[ ! -f "composer.json" ]]; then
        return 0
    fi

    print_info "Scanning PHP dependencies..."

    if command_exists composer; then
        if composer audit 2>&1; then
            print_success "No PHP vulnerabilities found"
            return 0
        else
            print_error "composer audit found vulnerabilities"
            return 1
        fi
    else
        print_warning "composer not found - skipping PHP scan"
        return 0
    fi
}

# Scan Ruby dependencies
scan_ruby() {
    if [[ ! -f "Gemfile" ]]; then
        return 0
    fi

    print_info "Scanning Ruby dependencies..."

    if command_exists bundle; then
        if bundle audit check 2>&1; then
            print_success "No Ruby vulnerabilities found"
            return 0
        else
            print_error "bundler-audit found vulnerabilities"
            echo ""
            echo "To update database:"
            echo "  bundle audit update"
            echo ""
            return 1
        fi
    else
        print_warning "bundler not found - skipping Ruby scan"
        return 0
    fi
}

# Main scanning logic
main() {
    # Check if package files changed
    if ! check_package_files_changed; then
        print_info "No package files changed - skipping dependency scan"
        return 0
    fi

    print_info "Package files changed - scanning for vulnerabilities..."
    echo ""

    local scan_errors=0

    # Run all scanners
    scan_npm || ((scan_errors++))
    scan_python || ((scan_errors++))
    scan_go || ((scan_errors++))
    scan_rust || ((scan_errors++))
    scan_php || ((scan_errors++))
    scan_ruby || ((scan_errors++))

    echo ""

    if [[ $scan_errors -gt 0 ]]; then
        print_header "⚠️ VULNERABILITIES DETECTED"

        cat << 'EOF'

Vulnerable dependencies were found in your project.

⚠️  RISKS:
• Security exploits
• Data breaches
• Compliance violations
• Supply chain attacks

✅ RECOMMENDED ACTIONS:

1. Review vulnerability details above
2. Update affected packages
3. Run fix commands provided
4. Re-run dependency scan
5. Test thoroughly after updates

🔧 GENERAL FIX COMMANDS:

JavaScript/Node:
  npm audit fix
  npm audit fix --force  (for breaking changes)

Python:
  pip install --upgrade <package>
  pip-audit --fix

Go:
  go get -u <package>
  go mod tidy

Rust:
  cargo update

PHP:
  composer update

Ruby:
  bundle update <gem>

EOF

        if ask_yes_no "Proceed with commit despite vulnerabilities?"; then
            print_warning "Proceeding with commit..."
            print_warning "Please address vulnerabilities ASAP!"
            return 0
        else
            print_error "Commit aborted. Please fix vulnerabilities first."
            exit 1
        fi
    else
        print_success "No vulnerabilities detected!"
    fi
}

main "$@"
