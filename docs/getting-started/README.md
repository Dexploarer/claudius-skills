# Quick Start Guide - Claudius Skills

> Get up and running with Claude Code extensibility in under 10 minutes

---

## 🚀 Choose Your Path

### Path 1: Complete Beginner (Start Here!)

**Install Starter Kit** - Basic automation and learning

```bash
# Copy starter kit to your project
cp -r claudius-skills/starter-kit/.claude /path/to/your/project/

# You now have:
# ✓ 5 essential skills (README generation, code explanation, etc.)
# ✓ 12 basic commands (/explain, /test, /commit, etc.)
# ✓ 4 helpful agents (code reviewer, test writer, etc.)
```

**First Tasks:**
1. Try `/explain` on a complex file
2. Use the README generator skill by saying "create a README"
3. Run `/test` to generate tests for your code

---

### Path 2: Production Project

**Install Intermediate Kit** - Framework-specific + production hooks

```bash
# Copy intermediate kit
cp -r claudius-skills/intermediate-kit/.claude /path/to/your/project/

# Add essential safety hooks
cp claudius-skills/hooks-collection/development-safety/*.json /path/to/your/project/.claude/hooks/
cp claudius-skills/hooks-collection/security-enforcement/secret-scanning.json /path/to/your/project/.claude/hooks/

# You now have:
# ✓ 10 framework skills (React, Vue, Django, etc.)
# ✓ 15 production commands
# ✓ 6 specialist agents
# ✓ Critical safety hooks
```

---

### Path 3: Enterprise/Advanced

**Install Advanced Kit** - Full enterprise suite

```bash
# Copy advanced kit
cp -r claudius-skills/advanced-kit/.claude /path/to/your/project/

# Add all hooks
cp -r claudius-skills/hooks-collection/* /path/to/your/project/.claude/hooks/

# Add emerging tech skills
cp -r claudius-skills/examples/advanced/emerging-tech-skills/*/.claude/skills/* \
   /path/to/your/project/.claude/skills/

# You now have:
# ✓ 15 enterprise skills
# ✓ 20 advanced commands
# ✓ 10 specialist consultants
# ✓ 30 production hooks
# ✓ 10 emerging tech skills
```

---

## 📦 Installing Specific Features

### Just the Hooks (Safety First)

```bash
# Install all critical safety hooks
cp claudius-skills/hooks-collection/development-safety/*.json .claude/hooks/
cp claudius-skills/hooks-collection/security-enforcement/*.json .claude/hooks/
```

**You'll get protection from:**
- Committing secrets (.env files, API keys)
- Force pushing to main/master
- Destructive operations (rm -rf, DROP TABLE)
- Security vulnerabilities
- Large files without Git LFS

### Just One Skill

```bash
# Example: Install AI/ML Ops skill
cp claudius-skills/examples/advanced/emerging-tech-skills/ai-ml-ops/.claude/skills/ai-ml-ops.md \
   .claude/skills/
```

### Framework-Specific Rules

```bash
# Example: Add SvelteKit rules
cp claudius-skills/framework-rules/svelte/sveltekit-rules.md .claude/rules/
```

---

## ⚡ Quick Wins (5-Minute Setup)

### 1. Prevent Secrets in Git (1 minute)

```bash
mkdir -p .claude/hooks
cp claudius-skills/hooks-collection/security-enforcement/secret-scanning.json .claude/hooks/
cp claudius-skills/hooks-collection/development-safety/env-file-protection.json .claude/hooks/
```

**Result:** Never accidentally commit API keys or .env files again!

### 2. Automated Code Review (2 minutes)

```bash
mkdir -p .claude/agents
cp claudius-skills/starter-kit/.claude/agents/code-reviewer.md .claude/agents/
```

**Usage:** Just say "review my code" and get comprehensive feedback!

### 3. Smart Test Generation (2 minutes)

```bash
mkdir -p .claude/skills .claude/commands
cp claudius-skills/starter-kit/.claude/skills/test-helper.md .claude/skills/
cp claudius-skills/starter-kit/.claude/commands/test.md .claude/commands/
```

**Usage:** Say "generate tests for this file" or run `/test`

---

## 🎯 Common Scenarios

### Scenario: "I want to prevent accidents"

```bash
# Install all safety hooks
cp claudius-skills/hooks-collection/development-safety/*.json .claude/hooks/
```

Protects you from:
- Force pushes to main
- Committing large files
- Destructive rm -rf commands
- Installing typosquatted packages

### Scenario: "I'm learning a new framework"

```bash
# Example: Learning SvelteKit
cp claudius-skills/framework-rules/svelte/*.md .claude/rules/
```

**Result:** Claude knows SvelteKit best practices and helps you follow them!

### Scenario: "I want to standardize my team's practices"

```bash
# Install complete hooks collection
cp -r claudius-skills/hooks-collection/* .claude/hooks/

# Add golden path template skill
cp claudius-skills/examples/advanced/emerging-tech-skills/*/platform-architect.md .claude/agents/
```

**Result:** Automated enforcement of best practices + standardized project templates!

### Scenario: "I need ML/AI capabilities"

```bash
# Install AI/ML Ops skill
cp claudius-skills/examples/advanced/emerging-tech-skills/ai-ml-ops/.claude/skills/ai-ml-ops.md .claude/skills/

# Add ML Ops agent
cp claudius-skills/specialized-agents/ml-ops-engineer.md .claude/agents/

# Add ML commands
cp claudius-skills/modern-commands/ai-ml-workflows/*.md .claude/commands/
```

**Usage:** "Set up MLflow", "/train-model", "deploy my model to Kubernetes"

---

## 🔄 Updating and Customizing

### Enable/Disable Hooks

Edit any hook JSON file:
```json
{
  "enabled": false  // Set to true to enable
}
```

### Customize Thresholds

```json
// In test-coverage-enforcement.json
"Statements: >= 80%"  // Change to your threshold
```

### Add Your Own Content

Use the templates:
```bash
# Copy templates
cp claudius-skills/templates/skill-template.md .claude/skills/my-skill.md
cp claudius-skills/templates/command-template.md .claude/commands/my-command.md
```

---

## 📚 Next Steps

1. **Explore Examples:** Check `examples/` for real-world usage
2. **Read Documentation:** See `CLAUDE.md` for complete capabilities
3. **Join Community:** Share your own skills and hooks
4. **Customize:** Tailor everything to your workflow

---

## 🆘 Troubleshooting

### Skill Not Activating?

1. Check file location: `.claude/skills/skill-name.md`
2. Verify activation phrases match your request
3. Try being more explicit: "Use the X skill to..."

### Hook Not Triggering?

1. Verify `"enabled": true` in hook JSON
2. Check event type matches (user-prompt-submit vs post-tool-use)
3. Ensure hook is in `.claude/hooks/` directory

### Command Not Found?

1. Check file is in `.claude/commands/`
2. File should be named `command-name.md`
3. Try `/help` to see available commands

---

## 💡 Pro Tips

1. **Start Small:** Don't install everything at once
2. **Critical First:** Install safety/security hooks first
3. **Learn by Doing:** Try features hands-on
4. **Customize Gradually:** Adapt to your workflow over time
5. **Share:** Contribute your improvements back!

---

**Ready to Level Up?** See `BEST_PRACTICES.md` for advanced techniques!

**Last Updated:** 2025-11-02
