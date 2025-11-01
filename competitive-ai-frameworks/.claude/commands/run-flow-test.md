---
description: Run competitive user flow olympics with 3 AI teams
---

You are running the User Flow Olympics command.

## Command Purpose

Execute a competitive user flow olympics where three specialized AI teams compete to optimize user flows for completion, accessibility, and integration.

## Arguments

- `--flows <list>` - Flows to test (required): registration,login,checkout,profile,search
- `--rounds <n>` - Number of rounds (default: 4)
- `--output <path>` - Output directory (default: ./results)
- `--team <name>` - Run only specific team (optional: happy-path/edge-case/integration)
- `--target <path>` - Target application path (optional)

## Execution

1. **Select Flows**
   ```
   Testing flows:
   - User Registration
   - Checkout Process
   - Profile Management
   ```

2. **Measure Baseline**
   ```
   Baseline metrics:
   - Completion rates
   - Time to complete
   - Error rates
   - Friction points
   ```

3. **Run Olympics**
   ```bash
   python frameworks/user-flows/coordinator.py \
     --flows [list] \
     --rounds [n]
   ```

4. **Display Results**
   ```
   🥇 WINNER: Team 1 - Happy Path Optimizers
      Score: 189 points
      
   FLOW IMPROVEMENTS:
   
   Registration:
   - Completion: 68% → 92% (+24 pts)
   - Time: 3m 45s → 1m 30s (-60%)
   - Friction: 5 → 1 point
   
   Checkout:
   - Completion: 71% → 88% (+17 pts)
   - Time: 4m 30s → 2m 15s (-50%)
   - Abandonment: 29% → 12%
   
   RECOMMENDATIONS:
   1. Reduce form fields (Team 1)
   2. Add error recovery (Team 2)
   3. Improve API reliability (Team 3)
   ```

## Example Usage

```bash
# Test critical flows
/run-flow-test --flows registration,checkout

# All flows
/run-flow-test --flows registration,login,checkout,profile,search

# Focus on accessibility
/run-flow-test --flows registration --team edge-case
```

## Success Criteria

- All flows tested
- Improvements measured  
- Winner determined
- Recommendations provided
