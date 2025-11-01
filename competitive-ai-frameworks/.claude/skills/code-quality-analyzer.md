---
name: code-quality-analyzer
description: Orchestrate competitive code quality improvement where three specialized AI teams compete to enhance performance, maintainability, and best practices. Activates when user wants to improve code quality, refactor code, optimize codebase, reduce technical debt, or analyze code health.
allowed-tools: [Read, Grep, Glob, Bash, Task, Edit]
---

# Code Quality Championship Analyzer

Orchestrates a competitive multi-agent simulation where three specialized AI teams compete to improve your code quality across performance, maintainability, and best practices using reinforcement learning.

## When to Use

This skill should be used when:
- User wants to improve overall code quality
- User mentions refactoring or optimization
- User needs to reduce technical debt
- User requests code health analysis
- User wants comprehensive code improvement across multiple dimensions
- User mentions performance, maintainability, or best practices improvements

## Instructions

### Step 1: Analyze Current State

Before starting the championship, establish baseline metrics:

1. **Performance Metrics:**
   - Runtime complexity
   - Memory usage
   - Bundle size
   - Load time

2. **Maintainability Metrics:**
   - Cyclomatic complexity
   - Test coverage percentage
   - Documentation coverage
   - Code duplication

3. **Best Practices Metrics:**
   - Linting errors/warnings
   - Security vulnerabilities
   - Accessibility issues (WCAG)
   - Style consistency

Example:
```bash
Baseline Analysis:
- Test Coverage: 45%
- Complexity: High (avg 12.5)
- Bundle Size: 2.5 MB
- Security Issues: 8
- WCAG Issues: 23
```

### Step 2: Configure Championship

Ask user for:
- **Target path:** Directory to analyze (default: current directory)
- **Rounds:** Number of improvement rounds (default: 3)
- **Focus areas:** Specific quality aspects to prioritize (optional)
- **Output:** Where to save results (default: ./quality-results)

### Step 3: Run Competition Rounds

For each round (typically 3 rounds):

1. **Team 1 (Performance)** applies optimizations:
   - Algorithm improvements
   - Memory leak fixes
   - Bundle size reductions
   - Lazy loading implementations

2. **Team 2 (Maintainability)** enhances code:
   - Complexity reduction via refactoring
   - Test coverage improvements
   - Documentation additions
   - Code duplication removal

3. **Team 3 (Best Practices)** enforces standards:
   - Linting fixes
   - Security vulnerability patches
   - Accessibility improvements
   - Style consistency

4. **Measure improvements** and score based on:
   - Magnitude of improvement
   - Impact on codebase
   - Quality of changes
   - No regressions introduced

5. **Update strategies** via reinforcement learning

### Step 4: Present Results

Generate report showing:
- 🥇 Winner and scores
- 📊 Before/after metrics comparison
- 🎯 Key improvements made
- 💡 Combined recommendations
- 📝 Suggested next steps

Example command:
```bash
cd competitive-ai-frameworks/frameworks/code-quality
python coordinator.py \
  --target /path/to/codebase \
  --rounds 3 \
  --output ./quality-results
```

## Best Practices

- ✅ Run on a clean git branch so changes can be reviewed/reverted
- ✅ Start with baseline analysis to measure actual improvements
- ✅ Use 3-5 rounds for optimal balance of improvement and time
- ✅ Review all changes before committing (teams make actual code edits)
- ✅ Focus on high-impact improvements first (complexity, test coverage)
- ✅ Re-run after accepting changes to verify improvements persist
- ✅ Save metrics over time to track code health trends
- ✅ Combine insights from all three teams for holistic improvement

## Examples

### Example 1: Comprehensive Code Quality Improvement

**User Input:**
```
I need to improve the code quality of my project
```

**Skill Process:**
1. Analyze current state: 45% test coverage, high complexity, 2.5MB bundle
2. Run 3 rounds of competitive improvement
3. Teams apply improvements in their specialty areas
4. Measure and compare results

**Output:**
```markdown
🎯 Code Quality Championship Results

🥇 Winner: Team 2 - Maintainability Engineers (245 points)

Improvements:
- Test Coverage: 45% → 92% (+47% improvement)
- Cyclomatic Complexity: 12.5 → 5.8 (-54% improvement)
- Documentation: 30% → 85% (+55% improvement)

🥈 Team 1 - Performance Optimizers (210 points)
- Bundle Size: 2.5MB → 1.8MB (-28% improvement)
- Memory Usage: -15% improvement
- Runtime: -22% improvement

🥉 Team 3 - Best Practices (185 points)
- Security Issues: 8 → 0 (100% fixed)
- WCAG Issues: 23 → 3 (-87% improvement)
- Linting Errors: 156 → 0 (100% fixed)

Recommended Approach: Focus on test coverage and documentation
first (Team 2), then optimize performance (Team 1), finally
enforce best practices (Team 3).
```

**Explanation:** All teams improved different aspects, but Maintainability team made the highest impact by dramatically increasing test coverage and reducing complexity.

### Example 2: Performance-Focused Improvement

**User Input:**
```
Optimize my application's performance
```

**Skill Process:**
1. User indicates performance focus
2. Increase Team 1 (Performance) weight
3. Run 3 rounds focused on performance metrics
4. Present performance-specific results

**Output:**
Results emphasizing runtime optimizations, memory improvements, and bundle size reductions.

## Common Mistakes to Avoid

- ❌ Running on uncommitted changes (hard to review what changed)
- ❌ Accepting all changes blindly (always review team improvements)
- ❌ Using only 1 round (prevents RL from improving strategies)
- ❌ Ignoring test failures introduced by refactoring
- ❌ Focusing only on one quality dimension (miss holistic improvement)
- ❌ Not measuring baseline first (can't quantify improvements)
- ✅ Use git, review changes, run multiple rounds, verify tests pass, measure holistically

## Tips

- 💡 **First time:** Start with small codebase to understand the process
- 💡 **Best results:** 3-5 rounds optimal for quality improvement
- 💡 **High impact:** Team 2 (Maintainability) often wins with test coverage improvements
- 💡 **Performance issues:** Increase Team 1 weight if performance is critical
- 💡 **Legacy code:** Expect Team 2 to excel at complexity reduction
- 💡 **Review carefully:** Teams make actual code changes - always review before committing
- 💡 **Trend tracking:** Run monthly to track code health over time

## Related Skills/Commands

- `/run-quality-check` - Quick start quality championship
- `/run-bug-hunt` - Security-focused championship
- `performance-optimizer` subagent - Performance specialist
- `code-reviewer` skill - General code review

## Notes

**Scoring System:**
Teams earn points based on:
- Improvement magnitude (% change in metrics)
- Impact scope (how much code affected)
- Quality of implementation (no regressions)
- Passing all tests after changes

**Team Specialties:**
- **Team 1 (Performance):** Algorithms, memory, bundle size, runtime optimization
- **Team 2 (Maintainability):** Complexity reduction, tests, documentation, refactoring
- **Team 3 (Best Practices):** Linting, security, accessibility, style enforcement

**Reinforcement Learning:**
Teams learn which types of improvements yield highest scores in your codebase. Later rounds focus more on high-impact changes.

**Safety:**
All changes are made on disk, so use git to review and control what gets committed. The framework does not automatically commit changes.

**Integration:**
Uses subagents in `.claude/subagents/team[1-3]-*.md` and Python framework in `frameworks/code-quality/`.
