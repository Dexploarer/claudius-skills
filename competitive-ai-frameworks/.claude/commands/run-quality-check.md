Run competitive code quality championship with three specialized AI teams competing to improve performance, maintainability, and best practices.

## Instructions

1. **Analyze Baseline**
   - Measure current code quality metrics
   - Identify improvement opportunities
   - Establish before metrics for comparison

2. **Parse Arguments**
   - `$1` or `--target`: Target directory path (default: current directory)
   - `$2` or `--rounds`: Number of rounds (default: 3)
   - `--output`: Output directory for results (default: ./quality-results)
   - `--focus`: Specific area (performance/maintainability/practices)

3. **Execute Championship**
   ```bash
   cd competitive-ai-frameworks/frameworks/code-quality
   python coordinator.py \
     --target $TARGET \
     --rounds $ROUNDS \
     --output $OUTPUT \
     ${FOCUS:+--focus $FOCUS}
   ```

4. **Display Progress**
   - Show each round with improvements applied
   - Display metrics changing over rounds
   - Show current team scores

5. **Present Results**
   - Winner announcement
   - Before/after metrics comparison
   - Key improvements made
   - Combined recommendations

## Example Usage

```bash
# Basic usage (current directory, 3 rounds)
/run-quality-check

# Specify target
/run-quality-check ./src

# Focus on performance
/run-quality-check --target ./api --focus performance

# More rounds for better optimization
/run-quality-check --rounds 5
```

## What This Does

1. Measures baseline code quality metrics (coverage, complexity, performance, etc.)
2. Initializes three competing AI teams (Performance, Maintainability, Best Practices)
3. Runs championship for specified number of rounds
4. Teams apply improvements in their specialty areas
5. Applies reinforcement learning to optimize strategies
6. Scores based on improvement magnitude and impact
7. Presents comprehensive before/after comparison

## Options

- **No arguments:** Uses current directory, 3 rounds, all teams
- **--target <path>:** Specific codebase to improve
- **--rounds <n>:** Number of improvement rounds
- **--focus <area>:** Emphasize performance/maintainability/practices
- **--output <path>:** Custom output directory

## Output Format

```markdown
🎯 Code Quality Championship Results

🥇 Winner: Team 2 - Maintainability Engineers (245 pts)

Improvements:
- Test Coverage: 45% → 92% (+47%)
- Complexity: 12.5 → 5.8 (-54%)
- Documentation: 30% → 85% (+55%)

🥈 Team 1 - Performance (210 pts)
- Bundle Size: 2.5MB → 1.8MB (-28%)
- Memory Usage: -15%
- Runtime: -22%

🥉 Team 3 - Best Practices (185 pts)
- Security Issues: 8 → 0
- WCAG Issues: 23 → 3
- Linting Errors: 156 → 0

Recommended Approach: Focus on tests and docs (Team 2),
then optimize performance (Team 1), then enforce practices (Team 3).

Results: ./quality-results/championship_*.json
```

## Notes

- **Git recommended:** Run on clean branch to review changes
- **Teams make edits:** Review all changes before committing
- **Metrics:** Coverage, complexity, documentation, performance, security, accessibility
- **Best rounds:** 3-5 rounds optimal for quality improvement
- **High impact:** Test coverage and complexity reduction usually win
- **Follow-up:** Review changes, run tests, commit approved improvements
