#!/usr/bin/env bash
# Pre-commit hook: Secret Scanner
# Scans for accidentally committed secrets and API keys

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../helpers/common.sh"

print_header "🔐 Secret Scanner"

# Secret patterns to detect
declare -A SECRET_PATTERNS=(
    ["AWS_ACCESS_KEY"]='(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}'
    ["AWS_SECRET_KEY"]='aws(.{0,20})?['\''"][0-9a-zA-Z\/+]{40}['\''"]'
    ["GITHUB_TOKEN"]='gh[pousr]_[A-Za-z0-9]{36,251}'
    ["GENERIC_API_KEY"]='api[_-]?key['\''"\s]*[:=]['\''"\s]*[A-Za-z0-9_\-]{20,}'
    ["GENERIC_SECRET"]='secret['\''"\s]*[:=]['\''"\s]*[A-Za-z0-9_\-]{20,}'
    ["PASSWORD"]='password['\''"\s]*[:=]['\''"\s]*[A-Za-z0-9_\-@!#$%^&*]{8,}'
    ["PRIVATE_KEY"]='-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----'
    ["JWT_TOKEN"]='eyJ[A-Za-z0-9_-]*\.eyJ[A-Za-z0-9_-]*\.[A-Za-z0-9_-]*'
    ["STRIPE_KEY"]='(sk|pk)_(test|live)_[0-9a-zA-Z]{24,}'
    ["GOOGLE_API_KEY"]='AIza[0-9A-Za-z\-_]{35}'
    ["SLACK_TOKEN"]='xox[baprs]-[0-9]{10,13}-[0-9]{10,13}-[A-Za-z0-9]{24,}'
    ["SLACK_WEBHOOK"]='https://hooks\.slack\.com/services/T[a-zA-Z0-9_]{8,}/B[a-zA-Z0-9_]{8,}/[a-zA-Z0-9_]{24,}'
    ["HEROKU_API_KEY"]='[h|H][e|E][r|R][o|O][k|K][u|U].*[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}'
    ["MAILGUN_API_KEY"]='key-[0-9a-zA-Z]{32}'
    ["TWILIO_API_KEY"]='SK[0-9a-fA-F]{32}'
    ["CONNECTION_STRING"]='(mongodb|mysql|postgresql|postgres):\/\/[^\s]+'
)

# Files to always exclude
EXCLUDED_FILES=(
    "package-lock.json"
    "yarn.lock"
    "pnpm-lock.yaml"
    "go.sum"
    "Cargo.lock"
    ".min.js"
    ".min.css"
)

# Check if file should be excluded
should_exclude_file() {
    local file="$1"

    for excluded in "${EXCLUDED_FILES[@]}"; do
        if [[ "$file" == *"$excluded"* ]]; then
            return 0
        fi
    done
    return 1
}

# Scan file for secrets
scan_file() {
    local file="$1"
    local found_secrets=0

    # Skip if file doesn't exist (deleted files)
    if [[ ! -f "$file" ]]; then
        return 0
    fi

    # Skip excluded files
    if should_exclude_file "$file"; then
        return 0
    fi

    # Scan for each pattern
    for secret_type in "${!SECRET_PATTERNS[@]}"; do
        local pattern="${SECRET_PATTERNS[$secret_type]}"

        # Use grep to find matches
        if grep -qE "$pattern" "$file" 2>/dev/null; then
            if [[ $found_secrets -eq 0 ]]; then
                echo -e "\n${RED}${BOLD}⛔ SECRETS DETECTED!${NC}"
                echo -e "${RED}File: $file${NC}\n"
            fi

            # Get line numbers and show context
            while IFS= read -r line; do
                local line_num=$(echo "$line" | cut -d: -f1)
                local content=$(echo "$line" | cut -d: -f2-)

                # Redact the secret (show first few chars)
                local redacted=$(echo "$content" | sed -E "s/($pattern)/\1.../g" | head -c 100)

                echo -e "${YELLOW}Line $line_num:${NC} Type: ${BOLD}$secret_type${NC}"
                echo -e "  ${redacted}..."
                echo ""

                found_secrets=1
            done < <(grep -nE "$pattern" "$file" 2>/dev/null)
        fi
    done

    return $found_secrets
}

# Main scanning logic
main() {
    local total_issues=0
    local files_scanned=0

    print_info "Scanning staged files for secrets..."

    # Get all staged files
    while IFS= read -r file; do
        if [[ -n "$file" ]]; then
            ((files_scanned++))

            if ! scan_file "$file"; then
                ((total_issues++))
            fi
        fi
    done < <(get_staged_files)

    echo ""
    print_info "Scanned $files_scanned file(s)"

    if [[ $total_issues -gt 0 ]]; then
        echo ""
        print_header "🚨 COMMIT BLOCKED - SECRETS DETECTED"

        cat << 'EOF'

This appears to contain real secrets!

Immediate actions required:
1. Remove secrets from code
2. Add to environment variables instead
3. Rotate the exposed credentials
4. Add pattern to .gitignore if needed

Secret management best practices:
• Use environment variables (.env files)
• Use secrets management tools (AWS Secrets Manager, HashiCorp Vault)
• Never hardcode credentials
• Use .env.example for documentation
• Add .env to .gitignore

If already committed to history:
1. Use git filter-branch or BFG Repo-Cleaner
2. Force push to rewrite history
3. Rotate ALL exposed credentials immediately
4. Audit access logs

EOF

        if ask_yes_no "Is this a false positive?"; then
            print_warning "Proceeding with commit..."
            return 0
        else
            print_error "Commit aborted. Please remove secrets and try again."
            exit 1
        fi
    else
        print_success "No secrets detected"
    fi
}

main "$@"
