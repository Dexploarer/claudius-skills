#!/bin/bash

# Competitive AI Frameworks Setup Script

set -e

echo "╔══════════════════════════════════════════════════════╗"
echo "║  Competitive AI Frameworks - Setup                 ║"
echo "╚══════════════════════════════════════════════════════╝"
echo ""

# Check Python version
echo "Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not found"
    echo "   Please install Python 3.8 or higher"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✓ Found Python $PYTHON_VERSION"

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is required but not found"
    exit 1
fi
echo "✓ Found pip3"

# Create virtual environment (optional but recommended)
echo ""
echo "Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"

# Install requirements (if requirements.txt exists)
if [ -f "requirements.txt" ]; then
    echo ""
    echo "Installing Python dependencies..."
    pip install -r requirements.txt
    echo "✓ Dependencies installed"
else
    echo ""
    echo "⚠️  No requirements.txt found - basic setup only"
fi

# Make Python scripts executable
echo ""
echo "Making scripts executable..."
chmod +x frameworks/bug-hunting/coordinator.py 2>/dev/null || true
chmod +x frameworks/code-quality/coordinator.py 2>/dev/null || true
chmod +x frameworks/user-flows/coordinator.py 2>/dev/null || true
echo "✓ Scripts are executable"

# Create results directory
echo ""
echo "Creating results directory..."
mkdir -p results
echo "✓ Results directory created"

# Verify structure
echo ""
echo "Verifying framework structure..."

REQUIRED_DIRS=(
    ".claude/skills"
    ".claude/commands"
    ".claude/subagents"
    "frameworks/bug-hunting"
    "frameworks/code-quality"
    "frameworks/user-flows"
    "docs"
    "examples"
)

ALL_OK=true
for dir in "${REQUIRED_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        echo "  ✓ $dir"
    else
        echo "  ❌ $dir (missing)"
        ALL_OK=false
    fi
done

if [ "$ALL_OK" = true ]; then
    echo ""
    echo "╔══════════════════════════════════════════════════════╗"
    echo "║  ✓ Setup Complete!                                 ║"
    echo "╚══════════════════════════════════════════════════════╝"
    echo ""
    echo "Quick Start:"
    echo ""
    echo "  1. Run bug hunting championship:"
    echo "     python frameworks/bug-hunting/coordinator.py --target ./src --rounds 5"
    echo ""
    echo "  2. Or use with Claude Code (copy .claude/ to your project):"
    echo "     cp -r .claude /path/to/your/project/"
    echo "     Then use: /run-bug-hunt --target ./src"
    echo ""
    echo "  3. Read the quick start guide:"
    echo "     cat docs/QUICKSTART.md"
    echo ""
    echo "Happy hunting! 🎯"
else
    echo ""
    echo "⚠️  Some directories are missing. Framework may not work correctly."
    echo "   Please check your installation."
fi
