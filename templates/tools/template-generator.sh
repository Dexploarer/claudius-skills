#!/bin/bash

# Claude Code Interactive Template Generator
# This script helps you generate Claude Code configurations interactively

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Template directories
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATES_DIR="$(dirname "$SCRIPT_DIR")"
TARGET_DIR="${TARGET_DIR:-.claude}"

# Helper functions
print_header() {
    echo -e "${PURPLE}╔══════════════════════════════════════════════════════════╗${NC}"
    echo -e "${PURPLE}║   Claude Code Interactive Template Generator            ║${NC}"
    echo -e "${PURPLE}╚══════════════════════════════════════════════════════════╝${NC}"
    echo
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Prompt for user input
prompt() {
    local message="$1"
    local default="$2"
    local input

    if [ -n "$default" ]; then
        echo -ne "${CYAN}?${NC} $message ${YELLOW}($default)${NC}: "
    else
        echo -ne "${CYAN}?${NC} $message: "
    fi

    read input
    echo "${input:-$default}"
}

# Select from menu
select_option() {
    local prompt="$1"
    shift
    local options=("$@")
    local PS3="${CYAN}?${NC} $prompt: "

    select opt in "${options[@]}" "Cancel"; do
        if [ "$opt" = "Cancel" ]; then
            echo "cancelled"
            return 1
        elif [ -n "$opt" ]; then
            echo "$opt"
            return 0
        fi
    done
}

# Main menu
show_main_menu() {
    echo -e "${CYAN}What would you like to create?${NC}"
    echo
    echo "  1) Skill"
    echo "  2) Command"
    echo "  3) Subagent"
    echo "  4) Hook"
    echo "  5) MCP Configuration"
    echo "  6) Complete Setup"
    echo "  7) Language-Specific Service"
    echo "  8) GitHub Workflow"
    echo "  9) Exit"
    echo
}

# Generate skill
generate_skill() {
    echo
    echo -e "${BLUE}═══ Creating New Skill ═══${NC}"
    echo

    # Select skill level
    echo -e "${CYAN}Select skill level:${NC}"
    local level=$(select_option "Skill level" "Beginner (simple, focused)" "Intermediate (framework-specific)" "Advanced (full-stack)")

    if [ "$level" = "cancelled" ]; then
        return
    fi

    # Get skill name
    local skill_name=$(prompt "Skill name (kebab-case)")
    local skill_file="${TARGET_DIR}/skills/${skill_name}.md"

    # Get description
    local description=$(prompt "Description (when should this activate?)")

    # Get allowed tools
    echo -e "${CYAN}Select tools (comma-separated):${NC}"
    echo "  Common: Read, Write, Edit, Grep, Glob, Bash, Task"
    local tools=$(prompt "Allowed tools" "Read, Edit")

    # Copy template
    case "$level" in
        "Beginner"*)
            local template="$TEMPLATES_DIR/skills/beginner-skill-template.md"
            ;;
        "Intermediate"*)
            local template="$TEMPLATES_DIR/skills/intermediate-skill-template.md"
            ;;
        "Advanced"*)
            local template="$TEMPLATES_DIR/skills/advanced-skill-template.md"
            ;;
    esac

    mkdir -p "$(dirname "$skill_file")"
    cp "$template" "$skill_file"

    # Replace placeholders
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        sed -i '' "s/name: .*/name: $skill_name/" "$skill_file"
        sed -i '' "s/description: .*/description: $description/" "$skill_file"
        sed -i '' "s/allowed-tools: .*/allowed-tools: [$tools]/" "$skill_file"
    else
        # Linux
        sed -i "s/name: .*/name: $skill_name/" "$skill_file"
        sed -i "s/description: .*/description: $description/" "$skill_file"
        sed -i "s/allowed-tools: .*/allowed-tools: [$tools]/" "$skill_file"
    fi

    print_success "Created skill: $skill_file"
    print_info "Next steps:"
    echo "  1. Edit $skill_file to customize the skill"
    echo "  2. Add your specific instructions and examples"
    echo "  3. Test with: claude"
}

# Generate command
generate_command() {
    echo
    echo -e "${BLUE}═══ Creating New Command ═══${NC}"
    echo

    # Select command type
    echo -e "${CYAN}Select command type:${NC}"
    local cmd_type=$(select_option "Command type" "Basic (simple operation)" "Workflow (multi-step process)")

    if [ "$cmd_type" = "cancelled" ]; then
        return
    fi

    # Get command name
    local cmd_name=$(prompt "Command name (without /)")
    local cmd_file="${TARGET_DIR}/commands/${cmd_name}.md"

    # Get description
    local description=$(prompt "Description")

    # Copy template
    case "$cmd_type" in
        "Basic"*)
            local template="$TEMPLATES_DIR/commands/basic-command-template.md"
            ;;
        "Workflow"*)
            local template="$TEMPLATES_DIR/commands/workflow-command-template.md"
            ;;
    esac

    mkdir -p "$(dirname "$cmd_file")"
    cp "$template" "$cmd_file"

    # Replace placeholders
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "s/name: .*/name: $cmd_name/" "$cmd_file"
        sed -i '' "s/description: .*/description: $description/" "$cmd_file"
    else
        sed -i "s/name: .*/name: $cmd_name/" "$cmd_file"
        sed -i "s/description: .*/description: $description/" "$cmd_file"
    fi

    print_success "Created command: $cmd_file"
    print_info "Next steps:"
    echo "  1. Edit $cmd_file to customize the command"
    echo "  2. Test with: /$cmd_name"
}

# Generate subagent
generate_subagent() {
    echo
    echo -e "${BLUE}═══ Creating New Subagent ═══${NC}"
    echo

    # Select subagent type
    echo -e "${CYAN}Select subagent type:${NC}"
    local agent_type=$(select_option "Subagent type" \
        "Analyzer (read-only, review/audit)" \
        "Generator (create files/code)" \
        "Domain Expert (specialized knowledge)")

    if [ "$agent_type" = "cancelled" ]; then
        return
    fi

    # Get agent name
    local agent_name=$(prompt "Subagent name (kebab-case)")
    local agent_file="${TARGET_DIR}/agents/${agent_name}.md"

    # Get description
    local description=$(prompt "Description")

    # Copy template
    case "$agent_type" in
        "Analyzer"*)
            local template="$TEMPLATES_DIR/subagents/analyzer-subagent-template.md"
            ;;
        "Generator"*)
            local template="$TEMPLATES_DIR/subagents/generator-subagent-template.md"
            ;;
        "Domain Expert"*)
            local template="$TEMPLATES_DIR/subagents/domain-expert-template.md"
            ;;
    esac

    mkdir -p "$(dirname "$agent_file")"
    cp "$template" "$agent_file"

    # Replace placeholders
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "s/name: .*/name: $agent_name/" "$agent_file"
        sed -i '' "s/description: .*/description: $description/" "$agent_file"
    else
        sed -i "s/name: .*/name: $agent_name/" "$agent_file"
        sed -i "s/description: .*/description: $description/" "$agent_file"
    fi

    print_success "Created subagent: $agent_file"
    print_info "Next steps:"
    echo "  1. Edit $agent_file to customize the subagent"
    echo "  2. Test with: 'use the $agent_name subagent to...'"
}

# Generate language-specific service
generate_language_service() {
    echo
    echo -e "${BLUE}═══ Creating Language-Specific Service ═══${NC}"
    echo

    # Select language
    echo -e "${CYAN}Select language:${NC}"
    local language=$(select_option "Language" "Go" "Rust" "PHP")

    if [ "$language" = "cancelled" ]; then
        return
    fi

    # Get service name
    local service_name=$(prompt "Service name")

    # Get resource
    local resource=$(prompt "Resource to manage (e.g., users, products)" "users")

    print_info "Generating ${language} service for ${service_name}..."

    case "$language" in
        "Go")
            print_info "Use: 'Generate a Go service for managing ${resource}'"
            print_info "Template: templates/languages/go/go-service-generator.md"
            ;;
        "Rust")
            print_info "Use: 'Generate a Rust service for managing ${resource}'"
            print_info "Template: templates/languages/rust/rust-service-generator.md"
            ;;
        "PHP")
            print_info "Use: 'Generate a PHP Laravel service for managing ${resource}'"
            print_info "Template: templates/languages/php/php-service-generator.md"
            ;;
    esac

    print_warning "Note: Language services are generated via Claude Code skills, not copied as files"
    print_info "Start Claude Code and use the phrase above to generate the service"
}

# Generate GitHub workflow
generate_github_workflow() {
    echo
    echo -e "${BLUE}═══ Creating GitHub Workflow ═══${NC}"
    echo

    # Select workflow type
    echo -e "${CYAN}Select workflow type:${NC}"
    echo "  1) Node.js CI/CD"
    echo "  2) Python CI/CD"
    echo "  3) Go CI/CD"
    echo "  4) Rust CI/CD"
    echo "  5) PHP CI/CD"
    echo "  6) Docker Build & Push"
    echo "  7) Deploy to AWS ECS"
    echo "  8) Deploy to Vercel"
    echo "  9) Semantic Release"
    echo " 10) CodeQL Security Scan"
    echo

    local workflow_choice=$(prompt "Workflow number" "1")

    print_info "Generating GitHub workflow..."
    print_warning "Note: GitHub workflows are generated via Claude Code skills"
    print_info "Start Claude Code and use: 'Generate a GitHub Actions workflow for [your choice]'"
}

# Main loop
main() {
    print_header

    while true; do
        show_main_menu
        choice=$(prompt "Select option" "1")

        case $choice in
            1)
                generate_skill
                ;;
            2)
                generate_command
                ;;
            3)
                generate_subagent
                ;;
            4)
                print_info "Hook templates available in: $TEMPLATES_DIR/hooks/"
                print_info "Copy and customize the JSON hooks to your .claude/hooks/ or settings.json"
                ;;
            5)
                print_info "MCP templates available in: $TEMPLATES_DIR/mcp/"
                print_info "Copy a template to .mcp.json and customize with your server configs"
                ;;
            6)
                print_info "Complete setups available in: $TEMPLATES_DIR/complete-setups/"
                print_info "See README for frontend, backend, and fullstack configurations"
                ;;
            7)
                generate_language_service
                ;;
            8)
                generate_github_workflow
                ;;
            9)
                echo
                print_success "Thanks for using Claude Code Template Generator!"
                exit 0
                ;;
            *)
                print_error "Invalid option"
                ;;
        esac

        echo
        echo -e "${YELLOW}────────────────────────────────────────────${NC}"
        echo
    done
}

# Run main function
main
