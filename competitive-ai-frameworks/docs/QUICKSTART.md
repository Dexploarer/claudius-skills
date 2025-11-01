# Quick Start Guide - Competitive AI Frameworks

Get up and running with competitive AI team simulations in 5 minutes!

## 🚀 Installation

### Option 1: Use in Your Project

```bash
# Copy the entire framework to your project
cp -r competitive-ai-frameworks/.claude /path/to/your/project/

# Or copy specific framework
cp -r competitive-ai-frameworks/frameworks/bug-hunting /path/to/your/project/
```

### Option 2: Standalone Use

```bash
cd competitive-ai-frameworks
chmod +x scripts/setup.sh
./scripts/setup.sh
```

## 🎯 First Run - Bug Hunting

### Using Slash Command (Recommended)

```bash
# From your project directory (after copying .claude/)
/run-bug-hunt --target ./src --rounds 3
```

### Using Python Directly

```bash
cd competitive-ai-frameworks/frameworks/bug-hunting
python coordinator.py --target /path/to/your/code --rounds 5
```

### Automatic Skill Activation

Just mention in conversation:
```
"I need to find security vulnerabilities in this codebase"
```

The bug-hunting-simulator skill will activate automatically!

## 📊 Understanding Your First Results

After the championship completes, you'll see:

```
╔══════════════════════════════════════════════════════╗
║   FINAL CHAMPIONSHIP RESULTS                        ║
╚══════════════════════════════════════════════════════╝

🥇 WINNER: Team 2 - Manual Reviewers
   Total Score: 1,450 points
   Bugs Found: 12 (2 Critical, 5 High, 5 Medium)
```

**What this means:**
- **Team 2 won** by finding critical business logic flaws
- **2 Critical bugs** need immediate attention
- **Total score 1,450** - combination of severity + quality + uniqueness

## 🎓 What Each Team Does

### Team 1: Automated Scanners
- **Fast** coverage of known patterns
- Best for: SQL injection, XSS, command injection
- **Start here** for quick wins

### Team 2: Manual Reviewers
- **Deep** analysis of complex logic
- Best for: Auth bypasses, IDOR, privilege escalation
- **Critical bugs** are their specialty

### Team 3: Fuzzers
- **Edge cases** and runtime bugs
- Best for: Race conditions, buffer overflows, DoS
- **Unique finds** others miss

## 🔧 Common Use Cases

### 1. Quick Security Scan (1 round, automated only)

```bash
/run-bug-hunt --target ./src --team automated --rounds 1
```

**Time:** ~2 minutes
**Use when:** Quick check before commit

### 2. Thorough Security Audit (10 rounds, all teams)

```bash
/run-bug-hunt --target ./src --rounds 10 --visualize
```

**Time:** ~30 minutes
**Use when:** Pre-release security audit

### 3. Focus on Critical Bugs (manual review only)

```bash
/run-bug-hunt --target ./src --team manual --rounds 3
```

**Time:** ~10 minutes
**Use when:** Looking for high-impact vulnerabilities

## 💡 Pro Tips

### Tip 1: Run Multiple Rounds

```bash
# Good: Strategies adapt and improve
/run-bug-hunt --target ./src --rounds 5

# Better: More learning, better results
/run-bug-hunt --target ./src --rounds 10
```

**Why:** Reinforcement learning needs data to adapt!

### Tip 2: Focus on Critical Paths

```bash
# Instead of entire codebase
/run-bug-hunt --target ./src

# Focus on auth/payment code
/run-bug-hunt --target ./src/auth
/run-bug-hunt --target ./src/payment
```

**Why:** Faster, more targeted results

### Tip 3: Combine with CI/CD

```yaml
# .github/workflows/security.yml
- name: Weekly Security Championship
  run: |
    /run-bug-hunt --target ./src --rounds 5 --output ./security-results
```

**Why:** Continuous security monitoring

## 🐛 Troubleshooting

### "Permission denied"

```bash
chmod +x competitive-ai-frameworks/frameworks/bug-hunting/coordinator.py
```

### "Python module not found"

```bash
# Install dependencies
pip install -r competitive-ai-frameworks/requirements.txt
```

### "No bugs found"

This could mean:
- ✅ Your code is secure! (Verify with external tools)
- ⚠️ Teams need more rounds to adapt
- ⚠️ Target path is wrong

Try:
```bash
# More rounds for better detection
/run-bug-hunt --target ./src --rounds 10

# Verify target path exists
ls -la ./src
```

## 📚 Next Steps

### 1. Try Code Quality Championship

```bash
/run-quality-check --target ./src --rounds 3
```

Improves:
- Performance (runtime, memory, bundle size)
- Maintainability (complexity, documentation)
- Best practices (style, tests, accessibility)

### 2. Try User Flow Testing

```bash
/run-flow-test --flows registration,login,checkout
```

Optimizes:
- Happy path completion rates
- Error handling
- Cross-flow integration

### 3. Customize for Your Needs

Edit team configurations:
```bash
vim .claude/subagents/team1-automated-scanner.md
```

Adjust scoring:
```bash
vim frameworks/bug-hunting/scoring_engine.py
```

## 🎯 Success Checklist

After your first run, you should have:

- [ ] Seen championship run complete
- [ ] Identified a winner team
- [ ] Received vulnerability reports (if any)
- [ ] Understood why the winner succeeded
- [ ] Got combined recommendations
- [ ] Results saved to JSON file

## 🆘 Getting Help

**Read the docs:**
```bash
cat competitive-ai-frameworks/README.md
cat competitive-ai-frameworks/docs/bug-hunting-guide.md
```

**Check examples:**
```bash
ls competitive-ai-frameworks/examples/
```

**View results:**
```bash
cat results/championship_*.json | jq
```

## 🎉 You're Ready!

You now know how to:
- ✅ Run bug hunting championships
- ✅ Interpret results
- ✅ Use different teams strategically
- ✅ Customize for your needs

**Start hunting bugs! 🐛🎯**

---

**Next:** Read [Bug Hunting Guide](bug-hunting-guide.md) for advanced techniques
