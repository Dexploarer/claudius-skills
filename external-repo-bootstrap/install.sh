#!/bin/bash

# Claudius Skills Bootstrap Installer
# https://github.com/Dexploarer/claudius-skills

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
REPO_URL="https://github.com/Dexploarer/claudius-skills.git"
REPO_PATH="$HOME/.claudius-skills"
BOOTSTRAP_URL="https://raw.githubusercontent.com/Dexploarer/claudius-skills/main/external-repo-bootstrap"

# Show usage
show_usage() {
    echo "Claudius Skills Bootstrap Installer"
    echo ""
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --merge    Merge with existing .claude directory (keep existing files)"
    echo "  --backup   Backup existing .claude and create fresh installation"
    echo "  --force    Same as --merge (skip interactive prompts)"
    echo "  -h, --help Show this help message"
    echo ""
    echo "Examples:"
    echo "  # Interactive installation"
    echo "  curl -fsSL https://raw.githubusercontent.com/Dexploarer/claudius-skills/main/external-repo-bootstrap/install.sh | bash -s -- --merge"
    echo ""
    echo "  # Download and run"
    echo "  curl -fsSL https://raw.githubusercontent.com/Dexploarer/claudius-skills/main/external-repo-bootstrap/install.sh -o install.sh"
    echo "  bash install.sh --merge"
}

# Parse command-line arguments
MODE=""
while [[ $# -gt 0 ]]; do
    case $1 in
        --merge)
            MODE="merge"
            shift
            ;;
        --backup)
            MODE="backup"
            shift
            ;;
        --force)
            MODE="force"
            shift
            ;;
        -h|--help)
            show_usage
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            echo ""
            show_usage
            exit 1
            ;;
    esac
done

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  Claudius Skills Bootstrap Installer${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check prerequisites
echo -e "${YELLOW}Checking prerequisites...${NC}"

# Check git
if ! command -v git &> /dev/null; then
    echo -e "${RED}✗ Git is not installed${NC}"
    echo "Please install git and try again"
    exit 1
fi
echo -e "${GREEN}✓ Git installed${NC}"

# Check if running in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo -e "${YELLOW}⚠ Not in a git repository${NC}"
    echo "This installer works best when run from a git repository."
    if [ -z "$MODE" ]; then
        read -p "Continue anyway? (y/n) " -n 1 -r < /dev/tty
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi
fi

echo ""
echo -e "${YELLOW}Step 1: Setting up repository access...${NC}"

# Save current directory
ORIGINAL_DIR=$(pwd)

# Clone or update the main repository
if [ -d "$REPO_PATH" ]; then
    echo -e "${BLUE}Repository already exists at $REPO_PATH${NC}"
    echo "Updating to latest version..."
    (cd "$REPO_PATH" && git fetch origin && git pull origin main) || {
        echo -e "${RED}✗ Failed to update repository${NC}"
        exit 1
    }
    echo -e "${GREEN}✓ Repository updated${NC}"
else
    echo "Cloning repository to $REPO_PATH..."
    git clone "$REPO_URL" "$REPO_PATH" || {
        echo -e "${RED}✗ Failed to clone repository${NC}"
        exit 1
    }
    echo -e "${GREEN}✓ Repository cloned${NC}"
fi

# Return to original directory
cd "$ORIGINAL_DIR"

echo ""
echo -e "${YELLOW}Step 2: Installing bootstrap to current directory...${NC}"

# Get current directory
CURRENT_DIR=$(pwd)
echo "Current directory: $CURRENT_DIR"

# Check if .claude already exists
if [ -d ".claude" ]; then
    echo -e "${YELLOW}⚠ .claude directory already exists${NC}"

    # Determine action based on MODE or interactive input
    if [ -n "$MODE" ]; then
        CHOICE="$MODE"
    else
        echo "Choose an option:"
        echo "  1) Merge (add new files, keep existing)"
        echo "  2) Backup and replace"
        echo "  3) Cancel"
        read -p "Enter choice (1-3): " -n 1 -r < /dev/tty
        echo

        case $REPLY in
            1) CHOICE="merge" ;;
            2) CHOICE="backup" ;;
            3) CHOICE="cancel" ;;
            *)
                echo -e "${RED}Invalid choice${NC}"
                exit 1
                ;;
        esac
    fi

    case $CHOICE in
        merge|force)
            echo -e "${BLUE}Merging with existing .claude directory...${NC}"
            # Create any missing subdirectories
            mkdir -p .claude/{skills,commands,subagents,rules}
            echo -e "${GREEN}✓ Will merge files${NC}"
            ;;
        backup)
            BACKUP_DIR=".claude.backup.$(date +%Y%m%d_%H%M%S)"
            mv .claude "$BACKUP_DIR"
            echo -e "${GREEN}✓ Backed up to $BACKUP_DIR${NC}"
            mkdir -p .claude/{skills,commands,subagents,rules}
            echo -e "${GREEN}✓ Created fresh .claude directory structure${NC}"
            ;;
        cancel)
            echo "Installation cancelled"
            exit 1
            ;;
        *)
            echo -e "${RED}Invalid mode: $CHOICE${NC}"
            exit 1
            ;;
    esac
else
    # Create .claude directory structure
    mkdir -p .claude/{skills,commands,subagents,rules}
    echo -e "${GREEN}✓ Created .claude directory structure${NC}"
fi

# Copy bootstrap files
echo "Copying bootstrap files..."

if ! cp "$REPO_PATH/external-repo-bootstrap/.claude/skills/claudius-installer.md" .claude/skills/ 2>/dev/null; then
    echo -e "${RED}✗ Failed to copy claudius-installer skill${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Copied claudius-installer skill${NC}"

if ! cp "$REPO_PATH/external-repo-bootstrap/.claude/subagents/claudius-setup-agent.md" .claude/subagents/ 2>/dev/null; then
    echo -e "${RED}✗ Failed to copy claudius-setup-agent${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Copied claudius-setup-agent${NC}"

if ! cp "$REPO_PATH/external-repo-bootstrap/.claude/commands/"*.md .claude/commands/ 2>/dev/null; then
    echo -e "${RED}✗ Failed to copy setup commands${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Copied setup commands${NC}"

echo ""
echo -e "${YELLOW}Step 3: Verifying installation...${NC}"

# Verify files
REQUIRED_FILES=(
    ".claude/skills/claudius-installer.md"
    ".claude/subagents/claudius-setup-agent.md"
    ".claude/commands/claudius-setup.md"
    ".claude/commands/claudius-update.md"
    ".claude/commands/claudius-info.md"
)

ALL_PRESENT=true
for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓ $file${NC}"
    else
        echo -e "${RED}✗ $file missing${NC}"
        ALL_PRESENT=false
    fi
done

if [ "$ALL_PRESENT" = false ]; then
    echo -e "${RED}Installation incomplete. Please check the errors above.${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}  Installation Complete! 🎉${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${BLUE}What's been installed:${NC}"
echo "  • Repository cloned to: $REPO_PATH"
echo "  • Bootstrap installed to: $CURRENT_DIR/.claude"
echo "  • Skills: 1 (claudius-installer)"
echo "  • Commands: 3 (/claudius-setup, /claudius-update, /claudius-info)"
echo "  • Agents: 1 (claudius-setup-agent)"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "  1. Start Claude Code:"
echo -e "     ${YELLOW}claude${NC}"
echo ""
echo "  2. Run the setup wizard:"
echo -e "     ${YELLOW}Say: \"setup claudius for my project\"${NC}"
echo -e "     ${YELLOW}Or: /claudius-setup${NC}"
echo ""
echo "  3. Try your new capabilities:"
echo -e "     ${YELLOW}Say: \"create a Button component\"${NC}"
echo -e "     ${YELLOW}Or: /test${NC}"
echo ""
echo -e "${BLUE}Documentation:${NC}"
echo "  • Bootstrap guide: $CURRENT_DIR/external-repo-bootstrap/README.md"
echo "  • Main repository: $REPO_PATH/README.md"
echo "  • Online: https://github.com/Dexploarer/claudius-skills"
echo ""
echo -e "${BLUE}Support:${NC}"
echo "  • Issues: https://github.com/Dexploarer/claudius-skills/issues"
echo "  • Discussions: https://github.com/Dexploarer/claudius-skills/discussions"
echo ""
echo -e "${GREEN}Happy coding! 🚀${NC}"
