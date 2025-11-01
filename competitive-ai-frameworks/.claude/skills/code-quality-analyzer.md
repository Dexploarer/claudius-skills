# Code Quality Championship Analyzer

## Skill Activation

This skill automatically activates when the user mentions:
- "improve code quality"
- "code quality analysis"
- "refactor code"
- "optimize codebase"
- "technical debt"
- "code health"

## Skill Description

Orchestrates a competitive code quality championship where three specialized AI teams compete to improve code across performance, maintainability, and best practices using reinforcement learning.

## Teams

**Team 1: Performance Optimizers**
- Focus: Runtime, memory, bundle size
- Best at: Algorithm optimization, memory leaks, bundle reduction

**Team 2: Maintainability Engineers**  
- Focus: Complexity, tests, documentation
- Best at: Refactoring, test coverage, reducing complexity

**Team 3: Best Practices Auditors**
- Focus: Style, security, accessibility
- Best at: Linting, security fixes, WCAG compliance

## Execution

When activated:

1. **Analyze Current State**
   - Measure baseline metrics
   - Identify improvement opportunities
   - Categorize by team specialty

2. **Run Championship** (default 3 rounds)
   - Teams apply improvements
   - Measure impact
   - Update strategies via RL

3. **Present Results**
   - Winner announcement
   - Key improvements
   - Combined recommendations

## Usage

```bash
/run-quality-check --target ./src --rounds 3
```

Or mention: "I need to improve code quality"

## Output

```
🥇 WINNER: Team 2 - Maintainability Engineers
   Total Score: 245 points
   - Reduced complexity by 35%
   - Test coverage: 45% → 92%
   - Documentation: 30% → 85%
```
