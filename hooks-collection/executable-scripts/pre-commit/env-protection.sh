#!/usr/bin/env bash
# Pre-commit hook: .env File Protection
# Prevents committing .env and credential files

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../helpers/common.sh"

print_header "🔒 Environment File Protection"

# Patterns for files that should never be committed
PROTECTED_PATTERNS=(
    '\.env$'
    '\.env\.local$'
    '\.env\.development$'
    '\.env\.production$'
    '\.env\.test$'
    '\.env\.staging$'
    'credentials\.json$'
    'secrets\.json$'
    'service-account.*\.json$'
    '\.aws/credentials$'
    '\.ssh/id_rsa$'
    '\.ssh/id_ed25519$'
    'private.*\.key$'
    'private.*\.pem$'
    '\.p12$'
    '\.pfx$'
    'keystore\.jks$'
)

# Exceptions (files that are OK to commit)
ALLOWED_PATTERNS=(
    '\.env\.example$'
    '\.env\.template$'
    '\.env\.sample$'
    'example\.env$'
    'template\.env$'
)

# Check if file is allowed
is_allowed_file() {
    local file="$1"

    for pattern in "${ALLOWED_PATTERNS[@]}"; do
        if [[ "$file" =~ $pattern ]]; then
            return 0
        fi
    done
    return 1
}

# Check if file is protected
is_protected_file() {
    local file="$1"

    # Check if it's an allowed exception first
    if is_allowed_file "$file"; then
        return 1
    fi

    # Check against protected patterns
    for pattern in "${PROTECTED_PATTERNS[@]}"; do
        if [[ "$file" =~ $pattern ]]; then
            return 0
        fi
    done
    return 1
}

# Main checking logic
main() {
    local protected_files=()

    print_info "Checking for protected files..."

    # Get all staged files
    while IFS= read -r file; do
        if [[ -n "$file" ]] && is_protected_file "$file"; then
            protected_files+=("$file")
        fi
    done < <(get_staged_files)

    if [[ ${#protected_files[@]} -gt 0 ]]; then
        echo ""
        print_header "⛔ PROTECTED FILES DETECTED"

        echo -e "${RED}${BOLD}The following files should NOT be committed:${NC}\n"

        for file in "${protected_files[@]}"; do
            echo -e "  ${RED}✗${NC} $file"
        done

        cat << 'EOF'


⚠️  WHY THIS IS DANGEROUS:

These files typically contain:
• API keys and secrets
• Database credentials
• Private keys
• Access tokens
• Personal information

🔐 SECURITY RISKS:

• Secrets exposed in git history
• Unauthorized access to services
• Data breaches
• Compliance violations
• Costly security incidents

✅ WHAT TO DO INSTEAD:

1. Remove from staging:
   git restore --staged <file>

2. Add to .gitignore:
   echo ".env" >> .gitignore
   echo "credentials.json" >> .gitignore

3. Use environment variables:
   # In your code
   const apiKey = process.env.API_KEY

4. Create template files:
   cp .env .env.example
   # Then edit .env.example to remove real values

5. Use secrets management:
   • AWS Secrets Manager
   • HashiCorp Vault
   • Azure Key Vault
   • Google Secret Manager
   • Doppler
   • 1Password CLI

📝 EXAMPLE .env.example:

# API Keys
API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/db

# Feature Flags
FEATURE_X_ENABLED=true

EOF

        # Check if .gitignore exists and has these patterns
        if [[ -f ".gitignore" ]]; then
            local missing_patterns=()

            for file in "${protected_files[@]}"; do
                if ! grep -q "$(basename "$file")" ".gitignore" 2>/dev/null; then
                    missing_patterns+=("$(basename "$file")")
                fi
            done

            if [[ ${#missing_patterns[@]} -gt 0 ]]; then
                echo -e "${YELLOW}⚠️  These patterns are NOT in .gitignore:${NC}\n"
                for pattern in "${missing_patterns[@]}"; do
                    echo -e "  $pattern"
                done
                echo ""
            fi
        fi

        if ask_yes_no "Do you really want to commit these files? (NOT recommended)"; then
            print_warning "Proceeding with commit..."
            print_warning "Remember to rotate any exposed credentials!"
            return 0
        else
            print_error "Commit aborted. Please remove protected files from staging."
            exit 1
        fi
    else
        print_success "No protected files detected"
    fi
}

main "$@"
