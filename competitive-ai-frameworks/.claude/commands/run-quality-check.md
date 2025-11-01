---
description: Run competitive code quality championship with 3 AI teams
---

You are running the Code Quality Championship command.

## Command Purpose

Execute a competitive code quality championship where three specialized AI teams compete to improve code across performance, maintainability, and best practices.

## Arguments

- `--target <path>` - Path to codebase (required)
- `--rounds <n>` - Number of rounds (default: 3)
- `--output <path>` - Output directory (default: ./results)
- `--team <name>` - Run only specific team (optional: performance/maintainability/practices)
- `--focus <category>` - Focus on category (optional: performance/maintainability/practices)

## Execution

1. **Validate Target**
   Confirm target path exists and is accessible

2. **Measure Baseline**
   ```
   Analyzing baseline code quality...
   - Performance metrics
   - Complexity analysis
   - Test coverage
   - Linting errors
   - Security issues
   ```

3. **Run Championship**
   ```bash
   python frameworks/code-quality/coordinator.py \
     --target [path] \
     --rounds [n]
   ```

4. **Display Results**
   ```
   🥇 WINNER: Team 2 - Maintainability Engineers
      Score: 245 points
      
   KEY IMPROVEMENTS:
   - Complexity: 18 → 4 (-78%)
   - Test Coverage: 45% → 92% (+47 pts)
   - Documentation: 30% → 85% (+55 pts)
   
   RECOMMENDATIONS:
   1. Apply performance optimizations (Team 1)
   2. Maintain high test coverage (Team 2)
   3. Enforce linting rules (Team 3)
   ```

## Example Usage

```bash
# Full championship
/run-quality-check --target ./src --rounds 5

# Focus on performance
/run-quality-check --target ./src --team performance

# Quick check
/run-quality-check --target ./src --rounds 1
```

## Success Criteria

- All rounds complete
- Improvements measured
- Winner determined
- Recommendations provided
