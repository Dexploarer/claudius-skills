# Contributing to Claudius Skills

Thank you for your interest in contributing to Claudius Skills! This document provides guidelines and instructions for contributing.

## 🤝 How to Contribute

There are many ways to contribute to Claudius Skills:

1. **Report Bugs** - Help us identify issues
2. **Suggest Features** - Share ideas for new skills, commands, or improvements
3. **Improve Documentation** - Help make our docs clearer and more comprehensive
4. **Submit Code** - Contribute new skills, commands, hooks, or agents
5. **Share Examples** - Show others how you're using Claudius Skills

## 🐛 Reporting Bugs

Use our [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.yml) and include:

- Which kit you're using
- Component type (skill, command, hook, agent)
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment details

## ✨ Suggesting Features

Use our [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.yml) and include:

- Feature type (skill, command, hook, agent, etc.)
- Target skill level
- Problem statement
- Proposed solution
- Use cases
- Whether you'd like to implement it

## 📝 Submitting Changes

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/claudius-skills.git
cd claudius-skills
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 3. Follow Existing Patterns

When contributing, follow the established patterns:

#### Skills
- Use the template: `templates/skill-template.md`
- Place in appropriate kit directory: `[kit]/.claude/skills/`
- Include clear activation phrases
- Add comprehensive instructions
- Document expected behavior

#### Slash Commands
- Use the template: `templates/command-template.md`
- Place in: `[kit]/.claude/commands/`
- Use kebab-case naming
- Include usage examples
- Document parameters

#### Hooks
- Use the template: `templates/hook-template.sh`
- Place in: `hooks-collection/[category]/`
- Include clear hook type (user-prompt-submit, bash-call, etc.)
- Test thoroughly before submitting
- Document triggering conditions

#### Subagents
- Use the template: `templates/subagent-template.md`
- Place in appropriate kit: `[kit]/.claude/subagents/`
- Define clear expertise area
- Include workflow instructions
- Document when to use

### 4. Test Your Changes

- Test with Claude Code CLI
- Verify skills activate correctly
- Test slash commands execute properly
- Ensure hooks trigger as expected
- Check for any errors or warnings

### 5. Update Documentation

- Update relevant documentation files
- Add examples if applicable
- Update CHANGELOG.md with your changes
- Add to relevant catalog files in `docs/reference/`

### 6. Commit Guidelines

Use conventional commit messages:

```
feat: add database query optimizer skill
fix: correct hook trigger in prevent-force-push
docs: improve quick start guide clarity
refactor: reorganize intermediate kit structure
test: add test cases for new skill
```

**Commit message format:**
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation changes
- `style` - Formatting changes (no code change)
- `refactor` - Code refactoring
- `test` - Adding or updating tests
- `chore` - Maintenance tasks

### 7. Submit Pull Request

- Push your branch to your fork
- Create a Pull Request using our [PR template](.github/PULL_REQUEST_TEMPLATE.md)
- Fill out all sections of the template
- Link any related issues
- Wait for review

## 📋 Code Standards

### General Principles

1. **Consistency** - Follow existing patterns and styles
2. **Clarity** - Code should be self-documenting
3. **Simplicity** - Prefer simple solutions over complex ones
4. **Documentation** - Document complex logic and decisions
5. **Testing** - Test thoroughly before submitting

### TypeScript/JavaScript

- Use TypeScript strict mode
- Prefer classes over interfaces for data structures
- Include explicit return types
- No `any` types
- Follow ESLint rules in templates

### Python

- Follow PEP 8
- Use type hints
- Document functions and classes
- Write descriptive variable names

### Markdown

- Use proper heading hierarchy
- Include code blocks with language tags
- Keep line length reasonable (80-120 chars)
- Use tables for structured data
- Include links to related resources

### Shell Scripts (Hooks)

- Include shebang (`#!/bin/bash`)
- Add error handling
- Use descriptive variable names
- Comment complex logic
- Test on multiple platforms if possible

## 🎯 Contribution Areas

We especially welcome contributions in these areas:

### High Priority
- 🐛 Bug fixes
- 📚 Documentation improvements
- ✅ Test coverage
- 🎨 Example projects

### Feature Additions
- 🛠️ New framework integrations
- 🔌 New skills for emerging technologies
- 🎪 New hooks for common workflows
- 🤖 Specialized subagents

### Nice to Have
- 🌍 Internationalization
- 🎨 Visual improvements
- 📊 Analytics and metrics
- 🔍 Search and discovery improvements

## 🏗️ Project Structure

Understanding the project structure will help you contribute effectively:

```
claudius-skills/
├── .github/                      # GitHub configuration
│   ├── ISSUE_TEMPLATE/          # Issue templates
│   ├── DISCUSSION_TEMPLATE/     # Discussion templates
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/                         # Consolidated documentation
│   ├── getting-started/         # Quick start guides
│   ├── guides/                  # Comprehensive guides
│   ├── reference/               # Reference catalogs
│   └── architecture/            # Design decisions
├── starter-kit/                  # Level 1: Beginner kit
├── intermediate-kit/             # Level 2: Production kit
├── advanced-kit/                 # Level 4: Enterprise kit
├── productivity-skills/          # Productivity workflows
├── competitive-ai-frameworks/    # AI competitions
├── eliza-os-kit/                # ElizaOS integration
├── examples/                     # Multi-level examples
├── framework-rules/             # Framework-specific rules
├── hooks-collection/            # Production hooks
├── modern-commands/             # Modern workflow commands
├── specialized-agents/          # Specialized consultants
├── templates/                   # Component templates
└── resources/                   # Additional resources
```

## 📦 Kit Organization

Each kit follows this structure:

```
kit-name/
└── .claude/
    ├── skills/         # Skill definitions
    ├── commands/       # Slash commands
    ├── subagents/      # AI consultants
    ├── hooks/          # Event automation
    └── rules/          # Configuration rules
        ├── CLAUDE.md   # Kit overview
        └── frameworks/ # Framework-specific rules
```

## ✅ Review Process

1. **Initial Review** - Maintainers check if contribution meets basic requirements
2. **Technical Review** - Code/content quality, adherence to standards
3. **Testing** - Verification that changes work as expected
4. **Documentation Review** - Ensure documentation is updated
5. **Approval** - Final approval and merge

## 🎓 Learning Resources

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code/)
- [Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)
- [Hooks Reference](https://docs.claude.com/en/docs/claude-code/hooks)
- [Model Context Protocol](https://modelcontextprotocol.io/)

## 💬 Getting Help

- 💡 [GitHub Discussions](https://github.com/Dexploarer/claudius-skills/discussions) - Ask questions
- 🐛 [Issues](https://github.com/Dexploarer/claudius-skills/issues) - Report bugs or request features
- 📚 [Documentation](docs/) - Comprehensive guides

## 📜 License

By contributing to Claudius Skills, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors will be recognized in:
- Repository contributors list
- CHANGELOG.md for specific features
- Community showcase (for significant contributions)

---

**Thank you for contributing to Claudius Skills!** 🎉

Your contributions help make Claude Code more powerful and accessible for everyone.
